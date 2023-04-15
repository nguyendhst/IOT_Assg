import time
from AdafruitConnect import AdafruitConnect


AIO_FEED_IDS = ["button1", "button2"]
AIO_USERNAME = "xMysT"
AIO_KEY = "aio_OcUq99IvIe55uNA8OM0SCbUaI5vP"

gateway = AdafruitConnect(AIO_USERNAME, AIO_KEY, AIO_FEED_IDS)
gateway.connect()
gateway.subcribe()

while True:
    gateway.run()
    time.sleep(1)