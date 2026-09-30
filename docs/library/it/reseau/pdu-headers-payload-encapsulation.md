---
title: PDU, headers, payload & encapsulation
source: IT/03_Networking/PDU_Headers_Payload_Encapsulation.md
---

## Objectif de la section
Comprendre ce qu'est une PDU à chaque couche, la structure concrète des headers et du payload, puis maîtriser le processus d'encapsulation (envoi) et de décapsulation (réception) des données à travers les couches du modèle OSI/TCP-IP. Savoir comment ces éléments s'imbriquent, y compris dans un contexte VPN.

---

## Notions & explications

### 1. PDU (Protocol Data Unit)

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

### 2. Headers (en-têtes) — structure détaillée

**Définition** : Le header est un bloc de métadonnées ajouté **au début** de la PDU par chaque couche. Il contient les informations de contrôle nécessaires au bon fonctionnement du protocole à cette couche. 

**Principe** : Chaque couche ajoute son propre header. Le header ne contient jamais les données de l'utilisateur — il contient uniquement les informations dont le protocole a besoin pour faire son travail (adressage, contrôle, séquencement, etc.).

---

#### Header Ethernet (couche 2) — 14 octets + Trailer 4 octets

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

#### Header IPv4 (couche 3) — 20 octets minimum

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

#### Header TCP (couche 4) — 20 octets minimum (jusqu'à 60 avec options)

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

#### Header UDP (couche 4) — 8 octets (fixe)

| Champ | Taille | Rôle |
|-------|--------|------|
| Source Port | 2 octets | Port de l'application émettrice |
| Destination Port | 2 octets | Port de l'application destinataire |
| Length | 2 octets | Taille totale du datagramme (header + payload) |
| Checksum | 2 octets | Vérification d'intégrité (optionnel en IPv4, obligatoire en IPv6) |

> **Comparaison TCP vs UDP** : le header UDP est 2,5x plus petit que TCP (8 vs 20 octets). Pas de numéro de séquence, pas de flags, pas de fenêtre — c'est ce qui rend UDP plus rapide mais sans garantie de livraison ni d'ordre.

---

#### Chaîne d'identification entre couches

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

### 3. Payload (charge utile)

**Définition** : Le payload est la partie **données** de la PDU. C'est tout ce qui n'est pas le header (ni le trailer). C'est concrètement **ce que la couche transporte pour le compte de la couche supérieure**.

**Principe fondamental** : Le payload d'une couche N = la PDU complète (header + payload) de la couche N+1.

