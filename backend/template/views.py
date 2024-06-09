from rest_framework.views import APIView
from .models import TemplateName
from .serializers import TemplateNameSerializer
from accounts.models import CustomUser
from template.models import TemplateName
from rest_framework.response import Response
from rest_framework import status

class StockTemplateView(APIView):
    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = TemplateNameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OuvrirTemplateView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Filtrer les templates par l'utilisateur associé à l'étudiant
        templates = TemplateName.objects.filter(etudiant=user)
        
        # Sérialiser les données des templates
        serialized_data = TemplateNameSerializer(templates, many=True)
        
        # Retourner les données sérialisées
        return Response(serialized_data.data)
