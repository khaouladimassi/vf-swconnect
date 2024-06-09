from urllib.parse import urljoin
from django.shortcuts import render

from .models import Entreprise
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Offer
from .serializers import  OfferSerializer

from django.db.models import Count
from datetime import datetime
from demande.models import  Demande



from django.db.models import Q

class OfferViewSet(viewsets.ModelViewSet):

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title']

class OfferCreateView(APIView):
     def post(self, request, company_id):
        try:
            entreprise = Entreprise.objects.get(pk=company_id)
        except Entreprise.DoesNotExist:
            return Response({"error": "Entreprise does not exist"}, status=status.HTTP_404_NOT_FOUND)

        skills = request.data.get('competence', [])
        data = {
            'entreprise': entreprise.id,
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'minimal_payment': request.data.get('minimal_payment'),
            'maximal_payment': request.data.get('maximal_payment'),
            'number_of_interns': request.data.get('number_of_interns'),
            'skills': skills,
            'binome': request.data.get('binome'),
            'domain': request.data.get('domain'),
            'role': request.data.get('role'),
            'location': request.data.get('location'),
            'offer_type': request.data.get('offer_type'),
            'duration': request.data.get('duration'),
            'education': request.data.get('education'),
            'status': request.data.get('status'),
            'expirationDate':request.data.get('expirationDate'),
            
        }

        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
class GetOfferById(APIView):
    def get(self, request, offer_id):
        try:
            offer = Offer.objects.get(pk=offer_id)
            serializer = OfferSerializer(offer)
            serialized_data = serializer.data

            # Add the name of the entreprise to the serialized data
            serialized_data['nom'] = offer.entreprise.nom
            serialized_data['nom_rh'] = offer.entreprise.nom_rh
            serialized_data['prenom_rh'] = offer.entreprise.prenom_rh
            serialized_data['telephone'] = offer.entreprise.telephone
            serialized_data['email'] = offer.entreprise.email
            serialized_data['telephone_rh'] = offer.entreprise.telephone_rh
            serialized_data['email_rh'] = offer.entreprise.email_rh
            serialized_data['site_url'] = offer.entreprise.site_url
            serialized_data['entreprise_id'] = offer.entreprise.id
            serialized_data['entreprise_logo'] = urljoin(request.build_absolute_uri('/')[:-1], offer.entreprise.profile_logo.url)
            serialized_data['entreprise_cover'] = urljoin(request.build_absolute_uri('/')[:-1], offer.entreprise.profile_cover.url)

            return Response(serialized_data)
        except Offer.DoesNotExist:
            return Response({"error": "Offer does not exist"}, status=status.HTTP_404_NOT_FOUND)



class GetAllOffers(APIView):
   def get(self, request):
        offers = Offer.objects.all()
        serialized_offers = []
        
        for offer in offers:
            serialized_offer = OfferSerializer(offer).data
            serialized_offer['nom'] = offer.entreprise.nom
            serialized_offer['entreprise_id'] = offer.entreprise.id
            serialized_offer['profile_logo']= urljoin(request.build_absolute_uri('/')[:-1],offer.entreprise.profile_logo.url)
            serialized_offers.append(serialized_offer)
        
        return Response(serialized_offers, status=status.HTTP_200_OK)


