---
title: Bases de données (courant en audit)
source: IT/04 Réseau/Réseau — prises de notes.md
note: Réseau — prises de notes
up:
- - Réseau — prises de notes
  - index.md
---

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 1433 | TCP | MS SQL | Base Microsoft | Connexion au service Microsoft SQL Server |
> | 3306 | TCP | MySQL/MariaDB | Base | Connexion au serveur MySQL/MariaDB |
> | 5432 | TCP | PostgreSQL | Base | Connexion au serveur PostgreSQL |
> | 27017 | TCP | MongoDB | Base NoSQL | Connexion au serveur MongoDB |
> | 6379 | TCP | Redis | Cache/DB | Connexion à Redis (cache, file d’attente, KV store) |

> ---

> ## 2) Ports “Windows / Active Directory” (indispensable en entreprise)

> Pour que ton cours soit réellement opérationnel (SOC/pentest), voici les ports AD les plus “structurants”.

> | Port | Proto | Service AD | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 88 | TCP/UDP | Kerberos | Auth AD | Authentification Kerberos (tickets) pour domaine AD |
> | 389 | TCP/UDP | LDAP | Annuaire | Accès à l’annuaire (requêtes utilisateurs, groupes, objets) |
> | 636 | TCP | LDAPS | LDAP sur TLS | LDAP chiffré via TLS |
> | 464 | TCP/UDP | kpasswd | Chgt mdp Kerberos | Changement/gestion mot de passe via Kerberos |
> | 135 | TCP | RPC Endpoint | RPC Windows | Point d’entrée RPC (services Windows, administration, DCOM) |
> | 137/138 | UDP | NetBIOS | Name service / datagram | Résolution de noms et datagrammes NetBIOS (legacy LAN) |
> | 3268 | TCP | Global Catalog | Recherche AD | Recherche multi-domaines via Global Catalog |
> | 3269 | TCP | GC sur TLS | Recherche AD chiffrée | Global Catalog chiffré via TLS |
> | 445 | TCP | SMB | Partages + auth | Partages et services Windows, très lié à l’écosystème AD |

> ---

> ## 3) Description rapide par familles (pour comprendre “à quoi sert le port”)


## Web (80/443/8080/8443)

### 80/8080

> HTTP “pur” (souvent interne ou historique).

### 443/8443

> HTTPS (HTTP dans un tunnel TLS), très fréquent pour apps, API et consoles web.


## Accès distant (22/3389/5985/5986/5900)

> - 22 : shell distant (SSH).

### 3389

> bureau distant Windows (RDP).

### 5985/5986

> administration distante Windows (WinRM).

### 5900

> prise en main distante (VNC).


## Partage (445/139/2049)

> - 445 : SMB (partages Windows).
> - 139 : couche legacy autour de SMB.

### 2049

> NFS (partages Unix/Linux).


## Infra réseau (53/67-68/123)

> - 53 : DNS (résolution de noms).

### 67/68

> DHCP (adressage).

> > - 123 : NTP (temps).

> > ---

> > ## 4) Ports éphémères : la règle qui évite les confusions

> > - **Client** : utilise en général un **port source éphémère** (haut numéro).
> > - **Serveur** : écoute sur un **port connu** (22, 443, 445, etc.).

### Donc dans les flux, tu verras souvent

> `client:491xx → serveur:443` (ou l’inverse en réponse).

### Les plages exactes peuvent varier selon OS/config, mais la logique reste la même.

> > [Tools [Wireshark, TCPDump…]](https://www.notion.so/Tools-Wireshark-TCPDump-2b83297e15978034aa00df40cd2aee42?pvs=21)

---
