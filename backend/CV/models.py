from django.db import models
from etudiant.models import Etudiant


class CVModel(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    fichier = models.BinaryField()  # Pour stocker les données binaires du fichier PDF
    text_content = models.TextField() # Pour stocker le texte extrait du PDF


    def __str__(self):
        return f"PDF File {self.pk}"

class Image(models.Model):
    cv_model = models.ForeignKey(CVModel, related_name='images', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # Champs pour stocker la taille de l'image
    data = models.BinaryField(blank=True)  # Champs pour stocker les données binaires de l'image

    def __str__(self):
        return f"Image {self.pk} for CV {self.cv_model.pk}"
    


    
class InfoPersonnelles(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,default="")
    nom = models.CharField(max_length=100,default='')
    prenom = models.CharField(max_length=100,default='')
    profil = models.TextField(default='',null=True)
    email = models.EmailField(default='',null=True)
    telephone = models.CharField(max_length=20, default='',null=True)
    github = models.URLField(blank=True, default='',null=True)
    linkedin = models.URLField(blank=True, default='',null=True)
    skype = models.CharField(max_length=100, blank=True, default='',null=True)


class Formation(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='formations')
    nomformation = models.CharField(max_length=100,default='',null=True)
    etablissement = models.CharField(max_length=100,default='',null=True)
    debutformation = models.CharField(max_length=100, default='',null=True)
    finformation = models.CharField(max_length=100, default='',null=True)

class Competence(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='competences')
    categorie = models.CharField(max_length=100, default='', null=True)
    competence = models.CharField(max_length=100,default='', null=True)

class Experience(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE , related_name='experiences')
    titre = models.CharField(max_length=100,default='')
    entreprise = models.CharField(max_length=100,default='',null=True)
    debutexperience = models.CharField(max_length=100, default='',null=True)
    finexperience = models.CharField(max_length=100, default='',null=True)
    description = models.TextField(default='',null=True)

class Club(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='clubs')
    nomclub = models.CharField(max_length=100,default='',null=True)
    role = models.CharField(max_length=100,default='',null=True)

class Langue(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='langues')
    langue = models.CharField(max_length=100,default='',null=True)
    niveau = models.CharField(max_length=100, null=True, default='')

class Reference(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='references')
    titreref = models.TextField(default='',null=True)
    poste = models.TextField(default='',null=True)
    emailref = models.TextField(default='',null=True)



class Projets(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='projets')
    titreprojet = models.TextField(default='',null=True)
    descriptionprojet = models.TextField(default='',null=True)
    fichier_zip = models.FileField(upload_to='projets/', null=True ,blank=True)


class SoftSkills(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='softskills')
    titreskills = models.TextField(default='',null=True)

class CentresDinteret(models.Model):
    info = models.ForeignKey(InfoPersonnelles, on_delete=models.CASCADE, related_name='centresdinteret')
    titreInteret = models.TextField(default='',null=True)