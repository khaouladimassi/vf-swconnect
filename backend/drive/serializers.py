from rest_framework import serializers
from .models import FichierStocke

class FichierStockeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichierStocke
        fields = ('id', 'user', 'fichier', 'nomfichier', 'date_stockage')  # Champs à sérialiser

    def validate(self, data):
        """
        Valide les données de la requête.
        """
        # Vérifiez si le fichier est présent dans les données de la requête
        fichier = data.get('fichier')
        if not fichier:
            raise serializers.ValidationError("Le fichier est requis.")

        # Vous pouvez effectuer d'autres validations ici selon vos besoins

        return data