from django.db import models
from etudiant.models import Etudiant

class TemplateName(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    nomtemplate = models.CharField(max_length=255)

    def __str__(self):
        return self.nomtemplate
