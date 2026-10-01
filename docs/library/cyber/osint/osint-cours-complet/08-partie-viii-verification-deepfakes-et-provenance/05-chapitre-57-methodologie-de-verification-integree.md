---
title: Chapitre 57 — Méthodologie de vérification intégrée
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VIII — Vérification, deepfakes et provenance
  - index.md
---

## 57.1 La vérification comme discipline

La **vérification** est la discipline qui transforme une information collectée en un fait coté. Elle a été codifiée par le journalisme d'investigation (Verification Handbook, Bellingcat), et l'OSINT moderne l'a adoptée.

Cinq dimensions de vérification : **source**, **contenu**, **contexte**, **temporalité**, **corroboration**.

## 57.2 Vérification de la source

**Qui publie ?** Un compte vérifié, un média établi, un blog inconnu, un compte anonyme ?

**Fiabilité historique.** La source a-t-elle un track record de fiabilité ? Est-elle connue pour publier de la désinformation ?

**Motivations.** La source a-t-elle un intérêt à publier ? (Promotion, vengeance, idéologie, agent étranger.)

**Cotation Admiralty A-F** : voir Ch.84. La source est cotée systématiquement.

## 57.3 Vérification du contenu

**Authenticité technique.**

- Métadonnées (EXIF, C2PA).
- Recherche inversée (Ch.46).
- Analyse technique (ELA, etc. — Ch.47).
- Détection IA (Ch.56).

**Cohérence interne.**

- Éléments visuels cohérents (Ch.54).
- Affirmations vérifiables.

**Faits invariants.**

- Géographie correcte ?
- Date plausible ?
- Personnes existantes ?

## 57.4 Vérification du contexte

**Contexte de production.**

- Où, quand, par qui a-t-il été produit ?
- Conditions de production cohérentes avec ce qu'il montre ?

**Contexte de diffusion.**

- Quand et par qui diffusé ?
- Premier publié ou recyclage d'ancien ?
- Diffusion organique ou amplification coordonnée ?

**Contexte sémantique.**

- Cadrage tronqué qui change le sens ?
- Légende trompeuse ?

## 57.5 Vérification temporelle

**Date de prise effective.**

- Métadonnées EXIF.
- Chronolocation (Ch.49).
- Cross-référence événements.

**Date de publication.**

- Première apparition (TinEye « first seen », Wayback).
- Diffusion ultérieure.

**Cohérence chronologique.**

- Présentée comme récente alors qu'ancienne ?
- Diffusion avant les événements supposés ?

## 57.6 Corroboration

**Multiple sources indépendantes.**

- Deux sources de la même chaîne d'agence ne sont pas indépendantes.
- Différentes perspectives géographiques et politiques renforcent.

**Cross-check sur faits vérifiables.**

- Détails qui peuvent être confirmés ou infirmés (météo, événements concurrents, présence de personnes connues).

**Triangulation.**

- Témoignages multiples.
- Sources documentaires.
- Sources techniques.

## 57.7 Workflow Verification Handbook

Le **Verification Handbook** (European Journalism Centre, multiples éditions) propose un workflow standard.

1. **Provenance** : d'où vient ?
2. **Source** : qui a posté ?
3. **Date** : quand ?
4. **Localisation** : où ?
5. **Motivation** : pourquoi ?

## 57.8 Bellingcat methodology

**Méthodologie Bellingcat** : ouverte, documentée, transparente.

**Principes.**

- Sources publiques exclusivement.
- Captures avec horodatage et préservation.
- Documentation de chaque étape.
- Conclusions cotées avec vocabulaire calibré.
- Publication transparente du raisonnement.

## 57.9 Information Laundromat et outils

**Information Laundromat** (Stanford Internet Observatory). Outil de cross-référencement de narratifs et opérations d'influence. Plus mature en 2025-2026.

**Hamilton 2.0** (German Marshall Fund). Monitoring opérations Russie/Chine.

**EU DisinfoLab.** Méthodologie référence pour CIB.

**Graphika** (sociale enterprise). Standards de référence sur CIB et analyse de réseaux.

## 57.10 Fact-checking professionnel

Les organisations de fact-checking professionnel (AFP Factuel, FactCheck.org, Snopes, Les Décodeurs, Liberation CheckNews) utilisent OSINT massivement.

**Différence OSINT vs fact-checking.**

- Fact-checking : finalité publication, vérification ponctuelle d'une affirmation.
- OSINT : finalité investigation, vue d'ensemble structurée.

Mais méthodologies convergent largement.

## 57.11 Cotation calibrée

À la fin de la vérification, **cotation explicite** :

- Source : A-F (Ch.84).
- Information : 1-6 (Ch.84).
- Conclusion : WEP (Ch.85).

**Exemple.**

- Image vérifiée comme authentique : source A1, contenu corroboré.
- Image vérifiée comme manipulée : source B (créateur opaque), contenu C (signaux techniques + recherche source).
- Conclusion : « la photographie est très probablement manipulée par face swap, niveau de confiance élevé ».

## 57.12 Synthèse — méthodologie de vérification

| Dimension | Méthode |
|---|---|
| Source | Identification, fiabilité, motivation |
| Contenu | Authenticité technique + cohérence interne |
| Contexte | Production + diffusion + sémantique |
| Temporalité | Date prise + date publication + cohérence |
| Corroboration | Sources indépendantes + cross-check |
| Synthèse | Cotation Admiralty + WEP + formulation calibrée |

-----
