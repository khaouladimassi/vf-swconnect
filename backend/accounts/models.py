from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 
from rest_framework.authtoken.models import Token
class CustomUser(AbstractUser):
    
    USER_TYPE_CHOICES = (
        ('etudiant', 'Etudiant'),
        ('entreprise', 'Entreprise'),
        ('admin', 'Admin'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES,default='etudiant')
    is_configured = models.BooleanField(default=False)
    first_name = None
    last_name = None
    
    def __str__(self):
        return f'{self.user_type}{self.username} {self.email} {self.password}{self.is_active}{self.last_login}{self.is_staff}{self.is_superuser}{self.is_authenticated} '