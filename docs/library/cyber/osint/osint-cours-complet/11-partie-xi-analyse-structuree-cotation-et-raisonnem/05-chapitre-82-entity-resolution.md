---
title: Chapitre 82 — Entity resolution
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 82.1 Le problème

Une enquête identifie souvent **plusieurs références** à la même entité réelle, sous des formes différentes. **Entity resolution** = fusion correcte de ces références.

**Cas typique.**

- « Marc Delaunay » dans LinkedIn.
- « M. Delaunay » dans communiqué.
- « Marc H. Delaunay » dans Pappers.
- « marcdelaunay76 » sur Twitter.

→ Même personne ? L'analyste doit décider.

## 82.2 Fusion d'identités : critères

**Forte présomption.**

- Mêmes sélecteurs forts (email, téléphone, identifiant unique).
- Photo identique cross-références.
- Mention explicite « connu sous le pseudo X ».

**Présomption.**

- Cohérence parcours, dates, lieu.
- Cohérence linguistique, stylistique.

**Présomption faible.**

- Similitudes nominales seules.
- Co-occurrence dans même milieu.

**Aucune présomption.**

- Coïncidence de nom commun.

## 82.3 Doublons et homonymes

**Doublons.** Plusieurs références à même entité.

**Homonymes.** Plusieurs entités distinctes avec mêmes éléments superficiels.

**Différenciation.** Cross-vérification systématique.

## 82.4 Entités faibles vs entités fortes

**Entité faible.** Mention sans sélecteur discriminant (« un certain Delaunay »).

**Entité forte.** Sélecteurs uniques (email, téléphone, numéro identité).

**Pratique.** Toujours s'efforcer de renforcer les entités faibles avant intégration dans le graphe.

## 82.5 Outils entity resolution

**Manuels.** Analyse cas par cas. Pour petites enquêtes.

**Semi-automatiques.**

- **RapidFuzz** (Python) : fuzzy matching strings.
- **dedupe.io** (Python library) : entity resolution structurée.
- **Splink** (UK gov) : pour grands volumes.

**Algorithmes.**

- Jaro-Winkler, Levenshtein pour distance de noms.
- Soundex, Metaphone pour phonétique.

## 82.6 Discipline pour graphe d'enquête

**Avant insertion** dans le graphe d'enquête, validation :

- Sélecteurs identifiants vérifiés.
- Sources documentées.
- Cotation Admiralty initiale.

**Discipline.** Une entité douteuse marquée comme telle (« hypothèse forte non confirmée »). Pas de pollution du graphe par entités mal résolues.

## 82.7 Liens faibles vs forts

**Lien fort.**

- Officiellement documenté (registre, contrat).
- Cohérence cross-sources.

**Lien faible.**

- Coïncidence temporelle / géographique.
- Mention sans confirmation.

**Pratique.** Annoter les arêtes du graphe par force du lien.

## 82.8 Exemple MIRAGE

**Marc Delaunay** : entité forte (multi-sources A1 convergentes).

**Société Delta Consulting Ltd** : entité forte (Companies Registry Malte).

**Lien Delaunay → Delta** : lien fort (admin déclaré).

**Lien Delaunay → cluster désinformation** : lien faible (cohérence d'intérêt, pas démonstration directe).

## 82.9 Pièges

**Sur-fusion.** Fusionner indûment deux entités distinctes → confusion catastrophique.

**Sous-fusion.** Maintenir doublons → analyse fragmentée.

## 82.10 Synthèse

Entity resolution est **discipline silencieuse** mais critique. Une analyse OSINT mature consacre 10-20 % du temps à l'entity resolution. Sans, le graphe est inutilisable.

-----
