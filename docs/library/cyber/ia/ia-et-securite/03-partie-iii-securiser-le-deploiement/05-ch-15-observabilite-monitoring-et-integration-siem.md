---
title: Ch.15 — Observabilité, monitoring et intégration SIEM
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie III — Sécuriser le déploiement
  - index.md
---

## 15.1 Logging

Chaque interaction avec le système IA doit être tracée. Le log minimal inclut le timestamp, l’identifiant de l’utilisateur, le prompt (ou un hash si la taille est prohibitive), la réponse (ou un résumé), le modèle utilisé, les sources RAG consultées (identifiants des chunks), les actions de l’agent (si applicable), la latence, le coût (tokens consommés), et le résultat des guardrails (requête filtrée ? réponse filtrée ? raison ?).

Les logs eux-mêmes sont des données sensibles — ils contiennent en clair les questions et les réponses, qui peuvent inclure des données personnelles, des informations médicales, des données financières. Ils doivent être chiffrés at rest, avec un contrôle d’accès strict, et une durée de conservation définie (alignée avec la politique de rétention des données et les exigences RGPD).

## 15.2 Métriques opérationnelles

Les métriques de monitoring IA couvrent la performance (latence par requête, throughput, taux d’erreur, disponibilité), la qualité (taux d’hallucination mesuré par spot-check, satisfaction utilisateur, taux de correction des réponses), la sécurité (nombre de tentatives d’injection détectées, nombre de fuites détectées, nombre d’actions agent bloquées), le coût (coût par requête, coût par cas d’usage, tendance du coût dans le temps), et l’usage (volume de requêtes par utilisateur/groupe, heures d’utilisation, requêtes les plus fréquentes).

## 15.3 Détection d’abus

Les patterns suspects à surveiller incluent le volume anormal d’un utilisateur (extraction de données potentielle), les requêtes de type extraction (« liste tous les… », « donne-moi toutes les informations sur… »), les tentatives de jailbreak répétées (l’utilisateur essaie différentes formulations pour contourner les guardrails), les requêtes hors périmètre (un gestionnaire de sinistres qui pose des questions sur la comptabilité ou les RH), et les patterns temporels anormaux (requêtes à 3h du matin, weekend, vacances).

## 15.4 Intégration SIEM/SOAR

Les événements du système IA doivent alimenter le SIEM existant pour permettre la corrélation avec les autres logs de sécurité. Un jailbreak détecté sur l’assistant peut être corrélé avec une connexion suspecte sur l’AD. Une injection détectée dans un ticket peut être corrélée avec l’identité du soumetteur. Un pic de requêtes peut être corrélé avec une alerte DLP sur les flux sortants.

L’intégration se fait typiquement via syslog ou via une API de collecte (Splunk HEC, Elastic API). Les alertes SIEM spécifiques à l’IA doivent être définies : jailbreak détecté, fuite de données détectée, action agent bloquée par le kill switch, modification d’un document source du RAG, échec d’authentification sur l’API du modèle.

Le monitoring des coûts mérite une attention particulière : un pic de consommation (tokens, GPU) peut être un signe d’abus (un utilisateur qui extrait massivement des données), d’attaque (DoS par prompts complexes), ou simplement d’un usage inattendu à investiguer.

-----
