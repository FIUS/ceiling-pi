from flask import Flask, request, jsonify
import leds.led_main as led
import threading
import json

import PythonTelegramWraper.bot as BotWrapper
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext.filters import Filters
from telegram.ext import CallbackQueryHandler
import PythonTelegramWraper.config as config

app=Flask(__name__)

threading.Thread(target=led.loop).start()

@app.route("/color", methods=['POST'])
def color():
    ''' Input as json in form of [r,g,b] with 0 <= r,g,b <= 255 '''
    
    content=request.json
    if content is not None:
        led.led_state['color']=content
        led.led_state['type']=4
        return "Ok"
    
    return "Wrong format"

    

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

@app.route("/getAnimations", methods=['GET'])
def animations():
    '''
    Return the available animations
    '''
    out=[]
    for i in led.led_functions:
        name=i.__module__
        if name not in out:
            out.append(name)
    
    return str(out)

def admin(update, context):
    user = update.message.from_user
    chatID = BotWrapper.chatID(update)
    print(chatID)
    BotWrapper.sendMessage(chatID, "Request has been sent...")
    button_list = [
        InlineKeyboardButton("Ja", callback_data=chatID),
        InlineKeyboardButton("Nein", callback_data="no")
    ]
    reply_markup = InlineKeyboardMarkup(
        BotWrapper.build_menu(button_list, n_cols=1))
    message = '{} (@{}) wants to admin, accept request?'.format(
        user['first_name'], user['username'])
    BotWrapper.getBot().sendMessage(config.admin, message, reply_markup=reply_markup)

def adminResponse(update, context):
    chatID = BotWrapper.chatID(update)
    try:
        BotWrapper.getBot().delete_message(chat_id=update.effective_chat.id,
                                message_id=update.effective_message.message_id)
    except Exception as e:
        print(e)
    inp = str(update.callback_query.data)
    if inp is not "no":
        BotWrapper.modifyUser(int(inp), True)
        BotWrapper.sendMessage(inp, "You have been accepted")
        BotWrapper.sendMessage(chatID, "Request has been accepted")
    else:
        BotWrapper.sendMessage(chatID, "Request has been denied")

def modeChange(update, context):
    chatID = BotWrapper.chatID(update)

    if str(chatID) in BotWrapper.getUserData():

        msg = update.message.text.split()[0][1:]
        
        led.stringToMode(msg.lower())

        BotWrapper.sendMessage(chatID, "Switched to "+str(msg))



BotWrapper.botBackend.dispatcher.add_handler(
    CallbackQueryHandler(adminResponse))
BotWrapper.addBotCommand("admin", admin)

for i in led.modeSwitchCase:
    print(i)
    BotWrapper.addBotCommand(i,modeChange)
BotWrapper.startBot()

app.run(host="0.0.0.0")
