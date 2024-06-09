from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notificationadmin
from demande.models import Demande
from etudiant.models import Etudiant
from .serializers import NotificationAdminSerializer
from accounts.models import CustomUser
from rest_framework.decorators import api_view
from urllib.parse import urljoin
from entreprise.models import Entreprise
from django.shortcuts import get_object_or_404




class StockNotifAdmin(APIView):
    def post(self, request):
        # Vérifier si toutes les données nécessaires sont présentes dans la requête POST
        if 'message' not in request.data:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Récupérer le message de la requête
        message = request.data.get('message')


        # Créer et sauvegarder la nouvelle notification
        notification = Notificationadmin(message=message)
        notification.save()

        serializer = NotificationAdminSerializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetNotifByAdmin(APIView):
    def get(self, request):
        try:
            # Récupérer les 7 dernières notifications
            notifications = Notificationadmin.objects.order_by('-created_at')[:7]
            serialized_notifications = []

            for notification in notifications:
                serialized_notification = {
                    'message': notification.message,
                    'created_at': notification.created_at
                }
                serialized_notifications.append(serialized_notification)

            return Response(serialized_notifications, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)