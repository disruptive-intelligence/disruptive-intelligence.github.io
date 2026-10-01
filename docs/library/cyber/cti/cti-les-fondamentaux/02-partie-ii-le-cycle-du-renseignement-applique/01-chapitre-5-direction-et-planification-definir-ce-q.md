---
title: 'Chapitre 5 — Direction et planification : définir ce qu''on cherche'
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - Partie II — Le cycle du renseignement appliqué
  - index.md
---

## 5.1 Les PIR (Priority Intelligence Requirements)

Les PIR sont les questions stratégiques auxquelles la CTI doit répondre. Sans PIR, la CTI produit du bruit — des rapports intéressants mais non ciblés, des IoC par milliers sans priorisation, des analyses brillantes qui ne répondent à aucun besoin opérationnel. Les PIR sont la boussole qui oriente chaque étape du cycle.

Un bon PIR est spécifique (pas « que se passe-t-il dans la menace ? » mais « quels acteurs ciblent les opérateurs de distribution d'énergie en Europe, avec quelles TTP, et notre couverture de détection couvre-t-elle ces TTP ? »), mesurable (on peut évaluer si le PIR a reçu une réponse), orienté décision (la réponse au PIR doit conduire à une action — déployer des détections, ajuster la posture, informer la direction), et temporel (le PIR a une période de validité — il est réexaminé trimestriellement).

Les PIR sont co-construits avec le RSSI (qui apporte la vision stratégique et la connaissance des risques business), le SOC manager (qui apporte la connaissance des capacités de détection et des gaps), l'IR lead (qui apporte le retour d'expérience des incidents passés), et les métiers (qui apportent la connaissance des actifs critiques et des enjeux business). La CTI seule ne peut pas définir ses propres PIR — elle les définit avec ses consommateurs.

## 5.2 Des PIR aux IR et au plan de collecte

Chaque PIR se décline en **IR** (Intelligence Requirements) plus granulaires, qui eux-mêmes orientent le plan de collecte. Exemple de décomposition pour la mission MERIDIAN :

**PIR 1 :** Qui est UNC-VOLT ? → IR 1.1 : Quelles TTP caractéristiques UNC-VOLT utilise-t-il ? → IR 1.2 : Ces TTP correspondent-elles à un acteur connu ? → IR 1.3 : Quel est le sponsor présumé ? → Plan de collecte : analyse des artefacts IR, corrélation avec les bases ATT&CK, recherche dans les rapports communautaires et commerciaux.

**PIR 2 :** UNC-VOLT cible-t-il d'autres opérateurs d'énergie ? → IR 2.1 : Les IoC de l'incident EDE apparaissent-ils dans les feeds communautaires ? → IR 2.2 : Des incidents similaires ont-ils été signalés par l'ISAC énergie ? → Plan de collecte : partage d'IoC via MISP (ISAC énergie), requêtes auprès des contacts communautaires, monitoring des rapports vendor sur le secteur énergie.

**PIR 3 :** Quelle est la menace résiduelle pour EDE ? → IR 3.1 : Les mécanismes de persistance ont-ils tous été éradiqués ? → IR 3.2 : L'attaquant a-t-il d'autres points d'entrée (vulnérabilités non patchées, credentials non resetés) ? → Plan de collecte : revue des conclusions IR, audit des vulnérabilités exposées, monitoring dark web pour les credentials EDE.

## 5.3 Fil rouge — MERIDIAN : les PIR

> **🔎 MERIDIAN — Épisode 4**
>
> Élise formule 5 PIR validés avec Thomas Kessler (RSSI d'EDE) et l'équipe Sentinelle.
>
> PIR 1 : Identité et attribution de UNC-VOLT (qui, sponsor, niveau de confiance)
> PIR 2 : Victimologie élargie (d'autres opérateurs énergie sont-ils ciblés ?)
> PIR 3 : Menace résiduelle pour EDE (l'attaquant va-t-il revenir ? par quel vecteur ?)
> PIR 4 : TTP à anticiper (quelles techniques futures utiliserait UNC-VOLT s'il revient ?)
> PIR 5 : Couverture de détection (nos détections couvrent-elles les TTP de UNC-VOLT ?)

---
