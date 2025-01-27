# Generated by Django 4.2.11 on 2024-05-20 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("etudiant", "0013_etudiant_blocked"),
    ]

    operations = [
        migrations.CreateModel(
            name="CVModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fichier", models.BinaryField()),
                ("text_content", models.TextField()),
                (
                    "etudiant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="etudiant.etudiant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InfoPersonnelles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(default="", max_length=100)),
                ("prenom", models.CharField(default="", max_length=100)),
                ("profil", models.TextField(default="", null=True)),
                ("email", models.EmailField(default="", max_length=254, null=True)),
                ("telephone", models.CharField(default="", max_length=20, null=True)),
                ("github", models.URLField(blank=True, default="", null=True)),
                ("linkedin", models.URLField(blank=True, default="", null=True)),
                (
                    "skype",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "etudiant",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="etudiant.etudiant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SoftSkills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titreskills", models.TextField(default="", null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="softskills",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titreref", models.TextField(default="", null=True)),
                ("poste", models.TextField(default="", null=True)),
                ("emailref", models.TextField(default="", null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="references",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titreprojet", models.TextField(default="", null=True)),
                ("descriptionprojet", models.TextField(default="", null=True)),
                (
                    "fichier_zip",
                    models.FileField(blank=True, null=True, upload_to="projets/"),
                ),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projets",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Langue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("langue", models.CharField(default="", max_length=100, null=True)),
                ("niveau", models.CharField(default="", max_length=100, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="langues",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=50)),
                ("data", models.BinaryField(blank=True)),
                (
                    "cv_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="CV.cvmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Formation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nomformation",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "etablissement",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "debutformation",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "finformation",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formations",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(default="", max_length=100)),
                ("entreprise", models.CharField(default="", max_length=100, null=True)),
                (
                    "debutexperience",
                    models.CharField(default="", max_length=100, null=True),
                ),
                (
                    "finexperience",
                    models.CharField(default="", max_length=100, null=True),
                ),
                ("description", models.TextField(default="", null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Competence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categorie", models.CharField(default="", max_length=100, null=True)),
                ("competence", models.CharField(default="", max_length=100, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="competences",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomclub", models.CharField(default="", max_length=100, null=True)),
                ("role", models.CharField(default="", max_length=100, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clubs",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CentresDinteret",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titreInteret", models.TextField(default="", null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="centresdinteret",
                        to="CV.infopersonnelles",
                    ),
                ),
            ],
        ),
    ]
