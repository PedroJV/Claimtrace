from django.db import models


class DimInsured(models.Model):
    insured_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    months_as_customer = models.IntegerField()
    insured_sex = models.CharField(max_length=10)
    insured_education_level = models.CharField(max_length=50)
    insured_occupation = models.CharField(max_length=50)
    insured_hobbies = models.CharField(max_length=50)
    insured_relationship = models.CharField(max_length=50)

    class Meta:
        db_table = 'dim_insured'
        managed = False


class DimIncident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    incident_date = models.DateField()
    incident_type = models.CharField(max_length=50)
    collision_type = models.CharField(max_length=50, null=True)
    incident_severity = models.CharField(max_length=50)
    authorities_contacted = models.CharField(max_length=50, null=True)
    incident_state = models.CharField(max_length=10)
    incident_city = models.CharField(max_length=50)

    class Meta:
        db_table = 'dim_incident'
        managed = False


class FactClaims(models.Model):
    claim_id = models.AutoField(primary_key=True)
    insured = models.ForeignKey(DimInsured, on_delete=models.DO_NOTHING, db_column='insured_id')
    incident = models.ForeignKey(DimIncident, on_delete=models.DO_NOTHING, db_column='incident_id')
    policy_number = models.IntegerField()
    policy_bind_date = models.DateField()
    policy_state = models.CharField(max_length=10)
    policy_annual_premium = models.DecimalField(max_digits=10, decimal_places=2)
    auto_make = models.CharField(max_length=50)
    auto_model = models.CharField(max_length=50)
    auto_year = models.IntegerField()
    total_claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    injury_claim = models.DecimalField(max_digits=10, decimal_places=2)
    property_claim = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_claim = models.DecimalField(max_digits=10, decimal_places=2)
    capital_gains = models.DecimalField(max_digits=10, decimal_places=2)
    capital_loss = models.DecimalField(max_digits=10, decimal_places=2)
    days_policy_to_incident = models.IntegerField()
    is_date_anomaly = models.BooleanField()
    fraud_reported = models.CharField(max_length=5)

    class Meta:
        db_table = 'fact_claims'
        managed = False