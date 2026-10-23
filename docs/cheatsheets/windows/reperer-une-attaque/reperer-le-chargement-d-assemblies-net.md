---
title: Repérer le chargement d'assemblies .NET
source: IT/02 Windows/Repérer une attaque/Repérer le chargement d'assemblies .NET.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Un attaquant apporte ses propres outils .NET et les exécute, parfois directement en mémoire. Deux niveaux : Sysmon `7` voit le runtime .NET se charger, ETW (`Microsoft-Windows-DotNETRuntime`) montre les assemblies et les méthodes. Les étapes vont du plus large au plus précis.

## En bref

| | |
|---|---|
| Technique | Chargement d'assemblies .NET malveillants (Bring Your Own Land) |
| MITRE ATT&CK | [T1620 — Reflective Code Loading](https://attack.mitre.org/techniques/T1620/) |
| Journaux | `Microsoft-Windows-Sysmon/Operational` ; trace ETW `Microsoft-Windows-DotNETRuntime` (SilkETW) |
| Événements | Sysmon `7` (chargement de `clr.dll`, `mscoree.dll`) ; ETW : assemblies chargées, méthodes compilées |
| Indice clé | Un exécutable inconnu ou lancé depuis un dossier inhabituel initialise .NET |

## Le principe

- Living off the Land (LotL) : utiliser les outils déjà présents (PowerShell, outils natifs). Bring Your Own Land (BYOL, décrit par Mandiant) : apporter ses propres outils, souvent des assemblies .NET en C#.
- Pourquoi .NET : présent sur tout Windows, bibliothèques prêtes (HTTP, crypto, IPC), chargement en mémoire sans fichier sur disque (ex. [`execute-assembly`](https://www.cobaltstrike.com/blog/cobalt-strike-3-11-the-snake-that-eats-its-tail/) de Cobalt Strike).
- DLL à surveiller : `clr.dll` (Common Language Runtime), `clrjit.dll` (Just-In-Time), `mscoree.dll` (initialisation du runtime).
- Limite de Sysmon `7` : il dit quel processus a chargé .NET, pas quel assembly a été exécuté. ETW complète.

## Chercher, étape par étape

Sur un journal exporté : `Path = '<fichier>.evtx'` ; tout un dossier : `Path = '<dossier>\*.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

### 1. Garder les chargements de DLL

Observateur : *Filter Current Log…* → Event ID `7`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 7
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


### 2. Chercher l'initialisation de .NET

Observateur : *Find* sur `mscoree.dll`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 7
} |
    Where-Object { $_.Message -like "*mscoree.dll*" } |
    Format-List TimeCreated, Message
```


Même recherche avec `clr.dll`. Dans chaque résultat, lire `Image` : l'exécutable qui a initialisé .NET.

### 3. Cibler un exécutable avec une requête XML

Observateur : *Filter Current Log…* → onglet **XML** → *Edit query manually*.

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=7]
        and EventData[
          Data[@Name='Image']='<chemin du programme>'
          and Data[@Name='ImageLoaded']='C:\Windows\System32\mscoree.dll'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


Gabarits : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

### 4. Collecter le provider DotNETRuntime avec SilkETW

```
SilkETW.exe -t user -pn Microsoft-Windows-DotNETRuntime -uk 0x2038 -ot file -p C:\Windows\Temp\etw.json
```


Lancer la collecte, rejouer l'exécution suspecte, puis arrêter. `-uk 0x2038` sélectionne les mots-clés :

| Keyword | Ce qu'il apporte |
|---|---|
| JitKeyword | Méthodes compilées pendant l'exécution |
| InteropKeyword | Appels entre code managé et API natives |
| LoaderKeyword | Assemblies chargées |
| NGenKeyword | Composants .NET précompilés |

### 5. Chercher les méthodes appelées

```powershell
Select-String -Path "C:\Windows\Temp\etw.json" `
    -Pattern '"ManagedInteropMethodName"\s*:\s*"[^"]+"' -AllMatches |
ForEach-Object { $_.Matches.Value } |
Sort-Object -Unique
```


Les noms de méthodes distincts de toute la trace ; les replacer dans leur contexte (heure, processus) avant de les attribuer. Commandes ETW : cheat sheet [ETW](/cheatsheets/windows/fondamentaux/logs/etw/).

## Ce qui doit alerter

- Un exécutable inconnu, ou lancé depuis un dossier utilisateur, un dossier d'outils ou `Temp`, qui charge `mscoree.dll` / `clr.dll`.
- Dans la trace ETW, des noms d'assemblies ou de méthodes d'outils offensifs (énumération des privilèges, du système, des identifiants).

## À ne pas confondre

- Beaucoup d'applications légitimes sont en .NET : le chargement de `clr.dll` est banal, seul le contexte le rend suspect.
- ETW n'enregistre que ce que les keywords activés et le runtime émettent : tous les appels de méthodes n'y sont pas.
- Une collecte ETW est volumineuse : la lancer de façon ciblée, le temps de vérifier une hypothèse.

## Cas concret

<details markdown="1">
<summary>Lab HTB : Seatbelt.exe, vu par Sysmon puis par ETW</summary>

[Seatbelt](https://github.com/GhostPack/Seatbelt) (GhostPack) énumère le système. `.\Seatbelt.exe TokenPrivileges` affiche les privilèges du token (`SeDebugPrivilege`, `SeImpersonatePrivilege`…).

![image-42](../../../library/assets/reperer-le-chargement-d-assemblies-net-image-42.png)

Sysmon `7` : `Seatbelt.exe` charge `clr.dll` et `mscoree.dll`.

![Sysmon Event 7 : chargement d'image par Seatbelt.exe](../../../library/assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-44.png)

![Sysmon Event 7 : second chargement de DLL .NET par Seatbelt.exe](../../../library/assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-45.png)

ETW (`etw.json`) : les noms des méthodes de Seatbelt, bien plus parlants qu'un simple chargement de `clr.dll`.

![etw.json : evenements DotNETRuntime de Seatbelt avec les noms de methodes](../../../library/assets/reperer-le-chargement-d-assemblies-net-htb-windows-event-logs-46.png)

Requête XML du lab : `Image` = `C:\Tools\GhostPack Compiled Binaries\Seatbelt.exe`, `ImageLoaded` = `mscoree.dll`. Lab pas à pas : [Sysmon et ETW › Labs › Lab 3, question 1](../../../library/it/windows/sysmon-et-etw/04-labs/02-lab-3-travailler-avec-etw.md#question-1-suivre-seatbelt-avec-sysmon-et-etw). Pour aller plus loin : [article sur SilkETW](https://medium.com/threat-hunters-forge/threat-hunting-with-etw-events-and-helk-part-1-installing-silketw-6eb74815e4a0).

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
