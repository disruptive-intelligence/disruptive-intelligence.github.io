---
title: Red teaming
source: Cyber/Red_Teaming.md
---

*Penser comme l'adversaire pour décider sous incertitude*

**Cours complet — 34 chapitres • 7 parties • 7 annexes**

*Pensée adversaire structurée • Techniques analytiques structurées • Exercices adversariaux • Stress-test décisionnel*

---

## Note d'architecture

Ce cours est construit autour d'une **logique en trois temps**, qui doit rester lisible de bout en bout :

1. **Penser comme l'adversaire** (Parties I-III) — développer la discipline intellectuelle : modéliser la menace, maîtriser les techniques analytiques structurées.
2. **Transformer cette pensée en exercices** (Partie IV) — wargame et tabletop comme deux modalités complémentaires d'un même champ : l'exercice adversarial structuré.
3. **Utiliser cette pensée et ces exercices pour tester l'organisation** (Partie V) — stress-test des plans et des stratégies existantes.

Les trois dernières parties (VI-VII) installent cette capacité dans la durée (programme, anti-patterns, culture) et la consolident par des cas complets.

**Ce cours n'est pas** un cours sur les cyber exercises au sens NIS 2/DORA, ni un cours de gestion de crise, ni un cours de CTI, ni un cours de GRC. Il emprunte à ces disciplines et s'articule avec elles (voir mapping en Annexe F), mais son centre de gravité est unique : **la pensée adversaire appliquée à la décision**.

---

## Table des matières

