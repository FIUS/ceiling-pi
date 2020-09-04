import leds.colorMagic as cm
from neopixel import *
import random as rdm
import structs.CinemaBlob as cblob
import time

blobs = []


def init(strip, data):

    while not cm.fadeTo(strip, 20., (5, 10, 8)):
        strip.show()
        time.sleep(1/60)

    cm.setAll(strip, 10, 5, 8)
    strip.show()

    for i in range(5):
        blobs.append(cblob.CinemaBlob(strip, (30, 250), i*200+145))


def update(strip, data):
    for b in blobs:
        b.animate()
    strip.show()
