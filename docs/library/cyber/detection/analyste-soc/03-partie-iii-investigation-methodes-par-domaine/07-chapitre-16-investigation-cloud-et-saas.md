---
title: Chapitre 16 — Investigation cloud et SaaS
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

Ce chapitre développe l'investigation dans les environnements M365/Azure et AWS avec des requêtes concrètes. Scénario BEC complet (phishing AitM → token replay → forwarding rule → exfiltration SharePoint → phishing interne) avec les requêtes KQL Sentinel à chaque étape. Scénario AWS (access keys compromises → CloudTrail analysis → modification de security groups → lancement d'instances). Le défi de la corrélation cloud ↔ on-premise quand l'attaquant pivote entre les deux mondes.

---
