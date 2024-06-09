from unicodedata import category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from PyPDF2 import PdfReader
import io
from .models import CVModel, Image  # Assurez-vous que le chemin est correct
from PIL import Image as PilImage
import openai
from dotenv import load_dotenv
import os
import requests
from django.http import JsonResponse
from django.http import HttpResponse
import google.generativeai as genai
import json
from .models import InfoPersonnelles, Formation, Competence, Experience, Club, Langue,Reference,Projets,SoftSkills,CentresDinteret
from rest_framework import viewsets
from etudiant.models import Etudiant





class UploadPDF(APIView):
    def post(self, request):
        try:
            etudiant_id = request.data.get('etudiant_id')  # Extraire user_id de la requête POST
            etudiant = Etudiant.objects.get(pk=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if 'imageUpload' in request.FILES:
            pdf_file = request.FILES['imageUpload']

            try:
                # Extraction du contenu du fichier PDF
                pdf_content = self.extract_content_from_pdf(pdf_file)

                # Création d'une instance de modèle CVModel
                cv_model = CVModel.objects.create(text_content=pdf_content['text'],etudiant=etudiant)

                # Enregistrement des images dans le modèle Image
                for image_data in pdf_content['images']:
                    # Convertir l'image en bytes
                    image_bytes = self.convert_image_to_bytes(image_data['image'])
                    Image.objects.create(cv_model=cv_model, size=image_data['size'], data=image_bytes)
                
                    # Appel à la méthode analyse_cv avec le contenu du PDF en argument
                    gemini_response = self.analyse_cv(cv_model.text_content)
                    print(gemini_response)

                    # Stocker les données du CV
                    self.stocker_donnees_cv(gemini_response, etudiant)

                return Response({'gemini_response': gemini_response})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('Aucun fichier PDF téléchargé.', status=status.HTTP_400_BAD_REQUEST)
        
    def extract_content_from_pdf(self, file):
        try:
            reader = PdfReader(file)
            content = {
                'text': '',
                'images': []
            }
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                # Extraction du texte de la page
                text = page.extract_text()
                if text:  # Vérifier si du texte a été extrait
                    content['text'] += text

                # Extraction des images de la page
                content['images'].extend(self.extract_images_from_page(page))
            return content
        except Exception as e:
            raise e

    def extract_images_from_page(self, page):
        images = []
        xObject = page['/Resources'].get('/XObject', None)
        if xObject:
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].get_object().get_data()
                    # Vérifier si les données binaires représentent une image valide
                    if self.is_valid_image(data):
                        # Convertir les données binaires de l'image en image lisible
                        image = self.open_image_from_bytes(data)
                        if image:
                            images.append({'size': size, 'image': image})
        return images

    def is_valid_image(self, data):
        try:
            # Ouvrir l'image à partir des données binaires pour vérifier si c'est une image valide
            PilImage.open(io.BytesIO(data))
            return True
        except (PilImage.UnidentifiedImageError, ValueError):
            return False

    def open_image_from_bytes(self, data):
        try:
            # Ouvrir l'image à partir des données binaires en spécifiant explicitement le format
            image_stream = io.BytesIO(data)
            image = PilImage.open(image_stream)
            return image
        except (PilImage.UnidentifiedImageError, ValueError):
            return None

    def convert_image_to_bytes(self, image):
        # Convertir l'image en bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')  # Correction ici: spécifier un format par défaut pour la sauvegarde
        return image_bytes.getvalue()
    
    def analyse_cv(self, cv_text):
      try:

        load_dotenv()  # Charge les variables d'environnement à partir de .env
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if gemini_api_key is None:
            raise ValueError("La clé API Gemini n'est pas définie dans les variables d'environnement.")

        genai.configure(api_key=gemini_api_key)

       

        # Configurer le modèle Gemini
        generation_config = {
           "temperature": 0.9,
           "top_p": 1,
           "top_k": 1,
           "max_output_tokens": 2048,
        }

        safety_settings = [
           {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
           {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
           {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
           {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]

        model = genai.GenerativeModel(
            model_name="gemini-1.0-pro",
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Démarrez une conversation avec le modèle Gemini
        convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["extraire tous  les donnes de ce text sous format json sans ```json et ``` comme nom ,prenom , formation ect \nFormation  : \n 2016 -2018  : master profession nel système  \nd’informatique sur  le web    \nUniversité  de Sousse  \n   \n 2013 -2016 : licence appliquée  en science \ninformatique   \nInstitut supérieur  d’informatique et des \ntechno logies de communication de Hamma m \nSousse  \n \n 2013  : baccalauréat  en science  \nLycée  Lamta , Monastir   \n \nExpérience  : \n 2020  : DEVELOPPEUR FRONT -END \nSENIOR  \n- Optimisation des fonctionnalités de la \nplateforme web  \n- Vision globale des objectifs \nd’accessibilité, d’attractivité, de \nréférencement, d’ergonomie et de \nlégitimit é \n \n \nLangages  info :  \nHTML / CSS 5.0        \nJS. (Node)  \nC++* \n \n \nLangues  : \n Arabe  : langue maternelle  \n Anglais  : lu , écrit  , parler  \n Français  : lu , écrit  , parler  \n \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n          \n \n                                             \n \n \n \n \n \n \n \n \n \n \n  \n \n \n \n \n \n \n \n \n©AZURIUS – Modelos -de-curriculum.com  Khaoula  \nDimassi  \n        27 315  712  \n \n \n        dimassikhaoula0 2@gmail.com   \n  \n \n       Bouhjar , Monastir  Developpeur web full stack  \nDétails  personnels  : \n- Sport  \n- Camping  \n- Cinéma   Loisirs  :  \n \n \n \n  \n- Prise de parole en public  \n- Gestion du trac  \n- Travail en group  Soft_skills :  \nTechnicien experimenté , passionné par \nl’univers ICT et son évolution croissante, \nj’ambitionne de mettre mes compétences au \nservice d’une entreprise à la culture \ninnovante, enthousiaste et audacieuse."]
  },
  {
    "role": "model",
    "parts": [
        "{",
        "    \"nom\": \"\",",
        "    \"prenom\": \"\",",
        "    \"profil\": \"\",",
        "    \"email\": \"\",",
        "    \"telephone\": \"\",",
        "    \"github\": \"\",",
        "    \"linkedin\": \"\",",
        "    \"skype\": \"\",",
        "    \"formations\": [",
        "        {",
        "            \"nomformation\": \"\",",
        "            \"etablissement\": \"\",",
        "            \"debutformation\": \"\",",
        "            \"finformation\": \"\"",
        "        },",
        "        {",
        "            \"nomformation\": \"\",",
        "            \"etablissement\": \"\",",
        "            \"debutformation\": \"\",",
        "            \"finformation\": \"\",",
        "        }",
        "    ],",
        "    \"projets\":  [",
        "     {",
        "        \"titreprojet\": \"\",",
        "        \"descriptionprojet\": \"\",",
        "        \"fichier_zip\": \"\",",

        "    },",
        "     ],",
        "    \"competences\": [",
        "        {",
        "            \"categorie\": \"\",",
        "            \"competence\": \"\",",
        "        }",
        "    ],",
        "    \"experiences\": [",
        "        {",
        "            \"titre\": \"\",",
        "            \"entreprise\": \"\",",
        "            \"debutexperience\": null,",
        "            \"finexperience\": null,",
        "            \"description\": \"\"",
        "        }",
        "    ],",
        "    \"clubs\": [",
        "        {",
        "            \"nomclub\": \"\",",
        "            \"role\": \"\"",
        "        },",
        "        {",
        "            \"nomclub\": \"\",",
        "            \"role\": \"\"",
        "        }",
        "    ],",
        "    \"softskills\": [",
        "        {",
        "            \"titreskills\": \"\"",
        "        },",
        "     ],", 
        "    \"centresdinteret\": [",
        "        {",
        "            \"titreInteret\": \"\",",
        "        },",
        "     ],", 
        "    \"langues\": {",
        "        \"Arabe\": \"\",",
        "        \"Anglais\": \"\",",
        "        \"Français\": \"\"",
        "    },",
        "    \"references\": [",
        "        {",
        "            \"titreref\": \"\",",
        "            \"poste\": \"\",",
        "            \"emailref\": \"\""
        "        }",
        "    ],",        
    ]  },
])

        # Envoyez le contenu du dernier CV au modèle Gemini
        convo.send_message(cv_text)

        

        # Récupérer et retourner la dernière réponse du modèle Gemini
        return convo.last.text
      

      except Exception as e:
            # Gérez les erreurs potentielles
            print("Une erreur s'est produite lors de l'analyse du CV:", e)

    
    def stocker_donnees_cv(self, data,etudiant):
      try:
        # Convertir la chaîne de caractères JSON en dictionnaire
        data_dict = json.loads(data)
        

        # Création de l'objet InfoPersonnelles
        info_personnelles = InfoPersonnelles.objects.create(
            etudiant=etudiant,
            nom=data_dict.get('nom', ''),
            prenom=data_dict.get('prenom', ''),
            profil=data_dict.get('profil', ''),
            email=data_dict.get('email', ''),
            telephone=data_dict.get('telephone', ''),
            github=data_dict.get('github', ''),
            linkedin=data_dict.get('linkedin', ''),
            skype=data_dict.get('skype', ''),
        )

        # Insérez les formations
        for formation_data in data_dict['formations']:
            debutformation = formation_data.get('debutformation') if formation_data.get('debutformation') is not None and formation_data.get('debutformation') != 'null' else None
            finformation = formation_data.get('finformation') if formation_data.get('finformation') is not None and formation_data.get('finformation') != 'null' else None
            Formation.objects.create(
                info=info_personnelles,
                nomformation=formation_data['nomformation'],
                etablissement=formation_data['etablissement'],
                debutformation=debutformation,
                finformation=finformation
            )

        for competence_data in data_dict['competences']:
            Competence.objects.create(
                info=info_personnelles,
                categorie=competence_data['categorie'],
                competence=competence_data['competence']
    )
  

        # Insérez les expériences
        for experience_data in data_dict['experiences']:
            Experience.objects.create(
                info=info_personnelles,
                titre=experience_data['titre'],
                entreprise=experience_data['entreprise'],
                debutexperience=experience_data['debutexperience'],
                finexperience=experience_data['finexperience'],
                description=experience_data['description']
            )

            

        # Insérez les clubss
        for club_data in data_dict['clubs']:
            Club.objects.create(
                info=info_personnelles,
                nomclub=club_data['nomclub'],
                role=club_data['role'],
            )

        # Insérez les softskills
        for skills_data in data_dict['softskills']:
            SoftSkills.objects.create(
                info=info_personnelles,
                titreskills=skills_data['titreskills'],
            )

        # Insérez les Centres d'interet
        for interet_data in data_dict['centresdinteret']:
            CentresDinteret.objects.create(
                info=info_personnelles,
                titreInteret=interet_data['titreInteret'],
            )

        # Insérez les langues
        for langue, niveau in data_dict['langues'].items():
            Langue.objects.create(
                info=info_personnelles,
                langue=langue,
                niveau=niveau
            )

        # Insérez les references
        for reference_data in data_dict['references']:
            Reference.objects.create(
                info=info_personnelles,
                titreref=reference_data['titreref'],
                poste=reference_data['poste'],
                emailref=reference_data['emailref'],
            )

        # Insérez les projets
        for projet_data in data_dict['projets']:
            Projets.objects.create(
              info=info_personnelles,
              titreprojet = projet_data['titreprojet'],
              descriptionprojet = projet_data['descriptionprojet'],
              fichier_zip = projet_data['fichier_zip'],

              
              )
    
       


        print("Données du CV enregistrées avec succès dans la base de données.")

      except Exception as e:
        print("Une erreur s'est produite lors de l'enregistrement des données du CV :", e)

class GetLastImage(APIView):
    def get(self, request, etudiant_id):
        try:
            # Récupérer le dernier CVModel de l'étudiant
            dernier_cvmodel = CVModel.objects.filter(etudiant_id=etudiant_id).latest('id')
        except CVModel.DoesNotExist:
            return JsonResponse({'error': f'No CVModel found for the student with ID {etudiant_id}'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            # Récupérer la dernière image associée au dernier CVModel de l'étudiant
            last_image = Image.objects.filter(cv_model=dernier_cvmodel).latest('id')
            # Renvoyer les données de l'image en tant que réponse HTTP
            return HttpResponse(last_image.data, content_type='image/jpeg')  # ou tout autre format approprié
        except Image.DoesNotExist:
            return JsonResponse({'error': f'No images found for the student with ID {etudiant_id}'}, status=status.HTTP_404_NOT_FOUND)


class GetLastInformations(APIView):
    def get(self, request,etudiant_id):
        try:
            etudiant = Etudiant.objects.get(pk=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant does not exist"}, status=status.HTTP_404_NOT_FOUND)
        try:
            # Récupérer le dernier ID des informations personnelles
            dernier_info_personnelles = InfoPersonnelles.objects.filter(etudiant=etudiant).latest('id')
            dernier_id = dernier_info_personnelles.id

            # Récupérer toutes les formations associées au dernier ID des informations personnelles
            info_formations = Formation.objects.filter(info_id=dernier_id)

            # Récupérer toutes les experiences associées au dernier ID des informations personnelles
            info_experiences = Experience.objects.filter(info_id=dernier_id)

            # Récupérer toutes les references associées au dernier ID des informations personnelles
            info_references = Reference.objects.filter(info_id=dernier_id)


            # Récupérer toutes les references associées au dernier ID des informations personnelles
            info_langues = Langue.objects.filter(info_id=dernier_id)

            # Récupérer toutes les Centres d'interet associées au dernier ID des informations personnelles
            info_interet = CentresDinteret.objects.filter(info_id=dernier_id)


            # Récupérer toutes les competences associées au dernier ID des informations personnelles
            info_competence = Competence.objects.filter(info_id=dernier_id)

            # Récupérer toutes les softskills associées au dernier ID des informations personnelles
            info_skills = SoftSkills.objects.filter(info_id=dernier_id)

            # Récupérer toutes les projets associées au dernier ID des informations personnelles
            info_projets = Projets.objects.filter(info_id=dernier_id)

             # Récupérer toutes les clubs associées au dernier ID des informations personnelles
            info_clubs = Club.objects.filter(info_id=dernier_id)



            # Préparer les données des formations
            formations_data = []
            for formation in info_formations:
                formations_data.append({
                    'nomformation': formation.nomformation,
                    'etablissement': formation.etablissement,
                    'debutformation': formation.debutformation,
                    'finformation': formation.finformation,
                })

            # Préparer les données des experiences
            experiences_data = []
            for experience in info_experiences:
                experiences_data.append({
                    'titre': experience.titre,
                    'entreprise': experience.entreprise,
                    'debutexperience': experience.debutexperience,
                    'finexperience': experience.finexperience,
                    'description': experience.description,

                })

            # Préparer les données des references
            references_data = []
            for reference in info_references:
                references_data.append({
                    'titreref': reference.titreref,
                    'poste': reference.poste,
                    'emailref': reference.emailref,

                })

            # Préparer les données des langues
            langues_data = []
            for langue in info_langues:
                langues_data.append({
                    'langue': langue.langue,
                    'niveau': langue.niveau,

                })

                  # Préparer les données des langues
            Clubs_data = []
            for club in info_clubs:
                Clubs_data.append({
                    'nomclub': club.nomclub,
                    'role': club.role,

                })


            # Préparer les données des Centres d'interet
            interet_data = []
            for interet in info_interet:
                interet_data.append({
                    'titreInteret': interet.titreInteret,
                })

             # Préparer les données des Competences
            competence_data = []
            for competence in info_competence:
                competence_data.append({
                    'categorie': competence.categorie,
                    'competence': competence.competence,

                })
            

            # Préparer les données des softskills
            skills_data = []
            for skills in info_skills:
                skills_data.append({
                    'titreskills': skills.titreskills,
                })

            
            projets_data = []
            for projet in info_projets:
                fichier_zip = projet.fichier_zip
                if fichier_zip and fichier_zip.name:  # Vérifie si le fichier ZIP est présent
                    projets_data.append({
                        'titreprojet': projet.titreprojet,
                        'descriptionprojet': projet.descriptionprojet,
                        'fichier_zip': fichier_zip.name,  # Utilise 'name' pour obtenir le nom du fichier
                        })
                else:
                    projets_data.append({
                        'titreprojet': projet.titreprojet,
                        'descriptionprojet': projet.descriptionprojet,
                        'fichier_zip': None,  # Indique qu'il n'y a pas de fichier ZIP
                })
                    print("No file associated with 'fichier_zip' for projet with titreprojet:", projet.titreprojet)




            # Préparer les données à envoyer
            data = {
                'nom': dernier_info_personnelles.nom,
                'prenom': dernier_info_personnelles.prenom,
                'profil': dernier_info_personnelles.profil,
                'email': dernier_info_personnelles.email,
                'telephone': dernier_info_personnelles.telephone,
                'github': dernier_info_personnelles.github,
                'linkedin': dernier_info_personnelles.linkedin,
                'skype': dernier_info_personnelles.skype,
                'formations': formations_data,  # Ajout des formations
                'experiences':  experiences_data,  # Ajout des experiences
                'references':references_data,
                'langues':langues_data,
                'interets':interet_data,
                'competences':competence_data,
                'softskills':skills_data,
                'projets':projets_data,
                'clubs':Clubs_data,



                

            }
            return Response(data, status=status.HTTP_200_OK)
        except InfoPersonnelles.DoesNotExist:
            return Response({'error': 'Aucune donnée n\'est disponible.'}, status=status.HTTP_404_NOT_FOUND)

class stocknewInformations(APIView):
    def post(self, request, etudiant_id):
        try:
            etudiant = Etudiant.objects.get(pk=etudiant_id)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Récupérer le dernier objet InfoPersonnelles associé à l'étudiant
            dernier_info_personnelles = InfoPersonnelles.objects.filter(etudiant=etudiant).latest('id')

            # Récupérer le profil mis à jour depuis les données envoyées
            profil = request.data.get('profil', dernier_info_personnelles.profil)

            # Mettre à jour le champ 'profil' de l'objet InfoPersonnelles
            dernier_info_personnelles.profil = profil
            dernier_info_personnelles.save()

            # Récupérer les données des formations
            formations_data = request.data.get('formations', [])
            
            # Supprimer toutes les formations existantes associées à l'étudiant
            Formation.objects.filter(info_id=dernier_info_personnelles.id).delete()

            # Récupérer les données des experiences
            experiences_data = request.data.get('experiences', [])
            
            # Supprimer toutes les experiences existantes associées à l'étudiant
            Experience.objects.filter(info_id=dernier_info_personnelles.id).delete()


            # Récupérer les données des competences
            competences_data = request.data.get('competences', [])
            # Supprimer toutes les competences existantes associées à l'étudiant
            Competence.objects.filter(info_id=dernier_info_personnelles.id).delete()

            skills_data = request.data.get('softskills', [])
            SoftSkills.objects.filter(info_id=dernier_info_personnelles.id).delete()

            centreinteret_data = request.data.get('interets', [])
            CentresDinteret.objects.filter(info_id=dernier_info_personnelles.id).delete()

            langues_data = request.data.get('langues', [])
            Langue.objects.filter(info_id=dernier_info_personnelles.id).delete()

            references_data = request.data.get('references', [])
            Reference.objects.filter(info_id=dernier_info_personnelles.id).delete()
            existing_references = set()

            clubs_data = request.data.get('clubs', [])
            Club.objects.filter(info_id=dernier_info_personnelles.id).delete()
            existing_clubs = set()

            projets_data = request.data.get('projets', [])
            Projets.objects.filter(info_id=dernier_info_personnelles.id).delete()

            
            # Enregistrer les nouvelles formations
            for formation_data in formations_data:
                Formation.objects.create(
                    info_id=dernier_info_personnelles.id,
                    nomformation=formation_data.get('nomformation', ''),
                    etablissement=formation_data.get('etablissement', ''),
                    debutformation=formation_data.get('debutformation', None),
                    finformation=formation_data.get('finformation', None)
                )

            # Enregistrer les nouvelles expériences professionnelles
            for experience_data in experiences_data:
                Experience.objects.create(
                    info_id=dernier_info_personnelles.id,
                    titre=experience_data.get('titre', ''),
                    entreprise=experience_data.get('entreprise', ''),
                    debutexperience=experience_data.get('debutexperience', None),
                    finexperience=experience_data.get('finexperience', None),
                    description=experience_data.get('description', '')
                )

                  # Enregistrer les nouvelles competences
            for competence_data in competences_data:
                Competence.objects.create(
                    info_id=dernier_info_personnelles.id,
                    categorie=competence_data.get('categorie', ''),
                    competence=competence_data.get('competence', ''),
                
                )

            for skill_data in skills_data:
                SoftSkills.objects.create(
                    info_id=dernier_info_personnelles.id,
                    titreskills=skill_data.get('titreskills', ''),
                
                )

            for centreinterett_data in centreinteret_data:
                CentresDinteret.objects.create(
                    info_id=dernier_info_personnelles.id,
                    titreInteret=centreinterett_data.get('titreInteret', ''),
                
                )


            for langue_data in langues_data:
                Langue.objects.create(
                    info_id=dernier_info_personnelles.id,
                    langue=langue_data.get('langue', ''),
                    niveau=langue_data.get('niveau', ''),

                
                )


            for reference_data in references_data:
             titreref = reference_data.get('titreref', '')
             poste = reference_data.get('poste', '')
             emailref = reference_data.get('emailref', '')
             if (titreref, poste, emailref) not in existing_references:
                Reference.objects.create(
                    info_id=dernier_info_personnelles.id,
                    titreref=titreref,
                    poste=poste,
                    emailref=emailref
                    )
                existing_references.add((titreref, poste, emailref))  # Ajouter la référence à l'ensemble existing_references

                 
            for club_data in clubs_data:
             nomclub = club_data.get('nomclub', '')
             role = club_data.get('role', '')
             if (nomclub, role) not in existing_clubs:
                Club.objects.create(
                    info_id=dernier_info_personnelles.id,
                    nomclub=nomclub,
                    role=role,
                    )
                existing_clubs.add((nomclub, role))  


            for projet_data in projets_data:
                titreprojet = projet_data.get('titreprojet', '')
                descriptionprojet = projet_data.get('descriptionprojet', '')
    
                 # Vérifiez si un fichier zip est associé aux données du projet
                fichier_zip = projet_data.get('fichier_zip')
                if fichier_zip:
                              # Si un fichier zip est présent, créez l'objet Projets avec le fichier associé
                    Projets.objects.create(
                        info_id=dernier_info_personnelles.id,
                        titreprojet=titreprojet,
                        descriptionprojet=descriptionprojet,
                        fichier_zip=fichier_zip,
                        )
                else:
        # Si aucun fichier zip n'est présent, créez l'objet Projets sans le fichier
                    Projets.objects.create(
                        info_id=dernier_info_personnelles.id,
                        titreprojet=titreprojet,
                        descriptionprojet=descriptionprojet,
        )

                
        
            # Vous pouvez également renvoyer une réponse indiquant que la mise à jour a réussi
            return Response({'message': 'Profil, formations et expériences professionnelles mis à jour avec succès!'}, status=status.HTTP_200_OK)
        except InfoPersonnelles.DoesNotExist:
            return Response({'error': 'Aucune donnée n\'est disponible.'}, status=status.HTTP_404_NOT_FOUND)