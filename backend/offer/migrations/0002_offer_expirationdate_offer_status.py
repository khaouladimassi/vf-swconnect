# Generated by Django 4.2.11 on 2024-05-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="expirationDate",
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="offer",
            name="status",
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
    ]
