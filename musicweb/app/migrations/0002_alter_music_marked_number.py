# Generated by Django 4.1.7 on 2023-03-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="marked_number",
            field=models.IntegerField(default=0),
        ),
    ]