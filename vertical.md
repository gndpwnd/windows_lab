## Enumeration

sysinfo
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

Processes
```
tasklist /SVC
```

networking
```
ipconfig /all
route print
```

ports
```
netstat -ano
netsh advfirewall show currentprofile
netsh advfirewall firewall show rule name=all
```

scheduled tasks
```
schtasks /query /fo LIST /v
```

versions of installed apps
```
wmic product get name, version, vendor
```

get update list
```
wmic qfe get Caption, Description, HotFixID, InstalledOn
```

file permissions
link to sysinternals tool [here]( https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk)
```
accesschk.exe -uws "Everyone" "C:\Program Files"
```

powershell check file permissions
```
Get-ChildItem "C:\Program Files" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sModify"}
```

unounted disks
```
mountvol
```

get drivers
link to driverquery [here]( https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/driverquery)
```
powershell
driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object ‘Display Name’, ‘Start Mode’, Path
Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName,DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"}
```

Enumerating Binaries That AutoElevate
```
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer
```


AutoEnum
privesc-checker [here](https://github.com/pentestmonkey/windows-privesc-check)
```
windows-privesc-check2.exe -h
windows-privesc-check2.exe --dump -G
```

## Privesc Examples

User Account Control Bypass - FoodHelper
```

```