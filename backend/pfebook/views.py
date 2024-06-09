from urllib.parse import urljoin
from django.shortcuts import render

from .models import Entreprise
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Pfebook
from .serializers import  PfebookSerializer
from django.db.models import Q

class PfebookViewSet(viewsets.ModelViewSet):

    queryset = Pfebook.objects.all()
    serializer_class = PfebookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]


class PfebookCreateView(APIView):
     def post(self, request, company_id):
        try:
            entreprise = Entreprise.objects.get(pk=company_id)
        except Entreprise.DoesNotExist:
            return Response({"error": "Entreprise does not exist"}, status=status.HTTP_404_NOT_FOUND)

   

        # Get the uploaded file from the request
        pfe_book = request.FILES.get('pfe_book')


        print(pfe_book)
    

        # Check if both title and file are present
        if  pfe_book:
            # Create data dictionary for serializer
            data = {
                'entreprise': entreprise.id,

                'file': pfe_book,
                'titre':request.data.get('titre'),

            }

            # Create serializer instance with data

            print(pfe_book)
            serializer = PfebookSerializer(data=data)

            # Validate the serializer
            if serializer.is_valid():
                # Save the serializer
                serializer.save()
                # Return successful response
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                # Return error response if serializer is not valid
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return error response if title or file is missing
            return Response({"error": " file missing"}, status=status.HTTP_400_BAD_REQUEST)
        
class getBookById(APIView):
    def get(self, request, pk):
        try:
            pfebook = Pfebook.objects.get(pk=pk)
            serializer = PfebookSerializer(pfebook)
            return Response(serializer.data)
        except Pfebook.DoesNotExist:
            return Response({"error": "Pfebook does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
class updateBook(APIView):
    def put(self, request, entreprise_id, pk):
        try:
            # Get the Pfebook instance to update
            pfebook = Pfebook.objects.get(pk=pk)

            # Check if the Pfebook belongs to the specified entreprise
            if pfebook.entreprise_id != entreprise_id:
                return Response({"error": "Pfebook does not belong to specified entreprise"}, status=status.HTTP_403_FORBIDDEN)

            # Update the Pfebook instance with request data
            serializer = PfebookSerializer(pfebook, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pfebook.DoesNotExist:
            return Response({"error": "Pfebook does not exist"}, status=status.HTTP_404_NOT_FOUND)

class deleteBook(APIView):        
 def delete(self, request, pk):
        try:
            pfebook = Pfebook.objects.get(pk=pk)
            pfebook.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pfebook.DoesNotExist:
            return Response({"error": "Pfebook does not exist"}, status=status.HTTP_404_NOT_FOUND)

class getAllBook(APIView):
    def get(self, request):
        books = Pfebook.objects.all()
        serialized_books=[]

        for book in books:
            serialized_book=PfebookSerializer(book).data
            serialized_book['entreprise_id']=book.entreprise.id
            serialized_book['title']=book.titre
            serialized_book['entreprise_nom']=book.entreprise.nom
            serialized_book['entreprise_location']=book.entreprise.location
            serialized_book['profile_logo']= urljoin(request.build_absolute_uri('/')[:-1],book.entreprise.profile_logo.url)
            serialized_books.append(serialized_book)
        return Response(serialized_books,status=status.HTTP_200_OK)

class getBookByEnt(APIView):   
 def get(self, request, entreprise_id):
        try:
            pfebooks = Pfebook.objects.filter(entreprise_id=entreprise_id)
            serializer = PfebookSerializer(pfebooks, many=True)
            return Response(serializer.data)
        except Pfebook.DoesNotExist:
            return Response({"error": "Pfebooks for this entreprise do not exist"}, status=status.HTTP_404_NOT_FOUND)

            ####################################
class GetpfebookByMc(APIView):
    def get(self, request, format=None):
        query = request.GET.get('q', '')  # Récupère le mot-clé de la requête
        domain = request.GET.get('domain', '')  # Récupère le domaine de la requête

        if query:
            # Filtre les PFE books en fonction du mot-clé
            books = Pfebook.objects.filter(
                Q(entreprise__nom__icontains=query) | 
                Q(titre__icontains=query) 
            )
        else:
            # Si aucun mot-clé n'est fourni, retourne tous les PFE books
            books = Pfebook.objects.all()

        # Applique les filtres supplémentaires
        if domain:
            books = books.filter(domain__icontains=domain)

        # Sérialise les PFE books trouvés
        serialized_books = []
        for book in books:
            serialized_book = PfebookSerializer(book).data
            serialized_book['entreprise_id'] = book.entreprise.id
            serialized_book['title'] = book.titre
            serialized_book['entreprise_nom'] = book.entreprise.nom
            serialized_book['entreprise_location'] = book.entreprise.location
            serialized_book['profile_logo'] = urljoin(request.build_absolute_uri('/')[:-1], book.entreprise.profile_logo.url)
            serialized_books.append(serialized_book)

        return Response(serialized_books, status=status.HTTP_200_OK)
