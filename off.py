import random
import colorMagic as cm
from neopixel import *
pixelsLeft=None
speed=2

def init(strip, data):
    global pixelsLeft
    pixelsLeft = [i for i in range(data['num_pixel'])]

def update(strip, data):
    global pixelsLeft
    
    for i in range(0,speed):
        if len(pixelsLeft)>0:
            offLED=random.randrange(len(pixelsLeft))
            strip.setPixelColor(pixelsLeft[offLED],cm.rgb(0,0,0))
            pixelsLeft.pop(offLED)