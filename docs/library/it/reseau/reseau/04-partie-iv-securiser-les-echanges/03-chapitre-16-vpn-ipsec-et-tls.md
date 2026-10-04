---
title: 'Chapitre 16 — VPN : IPsec et TLS'
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie IV — Sécuriser les échanges
  - index.md
---

## 16.1 Principe

Un **VPN** crée un tunnel chiffré à travers un réseau non sûr. En **accès distant** (*remote access*), le poste d'un utilisateur reçoit une adresse interne et accède aux ressources de l'entreprise comme s'il était sur place. En **site à site** (*site-to-site*), deux réseaux sont reliés en permanence par leurs passerelles.

| Composant | Rôle |
|---|---|
| Client VPN | Logiciel sur le poste (OpenVPN, AnyConnect, GlobalProtect, FortiClient…) |
| Passerelle / serveur VPN | Accepte les connexions et route le trafic vers le réseau interne |
| Chiffrement | Protège la confidentialité et l'intégrité dans le tunnel |
| Authentification | Les deux extrémités prouvent leur identité |

| Protocole | Port | Usage |
|---|---|---|
| IKE (IPsec) | UDP 500, UDP 4500 (NAT-T), ESP (protocole IP 50) | VPN IPsec |
| L2TP/IPsec | UDP 1701 (+ ports IPsec) | Ancien VPN d'accès distant |
| VPN SSL/TLS | TCP 443 (ou UDP 443 en DTLS) | OpenVPN, portails SSL |
| WireGuard | UDP 51820 (par défaut) | VPN moderne et léger |
| PPTP | TCP 1723 | Obsolète, à proscrire |

## 16.2 IPsec : protéger les paquets IP

IPsec travaille à la **couche 3** : il protège directement les paquets IP. Il s'appuie sur trois briques :

| Brique | Rôle |
|---|---|
| **IKE** (*Internet Key Exchange*, v2 de préférence) | Négocie les algorithmes, échange les clés (Diffie-Hellman), authentifie les pairs, crée les **SA** (*Security Associations*) |
| **ESP** (*Encapsulating Security Payload*) | Chiffre et authentifie — le protocole utilisé en pratique |
| **AH** (*Authentication Header*) | Authentifie et assure l'intégrité, sans chiffrer — rarement utilisé |

| Mode | Ce qui est protégé | Usage |
|---|---|---|
| **Transport** | La charge utile du paquet ; l'en-tête IP d'origine reste visible | Hôte à hôte |
| **Tunnel** | Le paquet IP entier, encapsulé dans un nouveau paquet IP | VPN site à site et accès distant |

**L'établissement d'un tunnel IPsec, pas à pas** (siège A `203.0.113.1`, réseau `10.1.0.0/24` ; agence B `198.51.100.1`, réseau `10.2.0.0/24`) :

1. **Déclenchement** — un paquet de `10.1.0.0/24` vers `10.2.0.0/24` correspond à une politique IPsec, ou le tunnel est maintenu en permanence.
2. **IKE phase 1** (UDP 500) — A propose des algorithmes (AES-256, SHA-256, groupe Diffie-Hellman), B choisit ; échange **Diffie-Hellman** pour calculer un secret partagé sans le transmettre ; **authentification mutuelle** par clé pré-partagée (PSK) ou par certificats. Résultat : un canal de gestion chiffré, l'**IKE SA**.
3. **IKE phase 2** — dans ce canal, négociation du tunnel de données : sous-réseaux à protéger (*traffic selectors*), ESP, algorithmes, durée de vie des clés, éventuellement un nouvel échange DH (*Perfect Forward Secrecy*). Résultat : une paire d'**IPsec SA**, une par sens, chacune identifiée par un **SPI**.
4. **NAT-T** — si un NAT est détecté entre les pairs, tout bascule sur UDP 4500 : ESP n'a pas de ports et le NAT ne saurait pas le traduire.
5. **Transport** — chaque paquet est chiffré en entier par ESP puis encapsulé dans un nouveau paquet IP entre les adresses publiques ; l'autre passerelle déchiffre et route en interne.
6. **Maintenance** — renouvellement automatique des clés (*rekeying*), détection d'un pair tombé (*Dead Peer Detection*).

```text
Paquet d'origine :
[IP 10.1.0.50 → 10.2.0.10] [TCP] [Données]

Après ESP en mode tunnel :
[IP 203.0.113.1 → 198.51.100.1] [ESP (SPI)] [████ IP d'origine + TCP + données, chiffrés ████] [ESP trailer + auth]
```


Les routeurs d'Internet ne voient que les adresses publiques et « protocole ESP ».

## 16.3 VPN TLS : un tunnel dans HTTPS

Le VPN SSL/TLS encapsule le trafic du client dans une session **TLS**, typiquement sur **TCP 443** — vu de l'extérieur, c'est du HTTPS ordinaire.

