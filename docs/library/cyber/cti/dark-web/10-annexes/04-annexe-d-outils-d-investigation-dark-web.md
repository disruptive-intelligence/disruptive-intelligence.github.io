---
title: Annexe D — Outils d'investigation dark web
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Annexes
  - index.md
---

## D.1 Environnements et navigateurs

| Outil | Usage | Coût |
|---|---|---|
| **Tor Browser** | Navigation .onion (référence) | Gratuit, open source |
| **Tails** | Distribution Linux live (USB) | Gratuit, open source |
| **Whonix** | Architecture VM Gateway+Workstation | Gratuit, open source |
| **Qubes OS** | OS isolation par VM | Gratuit, open source |
| **VirtualBox / VMware** | Hyperviseur pour VM jetables | Gratuit / payant |

## D.2 Capture et documentation

| Outil | Usage | Coût |
|---|---|---|
| **Hunchly** | Capture structurée d'investigation, horodatage | Commercial (~130 USD/an) |
| **OSINT Cloner** | Alternative open source | Gratuit |
| **wget / curl + torify** | Récupération CLI via Tor | Gratuit |
| **Aquatone** | Capture screenshot en masse | Gratuit, open source |
| **Eyewitness** | Reconnaissance web automatique | Gratuit, open source |
| **OnionScan** | Audit OPSEC de services .onion | Gratuit, open source |

## D.3 Plateformes commerciales CTI

| Plateforme | Force principale | Ordre de prix |
|---|---|---|
| **Recorded Future** | Vision globale, intégration extensive | 100k - 500k+ USD/an |
| **Flashpoint** | Russophone, Telegram | 100k - 300k USD/an |
| **Intel471** | Acteurs, cybercrime profondeur | 100k - 300k USD/an |
| **SOCRadar** | Rapport qualité/prix, PME-friendly | 30k - 100k USD/an |
| **Flare** | Niche dark web et data leaks | 30k - 100k USD/an |
| **DarkOwl** | Crawling .onion étendu | 50k - 200k USD/an |
| **Cybersixgill** (Zenity) | Profilage, attribution | 100k - 300k USD/an |
| **Hudson Rock** | Stealer logs spécialisé | 30k - 100k USD/an |
| **KELA** | Russophone fort | 100k - 300k USD/an |
| **Group-IB** | Vision Europe/Asie | 100k - 300k USD/an |

## D.4 OSINT et pivoting

| Outil | Usage |
|---|---|
| **Maltego** | Graphing relations entités |
| **SpiderFoot** | Reconnaissance automatisée |
| **Have I Been Pwned** | Vérification breaches publics |
| **DeHashed** | Recherche dans dumps publics |
| **LeakCheck, Snusbase** | Bases de breach |
| **IntelX** | Archives leaks et .onion |
| **GitHub dorking** | Secrets dans repos publics |
| **Reverse image search** | Google Images, TinEye, Yandex |
| **DomainTools, SecurityTrails, ViewDNS** | WHOIS, DNS history |
| **Shodan, Censys** | Recherche infrastructure exposée |

## D.5 Analyse blockchain

| Outil | Force |
|---|---|
| **Chainalysis** (Reactor, KYT) | Standard industrie, labellisation massive |
| **TRM Labs** (Forensics) | Compliance et investigation |
| **Elliptic** (Navigator) | Graphing et labellisation |
| **CipherTrace** | Mastercard subsidiary |
| **Crystal** | Bitfury subsidiary |
| **Breadcrumbs.app** | Open access partiel |
| **OXT.me** | Open Bitcoin analysis |
| **WalletExplorer** | Clustering basique |
| **Blockstream.info, Mempool.space** | Bitcoin explorers |
| **Etherscan, Tronscan** | Ethereum, TRON explorers |

## D.6 Threat intelligence platforms

| Plateforme | Usage |
|---|---|
| **MISP** | Plateforme open source de partage d'IoC |
| **OpenCTI** | Plateforme open source TI |
| **Anomali ThreatStream, ThreatConnect, EclecticIQ** | Commerciales |
| **Recorded Future, Flashpoint, etc.** | Plateformes commerciales (incluent TIP) |

## D.7 Surveillance leak sites

| Outil | Usage |
|---|---|
| **Ransomwatch** | Archive open source des leak sites |
| **Ransomfeed.it** | Agrégateur public |
| **SOCRadar Threat Hunting** | Commercial |
| **DarkOwl Vision** | Commercial |
| **Plateformes générales CTI** | Recorded Future, Flare, etc. |

## D.8 Outils analyse fichiers

| Outil | Usage |
|---|---|
| **exiftool** | Extraction métadonnées |
| **VirusTotal** | Scan multi-AV |
| **Hybrid Analysis, Joe Sandbox** | Sandboxing |
| **ANY.RUN** | Sandboxing interactif |
| **CyberChef** | Conversions, decoding |
| **Wireshark** | Analyse réseau |
| **Volatility** | Analyse mémoire |

## D.9 Communication chiffrée

| Outil | Usage |
|---|---|
| **GPG / GnuPG** | Signature et chiffrement PGP |
| **Pidgin + OTR** | XMPP avec chiffrement |
| **Signal, Wire** | Messagerie chiffrée pour équipe |
| **Element / Matrix** | Communication chiffrée fédérée |
| **OnionShare** | Partage de fichiers via Tor |

---
