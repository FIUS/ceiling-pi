import time
from leds.neo import *
from leds.animation_import import *
from leds.doorState import DoorStateWatcher
import threading
import traceback

led_state = {
    'type': 0,  # 18 is for cinema
    'color': [0, 50, 0],
    'printer-color': 0,
    'printerStart': 400,
    'animation_data': {}
}

fps = None
tick = None
minDeltaTime = None
led_functions = None
mutex = threading.Lock()

led_state['num_pixel'] = strip.numPixels()

def run(mqtt_broker: str,
        mqtt_port: int,
        mqtt_user: str,
        mqtt_pw: str,
        mqtt_topic_door_state: str):
    dsw = DoorStateWatcher(mqtt_broker, mqtt_port, mqtt_user, mqtt_pw, mqtt_topic_door_state, setLedType)
    threading.Thread(target=loop).start()


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
                with mutex:
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

def setLedType(ledType):
    with mutex:
        led_state['type']=ledType

def stringToMode(mode):
    setLedType(modeSwitchCase[mode])


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
