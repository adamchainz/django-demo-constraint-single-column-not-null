from django.db import models


class ScoreType(models.IntegerChoices):
    POINTS = 1, "Points"
    DURATION = 2, "Duration"


class Score(models.Model):
    type = models.IntegerField(choices=ScoreType.choices)
    value_points = models.IntegerField(null=True)
    value_duration = models.DurationField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="score_value_matches_type",
                check=(
                    models.Q(
                        type=ScoreType.POINTS,
                        value_points__isnull=False,
                        value_duration__isnull=True,
                    )
                    | models.Q(
                        type=ScoreType.DURATION,
                        value_points__isnull=True,
                        value_duration__isnull=False,
                    )
                ),
            )
        ]
