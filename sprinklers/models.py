from django.db import models

# Create your models here.
class Sprinkler(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    enabled = models.BooleanField()
    status = models.BooleanField(default=False)
    isMaster = models.BooleanField(default=False)
    currentLog = models.IntegerField(null=True, blank=True) #If the sprinkler is on, this variable contains the active log entry so it can be ended when it's turned off

class LogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    sprinkler_id = models.IntegerField()
    timeOn = models.DateTimeField(auto_now_add=True)
    timeOff = models.DateTimeField(auto_now=True)
