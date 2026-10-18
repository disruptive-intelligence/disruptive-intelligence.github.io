---
title: Journaux Windows, Sysmon et ETW
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
format: cours
provenance: HTB Academy
revue: '2026-10-18'
---

Ce cours apprend à repérer une activité malveillante dans les journaux Windows : anatomie d'un événement, ouvertures de session (4624, Logon Types, Logon ID), requêtes XML dans l'Observateur d'événements et Event IDs utiles ; puis, avec Sysmon, trois détections pas à pas : DLL hijacking, injection de PowerShell non managé et vol d'identifiants dans LSASS.

Les journaux Windows sont détaillés dans [Analyse des journaux d'événements Windows (Event Logs)](../analyse-des-journaux-d-evenements-windows-event-logs/index.md) ; les Event IDs Sysmon et les commandes dans la cheat sheet [Sysmon et requêtes SIEM](/cheatsheets/windows/fondamentaux/logs/sysmon/).

## Sommaire

- [Les journaux d'événements Windows](01-les-journaux-d-evenements-windows/index.md)
    - [Comprendre un événement Windows](01-les-journaux-d-evenements-windows/01-comprendre-un-evenement-windows.md)
    - [Ouvertures de session : 4624 et Logon ID](01-les-journaux-d-evenements-windows/02-ouvertures-de-session-4624-et-logon-id.md)
    - [Requêtes XML et investigation guidée](01-les-journaux-d-evenements-windows/03-requetes-xml-et-investigation-guidee.md)
    - [Event IDs utiles et démarche de chasse](01-les-journaux-d-evenements-windows/04-event-ids-utiles-et-demarche-de-chasse.md)
- [Détecter avec Sysmon](02-detecter-avec-sysmon/index.md)
    - [Installer et configurer Sysmon](02-detecter-avec-sysmon/01-installer-et-configurer-sysmon.md)
    - [Repérer un DLL hijacking](02-detecter-avec-sysmon/02-reperer-un-dll-hijacking.md)
    - [Repérer du PowerShell non managé](02-detecter-avec-sysmon/03-reperer-du-powershell-non-manage.md)
    - [Repérer un accès à LSASS](02-detecter-avec-sysmon/04-reperer-un-acces-a-lsass.md)
- [Comprendre ETW](03-comprendre-etw/index.md)
    - [Fondamentaux et architecture d'ETW](03-comprendre-etw/01-fondamentaux-et-architecture-d-etw.md)
    - [Explorer ETW : logman et interfaces](03-comprendre-etw/02-explorer-etw-logman-et-interfaces.md)
    - [Providers utiles et providers restreints](03-comprendre-etw/03-providers-utiles-et-providers-restreints.md)
    - [ETW en investigation](03-comprendre-etw/04-etw-en-investigation.md)
- [Détecter avec ETW](04-detecter-avec-etw/index.md)
    - [Repérer une relation parent-enfant anormale](04-detecter-avec-etw/01-reperer-une-relation-parent-enfant-anormale.md)
    - [Démasquer un faux processus parent (PPID spoofing)](04-detecter-avec-etw/02-demasquer-un-faux-processus-parent-ppid-spoofing.md)
    - [Repérer le chargement d'assemblies .NET](04-detecter-avec-etw/03-reperer-le-chargement-d-assemblies-net.md)
    - [Aller plus loin avec le provider DotNETRuntime](04-detecter-avec-etw/04-aller-plus-loin-avec-le-provider-dotnetruntime.md)
- [Labs](05-labs/index.md)
    - [Lab 1 — Les bases des journaux d'événements Windows](05-labs/01-lab-1-les-bases-des-journaux-d-evenements-windows.md)
    - [Lab 2 — Analyser avec Sysmon](05-labs/02-lab-2-analyser-avec-sysmon.md)
    - [Lab 3 — Travailler avec ETW](05-labs/03-lab-3-travailler-avec-etw.md)
