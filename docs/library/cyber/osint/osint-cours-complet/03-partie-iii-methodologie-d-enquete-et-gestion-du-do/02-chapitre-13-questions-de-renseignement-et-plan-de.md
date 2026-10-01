---
title: Chapitre 13 — Questions de renseignement et plan de collecte
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 13.1 Du cadrage aux questions opérationnelles

Le cadrage produit des objectifs généraux. La phase suivante transforme ces objectifs en **questions de renseignement** précises, qui guideront la collecte.

Une question de renseignement (Intelligence Requirement, IR) est :

- **Fermée** : elle admet une réponse délimitée (oui/non, valeur, identifiant, liste).
- **Vérifiable** : on peut tester si la réponse trouvée est correcte.
- **Reformulable en hypothèse** : on peut imaginer une réponse alternative.
- **Pertinente** : sa réponse contribue à la décision attendue.

## 13.2 IR principales et IR secondaires

On distingue deux niveaux.

**IR principales** (3-5 maximum) : les questions critiques qui structurent l'enquête et conditionnent la décision finale.

**IR secondaires** (5-15 selon enquête) : les sous-questions qui alimentent les IR principales et organisent le travail tactique.

**Exemple sur MIRAGE.**

*IR principales.*

- IR1 : Marc Delaunay détient-il, contrôle-t-il ou bénéficie-t-il de sociétés offshore non déclarées ?
- IR2 : Existe-t-il des flux financiers visibles entre TechnoVert et ces sociétés ?
- IR3 : Delaunay possède-t-il des actifs (immobilier, crypto) incohérents avec ses revenus déclarés ?
- IR4 : Une campagne de désinformation contre Antoine Berthier est-elle organisée, et si oui, peut-elle être attribuée à Delaunay ou à son entourage ?
- IR5 : Des contenus synthétiques (deepfakes, photos IA) ont-ils été produits dans le cadre de cette campagne ?

*IR secondaires (extrait).*

- IR1a : Quelles sociétés offshore identifiables sont liées à Delaunay ?
- IR1b : Quels sont les UBO réels de ces sociétés ?
- IR1c : Y a-t-il des nominees, des prête-noms identifiables ?
- IR2a : Quels prestataires de TechnoVert reçoivent des paiements visibles vers ces sociétés ?
- IR2b : Existe-t-il des contrats publiés (annonces légales) entre TechnoVert et ces entités ?
- IR4a : Quels sont les comptes coordonnés diffusant des contenus diffamatoires ?
- IR4b : Existe-t-il un narratif central et une infrastructure (domaine, hébergement, créateurs) ?
- (etc.)

## 13.3 Formulation des IR : pièges à éviter

**Question trop large.** « Que peut-on dire sur Delaunay ? » → reformuler en sous-questions précises.

**Question fermée sans réponse possible.** « Delaunay a-t-il volé ? » → c'est une qualification pénale qui ne se prouve pas en OSINT.

**Question chargée.** « Comment Delaunay blanchit-il son argent ? » → présuppose la conclusion.

**Question sans lien à la décision.** « Combien a-t-il d'enfants ? » → si non pertinent pour la décision, à exclure.

**Reformulation correcte.** « Marc Delaunay détient-il, contrôle-t-il, ou bénéficie-t-il de sociétés non déclarées hors de France ? » → fermée, vérifiable, neutre, pertinente.

## 13.4 Hypothèses initiales

À chaque IR, on associe une ou plusieurs **hypothèses concurrentes** (méthode ACH — Ch.79). Cela structure la collecte autour de la **réfutation** plutôt que de la confirmation.

**Exemple IR1.**

- H1 : Delaunay détient personnellement plusieurs sociétés offshore.
- H2 : Delaunay est administrateur nominee, contrôlé par un tiers (vrai bénéficiaire ailleurs).
- H3 : Delaunay n'a aucun lien avec des sociétés offshore — soupçon infondé.

