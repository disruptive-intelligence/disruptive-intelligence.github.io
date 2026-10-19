---
title: Repérer une relation parent-enfant anormale
source: IT/02 Windows/Repérer une attaque/Repérer une relation parent-enfant anormale.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Chaque processus Windows a des parents et des enfants attendus : une calculatrice ou un service d'impression ne lance pas d'invite de commandes. Les étapes ci-dessous vont du plus large au plus précis : chacune se teste, puis s'affine.

Quand le parent affiché est lui-même faux : [Démasquer un faux processus parent (PPID spoofing)](demasquer-un-faux-processus-parent-ppid-spoofing.md).

## En bref

| | |
|---|---|
| Technique | Pas une technique à elle seule : un signal commun à beaucoup d'entre elles (exécution de commandes, injection, exploitation d'un service) |
| MITRE ATT&CK | Voir par exemple [T1059 — Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` |
| Événement | Sysmon `1` — création de processus |
| Indice clé | Un parent qui n'a pas vocation à lancer cet enfant : `calc.exe` → `cmd.exe`, `spoolsv.exe` → `whoami.exe` |

## Le principe

- Les relations parent → enfant suivent la fonction des programmes : `spoolsv.exe` → `conhost.exe` est normal, `spoolsv.exe` → `whoami.exe` ne l'est pas.
- Référence des filiations courantes : la [carte de Samir Bousseaden](https://twitter.com/SBousseaden/status/1195373669930983424).
- Trace : Sysmon `1`, avec `Image` (l'enfant), `ParentImage` (le parent) et `CommandLine`.

## Chercher, étape par étape

Sur un journal exporté : `Path = '<fichier>.evtx'`. Sur la machine elle-même : `LogName = 'Microsoft-Windows-Sysmon/Operational'` à la place de `Path`.

### 1. Sur la machine : l'arborescence des processus

Process Hacker : parent, enfant, PID et ligne de commande de chaque processus.

![Process Hacker : arborescence des processus](../../assets/reperer-une-relation-parent-enfant-anormale-htb-windows-event-logs-39.png)

### 2. Garder les créations de processus

Observateur : *Filter Current Log…* → Event ID `1`.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 1
} -MaxEvents 10 |
    Format-List TimeCreated, Message
```


### 3. Chercher ce que lance un parent suspect

Observateur : *Find* sur le nom du parent.

```powershell
Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 1
} |
    Where-Object { $_.Message -like '*ParentImage:*spoolsv.exe*' } |
    Format-List TimeCreated, Message
```


Dans chaque résultat, `Image` donne l'enfant et `CommandLine` ce qu'il a exécuté.

### 4. Compter les couples parent / enfant

```powershell
$events = Get-WinEvent -FilterHashtable @{
    Path = '<fichier>.evtx'
    Id   = 1
} | ForEach-Object {
    $data = ([xml]$_.ToXml()).Event.EventData.Data

    [pscustomobject]@{
        ParentImage = ($data | Where-Object Name -eq 'ParentImage').'#text'
        Image       = ($data | Where-Object Name -eq 'Image').'#text'
    }
}

$events |
    Group-Object ParentImage, Image |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```


Un couple vu une ou deux fois, en bas de la liste, mérite d'être ouvert.

## Ce qui doit alerter

- Un service ou une application sans rapport (`spoolsv.exe`, `calc.exe`…) qui lance `cmd.exe`, `powershell.exe` ou des commandes de reconnaissance (`whoami.exe`…).
- Une filiation absente de la carte des relations habituelles.

## À ne pas confondre

- Outils d'administration, scripts de déploiement et logiciels métier créent des filiations propres à chaque parc.
- Le parent affiché peut être faux : [Démasquer un faux processus parent (PPID spoofing)](demasquer-un-faux-processus-parent-ppid-spoofing.md).

## Cas concret

<details markdown="1">
<summary>Cours HTB : relation normale de spoolsv.exe et carte des filiations</summary>

Relation attendue : `spoolsv.exe` et son enfant `conhost.exe`.

![Relation normale : spoolsv.exe et son enfant conhost.exe](../../assets/reperer-une-relation-parent-enfant-anormale-htb-windows-event-logs-40.png)

![Carte mentale des relations parent-enfant courantes des processus Windows, par Samir Bousseaden (@SBousseaden)](../../assets/reperer-une-relation-parent-enfant-anormale-ejeyi8vxyai3gra.jpg)

*Carte : Samir Bousseaden ([@SBousseaden](https://twitter.com/SBousseaden/status/1195373669930983424)).* Pas de question de lab dédiée dans le module.

</details>

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
