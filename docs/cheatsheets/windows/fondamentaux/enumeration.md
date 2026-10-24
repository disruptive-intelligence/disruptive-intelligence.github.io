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

`wmic product get name` et `Get-WmiObject -Class Win32_Product | Select-Object Name, Version` figurent dans le cours : ces requêtes peuvent lancer des réparations MSI. Préférer l'[inventaire par le registre](../administration/logiciels.md#lister-les-logiciels-installes). `wmic.exe` peut être absent ; `Get-WmiObject` appartient à Windows PowerShell 5.1.

## Identité et comptes

Les sorties ci-dessous sont des exemples abrégés et fictifs. Les blocs `bat` se tapent dans CMD ; les blocs `powershell` dans PowerShell.

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
    USER INFORMATION
    meridian\alice    S-1-5-21-…-1104
    PRIVILEGES INFORMATION
    SeChangeNotifyPrivilege    Enabled
    GROUP INFORMATION
    Mandatory Label\Medium Mandatory Level    S-1-16-8192
    ```

Lire les privilèges **présents** dans ce token et leur état. `Disabled` ne signifie pas absent ; Medium ne signifie pas processus administrateur élevé.

Ensuite : [interpréter les privilèges et le niveau d'intégrité](droits.md#voir-mon-sid-mes-groupes-et-mes-privileges).
{ .kw-cs-meta }

### Repérer les sessions ouvertes et le compte courant

```bat title="Commande"
query user
echo %USERNAME%
```

```bat title="Exemple"
query user
```

??? example "Sortie"
    ```text
    USERNAME      SESSIONNAME   ID  STATE   IDLE TIME
    >alice        console        1  Active       none
     adm.martin   rdp-tcp#3      2  Active          5
    ```

Une session déconnectée peut rester ouverte. La présence d'un administrateur connecté ne donne aucun droit supplémentaire. En PowerShell, le nom courant s'obtient avec `$env:USERNAME`.

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
    ObjectClass Name                       PrincipalSource
    User        PC-AUDIT\Administrateur    Local
    Group       MERIDIAN\GG-Support        ActiveDirectory
    ```

Sur Windows français, le groupe CMD s'appelle `Administrateurs` ; le SID reste identique. Examiner les comptes de service et les appartenances inutiles aux groupes privilégiés ou d'accès distant.

### Lire la politique de mot de passe et de verrouillage

```bat title="Commande"
net accounts
```

```bat title="Exemple"
net accounts /domain
```

??? example "Sortie"
    ```text
    Minimum password length:       0
    Length of password history:    None
    Lockout threshold:             Never
    Lockout duration (minutes):    30
    ```

Dans cet exemple, longueur nulle et absence de verrouillage demandent une vérification. Distinguer politique locale, politique de domaine et stratégies affinées ; cela ne prouve pas que les mots de passe sont vides.

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
    Caption                                 Version     BuildNumber OSArchitecture
    Microsoft Windows Server 2016 Standard   10.0.14393  14393       64-bit
    ```

Avec `systeminfo`, relever aussi dernier démarrage, domaine/groupe de travail, correctifs et interfaces. Le build exact compte davantage que le seul nom « Windows Server ».

### Examiner les correctifs installés

```powershell title="Commande"
Get-HotFix | Sort-Object InstalledOn -Descending
```

```powershell title="Exemple"
Get-HotFix | Select-Object HotFixID, Description, InstalledOn -First 3
```

??? example "Sortie"
    ```text
    HotFixID  Description      InstalledOn
    KB3199986 Update           …
    KB5001078 Security Update  …
    KB4103723 Security Update  …
    ```

`wmic qfe` est la forme historique en CMD. Ces inventaires sont partiels ; vérifier build, correctifs cumulatifs et conditions de la CVE avant de conclure à une vulnérabilité.

### Relier les processus aux services

```bat title="Commande"
tasklist /svc
```

```bat title="Exemple"
tasklist /svc /FI "PID eq 3520"
```

??? example "Sortie"
    ```text
    Image Name      PID  Services
    sqlservr.exe   3520  MSSQLSERVER
    ```

Le PID fait le lien avec les connexions réseau. Pour un service tiers, poursuivre avec le compte d'exécution, le binaire, la version et les ACL.

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
    C:\Windows\system32
    C:\Windows
    C:\Tools
    ```

