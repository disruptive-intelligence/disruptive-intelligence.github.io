---
title: 'PARTIE V — Cadres de réponse : réglementation, coopération et résilience'
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
chapter: 5
chapters: 7
---

## Chapitre 21 — Le cadre réglementaire européen de cybersécurité

### 21.1 — NIS2 : la directive socle

La directive NIS2 (Network and Information Security 2) constitue le socle réglementaire européen de cybersécurité. Son périmètre est considérablement élargi par rapport à NIS1 : elle couvre 18 secteurs classés en haute criticité (énergie, transport, banque, santé, eau potable, infrastructure numérique, espace, administration publique, etc.) et autres critiques (services postaux, gestion des déchets, industrie chimique, agroalimentaire, fabrication, recherche, etc.).

La distinction entre **entités essentielles** (soumises à un régime de supervision complet) et **entités importantes** (régime allégé) détermine le niveau d'obligations. L'article 21 impose des mesures de gestion des risques proportionnées et appropriées, couvrant : l'analyse des risques, la gestion des incidents, la continuité d'activité, la sécurité de la chaîne d'approvisionnement, la gestion des vulnérabilités, les pratiques de base en cyber-hygiène, l'utilisation de la cryptographie, la sécurité des ressources humaines, et les politiques de contrôle d'accès.

La transposition dans les droits nationaux est en cours, avec des variations significatives entre États membres. L'ANSSI note que les réglementations françaises et européennes — NIS2 et le CRA — « permettent de définir et imposer des socles de mesures de sécurité et d'élever le niveau de maturité global de la Nation ».

Pour le praticien, NIS2 fait du CTL un livrable quasi-obligatoire : la gestion des risques « tenant compte de l'état de l'art » suppose une connaissance actualisée du paysage de menace. Un RSSI qui ne dispose pas d'un CTL ne peut pas démontrer que ses mesures de sécurité sont proportionnées aux menaces réelles.

### 21.2 — Cyber Resilience Act (CRA) : sécurité des produits numériques

Le CRA, publié au Journal officiel en novembre 2024, est la première législation européenne imposant des exigences de cybersécurité pour les produits avec des éléments numériques tout au long de leur cycle de vie. L'ENISA note que le CRA « devrait avoir un impact significatif sur le développement, les opérations et le décommissionnement des systèmes spatiaux ». Le CRA est décrit par Microsoft comme potentiellement le « gold standard » mondial de la cybersécurité des produits, à l'instar de ce que le RGPD a été pour la protection des données.

Les obligations incluent la sécurité par conception et par défaut, la gestion des vulnérabilités tout au long du cycle de vie, la notification des vulnérabilités activement exploitées, et la génération de SBOM (Software Bills of Materials). Pour les fabricants, cela implique une transformation des processus de développement et de maintenance.

### 21.3 — DORA : résilience du secteur financier

Le règlement DORA (Digital Operational Resilience Act) impose au secteur financier des exigences spécifiques de résilience opérationnelle numérique : gestion des risques ICT, notification d'incidents, tests de résilience (y compris des tests de pénétration fondés sur des scénarios de menace — Threat-Led Penetration Testing), gestion des risques liés aux prestataires ICT tiers, et partage d'informations sur les cybermenaces.

### 21.4 — Articulation réglementaire

