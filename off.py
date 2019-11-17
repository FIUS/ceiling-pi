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

def update(strip, data):
    global fading
    global onStateChanged
    global slowFade
    global offState

    if onStateChanged:
        if fading > 0:
            for i in range (0,(data['num_pixel'] / fadingSize) - fadingSize):
                if i * fadingSize + offState > data['num_pixel'] - 1:
                    fading = 0
                    break
                
                if slowFade:
                    r = leds[i * fadingSize + offState].r / 2
                    g = leds[i * fadingSize + offState].g / 2
                    b = leds[i * fadingSize + offState].b / 2
                    leds[i * fadingSize + offState] = CRGB(r, g, b)

                else:
                    leds[i * fadingSize + offState] = CRGB(0, 0, 0)

            leds[offState] = CRGB(0, 0, 0)
            offState+=1
            slowFade = not slowFade

            fading-=1
            else:
                for i in range(0,data['num_pixel']):
                    leds[i] = CRGB(0, 0, 0)
                onStateChanged = False
            

    
