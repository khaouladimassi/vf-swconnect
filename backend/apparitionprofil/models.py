from django.db import models
from etudiant.models import Etudiant

class ApparitionProfil(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    date = models.DateField()
    nombre_apparitions = models.IntegerField(default=0)

    class Meta:
        unique_together = ['etudiant', 'date']
