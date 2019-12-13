import time
import requests

doorIsOpen = True

def routine():
    checkDoor()
    time.sleep(1)

def doCheckedPostRequestWithBody(url,state):
    try:
        requests.post(url, json={"type": state})
    except Exception as e:
        print("Error in post: ", e)

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
                doCheckedPostRequestWithBody("http://127.0.0.1:5000/animationType",1)
            else:
                print("Door was closed")
                doCheckedPostRequestWithBody("http://127.0.0.1:5000/animationType",0)

        except:
            print("Error")