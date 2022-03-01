import json
from machine import Pin, PWM
from utils.wifi import Wifi
import utils.ws as ws
from utils.dcmotor import DCMotor

# Constants
MOTOR_FREQUENCY = 15000
MOTOR_SPEED = 50
# Pin definitions
motor1_pin1 = Pin(5, Pin.OUT)
motor1_pin2 = Pin(16, Pin.OUT)
motor1_enable = PWM(Pin(14), MOTOR_FREQUENCY)
motor2_pin1 = Pin(0, Pin.OUT)
motor2_pin2 = Pin(4, Pin.OUT)
motor2_enable = PWM(Pin(12), MOTOR_FREQUENCY)
# Motor definition
dc_motor1 = DCMotor(motor1_pin1, motor1_pin2, motor1_enable, 350, 1023)
dc_motor2 = DCMotor(motor2_pin1, motor2_pin2, motor2_enable, 350, 1023)
# Connecting to Wifi
Wifi.connect()
# Public a html file
ws.routefile("/", "public/index.html")


@ws.route("/turn_left")
def turn_left(query=None):
    dc_motor1.backward(MOTOR_SPEED)
    dc_motor2.forward(MOTOR_SPEED)
    return json.dumps({"action": "turn_left", "message": "OK"})


@ws.route("/turn_right")
def turn_right(query=None):
    dc_motor2.backward(MOTOR_SPEED)
    dc_motor1.forward(MOTOR_SPEED)
    return json.dumps({"action": "turn_right", "message": "OK"})


@ws.route("/forward")
def forward(query=None):
    dc_motor1.forward(MOTOR_SPEED)
    dc_motor2.forward(MOTOR_SPEED)
    return json.dumps({"action": "forward", "message": "OK"})


@ws.route("/backward")
def backward(query=None):
    dc_motor1.backward(MOTOR_SPEED)
    dc_motor2.backward(MOTOR_SPEED)
    return json.dumps({"action": "backward", "message": "OK"})


@ws.route("/stop")
def stop(query=None):
    dc_motor1.stop()
    dc_motor2.stop()
    return json.dumps({"action": "stop", "message": "OK"})


ws.serve()
