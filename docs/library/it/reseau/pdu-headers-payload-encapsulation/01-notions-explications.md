---
title: Notions & explications
source: IT/04 Réseau/PDU, headers, payload & encapsulation.md
note: PDU, headers, payload & encapsulation
up:
- - PDU, headers, payload & encapsulation
  - index.md
---

## 1. PDU (Protocol Data Unit)

**Définition** : La PDU est l'unité de données propre à chaque couche du modèle réseau. Chaque couche donne un **nom spécifique** au bloc de données qu'elle manipule.

**Principe clé** : Une PDU = **Header + Payload** (et parfois un **Trailer**)

| Couche OSI | Couche TCP/IP | Nom de la PDU | Protocoles courants |
|------------|---------------|----------------|---------------------|
| Couche 7 — Application | Application | **Data** (données) | HTTP, FTP, SMTP, DNS, SSH |
| Couche 4 — Transport | Transport | **Segment** (TCP) / **Datagramme** (UDP) | TCP, UDP |
| Couche 3 — Réseau | Internet | **Paquet** (Packet) | IP (IPv4, IPv6), ICMP |
| Couche 2 — Liaison | Accès réseau | **Trame** (Frame) | Ethernet, Wi-Fi (802.11) |
| Couche 1 — Physique | Accès réseau | **Bits** | Signaux électriques, optiques, radio |

**Ce qu'il faut retenir** : quand on dit "segment TCP", "paquet IP" ou "trame Ethernet", on parle de la PDU à cette couche. Ce ne sont pas des termes interchangeables — chacun désigne un bloc de données à un niveau précis.

---

## 2. Headers (en-têtes) — structure détaillée

**Définition** : Le header est un bloc de métadonnées ajouté **au début** de la PDU par chaque couche. Il contient les informations de contrôle nécessaires au bon fonctionnement du protocole à cette couche. 

**Principe** : Chaque couche ajoute son propre header. Le header ne contient jamais les données de l'utilisateur — il contient uniquement les informations dont le protocole a besoin pour faire son travail (adressage, contrôle, séquencement, etc.).

---

### Header Ethernet (couche 2) — 14 octets + Trailer 4 octets

| Champ | Taille | Rôle |
|-------|--------|------|
| Préambule | 7 octets | Synchronisation (non compté dans la trame) |
| SFD (Start Frame Delimiter) | 1 octet | Signale le début de la trame |
| MAC Destination | 6 octets | Adresse physique du destinataire sur le réseau local (ou du routeur/passerelle si destination distante) |
| MAC Source | 6 octets | Adresse physique de la NIC émettrice |
| EtherType | 2 octets | Identifie le protocole de la couche supérieure (0x0800 = IPv4, 0x86DD = IPv6, 0x0806 = ARP) |

>**Note** : Ethernet ajoute aussi un **Trailer** (FCS — Frame Check Sequence, 4 octets) à la fin de la trame pour la détection d'erreurs.
>
**Trailer** : Ethernet est l'une des rares couches qui ajoute aussi quelque chose **à la fin** — le **FCS** (Frame Check Sequence, 4 octets), un checksum CRC-32 pour la détection d'erreurs de transmission.

> **Taille d'une trame Ethernet** : 64 à 1518 octets (sans VLAN tagging).

---

### Header IPv4 (couche 3) — 20 octets minimum

| Champ | Taille | Rôle |
|-------|--------|------|
| Version | 4 bits | Version du protocole (4 pour IPv4) |
| IHL (Header Length) | 4 bits | Longueur du header (en mots de 32 bits) |
| DSCP/ToS | 1 octet | Qualité de service, priorité |
| Total Length | 2 octets | Taille totale du paquet (header + payload) |
| Identification, Flags, Fragment Offset | 4 octets | Gestion de la fragmentation |
| TTL (Time To Live) | 1 octet | Nombre max de sauts (routeurs) avant destruction du paquet. Décrementé à chaque routeur, paquet détruit si TTL = 0 (→ ICMP "Time Exceeded") |
| Protocol | 1 octet | Identifie le protocole dans le payload (6 = TCP, 17 = UDP, 1 = ICMP) |
| Header Checksum | 2 octets | Vérification d'intégrité du header IP uniquement |
| Source IP | 4 octets | Adresse IP de l'expéditeur |
| Destination IP | 4 octets | Adresse IP du destinataire |

