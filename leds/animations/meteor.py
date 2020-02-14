import leds.colorMagic as cm
from structs.Meteor import *
import time
from neopixel import *

meteorCount = 7
beaconSpawnTime = 60000
backgroundColor = (10, 10, 10)
colors = None
meteors = None


def init(strip, data):
    global meteors
    global colors

    colors = []
    for i in range(0, data['num_pixel']):
        colors.append([0.0, 0.0, 0.0])
        strip.setPixelColor(i, cm.rgb(0, 0, 0))

    meteors = []

    for i in range(0, meteorCount):
        meteors.append(Meteor(5, data['num_pixel'], 100,100,10))


def update(strip, data):
    global meteors
    global colors
    dif=0
    for m in meteors:
        m.move()    
        m.draw(strip,colors)
    
    fade(strip,colors,1.08)
    show(strip,colors)
    

