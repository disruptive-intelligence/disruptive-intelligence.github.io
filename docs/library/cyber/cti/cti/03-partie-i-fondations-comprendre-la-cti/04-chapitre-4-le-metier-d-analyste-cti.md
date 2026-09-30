---
title: Chapitre 4 — Le métier d'analyste CTI
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - ../index.md
- - 'Partie I — Fondations : comprendre la CTI'
  - index.md
---

## 4.1 Ce que fait concrètement un analyste CTI au quotidien

La journée type d'un analyste CTI senior combine : la **veille** (1-2h — consultation des sources prioritaires, lecture des rapports publiés dans les dernières 24h, vérification des feeds et des alertes de monitoring), l'**analyse** (3-4h — le cœur du métier : analyse approfondie des données collectées, rédaction des notes et des profils, corrélation multi-sources, application des TAS), la **production** (1-2h — rédaction des livrables : flash alerts, notes tactiques, mises à jour de profils d'acteurs, briefings), la **collaboration** (1h — échanges avec le SOC, l'IR, le hunting, le RSSI : briefings, réponses aux questions, orientation des détections), et le **développement** (temps variable — participation aux communautés, formation continue, développement d'outils et de processus).

La répartition varie selon le contexte : en période calme, la veille et l'analyse dominent ; pendant un incident, la collaboration et la production prennent le dessus ; et le développement des capacités est un investissement continu qui ne doit pas être sacrifié aux urgences.

## 4.2 Compétences requises

Les **compétences techniques** incluent la capacité à lire et interpréter un rapport technique d'incident (comprendre les artefacts, les TTP, les IoC), une compréhension des systèmes d'exploitation (Windows, Linux — registre, Event Logs, processus, réseau), une compréhension des réseaux (TCP/IP, DNS, HTTP/HTTPS, proxy, pare-feu), une capacité d'analyse de malware de premier niveau (soumission sandbox, interprétation des résultats, extraction d'IoC — pas du reverse engineering complet), et une maîtrise des outils CTI (TIP, ATT&CK Navigator, STIX/TAXII, feeds).

Les **compétences analytiques** sont les plus distinctives : raisonnement structuré (formuler des hypothèses, les tester, gérer l'incertitude), évaluation de sources (fiabilité, biais, crédibilité), rédaction analytique (formuler des conclusions avec niveaux de confiance, distinguer fait/déduction/hypothèse), et pensée critique (résistance aux biais, devil's advocate, remise en question des certitudes).

Les **compétences relationnelles** sont souvent sous-estimées : capacité de vulgarisation (expliquer une menace technique à un CEO sans jargon), collaboration interéquipes (travailler avec le SOC, l'IR, le RSSI dans des temporalités et des langages différents), et communication orale (briefings, présentations, argumentation).

## 4.3 Les rôles CTI

L'**analyste CTI junior** (0-2 ans) traite les feeds, enrichit les IoC, rédige les résumés de rapports, et assiste les analystes seniors. L'**analyste CTI senior** (2-5 ans) mène les analyses de fond (profilage, attribution, corrélation), produit les notes analytiques, et gère les missions d'intelligence. Le **CTI team lead** (5+ ans) définit les PIR avec le RSSI, gère l'équipe, arbitre les priorités, et porte la relation avec les communautés. Le **directeur CTI / Head of Intelligence** oriente la stratégie, gère le budget et les partenariats, et reporte au RSSI ou au board.

La CTI peut être organisée dans le SOC (intégrée à l'équipe de détection — avantage : boucle courte CTI→SOC ; inconvénient : risque de se faire absorber par l'opérationnel au détriment de l'analyse de fond), en équipe dédiée (séparée du SOC — avantage : profondeur d'analyse ; inconvénient : risque de déconnexion avec l'opérationnel), ou en modèle hybride (cellule CTI dédiée avec un « CTI liaison » intégré au SOC pour la boucle courte).

## 4.4 Posture intellectuelle

La rigueur : chaque affirmation est sourcée, chaque conclusion est accompagnée d'un niveau de confiance, chaque raisonnement est documenté. Le doute méthodique : l'analyste ne prend rien pour acquis, teste les hypothèses alternatives, et cherche activement ce qui contredit sa conclusion préférée. L'honnêteté : dire « nous ne savons pas » quand c'est le cas est un signe de maturité, pas de faiblesse. La résistance au sensationnalisme : le paysage de la menace est suffisamment inquiétant sans avoir besoin de l'exagérer — un rapport alarmiste non étayé détruit la crédibilité de la CTI.

---
