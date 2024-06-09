from django.db import models
from entreprise.models import Entreprise



class Offer(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    minimal_payment = models.DecimalField(max_digits=10, decimal_places=0,blank=True)
    maximal_payment = models.DecimalField(max_digits=10, decimal_places=0, blank=True)
    number_of_interns = models.IntegerField( blank=True)
    skills = models.JSONField(default=list)
    binome = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    offer_type = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=100, blank=True)
    expirationDate = models.CharField(max_length=100, blank=True)
   

    def __str__(self):
        return self.title