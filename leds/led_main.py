import time
from leds.neo import *
from leds.animation_import import *
import leds.listener as listener
import threading
import traceback

led_state = {
    'type': 0,  # 18 is for cinema
    'color': [0, 50, 0],
    'printer-color': 0,
    'printerStart': 400
}

fps = None
tick = None
minDeltaTime = None
led_functions = None

led_state['num_pixel'] = strip.numPixels()

threading.Thread(target=listener.routine).start()


def getMilis():
    return int(round(time.time() * 1000))


def loop():
    global tick
    global minDeltaTime
    global led_state
    while True:
        try:
            delta = getMilis()-tick
            if delta > minDeltaTime:
                led_functions[led_state['type']](strip, led_state)
                if led_state['type'] % 2 == 0:
                    led_state['type'] += 1
                if led_state['type'] > 1:
                    printer.magicOverride(strip, led_state)
                    printer_3d.magicOverride(strip, led_state)
                strip.show()
            else:
                time.sleep(0.01)
        except Exception as e:
            traceback.print_exc()
            print("Something went wrong !!!", e)
            exit()


def stringToMode(mode):
    led_state['type']=modeSwitchCase[mode]


modeSwitchCase={"off": 0, "on": 2, "color": 4, "binarycounter": 6, "music": 8, "lsd": 10,
        "colorbomb": 12, "strobo": 14, "meteor": 16, "cinema": 18, "cinemaoff": 20}

led_functions = [
    off.init,
    off.update,
    on.init,
    on.update,
    plainColor.init,
    plainColor.update,
    binaryCounter.init,
    binaryCounter.update,
    music.init,
    music.update,
    lsd.init,
    lsd.update,
    colorBomb.init,
    colorBomb.update,
    strobo.init,
    strobo.update,
    meteor.init,
    meteor.update,
    cinema.init,
    cinema.update,
    cinemaOff.init,
    cinemaOff.update
]

fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
