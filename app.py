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
    led.led_state['type']=4

    return "Ok"

@app.route("/animationType", methods=['POST'])
def animationType():
    '''Input as json in form of {"type":5} '''
    content=request.json
    led.led_state['type']=content['type']*2
    
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

@app.route("/printer", methods=['POST'])
def printer():
    '''
    Input as json in form of {"color":0.1} - Number in 0<=n<=1
    0 = Email red
    0.6 = Telegram blue
    '''
    content=request.json
    led.led_state['printer-color']=content['color']
    led.led_state['printerStart']=600
    return "Ok"


app.run(host="0.0.0.0")

print(led.led_functions[0].__module__)