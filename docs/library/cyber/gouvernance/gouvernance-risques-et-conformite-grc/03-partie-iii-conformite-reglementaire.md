---
title: Partie III — Conformité réglementaire
source: Cyber/08 Gouvernance & résilience/Gouvernance & conformité/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - index.md
---

*Ce que la loi exige — et comment transformer l'obligation en levier de sécurité réelle.*

---


## Chapitre 10 — RGPD : obligations et articulation sécurité

Le RGPD n'est pas qu'un sujet juridique — c'est un sujet sécurité. L'article 32 impose des mesures techniques et organisationnelles « appropriées » (chiffrement, pseudonymisation, capacité de restauration, tests) — proportionnelles au risque. La notification de violation (art.33-34 — 72h CNIL + personnes si risque élevé) est un processus IR. L'AIPD (art.35) est une analyse de risques. Le cours traite le RGPD sous cet angle opérationnel.

Les **7 principes** (licéité/loyauté/transparence, limitation des finalités, minimisation, exactitude, limitation de conservation, intégrité/confidentialité, responsabilisation). Les **6 bases légales** (consentement, contrat, obligation légale, intérêts vitaux, intérêt public, intérêt légitime). Les **droits des personnes** (accès, rectification, effacement, portabilité, opposition, limitation, non-profilage — processus interne obligatoire, délai 1 mois). Les **obligations clés** : registre des traitements (art.30), AIPD/DPIA (art.35 — obligatoire pour les traitements à risque, notamment les données de santé à grande échelle), DPO (art.37 — obligatoire si autorité publique ou données sensibles à grande échelle), Privacy by Design (art.25), et notification de violation (art.33-34). **Sanctions** : jusqu'à 20 M€ ou 4 % du CA mondial.

Fil rouge : Néoforma traite des données de santé (art.9) de 3 millions de patients — AIPD obligatoire, DPO nommé, hébergement HDS requis, notification 72h en cas de violation. Marine articule la mise en conformité RGPD avec le programme de sécurité global.

---


## Chapitre 11 — NIS 2 : la directive qui change tout

NIS 2 (Network and Information Security Directive v2, 2022/2555) est la directive européenne de cybersécurité qui remplace NIS 1. Élargissement massif du périmètre : 18 secteurs, 2 catégories (entités essentielles — grandes entreprises + secteurs critiques : énergie, transports, santé, eau, infra numérique, espace ; entités importantes — moyennes entreprises + secteurs importants : postaux, chimie, alimentation, fabrication, fournisseurs numériques), critères de taille harmonisés.

