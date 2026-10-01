---
title: Chapitre 20 — Politique de gestion des vulnérabilités
source: Cyber/08 Gouvernance & résilience/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - ../index.md
- - Partie IV — Sécurité opérationnelle vue GRC
  - index.md
---

du score brut au score contextualisé

La gestion des vulnérabilités est un processus de gouvernance avant d'être un processus technique. Le scanner de vulnérabilités (Qualys, Nessus, Rapid7) produit des centaines de findings par semaine, chacun accompagné d'un score CVSS Base (v3.1 ou v4.0). Sans politique de contextualisation, le résultat est prévisible : tout est « critique », les équipes sont saturées, et les vraies urgences se noient dans le bruit. La politique de gestion des vulnérabilités définit les règles du jeu — quel framework de scoring est utilisé, comment le score est contextualisé, qui a l'autorité de re-qualifier, et quels SLA s'appliquent par niveau contextualisé.

## 20.1 Le problème du score Base brut

Le score CVSS Base est **générique** — il décrit la vulnérabilité dans l'absolu, indépendamment de l'environnement de l'organisation. Il ne tient compte ni de l'exposition réelle de l'actif (Internet vs réseau interne vs segment isolé), ni des contrôles compensatoires en place (WAF, segmentation, MFA, EDR), ni de la criticité métier de l'actif (un serveur de test et un serveur de production financière ne méritent pas le même SLA de traitement), ni de l'état d'exploitation (un exploit théorique et un exploit utilisé activement in-the-wild ne représentent pas le même risque).

Le rôle de la gouvernance est de transformer ce score brut en un score actionnable qui reflète la réalité de l'organisation. C'est un acte de pilotage GRC : le GRC définit la politique, le SOC et les équipes techniques l'appliquent.

## 20.2 CVSS v4.0 : la structure qui supporte la politique

CVSS v4.0 (FIRST, fin 2023, supporté par le NVD depuis 2024) apporte une structure de scoring en quatre groupes de métriques conçue pour la contextualisation :

