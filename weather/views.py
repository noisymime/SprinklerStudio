# Create your views here.
import json
import urllib2
from django.core.cache import cache
from django.http import HttpResponse
from weather.models import Location
from django.template import Context, loader
from weather import WeatherUtils

weatherURL = "http://api.openweathermap.org/data/2.5/weather?"

def index(request):
    #cache.clear()
    latitude = Location.objects.all()[0].latitude
    longitude = Location.objects.all()[0].longitude

    queryURL = weatherURL + "lat=" + str(latitude) + "&lon=" + str(longitude)
    response = urllib2.urlopen(queryURL)

    decoder = json.JSONDecoder()
    data = decoder.decode(response.read())

    template = loader.get_template('weather/index.html')
    context = Context({
        'latitude': latitude,
    })
    return HttpResponse(template.render(context))

def ajax(request):

    latitude = request.GET['lat'] # request.POST.get('lat', False)
    longitude = request.GET['lon'] # request.POST.get('lat', False)
    
    temperature = WeatherUtils.currentTempByLatLon(latitude, longitude)
    return HttpResponse(temperature)
