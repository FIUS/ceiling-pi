import colorMagic as cm
from neopixel import *
state=0
speed=5

def init(strip, data):
    global state
    state=0

def update(strip, data):
    global state
    global speed
    
    if state<255:
        for i in range(0,data['num_pixel']):
            strip.setPixelColor(i, cm.hsv(0.18,1,state/255.0))
            
        state+=speed
        if state>255:
            state=255