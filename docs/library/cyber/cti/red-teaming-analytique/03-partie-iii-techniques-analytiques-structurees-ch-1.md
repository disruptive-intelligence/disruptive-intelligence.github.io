---
title: Partie III — Techniques analytiques structurées (ch.10-15)
source: Cyber/Red_Teaming.md
note: Red teaming analytique
up:
- - Red teaming analytique
  - index.md
---

*La colonne méthodologique du cours. Les TAS sont les outils qui transforment le doute intuitif en intelligence exploitable — applicables tant à la modélisation (Partie II) qu'aux exercices (Partie IV) et aux stress-tests (Partie V).*

---


## Chapitre 10 — Devil's Advocacy

### Synopsis

La technique la plus ancienne et la plus fondamentale. Le Devil's Advocate n'exprime pas son opinion personnelle — il défend systématiquement la position contraire pour tester la solidité de l'hypothèse dominante.

Protocole en 5 étapes. Applications cyber : challenger la stratégie, les conclusions CTI, les décisions de crise. Règles de facilitation : mandaté (pas auto-proclamé), temporaire (pas un rôle permanent), dépersonnalisé (challenge l'argument, pas la personne). Pièges : DA de façade, complaisant, toxique.

> **🪞 MIRRORGATE — Épisode 10 :** Diane joue le DA au comité de revue stratégique. Le RSSI : « Priorité Zero Trust et SOC 24/7. » Diane : « Votre Zero Trust couvre l'IT. L'attaquant est passé par l'OT. Votre SOC analyse les logs Windows. L'attaquant a utilisé des protocoles ICS. En quoi cette roadmap empêche le scénario qui s'est déjà produit ? »

---


## Chapitre 11 — Team A / Team B

### Synopsis

Protocole complet. Variantes : hypothèse imposée vs. libre. Applications : évaluation de la posture, attribution d'un incident, choix stratégique. Le cas historique Team B (1976) — succès (biais révélés), excès (sur-estimation idéologique), leçons.

> **🪞 MIRRORGATE — Épisode 11 :** Team A vs. Team B sur OTIS Maintenance. Team A (RSSI) : « Risque géré. » Team B (Thomas) : « VPN permanent, postes non monitorés, 3 techniciens avec droits AD excessifs. » Le DG : « Depuis quand a-t-on ces informations ? » — « Depuis toujours. Personne ne les avait rassemblées. »

---


## Chapitre 12 — Pre-mortem

### Synopsis

Gary Klein, 1998. Se projeter dans un futur où le plan a échoué, et travailler à rebours. L'inverse du planning optimiste.

Protocole en 6 étapes. Pourquoi ça fonctionne : contourne la dynamique de groupe qui inhibe la critique, force la spécificité (pas « ça pourrait mal tourner » mais « ça a mal tourné parce que... »), produit directement des indicateurs d'alerte précoce.

Applications cyber : pre-mortem du plan IR, d'une migration cloud, d'un programme de sensibilisation.

> **🪞 MIRRORGATE — Épisode 12 :** Pre-mortem du PCA. Postulat : « Ransomware, 80 % du parc chiffré, sauvegardes incluses. 3 semaines plus tard, production pas reprise. Pourquoi ? » Les réponses convergent : sauvegardes jamais testées, PCA ne couvre pas la perte simultanée AD + messagerie, personne ne sait qui décide l'arrêt OT. Diane : « Tout ce que vous venez de dire était déjà vrai hier. Le pre-mortem vous a juste donné la permission de le formuler. »

---


## Chapitre 13 — Analysis of Competing Hypotheses (ACH)

### Synopsis

ACH de Richards Heuer (CIA, 1999) — technique analytique la plus rigoureuse pour évaluer des hypothèses concurrentes.

**L'ACH retournée pour le red teaming** : au lieu de « quel acteur est responsable ? », la question devient « quel scénario est le plus probable ? » ou « quelle hypothèse de défense est la plus fragile ? ».

L'ACH comme outil de priorisation des exercices et stress-tests. L'ACH comme antidote au biais de confirmation. Limites : dépendance à la qualité des hypothèses, sous-évaluation des scénarios « impensables », difficulté avec les hypothèses combinées.

> **🪞 MIRRORGATE — Épisode 13 :** ACH sur le vecteur du prochain incident. 5 hypothèses. Après la matrice : H3 (compromission sous-traitant) est l'hypothèse la moins réfutable ET la moins couverte. C'est le scénario prioritaire.

---


## Chapitre 14 — What-If Analysis, indicateurs et signaux d'alerte précoce

### Synopsis

Protocole What-If en contexte cyber. Les **I&W (Indicators and Warnings)** : concept issu du renseignement militaire adapté au cyber. Méthodologie de construction d'une matrice I&W.

Application : transformer la CTI passive (« voici les menaces ») en CTI proactive (« voici ce qu'il faut surveiller pour détecter les menaces avant qu'elles ne se matérialisent »).

> **🪞 MIRRORGATE — Épisode 14 :** Matrice I&W pour le scénario « compromission sous-traitant OT ». 5 indicateurs transmis au SOC : « Si vous voyez 3 sur 5, ça ne veut pas dire qu'on est attaqué — ça veut dire qu'il faut investiguer. »

---


## Chapitre 15 — Autres TAS

Outside-In Thinking, Quadrant Crunching, Red Hat Analysis

### Synopsis

**Outside-In Thinking :** renverser la perspective depuis l'environnement externe. Quels facteurs externes (géopolitiques, technologiques, réglementaires) pourraient changer radicalement notre profil de menace ?

**Quadrant Crunching :** matrice 2×2 de scénarisation prospective. Identifier les deux incertitudes critiques, les croiser, explorer les 4 scénarios résultants.

**Red Hat Analysis :** empathie adversaire immersive. Le red teamer joue littéralement le rôle de l'adversaire avec ses données, contraintes, chaîne de commandement. Plus exigeant que le simple profilage.

Tableau comparatif complet des TAS : quand utiliser, participants, durée, livrables, limites.

> **🪞 MIRRORGATE — Épisode 15 :** Quadrant Crunching sur l'évolution à 18 mois. Incertitudes : escalade géopolitique × obtention du contrat ESA. Quatre scénarios. Celui « escalade + contrat » multiplie drastiquement le risque d'espionnage et de sabotage. Jamais envisagé formellement.

---
