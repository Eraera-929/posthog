# Generated by Django 4.2.15 on 2024-10-15 13:04

from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import ValidateConstraint


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0493_insightvariable_values"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                # The only difference is lack of null=True
                migrations.AlterField(
                    model_name="team",
                    name="project",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        related_query_name="team",
                        to="posthog.project",
                    ),
                )
            ],
            database_operations=[
                # Finishing the job started in 0445_require_team_project_id_not_valid
                # This is safe in both Cloud regions, as project_id is not null for any posthog_team record
                ValidateConstraint(model_name="team", name="project_id_is_not_null")
            ],
        )
    ]
