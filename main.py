import time
from Gateway import *
from hooks.InfluxDB_Hook import *
from hooks.Adafruit_Hook import *
from hooks.Serial_Hook import *


gateway = Gateway()

serial = Serial()
gateway.addHook(serial)

influx = InfluxDB(
    host=gateway.config["INFLUXDB"]["INF_URL"],
    bucket=gateway.config["INFLUXDB"]["INF_BUCKET"],
    org=gateway.config["INFLUXDB"]["INF_ORG"],
    token=gateway.config["INFLUXDB"]["INF_TOKEN"],
)
gateway.addHook(influx)

# adafruit = Adafruit()
# gateway.addHook(adafruit)


def main():
    gateway.start()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
