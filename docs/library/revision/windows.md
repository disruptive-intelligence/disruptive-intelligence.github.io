---
title: Révision — Windows
revision: it/windows
domaine: IT
sources:
- IT/02 Windows/Comprendre Windows/Windows en profondeur.md
---

*D'après le cours [Windows en profondeur](../it/windows/windows-en-profondeur/index.md)*

## Questions essentielles

- **Question :** Décrivez l'arbre de processus normal de Windows et comment vous l'utilisez pour détecter des anomalies.
  - **Réponse type :** L'arbre normal suit une chaîne précise : System → smss.exe → csrss.exe + wininit.exe → services.exe → svchost.exe. En parallèle, winlogon.exe → explorer.exe → applications. Pour chaque processus critique, je vérifie quatre choses : le parent est-il le bon, le chemin d'image est-il le bon (System32), le nombre d'instances est-il normal (un seul lsass.exe), et l'utilisateur est-il attendu (services.exe sous SYSTEM). Si un de ces critères ne colle pas, c'est suspect.

- **Question :** Comment un attaquant vole-t-il les credentials sur Windows et comment s'en protéger ?
  - **Réponse type :** La cible principale c'est lsass.exe, qui contient en mémoire les hashes NTLM et les tickets Kerberos. L'outil classique c'est Mimikatz. L'attaquant peut aussi extraire la SAM et SYSTEM du registre pour récupérer les hashes locaux, ou faire un DCSync pour extraire les hashes du contrôleur de domaine. Côté protection : Credential Guard isole lsass dans un environnement virtuel, RunAsPPL protège le processus contre les injections, et LAPS évite que le même mot de passe admin local soit utilisé partout.

- **Question :** Qu'est-ce qu'un LOLBin et pourquoi c'est un problème ?
  - **Réponse type :** Un LOLBin, c'est un binaire légitime de Windows détourné par un attaquant — par exemple certutil pour télécharger un payload, rundll32 pour exécuter une DLL malveillante, ou mshta pour lancer un script distant. Le problème, c'est que ces binaires sont signés Microsoft, présents sur toutes les machines, et passent souvent sous le radar des antivirus. La détection repose sur Sysmon et les Event Logs — on cherche des command lines suspectes sur des binaires légitimes.

- **Question :** Expliquez la chaîne MotW → SmartScreen → Protected View.
  - **Réponse type :** Quand un fichier est téléchargé depuis Internet, Windows lui ajoute un Mark of the Web dans un Alternate Data Stream. Ce MotW déclenche SmartScreen qui vérifie la réputation du fichier. Si c'est un document Office, il s'ouvre en Protected View avec les macros désactivées. C'est une défense en couches — chaque étape réduit le risque. C'est pour ça que les attaquants essaient de supprimer le MotW ou d'inciter l'utilisateur à cliquer sur "Activer le contenu".

- **Question :** Quels Event Logs surveillez-vous en priorité en tant qu'analyste SOC ?
  - **Réponse type :** Les Security Logs : 4624/4625 (connexions réussies/échouées), 4672 (attribution de privilèges spéciaux), 4688 (création de processus — avec la command line si activée). Sysmon Event 1 (création de processus avec hash et parent), Event 3 (connexions réseau), Event 10 (accès à un processus — critique pour détecter le dump de lsass), Event 7 (chargement de DLL). PowerShell 4104 (Script Block Logging). Et Event 7045 (création de service — PsExec par exemple).

## Questions complémentaires

- **Question :** Qu'est-ce que NTFS apporte comme artefacts forensic ?
  - **Réponse type :** La MFT (Master File Table) contient un enregistrement pour chaque fichier, même supprimé récemment — c'est un artefact majeur. Les timestamps MACB existent en double : dans $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le kernel). Si les deux divergent, c'est du timestomping — un signe de manipulation. Le $UsnJrnl enregistre toutes les modifications de fichiers et aide à reconstruire la timeline.

- **Question :** C'est quoi AMSI et comment les attaquants le contournent ?
  - **Réponse type :** AMSI est l'interface qui permet à PowerShell, VBA et d'autres moteurs de script de soumettre le code à l'antivirus avant exécution. Les attaquants le contournent en patchant amsi.dll en mémoire pour que le scan retourne toujours "propre". Mais le bypass lui-même est souvent détecté par le Script Block Logging (Event 4104), car le code du bypass est enregistré avant qu'il ne prenne effet.

- **Question :** C'est quoi le User mode vs Kernel mode ?
  - **Réponse type :** User mode (Ring 3), c'est là où tournent les applications — elles ont un accès limité et ne peuvent pas accéder directement au matériel. Kernel mode (Ring 0), c'est le noyau, les drivers — accès total à la mémoire et au matériel. Un crash en user mode ne plante que l'application, un crash en kernel mode provoque un écran bleu. Cette séparation est la base de la sécurité : pour accéder au kernel, il faut passer par des syscalls contrôlés.

## Questions les plus probables en entretien

1. Arbre de processus normal Windows ?
2. Comment les credentials sont volés et comment s'en protéger ?
3. LOLBins : c'est quoi, exemples, détection ?
4. Chaîne MotW → SmartScreen → Protected View ?
5. Event Logs prioritaires pour un SOC ?
6. User mode vs Kernel mode ?

## Réponses flash

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
