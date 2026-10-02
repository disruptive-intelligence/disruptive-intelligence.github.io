---
title: Chapitre 24 — Réponse à un incident de social engineering
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie V — Défense et contre-ingénierie sociale
  - index.md
---

## 24.1 Détection

La détection d'un incident de social engineering repose sur trois sources : le signalement par l'employé (scénario optimal — c'est pourquoi la culture de signalement est la première défense), la détection technique (connexion anormale, alertes EDR, détection de credentials compromis, analyse de sessions) et la notification externe (un partenaire alerte, un service de renseignement notifie, un chercheur en sécurité signale).

Le temps de détection est critique, en particulier pour le BEC (un virement frauduleux peut être irrécupérable en quelques heures) et pour les intrusions utilisant des credentials compromis (l'attaquant latéralise et exfiltre rapidement).

## 24.2 Qualification

La qualification de l'incident détermine la réponse. Les scénarios principaux sont : phishing réussi simple (credentials compromis — impact limité si le compte n'a pas de privilèges élevés), BEC en cours (virement initié — nécessite une action bancaire urgente pour bloquer le transfert), intrusion physique (implant posé — nécessite une recherche physique et réseau), élicitation de renseignement (fuite d'information — difficile à quantifier, nécessite une évaluation de l'impact).

## 24.3 Containment

Le containment dépend du type d'incident : reset des credentials compromis (tous les comptes affectés), révocation des sessions actives, blocage des accès à risque, recherche de persistence (l'attaquant a-t-il installé des backdoors ou créé des comptes additionnels ?), isolement du segment réseau si un implant physique est suspecté, et pour le BEC, gel du virement via la banque (la rapidité est déterminante — les fonds transférés à l'étranger sont souvent irrécupérables après 24-48h).

## 24.4 Investigation

L'investigation d'un incident de social engineering combine forensique technique et analyse humaine. Forensique email (headers complets, analyse de la landing page, identification de l'infrastructure de phishing), identification de l'acteur (phishing de masse vs spear-phishing ciblé vs APT — la sophistication et la personnalisation sont des indicateurs), évaluation de l'impact (quels accès ont été compromis, quelles données ont potentiellement été exfiltrées, quelle est la persistance de l'attaquant), et analyse de la chaîne de compromission (comment l'attaquant est passé de l'accès initial à ses objectifs finaux).

## 24.5 Retex et amélioration

Le retex (retour d'expérience) post-incident est une obligation, pas une option. Il doit suivre le modèle « no blame post-mortem » : l'objectif est d'identifier les défenses qui ont échoué et de les améliorer, pas de blâmer l'employé qui a cliqué.

Le retex couvre : la chronologie de l'incident (de la première action de l'attaquant à la détection et au containment), les défenses qui ont fonctionné (qu'est-ce qui a alerté ou ralenti l'attaquant ?), les défenses qui ont échoué (pourquoi le phishing n'a pas été filtré ? pourquoi le helpdesk a procédé au reset sans vérification suffisante ?), les recommandations d'amélioration (classées P0/P1/P2), et le plan d'action avec responsable et échéance pour chaque recommandation.

---
