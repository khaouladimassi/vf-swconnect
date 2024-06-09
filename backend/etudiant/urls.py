from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register ("api/etudiant",views.EtudiantViewSet , basename="etudiant")
urlpatterns = router.urls