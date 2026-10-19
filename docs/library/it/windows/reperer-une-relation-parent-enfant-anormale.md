---
title: Repérer une relation parent-enfant anormale
source: IT/02 Windows/Repérer une attaque/Repérer une relation parent-enfant anormale.md
format: detection
provenance: HTB Academy
revue: '2026-10-19'
---

Sous Windows, chaque processus a des parents et des enfants attendus : une calculatrice ou un service d'impression ne lance pas d'invite de commandes. Cette fiche montre comment repérer une filiation anormale dans Process Hacker et dans les événements Sysmon `1`.

Quand le parent affiché est lui-même falsifié : [Démasquer un faux processus parent (PPID spoofing)](demasquer-un-faux-processus-parent-ppid-spoofing.md).

## En bref

| | |
|---|---|
| Technique | Pas une technique à elle seule : un signal commun à beaucoup d'entre elles (exécution de commandes, injection, exploitation d'un service) |
| MITRE ATT&CK | Voir par exemple [T1059 — Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/) |
| Journal | `Microsoft-Windows-Sysmon/Operational` (ou Security `4688` si l'audit des créations de processus est actif) |
| Événement | Sysmon `1` — création de processus (champs `Image`, `ParentImage`, `CommandLine`) |
| Indice clé | Un parent qui n'a pas vocation à lancer cet enfant : `calc.exe` → `cmd.exe`, `spoolsv.exe` → `whoami.exe` |

## Comprendre l'attaque

Les processus Windows présentent des relations parent/enfant cohérentes avec leur fonction. Une relation inhabituelle peut révéler une activité malveillante, par exemple :

```
calc.exe
   └── cmd.exe
```


```
spoolsv.exe
   └── whoami.exe
```


Ces relations sont suspectes : une calculatrice ou un service d'impression n'a pas vocation à lancer de telles commandes.

![Relation normale : spoolsv.exe et son enfant conhost.exe](../../assets/reperer-une-relation-parent-enfant-anormale-htb-windows-event-logs-40.png)

Samir Bousseaden a partagé une carte mentale des relations parent-enfant courantes, consultable [ici](https://twitter.com/SBousseaden/status/1195373669930983424).

![Carte mentale des relations parent-enfant courantes des processus Windows, par Samir Bousseaden (@SBousseaden)](../../assets/reperer-une-relation-parent-enfant-anormale-ejeyi8vxyai3gra.jpg)

*Carte : Samir Bousseaden ([@SBousseaden](https://twitter.com/SBousseaden/status/1195373669930983424)).*

## Les traces

### Process Hacker

Process Hacker affiche les processus actifs sous forme d'arborescence.

![Process Hacker : arborescence des processus](../../assets/reperer-une-relation-parent-enfant-anormale-htb-windows-event-logs-39.png)

À examiner :

- Parent Process : processus parent apparent ;
- Child Process : processus enfant ;
- Process ID (PID) : identifiant du processus ;
- Process Hierarchy : organisation des processus ;
- Command Line : arguments d'exécution, lorsqu'ils sont disponibles.

### Sysmon Event ID 1 — création de processus

Après coup, la filiation se lit dans l'Event ID 1 : `Image` (l'enfant), `ParentImage` (le parent), `CommandLine` et `ParentCommandLine`, `User`.

## Les requêtes

**1. Que lance ce processus ?** Tous les enfants de `spoolsv.exe` :

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">
      *[
        System[EventID=1]
        and EventData[
          Data[@Name='ParentImage']='C:\Windows\System32\spoolsv.exe'
        ]
      ]
    </Select>
  </Query>
</QueryList>
```


- `ParentImage` : le parent ; dans chaque résultat, `Image` donne l'enfant et `CommandLine` ce qu'il a exécuté.
- Pour un enfant précis, ajouter `and Data[@Name='Image']='C:\Windows\System32\cmd.exe'`.

**2. Quelles filiations sont rares ?** Compter les couples parent → enfant et lire d'abord les moins fréquents :

```powershell
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -FilterXPath "*[System[EventID=1]]" |
    ForEach-Object {
        $data = ([xml]$_.ToXml()).Event.EventData.Data
        $parent = Split-Path ($data | Where-Object Name -eq 'ParentImage').'#text' -Leaf
        $enfant = Split-Path ($data | Where-Object Name -eq 'Image').'#text' -Leaf
        "$parent -> $enfant"
    } |
    Group-Object |
    Sort-Object Count |
    Select-Object Count, Name -First 20
```


- `Split-Path -Leaf` garde le nom de l'exécutable sans son chemin ; `Group-Object` compte les couples identiques ; `Sort-Object Count` met les plus rares en tête.
- Un couple vu une ou deux fois (`spoolsv.exe -> whoami.exe`) mérite d'être ouvert ; un couple vu des milliers de fois est le fonctionnement normal.

Gabarits et pièges du XML : cheat sheet [Requêtes XML de l'Observateur](/cheatsheets/windows/fondamentaux/logs/requetes-xml/).

## Les indicateurs

- Un service ou une application sans rapport (`spoolsv.exe`, `calc.exe`, un navigateur, une suite bureautique) qui lance `cmd.exe`, `powershell.exe` ou des commandes de reconnaissance (`whoami.exe`, `net.exe`…).
- Une filiation qui sort de la carte des relations habituelles.
- Une ligne de commande inhabituelle pour l'enfant, ou un enfant lancé depuis un dossier utilisateur.

## Les faux positifs

- L'analyse tient compte des comportements habituels de l'environnement : outils d'administration, scripts de déploiement et logiciels métier créent des filiations propres à chaque parc.
- Le parent affiché peut être faux : voir [Démasquer un faux processus parent (PPID spoofing)](demasquer-un-faux-processus-parent-ppid-spoofing.md).

## Pour s'entraîner

- Le module HTB n'a pas de question de lab dédiée : rejouer la requête 2 sur ses propres journaux Sysmon pour apprendre les filiations normales de son parc.
- Event IDs Sysmon et requêtes SIEM : cheat sheet [Sysmon](/cheatsheets/windows/fondamentaux/logs/sysmon/).

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
