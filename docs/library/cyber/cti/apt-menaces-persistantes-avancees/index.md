---
title: APT — menaces persistantes avancées
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
format: cours
revue: '2026-04-24'
---

*Advanced Persistent Threats — Acteurs étatiques, campagnes et géopolitique cyber*

**Cours complet — 32 chapitres • 8 parties • 8 annexes**

*Comprendre qui menace • Pourquoi • Avec quels moyens • Dans quel contexte*

-----

## Fil rouge : Opération BLACKOUT

> **Contexte narratif — ce fil rouge traverse le cours et se conclut au Ch.32.**
> 
> Un **opérateur de distribution d’énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
> 
> **L’intrusion** : l’attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d’une application de supervision, s’est déplacé latéralement via PsExec et Kerberoasting, puis a pivoté vers le réseau de supervision SCADA via un poste d’ingénierie à double connexion. Il a été détecté et éjecté avant d’atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
> 
> **Le mystère** : aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L’attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d’appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
> 
> L’investigation traverse le cours à travers une dizaine d’épisodes — chacun placé là où il apporte une clé analytique réelle : identification des TTP, comparaison aux profils par pays, analyse du ciblage OT, processus d’attribution et calibration de la réponse, synthèse finale au Ch.32.

-----

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Qu’est-ce qu’une APT : définition, frontières, typologies](01-partie-i-fondations/01-chapitre-1-quest-ce-quune-apt-definition-frontiere.md)
    - [Chapitre 2 — Cycle de vie d’une intrusion APT](01-partie-i-fondations/02-chapitre-2-cycle-de-vie-dune-intrusion-apt.md)
    - [Chapitre 3 — Tradecraft et TTP : le comment opérationnel](01-partie-i-fondations/03-chapitre-3-tradecraft-et-ttp-le-comment-operationn.md)
    - [Chapitre 4 — Le cyber comme instrument de puissance étatique](01-partie-i-fondations/04-chapitre-4-le-cyber-comme-instrument-de-puissance.md)
- [Partie II — Russie](02-partie-ii-russie/index.md)
    - [Chapitre 5 — Russie : contexte, doctrine et appareil cyber](02-partie-ii-russie/01-chapitre-5-russie-contexte-doctrine-et-appareil-cy.md)
    - [Chapitre 6 — Russie : les groupes APT en détail](02-partie-ii-russie/02-chapitre-6-russie-les-groupes-apt-en-detail.md)
    - [Chapitre 7 — Russie : campagnes de référence et opérations d’influence](02-partie-ii-russie/03-chapitre-7-russie-campagnes-de-reference-et-operat.md)
- [Partie III — Chine](03-partie-iii-chine/index.md)
    - [Chapitre 8 — Chine : contexte, doctrine et appareil cyber](03-partie-iii-chine/01-chapitre-8-chine-contexte-doctrine-et-appareil-cyb.md)
    - [Chapitre 9 — Chine : les groupes APT en détail](03-partie-iii-chine/02-chapitre-9-chine-les-groupes-apt-en-detail.md)
    - [Chapitre 10 — Chine : campagnes de référence et tendances 2023-2026](03-partie-iii-chine/03-chapitre-10-chine-campagnes-de-reference-et-tendan.md)
- [Partie IV — DPRK, Iran et autres acteurs](04-partie-iv-dprk-iran-et-autres-acteurs/index.md)
    - [Chapitre 11 — DPRK : contexte, groupes et modèle unique](04-partie-iv-dprk-iran-et-autres-acteurs/01-chapitre-11-dprk-contexte-groupes-et-modele-unique.md)
    - [Chapitre 12 — DPRK : campagnes de référence et financement du régime](04-partie-iv-dprk-iran-et-autres-acteurs/02-chapitre-12-dprk-campagnes-de-reference-et-finance.md)
    - [Chapitre 13 — Iran : contexte, doctrine et groupes APT](04-partie-iv-dprk-iran-et-autres-acteurs/03-chapitre-13-iran-contexte-doctrine-et-groupes-apt.md)
    - [Chapitre 14 — Iran : campagnes de référence](04-partie-iv-dprk-iran-et-autres-acteurs/04-chapitre-14-iran-campagnes-de-reference.md)
    - [Chapitre 15 — Autres acteurs étatiques, mercenaires cyber et zones grises](04-partie-iv-dprk-iran-et-autres-acteurs/05-chapitre-15-autres-acteurs-etatiques-mercenaires-c.md)
