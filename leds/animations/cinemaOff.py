import leds.colorMagic as cm
from neopixel import *
import random as rdm

area = [246]


def init(strip, data):
    area = [246]


def update(strip, data):
    if area[0] > 0:
        area.insert(0, area[0]-1)
    if area[len(area)-1] < data['num_pixel']-1:
        area.append(area[len(area)-1]+1)
    cm.fadeArea(strip, 1.05, area)
