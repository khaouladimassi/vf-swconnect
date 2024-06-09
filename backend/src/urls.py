"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from CV.views import UploadPDF , GetLastImage ,GetLastInformations,stocknewInformations
from accounts.views import LoginView, LogoutView,GetUserById,GetUserByUsername,NewUsersPerMonthView
from adminsite.views import GetAdmin,AdminUpdateView,GetAdmins
from entreprise.views import GetEntrepriseById,DeleteEntreprise,AllEntreprise,EntrepriseUpdateView,verify,TotalEntreprises,GetCompanyByMc
from etudiant.views import EtudiantCreateView, GetEtudiantById,AllEtudiant,EtudiantUpdateView,block,unblock,GetEtudByMc,FilteredEtudAPIView,TotalEtudiants,DeleteEtudiant
from offer.views import DeleteOffer, GetAllOffers, GetOfferById, OfferCreateView, UpdateOffer,getOffersByEntreprise,GetOffersByMc,FilteredOfferAPIView,GetTotalOffersByEntreprise,RecentOffersView,TopOffersView,OffersPerMonthView,OffersSummaryView
from pfebook.views import PfebookCreateView,getAllBook,getBookByEnt,getBookById,updateBook,deleteBook,GetpfebookByMc
from drive.views import CreerFichierView,AfficherFichierView,SupprimerFichierView,OuvrirFichierView,GetFileView
from FavorisOffre.views import AddFavoris,GetFavoris,DeleteFavoris,GetFavorisById
from FavorisEntreprise.views import AddFavoriss,GetFavoriss,DeleteFavoriss,GetFavorissById
from demande.views import AddDemande,GetDemandeById,GetDemandeByEtudiant,GetDemandeByOffer,DeleteDemande,SetAccepted,SetRefused,GetDemandeByOfferEtudiant,DemandeStats,CandidatureFrequencyView,TopCompaniesView,TopDomainsView,TopSkillsView,TotalDemandsByEntrepriseView
from historique.views import UserActionCreateView,get_all_actions,search_by_mc
from boitemessagerie.views import SendMessage,DeleteMessage,SeenMessage,GetMessagesBetweenUsers,GetRecipientOrSender
from apparitionprofil.views import EnregistrerApparitionProfil ,ApparitionProfilParSemaine
from book.views import CreateBookView,GetPfeBookByEntrepriseView,UpdateBookView,BookDetailView,Delete
from template.views import StockTemplateView ,OuvrirTemplateView
from notif_etud.views import StockNotifEtud,GetNotifByEtudiant
from notif_entre.views import StockNotifEntre,GetNotifByEntreprise
from notif_admin.views import StockNotifAdmin ,GetNotifByAdmin



