from neopixel import *
import colorMagic as cm

fading = 0
onStateChanged = False
slowFade = True
offState = 0

## Constants
fadingSize = 20

def init(strip, data):
    global fading
    global onStateChanged
    global offState

    fading = data['num_pixel']
    onStateChanged = True
    offState = 0
    print("lul")

def update(strip, data):
    global fading
    global onStateChanged
    global slowFade
    global offState
    
    if onStateChanged:
        print("1")
        if fading > 0:
            print("2")
            for i in range (0,int((data['num_pixel'] / fadingSize) - fadingSize)):
                print("3")
                if i * fadingSize + offState > data['num_pixel'] - 1:
                    fading = 0
                    break
                
                if slowFade:
                    clr=cm.getRGBfromI(strip.getPixelColor(i * fadingSize + offState))
                    r = clr[0] / 2
                    g = clr[1] / 2
                    b = clr[2] / 2
                    strip.setPixelColor(i * fadingSize + offState,cm.rgb(r, g, b))

                else:
                    strip.setPixelColor(i * fadingSize + offState, cm.rgb(0, 0, 0))

            strip.setPixelColor(offState, cm.rgb(0, 0, 0))
            offState+=1
            slowFade = not slowFade

            fading-=1
        else:
            for i in range(0,data['num_pixel']):
                strip.setPixelColor(i, cm.rgb(0, 0, 0))
            onStateChanged = False
            