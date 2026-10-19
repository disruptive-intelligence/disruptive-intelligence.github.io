---
title: "Sysmon et requêtes SIEM"
---

# Sysmon et requêtes SIEM

Ce que Sysmon enregistre et comment le chasser : processus, connexions, requêtes DNS, fichiers créés, clés Run, chaîne des parents, binaires renommés, accès à LSASS, reconnaissance du domaine, PowerShell encodé ; sur la machine, dans un journal exporté (`.evtx`) et dans Wazuh.

Les incontournables : `Sysmon 1` · `Sysmon 3` · `Sysmon 11` · `Sysmon 13` · `Sysmon 22` · `Get-WinEvent -Path` · `OriginalFileName` · `rule.groups: sysmon_event1`
{ .kw-cs-top }

## Lire Sysmon

### Vérifier que Sysmon tourne et lire ses événements

```powershell title="Commande"
Get-Service Sysmon64, Sysmon -ErrorAction SilentlyContinue                                # installé ? démarré ?
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'} -MaxEvents 20
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'} -MaxEvents 500 |
    Group-Object Id | Sort-Object Count -Descending | Select-Object Name, Count   # quels Event IDs remontent
```

??? example "Sortie"
    ```text
    Name Count
    ---- -----
    1      214
    3      131
    22      98
    11      41
    13      16
    ```

Sysmon n'est pas installé par défaut (`sysmon64 -accepteula -i config.xml`). Ce qu'il journalise dépend entièrement de sa **configuration** : un Event ID absent veut souvent dire « non configuré », pas « rien ne s'est passé ».

Pour comprendre : [Outils de collecte de données : Sysmon](../../../../library/cyber/detection/outils-de-threat-hunting/02-outils-de-collecte-de-donnees-data-collection-tool.md)
{ .kw-cs-meta }

### Configurer ce que Sysmon collecte

```powershell title="Commande"
sysmon64 -c                                   # affiche la configuration active (console administrateur)
sysmon64 -c C:\Outils\sysmonconfig.xml        # applique une nouvelle configuration, sans réinstaller
```

```xml title="Exemple — enregistrer tous les chargements de DLL (Event ID 7)"
<ImageLoad onmatch="exclude">
</ImageLoad>
```

```powershell title="Exemple 2 — vérifier que les Event ID 7 remontent"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=7} -MaxEvents 5 | Select-Object TimeCreated, Id
```

Chaque type d'événement a son bloc dans le XML (`ProcessCreate`, `NetworkConnect`, `ImageLoad`…) avec un attribut `onmatch` :

| Bloc | Sans règle à l'intérieur | Avec des règles |
|---|---|---|
| `onmatch="include"` | **Rien** n'est enregistré | Seul ce qui correspond est enregistré |
| `onmatch="exclude"` | **Tout** est enregistré | Tout, sauf ce qui correspond |

Beaucoup de configurations de départ (dont SwiftOnSecurity) livrent `ImageLoad` en `include` vide : aucun Event ID 7. Pour voir les chargements de DLL (DLL hijacking, runtime .NET dans un processus inattendu), passer `ImageLoad` en `exclude`, puis recharger la configuration avec `sysmon64 -c`. C'est très bavard : sur un lab, ou avec des exclusions ciblées (DLL signées Microsoft, processus connus) en production.

