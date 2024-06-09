from urllib.parse import urljoin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FavorisOffer
from .serializers import FavorisOfferSerializer
from etudiant.models import Etudiant
from offer.models import Offer

class AddFavoris(APIView):
    def post(self, request, etudiant_id,offer_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
            offer = Offer.objects.get(id=offer_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        except Offer.DoesNotExist:
            return Response({"message": "Offer not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the favorite already exists
        if FavorisOffer.objects.filter(etudiant=etudiant, offer=offer).exists():
            return Response({"message": "Offer already favorited"}, status=status.HTTP_400_BAD_REQUEST)

        favorite_offer = FavorisOffer(etudiant=etudiant, offer=offer)
        favorite_offer.save()

        serializer = FavorisOfferSerializer(favorite_offer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetFavorisById(APIView):
    def get(self, request, favorite_offer_id):
        try:
            favorite_offer = FavorisOffer.objects.get(id=favorite_offer_id)
            serializer = FavorisOfferSerializer(favorite_offer)
            return Response(serializer.data)
        except FavorisOffer.DoesNotExist:
            return Response({"message": "Favorite offer not found"}, status=status.HTTP_404_NOT_FOUND)


class GetFavoris(APIView):
    def get(self, request, etudiant_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

        favorite_offers = FavorisOffer.objects.filter(etudiant=etudiant)
        serialized_favorite_offers = []
        for favorite_offer in favorite_offers:
            serialized_favorite_offer = FavorisOfferSerializer(favorite_offer).data
            serialized_favorite_offer['title'] = favorite_offer.offer.title
            serialized_favorite_offer['location']=favorite_offer.offer.location
            serialized_favorite_offer['maximal_payment']=favorite_offer.offer.maximal_payment
            serialized_favorite_offer['description']=favorite_offer.offer.description
            serialized_favorite_offer['created_at']=favorite_offer.offer.created_at
            serialized_favorite_offer['offer_type']=favorite_offer.offer.offer_type
            serialized_favorite_offer['skills']=favorite_offer.offer.skills
            serialized_favorite_offer['offer_id']=favorite_offer.offer.id
            serialized_favorite_offer['entreprise']=favorite_offer.offer.entreprise.nom
            serialized_favorite_offer['entreprise_id']=favorite_offer.offer.entreprise.id
            serialized_favorite_offer['profile_logo']= urljoin(request.build_absolute_uri('/')[:-1],favorite_offer.offer.entreprise.profile_logo.url)
            serialized_favorite_offers.append(serialized_favorite_offer)
        return Response(serialized_favorite_offers, status=status.HTTP_200_OK)
    


class DeleteFavoris(APIView):
    def delete(self, request, favorite_offer_id):
        try:
            favorite_offer = FavorisOffer.objects.get(id=favorite_offer_id)
        except FavorisOffer.DoesNotExist:
            return Response({"message": "Favorite offer not found"}, status=status.HTTP_404_NOT_FOUND)

        favorite_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
