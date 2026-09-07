from rest_framework import serializers
from .models import DimInsured, DimIncident, FactClaims


class DimInsuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimInsured
        fields = '__all__'


class DimIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimIncident
        fields = '__all__'


class FactClaimsSerializer(serializers.ModelSerializer):
    insured = DimInsuredSerializer(read_only=True)
    incident = DimIncidentSerializer(read_only=True)

    class Meta:
        model = FactClaims
        fields = '__all__'