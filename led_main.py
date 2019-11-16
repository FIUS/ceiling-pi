import time
temp = int(round(time.time() * 1000))

def loop():
    global temp
    while True:
        print(int(round(time.time() * 1000))-temp)
        temp =int(round(time.time() * 1000))
        print("haha")
        print("haha")
        print("looploop")