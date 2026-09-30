---
title: 'Ch.25 — Cas complet : réponse à incident IA'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie VI — Cas de synthèse
  - index.md
---

Ce chapitre documente l’incident complet du RAG poisoning décrit au Ch.22 sous un angle processus de réponse à incident, en appliquant les 6 phases classiques (préparation, détection, confinement, investigation, remédiation, retex) au contexte spécifique d’un incident IA.

Le point clé est que la réponse à incident IA suit le même processus que la réponse à incident classique, mais avec des spécificités : le confinement peut nécessiter un kill switch du système IA (pas seulement une isolation réseau), l’investigation doit tracer les réponses contaminées (pas seulement les accès réseau), la remédiation implique une purge et réindexation de la base vectorielle (pas seulement un patch), et la communication doit inclure le DPO pour évaluer si une notification CNIL est nécessaire.

Le livrable de cet exercice est un plan de réponse à incident IA formel pour NovaSanté, intégré au plan de réponse à incident existant, avec les procédures spécifiques (kill switch, purge vectorielle, analyse des réponses contaminées) et les rôles (RSSI pilote, ML Engineer exécute, DPO évalue la notification).

-----
