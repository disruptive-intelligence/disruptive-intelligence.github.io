---
title: À retenir
source: IT/04 Réseau/PDU, headers, payload & encapsulation.md
note: PDU, headers, payload & encapsulation
up:
- - PDU, headers, payload & encapsulation
  - index.md
---

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
