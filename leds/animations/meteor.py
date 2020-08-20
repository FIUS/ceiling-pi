import leds.colorMagic as cm
from structs.Meteor import *
from structs.RainbowBlob import *
import time
from neopixel import *

meteorCount = 9
beaconSpawnTime = 60000
backgroundColor = (10, 10, 10)
colors = None
meteors = None
rainbowBlob=None

def init(strip, data):
    global meteors
    global colors
    global rainbowBlob

    colors = []
    for i in range(0, data['num_pixel']):
        colors.append([0.0, 0.0, 0.0])
        strip.setPixelColor(i, cm.rgb(0, 0, 0))

    meteors = []

    for i in range(0, meteorCount):
        meteors.append(Meteor(5, data['num_pixel'], 100, 100, 10))
    
    rainbowBlob=RainbowBlob(40,data['num_pixel'])


def update(strip, data):
    global meteors
    global colors
    dif = 0
    for m in meteors:
        m.move()
        m.draw(strip, colors)
        
    for m in meteors:
        for m2 in meteors:
            if m is not m2:
                m.collide(m2)

    if rainbowBlob.spawned:
        rainbowBlob.draw(colors)
        if rainbowBlob.isEatable:
            for m in meteors:
                isCollided=m.checkCollisionWithRainbow(rainbowBlob.position,rainbowBlob.size)
                if isCollided:
                    rainbowBlob.spawned=False
                    m.rainbowEaten()
                    break
        else:
            
            for m in meteors:
                isCollided=m.checkCollisionWithRainbow(rainbowBlob.position,rainbowBlob.size)
                if isCollided:
                    m.changeDirection()

    for m in meteors:
        m.reactOnCollision()
    
    for i in range (0, meteorCount):
        
        if meteors[i].isDead or meteors[i].speed<30:
            del meteors[i]
            meteors.insert(i,Meteor(5, data['num_pixel'], 100, 100, 15))

    
        

    fade(strip, colors, 1.08)
    show(strip, colors)
