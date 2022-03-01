from machine import Pin, PWM
from utils.wifi import Wifi
import utils.ws as ws
from utils.dcmotor import DCMotor

# Pin definitions
frequency = 15000
# led = Pin(4, Pin.OUT)
motor1_pin1 = Pin(16, Pin.OUT)
motor1_pin2 = Pin(5, Pin.OUT)
motor1_enable = PWM(Pin(14), frequency)
motor2_pin1 = Pin(4, Pin.OUT)
motor2_pin2 = Pin(0, Pin.OUT)
motor2_enable = PWM(Pin(12), frequency)
# Motor definition
dc_motor1 = DCMotor(motor1_pin1, motor1_pin2, motor1_enable, 350, 1023)
dc_motor2 = DCMotor(motor2_pin1, motor2_pin2, motor2_enable, 350, 1023)
# Connecting to Wifi
Wifi.connect()
# Public a html file
ws.routefile("/", "public/index.html")


@ws.route("/turn_left")
def turn_left(query=None):
    dc_motor2.stop()
    dc_motor1.forward(50)
    return "off"


@ws.route("/turn_right")
def turn_right(query=None):
    dc_motor1.stop()
    dc_motor2.forward(50)
    return "off"


@ws.route("/forward")
def forward(query=None):
    dc_motor1.forward(50)
    dc_motor2.forward(50)
    return "off"


@ws.route("/backward")
def backward(query=None):
    dc_motor1.backward(50)
    dc_motor2.backward(50)
    return "off"


@ws.route("/stop")
def stop(query=None):
    dc_motor1.stop()
    dc_motor2.stop()
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
