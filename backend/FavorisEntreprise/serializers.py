from rest_framework import serializers
from .models import FavorisEntreprise
class FavorisEntrepriseSerializer(serializers.ModelSerializer):

  class Meta:
        model=FavorisEntreprise
        fields = '__all__'