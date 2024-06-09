from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drive.models import FichierStocke
from .serializers import FichierStockeSerializer
from accounts.models import CustomUser

class CreerFichierView(APIView):
    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FichierStockeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'message': 'Fichier créé avec succès.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AfficherFichierView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Filtrer les fichiers par utilisateur
        fichiers = FichierStocke.objects.filter(user=user)
        
        # Sérialiser les données des fichiers
        serialized_data = FichierStockeSerializer(fichiers, many=True)
        
        # Retourner les données sérialisées
        return Response(serialized_data.data)
class SupprimerFichierView(APIView):
    def delete(self, request, user_id, pk):
        try:
            # Vérifier si l'utilisateur existe
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Vérifier si le fichier appartient à l'utilisateur
            fichier = FichierStocke.objects.get(id=pk, user=user)
            fichier.delete()
            return Response({'message': 'Fichier supprimé avec succès.'}, status=status.HTTP_204_NO_CONTENT)
        except FichierStocke.DoesNotExist:
            return Response({'erreur': 'Le fichier spécifié n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'erreur': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class OuvrirFichierView(APIView):
    def get(self, request, fichier_id):
        try:
            # Récupérer le fichier à partir de l'ID
            fichier = FichierStocke.objects.get(id=fichier_id)
        except FichierStocke.DoesNotExist:
            return Response({'erreur': 'Le fichier spécifié n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Ouvrir le fichier et retourner une réponse HTTP avec son contenu
        response = HttpResponse(fichier.fichier, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(fichier.nomfichier)  # Nom du fichier
        return response

class GetFileView(APIView):
    def get(self, request, file_path):
        try:
            fichier = FichierStocke.objects.get(fichier=file_path)
            with open(fichier.fichier.path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{fichier.nomfichier}"'
                return response
        except FichierStocke.DoesNotExist:
            raise Http404("File does not exist")
        except Exception as e:
            return HttpResponse(status=500, content=str(e))