> **Champ Protocol** : c'est ce champ qui permet à la couche réseau de savoir à quel protocole de transport remettre le payload. Sans lui, IP ne saurait pas s'il doit envoyer la charge utile à TCP ou à UDP.

---

### Header TCP (couche 4) — 20 octets minimum (jusqu'à 60 avec options)

| Champ | Taille | Rôle |
|-------|--------|------|
| Source Port | 2 octets | Port de l'application émettrice (souvent éphémère, ex: 54321) |
| Destination Port | 2 octets | Port de l'application destinataire (ex: 80 = HTTP, 443 = HTTPS) |
| Sequence Number | 4 octets | Numéro de séquence — permet de remettre les données dans l'ordre |
| Acknowledgment Number | 4 octets | Numéro de séquence du prochain octet attendu (pour les ACK) |
| Flags | 6 bits | Indicateurs de contrôle : SYN, ACK, FIN, RST, PSH, URG |
| Window Size | 2 octets | Taille de la fenêtre de réception (contrôle de flux) |
| Checksum | 2 octets | Vérification d'intégrité du segment entier (header + payload) |
| Options | Variable | MSS (Maximum Segment Size), Window Scaling, Timestamps... |

> **Les ports** (Source Port et Destination Port) sont dans le header **TCP/UDP**, **pas** dans le header IP. C'est pour ça qu'un firewall qui filtre par port doit lire au-delà du header IP.

---

### Header UDP (couche 4) — 8 octets (fixe)

| Champ | Taille | Rôle |
|-------|--------|------|
| Source Port | 2 octets | Port de l'application émettrice |
| Destination Port | 2 octets | Port de l'application destinataire |
| Length | 2 octets | Taille totale du datagramme (header + payload) |
| Checksum | 2 octets | Vérification d'intégrité (optionnel en IPv4, obligatoire en IPv6) |

> **Comparaison TCP vs UDP** : le header UDP est 2,5x plus petit que TCP (8 vs 20 octets). Pas de numéro de séquence, pas de flags, pas de fenêtre — c'est ce qui rend UDP plus rapide mais sans garantie de livraison ni d'ordre.

---

### Chaîne d'identification entre couches

Chaque couche utilise un champ spécifique de son header pour savoir **à quel protocole de la couche supérieure remettre le payload** :

```
EtherType (couche 2)  →  identifie le protocole L3  (0x0800 = IPv4, 0x0806 = ARP)
         │
         ▼
Protocol (couche 3)   →  identifie le protocole L4  (6 = TCP, 17 = UDP, 1 = ICMP)
         │
         ▼
Port destination (L4) →  identifie l'application    (80 = HTTP, 443 = HTTPS, 53 = DNS)
```


Sans cette chaîne, les données arriveraient au bon endroit physiquement mais personne ne saurait quoi en faire.

---

## 3. Payload (charge utile)

**Définition** : Le payload est la partie **données** de la PDU. C'est tout ce qui n'est pas le header (ni le trailer). C'est concrètement **ce que la couche transporte pour le compte de la couche supérieure**.

**Principe fondamental** : Le payload d'une couche N = la PDU complète (header + payload) de la couche N+1.

| Couche                 | La PDU               | Son payload contient concrètement...                                                       |
| ---------------------- | -------------------- | ------------------------------------------------------------------------------------------ |
| Couche 2 (Ethernet)    | Trame                | Le **paquet IP en entier** (header IP + tout ce qu'il contient)                            |
| Couche 3 (IP)          | Paquet               | Le **segment TCP ou datagramme UDP en entier** (header TCP/UDP + données applicatives)     |
| Couche 4 (TCP/UDP)     | Segment / Datagramme | Les **données applicatives pures** (requête HTTP, mail SMTP, commande FTP, données SSH...) |
| Couche 7 (Application) | Data                 | Le **contenu final** : page HTML, image JPEG, fichier PDF, texte d'un email...             |
