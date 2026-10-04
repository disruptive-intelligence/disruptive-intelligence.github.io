---
title: Chapitre 7 — IPv6, adresses publiques et privées, NAT
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie II — Adressage et acheminement
  - index.md
---

## 7.1 IPv6

IPv6 a été créé pour faire face à l'épuisement des adresses IPv4.

| | IPv4 | IPv6 |
|---|---|---|
| Taille | 32 bits | 128 bits |
| Notation | Décimale pointée : `192.168.1.1` | 8 groupes hexadécimaux : `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (abrégeable en `2001:db8:85a3::8a2e:370:7334`) |
| Diffusion | Broadcast | Plus de broadcast : multicast |
| Fragmentation | Par les routeurs | Par l'émetteur seulement |
| Résolution locale | ARP | NDP (*Neighbor Discovery*, ICMPv6) |

| Type d'adresse IPv6 | Destinataire |
|---|---|
| **Unicast** | Une interface précise (un vers un) |
| **Multicast** | Un groupe d'interfaces (remplace le broadcast) |
| **Anycast** | Plusieurs interfaces possibles, la plus proche répond (répartition de charge, serveurs DNS racine) |

![Format d'une adresse IPv6](../../../../assets/reseau-addressing-2.png)

## 7.2 Adresses publiques et privées

- Une **adresse publique** est unique sur Internet, attribuée par le FAI : la machine est joignable de partout.
- Une **adresse privée** (RFC 1918 : `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) n'est valable que dans un réseau local et n'est pas routée sur Internet. Le même `192.168.1.10` existe dans des millions de foyers.

## 7.3 Le NAT

Le **NAT** (*Network Address Translation*) permet à des machines en adresses privées de sortir sur Internet derrière une ou plusieurs adresses publiques.

**Le fonctionnement**, sur une box domestique (LAN `192.168.1.1`, WAN `203.0.113.50`) :

```text
1. Le PC 192.168.1.10:5555 envoie une requête vers un site web.
2. Le routeur remplace la source par son IP publique : 203.0.113.50:4444,
   et note la correspondance dans sa table NAT (4444 ↔ 192.168.1.10:5555).
3. Le serveur répond à 203.0.113.50:4444.
4. Le routeur consulte sa table, remet la destination 192.168.1.10:5555
   et transmet la réponse au PC.
```


| Type | Principe | Usage |
|---|---|---|
| **NAT statique** | Une IP privée ↔ une IP publique fixe | Publier un serveur interne |
| **NAT dynamique** | IP publique prise dans un pool, à la demande | Peu courant aujourd'hui |
| **PAT** (*Port Address Translation*, « NAT overload ») | Toutes les IP privées partagent **une** IP publique, distinguées par le port | Le cas de toutes les box et de la plupart des entreprises |

> Le NAT n'est pas un pare-feu : il masque l'adressage interne et bloque de fait les connexions entrantes non sollicitées, mais il ne filtre ni n'inspecte rien.

---
