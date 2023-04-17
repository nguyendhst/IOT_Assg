import serial.tools.list_ports
import serial
from AdafruitConnect import AdafruitConnect
from hooks.Hook import *
import threading


class Serial(Hook):
    def __init__(self) -> None:
        self.ser = None
        self.mess = ""
        self.gateway = None

    def start(self, gateway):
        if Serial.getPort() != None:
            self.ser = serial.Serial(port=Serial.getPort(), baudrate=115200)
            self.gateway = gateway

        if self.ser.isOpen():
            print("Serial is open")
            # listen for data in a separate thread
            thread = threading.Thread(target=self.readSerial, args=(gateway,))
            thread.daemon = True
            thread.start()

        else:
            print("Serial is not open")

    def getPort():
        ports = serial.tools.list_ports.comports()
        N = len(ports)
        commPort = "None"
        for i in range(0, N):
            port = ports[i]
            strPort = str(port)
            # print(strPort)
            if "USB-SERIAL" in strPort:
                splitPort = strPort.split(" ")
                commPort = splitPort[0]
        print("COM10")
        return "/dev/ttys013"

    def processData(client, data):
        data = data.replace("!", "")
        data = data.replace("#", "")
        splitData = data.split(":")
        print(splitData)
        if splitData[1] == "T":
            client.publish(client.username+"/feeds/button1", splitData[2])
            print("Published to button1")
        if splitData[1] == "R":
            client.publish("receive", splitData[2])

    def readSerial(self, client):
        while True:
            bytesToRead = self.ser.inWaiting()
            # print(ser)
            if bytesToRead > 0:
                # global mess
                self.mess = self.mess + self.ser.read(bytesToRead).decode("UTF-8")
                while ("#" in self.mess) and ("!" in self.mess):
                    start = self.mess.find("!")
                    end = self.mess.find("#")
                    Serial.processData(client, self.mess[start : end + 1])
                    if end == len(self.mess):
                        self.mess = ""
                    else:
                        self.mess = self.mess[end + 1 :]

    def on_message(self, feed, payload):
        print("Serial: Received: " + payload.decode() + ", feed_id: " + feed)
        # TODO: Send to serial
