---
title: Chapitre 84 — Cotation source / information (Admiralty)
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 84.1 La grille Admiralty

La **grille Admiralty** est le standard de cotation hérité du renseignement militaire britannique et adopté internationalement (NATO, US IC, services européens).

Elle cote deux dimensions :

- **Fiabilité de la source** (A-F).
- **Crédibilité de l'information** (1-6).

**Pour OSINT, c'est le standard de référence.**

## 84.2 Échelle A-F : fiabilité de la source

- **A** — **Complètement fiable**. Source dont la fiabilité est démontrée sans réserve. Ex : registre officiel, communiqué officiel d'une institution réputée.
- **B** — **Habituellement fiable**. Source avec historique de fiabilité élevé. Ex : grande presse établie, ICIJ leaks vérifiés.
- **C** — **Plutôt fiable**. Source généralement fiable mais avec quelques erreurs documentées. Ex : presse spécialisée correcte, blog d'expert reconnu.
- **D** — **Plutôt non fiable**. Source avec historique mixte ou faible. Ex : blogs anonymes, certains réseaux sociaux.
- **E** — **Non fiable**. Source historiquement peu fiable.
- **F** — **Non évaluable**. Source sans historique ou inconnue.

## 84.3 Échelle 1-6 : crédibilité de l'information

- **1** — **Confirmée**. Information confirmée par multiples sources indépendantes fiables.
- **2** — **Probablement vraie**. Cohérente avec autres informations connues, plausible.
- **3** — **Possiblement vraie**. Pas contredite, mais peu corroborée.
- **4** — **Doute**. Cohérence faible avec autres données.
- **5** — **Improbable**. Contradictions avec sources fiables.
- **6** — **Non évaluable**. Manque d'information pour juger.

## 84.4 Notation combinée

Chaque fait porte une cotation **lettre + chiffre** : **A1**, **B2**, **C3**, etc.

**Exemples MIRAGE.**

- Marc Delaunay est DAF TechnoVert : **A1** (multi-sources A indépendantes confirmant).
- Email perso `marc.delaunay76@gmail.com` : **B2** (faisceau indices convergents).
- Cluster désinformation orchestré par Delaunay : **B3** (cohérence forte mais pas démonstration directe).
- Allégations vidéo deepfake du contenu : **A1** (analyses techniques convergentes).

## 84.5 Indépendance des sources

**Critère central.** Pour cotation 1 (confirmé), sources doivent être **indépendantes**.

**Non indépendant.** Articles qui se citent. Multiple agences reprenant même dépêche.

**Indépendant.** Sources avec accès propre, perspectives différentes.

## 84.6 Corroboration vs corrélation

**Corroboration.** Plusieurs sources reportent le même fait depuis canaux différents.

**Corrélation.** Plusieurs faits cohérents entre eux mais sans confirmation directe.

**Pour cotation.** Corroboration → 1 ou 2. Corrélation seule → 3.

## 84.7 Cotation des LLMs

**Important.** Un LLM **n'est jamais une source cotable**. C'est un assistant.

**Mauvaise pratique.** Coter « Claude m'a confirmé » A1.

**Bonne pratique.** Coter la source primaire que le LLM a identifiée (après vérification directe).

## 84.8 Limites de l'auto-cotation

L'analyste cote ses propres sources. Subjectivité existe.

**Garde-fous.**

- Justification explicite de chaque cotation.
- Revue par pair.
- Cohérence interne (mêmes sources cotées de même).

## 84.9 Cotation en équipe

En cabinet, **harmonisation** des cotations :

- Charte interne définissant standards.
- Revue croisée.
- Calibration périodique.

## 84.10 Synthèse — discipline de cotation

> **Règle d'or.** Chaque fait dans un rapport porte sa cotation. Aucune affirmation sans cotation. Aucune cotation sans justification.

-----
