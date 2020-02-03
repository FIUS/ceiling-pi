import colorMagic as cm
from neopixel import *
import random as rdm

colorArray=None

def init(strip, data):
    global colorArray
    colorArray=[]
    last=0.0
    for i in range(0,data['num_pixel']):
        upOrDown=bool(rdm.randint(0,1))
        if upOrDown:
            last+=0.01
        else:
            last-=0.01
        last%=1.0
        colorArray.append(last)
        print(last)
        strip.setPixelColor(i, cm.hsv(last,1,1))


def update(strip, data):
    global state
    global speed
    
    