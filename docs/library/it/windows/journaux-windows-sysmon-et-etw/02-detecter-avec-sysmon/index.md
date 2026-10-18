---
title: Détecter avec Sysmon
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

- [Installer et configurer Sysmon](01-installer-et-configurer-sysmon.md)
- [Repérer un DLL hijacking](02-reperer-un-dll-hijacking.md)
- [Repérer du PowerShell non managé](03-reperer-du-powershell-non-manage.md)
- [Repérer un accès à LSASS](04-reperer-un-acces-a-lsass.md)