Le groupe **Base** mesure la sévérité intrinsèque (vecteur d'attaque, complexité, privilèges requis, interaction utilisateur, impacts CIA). Le groupe **Threat** (remplace le « Temporal » de v3.1) intègre l'état d'exploitation réel via Exploit Maturity (Unreported — pas d'exploitation connue, PoC — preuve de concept publique, Attacked — exploitation confirmée in-the-wild). Le groupe **Environmental** permet d'adapter le score au contexte de l'organisation (Modified Attack Vector — le service est-il réellement exposé ?, Modified Privileges Required — des contrôles compensent-ils ?, Security Requirements CIA — la criticité métier de l'actif). Le groupe **Supplemental** (nouveau en v4 — Safety, Automatable, Recovery, Value Density, Provider Urgency) enrichit la contextualisation sans modifier le score numérique.

CVSS v4 produit des scores différenciés : **CVSS-B** (Base seul), **CVSS-BT** (Base + Threat), **CVSS-BE** (Base + Environmental), **CVSS-BTE** (Base + Threat + Environmental). Cette nomenclature force la transparence — le rapport de vulnérabilités doit indiquer quel niveau de contextualisation a été appliqué.

## 20.3 Ce que la politique de gestion des vulnérabilités doit définir

La politique GRC doit répondre à sept questions :

(1) **Quel framework de scoring ?** CVSS v3.1 reste utilisé dans de nombreuses bases (NVD historique, scanners), mais la transition vers CVSS v4.0 est recommandée — le NVD supporte les deux. La politique peut imposer le rescoring en v4 pour toutes les vulnérabilités au-dessus d'un seuil (ex : tout CVSS-B ≥ 7.0 doit être re-scoré en v4 avec les métriques Threat + Environmental).

(2) **Qui a l'autorité de re-qualifier ?** Le rescoring contextuel n'est pas un acte anodin — re-qualifier un 9.8 en 5.5 doit être tracé, justifié, et validé. La politique doit désigner qui peut re-qualifier (le SOC manager, le RSSI, le vulnerability manager) et exiger une justification documentée pour chaque re-qualification significative (baisse de plus de 2 points par rapport au score Base).

(3) **Quelles métriques Environmental sont appliquées ?** La politique doit définir les règles d'application des métriques environnementales : comment est déterminé le Modified Attack Vector (cartographie de l'exposition — la CMDB doit indiquer si l'actif est exposé sur Internet), comment sont évalués les contrôles compensatoires (une matrice de correspondance entre les contrôles en place et les Modified Metrics CVSS), et comment est déterminée la criticité métier (les Security Requirements CIA sont dérivées de la classification des actifs — un actif classé « critique » dans la cartographie des risques a des Security Requirements High).

(4) **Comment est intégrée la métrique Threat ?** Le SOC et le CTI alimentent l'Exploit Maturity : si la CVE est dans le KEV (Known Exploited Vulnerabilities) de la CISA, ou si le CTI interne observe une exploitation active, l'Exploit Maturity passe à « Attacked » → le score CVSS-BT monte, la priorité de traitement aussi.

(5) **Quels SLA par score contextualisé ?** Les SLA de traitement sont définis sur le score contextualisé (CVSS-BTE), pas sur le score Base brut. Exemple : CVSS-BTE ≥ 9.0 = P0 (24-48h), 7.0-8.9 = P1 (7 jours), 4.0-6.9 = P2 (30 jours), < 4.0 = P3 (90 jours ou risque accepté). Sans cette distinction, les SLA sont basés sur le score Base → tout est P0 → les équipes sont saturées → rien n'est traité en temps.

(6) **Comment est documenté le rescoring ?** Chaque rescoring doit être tracé : CVE, score Base original (source — éditeur/NVD), score contextuel interne (CVSS-BTE), justification des métriques Environmental appliquées, date du rescoring, et auteur. Cette traçabilité est indispensable pour l'audit (ISO 27001 A.12.6, NIS2) et pour le retex post-incident (si un incident exploite une vulnérabilité re-qualifiée à la baisse, le retex doit analyser si la re-qualification était justifiée).

(7) **Quelle est l'articulation avec la gravité des incidents ?** Le rescoring CVSS contextuel et la qualification de gravité IR (P1/P2/P3/P4) sont deux évaluations distinctes. Le CVSS contextuel évalue la sévérité de la vulnérabilité dans l'environnement. La gravité IR évalue l'impact de l'incident sur l'organisation. Les deux se nourrissent (une vulnérabilité avec un CVSS-BTE élevé exploitée activement alimente une gravité IR élevée), mais elles ne sont pas interchangeables. La politique doit le stipuler explicitement pour éviter les confusions opérationnelles.

## 20.4 Articulation avec les référentiels

**ISO 27001** (A.12.6 — Gestion des vulnérabilités techniques) : la norme exige que les vulnérabilités soient évaluées et traitées en fonction du risque pour l'organisation. Le rescoring contextuel CVSS v4 est un moyen concret de satisfaire cette exigence — il documente l'évaluation du risque spécifique à l'environnement, pas seulement le score générique.

**EBIOS RM** : la méthode d'analyse de risque française intègre les scénarios opérationnels (quelles vulnérabilités, exploitées par quels acteurs, avec quel impact). Le rescoring CVSS v4 alimente ces scénarios — l'Exploit Maturity (Threat) reflète la capacité de l'acteur, les Modified Metrics (Environmental) reflètent l'exposition du système, et le score résultant alimente l'évaluation de la vraisemblance.

**NIS2** : la directive impose une gestion des vulnérabilités proportionnée. Le rescoring contextuel documente cette proportionnalité — un auditeur qui voit un CVSS-B 9.8 non traité en 7 jours posera la question. Si la réponse est « le CVSS-BTE est 4.2 parce que le service est isolé, compensé par un WAF, et ne traite pas de données critiques — voici la documentation », c'est une réponse de gouvernance mature.

## 20.5 En résumé

| Composante | Responsable | Ce qu'elle produit |
|-----------|-------------|-------------------|
| Score CVSS-B (éditeur/NVD) | Externe (éditeur, NVD) | Score générique de référence |
| Rescoring CVSS-BTE contextuel | Vulnerability manager (sous politique GRC) | Score adapté à l'environnement réel |
| SLA de traitement | GRC (politique de gestion des vulnérabilités) | Délai de remédiation par niveau contextualisé |
| Gravité IR (P1-P4) | SOC / IR (sous politique de gestion des incidents) | Niveau de mobilisation et d'escalade |

La politique de gestion des vulnérabilités est le pont entre la gouvernance (GRC) et l'opérationnel (SOC, IT, DevOps). Le rescoring contextuel CVSS v4 est l'outil qui rend ce pont concret et auditable.

---
