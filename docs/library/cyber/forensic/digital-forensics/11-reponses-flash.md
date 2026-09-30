---
title: Réponses flash
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - index.md
---

- **Forensic vs triage** → Judiciaire = exhaustivité, preuve recevable, chaîne de custody. DFIR = rapidité, contenir la menace. Les deux s'articulent.
- **Chaîne de custody** → Qui, quand, comment, où. Hash (MD5 + SHA-256). Rupture = preuve contestable.
- **Volatilité** → RAM → cache → logs → fichiers temp → disque. D'abord DumpIt, puis KAPE, puis image disque.
- **Artefacts Windows** → Prefetch, Amcache, ShimCache (exécution). ShellBags, LNK, Jump Lists (activité). Run keys, services, tasks (persistence). MFT (timeline).
- **Timestomping** → Comparer $STANDARD_INFORMATION vs $FILE_NAME dans la MFT. Divergence = manipulation.
- **Outils** → KAPE (triage), Velociraptor (collecte à distance), FTK Imager (image E01), DumpIt (RAM), Volatility 3 (analyse mémoire), Eric Zimmerman tools (parsing).

---


> **Note de clôture**
>
> Ce cours a été conçu pour former à l'investigation numérique comme discipline scientifique complète — de l'acquisition rigoureuse des preuves à la production d'un rapport défendable devant un tribunal, en passant par l'analyse technique approfondie des artefacts sur tous les types de systèmes.
>
> L'investigation MUSIC BOX qui traverse les 29 premiers chapitres illustre la réalité du terrain : l'analyste forensic ne se contente pas d'extraire des artefacts d'une machine — il reconstitue une histoire de 60 jours de compromission, il corrèle des sources hétérogènes (endpoint, réseau, AD, cloud), il détecte les tentatives d'anti-forensics de l'attaquant, il raisonne par hypothèses en gérant ses propres biais, et il produit un rapport qui sera lu par un juge ET par un CEO.
>
> La compétence forensic ne se résume pas à la maîtrise des outils — c'est une posture intellectuelle : rigueur, doute méthodique, transparence des conclusions, et humilité face à la complexité du réel. Les outils évoluent (Volatility 4 remplacera peut-être Volatility 3, de nouveaux artefacts apparaîtront avec chaque version de Windows), mais la posture reste.
>
> *Acquisition • Analyse • Preuve • Rapport — avec rigueur et objectivité.*
