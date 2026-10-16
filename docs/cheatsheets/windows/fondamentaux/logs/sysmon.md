---
title: "Sysmon et requêtes SIEM"
---

# Sysmon et requêtes SIEM

Ce que Sysmon enregistre et comment le chasser : processus, connexions, requêtes DNS, binaires renommés, accès à LSASS, reconnaissance du domaine, PowerShell encodé ; les mêmes recherches en PowerShell et dans Wazuh.

Les incontournables : `Sysmon 1` · `Sysmon 3` · `Sysmon 22` · `Sysmon 10` · `OriginalFileName` · `rule.groups: sysmon_event1`
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

Pour comprendre : [Outils de collecte de données : Sysmon](../../../../library/cyber/outils/outils-de-threat-hunting/02-outils-de-collecte-de-donnees-data-collection-tool.md)
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

LSASS garde en mémoire des secrets d'authentification : un processus inconnu qui l'ouvre est un signe de vol d'identifiants (T1003.001). Les antivirus, EDR et outils de supervision y accèdent aussi : juger sur `SourceImage`, pas sur l'événement seul.

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

| Event ID | Événement | À retenir en chasse |
|---|---|---|
| **1** | Processus créé | Chemin, ligne de commande, parent, hash, `OriginalFileName` : la base de toute chasse |
| **2** | Date de création d'un fichier modifiée | Timestomping : un attaquant vieillit son fichier |
| **3** | Connexion réseau | Processus → IP:port ; pivot vers le pare-feu et la CTI |
| **5** | Processus terminé | Durée de vie d'un processus (avec le 1) |
| **6** | Pilote chargé | Pilote non signé ou vulnérable (BYOVD) |
| **7** | Image (DLL) chargée | DLL chargée depuis un dossier inhabituel (sideloading) ; très bavard |
| **8** | CreateRemoteThread | Injection de code dans un autre processus |
| **10** | Accès à un processus | Vers `lsass.exe` : vol d'identifiants |
| **11** | Fichier créé | Charge déposée dans `%TEMP%`, `Downloads`, dossier de démarrage |
| **12 / 13 / 14** | Registre : clé créée ou supprimée / valeur écrite / renommée | Persistance (`Run`, `RunOnce`, services) |
| **15** | Flux de données alternatif créé | `Zone.Identifier` : fichier venu d'Internet |
| **17 / 18** | Pipe nommé créé / connecté | Outils de post-exploitation et mouvements latéraux |
| **19 / 20 / 21** | WMI : filtre / consommateur / liaison | Persistance par abonnement WMI |
| **22** | Requête DNS | Domaine résolu **et** processus demandeur |
| **23 / 26** | Fichier supprimé (archivé / seulement détecté) | Nettoyage de traces |
| **25** | Altération de processus | Process hollowing, herpaderping |
| **255** | Erreur Sysmon | Sysmon en difficulté ou altéré |

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
