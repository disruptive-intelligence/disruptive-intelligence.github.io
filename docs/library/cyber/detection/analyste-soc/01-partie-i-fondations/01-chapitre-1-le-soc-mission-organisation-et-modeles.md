---
title: 'Chapitre 1 — Le SOC : mission, organisation et modèles'
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 1.1 Définition opérationnelle

Le Security Operations Center est la structure qui assure la surveillance, la détection, l'investigation et la réponse aux incidents de sécurité en continu. Sa mission se résume en trois verbes : **détecter** (transformer les logs et les alertes en signaux exploitables), **investiguer** (comprendre ce qui s'est passé, avec quelle certitude), et **répondre** (contenir la menace, éradiquer, et restaurer).

Le SOC ne fait pas tout et c'est important de le poser d'emblée. Il ne définit pas la politique de sécurité (c'est le RSSI), ne réalise pas de tests d'intrusion (c'est le pentest/red team), ne gère pas les vulnérabilités au quotidien (c'est le vulnerability management, même si les frontières bougent — Ch.32), et ne mène pas les investigations forensiques approfondies (c'est le CERT/forensicien, traité dans le cours Forensic de la bibliothèque). Le SOC est le système nerveux central de la sécurité opérationnelle — il capte les signaux, les interprète, et déclenche les réponses de premier niveau.

## 1.2 Le modèle L1/L2/L3 — et ses évolutions

Le modèle classique organise le SOC en trois niveaux.

Le **L1 (Triage)** est le premier contact avec l'alerte. L'analyste L1 qualifie rapidement chaque alerte : vrai positif (VP — une menace réelle), faux positif (FP — alerte sans menace), benign true positive (BTP — l'alerte est techniquement correcte mais l'action est légitime), ou inconclusive (doute — nécessite investigation approfondie). Le L1 enrichit l'alerte (lookup IP, hash, utilisateur), applique le playbook de réponse si la qualification est claire, et escalade au L2 si l'investigation dépasse le triage. Compétences clés : lecture rapide de logs, connaissance des use cases, application des playbooks, rapidité de qualification.

Le **L2 (Investigation)** mène les investigations approfondies. L'analyste L2 reconstitue la séquence d'événements (timeline), corrèle les sources (endpoint + réseau + identité + cloud), pivote entre les entités (IP → hostname → user → process → hash), formule des hypothèses, et produit la conclusion argumentée. Le L2 exécute aussi les actions de confinement de premier niveau (isolation endpoint, blocage IoC, reset credentials). Compétences clés : pivoting, requêtes SIEM avancées, compréhension des TTP, raisonnement analytique.

Le **L3 (Expert)** couvre les fonctions avancées : detection engineering (écriture et maintenance des règles de détection), threat hunting (recherche proactive de menaces non détectées), forensique de premier niveau (collecte d'artefacts, analyse de malware first-pass), et purple teaming (validation des détections avec le red team).

**Ce modèle est pédagogiquement utile mais pas universel.** De nombreux SOC modernes adoptent des organisations différentes, mieux adaptées à leur contexte.

Le modèle **par rôle spécialisé** remplace les niveaux par des fonctions : des **analystes généralistes** (qui trient ET investiguent, sans séparation L1/L2 — souvent plus satisfaisant pour les analystes et plus efficace car l'investigateur a le contexte depuis le début), des **detection engineers** (qui écrivent, testent et maintiennent les règles — un rôle de plus en plus identifié et valorisé), des **hunters** (recherche proactive dédiée), des **incident responders** (réponse et confinement), et des **content engineers** (gestion du SIEM — parsing, normalisation, data quality).

Le modèle **squad/pod** organise de petites équipes pluridisciplinaires (1 detection engineer + 2-3 analystes + 1 hunter) assignées à un périmètre client ou technologique, avec une autonomie opérationnelle forte.

Le modèle **follow-the-sun** distribue les shifts entre plusieurs fuseaux horaires (SOC Paris 6h-14h, SOC Montréal 14h-22h, SOC Singapour 22h-6h) — chaque site travaille en journée plutôt qu'en nuit.

La tendance 2025-2026 est à la spécialisation par rôle (detection engineering et hunting comme fonctions distinctes) et à la réduction de la séparation L1/L2 (les analystes « full-stack » qui trient et investiguent sont plus efficaces et plus motivés que les L1 cantonnés au triage).

## 1.3 Les modèles de SOC

**SOC interne :** géré par l'entreprise. Avantage : connaissance fine du contexte métier (l'analyste connaît les processus, les utilisateurs, les applications). Inconvénient : coût (recrutement, formation, 24/7), difficulté à recruter et retenir les talents.

**SOC externalisé (MSSP) :** sous-traité à un prestataire de services managés. Avantage : mutualisation des coûts, expertise partagée, 24/7 natif. Inconvénient : moindre connaissance du contexte client (l'analyste MSSP gère 10-20 clients et ne connaît pas les spécificités métier de chacun).

**MDR (Managed Detection & Response) :** service managé combinant EDR + analystes. Le fournisseur MDR gère la détection et la réponse initiale (triage, confinement). Le client conserve la décision finale sur les actions impactantes. Avantage : rapidité de déploiement, expertise EDR native. Inconvénient : périmètre limité (souvent endpoint-centric, peu de corrélation avec les logs réseau, AD, ou cloud).

**Hybride :** le modèle le plus courant en 2025-2026. Le triage et la surveillance 24/7 sont externalisés (volume, nuits, week-ends), l'investigation L2/L3, le detection engineering, et le hunting sont internes (contexte, expertise, valeur ajoutée).

## 1.4 Les interactions du SOC

Le SOC n'opère pas en silo — il interagit avec toute l'organisation sécurité. Avec le **CERT/CSIRT** : escalade des incidents confirmés nécessitant une investigation approfondie, coordination de la réponse aux incidents majeurs, partage d'IoC. Avec le **RSSI** : reporting des métriques et des incidents, gouvernance des règles de détection, validation des exceptions. Avec l'**IT/Infra** : exécution des actions de confinement (isolation réseau, désactivation de compte), collecte de logs supplémentaires, patching coordonné. Avec la **CTI** : consommation des IoC et des TTP (feeds → SIEM), feedback sur les détections (FP, gaps), et contextualisation des incidents (cours CTI de la bibliothèque). Avec le **NOC** : corrélation des événements réseau, distinction entre incident de sécurité et incident de disponibilité. Avec les **métiers** : signalement d'activités suspectes, validation de la légitimité d'une action (« est-ce vous qui avez transféré ces fichiers vers Google Drive ? »).

## 1.5 Fil rouge — FALCONWATCH : le contexte

> **🛡️ FALCONWATCH — Épisode 1**
>
> Lundi 10 mars 2026, 07h42 UTC. Karim arrive à son poste de travail dans le SOC CyberShield (open space sécurisé, 8 analystes par shift, 4 écrans par poste — SIEM, EDR, ticketing, communication). Il prend le handover du shift de nuit : « Nuit calme, 12 alertes traitées, 0 escalade, backlog à 3 alertes en attente de contexte client. » Karim ouvre le dashboard CrowdStrike et voit immédiatement l'alerte rouge sur le tenant Norexia. Sévérité : Critical. Technique ATT&CK : T1218.011 (Rundll32) + T1105 (Ingress Tool Transfer). Machine : WKS-PROD-112. Il commence le triage.

---
