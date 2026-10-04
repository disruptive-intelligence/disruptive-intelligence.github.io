---
title: 'Chapitre 20 — Détection moderne : AMSI, ETW, EDR et BYOVD'
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie V — Modèle de sécurité et protections
  - index.md
---

## 20.1 AMSI (Anti-Malware Scan Interface)

AMSI est l'interface qui permet à PowerShell, VBA, JavaScript, .NET, et WSH de soumettre le code au moteur antimalware AVANT exécution. Quand un script PowerShell s'exécute, chaque bloc de code est passé à AMSI → l'AV le scanne → autorisation ou blocage. Les attaquants **patachent amsi.dll en mémoire** pour désactiver le scan (le champ amsiInitFailed est mis à $true, ou les instructions de AmsiScanBuffer sont remplacées par un retour immédiat). Détection : Script Block Logging (Event 4104) capture le code APRÈS le bypass AMSI (le bypass est lui-même loggé), ETW peut détecter le patching.

## 20.2 ETW (Event Tracing for Windows)

ETW est le mécanisme de trace universel de Windows. Les **providers** ETW génèrent des événements. Les **consumers** consomment ces événements — Event Logs, Sysmon, et les EDR sont des consumers ETW. Le provider **Microsoft-Windows-Threat-Intelligence** est utilisé par les EDR pour détecter les injections de code (il enregistre les opérations sur la mémoire de processus distants — WriteProcessMemory, NtMapViewOfSection). Les attaquants avancés **désactivent ou contournent les providers ETW** (patching des structures ETW en mémoire, NtTraceControl abuse). Détection : monitoring de la configuration ETW (Event 11 Sysmon sur les fichiers ETW, vérification de l'intégrité des providers).

## 20.3 EDR (Endpoint Detection and Response)

Comment les EDR fonctionnent : **hooking user mode** (les EDR remplacent les premières instructions des fonctions ntdll.dll par un JMP vers leur DLL de monitoring → chaque appel API suspect est intercepté et analysé), **callbacks kernel** (PsSetCreateProcessNotifyRoutine, PsSetLoadImageNotifyRoutine — le driver EDR est notifié à chaque création de processus et chargement d'image), **ETW consumption** (le driver EDR consomme les événements du provider Threat-Intelligence), **minifilter drivers** (interception des opérations I/O pour scanner les fichiers). Comment les EDR sont contournés : **unhooking** (restaurer les bytes originaux de ntdll.dll pour supprimer les hooks EDR), **syscalls directs** (sauter ntdll.dll entièrement → les hooks ne sont jamais traversés), **BYOVD** (voir ci-dessous), et **ETW patching** (désactiver les providers ETW qui alimentent l'EDR).

## 20.4 BYOVD (Bring Your Own Vulnerable Driver)

*Une technique moderne majeure qui mérite une attention particulière.*

Le **BYOVD** consiste à charger un driver légitime mais vulnérable (un ancien driver signé par un éditeur reconnu — Dell, Intel, HP, Realtek — qui contient une vulnérabilité connue) pour obtenir un accès kernel. Une fois en kernel mode, l'attaquant peut : désactiver l'EDR (tuer le processus EDR, désactiver les callbacks kernel, supprimer les hooks), désactiver la protection de lsass (accéder à la mémoire de lsass même avec RunAsPPL), et charger un rootkit. Le driver est légitime et signé → il passe le driver signing enforcement. Exemples : gdrv.sys (Gigabyte), procexp.sys (Process Explorer — le driver du propre outil Sysinternals a été abusé), dbutil_2_3.sys (Dell).

La défense : **HVCI** (Hypervisor-Protected Code Integrity — vérifie l'intégrité du code kernel et peut bloquer les drivers vulnérables connus), les **Microsoft Vulnerable Driver Blocklist** (liste de drivers vulnérables bloqués par Windows), **WDAC** avec blocage de drivers spécifiques, et le monitoring (Event 7045 chargement de driver, Sysmon 6 — DriverLoaded — hash du driver → comparaison avec la liste des drivers vulnérables connus).

---
