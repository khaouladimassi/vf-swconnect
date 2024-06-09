from django.db import models
from django.conf import settings 
from accounts.models import CustomUser
from rest_framework import serializers 

class Entreprise(CustomUser):
    nom=models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    description=models.TextField(blank=True)
    vision=models.TextField(blank=True)
    type_organisation=models.CharField(max_length=50, blank=True)
    type_industrie=models.CharField(max_length=50, blank=True)
    nombre_equipe=models.IntegerField(blank=True, null=True)
    date_etablissement=models.CharField(max_length=100,blank=True)
    site_url=models.URLField(blank=True, null=True)
    fb_lien = models.URLField(blank=True, null=True)
    twit_lien = models.URLField(blank=True, null=True)
    in_lien = models.URLField(blank=True, null=True)
    link_lien = models.URLField(blank=True, null=True)
    yout_lien = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100,blank=True)
    telephone_rh = models.CharField(max_length=15, blank=True)
    nom_rh = models.CharField(max_length=50, blank=True)
    prenom_rh = models.CharField(max_length=50, blank=True)
    email_rh = models.EmailField(max_length=50, blank=True)
    verified=models.BooleanField(default=False)


    profile_logo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    profile_cover = models.ImageField(upload_to='cover_photos/', null=True, blank=True)
    



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
    def __str__(self):
        return f'{self.type_industrie} {self.telephone} ' + super().__str__()
    
    
    
   


