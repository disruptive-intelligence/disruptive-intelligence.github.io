---
title: Repérer un accès à LSASS
source: IT/02 Windows/Repérer une attaque/Repérer un accès à LSASS.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Pour voler des identifiants, l'attaquant lit la mémoire de LSASS, le processus qui gère les authentifications Windows. Les étapes ci-dessous vont du plus large au plus précis : chacune se teste, puis s'affine.

## En bref

| | |
|---|---|
| Technique | Vol d'identifiants dans la mémoire de LSASS (credential dumping) |
| MITRE ATT&CK | [T1003.001 — OS Credential Dumping : LSASS Memory](https://attack.mitre.org/techniques/T1003/001/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` |
| Événement | Sysmon `10` — accès à un processus (ProcessAccess) |
| Indice clé | Un exécutable inhabituel, lancé depuis un dossier utilisateur, qui ouvre `lsass.exe` |

## Le principe

- LSASS (Local Security Authority Subsystem Service) gère les authentifications et les sessions : ses secrets (hashes…) sont en mémoire.
- Un outil comme Mimikatz (`privilege::debug`, puis `sekurlsa::logonpasswords`) ouvre `lsass.exe` pour les lire.
- Trace : Sysmon `10`, qui enregistre les accès entre processus.

| Champ | Ce qu'il donne |
|---|---|
| `SourceImage` | Le processus qui accède |
| `TargetImage` | Le processus ciblé (`lsass.exe`) |
| `SourceUser` / `TargetUser` | Les comptes des deux processus |
| `GrantedAccess` | Les droits obtenus sur la cible |

## Chercher, étape par étape

Sur un journal exporté : `Path = '<fichier>.evtx'` ; tout un dossier : `Path = '<dossier>\*.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

### 1. Garder les accès entre processus

Observateur : *Filter Current Log…* → Event ID `10`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 10
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


Aucun événement 10 ? Vérifier que `ProcessAccess` est collecté dans la configuration Sysmon.

### 2. Chercher les accès à LSASS

Observateur : *Find* sur `lsass.exe`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 10
} |
    Where-Object { $_.Message -like "*lsass.exe*" } |
    Format-List TimeCreated, Message
```


Pour écarter une partie des accès système :

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 10
} |
    Where-Object { $_.Message -match "lsass.exe" -and $_.Message -notmatch "svchost.exe" } |
    Format-List
```


### 3. Lire qui accède

Dans chaque résultat : `SourceImage` (qui), son dossier, `SourceUser` et `GrantedAccess` (avec quels droits). Relever l'heure (`TimeCreated`) de l'accès suspect.

### 4. Et après ? Les connexions qui suivent

Les identifiants volés servent ensuite à se connecter : garder les ouvertures de session (`4624`) postérieures à l'accès.

```powershell
$dumpTime = Get-Date "AAAA-MM-JJ HH:MM:SS"

Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 4624
} |
    Where-Object { $_.TimeCreated -gt $dumpTime } |
    Format-List
```


Lire le Logon Type et le compte : `5` (service, `SYSTEM`) est normal ; `2`, `3`, `9` ou `10` juste après un dump méritent d'être examinés ([Logon Types](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/04-authentification-et-ouvertures-de-session.md#logon-types)).

## Ce qui doit alerter

- Un processus source inhabituel, lancé depuis un dossier comme `Downloads` ou `Temp`.
- Une demande de droits sensibles sur `lsass.exe`, ou l'usage de `SeDebugPrivilege`.
- Une connexion interactive, réseau ou RDP peu après l'accès à LSASS.

## À ne pas confondre

- Composants d'authentification, antivirus et EDR accèdent légitimement à LSASS : les reconnaître avant de conclure.
- `SourceUser` différent de `TargetUser`, ou `SeDebugPrivilege`, ne prouvent rien seuls.
- Un Sysmon `10` est un accès, pas une extraction réussie.

## Cas concret

<details markdown="1">
<summary>Lab HTB : AgentEXE.exe, depuis Downloads, accède à lsass.exe</summary>

```
SourceImage : ...\Downloads\AgentEXE.exe
TargetImage : ...\lsass.exe
SourceUser  : ...\waldo
TargetUser  : NT AUTHORITY\SYSTEM
```


![Sysmon Event 10 : AgentEXE.exe accede a lsass.exe](../../../library/assets/reperer-un-acces-a-lsass-htb-windows-event-logs-34.png)

Un exécutable peu connu, venu d'un dossier utilisateur, accède à un processus sensible. Côté attaque, la sortie Mimikatz : un compte `Administrator` et ses hashes.

![image-22](../../../library/assets/reperer-un-acces-a-lsass-image-22.png)

Lab pas à pas : [Sysmon et ETW › Labs › Question 3](../../../library/it/windows/sysmon-et-etw/04-labs/01-lab-2-analyser-avec-sysmon.md#question-3-credential-dumping-lsass).

</details>

<details markdown="1">
<summary>Skills Assessment : qui a dumpé LSASS, et une connexion a-t-elle suivi ? (C:\Logs\Dump)</summary>

Les accès à LSASS du dossier, puis le processus lancé depuis un dossier utilisateur :

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=10} |
    Where-Object { $_.Message -match "lsass.exe" } |
    Format-List
```


Puis les `4624` postérieurs à l'heure de cet accès (étape 4), en lisant le Logon Type. Méthode pas à pas : [Sysmon et ETW › Labs › Lab 4](../../../library/it/windows/sysmon-et-etw/04-labs/03-lab-4-evaluation-finale-skills-assessment.md), questions 4 et 5.

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
