# Generated by Django 4.2.11 on 2024-05-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0002_offer_expirationdate_offer_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="workspace",
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
    ]
