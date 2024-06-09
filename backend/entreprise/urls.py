from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register ("api/entreprise",views.EntrepriseViewSet , basename="entreprise")
urlpatterns = router.urls