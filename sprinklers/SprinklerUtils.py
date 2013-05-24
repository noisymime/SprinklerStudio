from django.core.cache import cache
import RPi.GPIO as GPIO
from sprinklers.model import Sprinkler
from sprinklers.model import LogEntry

# NUMBER OF STATIONS
num_stations = 16

# GPIO PIN DEFINES

pin_sr_clk =  4
pin_sr_noe = 17
pin_sr_dat = 21 # NOTE: if you have a RPi rev.2, need to change this to 27
pin_sr_lat = 22

def get_sprinkler(sprinkler_id):
    sprinkler_id = int(sprinkler_id)
    try:
        sprinkler = Sprinkler.objects.get(id=sprinkler_id)
    except Sprinkler.DoesNotExist:
        return None
    return sprinkler

def enableShiftRegisterOutput():
    GPIO.output(pin_sr_noe, False)

def disableShiftRegisterOutput():
    GPIO.output(pin_sr_noe, True)

def setShiftRegister(values):
    GPIO.output(pin_sr_clk, False)
    GPIO.output(pin_sr_lat, False)
    for s in range(0,num_stations):
        GPIO.output(pin_sr_clk, False)
        GPIO.output(pin_sr_dat, values[num_stations-1-s])
        GPIO.output(pin_sr_clk, True)
    GPIO.output(pin_sr_lat, True)
    
def setup():
    values = [0]*num_stations
    
    GPIO.cleanup()
    # setup GPIO pins to interface with shift register
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_sr_clk, GPIO.OUT)
    GPIO.setup(pin_sr_noe, GPIO.OUT)
    disableShiftRegisterOutput()
    GPIO.setup(pin_sr_dat, GPIO.OUT)
    GPIO.setup(pin_sr_lat, GPIO.OUT)

    setShiftRegister(values)
    enableShiftRegisterOutput()

def turn_on(sprinkler_id):
    values = [0]*num_stations
    sprinkler = get_sprinkler(sprinkler_id)

    #Check if sprinkler is already on
    if sprinkler.status == True: return "Sprinkler already on"
    sprinkler.status = True
    
    #loop through all sprinklers and set them appropriately
    for tmpSprinkler in Sprinkler.objects.all():
        #Check for masters
        if tmpSprinkler.IsMaster:
            values[tmpSprinkler.id] = 1
        else:
            values[tmpSprinkler.id] tmpSprinkler.status
    #Perform update on the HW
    setShiftRegister(values):

    #Insert the log entry
    new_log = LogEntry(sprinkler_id=sprinkler.id)
    new_log.save()
    sprinkler.currentLog = new_log    
    sprinkler.save()