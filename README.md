# ceiling-pi
This is the code controlling the leds and the music in our room

## Installation
There are several libraries needed in order to run the script.
1. The pip installable files are in the ``requirements.txt`` file. You can install these by running ``python3 -m pip install -r requirements.txt``. 

2. Some basic dependencies wich are installable with apt on Ubuntu with ``sudo apt-get install gcc make build-essential python-dev git scons swig``.

3. The library for communication with the leds. A tutorial on how to install the library is found [here](https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/). The Git library it self [here](https://github.com/jgarff/rpi_ws281x).

## Using
Run the ``app.py`` file as sudo

## Adding animations
Add a file called ``<yourAnimation>.py`` to the directory ``/leds/animations``.

The file must import ``from neopixel import *``

This file must also contain 2 functions with the following names and parameters
1. ``def init(strip, data):``
2. ``def update(strip, data):``

``strip`` is the led object on wich the colors can be changed. The ``data`` object stores some informations like the total number of leds. What exactly the stored informations are you can look up in ``led_main`.py`` in the variable ``led_state``.

Alternatively you can use the ``blueprints/animationBlueprint.py`` file which also contains some helper modules.

## Service Files
The script is run in a Service stored in /etc/systemd/system/led.services
