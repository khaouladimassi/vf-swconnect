from urllib.parse import urljoin
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from rest_framework import status
from django.http import JsonResponse
from django.views import View
from .models import Book, Entreprise, Offer
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class CreateBookView(APIView):
    def post(self, request):
        try:
            data = request.data
            offer_ids = data.get('offer_ids', [])
            entreprise_id = data.get('entreprise')
 

            if not offer_ids:
                return Response({'offers': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)

            entreprise = Entreprise.objects.get(id=entreprise_id)
            offers = Offer.objects.filter(id__in=offer_ids)

            if not offers.exists():
                return Response({'offers': ['Invalid offer ids.']}, status=status.HTTP_400_BAD_REQUEST)

            book = Book.objects.create(
                entreprise=entreprise,
            
            )
            book.offers.set(offers)
            book.save()

            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Entreprise.DoesNotExist:
            return Response({'error': 'Entreprise not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetailView(APIView):
    def get(self, request,pk):
        try:
            book = Book.objects.get(pk=pk)
            serialized_book= BookSerializer(book).data
            serialized_book['entreprise_nom'] = book.entreprise.nom
            serialized_book['entreprise_description'] = book.entreprise.description
            serialized_book['entreprise_vision'] = book.entreprise.vision
            serialized_book['entreprise_telephone'] = book.entreprise.telephone
            serialized_book['entreprise_fb'] = book.entreprise.fb_lien
            serialized_book['entreprise_location'] = book.entreprise.location
            serialized_book['entreprise_email'] = book.entreprise.email
            serialized_book['entreprise_site'] = book.entreprise.site_url
            serialized_book['entreprise_in_lien'] = book.entreprise.in_lien
            serialized_book['entreprise_link_lien'] = book.entreprise.link_lien
            serialized_book['profile_logo']= urljoin(request.build_absolute_uri('/')[:-1],book.entreprise.profile_logo.url)
            offer_details = []
            for offer in book.offers.all():
            # Customize this part to extract the required details from each offer
                    offer_detail = {
                        'title': offer.title,
                        'description': offer.description,
                        'id_offre':offer.id,
                        'domain':offer.domain,
                        'role':offer.role,
                    'minimal_payment' :offer.minimal_payment,
                    'maximal_payment':offer.maximal_payment,
                    'education':offer.education,
                    'offer_type':offer.offer_type,
                    'duration':offer.duration,
                    'binome':offer.binome,
                    'number_of_interns': offer.number_of_interns


                    }
                    offer_details.append(offer_detail)
     

            serialized_book['offer_details'] = offer_details
            return Response(serialized_book, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)


class GetPfeBookByEntrepriseView(APIView):
    def get(self, request, entreprise_id):
        try:
            entreprise = get_object_or_404(Entreprise, id=entreprise_id)
            books = Book.objects.filter(entreprise=entreprise)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Entreprise.DoesNotExist:
            return Response({'error': 'Entreprise not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateBookView(APIView):
    def put(self, request, book_id):
        try:
            data = request.data
            file = data.get('file')
            titre = data.get('titre', 'Default title')
            text = data.get('text', 'Default text')
            template = data.get('template')

            book = get_object_or_404(Book, id=book_id)

            if file:
                book.file = file

            book.titre = titre
            book.text = text
            book.template=template
            book.save()

            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Delete(APIView):
    def delete(self, request, book_id):
        try:
           book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)