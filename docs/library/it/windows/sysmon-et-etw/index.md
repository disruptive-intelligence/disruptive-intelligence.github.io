---
title: Sysmon et ETW
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
format: cours
provenance: HTB Academy
revue: '2026-10-19'
---

Ce cours va au-delà des journaux natifs : installer et configurer Sysmon, puis comprendre ETW, son architecture, ses outils et ses providers. Les détections pas à pas (DLL hijacking, PowerShell non managé, accès à LSASS, faux processus parent, assemblies .NET) ont chacune leur fiche dans la sous-rubrique « Repérer une attaque ».

Les bases (anatomie d'un événement, ouvertures de session, requêtes XML, Event IDs utiles) sont dans [Analyse des journaux d'événements Windows (Event Logs)](../analyse-des-journaux-d-evenements-windows-event-logs/index.md) ; les Event IDs Sysmon et les commandes dans la cheat sheet [Sysmon et requêtes SIEM](/cheatsheets/windows/fondamentaux/logs/sysmon/).

## Sommaire

- [Détecter avec Sysmon](01-detecter-avec-sysmon/index.md)
    - [Installer et configurer Sysmon](01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md)
    - [Trois détections avec Sysmon](01-detecter-avec-sysmon/02-trois-detections-avec-sysmon.md)
- [Comprendre ETW](02-comprendre-etw/index.md)
    - [Fondamentaux et architecture d'ETW](02-comprendre-etw/01-fondamentaux-et-architecture-d-etw.md)
    - [Explorer ETW : logman et interfaces](02-comprendre-etw/02-explorer-etw-logman-et-interfaces.md)
    - [Providers utiles et providers restreints](02-comprendre-etw/03-providers-utiles-et-providers-restreints.md)
    - [ETW en investigation](02-comprendre-etw/04-etw-en-investigation.md)
- [Détecter avec ETW](03-detecter-avec-etw.md)
- [Labs](04-labs/index.md)
    - [Lab 2 — Analyser avec Sysmon](04-labs/01-lab-2-analyser-avec-sysmon.md)
    - [Lab 3 — Travailler avec ETW](04-labs/02-lab-3-travailler-avec-etw.md)
    - [Lab 4 — Évaluation finale (Skills Assessment)](04-labs/03-lab-4-evaluation-finale-skills-assessment.md)
