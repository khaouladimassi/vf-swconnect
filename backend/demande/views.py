from urllib.parse import urljoin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Demande
from .serializers import DemandeSerializer
from etudiant.models import Etudiant
from offer.models import Offer
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncDate
from datetime import timedelta

from django.views import View
from django.http import JsonResponse
from collections import Counter

class AddDemande(APIView):
    def post(self, request, etudiant_id,offer_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
            offer = Offer.objects.get(id=offer_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        except Offer.DoesNotExist:
            return Response({"message": "Offer not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the favorite already exists
        if Demande.objects.filter(etudiant=etudiant, offer=offer).exists():
            return Response({"message": "Demande already sent"}, status=status.HTTP_400_BAD_REQUEST)

        demande = Demande(etudiant=etudiant, offer=offer)
        demande.save()

        serializer = DemandeSerializer(demande)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class GetDemandeById(APIView):
    def get(self, request, demande_id):
        try:
            demande =demande.objects.get(id=demande_id)
            serializer = DemandeSerializer(demande)
            return Response(serializer.data)
        except Demande.DoesNotExist:
            return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)


class GetDemandeByOffer(APIView):
    def get(self, request, offer_id):
        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            return Response({"message": "Offer not found"}, status=status.HTTP_404_NOT_FOUND)

        demandes = Demande.objects.filter(offer=offer)
        serialized_demandes=[]
        for demande in demandes:
            serialized_demande=DemandeSerializer(demande).data
            serialized_demande['etudiant_id']=demande.etudiant.id
            serialized_demande['nom']=demande.etudiant.last_name
            serialized_demande['prenom']=demande.etudiant.first_name
            serialized_demande['profile_photo']= urljoin(request.build_absolute_uri('/')[:-1],demande.etudiant.profile_photo.url)
            serialized_demandes.append(serialized_demande)
        return Response(serialized_demandes, status=status.HTTP_200_OK)
    
    
class GetDemandeByOfferEtudiant(APIView):
    def get(self, request, offer_id, etudiant_id):
        try:
            offer = Offer.objects.get(id=offer_id)
            etudiant = Etudiant.objects.get(id=etudiant_id)
        except Offer.DoesNotExist:
            return Response({"message": "Offer not found"}, status=status.HTTP_404_NOT_FOUND)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            demande = Demande.objects.get(offer=offer, etudiant=etudiant)
        except Demande.DoesNotExist:
            return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DemandeSerializer(demande)
        return Response(serializer.data)

class GetDemandeByEtudiant(APIView):
    def get(self, request, etudiant_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

        demandes = Demande.objects.filter(etudiant=etudiant)
        serialized_demandes=[]
        for demande in demandes:
            serialized_demande=DemandeSerializer(demande).data
            serialized_demande['entreprise_id']=demande.offer.entreprise.id
            serialized_demande['entreprise_nom']=demande.offer.entreprise.nom
            serialized_demande['offer_title']=demande.offer.title
            serialized_demande['profile_logo']= urljoin(request.build_absolute_uri('/')[:-1],demande.offer.entreprise.profile_logo.url)
            serialized_demandes.append(serialized_demande)
        return Response(serialized_demandes, status=status.HTTP_200_OK)
    
class DeleteDemande(APIView):
     def delete(self, request, demande_id):
         try:
            demande = Demande.objects.get(id=demande_id)
         except Demande.DoesNotExist:
             return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

         demande.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     

class SetAccepted(APIView):
    def put(self, request, demande_id):
        try:
            demande = Demande.objects.get(id=demande_id)
        except Demande.DoesNotExist:
            return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

        demande.status = 'accepted'
        demande.save()
        
        serialized_demandes = []
        demandes = Demande.objects.filter(id=demande_id)
        for demande in demandes:
            serialized_demande = DemandeSerializer(demande).data
            serialized_demande['offer_title'] = demande.offer.title
            serialized_demandes.append(serialized_demande)
        
        response_data = {
            "message": "Demande accepted",
            "demandes": serialized_demandes
        }
        
        return Response(response_data, status=status.HTTP_200_OK)

class SetRefused(APIView):
    def put(self, request, demande_id):
        try:
            demande = Demande.objects.get(id=demande_id)
        except Demande.DoesNotExist:
            return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

        demande.status = 'refused'
        demande.save()
        return Response({"message": "Demande refused"}, status=status.HTTP_200_OK)
    
#######################################################""
class DemandeStats(APIView):
    def get(self, request, etudiant_id):
        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

        accepted_count = Demande.objects.filter(etudiant=etudiant, status='accepted').count()
        refused_count = Demande.objects.filter(etudiant=etudiant, status='refused').count()
        pending_count = Demande.objects.filter(etudiant=etudiant, status='en attente').count()


        
        response_data = {
            "accepted_count": accepted_count,
            "refused_count": refused_count,
            "pending_count":pending_count


        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    

class CandidatureFrequencyView(View):
    def get(self, request, etudiant_id):
        # Récupérer la date actuelle
        current_date = timezone.now().date()

        # Calculer la date il y a 7 jours
        seven_days_ago = current_date - timedelta(days=6)  # Utiliser timedelta(days=6) pour obtenir une période de 7 jours

        # Récupérer la fréquence de candidature par jour pour l'étudiant donné
        candidature_frequency = Demande.objects.filter(
            etudiant_id=etudiant_id,
            created_at__date__gte=seven_days_ago,  # Utiliser la date d'il y a 7 jours comme filtre de début
            created_at__date__lte=current_date  # Utiliser la date actuelle comme filtre de fin
        ).annotate(
            date=TruncDate('created_at')  # Tronquer la date pour obtenir uniquement la partie jour
        ).values('date').annotate(
            frequency=Count('id')  # Compter le nombre de candidatures pour chaque jour
        ).order_by('date')  # Trier les résultats par date

        # Créer un dictionnaire pour stocker les données de chaque jour
        candidature_data = {}

        # Remplir le dictionnaire avec les données de chaque jour
        for single_date in (seven_days_ago + timedelta(n) for n in range(7)):
            date_str = single_date.strftime('%Y-%m-%d')
            candidature_data[date_str] = 0  # Initialiser la fréquence à 0 pour chaque jour

        # Mettre à jour la fréquence dans le dictionnaire avec les données réelles
        for item in candidature_frequency:
            date_str = item['date'].strftime('%Y-%m-%d')
            candidature_data[date_str] = item['frequency']

        # Convertir le dictionnaire en une liste de dictionnaires pour la réponse JSON
        candidature_data_list = [{'date': date_str, 'frequency': freq} for date_str, freq in candidature_data.items()]

        return JsonResponse(candidature_data_list, safe=False)  # Renvoyer les données au format JSON

class TopCompaniesView(APIView):
    def get(self, request):
        """
        Vue pour obtenir les 3 entreprises ayant reçu le plus de demandes.
        """
        # Agréger les demandes par entreprise et les compter
        #creer une liste de dictionnaires , chaque dictionnaire contient id_entreprise et nom_entreprise
        company_demands = Demande.objects.values('offer__entreprise__id', 'offer__entreprise__nom') \
            .annotate(total_demandes=Count('id')) \
            .order_by('-total_demandes')

        # Prendre les trois premières entreprises
        top_companies = company_demands[:3]

        return Response(top_companies, status=status.HTTP_200_OK)
    
class TopDomainsView(APIView):
    def get(self, request):
        # Récupérer les trois domaines les plus populaires avec le nombre total de demandes
        company_demands = Demande.objects.values('offer__domain') \
            .annotate(total_demandes=Count('id')) \
            .order_by('-total_demandes')[:3]

        # Initialiser une liste pour stocker les domaines les plus demandés avec leurs nombres de demandes
        top_domains = []

        # Parcourir les trois premiers domaines
        for company_demand in company_demands:
            domain = company_demand['offer__domain']
            total_demandes = company_demand['total_demandes']
            top_domains.append({'domain': domain, 'total_demandes': total_demandes})

        # Retourner la réponse avec les trois domaines les plus populaires et le nombre total de demandes pour chaque domaine
        return Response(top_domains, status=status.HTTP_200_OK)

class TopSkillsView(APIView):
    def get(self, request, domain):
        # Récupérer toutes les offres associées à ce domaine
        offers = Offer.objects.filter(domain=domain)

        # Initialiser une liste pour stocker les compétences de ce domaine
        skills = []

        # Parcourir chaque offre et récupérer ses compétences
        for offer in offers:
            skills.extend(offer.skills)

        # Compter l'occurrence de chaque compétence
        skill_counts = Counter(skills)

        # Trier les compétences par nombre d'occurrences pour obtenir les compétences les plus demandées
        top_skills = skill_counts.most_common()

        # Retourner la réponse avec les compétences les plus demandées pour ce domaine
        return Response(top_skills, status=status.HTTP_200_OK)

class TotalDemandsByEntrepriseView(APIView):
    def get(self, request, entreprise_id):
        """
        Vue pour obtenir le nombre total de demandes pour une entreprise spécifique.
        """
        try:
            total_demandes = Demande.objects.filter(offer__entreprise__id=entreprise_id).count()
            return Response({"entreprise_id": entreprise_id, "total_demandes": total_demandes}, status=status.HTTP_200_OK)
        except Demande.DoesNotExist:
            return Response({"error": "No demands found for this entreprise"}, status=status.HTTP_404_NOT_FOUND)