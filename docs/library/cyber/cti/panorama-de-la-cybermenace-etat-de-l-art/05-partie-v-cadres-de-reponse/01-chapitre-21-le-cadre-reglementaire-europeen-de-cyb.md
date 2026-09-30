---
title: Chapitre 21 — Le cadre réglementaire européen de cybersécurité
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE V — Cadres de réponse
  - index.md
---

## 21.1 — NIS2 : la directive socle

La directive NIS2 (Network and Information Security 2) constitue le socle réglementaire européen de cybersécurité. Son périmètre est considérablement élargi par rapport à NIS1 : elle couvre 18 secteurs classés en haute criticité (énergie, transport, banque, santé, eau potable, infrastructure numérique, espace, administration publique, etc.) et autres critiques (services postaux, gestion des déchets, industrie chimique, agroalimentaire, fabrication, recherche, etc.).

La distinction entre **entités essentielles** (soumises à un régime de supervision complet) et **entités importantes** (régime allégé) détermine le niveau d'obligations. L'article 21 impose des mesures de gestion des risques proportionnées et appropriées, couvrant : l'analyse des risques, la gestion des incidents, la continuité d'activité, la sécurité de la chaîne d'approvisionnement, la gestion des vulnérabilités, les pratiques de base en cyber-hygiène, l'utilisation de la cryptographie, la sécurité des ressources humaines, et les politiques de contrôle d'accès.

La transposition dans les droits nationaux est en cours, avec des variations significatives entre États membres. L'ANSSI note que les réglementations françaises et européennes — NIS2 et le CRA — « permettent de définir et imposer des socles de mesures de sécurité et d'élever le niveau de maturité global de la Nation ».

Pour le praticien, NIS2 fait du CTL un livrable quasi-obligatoire : la gestion des risques « tenant compte de l'état de l'art » suppose une connaissance actualisée du paysage de menace. Un RSSI qui ne dispose pas d'un CTL ne peut pas démontrer que ses mesures de sécurité sont proportionnées aux menaces réelles.

## 21.2 — Cyber Resilience Act (CRA) : sécurité des produits numériques

Le CRA, publié au Journal officiel en novembre 2024, est la première législation européenne imposant des exigences de cybersécurité pour les produits avec des éléments numériques tout au long de leur cycle de vie. L'ENISA note que le CRA « devrait avoir un impact significatif sur le développement, les opérations et le décommissionnement des systèmes spatiaux ». Le CRA est décrit par Microsoft comme potentiellement le « gold standard » mondial de la cybersécurité des produits, à l'instar de ce que le RGPD a été pour la protection des données.

Les obligations incluent la sécurité par conception et par défaut, la gestion des vulnérabilités tout au long du cycle de vie, la notification des vulnérabilités activement exploitées, et la génération de SBOM (Software Bills of Materials). Pour les fabricants, cela implique une transformation des processus de développement et de maintenance.

## 21.3 — DORA : résilience du secteur financier

Le règlement DORA (Digital Operational Resilience Act) impose au secteur financier des exigences spécifiques de résilience opérationnelle numérique : gestion des risques ICT, notification d'incidents, tests de résilience (y compris des tests de pénétration fondés sur des scénarios de menace — Threat-Led Penetration Testing), gestion des risques liés aux prestataires ICT tiers, et partage d'informations sur les cybermenaces.

## 21.4 — Articulation réglementaire

L'écosystème réglementaire européen est dense : NIS2 (obligations sectorielles), CRA (produits), DORA (finance), EU Cybersecurity Act (certification), RGPD (données personnelles), Cyber Solidarity Act (coordination de crise via EU-CyCLONe). L'articulation entre ces textes est un enjeu opérationnel : un incident de ransomware impliquant une fuite de données personnelles dans une entité essentielle du secteur financier active simultanément NIS2 (notification d'incident), DORA (gestion ICT), et RGPD (violation de données). Les délais, formats et destinataires de notification diffèrent, créant une charge de conformité significative.

Microsoft note le risque de la **fragmentation réglementaire** : « des cadres réglementaires fragmentés peuvent ralentir la réponse à incident et finalement affaiblir les défenses ».

## 21.5 — 🔴 Fil rouge : audit NIS2

> **📌 FIL ROUGE — Épisode 21**
>
> En octobre 2025, l'audit NIS2 d'EuroDefense approche. Sophie doit démontrer que le CTL du groupe alimente effectivement la gestion des risques. Elle produit un document de traçabilité montrant comment les menaces identifiées dans le CTL sont mappées sur les mesures de sécurité de l'article 21 NIS2 : chaque menace est associée à une mesure de mitigation, un niveau de maturité actuel, et un plan d'action avec échéance. Le CRA impose un audit supplémentaire sur la branche spatial (composants avec éléments numériques destinés à des satellites). DORA ne s'applique pas directement à EuroDefense (secteur industriel, pas financier) mais plusieurs de ses clients bancaires exigent une conformité de facto via leurs clauses contractuelles.

---