Pour comprendre : [Configurer la collecte (ImageLoad)](../../../../library/it/windows/sysmon-et-etw/01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md#configurer-la-collecte-imageload)
{ .kw-cs-meta }

### Lire un journal Sysmon exporté

```powershell title="Commande"
Get-WinEvent -Path 'C:\Cas\sysmon.evtx' -FilterXPath "*[System[EventID=3]]"                                             # un Event ID
Get-WinEvent -Path 'C:\Cas\sysmon.evtx' -FilterXPath "*[System[EventID=3] and EventData[Data[@Name='DestinationPort']='22']]"   # + la valeur d'un champ
```

```powershell title="Exemple"
Get-WinEvent -Path 'C:\Cas\sysmon.evtx' -FilterXPath "*[System[EventID=3] and EventData[Data[@Name='DestinationIp']='203.0.113.50']]" |
    ForEach-Object { ([xml]$_.ToXml()).Event.EventData.Data | Where-Object Name -eq 'Image' | Select-Object -ExpandProperty '#text' }
```

??? example "Sortie"
    ```text
    C:\Windows\Temp\plink.exe
    ```

Un `.evtx` exporté (copie d'un poste, pièce d'enquête) se lit hors de la machine : `-Path` remplace `-FilterHashtable @{LogName=…}`. Le filtre XPath vise un **champ** (`EventData[Data[@Name='…']='…']`) : l'égalité doit être exacte. Pour lire un champ, passer par le XML de l'événement (`[xml]$_.ToXml()`). Dans l'Observateur d'événements : *Open Saved Log…*, puis *Filter Current Log…* (Event ID) et *Find…* (`CTRL + F`) pour une valeur.

??? example "Cas concret : quel processus communique avec l'IP signalée par la CTI ?"
    ```powershell
    # Sysmon 3 vers l'IP, puis le champ Image : ici un client SSH (port 22) lancé depuis C:\Windows\Temp = tunnel sortant
    Get-WinEvent -Path 'C:\Users\LetsDefend\Desktop\sysmon.evtx' -FilterXPath "*[System[EventID=3] and EventData[Data[@Name='DestinationIp']='<IP>']]" |
        ForEach-Object { ([xml]$_.ToXml()).Event.EventData.Data | Where-Object Name -eq 'Image' | Select-Object -ExpandProperty '#text' }
    ```
    [Lab DFIR avec l'EDR, question 1](../../../../library/cyber/forensic/dfir-avec-l-edr/05-lab-analyse-d-un-journal-sysmon-exporte.md#question-1-le-processus-qui-communique-avec-lip-signalee-par-la-cti)

Pour comprendre : [Lab — analyse d'un journal Sysmon exporté](../../../../library/cyber/forensic/dfir-avec-l-edr/05-lab-analyse-d-un-journal-sysmon-exporte.md) · [Lire, filtrer et exporter les journaux](lire.md) · [Tout un dossier de .evtx](lire.md#lire-tous-les-journaux-dun-dossier)
{ .kw-cs-meta }

## Chasser avec Sysmon

### Retrouver les requêtes DNS d'un processus

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=22}   # DNSEvent : domaine résolu, par quel processus
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=22} -MaxEvents 300 |
    Where-Object Message -match 'Image:.*\\Downloads\\' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Dns query:
    UtcTime: 2026-10-02 07:16:44.902
    ProcessId: 6120
    QueryName: pool.mining-example.net
    QueryStatus: 0
    QueryResults: ::ffff:203.0.113.25;
    Image: C:\Users\alice\Downloads\miner.exe
    User: MERIDIAN\alice
    ```

Le **22** relie un nom de domaine au processus qui l'a demandé, ce que les journaux du serveur DNS ne savent pas faire. Un exécutable dans `Downloads`, `%TEMP%` ou `%APPDATA%` qui résout un domaine inconnu : passer le domaine en CTI.

```text title="Wazuh (DQL)"
data.win.system.eventID: 22 and data.win.eventdata.image: *miner.exe*
```

Pour comprendre : [Threat hunting avec l'EDR : lab 1](../../../../library/cyber/detection/threat-hunting-avec-l-edr/04-labs-chasse-aux-menaces-dans-wazuh.md#lab-1-malware-de-minage)
{ .kw-cs-meta }

### Retrouver les connexions réseau d'un processus

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=3}   # NetworkConnect : processus → IP:port
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=3} -MaxEvents 300 |
    Where-Object Message -match 'Image:.*\\Windows\\Temp\\' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Network connection detected:
    Image: C:\Windows\Temp\malware.exe
    User: MERIDIAN\alice
    Protocol: tcp
    Initiated: true
    SourceIp: 10.0.20.15
    DestinationIp: 203.0.113.80
    DestinationPort: 443
    ```

Croiser avec le pare-feu : une connexion **bloquée** ne veut pas dire poste sain, le programme a tourné.

```text title="Wazuh (DQL)"
rule.groups: sysmon_event3 and data.win.eventdata.image: *malware.exe*
rule.groups: firewall and data.dstip: "203.0.113.80"
```

Pour comprendre : [Threat hunting avec l'EDR : lab 2](../../../../library/cyber/detection/threat-hunting-avec-l-edr/04-labs-chasse-aux-menaces-dans-wazuh.md#lab-2-powershell-encode)
{ .kw-cs-meta }

### Démasquer un binaire renommé

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} |
    Where-Object Message -match 'OriginalFileName: (nltestrk|wevtutil|certutil|PsExec)\.(exe|c)'   # l'outil, quel que soit son nom
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 1000 |
    Where-Object Message -match 'OriginalFileName: nltestrk\.exe' |
    Select-Object -First 1 TimeCreated, @{n='Image';e={($_.Message -split "`n" | Select-String '^Image:').Line}}
```

??? example "Sortie"
    ```text
    TimeCreated          Image
    -----------          -----
    02/10/2026 09:41:12  Image: C:\Users\Public\svc.exe
    ```

Sysmon 1 donne `OriginalFileName`, le nom inscrit dans le binaire à la compilation. Si l'outil est renommé, `Image` change mais pas `OriginalFileName`. Attention : ce nom interne n'est pas toujours le nom du fichier : celui de `nltest.exe` est **`nltestrk.exe`**.

```text title="Wazuh (DQL)"
data.win.eventdata.originalFileName: "nltestrk.exe"
```

### Repérer une reconnaissance du poste et du domaine

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} |
    Where-Object Message -match 'CommandLine:.*(nltest|net(1)?(\.exe)? (user|group|localgroup)|whoami|ifconfig\.me)'
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 1000 |
    Where-Object Message -match 'CommandLine:.*nltest' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Process Create:
    Image: C:\Windows\System32\nltest.exe
    OriginalFileName: nltestrk.exe
    CommandLine: nltest  /dclist:meridian.local
    User: MERIDIAN\alice
    ParentImage: C:\Windows\System32\cmd.exe
    ```

| Commande | Ce que cherche l'attaquant | ATT&CK |
|---|---|---|
| `net user` | Comptes locaux | T1087.001 |
| `net group "Domain Admins" /domain` | Comptes et groupes du domaine | T1087.002 |
| `nltest /dclist:<domaine>` | Contrôleurs de domaine | T1018 |
| `curl ifconfig.me` | IP publique de sortie | T1016.001 |

Une commande seule ne prouve rien (un administrateur fait la même chose) ; plusieurs en quelques minutes, par un compte utilisateur, depuis `cmd.exe` ou `powershell.exe`, dessinent une reconnaissance. Sans Sysmon : le **4688** avec la ligne de commande.

```text title="Wazuh (DQL)"
data.win.eventdata.commandLine: *nltest*
rule.groups: windows and rule.mitre.id: T1087.001
```

Pour comprendre : [Threat hunting avec l'EDR : lab 3](../../../../library/cyber/detection/threat-hunting-avec-l-edr/04-labs-chasse-aux-menaces-dans-wazuh.md#lab-3-reconnaissance-et-effacement-des-journaux) · [Comptes, groupes et DC : nltest](../../administration/active-directory/kerberos-dc.md)
{ .kw-cs-meta }

### Retrouver qui a créé un fichier

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=11}   # FileCreate : fichier créé et processus créateur
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=11} -MaxEvents 500 |
    Where-Object Message -match 'TargetFilename:.*\\Startup\\' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    File created:
    ProcessId: 4632
    Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
    TargetFilename: C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ncat.ps1
    User: TESTPC\admin
    ```

Le **11** relie un fichier (`TargetFilename`) au processus qui l'a créé (`ProcessId`, `Image`). Dossiers à surveiller : **Startup** (exécuté à chaque ouverture de session, T1547.001), `%TEMP%`, `Downloads`, `C:\Users\Public`.

??? example "Cas concret : quel processus a déposé un script dans le dossier Démarrage ?"
    ```powershell
    Get-WinEvent -Path 'C:\Users\LetsDefend\Desktop\sysmon.evtx' -FilterXPath "*[System[EventID=11] and EventData[Data[@Name='TargetFilename']='C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ncat.ps1']]" |
        Select-Object -ExpandProperty Message   # lire ProcessId et Image
    ```
    [Lab DFIR avec l'EDR, question 2](../../../../library/cyber/forensic/dfir-avec-l-edr/05-lab-analyse-d-un-journal-sysmon-exporte.md#question-2-le-processus-qui-depose-un-script-dans-le-dossier-demarrage)

### Remonter la chaîne des processus parents

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} |
    Where-Object Message -match 'ProcessId: 8264\r?\n'   # le Sysmon 1 du parent, par son ProcessId
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 1000 |
    Where-Object Message -like '*procdump.zip*' |
    ForEach-Object { $d = @{}; ([xml]$_.ToXml()).Event.EventData.Data | ForEach-Object { $d[$_.Name] = $_.'#text' }
                     [pscustomobject]@{ Image = $d.Image; ParentProcessId = $d.ParentProcessId; ParentImage = $d.ParentImage } }
```

