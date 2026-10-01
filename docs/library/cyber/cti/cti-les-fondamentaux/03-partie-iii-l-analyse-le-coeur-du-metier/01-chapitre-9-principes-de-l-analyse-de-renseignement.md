---
title: Chapitre 9 — Principes de l'analyse de renseignement
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - 'Partie III — L''analyse : le cœur du métier'
  - index.md
---

## 9.1 Ce que signifie « analyser »

Analyser, en CTI, ne signifie pas résumer un rapport (« Mandiant dit que APT29 cible le secteur énergie »). Analyser signifie contextualiser (cette information est-elle pertinente pour notre organisation ? dans quel contexte s'inscrit-elle ?), corréler (cette information est-elle cohérente avec ce que nous observons dans nos logs, dans les autres sources, dans nos incidents passés ?), évaluer (quelle confiance accorder à cette information ? la source est-elle fiable ? l'information est-elle corroborée ?), et conclure avec un niveau de confiance (« nous évaluons avec un niveau de confiance modéré que UNC-VOLT est lié au GRU, sur la base de la convergence de TTP, d'infrastructure partagée, et de victimologie cohérente, tout en notant que ces éléments pourraient être des faux drapeaux »).

## 9.2 Fait, déduction, hypothèse, inconnue

Cette distinction — empruntée à la rigueur forensique — doit être explicite dans chaque produit CTI.

Un **fait** est un observable vérifiable : « l'attaquant a utilisé le domaine C2 `update-srv-infra[.]xyz`, enregistré le 15 janvier 2026 via le registrar NameCheap, résolvant vers l'IP 185.xx.xx.xx (ASN: Serverius, Pays-Bas) » — vérifiable par passive DNS, Whois, et les artefacts IR.

Une **déduction** est une conclusion logique tirée de faits vérifiés : « l'attaquant a exploité la vulnérabilité CVE-2024-21887 (Ivanti Connect Secure) comme vecteur d'accès initial, car les logs du VPN Ivanti montrent une requête d'exploitation correspondant à la signature publique de cette CVE, suivie immédiatement d'une session authentifiée avec un compte de service compromis » — déduction forte, basée sur la corrélation de deux sources indépendantes.

Une **hypothèse** est une interprétation plausible non confirmée : « UNC-VOLT est probablement lié au GRU car les TTP observées sont compatibles avec le tradecraft de Sandworm, l'infrastructure partage des patterns d'enregistrement avec des campagnes Sandworm précédentes, et la victimologie (opérateur d'énergie européen) est cohérente avec les objectifs stratégiques du GRU » — hypothèse étayée par un faisceau d'indices mais qui admet des alternatives (faux drapeaux, acteur imitant Sandworm, infrastructure partagée accidentellement).

Une **inconnue** est ce que l'investigation n'a pas pu déterminer : « l'investigation n'a pas pu confirmer si l'attaquant a exfiltré des données du réseau SCADA — les logs de supervision ne couvraient pas la période concernée ».

## 9.3 Le raisonnement abductif

L'analyste CTI pratique le raisonnement abductif — l'inférence à la meilleure explication. Face à un ensemble d'observables, il cherche l'explication qui rend compte du plus grand nombre d'observations de la manière la plus simple et la plus cohérente. Ce n'est pas de la déduction (certitude logique) ni de l'induction (généralisation statistique) — c'est un raisonnement probabiliste qui accepte l'incertitude et qui doit être accompagné d'un niveau de confiance.

---
