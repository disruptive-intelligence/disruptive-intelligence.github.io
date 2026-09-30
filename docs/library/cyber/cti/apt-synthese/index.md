---
title: APT — synthèse
source: Cyber/01_CTI/APT_Synthese.md
format: synthese
---

*Advanced Persistent Threats — Acteurs étatiques, campagnes et géopolitique cyber*

**Cours complet — 32 chapitres • 8 parties • 7 annexes**

*Russie • Chine • DPRK • Iran • Puissances occidentales • OT/ICS • Attribution • Défense APT-ready*

---

## Fil rouge : Opération BLACKOUT

> **Contexte narratif — ce fil rouge traverse les 28 premiers chapitres et se conclut au Ch.32.**
>
> Un **opérateur de distribution d'énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
>
> **L'intrusion :** l'attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d'une application de supervision, se déplacé latéralement via PsExec et Kerberoasting, puis pivoté vers le réseau de supervision SCADA via un poste d'ingénierie à double connexion. Il a été détecté et éjecté avant d'atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
>
> **Le mystère :** aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L'attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d'appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
>
> L'investigation va traverser les 8 parties du cours : identification des TTP (Partie I), comparaison avec les profils par pays (Parties II-V), analyse du ciblage OT (Partie VI), processus d'attribution et calibration de la réponse (Partie VII), et synthèse complète (Partie VIII, Ch.32).

---

## Sommaire

- [Partie I — Fondations : comprendre les APT](01-partie-i-fondations-comprendre-les-apt/index.md)
    - [Chapitre 1 — Qu'est-ce qu'une APT](01-partie-i-fondations-comprendre-les-apt/01-chapitre-1-qu-est-ce-qu-une-apt.md)
    - [Chapitre 2 — Cycle de vie d'une intrusion APT](01-partie-i-fondations-comprendre-les-apt/02-chapitre-2-cycle-de-vie-d-une-intrusion-apt.md)
    - [Chapitre 3 — Tradecraft et TTP : comment une APT opère](01-partie-i-fondations-comprendre-les-apt/03-chapitre-3-tradecraft-et-ttp-comment-une-apt-opere.md)
    - [Chapitre 4 — Le cyber comme instrument de puissance étatique](01-partie-i-fondations-comprendre-les-apt/04-chapitre-4-le-cyber-comme-instrument-de-puissance.md)
- [Partie II — Russie](02-partie-ii-russie/index.md)
    - [Chapitre 5 — Russie : contexte, doctrine et appareil cyber](02-partie-ii-russie/01-chapitre-5-russie-contexte-doctrine-et-appareil-cy.md)
    - [Chapitre 6 — Russie : les groupes APT en détail](02-partie-ii-russie/02-chapitre-6-russie-les-groupes-apt-en-detail.md)
    - [Chapitre 7 — Russie : campagnes de référence et influence](02-partie-ii-russie/03-chapitre-7-russie-campagnes-de-reference-et-influe.md)
- [Partie III — Chine](03-partie-iii-chine.md)
- [Partie IV — Corée du nord, iran ET autres acteurs](04-partie-iv-coree-du-nord-iran-et-autres-acteurs.md)
- [Partie V — Puissances cyber occidentales ET alliées](05-partie-v-puissances-cyber-occidentales-et-alliees.md)
- [Partie VI — Menaces sur les infrastructures critiques ET L'OT](06-partie-vi-menaces-sur-les-infrastructures-critique.md)
- [Partie VII — Géopolitique, attribution ET prospective](07-partie-vii-geopolitique-attribution-et-prospective.md)
- [Partie VIII — Études de cas intégrées](08-partie-viii-etudes-de-cas-integrees.md)
- [Annexes](09-annexes.md)
