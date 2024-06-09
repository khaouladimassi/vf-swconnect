from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser

from django.db.models import Q
from urllib.parse import urljoin

from .models import Etudiant
from .serializers import EtudiantSerializer
# cette vue prend en charge toutes les opérations CRUD (Create, Retrieve, Update, Delete) pour le modèle Etudiant.
class EtudiantViewSet(viewsets.ModelViewSet):

    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['last_name', 'first_name', 'email', 'password']

    def perform_create(self, serializer):
        # Set user_type to "etudiant" before saving the new instance
        serializer.save(user_type='etudiant',profile_cover=settings.MEDIA_URL + 'cover_photos/telecharge.jpeg', profile_photo=settings.MEDIA_URL + 'profile_photos/Default_pfp.jpg')

        # Get the newly created instance
        new_etudiant = serializer.instance

        # Create or retrieve token for the new etudiant
        token, created = Token.objects.get_or_create(user=new_etudiant)
        print("Token:", token.key)

        # Serialize the newly created instance
        serialized_etudiant = EtudiantSerializer(new_etudiant)
        print("Serialized Etudiant Data:", serialized_etudiant.data)


        # Return the serialized data with token and etudiant id
        return Response({
            'token': token.key,
            'etudiant_data': serialized_etudiant.data
        }, status=status.HTTP_201_CREATED)

class Login(APIView):
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
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class EtudiantCreateView(APIView):
     def put(self, request, pk):
        try:
            etudiant = Etudiant.objects.get(pk=pk)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        
        etudiant = request.etudiant
        first_name = etudiant.first_name
        last_name = etudiant.last_name
        username=etudiant.username
        email=etudiant.email
        password=etudiant.password
        user_type=etudiant.user_type
      
          
        skills = request.data.get('competence', [])
        data = {
            'etudiant': etudiant.id,
            'first_name': first_name,
            'last_name': last_name,
            'usename':username,
            'email':email,
            'password':password,
            'user_type':user_type,

          'photo_profile': request.data.get('photo'),
            'cv': request.data.get('cv'),
            'certificates': request.data.get('certif'),
            'lettre': request.data.get('lettre'),
            'skills': skills,
            'bio': request.data.get('bio'),
            'location': request.data.get('location'),
           'fb_lien':request.data.get('fbLien'),
            'git_lien':request.data.get('gitLien'),
             'twit_lien':request.data.get('twitLien'),
              'in_lien':request.data.get('inLien'),
               'link_lien':request.data.get('linkLien'),
                'yout_lien':request.data.get('youtLien'),
            'telephone': request.data.get('telephone'),
            'education': request.data.get('education'),
            'sexe': request.data.get('sexe'),
            'date_naissance':request.data.get('dateNaissance'),
            
        }

        serializer = EtudiantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetEtudiantById(APIView):
    def get(self, request, pk):
        try:
            etudiant = Etudiant.objects.get(pk=pk)
            # Assuming there's a one-to-one relationship between Etudiant and Profile_photo
            profile_logo_path = etudiant.profile_photo.url
            profile_cover_path = etudiant.profile_cover.url
    
            cv_path = etudiant.cv.url if etudiant.cv and etudiant.cv.name else None  # Check if cv is not None and has a name
            certificats_path = etudiant.certificats.url if etudiant.certificats and etudiant.certificats.name else None 

                
            serializer = EtudiantSerializer(etudiant)
            # Add profile_id to the serialized data
            serialized_data = serializer.data
            serialized_data['profile_photo'] = profile_logo_path
            serialized_data['profile_cover'] = profile_cover_path
            serialized_data['cv']=cv_path
            serialized_data['certificats']=certificats_path
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
    
