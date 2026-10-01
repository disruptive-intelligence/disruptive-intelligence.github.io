---
title: Partie I — Fondations (ch.1-4)
source: Cyber/01 CTI & renseignement/Méthodes d'analyse/Red teaming analytique.md
note: Red teaming analytique
up:
- - Red teaming analytique
  - index.md
---

*Qu'est-ce que le red teaming analytique, d'où vient-il, et qu'est-ce qui le distingue radicalement des disciplines voisines ?*

---


## Chapitre 1 — Définition et frontières

### Synopsis

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


## Chapitre 2 — Origines et positionnement

### Synopsis

L'histoire du red teaming comme discipline : Kriegsspiel prussiens (1811), Red Cell CIA (années 1960), Team B (1976), programmes DoD post-11 septembre. Le rôle de l'*advocatus diaboli* dans la tradition vaticane comme fonction institutionnalisée de contradiction.

L'adoption par la cybersécurité : le red teaming technique a précédé le red teaming analytique. Les limites du purement technique sont devenues évidentes — tester les défenses sans tester les décisions laisse des angles morts critiques. Le Millennium Challenge 2002 comme cas d'école (red teaming authentique vs. red teaming de façade, puisque les règles ont été changées quand le Red l'a emporté).

Publications fondatrices : *Red Team Handbook* (UFMCS Fort Leavenworth), *Red Team* de Micah Zenko, framework OTAN, adaptations cyber récentes (CBEST, TIBER-EU, DORA TLPT — qui combinent pentest et dimension analytique, mais restent largement techniques dans leur mise en œuvre).

Positionnement dans l'écosystème cyber : à l'intersection de la CTI (comprendre l'adversaire), de la gestion de crise (tester les réponses), de la stratégie (valider les choix), et de l'analyse de renseignement (rigueur méthodologique).

> **🪞 MIRRORGATE — Épisode 2 :** Le RSSI : « On fait un pentest annuel et un exercice NIS 2. C'est du red teaming, non ? » Diane : « Le pentest teste vos murs. L'exercice teste votre compliance. Aucun des deux ne teste vos décisions. »

---


## Chapitre 3 — Biais cognitifs et défaillances organisationnelles

### Synopsis

Le chapitre central sur le « pourquoi » profond du red teaming analytique.

**Biais cognitifs critiques pour le décideur cyber :** confirmation, ancrage, illusion de contrôle, biais du survivant, normalisation de la déviance (Challenger, Columbia, et les logs SolarWinds ignorés pendant 14 mois), biais d'optimisme, biais de disponibilité (on se prépare au dernier incident, pas au prochain).

**Défaillances organisationnelles :** groupthink (Janis — Baie des Cochons, escalade au Vietnam), silos informationnels (le SOC sait ce que le RSSI ignore, que le DG n'apprendra jamais), effet HIPPO, culture du « oui » (personne ne contredit le plan du RSSI en réunion).

**Le paradoxe de la préparation :** les organisations les plus convaincues d'être préparées sont souvent les moins bien préparées — parce que leur confiance inhibe le questionnement.

Chaque biais illustré par un cas cyber réel : SolarWinds (normalisation de la déviance), Colonial Pipeline (illusion de contrôle — le plan ne couvrait pas l'arrêt volontaire par panique), Capital One (biais de confirmation — le WAF était supposé bloquer les SSRF).

> **🪞 MIRRORGATE — Épisode 3 :** Diane demande à 5 responsables clés le scénario de menace n°1 pour Hélio. 5 réponses différentes. Aucune ne correspond au scénario qui a effectivement touché l'entreprise.

---


## Chapitre 4 — Le red teamer analytique

posture, compétences et déontologie

### Synopsis

Le profil : ni pentester, ni consultant GRC, ni analyste CTI — un métier distinct qui emprunte aux trois.

**Compétences :** pensée critique et logique argumentative, connaissance du paysage de la menace, facilitation, diplomatie et intelligence situationnelle, production écrite.

**Déontologie :** transparence sur les objectifs, confidentialité des résultats bruts, distinction « tester les plans » vs. « tester les personnes », gestion du stress (un exercice qui terrorise est un exercice raté).

**Première apparition du thème des anti-patterns :** le red teaming « de façade » est introduit ici comme une posture à éviter, et fera l'objet du Ch.29 dédié.

> **🪞 MIRRORGATE — Épisode 4 :** Diane recrute Thomas, ex-analyste CTI. « Notre job n'est pas d'avoir raison. Notre job est de forcer l'organisation à se poser les bonnes questions. Le jour où le RSSI nous remercie trop chaleureusement, c'est qu'on n'a pas assez poussé. »

---
