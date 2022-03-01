from machine import Pin, PWM
from utils.wifi import Wifi
import utils.ws as ws
from utils.dcmotor import DCMotor

# Pin definitions
frequency = 15000
# led = Pin(4, Pin.OUT)
pin1 = Pin(5, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
enable = PWM(Pin(13), frequency)
# Motor definition
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)
# Connecting to Wifi
Wifi.connect()
# Public a html file
ws.routefile("/", "public/index.html")


@ws.route("/forward")
def forward(query=None):
    dc_motor.forward(50)
    return "off"


@ws.route("/backward")
def backward(query=None):
    dc_motor.backward(50)
    return "off"


@ws.route("/stop")
def stop(query=None):
    dc_motor.stop()
    return "off"


@ws.route("/off")
def off(query=None):
    led.off()
    return "off"


@ws.route("/on")
def on(query=None):
    led.on()
    return "on"


ws.serve()
