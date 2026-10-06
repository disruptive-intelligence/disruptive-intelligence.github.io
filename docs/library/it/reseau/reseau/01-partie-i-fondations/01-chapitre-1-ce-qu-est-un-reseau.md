---
title: Chapitre 1 — Ce qu'est un réseau
source: IT/04 Réseau/Comprendre le réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 1.1 Définition et types de réseaux

Un **réseau** est un ensemble d'appareils interconnectés capables d'échanger des données. On les classe d'abord par étendue :

| Type | Étendue | Exemple |
|---|---|---|
| **LAN** (*Local Area Network*) | Un bâtiment, un site | Réseau d'une entreprise, d'une maison |
| **WLAN** | LAN sans fil | Wi-Fi d'un bureau |
| **WAN** (*Wide Area Network*) | Région, pays, monde ; relie plusieurs LAN | Internet, liaison entre deux sites |
| **WWAN** | Réseau étendu sans fil | Réseau mobile 4G/5G |

Un LAN se raccorde au WAN de son fournisseur d'accès (FAI) par un routeur : c'est ainsi qu'un réseau local accède à Internet.

## 1.2 Les équipements

| Équipement | Couche | Rôle |
|---|---|---|
| **Terminaux** (*end devices*) | — | Postes, serveurs, téléphones : ils émettent et reçoivent les données |
| **Carte réseau** (NIC) | 1-2 | Interface physique entre l'appareil et le support ; porte une adresse MAC unique |
| **Concentrateur** (hub) | 1 | Répète le signal sur tous les ports (obsolète) |
| **Commutateur** (switch) | 2 | Relie les appareils d'un même LAN ; transmet chaque trame au seul port du destinataire grâce à sa **table CAM** (MAC ↔ port) |
| **Routeur** | 3 | Relie des réseaux différents ; choisit le chemin grâce à sa **table de routage** et aux protocoles de routage (OSPF, BGP…) |
| **Point d'accès Wi-Fi** (WAP) | 2 | Passerelle entre les clients sans fil et le réseau filaire |
| **Pare-feu, proxy, IDS** | 3 à 7 | Filtrent et surveillent le trafic (Ch.16) |

Les équipements dits **intermédiaires** (switch, routeur, point d'accès, modem) n'ont qu'un rôle : faire circuler les données entre terminaux.

## 1.3 Transmission : types, modes et supports

| Notion | Valeurs |
|---|---|
| **Type de signal** | Analogique (signal continu, radio FM) ; numérique (bits) |
| **Mode** | *Simplex* : un seul sens (clavier → ordinateur) ; *half-duplex* : deux sens, à tour de rôle (talkie-walkie) ; *full-duplex* : deux sens simultanés (téléphone) |
| **Supports filaires** | Paire torsadée (Ethernet, RJ45), coaxial, fibre optique |
| **Supports sans fil** | Ondes radio (Wi-Fi, mobile), micro-ondes (satellite), infrarouge (courte portée) |

Un **protocole** est l'ensemble des règles qui fixent le format des données et la manière de les traiter, pour que des appareils différents se comprennent.

## 1.4 Architectures

| Architecture | Contrôle | Passage à l'échelle | Administration | Usage |
|---|---|---|---|---|
| **Client-serveur** | Centralisé | Moyen | Simple | Sites web, messagerie |
| **Pair à pair** (P2P) | Décentralisé | Élevé | Complexe (pas de point central) | Partage de fichiers, blockchain |
| **Hybride** | Partiellement centralisé | Élevé | Plus complexe | Messageries, visioconférence |
| **Cloud** | Centralisé chez un fournisseur | Élevé | Simple | Stockage, SaaS, PaaS |
| **SDN** (*Software-Defined Networking*) | Plan de contrôle centralisé | Élevé | Outils spécialisés | Centres de données, grandes entreprises |

En **client-serveur**, les clients envoient des requêtes (un navigateur demande une page) et des serveurs centralisés y répondent. En **P2P**, chaque nœud est à la fois client et serveur et partage directement ses ressources.

## 1.5 Segmenter : VLAN, ACL et zones

- Un **VLAN** (*Virtual LAN*) découpe logiquement un réseau physique en plusieurs domaines de diffusion isolés (postes, serveurs, imprimantes, invités…), sans matériel dédié.
- Une **ACL** réseau est une liste de règles (source, destination, port, action) qui détermine quel trafic peut passer entre deux segments.
- Les **paires de zones** (*zone pairs*) appliquent une politique dans un seul sens à la fois (LAN → DMZ, DMZ → LAN), ce qui permet d'autoriser une direction sans ouvrir l'autre.

> **Pourquoi segmenter ?** Une machine compromise ne voit que son segment : la segmentation limite la propagation latérale et réduit le bruit à surveiller.

---
