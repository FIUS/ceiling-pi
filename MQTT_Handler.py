import paho.mqtt.client as mqtt
from mqttconfig import MQTT_BROKER_ADDRESS, MQTT_USERNAME, MQTT_PASSWORD


class MQTT_Handler:
    mqtt_client = None
    

    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = MQTT_Handler.on_message
        self.mqtt_client.on_connect = MQTT_Handler.on_connect
        self.mqtt_client.username_pw_set(MQTT_USERNAME, password=MQTT_PASSWORD)
        self.mqtt_client.connect(MQTT_BROKER_ADDRESS, keepalive=60)
        self.mqtt_client.publish("fs/ledcontrol/status", "online")
        self.mqtt_client.loop_start()

    def on_message(self, client, userdata, message):
        text = "New message: {}, Topic: {}, QOS: {}, Retain Flag: {}".format(message.payload.decode("utf-8"),
                                                                             message.topic,
                                                                             message.qos,
                                                                             message.retain)
        print(text)

    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK")

    def publish(self, topic, message):
        self.mqtt_client.publish(topic, message)
        print("[MQTT] Message published. Topic: {}, Message: {}".format(topic, message))


