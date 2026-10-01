---
title: Chapitre 12 — Évaluer la fiabilité des sources et la crédibilité de l'information
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - 'Partie III — L''analyse : le cœur du métier'
  - index.md
---

## 12.1 Le système Admiralty adapté à la CTI

Le système de cotation Admiralty (NATO standard) évalue indépendamment la fiabilité de la source et la crédibilité de l'information. La **fiabilité de la source** (A à F) : A = complètement fiable (source avec un historique de fiabilité parfait — CERT-FR, CISA), B = habituellement fiable (éditeur CTI réputé — Mandiant, CrowdStrike), C = assez fiable (source avec un historique mixte), D = habituellement non fiable, E = non fiable, F = fiabilité inévaluable (nouvelle source sans historique). La **crédibilité de l'information** (1 à 6) : 1 = confirmée (corroborée par au moins une source indépendante), 2 = probablement vraie (cohérente avec ce qu'on sait, source fiable), 3 = possiblement vraie (pas d'incohérence mais pas de corroboration), 4 = douteuse (incohérences mineures), 5 = improbable (incohérences majeures), 6 = crédibilité inévaluable.

La cotation systématique de chaque source et de chaque information dans le TIP (OpenCTI, MISP) est une discipline fondamentale. Pas de renseignement sans cotation.

## 12.2 Les biais des sources

Les **rapports vendor** ont un biais commercial : l'éditeur a intérêt à dramatiser la menace (pour vendre ses produits et services de CTI), à nommer ses découvertes avec des noms accrocheurs (pour la couverture médiatique), et à attribuer à des acteurs étatiques (plus impressionnant que « cybercriminel inconnu »). Ce biais ne rend pas les rapports inutilisables — il rend nécessaire la lecture critique. L'analyste qui prend un rapport Mandiant comme vérité absolue fait une erreur ; l'analyste qui le lit en évaluant les évidences présentées, en identifiant les lacunes, et en formulant ses propres conclusions fait son travail.

Les **rapports gouvernementaux** ont un biais politique : l'attribution publique par un gouvernement (US, UK, EU) sert parfois un objectif diplomatique autant que sécuritaire. L'attribution de NotPetya à la Russie en 2018 était techniquement solide mais aussi politiquement motivée. L'analyste utilise ces attributions comme un indice (source généralement fiable, crédibilité élevée) mais ne les traite pas comme des preuves — il les évalue avec la même rigueur que les autres sources.

---
