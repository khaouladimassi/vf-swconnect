# Generated by Django 4.2.11 on 2024-05-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0011_alter_offer_binome_alter_offer_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="maximal_payment",
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="offer",
            name="minimal_payment",
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
    ]
