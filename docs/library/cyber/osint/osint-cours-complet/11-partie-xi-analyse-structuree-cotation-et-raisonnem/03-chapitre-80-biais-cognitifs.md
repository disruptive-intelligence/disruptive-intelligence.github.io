---
title: Chapitre 80 — Biais cognitifs
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 80.1 L'analyste face à ses biais

L'**analyste OSINT** est humain. Ses jugements sont sujets aux biais cognitifs documentés en psychologie. Reconnaître ses biais est la première défense contre eux.

## 80.2 Biais de confirmation

**Le plus important.** Tendance à chercher / privilégier les informations qui confirment l'hypothèse de départ.

**Symptômes.**

- Lecture sélective.
- Mémorisation différentielle.
- Interprétation favorable.

**Défense.**

- ACH systématique.
- Devil's advocate.
- Revue par pair.

## 80.3 Ancrage

**Tendance.** S'accrocher à la première information rencontrée comme référence (ancre).

**Symptômes.**

- L'estimation de revenus est faussée par la première mention vue.
- L'opinion sur la cible est ancrée sur le premier rapport.

**Défense.**

- Plusieurs sources avant conclusion.
- Réviser explicitement.

## 80.4 Disponibilité (availability)

**Tendance.** Sur-pondérer ce qu'on retrouve facilement / récemment.

**Symptômes.**

- Sur-représentation des cas médiatisés.
- Oubli des cas peu visibles.

**Défense.**

- Recherche systématique au-delà du visible.
- Quantification.

## 80.5 Narratif séduisant

