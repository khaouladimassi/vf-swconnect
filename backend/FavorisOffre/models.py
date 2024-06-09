from django.db import models
from etudiant.models import Etudiant
from offer.models import Offer

class FavorisOffer(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.etudiant} - {self.offer.title}'
