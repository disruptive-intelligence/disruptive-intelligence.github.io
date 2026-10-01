---
title: Ch.11 — Politique d’usage IA et gouvernance
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie III — Sécuriser le déploiement
  - index.md
---

## 11.1 La politique d’usage IA

La politique d’usage IA est le document fondateur de la gouvernance IA de l’entreprise. Elle n’est pas un document isolé — elle s’intègre dans la PSSI existante comme une extension couvrant les risques spécifiques de l’IA.

Son contenu minimum inclut le périmètre (quels systèmes IA sont couverts — internes, externes, shadow AI), la classification des données par type de modèle (quelles données peuvent être envoyées à un LLM cloud vs un LLM on-premise vs aucun LLM), les interdictions explicites (jamais de données de santé dans un LLM cloud sans DPA et HDS, jamais de credentials dans un prompt, jamais d’exécution de code généré par IA sans revue), les responsabilités (qui valide un nouveau cas d’usage IA, qui est responsable de la sécurité, qui est responsable de la conformité, qui assure le monitoring), les procédures de validation (gate de sécurité avant déploiement — voir Ch.14), et les sanctions (alignées avec le règlement intérieur).

La politique doit être pragmatique, pas prohibitive. Une politique qui interdit tout pousse au shadow AI. Une politique qui autorise sous conditions, avec des alternatives internes, est respectée.

## 11.2 La gouvernance IA

La gouvernance IA définit les rôles et les processus de décision. Les rôles clés sont le comité IA / sponsor (valide les cas d’usage, arbitre les budgets, assume le risque résiduel), le RSSI (évalue les risques, définit les exigences de sécurité, valide les architectures, pilote le monitoring — c’est le rôle de Karim), le DPO (évalue la conformité RGPD, pilote les AIPD, gère les droits des personnes), le ML Engineer / architecte IA (conçoit et déploie les systèmes, implémente les contrôles techniques), le métier (définit le besoin, valide la pertinence des résultats, assume la responsabilité de l’usage), et les utilisateurs finaux (utilisent le système dans le cadre de la politique, remontent les anomalies).

L’articulation avec la gouvernance SI existante est essentielle : le comité IA peut être un sous-comité du comité de sécurité existant, les revues de risques IA s’intègrent dans le processus de gestion des risques SSI, les incidents IA sont traités dans le processus de gestion des incidents existant.

## 11.3 KPI de gouvernance IA

Les indicateurs de pilotage incluent le nombre de cas d’usage IA déployés (vs demandés vs refusés), le taux de shadow AI résiduel, le nombre d’incidents IA (par type et par gravité), les coûts IA (par cas d’usage et au global), la satisfaction utilisateurs, la conformité (nombre d’AIPD réalisées vs requises, nombre de non-conformités identifiées), et la couverture de monitoring (pourcentage de systèmes IA avec un monitoring actif).

-----
