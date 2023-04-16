import time
import random
from AdafruitConnect import AdafruitConnect
from PortManagement import PortManagement

# read from .env
import os
#pip3 install python-dotenv
from dotenv import load_dotenv
load_dotenv()

AIO_FEED_IDS = ["button1", "button2"]
AIO_USERNAME = os.getenv("ADA_USR")
AIO_KEY = os.getenv("ADA_KEY")

gateway = AdafruitConnect(AIO_USERNAME, AIO_KEY, AIO_FEED_IDS)
gateway.connect()
gateway.subscribe()

port = PortManagement()

while True:
    port.readSerial(gateway)
    gateway.run()
    time.sleep(1)