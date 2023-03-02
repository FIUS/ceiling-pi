import leds.colorMagic as cm
from neopixel import *
from datetime import datetime

state=0
speed=5
brightnessCap=110
dayColor=0
pixels_to_light_up = []

def init(strip, data):
    global state
    global pixels_to_light_up
    state=0

    pixels_to_light_up = [i for i in range(data['num_pixel'])]
    if "off" in data["animation_data"] and "pixels_left" in data["animation_data"]["off"]:
        pixels_to_light_up  = [i for i in range(data['num_pixel']) if i not in data["animation_data"]["off"]["pixels_left"]]

    for i in range(0,data['num_pixel']):
        if i not in pixels_to_light_up:
            continue
        strip.setPixelColor(i, cm.rgb(0,0,0))


def update(strip, data):
    global state
    global speed
    global dayColor
    global pixels_to_light_up

    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    seconds_since_midnight=seconds_since_midnight**2
    colorToSet=seconds_since_midnight/7464960000.0
    colorToSet=int(colorToSet*1000)/1000.0

    if state<255:
        for i in range(0,data['num_pixel']):
            if i not in pixels_to_light_up:
                continue
            if i > 22 and i < 115 or i > 192 and i < 300:
                strip.setPixelColor(i, cm.hsv(0.14,0,state/(255.0+brightnessCap)))
            else:
                strip.setPixelColor(i, cm.hsv(colorToSet,1,state/(255.0+brightnessCap)))
        state+=speed
        if state>255:
            state=255
    else:
        if dayColor!=colorToSet:
            print("changed color due daytime ",colorToSet)
            for i in range(0,data['num_pixel']):
                if i > 22 and i < 115 or i > 192 and i < 300:
                    strip.setPixelColor(i, cm.hsv(0.14,0,state/(255.0+brightnessCap)))
                else:
                    strip.setPixelColor(i, cm.hsv(colorToSet,1,state/(255.0+brightnessCap)))
            dayColor=colorToSet
