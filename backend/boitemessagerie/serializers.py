from rest_framework import serializers
from .models import Messagerie, CustomUser
from accounts.serializers import CustomUserSerializer

class MessagerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagerie
        fields = '__all__'

        def validate(self, data):
                if not data.get('body') and not data.get('file'):
                    raise serializers.ValidationError("Either body or file must be provided")
                return data
