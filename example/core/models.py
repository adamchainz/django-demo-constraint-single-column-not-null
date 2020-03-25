import functools
import operator

from django.db import models


class ScoreType(models.IntegerChoices):
    POINTS = 1, "Points"
    DURATION = 2, "Duration"


def check_value_field_matches(*, name, enum_type):
    q_objs = []
    all_field_names = [f"value_{type_.name.lower()}" for type_ in enum_type]
    for type_ in enum_type:
        type_field_name = f"value_{type_.name.lower()}"
        q_obj = models.Q(
            type=type_.value,
            **{
                f"{field_name}__isnull": (field_name != type_field_name)
                for field_name in all_field_names
            },
        )
        q_objs.append(q_obj)
    return models.CheckConstraint(
        check=functools.reduce(operator.or_, q_objs), name=name,
    )


class Score(models.Model):
    type = models.IntegerField(choices=ScoreType.choices)
    value_points = models.IntegerField(null=True)
    value_duration = models.DurationField(null=True)

    class Meta:
        constraints = [
            check_value_field_matches(
                name="score_value_matches_type", enum_type=ScoreType
            ),
        ]


class PointsScoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=ScoreType.POINTS)


class PointsScore(Score):
    objects = PointsScoreManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = ScoreType.POINTS

    class Meta:
        proxy = True


class DurationScoreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=ScoreType.DURATION)


class DurationScore(Score):
    objects = DurationScoreManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = ScoreType.DURATION

    class Meta:
        proxy = True
