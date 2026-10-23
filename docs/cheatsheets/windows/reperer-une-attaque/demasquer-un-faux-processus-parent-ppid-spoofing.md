---
title: Démasquer un faux processus parent (PPID spoofing)
source: IT/02 Windows/Repérer une attaque/Démasquer un faux processus parent (PPID spoofing).md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

L'attaquant crée un processus en lui donnant un autre parent que celui qui l'a réellement lancé. Sysmon `1` affiche le faux parent ; le provider ETW `Microsoft-Windows-Kernel-Process` révèle le vrai. Les étapes vont du plus large au plus précis.

Repérer d'abord une filiation anormale : [Repérer une relation parent-enfant anormale](reperer-une-relation-parent-enfant-anormale.md).

## En bref

| | |
|---|---|
| Technique | Usurpation du processus parent (Parent PID Spoofing) |
| MITRE ATT&CK | [T1134.004 — Access Token Manipulation : Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004/) |
| Journaux | `Microsoft-Windows-Sysmon/Operational` ; trace ETW `Microsoft-Windows-Kernel-Process` (SilkETW) |
| Événements | Sysmon `1` (parent apparent) ; ETW Kernel-Process (processus créateur réel) |
| Indice clé | Le parent affiché par Sysmon n'est pas le processus qui a créé l'enfant |

## Le principe

- Le PPID (identifiant du processus parent) se choisit à la création : un processus lancé par PowerShell peut s'afficher comme enfant de `spoolsv.exe`.
- Sysmon `1` enregistre le parent **apparent** : il se laisse tromper.
- ETW `Microsoft-Windows-Kernel-Process` enregistre le processus qui a **réellement** créé l'enfant.

## Chercher, étape par étape

Sur un journal exporté : `Path = '<fichier>.evtx'` ; tout un dossier : `Path = '<dossier>\*.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

### 1. Garder les créations de processus

Observateur : *Filter Current Log…* → Event ID `1`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 1
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


### 2. Retrouver la création suspecte

Observateur : *Find* sur le nom de l'enfant.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 1
} |
    Where-Object { $_.Message -like "*cmd.exe*" } |
    Format-List TimeCreated, Message
```


Relever le `ProcessId` de l'enfant, son parent apparent (`ParentImage`) et l'heure.

### 3. Collecter le provider Kernel-Process avec SilkETW

```
SilkETW.exe -t user -pn Microsoft-Windows-Kernel-Process -ot file -p C:\Windows\Temp\etw.json
```


| Paramètre | Fonction |
|---|---|
| `-t user` | Type de session ETW |
| `-pn` | Nom du fournisseur ETW |
| `-ot file` | Écriture dans un fichier |
| `-p` | Chemin du fichier de sortie |

### 4. Comparer avec la trace ETW

Dans `etw.json`, rechercher le PID relevé à l'étape 2 : l'événement de création indique le processus réellement à l'origine. S'il diffère du parent annoncé par Sysmon, le parent a été falsifié. Commandes ETW : cheat sheet [ETW](/cheatsheets/windows/fondamentaux/logs/etw/).

## Ce qui doit alerter

- Un écart entre le parent annoncé par Sysmon et le processus créateur vu par ETW.
- Une filiation anormale dont le parent annoncé est un service système.

## À ne pas confondre

- Windows change lui-même le parent dans certains cas légitimes : lors d'une élévation UAC, le processus élevé est rattaché au programme qui l'a demandée.
- Un PID est réutilisé après la fin d'un processus : vérifier aussi l'heure.
- ETW ajoute du contexte sans garantir de détecter toutes les formes de PPID spoofing.

## Cas concret

<details markdown="1">
<summary>Cours HTB : cmd.exe lancé par PowerShell, affiché sous spoolsv.exe</summary>

L'outil [psgetsystem](https://github.com/decoder-it/psgetsystem) lance `cmd.exe` depuis PowerShell avec `spoolsv.exe` comme parent apparent :

```
powershell -ep bypass
Import-Module .\psgetsys.ps1
[MyProcess]::CreateProcessFromParent(
    [Process ID of spoolsv.exe],
    "C:\Windows\System32\cmd.exe",
    ""
)
```


Sysmon `1` affiche `spoolsv.exe` → `cmd.exe` :

![Sysmon Event 1 : cmd.exe affiche spoolsv.exe comme parent](../../../library/assets/demasquer-un-faux-processus-parent-ppid-spoofing-htb-windows-event-logs-41.png)

Collecte SilkETW, puis recherche du PID dans `etw.json` : `powershell.exe` est le vrai créateur.

![SilkETW collectant le provider Microsoft-Windows-Kernel-Process](../../../library/assets/demasquer-un-faux-processus-parent-ppid-spoofing-htb-windows-event-logs-42.png)

![etw.json : recherche du PID dans les evenements Kernel-Process](../../../library/assets/demasquer-un-faux-processus-parent-ppid-spoofing-htb-windows-event-logs-43.png)

Les événements SilkETW peuvent aussi être versés dans les journaux Windows via SilkService. Pas de question de lab dédiée dans le module.

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
