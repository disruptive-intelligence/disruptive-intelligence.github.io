---
title: Chapitre 81 — Raisonnement adversaire
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 81.1 Penser comme l'adversaire

Le **raisonnement adversaire** consiste à se mettre dans la position de l'opposant pour anticiper ses contre-mesures.

**Pour OSINT.**

- Comment la cible pourrait-elle manipuler les sources que j'observe ?
- Quelles fausses pistes pourrait-elle planter ?
- Comment pourrait-elle détecter mon investigation ?
- Comment retournerait-elle mon analyse contre moi ?

## 81.2 Leurres et faux signaux

**Cas.** Cible compétente plante des leurres :

- Fausses identités sur réseaux sociaux.
- Faux comptes pour amplifier diversion.
- Fausses pistes (sociétés écrans pour distraire).
- Faux indices techniques (User-Agent volontairement misleading).

**Défense.**

- Cross-vérification multiples.
- Cohérence interne des éléments.
- Suspicion saine.

## 81.3 Planting d'évidences

**Cas avancé.** Cible plante des évidences trompeuses (faux documents leakés, faux comptes coordonnés pointant ailleurs).

**Défense.**

- Provenance toujours suspecte.
- Vérification croisée indépendante.
- Source primaire vs source secondaire.

## 81.4 Counter-OSINT

**Cible aguerrie pratique du counter-OSINT.**

**Méthodes adverses.**

- Honeypot social.
- Désinformation contrôlée.
- Monitoring des consultations.
- Identités secondaires propres.

Voir Ch.10 pour défense.

## 81.5 Devil's advocate institutionnel

Dans une cellule ou cabinet, **rôle formalisé** de devil's advocate.

**Pratique.**

- Un membre de l'équipe (par roulement) joue ce rôle.
- Conteste systématiquement les conclusions de l'équipe.
- Pose les questions inconfortables.
- Cherche les failles méthodologiques.

## 81.6 Red teaming

**Red team.** Équipe qui adopte le rôle de l'adversaire pour tester analyses ou systèmes.

**Pour OSINT.**

- Red team relit le rapport.
- Identifie failles.
- Propose interprétations alternatives.

## 81.7 Pre-mortem

**Pre-mortem.** Imaginer que le rapport a échoué (preuves invalidées, conclusion fausse). Pourquoi ? Quelles failles ?

**Bénéfice.** Découvrir les vulnérabilités avant publication.

## 81.8 Key Assumptions Check

**Méthode IC US.** Lister les hypothèses tacites sur lesquelles repose l'analyse. Tester chacune.

**Exemple MIRAGE.**

- Hypothèse tacite : « les communiqués TechnoVert sont fiables. »
- Test : et s'ils étaient eux-mêmes manipulés ?
- Implication : vérifier cohérence avec sources externes.

## 81.9 Liste de contrôle adversaire

Avant publication :

1. Quelle évidence pourrait être plantée ?
2. Quelle source pourrait être contrôlée par la cible ?
3. Quelle interprétation alternative privilégierait l'avocat de la défense ?
4. Comment la cible utilisera-t-elle ce rapport contre moi (procédure abusive) ?
5. Quelles erreurs identifierait un expert en contre-expertise ?

## 81.10 Synthèse

Le raisonnement adversaire est un **multiplicateur de qualité**. Une analyse qui résiste à devil's advocate, red team, pre-mortem est défendable. Une analyse qui n'a pas été testée ainsi est fragile.

-----
