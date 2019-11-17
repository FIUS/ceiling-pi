from neopixel import *

def rgb(r,g,b):
    return Color(int(g),int(r),int(b))

def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return (red, green, blue)

def hsv(h,s,v):
    '''h,s,v in range [0,1]'''
    r = 0.0
    g = 0.0
    b = 0.0

    h_i = int(h * 360 / 60)
    f = h * 360 / 60.0 - h_i
    p = v * float(1 - s)
    q = v * float(1 - s * f)
    t = v * float(1 - s * float(1 - f))

    print(h_i)
    print(f)
    print(p)
    print(q)
    print(t)

    if h_i==0 or h_i==6:
        r = v
        g = t
        b = p
    elif h_i==1:
        r = q
        g = v
        b = p
    elif h_i==2:
        r = p
        g = v
        b = t
    elif h_i==3:
        r = p
        g = q
        b = v
    elif h_i==4:
        r = t
        g = p
        b = v
    elif h_i==5:
        r = v
        g = p
        b = q

    


    return rgb(r*255,g*255,b*255)