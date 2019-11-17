from neopixel import *

def init(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(color[0],color[1],color[2]))
    strip.show()

def update(strip):
    return None