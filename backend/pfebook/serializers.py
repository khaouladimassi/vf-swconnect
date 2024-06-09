#Convertir les objets django en json

from rest_framework import serializers
from .models import Pfebook

class PfebookSerializer(serializers.ModelSerializer):

    class Meta :
        model = Pfebook
        fields = "__all__"