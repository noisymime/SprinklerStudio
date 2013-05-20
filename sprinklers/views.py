from django.core.cache import cache
from django.http import HttpResponse
from django.template import Context, loader

from sprinklers.models import Sprinkler
from sprinklers.models import LogEntry

def get_sprinkler(sprinkler_id):
    sprinkler_id = int(sprinkler_id)
    try:
        sprinkler = Sprinkler.objects.get(id=sprinkler_id)
    except Sprinkler.DoesNotExist:
        return None
    return sprinkler

def index(request):
    return HttpResponse("Hello, world. You're at the sprinkler index.")

def detail(request, sprinkler_id):
    tmp_sprinkler = get_sprinkler(sprinkler_id)

    log_entries = []
    #Retrieve all the log entries for this sprinkler
    try:
        log_entries = LogEntry.objects.filter(sprinkler_id=tmp_sprinkler.id)
    except LogEntry.DoesNotExist:  
        log_entries = []

    template = loader.get_template('sprinklers/detail.html')
    context = Context({
        'sprinkler': tmp_sprinkler,
        'sprinkler_log': log_entries,
    })
    return HttpResponse(template.render(context))

def on(request, sprinkler_id):
    sprinkler = get_sprinkler(sprinkler_id)
    #Check if sprinkler is already on
    if sprinkler.status == True: return HttpResponse("Sprinkler already on")
    sprinkler.status = True

    #Insert the log entry
    new_log = LogEntry(sprinkler_id=sprinkler.id)
    new_log.save()
    sprinkler.currentLog = new_log    
    sprinkler.save()

    return HttpResponse("Turning sprinkler on")

def off(request, sprinkler_id):
    sprinkler = get_sprinkler(sprinkler_id)
    sprinkler.status = False
    
    LogEntry.objects.get(id=sprinkler.currentLog).save()
    sprinkler.currentLog = None
    sprinkler.save()

    return HttpResponse("Turning sprinkler off")

def status(request, sprinkler_id):
    sprinkler = get_sprinkler(sprinkler_id)
    if not sprinkler is None:
        return HttpResponse(str(sprinkler.status))
    else:
        return HttpResponse("Sprinkler not found")
