#Convertir les objets django en json

from rest_framework import serializers
from .models import Admin
from rest_framework.authtoken.models import Token




class AdminSerializer(serializers.ModelSerializer):
 

    def update(self, instance, validated_data):
        # Update only the fields that are provided in the request
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


    class Meta :
        model = Admin
        fields = "__all__"