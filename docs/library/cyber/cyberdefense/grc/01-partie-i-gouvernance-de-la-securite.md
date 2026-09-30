---
title: Partie I — Gouvernance de la sécurité
source: Cyber/05_Cyberdefense/GRC.md
note: GRC
up:
- - GRC
  - index.md
---

*Avant de gérer les risques ou d'auditer la conformité : structurer la gouvernance — qui décide quoi, avec quels moyens, dans quel cadre.*

---


## Chapitre 1 — Introduction : pourquoi la GRC existe

### 1.1 Le constat : la technique seule ne suffit pas

On peut avoir les meilleurs firewalls, le SIEM le plus cher et l'EDR le plus avancé — et se faire compromettre par un prestataire non audité, un processus de patching inexistant, un employé qui clique sur un phishing, ou un bucket S3 public oublié. La technique est nécessaire, pas suffisante. Les incidents les plus coûteux ne viennent pas d'un manque de technologie mais d'un manque de gouvernance : pas de classification des données (on ne sait pas ce qui est critique), pas de gestion des tiers (le prestataire a un accès admin non surveillé), pas de plan de réponse (personne ne sait quoi faire le jour J), pas de revue des accès (les comptes fantômes s'accumulent).

Le cours GRC donne le cadre qui permet à la technique d'être efficace. Sans ce cadre, les investissements techniques sont dispersés, les risques sont mal priorisés, et les incidents sont gérés dans le chaos.

### 1.2 Les trois piliers

**Gouvernance :** qui décide quoi ? Comment on organise la sécurité ? La gouvernance définit la politique (PSSI), les rôles et responsabilités (RACI), les comités (comité de sécurité, revue de direction), le budget, et la stratégie. Sans gouvernance, personne ne sait qui est responsable de quoi, et les décisions sont prises au cas par cas sans cohérence.

**Risques :** qu'est-ce qui peut mal tourner ? Comment on priorise ? La gestion des risques identifie les menaces, évalue leur vraisemblance et leur impact, et définit les actions à mener. Sans gestion des risques, on investit au hasard — 100 K€ sur un WAF alors qu'il n'y a pas de MFA sur les comptes admin.

**Conformité :** quelles obligations légales et réglementaires doit-on respecter ? La conformité assure le respect du RGPD, de NIS 2, de PCI-DSS, de HDS, de DORA, et des textes applicables. Sans conformité, l'organisation s'expose à des sanctions financières, des poursuites, et une perte de confiance.

Ces trois piliers s'alimentent mutuellement : l'analyse de risques guide la sélection des contrôles, la conformité impose des exigences minimales, et la gouvernance arbitre les priorités et alloue les ressources.

### 1.3 Risk ≠ Compliance ≠ Security

Trois concepts distincts, souvent confondus. La **conformité** est une obligation minimale — cocher les cases d'un référentiel. On peut être 100 % conforme et se faire pirater le lendemain : si les contrôles sont formels (la politique existe) mais pas effectifs (personne ne l'applique), la conformité est un leurre. La **sécurité** est la gestion du risque réel — protéger les actifs contre les menaces concrètes, au-delà des cases à cocher. Le **risque** est une décision business — accepter un risque est une décision de la direction, documentée et signée, pas un oubli.

La conformité sans sécurité est un leurre. La sécurité sans gouvernance est fragile. Le risque sans décision formelle est de la négligence.

### 1.4 La sécurité vue du COMEX

Le COMEX ne parle pas en CVE et en IoC — il parle en risques business, en coût, en impact sur le chiffre d'affaires, et en conformité réglementaire. Un RSSI qui présente « 47 vulnérabilités critiques » sera ignoré. Un RSSI qui présente « un risque de ransomware estimé à 2 M€ d'arrêt de production, réductible à un risque résiduel acceptable avec 80 K€ d'investissement » sera écouté. Le langage business est la compétence n°1 du RSSI — et c'est celle que ce cours enseigne.

### 1.5 Les rôles clés

Le **RSSI / CISO** pilote la sécurité de l'information — rattaché à la DSI (le plus courant) ou à la direction générale (le plus efficace). Le **DPO** protège les données personnelles (exigence RGPD — indépendant). Le **Risk Manager** gère les risques de l'entreprise au sens large (pas seulement cyber). Le **Compliance Officer** assure la conformité réglementaire. Dans une ETI comme Néoforma, le RSSI porte souvent plusieurs de ces casquettes — c'est un défi mais c'est la réalité.

### 1.6 Fil rouge — COMPLIANCE : l'état des lieux