class UpdateOffer(APIView):
    def put(self, request, entreprise_id, offer_id):
        try:
            # Retrieve the offer
            offer = Offer.objects.get(pk=offer_id)
        except Offer.DoesNotExist:
            return Response({"error": "Offer does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Ensure that the offer belongs to the specified entreprise
        if offer.entreprise_id != entreprise_id:
            return Response({"error": "Offer does not belong to specified entreprise"}, status=status.HTTP_403_FORBIDDEN)

        # Get the data from the request
        data = request.data
        data["entreprise"] = offer.entreprise_id

        # Pass the data to the serializer along with the instance of the offer
        serializer = OfferSerializer(offer, data=data)

        # Validate and save the serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteOffer(APIView):
   def delete(self, request, offer_id):
        try:
            # Retrieve the offer
            offer = Offer.objects.get(pk=offer_id)
            # Delete the offer
            offer.delete()
            return Response({"message": "Offer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Offer.DoesNotExist:
            return Response({"error": "Offer does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class getOffersByEntreprise(APIView):
    def get(self, request, entreprise_id):
        try:
            offers = Offer.objects.filter(entreprise_id=entreprise_id)
            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        except Offer.DoesNotExist:
            return Response({"error": "Offers for this entreprise do not exist"}, status=status.HTTP_404_NOT_FOUND)

####################################
class GetOffersByMc(APIView):
    def get(self, request, format=None):
        query = request.GET.get('q', '')  # Récupère le mot-clé de la requête
        domain = request.GET.get('domain', '')  # Récupère le domaine de la requête
        type_stage = request.GET.get('type_stage', '')  # Récupère le type de stage de la requête
        binome = request.GET.get('binome', '')  # Récupère si c'est un binôme de la requête
        min_price = request.GET.get('minPrice', '')  # Récupère la valeur minimale de la fourchette de prix
        max_price = request.GET.get('maxPrice', '')  # Récupère la valeur maximale de la fourchette de prix

        # Filtre les offres en fonction du mot-clé
        offers = Offer.objects.filter(
            Q(entreprise__nom__icontains=query) | 
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(domain__icontains=query) |
            Q(role__icontains=query) |
            Q(location__icontains=query) |
            Q(offer_type__icontains=query) |
            Q(education__icontains=query) |
            Q(status__icontains=query) 
        )

        # Applique les filtres supplémentaires
        if domain:
            offers = offers.filter(domain__icontains=domain)
        if type_stage:
            offers = offers.filter(type_stage__icontains=type_stage)
        if binome:
            offers = offers.filter(binome__icontains=binome)
        if min_price:
            offers = offers.filter(price__gte=min_price)  # Filtre les offres avec un prix supérieur ou égal à la valeur minimale
        if max_price:
            offers = offers.filter(price__lte=max_price)  # Filtre les offres avec un prix inférieur ou égal à la valeur maximale

        # Sérialise les offres trouvées
        serialized_offers = []
        for offer in offers:
            serialized_offer = OfferSerializer(offer).data
            serialized_offer['nom'] = offer.entreprise.nom
            serialized_offer['entreprise_id'] = offer.entreprise.id
            serialized_offer['profile_logo'] = urljoin(request.build_absolute_uri('/')[:-1], offer.entreprise.profile_logo.url)
            serialized_offers.append(serialized_offer)

        return Response(serialized_offers, status=status.HTTP_200_OK)
    
class FilteredOfferAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Récupérer les paramètres de l'URL
        domain = kwargs.get('domain')
        offer_type = kwargs.get('stage_type')  # Utiliser le champ 'offer_type' pour le type de stage
        binome = kwargs.get('binome')
        min_price = kwargs.get('min_price')

        # Filtrer les offres en fonction des paramètres
        filtered_offers = Offer.objects.all()
        if domain:
            filtered_offers = filtered_offers.filter(domain=domain)
        if offer_type:
            filtered_offers = filtered_offers.filter(offer_type=offer_type)
        if binome:
            filtered_offers = filtered_offers.filter(binome=binome)
        if min_price is not None:
            filtered_offers = filtered_offers.filter(minimal_payment__gte=min_price)

        # Serializer les offres filtrées
        serializer = OfferSerializer(filtered_offers, many=True)
        serialized_offers = []
        for offer in filtered_offers:  # Utilisation de filtered_offers ici
            serialized_offer = OfferSerializer(offer).data
            serialized_offer['nom'] = offer.entreprise.nom
            serialized_offer['entreprise_id'] = offer.entreprise.id
            serialized_offer['profile_logo'] = urljoin(request.build_absolute_uri('/')[:-1], offer.entreprise.profile_logo.url)
            serialized_offers.append(serialized_offer)

        # Retourner la réponse
        return Response(serialized_offers, status=status.HTTP_200_OK)
    
class GetTotalOffersByEntreprise(APIView):
    def get(self, request, entreprise_id):
        try:
            total_offers = Offer.objects.filter(entreprise_id=entreprise_id).count()
            return Response({"total_offers": total_offers})
        except Offer.DoesNotExist:
            return Response({"error": "Offers for this entreprise do not exist"}, status=status.HTTP_404_NOT_FOUND)
        
class RecentOffersView(APIView):
    def get(self, request, entreprise_id):
        try:
            recent_offers = Offer.objects.filter(entreprise_id=entreprise_id) \
                              .order_by('-created_at')[:5]

            offer_data = []
            for offer in recent_offers:
                total_demandes = Demande.objects.filter(offer=offer).count()
                demandes_acceptees = Demande.objects.filter(offer=offer, status='accepted').count()
                demandes_refusees = Demande.objects.filter(offer=offer, status='refused').count()
                demandes_en_attente = Demande.objects.filter(offer=offer, status='en attente').count()

                offer_info = {
                    "title": offer.title,
                    "total_demandes": total_demandes,
                    "demandes_acceptees": demandes_acceptees,
                    "demandes_refusees": demandes_refusees,
                    "demandes_en_attente": demandes_en_attente
                }
                offer_data.append(offer_info)

            return Response({"recent_offers": offer_data})
        except Offer.DoesNotExist:
            return Response({"error": "No offers found for this entreprise"}, status=status.HTTP_404_NOT_FOUND)
        
class TopOffersView(APIView):
    def get(self, request, entreprise_id):
        try:
            # Annoter les offres avec le nombre total de demandes associées
            top_offers = Offer.objects.filter(entreprise_id=entreprise_id) \
                .annotate(total_demandes=Count('demande')) \
                .order_by('-total_demandes')[:4]  # Sélectionner les 4 meilleures offres

            # Créer une liste de dictionnaires pour stocker les données des offres
            top_offers_data = []
            for offer in top_offers:
                total_demandes = Demande.objects.filter(offer=offer).count()
               

                # Ajouter les informations de l'offre à la liste
                top_offers_data.append({
                    "title": offer.title,
                    "total_demandes": total_demandes,
                  
                })

            return Response({"top_offers": top_offers_data})
        except Offer.DoesNotExist:
            return Response({"error": "No offers found for this entreprise"}, status=status.HTTP_404_NOT_FOUND)
        
class OffersPerMonthView(APIView):
    def get(self, request, entreprise_id):
        try:
            # Récupérer la date actuelle
            current_month = datetime.now().month
            current_year = datetime.now().year

            # Filtrer les offres de l'entreprise pour le mois actuel
            offers_per_month = Offer.objects.filter(entreprise_id=entreprise_id, created_at__month=current_month, created_at__year=current_year) \
                                              .values('created_at__month') \
                                              .annotate(offers_count=Count('id'))

            # Créer une liste pour stocker les données du nombre d'offres par mois
            offers_per_month_data = []
            for offer_per_month in offers_per_month:
                offers_per_month_data.append({
                    "month_number": offer_per_month['created_at__month'],
                    "offers_count": offer_per_month['offers_count']
                })

            return Response({"offers_per_month": offers_per_month_data})
        except Offer.DoesNotExist:
            return Response({"error": "No offers found for this entreprise"}, status=status.HTTP_404_NOT_FOUND)

class OffersSummaryView(APIView):
    def get(self, request):
        try:
            # Nombre total d'offres
            total_offers = Offer.objects.count()

            # Nombre d'offres avec le statut "en cours de recrutement"
            recruitment_offers = Offer.objects.filter(status='en cours de recrutement').count()

            # Nombre d'offres avec le statut "soon"
            soon_offers = Offer.objects.filter(status='soon').count()

            # Nombre d'offres expirées
            expired_offers = Offer.objects.filter(status='Expirée').count()

            # Construire la réponse
            response_data = {
                'total_offers': total_offers,
                'recruitment_offers': recruitment_offers,
                'soon_offers': soon_offers,
                'expired_offers': expired_offers,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