La collecte va chercher des éléments **pour ET contre** chaque hypothèse. C'est la garantie anti-biais.

## 13.5 Sources prioritaires par IR

À chaque IR, on associe les **sources prioritaires** où chercher la réponse.

**Tableau type.**

| IR | Hypothèse | Sources prioritaires |
|---|---|---|
| IR1 (offshores) | H1, H2, H3 | OpenCorporates, ICIJ Offshore Leaks, Pappers (volet français), Companies House (UK), Companies Registry (Malte, Chypre), BORIS |
| IR2 (flux) | (idem) | BODACC, annonces légales, presse économique, comptes consolidés AMF, Cyprus Confidential si applicable |
| IR3 (actifs) | (idem) | Cadastre, Pages Jaunes, presse locale, réseaux sociaux, registres maritime/aérien selon indices |
| IR4 (désinfo) | (idem) | X, Telegram, archive.today, WHOIS du domaine `verites-technovert.com`, hostnames cluster, EU DisinfoLab méthodologie |
| IR5 (deepfakes) | (idem) | Hive Moderation, Sensity AI, C2PA inspector, analyses image classiques (FotoForensics, ELA) |

Ce tableau est l'embryon du **plan de collecte**.

## 13.6 Plan de collecte

Le plan de collecte organise concrètement :

- Quelles IR sont travaillées en parallèle, lesquelles en séquence.
- Quels sélecteurs initiaux ouvrent la collecte (Ch.14).
- Quelle priorité (IR1 critique pour la décision, IR3 secondaire).
- Quels jalons (point à J+15, point à J+30).
- Quels arbitrages si une source-clé est inaccessible.

Pour une enquête de 6 semaines comme MIRAGE, le plan type :

- **Semaine 1** : OPSEC, sock puppets si nécessaire, recherche large sur Delaunay (personne + société), premier graphe.
- **Semaine 2** : Approfondissement corporate (sociétés offshore, UBO), pivot via WHOIS.
- **Semaine 3** : Volet financier visible, flux, ICIJ leaks, registres.
- **Semaine 4** : Volet désinformation (faux comptes, blog, faux médias), volet IA (deepfakes).
- **Semaine 5** : Volet crypto (triage OSINT, renvoi vers spécialiste si nécessaire), patrimoine immobilier.
- **Semaine 6** : Vérification, ACH, rédaction, revue, livraison.

Le plan reste **adaptatif**. Une découverte précoce peut réorienter. Mais avoir un plan évite la dérive.

## 13.7 Critères d'arrêt

Quand s'arrête-t-on de chercher ?

**Critères positifs.**

- Toutes les IR ont une réponse cotée.
- Le seuil de confiance pour la décision est atteint.
- Le budget est consommé.
- Le délai est consommé.

**Critères négatifs (rebond).**

- Une IR centrale reste sans réponse → escalade ou décision sur la limite à présenter.
- Une découverte ouvre un volet nouveau (élargissement du périmètre à valider avec commanditaire).
- Une source-clé inaccessible compromet la mission (renégociation).

L'analyste qui ne sait pas s'arrêter dérive vers la collecte infinie. La discipline d'arrêt est aussi importante que la discipline de pivot.

> **MIRAGE — Épisode 1 : Questions de renseignement**
>
> Lundi 19 mai 2026. L'analyste tient une séance de cadrage IR avec Me Legrand. Cinq IR principales sont formalisées (supra), avec 18 IR secondaires. Pour chaque IR, deux à trois hypothèses concurrentes sont posées. Le plan de collecte est calé sur 6 semaines avec jalons à J+15 (revue avec Me Legrand) et J+30 (point d'étape).
>
> L'analyste insiste sur un point : la décision est un dépôt de plainte. Le seuil de preuve attendu est donc « faisceau d'indices convergents suffisant pour saisir le PNF », pas une « preuve au sens pénal ». Cette clarification calibre l'effort : on ne cherche pas l'irréfutable, on cherche un dossier soutenable.

-----
