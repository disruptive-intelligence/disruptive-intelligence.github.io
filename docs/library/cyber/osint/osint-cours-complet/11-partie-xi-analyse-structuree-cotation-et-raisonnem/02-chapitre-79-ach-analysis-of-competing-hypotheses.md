---
title: 'Chapitre 79 — ACH : Analysis of Competing Hypotheses'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 79.1 Méthode Heuer

L'**ACH** (Analysis of Competing Hypotheses) a été développée par **Richards Heuer** (CIA, années 1970-80, publié 1999 dans « Psychology of Intelligence Analysis »).

**Idée centrale.** L'esprit humain cherche naturellement à **confirmer** une hypothèse plutôt qu'à la **réfuter** (biais de confirmation). L'ACH inverse cette tendance : on cherche à **infirmer** les hypothèses.

**Méthode.** Lister hypothèses concurrentes, lister évidences, marquer pour chaque évidence si elle est compatible / incompatible / neutre avec chaque hypothèse. **L'hypothèse la moins infirmée** est retenue, pas l'hypothèse la plus confirmée.

## 79.2 Étapes ACH

**Étape 1.** Identifier les hypothèses concurrentes possibles (3-7 en pratique).

**Étape 2.** Lister les évidences et arguments (faits, indices, données).

**Étape 3.** Construire une matrice (hypothèses en colonnes, évidences en lignes).

**Étape 4.** Pour chaque cellule, indiquer :

- C : Compatible.
- I : Incompatible.
- N : Neutre.

**Étape 5.** Refine. Identifier évidences les plus discriminantes.

**Étape 6.** Sélectionner l'hypothèse **la moins infirmée**.

**Étape 7.** Identifier les évidences qui pourraient changer la conclusion.

**Étape 8.** Rapport et suivi.

## 79.3 Exemple ACH appliqué à MIRAGE IR1

**IR1.** Marc Delaunay détient-il, contrôle-t-il ou bénéficie-t-il de sociétés offshore non déclarées ?

**Hypothèses.**

- H1 : Detient personnellement plusieurs sociétés offshore avec bénéfice personnel.
- H2 : Administrateur nominee, contrôlé par tiers (vrai bénéficiaire ailleurs).
- H3 : Aucun lien réel avec sociétés offshore non déclarées (soupçon infondé).

**Évidences.**

| Évidence | H1 | H2 | H3 |
|---|---|---|---|
| Admin déclaré Delta Consulting (Malte) | C | C | I |
| Admin déclaré Verde Holdings (Chypre) | C | C | I |
| Email personnel dans WHOIS de domaine perso 2017 | N | N | N |
| Cyprus Confidential : flux TechnoVert → Delta → Verde | C | C | I |
| Patrimoine immobilier incohérent avec revenus | C | C | I |
| Aucun déclaration française des entités offshore | C | C | I |
| Pas de partenaire offshore identifié (autre UBO suggéré) | C | I | C |
| Activité offshore réelle pour bénéfice perso | (à vérifier) | (à vérifier) | (à vérifier) |

**Analyse.** H3 est **multiplement incompatible** → réfutée. H1 et H2 restent ouvertes. **H1 mieux soutenue** par absence de partenaire offshore identifiable (qui serait attendu si H2). Mais H2 reste possible avec partenaires bien dissimulés.

**Conclusion préliminaire.** « Faisceau d'indices convergents vers une **détention personnelle effective** par Delaunay de structures offshore non déclarées (H1 fortement soutenue, H2 résiduellement possible, H3 réfutée). »

**Niveau de confiance.** **Élevé** sur l'existence de structures offshore liées à Delaunay (H3 réfuté). **Probable** sur la nature « bénéfice personnel direct » (H1 vs H2).

## 79.4 Avantages ACH

**Anti-biais de confirmation.** Force à chercher évidences contre l'hypothèse préférée.

**Transparence.** Matrice publique du raisonnement.

**Robustesse.** Conclusion défendable contre objection (« voici la matrice »).

**Identification points faibles.** Met en évidence ce qui reste à investiguer.

## 79.5 Limites ACH

**Incompletes.** Toujours possible qu'une hypothèse non listée soit la vraie.

**Subjectivité.** L'attribution C/I/N reste un jugement.

**Inertie.** Pas idéal pour situations très dynamiques.

## 79.6 Variantes

**ACH-CD** (ACH with Cluster Deception). Intègre possibilité que sources soient manipulées.

**SATs** (Structured Analytic Techniques, IC US). Catalogue de techniques dont ACH.

**Red teaming.** Voir Ch.81.

## 79.7 Outils

**Hand-rolled.** Tableau Excel / Markdown / Obsidian.

**ACH software.** Palo Alto Research Center (PARC), CIA legacy.

**Pour OSINT pratique.** Tableau structuré dans vault d'enquête.

## 79.8 ACH dans rapport

**Bonne pratique.** Inclure la matrice ACH en annexe du rapport, ou résumer dans la section analyse.

**Bénéfice.** Démontre la rigueur, anticipe objections, transparente le raisonnement.

## 79.9 Quand utiliser ACH

**Adapté.**

- Décisions importantes.
- Sujets contestés.
- Plusieurs interprétations plausibles.
- Risque de biais.

**Pas nécessaire pour.**

- Faits simples corroborés.
- Identification routinière.

## 79.10 Synthèse

L'ACH est **l'outil méthodologique central** pour analyse OSINT mature. Tout analyste OSINT senior devrait maîtriser.

> **MIRAGE — Épisode 19 : Hypothèses concurrentes**
>
> L'analyste construit la matrice ACH pour les 5 IR principales. Conclusion :
> - IR1 (offshores) : H1 fortement soutenue, H2 résiduelle, H3 réfutée.
> - IR2 (flux) : flux TechnoVert→Delta confirmés (Cyprus Confidential + BODACC indices). H1 fortement.
> - IR3 (patrimoine incohérent) : incohérence visible. Hypothèse alternative (héritage, mariage favorable) à investiguer.
> - IR4 (désinfo coordonnée) : H1 (campagne coordonnée existe) fortement soutenue (cohérence technique et temporelle).
> - IR5 (contenus IA) : H1 (deepfakes et fausses photos fabriqués) fortement soutenue (analyses techniques convergentes).
>
> Le rapport inclura les matrices ACH résumées en annexe.

-----
