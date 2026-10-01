---
title: Chapitre 6 — Services d'infrastructure vitaux
source: IT/06 Infrastructure & architecture/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

DHCP, NTP, PKI et synchronisation

*Les briques « silencieuses » qui conditionnent tout le reste — on les oublie jusqu'au jour où elles tombent et plus rien ne fonctionne.*

## 6.1 DHCP

DHCP (Dynamic Host Configuration Protocol) attribue automatiquement les adresses IP, les masques de sous-réseau, les passerelles, et les serveurs DNS aux machines qui se connectent au réseau. En sécurité : un **rogue DHCP** (serveur DHCP malveillant installé par un attaquant sur le réseau) peut distribuer des configurations qui redirigent tout le trafic vers l'attaquant (passerelle malveillante → interception MITM, serveur DNS malveillant → résolution de noms falsifiée). Protection : **DHCP snooping** (fonctionnalité du switch qui bloque les réponses DHCP provenant de ports non autorisés). En investigation : les **baux DHCP** sont une source précieuse pour la corrélation — ils permettent de savoir quelle machine avait quelle IP à quel moment (logs du serveur DHCP → lier une IP suspecte à une machine physique).

## 6.2 NTP

NTP (Network Time Protocol) synchronise les horloges de toutes les machines. C'est la brique la plus sous-estimée en sécurité — et pourtant l'une des plus critiques.

Si les horloges des serveurs sont désynchronisées : les **corrélations de logs du SIEM sont fausses** (un événement à 14:03:12 sur le firewall et un événement à 14:10:47 sur l'AD peuvent être le même événement si le décalage est de 7 minutes — l'investigation devient impossible), les **timestamps forensiques sont inutilisables** (la chronologie d'une intrusion repose sur la précision des horodatages), et **Kerberos refuse les authentifications** si l'écart entre le client et le DC dépasse 5 minutes (MaxClockSkew — un NTP défaillant peut provoquer des pannes d'authentification en cascade).

La configuration correcte : toutes les machines pointent vers le même serveur NTP interne (ou un pool NTP de confiance — fr.pool.ntp.org, time.google.com), le serveur NTP interne est synchronisé sur une source de stratum 1 ou 2, et la synchronisation est vérifiée régulièrement. Sécurisation : NTS (Network Time Security — authentification des réponses NTP), restriction des sources (seuls les serveurs NTP autorisés peuvent distribuer le temps).

## 6.3 PKI interne et AC interne

Une PKI interne (Public Key Infrastructure) permet à l'organisation d'émettre ses propres certificats pour les services internes (serveurs web internes en HTTPS, mTLS entre microservices, authentification de machines, signature de code interne). L'**autorité de certification interne** (AC / CA) est la racine de confiance — si elle est compromise, n'importe qui peut émettre des certificats de confiance pour n'importe quel service interne, ce qui permet l'interception MITM de tout le trafic chiffré interne.

La gestion des certificats internes est un défi opérationnel : inventaire (quels certificats existent, sur quels serveurs, avec quelle date d'expiration), renouvellement (les certificats expirés causent des pannes de service — monitoring des expirations), et révocation (CRL ou OCSP interne — comment révoquer un certificat compromis).

Dans les environnements Windows, **AD CS** (Active Directory Certificate Services) est l'implémentation standard de la PKI interne. Une AC interne AD CS mal configurée peut devenir un vecteur d'escalade de privilèges majeur — les techniques ESC (Escalation via Certificate Services, documentées par SpecterOps/Will Schroeder) permettent à un attaquant de demander un certificat au nom d'un Domain Admin et d'obtenir un accès total au domaine. Le cours Active Directory de la bibliothèque traite ces attaques en profondeur.

## 6.4 Synchronisation d'identité — AD Connect / Entra Connect

AD Connect (renommé Entra Connect) synchronise les identités de l'Active Directory on-premise vers Azure AD/Entra ID. C'est la brique qui permet le hybrid AD — les utilisateurs se connectent avec le même compte en on-premise et en cloud.

Le risque : le serveur AD Connect a accès à **tous les mots de passe** (il synchronise les hash ou effectue du password hash sync) — c'est une cible critique, aussi sensible qu'un contrôleur de domaine. Les erreurs de configuration courantes : synchronisation de comptes admin vers le cloud (le compte Domain Admin ne devrait PAS être synchronisé), pas de filtering (tous les comptes sont synchronisés, y compris les comptes de service et les comptes à privilèges), et serveur AD Connect non durci (pas de tiering, pas de monitoring, pas d'EDR).

## 6.5 Fil rouge — BACKBONE : les services vitaux de CargoPlex

> **🔧 BACKBONE — Épisode 3**
>
> Lucas audite les services vitaux. NTP : les serveurs utilisent 3 sources différentes (2 serveurs Linux pointent vers pool.ntp.org, les Windows pointent vers le DC, et les équipements réseau pointent vers un serveur NTP public américain) — résultat : 7 minutes d'écart entre les serveurs Linux et les serveurs Windows. Les corrélations SIEM sont faussées. PKI : l'AC interne (AD CS) utilise un certificat racine auto-signé expiré depuis 8 mois — les alertes de certificat sont ignorées par les utilisateurs (ils ont pris l'habitude de cliquer « continuer quand même »), et 3 templates de certificats ont des permissions trop larges (ESC1 — n'importe quel utilisateur authentifié peut demander un certificat avec le SAN d'un admin). AD Connect : le serveur est un Windows Server 2016 non durci, pas dans le Tier 0, sans EDR, avec un compte de service Domain Admin.

---