??? example "Sortie"
    ```text
    Image                          ParentProcessId ParentImage
    -----                          --------------- -----------
    C:\Windows\SysWOW64\curl.exe   8264            C:\Windows\SysWOW64\cmd.exe
    ```

Méthode : Sysmon 1 de l'activité suspecte → `ParentProcessId` → Sysmon 1 de ce parent → son `ParentImage`, jusqu'à un processus qui explique l'entrée. Lecture du sommet de la chaîne : serveur web (`httpd.exe`, `w3wp.exe`) = application web exploitée ; `WINWORD.EXE` / `EXCEL.EXE` = document piégé ; `explorer.exe` = lancement par l'utilisateur. Un `ProcessId` est réutilisé par Windows : vérifier aussi l'heure, ou suivre le `ProcessGuid` / `ParentProcessGuid`, uniques.

??? example "Cas concret : qui a lancé le cmd.exe qui a téléchargé procdump.zip ?"
    ```powershell
    # 1. le téléchargement (curl) et son ParentProcessId
    Get-WinEvent -Path 'C:\Users\LetsDefend\Desktop\sysmon.evtx' | Where-Object { $_.Id -eq 1 -and $_.Message -like '*procdump.zip*' } |
        Select-Object -ExpandProperty Message
    # 2. le Sysmon 1 du cmd.exe parent, puis son ParentImage : httpd.exe (Apache) = commandes passées par l'application web
    Get-WinEvent -Path 'C:\Users\LetsDefend\Desktop\sysmon.evtx' -FilterXPath "*[System[EventID=1] and EventData[Data[@Name='ProcessId']='<ParentProcessId>']]" |
        Select-Object -ExpandProperty Message
    ```
    [Lab DFIR avec l'EDR, questions 3 et 4](../../../../library/cyber/forensic/dfir-avec-l-edr/05-lab-analyse-d-un-journal-sysmon-exporte.md#question-4-le-parent-du-cmdexe-qui-a-lance-le-telechargement)

### Repérer une persistance par clé Run

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=12,13,14} |
    Where-Object Message -match 'TargetObject:.*\\CurrentVersion\\Run'   # registre : clé créée/supprimée, valeur écrite, renommée
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=13} -MaxEvents 500 |
    Where-Object Message -match 'TargetObject:.*\\CurrentVersion\\Run' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Registry value set:
    RuleName: technique_id=T1547.001,technique_name=Registry Run Keys / Start Folder
    EventType: SetValue
    Image: C:\Windows\system32\reg.exe
    TargetObject: HKU\S-1-5-21-…-1001\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\RvcX App
    Details: C:\windows\temp\rvcx.exe
    ```

Le **13** donne la clé (`TargetObject`), le programme qui sera lancé (`Details`) et l'outil qui l'a écrit (`Image`). Sous HKCU, la clé apparaît avec le SID de l'utilisateur (`HKU\S-1-5-21-…`). Un programme dans `C:\Windows\Temp` ajouté à `Run` par `reg.exe` : persistance (T1547.001). Voir aussi [ce qui démarre avec Windows](../registre.md).

??? example "Cas concret : quel programme est lancé à chaque démarrage ?"
    ```powershell
    # Sysmon 13 sous ...\CurrentVersion\Run : lire Details (le programme) et Image (qui l'a écrit)
    Get-WinEvent -Path 'C:\Users\LetsDefend\Desktop\sysmon.evtx' -FilterXPath "*[System[EventID=13]]" |
        Where-Object Message -match 'CurrentVersion\\Run' | Select-Object -ExpandProperty Message
    ```
    [Lab DFIR avec l'EDR, question 5](../../../../library/cyber/forensic/dfir-avec-l-edr/05-lab-analyse-d-un-journal-sysmon-exporte.md#question-5-le-programme-lance-a-chaque-demarrage-cle-run)

### Repérer un DLL hijacking dans un journal exporté

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{ Path = "<fichier>.evtx"; Id = 7 } |
    Where-Object { $_.Message -like "*<DLL>*" } | Format-List TimeCreated, Message
```

