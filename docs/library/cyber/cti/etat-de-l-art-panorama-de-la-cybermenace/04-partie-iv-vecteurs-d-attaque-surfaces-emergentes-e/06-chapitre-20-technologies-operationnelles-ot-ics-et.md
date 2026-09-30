---
title: Chapitre 20 — Technologies opérationnelles (OT/ICS) et convergence IT-OT
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

## 20.1 — Le ciblage des systèmes industriels

Les systèmes OT (Operational Technology) et ICS (Industrial Control Systems) contrôlent les processus physiques dans les secteurs énergie, eau, transport, industrie manufacturière et infrastructures critiques. Leur compromission peut avoir des conséquences physiques directes — coupures d'électricité, perturbation de la distribution d'eau, arrêt de lignes de production.

Le ciblage OT émane de trois catégories d'acteurs. Les **acteurs étatiques** (Sandworm/GRU, Volt Typhoon/Chine, Cyber Av3ngers/Iran) ciblent l'OT pour le prépositionnement ou le sabotage. Les **hacktivistes** (Z-PENTEST-ALLIANCE, IDS) ciblent l'OT pour l'impact psychologique et la démonstration de capacité. Les **ransomware** ciblent l'OT comme extension de la compromission IT — le chiffrement de systèmes IT de gestion peut paralyser les opérations OT même sans ciblage direct des contrôleurs.

## 20.2 — L'attaque destructive contre les infrastructures électriques polonaises

L'attaque de fin 2025 contre les infrastructures électriques polonaises est l'événement OT le plus significatif de la période. L'ANSSI la décrit comme « une première pour un État membre de l'Union européenne » — un seuil franchi qui matérialise le scénario de cyberattaque destructive sur les infrastructures critiques européennes. L'objectif était de « provoquer des coupures d'électricité et de chauffage pour un nombre conséquent de citoyens ».

Cet événement place la menace OT dans une catégorie différente du hacktivisme démonstratif : il s'agit d'une tentative de **sabotage à effet physique**, potentiellement attribuable à un acteur étatique. L'ANSSI note que la France se prépare à une « augmentation massive — d'ici 2030 — des attaques hybrides avec des effets concrets voire destructeurs sur nos infrastructures critiques ».

## 20.3 — Convergence IT-OT : risques et remédiation

La convergence IT-OT — l'interconnexion croissante des réseaux industriels avec les réseaux informatiques d'entreprise — crée de nouvelles surfaces d'attaque. Un attaquant qui compromet le réseau IT corporate peut potentiellement pivoter vers le réseau OT si la segmentation est insuffisante. Les cas documentés par l'ANSSI incluent des ransomware déployés sur les réseaux IT de prestataires qui ont impacté les opérations OT de leurs clients.

Les particularités de la sécurité OT compliquent la remédiation : les systèmes ont des cycles de vie longs (15-30 ans), utilisent des protocoles propriétaires ou legacy, ne supportent pas toujours les mises à jour de sécurité, et fonctionnent sous des contraintes de disponibilité extrêmes (24/7, pas de fenêtre de maintenance). L'ASD australien opère des programmes spécifiques de cybersécurité OT — le Critical Infrastructure Uplift Program (CI-UP) — qui fournissent des services d'audit, de durcissement et de formation aux opérateurs d'infrastructures critiques.

## 20.4 — 🔴 Fil rouge : scan OT par Z-PENTEST-ALLIANCE

> **📌 FIL ROUGE — Épisode 20**
>
> En octobre 2025, le SOC d'EuroDefense détecte des scans réseau ciblant les interfaces de gestion d'un système SCADA dans l'usine de production aéronautique du groupe. Les adresses IP source correspondent à un range associé à Z-PENTEST-ALLIANCE dans un feed CTI. Le système SCADA est accessible depuis un segment réseau qui n'aurait pas dû être exposé — une erreur de configuration découverte lors de l'incident.
>
> Sophie évalue : l'impact potentiel est limité (les scans n'ont pas abouti à une intrusion), mais le risque réputationnel est élevé (Z-PENTEST-ALLIANCE publie des vidéos de ses intrusions OT sur Telegram). Elle recommande : correction immédiate de la segmentation réseau, audit complet de la surface OT exposée, et mise en place d'un monitoring spécifique OT (IDS industriel). Elle note dans son CTL : « La menace hacktiviste sur l'OT d'EuroDefense est réelle mais actuellement limitée en impact. Le risque principal n'est pas le hacktivisme lui-même mais les déficiences de segmentation qu'il révèle — déficiences qui pourraient être exploitées par un acteur étatique avec des capacités et des intentions très différentes. »

> **🎯 CAPSTONE Partie IV** : Pour une organisation industrielle multi-sectorielle (défense/spatial/industrie), cartographier les 10 vecteurs d'attaque les plus pertinents, évaluer les 3 tendances émergentes les plus préoccupantes (horizon 18 mois), et formuler 5 recommandations d'anticipation priorisées P0/P1/P2 avec justification fondée sur la menace réelle.

---
