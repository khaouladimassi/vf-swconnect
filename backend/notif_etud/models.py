from django.db import models
from datetime import datetime
from accounts.models import CustomUser
from demande.models import Demande

class NotificationEtudiant(models.Model):
    demande=models.ForeignKey(Demande, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message
