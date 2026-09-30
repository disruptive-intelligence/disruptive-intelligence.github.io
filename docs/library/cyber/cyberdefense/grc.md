---
title: GRC
source: Cyber/05_Cyberdefense/GRC.md
---

*Le cadre qui donne sens à la technique*

**Cours complet — 31 chapitres • 7 parties • 7 annexes**

*Gouvernance • Analyse de risques • Conformité • Résilience • Maturité*

---

## Table des matières

- [Fil rouge : Opération COMPLIANCE](#fil-rouge-operation-compliance)
- **PARTIE I — GOUVERNANCE DE LA SÉCURITÉ (Ch.1-5)**
  - [Ch.1 — Introduction : pourquoi la GRC existe](#chapitre-1-introduction-pourquoi-la-grc-existe)
  - [Ch.2 — Cadres et référentiels](#chapitre-2-cadres-et-referentiels-la-carte-du-territoire)
  - [Ch.3 — La PSSI : rédiger et faire vivre la politique de sécurité](#chapitre-3-la-pssi-rediger-et-faire-vivre-la-politique-de-securite)
  - [Ch.4 — Gouvernance opérationnelle : comités, rôles et reporting](#chapitre-4-gouvernance-operationnelle-comites-roles-et-reporting)
  - [Ch.5 — Inventaire des actifs, classification et propriété](#chapitre-5-inventaire-des-actifs-classification-et-propriete)
- **PARTIE II — GESTION DES RISQUES (Ch.6-9)**
  - [Ch.6 — Concepts fondamentaux du risque](#chapitre-6-concepts-fondamentaux-du-risque)
  - [Ch.7 — Méthodologies d'analyse de risques](#chapitre-7-methodologies-danalyse-de-risques)
  - [Ch.8 — Analyse de risques en pratique : walkthrough EBIOS RM](#chapitre-8-analyse-de-risques-en-pratique-walkthrough-ebios-rm-complet)
  - [Ch.9 — Indicateurs, tableaux de bord et amélioration continue](#chapitre-9-indicateurs-tableaux-de-bord-et-amelioration-continue)
- **PARTIE III — CONFORMITÉ RÉGLEMENTAIRE (Ch.10-15)**
  - [Ch.10 — RGPD : obligations et articulation sécurité](#chapitre-10-rgpd-obligations-et-articulation-securite)
  - [Ch.11 — NIS 2 : la directive qui change tout](#chapitre-11-nis-2-la-directive-qui-change-tout)
  - [Ch.12 — DORA et réglementations sectorielles](#chapitre-12-dora-et-reglementations-sectorielles)
  - [Ch.13 — Audits et certification ISO 27001](#chapitre-13-audits-et-certification-iso-27001)
  - [Ch.14 — Déclaration d'applicabilité et gestion des exceptions](#chapitre-14-declaration-dapplicabilite-et-gestion-des-exceptions)
  - [Ch.15 — Homologation de sécurité : décider, documenter, maintenir](#chapitre-15-homologation-de-securite-decider-documenter-maintenir)
- **PARTIE IV — SÉCURITÉ OPÉRATIONNELLE VUE GRC (Ch.16-19)**
  - [Ch.16 — Gestion des identités et des accès vue GRC](#chapitre-16-gestion-des-identites-et-des-acces-vue-grc)
  - [Ch.17 — Sensibilisation : construire un programme efficace](#chapitre-17-sensibilisation-construire-un-programme-qui-change-les-comportements)
  - [Ch.18 — Pilotage du changement, des vulnérabilités et du patching](#chapitre-18-pilotage-du-changement-des-vulnerabilites-et-du-patching)
  - [Ch.19 — Sécurité contractuelle et juridique](#chapitre-19-referentiels-vulnerabilites-utiles-a-la-gouvernance-cve-cwe-cvss-epss-kev)
- **PARTIE V — RÉSILIENCE ET CONTINUITÉ (Ch.20-23)**
  - [Ch.20 — Gestion des incidents de sécurité vue GRC](#chapitre-20--incidents-vue-grc)
  - [Ch.21 — Continuité (PCA) et reprise (PRA)](#chapitre-21-securite-contractuelle-et-juridique)
  - [Ch.22 — Gestion de crise cyber](#chapitre-22-gestion-des-incidents-de-securite-vue-grc)
  - [Ch.23 — Assurance cyber et transfert de risque](#chapitre-23-continuite-pca-et-reprise-pra)
- **PARTIE VI — GESTION DES TIERS ET CLOUD (Ch.24-25)**
  - [Ch.24 — Gouvernance des tiers : évaluation, scoring et surveillance](#chapitre-24-gestion-de-crise-cyber)
  - [Ch.25 — Cloud, souveraineté et conformité](#chapitre-25-assurance-cyber-et-transfert-de-risque)
- **PARTIE VII — MATURITÉ, PROGRAMME ET CAS DE SYNTHÈSE (Ch.26-31)**
  - [Ch.26 — Construire un programme de sécurité](#chapitre-26-gouvernance-des-tiers-evaluation-scoring-et-surveillance)
  - [Ch.27 — Modèles de maturité et amélioration continue](#chapitre-27-cloud-souverainete-et-conformite)
  - [Ch.28 — GRC et cybersécurité opérationnelle : la convergence](#chapitre-28-construire-un-programme-de-securite)
  - [Ch.29 — Cas complet : construction d'un programme de sécurité de 0](#chapitre-29-modeles-de-maturite-et-amelioration-continue)
  - [Ch.30 — Cas complet : gestion de crise ransomware](#chapitre-30-grc-et-cybersecurite-operationnelle-la-convergence)
  - [Ch.31 — Cas complet : mise en conformité NIS 2](#chapitre-31-cas-complet-construction-dun-programme-de-securite-de-0-synthese-compliance)
- **ANNEXES**

---

## Fil rouge : Opération COMPLIANCE

> **Contexte narratif — ce fil rouge traverse les 28 premiers chapitres et se conclut au Ch.29.**
>
> **Marine Vasseur**, nommée RSSI de **Néoforma** — ETI française de 1 200 collaborateurs, éditeur de logiciels SaaS pour le secteur médical (gestion de dossiers patients, télémédecine, facturation), 45 M€ de CA, hébergement cloud hybride (Azure + datacenter propre à Nantes), 200 clients (hôpitaux, cliniques, cabinets), données de santé de 3 millions de patients — arrive dans une organisation qui n'a jamais eu de RSSI.
>
> La DSI gérait « la sécurité » en parallèle du reste : un firewall Fortinet, un antivirus sur les postes, des sauvegardes « quelque part sur un NAS », pas de politique de sécurité formalisée, pas d'analyse de risques, pas de classification des données, pas de gestion des tiers structurée, pas de plan de continuité testé, et 15 comptes « admin temporaire » créés il y a 2 ans toujours actifs.
>
> Marine a **18 mois** pour construire le programme de sécurité : structurer la gouvernance, conduire l'analyse de risques, mettre en conformité (RGPD pour les données de santé, HDS pour l'hébergement, NIS 2 car Néoforma est fournisseur de services numériques pour le secteur santé), préparer la certification ISO 27001 (exigée par les CHU clients), gérer les tiers (3 sous-traitants critiques dont l'hébergeur non certifié HDS), construire la résilience, et obtenir l'homologation des SI sensibles. Budget : 400 K€/an. Équipe : 3 personnes (Marine + 1 consultant GRC + 1 analyste sécurité).

---

## PARTIE I — GOUVERNANCE DE LA SÉCURITÉ

*Avant de gérer les risques ou d'auditer la conformité : structurer la gouvernance — qui décide quoi, avec quels moyens, dans quel cadre.*

---

### Chapitre 1 — Introduction : pourquoi la GRC existe

#### 1.1 Le constat : la technique seule ne suffit pas

On peut avoir les meilleurs firewalls, le SIEM le plus cher et l'EDR le plus avancé — et se faire compromettre par un prestataire non audité, un processus de patching inexistant, un employé qui clique sur un phishing, ou un bucket S3 public oublié. La technique est nécessaire, pas suffisante. Les incidents les plus coûteux ne viennent pas d'un manque de technologie mais d'un manque de gouvernance : pas de classification des données (on ne sait pas ce qui est critique), pas de gestion des tiers (le prestataire a un accès admin non surveillé), pas de plan de réponse (personne ne sait quoi faire le jour J), pas de revue des accès (les comptes fantômes s'accumulent).

Le cours GRC donne le cadre qui permet à la technique d'être efficace. Sans ce cadre, les investissements techniques sont dispersés, les risques sont mal priorisés, et les incidents sont gérés dans le chaos.

#### 1.2 Les trois piliers

**Gouvernance :** qui décide quoi ? Comment on organise la sécurité ? La gouvernance définit la politique (PSSI), les rôles et responsabilités (RACI), les comités (comité de sécurité, revue de direction), le budget, et la stratégie. Sans gouvernance, personne ne sait qui est responsable de quoi, et les décisions sont prises au cas par cas sans cohérence.

**Risques :** qu'est-ce qui peut mal tourner ? Comment on priorise ? La gestion des risques identifie les menaces, évalue leur vraisemblance et leur impact, et définit les actions à mener. Sans gestion des risques, on investit au hasard — 100 K€ sur un WAF alors qu'il n'y a pas de MFA sur les comptes admin.

**Conformité :** quelles obligations légales et réglementaires doit-on respecter ? La conformité assure le respect du RGPD, de NIS 2, de PCI-DSS, de HDS, de DORA, et des textes applicables. Sans conformité, l'organisation s'expose à des sanctions financières, des poursuites, et une perte de confiance.

Ces trois piliers s'alimentent mutuellement : l'analyse de risques guide la sélection des contrôles, la conformité impose des exigences minimales, et la gouvernance arbitre les priorités et alloue les ressources.

#### 1.3 Risk ≠ Compliance ≠ Security

Trois concepts distincts, souvent confondus. La **conformité** est une obligation minimale — cocher les cases d'un référentiel. On peut être 100 % conforme et se faire pirater le lendemain : si les contrôles sont formels (la politique existe) mais pas effectifs (personne ne l'applique), la conformité est un leurre. La **sécurité** est la gestion du risque réel — protéger les actifs contre les menaces concrètes, au-delà des cases à cocher. Le **risque** est une décision business — accepter un risque est une décision de la direction, documentée et signée, pas un oubli.

La conformité sans sécurité est un leurre. La sécurité sans gouvernance est fragile. Le risque sans décision formelle est de la négligence.

#### 1.4 La sécurité vue du COMEX

Le COMEX ne parle pas en CVE et en IoC — il parle en risques business, en coût, en impact sur le chiffre d'affaires, et en conformité réglementaire. Un RSSI qui présente « 47 vulnérabilités critiques » sera ignoré. Un RSSI qui présente « un risque de ransomware estimé à 2 M€ d'arrêt de production, réductible à un risque résiduel acceptable avec 80 K€ d'investissement » sera écouté. Le langage business est la compétence n°1 du RSSI — et c'est celle que ce cours enseigne.

#### 1.5 Les rôles clés

Le **RSSI / CISO** pilote la sécurité de l'information — rattaché à la DSI (le plus courant) ou à la direction générale (le plus efficace). Le **DPO** protège les données personnelles (exigence RGPD — indépendant). Le **Risk Manager** gère les risques de l'entreprise au sens large (pas seulement cyber). Le **Compliance Officer** assure la conformité réglementaire. Dans une ETI comme Néoforma, le RSSI porte souvent plusieurs de ces casquettes — c'est un défi mais c'est la réalité.

#### 1.6 Fil rouge — COMPLIANCE : l'état des lieux

> **📊 COMPLIANCE — Épisode 1**
>
> Marine arrive chez Néoforma. Premier jour : tour du SI. Pas de PSSI. Pas d'analyse de risques. Pas de comité de sécurité. L'antivirus est géré par la DSI entre deux tickets helpdesk. Les sauvegardes sont sur un NAS dans la même salle serveur (pas de 3-2-1, pas de test de restauration depuis 18 mois). 5 SaaS souscrits par les métiers sans validation IT, dont un stockant des données patients. L'hébergeur du datacenter n'est pas certifié HDS — ce qui est une non-conformité réglementaire immédiate.
>
> Marine rédige sa note au DG : « Nous avons un risque de sanction CNIL, un risque de perte de clients CHU (qui exigent ISO 27001), et un risque de ransomware non couvert. Budget demandé : 400 K€/an. ROI : éviter 2 M€+ de pertes potentielles et conserver nos 3 plus gros clients. »

---

### Chapitre 2 — Cadres et référentiels : la carte du territoire

#### 2.1 Vue d'ensemble

Chaque référentiel répond à un besoin différent. Le choix dépend du contexte : taille, secteur, obligations, maturité.

**ISO 27001** est le standard international de certification d'un SMSI (Système de Management de la Sécurité de l'Information). Structure en 10 clauses (contexte → leadership → planification → support → fonctionnement → évaluation → amélioration). Le cycle PDCA (Plan-Do-Check-Act) est le moteur du SMSI. La certification (Phase 1 documentaire + Phase 2 terrain, surveillance annuelle, recertification 3 ans) prouve la maturité — exigée de plus en plus par les grands clients et les appels d'offres. ISO 27001 exige le « quoi », pas le « comment » — la liberté d'implémentation est totale tant que le résultat est démontrable.

**ISO 27002** (version 2022) est le catalogue de 93 mesures de sécurité en 4 thèmes (organisationnelles — 37, humaines — 8, physiques — 14, technologiques — 34). La sélection des mesures est guidée par l'analyse de risques et documentée dans la DdA/SoA (Ch.14).

**NIST CSF v2.0** (Cybersecurity Framework, 2024) structure le programme de sécurité en 6 fonctions : Govern (nouveau en v2.0), Identify, Protect, Detect, Respond, Recover. Auto-évaluation par tiers (Partial → Risk Informed → Repeatable → Adaptive). Les profiles (état actuel vs état cible) guident la feuille de route.

**CIS Controls v8** : 18 contrôles priorisés en 3 niveaux d'implémentation (IG1 — hygiène de base pour toutes les organisations, IG2 — protection renforcée, IG3 — maturité avancée). IG1 est la rampe de démarrage parfaite pour une organisation qui part de zéro.

**ANSSI** : le guide d'hygiène (42 mesures — le socle français), EBIOS RM (méthode d'analyse de risques — Ch.7), les qualifications (SecNumCloud, PASSI, PDIS), et les guides sectoriels.

**MITRE ATT&CK vu GRC** : mapper les contrôles de sécurité sur les techniques d'attaque permet d'identifier les lacunes — c'est le pont entre la GRC et le SOC (le cours SOC utilise ATT&CK pour la détection, le cours GRC l'utilise pour la couverture des contrôles).

#### 2.2 Comment choisir

L'arbre de décision : obligation contractuelle de certification → ISO 27001. Secteur financier UE → DORA + ISO 27001. Données de santé France → HDS + RGPD. Secteur public France → RGS + EBIOS RM. Démarrage rapide sans certification → CIS Controls IG1 + NIST CSF. En pratique, la plupart des organisations combinent plusieurs référentiels : ISO 27001 comme cadre de certification, CIS Controls comme quick wins, EBIOS RM pour l'analyse de risques, et NIST CSF pour le reporting.

---

### Chapitre 3 — La PSSI : rédiger et faire vivre la politique de sécurité

#### 3.1 Le document fondateur

La PSSI (Politique de Sécurité des Systèmes d'Information) est le « contrat social » de la sécurité dans l'organisation. Elle formalise l'engagement de la direction, les principes directeurs, les règles applicables à tous, et l'organisation de la sécurité. Sans PSSI, il n'y a pas de référence — chacun fait ce qu'il pense être bien, sans cohérence ni autorité.

#### 3.2 Structure type

**Contexte et périmètre** : quels systèmes, quelles données, quelles entités sont couverts. **Engagement de la direction** : la signature du DG n'est pas un détail — c'est l'acte qui donne autorité au RSSI et engage l'entreprise. **Objectifs de sécurité** : ce que l'organisation veut protéger (disponibilité, confidentialité, intégrité) et pourquoi. **Principes directeurs** : défense en profondeur, moindre privilège, séparation des devoirs, besoin d'en connaître, security by design. **Organisation et responsabilités** : RACI — qui est responsable de quoi (le RSSI, la DSI, les métiers, les utilisateurs). **Classification des données** : les 4 niveaux et les mesures associées (renvoi Ch.5). **Règles par domaine** : accès (politique MdP, MFA, revue), réseau (segmentation, flux, VPN), endpoint (EDR, chiffrement, politique BYOD), cloud (fournisseurs autorisés, classification), données (chiffrement, rétention, destruction), tiers (PAS, questionnaire, droit d'audit), incidents (processus, contacts, notification), continuité (PCA/PRA, tests). **Gestion des exceptions** : processus formel pour les dérogations (Ch.14). **Sanctions** : les conséquences du non-respect. **Revue** : fréquence de mise à jour (annuelle minimum, après tout changement majeur).

#### 3.3 La hiérarchie documentaire

La PSSI est le sommet de la pyramide. En dessous : les **politiques thématiques** (politique d'accès, politique de sauvegarde, politique de gestion des tiers — chacune détaille un domaine de la PSSI). Puis les **procédures** (comment faire concrètement — procédure de revue des accès, procédure de notification d'incident). Puis les **guides techniques** (configurations, standards techniques). Chaque niveau est de plus en plus détaillé et de plus en plus technique.

#### 3.4 Faire vivre la PSSI

Une PSSI dans un tiroir est pire qu'une absence de PSSI — elle crée l'illusion de gouvernance. Pour la faire vivre : la diffuser (pas juste un email — formation dédiée, intégration dans l'onboarding, rappels réguliers), la référencer (chaque procédure, chaque exception, chaque décision de sécurité renvoie à la PSSI), la maintenir (revue annuelle minimum, mise à jour après chaque incident significatif, changement d'architecture, ou nouvelle réglementation), et la rendre accessible (intranet, pas un SharePoint oublié).

---

### Chapitre 4 — Gouvernance opérationnelle : comités, rôles et reporting

#### 4.1 Le comité de sécurité

Le comité de sécurité est l'instance de pilotage. Composition : RSSI (pilote), DSI (moyens), DPO (données personnelles), représentants métiers (besoins), direction (arbitrage). Fréquence : mensuel ou trimestriel selon la maturité. Ordre du jour type : revue des risques (registre, évolutions, nouveaux risques), incidents (résumé, retex, actions correctives), indicateurs (dashboard opérationnel — Ch.9), avancement du PTR (plan de traitement des risques), budget (consommation, demandes), exceptions (nouvelles, expirées, à renouveler), et sujets à arbitrer.

#### 4.2 Le reporting au COMEX

Le reporting stratégique au COMEX suit une règle d'or : pas de CVE, pas de CVSS, pas de jargon. Le format : 3 à 5 indicateurs clés (tendances, couleurs, comparaison avec les objectifs), les risques majeurs (en termes d'impact business — perte de CA, amende, perte de clients), le coût du traitement vs le coût de l'incident (le langage du ROI), et les décisions demandées (budget, arbitrage, validation d'une acceptation de risque). La fréquence : trimestriel, avec des alertes flash si incident significatif.

#### 4.3 Fil rouge — COMPLIANCE : la gouvernance installée

> **📊 COMPLIANCE — Épisode 2**
>
> Marine installe la gouvernance en M1-M2. PSSI rédigée (15 pages, signée par le DG), comité de sécurité mensuel lancé (RSSI, DSI, DPO désigné, directeur R&D, directeur commercial), RACI sécurité défini, et premier reporting COMEX (3 risques rouges, 12 contrôles non implémentés, taux de clic phishing à 34 %, hébergeur non certifié HDS). La direction débloque le budget de 400 K€.

---

### Chapitre 5 — Inventaire des actifs, classification et propriété

On ne protège pas ce qu'on ne connaît pas. L'inventaire des actifs (matériels — serveurs, postes, équipements réseau ; logiciels — applications, SaaS, licences ; données — bases, fichiers, flux ; services cloud — IaaS, PaaS, SaaS ; et personnes clés — les détenteurs de savoir-faire critique) est le fondement de toute démarche de sécurité. La CMDB (Configuration Management Database) est l'outil de référence.

La classification des données en 4 niveaux : **C0 — Public** (aucun impact si divulgué — site web, brochures ; aucune restriction), **C1 — Interne** (impact limité — procédures, org. interne ; accès authentifié), **C2 — Confidentiel** (impact significatif — données clients, finances ; chiffrement, accès restreint), **C3 — Secret** (impact critique — données de santé, stratégie, brevets ; chiffrement fort, traçabilité, besoin d'en connaître strict). Qui classifie : le propriétaire des données (le métier, pas l'IT — le directeur commercial classifie les données commerciales, le directeur R&D classifie les données de recherche).

Le Shadow IT : les SaaS souscrits par les métiers sans validation IT sont un angle mort majeur. Détection : CASB (Cloud Access Security Broker), analyse DNS, revue des dépenses par carte bancaire.

---

## PARTIE II — GESTION DES RISQUES

*Prioriser ce qui compte vraiment — l'analyse de risques est l'outil de décision du RSSI.*

---

### Chapitre 6 — Concepts fondamentaux du risque

#### 6.1 Vocabulaire

Un **actif** est ce qu'on protège (base de données patients, plateforme SaaS, brevet). Une **menace** est ce qui peut arriver (ransomware, employé malveillant, compromission d'un sous-traitant). Une **vulnérabilité** est la faiblesse exploitable (patch manquant, MFA absent, segmentation inexistante). Un **risque** est la combinaison vraisemblance × impact (une fuite de données via l'exploitation d'une vulnérabilité connue non patchée).

Le **risque inhérent** est le risque avant application des contrôles (risque brut). Le **risque résiduel** est le risque après application des contrôles (ce qui reste — et qui doit être formellement accepté par la direction). L'**appétence au risque** (risk appetite) est le niveau de risque que l'organisation est prête à accepter — défini par la direction, pas par le RSSI.

#### 6.2 La formule et la matrice

Risque = Vraisemblance × Impact. L'évaluation peut être **qualitative** (échelles 1-4 : faible/modéré/élevé/critique — la plus courante) ou **quantitative** (en euros via FAIR — la plus convaincante devant le COMEX). La matrice heat map croise les deux axes et visualise les risques en couleurs : rouge (critique — traitement immédiat), orange (élevé — dans les 6 mois), jaune (modéré — surveillance), vert (faible — acceptation possible).

#### 6.3 Traitement du risque

4 options : **réduire** (mettre un contrôle — déployer le MFA), **transférer** (assurance cyber, sous-traitance à un prestataire certifié), **éviter** (supprimer l'activité — ne pas stocker les données de carte bancaire), **accepter** (décision documentée et signée par la direction — pas un oubli). L'acceptation est la décision la plus importante : un risque accepté n'est pas un risque ignoré — c'est un risque évalué, dont le coût du traitement a été pesé, et dont la direction a décidé, par écrit avec signature, de ne pas traiter.

#### 6.4 Le registre des risques

Document vivant, revu trimestriellement minimum : description du risque, vraisemblance (1-4), impact (1-4), niveau (calcul), option de traitement retenue, contrôle(s) associé(s), propriétaire du risque (un membre de la direction, pas le RSSI), statut (ouvert, en traitement, accepté, clos), risque résiduel, et date de prochaine revue.

---

### Chapitre 7 — Méthodologies d'analyse de risques

#### 7.1 EBIOS RM — la méthode française

EBIOS RM (Expression des Besoins et Identification des Objectifs de Sécurité — Risk Manager), développée par l'ANSSI, est structurée en 5 ateliers. Sa force : l'approche par les menaces réelles (les sources de risque sont des attaquants concrets — un groupe APT, un affilié ransomware, un insider — pas des catégories abstraites). Les scénarios produits sont exploitables par le SOC et les équipes techniques.

**Atelier 1 — Cadrage et socle :** définir le périmètre (quel système, quelles données, quelles parties prenantes), les valeurs métier (ce qui a de la valeur pour l'organisation — disponibilité du service, confidentialité des données, intégrité des prescriptions), les événements redoutés (ce qu'on ne veut PAS qu'il se passe), et le socle de sécurité existant (les contrôles déjà en place). **Atelier 2 — Sources de risque :** identifier les attaquants plausibles (qui pourrait attaquer, pourquoi, avec quels moyens) — ici la CTI est le fournisseur d'intelligence (cours CTI de la bibliothèque). Chaque couple source/objectif est évalué en pertinence et en potentiel. **Atelier 3 — Scénarios stratégiques :** construire les chemins d'attaque à haut niveau (l'attaquant X cible la valeur Y via le vecteur Z en exploitant la partie prenante W). **Atelier 4 — Scénarios opérationnels :** décliner en technique (quels systèmes, quelles vulnérabilités, quels artefacts) et évaluer la vraisemblance. **Atelier 5 — Traitement :** définir les mesures pour chaque scénario (contrôle, responsable, échéance, coût) et évaluer le risque résiduel.

#### 7.2 ISO 27005 et FAIR

**ISO 27005** est le cadre générique d'analyse de risques aligné sur ISO 27001 : contexte → identification → analyse → évaluation → traitement → acceptation → communication → surveillance. Plus flexible qu'EBIOS RM, moins prescriptif — il dit « faites une analyse de risques » mais ne dit pas exactement comment.

**FAIR** (Factor Analysis of Information Risk) est la méthode quantitative : elle exprime le risque en euros/dollars, pas en couleurs. Parfaite pour justifier un budget devant le COMEX (« ce risque coûte entre 500 K€ et 2 M€ en espérance de perte annuelle, le contrôle coûte 80 K€ »). Plus complexe à mettre en œuvre, nécessite des données de calibrage.

En pratique, beaucoup combinent : ISO 27005 pour le cadre global + EBIOS RM pour les scénarios concrets + FAIR pour quantifier les risques critiques devant le COMEX.

---

### Chapitre 8 — Analyse de risques en pratique : walkthrough EBIOS RM complet

*Ce chapitre est un walkthrough concret appliqué au fil rouge — pas une description de méthode mais un exercice complet avec des résultats réels.*

**Atelier 1 — Cadrage Néoforma :** périmètre = plateforme SaaS santé (application web, API, bases de données patients, infrastructure cloud Azure + datacenter Nantes). Valeurs métier identifiées avec les métiers : V1 — disponibilité du service SaaS (impact direct sur le CA — 200 hôpitaux dépendent de Néoforma pour la gestion quotidienne des patients), V2 — confidentialité des données de santé (3 millions de dossiers patients — obligation RGPD art.9, risque de sanction CNIL + perte de confiance clients), V3 — intégrité des prescriptions médicales (une modification non autorisée des prescriptions a un impact potentiel sur la sécurité des patients). Événements redoutés : ER1 — indisponibilité prolongée de la plateforme (>4h), ER2 — fuite de données patients, ER3 — modification non autorisée de données médicales. Socle existant évalué via CIS Controls IG1 : 40 % couvert (firewall, antivirus, sauvegardes non testées, pas de MFA, pas d'EDR, pas de segmentation).

**Atelier 2 — Sources de risque :** SR1 — affilié ransomware ciblant le secteur santé (motivation : profit financier, capacité : élevée, vraisemblance : élevée — le secteur santé est le 3ème secteur le plus ciblé par les ransomwares en Europe). SR2 — acteur APT ciblant les données de santé (motivation : espionnage étatique ou économique, capacité : élevée, vraisemblance : modérée). SR3 — insider négligent (motivation : erreur, capacité : accès légitime, vraisemblance : élevée). SR4 — prestataire compromis (motivation : supply chain, capacité : variable, vraisemblance : modérée — 3 sous-traitants critiques dont l'hébergeur non certifié).

**Atelier 3 — Scénarios stratégiques :** SS1 — un affilié ransomware compromet la plateforme SaaS via un phishing sur un admin, chiffre les bases de données patients, et demande 500 K€ de rançon → indisponibilité pour 200 hôpitaux + double extorsion (fuite des données). SS2 — un attaquant exploite une vulnérabilité sur le portail web, accède aux données patients, et les exfiltre → notification CNIL de 3 millions de personnes. SS3 — l'hébergeur non certifié est compromis, les backups sont accessibles, les données patients sont exfiltrées.

**Atelier 4 — Scénarios opérationnels :** déclinaison technique de SS1 : phishing ciblé sur un admin IT → vol de credentials → accès VPN → escalade de privilèges (pas de PAM, comptes admin partagés) → mouvement latéral vers les serveurs de base de données → chiffrement + exfiltration via rclone. Logs nécessaires : email gateway, proxy, AD auth, Sysmon, EDR. Contrôles existants : antivirus (insuffisant). Gaps identifiés : pas de MFA, pas d'EDR, pas de segmentation, pas de monitoring, comptes admin partagés.

**Atelier 5 — Traitement :** pour SS1 : déployer MFA sur tous les accès admin (P0, M1, 15 K€), déployer EDR (P0, M2, 40 K€/an), segmenter le réseau (P1, M6, 30 K€), mettre en place le PAM (P1, M6, 25 K€), sauvegardes immutables et testées (P0, M2, 20 K€/an), plan de réponse incident (P0, M3, 10 K€). Risque résiduel post-traitement : modéré (réduit de critique à modéré).

> **📊 COMPLIANCE — Épisode 3**
>
> Marine présente le rapport EBIOS RM au COMEX avec la matrice heat map : 3 risques critiques (SS1, SS2, SS3), 2 risques élevés, 4 risques modérés. Le PTR chiffré montre que 160 K€ d'investissement immédiat réduisent les 3 risques critiques à modérés. Le DG signe le PTR et l'acceptation formelle des risques résiduels. Le budget est débloqué.

---

### Chapitre 9 — Indicateurs, tableaux de bord et amélioration continue

#### 9.1 Les KPIs sécurité

**Indicateurs opérationnels** (pour le RSSI et l'équipe sécurité, fréquence hebdomadaire) : nombre d'incidents par sévérité, MTTD (temps moyen de détection), MTTR (temps moyen de réponse), taux de patching par criticité (critique < 48h, élevé < 15 jours), nombre de vulnérabilités critiques ouvertes et tendance, couverture EDR (% des endpoints protégés), et backlog d'alertes SOC.

**Indicateurs de conformité** (pour les auditeurs et le suivi interne, fréquence mensuelle) : % de contrôles ISO 27001 implémentés (sur les 78 applicables de la DdA), avancement du PTR (% des actions complétées), nombre de non-conformités ouvertes, échéances des exceptions, et état de la certification.

**Indicateurs humains** (pour la sensibilisation, fréquence continue) : taux de clic phishing simulé (par département et dans le temps), taux de signalement des emails suspects (les utilisateurs qui reportent — aussi important que ceux qui ne cliquent pas), complétion des formations obligatoires, et nombre d'incidents signalés par les utilisateurs.

#### 9.2 Les 3 dashboards

Le **dashboard opérationnel** (audience : RSSI et équipe sécurité, fréquence : hebdomadaire) contient les KPIs détaillés, les incidents en cours, les vulnérabilités, le patching, et les alertes. Le **dashboard stratégique** (audience : COMEX, fréquence : trimestriel) contient 3-5 indicateurs clés avec tendances, les risques majeurs en termes business, le budget consommé vs prévu, et les décisions demandées. Règle d'or : pas de jargon — couleurs, scénarios, impact business. Le **dashboard conformité** (audience : auditeurs et régulateurs, fréquence : avant audit) contient le % de contrôles implémentés, les écarts, l'avancement du PTR, et les preuves disponibles.

---

## PARTIE III — CONFORMITÉ RÉGLEMENTAIRE

*Ce que la loi exige — et comment transformer l'obligation en levier de sécurité réelle.*

---

### Chapitre 10 — RGPD : obligations et articulation sécurité

Le RGPD n'est pas qu'un sujet juridique — c'est un sujet sécurité. L'article 32 impose des mesures techniques et organisationnelles « appropriées » (chiffrement, pseudonymisation, capacité de restauration, tests) — proportionnelles au risque. La notification de violation (art.33-34 — 72h CNIL + personnes si risque élevé) est un processus IR. L'AIPD (art.35) est une analyse de risques. Le cours traite le RGPD sous cet angle opérationnel.

Les **7 principes** (licéité/loyauté/transparence, limitation des finalités, minimisation, exactitude, limitation de conservation, intégrité/confidentialité, responsabilisation). Les **6 bases légales** (consentement, contrat, obligation légale, intérêts vitaux, intérêt public, intérêt légitime). Les **droits des personnes** (accès, rectification, effacement, portabilité, opposition, limitation, non-profilage — processus interne obligatoire, délai 1 mois). Les **obligations clés** : registre des traitements (art.30), AIPD/DPIA (art.35 — obligatoire pour les traitements à risque, notamment les données de santé à grande échelle), DPO (art.37 — obligatoire si autorité publique ou données sensibles à grande échelle), Privacy by Design (art.25), et notification de violation (art.33-34). **Sanctions** : jusqu'à 20 M€ ou 4 % du CA mondial.

Fil rouge : Néoforma traite des données de santé (art.9) de 3 millions de patients — AIPD obligatoire, DPO nommé, hébergement HDS requis, notification 72h en cas de violation. Marine articule la mise en conformité RGPD avec le programme de sécurité global.

---

### Chapitre 11 — NIS 2 : la directive qui change tout

NIS 2 (Network and Information Security Directive v2, 2022/2555) est la directive européenne de cybersécurité qui remplace NIS 1. Élargissement massif du périmètre : 18 secteurs, 2 catégories (entités essentielles — grandes entreprises + secteurs critiques : énergie, transports, santé, eau, infra numérique, espace ; entités importantes — moyennes entreprises + secteurs importants : postaux, chimie, alimentation, fabrication, fournisseurs numériques), critères de taille harmonisés.

**Obligations de sécurité** (art.21) : analyse de risques, gestion des incidents (détection, qualification, réponse), continuité d'activité (PCA, PRA, sauvegardes, tests), sécurité de la supply chain (évaluation des fournisseurs — rendu obligatoire), chiffrement et contrôle d'accès, hygiène et formation, et politiques de sécurité formalisées. **Notification d'incident** (art.23) : alerte précoce 24h (« quelque chose se passe »), notification 72h (« voici ce qui s'est passé »), rapport final 1 mois (« voici l'analyse complète, les causes, les mesures »). Autorité compétente en France : ANSSI. **Sanctions** : EE jusqu'à 10 M€ ou 2 % du CA ; EI jusqu'à 7 M€ ou 1,4 % du CA. **Responsabilité des dirigeants** : NIS 2 engage personnellement les dirigeants — une première.

**NIS 2 vs RGPD vs ISO 27001 :** les trois se recoupent partiellement (analyse de risques, gestion des incidents, mesures techniques) mais avec des angles différents (RGPD = données personnelles, NIS 2 = continuité des services essentiels, ISO 27001 = management de la sécurité). Une organisation qui fait son ISO 27001 sérieusement est largement en conformité NIS 2.

---

### Chapitre 12 — DORA et réglementations sectorielles

**DORA** (Digital Operational Resilience Act — règlement UE 2022/2554, applicable janvier 2025) est la réglementation de résilience opérationnelle numérique pour le secteur financier. Périmètre : établissements financiers (banques, assurances, sociétés de gestion) + prestataires TIC critiques. Exigences : gestion des risques TIC (cadre formalisé, mis à jour), gestion des incidents TIC (classification, notification, reporting), tests de résilience (tests d'intrusion TLPT pour les entités significatives), gestion des tiers TIC (registre, évaluation, clauses contractuelles spécifiques, stratégie de sortie), et partage d'information (échange de renseignement sur les menaces). DORA vs NIS 2 : DORA est lex specialis pour le secteur financier (il prime sur NIS 2 pour les entités financières).

**HDS** (Hébergement de Données de Santé) : certification ANSSI obligatoire pour tout hébergeur de données de santé à caractère personnel en France. Basée sur ISO 27001 + exigences spécifiques santé. Processus : audit de certification par un organisme accrédité. **PCI-DSS v4.0** : 12 exigences pour la protection des données de carte de paiement, 4 niveaux de conformité selon le volume de transactions (SAQ pour les petits commerçants, ROC pour les grands). **II 901** (Instruction Interministérielle n°901) : cadre de sécurité pour les SI sensibles du secteur public (classification Diffusion Restreinte). **RGS** (Référentiel Général de Sécurité) : obligations de sécurité pour les administrations et les téléservices publics. **AI Act** (règlement UE 2024) : classification des systèmes d'IA par niveau de risque (inacceptable, élevé, limité, minimal), obligations par catégorie, lien avec la GRC (les systèmes IA « élevé risque » nécessitent une analyse de risques, un système de management qualité, et une documentation technique).

---

### Chapitre 13 — Audits et certification ISO 27001

#### 13.1 Types d'audits

L'**audit interne** est une auto-évaluation structurée : l'organisation vérifie elle-même la conformité de ses contrôles (exigence ISO 27001 — au moins un audit interne par cycle). L'**audit externe de certification** ISO 27001 se déroule en 2 phases : Phase 1 (revue documentaire — la documentation existe-t-elle ? PSSI, DdA, analyse de risques, PTR, procédures) et Phase 2 (audit terrain — les contrôles sont-ils effectivement implémentés ? Interviews, observations, preuves). L'**audit réglementaire** (contrôle CNIL, ANSSI) vérifie la conformité aux obligations légales. L'**audit client** (questionnaire sécurité, droit d'audit) est exigé par les clients — de plus en plus fréquent dans les appels d'offres.

#### 13.2 Dire vs prouver

La politique existe ≠ la politique est appliquée. L'auditeur demande des preuves : MFA → export IAM avec taux d'activation, patching → rapport de scan + tickets de remédiation fermés, revue des accès → CR signé + captures avant/après, sauvegardes → PV de test de restauration daté, sensibilisation → attestations + résultats phishing, incidents → fiches traitées + retex documenté, SIEM → dashboard des sources connectées + alertes traitées. L'Annexe C fournit le tableau complet « evidence pack ».

#### 13.3 La certification ISO 27001 pas à pas

Phase 1 (1-2 jours sur site) : l'auditeur vérifie que la documentation est complète et cohérente (PSSI, DdA, analyse de risques, PTR, procédures, registre des risques, PV de revue de direction). Phase 2 (3-5 jours sur site, 4-8 semaines après Phase 1) : interviews des responsables, vérification des preuves d'implémentation, tests sur un échantillon de contrôles. Les non-conformités : **majeure** (contrôle manquant ou systémiquement défaillant — bloque la certification), **mineure** (écart ponctuel — plan d'action requis), **observation** (point d'amélioration — pas bloquant). Surveillance annuelle (1-2 jours). Recertification tous les 3 ans (audit complet).

---

### Chapitre 14 — Déclaration d'applicabilité et gestion des exceptions

#### 14.1 La DdA / SoA

La Déclaration d'Applicabilité (Statement of Applicability) est le document ISO 27001 obligatoire qui fait le pont entre l'analyse de risques et les contrôles. Pour chaque mesure de l'Annexe A (93 mesures ISO 27002:2022) : applicable ou non ? Si applicable : implémentée ? Si non implémentée : plan d'action avec échéance. Si non applicable : justification (« nous ne traitons pas de données de carte bancaire → PCI-DSS non applicable »). C'est le document que l'auditeur lit en premier.

#### 14.2 La gestion des exceptions (waivers)

Certains contrôles ne peuvent pas être implémentés immédiatement (contrainte technique, coût, délai). La gestion des exceptions formalise ces dérogations. Chaque exception est : temporaire (date de début, date d'expiration — une exception sans date est un abandon), documentée (contrôle concerné, justification technique ou business, risque résiduel accepté, mesures compensatoires mises en place), signée (par le propriétaire du risque — un membre de la direction, pas le RSSI), et revue trimestriellement (échéance dépassée = renouvellement formel ou implémentation).

Les **contrôles compensatoires** : quand un contrôle requis n'est pas faisable, un contrôle alternatif visant le même objectif peut être mis en place (chiffrement de la base de données impossible car système legacy → segmentation réseau renforcée + contrôle d'accès strict + monitoring dédié + chiffrement au niveau disque).

---

### Chapitre 15 — Homologation de sécurité : décider, documenter, maintenir

#### 15.1 Qu'est-ce que l'homologation

L'homologation de sécurité est la **décision formelle** d'autoriser la mise en service ou le maintien en exploitation d'un système d'information, en connaissance de cause des risques résiduels. Ce n'est pas un audit, ce n'est pas une certification, ce n'est pas une simple acceptation de risque ponctuelle — c'est l'acte par lequel une autorité déclare : « j'ai compris les risques résiduels de ce SI, j'ai évalué que les mesures de sécurité en place sont suffisantes par rapport à l'usage prévu, et j'autorise son exploitation dans ces conditions ».

L'homologation est un processus central en GRC, particulièrement dans les environnements publics, sensibles, régulés, ou avec exigences client fortes. En France, elle est obligatoire pour les SI traitant d'informations classifiées ou Diffusion Restreinte (II 901), pour les SI des OIV (SIIV — Systèmes d'Information d'Importance Vitale), pour les SI des administrations (RGS), et de facto exigée dans de nombreux appels d'offres publics et pour les SI de santé.

#### 15.2 Homologation vs certification vs conformité vs acceptation de risque

La **certification** (ISO 27001, HDS) prouve qu'un système de management est conforme à un référentiel — elle est délivrée par un tiers indépendant et porte sur le système de management, pas sur un SI spécifique. La **conformité** vérifie le respect d'une réglementation (RGPD, NIS 2) — elle est continue et porte sur des obligations. L'**acceptation de risque** est une décision ponctuelle portant sur un risque individuel (« j'accepte le risque de ne pas avoir de MFA sur ce serveur legacy pendant 6 mois »). L'**homologation** est une décision globale portant sur un SI complet (« j'autorise l'exploitation de la plateforme SaaS Néoforma dans sa configuration actuelle, avec ses risques résiduels identifiés, pour une durée de 3 ans »). L'homologation intègre l'analyse de risques, la conformité, les audits, et les exceptions — c'est la synthèse décisionnelle.

#### 15.3 Les acteurs

L'**autorité d'homologation** est le responsable qui signe la décision — un membre de la direction (DG, DSI, directeur métier), jamais le RSSI (qui conseille mais ne décide pas). Le **RSSI** prépare le dossier, conduit l'analyse de risques, évalue les contrôles, et recommande. L'**exploitant** (DSI, équipe d'exploitation) fournit la documentation technique. Les **métiers** expriment les besoins et les contraintes d'usage. Les **auditeurs** (internes ou externes) vérifient la réalité des contrôles.

#### 15.4 Le dossier d'homologation

Le dossier comprend : la description du SI (périmètre, architecture, données traitées, utilisateurs, interconnexions), l'analyse de risques (EBIOS RM ou équivalent — Ch.7-8), le plan de traitement des risques (PTR — mesures décidées, responsables, échéances), la DdA/SoA (contrôles applicables, implémentés, et justifications), les résultats d'audit (audit interne, pentest, audit de conformité), les risques résiduels explicites (ce qui reste après traitement — chaque risque est décrit, évalué, et assumé), les exceptions actives (avec mesures compensatoires et échéances), et la recommandation du RSSI (homologation sans réserve, avec réserves, provisoire, ou refus).

#### 15.5 La décision d'homologation

4 issues possibles. **Homologation sans réserve** : les risques résiduels sont acceptables, les contrôles sont satisfaisants, le SI peut être exploité dans les conditions définies. **Homologation avec réserves** : les risques résiduels sont acceptables sous certaines conditions (actions à mener dans un délai défini — si les réserves ne sont pas levées, l'homologation est suspendue). **Homologation provisoire** : le SI peut être exploité pour une durée limitée (3-6 mois) le temps de mettre en œuvre des actions correctives. **Refus d'homologation** : les risques résiduels sont inacceptables — le SI ne peut pas être mis en service ou doit être arrêté.

#### 15.6 Maintien et ré-homologation

L'homologation a une durée de validité (typiquement 3 ans). Elle doit être **révisée** en cas de changement majeur (nouvelle fonctionnalité, changement d'hébergeur, nouvelle interconnexion, incident de sécurité significatif, évolution réglementaire) et **renouvelée** à échéance (nouveau cycle d'analyse de risques, d'audit, et de décision). Le suivi des réserves et des actions correctives est intégré au comité de sécurité (Ch.4).

#### 15.7 Fil rouge — COMPLIANCE : l'homologation Néoforma

> **📊 COMPLIANCE — Épisode 4**
>
> À M12, Marine prépare le dossier d'homologation de la plateforme SaaS Néoforma. Le dossier comprend l'analyse EBIOS RM (Ch.8), le PTR avec 85 % des actions complétées, la DdA avec 64/78 contrôles implémentés (14 en plan d'action), les résultats du pentest (3 vulnérabilités corrigées, 1 acceptée avec compensatoire), et 2 exceptions actives (pas de segmentation micro sur les bases legacy — échéance M18, compensatoire : monitoring renforcé + ACL strictes). Recommandation RSSI : homologation avec réserves (lever les 2 exceptions avant M18). Le DG signe.

---

## PARTIE IV — SÉCURITÉ OPÉRATIONNELLE VUE GRC

Elle couvre les dimensions de la sécurité opérationnelle qui relèvent du pilotage, de la gouvernance et de l'arbitrage, pas de l'opérationnel technique.*

---

### Chapitre 16 — Gestion des identités et des accès vue GRC

Les principes de gouvernance IAM : moindre privilège (ne donner que les droits nécessaires à la fonction), séparation des devoirs (l'approbateur n'est pas l'exécutant), besoin d'en connaître (l'accès à une information est conditionné par la nécessité fonctionnelle). Les processus : provisioning (création du compte avec les droits associés au profil de poste — automatisé via l'annuaire RH si possible), deprovisioning (désactivation immédiate au départ — le délai entre le départ d'un employé et la désactivation de ses comptes est un indicateur de maturité), et revue des accès (trimestrielle pour les accès privilégiés, semestrielle pour les accès standards — avec CR signé par le propriétaire des données, pas par l'IT). La gestion des comptes privilégiés (PAM — coffre-fort de mots de passe, enregistrement des sessions admin, rotation automatique des mots de passe de service). La politique de MFA (quels comptes : tous les admins + tous les accès distants + les utilisateurs avec accès aux données sensibles ; quels types : résistant au phishing pour les admins — FIDO2/clés physiques, push/TOTP pour les utilisateurs standard). La politique de mots de passe (longueur > complexité — NIST recommande 12+ caractères sans rotation obligatoire, gestionnaire de mots de passe, interdiction de réutilisation).

---

### Chapitre 17 — Sensibilisation : construire un programme qui change les comportements

La sensibilisation n'est pas « envoyer un PowerPoint une fois par an ». C'est un programme continu qui vise le changement de comportement — le facteur humain est le vecteur d'accès initial n°1 (phishing). Les composantes d'un programme efficace : **formation à l'intégration** (onboarding sécurité — 30 min, obligatoire, signée, focus sur les 5 règles essentielles), **phishing simulé** (campagnes mensuelles, métriques par département, coaching individuel pour les récidivistes — pas de punition, de l'accompagnement, sinon les utilisateurs arrêtent de signaler), **formations thématiques par rôle** (développeurs → AppSec, RH → données personnelles, voyageurs → sécurité des déplacements, direction → ingénierie sociale et fraude au président), **micro-learning** (5 min/mois — vidéos courtes, quiz, rappels — maintenir la sécurité dans le radar), et **communication continue** (affiches, newsletter sécurité, alertes — exemples concrets, pas de jargon).

Les métriques : taux de clic phishing (par département et dans le temps — l'objectif n'est pas 0 % mais une tendance à la baisse), taux de signalement (les utilisateurs qui reportent les emails suspects au SOC — aussi important que le taux de clic, car un utilisateur qui signale permet la détection précoce), complétion des formations, et nombre d'incidents signalés par les utilisateurs. L'objectif : que le taux de clic baisse ET que le taux de signalement augmente.

---

### Chapitre 18 — Pilotage du changement, des vulnérabilités et du patching

*Ce chapitre reste à l'angle pilotage GRC — politique, SLA, arbitrage, exceptions, gouvernance. Les détails techniques (scan de vulnérabilités, outils, requêtes) sont dans les cours SOC (Ch.32 VOC) et CTI (Ch.21 vuln intel).*

Le **change management** vu GRC : tout changement sur le SI passe par un processus de validation (demande → analyse d'impact sécurité → approbation → implémentation → vérification post-changement). L'arbitrage sécurité : chaque changement est évalué pour son impact sur les risques (« ce changement ouvre-t-il une vulnérabilité ? nécessite-t-il une mise à jour de l'analyse de risques ? affecte-t-il l'homologation ? »). Les changements d'urgence (le patch critique à 2h du matin — procédure accélérée mais documentée a posteriori).

La **politique de patching** : SLA par criticité (critique < 48h, élevé < 15 jours, moyen < 30 jours, faible trimestriel), exceptions documentées (le système legacy qui ne peut pas être patché → compensatoire : segmentation + monitoring), et le suivi (% de conformité au SLA par mois — indicateur du Ch.9). L'articulation avec la CTI et le VOC : les vulnérabilités exploitées in the wild (CISA KEV, EPSS — cf. cours CTI Ch.21 et cours SOC Ch.32) sont prioritaires indépendamment du CVSS.

L'**assurance cyber vue pilotage** : les prérequis des assureurs sont devenus un socle de sécurité de fait (MFA, EDR, sauvegardes immutables, plan IR, segmentation). Le questionnaire assureur est un mini-audit qui révèle les gaps. L'assurance couvre le risque résiduel après réduction — ce n'est pas un substitut aux contrôles.

---
#### **Chapitre 19 — Référentiels vulnérabilités utiles à la gouvernance : CVE, CWE, CVSS, EPSS, KEV**

_Avant de définir une politique de gestion des vulnérabilités, il faut parler le même langage. Ce chapitre pose les référentiels que la gouvernance utilise pour qualifier, prioriser, tracer et justifier les décisions. L’objectif n’est pas d’entrer dans la technique d’exploitation, mais de comprendre ce que chaque indicateur apporte — et ce qu’il n’apporte pas — dans une logique de pilotage, de conformité et d’auditabilité._

---

## **19.1 Pourquoi la gouvernance a besoin de ces référentiels**

### Idée directrice

En GRC, le problème n’est pas seulement de “connaître les sigles”, mais de **disposer d’un vocabulaire commun** entre :

- RSSI,
- vulnerability manager,
- SOC,
- équipes infra / patching,
- auditeurs,
- direction.

### Ce que tu peux développer

- Les dashboards, rapports d’audit, tickets de remédiation, bulletins CTI et scans de vulnérabilités utilisent tous ces référentiels.
- Sans cadre commun, les arbitrages deviennent incohérents :
    - un CVSS élevé est pris comme une urgence absolue sans contexte ;
    - une CVE en KEV n’est pas traitée plus vite qu’une autre ;
    - EPSS est mal compris comme une preuve d’exploitation ;
    - la direction reçoit des chiffres sans lecture décisionnelle.
- La gouvernance a besoin de ces référentiels pour transformer des données techniques en **décisions traçables et défendables**.

### Message clé

**La GRC n’utilise pas ces référentiels pour faire de la technique ; elle les utilise pour encadrer la décision.**

---

## **19.2 CVE — l’identifiant de référence**

### Objectif

Présenter la CVE comme la **clé d’identification et de traçabilité**.

### À couvrir

- Une **CVE** est un identifiant unique associé à une vulnérabilité connue.
- Elle permet de relier :
    - bulletin éditeur,
    - scanner de vulnérabilités,
    - CTI,
    - ticket de remédiation,
    - exception,
    - audit,
    - incident éventuel.

### Angle GRC

- La CVE sert de **référence commune** dans les processus.
- C’est l’identifiant à conserver dans :
    - les rapports de vulnérabilités,
    - les décisions de traitement,
    - les exceptions,
    - les preuves d’audit,
    - les comptes rendus de comité.

### Message clé

**La CVE permet de parler exactement du même sujet dans toute la chaîne de gouvernance.**

---

## **19.3 CWE — la faiblesse sous-jacente et l’intérêt pour l’amélioration structurelle**

### Objectif

Montrer que la CWE est utile en GRC non pour l’investigation fine, mais pour la **lecture structurelle des causes**.

### À couvrir

- Une **CWE** décrit une catégorie de faiblesse :
    - contrôle d’accès insuffisant,
    - injection,
    - mauvaise validation d’entrée,
    - erreurs mémoire,
    - désérialisation, etc.
- Différence avec CVE :
    - **CVE** = vulnérabilité précise ;
    - **CWE** = famille de faiblesse.

### Angle GRC

- Très utile pour détecter des tendances :
    - plusieurs CVE sur une même famille de produits peuvent pointer vers la même faiblesse ;
    - plusieurs audits peuvent révéler un défaut systémique de développement, de configuration ou d’architecture.
- Intérêt pour :
    - plans d’action structurels,
    - secure by design,
    - exigences fournisseurs,
    - politique de développement sécurisé,
    - priorisation des efforts de remédiation à moyen terme.

### Message clé

**La CVE aide à traiter un cas ; la CWE aide à corriger une cause récurrente.**

---

## **19.4 CVSS — mesurer la sévérité technique d’une vulnérabilité**

### Objectif

Introduire CVSS comme **score de sévérité**, pas comme décision finale.

### À couvrir

- Le **CVSS** est le référentiel de sévérité le plus utilisé pour exprimer la criticité technique d’une vulnérabilité.
- Expliquer simplement ce qu’il cherche à mesurer :
    - facilité d’exploitation,
    - conditions d’exploitation,
    - impact potentiel sur confidentialité, intégrité, disponibilité.
- Préciser qu’un score CVSS :
    - aide à comparer,
    - aide à prioriser,
    - mais ne suffit jamais seul.

### Angle GRC

- Le score CVSS est un **point de départ**, utile pour :
    - les dashboards,
    - la priorisation initiale,
    - la communication entre équipes,
    - la définition de seuils de rescoring.
- Mais la gouvernance doit explicitement empêcher une lecture naïve du type :
    - “9.8 = toujours urgence absolue”,
    - “5.5 = toujours secondaire”.

Ton cours actuel dit déjà bien que le **score Base brut** est générique et que la gouvernance doit le transformer en score actionnable. Ce nouveau chapitre vient donc préparer naturellement l’actuel chapitre suivant.

### Message clé

**CVSS donne une sévérité technique de référence ; la gouvernance décide ensuite comment l’utiliser.**

---

## **19.5 EPSS — introduire la probabilité d’exploitation dans la décision**

### Objectif

Faire comprendre pourquoi EPSS complète CVSS dans une logique de pilotage.

### À couvrir

- **EPSS** estime la probabilité qu’une vulnérabilité soit exploitée dans un horizon proche.
- Il ne mesure pas la sévérité technique, mais la **pression d’exploitation probable**.
- Deux CVE proches en CVSS peuvent avoir des profils EPSS très différents.

### Angle GRC

- EPSS est utile pour :
    - enrichir les règles de priorisation,
    - arbitrer entre plusieurs remédiations concurrentes,
    - alimenter les comités de sécurité,
    - justifier une accélération de traitement.
- Important de préciser :
    - EPSS n’est pas une preuve d’exploitation ;
    - c’est un **facteur de priorisation** parmi d’autres.

Ton chapitre 18 mentionne déjà que les vulnérabilités exploitées in the wild et les signaux de menace doivent être prioritaires indépendamment du CVSS ; ce chapitre 19 permet justement d’expliquer pourquoi.

### Message clé

**CVSS dit “c’est grave techniquement”, EPSS aide à dire “ça risque d’être exploité bientôt”.**

---

## **19.6 KEV — quand la menace n’est plus théorique**

### Objectif

Donner à KEV sa place de signal fort de gouvernance.

### À couvrir

- Le **KEV** recense les vulnérabilités connues comme exploitées dans le monde réel.
- Là, on ne parle plus de potentiel, mais d’**exploitation observée**.

### Angle GRC

- La présence en KEV change la posture de gouvernance :
    - raccourcissement des SLA,
    - priorisation au comité,
    - demande de suivi renforcé,
    - revue immédiate des actifs exposés,
    - potentiellement note d’alerte RSSI / DSI / COMEX selon le contexte.
- C’est un marqueur fort de **proportionnalité** et de **diligence** dans un contexte audit/conformité.

Ton cours actuel le mobilise déjà dans la logique de rescoring et d’Exploit Maturity ; ici on le pose explicitement en amont comme brique de gouvernance.

### Message clé

**KEV transforme une vulnérabilité théorique en sujet de gouvernance prioritaire.**

---

## **19.7 Bien distinguer les rôles de chaque référentiel**

### Objectif

Faire une sous-partie de synthèse très claire.

### Tableau conseillé

|Référentiel|Ce qu’il dit|Ce qu’il ne dit pas|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on|Si elle est grave ou exploitée|
|**CWE**|Quelle faiblesse est en cause|Si un système précis est compromis|
|**CVSS**|Quelle est la sévérité technique|Quelle priorité absolue retenir chez nous|
|**EPSS**|Quelle est la probabilité d’exploitation|Si la vulnérabilité est déjà exploitée chez nous|
|**KEV**|Qu’elle est exploitée dans le réel|Quel est le niveau de risque précis dans notre SI|

### Message clé

**Aucun de ces référentiels, pris seul, ne suffit à décider. Leur valeur est dans leur combinaison.**

---

## **19.8 Ce que la gouvernance doit en faire concrètement**

### Objectif

Raccorder immédiatement ce chapitre au suivant.

### À couvrir

La gouvernance doit définir :

- quels référentiels sont retenus officiellement ;
- quelles sources sont considérées comme de référence ;
- qui lit quoi et à quel moment ;
- comment les scores et signaux alimentent :
    - la priorisation,
    - les SLA,
    - les exceptions,
    - la traçabilité,
    - les revues de risque,
    - les audits.

### Pont avec le chapitre suivant

Cette sous-partie doit préparer explicitement le futur **chapitre 20 — Politique de gestion des vulnérabilités : du score brut au score contextualisé**, qui expliquera déjà :

- le problème du score Base brut ;
- CVSS v4 et ses groupes Base / Threat / Environmental / Supplemental ;
- les rôles de requalification ;
- les SLA par score contextualisé ;
- la documentation et l’articulation avec ISO 27001, EBIOS RM et NIS2.

### Message clé

**Ce chapitre pose le vocabulaire ; le suivant posera les règles de décision.**

---

## **19.9 Fil rouge — COMPLIANCE : lecture gouvernance d’une vulnérabilité**

Je te conseille une petite sous-partie narrative, comme dans le reste du cours.

### Format possible

> **📊 COMPLIANCE — Épisode X**  
> Marine reçoit un rapport de scan mentionnant plusieurs CVE “critiques” sur des serveurs exposés et internes. Avant de demander une remédiation générale en urgence, elle fait clarifier les éléments de lecture : quelles CVE sont réellement concernées, quelles faiblesses reviennent de manière récurrente, quelles vulnérabilités sont déjà connues comme exploitées, et lesquelles présentent une forte probabilité d’exploitation. Ce premier cadrage ne décide pas encore du SLA, mais il permet d’éviter deux erreurs classiques : traiter toutes les vulnérabilités comme équivalentes, ou s’appuyer sur le seul score brut sans tenir compte du contexte de menace.

### Intérêt

Ça colle bien au ton de ton fil rouge COMPLIANCE, où Marine structure la gouvernance progressivement dans une organisation immature.

---

## **19.10 Transition vers le chapitre 20**

### Phrase de transition possible

> Connaître les référentiels ne suffit cependant pas à piloter une gestion des vulnérabilités. La question décisive pour la gouvernance n’est pas seulement de savoir ce que signifie une CVE ou un score CVSS, mais de définir comment ces éléments seront utilisés dans l’organisation : qui peut requalifier, selon quelles règles, avec quels SLA, et avec quelle traçabilité. C’est l’objet du chapitre suivant.

---

## Structure finale recommandée

Je te conseille donc ce plan :

- **19.1 Pourquoi la gouvernance a besoin de ces référentiels**
- **19.2 CVE — l’identifiant de référence**
- **19.3 CWE — la faiblesse sous-jacente et l’intérêt pour l’amélioration structurelle**
- **19.4 CVSS — mesurer la sévérité technique d’une vulnérabilité**
- **19.5 EPSS — introduire la probabilité d’exploitation dans la décision**
- **19.6 KEV — quand la menace n’est plus théorique**
- **19.7 Bien distinguer les rôles de chaque référentiel**
- **19.8 Ce que la gouvernance doit en faire concrètement**
- **19.9 Fil rouge — COMPLIANCE : lecture gouvernance d’une vulnérabilité**
- **19.10 Transition vers le chapitre 20**

## Renumérotation recommandée

Avec ton option “la plus propre”, ça donnerait :

- **Ch.18 — Pilotage du changement, des vulnérabilités et du patching**
- **Ch.19 — Référentiels vulnérabilités utiles à la gouvernance : CVE, CWE, CVSS, EPSS, KEV**
- **Ch.20 — Politique de gestion des vulnérabilités : du score brut au score contextualisé**
- **Ch.21 — Sécurité contractuelle et juridique**
- puis le reste décale.

---
### 20 — Politique de gestion des vulnérabilités : du score brut au score contextualisé

La gestion des vulnérabilités est un processus de gouvernance avant d'être un processus technique. Le scanner de vulnérabilités (Qualys, Nessus, Rapid7) produit des centaines de findings par semaine, chacun accompagné d'un score CVSS Base (v3.1 ou v4.0). Sans politique de contextualisation, le résultat est prévisible : tout est « critique », les équipes sont saturées, et les vraies urgences se noient dans le bruit. La politique de gestion des vulnérabilités définit les règles du jeu — quel framework de scoring est utilisé, comment le score est contextualisé, qui a l'autorité de re-qualifier, et quels SLA s'appliquent par niveau contextualisé.

#### 20.1 Le problème du score Base brut

Le score CVSS Base est **générique** — il décrit la vulnérabilité dans l'absolu, indépendamment de l'environnement de l'organisation. Il ne tient compte ni de l'exposition réelle de l'actif (Internet vs réseau interne vs segment isolé), ni des contrôles compensatoires en place (WAF, segmentation, MFA, EDR), ni de la criticité métier de l'actif (un serveur de test et un serveur de production financière ne méritent pas le même SLA de traitement), ni de l'état d'exploitation (un exploit théorique et un exploit utilisé activement in-the-wild ne représentent pas le même risque).

Le rôle de la gouvernance est de transformer ce score brut en un score actionnable qui reflète la réalité de l'organisation. C'est un acte de pilotage GRC : le GRC définit la politique, le SOC et les équipes techniques l'appliquent.

#### 20.2 CVSS v4.0 : la structure qui supporte la politique

CVSS v4.0 (FIRST, fin 2023, supporté par le NVD depuis 2024) apporte une structure de scoring en quatre groupes de métriques conçue pour la contextualisation :

Le groupe **Base** mesure la sévérité intrinsèque (vecteur d'attaque, complexité, privilèges requis, interaction utilisateur, impacts CIA). Le groupe **Threat** (remplace le « Temporal » de v3.1) intègre l'état d'exploitation réel via Exploit Maturity (Unreported — pas d'exploitation connue, PoC — preuve de concept publique, Attacked — exploitation confirmée in-the-wild). Le groupe **Environmental** permet d'adapter le score au contexte de l'organisation (Modified Attack Vector — le service est-il réellement exposé ?, Modified Privileges Required — des contrôles compensent-ils ?, Security Requirements CIA — la criticité métier de l'actif). Le groupe **Supplemental** (nouveau en v4 — Safety, Automatable, Recovery, Value Density, Provider Urgency) enrichit la contextualisation sans modifier le score numérique.

CVSS v4 produit des scores différenciés : **CVSS-B** (Base seul), **CVSS-BT** (Base + Threat), **CVSS-BE** (Base + Environmental), **CVSS-BTE** (Base + Threat + Environmental). Cette nomenclature force la transparence — le rapport de vulnérabilités doit indiquer quel niveau de contextualisation a été appliqué.

#### 20.3 Ce que la politique de gestion des vulnérabilités doit définir

La politique GRC doit répondre à sept questions :

(1) **Quel framework de scoring ?** CVSS v3.1 reste utilisé dans de nombreuses bases (NVD historique, scanners), mais la transition vers CVSS v4.0 est recommandée — le NVD supporte les deux. La politique peut imposer le rescoring en v4 pour toutes les vulnérabilités au-dessus d'un seuil (ex : tout CVSS-B ≥ 7.0 doit être re-scoré en v4 avec les métriques Threat + Environmental).

(2) **Qui a l'autorité de re-qualifier ?** Le rescoring contextuel n'est pas un acte anodin — re-qualifier un 9.8 en 5.5 doit être tracé, justifié, et validé. La politique doit désigner qui peut re-qualifier (le SOC manager, le RSSI, le vulnerability manager) et exiger une justification documentée pour chaque re-qualification significative (baisse de plus de 2 points par rapport au score Base).

(3) **Quelles métriques Environmental sont appliquées ?** La politique doit définir les règles d'application des métriques environnementales : comment est déterminé le Modified Attack Vector (cartographie de l'exposition — la CMDB doit indiquer si l'actif est exposé sur Internet), comment sont évalués les contrôles compensatoires (une matrice de correspondance entre les contrôles en place et les Modified Metrics CVSS), et comment est déterminée la criticité métier (les Security Requirements CIA sont dérivées de la classification des actifs — un actif classé « critique » dans la cartographie des risques a des Security Requirements High).

(4) **Comment est intégrée la métrique Threat ?** Le SOC et le CTI alimentent l'Exploit Maturity : si la CVE est dans le KEV (Known Exploited Vulnerabilities) de la CISA, ou si le CTI interne observe une exploitation active, l'Exploit Maturity passe à « Attacked » → le score CVSS-BT monte, la priorité de traitement aussi.

(5) **Quels SLA par score contextualisé ?** Les SLA de traitement sont définis sur le score contextualisé (CVSS-BTE), pas sur le score Base brut. Exemple : CVSS-BTE ≥ 9.0 = P0 (24-48h), 7.0-8.9 = P1 (7 jours), 4.0-6.9 = P2 (30 jours), < 4.0 = P3 (90 jours ou risque accepté). Sans cette distinction, les SLA sont basés sur le score Base → tout est P0 → les équipes sont saturées → rien n'est traité en temps.

(6) **Comment est documenté le rescoring ?** Chaque rescoring doit être tracé : CVE, score Base original (source — éditeur/NVD), score contextuel interne (CVSS-BTE), justification des métriques Environmental appliquées, date du rescoring, et auteur. Cette traçabilité est indispensable pour l'audit (ISO 27001 A.12.6, NIS2) et pour le retex post-incident (si un incident exploite une vulnérabilité re-qualifiée à la baisse, le retex doit analyser si la re-qualification était justifiée).

(7) **Quelle est l'articulation avec la gravité des incidents ?** Le rescoring CVSS contextuel et la qualification de gravité IR (P1/P2/P3/P4) sont deux évaluations distinctes. Le CVSS contextuel évalue la sévérité de la vulnérabilité dans l'environnement. La gravité IR évalue l'impact de l'incident sur l'organisation. Les deux se nourrissent (une vulnérabilité avec un CVSS-BTE élevé exploitée activement alimente une gravité IR élevée), mais elles ne sont pas interchangeables. La politique doit le stipuler explicitement pour éviter les confusions opérationnelles.

#### 20.4 Articulation avec les référentiels

**ISO 27001** (A.12.6 — Gestion des vulnérabilités techniques) : la norme exige que les vulnérabilités soient évaluées et traitées en fonction du risque pour l'organisation. Le rescoring contextuel CVSS v4 est un moyen concret de satisfaire cette exigence — il documente l'évaluation du risque spécifique à l'environnement, pas seulement le score générique.

**EBIOS RM** : la méthode d'analyse de risque française intègre les scénarios opérationnels (quelles vulnérabilités, exploitées par quels acteurs, avec quel impact). Le rescoring CVSS v4 alimente ces scénarios — l'Exploit Maturity (Threat) reflète la capacité de l'acteur, les Modified Metrics (Environmental) reflètent l'exposition du système, et le score résultant alimente l'évaluation de la vraisemblance.

**NIS2** : la directive impose une gestion des vulnérabilités proportionnée. Le rescoring contextuel documente cette proportionnalité — un auditeur qui voit un CVSS-B 9.8 non traité en 7 jours posera la question. Si la réponse est « le CVSS-BTE est 4.2 parce que le service est isolé, compensé par un WAF, et ne traite pas de données critiques — voici la documentation », c'est une réponse de gouvernance mature.

#### 20.5 En résumé

| Composante | Responsable | Ce qu'elle produit |
|-----------|-------------|-------------------|
| Score CVSS-B (éditeur/NVD) | Externe (éditeur, NVD) | Score générique de référence |
| Rescoring CVSS-BTE contextuel | Vulnerability manager (sous politique GRC) | Score adapté à l'environnement réel |
| SLA de traitement | GRC (politique de gestion des vulnérabilités) | Délai de remédiation par niveau contextualisé |
| Gravité IR (P1-P4) | SOC / IR (sous politique de gestion des incidents) | Niveau de mobilisation et d'escalade |

La politique de gestion des vulnérabilités est le pont entre la gouvernance (GRC) et l'opérationnel (SOC, IT, DevOps). Le rescoring contextuel CVSS v4 est l'outil qui rend ce pont concret et auditable.

---

### Chapitre 21 — Sécurité contractuelle et juridique

*Ce chapitre traite de la dimension juridique et contractuelle de la sécurité — les clauses, les responsabilités, les NDA. La gouvernance des tiers (évaluation, scoring, surveillance) est au Ch.24 pour éviter la redondance.*

Les **clauses de sécurité dans les contrats** : le PAS (Plan d'Assurance Sécurité — mesures techniques et organisationnelles exigées du prestataire), le SLA sécurité (notification d'incident dans les X heures, patching des vulnérabilités critiques dans les Y jours, disponibilité, taux de disponibilité), la notification d'incident (obligation contractuelle du prestataire de notifier immédiatement tout incident affectant les données ou les services du client), la réversibilité (conditions de récupération des données en fin de contrat — format, délai, coût, destruction), le droit d'audit (droit du client d'auditer le prestataire ou d'accéder aux rapports d'audit — SOC 2, ISO 27001), et l'article 28 RGPD (contrat de sous-traitance obligatoire — objet, durée, nature des données, obligations du sous-traitant).

La **responsabilité en cas d'incident** : responsabilité contractuelle (le prestataire n'a pas respecté le PAS → dommages et intérêts), responsabilité délictuelle (négligence → l'organisation n'a pas pris les mesures « appropriées » au sens RGPD art.32), obligation de moyens vs obligation de résultat (la sécurité est généralement une obligation de moyens — « nous avons pris les mesures raisonnables » — mais la conformité réglementaire est une obligation de résultat — « vous devez notifier dans les 72h »). La PSSI comme preuve de diligence (en cas de contentieux, une PSSI appliquée démontre que l'organisation a pris des mesures).

Les **NDA** (accords de confidentialité) : quand en signer (avant toute discussion impliquant des informations confidentielles — partenariat, prestation, recrutement), contenu (définition de l'information confidentielle, durée, exceptions, sanctions). La **protection de la PI dans les contrats** de développement (qui détient les résultats : en prestation → le client sauf stipulation contraire, en co-développement → à définir explicitement, en stage/thèse → cadre spécifique avec l'établissement d'enseignement).

---

## PARTIE V — RÉSILIENCE ET CONTINUITÉ

*Quand ça tourne mal — comment l'organisation se prépare, réagit, et se reconstruit.*

---

### Chapitre 22 — Gestion des incidents de sécurité vue GRC

*Ce chapitre couvre le processus, les obligations, et la coordination de la gestion d'incident. La bascule vers la gestion de crise (quand l'incident dépasse la capacité de gestion normale) est traitée au Ch.22 — la distinction est structurante.*

#### 22.1 Événement vs incident

Un **événement de sécurité** est un observable qui peut ou non indiquer une menace (une alerte SIEM, un email suspect signalé par un utilisateur). Un **incident de sécurité** est un événement confirmé qui a un impact sur la confidentialité, l'intégrité, ou la disponibilité des actifs. La classification par sévérité : **P1 — Critique** (impact business majeur — ransomware actif, fuite massive, compromission AD — activation cellule de crise, notification réglementaire probable), **P2 — Élevé** (impact significatif — serveur compromis, phishing réussi avec accès aux données — investigation approfondie, confinement immédiat), **P3 — Modéré** (impact limité — malware isolé sur un poste — traitement standard), **P4 — Informatif** (pas d'impact — scan détecté, tentative bloquée — documentation).

#### 22.2 Le processus

Le processus suit le modèle NIST SP 800-61 : **détection** (SOC, utilisateurs, tiers — cf. cours SOC), **qualification** (VP/FP, sévérité, périmètre — le RSSI qualifie P1/P2, le SOC qualifie P3/P4), **confinement** (isoler les machines, bloquer les comptes, bloquer les IoC — cf. cours SOC Ch.23), **éradication** (supprimer la menace, patcher la vulnérabilité, réinitialiser les credentials), **récupération** (restaurer les services, vérifier l'intégrité), et **retex** (post-mortem sans blame — timeline, ce qui a fonctionné, ce qui a échoué, actions correctives → alimente le registre des risques).

#### 22.3 Obligations de notification

| Réglementation | Délai | Destinataire | Contenu |
|---------------|-------|-------------|---------|
| RGPD | 72h | CNIL + personnes si risque élevé | Nature, données, conséquences, mesures |
| NIS 2 | 24h / 72h / 1 mois | ANSSI | Alerte précoce / notification / rapport final |
| DORA | Selon classification | Régulateur financier | Incident TIC majeur |
| PCI-DSS | Immédiat | Brands, banque acquéreuse | Compromission données CB |
| OIV/SIIV | Sans délai | ANSSI | Incident sur un SIIV |

#### 22.4 La coordination GRC-SOC-IR

Le RSSI coordonne (vision globale, arbitrage, communication direction), le SOC détecte et investigue (cf. cours SOC), l'IR remédie (cf. cours IR), le DPO notifie la CNIL si données personnelles, le juridique qualifie les obligations, et la COM communique (interne et externe). Le RSSI ne fait pas tout — il orchestre.

---

### Chapitre 23 — Continuité (PCA) et reprise (PRA)

Les concepts : **PCA** (Plan de Continuité d'Activité — comment continuer à fonctionner pendant la crise), **PRA** (Plan de Reprise d'Activité — comment revenir à la normale après la crise), **BIA** (Business Impact Analysis — quels processus sont critiques), **RPO** (Recovery Point Objective — combien de données peut-on perdre ? → dimensionne les sauvegardes), **RTO** (Recovery Time Objective — en combien de temps doit-on redémarrer ? → dimensionne l'infrastructure de reprise).

Le **BIA en pratique** : identifier les processus critiques AVEC les métiers (pas avec l'IT seul — les métiers savent ce qui est vital pour le business), évaluer l'impact à 1h, 4h, 24h, 48h, 1 semaine (financier, réputationnel, réglementaire, humain), identifier les dépendances (SI, prestataires, personnes), et définir les RPO/RTO par processus.

Les **stratégies de continuité** : sauvegardes 3-2-1 + immutables (3 copies, 2 supports, 1 hors site, anti-ransomware — RPO : heures à 24h, RTO : heures à jours, coût : faible à moyen), haute disponibilité (redondance, clustering, failover — RPO : quasi 0, RTO : minutes, coût : élevé), site de repli cold/warm/hot (du local vide au prêt à fonctionner — RPO/RTO et coût croissants), et Cloud DRaaS (réplication cloud, basculement automatisé). Les **tests** : test de restauration (semestriel minimum — « testez vos sauvegardes : la question n'est pas SI elles ne marchent pas, mais QUAND vous le découvrirez »), tabletop (simulation en salle, annuel), et exercice technique (basculement réel site de repli, annuel pour les processus critiques).

---

### Chapitre 24 — Gestion de crise cyber

*La gestion de crise commence là où la gestion d'incident s'arrête. Un incident P1 qui dépasse la capacité de gestion normale (SOC débordé, impact business majeur, médias, clients impactés) bascule en crise. La bascule est le moment clé — elle doit être formalisée (seuil défini, pas de débat le jour J).*

#### 24.1 L'organisation de crise

La **cellule de crise** est pré-constituée (pas improvisée le jour J) : DG (décisions stratégiques — payer ou non la rançon, communiquer ou non), RSSI (coordinateur technique — pilote la réponse, fait le lien entre technique et direction), Direction COM (communication interne, externe, médias — ce qui est dit et ce qui ne l'est pas), Juridique/DPO (notifications réglementaires, qualification juridique, plainte), Technique/IR/SOC (investigation, confinement, éradication — cf. cours IR). La **salle de crise** utilise des outils HORS du SI compromis (téléphones personnels, messagerie externe, visio dédiée, tableaux physiques). Les moyens de communication sont testés en amont.

#### 24.2 La communication de crise

4 audiences : les **collaborateurs** (ce qui se passe, quoi faire/ne pas faire, point de contact — « ne redémarrez pas vos postes, n'envoyez pas d'emails, utilisez vos téléphones personnels »), les **clients/partenaires** (impact sur les services, mesures prises, calendrier de reprise — « nos services sont temporairement indisponibles, nous travaillons à la résolution »), les **régulateurs** (notification formelle CNIL/ANSSI selon les délais réglementaires — Ch.20), et les **médias** (communiqué factuel, pas de spéculation, pas de détails techniques — « nous avons détecté un incident de sécurité, nos équipes sont mobilisées »). Principes : transparence dosée, ne pas mentir, ne pas spéculer, communiquer ce qu'on sait et ce qu'on fait. Les templates sont préparés à l'avance et adaptés le jour J.

#### 24.3 L'exercice de crise

Scénario réaliste (ransomware vendredi soir, fuite de données, compromission d'un fournisseur critique). Participants : direction + équipes clés. Injections d'événements toutes les 15-30 min (le scénario évolue — « les médias appellent », « un client menace de rompre le contrat », « les sauvegardes ne fonctionnent pas »). Décisions à prendre et communication à produire. Retex : ce qui a fonctionné, les blocages, les améliorations.

---

### Chapitre 25 — Assurance cyber et transfert de risque

L'assurance cyber comme option de traitement du risque résiduel. Le marché (acteurs, couvertures types — interruption d'activité, frais de réponse à incident, notification des personnes, responsabilité civile, cyber-extorsion, frais juridiques). Les prérequis des assureurs (MFA obligatoire, EDR déployé, sauvegardes immutables testées, plan IR formalisé, segmentation — les assureurs imposent un socle de sécurité minimum qui est devenu un standard de facto). Les exclusions (actes de guerre — clause Lloyds 2023, amendes réglementaires, perte de données non chiffrées, incidents antérieurs — lire les petites lignes). Le processus (questionnaire, audit de souscription, tarification, couverture). L'articulation avec la gestion des risques (l'assurance couvre le risque financier résiduel APRÈS la réduction — pas un substitut aux contrôles ; un assureur qui couvre une organisation sans MFA n'existe plus). Fil rouge : Néoforma souscrit une assurance cyber — le questionnaire assureur révèle 3 non-conformités.

---

## PARTIE VI — GESTION DES TIERS ET CLOUD

*Les tiers sont la surface d'attaque n°1 — NIS 2 impose leur gestion.*

---

### Chapitre 26 — Gouvernance des tiers : évaluation, scoring et surveillance

*Ce chapitre couvre la gouvernance des tiers — processus d'évaluation, scoring, surveillance continue. Les clauses contractuelles et la dimension juridique sont au Ch.19 pour éviter la redondance.*

Le risque tiers : les prestataires ont accès aux systèmes et aux données, les compromissions via tiers sont parmi les plus dévastatrices (SolarWinds, Cloud Hopper, incidents via infogérants), et NIS 2 impose explicitement la gestion de la supply chain.

L'évaluation et le scoring : chaque fournisseur est classé selon son niveau d'accès et de criticité. **Critique** (accès données sensibles ou SI critiques — hébergeur, infogérant, éditeur ERP) : PAS complet, audit ou certification exigée (ISO 27001, SOC 2 Type II, HDS), SLA sécurité renforcé, revue annuelle. **Important** (accès SI ou données internes — prestataire dev, support IT) : questionnaire sécurité structuré, clauses contractuelles, revue bisannuelle. **Standard** (pas d'accès SI ni données sensibles — fournitures, nettoyage) : clauses RGPD basiques si données personnelles traitées.

La due diligence AVANT contractualisation (pas après — quand le contrat est signé, le rapport de force est inversé). Le questionnaire fournisseur (gouvernance, accès, chiffrement, gestion des incidents, continuité, certifications, sous-traitance éventuelle). La surveillance continue (revue annuelle des fournisseurs critiques, surveillance des certifications — expiration, retrait, surveillance des incidents publics, et ratings externes — SecurityScorecard, BitSight — utiles pour le screening initial, insuffisants pour l'évaluation en profondeur). Le registre des tiers (document vivant — fournisseur, criticité, accès, score, date de dernière revue, prochaine revue).

---

### Chapitre 27 — Cloud, souveraineté et conformité

La sécurité du cloud vue GRC repose sur le modèle de **responsabilité partagée** : en IaaS, le fournisseur gère l'infrastructure physique et la virtualisation, le client gère tout le reste (OS, applications, données, accès) ; en PaaS, le fournisseur gère aussi l'OS et le middleware ; en SaaS, le fournisseur gère quasi tout, le client gère les accès et la configuration. La confusion sur ce modèle est la source n°1 des incidents cloud.

La **souveraineté des données** : le Cloud Act permet aux autorités US d'accéder aux données hébergées par des entreprises américaines (AWS, Azure, Google), même si les données sont physiquement en Europe. Le FISA 702 permet la surveillance des communications de personnes non américaines. Schrems II a invalidé le Privacy Shield. Les solutions : **SecNumCloud** (qualification ANSSI — hébergement souverain avec immunité aux lois extraterritoriales), chiffrement côté client (le fournisseur ne peut pas lire les données — mais cela limite les fonctionnalités), cloud souverain européen (3DS Outscale, OVHcloud, Scaleway — certifiés ou en cours de certification SecNumCloud), et C5 (certification cloud allemande — BSI).

Le questionnaire cloud : localisation des données (pays, région, transferts internationaux), chiffrement (en transit, au repos, gestion des clés — qui détient les clés ?), accès (qui accède aux données, depuis où, avec quel contrôle), conformité (certifications, audits, transparence), réversibilité (format d'export, délai, coût, destruction des données), et SLA (disponibilité, support, notification d'incident).

---

## PARTIE VII — MATURITÉ, PROGRAMME ET CAS DE SYNTHÈSE

---

### Chapitre 28 — Construire un programme de sécurité

Par où commencer : évaluation de maturité initiale (CIS Controls IG1 comme benchmark rapide, NIST CSF tier assessment pour le positionnement). Les **10 quick wins** à impact maximal : (1) inventaire des actifs, (2) MFA sur tous les accès admin et distants, (3) patching automatisé, (4) sauvegardes 3-2-1 + immutables, (5) EDR sur tous les endpoints et serveurs, (6) logs centralisés, (7) politique de mots de passe + gestionnaire, (8) sensibilisation continue, (9) plan d'incident + contacts d'urgence, (10) segmentation réseau. Les 5 premiers couvrent la majorité du risque — commencer par eux crédibilise le RSSI et débloque le budget.

La roadmap sécurité (plan à 1 an et 3 ans avec jalons, budget, et responsables). Le budget (justification en langage business : coût de l'incident vs coût de la prévention, obligations réglementaires, exigences contractuelles des clients, prérequis assureurs ; benchmark : 5-15 % du budget IT). Les modèles d'organisation (SOC interne vs MSSP, RSSI interne vs temps partagé vs vCISO — avantages, inconvénients, adaptés à quels contextes).

---

### Chapitre 29 — Modèles de maturité et amélioration continue

Les modèles de maturité : **Niveau 1 — Initial** (ad hoc, pas de processus formalisé, la sécurité dépend des individus), **Niveau 2 — Répétable** (des processus existent pour les activités principales, mais pas systématiques), **Niveau 3 — Défini** (processus documentés, appliqués, et mesurés — c'est le niveau ISO 27001), **Niveau 4 — Géré** (indicateurs quantitatifs, amélioration pilotée par les données), **Niveau 5 — Optimisé** (amélioration continue intégrée, anticipation, innovation).

L'auto-évaluation (CIS Controls IG assessment, NIST CSF tier assessment — comment la conduire, quoi en faire). Le programme d'amélioration continue (PDCA appliqué : indicateurs → revue → actions correctives → contrôles améliorés → re-mesure ; retex post-incident comme moteur d'amélioration ; purple team et tests de contrôles comme validation).

---

### Chapitre 30 — GRC et cybersécurité opérationnelle : la convergence

Ce chapitre fait le pont entre la GRC et la sécurité technique — la convergence que la bibliothèque rend possible.

Comment l'analyse de risques alimente la CTI : les sources de risque de l'atelier 2 EBIOS RM sont les acteurs du cours APT — la CTI fournit le renseignement qui rend l'analyse de risques concrète et **threat-informed** plutôt qu'abstraite. Un scénario EBIOS RM qui dit « un attaquant sophistiqué cible nos données de santé » est générique. Un scénario qui dit « APT41 cible les éditeurs SaaS santé européens avec exploitation de vulnérabilités web et mouvement latéral vers les bases de données — cf. campagne X documentée par Mandiant » est actionnable.

Comment les indicateurs GRC se nourrissent du SOC : le MTTD, le MTTR, le taux de FP, la couverture ATT&CK sont des indicateurs opérationnels (cours SOC) qui remontent dans le dashboard COMEX (Ch.9). Le RSSI qui présente au COMEX « notre temps moyen de détection est passé de 48h à 4h grâce à l'investissement EDR » parle le langage du résultat.

Comment l'IR alimente la revue des risques : chaque incident est un retex qui met à jour le registre des risques — le scénario S1 de l'EBIOS RM s'est réalisé, le PTR est ajusté, les contrôles sont renforcés, et la prochaine revue de direction intègre les leçons.

---

### Chapitre 31 — Cas complet : construction d'un programme de sécurité de 0 (synthèse COMPLIANCE)

Synthèse du fil rouge — 18 mois de construction du programme sécurité de Néoforma.

**M0-M3 — Fondations :** nomination RSSI, état des lieux (CIS IG1 : 40 % couvert), PSSI rédigée et signée, comité de sécurité lancé, DPO nommé, quick wins démarrés (MFA, EDR, sauvegardes immutables), début EBIOS RM.

**M3-M6 — Analyse et conformité :** EBIOS RM complété (3 scénarios critiques, PTR validé et signé par le COMEX), registre RGPD (12 traitements identifiés, AIPD réalisée pour la plateforme SaaS), PAS envoyé aux 3 sous-traitants critiques, migration hébergeur HDS lancée, sensibilisation démarrée (première campagne phishing : 34 % de clic).

**M6-M12 — Implémentation :** PTR en exécution (85 % à M12), PCA/PRA construit et testé (1 test de restauration — échec partiel corrigé), premiers audits internes, migration cloud HDS terminée, DdA construite (78 contrôles applicables, 64 implémentés), pentest réalisé (3 vulnérabilités corrigées), homologation préparée et signée (avec réserves), assurance cyber souscrite.

**M12-M18 — Certification et maturité :** audit ISO 27001 Phase 1 (2 non-conformités mineures corrigées), Phase 2 (certification obtenue), premier exercice de crise (retex : templates COM créés, processus de notification formalisé), réserves d'homologation levées, et programme de sensibilisation mature (taux de clic : 8 %).

**Métriques d'évolution :** maturité CIS de 40 % à 82 %, taux de clic phishing de 34 % à 8 %, 3 risques critiques réduits à modérés, couverture EDR de 60 % à 100 %, certification ISO 27001 obtenue, HDS certifié, homologation signée, assurance cyber en place.

---

### Chapitre 32 — Cas complet : gestion de crise ransomware dans une ETI

Une ETI industrielle (800 employés, 2 sites, ERP cloud, production connectée) fait face à un ransomware le vendredi soir à 22h. L'attaquant a chiffré les serveurs de fichiers, l'ERP, et les postes de production. Demande de rançon : 2 M€.

Le cas traverse toutes les dimensions GRC. **Qualification** (sévérité P1 — activation cellule de crise). **Notification** (CNIL dans les 72h — données employés chiffrées ; ANSSI — NIS 2 entité importante, alerte précoce 24h). **Communication** interne (« ne touchez à rien ») et clients (« nos services sont temporairement indisponibles »). **Décision rançon** (ne pas payer — recommandation ANSSI, position assureur). **Activation PRA** (restauration depuis sauvegardes immutables — RTO 48h, RPO 4h — perte de 4h de données de production). **Coordination** (RSSI coordonne, SOC/IR technique, DPO notification, COM communication, assureur couverture frais de réponse). **Retex** (3 contrôles manquants identifiés — PAM, segmentation OT, monitoring 24/7 → PTR mis à jour, exercice de crise annuel instauré).

---

### Chapitre 33 — Cas complet : mise en conformité NIS 2 pour un opérateur

Un opérateur de services postaux (entité importante NIS 2, 3 000 employés, SI distribué sur 150 sites) doit se mettre en conformité NIS 2. Le cas couvre : gap analysis (état actuel vs exigences NIS 2 art.21 — 60 % couvert), plan de mise en conformité (24 mois, 5 chantiers : gouvernance, incidents, continuité, supply chain, formation), analyse de risques EBIOS RM orientée NIS 2 (les scénarios de l'atelier 2 sont calibrés sur les menaces sectorielles — ransomware ciblant la logistique, compromission d'un sous-traitant IT), gestion de la supply chain (50 sous-traitants IT dont 10 critiques — évaluation, scoring, PAS, revue annuelle), notification d'incident (mise en place du processus 24h/72h/1 mois avec l'ANSSI), et programme de formation (obligation NIS 2 — sensibilisation direction + formation équipes IT + exercice de crise). Le cas illustre le volume de travail et la nécessité d'une approche structurée.

---

## ANNEXES

---

### Annexe A — Glossaire GRC

| Terme | Définition |
|-------|-----------|
| **AIPD / DPIA** | Analyse d'Impact relative à la Protection des Données (art.35 RGPD) |
| **BIA** | Business Impact Analysis — analyse d'impact sur l'activité |
| **CASB** | Cloud Access Security Broker — contrôle des accès cloud |
| **CIS Controls** | 18 contrôles de sécurité priorisés (Center for Internet Security) |
| **CMDB** | Configuration Management Database — inventaire des actifs |
| **COMEX** | Comité Exécutif — direction générale |
| **DdA / SoA** | Déclaration d'Applicabilité / Statement of Applicability (ISO 27001) |
| **DORA** | Digital Operational Resilience Act — réglementation financière UE |
| **DPO** | Data Protection Officer — délégué à la protection des données |
| **EBIOS RM** | Expression des Besoins et Identification des Objectifs de Sécurité — Risk Manager |
| **FAIR** | Factor Analysis of Information Risk — méthode quantitative de risque |
| **HDS** | Hébergement de Données de Santé — certification française |
| **Homologation** | Décision formelle d'autoriser l'exploitation d'un SI en connaissance des risques |
| **IAM** | Identity and Access Management — gestion des identités et des accès |
| **II 901** | Instruction Interministérielle n°901 — SI sensibles / Diffusion Restreinte |
| **ISO 27001** | Standard international de certification d'un SMSI |
| **ISO 27002** | Catalogue de 93 mesures de sécurité (version 2022) |
| **ISO 27005** | Cadre générique d'analyse de risques aligné ISO 27001 |
| **KPI** | Key Performance Indicator — indicateur clé de performance |
| **MFA** | Multi-Factor Authentication — authentification multi-facteur |
| **MTTD / MTTR** | Mean Time to Detect / Mean Time to Respond |
| **NIS 2** | Network and Information Security Directive v2 (UE 2022/2555) |
| **NIST CSF** | Cybersecurity Framework du NIST (v2.0, 2024) |
| **OIV** | Opérateur d'Importance Vitale (France) |
| **PAM** | Privileged Access Management — gestion des accès privilégiés |
| **PAS** | Plan d'Assurance Sécurité — exigences de sécurité pour un prestataire |
| **PASSI** | Prestataire d'Audit de SSI Qualifié (ANSSI) |
| **PCA / PRA** | Plan de Continuité / Plan de Reprise d'Activité |
| **PDCA** | Plan-Do-Check-Act — cycle d'amélioration continue |
| **PSSI** | Politique de Sécurité des Systèmes d'Information |
| **PTR** | Plan de Traitement des Risques |
| **RACI** | Responsible, Accountable, Consulted, Informed — matrice de responsabilités |
| **RGS** | Référentiel Général de Sécurité (secteur public français) |
| **RGPD** | Règlement Général sur la Protection des Données (UE 2016/679) |
| **RPO / RTO** | Recovery Point Objective / Recovery Time Objective |
| **RSSI / CISO** | Responsable de la Sécurité des Systèmes d'Information |
| **SecNumCloud** | Qualification ANSSI pour les prestataires de cloud sécurisé |
| **Shadow IT** | Applications et services IT non référencés par la DSI |
| **SIIV** | Système d'Information d'Importance Vitale |
| **SMSI / ISMS** | Système de Management de la Sécurité de l'Information |
| **SOC 2** | Service Organization Control Type 2 — rapport d'audit de contrôles |
| **Waiver** | Exception formalisée à un contrôle de sécurité |

---

### Annexe B — Templates de livrables GRC

#### Structure type PSSI (sommaire)

```
1. Contexte et périmètre
2. Engagement de la direction (signature DG)
3. Objectifs de sécurité
4. Principes directeurs
5. Organisation et responsabilités (RACI)
6. Classification des données
7. Règles par domaine
   7.1 Gestion des accès
   7.2 Sécurité réseau
   7.3 Sécurité des endpoints
   7.4 Sécurité cloud
   7.5 Protection des données
   7.6 Gestion des tiers
   7.7 Gestion des incidents
   7.8 Continuité d'activité
8. Gestion des exceptions
9. Sanctions
10. Revue et mise à jour
Annexe : glossaire, contacts, références
```

#### Registre des risques (colonnes)

```
ID | Description | Actif | Menace | Vulnérabilité | Vraisemblance (1-4) | 
Impact (1-4) | Niveau | Traitement (réduire/transférer/éviter/accepter) | 
Contrôle(s) | Propriétaire | Statut | Risque résiduel | Date revue
```

#### Fiche incident (structure)

```
FICHE INCIDENT #[numéro]
Sévérité : [P1/P2/P3/P4]    Date détection : [date UTC]
Détecté par : [SOC/utilisateur/tiers]

RÉSUMÉ : [2 lignes — quoi, qui, impact]
TIMELINE : [horodaté — chaque événement clé]
ACTIONS PRISES : [confinement, éradication, communication]
NOTIFICATION : [CNIL ? ANSSI ? Clients ?]
IMPACT : [données, services, financier, réglementaire]
CAUSE RACINE : [identifiée / en cours]
ACTIONS CORRECTIVES : [registre risques mis à jour ?]
RETEX : [ce qui a fonctionné / échoué / à améliorer]
```

---

### Annexe C — Evidence pack : preuves par contrôle

| Contrôle | Preuve attendue | Fréquence | Propriétaire |
|----------|----------------|-----------|-------------|
| MFA | Export IAM + config conditional access | Trimestrielle | IT / IAM |
| Patching | Rapport scan + tickets fermés + taux SLA | Mensuelle | SecOps |
| Sauvegardes | PV test restauration + RPO/RTO mesurés | Semestrielle | IT / Infra |
| Revue accès | CR signé + captures avant/après + actions | Trimestrielle | Propriétaires données |
| Sensibilisation | Attestations + résultats phishing + tendance | Annuelle + continue | RSSI / RH |
| Incidents | Fiches traitées + timeline + retex + MTTD/MTTR | Continue | SOC / RSSI |
| Changes | Tickets avec approbation + validation post-change | Continue | Change Manager |
| SIEM | Dashboard sources connectées + règles + alertes | Mensuelle | SOC |
| Scan vulnérabilités | Rapports + tendances + exceptions documentées | Mensuelle | SecOps |
| Segmentation | Schéma réseau + règles FW + tests de flux | Annuelle | Réseau |
| Classification | Registre classifié + politique appliquée | Annuelle | Propriétaires données |
| Tiers | Questionnaires + PAS + revues annuelles | Annuelle | RSSI / Achats |
| Exercice crise | CR + participants + retex + actions correctives | Annuelle | RSSI / DG |
| PSSI | Versionnée + signée + diffusée + formation | Annuelle | RSSI / DG |
| Analyse risques | Registre + PTR + CR revue direction | Annuelle + trimestrielle | RSSI |
| Homologation | Dossier complet + décision signée + suivi réserves | Selon validité (3 ans) | Autorité d'homologation |

---

### Annexe D — Top 20 contrôles à plus fort ROI

| # | Contrôle | Pourquoi prioritaire | Effort |
|---|----------|---------------------|--------|
| 1 | Inventaire actifs | On ne protège pas ce qu'on ne connaît pas | Moyen |
| 2 | MFA admin + accès distants | Bloque >90 % des compromissions de comptes | Faible |
| 3 | Patching automatisé | Vulnérabilités connues = vecteur #1 | Moyen |
| 4 | Sauvegardes 3-2-1 + immutables | Anti-ransomware | Moyen |
| 5 | EDR endpoints + serveurs | Détection et réponse | Moyen |
| 6 | Logs centralisés (SIEM) | Pas de détection sans logs | Élevé |
| 7 | Segmentation réseau | Limite le mouvement latéral | Élevé |
| 8 | Politique MdP + gestionnaire | MdP faibles = porte ouverte | Faible |
| 9 | Sensibilisation continue | Facteur humain = maillon #1 | Faible |
| 10 | Hardening AD (tiering) | AD compromis = tout compromis | Élevé |
| 11 | Plan incident + contacts | Savoir quoi faire AVANT la crise | Faible |
| 12 | Revue accès trimestrielle | Droits cumulés = risque cumulé | Moyen |
| 13 | Gestion tiers + PAS | Supply chain = surface #1 | Moyen |
| 14 | Chiffrement transit + repos | Obligation + protection | Moyen |
| 15 | Désactivation services inutiles | Réduire la surface | Faible |
| 16 | Use cases SIEM (5-10 règles) | Logs sans règles = bruit | Moyen |
| 17 | Scan vuln + SLA remédiation | Identifier avant l'attaquant | Moyen |
| 18 | Exercice crise annuel | Tester avant la vraie crise | Faible |
| 19 | Classification données | Adapter protection à sensibilité | Moyen |
| 20 | Assurance cyber | Transférer le risque financier résiduel | Moyen |

*Les 5 premiers couvrent la majorité du risque — commencer par eux crédibilise le RSSI et débloque le budget.*

---

### Annexe E — Mapping réglementaire

| Exigence | RGPD | NIS 2 | ISO 27001 | DORA | HDS |
|----------|:---:|:---:|:---:|:---:|:---:|
| Analyse de risques | Art.32 (implicite) | Art.21 | Clause 6.1 | Art.6 | Oui |
| Politique de sécurité | Art.32 | Art.21 | Clause 5.2 | Art.6 | Oui |
| Gestion des incidents | Art.33-34 | Art.23 | A.5.24-28 | Art.17 | Oui |
| Continuité / PCA | Art.32 (restauration) | Art.21 | A.5.29-30 | Art.11-12 | Oui |
| Supply chain / tiers | Art.28 (sous-traitant) | Art.21 | A.5.19-23 | Art.28-30 | Oui |
| Chiffrement | Art.32 (mesure) | Art.21 | A.8.24 | Art.6 | Oui |
| Contrôle d'accès | Art.32 (mesure) | Art.21 | A.8.1-5 | Art.6 | Oui |
| Sensibilisation | Art.39 (DPO) | Art.21 | A.6.3 | Art.13 | Oui |
| Notification incident | 72h CNIL | 24h/72h/1m ANSSI | Interne | Selon classif. | Oui |
| Responsabilité dirigeants | — | Art.20 | Clause 5.1 | Art.5 | — |
| Sanctions | 20M€ / 4% CA | 10M€ / 2% (EE) | Retrait certif. | Variables | Retrait certif. |

---

### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Gouvernance, risques, conformité | **Ce cours (GRC)** | — |
| Threat intelligence (menaces, acteurs) | **Cours CTI** | GRC (Ch.8 EBIOS RM atelier 2 — sources de risque alimentées par la CTI) |
| Acteurs APT (profils, campagnes) | **Cours APT** | GRC (Ch.8 — les sources de risque sont les acteurs du cours APT) |
| Détection SOC (SIEM, investigation) | **Cours SOC** | GRC (Ch.9 — indicateurs SOC dans le dashboard COMEX, Ch.28 convergence) |
| Incident Response (technique) | **Cours IR** | GRC (Ch.20 gestion incidents vue GRC, Ch.22 gestion de crise) |
| Forensic numérique | **Cours Forensic** | GRC (Ch.20 — préservation des preuves) |
| Intelligence économique | **Cours IE** | GRC (Ch.19 sécurité contractuelle, Ch.24 tiers) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | GRC (Ch.8 — scénarios ransomware dans l'EBIOS RM) |
| OSINT | **Cours OSINT** | GRC (Ch.17 — sensibilisation, social engineering) |
| Windows / AD | **Cours Windows / AD** | GRC (Ch.16 IAM, Ch.18 patching) |

---

### Annexe G — Ressources et formation

#### Certifications

| Certification | Organisme | Focus | Niveau |
|--------------|-----------|-------|--------|
| ISO 27001 Lead Implementer | PECB / BSI | Mettre en place un SMSI | Intermédiaire |
| ISO 27001 Lead Auditor | PECB / BSI | Auditer un SMSI | Intermédiaire |
| CISSP | (ISC)² | Sécurité globale (8 domaines) | Avancé |
| CISM | ISACA | Management de la sécurité | Avancé |
| CRISC | ISACA | Gestion des risques IT | Avancé |
| CISA | ISACA | Audit des SI | Avancé |
| EBIOS RM | ANSSI / Club EBIOS | Analyse de risques | Intermédiaire |
| DPO / RGPD | CNIL / organismes agréés | Protection des données | Intermédiaire |
| CompTIA Security+ | CompTIA | Fondamentaux sécurité | Débutant |

#### Organismes et ressources

| Organisme | Ressource | URL |
|-----------|----------|-----|
| **ANSSI** | Guides, EBIOS RM, hygiène, SecNumCloud, PASSI | cyber.gouv.fr |
| **CNIL** | Guides RGPD, AIPD, registre, outils PIA | cnil.fr |
| **ENISA** | Guides NIS 2, threat landscape, bonnes pratiques | enisa.europa.eu |
| **NIST** | CSF v2.0, SP 800-53, SP 800-61, FAIR | nist.gov |
| **ISO** | 27001, 27002, 27005, 22301 | iso.org |
| **CIS** | CIS Controls v8, CIS Benchmarks | cisecurity.org |
| **MITRE** | ATT&CK, D3FEND | attack.mitre.org |
| **Club EBIOS** | Communauté EBIOS RM, retours d'expérience | club-ebios.org |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former au pilotage de la sécurité par la gouvernance, le risque, et la conformité — le cadre qui donne sens à la technique et qui permet au RSSI de parler le langage de la direction.
>
> L'opération COMPLIANCE illustre cette ambition : Marine ne déploie pas des outils — elle construit un programme. Elle ne coche pas des cases — elle réduit des risques. Elle ne rédige pas des documents — elle produit des décisions. La PSSI n'est pas un fichier Word — c'est un engagement signé par le DG. L'analyse de risques n'est pas un exercice académique — c'est l'outil qui débloque le budget. L'homologation n'est pas un tampon — c'est la décision formelle d'accepter de vivre avec les risques résiduels.
>
> Le cours assume trois convictions. Première : la conformité sans sécurité est un leurre — cocher les cases d'un référentiel ne protège pas. Deuxième : la sécurité sans gouvernance est fragile — les contrôles techniques sans politique, sans budget, et sans arbitrage se dégradent. Troisième : le risque sans décision formelle est de la négligence — accepter un risque est un acte de management, pas un oubli.
>
> *Gouverner • Évaluer • Se conformer • Protéger • Décider — avec rigueur et pragmatisme.*
