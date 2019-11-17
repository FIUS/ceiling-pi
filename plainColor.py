from neopixel import *
import colorMagic as cm

def init(strip, data):
    for i in range(strip.numPixels()):
        clr=cm.rgb(data['color'][0],data['color'][1],data['color'][2])
        strip.setPixelColor(i, clr)
    print(strip.getPixelColor(5))

def update(strip, data):
    return None