> **📊 COMPLIANCE — Épisode 1**
>
> Marine arrive chez Néoforma. Premier jour : tour du SI. Pas de PSSI. Pas d'analyse de risques. Pas de comité de sécurité. L'antivirus est géré par la DSI entre deux tickets helpdesk. Les sauvegardes sont sur un NAS dans la même salle serveur (pas de 3-2-1, pas de test de restauration depuis 18 mois). 5 SaaS souscrits par les métiers sans validation IT, dont un stockant des données patients. L'hébergeur du datacenter n'est pas certifié HDS — ce qui est une non-conformité réglementaire immédiate.
>
> Marine rédige sa note au DG : « Nous avons un risque de sanction CNIL, un risque de perte de clients CHU (qui exigent ISO 27001), et un risque de ransomware non couvert. Budget demandé : 400 K€/an. ROI : éviter 2 M€+ de pertes potentielles et conserver nos 3 plus gros clients. »

---


## Chapitre 2 — Cadres et référentiels : la carte du territoire

### 2.1 Vue d'ensemble

Chaque référentiel répond à un besoin différent. Le choix dépend du contexte : taille, secteur, obligations, maturité.

**ISO 27001** est le standard international de certification d'un SMSI (Système de Management de la Sécurité de l'Information). Structure en 10 clauses (contexte → leadership → planification → support → fonctionnement → évaluation → amélioration). Le cycle PDCA (Plan-Do-Check-Act) est le moteur du SMSI. La certification (Phase 1 documentaire + Phase 2 terrain, surveillance annuelle, recertification 3 ans) prouve la maturité — exigée de plus en plus par les grands clients et les appels d'offres. ISO 27001 exige le « quoi », pas le « comment » — la liberté d'implémentation est totale tant que le résultat est démontrable.

**ISO 27002** (version 2022) est le catalogue de 93 mesures de sécurité en 4 thèmes (organisationnelles — 37, humaines — 8, physiques — 14, technologiques — 34). La sélection des mesures est guidée par l'analyse de risques et documentée dans la DdA/SoA (Ch.14).

**NIST CSF v2.0** (Cybersecurity Framework, 2024) structure le programme de sécurité en 6 fonctions : Govern (nouveau en v2.0), Identify, Protect, Detect, Respond, Recover. Auto-évaluation par tiers (Partial → Risk Informed → Repeatable → Adaptive). Les profiles (état actuel vs état cible) guident la feuille de route.

**CIS Controls v8** : 18 contrôles priorisés en 3 niveaux d'implémentation (IG1 — hygiène de base pour toutes les organisations, IG2 — protection renforcée, IG3 — maturité avancée). IG1 est la rampe de démarrage parfaite pour une organisation qui part de zéro.

**ANSSI** : le guide d'hygiène (42 mesures — le socle français), EBIOS RM (méthode d'analyse de risques — Ch.7), les qualifications (SecNumCloud, PASSI, PDIS), et les guides sectoriels.

**MITRE ATT&CK vu GRC** : mapper les contrôles de sécurité sur les techniques d'attaque permet d'identifier les lacunes — c'est le pont entre la GRC et le SOC (le cours SOC utilise ATT&CK pour la détection, le cours GRC l'utilise pour la couverture des contrôles).

### 2.2 Comment choisir

L'arbre de décision : obligation contractuelle de certification → ISO 27001. Secteur financier UE → DORA + ISO 27001. Données de santé France → HDS + RGPD. Secteur public France → RGS + EBIOS RM. Démarrage rapide sans certification → CIS Controls IG1 + NIST CSF. En pratique, la plupart des organisations combinent plusieurs référentiels : ISO 27001 comme cadre de certification, CIS Controls comme quick wins, EBIOS RM pour l'analyse de risques, et NIST CSF pour le reporting.

---


## Chapitre 3 — La PSSI : rédiger et faire vivre la politique de sécurité

### 3.1 Le document fondateur

