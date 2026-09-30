---
title: Questions essentielles
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - index.md
---

- **Question :** Quelle est la différence entre le forensic judiciaire et le triage DFIR ?
  - **Réponse type :** Le forensic judiciaire vise à produire des preuves recevables devant un tribunal — l'exhaustivité et la chaîne de custody priment. Le triage DFIR vise à comprendre rapidement ce qui se passe pour contenir la menace — la rapidité prime. En pratique, les deux s'articulent : on commence souvent en triage et on bascule en judiciaire si les constatations le justifient. C'est pour ça qu'il faut respecter les bonnes pratiques de préservation dès le début, même en triage — on ne sait jamais si l'affaire finira devant un juge.

- **Question :** Qu'est-ce que la chaîne de custody et pourquoi c'est critique ?
  - **Réponse type :** La chaîne de custody trace chaque manipulation d'une preuve : qui l'a collectée, quand, comment, où elle a été stockée, qui y a eu accès. C'est ce qui garantit l'intégrité et la recevabilité de la preuve en justice. Si la chaîne est rompue — par exemple une image disque non hashée ou un scellé mal documenté —, la partie adverse peut contester la preuve et le juge peut la rejeter.

- **Question :** Qu'est-ce que l'ordre de volatilité et comment l'appliquez-vous ?
  - **Réponse type :** L'ordre de volatilité dicte la priorité de collecte : on commence par ce qui disparaît le plus vite. La mémoire RAM est la plus volatile — elle contient les processus en cours, les clés de chiffrement, les connexions réseau, et elle disparaît au redémarrage. Ensuite les logs système, le cache, les fichiers temporaires, puis le disque dur. En pratique : d'abord le dump RAM (DumpIt), puis le triage KAPE pour les artefacts, puis l'image disque complète. Et surtout, ne jamais éteindre une machine avant d'avoir capturé la mémoire.

- **Question :** Quels sont les principaux artefacts Windows que vous analysez ?
  - **Réponse type :** Pour l'exécution : le Prefetch (programmes exécutés avec dates), l'Amcache et le ShimCache (historique d'exécution avec hash), les Event Logs (4688 création de processus, Sysmon). Pour l'activité utilisateur : les ShellBags (navigation explorateur), les Jump Lists (fichiers récents par application), les fichiers LNK (raccourcis avec chemins et dates). Pour la persistence : les clés Run/RunOnce du registre, les services, les tâches planifiées. La MFT pour la timeline de tous les fichiers. Les outils Eric Zimmerman (MFTECmd, PECmd, AmcacheParser) sont la référence pour parser tout ça.

- **Question :** Comment détectez-vous le timestomping ?
  - **Réponse type :** Le timestomping consiste à modifier les timestamps des fichiers pour masquer l'activité. Sous NTFS, il y a deux jeux de timestamps : $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le kernel). Si les deux divergent — par exemple si $SI montre une date ancienne mais $FN montre une date récente — c'est un signe de manipulation. MFTECmd extrait les deux et la comparaison est immédiate.


## Questions complémentaires

- **Question :** Quels outils utilisez-vous pour le triage rapide ?
  - **Réponse type :** KAPE (Kroll Artifact Parser and Extractor) pour la collecte et le parsing automatisé des artefacts Windows — en quelques minutes il collecte les Event Logs, le registre, le Prefetch, la MFT, l'Amcache, les historiques navigateur. Velociraptor pour la collecte à distance sur un parc entier via des requêtes VQL. FTK Imager pour l'acquisition disque en format E01 avec write blocker. Et DumpIt pour le dump mémoire.

- **Question :** C'est quoi l'analyse mémoire et pourquoi c'est indispensable ?
  - **Réponse type :** L'analyse mémoire capture l'état instantané du système : les processus en cours, les connexions réseau, les DLLs chargées, les credentials en clair, et le code des malwares fileless qui n'existent qu'en RAM. L'outil de référence c'est Volatility 3. On peut identifier un processus injecté (svchost.exe avec un parent anormal), extraire les clés de chiffrement d'un ransomware, ou trouver un RAT qui ne touche jamais le disque. Sans dump mémoire, on perd toute cette information au redémarrage.


## Questions les plus probables en entretien

1. Forensic judiciaire vs triage DFIR ?
2. Chaîne de custody : pourquoi c'est critique ?
3. Ordre de volatilité : RAM en premier ?
4. Artefacts Windows clés ?
5. Comment détecter le timestomping ?
6. Outils de triage et d'acquisition ?
