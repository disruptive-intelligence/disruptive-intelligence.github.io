---
title: Réponses flash
source: IT/02_Windows/Windows.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

- **Arbre processus** → System → smss → csrss + wininit → services → svchost. Winlogon → explorer → apps. Vérifier : parent, chemin, instances, user.
- **Credentials** → Cible = lsass.exe (Mimikatz). Protection = Credential Guard, RunAsPPL, LAPS.
- **LOLBins** → Binaires légitimes détournés (certutil, rundll32, mshta). Signés MS, passent les AV. Détection = Sysmon + command line.
- **MotW** → Fichier téléchargé → ADS Zone.Identifier → SmartScreen → Protected View → macros bloquées.
- **Event Logs SOC** → 4624/4625 (logon), 4672 (privs), 4688 (process), Sysmon 1/3/10, PowerShell 4104, 7045 (service).
- **User/Kernel mode** → Ring 3 (applis, limité) vs Ring 0 (noyau, drivers, accès total). Séparation = base de la sécurité.
- **NTFS forensic** → MFT (tous les fichiers), timestamps $SI vs $FN (détecte timestomping), $UsnJrnl (journal modifs).

---

> **Note de clôture**
>
> Ce cours a été conçu pour enseigner comment Windows fonctionne sous le capot avec un prisme sécurité permanent — chaque concept est relié à son exploitation ou sa défense.
>
> L'opération SHADOW illustre une réalité que tout analyste SOC et IR constate : les attaques modernes n'utilisent pas de malware exotique — elles utilisent les mécanismes légitimes de Windows. Une macro Word, un LOLBin (certutil + rundll32), du Process Hollowing dans svchost.exe, un dump lsass via comsvcs.dll, du mouvement latéral via WMI et PsExec, et un DCSync. Chaque technique est un mécanisme Windows détourné. C'est pourquoi comprendre les internals est le prérequis pour détecter : si on ne sait pas à quoi ressemble un svchost.exe normal, on ne peut pas identifier le faux.
>
> Le cours assume une conviction : la défense en profondeur fonctionne quand chaque couche est comprise. Le MotW déclenche SmartScreen qui déclenche Protected View qui bloque les macros. AMSI scanne le code avant exécution. ETW alimente les Event Logs, Sysmon, et l'EDR. Credential Guard isole les secrets. HVCI protège le kernel. Chaque couche est contournable individuellement — mais les empiler force l'attaquant à dépenser plus de temps, générer plus de signaux, et prendre plus de risques d'être détecté. La victoire de la défense est dans la profondeur.
>
> *Comprendre les internals • Détecter l'anormal • Investiguer les artefacts • Durcir les configurations — parce que la sécurité Windows commence par la compréhension de Windows.*
