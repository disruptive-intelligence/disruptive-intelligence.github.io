---
title: 'Ch.17 — L’IA au service de la cybersécurité : potentiel et limites'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie IV — IA offensive et défensive
  - index.md
---

## 17.1 L’IA dans le SOC

L’IA est de plus en plus intégrée dans les opérations de cybersécurité, principalement dans le SOC. Les cas d’usage matures incluent le tri d’alertes (classification automatique des alertes par criticité et par type — réduit le volume d’alertes à traiter manuellement), la corrélation (identification de liens entre des événements apparemment indépendants), la contextualisation (enrichissement automatique des alertes avec du contexte — CTI, informations sur l’asset, historique), et la détection de phishing par analyse du contenu des emails.

L’IA de type PredAI (ML classique prédictif) est solidement installée dans les SOC pour quatre cas d’usage principaux : le UEBA (User and Entity Behavior Analytics), la détection d’anomalies réseau, la priorisation d’incidents, et la détection de malware. La GenAI (IA générative) s’ajoute comme couche de qualification et de contextualisation des alertes, avec l’émergence de l’Agentic AI (agents IA qui tentent d’automatiser la qualification et, à terme, la remédiation).

L’étude ANSSI de février 2026 sur l’IA au service de la détection recense plus de 50 éditeurs de solutions de cybersécurité intégrant l’IA, et note que la maturité varie considérablement entre les solutions. Les éditeurs pionniers français (Sekoia, HarfangLab, Gatewatcher, Custocy, Sesame IT) développent des approches combinant ML/DL et LLMs.

## 17.2 UEBA et détection d’anomalies

Le UEBA modélise le comportement normal des utilisateurs et des entités (serveurs, endpoints, applications) et alerte quand un comportement dévie significativement. Les forces : capacité à détecter des menaces inconnues (pas besoin de signature), adaptation au contexte spécifique de l’organisation. Les faiblesses : faux positifs fréquents (un comportement inhabituel n’est pas nécessairement malveillant — un collaborateur en déplacement, un changement de poste, une charge de travail exceptionnelle), concept drift (le comportement « normal » évolue), besoin de données d’entraînement propres (un modèle entraîné sur des données déjà compromises est aveugle à la compromission), et temps de calibration initial.

## 17.3 IA pour l’analyse de malware

L’IA facilite la classification automatique des malwares (famille, variante, capacités), l’extraction automatique d’IOC (indicateurs de compromission), et l’analyse statique augmentée (identification de patterns suspects dans le code sans exécution). Les limites : les techniques d’évasion adversariale (modification du malware pour contourner le classifieur IA) sont efficaces, et la classification automatique ne remplace pas l’analyse manuelle pour les menaces nouvelles ou sophistiquées.

## 17.4 Automation bias et overreliance

L’intégration de l’IA dans la cybersécurité introduit un risque humain majeur : l’automation bias (biais d’automatisation) et l’overreliance (surconfiance). L’analyste SOC qui reçoit une qualification automatique d’une alerte par l’IA a tendance à la valider sans vérification approfondie — « l’IA l’a dit, donc c’est vrai ». Ce biais est amplifié par la fatigue d’alerte et la pression de volume.

Les conséquences sont doubles : les faux négatifs de l’IA ne sont pas rattrapés par l’humain (la menace réelle est ignorée parce que l’IA l’a classée comme bénigne), et les faux positifs de l’IA sont confirmés par l’humain (des ressources sont gaspillées à investiguer des non-incidents). Le phénomène d’effondrement de la vigilance humaine quand un système automatisé est en place est bien documenté en ergonomie des systèmes critiques (aviation, médecine).

Les défenses contre l’overreliance incluent la formation explicite des analystes à la faillibilité de l’IA (l’IA est une aide, pas un oracle — ses sorties sont des suggestions à vérifier, pas des verdicts), la rotation des tâches (ne pas laisser un analyste uniquement en mode « validation de l’IA »), les checks croisés (certaines alertes sont volontairement présentées sans la qualification IA pour maintenir la capacité de jugement indépendant), et les métriques de performance individuelle qui mesurent la capacité de détection indépendante, pas seulement le volume traité.

## 17.5 Limites fondamentales de l’IA défensive

L’IA ne comprend pas le contexte métier — elle détecte des patterns statistiques. Une alerte « anomalie de comportement sur le compte du CFO » peut être une compromission ou le CFO qui prépare une acquisition confidentielle. Seul l’humain avec le contexte métier peut discriminer. L’IA est vulnérable aux données adversariales — un attaquant qui connaît (ou devine) les features du modèle de détection peut ajuster son comportement pour rester sous le seuil. Un modèle de détection n’est jamais meilleur que ses données d’entraînement — si les données historiques ne contiennent pas de cas de l’attaque en question, le modèle ne la détectera pas. Et l’explicabilité et la reproductibilité des résultats restent des enjeux majeurs pour l’Agentic AI dans le SOC.

-----