Vérifier les permissions d'un chemin inhabituel avec `icacls C:\Tools`. Un dossier du `PATH` modifiable constitue une piste ; il faut encore confirmer qu'un programme privilégié y recherche réellement un exécutable ou une DLL.

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
    DisplayName                 DisplayVersion  Publisher
    Microsoft SQL Server 2016   13.0.…          Microsoft Corporation
    VMware Tools               …               VMware, Inc.
    ```

Inventaire partiel : les logiciels portables et ceux d'autres profils peuvent manquer. Examiner versions, services associés et configurations. Les requêtes `Win32_Product` du cours restent documentées dans la [fiche logiciels](../administration/logiciels.md#lister-les-logiciels-installes).

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
    InterfaceAlias    IPv4Address       IPv4DefaultGateway
    Ethernet0         192.168.1.50      192.168.1.1
    Ethernet1         192.168.20.56     192.168.20.1
    ```

Plusieurs interfaces peuvent placer la machine sur plusieurs sous-réseaux. Un suffixe DNS ne prouve pas l'appartenance à Active Directory ; `IP Routing Enabled: No` indique que le routage IP n'est pas activé.

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
    0.0.0.0              0.0.0.0        192.168.1.1    192.168.1.50       25
    192.168.20.0         255.255.255.0  On-link        192.168.20.56     271
    ```

`On-link` désigne un réseau directement accessible. La route la plus spécifique prime, puis la métrique départage les routes de même spécificité. ARP fournit des voisins connus, sans historique des sessions ni garantie de joignabilité.

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
    Proto Local Address    Foreign Address  State      PID
    TCP   0.0.0.0:1433    0.0.0.0:0        LISTENING  3520
    TCP   127.0.0.1:8080  0.0.0.0:0        LISTENING  4812
    ```

`-a` : connexions et écoute ; `-n` : valeurs numériques ; `-o` : PID. Loopback (`127.0.0.1`) = accès local ; `0.0.0.0` = toutes les interfaces IPv4. Vérifier le pare-feu et le programme responsable avant d'attribuer un service au numéro de port.

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
    AMServiceEnabled AntivirusEnabled RealTimeProtectionEnabled
    ---------------- ---------------- -------------------------
                True             True                     False
    ```

Le service est actif dans cet exemple, tandis que la protection temps réel ne l'est pas. Examiner aussi surveillance comportementale, analyse à l'accès, signatures et leur ancienneté, en tenant compte du mode de Defender.

### Lire et tester la politique AppLocker

```powershell title="Commande"
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
```

```powershell title="Exemple"
Get-AppLockerPolicy -Effective |
    Test-AppLockerPolicy -Path C:\Windows\System32\cmd.exe -User "$env:USERDOMAIN\$env:USERNAME"
```

??? example "Sortie"
    ```text
    FilePath                       PolicyDecision MatchingRule
    C:\Windows\System32\cmd.exe     Denied         …
    ```

`-Local` = politique locale ; `-Effective` = fusion des politiques appliquées par GPO. Le résultat dépend de l'utilisateur testé ; vérifier le mode audit/application. Ces cmdlets ne décrivent pas correctement une politique AppLocker déployée par CSP/MDM.

Ensuite : [interpréter les règles AppLocker](systeme.md#consulter-et-tester-la-politique-applocker).
{ .kw-cs-meta }

## Lire les résultats

- **Droits** : groupe Administrators, processus élevé et SYSTEM sont trois notions distinctes. SYSTEM local n'est pas Domain Admin. Un privilège `Disabled` reste présent dans le token ; un privilège absent ne s'active pas simplement.
- **Correctifs et logiciels** : rapprocher build, KB et versions des vulnérabilités applicables. Un inventaire incomplet ou un ancien redémarrage ne démontre pas une faille exploitable.
- **Réseau** : ARP n'est pas un historique de sessions. Une route indique un chemin configuré ; `0.0.0.0` indique une écoute sur toutes les interfaces IPv4. Le pare-feu peut bloquer le trafic dans les deux cas.
- **Durcissement** : vérifier les ACL des programmes et dossiers du `PATH`, réduire les appartenances privilégiées inutiles et examiner les protections désactivées. Une anomalie constitue une piste à valider dans son contexte.

Pour approfondir : [cours complet et outils d'énumération](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md) · [démarche d'élévation locale](../../../privesc/windows.md).
