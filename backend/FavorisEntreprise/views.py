from urllib.parse import urljoin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FavorisEntreprise
from .serializers import FavorisEntrepriseSerializer
from etudiant.models import Etudiant
from entreprise.models import Entreprise

class AddFavoriss(APIView):
    def post(self, request,entreprise_id,etudiant_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
            entreprise = Entreprise.objects.get(id=entreprise_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        except Entreprise.DoesNotExist:
            return Response({"message": "Entreprise not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the favorite already exists
        if FavorisEntreprise.objects.filter(etudiant=etudiant, entreprise=entreprise).exists():
            return Response({"message": "Etudiant already favorited"}, status=status.HTTP_400_BAD_REQUEST)

        favorite_etudiant= FavorisEntreprise(etudiant=etudiant, entreprise=entreprise)
        favorite_etudiant.save()

        serializer = FavorisEntrepriseSerializer(favorite_etudiant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetFavoriss(APIView):
    def get(self, request, entreprise_id):
        try:
            entreprise = Entreprise.objects.get(id=entreprise_id)
        except Entreprise.DoesNotExist:
            return Response({"message": "Entreprise not found"}, status=status.HTTP_404_NOT_FOUND)

        favorite_etudiants = FavorisEntreprise.objects.filter(entreprise=entreprise)
        serialized_favorite_etudiants=[]
        for favorite_etudiant in favorite_etudiants:
            serialized_favorite_etudiant=FavorisEntrepriseSerializer(favorite_etudiant).data
            serialized_favorite_etudiant['nom']=favorite_etudiant.etudiant.last_name
            serialized_favorite_etudiant['prenom']=favorite_etudiant.etudiant.first_name
            serialized_favorite_etudiant['bio']=favorite_etudiant.etudiant.bio
            serialized_favorite_etudiant['role']=favorite_etudiant.etudiant.role
            serialized_favorite_etudiant['skills']=favorite_etudiant.etudiant.skills
            serialized_favorite_etudiant['etudiant_id']=favorite_etudiant.etudiant.id
            serialized_favorite_etudiant['domain']=favorite_etudiant.etudiant.domain
            serialized_favorite_etudiant['education']=favorite_etudiant.etudiant.education
            serialized_favorite_etudiant['date_naissance']=favorite_etudiant.etudiant.date_naissance
            serialized_favorite_etudiant['profile_photo']= urljoin(request.build_absolute_uri('/')[:-1],favorite_etudiant.etudiant.profile_photo.url)
            serialized_favorite_etudiants.append(serialized_favorite_etudiant)
        return Response(serialized_favorite_etudiants, status=status.HTTP_200_OK)

class GetFavorissById(APIView):
    def get(self, request, favorite_etudiant_id):
        try:
            favorite_etudiant = FavorisEntreprise.objects.get(id=favorite_etudiant_id)
            serializer = FavorisEntrepriseSerializer(favorite_etudiant)
            return Response(serializer.data)
        except FavorisEntreprise.DoesNotExist:
            return Response({"message": "Favorite offer not found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteFavoriss(APIView):
    def delete(self, request, favorite_etudiant_id):
        try:
            favorite_etudiant = FavorisEntreprise.objects.get(id=favorite_etudiant_id)
        except FavorisEntreprise.DoesNotExist:
            return Response({"message": "Favorite etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

        favorite_etudiant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
