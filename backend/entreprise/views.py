from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from rest_framework.response import Response
from rest_framework import status
from urllib.parse import urljoin
from django.db.models import Count
from django.db.models import Q




from .models import Entreprise
from .serializers import EntrepriseSerializer



class EntrepriseViewSet (viewsets.ModelViewSet):

    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['username']

    def perform_create(self, serializer):
        # Set user_type to "etudiant" before saving the new instance
        serializer.save(user_type='entreprise', profile_cover=settings.MEDIA_URL + 'cover_photos/telecharge.jpeg', profile_logo=settings.MEDIA_URL + 'profile_photos/Default_pfp.jpg')

        # Get the newly created instance
        new_entreprise = serializer.instance
        print('new_entreprise')

        # Create or retrieve token for the new etudiant
        token, created = Token.objects.get_or_create(user=new_entreprise)
        print("Token:", token.key)

        # Serialize the newly created instance
        serialized_entreprise = EntrepriseSerializer(new_entreprise)
        print(serialized_entreprise)
        print("Serialized EntrepriseData:", serialized_entreprise.data)


        # Return the serialized data with token and etudiant id
        return Response({
            'token': token.key,
            'entreprise_data': serialized_entreprise.data
        }, status=status.HTTP_201_CREATED)


class GetEntrepriseById(APIView):
    def get(self, request, pk):
        try:
            entreprise = Entreprise.objects.get(pk=pk)
            # Get the profile logo and cover paths
            profile_logo_path = entreprise.profile_logo.url
            profile_cover_path = entreprise.profile_cover.url

            serializer = EntrepriseSerializer(entreprise)
            # Add profile paths to the serialized data
            serialized_data = serializer.data
            serialized_data['profile_logo'] = profile_logo_path
            serialized_data['profile_cover'] = profile_cover_path
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Entreprise.DoesNotExist:
            return Response({"error": "Entreprise not found"}, status=status.HTTP_404_NOT_FOUND)
    
class DeleteEntreprise(APIView):
    def delete(self, request, pk):
        try:
            etudiant = Entreprise.objects.get(pk=pk)
            etudiant.delete()
            return Response({"success": "Entreprise deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Entreprise.DoesNotExist:
            return Response({"error": "Entreprise not found"}, status=status.HTTP_404_NOT_FOUND)

class AllEntreprise(APIView):
    def get(self, request):
        entreprises = Entreprise.objects.all()
        serializer = EntrepriseSerializer(entreprises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class EntrepriseUpdateView(APIView):
    
    def put(self, request, pk):
        try:
            entreprise = Entreprise.objects.get(pk=pk)
        except Entreprise.DoesNotExist:
            return Response({"message": "Entreprise not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EntrepriseSerializer(entreprise, data=request.data, partial=True)
        if 'username' in request.data:
            new_username = request.data['username']
            if Entreprise.objects.exclude(pk=pk).filter(username=new_username).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            serializer.save()
            entreprise.is_configured = True
            entreprise.save()


            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Construct detailed error messages
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
class verify(APIView):
      def put(self,request, pk):
            try:
                entreprise = Entreprise.objects.get(pk=pk)
            except Entreprise.DoesNotExist:
                return Response({'error': 'Entreprise not found'}, status=status.HTTP_404_NOT_FOUND)
            
            entreprise.verified = True
            entreprise.save()
            serializer = EntrepriseSerializer(entreprise)
            return Response(serializer.data)

##########################################  
class TotalEntreprises(APIView):
    def get(self, request):
        total_entreprises = Entreprise.objects.count()
        return Response({"total_entreprises": total_entreprises}, status=status.HTTP_200_OK)


class GetCompanyByMc(APIView):
    def get(self, request):
        query = request.GET.get('q', '')  # Récupère le mot-clé de la requête

        # Filtre les entreprises en fonction du mot-clé
        entreprises = Entreprise.objects.filter(
            Q(nom__icontains=query) | 
            Q(location__icontains=query) |
            Q(type_industrie__icontains=query) 
        )

        # Calcul du total d'offres pour chaque entreprise filtrée
        entreprises_with_total_offers = entreprises.annotate(total_offers=Count('offer__entreprise_id'))

        # Sérialisation des entreprises trouvées
        serialized_entreprises = []
        for entreprise in entreprises_with_total_offers:
            serialized_entreprise = EntrepriseSerializer(entreprise).data
            serialized_entreprise['nom'] = entreprise.nom
            serialized_entreprise['entreprise_id'] = entreprise.id
            serialized_entreprise['location'] = entreprise.location
            serialized_entreprise['type_industrie'] = entreprise.type_industrie
            serialized_entreprise['profile_logo'] = entreprise.profile_logo.url
            serialized_entreprise['total_offers'] = entreprise.total_offers  # Ajout du total d'offres
            serialized_entreprises.append(serialized_entreprise)

        return Response(serialized_entreprises, status=status.HTTP_200_OK)