| Couche                 | La PDU               | Son payload contient concrètement...                                                       |
| ---------------------- | -------------------- | ------------------------------------------------------------------------------------------ |
| Couche 2 (Ethernet)    | Trame                | Le **paquet IP en entier** (header IP + tout ce qu'il contient)                            |
| Couche 3 (IP)          | Paquet               | Le **segment TCP ou datagramme UDP en entier** (header TCP/UDP + données applicatives)     |
| Couche 4 (TCP/UDP)     | Segment / Datagramme | Les **données applicatives pures** (requête HTTP, mail SMTP, commande FTP, données SSH...) |
| Couche 7 (Application) | Data                 | Le **contenu final** : page HTML, image JPEG, fichier PDF, texte d'un email...             |
## Récap OSI : PDU + Header + Payload

|         Couche | PDU                              | Header (ajouté par la couche)                                                | Payload (transporté par la couche)                                                     |
| -------------: | -------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 7- Application | Data                             | Header applicatif (ex: HTTP, DNS)                                            | **Contenu final** : page HTML, image JPEG, fichier PDF, texte d'un email...            |
|  4 - Transport | Segment (TCP) / Datagramme (UDP) | TCP/UDP header (Ports src/dst, seq/ack, Windows, Checksumetc.) : 20 vs 8 oct | **Données applicatives pures** (requête HTTP, mail SMTP, commande FTP, données SSH...) |
|     3 - Réseau | IP : Paquet IP                   | IP header (IP src/dst, TTL, protocole…) : 20 oct                             | **Segment TCP / datagramme UDP en entier** (header TCP/UDP + données applicatives)     |
|    2 - Liaison | Ethernet - Trame                 | Ethernet/Wi-Fi header (MAC src/dst, EtherType…) : 14 oct (+4 FCS)            | **Paquet IP en entier** (header IP + tout ce qu'il contient)                           |



---

#### Exemples concrets de payloads applicatifs (couche 7)

**Requête HTTP GET** (tu tapes une URL dans ton navigateur) :
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Requête HTTP POST** (tu soumets un formulaire de login) :
```
POST /login HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded

username=jean&password=secret123
```

**Réponse HTTP** (le serveur renvoie la page) :
```
HTTP/1.1 200 OK
Content-Type: text/html

<html><body><h1>Bienvenue</h1></body></html>
```

**Requête DNS** (résolution de nom) :
```
Query: www.example.com → A record?
```

**Commande SMTP** (envoi d'email) :
```
MAIL FROM:<jean@example.com>
RCPT TO:<alice@example.com>
DATA
Subject: Bonjour
Ceci est un email.
.
```

Tous ces exemples sont des **payloads de la couche transport** (TCP ou UDP). Pour TCP/UDP, ce texte est juste un bloc d'octets à transporter. Pour IP, ce bloc + le header TCP = juste un payload à router. Et ainsi de suite — chaque couche ne voit que son propre niveau.

---

### 4. Vue d'ensemble — La relation Header / Payload / PDU

Le schéma de principe est toujours le même :

```
PDU = Header + Payload
```

Et le payload d'une couche = la PDU complète de la couche du dessus. Voici une vue concrète d'une requête HTTPS traversant toutes les couches :

```
COUCHE APPLICATION (Data)
┌──────────────────────────────────────────┐
│  Données HTTP (GET /page, headers, body) │  ← Données pures
└──────────────────────────────────────────┘
                     │
                     ▼ cette data devient le payload de la couche 4

COUCHE TRANSPORT (Segment TCP)
┌────────────┬─────────────────────────────────────────┐
│ Header TCP │  Payload = Données HTTP                  │
│ (20 oct)   │  (GET /page, headers, body)              │
└────────────┴─────────────────────────────────────────┘
                     │
                     ▼ ce segment entier devient le payload de la couche 3

COUCHE RÉSEAU (Paquet IP)
┌────────────┬──────────────────────────────────────────────────────┐
│ Header IP  │  Payload = Segment TCP entier                        │
│ (20 oct)   │  (Header TCP + Données HTTP)                         │
└────────────┴──────────────────────────────────────────────────────┘
                     │
                     ▼ ce paquet entier devient le payload de la couche 2

COUCHE LIAISON (Trame Ethernet)
┌──────────────┬────────────────────────────────────────────────────────────────┬─────────┐
│ Header Eth   │  Payload = Paquet IP entier                                    │ Trailer │
│ (14 oct)     │  (Header IP + Header TCP + Données HTTP)                       │ (4 oct) │
└──────────────┴────────────────────────────────────────────────────────────────┴─────────┘
```

**Ce qu'il faut voir** : à chaque couche, le header "emballe" tout ce qui vient du dessus. La couche Ethernet ne sait pas qu'elle transporte du HTTP — elle voit juste un bloc d'octets. IP ne sait pas qu'il y a une requête web dans son payload — il voit juste un bloc à router vers l'IP destination. **Chaque couche ne lit que son propre header** et traite le reste comme un payload opaque — c'est le principe d'**indépendance des couches**.

---

### 5. Encapsulation étape par étape (envoi)

**Définition** : Processus par lequel chaque couche ajoute son propre header (et parfois un trailer) autour des données reçues de la couche supérieure, puis transmet cette unité "encapsulée" à la couche inférieure.

**Pourquoi ?** L'encapsulation permet à chaque couche de se concentrer uniquement sur sa fonction prévue, sans se soucier de ce que font les autres couches. Chaque couche traite ce qu'elle reçoit comme un bloc opaque à emballer.

**Principe clé** : À chaque couche, les données reçues de la couche supérieure deviennent le **payload** (charge utile), et la couche ajoute son **header** pour former une nouvelle **PDU** (Protocol Data Unit).

```
Couche N reçoit la PDU de la couche N+1
         │
         ▼
┌──────────────┬──────────────────────────────┐
│ Header       │ Payload                       │
│ (ajouté par  │ (= PDU de la couche N+1,     │
│  couche N)   │   traitée comme un bloc brut) │
└──────────────┴──────────────────────────────┘
         = PDU de la couche N
```

Voici le parcours complet d'une requête HTTPS envoyée depuis un navigateur vers un serveur web.

---

#### Étape 1 — Couches 7-6-5 (Application)

**Action** : L'application produit les données brutes. Possible formatage ou chiffrement applicatif (ex: TLS). Les données sont remises à la couche Transport.

**PDU** : **Data** (Données)

**Exemple concret** :
```
GET / HTTP/1.1\r\nHost: example.com\r\n\r\n
```

**Résultat** :
```
[ Données HTTP ]
```

> C'est le point de départ. L'utilisateur saisit une URL, le navigateur génère la requête HTTP et la transmet à la couche Transport.

---

#### Étape 2 — Couche 4 (Transport)

**Action** : La couche Transport reçoit les données applicatives et les encapsule dans un **segment TCP** ou un **datagramme UDP**. Elle ajoute son header contenant les informations nécessaires à la communication fiable (TCP) ou rapide (UDP).

**PDU** : **Segment** (TCP) / **Datagramme** (UDP)

**Header TCP ajouté** : ports source/destination, sequence number, acknowledgment number, flags, window size, checksum, options (détails → voir section 2).

**Résultat** :
```
[ Header TCP | Données HTTP ]
```

> **Point important** : les ports source/destination sont ajoutés **ici**, à la couche 4. C'est pour ça qu'un firewall doit inspecter au-delà du header IP pour filtrer par port.

---

#### Étape 3 — Couche 3 (Réseau / Internet)

**Action** : La couche Réseau reçoit le segment TCP (ou datagramme UDP) et l'encapsule dans un **paquet IP**. Elle ajoute un header IP contenant les adresses IP source/destination et détermine le prochain saut (next-hop) via la table de routage.

**PDU** : **Paquet** (Packet)

**Header IP ajouté** : version, IHL, DSCP/ToS, total length, identification/flags/fragment offset, TTL, protocol, checksum, IP source, IP destination (détails → voir section 2).

**Résultat** :
```
[ Header IP | Header TCP | Données HTTP ]
```

> **Champ Protocol** : c'est ce champ qui permet au destinataire de savoir à quel protocole de couche 4 remettre le payload (6 → TCP, 17 → UDP).

---

#### Étape 4 — Couche 2 (Liaison de données)

**Action** : La couche Liaison reçoit le paquet IP et l'encapsule dans une **trame** (Ethernet ou Wi-Fi). Elle ajoute un header avec les adresses MAC et un **trailer** (FCS) pour la détection d'erreurs. L'adresse MAC de destination est celle du **prochain saut** (routeur/passerelle), pas celle de la destination finale.

**PDU** : **Trame** (Frame)

**Header Ethernet ajouté** : préambule, SFD, MAC destination, MAC source, EtherType (détails → voir section 2).
**Trailer ajouté** : FCS (4 octets, CRC-32).

**Résultat** :
```
[ Header Ethernet | Header IP | Header TCP | Données HTTP | FCS ]
```

> **MAC destination ≠ IP destination** : c'est un point fondamental. La MAC destination **change à chaque saut** réseau (routeur → routeur), alors que l'IP destination **reste la même** de bout en bout. La MAC est une adresse locale (saut par saut), l'IP est une adresse globale (end-to-end).

---

#### Étape 5 — Couche 1 (Physique)

**Action** : La couche Physique reçoit la trame et la convertit en **signaux physiques** (bits) pour la transmettre sur le média.

**PDU** : **Bits**

| Média               | Type de signal                     | Exemples              |
| ------------------- | ---------------------------------- | --------------------- |
| Câble cuivre (RJ45) | Électrique (variations de tension) | Cat5e, Cat6, Cat6a    |
| Fibre optique       | Optique (impulsions lumineuses)    | Monomode, multimode   |
| Sans fil (Wi-Fi)    | Radio (ondes électromagnétiques)   | 2.4 GHz, 5 GHz, 6 GHz |

**Encodage** : Manchester, NRZ, 4B/5B, etc.

**Débits courants** : 10 Mbps (Ethernet) → 100 Mbps (Fast Ethernet) → 1 Gbps (Gigabit) → 10 Gbps → 100 Gbps

**Résultat** : Suite de 0 et 1 transmis physiquement sur le média.

---

### 6. Vue d'ensemble — Encapsulation complète

```
ENVOI (du haut vers le bas)

Couche 7   │  Données HTTP
           │  GET / HTTP/1.1 ...
           ▼
Couche 4   │  [ Header TCP  │  Données HTTP                         ]
           │    ports, seq#     = payload couche 4
           ▼
Couche 3   │  [ Header IP   │  Header TCP  │  Données HTTP          ]
           │    IPs, TTL        = payload couche 3
           ▼
Couche 2   │  [ Header Eth  │  Header IP  │  Header TCP  │  Data HTTP  │  FCS ]
           │    MACs              = payload couche 2              trailer
           ▼
Couche 1   │  01101001 01010011 11001010 01110101 00101101 ...
           │  → signaux électriques / optiques / radio
```

**Chaque couche emballe la précédente sans la modifier.** L'empilement des headers forme une structure de "poupées russes" — le destinataire les retirera une par une dans l'ordre inverse.

---

### 7. Décapsulation étape par étape (réception)

**Définition** : Processus inverse de l'encapsulation. Côté destinataire, chaque couche retire son header, vérifie les informations de contrôle, et transmet le payload à la couche supérieure.

---

#### Étape 1 — Couche 1 (Physique)

**Action** : Réception des signaux physiques (électriques, optiques, radio) et reconstruction de la trame binaire.

```
01101001 01010011 ... → [ Header Eth | Header IP | Header TCP | Data HTTP | FCS ]
```

---

#### Étape 2 — Couche 2 (Liaison)

**Actions** :
1. **Vérification FCS** → si le checksum CRC-32 ne correspond pas, la trame est **rejetée** (erreur de transmission)
2. **Lecture MAC destination** → si l'adresse correspond à la NIC locale → traiter. Sinon → ignorer (ou router si c'est un switch/routeur)
3. **Lecture EtherType** → détermine à quel protocole couche 3 remettre le payload (0x0800 → IPv4)
4. **Retrait du header Ethernet et du trailer FCS**

**Transmis à la couche 3** :
```
[ Header IP | Header TCP | Données HTTP ]
```

---

#### Étape 3 — Couche 3 (Réseau)

**Actions** :
1. **Vérification checksum IP** → si invalide, le paquet est rejeté
2. **Lecture IP destination** → si correspond à une IP locale → traiter. Sinon → router vers le prochain saut
3. **Décrémentation du TTL** → si TTL = 0, le paquet est détruit (et un message ICMP "Time Exceeded" est renvoyé)
4. **Lecture du champ Protocol** → détermine à quel protocole couche 4 remettre le payload (6 → TCP, 17 → UDP)
5. **Retrait du header IP**

**Transmis à la couche 4** :
```
[ Header TCP | Données HTTP ]
```

---

#### Étape 4 — Couche 4 (Transport)

**Actions** :
1. **Vérification checksum TCP** → si invalide, le segment est rejeté
2. **Lecture port destination** → identifie l'application destinataire (443 → HTTPS)
3. **Gestion du séquencement** → remise des segments dans l'ordre grâce au Sequence Number
4. **Gestion des ACK et retransmissions** → si un segment manque, demande de retransmission
5. **Retrait du header TCP**

**Transmis à la couche 7** :
```
[ Données HTTP ]
```

---

#### Étape 5 — Couches 7-6-5 (Application)

**Action** : Remise des données à l'application. Le navigateur reçoit la réponse HTTP et affiche la page web.

```
GET / HTTP/1.1\r\nHost: example.com\r\n\r\n  →  traité par le navigateur
```

---

### 8. Vue d'ensemble — Décapsulation complète

```
RÉCEPTION (du bas vers le haut)

Couche 1   │  01101001 01010011 ... → reconstruction trame
           ▼
Couche 2   │  Vérifie FCS ✓ → Vérifie MAC ✓ → Lit EtherType → Retire header Eth + FCS
           │  Transmet : [ Header IP | Header TCP | Data HTTP ]
           ▼
Couche 3   │  Vérifie checksum IP ✓ → Vérifie IP dest ✓ → TTL-- → Lit Protocol → Retire header IP
           │  Transmet : [ Header TCP | Data HTTP ]
           ▼
Couche 4   │  Vérifie checksum TCP ✓ → Lit port dest → Gère séquence/ACK → Retire header TCP
           │  Transmet : [ Data HTTP ]
           ▼
Couche 7   │  Application reçoit les données pures
           │  → Navigateur affiche la page
```

**Pattern commun à chaque couche** : Vérifier l'intégrité → Vérifier que les données nous sont destinées → Lire les champs de contrôle → Retirer le header → Transmettre le payload à la couche du dessus.

---

### 9. MTU, MSS, fragmentation et overhead

#### MTU et MSS

**MTU (Maximum Transmission Unit)** : Taille maximale du **paquet IP** (header IP + payload IP) qu'un lien de couche 2 peut transporter. Sur Ethernet standard, le MTU = **1500 octets**.

Concrètement, ça veut dire que le paquet IP entier (header IP + payload IP) ne peut pas dépasser 1500 octets dans une trame Ethernet standard.

| Élément      | Taille          | Calcul                          |
| ------------ | --------------- | ------------------------------- |
| MTU Ethernet | 1500 octets     | Défini par le standard Ethernet |
| Header IP    | 20 octets       | Minimum IPv4                    |
| Header TCP   | 20 octets       | Minimum TCP                     |
| **MSS**      | **1460 octets** | 1500 - 20 - 20                  |

**MSS (Maximum Segment Size)** : Taille maximale du **payload TCP** (données applicatives pures) qui peut tenir dans un seul paquet sans fragmentation.

**Si les données dépassent le MSS** : Si une application veut envoyer plus de 1460 octets, TCP les découpe en plusieurs segments, chacun envoyé dans un paquet IP séparé, chacun dans une trame séparée.

**Exemple** : Un fichier HTML de 14 600 octets → 10 segments TCP de 1460 octets → 10 paquets IP → 10 trames Ethernet.

> **Avec un VPN** : les headers supplémentaires (IPsec, etc.) réduisent encore le MSS disponible. C'est pourquoi les connexions VPN ont souvent un MTU ajusté (ex: 1400 au lieu de 1500) pour éviter la fragmentation.

#### Jumbo Frames

Trames Ethernet surdimensionnées (jusqu'à **9000 octets** de MTU au lieu de 1500). Réduit l'overhead puisque le ratio header/payload est meilleur. Nécessite que **tout le matériel réseau sur le chemin** supporte les jumbo frames, sinon il y aura fragmentation ou rejet.

#### Overhead des headers

L'overhead désigne l'espace "consommé" par les headers par rapport aux données utiles transportées. Plus il y a de couches et de protocoles, plus l'overhead augmente.

**Connexion standard (HTTP sur TCP/IP sur Ethernet)** :

| Couche             | Header/Trailer | Taille                  |
| ------------------ | -------------- | ----------------------- |
| Ethernet           | Header + FCS   | 14 + 4 = 18 octets      |
| IP                 | Header IPv4    | 20 octets               |
| TCP                | Header TCP     | 20 octets               |
| **Total overhead** |                | **58 octets par trame** |

Pour un MSS de 1460 octets de données HTTP, on envoie réellement **1518 octets** sur le réseau → overhead de **~4%**.

**Connexion VPN (IPsec Tunnel Mode)** :

**Avec un VPN (IPsec Tunnel Mode)**, l'overhead augmente significativement car il y a un header IP externe + ESP + le paquet original complet → overhead de ~8-10%, ce qui explique la légère perte de débit.

| Couche                | Header/Trailer          | Taille                        |
| --------------------- | ----------------------- | ----------------------------- |
| Ethernet              | Header + FCS            | 18 octets                     |
| IP externe (tunnel)   | Header IPv4             | 20 octets                     |
| ESP (IPsec)           | Header + Trailer + Auth | ~40-60 octets                 |
| IP interne (original) | Header IPv4             | 20 octets                     |
| TCP                   | Header TCP              | 20 octets                     |
| **Total overhead**    |                         | **~120-140 octets par trame** |

L'overhead passe à **~8-10%**, ce qui explique pourquoi un VPN réduit légèrement le débit effectif. C'est aussi pourquoi les connexions VPN ajustent souvent le MTU (ex: 1400 au lieu de 1500) pour éviter la fragmentation.

**Comparaison Standard vs Jumbo Frames** :

| Élément | Standard | Jumbo |
|---------|----------|-------|
| MTU | 1500 | 9000 |
| MSS | 1460 | 8960 |
| Overhead | 58 octets (~4%) | 58 octets (~0.6%) |

L'overhead passe de 4% à 0.6% — même nombre de headers, mais beaucoup plus de données utiles par trame.

---

### 10. Encapsulation dans un contexte VPN (IPsec Tunnel Mode)

L'encapsulation VPN ajoute une **couche supplémentaire**. Le paquet IP original est chiffré en entier, puis encapsulé dans un nouveau paquet IP avec un header ESP.

```
SANS VPN :
[ Header Eth | Header IP | Header TCP | Données HTTP | FCS ]

AVEC VPN (IPsec Tunnel Mode) :
[ Header Eth | Header IP ext | ESP Header | Header IP orig | Header TCP | Données HTTP | ESP Trailer | FCS ]
                │                              │
                │                              └─ Tout ce bloc est CHIFFRÉ
                └─ IPs du tunnel VPN (client VPN ↔ serveur VPN)
```

Le paquet original (IP + TCP + Data) est chiffré et devient le **payload** du nouveau paquet IP. Les routeurs intermédiaires ne voient que les adresses IP du tunnel VPN — ils **ne peuvent pas lire** les IP originales, les ports, ni les données.

> **Lien avec le payload** : ici, le "payload" du paquet IP externe, c'est le paquet IP original chiffré en entier. Le principe est exactement le même que pour l'encapsulation normale — c'est juste une couche de plus.

---

## À retenir

**PDU & structure :**
✅ **PDU** = unité de données à chaque couche : Data (L7) → Segment/Datagramme (L4) → Paquet (L3) → Trame (L2) → Bits (L1)
✅ **PDU = Header + Payload** (+ Trailer parfois, comme Ethernet FCS)

**Headers :**
✅ **Header** = métadonnées de contrôle propres à chaque protocole (adressage, séquencement, contrôle d'erreur)
✅ **Tailles des headers courants** : Ethernet = 14 oct / IPv4 = 20 oct / TCP = 20 oct / UDP = 8 oct
✅ **Les ports** (src/dst) sont dans le header **TCP/UDP**, pas dans le header IP. Le header IP contient les **adresses IP** et le champ **Protocol**
✅ **Chaîne d'identification** : EtherType (L2) → Protocol (L3) → Port destination (L4) → chaque couche sait à qui remettre le payload

**Payload :**
✅ **Payload** = tout ce qui n'est pas le header ; c'est la PDU complète de la couche supérieure
✅ **Le payload d'une couche N = la PDU entière de la couche N+1** — principe des poupées russes
✅ Chaque couche ne lit que **son propre header** et traite le payload comme un bloc opaque → **indépendance des couches**

**Encapsulation & Décapsulation :**
✅ **Encapsulation** (envoi) : chaque couche ajoute son header autour des données de la couche supérieure → forme une nouvelle PDU
✅ **Décapsulation** (réception) : chaque couche vérifie, lit, et retire son header avant de transmettre le payload au-dessus
✅ **Pattern de décapsulation** : Vérifier intégrité → Vérifier destination → Lire champs contrôle → Retirer header → Transmettre au-dessus
✅ **MAC vs IP** : la MAC change à chaque saut (locale, saut par saut), l'IP reste la même de bout en bout (globale, end-to-end)

**Taille & performance :**
✅ **MTU Ethernet** = 1500 octets → **MSS TCP** = 1460 octets (1500 - 20 IP - 20 TCP)
✅ Si données > MSS → TCP découpe en plusieurs segments → plusieurs paquets IP → plusieurs trames
✅ **Overhead standard** = 58 octets (~4%) / **Overhead VPN** = ~120-140 octets (~8-10%)
✅ **Jumbo Frames** = MTU 9000 → overhead réduit à ~0.6%, nécessite support matériel sur tout le chemin
✅ **VPN (IPsec Tunnel Mode)** = couche d'encapsulation supplémentaire, paquet IP original chiffré encapsulé dans un nouveau paquet IP