**Obligations de sécurité** (art.21) : analyse de risques, gestion des incidents (détection, qualification, réponse), continuité d'activité (PCA, PRA, sauvegardes, tests), sécurité de la supply chain (évaluation des fournisseurs — rendu obligatoire), chiffrement et contrôle d'accès, hygiène et formation, et politiques de sécurité formalisées. **Notification d'incident** (art.23) : alerte précoce 24h (« quelque chose se passe »), notification 72h (« voici ce qui s'est passé »), rapport final 1 mois (« voici l'analyse complète, les causes, les mesures »). Autorité compétente en France : ANSSI. **Sanctions** : EE jusqu'à 10 M€ ou 2 % du CA ; EI jusqu'à 7 M€ ou 1,4 % du CA. **Responsabilité des dirigeants** : NIS 2 engage personnellement les dirigeants — une première.

**NIS 2 vs RGPD vs ISO 27001 :** les trois se recoupent partiellement (analyse de risques, gestion des incidents, mesures techniques) mais avec des angles différents (RGPD = données personnelles, NIS 2 = continuité des services essentiels, ISO 27001 = management de la sécurité). Une organisation qui fait son ISO 27001 sérieusement est largement en conformité NIS 2.

---


## Chapitre 12 — DORA et réglementations sectorielles

**DORA** (Digital Operational Resilience Act — règlement UE 2022/2554, applicable janvier 2025) est la réglementation de résilience opérationnelle numérique pour le secteur financier. Périmètre : établissements financiers (banques, assurances, sociétés de gestion) + prestataires TIC critiques. Exigences : gestion des risques TIC (cadre formalisé, mis à jour), gestion des incidents TIC (classification, notification, reporting), tests de résilience (tests d'intrusion TLPT pour les entités significatives), gestion des tiers TIC (registre, évaluation, clauses contractuelles spécifiques, stratégie de sortie), et partage d'information (échange de renseignement sur les menaces). DORA vs NIS 2 : DORA est lex specialis pour le secteur financier (il prime sur NIS 2 pour les entités financières).

**HDS** (Hébergement de Données de Santé) : certification ANSSI obligatoire pour tout hébergeur de données de santé à caractère personnel en France. Basée sur ISO 27001 + exigences spécifiques santé. Processus : audit de certification par un organisme accrédité. **PCI-DSS v4.0** : 12 exigences pour la protection des données de carte de paiement, 4 niveaux de conformité selon le volume de transactions (SAQ pour les petits commerçants, ROC pour les grands). **II 901** (Instruction Interministérielle n°901) : cadre de sécurité pour les SI sensibles du secteur public (classification Diffusion Restreinte). **RGS** (Référentiel Général de Sécurité) : obligations de sécurité pour les administrations et les téléservices publics. **AI Act** (règlement UE 2024) : classification des systèmes d'IA par niveau de risque (inacceptable, élevé, limité, minimal), obligations par catégorie, lien avec la GRC (les systèmes IA « élevé risque » nécessitent une analyse de risques, un système de management qualité, et une documentation technique).

---


## Chapitre 13 — Audits et certification ISO 27001

### 13.1 Types d'audits

L'**audit interne** est une auto-évaluation structurée : l'organisation vérifie elle-même la conformité de ses contrôles (exigence ISO 27001 — au moins un audit interne par cycle). L'**audit externe de certification** ISO 27001 se déroule en 2 phases : Phase 1 (revue documentaire — la documentation existe-t-elle ? PSSI, DdA, analyse de risques, PTR, procédures) et Phase 2 (audit terrain — les contrôles sont-ils effectivement implémentés ? Interviews, observations, preuves). L'**audit réglementaire** (contrôle CNIL, ANSSI) vérifie la conformité aux obligations légales. L'**audit client** (questionnaire sécurité, droit d'audit) est exigé par les clients — de plus en plus fréquent dans les appels d'offres.

### 13.2 Dire vs prouver

La politique existe ≠ la politique est appliquée. L'auditeur demande des preuves : MFA → export IAM avec taux d'activation, patching → rapport de scan + tickets de remédiation fermés, revue des accès → CR signé + captures avant/après, sauvegardes → PV de test de restauration daté, sensibilisation → attestations + résultats phishing, incidents → fiches traitées + retex documenté, SIEM → dashboard des sources connectées + alertes traitées. L'Annexe C fournit le tableau complet « evidence pack ».

### 13.3 La certification ISO 27001 pas à pas

Phase 1 (1-2 jours sur site) : l'auditeur vérifie que la documentation est complète et cohérente (PSSI, DdA, analyse de risques, PTR, procédures, registre des risques, PV de revue de direction). Phase 2 (3-5 jours sur site, 4-8 semaines après Phase 1) : interviews des responsables, vérification des preuves d'implémentation, tests sur un échantillon de contrôles. Les non-conformités : **majeure** (contrôle manquant ou systémiquement défaillant — bloque la certification), **mineure** (écart ponctuel — plan d'action requis), **observation** (point d'amélioration — pas bloquant). Surveillance annuelle (1-2 jours). Recertification tous les 3 ans (audit complet).

---


## Chapitre 14 — Déclaration d'applicabilité et gestion des exceptions

### 14.1 La DdA / SoA

La Déclaration d'Applicabilité (Statement of Applicability) est le document ISO 27001 obligatoire qui fait le pont entre l'analyse de risques et les contrôles. Pour chaque mesure de l'Annexe A (93 mesures ISO 27002:2022) : applicable ou non ? Si applicable : implémentée ? Si non implémentée : plan d'action avec échéance. Si non applicable : justification (« nous ne traitons pas de données de carte bancaire → PCI-DSS non applicable »). C'est le document que l'auditeur lit en premier.

### 14.2 La gestion des exceptions (waivers)

Certains contrôles ne peuvent pas être implémentés immédiatement (contrainte technique, coût, délai). La gestion des exceptions formalise ces dérogations. Chaque exception est : temporaire (date de début, date d'expiration — une exception sans date est un abandon), documentée (contrôle concerné, justification technique ou business, risque résiduel accepté, mesures compensatoires mises en place), signée (par le propriétaire du risque — un membre de la direction, pas le RSSI), et revue trimestriellement (échéance dépassée = renouvellement formel ou implémentation).

Les **contrôles compensatoires** : quand un contrôle requis n'est pas faisable, un contrôle alternatif visant le même objectif peut être mis en place (chiffrement de la base de données impossible car système legacy → segmentation réseau renforcée + contrôle d'accès strict + monitoring dédié + chiffrement au niveau disque).

---


## Chapitre 15 — Homologation de sécurité

décider, documenter, maintenir

### 15.1 Qu'est-ce que l'homologation

L'homologation de sécurité est la **décision formelle** d'autoriser la mise en service ou le maintien en exploitation d'un système d'information, en connaissance de cause des risques résiduels. Ce n'est pas un audit, ce n'est pas une certification, ce n'est pas une simple acceptation de risque ponctuelle — c'est l'acte par lequel une autorité déclare : « j'ai compris les risques résiduels de ce SI, j'ai évalué que les mesures de sécurité en place sont suffisantes par rapport à l'usage prévu, et j'autorise son exploitation dans ces conditions ».

L'homologation est un processus central en GRC, particulièrement dans les environnements publics, sensibles, régulés, ou avec exigences client fortes. En France, elle est obligatoire pour les SI traitant d'informations classifiées ou Diffusion Restreinte (II 901), pour les SI des OIV (SIIV — Systèmes d'Information d'Importance Vitale), pour les SI des administrations (RGS), et de facto exigée dans de nombreux appels d'offres publics et pour les SI de santé.

### 15.2 Homologation vs certification vs conformité vs acceptation de risque

La **certification** (ISO 27001, HDS) prouve qu'un système de management est conforme à un référentiel — elle est délivrée par un tiers indépendant et porte sur le système de management, pas sur un SI spécifique. La **conformité** vérifie le respect d'une réglementation (RGPD, NIS 2) — elle est continue et porte sur des obligations. L'**acceptation de risque** est une décision ponctuelle portant sur un risque individuel (« j'accepte le risque de ne pas avoir de MFA sur ce serveur legacy pendant 6 mois »). L'**homologation** est une décision globale portant sur un SI complet (« j'autorise l'exploitation de la plateforme SaaS Néoforma dans sa configuration actuelle, avec ses risques résiduels identifiés, pour une durée de 3 ans »). L'homologation intègre l'analyse de risques, la conformité, les audits, et les exceptions — c'est la synthèse décisionnelle.

