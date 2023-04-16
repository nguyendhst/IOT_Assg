import time
import random
from AdafruitConnect import AdafruitConnect
from PortManagement import PortManagement


AIO_FEED_IDS = ["button1", "button2"]
AIO_USERNAME = "xMysT"
AIO_KEY = "aio_ojbG10jK1n7p7V1gSElP7xuttiUV"

gateway = AdafruitConnect(AIO_USERNAME, AIO_KEY, AIO_FEED_IDS)
gateway.connect()
gateway.subscribe()

port = PortManagement()

while True:
    port.readSerial(gateway)
    gateway.run()
    time.sleep(1)