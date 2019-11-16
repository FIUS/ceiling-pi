from flask import Flask
import led_main as led
import threading

app=Flask(__name__)

threading.Thread(target=led.loop).start()

@app.route("/")
def hello():
    print("test")
    return "Hi"

app.run(host="0.0.0.0")