L'écosystème réglementaire européen est dense : NIS2 (obligations sectorielles), CRA (produits), DORA (finance), EU Cybersecurity Act (certification), RGPD (données personnelles), Cyber Solidarity Act (coordination de crise via EU-CyCLONe). L'articulation entre ces textes est un enjeu opérationnel : un incident de ransomware impliquant une fuite de données personnelles dans une entité essentielle du secteur financier active simultanément NIS2 (notification d'incident), DORA (gestion ICT), et RGPD (violation de données). Les délais, formats et destinataires de notification diffèrent, créant une charge de conformité significative.

Microsoft note le risque de la **fragmentation réglementaire** : « des cadres réglementaires fragmentés peuvent ralentir la réponse à incident et finalement affaiblir les défenses ».

### 21.5 — 🔴 Fil rouge : audit NIS2

> **📌 FIL ROUGE — Épisode 21**
>
> En octobre 2025, l'audit NIS2 d'EuroDefense approche. Sophie doit démontrer que le CTL du groupe alimente effectivement la gestion des risques. Elle produit un document de traçabilité montrant comment les menaces identifiées dans le CTL sont mappées sur les mesures de sécurité de l'article 21 NIS2 : chaque menace est associée à une mesure de mitigation, un niveau de maturité actuel, et un plan d'action avec échéance. Le CRA impose un audit supplémentaire sur la branche spatial (composants avec éléments numériques destinés à des satellites). DORA ne s'applique pas directement à EuroDefense (secteur industriel, pas financier) mais plusieurs de ses clients bancaires exigent une conformité de facto via leurs clauses contractuelles.

---

## Chapitre 22 — Doctrines nationales, coopération stratégique et normes internationales

> **Note de frontière** : Ce chapitre traite des **cadres stratégiques** — doctrines nationales, coopération diplomatique, normes de comportement, postures publiques — qui structurent la réponse étatique à la cybermenace à un niveau politique et stratégique. La coopération **opérationnelle** (enquêtes, takedowns, coordination tactique) est traitée au Chapitre 14.

### 22.1 — L'ANSSI et la stratégie nationale française 2026-2030

L'ANSSI occupe une position institutionnelle singulière : agence nationale de cybersécurité, autorité nationale NIS2, et centre de réponse à incident de premier plan. La nouvelle stratégie nationale de cybersécurité 2026-2030 fait du « renforcement de la résilience de la Nation » l'une de ses priorités. L'ANSSI n'est pas seule dans cet écosystème : le GIP ACYMA (Cybermalveillance.gouv.fr), les campus cyber, les prestataires de confiance et l'InterCERT France (première communauté de CERT en France) contribuent à la mission.

### 22.2 — Le NCSC UK : construction de la résilience à grande échelle

Le National Cyber Security Centre britannique, rattaché au GCHQ, se distingue par son approche de la résilience à grande échelle — « Resilience at Scale ». L'approche britannique met l'accent sur les services de protection automatisés (Active Cyber Defence), le conseil aux entreprises et aux particuliers, et la coopération avec le secteur privé. Le positionnement post-Brexit a conduit à une politique de partenariats bilatéraux plus actifs avec les pays Five Eyes et les partenaires européens.

### 22.3 — L'approche Five Eyes et l'attribution publique

Les cinq pays de l'alliance Five Eyes (États-Unis, Royaume-Uni, Canada, Australie, Nouvelle-Zélande) constituent le noyau de la coopération en matière de threat intelligence et d'attribution publique. Les advisories conjoints (sur APT40, Volt Typhoon, Salt Typhoon, ciblage de la logistique Ukraine) illustrent cette coordination : un même message porté simultanément par cinq pays crée un impact politique et médiatique significativement supérieur à une attribution unilatérale.

Le CSE canadien inscrit explicitement ses évaluations dans le cadre Five Eyes, notant que « le Canada, avec nos partenaires Five Eyes, est une cible continue du programme cyber de la RPC ».

### 22.4 — L'approche australienne (ASD) : particularités Indo-Pacifique

L'ASD se distingue par son programme CTIS (Cyber Threat Intelligence Sharing) qui opérationnalise le partage de threat intelligence entre le gouvernement et le secteur privé. Le programme a permis de « bloquer des centaines de sites web malveillants » en collaboration avec les banques et les opérateurs télécom. Le programme de **threat sharing et threat blocking** sous la stratégie australienne de cybersécurité 2023-2030 est un modèle de coopération public-privé à grande échelle.

### 22.5 — L'OTAN et la cyber-diplomatie

L'OTAN a avancé des cadres d'attribution collective et explore des contre-mesures collectives en réponse aux cyberattaques. En juillet 2025, l'alliance a publié une déclaration reconnaissant et condamnant les activités cyber malveillantes attribuées à la Russie par les États membres. La question de l'invocation de l'article 5 (défense collective) en réponse à une cyberattaque reste un débat ouvert.

Le **Cyber Diplomacy Toolbox** de l'UE permet l'utilisation de sanctions contre les acteurs de cyberattaques. Microsoft note que la mise en œuvre reste « inégale » et plaide pour des conséquences plus crédibles et proportionnées.

### 22.6 — Normes internationales de comportement responsable

Le cadre onusien de comportement responsable des États dans le cyberespace établit des normes volontaires. La notion de **due diligence** — l'obligation pour un État de prévenir les activités cybercriminelles depuis son territoire — est un levier juridique et diplomatique contre les « safe haven states ». Microsoft propose la **désignation d'États sponsors de ransomware**, sur le modèle des États sponsors du terrorisme, comme mécanisme de pression.

### 22.7 — Fragmentation et harmonisation

La fragmentation réglementaire internationale est un risque identifié par Microsoft, l'ENISA et les agences nationales. Les efforts d'harmonisation — comme l'initiative Allemagne-Corée du Sud pour la coopération réglementaire internationale — sont des signaux positifs mais restent embryonnaires.

---

## Chapitre 23 — Réponse à incident, remédiation et résilience opérationnelle

### 23.1 — La chaîne de réponse

La réponse à incident suit un processus structuré : **détection** (identification d'un événement suspect), **qualification** (l'événement est-il un incident ? Quelle gravité ?), **containment** (limiter la propagation), **investigation** (comprendre la chaîne d'attaque), **remédiation** (éliminer la présence de l'attaquant et corriger les vulnérabilités exploitées), et **retour d'expérience** (leçons apprises, amélioration des défenses).

L'ANSSI a publié en janvier 2026 un guide « Préparer la remédiation » qui fournit un cadre structuré pour la phase de remédiation — souvent la phase la plus complexe et la plus longue. Le guide insiste sur la nécessité de **préparer la remédiation en amont** de l'incident, pas pendant la crise.

### 23.2 — La supply chain comme facteur aggravant

Les cas documentés par l'ANSSI illustrent comment la compromission d'un prestataire peut entraîner des effets en cascade sur ses clients. La remédiation dans ce contexte est considérablement plus complexe : elle implique la coordination entre organisations indépendantes, le partage d'informations sensibles (quelles données ont été exfiltrées ?), et la gestion de relations commerciales sous tension.

La **latéralisation inter-organisationnelle** — un attaquant qui pivote depuis un prestataire compromis vers les réseaux de ses clients via des interconnexions existantes — est un pattern récurrent en 2025. L'ANSSI documente des cas où les attaquants ont utilisé « les ressources internes de la première entité compromise pour forger ou utiliser des éléments crédibles permettant de mieux cibler une deuxième entité ».

### 23.3 — L'écosystème CERT/CSIRT

L'écosystème de réponse s'articule autour de plusieurs niveaux. Les CERT/CSIRT nationaux (CERT-FR en France, CERT-EU pour les institutions européennes) traitent les incidents les plus graves et produisent des alertes et advisories. Les CERT sectoriels (ISACs) partagent l'intelligence de menace au sein de secteurs spécifiques. Les CERT d'entreprise gèrent la réponse opérationnelle au niveau organisationnel.

Les réseaux de coordination incluent FIRST (Forum of Incident Response and Security Teams — réseau mondial), TF-CSIRT (réseau européen), InterCERT France (premier réseau national de CERT en France), et le réseau européen des CSIRTs sous NIS2.

### 23.4 — Construire la cyber-résilience

La cyber-résilience va au-delà de la prévention : c'est la capacité d'une organisation à **anticiper, résister, récupérer et s'adapter** face aux cyberattaques. L'approche **threat-informed defense** — défendre en fonction des menaces réelles documentées dans le CTL — est le cadre méthodologique.

Les recommandations convergentes des agences du corpus s'organisent en priorités :

**P0 — Critique** : patching des vulnérabilités activement exploitées (KEV/EUVD), MFA résistant au phishing sur tous les accès critiques, segmentation réseau IT/OT, sauvegarde hors ligne testée, plan de réponse à incident documenté et exercé.

**P1 — Important** : réduction de la surface d'attaque (désactivation des services inutiles, restriction des outils RMM), monitoring comportemental (EDR/XDR), gestion des accès privilégiés (PAM), sécurité de la supply chain (audit des prestataires, clauses contractuelles), sensibilisation ciblée (C-level, OT, supply chain).

**P2 — Structurant** : architecture zero trust, programme de threat hunting, purple teaming régulier, SBOM et gestion des dépendances, participation aux ISACs sectoriels, automatisation de la détection et de la réponse.

### 23.5 — 🔴 Fil rouge : réponse complète à l'incident

> **📌 FIL ROUGE — Épisode 23**
>
> Sophie pilote la réponse complète à l'incident EuroDefense. L'investigation, conduite avec l'appui de l'ANSSI (mobilisée en raison de la dimension espionnage étatique), confirme la présence simultanée de Qilin (ransomware) et ShadowPad (espionnage). La remédiation est complexe : l'attaquant ShadowPad a établi plusieurs points de persistance indépendants du vecteur d'accès initial du ransomware.
>
> La remédiation prend trois mois et inclut : reconstruction des serveurs compromis, changement de tous les credentials partagés avec le prestataire, segmentation réseau renforcée entre EuroDefense et ses sous-traitants, déploiement d'un monitoring renforcé (EDR sur les serveurs de contrats OTAN, IDS sur les segments OT), et notification NIS2 à l'ANSSI comme autorité compétente.
>
> Le retour d'expérience identifie trois échecs défensifs : (1) l'interconnexion réseau avec le prestataire n'était pas suffisamment segmentée, (2) aucune surveillance ne portait sur les forums underground pour les credentials des sous-traitants, (3) le serveur Exchange exposé identifié en février (Ch. 5) n'avait pas été correctement remédié. Sophie documente ces leçons dans le rapport post-incident et les intègre dans le plan de résilience.

---

## Chapitre 24 — De l'analyse de la menace à la décision stratégique

### 24.1 — Le CTL comme outil de gouvernance

Le CTL n'est pas un produit technique destiné à rester dans le CERT. C'est un **outil de gouvernance** qui doit remonter jusqu'au conseil d'administration. Sa valeur stratégique réside dans sa capacité à informer les arbitrages budgétaires, les décisions d'investissement en sécurité, et les choix d'architecture.

### 24.2 — Briefings exécutifs : traduire l'intelligence en décision

Le briefing exécutif est l'exercice de traduction le plus exigeant : transformer une analyse technique complexe en un message clair, actionnable et calibré pour un public non technique. Les principes : commencer par la conclusion (pas par la méthodologie), quantifier quand c'est possible, relier chaque menace à un impact business, proposer des actions priorisées avec des coûts estimatifs.

### 24.3 — Priorisation des mesures défensives

La priorisation fondée sur la menace réelle (threat-based prioritization) est plus efficace que la priorisation fondée sur la conformité seule. Un CTL de qualité permet de répondre à la question : « Parmi toutes les mesures de sécurité que nous pourrions implémenter, lesquelles auront le plus d'impact contre les menaces qui nous ciblent réellement ? »

### 24.4 — 🔴 Fil rouge : présentation au COMEX

> **📌 FIL ROUGE — Épisode 24**
>
> En novembre 2025, Sophie présente le CTL v1 d'EuroDefense au COMEX. Son briefing de 20 minutes couvre : (1) les 4 menaces prioritaires identifiées (espionnage Chine, espionnage Russie, ransomware supply chain, menaces hybrides), (2) l'incident majeur traversé (Qilin + ShadowPad) et les leçons apprises, (3) les 5 investissements prioritaires pour le plan de résilience 2026-2030, priorisés P0/P1/P2 avec estimation budgétaire.
>
> Le PDG demande : « Quel est le risque qu'on perde un contrat OTAN à cause d'une cyberattaque ? ». Sophie répond avec précision : « La probabilité d'une tentative d'espionnage ciblant nos contrats OTAN est évaluée comme élevée — nous en avons déjà été victimes. La probabilité de perte de contrat dépend de notre capacité à démontrer notre résilience aux audits de nos clients OTAN. Les investissements P0 que je recommande réduisent significativement ce risque. » Le COMEX valide le budget de remédiation et le plan de résilience.

> **🎯 CAPSTONE Partie V** : Rédiger un briefing exécutif COMEX de 2 pages maximum, intégrant : les 3 menaces prioritaires pour une entité NIS2 du secteur industriel/défense, la posture réglementaire (NIS2, CRA), les 5 recommandations priorisées P0/P1/P2 avec justification fondée sur le CTL, et l'estimation budgétaire associée.

---
