---
title: Chapitre 39 — Métriques, maturité et programme IR durable
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VIII — Post-incident, maturité et capitalisation
  - index.md
---

## 39.1 Métriques de performance IR

Les métriques clés pour évaluer et améliorer la capacité IR. Le **MTTD** (Mean Time To Detect) : délai entre la compromission initiale et la détection. Pour BLACKTIDE : 35 jours (l'infostealer est resté non détecté pendant 5 semaines) — un chiffre élevé qui révèle les failles de détection. Le **MTTC** (Mean Time To Contain) : délai entre la détection et le confinement effectif. Pour BLACKTIDE : environ 3 heures (de l'alerte EDR à la décision de confinement des 3 sites) — un chiffre honorable. Le **MTTR** (Mean Time To Recover) : délai entre le confinement et la reprise complète. Pour BLACKTIDE : 12 jours — un chiffre dans la norme pour un incident de cette ampleur.

Les métriques complémentaires incluent le taux de couverture EDR (92 % → objectif 100 %), la couverture des logs critiques (PowerShell logging activé sur les serveurs seulement → objectif : tout le parc), le pourcentage du parc sans Sysmon (100 % → objectif : 0 %), et la fréquence des exercices (1 tabletop en 18 mois → objectif : 1 tabletop trimestriel, 1 technique semestriel, 1 crise annuel).

## 39.2 Modèle de maturité IR

5 niveaux de maturité pour auto-évaluation :

**Niveau 1 — Réactif ad hoc :** Pas de processus formalisé. L'équipe IT improvise quand un incident survient. Pas d'IRP, pas de playbooks, pas de PRIS sous contrat.

**Niveau 2 — Processus défini :** Un IRP existe, les rôles sont attribués, un PRIS est sous contrat. Mais l'IRP n'est pas testé, les playbooks sont incomplets, les logs sont partiels. C'est le niveau d'Arvantis avant BLACKTIDE.

**Niveau 3 — Outillage intégré :** EDR à 100 %, SIEM avec logs complets, playbooks testés, exercices réguliers, PRIS avec SLA validé. La capacité IR fonctionne en cas d'incident mais n'est pas proactive.

**Niveau 4 — Capacité proactive :** Threat hunting régulier, purple team, exercices de crise avec la direction, métriques suivies, amélioration continue post-incidents et post-exercices. C'est l'objectif d'Arvantis à 18 mois.

**Niveau 5 — Résilience systémique :** L'IR est intégré dans la culture de l'organisation. La direction participe activement aux exercices. Les boucles de rétroaction SOC → IR → CTI → Prévention fonctionnent. Le programme IR est budgété, staffé, et évalué annuellement.

## 39.3 Construire un programme IR durable

Un programme IR durable repose sur une équipe dimensionnée et formée (formation continue SANS/GIAC, participation aux communautés FIRST/InterCERT), un budget pérenne (investissement initial + fonctionnement annuel — le budget IR ne doit pas être une ligne « exceptionnelle » supprimée l'année suivante), un outillage maintenu (EDR, SIEM, NDR, SOAR, outils forensic — mis à jour, calibrés, testés), des contrats à jour (PRIS, assurance, exercices), une astreinte organisée (rotation, compensation, formation des astreinteurs), un entraînement régulier (exercices progressifs, participation à des CTF, sessions de retex avec d'autres organisations), et une amélioration continue (chaque incident, chaque exercice, chaque retex alimente un plan de progrès suivi trimestriellement).

L'intégration des boucles de rétroaction entre disciplines est l'indicateur de maturité le plus avancé : le SOC alimente l'IR (détection → escalade), l'IR alimente le forensic (questions → investigation), le forensic alimente la CTI (artefacts → attribution → renseignement), la CTI alimente le SOC (IoC → règles de détection), et l'IR alimente la gestion de crise (situation technique → décisions stratégiques). Le programme IR durable organise ces boucles explicitement.

---
