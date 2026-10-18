---
title: Repérer une relation parent-enfant anormale
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Détecter avec ETW
  - index.md
---

## 1. Détecter les relations parent-enfant étranges

### Analyser les relations parent-enfant

Sous Windows, les processus présentent généralement des relations parent/enfant cohérentes avec leur fonction.

Une relation inhabituelle peut révéler une activité malveillante.

Exemples du cours :

```
calc.exe
   └── cmd.exe
```


```
spoolsv.exe
   └── whoami.exe
```


Ces relations sont suspectes, car une calculatrice ou un service d'impression n'a normalement pas vocation à lancer de telles commandes dans les scénarios présentés.

![Relation normale : spoolsv.exe et son enfant conhost.exe](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-40.png)

- Samir Bousseaden a partagé une carte mentale (mind map) pertinente présentant les relations parent-enfant courantes, qui peut être consultée [ici](https://twitter.com/SBousseaden/status/1195373669930983424).

![Carte mentale des relations parent-enfant courantes des processus Windows, par Samir Bousseaden (@SBousseaden)](../../../../assets/journaux-windows-sysmon-et-etw-ejeyi8vxyai3gra.jpg)

*Carte : Samir Bousseaden ([@SBousseaden](https://twitter.com/SBousseaden/status/1195373669930983424)).*

### Process Hacker

Process Hacker permet de visualiser les processus actifs sous forme d'arborescence.

![Process Hacker : arborescence des processus](../../../../assets/journaux-windows-sysmon-et-etw-htb-windows-event-logs-39.png)

L'analyste peut notamment examiner :

- Parent Process : processus parent apparent.
- Child Process : processus enfant.
- Process ID (PID) : identifiant du processus.
- Process Hierarchy : organisation des processus.
- Command Line : arguments d'exécution, lorsqu'ils sont disponibles.

L'analyse doit tenir compte des comportements habituels de l'environnement.
