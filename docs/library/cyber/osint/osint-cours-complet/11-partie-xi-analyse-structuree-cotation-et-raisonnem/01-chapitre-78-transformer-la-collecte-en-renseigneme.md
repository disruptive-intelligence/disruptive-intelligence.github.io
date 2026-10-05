---
title: Chapitre 78 — Transformer la collecte en renseignement
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 78.1 De la masse au sens

Une enquête mature accumule **des centaines de pièces** : captures, documents, résultats de recherche, exports d'outils. Cette masse n'est pas du renseignement. Le renseignement émerge de **l'analyse structurée** de cette masse.

Trois opérations clés transforment la collecte en renseignement : **tri**, **corrélation**, **synthèse**.

## 78.2 Tri et qualification

**Première opération.** Évaluer chaque pièce :

- Pertinente pour quelle IR ?
- Source cotée.
- Niveau d'évidence (donnée, indice, fait — Ch.4).
- À conserver, à approfondir, à écarter.

**Outil.** Tableau de qualification dans le vault.

## 78.3 Déduplication

Plusieurs sources reportent souvent **le même fait**. Identifier les redondances vs vraies corroborations.

**Redondance.** Articles qui se citent l'un l'autre = 1 source recyclée, pas N sources indépendantes.

**Corroboration vraie.** Sources indépendantes qui reportent le même fait depuis canaux différents.

## 78.4 Corrélation

**Cross-référencement des données collectées.**

**Exemples.**

- Email apparaît dans WHOIS + breach → confirme propriétaire.
- Personne photo + lieu sur Instagram + propriété cadastre → consolide propriété.
- Timing post X + timing publication blog → coordination.

**Outils.** Graphes (Maltego, Neo4j, Obsidian), timelines, matrices.

## 78.5 Synthèse

**Synthèse** = production d'une vue d'ensemble cohérente.

**Niveaux.**

- Synthèse par IR.
- Synthèse globale.
- Identification des points-clés (ce qui change la décision).
- Identification des limites (ce qu'on ne sait pas).

## 78.6 Test de stress

Avant rédaction du rapport, **stress test** :

**Questions.**

- Si on me demande de défendre cette conclusion en audition, qu'est-ce que je dirais ?
- Quelle question difficile peut-on me poser ?
- Quels faits puis-je oublier ?
- Quel biais peut m'avoir égaré ?

## 78.7 Revue par pair

Si possible, un confrère **relit avant publication**.

**Bénéfice.** Œil frais identifie biais et lacunes.

**Pratique.** Briefing court (15-30 min) au confrère, lecture du rapport, commentaires.

## 78.8 Différence collecte / renseignement

**Collecte.** « J'ai trouvé X. »

**Renseignement.** « X, coté A2, en faisceau avec Y et Z, supporte l'hypothèse H1 avec niveau de confiance « probable », sous réserve des limites L1 et L2. »

La différence est dans la **structuration** et la **qualification**.

## 78.9 Synthèse — passage collecte → renseignement

| Étape | Action |
|---|---|
| Tri | Pertinence par IR |
| Qualification | Niveau (donnée, indice, fait) |
| Déduplication | Redondance vs corroboration |
| Corrélation | Cross-référence multi-domaines |
| Synthèse | Vue d'ensemble cohérente |
| Stress test | Anticiper objections |
| Revue pair | Œil frais |

## 78.10 Frameworks d'analyse structurée IC

L'IC US a structuré en **Structured Analytic Techniques (SATs)** un ensemble de méthodes formalisées. Référence : Heuer & Pherson, « Structured Analytic Techniques for Intelligence Analysis » (3e éd. 2020).

**Catégories de SATs.**

**Diagnostic.**

- Key Assumptions Check (vérification des hypothèses tacites).
- Quality of Information Check (qualité des sources).
- Indicators and Signposts (signaux d'évolution).

**Contrarian.**

- Devil's Advocacy (Ch.81).
- Team A / Team B (équipes opposées).
- Red Cell (rôle adversaire).
- High-Impact / Low-Probability (scénarios extrêmes).

**Imaginative.**

- Brainstorming structuré.
- Outside-In Thinking (vue extérieure).
- Red Hat Analysis (perspective adverse).
- Alternative Futures (scénarios).

**Hypothesis.**

- ACH (Ch.79).
- ACH-CD (Cluster Deception variant).
- Argument Mapping.

**Causal.**

- Causal Flow Diagram.
- Force Field Analysis.

Pour l'OSINT, les SATs les plus mobilisés sont : ACH, Key Assumptions Check, Devil's Advocacy, Quality of Information Check, Indicators and Signposts.

## 78.11 Key Assumptions Check

Le **Key Assumptions Check** identifie et teste les hypothèses tacites sur lesquelles repose l'analyse.

**Méthode.**

1. Lister explicitement les hypothèses non démontrées qui sous-tendent l'analyse.
2. Pour chaque hypothèse, évaluer :
    - Est-elle nécessaire ?
    - Est-elle vraie ?
    - Quelle évidence la soutient ?
    - Quelle évidence la contredirait ?
3. Identifier les hypothèses dont l'invalidation casserait l'analyse.
4. Tester ces hypothèses avec sources spécifiques.

**Exemple MIRAGE.** Hypothèse tacite : « Les comptes consolidés TechnoVert publiés sont fiables. » Test : et s'ils avaient été manipulés pour masquer le détournement ? Implication : ne pas se baser uniquement sur ces comptes, croiser avec d'autres signaux.

## 78.12 Quality of Information Check

Vérification systématique de la qualité des sources.

**Critères.**

- Source primaire ou secondaire ?
- Fiabilité historique de la source.
- Indépendance des sources entre elles.
- Possibilité de manipulation par cible.
- Possibilité d'erreur d'attribution.
- Cohérence temporelle.

**Pour chaque pièce clé du dossier**, audit indépendant. Identification des points faibles.

## 78.13 Indicators and Signposts

Identification de **signaux observables** qui confirmeraient ou infirmeraient les hypothèses retenues.

**Pour l'enquête en cours.**

- Quels signaux supplémentaires confirmeraient mon hypothèse principale ?
- Quels signaux la réfuteraient ?
- Comment les obtenir ?

**Pour la veille post-rapport.**

- Quels signaux surveiller pour suivre l'évolution ?
- Critères d'alerte.

## 78.14 Argument mapping

Représentation graphique du **raisonnement** : prémisses, inférences, conclusions, contre-arguments.

**Méthode.** Schéma arborescent ou réseau qui rend visible la structure logique de l'analyse. Permet d'identifier les sauts logiques, les inférences faibles, les hypothèses cachées.

**Outils.** Argumap, Rationale, papier-crayon, Miro / FigJam.

## 78.15 Synthèse — analyste senior

L'analyste senior :

- Applique au minimum 2-3 SATs par enquête importante.
- Documente les SATs utilisées dans la méthodologie du rapport.
- Capitalise les leçons (« cette SAT a révélé tel biais »).
- Forme son équipe à ces méthodes.

> **Principe.** Les SATs ne sont pas des décorations méthodologiques. Elles transforment l'analyse subjective en analyse défendable. Une enquête sans SATs structurées est une enquête fragile face à contestation.

-----
