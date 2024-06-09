from django.db import models
from entreprise.models import Entreprise
from offer.models import Offer

# Create your models here.
class Book(models.Model):
    offers = models.ManyToManyField(Offer, related_name='books')
    file = models.FileField(upload_to='books/',blank=True,null=True)
    template=models.CharField(max_length=255)
    text = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    titre=models.CharField(max_length=255,default='Entreprise est une entreprise qui cherche à changer la façon dont les gens se connectent.')
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"Book for {self.entreprise.name} with offers: {', '.join(offer.title for offer in self.offers.all())}"