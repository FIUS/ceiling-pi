import random
import leds.colorMagic as cm
from neopixel import *
import sounddevice as sd #pip install sounddevice
import numpy as np
import math
import sys
import threading 
from threading import Lock
import mqttUtil.MQTT_Handler as mqtt
import pyaudio
import wave
import time
import mqttUtil.mqttconfig as config

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

lock = Lock()
pixelState=None
speed=2
sd.default.device = 0
sd.default.channels = 1
fs=44100
recording=None
blobs=[]
threadstate=False
isBeat=None
blobState=0
blobColour=1
boxState=0
boxOn=False

def init(strip, data):
    global pixelState
    pixelState = [i for i in range(data['num_pixel'])]
    for i in range(data['num_pixel']-1,0,-1):    
        strip.setPixelColor(i,cm.rgb(0,0,0))
    blobs.append([300,1])

def update(strip, data):
    global blobs
    global recording
    global threadstate
    global lock
    global blobState
    global blobColour

    if threadstate:
        #CS----------
        #lock.acquire()
        threadstate=False
        pulse=isBeat
        #lock.release()
        #-------------
        #print(pulse)
        if pulse :
            '''
            print(pulse)
            pos=random.random()*data['num_pixel']-300
            pos=int(pos)+150
            blobs.append([pos,0])
            
            blobState=1

            pos=random.random()*data['num_pixel']-300
            pos=int(pos)+150
            blobs.append([pos,0])
            
            blobState=1

            pos=random.random()*data['num_pixel']-300
            pos=int(pos)+150
            blobs.append([pos,0])
            '''
            blobState=1
            
            print("blob")

    

    if blobState>0:
        for i in range(data['num_pixel']-1,0,-1):    
            strip.setPixelColor(i,cm.hsv(blobColour,1,blobState))
        blobState=blobState/2
        if blobState<0.01:
            blobState=0
            blobColour=random.random()
    
    for i in range(0,len(blobs)):
        light=blobs[i][1]+1
        light=1-(light*7)/255
        #print(light)
        clr=random.random()
        #print(clr)
        left=blobs[i][0]+blobs[i][1]
        right=blobs[i][0]-blobs[i][1]
        #print(left)
        #print(right)
        strip.setPixelColor(left,cm.hsv(clr,1,light))
        strip.setPixelColor(right,cm.hsv(clr,1,light))

        strip.setPixelColor(left-1,cm.hsv(0,0,0))
        strip.setPixelColor(right+1,cm.hsv(0,0,0))

        blobs[i][1]=blobs[i][1]+1
        if blobs[i][1]>35:
            del blobs[i]
            strip.setPixelColor(left,cm.hsv(clr,1,0))
            strip.setPixelColor(right,cm.hsv(clr,1,0))
            break

def record():
    
    global threadstate
    global isBeat
    global lock
    global boxState

    thresh=5000

    while True:
        try:
            stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index = 0)
            data = np.frombuffer(stream.read(CHUNK, exception_on_overflow = False),dtype=np.int16)
            stream.close()
            peak=np.average(np.abs(data))*2
            #print("musicstate ",float(thresh)*peak/2**16)
            epPeak=int(thresh*peak/2**16)
            ykout=data
            #CS-------
            #lock.acquire()
            isBeat=epPeak>0
            isESwitch=float(thresh)*peak/2**16>0.30
            threadstate=True
            #lock.release()
            #CS-------

            if isESwitch:
                boxState+=1
                boxState=min(boxState,30)

            if isBeat:
                thresh=max(thresh-1000,2000)
            else:
                thresh=min(thresh+1500,6000)
        except Exception as e:
            print("Spotify mag das nicht")



def boxControll():
    global boxState
    global boxOn
    mqttc = mqtt.MQTT_Handler()

    while True:
        print("state: ",boxState)
        time.sleep(5)
        if boxOn and boxState<1:
            boxOn=False
            mqttc.publish(config.MQTT_SOUND_CONTROL, "OFF")
        
        if not boxOn and boxState>10:
            boxOn=True
            mqttc.publish(config.MQTT_SOUND_CONTROL, "ON")
        
        boxState-=2

        boxState=max(0,boxState)



recording = threading.Thread(target=record)
recording.start()

box = threading.Thread(target=boxControll)
box.start()