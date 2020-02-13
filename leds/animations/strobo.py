import random
import leds.colorMagic as cm
from neopixel import *

on=True

def init(strip, data):
    clr=cm.rgb(0,0,0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, clr)

def update(strip, data):
    global on

    if on:
        clr=cm.rgb(250,250,250)
        on=False
    else:
        clr=cm.rgb(0,0,0)
        on=True

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, clr)
    
