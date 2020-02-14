import random as rdm
import leds.colorMagic as cm
from neopixel import *

def fade(strip, colors, strength):
        for i in range(0, strip.numPixels()):
            colors[i][2] /= strength

def show(strip,colors):
    for i in range(0, strip.numPixels()):
        if colors[i][2]<0.05:
            colors[i]=[0,0,0]
            strip.setPixelColor(i,cm.rgb(0,0,0))
        else:
            strip.setPixelColor(i, cm.hsv(colors[i][0], colors[i][1], colors[i][2]))

class Meteor:

    def __init__(self, border, numLeds, resolution,speed,health):
        spawnsLeft = bool(rdm.randint(0, 1))
        hue = rdm.randint(0, 359)/360.0

        self.speed = speed
        self.position = rdm.randint(0, numLeds*resolution-1)
        self.direction = 1 if spawnsLeft else -1
        self.flickerProtection = 5
        self.color = [hue, 1, 1]
        self.health = health
        self.numLeds = numLeds
        self.border = border
        self.resolution = resolution

    def draw(self, strip, colors):
        pos = int(self.position/self.resolution)
        posExact=self.position/self.resolution
        posDif=abs(posExact-pos)
          
        if self.speed>120:
            colors[pos][0]=self.color[0]
            colors[pos][1]=min(self.color[1],1)
            colors[pos][2]=min(colors[pos][2]+self.color[2],1)

            colors[(pos-self.direction)%self.numLeds][0]=self.color[0]
            colors[(pos-self.direction)%self.numLeds][1]=min(self.color[1],1)
            colors[(pos-self.direction)%self.numLeds][2]=min(colors[pos][2]+self.color[2]*(posDif/4),1)

            colors[(pos-self.direction*2)%self.numLeds][0]=self.color[0]
            colors[(pos-self.direction*2)%self.numLeds][1]=min(self.color[1],1)
            colors[(pos-self.direction*2)%self.numLeds][2]=min(colors[pos][2]+self.color[2]*(posDif/3),1)

            colors[(pos-self.direction*3)%self.numLeds][0]=self.color[0]
            colors[(pos-self.direction*3)%self.numLeds][1]=min(self.color[1],1)
            colors[(pos-self.direction*3)%self.numLeds][2]=min(colors[pos][2]+self.color[2]*(posDif/2),1)
        else:

            colors[pos][0]=self.color[0]
            colors[pos][1]=min(self.color[1],1)
            colors[pos][2]=min(colors[pos][2]+self.color[2]*(1-posDif),1)

            colors[(pos-self.direction)%self.numLeds][0]=self.color[0]
            colors[(pos-self.direction)%self.numLeds][1]=min(self.color[1],1)
            colors[(pos-self.direction)%self.numLeds][2]=min(colors[pos][2]+self.color[2]*(posDif),1)
        
    

    def move(self):
        newPosition = (self.position+self.direction *
                       self.speed) % (self.numLeds*self.resolution)

        if newPosition < self.border*self.resolution:
            newPosition = self.numLeds*self.resolution-self.border*self.resolution
        elif newPosition > self.numLeds*self.resolution-self.border*self.resolution:
            newPosition = self.border*self.resolution

        self.position = newPosition