1. **Connexion** — le client résout `vpn.entreprise.com` et ouvre une connexion TCP 443 (ou UDP en DTLS).
2. **Handshake TLS** — comme pour un site web : versions, suites, **certificat serveur** vérifié, éventuellement **certificat client** (seuls les postes de l'entreprise passent), échange ECDHE.
3. **Authentification utilisateur**, dans le tunnel déjà chiffré — identifiant et mot de passe vérifiés contre l'annuaire (AD, LDAP, RADIUS), **MFA**, éventuellement **contrôle de posture** (antivirus, correctifs, chiffrement du disque).
4. **Configuration** — la passerelle attribue une IP interne (`10.0.100.50`), le client crée une **interface virtuelle** (`tun0`), la passerelle pousse les routes et les DNS internes.
5. **Transport** — un paquet vers `10.0.1.20` est capté par l'interface virtuelle, chiffré dans la session TLS et envoyé à la passerelle, qui le déchiffre et le route.

| Variante | Principe |
|---|---|
| **Split tunnel** | Seules les routes internes (`10.0.0.0/8`) passent dans le tunnel ; Internet sort en direct |
| **Full tunnel** | Tout le trafic (`0.0.0.0/0`) passe par l'entreprise, qui peut le filtrer |
| **Clientless (portail web)** | Rien à installer : l'utilisateur se connecte à un portail HTTPS qui sert de reverse proxy vers des applications précises — idéal pour un prestataire sur un poste non géré, sans accès réseau |
| **DTLS** | TLS sur UDP : évite le *TCP-over-TCP*, où une perte déclenche deux retransmissions concurrentes (celle du TCP applicatif et celle du TCP du tunnel) |

```text
Paquet d'origine :      [IP 10.0.100.50 → 10.0.1.20] [TCP 80] [HTTP…]
Dans le tunnel TLS :    [IP 82.x.x.x → 203.0.113.50] [TCP 443] [TLS record : ████ paquet d'origine chiffré ████]
```


## 16.4 IPsec ou TLS : comparer et choisir

| Critère | VPN IPsec | VPN SSL/TLS |
|---|---|---|
| Couche | Réseau (3) : protège les paquets IP | Au-dessus de TCP/UDP (4+) : encapsule le trafic dans TLS |
| Négociation | IKE en deux phases | Un handshake TLS |
| Flux réseau | UDP 500 + ESP (50) + UDP 4500 | Un seul flux TCP/UDP 443 |
| Traversée des pare-feu et NAT | Parfois bloqué (hôtels, Wi-Fi publics) | Passe presque partout |
| Interopérabilité | Standard RFC, multi-constructeurs | Liée au produit |
| Performance | Très bonne (accélération matérielle) | Bonne en DTLS ; TCP-over-TCP sinon |
| Authentification | PSK ou certificats en phase 1 (EAP en IKEv2) | Certificat pendant TLS, puis utilisateur + MFA |
| Accès sans client | Non | Oui (portail web) |
| Usage typique | **Site à site** | **Accès distant** |

**Logique de choix.** Site à site → IPsec, quasi systématiquement. Accès distant depuis des réseaux maîtrisés ou en mobilité (IKEv2 gère bien le passage Wi-Fi ↔ 4G) → IPsec possible. Accès distant depuis n'importe où → TLS, parce que le 443 passe partout. Besoin d'un accès sans logiciel → TLS (portail). Beaucoup d'entreprises utilisent les deux.

> **Réponse d'entretien.** « IPsec opère au niveau IP : il chiffre les paquets via ESP après une négociation IKE sur UDP 500, et utilise plusieurs flux (ESP, UDP 4500 en cas de NAT). C'est le standard du site à site, interopérable et performant. Le VPN TLS encapsule le trafic dans une session TLS sur TCP 443, comme du HTTPS : il passe partout et convient à l'accès distant, avec une authentification en deux temps, certificat puis utilisateur et MFA. »

## 16.5 Accès distant, site à site et VPN grand public

- **Accès distant** : le tunnel part du **poste** ; l'utilisateur lance son client (ou il démarre seul hors du réseau d'entreprise, *always-on*) et s'authentifie.
- **Site à site** : le tunnel part des **pare-feu** des deux sites ; l'employé de Paris qui joint un serveur de Marseille ne voit qu'une adresse interne qui répond.
- **VPN grand public** (NordVPN, ProtonVPN, Mullvad…) : techniquement de l'accès distant, mais la passerelle sert de point de sortie vers Internet. Le site visité voit l'adresse du serveur VPN. On ne devient pas invisible : on **déplace la confiance** du FAI vers le fournisseur VPN, dont la politique « no-log » est un engagement contractuel, pas une garantie technique.

---
