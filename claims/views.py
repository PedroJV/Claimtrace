from rest_framework import viewsets
from .models import DimInsured, DimIncident, FactClaims
from .serializers import DimInsuredSerializer, DimIncidentSerializer, FactClaimsSerializer


class DimInsuredViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DimInsured.objects.all()
    serializer_class = DimInsuredSerializer


class DimIncidentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DimIncident.objects.all()
    serializer_class = DimIncidentSerializer


class FactClaimsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FactClaims.objects.all()
    serializer_class = FactClaimsSerializer