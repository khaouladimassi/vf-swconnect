# Generated by Django 4.2.11 on 2024-04-20 10:25

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("etudiant", "0003_remove_etudiant_confirm"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="etudiant",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelManagers(
            name="etudiant",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name="etudiant",
            old_name="nom",
            new_name="first_name",
        ),
        migrations.RenameField(
            model_name="etudiant",
            old_name="prenom",
            new_name="last_name",
        ),
        migrations.RemoveField(
            model_name="etudiant",
            name="email",
        ),
        migrations.RemoveField(
            model_name="etudiant",
            name="id",
        ),
        migrations.RemoveField(
            model_name="etudiant",
            name="password",
        ),
        migrations.AddField(
            model_name="etudiant",
            name="customuser_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=10,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
