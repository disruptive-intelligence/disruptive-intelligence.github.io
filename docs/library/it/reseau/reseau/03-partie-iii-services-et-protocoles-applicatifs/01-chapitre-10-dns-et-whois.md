---
title: Chapitre 10 — DNS et WHOIS
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie III — Services et protocoles applicatifs
  - index.md
---

## 10.1 À quoi sert le DNS

Le **DNS** (*Domain Name System*) est l'annuaire d'Internet : il traduit un nom (`www.example.com`) en adresse IP. Sans lui, il faudrait retenir l'adresse de chaque site. Il fonctionne sur le **port 53**, en UDP pour les requêtes courantes et en TCP pour les réponses volumineuses et les transferts de zone.

## 10.2 La hiérarchie

Le DNS est un arbre, lu de droite à gauche :

| Niveau | Exemple | Rôle |
|---|---|---|
| **Racine** (`.`) | 13 adresses de serveurs racine, gérées sous l'égide de l'ICANN, servies en **anycast** par des centaines de machines | Indique les serveurs de chaque TLD |
| **TLD** (*Top-Level Domain*) | `.com`, `.org`, `.fr`, `.uk` | Indique les serveurs faisant autorité de chaque domaine |
| **Domaine de second niveau** | `example.com` | Géré par son propriétaire |
| **Sous-domaine / nom d'hôte** | `www.example.com`, `admin.example.com` | Enregistrements dans la zone du domaine |

## 10.3 La résolution pas à pas

```text
1. Cache local du système, puis fichier hosts (/etc/hosts, C:\Windows\System32\drivers\etc\hosts)
2. Requête au résolveur récursif configuré (box, FAI, DNS d'entreprise, 1.1.1.1…) — il a lui aussi un cache
3. Sans réponse en cache, le résolveur interroge un serveur RACINE  → « voyez les serveurs de .com »
4. … puis un serveur du TLD .com                                   → « voyez ns1.example.com »
5. … puis le serveur FAISANT AUTORITÉ du domaine                  → « www.example.com = 93.184.216.34 »
6. Le résolveur met la réponse en cache (durée = TTL de l'enregistrement) et la renvoie au client
```


Sous Linux, les serveurs DNS utilisés sont dans `/etc/resolv.conf`. Un domaine a plusieurs serveurs de noms pour la redondance.

> Une réponse DNS n'est pas authentifiée par défaut : une machine du réseau local qui répond avant le vrai serveur peut rediriger la victime (empoisonnement, *spoofing*). DNSSEC signe les enregistrements ; DoH et DoT chiffrent le transport.

## 10.4 Les enregistrements

| Type | Contenu | Exemple |
|---|---|---|
| **A** | Adresse IPv4 | `www → 93.184.216.34` |
| **AAAA** | Adresse IPv6 | `www → 2606:2800:220:1::248` |
| **CNAME** | Alias vers un autre nom | `store.example.com → shop.shopify.com` |
| **MX** | Serveurs de messagerie du domaine (avec priorité) | `example.com → 10 mail.example.com` |
| **TXT** | Texte libre : SPF, DKIM, DMARC, vérifications de propriété | `v=spf1 include:_spf.google.com -all` |
| **NS** | Serveurs faisant autorité pour la zone | `example.com → ns1.example.com` |
| **PTR** | Résolution inverse : IP → nom | `34.216.184.93.in-addr.arpa → www.example.com` |
| **SRV** | Localisation d'un service (protocole, port) | `_ldap._tcp.dc._msdcs.meridian.local` (contrôleurs de domaine AD) |
| **SOA** | Paramètres de la zone (serveur primaire, numéro de série, durées) | — |

## 10.5 WHOIS et RDAP

**WHOIS** — aujourd'hui souvent via **RDAP**, son successeur structuré — donne les informations d'enregistrement d'un domaine ou d'une plage d'adresses : registrar, dates de création et d'expiration, serveurs de noms, parfois les contacts (souvent masqués). C'est une source de base en OSINT et en analyse d'un domaine suspect (un domaine créé il y a trois jours qui imite une banque…).

---
