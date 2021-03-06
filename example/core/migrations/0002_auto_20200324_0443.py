# Generated by Django 3.1 on 2020-03-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='score',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('type', 1), ('value_duration__isnull', True), ('value_points__isnull', False)), models.Q(('type', 2), ('value_duration__isnull', False), ('value_points__isnull', True)), _connector='OR'), name='score_value_matches_type'),
        ),
    ]
