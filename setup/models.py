from django.db import models

class Setup(models.Model):
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    cityID = models.IntegerField()
    
    googleID = models.CharField(max_length=100)
    calendarName = models.CharField(max_length=100)
    
    precipitationLimit = models.IntegerField()
    precipitationTime = models.IntegerField()