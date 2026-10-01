---
title: Chapitre 7 — Traitement et structuration
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - Partie II — Le cycle du renseignement appliqué
  - index.md
---

## 7.1 De la donnée brute au matériau analysable

Le traitement est la phase souvent négligée entre la collecte et l'analyse. Elle est pourtant déterminante : si les données sont mal normalisées, mal dédoublonnées, ou mal enrichies, l'analyse en souffrira.

La **normalisation** résout le problème des formats hétérogènes : un même IoC (domaine C2) peut apparaître sous 5 formes différentes dans 5 sources (avec ou sans protocole, avec ou sans port, avec ou sans defanging `hxxps://`). La normalisation le ramène à une forme canonique unique. Les noms d'acteurs sont normalisés vers un identifiant de référence (l'ID MITRE ou Malpedia) avec les alias comme métadonnées.

Le **dédoublonnage** identifie les doublons (le même rapport repris par 10 sources, le même IoC dans 5 feeds). L'analyste identifie la source primaire (le rapport original de l'éditeur) et les sources secondaires (les reprises). La source primaire est fiable ; les reprises ne la « corroborent » pas — elles la propagent. C'est le piège de la circularité (Ch.14).

L'**enrichissement automatisé** ajoute du contexte aux données brutes : un hash → soumission VirusTotal → famille de malware, detection rate, sandbox reports. Un domaine → Whois + passive DNS → dates d'enregistrement, registrar, IP hébergement, certificats. Une IP → géolocalisation + ASN + réputation (AbuseIPDB, GreyNoise). Un CVE → CVSS score + EPSS score + statut CISA KEV + exploitation ITW confirmée.

## 7.2 Les TIP (Threat Intelligence Platforms)

Les TIP sont l'outil central de structuration et de gestion du renseignement CTI. Ils stockent les IoC, les profils d'acteurs, les campagnes, et les relations entre eux, dans un format structuré (STIX) interrogeable et partageable.

**MISP** (Malware Information Sharing Platform, open source) : la référence communautaire, utilisée par de nombreux CERT et ISACs. Forces : gratuit, communauté massive, intégration riche (STIX/TAXII, SIEM, EDR). Limites : interface utilisateur datée, courbe d'apprentissage, nécessite de l'administration.

**OpenCTI** (open source, développé par Filigran) : la plateforme montante en 2024-2026, conçue spécifiquement pour la CTI analytique (pas seulement le partage d'IoC). Forces : modèle de données riche (STIX 2.1 natif), visualisation de graphes de relations, intégration ATT&CK, connecteurs multiples. Limites : nécessite une infrastructure (Elasticsearch, Redis, RabbitMQ), courbe d'apprentissage.

**ThreatConnect** et **Anomali** (commerciaux) : plateformes intégrées avec enrichissement, scoring, et orchestration. Forces : interface mature, support commercial, intégration SOAR. Limites : coût élevé.

## 7.3 Le problème de la qualité des données

Garbage in, garbage out : un IoC mal formaté propagé dans le SIEM génère des faux positifs. Un hash tronqué ne matche avec rien. Une attribution erronée (« ce malware est attribué à APT28 ») propagée dans un feed et intégrée automatiquement dans les profils d'acteurs de dizaines d'organisations crée une fausse certitude collective. La qualité des données est un enjeu permanent de la CTI — chaque IoC doit être vérifié, chaque attribution doit être sourcée, et chaque information automatisée doit être revue.

---
