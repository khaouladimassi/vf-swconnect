# Generated by Django 4.2.11 on 2024-05-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("etudiant", "0007_rename_cv_certificats_certificats"),
    ]

    operations = [
        migrations.AddField(
            model_name="etudiant",
            name="role",
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
    ]