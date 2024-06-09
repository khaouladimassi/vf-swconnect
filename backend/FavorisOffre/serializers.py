from rest_framework import serializers
from .models import FavorisOffer

class FavorisOfferSerializer(serializers.ModelSerializer):

  class Meta:
        model=FavorisOffer
        fields = '__all__'