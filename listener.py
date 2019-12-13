import time

doorIsOpen = True
led_state=None

def init(leds):
    global led_state
    led_state=leds

def routine():
    checkDoor()
    time.sleep(1)

def checkDoor():
    r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")
    try:
        if r.text == "open":
            setDoorOpen(True)
        else:
            setDoorOpen(False)
    except:
        print("Error")

def setDoorOpen(state):
    global doorIsOpen
    global led_state
    if not(state == doorIsOpen):
        try:
            doorIsOpen = state
            
            if doorIsOpen:
                print("Door was opened")
                led_state['state']=2
            else:
                print("Door was closed")
                led_state['state']=0

        except:
            print("Error")