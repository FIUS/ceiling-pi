from flask import Flask, request, jsonify
import led_main as led
import threading
import json

app=Flask(__name__)

threading.Thread(target=led.loop).start()

@app.route("/color", methods=['POST'])
def color():
    ''' Input as json in form of [r,g,b] with 0 <= r,g,b <= 255 '''
    
    content=request.json
    led.led_state['color']=content
    led.led_state['type']=2

    return "Ok"

@app.route("/animationType", methods=['POST'])
def animationType():
    '''Input as json in form of {"type":5} '''
    content=request.json
    led.led_state['type']=content['type']
    
    return "State ist now "+str(content['type'])

@app.route("/get")
def get():
    print("test")
    return "Hi"

@app.route("/doorOpen")
def doorOpen():
    print("test")
    return "Hi"

@app.route("/doorClosed")
def doorClosed():
    print("test")
    return "Hi"

@app.route("/printer")
def printer():
    print("test")
    return "Hi"


app.run(host="0.0.0.0")

