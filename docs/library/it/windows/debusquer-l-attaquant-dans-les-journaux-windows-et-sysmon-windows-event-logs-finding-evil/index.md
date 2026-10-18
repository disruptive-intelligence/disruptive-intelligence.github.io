---
title: Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil)
source: IT/02 Windows/Journaux & investigation/Débusquer l'attaquant dans les journaux Windows et Sysmon (Windows Event Logs & Finding Evil).md
format: cours
provenance: HTB Academy
revue: '2026-10-18'
---

Ce cours apprend à repérer une activité malveillante dans les journaux Windows : anatomie d'un événement, ouvertures de session (4624, Logon Types, Logon ID), requêtes XML dans l'Observateur d'événements et Event IDs utiles ; puis, avec Sysmon, trois détections pas à pas : DLL hijacking, injection de PowerShell non managé et vol d'identifiants dans LSASS.

Les journaux Windows sont détaillés dans [Analyse des journaux d'événements Windows (Event Logs)](../analyse-des-journaux-d-evenements-windows-event-logs/index.md) ; les Event IDs Sysmon et les commandes dans la cheat sheet [Sysmon et requêtes SIEM](/cheatsheets/windows/fondamentaux/logs/sysmon/).

## Sommaire

- [Les journaux d'événements Windows](01-les-journaux-d-evenements-windows.md)
- [Analyser avec Sysmon et les journaux d'événements](02-analyser-avec-sysmon-et-les-journaux-d-evenements.md)
- [Event Tracing for Windows (ETW)](03-event-tracing-for-windows-etw.md)
- [Tirer parti d'ETW](04-tirer-parti-d-etw.md)
- [Lab 1 — Les bases des journaux d'événements Windows](05-lab-1-les-bases-des-journaux-d-evenements-windows.md)
- [Lab 2 — Analyser avec Sysmon](06-lab-2-analyser-avec-sysmon.md)
- [Lab 3 — Travailler avec ETW](07-lab-3-travailler-avec-etw.md)
