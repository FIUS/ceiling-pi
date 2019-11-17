from neopixel import *

def init(strip, data):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(data['color'][0],data['color'][1],data['color'][2]))
    strip.show()

def update(strip, data):
    return None