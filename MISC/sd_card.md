# Interacting with SD cards

### Hardware

> Using the HW-125 Micro SD card module

**Pinout**

| Pico | SD Module |
| --- | --- |
| VBUS | VCC |
| GND | GND |
| GP10 | SCK |
| GP11 | MOSI |
| GP12 | MISO |
| GP13 | CS |


### Firmware

Make sure to copy these libraries to your pico:

- adafruit_bus_device/
- adafruit_register/
- adafruit_sdcard.mpy

### Example Usage

This code will create a file named test.txt on the sd card, and write some lines of text to it.

```python
import os
import board
import busio as io
import digitalio
import adafruit_sdcard
import storage
import microcontroller
from time import sleep

SD_CS=board.GP13

spi = io.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/test.txt", "w") as wf:
    wf.write("Hello world...")
    wf.close()

with open("/sd/test.txt", "a") as af:
    
    for i in range(1,10):
        af.write("\nThis is test "+str(i))
    af.close()
```