urlpatterns= [
    path('api/create-book/', CreateBookView.as_view(), name='create-book'),
    path('api/get-pfe-book-by-entreprise/<int:entreprise_id>/', GetPfeBookByEntrepriseView.as_view(), name='get-pfe-book-by-entreprise'),
    path('api/update-book/<int:book_id>/', UpdateBookView.as_view(), name='update-book'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
        path('api/book/<int:book_id>/', Delete.as_view(), name='book-delete'),





 path('api/message/get_messages_between_users/<int:sender_id>/<int:receiver_id>/',GetMessagesBetweenUsers.as_view(),name='get_messages_between_users'),
path('api/message/<int:sender_id>/send/<int:recipient_id>/',SendMessage.as_view(),name='send_message'),
path('delete_message/<int:message_id>/', DeleteMessage.as_view(), name='delete_message'),
    path('api/message/seen_message/<int:user_id>/', SeenMessage.as_view(), name='seen_message'),
    path('api/message/get_recipient_or_sender/<int:user_id>/', GetRecipientOrSender.as_view(), name='get_recipient_or_sender'),

path('api/demande/<int:etudiant_id>/add/<int:offer_id>/',AddDemande.as_view(),name='add_demande'),
path('api/demande/<int:etudiant_id>/get/<int:offer_id>/',GetDemandeByOfferEtudiant.as_view(),name='get_demande_by _both'),
path('api/demande/get/<int:demande_id>/',GetDemandeById.as_view(),name='get_demande'),
path('api/demande/offer/<int:offer_id>/', GetDemandeByOffer.as_view(), name='get_demande_by_offer'),
path('api/demande/etudiant/<int:etudiant_id>/', GetDemandeByEtudiant.as_view(), name='get_demande_by_etudiant'),
 path('api/demande/<int:demande_id>/delete/', DeleteDemande.as_view(), name='delete_demande'),
 path('api/demande/<int:demande_id>/setAccepted/', SetAccepted.as_view(), name='set_accepted'),
path('api/demande/<int:demande_id>/setRefused/', SetRefused.as_view(), name='set_refused'),



path('api/etudiant/<int:etudiant_id>/addFavoris/<int:offer_id>/',AddFavoris.as_view(),name='add_favoris_offre'),
path('api/etudiant/<int:etudiant_id>/getFavoris/',GetFavoris.as_view(),name='get_favoris_offre'),
path('api/etudiant/deleteFavoris/<int:favorite_offer_id>/',DeleteFavoris.as_view(),name='delete_favoris_offre'),
path('api/etudiant/getbyidFavoris/<int:favorite_offer_id>/',GetFavorisById.as_view(),name='get_favorite'),

path('api/entreprise/<int:entreprise_id>/addFavoriss/<int:etudiant_id>/',AddFavoriss.as_view(),name='add_favoris_etudiant'),
path('api/entreprise/<int:entreprise_id>/getFavoriss/',GetFavoriss.as_view(),name='get_favoris_etudiant'),
path('api/entreprise/deleteFavoriss/<int:favorite_etudiant_id>/',DeleteFavoriss.as_view(),name='delete_favoris_etudiant'),
path('api/entreprise/getbyidFavoriss/<int:favorite_offer_id>/',GetFavorissById.as_view(),name='get_favorites'),


path('api/Etudbymc/', GetEtudByMc.as_view(), name='get_etuds_by_mc'),
path('api/etuds/filter/<str:domain>/<str:education>/', FilteredEtudAPIView.as_view(), name='filtered_etuds_api'),




    path('api/offer/<int:offer_id>/', GetOfferById.as_view(), name='get_offer_by_id'),
    path('api/offers/', GetAllOffers.as_view(), name='get_all_offers'),
    path('api/entreprise/<int:entreprise_id>/update/<int:offer_id>/', UpdateOffer.as_view(), name='update_offer'),
    path('api/offer/delete/<int:offer_id>/', DeleteOffer.as_view(), name='delete_offer'),
    path('api/offers/entreprise/<int:entreprise_id>/', getOffersByEntreprise.as_view(), name='get_offers_byent'),

    path('', include('accounts.urls')),       # URL de l'application 
     path('api/login/', LoginView.as_view(), name='login'),
    path('api/get_user/<int:pk>/', GetUserById.as_view(), name='get_user'),
     path('api/get_user_username/<str:username>/', GetUserByUsername.as_view(), name='get_username'),
      path('api/logout/', LogoutView.as_view(), name='logout'),
    path('', include('etudiant.urls')),       # URL de l'application 'etudiant'

    path('api/etudiants/getall/', AllEtudiant.as_view(), name='etudiant-list'),
    path('api/etudiants/get/<int:pk>/', GetEtudiantById.as_view(), name='etudiant-detail'),
     path('api/etudiants/delete/<int:pk>/', DeleteEtudiant.as_view(), name='etudiant-delete'),
    path('api/etudiants/create', EtudiantCreateView.as_view(), name='etudiant-create'),
    path('api/etudiants/update/<int:pk>/', EtudiantUpdateView.as_view(), name='etudiant-update'),
    path('api/etudiants/block/<int:pk>/', block.as_view(), name='etudiant-block'),
    path('api/etudiants/unblock/<int:pk>/', unblock.as_view(), name='etudiant-unblock'),


    path('', include('entreprise.urls')),  # URL de l'application 'entreprise'
    path('api/entreprises/getall/', AllEntreprise.as_view(), name='entreprise-list'),
    path('api/entreprises/get/<int:pk>/', GetEntrepriseById.as_view(), name='entreprise-detail'),
     path('api/entreprises/delete/<int:pk>/', DeleteEntreprise.as_view(), name='entreprise-delete'),
    path('api/entreprises/update/<int:pk>/', EntrepriseUpdateView.as_view(), name='entreprise-update'),
    path('api/entreprise/<int:pk>/verify/', verify.as_view(), name='verify-entreprise'),

      path('api/entreprise/<int:company_id>/offers/', OfferCreateView.as_view(), name='offer-create'),

      path('api/entreprise/<int:company_id>/pfebook/', PfebookCreateView.as_view(), name='pfebook-create'),
      path('api/pfebook/entreprise/<int:entreprise_id>/', getBookByEnt.as_view(), name='  Pfebook-get-byent'),
      path('api/pfebook/<int:pk>/', getBookById.as_view(), name='  Pfebook-get-byId'),
      path('api/pfebooks/',getAllBook.as_view(), name='  Pfebook-get-all'),
      path('api/pfebook/delete/<int:pk>/', deleteBook.as_view(), name='  Pfebook-delete'),
      path('api/entreprise/<int:entreprise_id>/update/pfebook/<int:pk>/', updateBook.as_view(), name='  Pfebook-update'),


    path("admin/", admin.site.urls),          # URL de l'administration Django
    path("api/admin/<int:pk>/",GetAdmin.as_view(), name='admin-details'),
    path("api/admin/",GetAdmins.as_view(), name='admin-alls'),
    path("api/admin/update/<int:pk>/",AdminUpdateView.as_view(), name='admin-update'),
    


    path('api-auth/', include('rest_framework.urls')),  # URL pour l'authentification de l'API Django REST Framework
    path('api/upload-pdf/', UploadPDF.as_view(), name='uploaded-file'),
    path('get-last-image/', GetLastImage.as_view(), name='get_last_image'),
    path('get-last-info/', GetLastInformations.as_view(), name='get_last_info'),

    path('get-last-image/<int:etudiant_id>/', GetLastImage.as_view(), name='get_last_image'),
    path('get-last-info/<int:etudiant_id>', GetLastInformations.as_view(), name='get_last_info'),

    path('creer-fichier/<int:user_id>', CreerFichierView.as_view(), name='creer_fichier'),
    path('get-all-fichiers/<int:user_id>', AfficherFichierView.as_view(), name='get_all_fichiers'),
    path('supprimer-fichier/<int:pk>/<int:user_id>', SupprimerFichierView.as_view(), name='supprimer_fichier'),
    path('servir-fichier/<int:fichier_id>/', OuvrirFichierView.as_view(), name='servir_fichier'),
    path('api/get-file/<path:file_path>/', GetFileView.as_view(), name='get-file'),

    path('api/offersbymc/', GetOffersByMc.as_view(), name='get_offers_by_mc'),
    path('api/pfebooksbymc/', GetpfebookByMc.as_view(), name='get_offers_by_mc'),
    path('api/offers/filter/<str:domain>/<str:stage_type>/<str:binome>/<int:min_price>/', FilteredOfferAPIView.as_view(), name='filtered_offers_api'),

    path('creer-action/<int:user_id>/', UserActionCreateView.as_view(), name='creer_action'),
    path('get-all-actions/<int:user_id>/', get_all_actions, name='get_all_actions'),
    path('search_by_mc/<str:keyword>/', search_by_mc, name='search-by-mc'),




    path('demande/stats/<int:etudiant_id>/', DemandeStats.as_view(), name='demande-stats'),

    path('apparition_profil/<int:etudiant_id>/', EnregistrerApparitionProfil.as_view(), name='enregistrer_apparition_profil'),
    path('apparition_profil/semaine/<int:etudiant_id>/', ApparitionProfilParSemaine.as_view(), name='apparition_profil_semaine'),

    path('api/candidature/frequency/<int:etudiant_id>/', CandidatureFrequencyView.as_view(), name='candidature_frequency'),
    path('api/top-companies/', TopCompaniesView.as_view(), name='top_companies'),
    path('api/top-domaines/', TopDomainsView.as_view(), name='top_domains'),
    path('top-skills/<str:domain>/', TopSkillsView.as_view(), name='top_skills'),



    path('entreprise/<int:entreprise_id>/total_offers/', GetTotalOffersByEntreprise.as_view(), name='get_total_offers_by_entreprise'),
    path('entreprise/<int:entreprise_id>/total_demands/', TotalDemandsByEntrepriseView.as_view(), name='total_demands_by_entreprise'),
    path('entreprise/<int:entreprise_id>/recent_offers/', RecentOffersView.as_view(), name='recent_offers'),
    path('entreprise/<entreprise_id>/top_offers/',TopOffersView.as_view(),name='top_offers'),
    path('entreprise/<entreprise_id>/offers_per_month/',OffersPerMonthView.as_view(),name='top_offers'),

    path('totalentreprise/',TotalEntreprises.as_view(),name='all_companies'),
    path('totaletudiants/',TotalEtudiants.as_view(),name='all_students'),

    path('api/users_per_month/', NewUsersPerMonthView.as_view(), name='users_per_month'),
    path('api/offers_summary/', OffersSummaryView.as_view(), name='offers_summary'),
    


    path('api/entreprisesbymc/', GetCompanyByMc.as_view(), name='get_entreprises_by_mc'),


    path('creer-notif/<int:demande_id>/', StockNotifEtud.as_view(), name='notification-create'),
    path('notifications/<int:etudiant_id>/', GetNotifByEtudiant.as_view(), name='get_notifications_by_etudiant'),
    path('creer-notif-entre/<int:offer_id>/', StockNotifEntre.as_view(), name='notification-create'),
    path('notificationsEntre/<int:entreprise_id>/', GetNotifByEntreprise.as_view(), name='notifications_entreprise'),


    path('creer-notif-admin/', StockNotifAdmin.as_view(), name='notification-create'),
    path('notificationsAdmin/', GetNotifByAdmin.as_view(), name='notifications_entreprise'),
    
    
    path('stock-informations/<int:etudiant_id>/', stocknewInformations.as_view(), name='stock_informations'),
    path('stock-template/<int:user_id>/', StockTemplateView.as_view(), name='stock-template'),
    path('get-all-templates/<int:user_id>/', OuvrirTemplateView.as_view(), name='get_all_templates'),

]


 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)