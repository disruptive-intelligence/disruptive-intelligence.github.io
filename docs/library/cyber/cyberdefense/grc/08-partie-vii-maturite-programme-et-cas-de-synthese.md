---
title: Partie VII — Maturité, programme ET cas de synthèse
source: Cyber/05_Cyberdefense/GRC.md
note: GRC
up:
- - GRC
  - index.md
---

---


## Chapitre 28 — Construire un programme de sécurité

Par où commencer : évaluation de maturité initiale (CIS Controls IG1 comme benchmark rapide, NIST CSF tier assessment pour le positionnement). Les **10 quick wins** à impact maximal : (1) inventaire des actifs, (2) MFA sur tous les accès admin et distants, (3) patching automatisé, (4) sauvegardes 3-2-1 + immutables, (5) EDR sur tous les endpoints et serveurs, (6) logs centralisés, (7) politique de mots de passe + gestionnaire, (8) sensibilisation continue, (9) plan d'incident + contacts d'urgence, (10) segmentation réseau. Les 5 premiers couvrent la majorité du risque — commencer par eux crédibilise le RSSI et débloque le budget.

La roadmap sécurité (plan à 1 an et 3 ans avec jalons, budget, et responsables). Le budget (justification en langage business : coût de l'incident vs coût de la prévention, obligations réglementaires, exigences contractuelles des clients, prérequis assureurs ; benchmark : 5-15 % du budget IT). Les modèles d'organisation (SOC interne vs MSSP, RSSI interne vs temps partagé vs vCISO — avantages, inconvénients, adaptés à quels contextes).

---


## Chapitre 29 — Modèles de maturité et amélioration continue

Les modèles de maturité : **Niveau 1 — Initial** (ad hoc, pas de processus formalisé, la sécurité dépend des individus), **Niveau 2 — Répétable** (des processus existent pour les activités principales, mais pas systématiques), **Niveau 3 — Défini** (processus documentés, appliqués, et mesurés — c'est le niveau ISO 27001), **Niveau 4 — Géré** (indicateurs quantitatifs, amélioration pilotée par les données), **Niveau 5 — Optimisé** (amélioration continue intégrée, anticipation, innovation).

L'auto-évaluation (CIS Controls IG assessment, NIST CSF tier assessment — comment la conduire, quoi en faire). Le programme d'amélioration continue (PDCA appliqué : indicateurs → revue → actions correctives → contrôles améliorés → re-mesure ; retex post-incident comme moteur d'amélioration ; purple team et tests de contrôles comme validation).

---


## Chapitre 30 — GRC et cybersécurité opérationnelle : la convergence

Ce chapitre fait le pont entre la GRC et la sécurité technique — la convergence que la bibliothèque rend possible.

Comment l'analyse de risques alimente la CTI : les sources de risque de l'atelier 2 EBIOS RM sont les acteurs du cours APT — la CTI fournit le renseignement qui rend l'analyse de risques concrète et **threat-informed** plutôt qu'abstraite. Un scénario EBIOS RM qui dit « un attaquant sophistiqué cible nos données de santé » est générique. Un scénario qui dit « APT41 cible les éditeurs SaaS santé européens avec exploitation de vulnérabilités web et mouvement latéral vers les bases de données — cf. campagne X documentée par Mandiant » est actionnable.

Comment les indicateurs GRC se nourrissent du SOC : le MTTD, le MTTR, le taux de FP, la couverture ATT&CK sont des indicateurs opérationnels (cours SOC) qui remontent dans le dashboard COMEX (Ch.9). Le RSSI qui présente au COMEX « notre temps moyen de détection est passé de 48h à 4h grâce à l'investissement EDR » parle le langage du résultat.

Comment l'IR alimente la revue des risques : chaque incident est un retex qui met à jour le registre des risques — le scénario S1 de l'EBIOS RM s'est réalisé, le PTR est ajusté, les contrôles sont renforcés, et la prochaine revue de direction intègre les leçons.

---


## Chapitre 31 — Cas complet

construction d'un programme de sécurité de 0 (synthèse COMPLIANCE)

Synthèse du fil rouge — 18 mois de construction du programme sécurité de Néoforma.

**M0-M3 — Fondations :** nomination RSSI, état des lieux (CIS IG1 : 40 % couvert), PSSI rédigée et signée, comité de sécurité lancé, DPO nommé, quick wins démarrés (MFA, EDR, sauvegardes immutables), début EBIOS RM.

**M3-M6 — Analyse et conformité :** EBIOS RM complété (3 scénarios critiques, PTR validé et signé par le COMEX), registre RGPD (12 traitements identifiés, AIPD réalisée pour la plateforme SaaS), PAS envoyé aux 3 sous-traitants critiques, migration hébergeur HDS lancée, sensibilisation démarrée (première campagne phishing : 34 % de clic).

**M6-M12 — Implémentation :** PTR en exécution (85 % à M12), PCA/PRA construit et testé (1 test de restauration — échec partiel corrigé), premiers audits internes, migration cloud HDS terminée, DdA construite (78 contrôles applicables, 64 implémentés), pentest réalisé (3 vulnérabilités corrigées), homologation préparée et signée (avec réserves), assurance cyber souscrite.

**M12-M18 — Certification et maturité :** audit ISO 27001 Phase 1 (2 non-conformités mineures corrigées), Phase 2 (certification obtenue), premier exercice de crise (retex : templates COM créés, processus de notification formalisé), réserves d'homologation levées, et programme de sensibilisation mature (taux de clic : 8 %).

**Métriques d'évolution :** maturité CIS de 40 % à 82 %, taux de clic phishing de 34 % à 8 %, 3 risques critiques réduits à modérés, couverture EDR de 60 % à 100 %, certification ISO 27001 obtenue, HDS certifié, homologation signée, assurance cyber en place.

---


## Chapitre 32 — Cas complet : gestion de crise ransomware dans une ETI

Une ETI industrielle (800 employés, 2 sites, ERP cloud, production connectée) fait face à un ransomware le vendredi soir à 22h. L'attaquant a chiffré les serveurs de fichiers, l'ERP, et les postes de production. Demande de rançon : 2 M€.

Le cas traverse toutes les dimensions GRC. **Qualification** (sévérité P1 — activation cellule de crise). **Notification** (CNIL dans les 72h — données employés chiffrées ; ANSSI — NIS 2 entité importante, alerte précoce 24h). **Communication** interne (« ne touchez à rien ») et clients (« nos services sont temporairement indisponibles »). **Décision rançon** (ne pas payer — recommandation ANSSI, position assureur). **Activation PRA** (restauration depuis sauvegardes immutables — RTO 48h, RPO 4h — perte de 4h de données de production). **Coordination** (RSSI coordonne, SOC/IR technique, DPO notification, COM communication, assureur couverture frais de réponse). **Retex** (3 contrôles manquants identifiés — PAM, segmentation OT, monitoring 24/7 → PTR mis à jour, exercice de crise annuel instauré).

---


## Chapitre 33 — Cas complet : mise en conformité NIS 2 pour un opérateur

Un opérateur de services postaux (entité importante NIS 2, 3 000 employés, SI distribué sur 150 sites) doit se mettre en conformité NIS 2. Le cas couvre : gap analysis (état actuel vs exigences NIS 2 art.21 — 60 % couvert), plan de mise en conformité (24 mois, 5 chantiers : gouvernance, incidents, continuité, supply chain, formation), analyse de risques EBIOS RM orientée NIS 2 (les scénarios de l'atelier 2 sont calibrés sur les menaces sectorielles — ransomware ciblant la logistique, compromission d'un sous-traitant IT), gestion de la supply chain (50 sous-traitants IT dont 10 critiques — évaluation, scoring, PAS, revue annuelle), notification d'incident (mise en place du processus 24h/72h/1 mois avec l'ANSSI), et programme de formation (obligation NIS 2 — sensibilisation direction + formation équipes IT + exercice de crise). Le cas illustre le volume de travail et la nécessité d'une approche structurée.

---
