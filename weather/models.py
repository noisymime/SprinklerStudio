from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    cityID = models.CharField(max_length=8)
    
