---
title: Cartographie des écosystèmes cybercriminels
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
format: cours
revue: '2026-04-08'
---

*Comprendre • Relier • Analyser • Produire*

**Cours complet — 35 chapitres • 8 parties • 6 annexes**

---

## Fil rouge : Opération NEXUS

> **Contexte narratif — ce fil rouge traverse les 28 premiers chapitres du cours.**
>
> **Mars 2026.** Samira Khaled, analyste CTI senior chez *Énergis*, un opérateur français d'infrastructures énergétiques classé OIV (Opérateur d'Importance Vitale), reçoit une alerte du SOC interne. Un sample de malware a été détecté sur un poste d'ingénierie connecté au réseau OT (Operational Technology) du site de production de Fos-sur-Mer. L'antivirus a bloqué l'exécution, mais le fichier a déjà communiqué brièvement avec un domaine C2 inconnu : `update-srv-infra[.]xyz`.
>
> Le CERT interne confirme : le binaire est un variant de ransomware déployé par un builder connu, associé à une plateforme RaaS active. Mais la cible — un réseau OT dans le secteur énergie, en pleine tension géopolitique sur l'approvisionnement européen — ne correspond pas au profil opportuniste habituel des affiliés ransomware.
>
> Samira ouvre une investigation CTI. Son objectif : cartographier l'écosystème complet derrière ce sample — de l'opérateur RaaS à l'affilié, de l'IAB qui a vendu l'accès initial au service de mixing qui blanchit les fonds, de l'hébergeur bulletproof au relais médiatique qui amplifie la pression. Et surtout : déterminer si cette attaque est purement criminelle ou si elle sert aussi des intérêts para-étatiques.
>
> Chaque chapitre enrichira cette investigation, ajoutera des pièces au graphe, et confrontera Samira à des décisions méthodologiques concrètes. Le rapport final, livré au Chapitre 28, sera une note d'analyse complète destinée à la direction générale d'Énergis, au CERT, à l'ANSSI, et potentiellement aux forces de l'ordre.

---

## Sommaire

