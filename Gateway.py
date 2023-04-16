from InfluxDB_Hook import *
import paho.mqtt.client as mqtt
import time
import os

broker_address = "io.adafruit.com"
port = 1883

# pip3 install python-dotenv
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ADA_USR")
password = os.getenv("ADA_KEY")
topic = username + "/feeds/"

AIO_FEED_IDS = ["button1", "button2"]


class Gateway:
    def __init__(self):
        self.hooks: list[Hook] = []
        self.feeds = AIO_FEED_IDS
        self.client = mqtt.Client(
            clean_session=True,
        )
        self.client.username_pw_set(username, password)
        try:
            self.client.connect(broker_address, port)
            for feed in self.feeds:
                self.client.subscribe(topic + feed)
        except Exception as e:
            print(e)
            print("Failed to connect to broker")

        self.client.on_message = self.on_message


    def addHook(self, hook: Hook):
        try:
            self.hooks.append(hook)
        except Exception as e:
            print(e)
            print("Failed to add hook: " + hook.name)

    def start(self):
        self.client.loop_start()

        for hook in self.hooks:
            try:
                hook.start()
            except Exception as e:
                print(e)
                print("Failed to start hook: " + hook.name)

    def stop(self):
        self.client.loop_stop()

    def on_message(self, client, userdata, message):
        print("Received message: " + str(message.payload.decode("utf-8")))
        for hook in self.hooks:
            hook.on_message(message.topic, message.payload)
