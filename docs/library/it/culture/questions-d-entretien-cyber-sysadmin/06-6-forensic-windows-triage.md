---
title: 6) Forensic / Windows / Triage
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Comment vérifier la signature d'un fichier avec PowerShell ?**
  **Réponse type :** `Get-AuthenticodeSignature -FilePath C:\chemin\fichier.exe`. Ça retourne le statut de la signature : Valid (signée et chaîne de confiance valide), NotSigned (pas de signature — suspect si c'est dans System32), HashMismatch (fichier modifié après signature — très suspect), ou UnknownError. Pour vérifier en ligne : calculer le hash avec `Get-FileHash` et le soumettre à VirusTotal.

- **Question : Qu'est-ce qu'un dump de la base SAM ?**
  **Réponse type :** La SAM (Security Accounts Manager) est la base de données qui stocke les hashes NTLM des comptes locaux Windows. Un dump SAM permet à un attaquant de récupérer ces hashes pour les craquer offline ou les utiliser en Pass-the-Hash. La SAM est verrouillée quand Windows tourne — l'attaquant utilise des outils comme Mimikatz, reg save, ou boot depuis un live USB pour y accéder.

- **Question : Pour exploiter un dump SAM, quelles ruches faut-il récupérer en plus ?**
  **Réponse type :** Il faut aussi la ruche SYSTEM. La commande classique : `reg save HKLM\SAM sam.save` et `reg save HKLM\SYSTEM system.save`. Ensuite, on utilise un outil comme `secretsdump.py` (Impacket) ou `samdump2` pour extraire les hashes.

- **Question : Pourquoi la ruche SYSTEM est-elle nécessaire avec la SAM ?**
  **Réponse type :** Parce que les hashes dans la SAM sont chiffrés avec la Boot Key (aussi appelée SysKey), qui est stockée dans la ruche SYSTEM. Sans cette clé de déchiffrement, les hashes extraits de la SAM sont illisibles. L'outil d'extraction utilise le SYSTEM pour récupérer la Boot Key, déchiffrer la SAM, et obtenir les hashes NTLM exploitables.

- **Question : Quels sont les principaux artefacts forensic Windows ?**
  **Réponse type :** Pour l'exécution : Prefetch (programmes exécutés avec dates), Amcache et ShimCache (historique avec hash SHA1), Event Logs (4688 process creation, Sysmon). Pour l'activité utilisateur : ShellBags (navigation explorateur), Jump Lists (fichiers récents par application), LNK (raccourcis avec chemins et dates). Pour la persistence : clés Run/RunOnce du registre, services, tâches planifiées. La MFT pour la timeline complète de tous les fichiers. Les outils Eric Zimmerman (MFTECmd, PECmd, AmcacheParser) sont la référence pour parser tout ça.

- **Question : Qu'est-ce que l'arbre de processus normal de Windows et comment l'utiliser pour la détection ?**
  **Réponse type :** L'arbre normal suit une chaîne précise : System → smss.exe → csrss.exe + wininit.exe → services.exe → svchost.exe. En parallèle, winlogon.exe → explorer.exe → applications utilisateur. Pour chaque processus critique, je vérifie quatre choses : le parent est-il le bon (svchost doit avoir services.exe comme parent), le chemin d'image est-il le bon (System32), le nombre d'instances est-il normal (un seul lsass.exe), et l'utilisateur est-il attendu (services.exe sous SYSTEM). Si un critère ne colle pas, c'est suspect.

- **Question : C'est quoi un LOLBin ?**
  **Réponse type :** Un LOLBin (Living-off-the-Land Binary) est un binaire légitime de Windows détourné par un attaquant — certutil pour télécharger un payload, rundll32 pour exécuter une DLL malveillante, mshta pour lancer un script distant. Le problème c'est que ces binaires sont signés Microsoft, présents partout, et passent souvent sous le radar des antivirus. La détection repose sur Sysmon et les Event Logs — on cherche des command lines suspectes sur des binaires légitimes.

---
