from rest_framework.routers import DefaultRouter
from .views import DimInsuredViewSet, DimIncidentViewSet, FactClaimsViewSet

router = DefaultRouter()
router.register(r'insured', DimInsuredViewSet)
router.register(r'incidents', DimIncidentViewSet)
router.register(r'claims', FactClaimsViewSet)

urlpatterns = router.urls