- [Partie V — Puissances cyber occidentales et alliées](05-partie-v-puissances-cyber-occidentales-et-alliees/index.md)
    - [Chapitre 16 — États-Unis : doctrine, agences et cyber power](05-partie-v-puissances-cyber-occidentales-et-alliees/01-chapitre-16-etats-unis-doctrine-agences-et-cyber-p.md)
    - [Chapitre 17 — Royaume-Uni et Five Eyes](05-partie-v-puissances-cyber-occidentales-et-alliees/02-chapitre-17-royaume-uni-et-five-eyes.md)
    - [Chapitre 18 — Israël](05-partie-v-puissances-cyber-occidentales-et-alliees/03-chapitre-18-israel.md)
    - [Chapitre 19 — Ukraine : cyberdéfense et guerre en temps réel](05-partie-v-puissances-cyber-occidentales-et-alliees/04-chapitre-19-ukraine-cyberdefense-et-guerre-en-temp.md)
- [Partie VI — Menaces OT et pré-positionnement](06-partie-vi-menaces-ot-et-pre-positionnement/index.md)
    - [Chapitre 20 — Architecture OT/ICS et protocoles industriels](06-partie-vi-menaces-ot-et-pre-positionnement/01-chapitre-20-architecture-ot-ics-et-protocoles-indu.md)
    - [Chapitre 21 — Campagnes OT/ICS destructrices](06-partie-vi-menaces-ot-et-pre-positionnement/02-chapitre-21-campagnes-ot-ics-destructrices.md)
    - [Chapitre 22 — Le pré-positionnement : la menace silencieuse](06-partie-vi-menaces-ot-et-pre-positionnement/03-chapitre-22-le-pre-positionnement-la-menace-silenc.md)
    - [Chapitre 23 — Protection des infrastructures critiques](06-partie-vi-menaces-ot-et-pre-positionnement/04-chapitre-23-protection-des-infrastructures-critiqu.md)
- [Partie VII — Géopolitique, attribution et prospective](07-partie-vii-geopolitique-attribution-et-prospective/index.md)
    - [Chapitre 24 — Attribution : méthodes, limites et enjeux](07-partie-vii-geopolitique-attribution-et-prospective/01-chapitre-24-attribution-methodes-limites-et-enjeux.md)
    - [Chapitre 25 — L’écosystème cyber offensif mondial](07-partie-vii-geopolitique-attribution-et-prospective/02-chapitre-25-lecosysteme-cyber-offensif-mondial.md)
    - [Chapitre 26 — Dissuasion, normes et responsabilité étatique](07-partie-vii-geopolitique-attribution-et-prospective/03-chapitre-26-dissuasion-normes-et-responsabilite-et.md)
    - [Chapitre 27 — Tendances 2024-2026 et signaux d’anticipation](07-partie-vii-geopolitique-attribution-et-prospective/04-chapitre-27-tendances-2024-2026-et-signaux-dantici.md)
    - [Chapitre 28 — Construire une défense APT-ready](07-partie-vii-geopolitique-attribution-et-prospective/05-chapitre-28-construire-une-defense-apt-ready.md)
- [Partie VIII — Études de cas intégrées](08-partie-viii-etudes-de-cas-integrees/index.md)
    - [Chapitre 29 — SolarWinds / SUNBURST](08-partie-viii-etudes-de-cas-integrees/01-chapitre-29-solarwinds-sunburst.md)
    - [Chapitre 30 — Lazarus et l’empire crypto de la DPRK](08-partie-viii-etudes-de-cas-integrees/02-chapitre-30-lazarus-et-lempire-crypto-de-la-dprk.md)
    - [Chapitre 31 — Volt Typhoon : le pré-positionnement stratégique](08-partie-viii-etudes-de-cas-integrees/03-chapitre-31-volt-typhoon-le-pre-positionnement-str.md)
    - [Chapitre 32 — Synthèse BLACKOUT : attribution face à l’incertitude](08-partie-viii-etudes-de-cas-integrees/04-chapitre-32-synthese-blackout-attribution-face-a-l.md)
- [Annexes](09-annexes/index.md)
    - [Annexe A — Glossaire APT/CTI](09-annexes/01-annexe-a-glossaire-apt-cti.md)
    - [Annexe B — Groupes APT majeurs par pays](09-annexes/02-annexe-b-groupes-apt-majeurs-par-pays.md)
    - [Annexe C — Conventions de nommage par vendor](09-annexes/03-annexe-c-conventions-de-nommage-par-vendor.md)
    - [Annexe D — Timeline des cyberattaques étatiques (2007-2026)](09-annexes/04-annexe-d-timeline-des-cyberattaques-etatiques-2007.md)
    - [Annexe E — Mapping ATT&CK par acteur](09-annexes/05-annexe-e-mapping-att-ck-par-acteur.md)
    - [Annexe F — Malwares et implants emblématiques](09-annexes/06-annexe-f-malwares-et-implants-emblematiques.md)
    - [Annexe G — Cadres juridiques et réglementaires par juridiction](09-annexes/07-annexe-g-cadres-juridiques-et-reglementaires-par-j.md)
    - [Annexe H — Ressources et formation](09-annexes/08-annexe-h-ressources-et-formation.md)
- [Les quatre idées centrales](10-les-quatre-idees-centrales.md)
