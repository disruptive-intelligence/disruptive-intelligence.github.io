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

- [Partie I — Les journaux d'événements Windows](01-partie-i-les-journaux-d-evenements-windows/index.md)
    - [Chapitre 1 — Comprendre un événement Windows](01-partie-i-les-journaux-d-evenements-windows/01-chapitre-1-comprendre-un-evenement-windows.md)
    - [Chapitre 2 — Ouvertures de session : 4624 et Logon ID](01-partie-i-les-journaux-d-evenements-windows/02-chapitre-2-ouvertures-de-session-4624-et-logon-id.md)
    - [Chapitre 3 — Requêtes XML et investigation guidée](01-partie-i-les-journaux-d-evenements-windows/03-chapitre-3-requetes-xml-et-investigation-guidee.md)
    - [Chapitre 4 — Event IDs utiles et démarche de chasse](01-partie-i-les-journaux-d-evenements-windows/04-chapitre-4-event-ids-utiles-et-demarche-de-chasse.md)
- [Partie II — Détecter avec Sysmon](02-partie-ii-detecter-avec-sysmon/index.md)
    - [Chapitre 5 — Installer et configurer Sysmon](02-partie-ii-detecter-avec-sysmon/01-chapitre-5-installer-et-configurer-sysmon.md)
    - [Chapitre 6 — Repérer un DLL hijacking](02-partie-ii-detecter-avec-sysmon/02-chapitre-6-reperer-un-dll-hijacking.md)
    - [Chapitre 7 — Repérer du PowerShell non managé](02-partie-ii-detecter-avec-sysmon/03-chapitre-7-reperer-du-powershell-non-manage.md)
    - [Chapitre 8 — Repérer un accès à LSASS](02-partie-ii-detecter-avec-sysmon/04-chapitre-8-reperer-un-acces-a-lsass.md)
- [Partie III — Comprendre ETW](03-partie-iii-comprendre-etw/index.md)
    - [Chapitre 9 — Fondamentaux et architecture d'ETW](03-partie-iii-comprendre-etw/01-chapitre-9-fondamentaux-et-architecture-d-etw.md)
    - [Chapitre 10 — Explorer ETW : logman et interfaces](03-partie-iii-comprendre-etw/02-chapitre-10-explorer-etw-logman-et-interfaces.md)
    - [Chapitre 11 — Providers utiles et providers restreints](03-partie-iii-comprendre-etw/03-chapitre-11-providers-utiles-et-providers-restrein.md)
    - [Chapitre 12 — ETW en investigation](03-partie-iii-comprendre-etw/04-chapitre-12-etw-en-investigation.md)
- [Partie IV — Détecter avec ETW](04-partie-iv-detecter-avec-etw/index.md)
    - [Chapitre 13 — Repérer une relation parent-enfant anormale](04-partie-iv-detecter-avec-etw/01-chapitre-13-reperer-une-relation-parent-enfant-ano.md)
    - [Chapitre 14 — Démasquer un faux processus parent (PPID spoofing)](04-partie-iv-detecter-avec-etw/02-chapitre-14-demasquer-un-faux-processus-parent-ppi.md)
    - [Chapitre 15 — Repérer le chargement d'assemblies .NET](04-partie-iv-detecter-avec-etw/03-chapitre-15-reperer-le-chargement-d-assemblies-net.md)
    - [Chapitre 16 — Aller plus loin avec le provider DotNETRuntime](04-partie-iv-detecter-avec-etw/04-chapitre-16-aller-plus-loin-avec-le-provider-dotne.md)
- [Partie V — Labs](05-partie-v-labs/index.md)
    - [Lab 1 — Les bases des journaux d'événements Windows](05-partie-v-labs/01-lab-1-les-bases-des-journaux-d-evenements-windows.md)
    - [Lab 2 — Analyser avec Sysmon](05-partie-v-labs/02-lab-2-analyser-avec-sysmon.md)
