from flask import Flask
import time
import threading

app=Flask(__name__)

def temp():
    while True:
        print("haha")
        print("haha")
        time.sleep(2)

threading.Thread(target=temp).start()

@app.route("/")
def hello():
    print("test")
    return "Hi"

app.run(host="0.0.0.0")

