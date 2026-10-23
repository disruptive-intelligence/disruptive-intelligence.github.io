---
title: Repérer du PowerShell non managé
source: IT/02 Windows/Repérer une attaque/Repérer du PowerShell non managé.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Du code PowerShell ou C# est injecté dans un processus qui n'utilise pas .NET : le runtime .NET (CLR) s'y charge alors de façon inattendue. Les étapes ci-dessous vont du plus large au plus précis : chacune se teste, puis s'affine.

## En bref

| | |
|---|---|
| Technique | PowerShell non managé (Unmanaged PowerShell) / injection de code C# dans un processus |
| MITRE ATT&CK | [T1055 — Process Injection](https://attack.mitre.org/techniques/T1055/), [T1059.001 — PowerShell](https://attack.mitre.org/techniques/T1059/001/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` |
| Événements | Sysmon `7` — chargement d'image (Image Loaded) ; Sysmon `8` — CreateRemoteThread (l'injecteur) |
| Indice clé | `clr.dll` / `clrjit.dll` chargées par un processus natif qui n'utilise pas .NET |

## Le principe

- Le code C# s'exécute dans le runtime .NET : `clr.dll` (Common Language Runtime) et `clrjit.dll` (compilation Just-In-Time) se chargent dans le processus.
- Normal dans un processus .NET (PowerShell, outils d'administration) ; inattendu dans un processus natif : signe d'une attaque [execute-assembly](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) ou d'une [injection de PowerShell non managé](https://www.youtube.com/watch?v=7tvfb9poTKg&ab_channel=RaphaelMudge).
- Trace : Sysmon `7`, si la collecte `ImageLoad` est activée ([Configurer la collecte (ImageLoad)](../../../library/it/windows/sysmon-et-etw/01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md#configurer-la-collecte-imageload)).

## Chercher, étape par étape

Sur un journal exporté : `Path = '<fichier>.evtx'` ; tout un dossier : `Path = '<dossier>\*.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

### 1. Sur la machine : repérer un processus managé

Process Hacker : un processus .NET apparaît comme *Managed (.NET)*. Dans `Process Properties → Modules`, chercher `clr.dll` et `clrjit.dll`.

![Modules clr.dll et clrjit.dll (Microsoft .NET Runtime)](../../../library/assets/reperer-du-powershell-non-manage-htb-windows-event-logs-28.png)

### 2. Garder les chargements de DLL

Observateur : *Filter Current Log…* → Event ID `7`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 7
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


### 3. Chercher le chargement du CLR

Observateur : *Find* sur `clr.dll`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 7
} |
    Where-Object { $_.Message -like "*clr.dll*" } |
    Format-List TimeCreated, Message
```


Même recherche avec `clrjit.dll`. Dans chaque résultat, lire `Image` : le processus qui a chargé le CLR.

### 4. Cibler un processus et la DLL avec une requête XML

Observateur : *Filter Current Log…* → onglet **XML** → *Edit query manually*.

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=7]
        and EventData[
          Data[@Name='Image']='<chemin du processus>'
          and Data[@Name='ImageLoaded']='C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


Les deux conditions doivent être vraies ensemble (`and`). Pour `clrjit.dll` : `…\v4.0.30319\clrjit.dll`. `Hashes` de l'événement : l'empreinte `SHA256=…` de la DLL. Gabarits : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

### 5. Trouver qui a injecté

L'injection laisse un Sysmon `8` (CreateRemoteThread) : un processus crée un thread dans un autre. Observateur : *Filter Current Log…* → Event ID `8`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 8
} | Format-List
```


`SourceImage` = le processus qui injecte ; `TargetImage` = la victime, celle qui charge le CLR à l'étape 3.

## Ce qui doit alerter

- `clr.dll` / `clrjit.dll` chargées par un service ou un processus natif (`spoolsv.exe`, par exemple).
- Un processus qui devient *Managed (.NET)* dans Process Hacker alors qu'il ne l'était pas.
- Un Sysmon `8` dont la cible (`TargetImage`) est ce même processus.

## À ne pas confondre

- Un processus natif peut légitimement héberger le CLR (consoles MMC, certains services et modules complémentaires).
- Corréler avec le contexte du processus, ses autres modules et les autres événements avant de conclure.

## Cas concret

<details markdown="1">
<summary>Lab HTB : du PowerShell injecté dans spoolsv.exe (Print Spooler)</summary>

L'injection passe par PSInject (`Invoke-PSInject`), en ciblant le PID de `spoolsv.exe` :

```
powershell -ep bypass 
Set-Location "C:\Tools\PSInject"
Import-Module .\Invoke-PSInject.ps1
Invoke-PSInject -ProcId (Get-Process spoolsv).Id -PoshCode "V3JpdGUtSG9zdCAiSGVsbG8sIEd1cnU5OSEi"
```


Avant l'injection, `spoolsv.exe` n'est pas un processus .NET :

![spoolsv.exe avant l'injection : processus non manage](../../../library/assets/reperer-du-powershell-non-manage-htb-windows-event-logs-29.png)

Après : Process Hacker le voit comme .NET, les modules du CLR apparaissent et Sysmon `7` enregistre le chargement de `clr.dll`.

![spoolsv.exe apres l'injection : processus manage par .NET](../../../library/assets/reperer-du-powershell-non-manage-htb-windows-event-logs-30.png)

![Modules de spoolsv.exe dans Process Hacker](../../../library/assets/reperer-du-powershell-non-manage-htb-windows-event-logs-31.png)

![Sysmon Event 7 : spoolsv.exe charge clr.dll](../../../library/assets/reperer-du-powershell-non-manage-htb-windows-event-logs-32.png)

Requête XML du lab : `Image` = `C:\Windows\System32\spoolsv.exe`, `ImageLoaded` = `clr.dll`. Lab pas à pas : [Sysmon et ETW › Labs › Question 2](../../../library/it/windows/sysmon-et-etw/04-labs/01-lab-2-analyser-avec-sysmon.md#question-2-powershell-non-manage-spoolsvexe).

</details>

<details markdown="1">
<summary>Skills Assessment : la victime, puis l'injecteur, dans C:\Logs\PowershellExec</summary>

La victime : le processus, autre que `powershell.exe`, qui charge `clrjit.dll`.

```powershell
Get-WinEvent -Path "C:\Logs\PowershellExec\*.evtx" |
    Where-Object { $_.Id -eq 7 -and $_.Message -match "clrjit.dll" } |
    Select-Object -ExpandProperty Message
```


L'injecteur : le `SourceImage` du Sysmon `8` qui vise cette victime.

```powershell
Get-WinEvent -FilterHashtable @{Path='C:\Logs\PowershellExec\*.evtx'; Id=8} | Format-List
```


Méthode pas à pas : [Sysmon et ETW › Labs › Lab 4](../../../library/it/windows/sysmon-et-etw/04-labs/03-lab-4-evaluation-finale-skills-assessment.md), questions 2 et 3.

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
