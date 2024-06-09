from django.db import models
from datetime import datetime
from accounts.models import CustomUser

# Create your models here.
class FichierStocke(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='fichiers/')  # Champ pour stocker le fichier
    nomfichier = models.CharField(max_length=255)  # Champ pour stocker le nom du fichier
    date_stockage = models.DateField(auto_now_add=True) # Champ pour stocker la date de stockage

    def __str__(self):
        return self.nomfichier