class DeleteEtudiant(APIView):
    def delete(self, request, pk):
        try:
            etudiant = Etudiant.objects.get(pk=pk)
            etudiant.delete()
            return Response({"success": "Etudiant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

class AllEtudiant(APIView):
    def get(self, request):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantSerializer(etudiants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EtudiantUpdateView(APIView):
    
    def put(self, request, pk):
        try:
            etudiant = Etudiant.objects.get(pk=pk)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Update etudiant attributes
        etudiant.is_configured = True
        
        # Save the etudiant object to reflect the changes
        etudiant.save()

        # Serialize the etudiant object with the updated data
        serializer = EtudiantSerializer(etudiant, data=request.data, partial=True)
        if 'username' in request.data:
            new_username = request.data['username']
            if Etudiant.objects.exclude(pk=pk).filter(username=new_username).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            # Save the serialized data
            serializer.save()
         

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Construct detailed error messages
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

class block(APIView):
      def put(self,request, pk):
            try:
                etudiant = Etudiant.objects.get(pk=pk)
            except Etudiant.DoesNotExist:
                return Response({'error': 'Etudiant not found'}, status=status.HTTP_404_NOT_FOUND)
            
            etudiant.blocked = True
            etudiant.save()
            serializer = EtudiantSerializer(etudiant)
            return Response(serializer.data)
      
class unblock(APIView):
      def put(self,request, pk):
            try:
                etudiant = Etudiant.objects.get(pk=pk)
            except Etudiant.DoesNotExist:
                return Response({'error': 'Etudiant not found'}, status=status.HTTP_404_NOT_FOUND)
            
            etudiant.blocked = False
            etudiant.save()
            serializer = EtudiantSerializer(etudiant)
            return Response(serializer.data)


##################################################
class GetEtudByMc(APIView):
    def get(self, request, format=None):
        query = request.GET.get('q', '')  
        domain = request.GET.get('domain', '')
        education = request.GET.get('education', '')  
        role = request.GET.get('role', '')  
        skills = request.GET.get('skills', '')  
        location = request.GET.get('location', '')  



       

        # Filtre les offres en fonction du mot-clé
        etudiants = Etudiant.objects.filter(
            Q(education__icontains=query) |
            Q(domain__icontains=query) |
            Q(role__icontains=query) |
            Q(skills__icontains=query) |
            Q(location__icontains=query) 
        )

        # Applique les filtres supplémentaires
        if domain:
            etudiants = etudiants.filter(domain__icontains=domain)
        if education:
            etudiants = etudiants.filter(education__icontains=education)
        if role:
            etudiants = etudiants.filter(education__icontains=role)
        if skills:
            etudiants = etudiants.filter(education__icontains=skills)
        if location:
            etudiants = etudiants.filter(education__icontains=location)

        
        # Sérialise les offres trouvées

        serialized_etudiants = []
        for etudiant in etudiants:
 
            serializer = EtudiantSerializer(etudiant)
            # Add profile_id to the serialized data
            serialized_etudiant = serializer.data
            serialized_etudiant['profile_photo'] = etudiant.profile_photo.url
            serialized_etudiant['last_name'] = etudiant.last_name
            serialized_etudiant['first_name'] = etudiant.first_name

            serialized_etudiants.append(serialized_etudiant)


        return Response(serialized_etudiants, status=status.HTTP_200_OK)
    

class FilteredEtudAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Récupérer les paramètres de l'URL
        domain = kwargs.get('domain')
        education = kwargs.get('education')

       

        # Filtrer les offres en fonction des paramètres
        filtered_etuds = Etudiant.objects.all()
        if domain:
            filtered_etuds = filtered_etuds.filter(domain=domain)
        
        if education:
            filtered_etuds = filtered_etuds.filter(education=education)

        # Serializer les offres filtrées
        serializer = EtudiantSerializer(filtered_etuds, many=True)
        serialized_etudiants = []
        for etudiant in filtered_etuds:  
            serialized_etudiant = EtudiantSerializer(etudiant).data
            serialized_etudiant['profile_photo'] = etudiant.profile_photo.url
            serialized_etudiant['last_name'] = etudiant.last_name
            serialized_etudiant['first_name'] = etudiant.first_name
            #serialized_etudiant['profile_logo'] = urljoin(request.build_absolute_uri('/')[:-1], etudiant.profile_photo)
            serialized_etudiants.append(serialized_etudiant)

        # Retourner la réponse
        return Response(serialized_etudiants, status=status.HTTP_200_OK)
    

##############################"
class TotalEtudiants(APIView):
    def get(self, request):
        total_etudiants= Etudiant.objects.count()
        return Response({"total_etudiants": total_etudiants}, status=status.HTTP_200_OK)

