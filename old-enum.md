# Traditional Approach

resolve domain servers ips
```
nslookup CorpWebServer.corp.com
```


**set logfile vars**
```
set logfile1=log1.txt
set logfile2=log2.txt
```
#### get info about account policy
```
echo "--------------------  Net Accounts --------------------" >> %logfile1%
net accounts
```

#### get user accounts
```
echo "--------------------  Net USER --------------------" >> %logfile1%
net user > %logfile1%
net user /domain >> %logfile1%
```


set domain var
look in log2.txt
domain is right after the second "User accounts for \\"
```
set domain=domain.tld
```




#### query user accounts in the file
> put users in lists files

```
set localuserfile=localusers.txt
set domainuserfile=domainusers.txt
set lulog=lulog.txt
set dmulog=dmulog.txt
```

get local users info
```
echo "--------------------  LOCAL USERS INFO --------------------" > %lulog%
for /F "tokens=*" %A in (%localuserfile%) do (echo. & echo. & echo ---------------------------------------- & net user %A /domain & echo. & echo.) >> %lulog%
```

get domain users info
```
echo "--------------------  DOMAIN USERS INFO --------------------" > %dmulog%
for /F "tokens=*" %A in (%domainuserfile%) do (echo. & echo. & echo ---------------------------------------- & net user %A /domain & echo. & echo.) >> %dmulog%
```