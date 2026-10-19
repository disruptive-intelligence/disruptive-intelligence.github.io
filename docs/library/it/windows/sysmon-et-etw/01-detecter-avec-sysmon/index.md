---
title: Détecter avec Sysmon
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - ../index.md
---

Cette section présente l'utilisation de Sysmon et des Windows Event Logs pour détecter et investiguer trois techniques d'attaque :

- DLL Hijacking : détournement du chargement de bibliothèques DLL.
- Unmanaged PowerShell / C# Injection : exécution de code .NET au sein de processus inhabituels.
- Credential Dumping : tentative d'extraction d'identifiants Windows, notamment depuis LSASS.

L'objectif est de transformer des événements système en indicateurs exploitables pour le Threat Hunting et le DFIR.

## Dans cette partie

- [Installer et configurer Sysmon](01-installer-et-configurer-sysmon.md)
- [Trois détections avec Sysmon](02-trois-detections-avec-sysmon.md)
