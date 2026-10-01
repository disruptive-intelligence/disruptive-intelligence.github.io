---
title: Chapitre 1 — Qu'est-ce que la Cyber Threat Intelligence
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - 'Partie I — Fondations : comprendre la CTI'
  - index.md
---

## 1.1 Définition opérationnelle

La Cyber Threat Intelligence est la discipline qui transforme des informations brutes sur les menaces cyber en renseignement exploitable pour la prise de décision. Le mot clé est « discipline » : la CTI n'est pas un flux d'IoC injecté dans un SIEM, ni une revue de presse des dernières attaques, ni un dashboard de vulnérabilités. C'est un processus analytique structuré — collecte, traitement, analyse, production, dissémination — qui répond à des questions de renseignement définies, avec des niveaux de confiance explicites et des recommandations actionnables.

La distinction fondamentale est entre **information** et **renseignement**. Une information est un fait brut (« le hash X a été observé sur VirusTotal »). Un renseignement est une information analysée, contextualisée, et rendue exploitable (« le hash X est associé au loader BumbleBee, utilisé par le cluster UNC-VOLT qui cible les opérateurs d'énergie européens via exploitation de vulnérabilités Ivanti — notre infrastructure utilise Ivanti, nous recommandons une vérification immédiate et le déploiement des IoC joints dans le SIEM »). La différence est l'analyse : sans analyse, un IoC est un artefact mort. Avec analyse, il devient un renseignement qui oriente une décision.

## 1.2 CTI et disciplines voisines — interfaces et frontières

La CTI s'inscrit dans un écosystème de disciplines interconnectées, et les confusions entre elles sont fréquentes.

L'**OSINT** (Open Source Intelligence) est une méthode de collecte — la CTI l'utilise comme l'une de ses sources parmi d'autres (sources internes, communautaires, commerciales, techniques, dark web). Dire « je fais de l'OSINT » et « je fais de la CTI » ne désigne pas la même activité : l'OSINT collecte, la CTI analyse et produit. Un analyste CTI utilise l'OSINT, mais il utilise aussi les logs internes du SOC, les rapports d'IR post-incident, les feeds commerciaux, et les échanges en cercles de confiance.

Le **SOC** (Security Operations Center) est le principal consommateur de la CTI technique et tactique. Le SOC reçoit les IoC (pour le SIEM/EDR), les TTP (pour orienter les détections et le hunting), et le contexte (pour qualifier les alertes — « cette alerte correspond-elle à un comportement d'acteur connu ? »). En retour, le SOC alimente la CTI : les alertes, les faux positifs, et les incidents détectés sont des données de première main sur ce que les attaquants tentent contre l'organisation. La boucle SOC → CTI → SOC est le mécanisme le plus productif de la sécurité opérationnelle.

Le **DFIR** (Digital Forensics and Incident Response) fournit des données de terrain à la CTI : les artefacts collectés pendant un incident (malware samples, IoC, TTP observés) sont la matière première que la CTI contextualise et attribue. En retour, la CTI fournit au DFIR le contexte de menace pendant l'incident : « les TTP observées correspondent au cluster X, qui utilise typiquement les mécanismes de persistance Y — cherchez-les ».

Le **Threat Hunting** utilise les hypothèses CTI comme point de départ : « le cluster UNC-VOLT utilise le DLL sideloading sur les postes d'ingénieurs OT — nos postes d'ingénieurs OT sont-ils compromis ? ». Le hunter traduit l'hypothèse CTI en requête technique. Sans CTI, le hunting est aveugle. Sans hunting, la CTI reste théorique.

## 1.3 Les quatre niveaux de CTI

La CTI produit du renseignement à quatre niveaux distincts, chacun avec son audience, son format, sa temporalité, et son usage.

La **CTI stratégique** s'adresse à la direction, au RSSI, et au board. Elle traite des tendances de menace (quels acteurs ciblent notre secteur, quelle est l'évolution du paysage), de la géopolitique (quelles tensions internationales créent des risques cyber pour notre organisation), et des risques sectoriels (le secteur énergie est-il plus ciblé cette année ? par qui ?). Format : rapports semestriels ou annuels, briefings exécutifs, évaluations de risque. Temporalité : mois. La CTI stratégique informe les décisions de budget, de posture, et de stratégie.

La **CTI opérationnelle** s'adresse aux SOC managers, aux IR leads, et aux responsables sécurité. Elle traite des campagnes en cours (qui attaque, avec quoi, contre qui, depuis quand), des acteurs actifs (profils, TTP à haut niveau), et des alertes sur les menaces imminentes. Format : bulletins hebdomadaires, alertes flash, briefings opérationnels. Temporalité : semaines. La CTI opérationnelle oriente la préparation et la réponse.

La **CTI tactique** s'adresse aux analystes SOC, aux hunters, et aux ingénieurs de détection. Elle traite des TTP détaillés (techniques ATT&CK avec procédures spécifiques, patterns de comportement), des règles de détection associées, et des méthodologies de hunting. Format : mappings ATT&CK, règles Sigma, guides de hunting. Temporalité : jours. La CTI tactique transforme le renseignement en capacité de détection.

La **CTI technique** s'adresse directement aux outils (SIEM, EDR, pare-feu, proxy). Ce sont les IoC bruts : hash de malware, domaines C2, adresses IP, URLs, règles YARA. Format : feeds STIX/TAXII, listes d'IoC, règles de blocage. Temporalité : heures. La CTI technique est consommée automatiquement par les systèmes de détection.

## 1.4 IoC, TTP, IoA et la Pyramid of Pain

La hiérarchie de valeur du renseignement est structurée par la **Pyramid of Pain** (David Bianco, 2013). En bas de la pyramide, les indicateurs que l'attaquant peut changer facilement : les **hash values** (recompiler le malware = nouveau hash — trivial), les **adresses IP** (changer de VPS — facile), les **noms de domaine** (enregistrer un nouveau domaine — simple). Au milieu, les indicateurs plus coûteux à changer : les **artefacts réseau et host** (user-agents, JA3/JA4, certificats, artefacts de registre — ennuyeux à modifier), les **outils** (changer d'outil de C2, de framework d'exploitation — challenging). Au sommet, les **TTP** (Tactics, Techniques, and Procedures) — le savoir-faire opérationnel de l'attaquant, qui représente des mois ou des années d'investissement et qui est le plus douloureux à modifier.

Le message pour l'analyste CTI : visez le plus haut possible dans la pyramide. Un IoC (hash, IP, domaine) a une durée de vie de quelques heures à quelques jours — l'attaquant le change dès qu'il est détecté. Un TTP a une durée de vie de mois à années — c'est le comportement profond de l'attaquant, et le changer coûte cher en temps, en compétences, et en risque opérationnel. Les détections basées sur les TTP sont les plus résilientes et les plus douloureuses pour l'adversaire.

Les **IoA** (Indicators of Attack) sont un concept intermédiaire : des signaux comportementaux qui indiquent une attaque en cours (un process tree anormal, un beaconing régulier, une rafale de commandes de discovery) — avant même la compromission complète. Les IoA détectent l'action, pas l'artefact — ils survivent au changement d'outillage.

## 1.5 Ce que la CTI n'est PAS

La CTI n'est PAS un flux automatisé d'IoC injecté dans un SIEM sans contexte (c'est de la CTI technique brute — utile mais insuffisante). Elle n'est PAS une revue de presse des dernières attaques (c'est de la veille, pas du renseignement). Elle n'est PAS un dashboard de vulnérabilités (c'est du vulnerability management). Elle n'est PAS de l'attribution sensationnaliste (« c'est la Russie ! » sans niveau de confiance ni évidences). Et elle n'est PAS un service ponctuel activé uniquement pendant les incidents — c'est un processus continu qui alimente la posture de sécurité en permanence.

## 1.6 Fil rouge — MERIDIAN : la mission

> **🔎 MERIDIAN — Épisode 1**
>
> Élise reçoit le brief d'EDE. Le RSSI d'EDE, Thomas Kessler, pose les questions en termes business : « Qui nous a attaqués ? Vont-ils revenir ? Que devons-nous faire différemment ? » Élise traduit ces questions en objectifs CTI structurés (les 5 objectifs du fil rouge). Elle note que la première étape n'est pas de chercher des réponses — c'est de formuler les bonnes questions. Le chapitre 5 détaillera cette formulation.

---
