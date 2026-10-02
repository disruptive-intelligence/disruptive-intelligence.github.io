---
title: Partie I — Fondations et posture de l'investigateur
source: Cyber/02 OSINT/Méthode & enquête/OSINT — synthèse.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

*Avant de chercher, comprendre le cadre, la méthode et la sécurité. Le socle opérationnel de toute investigation crédible.*

---


## Chapitre 1 — L'OSINT

doctrine, cycle du renseignement et positionnement

### 1.1 Définition opérationnelle

L'OSINT (Open Source Intelligence) est la discipline du renseignement qui collecte, traite, analyse et exploite de l'information accessible publiquement pour produire du renseignement actionnable. Le mot clé est « discipline » : pas une collection d'outils, pas une recherche Google. C'est un processus structuré, reproductible et documenté qui transforme de l'information brute en renseignement exploitable par un décideur. L'OSINT se distingue de la simple recherche par trois traits : elle est **orientée par un objectif** (« Delaunay contrôle-t-il des sociétés offshore ? » est une question OSINT ; « que sais-je sur Delaunay ? » n'en est pas une), elle suit une **méthodologie rigoureuse** (le cycle du renseignement), et elle produit un **livrable avec un niveau de confiance explicite**.

### 1.2 Les disciplines du renseignement

L'OSINT s'inscrit dans un écosystème : **HUMINT** (renseignement humain — entretiens, informateurs ; légal si transparent, illégal si usurpation d'identité pour un privé), **SIGINT** (interception de communications — réservé à l'État), **IMINT** (renseignement par l'imagerie — accessible si sources ouvertes), **GEOINT** (renseignement géospatial — imagerie satellite, cartographie), **SOCMINT** (réseaux sociaux), **FININT** (renseignement financier — registres, flux, blockchain ; renvoi cours FININT pour la profondeur métier), **DARKINT** (dark web — consultation légale, interaction très encadrée). En pratique, une investigation typique combine OSINT + SOCMINT + IMINT + GEOINT + FININT + parfois DARKINT. Ce cours les enseigne de manière intégrée.

### 1.3 Le cycle du renseignement adapté à l'OSINT

**Orientation** (formuler les questions investigatives et le plan de collecte), **Collecte** (mobiliser les sources — documenter chaque donnée), **Traitement** (nettoyer, organiser, dédupliquer), **Analyse** (corréler, tester les hypothèses, coter la fiabilité), **Diffusion** (rapport avec conclusions et niveaux de confiance), **Feedback** (le commanditaire réagit — nouvelles pistes).

### 1.4 Les niveaux de confiance et la cotation de fiabilité

La grille à double entrée : fiabilité de la source (A = totalement fiable → F = inconnue) × crédibilité de l'information (1 = confirmée → 6 = non évaluable). Un registre officiel qui indique un dirigeant = A1. Un post anonyme sur un forum = F6. La cotation accompagne CHAQUE fait dans le rapport — c'est ce qui distingue le renseignement professionnel du bruit.

---


## Chapitre 2 — Cadre juridique et éthique

Le cadre français : RGPD (données personnelles — collecte proportionnelle, minimisation, finalité), Code pénal art. 226-1 (vie privée), art. 323-1 (accès frauduleux), art. 226-18 (collecte déloyale). Le principe fondamental : **accessible ≠ public** (un bucket S3 ouvert par erreur n'est pas une source OSINT — jurisprudence Bluetouff 2014). Proportionnalité, minimisation, finalité.

Le cadre par pays : USA (plus permissif — premier amendement), UK (Data Protection Act — modéré), Allemagne (forte protection vie privée), France (position intermédiaire). L'OSINT pour les LEA vs le secteur privé (les LEA ont des pouvoirs que le privé n'a pas — réquisitions, interceptions, perquisitions). L'éthique au-delà du droit : ne pas harceler, ne pas doxxer, ne pas manipuler, signaler les contenus illicites, ne pas stocker plus longtemps que nécessaire.

---


## Chapitre 3 — OPSEC : sécurité opérationnelle de l'investigateur

Le **threat model** (calibrer l'OPSEC sur la menace — un suspect financier a des moyens de contre-investigation différents d'un suspect lié au crime organisé). L'infrastructure : VM dédiée par enquête (Tails, Whonix, ou VM Linux + VPN), VPN non-corporate sans logs, navigateur profil vierge, DNS chiffré, stockage chiffré.

Les **avatars/sock puppets** : légende résistant au contrôle OSINT (nom crédible, photo IA non détectable en reverse search, historique de publications cohérent, maturation avant utilisation), registre interne, téléphones d'investigation (cartes SIM prépayées, IMEI dédié), destruction après usage. Les erreurs courantes : LinkedIn connecté au vrai profil, réutilisation VPN perso/investigation, copier-coller entre VM et machine personnelle, métadonnées dans les captures envoyées au client.

**Limites :** l'OPSEC parfaite n'existe pas — chaque interaction en ligne laisse une trace potentielle. L'objectif n'est pas l'invisibilité totale mais la réduction du risque à un niveau acceptable pour la mission. L'investigateur qui surévalue sa sécurité est aussi dangereux que celui qui la néglige — le premier prend des risques en croyant être invisible.

---


## Chapitre 4 — Méthodologie, outillage et gestion de l'investigation

Le processus structuré : cadrage → plan de collecte → collecte → traitement → corrélation → analyse → production → feedback. Les outils de gestion : **Obsidian** (notes structurées — un vault par enquête), **Maltego** (graphe de liens — entités, arêtes, transforms), **Hunchly** (capture horodatée + hashing — chaîne de custody), **Timeline Explorer** (chronologie visuelle).

Le **pivoting** (un sélecteur mène à un autre ; les 6 sélecteurs principaux : nom, email, username, téléphone, photo, adresse). La **préservation** : capturer AVANT disparition (la règle n°1), horodatage, hashing SHA-256, chaîne de custody.

*Note sur les outils cités dans ce cours :* les outils mentionnés tout au long du cours sont des exemples opérationnels à date (2025-2026). L'écosystème OSINT évolue rapidement — des outils ferment, d'autres apparaissent, les API changent, les plateformes bloquent. La méthodologie (comment chercher, pourquoi, dans quel ordre) est durable ; l'outil spécifique est remplaçable. Chaque chapitre enseigne d'abord le principe et la technique, puis cite les outils comme illustrations.

> **🎯 MIRAGE — Épisode 1 :** Cadrage. Questions : QI-1 sociétés offshore ? QI-2 flux de TechnoVert vers ces sociétés ? QI-3 crypto-actifs ? QI-4 campagne de désinformation ? Sélecteurs initiaux : nom, email pro, employeur.

---
