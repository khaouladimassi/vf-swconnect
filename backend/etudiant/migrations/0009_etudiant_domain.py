# Generated by Django 4.2.11 on 2024-05-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("etudiant", "0008_etudiant_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="etudiant",
            name="domain",
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
    ]