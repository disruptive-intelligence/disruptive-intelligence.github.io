---
title: Annexes
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - index.md
---

- Annexe A — Glossaire OSINT 2026 (80-120 termes)
- Annexe B — Dorks et opérateurs multi-moteurs
- Annexe C — Atlas des plateformes, registres et sources par pays
- Annexe D — Cheat sheets sélecteur → outils
- Annexe E — Catalogue d'outils par usage
- Annexe F — Checklist OPSEC
- Annexe G — Modèle de journal d'investigation
- Annexe H — Templates de fiches
- Annexe I — Matrice piste / indice / fait / preuve
- Annexe J — Cotation Admiralty + WEP
- Annexe K — Workflow OSINT en 10 étapes
- Annexe L — Modèles de livrables
- Annexe M — Templates de graphes et timelines
- Annexe N — Catalogue IA / agentic OSINT
- Annexe O — Mapping de la bibliothèque

-----


## Avant-propos


### Ce qu'est ce cours

**OSINT Mastery 2026** est le cours-mère de la bibliothèque. Il est conçu pour être **autonome** : un lecteur qui le travaille intégralement dispose des bases nécessaires pour conduire une investigation OSINT professionnelle de bout en bout, qu'il soit analyste CTI, investigateur financier, journaliste, magistrat, officier de renseignement, responsable conformité, consultant en due diligence, chercheur en sciences sociales ou citoyen formé.

Le cours adopte une posture **professionnelle, méthodologique et défensive**. Il enseigne comment investiguer rigoureusement à partir de sources ouvertes ; il n'enseigne ni à commettre une infraction, ni à échapper à la traçabilité, ni à contourner des protections légitimes. Cette posture est constante : chaque fois qu'une typologie criminelle ou un usage adverse de l'OSINT est exposé, c'est sous l'angle de la compréhension, de la détection et de la défense.

L'OSINT en 2026 n'est plus la même discipline qu'en 2020. Trois ruptures majeures ont reconfiguré le métier : (1) la **professionnalisation institutionnelle** — l'IC OSINT Strategy 2024-2026 de l'ODNI américaine formalise l'OSINT comme INT à part entière, la France crée le **Bataillon de Réserve en Renseignement Spécialisé (B2RS)** et le **service VIGINUM**, l'OTAN intègre l'OSINT à sa doctrine ; (2) l'**irruption de l'intelligence artificielle** — LLMs comme assistants, agents autonomes, deepfakes industriels, géolocalisation multi-agent ; (3) la **fermeture progressive des plateformes** — X payant, API LinkedIn restreinte, Meta verrouillée, Reddit fermé, Google dégradé. Le cours intègre ces ruptures comme structurantes, pas comme annexes.


### Public cible et prérequis

Ce cours s'adresse à des adultes professionnels ou en formation professionnalisante. Il suppose une **aisance numérique correcte** (navigation web, utilisation d'un terminal, compréhension générale du fonctionnement d'Internet, gestion de fichiers), mais ne suppose aucun bagage préalable en renseignement, en cybersécurité ou en droit. Les prérequis spécifiques (notions de réseau, bases Python, droit du numérique) sont introduits dans le cours quand nécessaire.

Le cours s'adresse également à des **citoyens formés** qui souhaitent comprendre la discipline pour mieux résister à la désinformation, vérifier l'information qu'ils consomment, ou s'engager dans une démarche d'enquête citoyenne encadrée (à l'image des contributeurs Bellingcat ou des participants Trace Labs).


### Ce que ce cours fait

- Il enseigne la **doctrine** : qu'est-ce que l'OSINT, comment elle s'inscrit dans le cycle du renseignement, quelles sont ses disciplines connexes, quelle est sa place en 2026.
- Il enseigne le **cadre légal et éthique** : RGPD, AI Act, DSA, CSDDD, sanctions, Failure to Prevent Fraud, jurisprudences, déontologie professionnelle.
- Il enseigne la **méthodologie** : cadrage, plan de collecte, sélecteurs, pivots, journal, chaîne de custody, structuration, vérification, ACH, cotation, formulation.
- Il enseigne la **technique** : moteurs, dorks, SOCMINT par plateforme, IMINT, GEOINT, infrastructure web, breaches, leaks, dark web (en vue maître).
- Il enseigne la **vérification** dans un monde post-deepfakes : C2PA, SynthID, signaux visuels, méthodologie intégrée, admissibilité judiciaire.
- Il enseigne l'**IA et l'automatisation** : LLMs comme assistants, prompting, hallucinations, agents autonomes, knowledge graphs locaux, pipelines Python.
- Il enseigne la **production** : note courte, rapport complet, fiche entité, rapport judiciaire, TLP, diffusion, veille.
- Il fournit un **fil rouge complet** (Opération MIRAGE 2026) traversant tous les chapitres jusqu'au cas de synthèse.
- Il fournit **17 cas pratiques** et un exercice final non guidé avec son corrigé.


### Ce que ce cours ne fait pas

- Il ne se substitue pas aux cours spécialisés de la bibliothèque pour les domaines suivants :
  - L'enquête crypto on-chain approfondie (clustering, attribution, mixers, bridges, cashout) — renvoi systématique à **OSINT Crypto vFULL**.
  - L'investigation financière approfondie (UBO complexes, schémas de blanchiment, AML/CFT, comptabilité forensique) — renvoi systématique à **FININT Investigation Financière vFULL**.
  - L'enquête dark web approfondie (Tor en profondeur, marketplaces, leak sites, IA criminelle, écosystèmes) — renvoi systématique à **Dark Web vFULL**.
  - La Cyber Threat Intelligence approfondie (acteurs, TTP, intrusion analysis, attribution étatique) — renvoi vers le cours CTI dédié.
