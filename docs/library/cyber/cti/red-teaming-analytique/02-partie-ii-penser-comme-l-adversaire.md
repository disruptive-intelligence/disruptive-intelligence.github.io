---
title: Partie II — Penser comme l'adversaire
source: Cyber/01 CTI & renseignement/Méthodes d'analyse/Red teaming analytique.md
note: Red teaming analytique
up:
- - Red teaming analytique
  - index.md
---

MODÉLISATION DE LA MENACE (Ch.5-9)

*Première couche du triptyque : comment construire un modèle mental crédible de l'adversaire. Cette partie est de la **modélisation**, pas de la conception d'exercice — elle prépare la matière première que les exercices et stress-tests utiliseront plus tard.*

---


## Chapitre 5 — Profilage adversaire

### Synopsis

Modèle en 6 dimensions : identité/attribution, motivation, capacités, contraintes, historique, adaptabilité.

Sources : CTI (cours CTI Ch.3, Ch.13-19), RETEX des incidents passés, OSINT sur les acteurs, renseignement dark web, rapports sectoriels.

**Le piège de l'adversaire omniscient** : l'erreur la plus fréquente est de modéliser un attaquant sans contraintes. L'adversaire réel fait des erreurs, a des ressources limitées, fait des arbitrages. Le red teaming crédible modélise **les contraintes autant que les capacités**.

> **🪞 MIRRORGATE — Épisode 5 :** Premier profilage. Cluster attribué avec confiance modérée à un acteur étatique. Motivations (espionnage industriel), capacités (TTP sophistiquées, pas de zero-day observé), contraintes (OPSEC stricte, objectif de discrétion = acteur patient).

---


## Chapitre 6 — Motivations, contraintes et rationalité de l'adversaire

### Synopsis

Le modèle RAG (Rational Actor + Goals) : l'adversaire est rationnel dans son propre cadre de référence, même quand ses actions semblent irrationnelles de notre point de vue.

Application aux quatre archétypes : acteur étatique (objectifs politiques, contraintes diplomatiques), groupe cybercriminel (objectifs financiers, rationalité économique), insider (objectifs personnels, rationalité émotionnelle), hacktiviste (objectifs idéologiques, rationalité de visibilité).

Le facteur **coût-bénéfice** : chaque action offensive a un coût (détection, consommation de capacités, temps, dépense d'une zero-day). Comprendre les arbitrages de l'adversaire permet d'anticiper ses choix.

Limites de l'analyse rationnelle : erreurs de l'adversaire, frictions organisationnelles internes (un APT n'est pas monolithique), décisions politiques qui contredisent la logique opérationnelle, « fog of war ».

> **🪞 MIRRORGATE — Épisode 6 :** « Si vous étiez le service de renseignement qui nous a ciblés, quel serait votre prochain mouvement ? » Personne dans la salle ne mentionne la possibilité que l'attaquant soit encore dans le réseau via un accès non détecté.

---


## Chapitre 7 — Cartographie de la surface d'attaque du point de vue adversaire

### Synopsis

Regarder sa propre organisation avec les yeux de l'adversaire — pas la surface d'attaque technique (pentest), mais la **surface d'attaque stratégique**.

La matrice exposition × valeur × accessibilité. Les vecteurs non techniques : surface humaine (lien cours HUMINT & SE), surface informationnelle (lien cours OSINT), surface juridique/réglementaire (forcer une divulgation publique via RGPD, par exemple).

L'exercice **Crown Jewels Analysis** : identifier les 5-10 actifs que l'adversaire ciblerait en priorité, les chemins d'accès, les défenses à chaque étape.

> **🪞 MIRRORGATE — Épisode 7 :** Exercice Crown Jewels. Les actifs protégés par l'IT (AD, messagerie) ne correspondent pas aux actifs ciblés par l'adversaire (plans de propulsion, données de simulation, poste OT). « L'IT protège ce qui fait tourner l'IT. L'adversaire cible ce qui a de la valeur pour son commanditaire. »

---


## Chapitre 8 — Modélisation de scénarios d'attaque plausibles

### Synopsis

**Point important** : ce chapitre est de la **modélisation analytique**, pas de la conception d'exercice. La conception d'exercice (mise en scène du scénario) est traitée en Partie IV. Ici, on produit la matière première : des scénarios cohérents, fondés, testables.

Structure d'un scénario en 7 éléments : acteur, objectif, vecteur d'accès, chemin d'attaque, actions sur objectif, chronologie, points de décision défenseur.

Calibrage de la plausibilité — scoring basé sur : précédent historique, capacité technique de l'adversaire, motivation, faisabilité dans le contexte spécifique.

Le **portfolio de scénarios** : une organisation ne teste pas un scénario unique mais un portfolio couvrant les menaces prioritaires, aligné sur le Cyber Threat Landscape sectoriel (lien cours Panorama).

Typiquement : un scénario APT/espionnage, un scénario ransomware, un scénario supply chain, un scénario insider, un scénario hybride (cyber + informationnel).

> **🪞 MIRRORGATE — Épisode 8 :** Premier portfolio de 5 scénarios pour Hélio Group. Le scénario n°1 (retour de l'APT par sous-traitant OT) provoque un débat. Le responsable achats affirme que les sous-traitants sont audités annuellement. Diane : « Audités sur quoi ? Par qui ? Avec quels critères cyber ? » Silence. Premier angle mort identifié.

---


## Chapitre 9 — L'adversaire adaptatif

### Synopsis

L'adversaire n'est pas statique — il apprend, s'adapte, réagit aux défenses.

Le cycle OODA de l'adversaire (Observe-Orient-Decide-Act). Quand il est détecté ou bloqué, il recommence le cycle : observe la réaction du défenseur, réévalue, adapte.

Les patterns d'adaptation : pivot de vecteur (phishing bloqué → exploitation), pivot d'infrastructure (C2 saisi → C2 alternatif), pivot de cible (cible durcie → sous-traitant), escalade (détection → destruction pour effacer les traces), abandon/retour (éradiqué → revient 6 mois plus tard).

L'exercice **« Et alors ? » (So What?)** : pour chaque mesure défensive envisagée, itérer la question sur 3-5 tours. Révèle les hypothèses fragiles.

> **🪞 MIRRORGATE — Épisode 9 :** Atelier « Et alors ? » sur les mesures post-incident. Tour 1 : « On a patché Ivanti. » — « L'adversaire revient par un 0-day. » Tour 2 : « On monitore les équipements de bordure. » — « Il passe par un sous-traitant. » Tour 3 : « On impose des exigences cyber aux sous-traitants. » — « Il compromet le fournisseur du sous-traitant. » Diane conclut : « Chaque mesure réduit le risque. Aucune ne l'élimine. Le red teaming sert à identifier quels risques résiduels vous acceptez consciemment — et lesquels vous ignorez inconsciemment. »

---
