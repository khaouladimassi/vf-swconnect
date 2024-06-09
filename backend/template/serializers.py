from rest_framework import serializers
from .models import TemplateName

class TemplateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateName
        fields = ['id', 'etudiant', 'nomtemplate']


    def validate(self, data):
        """
        Valide les données de la requête.
        """
        # Vérifiez si le fichier est présent dans les données de la requête
        nomtemplate = data.get('nomtemplate')
        if not nomtemplate:
            raise serializers.ValidationError("ou est le nomtemplate.")

        # Vous pouvez effectuer d'autres validations ici selon vos besoins

        return data

