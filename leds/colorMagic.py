from neopixel import *


def setAll(strip, r, g, b):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, rgb(r, g, b))


def fadeArea(strip, strength, area, r=None, g=None, b=None):
    off = True
    for i in area:
        color = getRGBfromInt(strip.getPixelColor(i))
        r=0
        g=0
        b=0
        if r is None:
            r = color[0]/strength
        else:
            r = max(color[0]/strength, r)

        if g is None:
            g = color[1]/strength
        else:
            g = max(color[1]/strength, g)

        if b is None:
            b = color[2]/strength
        else:
            b = max(color[2]/strength, b)

        if r > 5 or g > 5 or b > 5:
            off = False
        

        r-=1
        g-=1
        b-=1

        r=max(0,r)
        g=max(0,g)
        b=max(0,b)
        
        strip.setPixelColor(i, rgb(g, r, b))
    return off


def fadeAll(strip, strength, r=None, g=None, b=None):
    off = True
    for i in range(0, strip.numPixels()):

        color = getRGBfromInt(strip.getPixelColor(i))

        if r is None:
            r = color[0]/strength
        else:
            r = max(color[0]/strength, r)

        if g is None:
            g = color[1]/strength
        else:
            g = max(color[1]/strength, g)

        if b is None:
            b = color[2]/strength
        else:
            b = max(color[2]/strength, b)

        if r > 5 or g > 5 or b > 5:
            off = False

        strip.setPixelColor(i, rgb(r, g, b))
    return off


def fadeTo(strip, strength, rgbTarget):
    offIndicator = 0

    for i in range(0, strip.numPixels()):
        color = getRGBfromInt(strip.getPixelColor(i))

        difR = rgbTarget[0]-color[0]
        difG = rgbTarget[1]-color[1]
        difB = rgbTarget[2]-color[2]

        r = color[0]+difR/strength
        g = color[1]+difG/strength
        b = color[2]+difB/strength

        r = min(max(r, 3), 255)
        g = min(max(g, 3), 255)
        b = min(max(b, 3), 255)

        offIndicator = max(offIndicator, (abs(
            rgbTarget[0]-color[0]))+(abs(rgbTarget[1]-color[1]))+(abs(rgbTarget[2]-color[2])))
        strip.setPixelColor(i, rgb(int(g), int(r), int(b)))

    return offIndicator < 13 or (color[0] == int(r) and color[1] == int(g) and color[2] == int(b))


def rgb(r, g, b):
    return Color(int(g), int(r), int(b))


def getRGBfromInt(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)


def hsv(h, s, v):
    '''h,s,v in range [0,1]'''
    r = 0.0
    g = 0.0
    b = 0.0

    h_i = int(h * 360 / 60)
    h_i = h_i % 7
    f = h * 360 / 60.0 - h_i
    p = v * float(1 - s)
    q = v * float(1 - s * f)
    t = v * float(1 - s * float(1 - f))

    if h_i == 0 or h_i == 6:
        r = v
        g = t
        b = p
    elif h_i == 1:
        r = q
        g = v
        b = p
    elif h_i == 2:
        r = p
        g = v
        b = t
    elif h_i == 3:
        r = p
        g = q
        b = v
    elif h_i == 4:
        r = t
        g = p
        b = v
    elif h_i == 5:
        r = v
        g = p
        b = q

    return rgb(r*255, g*255, b*255)

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v