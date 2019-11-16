import time
from neo import *

fps = None
tick = None
minDeltaTime = None
color = [0,0,0]

def setColor():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(color[0],color[1],color[2]))
    strip.show()

def getMilis():
    return int(round(time.time() * 1000))

def loop():
    global tick
    global minDeltaTime
    while True:
        delta = getMilis()-tick
        if delta > minDeltaTime:
            #neo.strip
            print()
        else:
            time.sleep(0.01)


fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
