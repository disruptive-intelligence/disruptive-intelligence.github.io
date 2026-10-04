---
title: Annexes
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - index.md
---

---


## Annexe A — Ports à connaître

**Web et proxys**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 80 | TCP | HTTP | Web non chiffré (souvent redirigé vers 443) |
| 443 | TCP (UDP en HTTP/3) | HTTPS | Web chiffré, API, VPN TLS |
| 8080 / 8443 | TCP | HTTP / HTTPS alternatifs | Applications internes, consoles d'administration |
| 3128 | TCP | Proxy (Squid) | Proxy web explicite |
| 1080 | TCP | SOCKS | Proxy générique |

**Accès distant et administration**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 22 | TCP | SSH / SFTP | Shell distant chiffré, transfert de fichiers |
| 23 | TCP | Telnet | Shell distant **en clair** (à proscrire) |
| 3389 | TCP/UDP | RDP | Bureau à distance Windows |
| 5985 / 5986 | TCP | WinRM HTTP / HTTPS | Administration Windows (PowerShell Remoting) |
| 5900 | TCP | VNC | Prise en main d'écran |
| 69 | UDP | TFTP | Transfert minimal (équipements réseau, démarrage PXE) |

**Fichiers et impression**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 20 / 21 | TCP | FTP | Données / commandes |
| 990 | TCP | FTPS | FTP sur TLS |
| 445 | TCP | SMB | Partages Windows, authentification |
| 139 | TCP | NetBIOS Session | SMB historique |
| 2049 | TCP/UDP | NFS | Partages Unix/Linux |
| 631 | TCP | IPP | Impression |

**Infrastructure**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 53 | UDP/TCP | DNS | Résolution de noms |
| 67 / 68 | UDP | DHCP | Serveur / client |
| 123 | UDP | NTP | Synchronisation de l'heure (indispensable à Kerberos et aux journaux) |
| 161 / 162 | UDP | SNMP | Supervision / alertes (traps) |
| 514 | UDP | Syslog | Journaux |
| 6514 | TCP | Syslog TLS | Journaux chiffrés |

**Messagerie**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 25 | TCP | SMTP | Relais entre serveurs |
| 587 | TCP | Submission | Envoi depuis un client (authentifié, STARTTLS) |
| 465 | TCP | SMTPS | SMTP sur TLS implicite |
| 110 / 995 | TCP | POP3 / POP3S | Réception |
| 143 / 993 | TCP | IMAP / IMAPS | Réception synchronisée |

**Windows et Active Directory**

| Port | Protocole | Service | Usage |
|---|---|---|---|
| 88 | TCP/UDP | Kerberos | Authentification |
| 135 | TCP | RPC Endpoint Mapper | Services RPC, DCOM, WMI |
| 137 / 138 | UDP | NetBIOS | Noms et datagrammes (historique) |
| 389 / 636 | TCP/UDP | LDAP / LDAPS | Annuaire |
| 464 | TCP/UDP | kpasswd | Changement de mot de passe Kerberos |
| 3268 / 3269 | TCP | Global Catalog | Recherches dans la forêt |
| 49152-65535 | TCP | RPC dynamiques | Réplication, administration |

**Bases de données**

| Port | Service |
|---|---|
| 1433 | Microsoft SQL Server |
| 3306 | MySQL / MariaDB |
| 5432 | PostgreSQL |
| 1521 | Oracle |
| 27017 | MongoDB |
| 6379 | Redis |

**VPN**

| Port | Service |
|---|---|
| UDP 500 / 4500, ESP (protocole 50) | IPsec (IKE, NAT-T) |
| UDP 1194 | OpenVPN (par défaut) |
| UDP 51820 | WireGuard |
| TCP 1723 | PPTP (obsolète) |

> **Ports éphémères.** Le client utilise un port source élevé choisi par son système (49152-65535 sous Windows, 32768-60999 par défaut sous Linux) ; le serveur écoute sur un port connu. Dans un flux : `client:49xxx → serveur:443`.

---


## Annexe B — Glossaire

| Terme | Définition |
|---|---|
| **ARP** | Résolution d'une adresse IP en adresse MAC sur le réseau local |
| **Broadcast** | Diffusion à tous les hôtes d'un réseau |
| **CIDR** | Notation du masque par le nombre de bits réseau (`/24`) |
| **DHCP** | Attribution automatique de la configuration IP (DORA) |
| **DNS** | Traduction des noms en adresses IP |
| **Encapsulation** | Ajout successif des en-têtes de chaque couche |
| **ESP** | Protocole IPsec qui chiffre et authentifie |
| **Full / half-duplex** | Communication simultanée dans les deux sens / à tour de rôle |
| **ICMP** | Messages d'erreur et de diagnostic (ping, traceroute) |
| **IKE** | Négociation des clés et des SA d'IPsec |
| **MAC** | Adresse physique de 48 bits d'une interface |
| **MSS** | Taille maximale des données d'un segment TCP |
| **MTU** | Taille maximale d'un paquet sur un lien (1 500 octets en Ethernet) |
| **NAT / PAT** | Traduction d'adresses privées en adresse(s) publique(s), par port pour le PAT |
| **NGFW** | Pare-feu de nouvelle génération (stateful + DPI + IPS + contrôle applicatif) |
| **PDU** | Unité de données d'une couche : données, segment, paquet, trame, bits |
| **Port** | Numéro sur 16 bits qui identifie une application |
| **Socket** | Couple adresse IP : port |
| **SSID** | Nom d'un réseau Wi-Fi |
| **TLS** | Protocole qui chiffre et authentifie une connexion (HTTPS) |
| **TTL** | Nombre de sauts restants avant destruction d'un paquet |
| **VLAN** | Réseau local virtuel, segmentation logique |
| **VLSM** | Masques de sous-réseau de tailles différentes selon les besoins |
| **VPN** | Tunnel chiffré entre un poste ou un site et un réseau distant |

---

---
