from urllib.parse import urljoin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
import logging

from etudiant.models import Etudiant
from entreprise.models import Entreprise
from django.db.models.functions import TruncMonth
from django.db.models import Count



from .models import CustomUser
from .serializers import CustomUserSerializer
# cette vue prend en charge toutes les opérations CRUD (Create, Retrieve, Update, Delete) pour le modèle Etudiant.
class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [ 'username', 'email', 'password']


  
logger = logging.getLogger(__name__)

class LogoutView(APIView):
    def post(self, request):
        try:
            return Response({'message': 'Logout successful'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        
class GetUserById(APIView):
    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(pk=pk)

            serializer = CustomUserSerializer(user)
            print(serializer.data)       
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Entreprise.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class GetUserByUsername(APIView):
    def get(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(username=username, password=password)
        except CustomUser.DoesNotExist:
            user = None
        if user:
            token, created = Token.objects.get_or_create(user=user)
            user_type = user.user_type  # Assuming user_type is a field on your CustomUser model
            user_id=user.id
            user_isconfigured=user.is_configured
            verified=None
            blocked=None

            if user_type == 'etudiant':
                etudiant_user=Etudiant.objects.get(id=user.id)
                blocked=etudiant_user.blocked
                return Response({'user_id': user_id, 'token': token.key, 'user_type': 'etudiant','is_configured':user_isconfigured,'blocked':blocked}, status=status.HTTP_200_OK)
            elif user_type == 'entreprise':
                entreprise_user = Entreprise.objects.get(id=user.id)
                verified = entreprise_user.verified
                return Response({'user_id': user_id, 'token': token.key, 'user_type': 'entreprise','is_configured':user_isconfigured, 'verified': verified}, status=status.HTTP_200_OK)
            elif user_type == 'admin':
                # Redirect to the admin interface
                return Response({'user_id': user_id, 'token': token.key, 'user_type': 'admin'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

################################################""
class NewUsersPerMonthView(APIView):
    def get(self, request):
        # Group users by month and count the number of users for each month
        users_per_month = CustomUser.objects.annotate(month=TruncMonth('date_joined')) \
                                       .values('month') \
                                       .annotate(count=Count('id')) \
                                       .exclude(user_type = 'admin')\
                                       .order_by('month')
        return Response(users_per_month, status=status.HTTP_200_OK)