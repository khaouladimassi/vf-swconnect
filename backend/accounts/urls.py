from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/accounts",views.CustomUserViewSet , basename="customuser")
urlpatterns = router.urls