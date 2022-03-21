
## Why use older versions of firmware.

I have had lots of trouble getting current verions of thonnyIDE to work with the current versions of Adafruit micropython HID library. So here are links to the versions that I know work even though they might be slightly dated.

## Firware

- [Flash Nuke.](https://cdn-learn.adafruit.com/assets/assets/000/099/419/original/flash_nuke.uf2?1613329170) 

Flash Nuke is extremely handy when your getting lots of errors and just want to start your pico firware from scratch. 
All you need to do is bootselect, drag and drop the Flash Nuke uf2.

- [Adafruit Circuitpython uf2 file](https://adafruit-circuit-python.s3.amazonaws.com/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-6.2.0.uf2) 

Once Flash Nuke is loaded, drag and drop the Adafruit uf2 file.
Your pico's memory is cleand and you are setup to add libraries.

## Libraries

- [Adafruit HID](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/download/4.1.5/adafruit-circuitpython-hid-6.x-mpy-4.1.5.zip)

Make sure to drag and drop the *adafruit_hid* folder into the pico's lib folder.
Dont include the higher level *adafruit_circuitpython* folder bc of python import errors.

- [SD Card](https://raw.githubusercontent.com/micropython/micropython/master/drivers/sdcard/sdcard.py)

Simply wget this file, and drag and drop to the pico lb folder. 
The library is all included in the standalone python script.

Firewall and AV evasion is important. 
Why try to upload or donwload files over the network when you can load them directly with the pico. 
Also why try to store values/files in the target's memory when you can read and write to the pico.