```powershell title="Exemple — une DLL à examiner"
Get-WinEvent -FilterHashtable @{
    Path = ".\DLLHijack.evtx"
    Id   = 7
} |
    Where-Object { $_.Message -like "*NOM_DLL.dll*" } |
    Format-List TimeCreated, Message
```

```powershell title="Exemple 2 — réduire le bruit : filtrer sur un dossier (Temp)"
Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} |
    Where-Object { $_.Message -like '*ImageLoaded:*Temp\*' } |
    Format-List TimeCreated, Message
```

```powershell title="Exemple 3 — les DLL non signées"
Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} |
Where-Object { $_.Message -match 'Signed: false' } |
Select-Object -First 20 |
Format-List TimeCreated, Message
```

```powershell title="Exemple 4 — compter les associations processus / DLL"
$events = Get-WinEvent -FilterHashtable @{
    Path = '.\DLLHijack.evtx'
    Id   = 7
} | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data

    [pscustomobject]@{
        Image       = ($data | Where-Object Name -eq 'Image').'#text'
        ImageLoaded = ($data | Where-Object Name -eq 'ImageLoaded').'#text'
    }
}

$events |
    Group-Object Image, ImageLoaded |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```

Sysmon 7 : `Image` = processus qui charge une DLL, `ImageLoaded` = chemin de la DLL chargée. Pour voir d'abord ce que contient le fichier : [Découvrir le contenu d'un fichier .evtx](lire.md#decouvrir-le-contenu-dun-fichier-evtx).

Pour comprendre : [Repérer un DLL hijacking](../../../../library/it/windows/reperer-un-dll-hijacking.md) · [Analyser un fichier .evtx : l'exemple du DLL hijacking](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#analyser-un-fichier-evtx-lexemple-du-dll-hijacking)
{ .kw-cs-meta }

### Repérer une injection de thread

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=8} | Format-List
```

```powershell title="Exemple — tout un dossier de journaux exportés"
Get-WinEvent -FilterHashtable @{Path='C:\Logs\PowershellExec\*.evtx'; Id=8} | Format-List
```

Sysmon `8` (CreateRemoteThread) : un processus crée un thread dans un autre, signe d'injection de code. `SourceImage` = le processus qui injecte, `TargetImage` = la victime. Observateur : *Filter Current Log…* → `8`. Avec du PowerShell non managé, la victime est aussi celle qui charge `clrjit.dll` (Sysmon `7`).

??? example "Cas concret : quel processus a injecté du code dans la victime du PowerShell non managé ?"
    ```powershell
    # 1. la victime : le processus, autre que powershell.exe, qui charge clrjit.dll
    Get-WinEvent -Path "C:\Logs\PowershellExec\*.evtx" |
        Where-Object { $_.Id -eq 7 -and $_.Message -match "clrjit.dll" } |
        Select-Object -ExpandProperty Message
    # 2. l'injecteur : le SourceImage du Sysmon 8 qui la vise
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\PowershellExec\*.evtx'; Id=8} | Format-List
    ```
    [Skills Assessment, questions 2 et 3](../../../../library/it/windows/sysmon-et-etw/04-labs/03-lab-4-evaluation-finale-skills-assessment.md#question-2-powershell-non-manage-le-processus-victime)

Pour comprendre : [Repérer du PowerShell non managé](../../../../library/it/windows/reperer-du-powershell-non-manage.md#5-trouver-qui-a-injecte)
{ .kw-cs-meta }

### Repérer un accès à la mémoire de LSASS

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=10} |
    Where-Object Message -match 'TargetImage:.*lsass\.exe'   # ProcessAccess vers LSASS
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=10} -MaxEvents 500 |
    Where-Object Message -match 'TargetImage:.*lsass\.exe' | Select-Object -First 1 -ExpandProperty Message
```

??? example "Sortie"
    ```text
    Process accessed:
    SourceImage: C:\Users\alice\AppData\Local\Temp\p.exe
    TargetImage: C:\Windows\system32\lsass.exe
    GrantedAccess: 0x1010
    ```

```powershell title="Exemple 2 — tout un dossier, sans les accès de svchost.exe"
Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=10} |
    Where-Object { $_.Message -match "lsass.exe" -and $_.Message -notmatch "svchost.exe" } |
    Format-List
```

LSASS garde en mémoire des secrets d'authentification : un processus inconnu qui l'ouvre est un signe de vol d'identifiants (T1003.001). Les antivirus, EDR et outils de supervision y accèdent aussi : juger sur `SourceImage`, pas sur l'événement seul.

??? example "Cas concret : qui a dumpé LSASS, et une connexion a-t-elle suivi ?"
    ```powershell
    # 1. l'accès à LSASS : le SourceImage lancé depuis un dossier utilisateur, et son heure
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=10} |
        Where-Object { $_.Message -match "lsass.exe" } | Format-List
    # 2. les ouvertures de session après cette heure : lire le Logon Type
    $dumpTime = Get-Date "AAAA-MM-JJ HH:MM:SS"
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=4624} |
        Where-Object { $_.TimeCreated -gt $dumpTime } | Format-List
    ```
    [Skills Assessment, questions 4 et 5](../../../../library/it/windows/sysmon-et-etw/04-labs/03-lab-4-evaluation-finale-skills-assessment.md#question-4-qui-a-dumpe-lsass)

Pour comprendre : [Repérer un accès à LSASS](../../../../library/it/windows/reperer-un-acces-a-lsass.md)
{ .kw-cs-meta }

### Décoder une commande PowerShell encodée

```powershell title="Commande"
[Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('<chaîne après -EncodedCommand>'))   # Base64 de texte UTF-16LE
```

```powershell title="Exemple"
[Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('dwBoAG8AYQBtAGkA'))
```

??? example "Sortie"
    ```text
    whoami
    ```

Un décodage Base64 « simple » affiche des caractères séparés par des points : c'est de l'UTF-16LE. Dans CyberChef : `From Base64` puis `Decode text` (UTF-16LE). Variantes à chercher : `-EncodedCommand`, `-enc`, `-e`.

```text title="Wazuh (DQL)"
rule.groups: sysmon_event1 and data.win.eventdata.commandLine: *EncodedCommand*
```

Pour comprendre : [Processus et PowerShell](processus-powershell.md#retrouver-les-scripts-powershell-executes)
{ .kw-cs-meta }

## Vue d'ensemble : les Event IDs Sysmon

Tous dans Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational.

| Event ID | Événement | Intérêt |
|---|---|---|
| **1** | Process Creation | Processus exécutés et leur contexte : chemin, ligne de commande, parent, hash, `OriginalFileName` ; la base de toute chasse |
| **2** | File Creation Time Changed | Timestamps de fichiers modifiés (timestomping : un attaquant vieillit son fichier) |
| **3** | Network Connection | Connexions réseau d'un processus : IP et port de destination ; pivot vers le pare-feu et la CTI |
| **4** | Sysmon Service State Changed | Changements d'état du service Sysmon (arrêt = perte de visibilité) |
| **5** | Process Terminated | Fin d'exécution d'un processus ; durée de vie avec le 1 |
| **6** | Driver Loaded | Pilotes chargés : non signé ou vulnérable (BYOVD) |
| **7** | Image Loaded | DLL et modules chargés par un processus : DLL depuis un dossier inhabituel (sideloading) ; très bavard |
| **8** | CreateRemoteThread | Thread créé dans un autre processus : injection de code |
| **9** | RawAccessRead | Accès direct à un volume ou un disque (lecture hors du système de fichiers) |
| **10** | ProcessAccess | Accès d'un processus à un autre : vers `lsass.exe`, vol d'identifiants |
| **11** | File Create | Fichiers créés et processus créateur : charge déposée dans `%TEMP%`, `Downloads`, dossier Startup |
| **12** | Registry Event (Object create and delete) | Clés et valeurs du registre créées ou supprimées |
| **13** | Registry Value Set | Valeurs écrites : persistance (`Run`, `RunOnce`, services) |
| **14** | Registry Object Renamed | Clés et valeurs renommées |
| **15** | File Create Stream Hash | Flux de données alternatifs (ADS) : `Zone.Identifier` = fichier venu d'Internet |
| **16** | Sysmon Configuration Change | Configuration de Sysmon modifiée (règles affaiblies ?) |
| **17** | Pipe Created | Named Pipes créés : outils de post-exploitation |
| **18** | Pipe Connected | Connexions à des Named Pipes : mouvements latéraux |
| **19** | WMI Event Filter | Filtre WMI : persistance par abonnement WMI |
| **20** | WMI Event Consumer | Consommateur WMI : l'action exécutée |
| **21** | WMI Consumer-to-Filter | Liaison filtre ↔ consommateur : l'abonnement actif |
| **22** | DNS Query | Requêtes DNS **et** processus demandeur |
| **23** | FileDelete | Fichiers supprimés, avec archivage si configuré : nettoyage de traces |
| **24** | Clipboard Change | Modifications du presse-papiers |
| **25** | Process Tampering | Altérations de processus : process hollowing, herpaderping |
| **26** | FileDeleteDetected | Fichiers supprimés, sans archivage |
| **27** | FileBlockExecutable | Création d'exécutables PE bloquée |
| **28** | FileBlockShredding | Destruction sécurisée de fichiers bloquée |
| **29** | FileExecutableDetected | Nouveaux exécutables PE détectés |
| **255** | Error | Sysmon en difficulté ou altéré |

| Type d'analyse | Event IDs |
|---|---|
| Processus | 1, 5, 7, 8, 10, 25 |
| Réseau | 3, 22 |
| Fichiers | 2, 11, 15, 23, 26, 27, 28, 29 |
| Persistance | 12 – 14, 17 – 21 |
| Intégrité de la surveillance | 4, 16, 255 |

Sysmon n'enregistre pas tous ces événements par défaut : leur présence dépend de la version et de la configuration. Pour comprendre : [Principaux Sysmon Event IDs](../../../../library/cyber/forensic/dfir-avec-l-edr/01-dfir-with-edr-configuring-edr-tools-for-effective.md#principaux-sysmon-event-ids)

| Chercher dans Wazuh | Requête DQL |
|---|---|
| Processus (Sysmon 1) | `rule.groups: sysmon_event1` |
| Connexions (Sysmon 3) | `rule.groups: sysmon_event3` |
| Un Event ID précis | `data.win.system.eventID: 22` |
| Une ligne de commande | `data.win.eventdata.commandLine: *nltest*` |
| Un outil renommé | `data.win.eventdata.originalFileName: "nltestrk.exe"` |
| Une technique ATT&CK | `rule.mitre.id: T1070.001` |
| Un hash ou un mot partout | `*<hash>*` (étoiles autour du mot) |

Chaîne typique : 1 (processus) → 22 (domaine) → 3 (connexion) → 11 / 13 (dépôt, persistance).
