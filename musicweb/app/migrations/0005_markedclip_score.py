# Generated by Django 4.1.7 on 2023-04-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_user_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="markedclip",
            name="score",
            field=models.IntegerField(default=-1),
        ),
    ]
