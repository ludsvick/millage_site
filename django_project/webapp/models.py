from django.db import models

class County(models.Model):
    county_name = models.CharField(max_length=75)
    county_millage = models.DecimalField(max_digits=6, decimal_places=4)

class Municipality(models.Model):
    municipality_name = models.CharField(max_length=100)
    municipality_millage = models.DecimalField(max_digits=6, decimal_places=4)
    municipality_county = models.ForeignKey('County', on_delete = models.CASCADE)
    municipality_district = models.ForeignKey('District', on_delete = models.CASCADE)

class District(models.Model):
    district_name = models.CharField(max_length=100)
    district_millage = models.DecimalField(max_digits=7, decimal_places=4)
