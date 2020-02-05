import colorMagic as cm
from neopixel import *
import random as rdm

colorArray=None
point=0
distance=0
colorDistance=0.01
modifier=0

def init(strip, data):
    global colorArray
    colorArray=[]
    last=0.0
    for i in range(0,data['num_pixel']):
        upOrDown=bool(rdm.randint(0,1))
        if upOrDown:
            last+=colorDistance
        else:
            last-=colorDistance
        last%=1.0
        colorArray.append(last)
        
        strip.setPixelColor(i, cm.hsv(last,1,1))


def update(strip, data):
    global colorArray
    global point
    global distance
    global modifier

    
    if distance>100:
        point=(rdm.randint(0,data['num_pixel']-1)+200)%data['num_pixel']
        distance=0   
        if bool(rdm.randint(0,1)):
            modifier=-40
        else:
            modifier=40
        print("changed")

    for idx,clr in enumerate(colorArray):
        strip.setPixelColor(idx, cm.hsv(clr,1,1))

    if distance==0:
        colorArray[point]=(colorArray[point]+(1-colorDistance)*modifier)%1.0
        strip.setPixelColor(point, cm.hsv(clr,0,1))

    else:
        ##To the left
        tempPoint=(point+distance)%data['num_pixel']
        colorArray[tempPoint]=(colorArray[tempPoint]+(1-colorDistance)*modifier)%1.0
        strip.setPixelColor(tempPoint, cm.hsv(clr,0,1))

        #To the right
        tempPoint=(point-distance)%data['num_pixel']
        colorArray[tempPoint]=(colorArray[tempPoint]+colorDistance*modifier)%1.0
        strip.setPixelColor(tempPoint, cm.hsv(clr,0,1))
        
    distance+=1
    
    
    
    