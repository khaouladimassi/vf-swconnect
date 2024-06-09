from django.conf import settings
from rest_framework import serializers
from .models import Entreprise


class EntrepriseSerializer(serializers.ModelSerializer):
  
  
  def update(self, instance, validated_data):
        # Update only the fields that are provided in the request
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

  class Meta:
        model = Entreprise
        fields = '__all__'



    