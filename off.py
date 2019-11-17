import random
import colorMagic as cm
pixelsLeft=None

def init(strip, data):
    global pixelsLeft
    pixelsLeft = [i for i in range(data['num_pixel'])]

def update(strip, data):
    global pixelsLeft
    if len(pixelsLeft)>0:
        offLED=random.randrange(len(pixelsLeft))
        strip.setPixelColor(offLED,cm.rgb(0,0,0))
        pixelsLeft.remove(offLED)