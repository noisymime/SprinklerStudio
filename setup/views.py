# Create your views here.
import json
import urllib2
from django.core.cache import cache
from django.http import HttpResponse
from weather.models import Location
from django.template import Context, loader

from weather import WeatherUtils
from sprinklers.models import Sprinkler

def index(request):
    #cache.clear()
    latitude = Location.objects.all()[0].latitude
    longitude = Location.objects.all()[0].longitude
    
    sprinklers = Sprinkler.objects.all()

    template = loader.get_template('setup/index.html')
    context = Context({
        'sprinklers': sprinklers,
    })
    return HttpResponse(template.render(context))

def ajax(request):

    latitude = request.GET['lat'] # request.POST.get('lat', False)
    longitude = request.GET['lon'] # request.POST.get('lat', False)
    
    temperature = WeatherUtils.currentTempByLatLon(latitude, longitude)
    return HttpResponse(temperature)
