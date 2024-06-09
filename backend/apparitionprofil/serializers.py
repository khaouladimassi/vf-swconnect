from rest_framework import serializers
from .models import ApparitionProfil

class ApparitionProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApparitionProfil
        fields = ['etudiant', 'date', 'nombre_apparitions']
