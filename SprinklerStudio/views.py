# Create your views here.
import json
import urllib2
from django.core.cache import cache
from django.http import HttpResponse
from django.template import Context, loader
from sprinklers.models import Sprinkler
from weather import WeatherUtils

def index(request):
    sprinklers = Sprinkler.objects.all()
    weather = WeatherUtils.currentTemp()


    template = loader.get_template('templates/index.html')
    context = Context({
        'sprinkler_list': sprinklers,
        'weather': weather,
    })
    return HttpResponse(template.render(context))

