---
title: Partie II — Détecter avec Sysmon
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
---

Cette section présente l'utilisation de Sysmon et des Windows Event Logs pour détecter et investiguer trois techniques d'attaque :

- DLL Hijacking : détournement du chargement de bibliothèques DLL.
- Unmanaged PowerShell / C# Injection : exécution de code .NET au sein de processus inhabituels.
- Credential Dumping : tentative d'extraction d'identifiants Windows, notamment depuis LSASS.

L'objectif est de transformer des événements système en indicateurs exploitables pour le Threat Hunting et le DFIR.

## Dans cette partie

- [Chapitre 5 — Installer et configurer Sysmon](01-chapitre-5-installer-et-configurer-sysmon.md)
- [Chapitre 6 — Repérer un DLL hijacking](02-chapitre-6-reperer-un-dll-hijacking.md)
- [Chapitre 7 — Repérer du PowerShell non managé](03-chapitre-7-reperer-du-powershell-non-manage.md)
- [Chapitre 8 — Repérer un accès à LSASS](04-chapitre-8-reperer-un-acces-a-lsass.md)
