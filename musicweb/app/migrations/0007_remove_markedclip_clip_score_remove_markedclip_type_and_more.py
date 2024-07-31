# Generated by Django 4.1.7 on 2023-04-23 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_rename_score_markedclip_clip_score"),
    ]

    operations = [
        migrations.RemoveField(model_name="markedclip", name="clip_score",),
        migrations.RemoveField(model_name="markedclip", name="type",),
        migrations.AlterField(
            model_name="markedscore",
            name="score",
            field=models.IntegerField(default=-1),
        ),
        migrations.CreateModel(
            name="MarkedDimensionScore",
            fields=[
                (
                    "dimension_score_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("dimension", models.CharField(default="", max_length=30)),
                ("dimension_score", models.IntegerField(default=-1)),
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
        ),
    ]