import network
from .json_settings import get_settings

settings = get_settings()


class Wifi:
    @staticmethod
    def connect():
        ssid = settings["WIFI"]["WIFI_SSID"]
        password = settings["WIFI"]["WIFI_PASSWORD"]
        station = network.WLAN(network.STA_IF)
        if station.isconnected() == True:
            # print('network config:', station.ifconfig())
            print("Already connected")
            return

        station.active(True)
        station.connect(ssid, password)
        # print('network config:', station.ifconfig())
