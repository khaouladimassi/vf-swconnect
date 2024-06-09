from rest_framework import serializers
from .models import UserAction

class ActionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = "__all__"