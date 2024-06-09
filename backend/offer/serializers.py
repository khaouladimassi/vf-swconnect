#Convertir les objets django en json

from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
  def validate_skills(self, value):
        # Check if the value is empty or None
        if value in [None, ""]:
            # If it's empty or None, return an empty list
            return []
        else:
            # Otherwise, return the value as is
            return value

  
  
  def update(self, instance, validated_data):
        # Update only the fields that are provided in the request
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
  
  class Meta :
        model = Offer
        fields = "__all__"

    