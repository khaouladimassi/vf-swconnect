from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notificationentreprise
from demande.models import Demande
from etudiant.models import Etudiant
from .serializers import NotificationSerializer
from accounts.models import CustomUser
from rest_framework.decorators import api_view
from urllib.parse import urljoin
from offer.models import Offer
from django.shortcuts import get_object_or_404




class StockNotifEntre(APIView):
    def post(self, request, offer_id):
        # Vérifier si toutes les données nécessaires sont présentes dans la requête POST
        if 'message' not in request.data:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Récupérer le message de la requête
        message = request.data.get('message')

        # Vérifier si offer_id est valide
        offer = get_object_or_404(Offer, pk=offer_id)

        # Créer et sauvegarder la nouvelle notification
        notification = Notificationentreprise(offer=offer, message=message)
        notification.save()

        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetNotifByEntreprise(APIView):
    def get(self, request, entreprise_id):
        try:
            # Récupérer les 7 dernières notifications associées à l'entreprise
            notifications = Notificationentreprise.objects.filter(offer__entreprise_id=entreprise_id).order_by('-created_at')[:7]
            serialized_notifications = []

            for notification in notifications:
                serialized_notification = {
                    'message': notification.message,
                    'entreprise_id': notification.offer.entreprise_id,
                    'created_at': notification.created_at
                }
                serialized_notifications.append(serialized_notification)

            return Response(serialized_notifications, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)