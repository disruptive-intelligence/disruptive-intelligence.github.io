---
title: Repérer un accès à LSASS
source: IT/02 Windows/Repérer une attaque/Repérer un accès à LSASS.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Pour voler des identifiants, l'attaquant lit la mémoire de LSASS, le processus qui gère les authentifications Windows. Cette fiche montre comment repérer ces accès dans les événements Sysmon `10` et les distinguer des accès légitimes.

Installer et configurer Sysmon : [Sysmon et ETW](sysmon-et-etw/index.md).

## En bref

| | |
|---|---|
| Technique | Vol d'identifiants dans la mémoire de LSASS (credential dumping) |
| MITRE ATT&CK | [T1003.001 — OS Credential Dumping : LSASS Memory](https://attack.mitre.org/techniques/T1003/001/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` |
| Événement | Sysmon `10` — accès à un processus (ProcessAccess) |
| Indice clé | Un exécutable inhabituel, lancé depuis un dossier utilisateur, qui ouvre `lsass.exe` |

## Comprendre l'attaque

Le credential dumping consiste à extraire des secrets d'authentification d'un système compromis. Sous Windows, LSASS (Local Security Authority Subsystem Service) est une cible fréquente : il intervient dans la gestion des authentifications et des sessions de sécurité.

### Mimikatz & LSASS

Mimikatz examine certaines informations d'authentification Windows. Deux commandes :

| Commande Mimikatz          | Fonction                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| `privilege::debug`         | Tenter d'activer `SeDebugPrivilege`                                |
| `sekurlsa::logonpasswords` | Examiner certains secrets liés aux sessions de connexion via LSASS |

Selon la configuration et les protections Windows, les résultats peuvent comprendre des hashes ou d'autres informations d'authentification. Sa sortie montre ici un compte `Administrator` et des valeurs de hash, certains champs de mots de passe apparaissant comme `(null)`.

![image-22](../../assets/reperer-un-acces-a-lsass-image-22.png)

L'accès à LSASS et la réussite de l'extraction dépendent des privilèges et des mécanismes de protection en place.

## Les traces

### Sysmon Event ID 10 — accès à un processus (ProcessAccess)

L'Event ID 10 enregistre les accès entre processus : c'est lui qui signale un accès à LSASS.

![Documentation Sysmon de l'Event ID 10 ProcessAccess](../../assets/reperer-un-acces-a-lsass-htb-windows-event-logs-33.png)

| Champ         | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| SourceImage   | Processus à l'origine de l'accès                                   |
| TargetImage   | Processus ciblé                                                    |
| SourceUser    | Compte associé au processus source                                 |
| TargetUser    | Compte associé au processus cible                                  |
| GrantedAccess | Droits d'accès accordés au processus cible                         |
| CallTrace     | Informations sur la chaîne d'appels, lorsqu'elles sont disponibles |

### Exemple — AgentEXE.exe → lsass.exe

Un exécutable inhabituel, `AgentEXE.exe`, situé dans un répertoire `Downloads`, accède à `lsass.exe` :

```
SourceImage : ...\Downloads\AgentEXE.exe
TargetImage : ...\lsass.exe
SourceUser  : ...\waldo
TargetUser  : NT AUTHORITY\SYSTEM
```


![Sysmon Event 10 : AgentEXE.exe accede a lsass.exe](../../assets/reperer-un-acces-a-lsass-htb-windows-event-logs-34.png)

Cette activité est suspecte : un exécutable peu connu, venu d'un dossier utilisateur, accède à un processus sensible.

## Les requêtes

**1. Tous les accès à LSASS** : Event ID 10 dont la cible est `lsass.exe`.

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=10]
        and EventData[
          Data[@Name='TargetImage']='C:\Windows\system32\lsass.exe'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


- Copier la valeur de `TargetImage` depuis la vue XML d'un événement 10 : l'égalité est stricte.
- Dans chaque résultat, lire `SourceImage` (qui accède), `SourceUser` et `GrantedAccess` (avec quels droits).
- Aucun événement 10 ? Vérifier que `ProcessAccess` est collecté dans la configuration Sysmon (même logique que [Configurer la collecte (ImageLoad)](sysmon-et-etw/01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md#configurer-la-collecte-imageload)).

**2. Écarter les accès attendus** : garder les processus source situés hors de `C:\Windows\` et `C:\Program Files\` (le XML ne sait pas faire « hors de ») :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' `
    -FilterXPath "*[System[EventID=10] and EventData[Data[@Name='TargetImage']='C:\Windows\system32\lsass.exe']]" |
    ForEach-Object {
        $data = ([xml]$_.ToXml()).Event.EventData.Data
        [PSCustomObject]@{
            Heure         = $_.TimeCreated
            SourceImage   = ($data | Where-Object Name -eq 'SourceImage').'#text'
            SourceUser    = ($data | Where-Object Name -eq 'SourceUser').'#text'
            GrantedAccess = ($data | Where-Object Name -eq 'GrantedAccess').'#text'
        }
    } |
    Where-Object { $_.SourceImage -notlike 'C:\Windows\*' -and $_.SourceImage -notlike 'C:\Program Files*' }
```


- Dans l'exemple, `AgentEXE.exe` lancé depuis `Downloads` ressort ainsi.

**3. Dans un journal exporté (.evtx)** : les accès à LSASS, regroupés par processus source.

```powershell
$id10 = Get-WinEvent -FilterHashtable @{ Path = '.\Sysmon.evtx'; Id = 10 }

$id10 | Where-Object { $_.Message -like '*TargetImage:*lsass.exe*' } |
    Select-Object -First 20 | Format-List TimeCreated, Message

$id10 | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data
    [pscustomobject]@{
        SourceImage = ($data | Where-Object Name -eq 'SourceImage').'#text'
        TargetImage = ($data | Where-Object Name -eq 'TargetImage').'#text'
    }
} | Where-Object TargetImage -like '*\lsass.exe' |
    Group-Object SourceImage | Sort-Object Count | Select-Object Count, Name
```


- Les composants système accèdent à LSASS souvent et régulièrement ; un exécutable vu une ou deux fois, depuis `Downloads` ou `Temp`, remonte en tête.
- Démarche complète sur un `.evtx` : [Explorer un fichier .evtx inconnu, pas à pas](analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#explorer-un-fichier-evtx-inconnu-pas-a-pas).

Gabarits et pièges du XML : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

## Les indicateurs

- Processus source inattendu (Unexpected Source Process) : programme inhabituel accédant à LSASS.
- Emplacement suspect (Suspicious File Location) : exécutable provenant d'un dossier comme `Downloads`.
- Processus cible sensible (Sensitive Target Process) : accès à `lsass.exe`.
- Accès privilégié (Privileged Process Access) : demande ou obtention de droits sensibles.
- Privilège de débogage (Debug Privilege Usage) : éventuelle utilisation de `SeDebugPrivilege`.

```
Unknown Executable
       ↓
Access to lsass.exe
       ↓
Sysmon Event ID 10
       ↓
Investigate Credential Dumping
```


## Les faux positifs

- Des processus légitimes accèdent à LSASS, notamment des composants d'authentification et des solutions antivirus / EDR ; un antivirus ou un EDR installé hors des dossiers standards ressort aussi de la requête 2 : le reconnaître avant de conclure.
- `SourceUser` différent de `TargetUser` ne prouve pas une compromission.
- La présence de `SeDebugPrivilege` ne prouve pas un vol d'identifiants, et toutes les techniques n'en ont pas besoin.
- ProcessAccess ≠ extraction réussie : l'Event ID 10 signale un accès entre processus, pas nécessairement une extraction réussie.

L'analyse intègre l'identité du processus, son chemin, ses droits d'accès et les événements associés.

## Pour s'entraîner

- Lab pas à pas : [Sysmon et ETW › Labs › Question 3 — Credential dumping : LSASS](sysmon-et-etw/04-labs/01-lab-2-analyser-avec-sysmon.md#question-3-credential-dumping-lsass).
- Event IDs Sysmon et requêtes SIEM : cheat sheet [Sysmon](/cheatsheets/windows/fondamentaux/logs/sysmon/).

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
