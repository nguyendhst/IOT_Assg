import  sys
from Adafruit_IO import MQTTClient


class AdafruitConnect:
        def __init__(self, username, key, feed_ids):
            self.username = username
            self.key = key
            self.feed_ids = feed_ids
            self.client = MQTTClient(self.username, self.key)

        def connect(self):
            self.client.connect()

        def subcribe(self):
            for feed in self.feed_ids:
                self.client.subscribe(feed)

        def publish(self, feed, data):
            self.client.publish(feed, data)

        def run(self):
            self.client.loop_background()
            
        
