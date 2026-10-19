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

Sur un journal exporté : `Path = '<fichier>.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

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


### 3. Lire qui accède

Dans chaque résultat : `SourceImage` (qui), son dossier, `SourceUser` et `GrantedAccess` (avec quels droits).

## Ce qui doit alerter

- Un processus source inhabituel, lancé depuis un dossier comme `Downloads` ou `Temp`.
- Une demande de droits sensibles sur `lsass.exe`, ou l'usage de `SeDebugPrivilege`.

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


![Sysmon Event 10 : AgentEXE.exe accede a lsass.exe](../../assets/reperer-un-acces-a-lsass-htb-windows-event-logs-34.png)

Un exécutable peu connu, venu d'un dossier utilisateur, accède à un processus sensible. Côté attaque, la sortie Mimikatz : un compte `Administrator` et ses hashes.

![image-22](../../assets/reperer-un-acces-a-lsass-image-22.png)

Lab pas à pas : [Sysmon et ETW › Labs › Question 3](sysmon-et-etw/04-labs/01-lab-2-analyser-avec-sysmon.md#question-3-credential-dumping-lsass).

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
