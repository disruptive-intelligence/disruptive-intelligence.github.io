---
title: Chapitre 4 — L'écosystème d'outils au-delà du SIEM
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 4.1 EDR — la visibilité endpoint

L'EDR (Endpoint Detection and Response) est l'outil le plus important pour l'analyste SOC après le SIEM. Il offre une visibilité granulaire sur chaque endpoint (processus, fichiers, réseau, registre) et des capacités de réponse (isolation, quarantaine, collecte d'artefacts).

**CrowdStrike Falcon** : leader marché, cloud-native, threat intelligence intégrée. Le process tree est le cœur de l'investigation : chaque alerte montre la chaîne complète des processus avec les connexions réseau, les fichiers créés, et les modifications de registre. Langage de requête : Event Search (SPL-like). Réponse : containment réseau, Real Time Response (shell distant sur l'endpoint — attention aux droits, ce n'est pas pour tout le monde).

**SentinelOne** : autonome (IA locale pour la détection et la réponse automatique), Storyline (reconstruction automatique de la chaîne d'attaque). Langage : Deep Visibility (SQL-like). Réponse : rollback (restauration de l'état pré-attaque — unique à SentinelOne, utile pour les ransomwares).

**Microsoft Defender for Endpoint (MDE)** : intégration native avec Sentinel, M365, et Intune. Langage : KQL via Advanced Hunting. Très performant dans les environnements Microsoft. Réponse : isolation, collecte d'investigation package, live response.

## 4.2 NDR, SOAR, UEBA et outils complémentaires

Le **NDR** (Network Detection and Response — Darktrace, Vectra, Corelight/Zeek) offre une visibilité réseau qui complète l'EDR : détection de beaconing, analyse de trafic chiffré par métadonnées (JA3/JA4, taille des paquets, intervalles), et mouvement latéral réseau.

Le **SOAR** (Security Orchestration, Automation and Response — Cortex XSOAR, Splunk SOAR, TheHive + Cortex, Tines, Shuffle) automatise les actions répétitives : enrichissement d'alerte, création de ticket, blocage d'IoC, isolation d'endpoint. Le SOAR est le multiplicateur d'efficacité du SOC — traité en profondeur au Ch.31.

L'**UEBA** (User and Entity Behavior Analytics) établit des baselines d'activité normale et détecte les anomalies (connexion à une heure inhabituelle, accès à un volume de données anormal, changement de comportement). Forces : détection d'anomalies sans règle prédéfinie. Limites : beaucoup de FP si la baseline est mal calibrée, courbe d'apprentissage longue, tendance à l'excès d'alertes.

Les **TIP** (MISP, OpenCTI) gèrent les feeds CTI et injectent les IoC dans le SIEM. Les **sandbox** (ANY.RUN, Joe Sandbox, Hybrid Analysis) analysent dynamiquement les fichiers suspects. **Velociraptor** (open source) permet la collecte forensic et le hunting à distance via VQL sur l'ensemble du parc — c'est l'outil de prédilection du L3 et du hunter.

## 4.3 Fil rouge — FALCONWATCH : les outils mobilisés

> **🛡️ FALCONWATCH — Épisode 3**
>
> Karim utilise l'écosystème CyberShield pour l'investigation Norexia : CrowdStrike Falcon (EDR — process tree, isolation, collecte), Splunk (SIEM — corrélation multi-sources, requêtes SPL), TheHive (ticketing — documentation de l'investigation), et VirusTotal (enrichissement du hash de lib.dll). Le hash SHA-256 de lib.dll est soumis à VirusTotal : 0 détection. C'est un malware custom, non référencé — signe d'un attaquant qui investit dans l'évasion. Soumission à ANY.RUN : la DLL établit une connexion HTTPS vers `185.xx.xx.xx:443` avec un beaconing de 45 secondes et un user-agent custom. Le C2 est confirmé.

---
