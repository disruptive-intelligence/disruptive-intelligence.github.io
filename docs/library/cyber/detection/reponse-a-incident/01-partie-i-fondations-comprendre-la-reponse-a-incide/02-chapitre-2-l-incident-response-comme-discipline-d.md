---
title: Chapitre 2 — L'Incident Response comme discipline d'orchestration
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie I — Fondations : comprendre la réponse à incident'
  - index.md
---

## 2.1 Ce qui distingue l'IR du SOC

Le SOC (Security Operations Center) est un dispositif permanent de détection et de triage. Les analystes SOC N1 traitent les alertes en masse, filtrent les faux positifs, et escaladent les vrais positifs. Les analystes N2 investiguent les alertes escaladées et confirment ou infirment les incidents. Le SOC est un capteur permanent — il fonctionne 24/7, traite des centaines ou des milliers d'alertes par jour, et son objectif est de détecter et qualifier.

L'IR (Incident Response) prend le relais quand l'alerte est confirmée comme incident. L'IR pilote l'investigation approfondie, coordonne les acteurs techniques et non techniques, prend les décisions de confinement et d'éradication, et conduit l'organisation jusqu'à la résolution complète et le retour d'expérience. L'IR est une capacité activée ponctuellement — elle se déclenche quand un incident est confirmé et se désactive quand l'incident est clos.

La frontière entre SOC et IR n'est pas toujours nette dans les petites organisations (les mêmes personnes peuvent porter les deux casquettes), mais les fonctions sont distinctes : le SOC détecte, l'IR orchestre la réponse.

## 2.2 Ce qui distingue l'IR du forensic

Le forensic numérique (digital forensics) est une discipline d'analyse technique approfondie : acquisition d'images disque bit-à-bit, analyse de la mémoire vive, analyse d'artefacts système, reverse engineering de malware, reconstitution chronologique granulaire des actions sur un système. Le forensic produit des preuves — au sens technique et parfois judiciaire.

L'IR utilise le forensic comme un outil parmi d'autres. L'investigateur IR fait du forensic « good enough » — orienté décision, pas orienté preuve exhaustive. La question de l'IR n'est pas « quelle est l'empreinte exacte du malware dans le registre à la microseconde près ? » mais « ce serveur est-il compromis ? oui ou non — parce que je dois décider dans 30 minutes si je l'isole ». L'IR cherche la compréhension opérationnelle suffisante pour agir ; le forensic cherche la reconstitution exhaustive.

En pratique, les deux sont souvent menés en parallèle : l'IR guide les actions immédiates (confinement, éradication), pendant qu'un forensicien dédié ou un prestataire PRIS produit les analyses approfondies et les preuves pour la plainte pénale. Le cours SOC de la bibliothèque traite de la détection en détail ; le cours Forensic traite de l'analyse technique en profondeur. Ce cours traite de l'orchestration.

## 2.3 Ce qui distingue l'IR de la gestion de crise

La gestion de crise est un processus de gouvernance qui mobilise la direction générale, la communication, le juridique, et les métiers. Elle traite les aspects stratégiques, réputationnels, réglementaires et financiers de l'incident. L'IR est la composante technique de la gestion de crise.

Les deux doivent fonctionner en parallèle et se nourrir mutuellement, mais ce ne sont pas les mêmes compétences, les mêmes temporalités, ni les mêmes interlocuteurs. L'analyste forensic qui explique la structure des Event IDs Windows au CEO perd son temps et celui du CEO. Le CEO qui intervient dans les décisions de confinement technique prend des risques qu'il ne mesure pas. L'articulation entre la cellule technique (IR) et la cellule de crise exécutive est un enjeu majeur traité au Ch.3 (seuils de bascule) et en Partie VII (gestion de crise).

## 2.4 Le rôle d'orchestration de l'IR lead

