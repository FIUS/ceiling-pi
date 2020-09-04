import random as rdm
import leds.colorMagic as cm
from neopixel import *


class CinemaBlob:

    def __init__(self, strip, lightRange, pos):
        self.strip = strip
        self.lightRange = lightRange
        self.pos = pos
        self.light = lightRange[0]
        self.growLight = True

    def animate(self):
        if self.growLight:
            self.light += int(10*rdm.random())
            self.light = min(self.light, 255)
            if self.light >= self.lightRange[1]:
                self.growLight = False
        else:
            self.light -= 5
            if self.light <= self.lightRange[0]:
                self.growLight = True

        for i in range(self.pos-15, self.pos+15):
            index=abs(self.pos-i)
            
            index=1-(index*0.02)**2
            lightTemp = self.light*index
            self.strip.setPixelColor(
                i, cm.rgb(int(lightTemp), int(lightTemp/1.4), int(lightTemp/2)))
