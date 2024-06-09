from rest_framework import serializers
from .models import Notificationentreprise

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificationentreprise
        fields = ('id','offer', 'message','created_at')  # Champs à sérialiser

    def validate(self, data):
        """
        Valide les données de la requête.
        """
        # Vérifiez si le message est présent dans les données de la requête
        message = data.get('message')
        if not message:
            raise serializers.ValidationError("Le message est requis.")

        # Vous pouvez effectuer d'autres validations ici selon vos besoins

        return data