L'IR lead n'est pas nécessairement le meilleur forensicien de l'équipe, ni le meilleur analyste réseau, ni le meilleur spécialiste AD. Il est celui qui maintient la vision d'ensemble de l'incident, coordonne les experts en leur assignant des questions précises, arbitre les priorités quand les ressources sont limitées (et elles le sont toujours), fait l'interface entre le monde technique et le monde décisionnel (traduire « le krbtgt est compromis » en « l'attaquant contrôle potentiellement l'ensemble de notre infrastructure — c'est un incident majeur »), et documente les décisions et leurs justifications.

C'est un chef d'orchestre, pas un soliste. Sa valeur ne réside pas dans sa capacité à analyser un dump mémoire (il a des analystes pour ça) mais dans sa capacité à poser les bonnes questions, à prioriser les efforts, et à maintenir la cohérence de la réponse quand 15 personnes travaillent en parallèle sur des aspects différents de l'incident.

## 2.5 La logique fondamentale

temps court, forte incertitude, conséquences élevées

L'IR opère dans un régime de décision radicalement différent de la sécurité « temps de paix ». En temps de paix, une décision de sécurité (déployer un EDR, durcir l'AD, segmenter le réseau) peut être étudiée pendant des semaines, testée en environnement de pré-production, et déployée progressivement. En temps d'incident, les décisions doivent être prises en heures (parfois en minutes), avec des informations partielles et évolutives.

Les conséquences d'une mauvaise décision sont immédiates et parfois irréversibles. Isoler un serveur de production arrête la production. Redémarrer un serveur sans collecte forensic détruit la mémoire vive. Communiquer publiquement trop tôt peut être contredit par les faits. Ne pas contenir assez vite laisse l'attaquant progresser. Chaque décision est un arbitrage entre des risques concurrents, et cet arbitrage se fait sous pression, avec de la fatigue, et souvent au milieu de la nuit.

Cette pression n'est pas un accident — c'est la nature même de l'IR. La capacité à décider sous incertitude, à accepter le risque résiduel de chaque décision, et à documenter le raisonnement qui a conduit à cette décision (pour le retex et pour la protection juridique des décideurs) est la compétence fondamentale de l'IR lead. Le Ch.26 est entièrement dédié à cette dimension.

## 2.6 Fil rouge — BLACKTIDE : l'organisation de la réponse

> **🔍 BLACKTIDE — Épisode 2**
>
> 22h45. Karim appelle Nadia Moreau, IR lead d'Arvantis. Elle décroche immédiatement — elle était d'astreinte ce week-end.
>
> Nadia pose les questions de cadrage en 5 minutes : « Qu'est-ce qu'on voit ? » (PsExec + GPO Defender sur DC01). « Depuis quand ? » (l'alerte EDR date de 22h17, mais on ne sait pas depuis quand l'attaquant est dans le réseau). « Combien de systèmes ? » (DC01 confirmé, à vérifier sur les autres DC). « L'attaquant est-il toujours actif ? » (probablement — l'exécution est récente). « Est-ce qu'on a touché à quelque chose ? » (non, Karim n'a fait qu'observer).
>
> Nadia active le protocole de réponse :
> - Ouverture du canal Signal « IR-BLACKTIDE » (canal pré-configuré, hors SI d'entreprise — le SI interne n'est plus de confiance).
> - Appel au RSSI, Marc Delaunay (réveillé, répond en 2 sonneries — il était en astreinte).
> - Appel au prestataire PRIS sous contrat, CyberForce (SLA : intervention dans les 12h le week-end — arrivée estimée samedi 8h).
> - Message aux analystes SOC N2 disponibles : « surveillance renforcée immédiate sur tous les DC, recherche de PsExec et de modifications GPO sur le parc. »
>
> Première tension : le responsable astreinte IT, David Lemaire, est réveillé par les alertes et propose de « patcher et redémarrer DC01 pour stopper l'attaque ». Nadia l'arrête fermement : « Pas de redémarrage. Pas de modification. On ne touche à rien tant qu'on n'a pas compris ce qui se passe et collecté les preuves. La mémoire de DC01 contient peut-être les clés de l'investigation. » David accepte, mais avec réticence — il sent que « quelque chose de grave est en train de se passer » et son réflexe d'admin est de « réparer ».

---