**Tendance.** Préférer la version « belle histoire » (qui s'enchaîne logiquement) à la version probable.

**Symptômes.**

- Causalité reconstruite après les faits.
- Coïncidences mal pondérées.

**Défense.**

- Exigence de probabilité, pas de joli récit.
- Tester la version « banale » (rien de coordonné, juste coïncidence).

## 80.6 Causalité abusive

**Tendance.** Inférer cause à partir de corrélation.

**Symptômes.**

- A se passe après B, donc B a causé A.
- Co-occurrence interprétée comme lien causal.

**Défense.**

- Penser aux causes communes alternatives.
- Cohérence temporelle ≠ cohérence causale.

## 80.7 Homonymie

**Spécifique OSINT.** Confondre deux personnes du même nom.

**Symptômes.** Faits attribués à mauvaise personne.

**Défense.**

- Enrichissement systématique (Ch.26).
- Cross-vérification.

## 80.8 Effet outil

**« Si vous avez un marteau, tout ressemble à un clou. »**

**Symptômes.**

- Analyste expert OSINT crypto voit du crypto partout.
- Expert FININT voit du blanchiment partout.

**Défense.**

- Pluridisciplinarité.
- Méthodes structurées.

## 80.9 Effet halo

**Tendance.** Une qualité (positive ou négative) contamine la perception d'autres qualités.

**Symptômes.**

- Une personne identifiée comme « riche » est présumée intelligente.
- Une entreprise impliquée dans un scandale est présumée mauvaise sur tout.

**Défense.**

- Évaluation indépendante par dimension.

## 80.10 Biais de groupe

**Groupthink.** Conformité au consensus de l'équipe / communauté.

**Symptômes.**

- Reprise non critique des analyses communautaires.
- Pas d'expression du désaccord.

**Défense.**

- Devil's advocate explicite.
- Réflexion individuelle avant discussion collective.

## 80.11 Biais de récence

**Tendance.** Sur-pondérer les informations récentes.

**Défense.**

- Cadrage temporel large.
- Historique systématique.

## 80.12 Aversion à l'incertitude

**Tendance.** Préférer une conclusion fausse mais nette à une conclusion juste mais incertaine.

**Symptômes.**

- Cotation arbitraire « probable » au lieu de « possible ».
- Rapport qui sur-affirme.

**Défense.**

- WEP (Ch.85) systématique.
- Vocabulaire calibré.
- Documentation des limites.

## 80.13 Sunk cost (coûts irrécupérables)

**Tendance.** Continuer une piste fausse parce qu'on y a investi.

**Symptômes.**

- Refuser d'abandonner une hypothèse coûteuse à abandonner.

**Défense.**

- Critères d'arrêt définis ex ante.
- Revue mi-parcours.

## 80.14 Liste de contrôle anti-biais

Avant publication, **se poser ces questions** :

1. Ai-je cherché à infirmer mon hypothèse autant qu'à la confirmer ?
2. Si je n'avais aucune information préalable, lirais-je les mêmes preuves ?
3. Mes coups de cœur méthodologiques ont-ils influencé ?
4. Ai-je écarté des hypothèses alternatives ?
5. Ai-je sur-affirmé pour éviter d'admettre incertitude ?
6. Ai-je traité tous les sous-éléments de la cible avec la même rigueur ?

## 80.15 Synthèse

| Biais | Symptôme | Défense |
|---|---|---|
| Confirmation | Lecture sélective | ACH |
| Ancrage | Première info dominante | Multi-sources |
| Disponibilité | Sur-rep accessible | Recherche systématique |
| Narratif | Belle histoire préférée | Version banale aussi |
| Causalité abusive | Corrélation → cause | Causes alternatives |
| Homonymie | Confusion personnes | Enrichissement |
| Effet outil | Tout est X | Pluridisciplinaire |
| Halo | Une qualité contamine | Évaluation indépendante |
| Groupthink | Conformité équipe | Devil's advocate |
| Récence | Sur-rep récent | Cadrage large |
| Aversion incertitude | Sur-affirmation | WEP discipliné |
| Sunk cost | Persistance hypothèse coûteuse | Critères arrêt |

## 80.16 Biais d'autorité

**Tendance.** Sur-pondérer les affirmations issues de sources prestigieuses (institution, expert connu, média établi).

**Symptômes.**

- Acceptation moindre vérification quand source autoritative.
- Sous-pondération de sources non prestigieuses même quand justes.

**Défense.**

- Cotation Admiralty appliquée uniformément (même source NYT ne devient pas A1 automatiquement).
- Vérification du fait, pas de la source.

## 80.17 Biais de proportion (taille de l'échantillon)

**Tendance.** Tirer des conclusions sur petits échantillons. Sur-généraliser à partir de cas individuels.

**Symptômes.**

- « Tous les Russes pensent X » à partir de 3 tweets.
- « Le pattern Y est confirmé » sur 5 occurrences.

**Défense.**

- Distinguer cas individuel et tendance.
- Volume requis pour généraliser.

## 80.18 Biais de cadrage (framing)

**Tendance.** Conclusion influencée par la façon dont la question est posée.

**Symptômes.**

- Question « X est-il coupable ? » oriente vers chercher culpabilité.
- Question « Que s'est-il passé ? » est plus neutre.

**Défense.**

- Reformuler les IR de façon neutre.
- Tester avec cadrages alternatifs.

## 80.19 Biais d'attribution

**Tendance.** Attribuer les comportements observés à dispositions internes plutôt qu'à situations.

**Symptômes.**

- « Delaunay a fui » → présomption de culpabilité.
- Alors qu'il pouvait avoir d'autres raisons (mission, vacances, problème personnel).

**Défense.**

- Considérer explications situationnelles.
- Faire ACH avec hypothèses alternatives.

## 80.20 Méthodologie debiasing intégrée

**Avant l'enquête.**

- Identifier biais probables compte tenu du sujet.
- Documenter dans le journal.

**Pendant.**

- Devil's advocate par épisode majeur.
- Multi-sources systématique.
- Cotation rigoureuse.

**Avant publication.**

- Liste de contrôle anti-biais (80.14 + 80.16-80.19).
- Revue par pair.
- Test du « j'ai été récruté par la cible : comment réfuterais-je ce rapport ? ».

**Post-publication.**

- Debriefing : quels biais ont été identifiés ? Lesquels ont été surmontés ? Lesquels ont peut-être pollué ?

> **Principe.** Les biais ne disparaissent pas par bonne volonté. Seules les **méthodes structurées** (ACH, devil's advocate, revue par pair, cotation calibrée) en réduisent l'impact. La rigueur méthodologique est anti-biais par construction.

-----
