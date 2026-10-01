---
title: Chapitre 19 — Menaces sur le spatial
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

cybersécurité des systèmes satellitaires

## 19.1 — L'espace comme infrastructure critique

Le secteur spatial est désormais reconnu comme infrastructure critique par NIS2. Les dépendances sont massives : télécommunications (Starlink, constellations commerciales), navigation (GPS, Galileo), observation (imagerie satellite), défense (communications militaires, renseignement), et services financiers (synchronisation temporelle pour le trading haute fréquence). La compromission d'un système satellite peut avoir des effets en cascade sur l'ensemble des secteurs dépendants.

## 19.2 — Taxonomie des menaces spatiales

L'ENISA Space Threat Landscape 2025 fournit la première taxonomie systématique des menaces cyber pesant sur les systèmes satellitaires. La taxonomie distingue les menaces par segment (sol, spatial, utilisateur), par catégorie (activités malveillantes, écoute/interception, attaques physiques, défaillances, legacy), et par impact (confidentialité, intégrité, disponibilité).

Les menaces identifiées incluent : l'injection de code malveillant dans les logiciels embarqués (OBSW), l'exploitation de vulnérabilités dans les systèmes de contrôle au sol, l'interception des communications satellite (TM/TC), le détournement de satellite (hijacking), et les attaques physiques (y compris les armes anti-satellite ASAT). L'utilisation croissante de composants commerciaux (COTS) dans les satellites ajoute les risques classiques de la supply chain logicielle au domaine spatial.

## 19.3 — Scénarios d'attaque documentés

L'ENISA documente deux scénarios d'attaque détaillés.

**Scénario 1 — Compromission du centre de contrôle** : spearphishing ciblant un employé du centre de contrôle → installation d'un malware → reconnaissance réseau → mouvement latéral vers les systèmes de contrôle satellite → vol de credentials → accès aux configurations d'antenne et aux protocoles de communication → exfiltration de données sensibles (protocoles de communication, clés de chiffrement) → capacité de corruption du bus satellite et de la charge utile.

**Scénario 2 — Exploitation OBC/OBSW via code malveillant physique** : accès physique non autorisé à la chaîne d'assemblage ou au conteneur de transport du satellite → implantation de code malveillant via un port IO (USB) → exploitation des misconfiguration du logiciel embarqué → injection de données aléatoires provoquant l'épuisement des ressources du système temps réel (RTOS) → perte de contrôle du segment spatial.

## 19.4 — Cadre de contrôles et régulation

L'ENISA propose un cadre de contrôles de cybersécurité spécifiques au spatial, incluant : la gestion des risques et l'analyse d'impact, la sécurité par conception et par défaut (SDLC), la sécurité physique et environnementale (protection des composants pendant le transport et l'assemblage), la sécurité réseau (segmentation, chiffrement authentifié, désactivation des ports physiques non critiques), et la réponse à incidents adaptée au spatial.

Le cadre normatif inclut : NIS2 (espace comme secteur critique), CRA (sécurité des produits numériques), ECSS (standardisation spatiale européenne), BSI TR-03184 (guide de protection des infrastructures spatiales), NIST IR 8270/8323/8401, et les frameworks SPARTA/SPACE-SHIELD (basés sur MITRE ATT&CK adaptés au domaine spatial).

## 19.5 — 🔴 Fil rouge : audit spatial

> **📌 FIL ROUGE — Épisode 19**
>
> La branche satellite d'EuroDefense développe un composant de charge utile pour un satellite d'observation européen. Le responsable programme demande à Sophie une analyse de risque cyber. En utilisant le Space Threat Landscape ENISA et le framework SPARTA, Sophie identifie trois risques prioritaires : (1) compromission de la supply chain des composants COTS embarqués, (2) attaque sur le centre de contrôle au sol via spearphishing, (3) exploitation de vulnérabilités dans le logiciel de simulation utilisé pendant la phase d'assemblage. Elle recommande un audit de sécurité des fournisseurs COTS, une segmentation réseau stricte entre les systèmes de simulation et le réseau corporate, et un programme de sensibilisation spécifique pour le personnel du centre de contrôle.

---
