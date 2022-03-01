from utils.wifi import Wifi
import utils.ws as ws
from machine import Pin

# Pin definitions
led = Pin(4, Pin.OUT)
# Connecting to Wifi
Wifi.connect()
# Public a html file
ws.routefile("/", "public/index.html")


@ws.route("/off")
def off(query=None):
    led.off()
    return "off"


@ws.route("/on")
def on(query=None):
    led.on()
    return "on"


ws.serve()
