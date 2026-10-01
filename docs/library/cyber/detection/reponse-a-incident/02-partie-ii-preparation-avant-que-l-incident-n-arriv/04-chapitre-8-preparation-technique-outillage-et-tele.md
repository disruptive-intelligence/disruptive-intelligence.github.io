---
title: 'Chapitre 8 — Préparation technique : outillage et télémétrie'
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 8.1 Les outils qui doivent être en place AVANT l'incident

**EDR (Endpoint Detection and Response)** : déployé sur TOUS les endpoints — pas 85 %, pas 92 %, tous. Chaque machine non couverte est un angle mort dans lequel l'attaquant peut se cacher sans être détecté. L'EDR est le premier capteur de l'investigation (il fournit la telemetry qui reconstitue les actions de l'attaquant) et le premier outil de confinement (network containment, kill process). Les leaders du marché en 2025-2026 incluent CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, et Palo Alto Cortex XDR. Le choix dépend du contexte (environnement, budget, intégration avec le SIEM), mais la couverture à 100 % est non négociable.

**SIEM (Security Information and Event Management)** : collecte centralisée des logs critiques avec capacité de recherche et de corrélation. Les sources minimales à collecter : Windows Event Logs (Security, System, PowerShell, Sysmon si déployé), logs Active Directory (réplication, modifications d'objets), logs pare-feu (flux autorisés et refusés), logs proxy (URLs, user-agents, volumes), logs DNS (résolutions), logs VPN (connexions), et logs des solutions de sécurité (EDR, antivirus). Les plateformes courantes : Splunk, Microsoft Sentinel, Elastic Security (ELK), QRadar, Chronicle (Google). Le choix dépend du volume de logs, du budget, et des compétences disponibles.

**NDR (Network Detection and Response)** : pas obligatoire mais extrêmement précieux. Le NDR capture et analyse le trafic réseau en temps réel, détecte les anomalies (beaconing, exfiltration, mouvement latéral), et fournit une visibilité que les logs endpoint et SIEM ne donnent pas (notamment sur les systèmes sans EDR — serveurs legacy, équipements réseau, systèmes OT).

**Outils de collecte forensic pré-packagés** : clés USB bootables contenant KAPE (collecte automatisée d'artefacts Windows), Velociraptor (collecte et hunting à grande échelle), DumpIt ou WinPmem (acquisition mémoire), et des scripts de triage personnalisés. Ces kits doivent être prêts à l'emploi, testés, et accessibles physiquement (pas sur un partage réseau qui sera chiffré).

## 8.2 Rétention des logs

La durée de rétention des logs détermine la profondeur de l'investigation. Le dwell time médian (temps entre la compromission et la détection) est de 10 à 15 jours pour les ransomwares, mais peut atteindre des mois pour l'espionnage. Si les logs ne sont conservés que 30 jours et que l'attaquant est dans le réseau depuis 5 semaines, les traces du patient zéro sont perdues.

Minimum recommandé : 6 mois de rétention sur le SIEM chaud (recherche immédiate), 12 mois en stockage froid (archivage consultable). Pour les environnements à risque élevé (OIV, secteur financier, défense) : 12 mois chaud, 24 mois froid.

Le cas critique de Microsoft 365 : la rétention des Unified Audit Logs dépend de la licence. En E3 (la licence la plus courante en entreprise), la rétention est de 180 jours (améliorée par Microsoft en 2023, contre 90 jours auparavant pour certains types de logs). En E5, la rétention peut aller jusqu'à 365 jours. Cette différence est critique pour l'investigation — et elle est souvent découverte trop tard, au moment de l'incident.

## 8.3 Horodatage, sauvegardes, isolation et accès d'urgence

**Synchronisation NTP :** si les horloges des machines ne sont pas synchronisées, la corrélation des événements entre sources est impossible. La synchronisation NTP sur tous les systèmes est un prérequis trivial mais souvent négligé.

**Sauvegardes :** les sauvegardes doivent être segmentées du réseau principal (pas un NAS sur le même VLAN — le ransomware le chiffrera en même temps que les serveurs), testées régulièrement (une sauvegarde non testée est une promesse non vérifiée), et idéalement immuables (stockage WORM, cloud avec versioning et MFA delete protection) ou offline (bandes magnétiques, rotation hebdomadaire). Le ransomware cible systématiquement les sauvegardes — c'est même souvent sa première cible après la compromission de l'AD, car l'attaquant sait que la volonté de payer la rançon est directement proportionnelle à l'indisponibilité des sauvegardes.

**Capacité d'isolation réseau :** VLAN de quarantaine pré-configuré, ACL pare-feu prêtes à être activées (pas à écrire en urgence à 3h du matin), capacité d'isolation via EDR (network containment à distance), et éventuellement un kill switch réseau (coupure totale de l'accès Internet en un clic — procédure documentée et testée).

**Comptes et accès d'urgence :** comptes d'administration « break glass » (non synchronisés avec l'AD principal, stockés de manière sécurisée — coffre-fort physique, gestionnaire de mots de passe hors SI), accès console aux équipements réseau (si le réseau est compromis, les accès in-band via SSH ou HTTPS peuvent être inaccessibles), et accès physique aux datacenters (badges, clés).

## 8.4 Fil rouge — BLACKTIDE : forces et faiblesses techniques

> **🔍 BLACKTIDE — Épisode 8**
>
> **Forces :** EDR CrowdStrike Falcon déployé sur 92 % du parc (les 3 DC compromis sont couverts — c'est ce qui a permis la détection). SIEM Splunk avec 9 mois de rétention (suffisant pour remonter au patient zéro à J-35). Horodatage NTP synchronisé sur tout le parc. Logs pare-feu conservés 12 mois.
>
> **Faiblesses :** 8 % du parc sans EDR (postes legacy, serveurs OT, équipements réseau — autant d'angles morts). Pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu). Microsoft 365 en licence E3 (rétention UAL de 180 jours — suffisant pour cet incident, mais pas pour un espionnage long terme). Sauvegardes quotidiennes sur NAS réseau, sur le même VLAN que les serveurs de fichiers (elles seront partiellement chiffrées par le ransomware). Sauvegardes hebdomadaires sur bandes offline (intactes — seule sauvegarde exploitable, mais avec 6 jours de perte de données). Comptes break glass : inexistants. PowerShell script block logging : non activé sur tous les postes (activé uniquement sur les serveurs — lacune sur les postes de travail).

---
