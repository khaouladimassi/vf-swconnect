from django.db import models
from etudiant.models import Etudiant
from entreprise.models import Entreprise

class FavorisEntreprise(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.entreprise} - {self.etudiant}'