La PSSI (Politique de Sécurité des Systèmes d'Information) est le « contrat social » de la sécurité dans l'organisation. Elle formalise l'engagement de la direction, les principes directeurs, les règles applicables à tous, et l'organisation de la sécurité. Sans PSSI, il n'y a pas de référence — chacun fait ce qu'il pense être bien, sans cohérence ni autorité.

### 3.2 Structure type

**Contexte et périmètre** : quels systèmes, quelles données, quelles entités sont couverts. **Engagement de la direction** : la signature du DG n'est pas un détail — c'est l'acte qui donne autorité au RSSI et engage l'entreprise. **Objectifs de sécurité** : ce que l'organisation veut protéger (disponibilité, confidentialité, intégrité) et pourquoi. **Principes directeurs** : défense en profondeur, moindre privilège, séparation des devoirs, besoin d'en connaître, security by design. **Organisation et responsabilités** : RACI — qui est responsable de quoi (le RSSI, la DSI, les métiers, les utilisateurs). **Classification des données** : les 4 niveaux et les mesures associées (renvoi Ch.5). **Règles par domaine** : accès (politique MdP, MFA, revue), réseau (segmentation, flux, VPN), endpoint (EDR, chiffrement, politique BYOD), cloud (fournisseurs autorisés, classification), données (chiffrement, rétention, destruction), tiers (PAS, questionnaire, droit d'audit), incidents (processus, contacts, notification), continuité (PCA/PRA, tests). **Gestion des exceptions** : processus formel pour les dérogations (Ch.14). **Sanctions** : les conséquences du non-respect. **Revue** : fréquence de mise à jour (annuelle minimum, après tout changement majeur).

### 3.3 La hiérarchie documentaire

La PSSI est le sommet de la pyramide. En dessous : les **politiques thématiques** (politique d'accès, politique de sauvegarde, politique de gestion des tiers — chacune détaille un domaine de la PSSI). Puis les **procédures** (comment faire concrètement — procédure de revue des accès, procédure de notification d'incident). Puis les **guides techniques** (configurations, standards techniques). Chaque niveau est de plus en plus détaillé et de plus en plus technique.

### 3.4 Faire vivre la PSSI

Une PSSI dans un tiroir est pire qu'une absence de PSSI — elle crée l'illusion de gouvernance. Pour la faire vivre : la diffuser (pas juste un email — formation dédiée, intégration dans l'onboarding, rappels réguliers), la référencer (chaque procédure, chaque exception, chaque décision de sécurité renvoie à la PSSI), la maintenir (revue annuelle minimum, mise à jour après chaque incident significatif, changement d'architecture, ou nouvelle réglementation), et la rendre accessible (intranet, pas un SharePoint oublié).

---


## Chapitre 4 — Gouvernance opérationnelle : comités, rôles et reporting

### 4.1 Le comité de sécurité

Le comité de sécurité est l'instance de pilotage. Composition : RSSI (pilote), DSI (moyens), DPO (données personnelles), représentants métiers (besoins), direction (arbitrage). Fréquence : mensuel ou trimestriel selon la maturité. Ordre du jour type : revue des risques (registre, évolutions, nouveaux risques), incidents (résumé, retex, actions correctives), indicateurs (dashboard opérationnel — Ch.9), avancement du PTR (plan de traitement des risques), budget (consommation, demandes), exceptions (nouvelles, expirées, à renouveler), et sujets à arbitrer.

### 4.2 Le reporting au COMEX

Le reporting stratégique au COMEX suit une règle d'or : pas de CVE, pas de CVSS, pas de jargon. Le format : 3 à 5 indicateurs clés (tendances, couleurs, comparaison avec les objectifs), les risques majeurs (en termes d'impact business — perte de CA, amende, perte de clients), le coût du traitement vs le coût de l'incident (le langage du ROI), et les décisions demandées (budget, arbitrage, validation d'une acceptation de risque). La fréquence : trimestriel, avec des alertes flash si incident significatif.

### 4.3 Fil rouge — COMPLIANCE : la gouvernance installée

> **📊 COMPLIANCE — Épisode 2**
>
> Marine installe la gouvernance en M1-M2. PSSI rédigée (15 pages, signée par le DG), comité de sécurité mensuel lancé (RSSI, DSI, DPO désigné, directeur R&D, directeur commercial), RACI sécurité défini, et premier reporting COMEX (3 risques rouges, 12 contrôles non implémentés, taux de clic phishing à 34 %, hébergeur non certifié HDS). La direction débloque le budget de 400 K€.

---


## Chapitre 5 — Inventaire des actifs, classification et propriété

On ne protège pas ce qu'on ne connaît pas. L'inventaire des actifs (matériels — serveurs, postes, équipements réseau ; logiciels — applications, SaaS, licences ; données — bases, fichiers, flux ; services cloud — IaaS, PaaS, SaaS ; et personnes clés — les détenteurs de savoir-faire critique) est le fondement de toute démarche de sécurité. La CMDB (Configuration Management Database) est l'outil de référence.

La classification des données en 4 niveaux : **C0 — Public** (aucun impact si divulgué — site web, brochures ; aucune restriction), **C1 — Interne** (impact limité — procédures, org. interne ; accès authentifié), **C2 — Confidentiel** (impact significatif — données clients, finances ; chiffrement, accès restreint), **C3 — Secret** (impact critique — données de santé, stratégie, brevets ; chiffrement fort, traçabilité, besoin d'en connaître strict). Qui classifie : le propriétaire des données (le métier, pas l'IT — le directeur commercial classifie les données commerciales, le directeur R&D classifie les données de recherche).

Le Shadow IT : les SaaS souscrits par les métiers sans validation IT sont un angle mort majeur. Détection : CASB (Cloud Access Security Broker), analyse DNS, revue des dépenses par carte bancaire.

---
