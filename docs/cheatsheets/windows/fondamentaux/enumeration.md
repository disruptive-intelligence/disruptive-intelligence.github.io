---
title: "Énumération et audit local"
cours:
  - library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md
---
# Énumération et audit local

Faire l'état des lieux d'un poste Windows pour un audit de durcissement ou une recherche d'élévation de privilèges.

Les incontournables : `whoami /all` · `systeminfo` · `tasklist /svc` · `netstat -ano` · `net accounts`
{ .kw-cs-top }

## Parcours rapide

### Faire un premier inventaire local

| Étape | Commandes | À regarder |
|---|---|---|
| [Identité et droits](droits.md) | `whoami /all`, `whoami /priv`, `whoami /groups` | SID, groupes, privilèges, niveau d'intégrité du token courant |
| [Sessions](systeme.md#voir-qui-est-connecte-a-la-machine) | `query user`, `echo %USERNAME%` (CMD) | Sessions actives/déconnectées, compte courant |
| [Système et correctifs](systeme.md#voir-les-correctifs-installes) | `systeminfo`, `Get-HotFix` (PowerShell), `wmic qfe` (historique) | OS, build, architecture, dernier démarrage, domaine, KB |
| [Processus et services](processus.md#relier-les-processus-aux-services) | `tasklist /svc` | Processus habituels, logiciels tiers, PID et services hébergés |
| [Environnement](systeme.md#examiner-les-chemins-de-recherche-et-de-demarrage) | `set` (CMD), `Get-ChildItem Env:` (PowerShell) | `PATH`, profils, répertoires personnels et temporaires |
| [Logiciels](../administration/logiciels.md#lister-les-logiciels-installes) | `winget list`, `Get-ItemProperty` sur les clés `Uninstall` | Noms, versions, éditeurs, services et configurations associés |
| [Réseau](reseau.md) | `ipconfig /all`, `arp -a`, `route print` | Interfaces, DNS, voisins, routes ; machine sur plusieurs sous-réseaux |
| [Écoute et connexions](reseau.md#voir-les-ports-en-ecoute) | `netstat -ano`, `tasklist /FI "PID eq 3520"` | Port → PID → processus → service ; écoute locale ou sur toutes les interfaces |
| [Comptes et groupes](droits.md#enumerer-les-comptes-et-les-groupes-locaux) | `net user`, `net localgroup`, `net localgroup administrators` | Comptes de service, groupes inhabituels, administrateurs supplémentaires ; noms localisés |
| [Politique de comptes](droits.md#voir-la-politique-de-mot-de-passe-et-de-verrouillage) | `net accounts` | Longueur et historique, expiration, seuil/durée de verrouillage |
| [Protections](systeme.md#consulter-et-tester-la-politique-applocker) | `Get-MpComputerStatus`, `Get-AppLockerPolicy`, `Test-AppLockerPolicy` (PowerShell) | Composants Defender, règles AppLocker et mode d'application |

`wmic product get name` et `Get-WmiObject -Class Win32_Product` peuvent lancer des réparations MSI : préférer l'[inventaire par le registre](../administration/logiciels.md#lister-les-logiciels-installes).

## Identité et comptes

Les sorties viennent du lab HTB (serveur `WINLPE-SRV01`), abrégées. Les blocs `bat` se tapent dans CMD, les blocs `powershell` dans PowerShell.

### Voir mon identité, mes groupes et mes privilèges

```bat title="Commande"
whoami /all
```

```bat title="Exemple"
whoami /priv
whoami /groups
```

??? example "Sortie"
    ```text
    PRIVILEGES INFORMATION
    Privilege Name                Description                    State
    ============================= ============================== ========
    SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
    SeIncreaseWorkingSetPrivilege Increase a process working set Disabled

    GROUP INFORMATION
    BUILTIN\Remote Desktop Users
    Mandatory Label\Medium Mandatory Level
    ```

`Disabled` = présent dans le token mais désactivé. Medium = processus non élevé.

Ensuite : [interpréter les privilèges et le niveau d'intégrité](droits.md#voir-mon-sid-mes-groupes-et-mes-privileges).
{ .kw-cs-meta }

### Repérer les sessions ouvertes et le compte courant

```bat title="Commande"
query user
echo %USERNAME%
```

??? example "Sortie"
    ```text
     USERNAME        SESSIONNAME   ID  STATE   IDLE TIME  LOGON TIME
    >administrator   rdp-tcp#2      1  Active          .  3/25/2021 9:27 AM
    ```

Une session déconnectée reste ouverte. En PowerShell, le nom courant s'obtient avec `$env:USERNAME`.

### Lister les comptes et groupes locaux

```bat title="Commande"
net user
net localgroup
net localgroup administrators
```

```powershell title="Exemple"
Get-LocalGroupMember -SID S-1-5-32-544
```

??? example "Sortie"
    ```text
    C:\htb> net localgroup administrators
    Members
    ---------------------------------------------------
    Administrator
    helpdesk
    sarah
    secsvc
    ```

Sur un Windows français, le groupe s'appelle `Administrateurs` ; le SID `S-1-5-32-544` reste identique. Regarder les comptes de service (`secsvc`) et les appartenances inutiles aux groupes privilégiés.

### Lire la politique de mot de passe et de verrouillage

```bat title="Commande"
net accounts
```

```bat title="Exemple"
net accounts /domain
```

??? example "Sortie"
    ```text
    C:\htb> net accounts
    Minimum password age (days):    0
    Maximum password age (days):    42
    Minimum password length:        0
    Length of password history:     None
    Lockout threshold:              Never
    Lockout duration (minutes):     30
    ```

Longueur minimale nulle et aucun verrouillage : points faibles à signaler. `/domain` interroge la politique du domaine, qui peut différer de la politique locale.

## Système, processus et logiciels

### Identifier Windows, son architecture et son domaine

```bat title="Commande"
systeminfo
```

```powershell title="Exemple"
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, BuildNumber, OSArchitecture
```

??? example "Sortie"
    ```text
    C:\htb> systeminfo
    OS Name:             Microsoft Windows Server 2016 Standard
    OS Version:          10.0.14393 Build 14393
    System Manufacturer: VMware, Inc.
    System Type:         x64-based PC
    Domain:              WORKGROUP
    Hotfix(s):           3 Hotfix(s) Installed
    Network Card(s):     2 NIC(s) Installed
    ```

Relever aussi le dernier démarrage. Le build exact compte plus que le nom de l'OS.

### Examiner les correctifs installés

```powershell title="Commande"
Get-HotFix | Sort-Object InstalledOn -Descending
```

```powershell title="Exemple"
Get-HotFix | Format-Table -AutoSize
```

??? example "Sortie"
    ```text
    Source        Description      HotFixID  InstalledBy                  InstalledOn
    WINLPE-SRV01  Update           KB3199986 NT AUTHORITY\SYSTEM          11/21/2016
    WINLPE-SRV01  Update           KB4054590 WINLPE-SRV01\Administrator   3/30/2021
    WINLPE-SRV01  Security Update  KB5001078 NT AUTHORITY\SYSTEM          3/25/2021
    WINLPE-SRV01  Security Update  KB3200970 WINLPE-SRV01\Administrator   4/13/2021
    ```

`wmic qfe` est la forme historique en CMD. Avant de conclure à une faille, vérifier le build et les mises à jour cumulatives.

### Relier les processus aux services

```bat title="Commande"
tasklist /svc
```

```bat title="Exemple"
tasklist /svc /FI "PID eq 3520"
```

??? example "Sortie"
    ```text
    C:\htb> tasklist /svc
    Image Name     PID  Services
    lsass.exe      672  KeyIso, SamSs, VaultSvc
    svchost.exe    972  TermService
    spoolsv.exe   1884  Spooler
    svchost.exe   1988  W3SVC, WAS
    svchost.exe   1996  ftpsvc
    ```

Le PID fait le lien avec `netstat -ano`. Pour un service tiers : compte d'exécution, binaire, version, ACL.

Ensuite : [voir le binaire et le compte d'un service](processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service).
{ .kw-cs-meta }

### Lire les variables, le PATH et les dossiers de démarrage

```bat title="Commande"
set
```

```powershell title="Exemple"
$env:PATH -split ';'
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" -Force
```

??? example "Sortie"
    ```text
    C:\htb> set
    APPDATA=C:\Users\Administrator\AppData\Roaming
    COMPUTERNAME=WINLPE-SRV01
    HOMEPATH=\Users\Administrator
    LOGONSERVER=\\WINLPE-SRV01
    Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;…
    TEMP=C:\Users\ADMINI~1\AppData\Local\Temp\1
    USERDOMAIN=WINLPE-SRV01
    USERNAME=Administrator
    ```

Un dossier inhabituel dans le `PATH` : vérifier ses permissions avec `icacls`. Les éléments du dossier `Startup` s'exécutent à l'ouverture de session.

### Inventorier les logiciels sans interroger Win32_Product

```powershell title="Commande"
Get-ItemProperty `
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' `
  -ErrorAction SilentlyContinue |
  Where-Object DisplayName |
  Select-Object DisplayName, DisplayVersion, Publisher
```

```powershell title="Exemple"
winget list
```

??? example "Sortie"
    ```text
    PS C:\htb> Get-WmiObject -Class Win32_Product | select Name, Version
    Name                                            Version
    SQL Server 2016 Database Engine Services        13.2.5026.0
    SQL Server Management Studio for Reporting …    15.0.18369.0
    Microsoft ODBC Driver 13 for SQL Server         13.2.5026.0
    Java 8 Update 231 (64-bit)                      8.0.2310.11
    ```

Les logiciels portables n'apparaissent pas. Regarder versions, services associés et fichiers de configuration (sessions PuTTY ou FileZilla, par exemple).

## Réseau et exposition locale

### Repérer les interfaces, passerelles et serveurs DNS

```bat title="Commande"
ipconfig /all
```

```powershell title="Exemple"
Get-NetIPConfiguration
```

??? example "Sortie"
    ```text
    C:\htb> ipconfig /all
    Host Name . . . . . . . . : WINLPE-SRV01
    IP Routing Enabled. . . . : No
    DNS Suffix Search List. . : .htb

    Ethernet adapter Ethernet1:
       IPv4 Address. . . . . . : 192.168.20.56(Preferred)
       Default Gateway . . . . : 192.168.20.1

    Ethernet adapter Ethernet0:
       IPv4 Address. . . . . . : 10.1.43.8(Preferred)
       Default Gateway . . . . : 10.1.0.1
       DNS Servers . . . . . . : 1.1.1.1
    ```

Deux interfaces : la machine est sur deux sous-réseaux (dual-homed). `IP Routing Enabled: No` : elle ne route pas entre eux.

### Lire les voisins ARP et les routes

```bat title="Commande"
arp -a
route print
```

```bat title="Exemple"
route print -4
```

??? example "Sortie"
    ```text
    Network Destination  Netmask        Gateway        Interface      Metric
    0.0.0.0              0.0.0.0        10.1.0.1       10.1.43.8          25
    0.0.0.0              0.0.0.0        192.168.20.1   192.168.20.56     271
    10.1.0.0             255.255.0.0    On-link        10.1.43.8         281
    192.168.20.0         255.255.255.0  On-link        192.168.20.56     271
    ```

`On-link` = réseau directement accessible. Entre les deux routes par défaut, celle de métrique `25` l'emporte. ARP liste les voisins connus, pas un historique des connexions.

### Identifier un port en écoute et son processus

```bat title="Commande"
netstat -ano
```

```bat title="Exemple"
tasklist /FI "PID eq 3520"
tasklist /svc /FI "PID eq 3520"
```

??? example "Sortie"
    ```text
    Local Address     State       PID
    0.0.0.0:21        LISTENING   1096
    0.0.0.0:80        LISTENING   4
    0.0.0.0:445       LISTENING   4
    0.0.0.0:1433      LISTENING   3520
    0.0.0.0:3389      LISTENING   968
    ```

`-a` : connexions et écoute ; `-n` : valeurs numériques ; `-o` : PID. `127.0.0.1` = accès local seulement ; `0.0.0.0` = toutes les interfaces IPv4. Confirmer le programme avec le PID plutôt que de déduire le service du numéro de port.

## Protections

### Vérifier les composants de Microsoft Defender

```powershell title="Commande"
Get-MpComputerStatus
```

```powershell title="Exemple"
Get-MpComputerStatus |
    Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
```

??? example "Sortie"
    ```text
    AMServiceEnabled          : True
    AntivirusEnabled          : True
    RealTimeProtectionEnabled : False
    BehaviorMonitorEnabled    : False
    OnAccessProtectionEnabled : False
    IoavProtectionEnabled     : False
    ```

Service actif, mais protection temps réel et surveillance comportementale coupées. Regarder aussi l'âge des signatures.

### Lire et tester la politique AppLocker

```powershell title="Commande"
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

```powershell title="Exemple"
Get-AppLockerPolicy -Local |
    Test-AppLockerPolicy -Path C:\Windows\System32\cmd.exe -User Everyone
```

??? example "Sortie"
    ```text
    FilePath                     PolicyDecision MatchingRule
    C:\Windows\System32\cmd.exe          Denied c:\windows\system32\cmd.exe
    ```

`-Local` = politique locale ; `-Effective` = fusion des politiques appliquées par GPO. Pour tester le compte courant : `-User "$env:USERDOMAIN\$env:USERNAME"`. En mode audit, `Denied` ne bloque rien : vérifier le mode de la collection.

Ensuite : [interpréter les règles AppLocker](systeme.md#consulter-et-tester-la-politique-applocker).
{ .kw-cs-meta }

## Lire les résultats

- **Droits** : groupe Administrators, processus élevé et SYSTEM sont trois choses différentes. SYSTEM local n'est pas Domain Admin.
- **Correctifs et logiciels** : rapprocher build, KB et versions des vulnérabilités connues.
- **Réseau** : une machine sur deux sous-réseaux peut servir de pont vers un réseau autrement inaccessible.
- **Durcissement** : permissions des dossiers du `PATH`, appartenances privilégiées inutiles, protections désactivées.

## Vue d'ensemble

| Besoin | Commande | À retenir |
|---|---|---|
| Identité, groupes, privilèges | `whoami /all` · `/priv` · `/groups` | `Disabled` = présent mais désactivé ; Medium = non élevé |
| Sessions ouvertes, compte courant | `query user` · `echo %USERNAME%` | `$env:USERNAME` en PowerShell |
| Comptes et administrateurs locaux | `net user` · `net localgroup administrators` | `Administrateurs` en français ; SID `S-1-5-32-544` |
| Politique de mot de passe | `net accounts` · `/domain` | Longueur 0, verrouillage `Never` = faiblesses |
| Version, build, domaine | `systeminfo` · `Get-CimInstance Win32_OperatingSystem` | Le build compte plus que le nom |
| Correctifs | `Get-HotFix` · `wmic qfe` | Croiser avec les mises à jour cumulatives |
| Processus ↔ services | `tasklist /svc` · `/FI "PID eq <PID>"` | Le PID relie à `netstat -ano` |
| Variables, PATH, démarrage | `set` · `$env:PATH -split ';'` | Dossier du `PATH` modifiable = piste |
| Logiciels installés | `Get-ItemProperty` (clés `Uninstall`) · `winget list` | Éviter `Win32_Product` (réparations MSI) |
| Interfaces, DNS | `ipconfig /all` · `Get-NetIPConfiguration` | Deux interfaces = deux sous-réseaux |
| Voisins, routes | `arp -a` · `route print` | La métrique la plus faible l'emporte |
| Ports en écoute | `netstat -ano` | `0.0.0.0` = toutes les interfaces, `127.0.0.1` = local |
| Defender | `Get-MpComputerStatus` | Temps réel et comportemental à `False` = protection réduite |
| AppLocker | `Get-AppLockerPolicy -Effective` · `Test-AppLockerPolicy` | Vérifier le mode : audit ou application |

Pour approfondir : [cours complet et outils d'énumération](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md) · [démarche d'élévation locale](../../../privesc/windows.md).
