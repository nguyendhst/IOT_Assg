import abc
class Hook(abc.ABC):
    @abc.abstractmethod
    def start(self, gateway):
        pass
    
    @abc.abstractmethod
    def on_message(self, feed, payload):
        pass