- [Partie I — Fondations : penser en écosystème](01-partie-i-fondations-penser-en-ecosysteme/index.md)
    - [Chapitre 1 — Pourquoi raisonner en écosystème](01-partie-i-fondations-penser-en-ecosysteme/01-chapitre-1-pourquoi-raisonner-en-ecosysteme.md)
    - [Chapitre 2 — Typologie des écosystèmes clandestins](01-partie-i-fondations-penser-en-ecosysteme/02-chapitre-2-typologie-des-ecosystemes-clandestins.md)
    - [Chapitre 3 — Lecture systémique d'un environnement clandestin](01-partie-i-fondations-penser-en-ecosysteme/03-chapitre-3-lecture-systemique-d-un-environnement-c.md)
    - [Chapitre 4 — Cadre juridique, éthique et posture de travail](01-partie-i-fondations-penser-en-ecosysteme/04-chapitre-4-cadre-juridique-ethique-et-posture-de-t.md)
    - [Chapitre 5 — Outils et méthodologie de cartographie](01-partie-i-fondations-penser-en-ecosysteme/05-chapitre-5-outils-et-methodologie-de-cartographie.md)
- [Partie II — Les entités de L'écosystème](02-partie-ii-les-entites-de-l-ecosysteme/index.md)
    - [Chapitre 6 — Personnes, alias et identités fragmentées](02-partie-ii-les-entites-de-l-ecosysteme/01-chapitre-6-personnes-alias-et-identites-fragmentee.md)
    - [Chapitre 7 — Entités organisationnelles](02-partie-ii-les-entites-de-l-ecosysteme/02-chapitre-7-entites-organisationnelles.md)
    - [Chapitre 8 — Espaces relationnels et médiatiques](02-partie-ii-les-entites-de-l-ecosysteme/03-chapitre-8-espaces-relationnels-et-mediatiques.md)
    - [Chapitre 9 — Objets techniques](02-partie-ii-les-entites-de-l-ecosysteme/04-chapitre-9-objets-techniques.md)
    - [Chapitre 10 — Objets financiers](02-partie-ii-les-entites-de-l-ecosysteme/05-chapitre-10-objets-financiers.md)
- [Partie III — Liens, corrélations ET rigueur analytique](03-partie-iii-liens-correlations-et-rigueur-analytiqu/index.md)
    - [Chapitre 11 — Les types de liens](03-partie-iii-liens-correlations-et-rigueur-analytiqu/01-chapitre-11-les-types-de-liens.md)
    - [Chapitre 12 — Corrélation, faisceau d'indices et prudence analytique](03-partie-iii-liens-correlations-et-rigueur-analytiqu/02-chapitre-12-correlation-faisceau-d-indices-et-prud.md)
    - [Chapitre 13 — Niveaux de confiance et formulation analytique](03-partie-iii-liens-correlations-et-rigueur-analytiqu/03-chapitre-13-niveaux-de-confiance-et-formulation-an.md)
- [Partie IV — Comprendre L'économie cybercriminelle](04-partie-iv-comprendre-l-economie-cybercriminelle/index.md)
    - [Chapitre 14 — Évolution historique des écosystèmes cybercriminels](04-partie-iv-comprendre-l-economie-cybercriminelle/01-chapitre-14-evolution-historique-des-ecosystemes-c.md)
    - [Chapitre 15 — Pourquoi raisonner en économie](04-partie-iv-comprendre-l-economie-cybercriminelle/02-chapitre-15-pourquoi-raisonner-en-economie.md)
    - [Chapitre 16 — Les grands business models](04-partie-iv-comprendre-l-economie-cybercriminelle/03-chapitre-16-les-grands-business-models.md)
    - [Chapitre 17 — Division du travail et sous-traitance criminelle](04-partie-iv-comprendre-l-economie-cybercriminelle/04-chapitre-17-division-du-travail-et-sous-traitance.md)
    - [Chapitre 18 — La chaîne de valeur cybercriminelle](04-partie-iv-comprendre-l-economie-cybercriminelle/05-chapitre-18-la-chaine-de-valeur-cybercriminelle.md)
    - [Chapitre 19 — L'économie de la confiance dans l'illégal](04-partie-iv-comprendre-l-economie-cybercriminelle/06-chapitre-19-l-economie-de-la-confiance-dans-l-ille.md)
    - [Chapitre 20 — Crypto, blanchiment et circulation de la valeur](04-partie-iv-comprendre-l-economie-cybercriminelle/07-chapitre-20-crypto-blanchiment-et-circulation-de-l.md)
- [Partie V — Géopolitique, zones grises ET disruption](05-partie-v-geopolitique-zones-grises-et-disruption/index.md)
    - [Chapitre 21 — Zones grises entre criminalité, influence et para-étatique](05-partie-v-geopolitique-zones-grises-et-disruption/01-chapitre-21-zones-grises-entre-criminalite-influen.md)
    - [Chapitre 22 — Stratégies de disruption](05-partie-v-geopolitique-zones-grises-et-disruption/02-chapitre-22-strategies-de-disruption.md)
    - [Chapitre 23 — Les facteurs macro](05-partie-v-geopolitique-zones-grises-et-disruption/03-chapitre-23-les-facteurs-macro.md)
- [Partie VI — Construire ET exploiter une cartographie](06-partie-vi-construire-et-exploiter-une-cartographie/index.md)
    - [Chapitre 24 — Définir le périmètre](06-partie-vi-construire-et-exploiter-une-cartographie/01-chapitre-24-definir-le-perimetre.md)
    - [Chapitre 25 — Collecte et structuration des données](06-partie-vi-construire-et-exploiter-une-cartographie/02-chapitre-25-collecte-et-structuration-des-donnees.md)
    - [Chapitre 26 — Construire le graphe](06-partie-vi-construire-et-exploiter-une-cartographie/03-chapitre-26-construire-le-graphe.md)
    - [Chapitre 27 — Lecture analytique d'une cartographie](06-partie-vi-construire-et-exploiter-une-cartographie/04-chapitre-27-lecture-analytique-d-une-cartographie.md)
    - [Chapitre 28 — Rédiger une note d'analyse](06-partie-vi-construire-et-exploiter-une-cartographie/05-chapitre-28-rediger-une-note-d-analyse.md)
- [Partie VII — Études de cas](07-partie-vii-etudes-de-cas.md)
- [Partie VIII — Limites, biais ET contre-analyse](08-partie-viii-limites-biais-et-contre-analyse.md)
- [Annexes](09-annexes/index.md)
    - [Annexe A — Glossaire](09-annexes/01-annexe-a-glossaire.md)
    - [Annexe B — Modèle de cartographie vierge](09-annexes/02-annexe-b-modele-de-cartographie-vierge.md)
    - [Annexe C — Grille de cotation et template de note d'analyse](09-annexes/03-annexe-c-grille-de-cotation-et-template-de-note-d.md)
    - [Annexe D — Cheat sheets techniques](09-annexes/04-annexe-d-cheat-sheets-techniques.md)
    - [Annexe E — Ressources et formation continue](09-annexes/05-annexe-e-ressources-et-formation-continue.md)
    - [Annexe F — Faux positifs classiques en cartographie d'écosystèmes](09-annexes/06-annexe-f-faux-positifs-classiques-en-cartographie.md)
