---
title: Chapitre 17 — Construction de timeline multi-sources
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

La timeline multi-sources fusionne les événements de toutes les sources (EDR + SIEM + proxy + firewall + AD + email gateway + cloud) en une séquence chronologique unique. C'est le livrable le plus puissant de l'investigation — c'est aussi le plus exigeant à construire.

Les étapes de construction : normalisation des timestamps en UTC, identification des sources pertinentes pour chaque phase de l'attaque, extraction des événements clés par requête SIEM, fusion dans un format tabulaire (heure UTC | source | machine | utilisateur | action | détail), et analyse de la séquence (patterns, corrélations, lacunes). Les lacunes sont aussi informatives que les événements — un trou de 6 heures entre le mouvement latéral et l'exfiltration pose la question : l'attaquant était-il inactif, ou les logs manquent-ils ?

Fil rouge : Karim construit la timeline FALCONWATCH de 48 heures, qui révèle que l'attaquant a agi en 4 phases distinctes : samedi 08h-10h (phishing + infection initiale), samedi 22h-01h (reconnaissance + mouvement latéral), dimanche 06h-10h (Kerberoasting + staging des données R&D), lundi 04h-07h (suppression des shadow copies sur 3 machines + déploiement du binaire ransomware — non exécuté avant la détection EDR à 07h42).

---
