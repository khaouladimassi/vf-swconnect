from django.db import models
from entreprise.models import Entreprise

class Pfebook(models.Model):
    entreprise = models.OneToOneField(Entreprise, on_delete=models.CASCADE, related_name='pfe_book')
    file = models.FileField(upload_to='pfe_books')
    titre=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return self.file