## PREPARE ESP8266

List all usb ports
```sh
ls -l /dev/cu.*
```

Erase flash ESP8266
```sh
esptool.py --port /dev/cu.usbserial-0001 erase_flash
```

Load firmware
```sh
esptool.py --port /dev/cu.usbserial-0001 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20220117-v1.18.bin
```

Copy and configure .ampy file
```sh
cp .ampy.example .ampy
```

List files
```sh
ampy ls
```
