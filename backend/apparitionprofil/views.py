from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ApparitionProfil
from etudiant.models import Etudiant
from .serializers import ApparitionProfilSerializer
from datetime import date, timedelta
from django.http import JsonResponse



class EnregistrerApparitionProfil(APIView):
    def post(self, request, etudiant_id):
        # Vérifier si l'ID de l'étudiant est valide
        etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
        
        # Vérifier si une entrée existe déjà pour cet étudiant et cette date
        today = date.today()
        apparition_profil, created = ApparitionProfil.objects.get_or_create(etudiant=etudiant, date=today)
        
        # Si une entrée a été créée, initialiser à 1 sinon incrémenter
        if created:
            apparition_profil.nombre_apparitions = 1
        else:
            apparition_profil.nombre_apparitions += 1
        
        # Sauvegarder les modifications
        apparition_profil.save()
        
        serializer = ApparitionProfilSerializer(apparition_profil)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ApparitionProfilParSemaine(View):
    def get(self, request, etudiant_id):
        etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
        today = date.today()
        seven_days_ago = today - timedelta(days=6)  # Les 7 derniers jours incluant aujourd'hui

        apparitions = ApparitionProfil.objects.filter(etudiant=etudiant, date__range=[seven_days_ago, today]).order_by('date')
        
        data = []
        for single_date in (seven_days_ago + timedelta(n) for n in range(7)):
            apparition = apparitions.filter(date=single_date).first()
            nombre_apparitions = apparition.nombre_apparitions if apparition else 0
            data.append({
                'date': single_date,
                'nombre_apparitions': nombre_apparitions,
            })
        
        return JsonResponse(data, safe=False)