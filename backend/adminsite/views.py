from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser


from .models import Admin
from .serializers import AdminSerializer
# cette vue prend en charge toutes les opérations CRUD (Create, Retrieve, Update, Delete) pour le modèle Etudiant.
class AdminViewSet(viewsets.ModelViewSet):

    queryset = Admin.objects.all()
    serializer_class =AdminSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['username', 'email', 'password']


    

class GetAdmin(APIView):
    def get(self, request, pk):
        try:
            admin = Admin.objects.get(pk=pk)
            # Assuming there's a one-to-one relationship between Etudiant and Profile_photo
            profile_logo_path = admin.profile_photo.url
            profile_cover_path = admin.profile_cover.url
     
            serializer = AdminSerializer(admin)
            # Add profile_id to the serialized data
            serialized_data = serializer.data
            serialized_data['profile_photo'] = profile_logo_path
            serialized_data['profile_cover'] = profile_cover_path
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Admin.DoesNotExist:
            return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
    
class GetAdmins(APIView):
    def get(self, request):
            admins = Admin.objects.all()
            serializer = AdminSerializer(admins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



class AdminUpdateView(APIView):
    def put(self, request, pk):
        try:
            admin = Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Response({"message": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Save the etudiant object to reflect the changes
        admin.save()

        # Serialize the etudiant object with the updated data
        serializer = AdminSerializer(admin, data=request.data, partial=True)
        if 'username' in request.data:
            new_username = request.data['username']
            if Admin.objects.exclude(pk=pk).filter(username=new_username).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            # Save the serialized data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Construct detailed error messages
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
