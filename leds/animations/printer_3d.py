from neopixel import *
import leds.colorMagic as cm
import paho.mqtt.client as mqtt

mqtt_username = "3D"
mqtt_password = "ttOWySN37k9fqHf9QuJzoBQphUH269HeTfKDa1XLCt1Dz0MMHjU5Dpe9k9FyHYxz"

currentState = 0

area = (404, 670)

led_state = None


def init(data):
    global led_state
    led_state = data


def magicOverride(strip, data):

    if currentState > 0.05 and currentState < 99.95:
        dist = area[1]-area[0]
        currentDist = int(dist*currentState)
        green = cm.hsv(0.3, 1, 1)
        white = cm.hsv(0.3, 0, 1)
        black = cm.hsv(0.3, 1, 0)
        for i in range(area[0], area[1]+1):
            if i >= area[1]-currentDist:
                strip.setPixelColor(i, green)
            else:
                strip.setPixelColor(i, black)
        strip.setPixelColor(area[0]-1, white)
        strip.setPixelColor(area[0]-2, white)
        strip.setPixelColor(area[1]+1, white)
        strip.setPixelColor(area[1]+2, white)


def progressCallback(client, userdata, message):
    global currentState
    global led_state
    if message.topic == "i3mk3s/progress/completion":
        currentState = float(message.payload.decode("utf-8"))/100
    elif message.topic == "i3mk3s/state/text" and message.payload.decode("utf-8") != "Printing":
        currentState = -1
        current_type = led_state['type']
        setLedType(current_type-(current_type%2))

    print(currentState)


client = mqtt.Client()
try:
    client.username_pw_set(mqtt_username, mqtt_password)
    client.connect("fius-octopi", 1883, 60)
    client.subscribe("i3mk3s/progress/completion")
    client.subscribe("i3mk3s/state/text")
    client.on_message = progressCallback
    client.loop_start()
except:
    print("3d printer not reachable")
