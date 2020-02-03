import colorMagic as cm
from neopixel import *
from datetime import datetime

state=0
speed=5
brightnessCap=110
dayColor=0

def init(strip, data):
    global state
    state=0
    for i in range(0,data['num_pixel']):
        strip.setPixelColor(i, cm.rgb(0,0,0))


def update(strip, data):
    global state
    global speed
    global dayColor

    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    seconds_since_midnight=seconds_since_midnight**2
    colorToSet=seconds_since_midnight/7464960000.0
    colorToSet=int(colorToSet*10000)/10000.0
    
    if state<255:
        for i in range(0,data['num_pixel']):
            if i > 22 and i < 115 or i > 192 and i < 300:
                strip.setPixelColor(i, cm.hsv(0.14,0,state/(255.0+brightnessCap)))
            else:
                strip.setPixelColor(i, cm.hsv(colorToSet,1,state/(255.0+brightnessCap)))
        state+=speed
        if state>255:
            state=255
    else:
        if dayColor!=colorToSet:
            print("changed color due daytime")
            for i in range(0,data['num_pixel']):
                if i > 22 and i < 115 or i > 192 and i < 300:
                    strip.setPixelColor(i, cm.hsv(0.14,0,state/(255.0+brightnessCap)))
                else:
                    strip.setPixelColor(i, cm.hsv(colorToSet,1,state/(255.0+brightnessCap)))
            dayColor=colorToSet