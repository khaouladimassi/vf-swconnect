from rest_framework import serializers
from .models import CVModel ,NouveauProjet

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVModel
        fields = "__all__"



    def validate(self, data):
        """
        Valide les données de la requête.
        """
        # Vérifiez si le fichier est présent dans les données de la requête
        fichier_zip = data.get('fichier_zip')
        if not fichier_zip:
            raise serializers.ValidationError("Le fichier_zip est requis.")

        # Vous pouvez effectuer d'autres validations ici selon vos besoins

        return data