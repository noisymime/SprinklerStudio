# Create your views here.
import json
import urllib2
from django.core.cache import cache
from django.http import HttpResponse
from weather.models import Location

weatherURL = "http://api.openweathermap.org/data/2.5/weather?"

def index(request):
    #cache.clear()
    latitude = Location.objects.all()[0].latitude
    longitude = Location.objects.all()[0].longitude

    queryURL = weatherURL + "lat=" + str(latitude) + "&lon=" + str(longitude)
    response = urllib2.urlopen(queryURL)

    decoder = json.JSONDecoder()
    data = decoder.decode(response.read())

    return HttpResponse("Latitude: " + str(data))

