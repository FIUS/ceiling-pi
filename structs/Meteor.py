import random as rdm
import leds.colorMagic as cm
from neopixel import *


def fade(strip, colors, strength):
    for i in range(0, strip.numPixels()):
        colors[i][2] /= strength


def show(strip, colors):
    for i in range(0, strip.numPixels()):
        if colors[i][2] < 0.05:
            colors[i] = [0, 0, 0]
            strip.setPixelColor(i, cm.rgb(0, 0, 0))
        else:
            strip.setPixelColor(
                i, cm.hsv(colors[i][0], colors[i][1], colors[i][2]))


class Meteor:

    def __init__(self, border, numLeds, resolution, speed, health):
        spawnsLeft = bool(rdm.randint(0, 1))
        hue = rdm.randint(0, 359)/360.0

        self.speed = speed
        self.maxSpeed = speed*3
        self.position = rdm.randint(0, numLeds*resolution-1)
        self.direction = 1 if spawnsLeft else -1
        self.flickerProtection = 5
        hueTemp = None
        if rdm.randint(0, 10) < 7:
            hueTemp = [hue, 1, 1]
        else:
            hueTemp=[hue, rdm.random(), 1]
        self.color = hueTemp
        self.health = health
        self.numLeds = numLeds
        self.border = border
        self.resolution = resolution
        self.isCollided = 0
        self.collisionBreak = 10
        self.collisionType = False
        self.isDead = False
        self.maxSpeed = self.speed*3

    def draw(self, strip, colors):
        pos = int(self.position/self.resolution)
        posExact = self.position/self.resolution
        posDif = abs(posExact-pos)

        if self.speed > 120:
            colors[pos][0] = self.color[0]
            colors[pos][1] = min(self.color[1], 1)
            colors[pos][2] = min(colors[pos][2]+self.color[2], 1)

            colors[(pos-self.direction) % self.numLeds][0] = self.color[0]
            colors[(pos-self.direction) %
                   self.numLeds][1] = min(self.color[1], 1)
            colors[(pos-self.direction) % self.numLeds][2] = min(colors[pos]
                                                                 [2]+self.color[2]*(posDif/4), 1)

            colors[(pos-self.direction*2) % self.numLeds][0] = self.color[0]
            colors[(pos-self.direction*2) %
                   self.numLeds][1] = min(self.color[1], 1)
            colors[(pos-self.direction*2) %
                   self.numLeds][2] = min(colors[pos][2]+self.color[2]*(posDif/3), 1)

            colors[(pos-self.direction*3) % self.numLeds][0] = self.color[0]
            colors[(pos-self.direction*3) %
                   self.numLeds][1] = min(self.color[1], 1)
            colors[(pos-self.direction*3) %
                   self.numLeds][2] = min(colors[pos][2]+self.color[2]*(posDif/2), 1)
        else:

            colors[pos][0] = self.color[0]
            colors[pos][1] = min(self.color[1], 1)
            colors[pos][2] = min(colors[pos][2]+self.color[2]*(1-posDif), 1)

            colors[(pos-self.direction) % self.numLeds][0] = self.color[0]
            colors[(pos-self.direction) %
                   self.numLeds][1] = min(self.color[1], 1)
            colors[(pos-self.direction) %
                   self.numLeds][2] = min(colors[pos][2]+self.color[2]*(posDif), 1)

    def move(self):
        newPosition = (self.position+self.direction *
                       self.speed) % (self.numLeds*self.resolution)

        if newPosition < self.border*self.resolution:
            newPosition = self.numLeds*self.resolution-self.border*self.resolution
        elif newPosition > self.numLeds*self.resolution-self.border*self.resolution:
            newPosition = self.border*self.resolution

        self.position = newPosition

    def collide(self, other):
        if abs(self.position-other.position) < 3*self.resolution and (self.isCollided == 0 or other.isCollided == 0):
            self.isCollided = self.collisionBreak
            other.isCollided = self.collisionBreak
            if self.direction != other.direction:
                self.collisionType = -1
                other.collisionType = -1
            else:
                if self.direction == 1:
                    if self.position-other.position > 0:
                        self.collisionType = -2
                        other.collisionType = self.speed
                    else:
                        self.collisionType = other.speed
                        other.collisionType = -2
                else:
                    if self.position-other.position > 0:
                        self.collisionType = other.speed
                        other.collisionType = -2
                    else:
                        self.collisionType = -2
                        other.collisionType = self.speed

    def checkCollisionWithRainbow(self, pos, size):
        if self.position/self.resolution > pos-2 and self.position/self.resolution < pos+size+2:
            return True
        return False

    def changeDirection(self):
        self.isCollided = self.collisionBreak
        self.collisionType = -1

    def rainbowEaten(self):
        self.speed = self.maxSpeed

    def reactOnCollision(self):

        if self.isCollided == self.collisionBreak:
            if self.collisionType == -1:
                self.speed *= 0.8
                self.direction *= -1
            elif self.collisionType == -2:
                self.isDead = True
            else:
                self.speed = min(self.speed+self.collisionType, self.maxSpeed)
                self.collisionType = 0

        if self.isCollided > 0:
            self.isCollided -= 1
