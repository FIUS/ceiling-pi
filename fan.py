import RPi.GPIO as GPIO
import psutil as psu
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

while True:
    cpuTemp=psu.sensors_temperatures()['cpu-thermal'][0][1]
    print("CPU Temp: "+str(cpuTemp)+" °C")
    if cpuTemp>60:
        GPIO.output(5, GPIO.HIGH)
    elif cpuTemp<40:
        GPIO.output(5, GPIO.LOW)
    time.sleep('''5*60'''5)