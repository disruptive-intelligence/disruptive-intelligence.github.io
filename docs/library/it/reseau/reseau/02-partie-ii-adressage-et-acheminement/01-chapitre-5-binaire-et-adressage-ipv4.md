---
title: Chapitre 5 — Binaire et adressage IPv4
source: IT/04 Réseau/Comprendre le réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie II — Adressage et acheminement
  - index.md
---

## 5.1 Une adresse IPv4

Une adresse IPv4 fait **32 bits**, écrits en quatre octets décimaux séparés par des points (`192.168.1.10`). Chaque octet vaut de 0 à 255. L'adresse est logique (attribuée selon la topologie, elle peut changer), à la différence de l'adresse MAC liée à la carte réseau.

![Adresse MAC (couche 2) et adresse IP (couche 3)](../../../../assets/reseau-addressing.png)

## 5.2 Convertir entre décimal et binaire

Chaque position d'un octet vaut une puissance de 2 :

```text
Position :   7    6    5    4    3    2    1    0
Valeur   : 128   64   32   16    8    4    2    1
```


**Décimal → binaire** : on retire la plus grande puissance possible, de gauche à droite.

| Octet | Calcul | Binaire |
|---|---|---|
| 192 | 128 + 64 | `11000000` |
| 168 | 128 + 32 + 8 | `10101000` |
| 10 | 8 + 2 | `00001010` |
| 255 | toutes les positions | `11111111` |

**Binaire → décimal** : on additionne les valeurs des bits à 1 (`10101000` = 128 + 32 + 8 = 168).

## 5.3 Le masque et le ET logique

Le **masque** sépare la partie **réseau** (bits à 1) de la partie **hôte** (bits à 0). La notation **CIDR** donne le nombre de bits réseau : `/24` = `255.255.255.0`.

```text
IP     : 11000000.10101000.00000001.00001010   (192.168.1.10)
Masque : 11111111.11111111.11111111.00000000   (/24)
         |←──────── réseau (24 bits) ────────→|← hôte (8) →|
```


L'**adresse réseau** s'obtient par un **ET logique** bit à bit entre l'IP et le masque (1 ET 1 = 1, sinon 0) :

```text
IP      : 192.168.1.10     = 11000000.10101000.00000001.00001010
Masque  : 255.255.255.0    = 11111111.11111111.11111111.00000000
──────────────────────────────────────────────────────────── ET
Réseau  : 192.168.1.0      = 11000000.10101000.00000001.00000000
```


```text
IP      : 172.16.50.75     = 10101100.00010000.00110010.01001011
Masque  : 255.255.240.0    = 11111111.11111111.11110000.00000000   (/20)
──────────────────────────────────────────────────────────── ET
Réseau  : 172.16.48.0      = 10101100.00010000.00110000.00000000
```


C'est exactement le calcul que fait un système pour savoir si une destination est **locale** (même résultat que le sien) ou s'il doit passer par la **passerelle** (Ch.8).

## 5.4 Adresses particulières

| Adresse | Rôle |
|---|---|
| **Adresse réseau** (bits hôte à 0, ex. `192.168.1.0/24`) | Désigne le réseau lui-même, non attribuable |
| **Broadcast** (bits hôte à 1, ex. `192.168.1.255`) | Tous les hôtes du réseau, non attribuable |
| `127.0.0.0/8` (surtout `127.0.0.1`) | **Loopback** : la machine elle-même (`::1` en IPv6) |
| `169.254.0.0/16` | **APIPA** : adresse auto-attribuée faute de serveur DHCP — signe d'un problème DHCP |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | **Adresses privées** (RFC 1918), non routées sur Internet (Ch.7) |
| `0.0.0.0/0` | Route par défaut (« toute destination ») |

> La passerelle **n'est pas** une adresse réservée : c'est une adresse d'hôte comme une autre, souvent la première (`.1`) ou la dernière (`.254`) par convention.

---
