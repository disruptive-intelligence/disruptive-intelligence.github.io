---
title: Cyber Threat Intelligence (CTI)
source: Cyber/01_CTI/CTI.md
format: cours
revue: '2026-04-08'
---

*Du renseignement brut à l'intelligence actionnable*

**Cours complet — 36 chapitres • 8 parties • 7 annexes**

*Cycle intel • Analyse structurée • Profilage • Attribution • Production • Détection*

---

## Fil rouge : Opération MERIDIAN

> **Contexte narratif — ce fil rouge traverse les 33 premiers chapitres du cours et se conclut au Ch.34.**
>
> **Élise Moreau**, analyste CTI senior chez **Sentinelle Cyber** — MSSP français de 120 collaborateurs, clientèle ETI et grands groupes, SOC 24/7, CERT qualifié PRIS — reçoit une mission d'intelligence pour un client critique : **Européenne de Distribution Énergétique (EDE)**, opérateur de réseaux de distribution électrique dans 4 pays européens (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France et entité essentielle NIS 2.
>
> EDE a subi un incident de sécurité il y a 6 mois. L'équipe IR de Sentinelle a détecté et éradiqué l'intrusion (cf. cours IR de la bibliothèque). Les constats post-incident : l'attaquant a pénétré le réseau IT via un phishing ciblé sur un sous-traitant de maintenance, s'est déplacé latéralement via PsExec et RDP, a compromis l'Active Directory (Kerberoasting → DCSync), puis a pivoté vers le réseau de supervision SCADA via un poste d'ingénierie à double connexion. Il a été éjecté avant d'atteindre les automates, mais le CERT a identifié des mécanismes de persistance sophistiqués (DLL sideloading, tâches planifiées déguisées, modifications d'ACL AD) qui suggèrent un acteur de haut niveau. Aucune donnée exfiltrée confirmée, pas de ransomware, pas de sabotage — le positionnement semblait stratégique, pas financier.
>
> L'équipe IR a catalogué l'activité sous un cluster temporaire : **UNC-VOLT** (« UNC » pour uncategorized, convention Sentinelle). La mission d'Élise couvre cinq objectifs.
>
> **Objectif 1 — Profilage :** qui est UNC-VOLT ? Acteur étatique, mercenaire, cybercriminel sophistiqué ?
> **Objectif 2 — Attribution :** quel sponsor, quel pays, quel service de renseignement — avec quel niveau de confiance ?
> **Objectif 3 — Menace résiduelle :** UNC-VOLT va-t-il revenir ? Cible-t-il d'autres opérateurs d'énergie européens ?
> **Objectif 4 — Renseignement actionnable :** quelles TTP anticiper, quelles détections déployer, quelle posture défensive recommander à EDE ?
> **Objectif 5 — Contribution communautaire :** partager les conclusions avec l'ISAC énergie européen et contribuer à la connaissance collective sur ce cluster.
>
> L'investigation va mobiliser chaque compétence enseignée dans le cours : formulation de PIR, plan de collecte multi-sources, traitement et structuration dans OpenCTI, analyse structurée avec ACH (4 hypothèses concurrentes), gestion des biais, évaluation des sources, profilage d'acteur, analyse du tradecraft, attribution avec ses incertitudes, vulnerability intelligence (l'attaquant a exploité une vulnérabilité Ivanti), corrélation avec des campagnes connues, production de la note analytique, production de détections Sigma, briefing stratégique au COMEX d'EDE, et partage ISAC.

---

## Sommaire

- [Partie I — Fondations : comprendre la CTI](01-partie-i-fondations-comprendre-la-cti/index.md)
    - [Chapitre 1 — Qu'est-ce que la Cyber Threat Intelligence](01-partie-i-fondations-comprendre-la-cti/01-chapitre-1-qu-est-ce-que-la-cyber-threat-intellige.md)
    - [Chapitre 2 — Modèles et cadres analytiques de référence](01-partie-i-fondations-comprendre-la-cti/02-chapitre-2-modeles-et-cadres-analytiques-de-refere.md)
    - [Chapitre 3 — Le paysage de la menace](01-partie-i-fondations-comprendre-la-cti/03-chapitre-3-le-paysage-de-la-menace.md)
    - [Chapitre 4 — Le métier d'analyste CTI](01-partie-i-fondations-comprendre-la-cti/04-chapitre-4-le-metier-d-analyste-cti.md)
- [Partie II — Le cycle du renseignement appliqué](02-partie-ii-le-cycle-du-renseignement-applique/index.md)
    - [Chapitre 5 — Direction et planification : définir ce qu'on cherche](02-partie-ii-le-cycle-du-renseignement-applique/01-chapitre-5-direction-et-planification-definir-ce-q.md)
    - [Chapitre 6 — Collecte : sources, méthodes et gestion](02-partie-ii-le-cycle-du-renseignement-applique/02-chapitre-6-collecte-sources-methodes-et-gestion.md)
    - [Chapitre 7 — Traitement et structuration](02-partie-ii-le-cycle-du-renseignement-applique/03-chapitre-7-traitement-et-structuration.md)
    - [Chapitre 8 — Dissémination et feedback](02-partie-ii-le-cycle-du-renseignement-applique/04-chapitre-8-dissemination-et-feedback.md)
- [Partie III — L'analyse : le cœur du métier](03-partie-iii-l-analyse-le-coeur-du-metier/index.md)
    - [Chapitre 9 — Principes de l'analyse de renseignement](03-partie-iii-l-analyse-le-coeur-du-metier/01-chapitre-9-principes-de-l-analyse-de-renseignement.md)
    - [Chapitre 10 — Techniques analytiques structurées (TAS)](03-partie-iii-l-analyse-le-coeur-du-metier/02-chapitre-10-techniques-analytiques-structurees-tas.md)
    - [Chapitre 11 — Gestion des biais cognitifs en analyse CTI](03-partie-iii-l-analyse-le-coeur-du-metier/03-chapitre-11-gestion-des-biais-cognitifs-en-analyse.md)
    - [Chapitre 12 — Évaluer la fiabilité des sources et la crédibilité de l'information](03-partie-iii-l-analyse-le-coeur-du-metier/04-chapitre-12-evaluer-la-fiabilite-des-sources-et-la.md)
    - [Chapitre 13 — Niveaux de confiance et formulation analytique](03-partie-iii-l-analyse-le-coeur-du-metier/05-chapitre-13-niveaux-de-confiance-et-formulation-an.md)
    - [Chapitre 14 — Corrélation, recoupement et analyse multi-sources](03-partie-iii-l-analyse-le-coeur-du-metier/06-chapitre-14-correlation-recoupement-et-analyse-mul.md)
- [Partie IV — Profilage d'acteur ET attribution](04-partie-iv-profilage-d-acteur-et-attribution.md)
- [Partie V — CTI opérationnelle : de L'intelligence à L'action](05-partie-v-cti-operationnelle-de-l-intelligence-a-l.md)
- [Partie VI — Production de renseignement](06-partie-vi-production-de-renseignement.md)
- [Partie VII — Programme CTI ET maturité](07-partie-vii-programme-cti-et-maturite.md)
- [Partie VIII — Études de cas ET synthèse](08-partie-viii-etudes-de-cas-et-synthese/index.md)
    - [Chapitre 34 — Cas complet](08-partie-viii-etudes-de-cas-et-synthese/01-chapitre-34-cas-complet.md)
    - [Chapitre 35 — Cas complet](08-partie-viii-etudes-de-cas-et-synthese/02-chapitre-35-cas-complet.md)
    - [Chapitre 36 — Cas complet](08-partie-viii-etudes-de-cas-et-synthese/03-chapitre-36-cas-complet.md)
- [Annexes](09-annexes.md)
