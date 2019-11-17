import time
from neo import *
import printer
import off
import on
import plainColor

led_state={
    'type':0,
    'color' : [0,50,0],
    'printer-color':0,
    'printerStart':400
}

fps = None
tick = None
minDeltaTime = None
led_functions=None

led_state['num_pixel']=strip.numPixels()


def getMilis():
    return int(round(time.time() * 1000))

def loop():
    global tick
    global minDeltaTime
    global led_state
    while True:
        delta = getMilis()-tick
        if delta > minDeltaTime:
            led_functions[led_state['type']](strip,led_state)
            if led_state['type'] % 2==0:
                led_state['type']+=1
            printer.magicOverride(strip, led_state)
            strip.show()
        else:
            time.sleep(0.01)

led_functions=[
    off.init,
    off.update,
    on.init,
    on.update,
    plainColor.init,
    plainColor.update
]

fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
