from neopixel import *
import colorMagic as cm
printerStart=400
printerTemp=0
printerOn=True
tempColor = [0 for i in range(883-852)]

def magicOverride(strip, data):
    global printerStart
    global printerTemp
    global printerOn
    global tempColor

    if printerStart > 0:
        if printerTemp < 0:
            printerOn = not printerOn
      
            if printerOn:
                for i in range(852,883):
                    tempColor[i - 852] = strip.getPixelColor(i)
                    strip.setPixelColor(i,cm.hsv(data['printer-color'],1,1))
        
            else:
                for i in range(852,883):
                    strip.setPixelColor(i,tempColor[i - 852])
            
            printerTemp = 23

        else:
            printerTemp-=1
    
        printerStart-=1
    else:
        if printerOn:
            printerOn=False
            for i in range(852,883):
                strip.setPixelColor(i,tempColor[i - 852])