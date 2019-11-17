import time
from neo import *
import plainColor

fps = None
tick = None
minDeltaTime = None
color = [0,0,0]
led_functions=None
led_state=0


def getMilis():
    return int(round(time.time() * 1000))

def loop():
    global tick
    global minDeltaTime
    global led_state
    while True:
        delta = getMilis()-tick
        if delta > minDeltaTime:
            led_functions[led_state](neo.strip)
            if led_state % 2==0:
                led_state+=1
        else:
            time.sleep(0.01)

led_functions=[
    plainColor.init,
    plainColor.update
]

fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
