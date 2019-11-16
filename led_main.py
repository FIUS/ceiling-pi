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
        tick = getMilis()
        if delta > minDeltaTime:
            print("looploop")
            print(tick)
            print()

        else:
            time.sleep(1/1000)


fps = 60
minDeltaTime = 1000/fps

tick = getMilis()
