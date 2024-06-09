from rest_framework import serializers
from .models import NotificationEtudiant

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationEtudiant
        fields = ('id', 'user', 'demande', 'message', 'read', 'created_at')  # Champs à sérialiser

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