# Create your views here.
import json
import urllib2
from django.core.cache import cache
from django.http import HttpResponse
from weather.models import Location

weatherBaseURL = "http://api.openweathermap.org/data/2.5/weather?"
weatherFormat = "units=metric&"

weatherURL = weatherBaseURL + weatherFormat

def currentTemp():
    #cache.clear()
    latitude = Location.objects.all()[0].latitude
    longitude = Location.objects.all()[0].longitude

    queryURL = weatherURL + "lat=" + str(latitude) + "&lon=" + str(longitude)
    response = urllib2.urlopen(queryURL)

    decoder = json.JSONDecoder()
    temperature = decoder.decode(response.read())["main"]["temp"]

    return (str(temperature) + " Degrees")

def currentTempByLatLon(latitude, longitude):

    queryURL = weatherURL + "lat=" + str(latitude) + "&lon=" + str(longitude)
    response = urllib2.urlopen(queryURL)

    decoder = json.JSONDecoder()
    temperature = decoder.decode(response.read())["main"]["temp"]

    return (str(temperature) + " Degrees")