### 15.3 Les acteurs

L'**autorité d'homologation** est le responsable qui signe la décision — un membre de la direction (DG, DSI, directeur métier), jamais le RSSI (qui conseille mais ne décide pas). Le **RSSI** prépare le dossier, conduit l'analyse de risques, évalue les contrôles, et recommande. L'**exploitant** (DSI, équipe d'exploitation) fournit la documentation technique. Les **métiers** expriment les besoins et les contraintes d'usage. Les **auditeurs** (internes ou externes) vérifient la réalité des contrôles.

### 15.4 Le dossier d'homologation

Le dossier comprend : la description du SI (périmètre, architecture, données traitées, utilisateurs, interconnexions), l'analyse de risques (EBIOS RM ou équivalent — Ch.7-8), le plan de traitement des risques (PTR — mesures décidées, responsables, échéances), la DdA/SoA (contrôles applicables, implémentés, et justifications), les résultats d'audit (audit interne, pentest, audit de conformité), les risques résiduels explicites (ce qui reste après traitement — chaque risque est décrit, évalué, et assumé), les exceptions actives (avec mesures compensatoires et échéances), et la recommandation du RSSI (homologation sans réserve, avec réserves, provisoire, ou refus).

### 15.5 La décision d'homologation

4 issues possibles. **Homologation sans réserve** : les risques résiduels sont acceptables, les contrôles sont satisfaisants, le SI peut être exploité dans les conditions définies. **Homologation avec réserves** : les risques résiduels sont acceptables sous certaines conditions (actions à mener dans un délai défini — si les réserves ne sont pas levées, l'homologation est suspendue). **Homologation provisoire** : le SI peut être exploité pour une durée limitée (3-6 mois) le temps de mettre en œuvre des actions correctives. **Refus d'homologation** : les risques résiduels sont inacceptables — le SI ne peut pas être mis en service ou doit être arrêté.

### 15.6 Maintien et ré-homologation

L'homologation a une durée de validité (typiquement 3 ans). Elle doit être **révisée** en cas de changement majeur (nouvelle fonctionnalité, changement d'hébergeur, nouvelle interconnexion, incident de sécurité significatif, évolution réglementaire) et **renouvelée** à échéance (nouveau cycle d'analyse de risques, d'audit, et de décision). Le suivi des réserves et des actions correctives est intégré au comité de sécurité (Ch.4).

### 15.7 Fil rouge — COMPLIANCE : l'homologation Néoforma

> **📊 COMPLIANCE — Épisode 4**
>
> À M12, Marine prépare le dossier d'homologation de la plateforme SaaS Néoforma. Le dossier comprend l'analyse EBIOS RM (Ch.8), le PTR avec 85 % des actions complétées, la DdA avec 64/78 contrôles implémentés (14 en plan d'action), les résultats du pentest (3 vulnérabilités corrigées, 1 acceptée avec compensatoire), et 2 exceptions actives (pas de segmentation micro sur les bases legacy — échéance M18, compensatoire : monitoring renforcé + ACL strictes). Recommandation RSSI : homologation avec réserves (lever les 2 exceptions avant M18). Le DG signe.

---
