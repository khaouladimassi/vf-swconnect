from django.db import models
from django.conf import settings

from accounts.models import CustomUser 


class Etudiant(CustomUser):
    first_name = models.CharField(max_length=100 ,blank=True)
    last_name = models.CharField(max_length=100,blank=True )
    role = models.CharField(max_length=100 ,blank=True)
    domain= models.CharField(max_length=100,blank=True )
    bio = models.TextField(blank=True)
    date_naissance = models.CharField(max_length=50,blank=True)
    sexe = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100, blank=True)
    skills = models.JSONField(default=list,null=True,blank=True)
    lettre_motivation = models.TextField(blank=True)
    fb_lien = models.URLField(blank=True, null=True)
    in_lien = models.URLField(blank=True, null=True)
    link_lien = models.URLField(blank=True, null=True)
    git_lien = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    profile_cover = models.ImageField(upload_to='cover_photos/', blank=True, null=True)
    cv = models.FileField(upload_to='cv_upload/', blank=True, null=True)
    certificats = models.FileField(upload_to='certificats/', blank=True, null=True)
    blocked=models.BooleanField(default=False)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} {self.first_name} ' + super().__str__()
    





    