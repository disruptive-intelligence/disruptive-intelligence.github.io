---
title: Sysmon et ETW
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
format: cours
provenance: HTB Academy
revue: '2026-10-18'
---

Ce cours va au-delà des journaux natifs : avec Sysmon, trois détections pas à pas (DLL hijacking, injection de PowerShell non managé, vol d'identifiants dans LSASS) ; puis ETW, son architecture, ses outils et ses providers, et deux détections qui s'appuient dessus.

Les bases (anatomie d'un événement, ouvertures de session, requêtes XML, Event IDs utiles) sont dans [Analyse des journaux d'événements Windows (Event Logs)](../analyse-des-journaux-d-evenements-windows-event-logs/index.md) ; les Event IDs Sysmon et les commandes dans la cheat sheet [Sysmon et requêtes SIEM](/cheatsheets/windows/fondamentaux/logs/sysmon/).

## Sommaire

- [Détecter avec Sysmon](01-detecter-avec-sysmon/index.md)
    - [Installer et configurer Sysmon](01-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md)
    - [Repérer un DLL hijacking](01-detecter-avec-sysmon/02-reperer-un-dll-hijacking.md)
    - [Repérer du PowerShell non managé](01-detecter-avec-sysmon/03-reperer-du-powershell-non-manage.md)
    - [Repérer un accès à LSASS](01-detecter-avec-sysmon/04-reperer-un-acces-a-lsass.md)
- [Comprendre ETW](02-comprendre-etw/index.md)
    - [Fondamentaux et architecture d'ETW](02-comprendre-etw/01-fondamentaux-et-architecture-d-etw.md)
    - [Explorer ETW : logman et interfaces](02-comprendre-etw/02-explorer-etw-logman-et-interfaces.md)
    - [Providers utiles et providers restreints](02-comprendre-etw/03-providers-utiles-et-providers-restreints.md)
    - [ETW en investigation](02-comprendre-etw/04-etw-en-investigation.md)
- [Détecter avec ETW](03-detecter-avec-etw/index.md)
    - [Repérer une relation parent-enfant anormale](03-detecter-avec-etw/01-reperer-une-relation-parent-enfant-anormale.md)
    - [Démasquer un faux processus parent (PPID spoofing)](03-detecter-avec-etw/02-demasquer-un-faux-processus-parent-ppid-spoofing.md)
    - [Repérer le chargement d'assemblies .NET](03-detecter-avec-etw/03-reperer-le-chargement-d-assemblies-net.md)
    - [Aller plus loin avec le provider DotNETRuntime](03-detecter-avec-etw/04-aller-plus-loin-avec-le-provider-dotnetruntime.md)
- [Labs](04-labs/index.md)
    - [Lab 2 — Analyser avec Sysmon](04-labs/01-lab-2-analyser-avec-sysmon.md)
    - [Lab 3 — Travailler avec ETW](04-labs/02-lab-3-travailler-avec-etw.md)