- [Fil rouge : Opération MIRRORGATE](#fil-rouge-operation-mirrorgate)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - [Ch.1 — Qu'est-ce que le red teaming analytique — et ce qu'il n'est pas](#chapitre-1-definition-et-frontieres)
  - [Ch.2 — Origines, évolution et positionnement dans l'écosystème](#chapitre-2-origines-et-positionnement)
  - [Ch.3 — Biais cognitifs et défaillances organisationnelles](#chapitre-3-biais-cognitifs-et-defaillances-organisationnelles)
  - [Ch.4 — Le red teamer analytique : posture, compétences et déontologie](#chapitre-4-le-red-teamer-analytique-posture-competences-et-deontologie)
- **PARTIE II — PENSER COMME L'ADVERSAIRE : MODÉLISATION DE LA MENACE (Ch.5-9)**
  - [Ch.5 — Profilage adversaire : construire un modèle mental de l'attaquant](#chapitre-5-profilage-adversaire)
  - [Ch.6 — Motivations, contraintes et rationalité de l'adversaire](#chapitre-6-motivations-contraintes-et-rationalite-de-ladversaire)
  - [Ch.7 — Cartographie de la surface d'attaque du point de vue adversaire](#chapitre-7-cartographie-de-la-surface-dattaque-du-point-de-vue-adversaire)
  - [Ch.8 — Modélisation de scénarios d'attaque plausibles](#chapitre-8-modelisation-de-scenarios-dattaque-plausibles)
  - [Ch.9 — L'adversaire adaptatif : anticipation des pivots et de l'évolution tactique](#chapitre-9-ladversaire-adaptatif)
- **PARTIE III — TECHNIQUES ANALYTIQUES STRUCTURÉES (Ch.10-15)**
  - [Ch.10 — Devil's Advocacy : l'art de la contradiction méthodique](#chapitre-10-devils-advocacy)
  - [Ch.11 — Team A / Team B : structurer le débat contradictoire](#chapitre-11-team-a-team-b)
  - [Ch.12 — Pre-mortem : autopsier l'échec avant qu'il ne survienne](#chapitre-12-pre-mortem)
  - [Ch.13 — Analysis of Competing Hypotheses (ACH) appliquée au red teaming](#chapitre-13-analysis-of-competing-hypotheses-ach)
  - [Ch.14 — What-If Analysis, indicateurs et signaux d'alerte précoce](#chapitre-14-what-if-analysis-indicateurs-et-signaux-dalerte-precoce)
  - [Ch.15 — Outside-In Thinking, Quadrant Crunching, Red Hat Analysis](#chapitre-15-autres-tas-outside-in-thinking-quadrant-crunching-red-hat-analysis)
- **PARTIE IV — CONCEVOIR ET CONDUIRE LES EXERCICES ADVERSARIAUX (Ch.16-22)**
  - [Ch.16 — Panorama des formats d'exercice adversarial : wargame, tabletop, hybride](#chapitre-16-panorama-des-formats-dexercice-adversarial)
  - [Ch.17 — Wargame : dynamique compétitive, tours et adaptation Red/Blue](#chapitre-17-wargame-dynamique-competitive-tours-et-adaptation-redblue)
  - [Ch.18 — Wargame : conception, scénarisation et conduite](#chapitre-18-wargame-conception-scenarisation-et-conduite)
  - [Ch.19 — Tabletop : discussion structurée, coordination et procédures](#chapitre-19-tabletop-discussion-structuree-coordination-et-procedures)
  - [Ch.20 — Tabletop : conception des injects et conduite](#chapitre-20-tabletop-conception-des-injects-et-conduite)
  - [Ch.21 — L'exercice hybride : combiner les deux modalités](#chapitre-21-lexercice-hybride)
  - [Ch.22 — Facilitation, observation et RETEX : la colonne vertébrale commune](#chapitre-22-facilitation-observation-et-retex-la-colonne-vertebrale-commune)
- **PARTIE V — STRESS-TESTER L'ORGANISATION (Ch.23-27)**
  - [Ch.23 — La logique du stress-test : démonter les hypothèses d'un plan](#chapitre-23-la-logique-du-stress-test)
  - [Ch.24 — Stress-test de la stratégie de cybersécurité](#chapitre-24-stress-test-de-la-strategie-de-cybersecurite)
  - [Ch.25 — Stress-test du plan de réponse à incident](#chapitre-25-stress-test-du-plan-de-reponse-a-incident)
  - [Ch.26 — Stress-test des plans de continuité et de reprise (PCA/PRA)](#chapitre-26-stress-test-des-plans-de-continuite-et-de-reprise-pcapra)
  - [Ch.27 — Stress-test de la communication de crise et du dispositif réglementaire](#chapitre-27-stress-test-de-la-communication-de-crise-et-du-dispositif-reglementaire)
- **PARTIE VI — PROGRAMME, ANTI-PATTERNS ET CULTURE (Ch.28-31)**
  - [Ch.28 — Construire un programme de red teaming analytique en entreprise](#chapitre-28-construire-un-programme-de-red-teaming-analytique-en-entreprise)
  - [Ch.29 — Anti-patterns : pourquoi les programmes de red teaming échouent](#chapitre-29-anti-patterns-pourquoi-les-programmes-de-red-teaming-echouent)
  - [Ch.30 — Métriques, évaluation et retour sur investissement](#chapitre-30-metriques-evaluation-et-retour-sur-investissement)
  - [Ch.31 — Cultiver la pensée adversaire au quotidien](#chapitre-31-cultiver-la-pensee-adversaire-au-quotidien)
- **PARTIE VII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.32-34)**
  - [Ch.32 — Cas complet : red teaming d'une stratégie de défense face à une campagne APT](#chapitre-32-cas-complet-red-teaming-dune-strategie-de-defense-face-a-une-campagne-apt)
  - [Ch.33 — Cas complet : wargame de crise ransomware avec cellule de crise exécutive](#chapitre-33-cas-complet-wargame-de-crise-ransomware-avec-cellule-de-crise-executive)
  - [Ch.34 — Cas complet : tabletop hybride multi-acteurs — attaque hybride sur infrastructure critique](#chapitre-34-cas-complet-tabletop-hybride-multi-acteurs-attaque-hybride-sur-infrastructure-critique)
- **ANNEXES**
  - [Annexe A — Glossaire du red teaming analytique](#annexe-a-glossaire-du-red-teaming-analytique)
  - [Annexe B — Catalogue des techniques analytiques structurées](#annexe-b--catalogue-tas)
  - [Annexe C — Templates d'exercices et fiches de facilitation](#annexe-c-templates-dexercices-et-fiches-de-facilitation)
  - [Annexe D — Banque de scénarios et d'injects](#annexe-d-banque-de-scenarios-et-dinjects)
  - [Annexe E — Outils et ressources de référence](#annexe-e-outils-et-ressources-de-reference)
  - [Annexe F — Mapping de la bibliothèque](#annexe-f-mapping-de-la-bibliotheque)
  - [Annexe G — Ressources, formations et communautés](#annexe-g-ressources-formations-et-communautes)

---

## Fil rouge : Opération MIRRORGATE

> **Contexte narratif — ce fil rouge traverse les 31 premiers chapitres du cours et se conclut au Ch.32.**
>
> **Commandant Diane Lefèvre**, 38 ans, ancienne officier de renseignement (DGSE — Direction du Renseignement Technique), puis consultante senior en CTI chez un MSSP français, est recrutée comme **Directrice du Red Teaming Analytique** chez **Hélio Group** — conglomérat industriel européen (énergie, transport, spatial), 22 000 collaborateurs, 18 pays, classé OIV en France et entité essentielle sous NIS 2, fournisseur critique de l'ESA et d'Euratom.
>
> Le contexte de sa prise de poste est tendu. Six mois plus tôt, Hélio Group a subi une intrusion APT sophistiquée (traitée par le CERT dans le cadre du cours IR de la bibliothèque). L'attaquant — un cluster attribué avec confiance modérée à un acteur étatique — a résidé 14 semaines dans le réseau IT, a pivoté vers l'environnement OT d'une centrale thermique, et n'a été détecté que par un signal faible remonté par un ISAC partenaire. L'éradication a coûté 8 mois-hommes, et le RETEX post-incident a été accablant : le plan de réponse à incident n'avait jamais été testé, la cellule de crise s'est improvisée, la communication réglementaire a été tardive et désordonnée, et le SOC n'avait pas détecté les signaux pourtant présents dans ses propres logs.
>
> Le COMEX mandate Diane avec un objectif clair : **« Plus jamais ça. On veut quelqu'un qui pense comme l'adversaire, qui teste nos plans avant que le réel ne les teste, et qui nous force à regarder ce qu'on ne veut pas voir. »**
>
> La mission se décompose en trois axes — qui structurent le cours : (1) construire la capacité de pensée adversaire structurée d'Hélio Group, (2) mettre cette pensée en exercices, (3) stress-tester l'ensemble du dispositif existant.
>
> L'opération **MIRRORGATE** est le nom de code du programme. Le « miroir » est la métaphore : Diane force l'organisation à se regarder dans le miroir — pas le miroir flatteur des audits de conformité, mais le miroir honnête de la simulation adversaire.

---

## PARTIE I — FONDATIONS (Ch.1-4)

*Qu'est-ce que le red teaming analytique, d'où vient-il, et qu'est-ce qui le distingue radicalement des disciplines voisines ?*

---

### Chapitre 1 — Définition et frontières

#### Synopsis

Définition opérationnelle : le red teaming analytique est la discipline structurée qui consiste à adopter la perspective de l'adversaire — ou du réel hostile — pour tester les hypothèses, les plans, les stratégies et les processus décisionnels d'une organisation. **Il ne touche pas aux systèmes, il touche aux raisonnements.**

Les trois fonctions : (1) challenge des hypothèses implicites, (2) anticipation des futurs possibles, (3) préparation des réponses dans un environnement où l'échec est sans conséquence.

**Le tableau comparatif des frontières** — section centrale du chapitre, qui ancre l'identité du cours :

| Discipline | Ce qu'elle teste | Ce qu'elle mobilise | Ce qu'elle livre | Ce qu'elle n'est PAS |
|-----------|------------------|---------------------|------------------|---------------------|
| **Red teaming analytique** | Hypothèses, raisonnements, décisions | Pensée structurée, TAS, profilage | Analyses, contre-arguments, angles morts identifiés | Un pentest, un exercice cosmétique, une revue de conformité |
| **Red teaming technique (pentest, adversary simulation)** | Défenses techniques | Outils offensifs, exploitation | Vulnérabilités techniques, chemins d'intrusion | Un test de décision, un test de gouvernance |
| **Wargame cyber** | Coordination et décisions sous pression adversaire | Blue/Red/White Team, tours, injects, adaptation | Rapport de simulation avec constats décisionnels | Un audit statique, un plan validé sur papier |
| **Tabletop exercise (TTX)** | Procédures, coordination, connaissance des playbooks | Discussion structurée, scénario scripté | Identification de gaps procéduraux et organisationnels | Une simulation à haute fidélité, un test technique |
| **Exercice de crise NIS 2 / DORA / TLPT** | Conformité à une obligation réglementaire | Cadre normatif, livrables exigés | Preuve d'exécution pour le régulateur | Une évaluation honnête de la posture réelle |
| **Audit / challenge stratégique** | Conformité à un référentiel ou une stratégie | Checklist, entretiens, revue documentaire | Rapport d'audit, écarts | Une mise à l'épreuve dynamique |
| **Gestion de crise / cellule de crise** | Réponse à un événement réel | Organisation dédiée, procédures activées | Décisions réelles, résolution de l'incident | Un exercice, un apprentissage structuré |

**Le point central** : le red teaming analytique peut emprunter au wargame, au tabletop, et au stress-test — mais il les soumet tous à une même exigence : **servir l'amélioration de la décision, pas la démonstration de la préparation**.

Pourquoi les organisations échouent sans cette discipline : biais de confirmation institutionnel, groupthink, illusion de préparation, surprise stratégique.

> **🪞 MIRRORGATE — Épisode 1 :** Diane lit les documents existants : stratégie cyber (75 slides, 2 ans, jamais révisée), plan IR (120 pages, conforme ISO 27035 sur le papier, jamais testé), rapport RETEX (14 recommandations, 3 implémentées). Diagnostic : Hélio Group a des plans. Ce qu'il n'a pas, c'est la moindre idée de si ces plans fonctionnent.

---

### Chapitre 2 — Origines et positionnement

#### Synopsis

L'histoire du red teaming comme discipline : Kriegsspiel prussiens (1811), Red Cell CIA (années 1960), Team B (1976), programmes DoD post-11 septembre. Le rôle de l'*advocatus diaboli* dans la tradition vaticane comme fonction institutionnalisée de contradiction.

L'adoption par la cybersécurité : le red teaming technique a précédé le red teaming analytique. Les limites du purement technique sont devenues évidentes — tester les défenses sans tester les décisions laisse des angles morts critiques. Le Millennium Challenge 2002 comme cas d'école (red teaming authentique vs. red teaming de façade, puisque les règles ont été changées quand le Red l'a emporté).

Publications fondatrices : *Red Team Handbook* (UFMCS Fort Leavenworth), *Red Team* de Micah Zenko, framework OTAN, adaptations cyber récentes (CBEST, TIBER-EU, DORA TLPT — qui combinent pentest et dimension analytique, mais restent largement techniques dans leur mise en œuvre).

Positionnement dans l'écosystème cyber : à l'intersection de la CTI (comprendre l'adversaire), de la gestion de crise (tester les réponses), de la stratégie (valider les choix), et de l'analyse de renseignement (rigueur méthodologique).

> **🪞 MIRRORGATE — Épisode 2 :** Le RSSI : « On fait un pentest annuel et un exercice NIS 2. C'est du red teaming, non ? » Diane : « Le pentest teste vos murs. L'exercice teste votre compliance. Aucun des deux ne teste vos décisions. »

---

### Chapitre 3 — Biais cognitifs et défaillances organisationnelles

#### Synopsis

Le chapitre central sur le « pourquoi » profond du red teaming analytique.

**Biais cognitifs critiques pour le décideur cyber :** confirmation, ancrage, illusion de contrôle, biais du survivant, normalisation de la déviance (Challenger, Columbia, et les logs SolarWinds ignorés pendant 14 mois), biais d'optimisme, biais de disponibilité (on se prépare au dernier incident, pas au prochain).

**Défaillances organisationnelles :** groupthink (Janis — Baie des Cochons, escalade au Vietnam), silos informationnels (le SOC sait ce que le RSSI ignore, que le DG n'apprendra jamais), effet HIPPO, culture du « oui » (personne ne contredit le plan du RSSI en réunion).

**Le paradoxe de la préparation :** les organisations les plus convaincues d'être préparées sont souvent les moins bien préparées — parce que leur confiance inhibe le questionnement.

Chaque biais illustré par un cas cyber réel : SolarWinds (normalisation de la déviance), Colonial Pipeline (illusion de contrôle — le plan ne couvrait pas l'arrêt volontaire par panique), Capital One (biais de confirmation — le WAF était supposé bloquer les SSRF).

> **🪞 MIRRORGATE — Épisode 3 :** Diane demande à 5 responsables clés le scénario de menace n°1 pour Hélio. 5 réponses différentes. Aucune ne correspond au scénario qui a effectivement touché l'entreprise.

---

### Chapitre 4 — Le red teamer analytique : posture, compétences et déontologie

#### Synopsis

Le profil : ni pentester, ni consultant GRC, ni analyste CTI — un métier distinct qui emprunte aux trois.

**Compétences :** pensée critique et logique argumentative, connaissance du paysage de la menace, facilitation, diplomatie et intelligence situationnelle, production écrite.

**Déontologie :** transparence sur les objectifs, confidentialité des résultats bruts, distinction « tester les plans » vs. « tester les personnes », gestion du stress (un exercice qui terrorise est un exercice raté).

**Première apparition du thème des anti-patterns :** le red teaming « de façade » est introduit ici comme une posture à éviter, et fera l'objet du Ch.29 dédié.

> **🪞 MIRRORGATE — Épisode 4 :** Diane recrute Thomas, ex-analyste CTI. « Notre job n'est pas d'avoir raison. Notre job est de forcer l'organisation à se poser les bonnes questions. Le jour où le RSSI nous remercie trop chaleureusement, c'est qu'on n'a pas assez poussé. »

---

## PARTIE II — PENSER COMME L'ADVERSAIRE : MODÉLISATION DE LA MENACE (Ch.5-9)

*Première couche du triptyque : comment construire un modèle mental crédible de l'adversaire. Cette partie est de la **modélisation**, pas de la conception d'exercice — elle prépare la matière première que les exercices et stress-tests utiliseront plus tard.*

---

### Chapitre 5 — Profilage adversaire

#### Synopsis

Modèle en 6 dimensions : identité/attribution, motivation, capacités, contraintes, historique, adaptabilité.

Sources : CTI (cours CTI Ch.3, Ch.13-19), RETEX des incidents passés, OSINT sur les acteurs, renseignement dark web, rapports sectoriels.

**Le piège de l'adversaire omniscient** : l'erreur la plus fréquente est de modéliser un attaquant sans contraintes. L'adversaire réel fait des erreurs, a des ressources limitées, fait des arbitrages. Le red teaming crédible modélise **les contraintes autant que les capacités**.

> **🪞 MIRRORGATE — Épisode 5 :** Premier profilage. Cluster attribué avec confiance modérée à un acteur étatique. Motivations (espionnage industriel), capacités (TTP sophistiquées, pas de zero-day observé), contraintes (OPSEC stricte, objectif de discrétion = acteur patient).

---

### Chapitre 6 — Motivations, contraintes et rationalité de l'adversaire

#### Synopsis

Le modèle RAG (Rational Actor + Goals) : l'adversaire est rationnel dans son propre cadre de référence, même quand ses actions semblent irrationnelles de notre point de vue.

Application aux quatre archétypes : acteur étatique (objectifs politiques, contraintes diplomatiques), groupe cybercriminel (objectifs financiers, rationalité économique), insider (objectifs personnels, rationalité émotionnelle), hacktiviste (objectifs idéologiques, rationalité de visibilité).

Le facteur **coût-bénéfice** : chaque action offensive a un coût (détection, consommation de capacités, temps, dépense d'une zero-day). Comprendre les arbitrages de l'adversaire permet d'anticiper ses choix.

Limites de l'analyse rationnelle : erreurs de l'adversaire, frictions organisationnelles internes (un APT n'est pas monolithique), décisions politiques qui contredisent la logique opérationnelle, « fog of war ».

> **🪞 MIRRORGATE — Épisode 6 :** « Si vous étiez le service de renseignement qui nous a ciblés, quel serait votre prochain mouvement ? » Personne dans la salle ne mentionne la possibilité que l'attaquant soit encore dans le réseau via un accès non détecté.

---

### Chapitre 7 — Cartographie de la surface d'attaque du point de vue adversaire

#### Synopsis

Regarder sa propre organisation avec les yeux de l'adversaire — pas la surface d'attaque technique (pentest), mais la **surface d'attaque stratégique**.

La matrice exposition × valeur × accessibilité. Les vecteurs non techniques : surface humaine (lien cours HUMINT & SE), surface informationnelle (lien cours OSINT), surface juridique/réglementaire (forcer une divulgation publique via RGPD, par exemple).

L'exercice **Crown Jewels Analysis** : identifier les 5-10 actifs que l'adversaire ciblerait en priorité, les chemins d'accès, les défenses à chaque étape.

> **🪞 MIRRORGATE — Épisode 7 :** Exercice Crown Jewels. Les actifs protégés par l'IT (AD, messagerie) ne correspondent pas aux actifs ciblés par l'adversaire (plans de propulsion, données de simulation, poste OT). « L'IT protège ce qui fait tourner l'IT. L'adversaire cible ce qui a de la valeur pour son commanditaire. »

---

### Chapitre 8 — Modélisation de scénarios d'attaque plausibles

#### Synopsis

**Point important** : ce chapitre est de la **modélisation analytique**, pas de la conception d'exercice. La conception d'exercice (mise en scène du scénario) est traitée en Partie IV. Ici, on produit la matière première : des scénarios cohérents, fondés, testables.

Structure d'un scénario en 7 éléments : acteur, objectif, vecteur d'accès, chemin d'attaque, actions sur objectif, chronologie, points de décision défenseur.

Calibrage de la plausibilité — scoring basé sur : précédent historique, capacité technique de l'adversaire, motivation, faisabilité dans le contexte spécifique.

Le **portfolio de scénarios** : une organisation ne teste pas un scénario unique mais un portfolio couvrant les menaces prioritaires, aligné sur le Cyber Threat Landscape sectoriel (lien cours Panorama).

Typiquement : un scénario APT/espionnage, un scénario ransomware, un scénario supply chain, un scénario insider, un scénario hybride (cyber + informationnel).

> **🪞 MIRRORGATE — Épisode 8 :** Premier portfolio de 5 scénarios pour Hélio Group. Le scénario n°1 (retour de l'APT par sous-traitant OT) provoque un débat. Le responsable achats affirme que les sous-traitants sont audités annuellement. Diane : « Audités sur quoi ? Par qui ? Avec quels critères cyber ? » Silence. Premier angle mort identifié.

---

### Chapitre 9 — L'adversaire adaptatif

#### Synopsis

L'adversaire n'est pas statique — il apprend, s'adapte, réagit aux défenses.

Le cycle OODA de l'adversaire (Observe-Orient-Decide-Act). Quand il est détecté ou bloqué, il recommence le cycle : observe la réaction du défenseur, réévalue, adapte.

Les patterns d'adaptation : pivot de vecteur (phishing bloqué → exploitation), pivot d'infrastructure (C2 saisi → C2 alternatif), pivot de cible (cible durcie → sous-traitant), escalade (détection → destruction pour effacer les traces), abandon/retour (éradiqué → revient 6 mois plus tard).

L'exercice **« Et alors ? » (So What?)** : pour chaque mesure défensive envisagée, itérer la question sur 3-5 tours. Révèle les hypothèses fragiles.

> **🪞 MIRRORGATE — Épisode 9 :** Atelier « Et alors ? » sur les mesures post-incident. Tour 1 : « On a patché Ivanti. » — « L'adversaire revient par un 0-day. » Tour 2 : « On monitore les équipements de bordure. » — « Il passe par un sous-traitant. » Tour 3 : « On impose des exigences cyber aux sous-traitants. » — « Il compromet le fournisseur du sous-traitant. » Diane conclut : « Chaque mesure réduit le risque. Aucune ne l'élimine. Le red teaming sert à identifier quels risques résiduels vous acceptez consciemment — et lesquels vous ignorez inconsciemment. »

---

## PARTIE III — TECHNIQUES ANALYTIQUES STRUCTURÉES (Ch.10-15)

*La colonne méthodologique du cours. Les TAS sont les outils qui transforment le doute intuitif en intelligence exploitable — applicables tant à la modélisation (Partie II) qu'aux exercices (Partie IV) et aux stress-tests (Partie V).*

---

### Chapitre 10 — Devil's Advocacy

#### Synopsis

La technique la plus ancienne et la plus fondamentale. Le Devil's Advocate n'exprime pas son opinion personnelle — il défend systématiquement la position contraire pour tester la solidité de l'hypothèse dominante.

Protocole en 5 étapes. Applications cyber : challenger la stratégie, les conclusions CTI, les décisions de crise. Règles de facilitation : mandaté (pas auto-proclamé), temporaire (pas un rôle permanent), dépersonnalisé (challenge l'argument, pas la personne). Pièges : DA de façade, complaisant, toxique.

> **🪞 MIRRORGATE — Épisode 10 :** Diane joue le DA au comité de revue stratégique. Le RSSI : « Priorité Zero Trust et SOC 24/7. » Diane : « Votre Zero Trust couvre l'IT. L'attaquant est passé par l'OT. Votre SOC analyse les logs Windows. L'attaquant a utilisé des protocoles ICS. En quoi cette roadmap empêche le scénario qui s'est déjà produit ? »

---

### Chapitre 11 — Team A / Team B

#### Synopsis

Protocole complet. Variantes : hypothèse imposée vs. libre. Applications : évaluation de la posture, attribution d'un incident, choix stratégique. Le cas historique Team B (1976) — succès (biais révélés), excès (sur-estimation idéologique), leçons.

> **🪞 MIRRORGATE — Épisode 11 :** Team A vs. Team B sur OTIS Maintenance. Team A (RSSI) : « Risque géré. » Team B (Thomas) : « VPN permanent, postes non monitorés, 3 techniciens avec droits AD excessifs. » Le DG : « Depuis quand a-t-on ces informations ? » — « Depuis toujours. Personne ne les avait rassemblées. »

---

### Chapitre 12 — Pre-mortem

#### Synopsis

Gary Klein, 1998. Se projeter dans un futur où le plan a échoué, et travailler à rebours. L'inverse du planning optimiste.

Protocole en 6 étapes. Pourquoi ça fonctionne : contourne la dynamique de groupe qui inhibe la critique, force la spécificité (pas « ça pourrait mal tourner » mais « ça a mal tourné parce que... »), produit directement des indicateurs d'alerte précoce.

Applications cyber : pre-mortem du plan IR, d'une migration cloud, d'un programme de sensibilisation.

> **🪞 MIRRORGATE — Épisode 12 :** Pre-mortem du PCA. Postulat : « Ransomware, 80 % du parc chiffré, sauvegardes incluses. 3 semaines plus tard, production pas reprise. Pourquoi ? » Les réponses convergent : sauvegardes jamais testées, PCA ne couvre pas la perte simultanée AD + messagerie, personne ne sait qui décide l'arrêt OT. Diane : « Tout ce que vous venez de dire était déjà vrai hier. Le pre-mortem vous a juste donné la permission de le formuler. »

---

### Chapitre 13 — Analysis of Competing Hypotheses (ACH)

#### Synopsis

ACH de Richards Heuer (CIA, 1999) — technique analytique la plus rigoureuse pour évaluer des hypothèses concurrentes.

**L'ACH retournée pour le red teaming** : au lieu de « quel acteur est responsable ? », la question devient « quel scénario est le plus probable ? » ou « quelle hypothèse de défense est la plus fragile ? ».

L'ACH comme outil de priorisation des exercices et stress-tests. L'ACH comme antidote au biais de confirmation. Limites : dépendance à la qualité des hypothèses, sous-évaluation des scénarios « impensables », difficulté avec les hypothèses combinées.

> **🪞 MIRRORGATE — Épisode 13 :** ACH sur le vecteur du prochain incident. 5 hypothèses. Après la matrice : H3 (compromission sous-traitant) est l'hypothèse la moins réfutable ET la moins couverte. C'est le scénario prioritaire.

---

### Chapitre 14 — What-If Analysis, indicateurs et signaux d'alerte précoce

#### Synopsis

Protocole What-If en contexte cyber. Les **I&W (Indicators and Warnings)** : concept issu du renseignement militaire adapté au cyber. Méthodologie de construction d'une matrice I&W.

Application : transformer la CTI passive (« voici les menaces ») en CTI proactive (« voici ce qu'il faut surveiller pour détecter les menaces avant qu'elles ne se matérialisent »).

> **🪞 MIRRORGATE — Épisode 14 :** Matrice I&W pour le scénario « compromission sous-traitant OT ». 5 indicateurs transmis au SOC : « Si vous voyez 3 sur 5, ça ne veut pas dire qu'on est attaqué — ça veut dire qu'il faut investiguer. »

---

### Chapitre 15 — Autres TAS : Outside-In Thinking, Quadrant Crunching, Red Hat Analysis

#### Synopsis

**Outside-In Thinking :** renverser la perspective depuis l'environnement externe. Quels facteurs externes (géopolitiques, technologiques, réglementaires) pourraient changer radicalement notre profil de menace ?

**Quadrant Crunching :** matrice 2×2 de scénarisation prospective. Identifier les deux incertitudes critiques, les croiser, explorer les 4 scénarios résultants.

**Red Hat Analysis :** empathie adversaire immersive. Le red teamer joue littéralement le rôle de l'adversaire avec ses données, contraintes, chaîne de commandement. Plus exigeant que le simple profilage.

Tableau comparatif complet des TAS : quand utiliser, participants, durée, livrables, limites.

> **🪞 MIRRORGATE — Épisode 15 :** Quadrant Crunching sur l'évolution à 18 mois. Incertitudes : escalade géopolitique × obtention du contrat ESA. Quatre scénarios. Celui « escalade + contrat » multiplie drastiquement le risque d'espionnage et de sabotage. Jamais envisagé formellement.

---

## PARTIE IV — CONCEVOIR ET CONDUIRE LES EXERCICES ADVERSARIAUX (Ch.16-22)

*Deuxième couche du triptyque : transformer la pensée adversaire en exercices. Cette partie traite du **comment exercer**. Elle ne couvre pas encore **quoi tester** — c'est l'objet de la Partie V.*

*Wargame et tabletop sont ici présentés comme deux **modalités complémentaires** d'un même champ : l'exercice adversarial structuré. Leurs promesses sont distinctes :*

- **Wargame** = dynamique compétitive, tours, logique d'adaptation Red/Blue, pression du temps
- **Tabletop** = discussion structurée, coordination, maîtrise des procédures et de la gouvernance

---

### Chapitre 16 — Panorama des formats d'exercice adversarial

#### Synopsis

**La promesse de ce chapitre** : donner au lecteur une carte claire des formats d'exercice adversarial et des critères pour choisir entre eux.

Les trois familles : wargame, tabletop, hybride. Pour chaque famille : ce qu'elle permet d'observer, ce qu'elle ne permet pas, durée typique, public, coûts de préparation, logistique.

**Tableau de choix — quel format pour quel objectif ?**

| Objectif | Format recommandé | Pourquoi |
|----------|-------------------|----------|
| Tester la prise de décision sous pression évolutive | Wargame | Dynamique compétitive, adaptation Red/Blue, tours successifs |
| Tester la connaissance et l'application des playbooks | Tabletop technique | Discussion structurée, vérification des procédures |
| Tester la gouvernance de crise et les décisions exécutives | Tabletop stratégique | Focus sur les décisions non techniques, accessible au COMEX |
| Tester la coordination technique/stratégique | Exercice hybride | Deux salles, canal contrôlé, révèle les frictions |
| Anticiper une campagne longue durée | Wargame géopolitique | Horizon 6-18 mois simulés, multi-couches |
| Tester la résilience supply chain | Wargame supply chain | Modélise l'opacité des tiers |
| Évaluer rapidement une hypothèse défensive | Devil's Advocacy / pre-mortem | TAS légère, 1-3h, pas d'infrastructure |

Les trois rôles fondamentaux communs à tous les formats : Blue, Red, White/Control.

**Relation avec les autres formats d'exercices** (compliance NIS 2, TLPT DORA, exercices sectoriels) : un exercice adversarial de qualité peut satisfaire la compliance — mais la compliance seule ne produit pas un exercice adversarial de qualité. Cette distinction est fondamentale.

> **🪞 MIRRORGATE — Épisode 16 :** Diane présente au COMEX. Le DG : « Ce n'est pas un war game style jeu vidéo ? » Diane : « Non. Le Pentagone fait ça depuis 200 ans. Vos concurrents commencent à le faire. Vous n'avez jamais testé vos décisions autrement que dans une diapo PowerPoint. »

---

### Chapitre 17 — Wargame : dynamique compétitive, tours et adaptation Red/Blue

#### Synopsis

**La promesse du wargame** : observer comment les décisions Blue évoluent face à un adversaire qui s'adapte en temps réel, tour après tour.

Ce qui est propre au wargame : la dynamique compétitive (Red ne joue pas un script mais adapte ses actions aux réponses Blue), la logique de tours (simulation du temps compressé, chaque tour = X heures ou X jours), l'observation des boucles de rétroaction (Blue fait → Red réagit → Blue adapte → Red pivote).

Formats : seminar wargame (discussion, 2-4h), matrix wargame (argumentation + arbitrage facilitateur, 4-8h), wargame avec règles formelles (résolution mécanique par dés pondérés ou tables, plus immersif).

Applications typiques du wargame : simulation d'incident majeur, anticipation de campagnes APT (wargame géopolitique), simulation d'attaque supply chain, exercice d'escalade de crise.

> **🪞 MIRRORGATE — Épisode 17 :** Diane explique à l'équipe la différence entre un wargame et un tabletop. « Dans un tabletop, Red est dans le scénario scripté — il fait ce qui est prévu. Dans un wargame, Red est dans la salle d'à côté, il réagit à vos décisions, il change de plan s'il est bloqué. Le wargame est un combat, le tabletop est une répétition. »

---

### Chapitre 18 — Wargame : conception, scénarisation et conduite

#### Synopsis

Méthodologie complète de conception.

**Phase 1 — Cadrage :** objectif, participants, format, durée. **Phase 2 — Scénarisation en couches :** couche de fond (contexte géopolitique et sectoriel), couche initiale (situation de départ), injects scriptés, branches conditionnelles (si Blue fait X, Red fait Y). **Phase 3 — Règles du jeu :** déroulement des tours, simulation du temps, évaluation des décisions, arbitrage des résultats. **Phase 4 — Logistique :** salle, supports, rôles, observateurs, enregistrement.

**Variantes thématiques traitées dans ce chapitre :**
- Wargame de crise cyber (incident majeur, 5 phases : alerte, confinement, escalade, éradication, recovery). Les dilemmes : payer/ne pas payer, communiquer/se taire, couper/maintenir l'OT, signaler/attendre.
- Wargame géopolitique (horizon long, multi-couches : géopolitique, informationnelle, cyber, organisationnelle).
- Wargame supply chain (spécificité : le Blue ne contrôle pas les défenses des tiers, doit décider avec une opacité réaliste).

Erreurs courantes : scénario trop complexe, trop facile, Red qui joue pour « gagner » au lieu de jouer avec réalisme, wargame sans objectif clair.

> **🪞 MIRRORGATE — Épisode 18 :** Premier wargame d'Hélio. Scénario ransomware avec exfiltration. Tour 3 : le RSSI veut confiner. Le directeur de production refuse — livraison ESA dans 5 jours. Le DG hésite. Personne ne sait qui a l'autorité de trancher. « Ce conflit d'autorité est exactement ce qu'on cherchait. »

---

### Chapitre 19 — Tabletop : discussion structurée, coordination et procédures

#### Synopsis

**La promesse du tabletop** : vérifier que les procédures existent, sont connues, et produisent une coordination fluide quand on les suit — dans un format de discussion structurée où personne n'exécute réellement d'action.

Ce qui est propre au tabletop : la discussion structurée (les participants parlent de ce qu'ils feraient, n'exécutent pas), le focus sur les processus et la coordination (pas sur la prise de décision adversaire dynamique), l'accessibilité (2-4h, 8-20 participants, pas d'infrastructure technique).

**Ce que le tabletop teste :** connaissance des processus, coordination entre les rôles, qualité de la prise de décision sur scénario scripté, identification des angles morts procéduraux.

**Ce que le tabletop ne teste PAS :** compétences techniques individuelles, performance sous stress extrême (le stress d'un tabletop n'est pas celui d'un incident réel), capacité réelle à exécuter (dire « je confine le serveur » dans un tabletop ne prouve pas qu'on sait le faire techniquement), adaptation adversaire (le Red ne s'adapte pas dans un tabletop — il déroule le scénario).

Les trois niveaux : technique (SOC/CERT/IT), stratégique (COMEX/juridique/communication), hybride (couvert au Ch.21).

> **🪞 MIRRORGATE — Épisode 19 :** Diane analyse les « exercices » passés d'Hélio — en réalité des présentations PowerPoint. « Ce n'était pas un tabletop. C'était une réunion d'information. Un tabletop fait mal : les participants doivent prendre des décisions, affronter des dilemmes, réaliser qu'ils ne savent pas quelque chose qu'ils auraient dû savoir. »

---

### Chapitre 20 — Tabletop : conception des injects et conduite

#### Synopsis

Les injects sont le carburant du tabletop.

**Principes de conception :** réalisme (fondé sur des TTP documentées), escalade progressive, dilemmes intégrés (pas de réponse évidente), multi-dimensionnalité (techniques, opérationnels, communicationnels, réglementaires, humains, adversaires).

**Timing des injects :** trop vite → submergement ; trop lent → enlisement. Le facilitateur adapte en temps réel.

**Tabletop technique** : tester les playbooks IR, la chaîne détection → qualification → escalade, la coordination SOC/CERT, les décisions de confinement, la collecte de preuves, l'utilisation des outils.

**Tabletop stratégique** : tester l'activation de la cellule de crise, les processus de décision exécutive, la communication de crise, les obligations réglementaires (ANSSI, CNIL, NIS 2, DORA), la coordination avec les parties prenantes externes. Les dilemmes classiques : payer/ne pas payer, communiquer/se taire, arrêter/continuer, signaler/attendre.

Banque d'injects réutilisables (voir Annexe D).

> **🪞 MIRRORGATE — Épisode 20 :** Inject conçu par Diane : « Un journaliste de La Tribune appelle en affirmant avoir reçu des documents internes d'Hélio d'un groupe ransomware, dont un rapport d'audit nucléaire classifié. Article prévu demain matin. Que faites-vous ? » Cet inject teste simultanément communication de crise, coordination technique-juridique, et pression temporelle.

---

### Chapitre 21 — L'exercice hybride

#### Synopsis

Le format le plus réaliste et le plus complexe : un exercice qui combine la dynamique compétitive du wargame (adaptation Red/Blue) et la discussion structurée du tabletop multi-niveaux (technique + stratégique simultanément).

Mécanique : deux salles (technique et stratégique), deux facilitateurs synchronisés, un canal de communication contrôlé. Le groupe technique reçoit les injects opérationnels, le groupe stratégique reçoit les injects décisionnels. Les deux doivent communiquer — et c'est cette communication que l'exercice teste.

Ce que l'hybride révèle : perte d'information technique → stratégique, traduction technique → décisionnel, décisions nécessitant coordination des deux niveaux, frictions de tempo (le technique trop lent pour le stratégique, ou inversement).

> **🪞 MIRRORGATE — Épisode 21 :** Tabletop hybride. Salle A : SOC+CERT+IT. Salle B : COMEX+juridique+communication. Canal unique : talkie-walkie simulant des appels. Tour 4 : le CERT découvre des données de santé exfiltrées. Le RSSI ne transmet pas l'information au COMEX pendant 45 minutes. Quand le DPO l'apprend enfin, le compteur CNIL a déjà commencé. « Dans un incident réel, le DPO l'aurait appris par un article de presse. »

---

### Chapitre 22 — Facilitation, observation et RETEX : la colonne vertébrale commune

#### Synopsis

**Le rôle le plus critique et le plus sous-estimé** : le facilitateur (White Team lead). Un exercice mal facilité est une perte de temps — un exercice bien facilité produit des insights que des mois d'audit ne révèleraient pas.

Compétences : maîtrise du scénario, lecture de la salle, neutralité, gestion du temps.

**Protocole d'observation :** décisions prises (et celles évitées), processus utilisés (ou improvisés), informations demandées (et celles oubliées), conflits de rôle, hypothèses non vérifiées, silences révélateurs.

**Le RETEX en deux temps :**
- **Hot wash** (à chaud, 30-60 min) : émotions encore vives, impressions brutes, premiers constats.
- **Cold wash** (structuré, quelques jours après) : analyse consolidée avec les observations documentées.

**Le livrable final :** rapport calibré selon l'audience — synthèse COMEX (2 pages) et détail opérationnel RSSI. Matrice de suivi des recommandations avec responsable et échéance.

**Ce chapitre s'applique à tous les formats** (wargame, tabletop, hybride) — c'est la colonne vertébrale commune de la partie IV.

> **🪞 MIRRORGATE — Épisode 22 :** Diane rédige le rapport du premier cycle d'exercices. Constatations : aucun processus d'escalade SOC→COMEX, conflit d'autorité RSSI/production, notification ANSSI non maîtrisée, communication de crise inexistante. Le RSSI : « C'est brutal. Mais si on avait vécu ça en vrai, ça aurait été pire. »

---

## PARTIE V — STRESS-TESTER L'ORGANISATION (Ch.23-27)

*Troisième couche du triptyque : quoi tester. La Partie IV traitait du **comment exercer**. Cette partie traite des **objets du test** : les plans et stratégies existantes, démontés hypothèse par hypothèse.*

*La promesse du stress-test est distincte de celle de l'exercice : **démonter les hypothèses implicites d'un plan ou d'une stratégie, pour en révéler les fragilités avant qu'un incident réel ne les révèle.***

---

### Chapitre 23 — La logique du stress-test

#### Synopsis

Distinction fondamentale avec l'exercice :

- **L'exercice** (Partie IV) met en scène un scénario et observe comment l'organisation réagit.
- **Le stress-test** prend un plan ou une stratégie existante, identifie ses hypothèses implicites, et les soumet au démontage systématique par les TAS de la Partie III.

Les deux sont complémentaires : un stress-test peut précéder un exercice (« quelles hypothèses de ce plan sont les plus fragiles ? → on va tester celles-là ») ou lui succéder (« l'exercice a révélé que X ne fonctionnait pas → stress-test systématique de X »).

**Méthodologie générale du stress-test :**
1. Identifier l'objet à stress-tester (document : stratégie, plan IR, PCA, plan de com)
2. Déconstruire en hypothèses explicites et implicites
3. Pour chaque hypothèse, appliquer les TAS pertinentes : Devil's Advocacy, pre-mortem, What-If, ACH
4. Classer les hypothèses par solidité : vérifiées, plausibles non vérifiées, fragiles
5. Produire un rapport de stress-test avec recommandations

**L'écueil à éviter :** le stress-test qui se contente de lister des risques génériques sans les ancrer dans des hypothèses spécifiques du document analysé. Un stress-test qui pourrait s'appliquer à n'importe quelle organisation est un stress-test qui ne sert à rien.

> **🪞 MIRRORGATE — Épisode 23 :** Diane explique le protocole à Thomas. « On prend le plan IR. On sort un stylo rouge. On ne cherche pas ce qui nous plaît. On cherche chaque phrase qui commence par un 'en cas de' ou un 'si', et on se demande : cette hypothèse est-elle vraie ? Si elle est fausse, qu'est-ce qui casse ? »

---

### Chapitre 24 — Stress-test de la stratégie de cybersécurité

#### Synopsis

Application du protocole à la stratégie cyber.

**Hypothèses stratégiques les plus fréquemment fragiles :** « notre périmètre est défini et contrôlé » (shadow IT, IoT, OT non inventorié), « nos sous-traitants appliquent nos exigences » (pas de vérification réelle), « notre plan IR fonctionne » (jamais testé), « notre sensibilisation est efficace » (mesurée en taux de complétion de e-learning, pas en résistance réelle au phishing ciblé).

Livrable type : rapport de stress-test stratégique avec hypothèses vérifiées / plausibles / fragiles, et recommandations priorisées.

> **🪞 MIRRORGATE — Épisode 24 :** Stress-test de la stratégie 2025-2027 d'Hélio. 14 hypothèses implicites identifiées. 4 solides, 6 plausibles, 4 fragiles. La plus fragile : « notre architecture réseau empêche le pivot IT → OT ». Diane découvre 3 points de passage non documentés — dont un poste à double connexion, exactement le vecteur utilisé lors de l'incident passé. Non éliminé pendant la remédiation.

---

### Chapitre 25 — Stress-test du plan de réponse à incident

#### Synopsis

Application du protocole au plan IR (lien cours IR).

Pour chaque phase (détection, qualification, confinement, éradication, recovery, communication, RETEX), trois questions :
1. **« Le plan suppose X — est-ce vérifié ? »** (ex : le plan suppose une détection SOC en moins de 24h — est-ce le cas pour les TTP de nos adversaires prioritaires ?)
2. **« Le plan prévoit que Y fait Z — Y le sait-il ? A-t-il les moyens ? L'a-t-il déjà fait ? »**
3. **« Le plan fonctionne en conditions normales — fonctionne-t-il en conditions dégradées ? »** (ex : le plan fonctionne si l'AD est disponible — fonctionne-t-il si l'AD est compromis ?)

Défaillances les plus fréquemment révélées : plan non à jour, non connu (les personnes nommées ignorent leur rôle), non réaliste (délais incompatibles avec les capacités), non résilient (ne fonctionne pas si l'infrastructure de communication elle-même est compromise).

> **🪞 MIRRORGATE — Épisode 25 :** Diane interroge chaque personne nommée dans le plan IR. 3 sur 8 ne savent pas qu'elles y figurent. 2 ont changé de poste. Le numéro d'urgence du prestataire IR est un ancien numéro. Et le plan suppose que les communications de crise passent par l'email — premier service coupé en cas de ransomware.

---

### Chapitre 26 — Stress-test des plans de continuité et de reprise (PCA/PRA)

#### Synopsis

Spécificité du stress-test PCA/PRA dans un contexte cyber : ces plans sont souvent conçus pour des sinistres physiques (incendie, inondation) et ne couvrent pas les spécificités d'un incident cyber.

Hypothèses PCA/PRA à tester : sauvegardes intègres et restaurables (testé quand pour la dernière fois ?), site de repli opérationnel (avec quel délai, quelle capacité ?), processus métiers sans IT pendant X heures/jours (vérifié avec les métiers ?), reconstruction AD maîtrisée (avec quel processus, quels outils, quel personnel ?), reprise dans un environnement sain (comment s'assurer que l'attaquant n'est pas dans l'environnement restauré ?).

Le scénario **worst case réaliste** : ransomware + exfiltration + destruction des sauvegardes en ligne + compromission de l'AD + indisponibilité du prestataire habituel (mobilisé sur un autre incident).

> **🪞 MIRRORGATE — Épisode 26 :** « Combien de temps pour reconstruire l'AD de zéro ? » — « On n'a jamais fait l'exercice. Le PRA prévoit une restauration depuis la sauvegarde. » — « Et si la sauvegarde est chiffrée ? » Silence. « Vous avez un PRA qui fonctionne si les sauvegardes fonctionnent. Pas un PRA pour le cas où elles ne fonctionnent pas. »

---

### Chapitre 27 — Stress-test de la communication de crise et du dispositif réglementaire

#### Synopsis

Stress-test des dimensions souvent parents pauvres de la préparation — et pourtant les plus visibles (et les plus destructrices) en cas de défaillance.

**La communication de crise cyber :** parties prenantes (employés, clients, partenaires, régulateurs, médias, actionnaires), messages (que dit-on, que ne dit-on pas), timing (trop tôt = incomplet, trop tard = dissimulation), porte-parole (qui, avec quel mandat, avec quelle préparation).

**Les obligations réglementaires :** ANSSI (OIV, OSE, NIS 2), CNIL (RGPD — 72h), notification sectorielle (DORA pour la finance, réglementation nucléaire pour l'énergie), notification contractuelle (clients, partenaires). Stress-test : les responsables savent-ils quelles notifications sont obligatoires ? Connaissent-ils les délais ? Ont-ils les templates ? Les contacts ?

**Le scénario de stress communicationnel :** la fuite médiatique avant la communication officielle, l'instrumentalisation par l'adversaire (le groupe ransomware tweete, contacte les clients, publie sur le leak site), la crise réputationnelle qui survit à l'incident technique.

> **🪞 MIRRORGATE — Épisode 27 :** Stress-test du dispositif com. Aucun Q&A préparé pour scénario cyber, aucun porte-parole identifié, aucun template de communiqué, le responsable com « n'a jamais géré de crise cyber ». Diane : « Dans un incident réel, vous aurez 2 à 6 heures entre la fuite publique et le moment où vous devez parler. Si vous n'êtes pas prêts, ce sont les autres qui parleront de vous. »

---

## PARTIE VI — PROGRAMME, ANTI-PATTERNS ET CULTURE (Ch.28-31)

*Transformer le cours d'une suite d'outils en un programme structuré de capacité organisationnelle durable. Cette partie répond à la question : « Très bien, mais comment on installe ça dans la durée sans que ça dérive ? »*

---

### Chapitre 28 — Construire un programme de red teaming analytique en entreprise

#### Synopsis

Le passage de l'exercice ponctuel au programme structuré.

**Les composantes :** cadence d'exercices (cycle annuel type : 1 wargame stratégique, 2 tabletop hybrides, 4 tabletop techniques, sessions de Devil's Advocacy intégrées aux revues trimestrielles, stress-tests ponctuels sur les plans révisés), progression des scénarios (pas les mêmes chaque année), suivi des recommandations (chaque exercice en produit — un programme mature les implémente et vérifie), gouvernance (qui mandate, qui valide les scénarios, qui reçoit les résultats, à quel niveau).

**L'ancrage organisationnel :** connexions SOC, CTI, RSSI, COMEX, juridique, communication.

**Le budget et les ressources :** estimation réaliste (personnel interne, consultants externes, temps des participants, logistique). Argumentation du ROI.

**Commencer petit :** première année = 1 wargame ciblé + 2 tabletop + Devil's Advocacy sur une décision majeure. Ne pas essayer de tout faire d'emblée.

> **🪞 MIRRORGATE — Épisode 28 :** Diane présente MIRRORGATE au COMEX. Cycle annuel défini. Budget : 280K€/an (dont 180K€ de temps interne). Le DAF : « Comment mesure-t-on le retour ? » Diane : « Le dernier incident a coûté 12M€. Toutes les défaillances révélées par le wargame étaient déjà présentes lors de l'incident. »

---

### Chapitre 29 — Anti-patterns : pourquoi les programmes de red teaming échouent

#### Synopsis

**Chapitre dédié et dense.** Un programme de red teaming analytique qui ne produit pas de vérités inconfortables n'apporte rien. Or la tendance naturelle des organisations est de neutraliser l'inconfort. Ce chapitre identifie les dix anti-patterns les plus destructeurs, leurs symptômes, leurs causes profondes, et les contre-mesures.

**Anti-pattern 1 — L'exercice cosmétique.** Symptôme : le scénario est calibré pour que Blue « réussisse ». Les injects sont mous, les dilemmes absents, le Red joue sans conviction. Cause profonde : la peur du CEO d'être mis en difficulté publiquement, ou la culpabilité de « stresser les équipes ». Contre-mesure : mandat explicite d'inconfort dès la lettre de cadrage, validation du scénario par un tiers qui n'a pas intérêt au succès.

**Anti-pattern 2 — Le COMEX spectateur.** Symptôme : les dirigeants assistent mais ne participent pas. Ils écoutent les équipes opérationnelles simuler la crise, puis repartent en disant « impressionnant ». Cause profonde : les dirigeants considèrent que leur temps est trop précieux pour un exercice, ou craignent de montrer qu'ils ne savent pas quoi faire. Contre-mesure : tabletop stratégique dédié où le COMEX est la Blue Team et doit prendre les décisions qu'il aurait à prendre en vrai. Le SOC n'est pas dans la salle — seul le RSSI fait l'interface.

**Anti-pattern 3 — Le scénario trop simple.** Symptôme : tous les dilemmes ont une réponse évidente, tous les injects sont gérés sans friction, le débrief conclut que « l'organisation est prête ». Cause profonde : peur de l'humiliation, ou facilitateur qui cherche à plaire. Contre-mesure : chaque scénario doit contenir au minimum trois dilemmes sans bonne réponse évidente, et au moins un inject qui force un conflit entre objectifs légitimes (sécurité vs. continuité, transparence vs. confidentialité, rapidité vs. précision).

**Anti-pattern 4 — L'absence de suivi des recommandations.** Symptôme : chaque exercice produit un rapport, mais 18 mois plus tard, 90 % des recommandations ne sont pas implémentées. L'exercice suivant redécouvre les mêmes problèmes. Cause profonde : personne n'est propriétaire du suivi, ou le suivi n'est pas dans la gouvernance formelle. Contre-mesure : chaque recommandation a un propriétaire nommé, une échéance, et un statut revu trimestriellement devant le COMEX. Le taux d'implémentation est une métrique du programme.

**Anti-pattern 5 — La confusion entre animation et apprentissage.** Symptôme : l'exercice est bien animé, les participants sortent contents (« c'était intéressant »), mais rien n'est documenté de manière exploitable. Pas de rapport, pas de recommandations, pas de suivi. Cause profonde : le facilitateur est un bon animateur mais pas un analyste. Contre-mesure : séparer les rôles (facilitateur + observateur analyste dédié), et imposer un livrable écrit structuré dans les 5 jours ouvrés.

**Anti-pattern 6 — La culture punitive.** Symptôme : les erreurs révélées par l'exercice conduisent à des sanctions contre les personnes concernées. Conséquence : à l'exercice suivant, les participants se protègent — ils donnent les « bonnes réponses » qu'ils sont censés donner, pas leurs vraies réponses. L'exercice perd toute valeur. Cause profonde : confusion entre évaluation individuelle et évaluation du dispositif. Contre-mesure : règle explicite dès le cadrage — « les constatations de l'exercice concernent les processus et l'organisation, pas les personnes ». Les rapports ne nomment pas les individus.

**Anti-pattern 7 — La recherche du « show » plutôt que de la vérité utile.** Symptôme : l'exercice devient un événement médiatique interne — scénario spectaculaire, déploiement théâtral, communiqué post-exercice louant la performance. Cause profonde : l'exercice sert les ambitions politiques internes du RSSI ou du responsable du programme. Contre-mesure : séparer la fonction de communication interne (un sujet à part) et la fonction d'apprentissage (le cœur du programme). Les rapports d'exercice sont classifiés et diffusés restrictivement.

**Anti-pattern 8 — L'instrumentalisation politique.** Symptôme : le red teaming est utilisé pour pousser un agenda (justifier un investissement, discréditer un projet concurrent, évincer un responsable). Cause profonde : le red teaming est perçu comme un outil, pas comme une discipline. Contre-mesure : indépendance du red teamer vis-à-vis des lignes managériales impliquées, validation des scénarios par un comité multi-parties, rotation des facilitateurs.

**Anti-pattern 9 — La paralysie par l'analyse.** Symptôme inverse des précédents : le programme produit tellement de recommandations que plus rien n'est décidé ni implémenté. Chaque décision est bloquée par « on devrait d'abord faire un pre-mortem ». Cause profonde : le red teaming devient un outil de blocage plutôt que d'amélioration. Contre-mesure : calibrage de la profondeur analytique (un pre-mortem dure 2-3h, pas 3 semaines), règle de priorisation des recommandations (top 5 seulement), et acceptation explicite qu'une décision puisse être prise malgré des risques identifiés.

**Anti-pattern 10 — Le red teaming « deux jours par an ».** Symptôme : le red teaming est réduit à un événement annuel spectaculaire, sans continuité, sans ancrage dans les décisions quotidiennes. Cause profonde : vision événementielle plutôt que culturelle. Contre-mesure : micro-exercices réguliers (voir Ch.31), intégration des TAS dans les revues de décision, formation transversale.

**La boussole pour détecter la dérive :** trois questions simples à poser trimestriellement au programme.
1. Le dernier exercice a-t-il produit des résultats que le COMEX ne voulait pas entendre ? (Si non, il y a un problème.)
2. Combien de recommandations de l'exercice n-1 sont implémentées aujourd'hui ? (Si < 40 %, il y a un problème.)
3. Un observateur externe lisant nos rapports aurait-il une vision fidèle de nos vulnérabilités, ou une vision flatteuse ? (Si la seconde, il y a un problème.)

> **🪞 MIRRORGATE — Épisode 29 :** À 10 mois, Diane reçoit une alerte. Le RSSI lui demande « d'assouplir » le scénario du prochain tabletop stratégique parce que « le COMEX a eu des retours difficiles du dernier exercice ». Diane reconnaît l'anti-pattern n°1. Elle refuse, propose au DG un entretien direct sur la valeur comparée de l'inconfort en exercice vs. en incident réel. Le DG maintient le mandat initial. Le programme survit à sa première tentative de neutralisation.

---

### Chapitre 30 — Métriques, évaluation et retour sur investissement

#### Synopsis

**Métriques de processus :** nombre d'exercices, taux de participation des décideurs, nombre de recommandations produites, taux d'implémentation, délai moyen d'implémentation.

**Métriques d'impact :** angles morts identifiés et corrigés, amélioration de la coordination de crise (temps d'escalade, complétude des notifications), amélioration de la connaissance des processus (testée avant/après).

**Métriques de maturité :** modèle en 5 niveaux — Initial, Réactif, Défini, Géré, Optimisé. Le niveau 5 se caractérise par l'intégration de la pensée adversaire dans les décisions quotidiennes, pas seulement dans les exercices formels.

**Le piège de la métrique de vanité :** « on a fait 4 exercices » ne dit rien sur leur qualité. Lien direct avec les anti-patterns du Ch.29.

**La métrique ultime :** le « temps de surprise » lors d'un incident réel. L'organisation qui a pratiqué le red teaming est-elle moins surprise quand le réel arrive ?

> **🪞 MIRRORGATE — Épisode 30 :** Bilan à un an. 87 recommandations, 52 implémentées. Temps d'activation de la cellule de crise : de « jamais testé » à 45 minutes. Lors d'un incident mineur réel en octobre (phishing ciblé avec compromission de 2 postes), le SOC escalade en 12 minutes, le confinement en 35 minutes, le RSSI active le canal de crise prédéfini sans qu'on le demande. Diane : « Ça, c'est la métrique qui compte. »

---

### Chapitre 31 — Cultiver la pensée adversaire au quotidien

#### Synopsis

Le red teaming analytique ne peut pas être qu'un événement — il doit devenir un état d'esprit permanent.

**Les micro-exercices :** « 5 minutes Red Team » intégrés aux réunions régulières. À chaque décision de sécurité : « Si j'étais l'adversaire, comment contournerais-je cette mesure ? » Ce n'est pas un exercice formel, c'est un réflexe.

**Le « Red Team of One » :** l'analyste qui applique les TAS individuellement dans son travail quotidien. Devil's Advocacy sur ses propres analyses, pre-mortem sur ses propres recommandations, What-If sur ses propres hypothèses.

**La culture de la critique constructive :** développement progressif d'une culture où le désaccord argumenté est valorisé, où les hypothèses sont explicitement formulées, où les erreurs sont sources d'apprentissage, où le doute méthodique est signe de professionnalisme.

**Limites à reconnaître :** paralysie par l'analyse, cynisme (tout critiquer sans rien proposer), instrumentalisation (bloquer des décisions qu'on n'aime pas). Le red teaming est un outil de décision éclairée, pas un outil de blocage.

> **🪞 MIRRORGATE — Épisode 31 :** Six mois plus tard. Le SOC manager a spontanément intégré un « round Red Team » dans son daily standup. Le RSSI inclut un slide « hypothèses et limites » dans chaque présentation au COMEX. Et le DG, lors du dernier board, a demandé au DAF : « Quel est le pre-mortem de cette acquisition ? Quels sont les scénarios d'échec que personne ne veut évoquer ? » Diane réalise que le plus grand succès de MIRRORGATE n'est pas les exercices — c'est le changement de posture intellectuelle.

---

## PARTIE VII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.32-34)

*Trois cas complets qui intègrent l'ensemble des concepts du cours dans des livrables opérationnels. Chaque cas active une modalité différente (stress-test stratégique, wargame, tabletop hybride) pour montrer la complémentarité du triptyque.*

---

### Chapitre 32 — Cas complet : red teaming d'une stratégie de défense face à une campagne APT

#### Synopsis

**Modalité activée :** principalement stress-test (Partie V), avec ancrage fort sur la modélisation adversaire (Partie II) et les TAS (Partie III).

**Contexte :** Hélio Group a défini sa stratégie de défense post-incident face au cluster APT. La stratégie repose sur 5 piliers. Diane conduit un red teaming complet.

**Déroulé :** Devil's Advocacy sur chaque pilier, pre-mortem de la stratégie globale, ACH sur les vecteurs d'attaque résiduels, Team A/Team B sur la priorisation des investissements, What-If sur l'évolution du contexte géopolitique.

**Livrable :** rapport de red teaming stratégique avec matrice de vulnérabilités, recommandations priorisées, indicateurs d'alerte précoce.

**Conclusion du fil rouge MIRRORGATE :** le rapport est présenté au COMEX. 3 vulnérabilités critiques identifiées, 7 recommandations, plan d'implémentation sur 6 mois. Le DG : « Pour la première fois, j'ai le sentiment qu'on sait ce qu'on ne sait pas. C'est inconfortable — mais c'est infiniment mieux que l'illusion de sécurité. »

---

### Chapitre 33 — Cas complet : wargame de crise ransomware avec cellule de crise exécutive

#### Synopsis

**Modalité activée :** wargame (Partie IV Ch.17-18).

Format « prêt à jouer » : scénario complet, tous les injects, branches conditionnelles, fiches de rôle Red/Blue/White, guide de facilitation.

**Le scénario :** un opérateur RaaS (profil LockBit/BlackBasta) compromet Hélio via un infostealer acheté à un IAB sur Exploit.in. Accès initial à J-42. L'attaquant fait DCSync, exfiltre 800 Go, déclenche le chiffrement un vendredi 23h. Sauvegardes en ligne chiffrées. AD compromis. Note de rançon 8M€, compte à rebours 72h, leak site actif.

**12 injects sur 10 tours :** alerte initiale → dilemme de la rançon → notification ANSSI → notification CNIL (données de santé) → assureur → négociateur → panne du canal de communication → publication partielle → fuite presse.

**Guide de facilitation :** instructions par tour, critères d'observation, questions de relance, grille de RETEX.

---

### Chapitre 34 — Cas complet : tabletop hybride multi-acteurs — attaque hybride sur infrastructure critique

#### Synopsis

**Modalité activée :** tabletop hybride multi-organisations (Partie IV Ch.21), avec dimension d'exercice de coordination inter-acteurs.

Le cas le plus complexe du cours. Participants : l'opérateur (Hélio), le régulateur (ANSSI simulée), le CERT sectoriel (EE-ISAC simulé), un partenaire industriel (co-victime simulée).

**Le scénario :** dans un contexte de tensions géopolitiques élevées, un acteur étatique mène une opération multi-couches sur 90 jours : (1) campagne de reconnaissance et spearphishing (J-90), (2) compromission d'un sous-traitant partagé avec un autre industriel (J-60), (3) pré-positionnement IT/OT de deux cibles (J-30), (4) campagne de désinformation ciblant le secteur énergétique (J-7), (5) sabotage OT conditionnel (J-0) synchronisé avec hack-and-leak.

**L'exercice teste :** coordination inter-organisationnelle, gestion de l'ambiguïté (incident technique ou opération étatique — ou les deux ?), réponse à une attaque hybride (cyber + information), décisions de communication dans un environnement informationnel hostile.

**Intègre :** cours CTI (profilage), APT (TTP étatiques), L2I (dimension informationnelle), IR (processus), IE (coordination IE/cyber), Dark Web (leak site), OSINT (vérification).

---

## ANNEXES

---

### Annexe A — Glossaire du red teaming analytique

| Terme | Définition |
|-------|-----------|
| **ACH** | Analysis of Competing Hypotheses — TAS évaluant des hypothèses concurrentes contre des preuves |
| **Angle mort (blind spot)** | Zone de vulnérabilité non perçue par l'organisation |
| **Anti-pattern** | Pattern récurrent qui fait échouer un programme de red teaming |
| **Biais de confirmation** | Tendance à chercher les informations confirmant une croyance existante |
| **Blue Team** | Participants jouant leur propre rôle (défenseurs / décideurs) |
| **Cold wash** | Débriefing analytique post-exercice, structuré, quelques jours après |
| **Control / White Team** | Équipe de facilitation et d'arbitrage d'un exercice |
| **Crown Jewels Analysis** | Identification des actifs critiques du point de vue adversaire |
| **Devil's Advocacy** | TAS de contradiction méthodique — défendre systématiquement la position contraire |
| **Exercice adversarial** | Terme générique couvrant wargame, tabletop, et exercices hybrides |
| **Groupthink** | Pensée de groupe — convergence qui supprime les opinions divergentes |
| **Hot wash** | Débriefing à chaud immédiatement après un exercice |
| **HIPPO** | Highest Paid Person's Opinion — biais organisationnel |
| **I&W** | Indicators and Warnings — indicateurs signalant un changement de posture |
| **Inject** | Événement scripté injecté dans un exercice |
| **Matrix wargame** | Format de wargame basé sur l'argumentation arbitrée |
| **Normalisation de la déviance** | Signaux anormaux devenus « normaux » par habituation |
| **OODA** | Observe-Orient-Decide-Act (Boyd) — cycle décisionnel |
| **Outside-In Thinking** | TAS analysant un problème depuis l'extérieur de l'organisation |
| **Pre-mortem** | TAS de projection dans un futur d'échec pour en identifier les causes |
| **Quadrant Crunching** | TAS de scénarisation par matrice 2×2 |
| **Red Hat Analysis** | TAS d'empathie adversaire immersive |
| **Red Team** | Équipe simulant l'adversaire dans un exercice |
| **Red teaming analytique** | Discipline structurée de pensée adversaire pour tester hypothèses et décisions |
| **Red teaming technique** | Simulation d'intrusion réelle (pentest offensif) — distinct du red teaming analytique |
| **Seminar wargame** | Format léger de wargame basé sur la discussion |
| **Stress-test** | Démontage systématique des hypothèses d'un plan ou d'une stratégie |
| **Tabletop exercise (TTX)** | Exercice de discussion structurée autour d'un scénario |
| **TAS** | Techniques Analytiques Structurées |
| **Team A / Team B** | TAS de débat contradictoire structuré |
| **Wargame** | Simulation structurée avec dynamique compétitive Red/Blue |
| **What-If Analysis** | TAS d'exploration des conséquences de changements d'hypothèses |

---

### Annexe B — Catalogue des techniques analytiques structurées

| Technique | Catégorie | Participants | Durée | Livrable | Usage principal |
|-----------|-----------|-------------|-------|----------|-----------------|
| Devil's Advocacy | Challenge | 2-5 | 1-2h | Note de contre-argumentation | Tester une hypothèse dominante |
| Team A / Team B | Débat | 6-12 | 4-8h | Deux analyses concurrentes | Arbitrer entre deux options |
| Pre-mortem | Anticipation | 5-15 | 2-3h | Causes d'échec + indicateurs | Avant implémentation d'un plan |
| ACH | Évaluation | 3-8 | 3-6h | Matrice + hypothèse prioritaire | Comparer des scénarios |
| What-If Analysis | Prospective | 3-10 | 2-4h | Matrice I&W + actions | Conditions de rupture |
| Outside-In Thinking | Recadrage | 5-12 | 2-4h | Facteurs externes | Changement de contexte |
| Quadrant Crunching | Scénarisation | 5-15 | 3-5h | 4 scénarios + implications | Futurs possibles |
| Red Hat Analysis | Empathie | 3-8 | 3-6h | Profil adversaire enrichi | Acteur spécifique |
| Crown Jewels | Cartographie | 5-12 | 2-4h | Matrice actifs × risques | Cibles prioritaires adversaires |
| Seminar Wargame | Exercice | 10-20 | 2-4h | Constatations + recommandations | Coordination + décisions light |
| Matrix Wargame | Exercice | 15-30 | 4-8h | Rapport de wargame détaillé | Crise multi-acteurs |
| Tabletop Exercise | Exercice | 8-25 | 2-4h | Rapport + recommandations | Playbooks, gouvernance |

---

### Annexe C — Templates d'exercices et fiches de facilitation

**C.1 — Template de scénario d'exercice :** objectifs (principal, secondaires, hors périmètre), contexte (organisation, secteur, réglementation, géopolitique), participants (Blue, Red, White), format et timing (type, durée, tours, temps simulé), scénario initial, injects par tour, branches conditionnelles, critères d'observation, grille de RETEX.

**C.2 — Fiche de rôle Red Team :** profil adversaire (acteur, motivation, capacités, contraintes, objectif), règles d'engagement (rester dans le profil, adapter aux réponses Blue, signaler les décisions clés, ne pas chercher à gagner), actions prévues par tour + alternatives.

**C.3 — Template de rapport d'exercice :** synthèse exécutive (1-2 pages), déroulé chronologique, constats détaillés par catégorie, forces identifiées, vulnérabilités classées par criticité, recommandations priorisées avec responsable et échéance, matrice de suivi, annexes.

**C.4 — Template de rapport de stress-test :** objet analysé (document, version, date), hypothèses identifiées (explicites + implicites), classification (vérifiées / plausibles / fragiles), pour chaque hypothèse fragile : impact potentiel si fausse + recommandation + indicateur de dérive, plan d'implémentation.

---

### Annexe D — Banque de scénarios et d'injects

#### D.1 — Scénarios types par catégorie de menace

| Catégorie | Scénario | Adversaire | Durée simulée | Dimensions testées |
|-----------|----------|-----------|---------------|-------------------|
| Ransomware | RaaS avec exfiltration et leak site | Cybercriminel | 72h-7j | IR, crise, communication, réglementaire |
| APT / Espionnage | Intrusion longue avec pivot OT | Acteur étatique | 6-18 mois | CTI, détection, coordination, géopolitique |
| Supply chain | Compromission éditeur logiciel | Variable | 2-4 semaines | IR, supply chain, multi-organisations |
| Insider | Exfiltration par employé mécontent | Insider | 1-3 mois | DRH, juridique, forensic, éthique |
| Hybride | Cyber + désinformation + hack-and-leak | Acteur étatique | 3-6 mois | CTI, IE, L2I, communication |
| BEC | Fraude au président | Cybercriminel | 48-72h | Finance, validation, sensibilisation |
| Cloud | Compromission du tenant cloud | Variable | 1-2 semaines | Cloud security, PRA, dépendance |
| DDoS + extorsion | DDoS massif avec rançon | Cybercriminel | 24-72h | SOC, ISP, communication, continuité |

#### D.2 — Injects universels

| Type | Inject | Dimension testée |
|------|--------|-----------------|
| Technique | « L'EDR détecte Mimikatz sur DC02 à 03h17 » | Détection, qualification, escalade |
| Opérationnel | « Le VPN est indisponible — 200 collaborateurs bloqués » | Continuité, priorisation |
| Médiatique | « Un journaliste appelle en citant des documents internes » | Communication de crise |
| Réglementaire | « L'ANSSI appelle pour un point de situation dans 2h » | Notification, coordination |
| Adversaire | « Le groupe publie 10 Go et un ultimatum de 48h » | Décision stratégique |
| RH | « L'analyste SOC senior d'astreinte est injoignable » | Résilience, plans B |
| Juridique | « L'avocat déconseille de communiquer, le DPO recommande de notifier » | Arbitrage, autorité |
| Fournisseur | « Le prestataire IR annonce 48h de délai » | Dépendance, alternatives |
| Financier | « L'assureur exige un rapport sous 5 jours » | Coordination juridique/financière |
| Interne | « Un collaborateur poste sur LinkedIn : notre boîte a été hackée » | Communication interne, réseaux sociaux |

---

### Annexe E — Outils et ressources de référence

| Catégorie | Outil | Type | Usage |
|-----------|-------|------|-------|
| Facilitation | Miro / Mural | SaaS | Tableaux blancs collaboratifs |
| Facilitation | Excalidraw | Gratuit (OSS) | Schémas de situation |
| Scénarisation | MITRE ATT&CK | Base de données | TTP pour le réalisme |
| Scénarisation | The DFIR Report | Blog | Intrusions complètes pour inspiration |
| Profilage | Malpedia | Base de données | Profils d'acteurs |
| Profilage | MITRE ATT&CK Groups | Base de données | Mapping acteurs ↔ TTP |
| Analyse | ACH 2.0 (Palo Alto) | Logiciel gratuit | Matrice ACH informatisée |
| Analyse | PARC ACH | Logiciel gratuit | ACH en ligne |
| Exercice | CISA Tabletop Exercise Packages | Templates | Scénarios pré-construits |
| Exercice | ENISA Cyber Exercises | Guides | Conception d'exercices |
| Wargaming | RAND Corporation | Publications | Méthodologies |
| Documentation | Obsidian | Gratuit | Suivi des recommandations |

---

### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Red teaming analytique, pensée adversaire | **Ce cours** | — |
| Processus analytique CTI | **Cours CTI** | Ce cours (Ch.13 ACH, Ch.5-6 profilage — même rigueur) |
| Acteurs étatiques / APT | **Cours APT** | Ce cours (Ch.5-9, Ch.18 wargame géopolitique, Ch.32) |
| Réponse à incident | **Cours IR** | Ce cours (Ch.20 tabletop technique, Ch.25 stress-test plan IR, Ch.33) |
| Lutte informationnelle / L2I | **Cours L2I** | Ce cours (Ch.18, Ch.34 attaque hybride) |
| Intelligence économique | **Cours IE** | Ce cours (Ch.7 surface d'attaque stratégique, Ch.34) |
| OSINT | **Cours OSINT** | Ce cours (Ch.7 surface d'attaque OSINT sur soi-même) |
| Dark Web | **Cours Dark Web** | Ce cours (Ch.8 scénarios, Ch.33) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | Ce cours (Ch.6 modélisation, Ch.33 RaaS) |
| HUMINT et Social Engineering | **Cours HUMINT & SE** | Ce cours (Ch.7, Ch.20 injects SE) |
| Panorama de la Cybermenace | **Cours Panorama** | Ce cours (Ch.8 portfolio aligné sur CTL sectoriel) |
| FININT | **Cours FININT** | Ce cours (Ch.18 supply chain financière, Ch.33) |
| IA & Sécurité | **Cours IA & Sécurité** | Ce cours (Ch.31 micro-exercices) |
| GRC / Risques | **Cours GRC** | Ce cours (Ch.7, Ch.24-27 stress-tests, Ch.30 métriques) |
| SOC et détection | **Cours SOC** | Ce cours (Ch.20 tabletop technique, Ch.14 I&W) |
| Forensic numérique | **Cours Forensic** | Ce cours (Ch.20 chaîne de preuve dans les exercices) |
| Active Directory | **Cours AD** | Ce cours (Ch.26 reconstruction AD dans le stress-test PRA) |
| Cybersécurité du quotidien | **Cours Cyber Quotidien** | Ce cours (Ch.31 pensée adversaire quotidienne) |

---

### Annexe G — Ressources, formations et communautés

#### Ouvrages de référence

| Titre | Auteur(s) | Sujet |
|-------|-----------|-------|
| *Red Team: How to Succeed by Thinking Like the Enemy* | Micah Zenko | Red teaming — principes, cas, méthodologie |
| *Psychology of Intelligence Analysis* | Richards Heuer | Biais cognitifs et TAS — le livre fondateur |
| *Structured Analytic Techniques for Intelligence Analysis* | Heuer & Pherson | Manuel complet des TAS |
| *Thinking in Bets* | Annie Duke | Décision sous incertitude |
| *The Art of the Long View* | Peter Schwartz | Scénarisation et planification stratégique |
| *Superforecasting* | Philip Tetlock | Prévision et jugement calibré |
| *Thinking, Fast and Slow* | Daniel Kahneman | Biais cognitifs — base théorique |
| *Team of Teams* | Stanley McChrystal | Coordination et adaptabilité organisationnelle |
| *The Cyber Wargaming Handbook* | US Naval War College | Méthodologie de wargaming cyber |
| *Wargaming for Leaders* | Mark Herman et al. | Wargaming stratégique appliqué |

#### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| Red Team Leader (UFMCS) | US Army — Fort Leavenworth | Red teaming analytique — référence mondiale |
| Applied Critical Thinking | UFMCS | Techniques analytiques structurées |
| FOR578 — Cyber Threat Intelligence | SANS | CTI avec composante analytique |
| MGT514 — IT Security Strategic Planning | SANS | Stratégie cyber et exercices |
| Wargaming courses | King's College London | Wargaming stratégique et cyber |
| ENISA Cyber Exercises | ENISA | Conception et conduite d'exercices |

#### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| Connections (Wargaming Conference) | Conférence annuelle | Plus grande conférence de wargaming |
| PAXsims | Blog/communauté | Praticiens du wargaming |
| CISA Exercises | Ressources publiques | Templates et guides |
| FIRST | Communauté CERT | Exercices inter-CERT |
| FIC / InCyber (Lille) | Conférence | Track exercices de crise |
| CyCon (Tallinn) | Conférence | Dimension stratégique du cyber |

#### Publications institutionnelles

| Publication | Organisme | Contenu |
|------------|-----------|---------|
| Red Team Handbook | UFMCS / US Army | Manuel de référence |
| Cyber Tabletop Exercise Guide | CISA | Guide de conception de tabletop |
| Good Practice Guide on Exercises | ENISA | Guide européen des exercices cyber |
| Wargaming Handbook | UK MoD DCDC | Méthodologie britannique |
| TIBER-EU Framework | BCE | Cadre red team — secteur financier |
| DORA Testing Requirements (TLPT) | UE | Exigences de tests de résilience |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à la discipline du red teaming analytique — pas à un format d'exercice, pas à une méthodologie d'audit, pas à un cadre de compliance. Il forme à une **posture intellectuelle** : celle qui consiste à penser comme l'adversaire pour mieux défendre.
>
> L'architecture du cours suit un triptyque strict :
> - **Penser comme l'adversaire** (Parties I-III) — la discipline intellectuelle.
> - **Transformer cette pensée en exercices** (Partie IV) — wargame et tabletop comme deux modalités complémentaires.
> - **Utiliser cette pensée et ces exercices pour tester l'organisation** (Partie V) — le stress-test des plans et stratégies existantes.
>
> Les trois dernières parties installent cette capacité dans la durée (Partie VI) et la consolident par des cas complets (Partie VII).
>
> L'opération MIRRORGATE illustre la trajectoire : d'une organisation convaincue d'être préparée à une organisation réellement préparée. Le chemin est inconfortable — le red teaming analytique force à regarder ce qu'on préfère ignorer. Mais l'inconfort d'un exercice est infiniment préférable à l'inconfort d'un incident réel.
>
> Le cours assume quatre convictions.
> - Première : les plans non testés sont des fictions.
> - Deuxième : les biais cognitifs et organisationnels sont les vulnérabilités les plus critiques.
> - Troisième : les programmes de red teaming les plus destructeurs sont ceux qui fonctionnent en apparence — d'où le chapitre dédié aux anti-patterns.
> - Quatrième : le red teaming analytique n'est pas un luxe réservé aux grandes organisations, c'est un état d'esprit applicable à toute échelle.
>
> *Douter avec méthode • Tester avant que le réel ne teste • Regarder ce qu'on ne veut pas voir • Décider en connaissance de cause — et toujours distinguer ce qu'on sait de ce qu'on suppose.*

---

*Fin du cours — Red Teaming Analytique et Simulation Adversaire*
*Version 2025-2026 — v2 (restructuration)*
