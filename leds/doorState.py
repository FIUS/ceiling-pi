from typing import Dict, Any
import socket
from logging import getLogger
from paho.mqtt import client as mqtt_client
import json

QOS = 1

logger = getLogger(__name__)

class DoorStateWatcher():
    """
    Listens to the state of the physical door via mqtt and turns on/off the lights
    """
    def __init__(self,
                 mqtt_broker: str,
                 mqtt_port: int,
                 mqtt_user: str,
                 mqtt_pw: str,
                 mqtt_topic: str,
                 led_state: Dict[str, Any]) -> None:
        self.MQTT_BROKER: str = mqtt_broker
        self.MQTT_PORT: int = mqtt_port
        self.MQTT_USER: str = mqtt_user
        self.MQTT_PW: str = mqtt_pw
        self.MQTT_TOPIC: str = mqtt_topic
        self.led_state: Dict[str, Any] = led_state

        self.CLIENT_ID: str = f'ceiling-pi-{socket.gethostname()}-door-state-listener'

        self.doorOpen = False

        logger.debug("Connecting to mqtt server as %s", self.CLIENT_ID)

        # Connect to mqtt
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logger.info("Connected to MQTT Broker!")
            else:
                logger.warn("Failed to connect to broker, return code %d\n", rc)
        self.client = mqtt_client.Client(self.CLIENT_ID, clean_session=False)
        self.client.username_pw_set(self.MQTT_USER, self.MQTT_PW)
        self.client.on_connect = on_connect
        self.client.on_message = self.update
        self.client.connect(self.MQTT_BROKER, self.MQTT_PORT, keepalive=10)
        logger.debug("Subscribing to %s", self.MQTT_TOPIC)
        self.client.subscribe((self.MQTT_TOPIC, QOS))
        self.client.loop_start()

    def update(self, client, userdata, message):
        payload = message.payload
        
        logger.debug("Received door state update: %s", payload)
        payload_obj = json.loads(payload)
        if payload_obj["powerstate"] == 'on' and not self.doorOpen:
            self.doorOpen = True
            self.turnOn()
        if payload_obj["powerstate"] == 'off' and self.doorOpen:
            self.doorOpen = False
            self.turnOff()

    def turnOn(self):
        logger.debug("Turning on")
        self.led_state['type'] = 2

    def turnOff(self):
        logger.debug("Turning off")
        self.led_state['type'] = 0
