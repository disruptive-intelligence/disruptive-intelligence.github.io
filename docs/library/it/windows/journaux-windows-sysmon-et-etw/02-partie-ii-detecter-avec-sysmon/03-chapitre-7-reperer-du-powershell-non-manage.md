---
title: Chapitre 7 — Repérer du PowerShell non managé
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Partie II — Détecter avec Sysmon
  - index.md
---

## 3. Détection n° 2 — PowerShell non managé / injection C#

### Code managé et CLR

Le langage C# utilise généralement l'environnement d'exécution .NET, notamment le Common Language Runtime (CLR).

Le code compilé est exécuté à travers cet environnement, avec notamment des mécanismes de compilation Just-In-Time (JIT).

Deux DLL sont particulièrement importantes :

- `clr.dll` : composant du Common Language Runtime.
- `clrjit.dll` : composant associé à la compilation JIT.

Leur présence est normale dans certains processus qui utilisent .NET.

### Process Hacker — repérer un processus managé

Process Hacker permet d'examiner les processus actifs.

Un processus comme `powershell.exe` peut apparaître comme Managed (.NET).

![Liste des processus dans Process Hacker](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-26.png)

![Infobulle de powershell.exe : processus manage (.NET)](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-27.png)

Depuis :

`Process Hacker → Process Properties → Modules`

L'analyste peut rechercher les modules :

```
clr.dll
clrjit.dll
```


![Modules clr.dll et clrjit.dll (Microsoft .NET Runtime)](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-28.png)

Cette inspection permet d'identifier la présence du runtime .NET dans un processus.

- La présence de « Microsoft .NET Runtime... », `clr.dll` et `clrjit.dll` devrait attirer notre attention. Ces 2 DLL sont utilisées lorsque du code C# est exécuté dans le cadre du runtime pour exécuter le bytecode.
- Si nous observons ces DLL chargées dans des processus qui ne les requièrent généralement pas, cela suggère une potentielle attaque [execute-assembly](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) ou [d'injection PowerShell non managée](https://www.youtube.com/watch?v=7tvfb9poTKg&ab_channel=RaphaelMudge).

### Scénario du lab — injection dans spoolsv.exe

Exemple : une injection de code PowerShell dans `spoolsv.exe`, le processus Windows associé au Print Spooler.

L'injection est réalisée avec le projet PSInject, via `Invoke-PSInject`, en ciblant le PID de `spoolsv.exe`.

```
powershell -ep bypass 
Set-Location "C:\Tools\PSInject"
Import-Module .\Invoke-PSInject.ps1
Invoke-PSInject -ProcId (Get-Process spoolsv).Id -PoshCode "V3JpdGUtSG9zdCAiSGVsbG8sIEd1cnU5OSEi"
```


Avant l'injection, le processus ne présente pas les caractéristiques d'un processus .NET managé.

![spoolsv.exe avant l'injection : processus non manage](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-29.png)

Après l'injection :

- Process Hacker identifie `spoolsv.exe` comme utilisant .NET.
- Les modules associés au CLR deviennent observables.
- Sysmon Event ID `7` enregistre le chargement de `clr.dll`.

![spoolsv.exe apres l'injection : processus manage par .NET](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-30.png)

![Modules de spoolsv.exe dans Process Hacker](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-31.png)

![Sysmon Event 7 : spoolsv.exe charge clr.dll](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-32.png)

### Logique de détection

```
spoolsv.exe
    ↓
Unexpected CLR Initialization
    ↓
clr.dll / clrjit.dll Loaded
    ↓
Sysmon Event ID 7
    ↓
Potential Code Injection
```


L'indicateur principal est le chargement inattendu du runtime .NET dans un processus qui ne l'utilise normalement pas.

Cette technique de hunting peut contribuer à détecter :

- des injections de code C# ;
- certains usages d'Unmanaged PowerShell ;
- certaines techniques d'exécution d'assemblages .NET dans un processus tiers.

Limite : un processus natif peut légitimement héberger le CLR. La présence de `clr.dll` doit être corrélée au contexte du processus, aux modules chargés et aux autres événements disponibles.
