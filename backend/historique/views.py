# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserAction
from .serializers import ActionUserSerializer
from rest_framework.decorators import api_view
from accounts.models import CustomUser



class UserActionCreateView(APIView):
    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Extraire le message d'action de la requête POST
        action_message = request.data.get('action_message')

        # Vérifier si le message d'action est présent
        if action_message:
            # Créer une nouvelle instance de UserAction avec le message et l'utilisateur actuel
            user_action = UserAction.objects.create(user=user, action_message=action_message)

            # Répondre avec un message JSON indiquant que l'action a été enregistrée avec succès
            return Response({'message': 'Action enregistrée avec succès.'}, status=status.HTTP_201_CREATED)
        else:
            # Répondre avec un message JSON indiquant que le message d'action est manquant
            return Response({'error': 'Le message d\'action est manquant.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_actions(request, user_id):
    actions = UserAction.objects.filter(user_id=user_id)
    serialized_data = ActionUserSerializer(actions, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def search_by_mc(request, keyword):  # Ajout de la vue pour la recherche par mot-clé
    # Recherche les actions contenant le mot-clé dans le message d'action
    actions = UserAction.objects.filter(action_message__icontains=keyword)
    # Sérialise les données
    serialized_data = ActionUserSerializer(actions, many=True)
    # Retourne les données sérialisées
    return Response(serialized_data.data)