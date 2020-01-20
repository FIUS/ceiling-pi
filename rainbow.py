from neopixel import *
import colorMagic as cm

startRainbow=0.0
step=0.008
speed=0.01
def init(strip, data):
    for i in range(strip.numPixels()):
        clr=cm.rgb(data['color'][0],data['color'][1],data['color'][2])
        strip.setPixelColor(i, clr)

def update(strip, data):
    global startRainbow
    
    temp=startRainbow
    for i in range(strip.numPixels()):
        temp=temp+i*step
        temp=temp%1.0
        clr=cm.hsv(temp,1,0.2)
        strip.setPixelColor(i, clr)
    startRainbow=startRainbow+speed