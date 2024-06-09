

# Create your models here.
from django.db import models

from accounts.models import CustomUser

class Admin(CustomUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    profile_cover = models.ImageField(upload_to='cover_photos/', blank=True, null=True)