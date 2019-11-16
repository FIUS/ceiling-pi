import time

fps = None
tick = None
minDeltaTime = None


def getMilis():
    return int(round(time.time() * 1000))


def loop():
    global tick
    global minDeltaTime
    while True:
        delta = getMilis()-tick
        if delta > minDeltaTime:
            tick = getMilis()
            print("looploop")
            print(delta)
            print()
        else:
            time.sleep(0.01)


fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
