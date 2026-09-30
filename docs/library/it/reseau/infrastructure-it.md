---
title: Infrastructure IT
source: IT/03_Networking/Infrastructure_IT.md
---

*Comprendre ce qu'on attaque et ce qu'on défend*

**Cours complet — 31 chapitres • 7 parties • 7 annexes**

*Réseau • Systèmes • Cloud • Identité • Données • Virtualisation • Hardening*

---

### Table des matières

- [Fil rouge : Opération BACKBONE](#fil-rouge-operation-backbone)
- **PARTIE I — RÉSEAU, PROTOCOLES ET SERVICES FONDAMENTAUX (Ch.1-6)**
  - [Ch.1 — Modèle client-serveur, TCP/IP et protocoles fondamentaux](#chapitre-1-modele-client-serveur-tcpip-et-protocoles-fondamentaux)
  - [Ch.2 — Architecture réseau d'entreprise](#chapitre-2-architecture-reseau-dentreprise)
  - [Ch.3 — Sécurité réseau : firewalls, segmentation et détection](#chapitre-3-securite-reseau-firewalls-segmentation-et-detection)
  - [Ch.4 — Sécurité du Wi-Fi et des accès distants](#chapitre-4-securite-du-wi-fi-et-des-acces-distants)
  - [Ch.5 — Bastion, PAM et Zero Trust](#chapitre-5-bastion-pam-et-zero-trust)
  - [Ch.6 — Services d'infrastructure vitaux : DHCP, NTP, PKI et synchronisation](#chapitre-6-services-dinfrastructure-vitaux-dhcp-ntp-pki-et-synchronisation)
- **PARTIE II — SYSTÈMES, VIRTUALISATION ET HARDENING (Ch.7-11)**
  - [Ch.7 — Systèmes d'exploitation : Windows et Linux vue infrastructure](#chapitre-7-systemes-dexploitation-windows-et-linux-vue-infrastructure)
  - [Ch.8 — Virtualisation : hyperviseurs, réseaux virtuels et sécurité](#chapitre-8-virtualisation-hyperviseurs-reseaux-virtuels-et-securite)
  - [Ch.9 — Hardening : durcir les systèmes et les services](#chapitre-9-hardening-durcir-les-systemes-et-les-services)
  - [Ch.10 — Cryptographie : les fondamentaux pour l'infrastructure](#chapitre-10-cryptographie-les-fondamentaux-pour-linfrastructure)
  - [Ch.11 — Gestion des vulnérabilités et patching](#chapitre-11-gestion-des-vulnerabilites-et-patching)
- **PARTIE III — DONNÉES, STOCKAGE, MESSAGERIE ET TRANSFERTS (Ch.12-16)**
  - [Ch.12 — Bases de données relationnelles (SQL)](#chapitre-12-bases-de-donnees-relationnelles-sql)
  - [Ch.13 — Bases de données NoSQL](#chapitre-13-bases-de-donnees-nosql)
  - [Ch.14 — Stockage, sauvegardes et résilience technique](#chapitre-14-stockage-sauvegardes-et-resilience-technique)
  - [Ch.15 — Messagerie : SMTP, sécurité email et anti-phishing](#chapitre-15-messagerie-smtp-securite-email-et-anti-phishing)
  - [Ch.16 — Partage de fichiers et transfert de données](#chapitre-16-partage-de-fichiers-et-transfert-de-donnees)
- **PARTIE IV — APPLICATIONS, WEB ET APIs (Ch.17-19)**
  - [Ch.17 — Serveurs web, reverse proxy, WAF et CDN](#chapitre-17-serveurs-web-reverse-proxy-waf-et-cdn)
  - [Ch.18 — Architecture web et vulnérabilités : la vue d'ensemble](#chapitre-18-architecture-web-et-vulnerabilites-la-vue-densemble)
  - [Ch.19 — APIs : REST, GraphQL et sécurité](#chapitre-19-apis-rest-graphql-et-securite)
- **PARTIE V — IDENTITÉ ET AUTHENTIFICATION (Ch.20-24)**
  - [Ch.20 — LDAP et annuaires](#chapitre-20-ldap-et-annuaires)
  - [Ch.21 — Active Directory comme socle d'infrastructure](#chapitre-21-active-directory-comme-socle-dinfrastructure)
  - [Ch.22 — Authentification moderne : SSO, OAuth, SAML, OIDC](#chapitre-22-authentification-moderne-sso-oauth-saml-oidc)
  - [Ch.23 — IAM cloud : Azure AD/Entra ID, AWS IAM, GCP IAM](#chapitre-23-iam-cloud-azure-adentra-id-aws-iam-gcp-iam)
  - [Ch.24 — MFA, gestion des mots de passe et facteurs d'authentification](#chapitre-24-mfa-gestion-des-mots-de-passe-et-facteurs-dauthentification)
- **PARTIE VI — CLOUD, CONTAINERS ET ARCHITECTURES MODERNES (Ch.25-28)**
  - [Ch.25 — Cloud : modèles, architecture et responsabilité partagée](#chapitre-25-cloud-modeles-architecture-et-responsabilite-partagee)
  - [Ch.26 — Sécurité cloud : services natifs et bonnes pratiques](#chapitre-26-securite-cloud-services-natifs-et-bonnes-pratiques)
  - [Ch.27 — Containers : Docker, Kubernetes et sécurité](#chapitre-27-containers-docker-kubernetes-et-securite)
  - [Ch.28 — Architectures modernes : microservices, serverless et CI/CD](#chapitre-28-architectures-modernes-microservices-serverless-et-cicd)
- **PARTIE VII — OPÉRATIONS, MONITORING ET CAS DE SYNTHÈSE (Ch.29-31)**
  - [Ch.29 — Supervision, monitoring et automatisation](#chapitre-29-supervision-monitoring-et-automatisation)
  - [Ch.30 — Cas complet : audit d'infrastructure et plan de hardening](#chapitre-30-cas-complet-audit-dinfrastructure-et-plan-de-hardening)
  - [Ch.31 — Cas complet : investigation d'un incident sur une infrastructure hybride](#chapitre-31-cas-complet-investigation-dun-incident-sur-une-infrastructure-hybride)
- **ANNEXES**

---

### Fil rouge : Opération BACKBONE

> **Contexte narratif — ce fil rouge traverse les 29 premiers chapitres et se conclut aux Ch.30-31.**
>
> **Lucas Moreira**, ingénieur sécurité chez **Stratosphere** (MSSP, 80 personnes), est mandaté pour l'audit d'infrastructure et le hardening du SI de **CargoPlex** — entreprise de logistique européenne, 2 500 collaborateurs, 8 entrepôts connectés, SI hybride (datacenter on-premise Lyon sur VMware vSphere + Azure + 3 SaaS critiques), ERP SAP, WMS (Warehouse Management System) connecté aux automates d'entrepôt, 150 sous-traitants transporteurs avec accès VPN, classée entité importante NIS 2.
>
> L'infrastructure de CargoPlex s'est construite par couches sur 15 ans :
>
> **Couche legacy :** Windows Server 2012 R2 toujours en production, SQL Server sur la même VM que l'ERP, flat network sans segmentation, vCenter avec mot de passe par défaut accessible depuis le réseau utilisateur, LDAP anonymous bind actif, NTP avec 3 sources différentes et 7 minutes d'écart entre les serveurs, interfaces iLO des serveurs physiques accessibles depuis le LAN utilisateur avec credentials par défaut, NAS de sauvegarde joint au domaine AD.
>
> **Couche de modernisation partielle :** migration Azure commencée mais non terminée (hybrid AD via Entra Connect, Exchange Online, quelques VMs Azure), AD Connect sur un serveur non durci.
>
> **Couche récente non maîtrisée :** 3 SaaS souscrits par les métiers sans validation IT, API transporteurs en HTTP sans authentification forte avec documentation Swagger exposée publiquement, containers Docker en développement sans registry privé, pipeline GitLab CI avec secrets en clair.
>
> Lucas doit cartographier l'infrastructure, identifier les vulnérabilités architecturales, prioriser le hardening, et construire la baseline de sécurité.

---

### PARTIE I — RÉSEAU, PROTOCOLES ET SERVICES FONDAMENTAUX

*Le réseau est le terrain de jeu — comprendre les protocoles, l'architecture et les mécanismes de filtrage est un prérequis pour tout ce qui suit.*

---

#### Chapitre 1 — Modèle client-serveur, TCP/IP et protocoles fondamentaux

##### 1.1 Le modèle client-serveur

Presque toute l'informatique d'entreprise repose sur un principe simple : un client demande, un serveur répond. Le navigateur web (client) envoie une requête HTTP au serveur web. L'application mobile (client) appelle une API (serveur). Le poste de travail (client) demande un ticket Kerberos au contrôleur de domaine (serveur). En investigation, on cherche toujours « qui a demandé quoi à qui ». En pentest, on cherche à envoyer des requêtes malformées pour obtenir une réponse inattendue.

##### 1.2 TCP/IP

Tous les échanges réseau passent par la pile TCP/IP. **IP** (Internet Protocol) assure l'adressage des machines — IPv4 (192.168.1.10), IPv6 (2001:db8::1). **TCP** (Transmission Control Protocol) assure un transport fiable avec connexion en 3 étapes (SYN, SYN-ACK, ACK), garantit l'arrivée et l'ordre des données — utilisé par HTTP, SSH, SMTP, SQL. **UDP** (User Datagram Protocol) assure un transport rapide sans garantie — utilisé par DNS, SNMP, syslog, streaming. Les **ports** (0-65535) identifient le service sur une machine : HTTP=80, HTTPS=443, SSH=22, DNS=53, SMTP=25. Règle : un service qui écoute sur un port = une surface d'attaque. Moins de ports ouverts = moins de risque.

##### 1.3 HTTP/HTTPS

HTTP est le protocole du web. Chaque requête a une méthode (GET — récupérer, POST — créer/envoyer, PUT — remplacer, DELETE — supprimer, PATCH — modifier partiellement, OPTIONS — lister les méthodes autorisées), un chemin, des headers, et éventuellement un body. Les codes de retour essentiels en sécurité : 200 OK, 301/302 redirection (open redirect → phishing), 401 Unauthorized (pas authentifié), 403 Forbidden (authentifié mais pas autorisé), 404 Not Found, 500 Internal Server Error (peut révéler des infos en mode debug).

**Cookies et sessions :** HTTP est stateless — chaque requête est indépendante. Pour « se souvenir » de l'utilisateur, le serveur envoie un cookie (Set-Cookie: session_id=abc123) que le navigateur renvoie à chaque requête. Ce cookie est la clé de la session — le voler (XSS) revient à voler l'identité de l'utilisateur.

##### 1.4 TLS

HTTPS = HTTP + TLS. TLS chiffre le trafic entre le client et le serveur. Le serveur prouve son identité avec un **certificat** signé par une autorité de certification (CA). Le navigateur vérifie la chaîne de confiance. Ce que TLS fait : chiffrer en transit, authentifier le serveur. Ce que TLS ne fait PAS : protéger les données sur le serveur, authentifier l'utilisateur, empêcher les vulnérabilités applicatives.

##### 1.5 DNS en profondeur

Le DNS traduit les noms de domaine en adresses IP — c'est l'annuaire d'Internet. Les types d'enregistrement : **A/AAAA** (nom → IP), **CNAME** (alias), **MX** (serveur mail), **TXT** (métadonnées — SPF, DKIM, DMARC, vérification de propriété), **CAA** (quelles CA peuvent émettre des certificats), **NS** (serveurs DNS autoritaires), **PTR** (reverse DNS, IP → nom).

Le TXT est le couteau suisse du DNS : SPF (qui peut envoyer des mails pour ce domaine), DKIM (signature cryptographique des mails), DMARC (politique anti-spoofing), vérification de propriété (Google, Microsoft, Let's Encrypt).

Par défaut, les requêtes DNS sont en clair — un attaquant sur le réseau voit tous les domaines visités. DNS-over-HTTPS (DoH) et DNS-over-TLS (DoT) chiffrent les requêtes. Le DNS est aussi utilisé pour l'exfiltration de données (DNS tunneling — données encodées dans les sous-domaines) et comme canal C2 par les APT (cf. cours APT Ch.3).

##### 1.6 Fil rouge — BACKBONE : la cartographie protocolaire

> **🔧 BACKBONE — Épisode 1**
>
> Lucas lance un scan Nmap sur les plages IP de CargoPlex. Résultat : 47 services écoutent sur Internet (dont FTP 21 en clair, un vCenter 443 accessible, un Elasticsearch 9200 sans authentification, et 3 interfaces iLO/iDRAC en HTTPS avec credentials par défaut). 12 de ces services ne sont pas nécessaires et sont des surfaces d'attaque gratuites.

---

#### Chapitre 2 — Architecture réseau d'entreprise

##### 2.1 Les zones réseau

L'architecture réseau d'entreprise est structurée en zones de confiance décroissante. La **DMZ** (Demilitarized Zone) est la zone tampon entre Internet et le réseau interne — elle héberge les services exposés (reverse proxy, bastion, VPN gateway, serveurs web publics). Le **LAN** (Local Area Network) héberge les serveurs applicatifs, les bases de données, l'Active Directory, le SIEM — jamais exposés directement à Internet. La **zone d'administration** est un réseau isolé réservé aux outils d'administration (bastion, supervision, SIEM). La **zone OT/IoT** héberge les systèmes industriels (automates, SCADA) — si elle existe, elle doit être physiquement ou logiquement séparée du LAN IT.

##### 2.2 Les équipements réseau

Le **switch** connecte les machines dans un même réseau (couche 2) — pertinence sécurité : VLANs, port security, 802.1X. Le **routeur** connecte des réseaux différents (couche 3) — ACLs, filtrage inter-zones. Le **firewall** filtre le trafic selon des règles — point central de sécurité réseau. Le **load balancer** répartit la charge entre serveurs — TLS termination, health checks. Le **reverse proxy** est l'intermédiaire entre clients et serveurs — cache les serveurs internes. Le **WAF** filtre les requêtes HTTP malveillantes. L'**IDS/IPS** détecte et bloque les intrusions.

##### 2.3 Le management plane — le réseau d'administration

*Le management plane est la couche d'administration de l'infrastructure — souvent oubliée, toujours critique.*

Chaque équipement d'infrastructure (serveurs physiques, switches, firewalls, hyperviseurs, contrôleurs de stockage) possède une interface d'administration qui fonctionne indépendamment du système d'exploitation principal. Les **iLO** (HP), **iDRAC** (Dell), et **IPMI** (standard générique) sont des contrôleurs d'administration embarqués sur les serveurs physiques — ils permettent d'allumer/éteindre le serveur, d'accéder à la console, de monter des ISO, et de modifier la configuration matérielle, même si l'OS est éteint ou crashé. Les interfaces web d'administration des switches, firewalls et hyperviseurs (vCenter) offrent un contrôle total sur l'équipement.

Le risque est majeur : si ces interfaces sont accessibles depuis le réseau utilisateur (ce qui est le cas dans beaucoup d'organisations), un attaquant qui compromet un poste utilisateur peut accéder à l'administration de toute l'infrastructure physique. Les credentials par défaut (admin/admin sur iLO, root/calvin sur iDRAC) sont rarement changés. Les CVE sur ces interfaces sont régulièrement exploitées.

La solution : un **réseau de management dédié** (management VLAN ou réseau physiquement séparé), accessible uniquement depuis le bastion d'administration. Les interfaces iLO/iDRAC/IPMI, les consoles vCenter, les interfaces d'administration des switches et firewalls ne doivent JAMAIS être accessibles depuis le réseau utilisateur.

##### 2.4 L'architecture type

Le schéma type : Internet → firewall externe (+ WAF) → DMZ (reverse proxy, bastion, VPN gateway) → firewall interne → LAN (serveurs applicatifs, bases de données, AD, SIEM, mail) → postes de travail. Le réseau de management est parallèle au LAN, accessible uniquement via le bastion.

NAT (Network Address Translation) traduit les adresses IP privées en publiques — permet à plusieurs machines de partager une seule IP publique. VPN (tunnel chiffré — IPSec pour le site-to-site, OpenVPN/WireGuard pour le remote access). Proxy forward (intermédiaire pour les requêtes sortantes — filtrage URL, logging, cache).

##### 2.5 Fil rouge — BACKBONE : le réseau CargoPlex

> **🔧 BACKBONE — Épisode 2**
>
> Lucas dessine le schéma réseau de CargoPlex : un seul firewall Fortinet entre Internet et le LAN, pas de DMZ formalisée, flat network — tous les VLANs communiquent entre eux sans restriction. Le vCenter est accessible depuis les postes utilisateurs. Les interfaces iLO des 12 serveurs physiques sont sur le même réseau avec les credentials par défaut HP (admin/admin). Le NAS de sauvegarde est dans le même VLAN que les postes. En cas de compromission d'un poste utilisateur, l'attaquant peut atteindre directement l'administration de l'infrastructure physique, le vCenter, les sauvegardes, et l'AD.

---

#### Chapitre 3 — Sécurité réseau : firewalls, segmentation et détection

Les **firewalls** en profondeur : le firewall **stateless** filtre chaque paquet indépendamment (ACL basique sur IP/port — rapide mais limité), le firewall **stateful** suit les connexions (autorise les réponses aux requêtes initiées de l'intérieur), et le **NGFW** (Next-Generation Firewall) ajoute l'inspection applicative (filtrage URL, IPS intégré, inspection TLS, sandboxing — Palo Alto, Fortinet, Check Point). Politique de filtrage : **deny by default** — tout ce qui n'est pas explicitement autorisé est bloqué. Les règles de firewall (ordre — les règles sont évaluées séquentiellement, la première qui match s'applique ; logging — chaque règle de deny doit logger ; revue périodique — les règles obsolètes s'accumulent et créent des trous).

La **segmentation réseau** est le contrôle de sécurité le plus fondamental contre le mouvement latéral. VLANs (séparation logique au niveau 2 — utilisateurs, serveurs, admin, OT, guest, chaque VLAN dans son sous-réseau), sous-réseaux (séparation au niveau 3 avec filtrage inter-sous-réseaux par le firewall), et micro-segmentation (filtrage au niveau de chaque workload — NSG en cloud, Network Policies en Kubernetes). Pourquoi le flat network est un cadeau pour l'attaquant : sans segmentation, un ransomware ou un attaquant qui compromet un poste utilisateur peut atteindre directement le DC, le vCenter, les sauvegardes, et l'OT — tout le blast radius est maximal.

Les **IDS/IPS** (Intrusion Detection/Prevention System) : network-based (Snort, Suricata — analyse du trafic réseau) et host-based (OSSEC, Wazuh — analyse des logs et de l'intégrité). Détection par signatures (patterns connus — rapide mais aveugle aux attaques nouvelles) vs par anomalies (baseline comportementale — détecte l'inconnu mais génère des faux positifs). Le **NDR** (Network Detection and Response) analyse le trafic réseau de manière comportementale — détection de beaconing C2, mouvement latéral, exfiltration. Le **802.1X** (NAC — Network Access Control) authentifie les postes avant de leur accorder l'accès réseau — un poste non connu est placé dans un VLAN de quarantaine.

---

#### Chapitre 4 — Sécurité du Wi-Fi et des accès distants

**Wi-Fi :** WPA2-Personal (clé partagée — acceptable pour le domicile, pas pour l'entreprise), WPA2-Enterprise (802.1X/RADIUS — chaque utilisateur s'authentifie avec ses credentials AD, le seul mode acceptable en entreprise), WPA3 (SAE — résistant au brute force offline, adoption en cours). Les attaques (rogue AP — faux point d'accès, evil twin — copie du SSID légitime pour capturer les credentials). La segmentation du Wi-Fi guest (réseau isolé sans accès au LAN, uniquement Internet).

**Accès distants :** le VPN (split tunneling — seul le trafic vers l'entreprise passe par le VPN vs full tunneling — tout le trafic passe par le VPN, plus sécurisé ; MFA obligatoire sur le VPN ; le VPN comme surface d'attaque APT majeure — Ivanti, Fortinet, Pulse Secure exploités systématiquement — cf. cours APT Ch.3). Le RDP (Remote Desktop Protocol — port 3389, risques : BlueKeep CVE-2019-0708, brute force, exposition directe sur Internet = compromission quasi certaine ; bonnes pratiques : NLA — Network Level Authentication, restriction des sources, accès via bastion uniquement, jamais directement exposé). Le SSH (clés vs mots de passe — les clés sont plus sécurisées, PasswordAuthentication no dans sshd_config ; port non standard pour réduire le bruit ; fail2ban pour bloquer le brute force).

---

#### Chapitre 5 — Bastion, PAM et Zero Trust

Le **bastion/jump host** est un serveur renforcé, placé dans la zone d'administration, qui sert de point de passage obligatoire pour accéder aux serveurs internes. Principe : l'admin se connecte au bastion, puis du bastion vers le serveur cible (SSH ProxyJump — ssh -J bastion user@serveur_interne). Les serveurs cibles n'acceptent les connexions que depuis le bastion. Le bastion enregistre toute l'activité (commandes tapées avec horodatage, vidéo de session rejouable pour l'audit, fichiers transférés loggés). Comptes nominatifs obligatoires (pas de compte « admin » partagé — traçabilité individuelle). MFA obligatoire sur le bastion.

Le **PAM** (Privileged Access Management) est la solution de gestion des accès privilégiés : coffre-fort de mots de passe (stockage chiffré des credentials des comptes à privilèges), rotation automatique (les mots de passe sont changés après chaque utilisation), enregistrement de sessions (toutes les sessions privilégiées sont enregistrées), et injection de credentials (l'admin ne connaît pas le mot de passe root — le PAM l'injecte automatiquement). Solutions : CyberArk, Wallix, BeyondTrust, Delinea, Teleport, Apache Guacamole (open source).

**Zero Trust vs périmétrique :** le modèle périmétrique traditionnel (intérieur = sûr, extérieur = dangereux — le firewall est la frontière ; problème : une fois à l'intérieur, mouvement latéral facile) cède la place au Zero Trust (ne jamais faire confiance, toujours vérifier — chaque accès est authentifié et autorisé même depuis le LAN ; MFA, micro-segmentation, vérification continue, context-aware access).

---

#### Chapitre 6 — Services d'infrastructure vitaux : DHCP, NTP, PKI et synchronisation

*Les briques « silencieuses » qui conditionnent tout le reste — on les oublie jusqu'au jour où elles tombent et plus rien ne fonctionne.*

##### 6.1 DHCP

DHCP (Dynamic Host Configuration Protocol) attribue automatiquement les adresses IP, les masques de sous-réseau, les passerelles, et les serveurs DNS aux machines qui se connectent au réseau. En sécurité : un **rogue DHCP** (serveur DHCP malveillant installé par un attaquant sur le réseau) peut distribuer des configurations qui redirigent tout le trafic vers l'attaquant (passerelle malveillante → interception MITM, serveur DNS malveillant → résolution de noms falsifiée). Protection : **DHCP snooping** (fonctionnalité du switch qui bloque les réponses DHCP provenant de ports non autorisés). En investigation : les **baux DHCP** sont une source précieuse pour la corrélation — ils permettent de savoir quelle machine avait quelle IP à quel moment (logs du serveur DHCP → lier une IP suspecte à une machine physique).

##### 6.2 NTP

NTP (Network Time Protocol) synchronise les horloges de toutes les machines. C'est la brique la plus sous-estimée en sécurité — et pourtant l'une des plus critiques.

Si les horloges des serveurs sont désynchronisées : les **corrélations de logs du SIEM sont fausses** (un événement à 14:03:12 sur le firewall et un événement à 14:10:47 sur l'AD peuvent être le même événement si le décalage est de 7 minutes — l'investigation devient impossible), les **timestamps forensiques sont inutilisables** (la chronologie d'une intrusion repose sur la précision des horodatages), et **Kerberos refuse les authentifications** si l'écart entre le client et le DC dépasse 5 minutes (MaxClockSkew — un NTP défaillant peut provoquer des pannes d'authentification en cascade).

La configuration correcte : toutes les machines pointent vers le même serveur NTP interne (ou un pool NTP de confiance — fr.pool.ntp.org, time.google.com), le serveur NTP interne est synchronisé sur une source de stratum 1 ou 2, et la synchronisation est vérifiée régulièrement. Sécurisation : NTS (Network Time Security — authentification des réponses NTP), restriction des sources (seuls les serveurs NTP autorisés peuvent distribuer le temps).

##### 6.3 PKI interne et AC interne

Une PKI interne (Public Key Infrastructure) permet à l'organisation d'émettre ses propres certificats pour les services internes (serveurs web internes en HTTPS, mTLS entre microservices, authentification de machines, signature de code interne). L'**autorité de certification interne** (AC / CA) est la racine de confiance — si elle est compromise, n'importe qui peut émettre des certificats de confiance pour n'importe quel service interne, ce qui permet l'interception MITM de tout le trafic chiffré interne.

La gestion des certificats internes est un défi opérationnel : inventaire (quels certificats existent, sur quels serveurs, avec quelle date d'expiration), renouvellement (les certificats expirés causent des pannes de service — monitoring des expirations), et révocation (CRL ou OCSP interne — comment révoquer un certificat compromis).

Dans les environnements Windows, **AD CS** (Active Directory Certificate Services) est l'implémentation standard de la PKI interne. Une AC interne AD CS mal configurée peut devenir un vecteur d'escalade de privilèges majeur — les techniques ESC (Escalation via Certificate Services, documentées par SpecterOps/Will Schroeder) permettent à un attaquant de demander un certificat au nom d'un Domain Admin et d'obtenir un accès total au domaine. Le cours Active Directory de la bibliothèque traite ces attaques en profondeur.

##### 6.4 Synchronisation d'identité — AD Connect / Entra Connect

AD Connect (renommé Entra Connect) synchronise les identités de l'Active Directory on-premise vers Azure AD/Entra ID. C'est la brique qui permet le hybrid AD — les utilisateurs se connectent avec le même compte en on-premise et en cloud.

Le risque : le serveur AD Connect a accès à **tous les mots de passe** (il synchronise les hash ou effectue du password hash sync) — c'est une cible critique, aussi sensible qu'un contrôleur de domaine. Les erreurs de configuration courantes : synchronisation de comptes admin vers le cloud (le compte Domain Admin ne devrait PAS être synchronisé), pas de filtering (tous les comptes sont synchronisés, y compris les comptes de service et les comptes à privilèges), et serveur AD Connect non durci (pas de tiering, pas de monitoring, pas d'EDR).

##### 6.5 Fil rouge — BACKBONE : les services vitaux de CargoPlex

> **🔧 BACKBONE — Épisode 3**
>
> Lucas audite les services vitaux. NTP : les serveurs utilisent 3 sources différentes (2 serveurs Linux pointent vers pool.ntp.org, les Windows pointent vers le DC, et les équipements réseau pointent vers un serveur NTP public américain) — résultat : 7 minutes d'écart entre les serveurs Linux et les serveurs Windows. Les corrélations SIEM sont faussées. PKI : l'AC interne (AD CS) utilise un certificat racine auto-signé expiré depuis 8 mois — les alertes de certificat sont ignorées par les utilisateurs (ils ont pris l'habitude de cliquer « continuer quand même »), et 3 templates de certificats ont des permissions trop larges (ESC1 — n'importe quel utilisateur authentifié peut demander un certificat avec le SAN d'un admin). AD Connect : le serveur est un Windows Server 2016 non durci, pas dans le Tier 0, sans EDR, avec un compte de service Domain Admin.

---

### PARTIE II — SYSTÈMES, VIRTUALISATION ET HARDENING

*Les systèmes d'exploitation, les hyperviseurs et leur durcissement — la couche sur laquelle tout repose.*

---

#### Chapitre 7 — Systèmes d'exploitation : Windows et Linux vue infrastructure

*Vue d'ensemble — les cours Windows et Linux de la bibliothèque traitent chaque OS en profondeur.*

##### 7.1 Windows Server

Les rôles principaux : **AD DS** (Active Directory Domain Services — le cœur de l'identité, traité au Ch.21), **DNS** (résolution de noms, intégré à l'AD), **DHCP** (attribution d'adresses), **File Server** (partages SMB), **IIS** (serveur web Microsoft), **WSUS** (Windows Server Update Services — distribution des patches). Les versions et le cycle de vie : Windows Server 2012 R2 (fin de support octobre 2023 — plus de mises à jour de sécurité = risque critique), Windows Server 2016 (support étendu jusqu'en 2027), Windows Server 2019 et 2022 (versions actuelles). Les logs essentiels : Event Logs (Security — authentification, accès objets ; System — services, erreurs ; Application — applicatif), et Sysmon (Event ID 1 — création de processus, 3 — connexions réseau, 7 — chargement de DLL, 11 — création de fichiers, 13 — modification du registre — indispensable pour la détection, cf. cours SOC).

##### 7.2 Linux Server

Les distributions enterprise : **RHEL/CentOS/Rocky/AlmaLinux** (entreprise, stabilité, support long), **Ubuntu Server** (le plus utilisé en cloud et en conteneurs), **Debian** (stabilité, communautaire). Le filesystem (/ = racine, /etc = configuration, /var/log = logs, /home = utilisateurs, /tmp = temporaire — world-writable, souvent utilisé par les attaquants pour déposer des outils). Les permissions (rwx, owner/group/others, SUID/SGID — des binaires SUID mal configurés = escalade de privilèges). Les processus et services (systemd — systemctl, journald). Les logs : journald (journal structuré systemd), syslog (/var/log/syslog ou /var/log/messages), auth.log (authentification — SSH, sudo), et auditd (audit kernel — syscalls, fichiers, exécutables, le pendant Linux de Sysmon).

La coexistence dans l'entreprise : la majorité des infrastructures sont mixtes — Windows pour l'AD, les applications métier, les postes de travail ; Linux pour les serveurs web, les bases de données, les containers, et les appliances réseau. L'analyste SOC et l'IR doivent maîtriser les deux.

---

#### Chapitre 8 — Virtualisation : hyperviseurs, réseaux virtuels et sécurité

*La couche de virtualisation porte la quasi-totalité de l'infrastructure de beaucoup d'entreprises — si l'hyperviseur est compromis, tout le SI tombe.*

##### 8.1 Les hyperviseurs

Les hyperviseurs **Type 1** (bare-metal — directement sur le hardware) : **VMware ESXi** (le plus répandu en entreprise, géré par vCenter Server), **Microsoft Hyper-V** (intégré à Windows Server, géré par SCVMM ou Windows Admin Center), **Proxmox VE** (open source, KVM + LXC, interface web), **KVM** (Kernel-based Virtual Machine — hyperviseur Linux natif, base de Proxmox et d'OpenStack). Les hyperviseurs **Type 2** (sur un OS hôte) : VirtualBox, VMware Workstation — pour le lab et le développement, pas pour la production. L'isolation entre VMs est matérielle (via le processeur — Intel VT-x/AMD-V) — plus solide qu'un container mais plus lourde en ressources.

##### 8.2 L'architecture vSphere

**ESXi** est l'hyperviseur installé sur chaque serveur physique — il gère les VMs locales. **vCenter Server** est la console d'administration centralisée qui gère tous les ESXi d'un cluster — c'est le single point of control… et de compromission. Depuis vCenter, un administrateur peut créer, supprimer, migrer, snapshotter n'importe quelle VM. Si vCenter est compromis, l'attaquant contrôle l'ensemble du SI virtualisé.

##### 8.3 Les réseaux virtuels

Les **vSwitches** (switches virtuels dans l'hyperviseur) connectent les VMs entre elles et avec le réseau physique. Les **port groups** définissent les VLANs virtuels. La segmentation réseau commence à l'hyperviseur : si les vSwitches sont mal configurés, des VMs de zones de sécurité différentes (DMZ et LAN, par exemple) peuvent communiquer directement via le vSwitch sans passer par le firewall. Les **distributed vSwitches** (vDS) étendent la configuration réseau sur tout le cluster vSphere.

##### 8.4 Les fonctionnalités et leurs risques

Les **snapshots** capturent l'état complet d'une VM à un instant T (disque + mémoire). Pratiques pour les rollbacks avant un patch, mais un snapshot contient la mémoire vive avec potentiellement des credentials en clair (tickets Kerberos, tokens, mots de passe en mémoire). Les snapshots « oubliés » grossissent jusqu'à saturer le datastore — et chaque snapshot est une copie analysable par un attaquant. Les **templates** permettent le déploiement rapide de VMs pré-configurées — le risque : le template contient un compte admin local avec un mot de passe par défaut que personne ne change après clonage, ou des clés SSH pré-générées identiques sur toutes les VMs clonées. Les **datastores** sont les volumes de stockage partagés qui contiennent les fichiers des VMs (VMDK = disques virtuels, VMX = configuration). Si un attaquant accède au datastore, il peut copier, monter, et analyser n'importe quel disque virtuel.

##### 8.5 Les risques majeurs

Le **vCenter exposé** avec un mot de passe par défaut ou faible est le scénario le plus critique : l'attaquant obtient le contrôle total de toute l'infrastructure virtualisée. Les CVE vCenter sont régulièrement exploitées (CVE-2021-21985, CVE-2023-34048 — exploitées par des APT et des groupes ransomware). Le **mot de passe root ESXi par défaut** est rarement changé dans beaucoup d'organisations. Le **VM escape** (s'échapper de la VM vers l'hyperviseur) est rare mais critique (CVE-2023-20867 VMware Tools). L'**administration centralisée compromise** crée un effet domino : vCenter compromis = accès à toutes les VMs = l'équivalent d'un Domain Admin mais pour l'infrastructure physique. Et les **groupes ransomware ciblent désormais directement ESXi** (variantes Linux de LockBit, BlackBasta, Royal qui chiffrent les VMDK sur les datastores — plus rapide et plus dévastateur que de chiffrer chaque VM individuellement).

##### 8.6 Le hardening de la virtualisation

Mot de passe robuste et unique sur chaque ESXi et sur vCenter. MFA sur l'accès vCenter. Patching de l'hyperviseur en priorité (les CVE ESXi/vCenter sont exploitées dans les jours suivant la publication). Réseau de management dédié (vCenter et les interfaces ESXi accessibles uniquement depuis le réseau d'administration via le bastion — jamais depuis le réseau utilisateur). Désactivation des services inutiles sur ESXi (SSH désactivé sauf maintenance, shell interactif désactivé). Logging vers le SIEM (vCenter génère des logs d'audit — connexions, opérations sur les VMs, modifications de configuration). Nettoyage des snapshots (pas de snapshot de plus de 72h en production sauf justification documentée).

> **🔧 BACKBONE — Épisode 4**
>
> Lucas accède au vCenter de CargoPlex avec le mot de passe par défaut VMware (admin/VMware1!). Il constate : 12 snapshots « temporaires » dont le plus ancien date de 14 mois (2,1 To de stockage gaspillé), le réseau de management n'existe pas (vCenter accessible depuis les postes utilisateurs), 3 VMs de production sont encore sur ESXi 6.7 (fin de support), et aucun log vCenter n'est envoyé au SIEM. Il ajoute le hardening vSphere aux quick wins P0.

---

#### Chapitre 9 — Hardening : durcir les systèmes et les services

Le hardening est la réduction de la surface d'attaque par la configuration sécurisée. Principes : désactiver ce qui n'est pas nécessaire, changer les configurations par défaut, appliquer le moindre privilège, mettre à jour. Les benchmarks de référence : **CIS Benchmarks** (guides détaillés par système — Windows Server, Linux, Docker, Kubernetes, VMware, cloud — chaque recommandation avec justification et commande d'implémentation), **guides ANSSI** (recommandations de durcissement — Active Directory, Linux, Windows).

**Hardening Windows** : désactivation de SMBv1 (EternalBlue), désactivation de LLMNR et NBT-NS (résolution de noms broadcast → poisoning → capture de hashes NTLM), PowerShell Constrained Language Mode (limite les commandes PowerShell disponibles aux utilisateurs), AppLocker ou WDAC (contrôle d'exécution — seuls les exécutables autorisés peuvent s'exécuter), audit policy avancée (Event Logs détaillés), Sysmon déployé et configuré (cf. cours SOC), LAPS (Local Administrator Password Solution — mot de passe admin local unique et roté sur chaque poste, stocké dans l'AD), Credential Guard (isolation des credentials en mémoire — empêche Mimikatz).

**Hardening Linux** : SSH hardening (PasswordAuthentication no, PermitRootLogin no, port non standard, AllowUsers/AllowGroups), désactivation des services inutiles (systemctl disable), permissions des fichiers (chmod 600 sur les fichiers sensibles, pas de world-writable sauf /tmp), SELinux/AppArmor (contrôle d'accès obligatoire — MAC), auditd (monitoring des syscalls, fichiers, exécutables), fail2ban (blocage automatique après N tentatives échouées).

**Hardening des services** : serveurs web (headers de sécurité, version masquée, directory listing désactivé — cf. Ch.17), bases de données (authentification obligatoire, bind sur 127.0.0.1 sauf nécessité, audit activé — cf. Ch.12-13), DNS (zone transfers restreints, recursion limitée).

---

#### Chapitre 10 — Cryptographie : les fondamentaux pour l'infrastructure

**Chiffrement symétrique** (AES-256 — même clé pour chiffrer et déchiffrer, rapide, utilisé pour les données au repos et le trafic en transit ; le problème : comment transmettre la clé de manière sécurisée ?). **Chiffrement asymétrique** (RSA, ECC — paire clé publique/clé privée ; la clé publique chiffre, la clé privée déchiffre ; lent, utilisé pour l'échange de clés et la signature numérique ; le fondement de TLS et SSH). **Hachage** (SHA-256, SHA-3 — empreinte irréversible de taille fixe, utilisée pour vérifier l'intégrité des fichiers et les signatures ; bcrypt, Argon2 — fonctions de hachage adaptatives pour les mots de passe, conçues pour être lentes → résistantes au brute force ; MD5 et SHA-1 sont obsolètes — collisions démontrées, ne plus utiliser).

**PKI** (Public Key Infrastructure — l'infrastructure de confiance pour les certificats) : les autorités de certification (CA) émettent des certificats qui lient une identité à une clé publique. La chaîne de confiance (Root CA → Intermediate CA → certificat serveur). La révocation (CRL — Certificate Revocation List, OCSP — Online Certificate Status Protocol). Let's Encrypt et l'automatisation ACME (certificats gratuits, renouvelés automatiquement).

**Certificats X.509** : SAN (Subject Alternative Name — un certificat peut couvrir plusieurs domaines), wildcard (*.example.com), durée de validité (90 jours Let's Encrypt, 1 an maximum pour les CA commerciales). Erreurs courantes : certificats expirés en production (alerte ignorée → les utilisateurs cliquent « continuer » → perte de l'habitude de vérifier les certificats), certificats auto-signés en production (pas de chaîne de confiance vérifiable), clés privées stockées sur le serveur web sans protection.

**Chiffrement au repos** : FDE (Full Disk Encryption — BitLocker sur Windows, LUKS sur Linux), TDE (Transparent Data Encryption — chiffrement de la base de données au niveau du moteur), chiffrement de fichiers. **Chiffrement en transit** : TLS 1.2/1.3 (le handshake — échange de clés via asymétrique, trafic chiffré via symétrique ; cipher suites — combinaisons d'algorithmes ; PFS — Perfect Forward Secrecy — même si la clé privée est compromise plus tard, les sessions passées restent protégées), mTLS (authentification mutuelle — le client ET le serveur présentent un certificat, utilisé entre microservices et dans les architectures Zero Trust).

---

#### Chapitre 11 — Gestion des vulnérabilités et patching

Le cycle de vie d'une vulnérabilité : découverte (chercheur, vendor, attaquant) → attribution CVE (MITRE) → publication d'un advisory (vendor, CERT) → publication d'un patch → déploiement → vérification. La fenêtre entre la publication de l'advisory et le déploiement du patch est la surface d'attaque — les APT exploitent les CVE dans les heures suivant la publication (cf. cours APT Ch.3 — Ivanti, Fortinet, Citrix).

Le scoring : **CVSS** (Common Vulnerability Scoring System — Base score 0-10 + Temporal + Environmental ; les limites : un CVSS 9.8 sur un système isolé sans données sensibles est moins urgent qu'un CVSS 7.5 sur le contrôleur de domaine), **EPSS** (Exploit Prediction Scoring System — probabilité qu'une vulnérabilité soit exploitée dans les 30 prochains jours — plus opérationnel que le CVSS seul), **CISA KEV** (Known Exploited Vulnerabilities — la liste des vulnérabilités activement exploitées in the wild, la priorité absolue indépendamment du CVSS).

Les outils de scan : **Nessus/Tenable** (le plus répandu), **Qualys** (cloud-native), **OpenVAS** (open source). Scan authentifié (avec des credentials — voit les vulnérabilités internes, les patches manquants, les configurations) vs non authentifié (depuis l'extérieur — voit ce qu'un attaquant voit). Le processus de patching : WSUS/SCCM/Intune pour Windows, apt/yum pour Linux, Ansible pour l'automatisation multi-plateforme. SLA par criticité : critique < 48h, élevé < 15 jours, moyen < 30 jours, faible trimestriel. La gestion des assets end-of-life (les Windows Server 2012 de CargoPlex : pas de patch disponible → seules options : isoler, surveiller, et migrer).

---

### PARTIE III — DONNÉES, STOCKAGE, MESSAGERIE ET TRANSFERTS

*Comment les données sont stockées, sécurisées, échangées et sauvegardées — le patrimoine informationnel et son infrastructure.*

---

#### Chapitre 12 — Bases de données relationnelles (SQL)

Le modèle relationnel (tables, colonnes, clés primaires/étrangères, relations). SQL en pratique (SELECT, JOIN, INSERT, UPDATE, DELETE — les requêtes qu'un analyste doit comprendre pour investiguer). Les SGBD majeurs : **MySQL/MariaDB** (port 3306, le plus répandu en web — fichiers my.cnf, general_log, slow_query_log), **PostgreSQL** (port 5432, le plus riche fonctionnellement — postgresql.conf, pg_log, pgaudit), **SQL Server** (port 1433, écosystème Microsoft — .mdf/.ldf, SQL Audit), **Oracle** (port 1521, grandes entreprises/legacy — Unified Auditing).

L'**injection SQL** est l'une des vulnérabilités les plus dévastatrices. Le principe : l'attaquant insère du code SQL dans un champ utilisateur que l'application concatène dans une requête sans la nettoyer. Impact : lecture de toute la base, modification ou suppression de données, exécution de commandes OS (xp_cmdshell sur SQL Server, INTO OUTFILE sur MySQL, COPY TO sur PostgreSQL), contournement d'authentification. Défense : requêtes paramétrées (prepared statements), ORM, validation des entrées, moindre privilège sur le compte DB de l'application.

Les **credentials dans les fichiers de configuration** : les mots de passe de connexion à la base sont souvent en clair dans les fichiers de conf — .my.cnf, .pgpass, web.config, .env, wp-config.php, connection strings. Un attaquant qui accède au serveur applicatif trouve souvent les credentials DB.

📋 **Logs & traces à surveiller** — Sources : slow_query_log (MySQL), pg_log (PostgreSQL), SQL Audit (SQL Server). Normal : SELECT sur les tables applicatives, connexions depuis le serveur applicatif. Suspect : UNION SELECT, SLEEP(), tentatives d'export/écriture fichier, accès aux tables système (information_schema, pg_shadow).

---

#### Chapitre 13 — Bases de données NoSQL

Pourquoi NoSQL : scalabilité horizontale, schéma flexible, performances sur de gros volumes, cas d'usage spécifiques. Les types : **document** (MongoDB — port 27017), **clé-valeur** (Redis — port 6379), **colonnes** (Cassandra — port 9042), **graphe** (Neo4j — port 7474), **search** (Elasticsearch/OpenSearch — port 9200).

**MongoDB** : documents JSON/BSON dans des collections. Le risque historique : MongoDB sans authentification exposé sur Internet — des dizaines de milliers de bases ransonnées. Toujours activer l'authentification et restreindre l'écoute (bindIp: 127.0.0.1). **Redis** : base clé-valeur en mémoire, ultra-rapide (cache, sessions). Le risque : Redis sans authentification (pas de requirepass) permet l'injection de cron jobs à distance → RCE (CONFIG SET dir /var/spool/cron/ → SAVE). **Elasticsearch** : moteur de recherche full-text, backend de la stack ELK. Le risque : API port 9200 sans authentification (pas de X-Pack Security) → lecture/suppression de tous les index, exposition de logs contenant des données sensibles. **NoSQL injection** : concept similaire à l'injection SQL adapté au langage de requête NoSQL (MongoDB : { username: {$ne: null} } → bypass d'authentification).

---

#### Chapitre 14 — Stockage, sauvegardes et résilience technique

*Le stockage est à la fois une surface d'attaque et le dernier rempart en cas de compromission — les ransomwares ciblent les sauvegardes en priorité.*

##### 14.1 Technologies de stockage

**DAS** (Direct Attached Storage — disques locaux, le plus simple). **NAS** (Network Attached Storage — partage de fichiers en réseau via SMB/NFS, accessible depuis le LAN → attaquable depuis le LAN). **SAN** (Storage Area Network — stockage bloc haute performance via Fibre Channel ou iSCSI, normalement isolé du réseau utilisateur — sauf erreur de configuration). **Stockage objet** (S3, Azure Blob, GCS — accès via API REST, scalabilité illimitée, risque de buckets publics).

**RAID** : RAID 1 (mirroring — 2 disques identiques, survit à 1 panne), RAID 5 (parité distribuée — survit à 1 panne, capacité N-1), RAID 10 (mirroring + striping — survit à 1 panne par paire, performance + résilience). Point fondamental : **RAID ≠ sauvegarde**. RAID protège contre la panne matérielle d'un disque. Il ne protège PAS contre le ransomware (qui chiffre les données sur tous les disques du RAID simultanément), la suppression accidentelle, la corruption logique, ou l'exfiltration.

##### 14.2 Sauvegardes

**Snapshots vs vraies sauvegardes** : un snapshot est une copie à un instant T dans le même système de stockage — si le stockage est chiffré par un ransomware, les snapshots le sont aussi. Une vraie sauvegarde est une copie sur un système séparé, idéalement hors ligne ou immuable.

La règle **3-2-1** : 3 copies des données, sur 2 supports différents, dont 1 hors site (cloud, bande, datacenter distant). Les **sauvegardes immuables** (WORM — Write Once Read Many) sont le contrôle anti-ransomware le plus critique : même avec un accès admin, l'attaquant ne peut pas modifier ou supprimer les sauvegardes immuables pendant la période de rétention configurée. Le **chiffrement des sauvegardes** est impératif : les sauvegardes contiennent TOUTES les données de l'organisation — si elles ne sont pas chiffrées et qu'un attaquant y accède, c'est une fuite complète.

##### 14.3 Erreurs classiques

La sauvegarde sur un **NAS joint au domaine AD** est l'erreur la plus courante et la plus dévastatrice : le ransomware qui compromet le domaine chiffre aussi les sauvegardes. Le **même compte admin partout** (l'admin du domaine est admin du NAS de sauvegarde → pas d'isolation de la chaîne de sauvegarde). **Pas de test de restauration** (le jour J, on découvre que les sauvegardes sont corrompues, incomplètes, ou que la procédure de restauration prend 5 jours au lieu de 48h). Une **rétention incohérente** (30 jours de rétention mais le ransomware était dormant depuis 45 jours → les sauvegardes « propres » n'existent plus). Et **pas de segmentation du stockage** (le réseau de sauvegarde est accessible depuis le réseau utilisateur).

> **🔧 BACKBONE — Épisode 5**
>
> Lucas inspecte les sauvegardes de CargoPlex : NAS Synology joint au domaine AD, accessible en SMB depuis le réseau utilisateur, non chiffré, pas de snapshot immuable, et des tests de restauration jamais réalisés. Le NAS utilise le même compte admin que le domaine. Lucas réalise un test de restauration de l'ERP → échec partiel : les logs de transaction des 3 derniers jours sont absents. En cas de ransomware, les sauvegardes seraient chiffrées en même temps que le reste du SI, et même sans ransomware, la restauration est incomplète.

---

#### Chapitre 15 — Messagerie : SMTP, sécurité email et anti-phishing

L'architecture email : **MTA** (Mail Transfer Agent — le serveur qui envoie et relaye les mails : Postfix, Exchange, Sendmail), **MDA** (Mail Delivery Agent — stocke le mail dans la boîte), **MUA** (Mail User Agent — le client : Outlook, Thunderbird, webmail). Le flux : envoi SMTP 25/587/465, réception IMAP 143/993 ou POP3 110/995.

SMTP en détail : le protocole est conversationnel (HELO/EHLO, MAIL FROM, RCPT TO, DATA). Les commandes de reconnaissance (VRFY — vérifier si un utilisateur existe, EXPN — lister les membres d'une liste — à désactiver). L'**open relay** (un serveur SMTP qui relaye les mails de n'importe qui vers n'importe qui → vecteur de spam massif — à ne jamais configurer).

La sécurité email : **SPF** (Sender Policy Framework — enregistrement TXT DNS qui liste les serveurs autorisés à envoyer des mails pour le domaine — un mail provenant d'un serveur non listé échoue la vérification SPF), **DKIM** (DomainKeys Identified Mail — signature cryptographique du mail par le serveur d'envoi — le destinataire vérifie la signature avec la clé publique dans le DNS), **DMARC** (Domain-based Message Authentication, Reporting and Conformance — politique qui dit quoi faire si SPF ou DKIM échoue : none/quarantine/reject). Les trois sont complémentaires et indispensables : SPF seul ne suffit pas (contournable), DKIM seul ne suffit pas (pas de politique de rejet), DMARC orchestre les deux et fournit du reporting.

L'anti-phishing du point de vue infrastructure : **email gateway** (filtrage entrant — analyse des URLs, sandboxing des pièces jointes, réécriture des liens), les **headers email** comme artefacts d'investigation (Received — trace le chemin du mail serveur par serveur, X-Originating-IP, Authentication-Results — résultat SPF/DKIM/DMARC, Return-Path vs From — la différence trahit le spoofing).

---

#### Chapitre 16 — Partage de fichiers et transfert de données

Les protocoles de transfert : **FTP** (port 21, en clair → obsolète, ne jamais utiliser), **FTPS** (FTP + TLS — acceptable), **SFTP** (port 22, via SSH — recommandé, ce n'est PAS du FTP, c'est un sous-système SSH), **SCP** (copie simple via SSH), **rsync** (synchronisation incrémentale via SSH).

**SMB/CIFS** (Server Message Block — port 445, protocole de partage Windows) : SMBv1 est responsable de la propagation de WannaCry et NotPetya via EternalBlue (MS17-010) → **désactiver immédiatement** (Get-SmbServerConfiguration | Select EnableSMB1Protocol). SMBv2 est le minimum acceptable. SMBv3 ajoute le chiffrement et la signature — recommandé.

**NFS** (Network File System — port 2049, partage Unix) : les risques sont les exports trop larges (exporter vers * au lieu d'une IP/sous-réseau spécifique) et no_root_squash (un utilisateur root sur le client est root sur le partage → écriture de fichiers arbitraires, escalade de privilèges).

Le stockage cloud (S3, Azure Blob, GCS — accès via API REST, risque de buckets publics — des milliers de fuites documentées). Le transfert moderne (WebDAV — extension HTTP pour l'édition collaborative, MFT — Managed File Transfer — transfert sécurisé avec traçabilité).

---

### PARTIE IV — APPLICATIONS, WEB ET APIs

---

#### Chapitre 17 — Serveurs web, reverse proxy, WAF et CDN

Les 3 serveurs web majeurs : **Apache httpd** (configuration par fichiers .conf et .htaccess, modules mod_ssl/mod_security/mod_rewrite, logs access_log et error_log), **Nginx** (configuration déclarative, reverse proxy natif, performant en charge, logs access.log et error.log), **IIS** (Internet Information Services — intégré à Windows Server, configuration via GUI ou web.config, logs IIS dans W3SVC).

La configuration sécurisée : headers de sécurité (Strict-Transport-Security — HSTS, X-Content-Type-Options: nosniff, X-Frame-Options: DENY, Content-Security-Policy — CSP, Referrer-Policy), masquage de la version serveur (ServerTokens Prod sur Apache, server_tokens off sur Nginx), désactivation du directory listing (Options -Indexes), permissions strictes sur les fichiers web (pas de world-writable), et HTTPS obligatoire (redirect 80 → 443, Let's Encrypt + certbot pour l'automatisation).

Le **reverse proxy** est un intermédiaire entre les clients et les serveurs backend — il masque l'IP et la technologie du backend, centralise les certificats TLS, ajoute des headers de sécurité, et fournit un point unique de logging. **TLS termination** (le reverse proxy déchiffre TLS → trafic interne en clair sauf rechiffrement) et **mTLS** (authentification mutuelle — les deux côtés présentent un certificat, utilisé entre microservices et en Zero Trust).

Le **load balancer** répartit les requêtes entre serveurs backend (round-robin, least connections, IP hash, weighted) avec des health checks pour retirer les serveurs en panne. Le **WAF** (Web Application Firewall) filtre les requêtes HTTP malveillantes (ModSecurity + OWASP CRS, WAF cloud — AWS WAF, Cloudflare) — limite : ne remplace pas le secure coding, contournable par encodage/obfuscation. Le **CDN** (Cloudflare, Akamai, CloudFront) distribue le contenu géographiquement, absorbe les DDoS, et masque l'IP d'origine.

Les **logs web** comme source d'investigation : patterns suspects dans access_log — rafales de 404 (scan de répertoires), POST vers des fichiers uploadés (web shell), caractères spéciaux dans les URLs (' -- UNION <script>), user-agents d'outils de scan (sqlmap, nikto, dirsearch).

---

#### Chapitre 18 — Architecture web et vulnérabilités : la vue d'ensemble

*Vue d'ensemble — le cours AppSec (futur) traitera chaque vulnérabilité en profondeur.*

L'architecture **3 tiers** : frontend (navigateur — HTML, CSS, JavaScript), backend (serveur applicatif — logique métier), base de données (stockage persistant). Les langages et frameworks : PHP (Laravel, Symfony, WordPress), Python (Django, Flask, FastAPI), Java (Spring Boot), Node.js (Express, Next.js), .NET/C# (ASP.NET Core), Go (Gin, Fiber), Ruby (Rails).

Sessions et cookies : HTTP est stateless → le serveur crée une session et envoie un cookie (Set-Cookie: session_id=abc123). Le navigateur renvoie ce cookie à chaque requête. Les flags de sécurité : **Secure** (cookie transmis uniquement en HTTPS), **HttpOnly** (cookie inaccessible au JavaScript → protection XSS), **SameSite** (strict/lax/none → protection CSRF).

**OWASP Top 10** — la référence : A01 Broken Access Control (IDOR, privesc → vérification d'autorisation systématique), A02 Cryptographic Failures (données non chiffrées → TLS partout, chiffrement au repos), A03 Injection (SQL, OS, LDAP → requêtes paramétrées), A04 Insecure Design (failles de conception → threat modeling), A05 Security Misconfiguration (config par défaut, debug activé → hardening), A06 Vulnerable Components (dépendances avec CVE → SCA), A07 Auth & Identification Failures (auth faible → MFA, rate limiting), A08 Software & Data Integrity (désérialisation, supply chain → vérification d'intégrité), A09 Logging & Monitoring Failures (pas de logs → logging de sécurité), A10 SSRF (requêtes serveur vers cible contrôlée → whitelist d'URLs).

---

#### Chapitre 19 — APIs : REST, GraphQL et sécurité

**REST** (Representational State Transfer) : ressources identifiées par URL (/api/v1/users/42), verbes HTTP (GET/POST/PUT/DELETE), JSON, stateless. **GraphQL** : requêtes flexibles (le client demande exactement les champs voulus), introspection (par défaut activée → cartographie complète de l'API pour l'attaquant), risques spécifiques (requêtes imbriquées → DoS, injection). **SOAP** (Simple Object Access Protocol — XML, WSDL, legacy mais encore présent en entreprise — interfaces bancaires, ERP).

L'authentification API : **API Keys** (simple token dans le header — à protéger, à restreindre par IP/scope, à roter régulièrement), **OAuth 2.0** (authorization code flow — le standard moderne), **Bearer tokens** (JWT dans le header Authorization), **JWT** (JSON Web Token — structure header.payload.signature, signature HMAC ou RSA ; risques : alg:none → signature désactivée, secret HMAC faible → brute force, pas de vérification de la signature côté serveur, token trop longue durée de vie), **mTLS** (authentification mutuelle pour les API internes).

**OWASP API Security Top 10** : BOLA/IDOR (accès aux objets d'autres utilisateurs — la vulnérabilité API #1), Broken Authentication (auth faible sur l'API), Excessive Data Exposure (l'API renvoie plus de données que nécessaire — le client filtre au lieu du serveur), Lack of Rate Limiting (pas de throttling → brute force, DoS), Broken Function Level Authorization (accès à des fonctions admin sans vérification).

La documentation comme surface d'attaque : Swagger/OpenAPI exposé publiquement = cartographie complète de l'API pour l'attaquant (endpoints, paramètres, types, exemples).

---

### PARTIE V — IDENTITÉ ET AUTHENTIFICATION

*L'identité est le nouveau périmètre — en cloud comme on-premise, qui vous êtes détermine ce que vous pouvez faire.*

---

#### Chapitre 20 — LDAP et annuaires

Un annuaire est une base de données hiérarchique optimisée pour la lecture — il stocke les utilisateurs, les groupes, les machines et les services. **LDAP** (Lightweight Directory Access Protocol — port 389, LDAPS port 636) est le protocole standard. La structure DIT (Directory Information Tree) : DC (Domain Component — dc=corp,dc=com), OU (Organizational Unit — ou=Users), CN (Common Name — cn=Alice Dupont), DN (Distinguished Name — chemin complet : cn=Alice,ou=Users,dc=corp,dc=com). Les opérations : Bind (authentification), Search (recherche), Add, Modify, Delete.

OpenLDAP vs Active Directory : OpenLDAP est un annuaire LDAP léger sous Linux. Active Directory est un annuaire enrichi sous Windows — LDAP + Kerberos + DNS + GPO (traité au Ch.21). Les risques LDAP : **anonymous bind** (connexion sans credentials → lecture complète de l'annuaire — tous les utilisateurs, groupes, attributs), **LDAP sans TLS** (port 389 — credentials en clair sur le réseau → toujours utiliser LDAPS 636 ou STARTTLS), **injection LDAP** (similaire à l'injection SQL mais sur les requêtes LDAP).

---

#### Chapitre 21 — Active Directory comme socle d'infrastructure

*Ce chapitre ne redouble pas le cours AD — il traite l'AD comme brique d'infrastructure centrale dont la compréhension est indispensable même sans être spécialiste AD.*

##### 21.1 Ce que l'AD fait réellement

AD n'est pas « un annuaire » — c'est le **socle de l'infrastructure Windows**. AD = **LDAP** (annuaire des utilisateurs, groupes, machines — chaque objet a des attributs, des appartenances, des permissions) + **Kerberos** (protocole d'authentification — TGT, TGS, Service Ticket ; les mots de passe ne transitent jamais sur le réseau après l'authentification initiale) + **DNS** (résolution de noms intégrée — les machines trouvent leur DC via les enregistrements SRV DNS ; si le DNS AD tombe, plus rien ne fonctionne) + **GPO** (Group Policy Objects — configuration centralisée de tous les postes et serveurs : politique de mots de passe, restriction d'exécution, mapping de lecteurs, configuration du firewall Windows, déploiement de logiciels) + **SYSVOL** (réplication des politiques et scripts de login entre les DC) + **trusts** (relations de confiance entre domaines et forêts — un trust mal configuré = un chemin d'attaque inter-domaines).

##### 21.2 Le rôle des contrôleurs de domaine

Les DC (Domain Controllers) sont les serveurs les plus critiques de l'infrastructure — ils stockent **tous les comptes**, **tous les mots de passe** (sous forme de hashes NTLM), et délivrent les tickets Kerberos. Un DC compromis = le SI entier est compromis. C'est pourquoi le **tiering model** est le contrôle fondamental : **Tier 0** (DC, comptes admin domaine, AD CS, AD Connect — la zone la plus protégée), **Tier 1** (serveurs applicatifs, comptes admin serveur), **Tier 2** (postes de travail, comptes utilisateurs). La règle : un compte Tier 2 ne se connecte JAMAIS à un serveur Tier 0, et réciproquement.

##### 21.3 Les dépendances de l'écosystème Windows

Exchange dépend d'AD (les boîtes mail sont des objets AD). SQL Server peut utiliser l'authentification AD (authentification intégrée Windows). Les partages de fichiers utilisent les groupes AD pour les ACL. Le VPN authentifie contre AD (via RADIUS/NPS). Les applications métier délèguent l'authentification à AD (SSO via Kerberos ou SAML). Le SIEM collecte les logs AD (Event Logs Security). **Quand AD tombe, TOUT tombe.** Un problème AD n'est jamais « un sujet annuaire » — c'est un sujet infrastructure central.

##### 21.4 Les attaques qui exploitent l'AD

Vue d'ensemble (le cours AD de la bibliothèque couvre en profondeur) : **Kerberoasting** (demander des TGS pour des comptes de service et cracker les hashes offline), **AS-REP Roasting** (cibler les comptes sans pré-authentification Kerberos), **Pass-the-Hash** (utiliser le hash NTLM volé pour s'authentifier sans le mot de passe), **Golden Ticket** (forger un TGT avec le hash krbtgt → accès illimité au domaine), **Silver Ticket** (forger un Service Ticket), **DCSync** (simuler un DC pour demander la réplication des hashes de tous les comptes), **NTLM relay** (relayer une authentification NTLM vers un autre service). Pourquoi désactiver NTLM quand possible : NTLM est un protocole legacy vulnérable au relay et au pass-the-hash, Kerberos est plus sécurisé.

---

#### Chapitre 22 — Authentification moderne : SSO, OAuth, SAML, OIDC

**SSO** (Single Sign-On — s'authentifier une fois, accéder à tout) : avantage UX et sécurité (un seul mot de passe fort + MFA plutôt que 15 mots de passe faibles), risque (si le SSO est compromis, tout est compromis).

**SAML** (Security Assertion Markup Language — protocole de SSO XML, créé pour l'entreprise) : l'IdP (Identity Provider — AD FS, Okta, Azure AD) authentifie l'utilisateur et génère une assertion SAML (un document XML signé contenant l'identité et les attributs). Le SP (Service Provider — l'application) vérifie l'assertion et accorde l'accès. L'attaque **GoldenSAML** (forger des assertions SAML en compromettant la clé de signature de l'IdP → accès à tous les SP sans authentification — utilisé par APT29 dans SolarWinds, cf. cours APT Ch.29).

**OAuth 2.0** (framework d'autorisation — le standard moderne pour les APIs) : l'authorization code flow (le plus sécurisé — redirection vers l'IdP, code d'autorisation, échange contre un token), l'implicit flow (déprécié — le token est directement dans l'URL), le client credentials flow (entre services, pas d'utilisateur). Tokens (access token — durée de vie courte, refresh token — durée de vie longue pour renouveler l'access token). Scopes (permissions granulaires).

**OpenID Connect** (OIDC — couche d'authentification au-dessus d'OAuth 2.0) : ajoute l'ID Token (un JWT qui contient l'identité de l'utilisateur) et le UserInfo endpoint. C'est le standard moderne pour le SSO web.

**JWT** (JSON Web Token — token autoportant signé) : structure header.payload.signature (chaque partie en base64). Le header contient l'algorithme de signature (HS256, RS256). Le payload contient les claims (sub, iss, exp, iat, rôles). La signature garantit l'intégrité. Risques : alg:none (l'attaquant met « none » comme algorithme → la signature n'est pas vérifiée), secret HMAC faible (brute force du secret → forgeage de tokens), pas de vérification côté serveur, et token avec une durée de vie trop longue.

---

#### Chapitre 23 — IAM cloud : Azure AD/Entra ID, AWS IAM, GCP IAM

*L'IAM cloud est le terrain de jeu des APT modernes — Volt Typhoon, APT29 compromettent l'identité cloud.*

**Azure AD / Entra ID** : tenants (l'organisation), utilisateurs, groupes, applications enregistrées, rôles (Global Admin — le plus puissant, équivalent Domain Admin en cloud), Conditional Access (politiques d'accès contextuelles — autoriser/bloquer selon l'appareil, la localisation, le risque), et PIM (Privileged Identity Management — activation temporaire des rôles admin, just-in-time access).

**AWS IAM** : users, groups, roles, policies (documents JSON qui définissent les permissions). Le principe du moindre privilège : chaque entité a uniquement les permissions nécessaires. Les erreurs courantes : politique AdministratorAccess sur tous les utilisateurs, access keys (credentials programmatiques) en clair dans le code source, pas de MFA sur le compte root.

**GCP IAM** : service accounts, roles (predefined/custom), bindings (liaison role → identité → ressource).

L'**identité comme nouveau périmètre** : en cloud, il n'y a pas de firewall au sens traditionnel — l'identité EST le contrôle d'accès. Le token est la clé — token theft (vol de token OAuth/SAML), OAuth abuse (application malveillante demandant des scopes excessifs), et MFA bypass (AitM — Adversary-in-the-Middle, intercepte le token post-MFA) sont les vecteurs d'attaque cloud dominants. Le **monitoring identity** est indispensable : Azure AD sign-in logs (connexions, risques détectés), CloudTrail (toutes les actions API AWS), et les anomalies (connexion depuis un pays inhabituel, token utilisé depuis 2 IP simultanément).

---

#### Chapitre 24 — MFA, gestion des mots de passe et facteurs d'authentification

Les **3 facteurs** : ce que je sais (mot de passe, PIN), ce que j'ai (téléphone/TOTP, clé physique FIDO2/YubiKey, badge), ce que je suis (empreinte, reconnaissance faciale). Le MFA combine au moins 2 facteurs différents. Quels comptes : TOUS les comptes admin (P0), tous les accès distants (VPN, RDP), tous les accès cloud, et idéalement tous les utilisateurs. Quels types : **FIDO2/clés physiques** (résistantes au phishing — le gold standard pour les admins), **push/TOTP** (acceptable pour les utilisateurs standard), SMS (le plus faible — SIM swapping — à éviter).

Les **attaques anti-MFA** : MFA fatigue/prompt bombing (envoyer des dizaines de notifications push jusqu'à ce que l'utilisateur accepte par lassitude), AitM (Adversary-in-the-Middle — proxy qui intercepte le token de session après l'authentification MFA → contourne le MFA car le token est volé post-authentification), SIM swapping (transfert du numéro de téléphone vers une SIM contrôlée par l'attaquant → interception des SMS OTP), et vol de token post-MFA (le MFA protège l'authentification, pas le token de session résultant).

La **politique de mots de passe** : longueur > complexité (les recommandations NIST 2024 privilégient 12+ caractères sans exigence de caractères spéciaux — un mot de passe long est plus résistant qu'un mot de passe court et complexe), gestionnaire de mots de passe (un mot de passe unique et fort par service), interdiction de réutilisation (vérification contre les bases de mots de passe compromis — Have I Been Pwned), et pas de rotation obligatoire si MFA est en place (la rotation forcée pousse les utilisateurs à choisir des mots de passe plus faibles et prévisibles).

---

### PARTIE VI — CLOUD, CONTAINERS ET ARCHITECTURES MODERNES

*L'infrastructure moderne — ce qui remplace progressivement le datacenter on-premise.*

---

#### Chapitre 25 — Cloud : modèles, architecture et responsabilité partagée

Les 3 modèles : **IaaS** (le provider gère hardware/réseau/virtualisation, vous gérez OS/middleware/app/données — AWS EC2, Azure VM, GCP Compute), **PaaS** (le provider gère aussi OS/middleware/runtime, vous gérez app/données — Heroku, Azure App Service), **SaaS** (le provider gère tout, vous gérez la configuration et les données — Office 365, Salesforce, Slack). Le **Shared Responsibility Model** est la source n°1 de confusion : le provider est responsable de la sécurité DU cloud (infrastructure), vous êtes responsable de la sécurité DANS le cloud (configuration, accès, données). La majorité des brèches cloud viennent de mauvaises configurations (S3 buckets publics, IAM trop permissif, security groups ouverts).

Les concepts cloud transversaux : régions et zones de disponibilité (résilience géographique), VPC/VNet (réseau virtuel isolé — votre réseau privé dans le cloud), security groups/NSG (filtrage réseau cloud — l'équivalent du firewall), stockage objet (S3/Azure Blob/GCS). L'architecture cloud type (VPC multi-tiers : subnet public → load balancer → subnet privé → application → subnet privé → base de données, NAT gateway pour le trafic sortant, bastion cloud pour l'administration).

Les **erreurs de configuration** les plus courantes : S3 bucket public (données exposées sur Internet), security group 0.0.0.0/0 sur SSH (le serveur est accessible depuis n'importe où), IAM trop permissif (AdministratorAccess pour tout le monde), logs non activés (CloudTrail/Activity Log désactivés → aucune traçabilité), et chiffrement désactivé (données au repos en clair).

---

#### Chapitre 26 — Sécurité cloud : services natifs et bonnes pratiques

Les services de sécurité natifs : **AWS** (GuardDuty — détection de menaces, Security Hub — posture, Config — conformité, CloudTrail — audit API, KMS — gestion des clés, IAM Access Analyzer — permissions excessives), **Azure** (Defender for Cloud — posture et détection, Sentinel — SIEM cloud-native, Key Vault — secrets et clés, Azure Policy — conformité), **GCP** (Security Command Center — posture, Cloud KMS — clés, VPC Service Controls — périmètre de données).

Le **CSPM** (Cloud Security Posture Management) vérifie automatiquement les configurations cloud contre les benchmarks (CIS, propriétaire) — détecte les S3 publics, les security groups ouverts, les IAM excessifs, les logs désactivés. La gestion des secrets (Key Vault, KMS, Secret Manager — ne jamais stocker de secrets dans le code, les variables d'environnement en clair, ou les fichiers Terraform). L'**IaC sécurisée** : Terraform state files contiennent des secrets → backend distant chiffré obligatoire (S3 + KMS, Azure Blob + encryption) ; scanning IaC (tfsec, checkov — détectent les erreurs de configuration avant le déploiement). Le cloud logging (CloudTrail, Azure Activity Log, GCP Cloud Audit Logs — les logs qu'il faut absolument activer et centraliser vers le SIEM).

---

#### Chapitre 27 — Containers : Docker, Kubernetes et sécurité

*Traitement « socle » — les concepts et les risques fondamentaux, pas un cours DevSecOps complet.*

**Docker** : une image est un template read-only (construit depuis un Dockerfile), un container est une instance en exécution d'une image. Le registry (Docker Hub, registries privés — Harbor, GitLab Registry) stocke les images. La sécurité des images : utiliser des images officielles, scanner les vulnérabilités (Trivy, Snyk, Clair), et le risque de supply chain d'images (une image Docker Hub malveillante donne accès à tout ce que le container peut atteindre). L'isolation container vs VM : le container partage le kernel hôte → l'isolation est moins forte qu'une VM (namespaces et cgroups vs virtualisation matérielle). Le container escape est rare mais possible. Bonnes pratiques : utilisateur non-root dans le container, read-only filesystem, pas de capabilities inutiles, secrets via volume sécurisé (pas dans l'image), réseau isolé, registry privé. Le **Docker socket** (/var/run/docker.sock) : si le socket est monté dans un container → l'attaquant peut créer des containers avec des privilèges complets sur l'hôte → full host compromise.

**Kubernetes** : pods (la plus petite unité — 1+ containers), deployments (gestion du cycle de vie des pods), services (exposition réseau des pods), namespaces (isolation logique), ConfigMaps (configuration), Secrets (données sensibles — encodées en base64, PAS chiffrées par défaut → utiliser un KMS externe), Ingress (exposition HTTP/HTTPS externe). La sécurité K8s : **RBAC** (Role-Based Access Control — le mécanisme d'autorisation ; risque : cluster-admin attribué à tout le monde), **Network Policies** (segmentation réseau entre pods — par défaut, tous les pods peuvent communiquer entre eux), **Pod Security Standards** (baseline/restricted — restreindre les capabilities, forcer le non-root). Les risques majeurs : API server exposé sur Internet sans authentification, RBAC trop permissif, secrets en clair dans les ConfigMaps, images non vérifiées, et mouvement latéral entre pods (sans Network Policies, compromettre un pod = accéder à tous les pods du cluster). Le **service mesh** (Istio, Linkerd) ajoute le mTLS automatique entre tous les services, le rate limiting, et l'observabilité — couche d'infrastructure sécurité pour les microservices.

---

#### Chapitre 28 — Architectures modernes : microservices, serverless et CI/CD

Les **microservices** : l'application est découpée en N services indépendants qui communiquent via API REST, gRPC, ou message queues. Chaque service a sa propre base de données et son propre cycle de déploiement. Avantage : scalabilité, résilience, agilité. Risque : surface d'attaque multipliée — chaque microservice est un point d'entrée potentiel, la communication inter-services doit être authentifiée et chiffrée.

Les **message brokers** : RabbitMQ (queue de messages AMQP — tâches asynchrones, découplage), Apache Kafka (streaming d'événements — big data, SIEM, événements temps réel), AWS SQS/Azure Service Bus (queues managées cloud). Risque : broker sans authentification ou avec des permissions trop larges → lecture/injection de messages.

Le **serverless** (AWS Lambda, Azure Functions, GCP Cloud Functions) : le développeur écrit une fonction, le provider gère tout le reste. Risques : permissions IAM trop larges sur les fonctions, injection dans les paramètres, secrets en variables d'environnement visibles dans la console.

Le **pipeline CI/CD** (Continuous Integration/Continuous Deployment) : GitHub Actions, GitLab CI, Jenkins, ArgoCD. Le pipeline compile, teste, et déploie le code automatiquement. C'est une **cible critique** : il a accès au code source, aux secrets de déploiement, et peut exécuter du code arbitraire. Supply chain attack via CI/CD : compromettre le pipeline = compromettre l'application en production (cf. cours APT — SolarWinds, 3CX).

**Git et sécurité** : les repos Git contiennent parfois des secrets commités par erreur (clés API, mots de passe, tokens). L'historique Git conserve tout — même un secret supprimé dans un commit ultérieur est récupérable (git log, git diff). Outils de détection : truffleHog, gitleaks, git-secrets.

---

### PARTIE VII — OPÉRATIONS, MONITORING ET CAS DE SYNTHÈSE

---

#### Chapitre 29 — Supervision, monitoring et automatisation

**SNMP** (Simple Network Management Protocol — supervision des équipements réseau, switches, routeurs, firewalls) : SNMPv1 et v2c utilisent des community strings comme mots de passe, en clair sur le réseau — si elles n'ont pas été changées (« public », « private »), un attaquant peut lire toute la configuration ou la modifier. SNMPv3 ajoute l'authentification et le chiffrement.

**Syslog** (centralisation des logs) : port 514 (UDP, historique — non fiable, pas de chiffrement) → port 6514 (TCP + TLS, recommandé). Format : facility (origine : auth, kern, mail) + severity (emerg→debug) + timestamp + hostname + message. La centralisation des logs est critique : un attaquant root peut effacer les logs locaux, mais pas les logs déjà envoyés au serveur syslog distant.

Les **NMS** (Network Monitoring Systems) : Nagios (historique, stable), Zabbix (plus moderne, interface web), Prometheus + Grafana (métriques + dashboards, cloud-native, containers), PRTG (supervision réseau, interface simple). La collecte de logs pour le SIEM : les sources à connecter (firewall, proxy, AD, endpoints/EDR, applications, cloud, email gateway) — la qualité de la détection SOC dépend de la qualité de la collecte. Le cours SOC couvre l'analyse ; le cours Infra couvre l'infrastructure de collecte.

**Automatisation et IaC** : **Ansible** (configuration management — agentless, SSH, playbooks YAML ; l'outil idéal pour le hardening automatisé — appliquer les CIS Benchmarks sur 100 serveurs en un playbook ; risque : playbooks avec secrets → Ansible Vault, inventaire = cartographie complète). **Terraform** (provisioning cloud — déclaratif, cloud-agnostic ; risque : state files avec secrets → backend chiffré). **Git** pour le versioning de tout (playbooks, configurations, documentation). L'automatisation comme outil de sécurité : hardening automatisé, déploiement de baseline, compliance as code.

---

#### Chapitre 30 — Cas complet : audit d'infrastructure et plan de hardening

Synthèse du fil rouge BACKBONE — l'audit complet de CargoPlex avec les livrables concrets d'un audit professionnel.

**Phase 1 — Cartographie :** inventaire des assets (187 serveurs dont 23 physiques et 164 VMs, 1 800 postes, 47 services exposés sur Internet, 3 SaaS non référencés), cartographie réseau (schéma annoté — flat network, pas de DMZ, vCenter et iLO accessibles depuis le LAN), inventaire des versions (8 serveurs Windows 2012 R2, 5 Ubuntu 18.04, ESXi 6.7 sur 3 hôtes), et cartographie des flux (API transporteurs en HTTP, FTP actif, LDAP anonymous bind).

**Phase 2 — Évaluation :** scan de vulnérabilités Nessus authentifié (347 vulnérabilités — 23 critiques, 67 élevées, 124 moyennes, 133 faibles — les critiques sont concentrées sur les serveurs legacy et le vCenter), audit de configuration CIS Benchmarks (score moyen 38 % — les écarts majeurs : SMBv1 actif, LLMNR actif, NTP désynchronisé, iLO credentials par défaut, vCenter mot de passe par défaut, pas de Sysmon, pas d'audit policy avancée), et pentest interne (mouvement latéral de l'accueil au DC en 4 heures : scan réseau → découverte iLO credentials par défaut → accès console serveur → credentials en mémoire → pass-the-hash → Domain Admin).

**Phase 3 — Matrice des écarts et priorisation :** matrice domaine × contrôle × état actuel × état cible × écart × priorité × effort × responsable.

**Phase 4 — Plan de hardening :**

**Quick wins 30 jours (P0)** : changer le mot de passe vCenter et tous les iLO/iDRAC (J1), déployer MFA sur tous les accès admin — VPN, RDP, vCenter, Azure (J7), désactiver SMBv1 et LLMNR/NBT-NS (J3), corriger les 23 vulnérabilités critiques (J14), synchroniser NTP sur une source unique (J2), sauvegardes hors domaine + test de restauration immédiat (J14), et désactiver LDAP anonymous bind (J3).

**Chantiers 3 mois (P1)** : segmentation réseau — créer les VLANs (admin, serveurs, utilisateurs, OT, guest) et les règles de filtrage inter-zones. Déployer le bastion Teleport (administration uniquement via le bastion). Créer le réseau de management dédié (vCenter, iLO, switches, firewalls — accessible uniquement depuis le bastion). Configurer DKIM + DMARC. Migrer l'API transporteurs en HTTPS + authentification individuelle par transporteur. Authentifier Redis. Sécuriser le pipeline GitLab CI (secrets dans le vault, pas en clair). Déployer Sysmon sur tous les serveurs Windows.

**Chantiers 6 mois (P2)** : migration des serveurs Windows Server 2012 R2 et Ubuntu 18.04. Hardening AD (tiering model, LAPS, Credential Guard, désactivation NTLM progressive). Déployer 802.1X sur les ports réseau des entrepôts. CSPM Azure (Defender for Cloud). Sauvegardes immuables (WORM). Renouvellement de l'AC interne et correction des templates AD CS vulnérables. Durcissement d'AD Connect (Tier 0, EDR, monitoring).

**Risques résiduels acceptés** : 2 serveurs Windows 2012 R2 supportant le WMS ne peuvent pas être migrés avant 12 mois (dépendance éditeur) — compensatoire : segmentation dédiée + monitoring renforcé + pas d'accès Internet. 1 protocole FTP maintenu temporairement pour 3 transporteurs qui ne supportent pas SFTP — compensatoire : VLAN isolé + logging complet + migration planifiée à 6 mois.

---

#### Chapitre 31 — Cas complet : investigation d'un incident sur une infrastructure hybride

Un affilié ransomware cible une infrastructure similaire à CargoPlex. **Vecteur d'accès** : exploitation d'une vulnérabilité Fortinet non patchée sur le VPN (CVE publiée 3 semaines avant, patch disponible mais non déployé — SLA critique 48h non respecté). **Mouvement latéral** : l'attaquant compromet un poste d'administration (pas de bastion, RDP direct depuis le VPN), dump les credentials avec Mimikatz (pas de Credential Guard), et utilise pass-the-hash pour se déplacer latéralement dans le flat network. **Escalade** : accès au vCenter avec le mot de passe par défaut (réseau de management non isolé), puis accès aux interfaces iLO (credentials par défaut). **Impact** : l'attaquant chiffre les VMs directement au niveau du datastore ESXi (variante Linux du ransomware — plus rapide et plus dévastateur que de chiffrer chaque VM individuellement). Les sauvegardes sur le NAS joint au domaine sont chiffrées en même temps.

**L'investigation** : logs VPN (accès initial — adresse IP source, timestamp, CVE exploitée), logs AD (mouvement latéral — Event 4624 type 10 RDP, Event 4672 privilèges spéciaux, Event 4769 Kerberos service ticket), logs Sysmon (exécution Mimikatz — Event 1 process creation avec hash connu, PsExec — Event 1 + Event 13 registre), logs firewall (C2 beaconing — connexions sortantes régulières vers une IP externe), logs vCenter (accès admin, opérations sur les VMs — mais les logs n'étaient pas envoyés au SIEM → reconstitution partielle depuis les logs locaux vCenter), et NTP désynchronisé (7 minutes d'écart entre les serveurs Windows et Linux → les timestamps des logs ne correspondent pas entre les sources → corrélation manuelle nécessaire, chronologie de l'intrusion reconstituée avec incertitude).

**La restauration** : les sauvegardes locales (NAS) sont chiffrées — inutilisables. Seules les sauvegardes cloud Azure (non jointes au domaine AD, dans un tenant séparé) sont intactes — mais elles ne couvrent que 40 % des systèmes (la migration cloud n'était pas terminée). RTO réel : 5 jours au lieu des 48h attendus. Perte de données : 3 jours de transactions ERP (RPO non respecté).

**Le retex** : chaque chapitre du cours compte. La segmentation (Ch.3) aurait limité la propagation. Le bastion (Ch.5) aurait empêché l'accès RDP direct. Le NTP synchronisé (Ch.6) aurait permis la corrélation des logs. Le hardening vSphere (Ch.8) aurait protégé le vCenter. Le patching dans les SLA (Ch.11) aurait fermé le vecteur initial. Les sauvegardes hors domaine et immuables (Ch.14) auraient permis la restauration. Le réseau de management isolé (Ch.2) aurait protégé les iLO et le vCenter. Et la collecte de logs centralisée (Ch.29) aurait permis la détection en heures, pas en jours.

---

### ANNEXES

---

#### Annexe A — Cheat sheet : protocoles et ports

| Protocole | Port | Chiffré | Usage | Risque principal |
|-----------|------|---------|-------|-----------------|
| HTTP | 80 | Non | Web | Données en clair, injection |
| HTTPS | 443 | Oui (TLS) | Web sécurisé | Certificat mal configuré |
| SSH | 22 | Oui | Administration à distance | Brute force, clés exposées |
| FTP | 21 | Non | Transfert de fichiers | Credentials en clair — obsolète |
| SFTP | 22 | Oui (SSH) | Transfert sécurisé | Remplace FTP |
| SMTP | 25/587/465 | Possible (TLS) | Envoi de mails | Open relay, phishing |
| IMAP | 143/993 | Possible (TLS) | Réception de mails | Credentials en clair (143) |
| POP3 | 110/995 | Possible (TLS) | Réception de mails | Credentials en clair (110) |
| DNS | 53 | Non (sauf DoH/DoT) | Résolution de noms | Spoofing, tunneling, exfiltration |
| LDAP | 389/636 | Possible (LDAPS) | Annuaire | Anonymous bind, clair |
| Kerberos | 88 | Oui | Authentification AD | Kerberoasting, Golden Ticket |
| SMB | 445 | Possible (SMBv3) | Partage fichiers Windows | EternalBlue (SMBv1) |
| NFS | 2049 | Non | Partage fichiers Unix | no_root_squash |
| RDP | 3389 | Oui (TLS) | Bureau à distance | Brute force, BlueKeep |
| SNMP | 161/162 | Non (v1/v2c) | Supervision réseau | Community strings par défaut |
| Syslog | 514/6514 | Possible (TLS) | Centralisation logs | UDP non fiable |
| RADIUS | 1812/1813 | Partiel | Auth réseau (WiFi, VPN) | Shared secret faible |
| TACACS+ | 49 | Oui | Auth équipements réseau | Moins répandu |
| MySQL | 3306 | Possible (TLS) | Base de données | Injection SQL |
| PostgreSQL | 5432 | Possible (TLS) | Base de données | Injection SQL, trust auth |
| SQL Server | 1433 | Possible (TLS) | Base de données MS | Injection SQL, xp_cmdshell |
| MongoDB | 27017 | Possible | Base NoSQL | Accès sans auth par défaut |
| Redis | 6379 | Non (par défaut) | Cache / sessions | Accès sans auth → RCE |
| Elasticsearch | 9200/9300 | Possible | Search / SIEM backend | Accès sans auth |
| iLO/iDRAC | 443 (HTTPS) | Oui | Admin serveur physique | Credentials par défaut |
| IPMI | 623 | Non | Admin serveur physique | Credentials par défaut, hash leak |
| vCenter | 443 (HTTPS) | Oui | Admin virtualisation | Credentials par défaut, CVE critiques |

---

#### Annexe B — Architecture type d'une entreprise

```
                            INTERNET
                               |
                      [ Firewall externe ]
                         [ + WAF/IPS ]
                               |
              +----------------+----------------+
              |                |                |
        [Reverse Proxy]   [Bastion/PAM]   [VPN Gateway]
        [ Nginx/HAProxy ] [Session rec.]  [OpenVPN/WG]
              |                |                |
              +----------------+----------------+
                               |
                      [ Firewall interne ]
                               |
    +--------+--------+-------+-------+--------+--------+
    |        |        |       |       |        |        |
  [Web]    [API]    [DB]   [AD/DC]  [SIEM]  [Mail]  [vCenter]
  [App]   [REST]  [SQL/No] [DNS]  [Splunk] [Exch]  [ESXi]
                  [Redis]  [Kerb]  [ELK]
    |        |        |       |       |        |        |
    +--------+--------+-------+-------+--------+--------+
                               |
                    [ Postes de travail ]
                      [ Endpoints + EDR ]

    --- Réseau de management (séparé) ---
    [iLO/iDRAC] [vCenter mgmt] [Switches admin] [Firewalls admin]
    → Accessible uniquement via le bastion
```

- **DMZ :** reverse proxy, bastion, VPN gateway — seuls points exposés
- **LAN :** serveurs applicatifs, bases de données, AD, SIEM, mail — jamais exposés directement
- **Réseau de management :** iLO/iDRAC, interfaces admin switches/firewalls, vCenter management — isolé, accessible via bastion uniquement
- **Segmentation :** deux firewalls séparent Internet → DMZ → LAN, filtrage à chaque niveau
- **SIEM :** reçoit les logs de toutes les briques — point central de détection

---

#### Annexe C — CIS Benchmarks : contrôles prioritaires par système

**Windows Server (top 10) :** désactiver SMBv1, désactiver LLMNR/NBT-NS, configurer audit policy avancée, déployer LAPS, activer Credential Guard, configurer AppLocker/WDAC, restreindre PowerShell (CLM), activer Windows Firewall sur tous les profils, désactiver les comptes invité/administrateur par défaut, configurer le verrouillage de compte.

**Linux (top 10) :** SSH — PasswordAuthentication no + PermitRootLogin no, désactiver les services inutiles (systemctl disable), configurer auditd, activer SELinux/AppArmor enforcing, configurer fail2ban, permissions 600 sur /etc/shadow, désactiver le core dump, configurer les umask, restreindre les binaires SUID, configurer le logging (rsyslog/journald → syslog central).

**VMware ESXi/vCenter :** mot de passe robuste ESXi et vCenter, désactiver SSH sur ESXi (sauf maintenance), réseau de management isolé, activer le lockdown mode, configurer le syslog vers le SIEM, limiter les accès vCenter (RBAC), nettoyer les snapshots, patcher les CVE ESXi/vCenter en priorité.

**Docker :** utiliser des images officielles et les scanner, exécuter les containers en non-root, filesystem read-only, ne pas monter le Docker socket, utiliser un registry privé, limiter les capabilities (--cap-drop ALL), configurer les user namespaces, ne pas utiliser --privileged.

---

#### Annexe D — OWASP Top 10 résumé

| # | Vulnérabilité | Description | Défense en 1 ligne |
|---|--------------|-------------|-------------------|
| A01 | Broken Access Control | Accès non autorisé (IDOR, privesc) | Défaut deny, vérification systématique côté serveur |
| A02 | Cryptographic Failures | Données non chiffrées | TLS partout, chiffrement au repos |
| A03 | Injection | SQL, OS, LDAP, NoSQL | Requêtes paramétrées, validation entrées |
| A04 | Insecure Design | Failles de conception | Threat modeling, security by design |
| A05 | Security Misconfiguration | Config par défaut, debug activé | Hardening, review, automatisation |
| A06 | Vulnerable Components | Dépendances avec CVE | SCA, mises à jour |
| A07 | Auth & Identification Failures | Auth faible, sessions mal gérées | MFA, rate limiting |
| A08 | Software & Data Integrity | Désérialisation, supply chain | Vérification d'intégrité, signatures |
| A09 | Logging & Monitoring Failures | Pas de logs, pas d'alertes | Logging de sécurité, centralisation |
| A10 | SSRF | Requêtes serveur vers cible contrôlée | Whitelist d'URLs, filtrage réseau |

---

#### Annexe E — Logs essentiels par technologie

| Technologie | Source de logs | Quoi surveiller | Normal | Suspect |
|------------|---------------|----------------|--------|---------|
| Windows Server | Security Event Log | Auth (4624, 4625), Priv (4672), Account (4720) | Connexions heures ouvrées, postes connus | Connexions nocturnes, brute force, comptes créés |
| Sysmon | Event 1, 3, 7, 11, 13 | Processus, réseau, DLL, fichiers, registre | Processus légitimes | PowerShell encodé, Mimikatz, PsExec |
| Linux | auth.log, auditd | SSH, sudo, processus | Connexions SSH clés, sudo habituel | Brute force SSH, sudo root inhabituel |
| Active Directory | Security 4769, 4768 | Kerberos TGS/TGT | Requêtes TGS normales | Kerberoasting (rafale 4769), AS-REP |
| Firewall | Logs deny/allow | Flux bloqués, flux autorisés | Trafic vers services connus | Deny sortant (C2), flux vers IP suspectes |
| DNS | Query logs | Résolutions de noms | Domaines légitimes | Domaines longs (tunneling), DGA, domaines suspects |
| Proxy | Access logs | URLs visitées, user-agents | Navigation web normale | Beaconing régulier, domaines C2 |
| vCenter | Audit events | Connexions, opérations VMs | Admin pendant heures ouvrées | Connexion nocturne, snapshot, clone |
| Email gateway | Mail logs | Entrants/sortants, pièces jointes | Flux email normal | Phishing, pièces jointes malveillantes |
| Cloud (Azure/AWS) | Sign-in, CloudTrail | Connexions, appels API | Connexions depuis pays habituels | Connexion depuis pays inhabituel, API sensibles |

---

#### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Infrastructure IT (ce cours) | **Ce cours (Infra)** | — |
| Détection SOC (SIEM, investigation) | **Cours SOC** | Infra (Ch.29 collecte logs, Ch.12-13 logs DB) |
| Incident Response | **Cours IR** | Infra (Ch.31 investigation incident infra) |
| CTI (menaces, acteurs) | **Cours CTI** | Infra (Ch.11 CISA KEV, Ch.4 VPN comme vecteur APT) |
| APT (acteurs étatiques) | **Cours APT** | Infra (Ch.8 virtualisation ciblée, Ch.22 GoldenSAML) |
| GRC (gouvernance, risques) | **Cours GRC** | Infra (Ch.9 CIS Benchmarks, Ch.11 politique patching) |
| Windows en profondeur | **Cours Windows** | Infra (Ch.7 vue d'ensemble, Ch.21 AD socle) |
| Active Directory | **Cours AD** | Infra (Ch.21 AD comme socle infra, Ch.6 AD CS) |
| Intelligence économique | **Cours IE** | Infra (Ch.14 sauvegardes comme résilience) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | Infra (Ch.8 ransomware ESXi) |
| OSINT | **Cours OSINT** | Infra (Ch.1 DNS recon, Ch.19 Swagger exposé) |

---

#### Annexe G — Glossaire et ressources

##### Glossaire (sélection)

| Terme | Définition |
|-------|-----------|
| **ACL** | Access Control List — liste de règles de filtrage |
| **AD CS** | Active Directory Certificate Services — PKI Microsoft |
| **API** | Application Programming Interface |
| **BOLA** | Broken Object Level Authorization — OWASP API #1 |
| **CA** | Certificate Authority — autorité de certification |
| **CDN** | Content Delivery Network |
| **CI/CD** | Continuous Integration / Continuous Deployment |
| **CSPM** | Cloud Security Posture Management |
| **DAS/NAS/SAN** | Direct/Network/Storage Area Network — types de stockage |
| **DHCP** | Dynamic Host Configuration Protocol |
| **DMZ** | Demilitarized Zone — zone tampon réseau |
| **ESXi** | Hyperviseur bare-metal VMware |
| **FDE** | Full Disk Encryption — chiffrement disque complet |
| **FIDO2** | Standard d'authentification résistant au phishing |
| **GPO** | Group Policy Object — politique de configuration AD |
| **IAM** | Identity and Access Management |
| **IaC** | Infrastructure as Code |
| **iDRAC/iLO/IPMI** | Interfaces d'administration de serveurs physiques |
| **JWT** | JSON Web Token — token autoportant signé |
| **LAPS** | Local Administrator Password Solution |
| **MFA** | Multi-Factor Authentication |
| **mTLS** | Mutual TLS — authentification mutuelle |
| **NAC** | Network Access Control |
| **NDR** | Network Detection and Response |
| **NGFW** | Next-Generation Firewall |
| **NTP** | Network Time Protocol |
| **OIDC** | OpenID Connect — authentification sur OAuth 2.0 |
| **PAM** | Privileged Access Management |
| **PFS** | Perfect Forward Secrecy |
| **PKI** | Public Key Infrastructure |
| **RAID** | Redundant Array of Independent Disks |
| **RBAC** | Role-Based Access Control |
| **SAML** | Security Assertion Markup Language — SSO XML |
| **TDE** | Transparent Data Encryption |
| **vCenter** | Console d'administration centralisée VMware |
| **VPC/VNet** | Virtual Private Cloud / Virtual Network |
| **WAF** | Web Application Firewall |
| **WORM** | Write Once Read Many — sauvegarde immuable |

##### Ressources

| Ressource | Type | Focus |
|-----------|------|-------|
| CIS Benchmarks | Guides | Hardening par système (gratuit) |
| ANSSI Guides | Guides | Durcissement Windows, Linux, AD (gratuit) |
| NIST SP 800-123 | Standard | Guide de sécurité des serveurs |
| OWASP | Projet | Top 10, API Security, Testing Guide |
| The DFIR Report | Blog | Intrusions analysées pas à pas |
| SANS Reading Room | Articles | Recherche en sécurité |
| Shodan | Outil | Moteur de recherche de services exposés |
| Nmap | Outil | Scanner de ports et de services |

##### Formations

| Formation | Organisme | Focus |
|-----------|----------|-------|
| CompTIA Network+ | CompTIA | Fondamentaux réseau |
| CompTIA Security+ | CompTIA | Fondamentaux sécurité |
| CCNA | Cisco | Réseau Cisco |
| CKA/CKS | CNCF | Kubernetes admin / sécurité |
| AWS SAA/SCS | AWS | Architecture / sécurité cloud |
| AZ-500 | Microsoft | Sécurité Azure |

---

---

## Annexe — Questions types d'entretien et réponses types

### Questions essentielles

- **Question :** Décrivez l'architecture réseau type d'une entreprise.
  - **Réponse type :** On a généralement un firewall externe côté Internet, puis une DMZ qui héberge les services exposés (reverse proxy, bastion, VPN), un firewall interne, et le LAN avec les serveurs, l'AD, les bases de données. Les postes utilisateurs sont dans un réseau séparé. On ajoute un réseau de management isolé pour l'administration des équipements. L'idée c'est la défense en profondeur avec des zones de confiance décroissante.

- **Question :** Pourquoi la segmentation réseau est-elle fondamentale ?
  - **Réponse type :** Sans segmentation, un attaquant qui compromet un poste utilisateur peut atteindre directement le contrôleur de domaine, le vCenter, les sauvegardes — le blast radius est maximal. La segmentation via VLANs et firewalls inter-zones limite le mouvement latéral. C'est la mesure la plus efficace contre la propagation d'un ransomware ou d'un attaquant dans le réseau.

- **Question :** Quels sont les mécanismes anti-phishing côté infrastructure email ?
  - **Réponse type :** Il y a trois enregistrements DNS complémentaires : SPF qui liste les serveurs autorisés à envoyer pour le domaine, DKIM qui signe les mails cryptographiquement, et DMARC qui définit la politique si SPF ou DKIM échoue — none, quarantine ou reject. Les trois sont indispensables et complémentaires. En plus, on met une email gateway qui analyse les URLs, sandboxe les pièces jointes, et réécrit les liens.

- **Question :** Expliquez la règle 3-2-1 des sauvegardes et les erreurs courantes.
  - **Réponse type :** 3 copies des données, sur 2 supports différents, dont 1 hors site. L'erreur la plus critique, c'est le NAS de sauvegarde joint au domaine AD — en cas de ransomware, les sauvegardes sont chiffrées avec le reste. Autres erreurs : pas de test de restauration, même compte admin partout, pas de sauvegardes immuables (WORM). Les sauvegardes doivent être isolées du réseau standard et régulièrement testées.

- **Question :** C'est quoi le Zero Trust et en quoi ça diffère du modèle traditionnel ?
  - **Réponse type :** Le modèle traditionnel fait confiance au réseau interne — une fois à l'intérieur du périmètre, on accède à tout. Le Zero Trust part du principe que personne n'est de confiance par défaut, même en interne. Chaque accès est vérifié : identité forte (MFA), état du poste (conformité), moindre privilège, micro-segmentation. Le VPN est remplacé par des solutions d'accès conditionnel. C'est particulièrement pertinent avec le télétravail et le cloud.

### Questions complémentaires

- **Question :** Quelle est la différence entre un firewall stateful et un NGFW ?
  - **Réponse type :** Le firewall stateful suit les connexions et filtre sur IP/port — il sait si un paquet fait partie d'une connexion initiée depuis l'intérieur. Le NGFW ajoute l'inspection applicative : il peut identifier les applications même sur des ports non standards, faire du filtrage URL, de l'IPS intégré, de l'inspection TLS, et du sandboxing. C'est le standard en entreprise aujourd'hui.

- **Question :** Pourquoi le management plane est-il critique et souvent négligé ?
  - **Réponse type :** Les interfaces d'administration — iLO, iDRAC, vCenter — permettent un contrôle total sur l'infrastructure physique, même si l'OS est éteint. Le problème c'est qu'elles sont souvent sur le même réseau que les utilisateurs, avec des mots de passe par défaut. Un attaquant qui y accède peut tout contrôler. La solution c'est un réseau de management dédié, accessible uniquement via le bastion.

- **Question :** Quelles différences entre OAuth, SAML et OIDC ?
  - **Réponse type :** SAML est le plus ancien, basé sur XML, utilisé pour le SSO d'entreprise vers des applications web. OAuth 2.0 est un protocole d'autorisation (pas d'authentification) — il délivre des tokens d'accès. OIDC est une couche d'authentification construite sur OAuth 2.0, basée sur JSON/JWT — c'est le standard moderne pour le SSO, utilisé par Google, Microsoft, etc.

### Questions les plus probables en entretien

1. Architecture réseau type d'entreprise ?
2. Pourquoi segmenter le réseau ?
3. SPF, DKIM, DMARC — à quoi ça sert ?
4. Règle 3-2-1 et erreurs de sauvegarde ?
5. C'est quoi le Zero Trust ?
6. Firewall stateful vs NGFW ?

### Réponses flash

- **Architecture réseau** → Internet → FW → DMZ → FW → LAN (serveurs, AD) + réseau management séparé.
- **Segmentation** → VLANs + filtrage inter-zones. Sans ça = flat network = blast radius maximal.
- **SPF/DKIM/DMARC** → SPF = serveurs autorisés. DKIM = signature. DMARC = politique. Les trois ensemble.
- **Sauvegardes** → 3-2-1. Immuable (WORM). Hors domaine AD. Tester la restauration.
- **Zero Trust** → Aucune confiance par défaut, vérification continue, MFA, moindre privilège, micro-segmentation.
- **NGFW** → Stateful + inspection applicative, filtrage URL, IPS, inspection TLS.
- **Management plane** → iLO/iDRAC/vCenter = contrôle total. Réseau dédié, jamais sur le LAN utilisateur.

---

> **Note de clôture**
>
> Ce cours a été conçu comme le socle technique de la bibliothèque — la cartographie du terrain sur lequel les analystes SOC détectent, les incident responders interviennent, les pentesters attaquent, et les architectes construisent.
>
> L'opération BACKBONE illustre une vérité opérationnelle : la majorité des compromissions n'exploitent pas des vulnérabilités exotiques — elles exploitent des fondamentaux négligés. Un mot de passe par défaut sur le vCenter. Un flat network sans segmentation. Un NAS de sauvegarde joint au domaine. Un NTP désynchronisé qui rend les logs inutilisables. Un iLO accessible depuis le réseau utilisateur. Un VPN non patché. Ce sont ces « détails » d'infrastructure qui font la différence entre une organisation résiliente et une organisation qui paye une rançon.
>
> Le cours assume une conviction : comprendre l'infrastructure est la compétence la plus fondamentale en cybersécurité. Avant de détecter, il faut savoir ce qui génère les logs. Avant de répondre, il faut savoir sur quoi on intervient. Avant d'auditer, il faut savoir ce qu'on regarde. Et avant de protéger, il faut savoir ce qu'on défend.
>
> *Comprendre le terrain • Cartographier les surfaces • Durcir les fondations — parce que la sécurité commence par l'infrastructure.*
