# Generated by Django 4.2.11 on 2024-05-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0007_alter_offer_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="skills",
            field=models.JSONField(default=list),
        ),
    ]