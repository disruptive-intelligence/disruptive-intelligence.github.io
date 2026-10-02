---
title: Chapitre 2 — Architecture réseau d'entreprise
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

## 2.1 Les zones réseau

L'architecture réseau d'entreprise est structurée en zones de confiance décroissante. La **DMZ** (Demilitarized Zone) est la zone tampon entre Internet et le réseau interne — elle héberge les services exposés (reverse proxy, bastion, VPN gateway, serveurs web publics). Le **LAN** (Local Area Network) héberge les serveurs applicatifs, les bases de données, l'Active Directory, le SIEM — jamais exposés directement à Internet. La **zone d'administration** est un réseau isolé réservé aux outils d'administration (bastion, supervision, SIEM). La **zone OT/IoT** héberge les systèmes industriels (automates, SCADA) — si elle existe, elle doit être physiquement ou logiquement séparée du LAN IT.

## 2.2 Les équipements réseau

Le **switch** connecte les machines dans un même réseau (couche 2) — pertinence sécurité : VLANs, port security, 802.1X. Le **routeur** connecte des réseaux différents (couche 3) — ACLs, filtrage inter-zones. Le **firewall** filtre le trafic selon des règles — point central de sécurité réseau. Le **load balancer** répartit la charge entre serveurs — TLS termination, health checks. Le **reverse proxy** est l'intermédiaire entre clients et serveurs — cache les serveurs internes. Le **WAF** filtre les requêtes HTTP malveillantes. L'**IDS/IPS** détecte et bloque les intrusions.

## 2.3 Le management plane — le réseau d'administration

*Le management plane est la couche d'administration de l'infrastructure — souvent oubliée, toujours critique.*

Chaque équipement d'infrastructure (serveurs physiques, switches, firewalls, hyperviseurs, contrôleurs de stockage) possède une interface d'administration qui fonctionne indépendamment du système d'exploitation principal. Les **iLO** (HP), **iDRAC** (Dell), et **IPMI** (standard générique) sont des contrôleurs d'administration embarqués sur les serveurs physiques — ils permettent d'allumer/éteindre le serveur, d'accéder à la console, de monter des ISO, et de modifier la configuration matérielle, même si l'OS est éteint ou crashé. Les interfaces web d'administration des switches, firewalls et hyperviseurs (vCenter) offrent un contrôle total sur l'équipement.

Le risque est majeur : si ces interfaces sont accessibles depuis le réseau utilisateur (ce qui est le cas dans beaucoup d'organisations), un attaquant qui compromet un poste utilisateur peut accéder à l'administration de toute l'infrastructure physique. Les credentials par défaut (admin/admin sur iLO, root/calvin sur iDRAC) sont rarement changés. Les CVE sur ces interfaces sont régulièrement exploitées.

La solution : un **réseau de management dédié** (management VLAN ou réseau physiquement séparé), accessible uniquement depuis le bastion d'administration. Les interfaces iLO/iDRAC/IPMI, les consoles vCenter, les interfaces d'administration des switches et firewalls ne doivent JAMAIS être accessibles depuis le réseau utilisateur.

## 2.4 L'architecture type

Le schéma type : Internet → firewall externe (+ WAF) → DMZ (reverse proxy, bastion, VPN gateway) → firewall interne → LAN (serveurs applicatifs, bases de données, AD, SIEM, mail) → postes de travail. Le réseau de management est parallèle au LAN, accessible uniquement via le bastion.

NAT (Network Address Translation) traduit les adresses IP privées en publiques — permet à plusieurs machines de partager une seule IP publique. VPN (tunnel chiffré — IPSec pour le site-to-site, OpenVPN/WireGuard pour le remote access). Proxy forward (intermédiaire pour les requêtes sortantes — filtrage URL, logging, cache).

## 2.5 Fil rouge — BACKBONE : le réseau CargoPlex

> **🔧 BACKBONE — Épisode 2**
>
> Lucas dessine le schéma réseau de CargoPlex : un seul firewall Fortinet entre Internet et le LAN, pas de DMZ formalisée, flat network — tous les VLANs communiquent entre eux sans restriction. Le vCenter est accessible depuis les postes utilisateurs. Les interfaces iLO des 12 serveurs physiques sont sur le même réseau avec les credentials par défaut HP (admin/admin). Le NAS de sauvegarde est dans le même VLAN que les postes. En cas de compromission d'un poste utilisateur, l'attaquant peut atteindre directement l'administration de l'infrastructure physique, le vCenter, les sauvegardes, et l'AD.

---
