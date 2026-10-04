---
title: Chapitre 6 — Sous-réseaux, CIDR et VLSM
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie II — Adressage et acheminement
  - index.md
---

## 6.1 Compter les hôtes

Avec **n** bits hôte, un réseau contient 2ⁿ adresses, dont **2ⁿ − 2 hôtes utilisables** (on retire l'adresse réseau et le broadcast).

| CIDR | Masque | Bits hôte | Hôtes utilisables |
|---|---|---|---|
| /8 | 255.0.0.0 | 24 | 16 777 214 |
| /12 | 255.240.0.0 | 20 | 1 048 574 |
| /16 | 255.255.0.0 | 16 | 65 534 |
| /20 | 255.255.240.0 | 12 | 4 094 |
| /22 | 255.255.252.0 | 10 | 1 022 |
| /24 | 255.255.255.0 | 8 | 254 |
| /25 | 255.255.255.128 | 7 | 126 |
| /26 | 255.255.255.192 | 6 | 62 |
| /27 | 255.255.255.224 | 5 | 30 |
| /28 | 255.255.255.240 | 4 | 14 |
| /29 | 255.255.255.248 | 3 | 6 |
| /30 | 255.255.255.252 | 2 | 2 (liaison point à point entre deux routeurs) |
| /31 | 255.255.255.254 | 1 | 2 (RFC 3021, point à point) |
| /32 | 255.255.255.255 | 0 | 1 (un hôte seul) |

## 6.2 Trouver le réseau, le broadcast et la plage d'une adresse

La méthode rapide de l'**incrément** (*block size*) : repérer l'octet où le masque « coupe » (ni 255 ni 0), puis calculer **256 − valeur du masque dans cet octet**. Les réseaux commencent à chaque multiple de cet incrément.

**Exemple : 172.16.50.75/20**

1. Masque /20 = `255.255.240.0` → l'octet intéressant est le 3ᵉ (240).
2. Incrément = 256 − 240 = **16** → les réseaux commencent à 0, 16, 32, **48**, 64…
3. Le 3ᵉ octet de l'IP vaut 50 → il tombe dans le bloc **48-63**.

| Élément | Valeur |
|---|---|
| Adresse réseau | `172.16.48.0` |
| Première IP utilisable | `172.16.48.1` |
| Dernière IP utilisable | `172.16.63.254` |
| Broadcast | `172.16.63.255` |
| Hôtes utilisables | 2¹² − 2 = **4 094** |

**Mémo** de l'incrément dans le 3ᵉ octet : /17 → 128, /18 → 64, /19 → 32, /20 → 16, /21 → 8, /22 → 4, /23 → 2, /24 → 1. Même logique dans le 4ᵉ octet : /25 → 128, /26 → 64, /27 → 32, /28 → 16…

## 6.3 Découper un réseau en sous-réseaux

Pour obtenir **S** sous-réseaux, on emprunte **n** bits à la partie hôte, avec 2ⁿ ≥ S :

1. trouver le plus petit n tel que 2ⁿ ≥ S ;
2. nouveau masque = ancien masque + n ;
3. taille d'un sous-réseau = 2^(bits hôte restants) ; hôtes = taille − 2 ;
4. l'incrément est égal à la taille.

**Exemple : 192.168.1.0/24 en 4 sous-réseaux** → 2² = 4, donc n = 2 → **/26** (6 bits hôte, 64 adresses, 62 hôtes, incrément 64).

| Sous-réseau | Adresse réseau | Première IP | Dernière IP | Broadcast |
|---|---|---|---|---|
| 1 | 192.168.1.0/26 | .1 | .62 | .63 |
| 2 | 192.168.1.64/26 | .65 | .126 | .127 |
| 3 | 192.168.1.128/26 | .129 | .190 | .191 |
| 4 | 192.168.1.192/26 | .193 | .254 | .255 |

Les deux bits empruntés prennent les quatre valeurs `00`, `01`, `10`, `11` — d'où les quatre sous-réseaux :

```text
192.168.1.64 = 11000000.10101000.00000001.01000000
Masque /26   = 11111111.11111111.11111111.11000000
                                          ^^  bits empruntés = 01 → sous-réseau 2
```


**Le nombre exact n'existe pas toujours.** Pour 5, 6 ou 7 sous-réseaux, il faut n = 3 (2³ = 8) → /27 : on dispose de 8 sous-réseaux de 30 hôtes (.0, .32, .64, .96, .128, .160, .192, .224) et on en utilise une partie, le reste étant gardé pour plus tard.

**Exemple : 10.0.0.0/22 en 8 sous-réseaux.** Un /22 couvre 4 réseaux /24 (`10.0.0.x` à `10.0.3.x`, incrément 4 dans le 3ᵉ octet). Pour 8 sous-réseaux, n = 3 → **/25** (126 hôtes). Un /25 coupe chaque /24 en deux (.0 et .128) :

| Sous-réseau | Adresse réseau | Première IP | Dernière IP | Broadcast |
|---|---|---|---|---|
| 1 | 10.0.0.0/25 | 10.0.0.1 | 10.0.0.126 | 10.0.0.127 |
| 2 | 10.0.0.128/25 | 10.0.0.129 | 10.0.0.254 | 10.0.0.255 |
| 3 | 10.0.1.0/25 | 10.0.1.1 | 10.0.1.126 | 10.0.1.127 |
| 4 | 10.0.1.128/25 | 10.0.1.129 | 10.0.1.254 | 10.0.1.255 |
| 5 | 10.0.2.0/25 | 10.0.2.1 | 10.0.2.126 | 10.0.2.127 |
| 6 | 10.0.2.128/25 | 10.0.2.129 | 10.0.2.254 | 10.0.2.255 |
| 7 | 10.0.3.0/25 | 10.0.3.1 | 10.0.3.126 | 10.0.3.127 |
| 8 | 10.0.3.128/25 | 10.0.3.129 | 10.0.3.254 | 10.0.3.255 |

## 6.4 VLSM : des masques adaptés à chaque besoin

Le **VLSM** (*Variable Length Subnet Mask*) attribue à chaque sous-réseau le masque qui correspond à sa taille, au lieu d'un masque unique. On procède **du plus grand besoin au plus petit**, pour garder les blocs alignés.

**Exemple : 10.0.0.0/24 pour trois services de 100, 50 et 10 hôtes.**

| Service | Besoin | Bits hôte (2ⁿ − 2 ≥ besoin) | Masque | Réseau | Hôtes | Broadcast |
|---|---|---|---|---|---|---|
| A | 100 | 7 (126) | /25 | 10.0.0.0/25 | .1 – .126 | .127 |
| B | 50 | 6 (62) | /26 | 10.0.0.128/26 | .129 – .190 | .191 |
| C | 10 | 4 (14) | /28 | 10.0.0.192/28 | .193 – .206 | .207 |

Il reste `10.0.0.208` à `10.0.0.255` pour de futurs besoins.

## 6.5 Erreur classique : deux masques différents sur le même switch

Le poste du directeur (`192.168.1.200/25`) n'arrive pas à joindre le serveur de fichiers (`192.168.1.10/24`), pourtant branché sur le même switch.

- Le **serveur** (/24) considère que tout `192.168.1.1-254` est local : il répondrait directement.
- Le **directeur** (/25) coupe le réseau en deux (0-127 et 128-255) : il est dans la moitié haute et juge que `.10` est **hors de son réseau**. Il n'émet donc pas de requête ARP vers le serveur, mais envoie le trafic à sa passerelle — qui n'a peut-être pas de route adaptée.

> **À retenir.** Tous les hôtes d'un même segment doivent avoir le **même masque** ; un masque incohérent produit des pannes « inexplicables » et asymétriques.

---
