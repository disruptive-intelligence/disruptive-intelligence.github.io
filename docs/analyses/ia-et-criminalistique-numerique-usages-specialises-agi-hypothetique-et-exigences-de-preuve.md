---
title: "Analyse — IA et digital forensics : usages spécialisés, AGI hypothétique et exigences de preuve"
date: 2026-10-11
kind: analysis
theme: "ia"
slug: "ia-et-criminalistique-numerique-usages-specialises-agi-hypothetique-et-exigences-de-preuve"
author: "Eyric Phillyp Williams"
organization: "Middle Georgia State University"
source_file: "inbox/2026_Williams_0914103857.pdf"
source_url: "https://comp.mga.edu/static/media/doctoralpapers/2026_Williams_0914103857.pdf"
rubriques:
  - "ia-risques-surete"
  - "justice-enquete"
tags:
  - "digital forensics"
  - "intelligence artificielle"
  - "preuve numérique"
---

# Analyse — IA et digital forensics : usages spécialisés, AGI hypothétique et exigences de preuve

## Métadonnées

- **Titre original :** *Artificial Intelligence in Digital Forensics: A Thematic Review of Opportunities and Challenges*.
- **Auteur :** Eyric Phillyp Williams.
- **Date :** 2026, sans jour ni mois de publication indiqués dans le texte. Les métadonnées du PDF donnent une création le 14 septembre 2026, ce qui ne suffit pas à établir la date de diffusion.
- **Affiliation et nature :** travail de recherche soumis à la School of Computing de Middle Georgia State University dans le cadre d'un doctorat en technologies de l'information ; la page de titre ne mentionne ni revue ni évaluation par les pairs.
- **Source originale :** `inbox/2026_Williams_0914103857.pdf` (15 pages PDF, dont trois pages de références ; pagination interne de 1 à 14 après la couverture). [Version publique du document](https://comp.mga.edu/static/media/doctoralpapers/2026_Williams_0914103857.pdf), communiquée par l'utilisateur ; aucune URL publique n'est imprimée dans le PDF.
- **Périmètre :** revue narrative et analyse thématique d'études publiées entre 2015 et 2025 sur l'IA appliquée aux enquêtes et au digital forensics, surtout dans les services d'enquête.

## Repères pour comprendre le document

Une enquête numérique ne se résume pas à trouver un fichier intéressant : il faut acquérir et préserver les données, expliquer les choix de tri, relier les traces à une hypothèse et permettre à un tiers de contrôler le raisonnement. Williams oppose les systèmes entraînés pour une tâche précise à une intelligence artificielle générale (AGI), envisagée comme capable de transférer son raisonnement entre tâches. **Cette opposition est le cadre choisi par l'auteur**, et non la preuve qu'une AGI opérationnelle a été évaluée en laboratoire. Les définitions ci-dessous sont des repères pédagogiques tirés du contexte de la source ; les termes « IA forte » et « IA faible » reprennent sa terminologie.

- **Digital forensics** — recherche, acquisition, préservation et analyse de traces provenant d'appareils ou de services numériques, en vue d'une enquête (p. 1-2).
- **Artefact numérique** — élément exploitable d'une source numérique, par exemple une métadonnée de fichier, un journal ou une trace produite par un appareil (p. 1-3).
- **Triage** — sélection initiale des données à examiner en priorité ; un classement utile ne constitue pas à lui seul une preuve interprétée et validée (p. 2, 7-10).
- **IA spécialisée ou « faible »** — système limité à des fonctions définies, comme classer des artefacts ou rapprocher des fichiers (p. 1, 3, 8-10).
- **AGI ou « IA forte »** — catégorie que Williams emploie pour des capacités générales de raisonnement et d'adaptation ; il précise qu'une AGI pleinement développée n'existe pas dans les environnements forensiques opérationnels étudiés (p. 1-2).
- **Jeu de données d'entraînement** — exemples utilisés pour construire un modèle ; leur pertinence et leurs biais conditionnent sa performance hors des cas déjà vus (p. 3, 8).
- **Explicabilité** — possibilité de fournir une explication intelligible d'un résultat automatisé et de ses limites, nécessaire à sa discussion contradictoire (p. 3-4, 8-10).
- **Validation** — évaluation documentée de ce qu'un outil fait effectivement, de ses erreurs et de ses conditions d'emploi ; la source insiste sur son importance sans fournir un protocole expérimental propre (p. 3-5, 10-11).
- **Reproductibilité** — possibilité de retracer et de contrôler une méthode et ses résultats ; dans le document, elle est liée à la documentation des données, outils et décisions (p. 2-4).
- **Admissibilité** — acceptation d'un élément de preuve ou d'un témoignage dans une procédure ; ses critères dépendent de la juridiction et ne se déduisent pas de la seule précision annoncée d'un modèle (p. 3-4, 10).

## Résumé exécutif

Williams examine pourquoi les outils d'**IA spécialisée** servent déjà au tri, à l'identification et à la classification de traces numériques, alors qu'une **AGI** capable d'un raisonnement général reste une perspective théorique pour les laboratoires d'enquête. Son apport est d'articuler quatre familles de questions : intégration et performance, entraînement, droit et éthique, puis contraintes de mise en œuvre (p. 2-10).

Le travail repose sur une revue narrative : l'auteur dit avoir cherché dans Google Scholar, GALILEO, ScienceDirect et IEEE Xplore, puis retenu **30 études** après un ensemble initial d'environ **28 000 résultats**. Il décrit un codage manuel et quatre thèmes, mais ne donne pas le flux chiffré de sélection entre ces deux nombres ni un tableau complet des 30 études. Il ne teste ni outil ni jeu de données forensique (p. 4-7, 9).

Sa conclusion est surtout une exigence de méthode : un gain de vitesse au tri n'établit ni l'exactitude d'une conclusion d'enquête ni son admissibilité. La qualité des données, l'explication des sorties, la validation, le contrôle humain, les compétences et la gouvernance pèsent sur l'usage réel. **La source ne mesure pas le gain de performance d'une AGI face à une IA spécialisée** ; elle souligne elle-même l'absence de déploiement forensique opérationnel d'AGI (p. 8-11).

Pour la veille, l'intérêt tient à cette séparation entre promesse technique et preuve utilisable. Le texte aide à formuler les questions qu'un service d'enquête devrait poser avant d'adopter une fonction automatisée, mais ses généralisations sur les gains de l'IA et l'état du terrain doivent être vérifiées par des évaluations indépendantes et situées.

## Thèse principale

La thèse de Williams est que le recours actuel à l'IA spécialisée et le faible rôle de l'AGI en digital forensics s'expliquent conjointement par la disponibilité de tâches et de données bien définies, et par des obstacles de validation, de transparence, de ressources et de responsabilité. Il s'agit d'une **synthèse interprétative de publications**, et non d'une comparaison expérimentale entre deux systèmes (p. 2, 4-5, 10-11).

L'auteur emploie parfois « AGI » pour évoquer des systèmes émergents présentant quelques traits de raisonnement général, tout en reconnaissant l'absence d'AGI pleinement opérationnelle dans le domaine (p. 1). Cette extension de vocabulaire rend la frontière avec les modèles polyvalents contemporains difficile à tester et impose de lire les capacités d'AGI mentionnées comme des hypothèses.

## Informations et arguments importants

### Un terrain d'enquête riche en traces, mais un résultat automatisé à contrôler

La multiplication des téléphones, objets connectés, systèmes embarqués et services sociaux augmente les formats et volumes de traces à examiner. L'exemple d'une montre Fitbit mobilisée dans l'affaire *State v. Dabate* illustre l'intérêt possible d'une chronologie issue d'un objet connecté ; il ne démontre pas à lui seul la fiabilité de tout outil d'IA. Williams cite aussi une estimation selon laquelle les traces numériques interviennent dans près de **90 %** des dossiers judiciaires, chiffre repris de Miller (2023) et non mesuré dans sa propre revue (p. 1-2).

Dans ce contexte, l'auteur attribue aux outils spécialisés des fonctions de tri précoce, d'identification d'artefacts et de classification qui peuvent réduire le travail manuel. Les résultats sont décrits qualitativement ; le document ne fournit pas de temps gagnés, de taux d'erreurs ou de comparaison homogène entre laboratoires (p. 2-3, 7-10).

### L'entraînement détermine la portée des usages

Le raisonnement distingue deux régimes : des modèles spécialisés entraînés sur des données circonscrites et une AGI supposée apprendre de façon plus générale. Les premiers peuvent bien fonctionner sur une tâche délimitée, mais risquent d'être moins fiables si les formats, populations ou conditions changent ; les seconds sont présentés comme potentiellement plus adaptables sans mesure forensique directe. Williams cite notamment l'analyse de métadonnées de smartphones par Serhal et Le-Khac et le rapprochement approximatif de fichiers par Uhlig et ses collègues (p. 3, 8-9).

La source lie qualité, taille et diversité des jeux d'entraînement à la précision et à la généralisation. **Cette relation reste ici issue de la littérature citée** : la revue ne réanalyse pas les jeux de données, ne publie pas de métriques comparables et ne teste pas les résultats des modèles retenus (p. 3, 5, 8).

### Du modèle au dossier judiciaire : documentation, contrôle et compétences

L'auteur insiste sur la possibilité de documenter les outils, données et méthodes, puis de soumettre les conclusions à l'examen humain. Il mobilise le cadre de validation RVEF de Stoykova et Franke et le cadre de reporting DERDS de Horsman. Ces cadres éclairent la traçabilité des décisions ; le document ne montre pas qu'ils suffiraient à valider une AGI dans une procédure pénale (p. 3-4, 10).

Les barrières matérielles et organisationnelles complètent la question juridique : charge de travail, pénurie de personnels formés, budgets et intégration dans les pratiques des services. Williams souligne que les petites unités ont moins de capacité pour expérimenter et contrôler des systèmes avancés. La revue ne quantifie toutefois pas la part respective de chaque obstacle (p. 4, 8-10).

### Méthode et quatre thèmes obtenus

La recherche couvre les publications de **2015 à 2025** et énonce critères d'inclusion, exclusion des travaux non évalués par les pairs et usage du guide CASP pour une appréciation qualitative. L'auteur indique un codage manuel, des notes réflexives et une sélection finale de **30 études**, parmi lesquelles **15** sont résumées dans le tableau 1. Les quatre thèmes finaux sont : (1) intégration et performance, (2) entraînement et développement, (3) questions éthiques et juridiques, (4) obstacles de mise en œuvre (p. 4-9). La figure 1 schématise les étapes, sans ajouter de décompte vérifiable à chaque filtre (p. 7).

## Points particulièrement intéressants pour la veille

Le document dessine moins une course à « l'IA générale » qu'un programme de contrôle des fonctions précises déjà accessibles.

- **Triage assisté.** La source situe l'usage le plus concret de l'IA au début de l'examen des traces (p. 7-10). *Inférence pour la veille :* suivre les évaluations par tâche et les erreurs de classement, plutôt que des promesses globales de rapidité.
- **Données et changement de contexte.** Williams relie la qualité des données d'entraînement à la performance (p. 3, 8). *Inférence pour la veille :* surveiller les essais sur nouveaux appareils, formats et populations, ainsi que la dégradation après mise à jour.
- **Explication et contestation.** La source associe résultats opaques et difficulté à justifier une conclusion au tribunal (p. 3-4, 8-10). *Inférence pour la veille :* documenter si un tiers peut reconstituer la chaîne allant de la trace brute à l'affirmation retenue.
- **Capacité des services.** Les compétences et les moyens des équipes sont décrits comme des freins au déploiement (p. 4, 8-9). *Inférence pour la veille :* intégrer coûts de validation, formation et audit dans toute annonce d'adoption.
- **AGI comme horizon spéculatif.** Williams ne rapporte aucun essai opérationnel d'AGI (p. 1, 10-11). *Inférence pour la veille :* distinguer toute annonce de laboratoire, démonstration sur données synthétiques et usage probatoire réel.

## Faits, opinions et interprétations

### Faits rapportés par la source

Williams décrit une recherche bibliographique dans quatre services, une fenêtre **2015-2025**, environ **28 000** résultats initiaux, **30** études retenues, un codage manuel et quatre thèmes (p. 4-9). Ce sont des éléments de méthode **déclarés par l'auteur** : la source ne fournit pas le corpus complet ni les données nécessaires pour reproduire la sélection. Le tableau 1 identifie 15 études et leurs approches (p. 9).

### Opinions ou positions de l'auteur

L'auteur juge l'IA spécialisée bien établie dans la pratique forensique et considère l'AGI prometteuse mais encore inadaptée aux contraintes de preuve, compte tenu de la validation, de l'explicabilité et de la gouvernance disponibles (p. 8-11). Il estime que des travaux supplémentaires doivent porter sur des cadres de validation, des modèles de supervision et la possibilité d'une évaluation indépendante (p. 11).

### Interprétations et inférences

La distinction utile est celle entre **automatiser une étape** et **étayer une conclusion** : un modèle peut ordonner les fichiers à examiner tout en laissant à l'enquêteur la responsabilité de vérifier, contextualiser et rapporter le résultat. C'est une inférence de cette analyse, cohérente avec les contraintes que relève Williams, et non un résultat expérimental supplémentaire. Sa catégorie « AGI » mêle par ailleurs un objectif général de recherche et des fonctions adaptatives encore mal délimitées ; cette ambiguïté gêne toute comparaison de performance.

## Limites et points à vérifier

1. **Sélection peu reproductible.** Le passage d'environ 28 000 résultats à 30 études n'est pas détaillé par base, dédoublonnage, filtre et exclusion. La liste complète et les décisions de sélection ne sont pas fournies (p. 5-7).
2. **Évaluation des études peu observable.** La source annonce l'emploi des critères CASP, mais ne présente ni grille remplie, ni notation par étude, ni analyse de sensibilité. Le tableau final ne couvre que 15 des 30 études retenues (p. 5, 9).
3. **Absence de comparaison empirique avec l'AGI.** L'auteur reconnaît qu'aucune AGI n'a été déployée dans les environnements examinés. Les avantages potentiels et les obstacles propres à une AGI ne sont donc pas mesurés face à des outils spécialisés (p. 4, 10-11).
4. **Gains de l'IA non chiffrés.** Les bénéfices de rapidité, de réduction de charge et parfois d'erreurs sont rapportés à partir d'autres publications, sans protocole commun, taux d'erreur ou métrique exploitable pour une décision d'achat (p. 1-4, 7-10).
5. **Périmètre juridique large.** La revue évoque admissibilité, responsabilité et confidentialité sans analyser systématiquement une juridiction, un type de preuve ou une règle de procédure. Les exigences concrètes restent à vérifier selon le lieu et l'usage (p. 3-5, 10-11).
6. **Statistique de prévalence indirecte.** Le « près de 90 % des affaires » est une estimation citée via Miller (2023), sans dénominateur ni méthode présentés ici. Elle ne doit pas devenir une mesure générale de la fréquence de preuves numériques dans toutes les juridictions (p. 1).
7. **Frontière conceptuelle fluctuante.** L'introduction élargit « AGI » à des systèmes ayant certains traits de raisonnement général, puis la conclusion parle d'absence d'AGI opérationnelle. Le critère d'appartenance à la catégorie reste insuffisamment défini pour tester la thèse (p. 1-2, 10-11).

## Sources et références mentionnées

La bibliographie (p. 12-14) associe travaux sur le tri et les outils forensiques (Jusas et al., Serhal et Le-Khac, Uhlig et al.), réflexions sur l'IA forte (Butz ; Fähndrich et al.), cadres de fiabilité et de reporting (Stoykova et Franke ; Horsman), explicabilité (Hall et al. ; NIST IR 8312) et contraintes des services d'enquête (Wilson-Kovacs et Wilcox ; Horsman et Dodd). Elle cite également l'affaire *State v. Dabate* et une enquête de Miller auprès de procureurs et enquêteurs. Les références servent à étayer une revue narrative ; leur présence ne signifie pas que leurs constats ont été reproduits expérimentalement par Williams.

## Cinq éléments essentiels à retenir

1. **L'IA spécialisée** soutient surtout le tri et la classification initiale des traces numériques.
2. **L'AGI forensique** est traitée comme une perspective théorique et non comme un système opérationnel évalué.
3. **La qualité des données, l'explicabilité et la validation** conditionnent la valeur d'un résultat automatisé pour l'enquête.
4. **Les moyens humains et institutionnels** comptent autant que les capacités techniques dans l'adoption d'un outil.
5. **La revue est exploratoire** : ses 30 études déclarées et ses quatre thèmes ne fournissent pas une mesure comparative de performance ni un protocole de sélection intégralement reproductible.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-10-11. Les éléments qui suivent proviennent de sources extérieures vérifiées et ne modifient pas le compte rendu du document dans les sections précédentes.

### Travaux de référence

- **IA forte et digital forensics.** [Fähndrich et al. — « Digital forensics and strong AI: A structured literature review »](https://www.xn--fhndrich-0za.de/res/faehndrich2023c.pdf), article accepté le 4 août 2023, pose déjà la question des propriétés d'une IA utilisable pour l'analyse de traces numériques, dont l'explicabilité et la robustesse. Il constitue un précédent proche de Williams. Sa démarche et son champ ne sont pas identiques, mais sa présence nuance toute affirmation d'absence de revue antérieure sur le rapprochement entre IA forte et digital forensics.
- **Explication des sorties.** [NIST — « Four Principles of Explainable Artificial Intelligence »](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence), 29 septembre 2021, distingue production d'une explication, intelligibilité pour le destinataire, fidélité au fonctionnement du système et connaissance de ses limites. Ces principes éclairent la notion d'« explicabilité » invoquée par Williams sans démontrer l'admissibilité d'un outil donné.

### Compléments sur le sujet

La revue laisse de côté la traduction opérationnelle des exigences qu'elle identifie : quels essais faire, sur quels cas et avec quel suivi après déploiement ? Quatre ressources donnent des prises plus concrètes.

- **Tester une fonction précise.** Le [programme CFTT du NIST](https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt), page mise à jour le 1er mai 2026, publie une méthode de test de logiciels forensiques à partir de spécifications, procédures, critères et jeux d'essai. Il illustre une validation attachée à une fonction et à des conditions de test, ce qui évite de transformer « IA » en garantie générale de fiabilité.
- **Évaluer le risque sur tout le cycle de vie.** Le [cadre AI RMF du NIST](https://www.nist.gov/itl/ai-risk-management-framework), publié le 26 janvier 2023, propose un cadre volontaire de gestion des risques des systèmes d'IA. Son intérêt pour un laboratoire est de relier performance, conditions d'usage et risques pour les personnes ; il ne remplace ni un essai local sur des traces représentatives ni les règles de preuve applicables.
- **Confronter les détecteurs à de nouveaux contenus.** Le [projet *Guardians of Forensic Evidence* du NIST](https://www.nist.gov/programs-projects/guardians-forensic-evidence), page mise à jour le 25 septembre 2026, prépare une évaluation des outils de détection de manipulations et d'images synthétiques. Il insiste sur les tâches forensiques explicites, les jeux d'essai réalistes, le contrôle par les examinateurs et la réévaluation après évolution des systèmes. Le projet est en cours : il ne vaut pas certification déjà acquise d'un détecteur.
- **Documenter des évaluations adaptées au contexte.** Le [projet initial NIST AI 200-2, « TEVV-Athlon Framework »](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems), annoncé le 7 août 2026, présente une méthode de test, évaluation, vérification et validation adaptée à divers systèmes, y compris multimodaux et agentiques. Son statut de **projet soumis à commentaires** empêche de le présenter comme une norme définitive ou comme une validation forensique déjà accomplie.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| L'AGI est surtout théorique dans les environnements forensiques étudiés (p. 1, 10-11). | **Nuancé** : la revue antérieure traite bien l'IA forte comme un programme de recherche ; l'absence mondiale de tout usage ne peut être prouvée par ces seules sources. | [Fähndrich et al., 2023](https://www.xn--fhndrich-0za.de/res/faehndrich2023c.pdf). |
| La validation d'outils forensiques est une exigence concrète (p. 3-4). | **Confirmé** : le NIST décrit des méthodes et jeux de test par fonction. | [NIST CFTT, mise à jour 2026](https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt). |
| Les traces numériques concernent près de 90 % des affaires (p. 1). | **Nuancé** : Miller reprend « environ 90 % » comme estimation d'une autre source ; son enquête de 50 procureurs et 51 enquêteurs ne mesure pas cette prévalence. | [Miller, 2023](https://doi.org/10.1016/j.fsisyn.2022.100296). |
| La revue a réduit environ 28 000 résultats à 30 études (p. 5). | **Non établi** indépendamment : le PDF ne fournit pas les décomptes intermédiaires ni la liste complète permettant de reproduire le filtrage. | Document analysé, p. 5-7 et tableau 1 p. 9. |

### Contrepoints et critiques

- **Une revue antérieure existe.** [Fähndrich et al., 2023](https://www.xn--fhndrich-0za.de/res/faehndrich2023c.pdf) examinent déjà les thèmes d'« IA forte » en digital forensics. Williams peut apporter un autre assemblage de questions — entraînement, droit et contraintes d'organisation — mais ne peut être lu comme ouvrant un sujet totalement vierge. Ce contrepoint porte sur le cadrage bibliographique, pas sur la valeur de ses quatre thèmes.
- **Explicabilité seule insuffisante.** Les [quatre principes du NIST, 2021](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence) rappellent qu'une explication doit aussi être fidèle et connaître les limites du système. Une justification convaincante en langage naturel ne prouve donc pas à elle seule que l'outil a produit un résultat exact ou qu'une conclusion résiste à la contradiction.

### Évolutions depuis la publication

La date exacte de diffusion du travail de Williams n'est pas établie ; la création du PDF est datée du 14 septembre 2026. Une évolution **postérieure à cette date de création** est la mise à jour, le 25 septembre 2026, de la présentation du [projet NIST *Guardians of Forensic Evidence*](https://www.nist.gov/programs-projects/guardians-forensic-evidence), qui précise son approche d'évaluation continue des détecteurs de contenus falsifiés. Le projet [NIST AI 200-2](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems), annoncé le 7 août 2026, est au contraire antérieur à la création du PDF et reste un texte initial. Ces développements concernent l'évaluation d'outils spécialisés et d'autres IA ; ils ne constituent pas une preuve d'adoption d'AGI dans les laboratoires forensiques.

### Cadre juridique et éthique

- **États-Unis, témoignage d'expert.** La [Federal Rule of Evidence 702, texte et amendement de 2023](https://www.govinfo.gov/content/pkg/USCODE-2023-title28/pdf/USCODE-2023-title28-app-federalru-dup2-rule702.pdf), encadre la recevabilité d'un témoignage d'expert devant les juridictions fédérales, notamment par l'examen des méthodes fiables et de leur application fiable aux faits. Elle ne déclare pas automatiquement recevable ou irrecevable tout résultat d'IA ; d'autres règles et les droits des États peuvent s'ajouter.
- **Union européenne, usages de police.** Le [règlement (UE) 2024/1689 dans sa version consolidée du 27 juillet 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727), annexe III, point 6(c), classe parmi les usages à haut risque certains systèmes destinés à évaluer la fiabilité des preuves au cours d'enquêtes ou de poursuites pénales. Son article 113, dans cette version, reporte au **2 décembre 2027** l'application des sections 1 à 3 du chapitre III pour ces systèmes relevant de l'annexe III. Cette qualification dépend de la finalité précise du système ; elle ne couvre pas indistinctement chaque outil de tri forensique.

### Pour aller plus loin

- [NIST — *Computer Forensics Tool Testing Program*](https://www.nist.gov/itl/csd/secure-systems-and-applications/computer-forensics-tool-testing-program-cftt), mise à jour le 1er mai 2026 : méthodes et résultats de test d'outils forensiques par fonction.
- [NIST — *AI Risk Management Framework*](https://www.nist.gov/itl/ai-risk-management-framework), 26 janvier 2023 : cadre volontaire de gestion des risques à adapter aux usages d'enquête.
- [NIST — *Four Principles of Explainable Artificial Intelligence*](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence), 29 septembre 2021 : repères pour distinguer une explication intelligible d'une explication fidèle.
- [NIST — *Guardians of Forensic Evidence*](https://www.nist.gov/programs-projects/guardians-forensic-evidence), mise à jour le 25 septembre 2026 : état d'un projet de validation des détecteurs de manipulations et de médias synthétiques.
