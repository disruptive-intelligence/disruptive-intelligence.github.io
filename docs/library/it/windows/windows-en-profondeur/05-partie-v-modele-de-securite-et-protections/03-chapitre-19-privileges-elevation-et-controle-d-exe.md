---
title: Chapitre 19 — Privilèges, élévation et contrôle d'exécution
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie V — Modèle de sécurité et protections
  - index.md
---

## 19.1 Les privilèges Windows

Les **privilèges Windows** critiques : **SeDebugPrivilege** (accéder à la mémoire de tout processus → Mimikatz), **SeImpersonatePrivilege** (impersonation → Potato attacks), **SeBackupPrivilege** (lire tout fichier y compris SAM/NTDS.dit), **SeRestorePrivilege** (écrire tout fichier), **SeTcbPrivilege** (agir comme le système), **SeLoadDriverPrivilege** (charger un driver kernel). L'**élévation de privilèges** Potato (exploitent SeImpersonatePrivilege pour obtenir SYSTEM via la coercion NTLM interne — PrintSpoofer, GodPotato, JuicyPotato, SweetPotato ; détection : 4672 avec SeImpersonatePrivilege + processus inhabituel).

## 19.2 Le contrôle d'exécution

Le **contrôle d'exécution** : **AppLocker** (règles par path, hash, publisher → contournable mais ralentit l'attaquant — bypass via LOLBins, DLL side-loading), **WDAC** (Windows Defender Application Control — plus robuste, basé sur la politique code integrity du kernel, plus difficile à contourner que AppLocker), **SRP** (Software Restriction Policies — legacy, remplacé par AppLocker/WDAC).

---
