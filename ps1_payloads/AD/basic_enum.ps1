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