from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NotificationEtudiant
from demande.models import Demande
from etudiant.models import Etudiant
from .serializers import NotificationSerializer
from accounts.models import CustomUser
from rest_framework.decorators import api_view
from urllib.parse import urljoin
from offer.models import Offer



class StockNotifEtud(APIView):
    def post(self, request, demande_id):
        # Vérifier si toutes les données nécessaires sont présentes dans la requête POST
        if 'message' not in request.data:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Récupérer le message de la requête
        message = request.data.get('message')

       

        # Vérifier si demande_id est valide
        try:
            demande = Demande.objects.get(pk=demande_id)
        except Demande.DoesNotExist:
            return Response({"error": "Invalid demande ID"}, status=status.HTTP_404_NOT_FOUND)

        # Vérifier si une notification pour cette demande et cet utilisateur existe déjà
        if NotificationEtudiant.objects.filter(demande=demande).exists():
            return Response({"message": "Notification for this demande already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Créer et sauvegarder la nouvelle notification
        notification = NotificationEtudiant(demande=demande, message=message)
        notification.save()

        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetNotifByEtudiant(APIView):
    def get(self, request, etudiant_id):
        try:
            # Récupérer les 7 dernières notifications associées à l'étudiant
            notifications = NotificationEtudiant.objects.filter(demande__etudiant_id=etudiant_id).order_by('-created_at')[:7]
            serialized_notifications = []

            for notification in notifications:
                serialized_notification = {
                    'message': notification.message,
                    'etudiant_id': notification.demande.etudiant_id,
                    'profile_logo': urljoin(request.build_absolute_uri('/')[:-1], notification.demande.offer.entreprise.profile_logo.url),
                    'created_at': notification.created_at
                }
                serialized_notifications.append(serialized_notification)

            return Response(serialized_notifications, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)