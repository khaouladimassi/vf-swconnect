# models.py
from django.db import models
from accounts.models import CustomUser


class UserAction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100,default='')
    action_message = models.CharField(max_length=255, null=True)  # Ajout du champ action_message
    timestamp = models.DateTimeField(auto_now_add=True)
    # Autres champs nécessaires

    class Meta:
        ordering = ['-timestamp']