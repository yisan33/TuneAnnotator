# Generated by Django 5.0.6 on 2024-09-24 17:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0017_music_instrumental_music_vocal"),
    ]

    operations = [
        migrations.CreateModel(
            name="MusicEmotion",
            fields=[
                (
                    "dimension_score_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("emotion", models.CharField(default="", max_length=30)),
                ("mark_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "music_id",
                    models.ForeignKey(
                        db_column="music_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.music",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.user",
                    ),
                ),
            ],
            options={
                "db_table": "MusicEmotion",
            },
        ),
    ]
