---
title: Questions complémentaires
source: IT/02_Windows/Windows.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

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
