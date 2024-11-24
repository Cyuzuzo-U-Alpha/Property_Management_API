from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OwnerViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = router.urls
