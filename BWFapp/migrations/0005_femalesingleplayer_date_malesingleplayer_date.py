# Generated by Django 5.1.6 on 2025-03-11 12:31

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ("BWFapp", "0004_femalesingleplayer_country_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="femalesingleplayer",
            name="date",
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="malesingleplayer",
            name="date",
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
