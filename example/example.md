# Context to this lab

> This is a local lab follows the structure of TheCyberMentor's Active Directory outline in his course *Practical Ethical Hacking*
> 
> These lab notes do not exactly follow methodologies found in course instruction, hence the point of recording them

# Getting Started

**Get Basic Info About Domain**

*Checkout the scripts/ps.txt for variations*

```
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
```

![[1.png]]


**Resolve Domain Controller/s **

```
$dc_name=domain_controller
nslookup $dc_name
```

![[2.png]]

### Going Forward

**Powershell**

- powershell is an incredibly powerful tool to find incredible amounts of information about a domain.
- In addition, ps scripts are run in memory
- However, ps script execution must be enabled (admin privileges), and copying and pasting commands into a ps terminal have the potential of being logged and monitored.

**CMD**

- a good method due to seniority, using command line tools to enumerate domains can return good information 
- however there are tools that yield results faster and with more detail
- in addition, commands can be logged and monitored 

**Bloodhound**

- bloodhound is one of the best tools to enumerate domains
- however a common bloohound ingestor, *Sharphound*, is flagged by windows defender, and is hard to obfuscate and encrypt due to the project size.
- in addition, an attacker would need to store files on disk, so antivirus aside from defender have the potential to interfere.
- sharphound does offer proxying, but there are tools available that are more straightforward in setup


**Bloodhound-python**

- bloodhound python is an exceptional tool offering the same enumeration capability as its predecessor
- in additon, this tool can be run from a local linux machine, only requireing dns redirection, a domain controller address and name, and access to a user in the domain.
- in addition, bloodhound-python offers proxying capability through familiar tools such as proxychains and dnschef


