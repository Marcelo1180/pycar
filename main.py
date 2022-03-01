from lib.wifi import Wifi
from lib.json_settings import get_settings


Wifi.connect()

# s2 = Wifi()
#
# if id(s1) == id(s2):
#     print("Singleton works, both variables contain the same instance.")
# else:
#     print("Singleton failed, variables contain different instances.")
# import machine
#
# led = machine.Pin(4, machine.Pin.OUT)
# led.on()

# print('Hello world! I can count to 10:')
# for i in range(1,11):
#     print(i)
