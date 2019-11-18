import colorMagic as cm
from neopixel import *

state = 0
speed = 5


def init(strip, data):
    global state
    state = 0
    for i in range(0, data['num_pixel']):
        strip.setPixelColor(i, cm.rgb(0, 0, 0))


def update(strip, data):
    global state
    global speed
    zahl = "{0:b}".format(state)

    for i in range(0, data['num_pixel']):
        if len(zahl)>0:
            x = int(zahl[len(zahl)-1:len(zahl)])
            zahl = zahl[:len(zahl)-1]
            if x == 0:
                strip.setPixelColor(i, cm.rgb(0, 0, 0))
            else:
                strip.setPixelColor(i, cm.rgb(data['color'][0],data['color'][1],data['color'][2]))
        else:
            strip.setPixelColor(i, cm.rgb(0, 0, 0))

    state += speed
