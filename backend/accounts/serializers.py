#Convertir les objets django en json

from rest_framework import serializers

from etudiant.serializers import EtudiantSerializer
from etudiant.models import Etudiant

from entreprise.serializers import EntrepriseSerializer
from entreprise.models import Entreprise

from adminsite.serializers import AdminSerializer
from adminsite.models import Admin
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    entreprise_details = serializers.SerializerMethodField()
    etudiant_details = serializers.SerializerMethodField()
    admin_details = serializers.SerializerMethodField()


    class Meta :
        model = CustomUser
        fields = "__all__"
    def get_entreprise_details(self, obj):
        if hasattr(obj, 'entreprise'):
            entreprise = Entreprise.objects.get(pk=obj.pk)
            return EntrepriseSerializer(entreprise).data
        return None
    
    def get_etudiant_details(self, obj):
        if hasattr(obj, 'etudiant'):
            etudiant = Etudiant.objects.get(pk=obj.pk)
            return EtudiantSerializer(etudiant).data
        return None
    
    def get_admin_details(self, obj):
        if hasattr(obj, 'admin'):
            admin = Admin.objects.get(pk=obj.pk)
            return AdminSerializer(admin).data
        return None
    
    