- Il ne fournit pas de tutoriel exhaustif pour chaque outil cité : les outils changent tous les six mois, la méthodologie reste. Les outils sont présentés comme exemples opérationnels à date 2026.
- Il n'est pas un précis de droit ni un manuel de procédure pénale : il pose le cadre, il ne tient pas lieu de conseil juridique.
- Il ne forme pas à l'utilisation offensive de l'OSINT, à l'usurpation d'identité agressive, au harcèlement, au doxxing, ou à toute pratique non conforme au droit et à l'éthique professionnelle.


### Posture éthique constante

L'OSINT touche à la vie privée, à la réputation, à la liberté de circulation, parfois à la liberté physique de personnes — y compris de personnes innocentes ou non concernées. Une note d'analyse mal calibrée, un soupçon pris pour une preuve, une diffusion non maîtrisée, une confusion entre renseignement et accusation peuvent causer des dommages réels. La rigueur méthodologique n'est pas un luxe académique : elle est la condition même de la légitimité de la discipline. Tout au long du cours, cette rigueur est présentée comme un réflexe quotidien, pas comme un appendice de fin de chapitre.


### Place de l'IA dans l'OSINT moderne

L'IA est un **accélérateur, pas un substitut**. Elle excelle là où l'humain est inefficace (volume, traduction, extraction d'entités, monitoring continu, première classification) ; elle reste défaillante là où l'humain est irremplaçable (jugement contextuel, vérification, formulation calibrée, décision éthique). Le cours adopte une position **augmentée mais souveraine** : l'IA assiste l'analyste, l'analyste reste responsable. Le protocole **Retrieve-Store-Cite** (Ch.63) opérationnalise ce principe : aucune affirmation produite par IA n'entre dans un livrable sans source vérifiable et tracée.


### Articulation avec la bibliothèque

Le tableau suivant cartographie les renvois entre OSINT Mastery et les cours spécialisés.

| Domaine | Couverture dans OSINT Mastery | Cours spécialisé pour approfondir |
|---|---|---|
| Crypto / blockchain | Vue maître (Ch.72) | OSINT Crypto vFULL |
| Investigation financière | Vue maître (Ch.70-71, 77) | FININT Investigation Financière vFULL |
| Dark web / DARKINT | Vue opérationnelle (Ch.44) | Dark Web vFULL |
| Cyber Threat Intelligence | Chapitre dédié (Ch.74-75) | Cours CTI dédié |
| Intelligence économique / due diligence | Chapitres dédiés (Ch.36-38, 77) | Cours IE / Due Diligence |
| Forensic numérique | Méthodologie + chaîne de custody (Ch.15-16) | Cours Forensic dédié |

L'annexe O fournit la cartographie complète.


### Importance de la preuve, de la traçabilité et de l'incertitude

Trois principes traversent tout le cours.

**La preuve OSINT est toujours faillible.** Une capture peut être falsifiée, un registre peut être erroné, un compte peut être usurpé, un contenu peut être généré par IA. L'analyste OSINT ne produit pas de preuve absolue : il produit du renseignement coté, avec un niveau de confiance explicite et des limites documentées. Le vocabulaire calibré (Ch.86) protège contre la tentation du verdict.

**La traçabilité conditionne la valeur du renseignement.** Une affirmation sans source citée est du bruit. Une source non horodatée et non préservée est une affirmation faible. Le journal d'enquête (Ch.15) et la chaîne de conservation numérique (Ch.16) ne sont pas des formalités : ils sont la colonne vertébrale du métier.

**L'incertitude est constitutive du métier, pas un échec.** Le travail de l'analyste n'est pas de produire des certitudes, mais d'éclairer une décision sous incertitude. La cotation (Ch.84-85), l'ACH (Ch.79), la formulation analytique (Ch.86) sont les outils qui permettent de dire ce qu'on sait, ce qu'on ne sait pas, et ce qu'on suppose, sans confondre les trois.

-----


## Mode d'emploi du cours


### Comment lire ce cours

Le cours est **dense**. Il peut se lire de plusieurs manières.

**Lecture linéaire intégrale.** C'est le parcours recommandé pour une formation initiale ou une montée en compétence complète. Comptez entre 80 et 120 heures de lecture active selon votre rythme et votre niveau d'entrée. Le fil rouge MIRAGE est conçu pour être suivi dans cet ordre.

**Lecture par parcours thématique.** Si vous avez un objectif spécialisé (CTI, due diligence, GEOINT, IA, rapport judiciaire), suivez l'un des sept parcours proposés ci-dessous. Chaque parcours est conçu pour être autosuffisant sur son périmètre.

**Lecture par référence.** Chaque chapitre est conçu pour être autonome dans la mesure du possible. La table des matières et le glossaire (Annexe A) permettent un usage à la demande.

**Préparation d'enquête.** Avant de lancer une investigation réelle, le Parcours express (60 minutes) et les annexes opérationnelles (D, E, F, G, H, J, K, L) sont des compagnons de bureau.
