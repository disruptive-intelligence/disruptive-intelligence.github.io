---
title: Avant-propos
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 1
chapters: 10
---

Ce cours apprend à **comprendre et investiguer le dark web** dans une posture professionnelle. Il s'adresse aux analystes CTI, investigateurs, RSSI, chercheurs en sécurité, et professionnels de la conformité et de la lutte contre la cybercriminalité. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l'ordre, et fait les exercices proposés, acquiert un niveau professionnel.

**Ce que ce cours fait** : il vous apprend à situer le dark web dans le paysage numérique, comprendre ses infrastructures techniques (Tor, I2P, cryptomonnaies), cartographier ses écosystèmes (forums, marchés, leak sites, messageries), naviguer avec une OPSEC rigoureuse, investiguer une fuite de données ou une compromission, produire du renseignement actionnable, et coopérer avec les autorités. Il couvre aussi les cadres juridiques, les pièges analytiques, et les évolutions 2024-2026.

**Ce que ce cours ne fait pas** : il n'est pas un mode d'emploi pour l'activité criminelle. Il ne fournit pas de liens actifs vers des plateformes illicites, ne donne pas de techniques de contournement du law enforcement pour un usage criminel, et ne vend pas de sensationnel. Les exemples techniques sont suffisamment précis pour comprendre, pas assez pour reproduire une infraction.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport d'agence, publication journalistique reconnue, analyse vendor CTI sérieuse). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l'incertitude.

**Continuité avec la bibliothèque** : ce cours s'articule avec OSINT Mastery (techniques OSINT transposées au dark web), AU CŒUR DES APT (acteurs étatiques qui utilisent le dark web pour leurs opérations), Cartographie des écosystèmes cybercriminels (contexte structural), OSINT Crypto (traçage blockchain), et FININT (investigation financière). Les renvois explicites permettent d'approfondir sans dupliquer.

---


## Fil rouge : Opération DARKSTREAM

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré d'investigations réelles. **Opération DARKSTREAM** déroule, chapitre après chapitre, l'investigation d'une exfiltration de données industrielles.

**Le contexte.** **Vectris Aerospace** est un équipementier aérospatial européen (4 500 collaborateurs, coté SBF 120), partenaire de plusieurs programmes de défense et spatiaux. En mars 2026, son SOC détecte une anomalie de trafic sortant vers une IP résidentielle. L'investigation interne remonte à un poste R&D compromis. Volume exfiltré estimé : **420 Go** — spécifications techniques, documents de conception, bases clients, notes de conception propulsion. Compromission entre 8 et 14 semaines avant détection. Vectris classifie l'incident *critique*, notifie l'ANSSI et la DGSI (OIV défense), et mandate **Athéna Group**, un cabinet CTI français.

**L'analyste.** **Lucas Ferreira**, analyste CTI senior chez Athéna Group. 8 ans d'expérience dont 3 au CERT d'une grande banque. PASSI-qualifié. Le mandat d'Athéna : **(1)** confirmer ou infirmer la circulation des données Vectris sur le dark web ; **(2)** authentifier les données offertes ; **(3)** cartographier l'écosystème impliqué (vendeur, acheteurs potentiels, courtiers) ; **(4)** produire un rapport actionnable pour Vectris et la DGSI ; **(5)** si possible, contribuer à l'identification du vendeur.

**Les signaux initiaux.** Un service de monitoring (Recorded Future) a détecté une mention de « Vectris » et « propulsion specs » sur un forum .onion russophone, **IndustrialLeaks** — forum spécialisé dans les données industrielles, ~3 000 membres, créé en 2022. Un vendeur au pseudonyme **aero_source** propose « aerospace dump 420GB, EU supplier, reconnaissance française, propulsion R&D inside ». Prix demandé : 65 000 USDT.

**La méthode.** Lucas applique une méthode rigoureuse : OPSEC stricte pour la collecte, authentification par échantillons, pivoting OSINT sur le pseudonyme, traçage crypto des transactions connues, analyse linguistique, corrélation cross-forum, calibration de l'attribution. L'opération durera **6 semaines** — Ch.41 en détaillera la synthèse complète.

Les épisodes DARKSTREAM jalonnent le cours aux moments où le concept enseigné éclaire la progression de Lucas.

---
