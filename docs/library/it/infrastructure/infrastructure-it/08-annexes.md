---
title: Annexes
source: IT/06 Infrastructure & architecture/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

---


## Annexe A — Cheat sheet : protocoles et ports

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


## Annexe B — Architecture type d'une entreprise

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


## Annexe C — CIS Benchmarks : contrôles prioritaires par système

**Windows Server (top 10) :** désactiver SMBv1, désactiver LLMNR/NBT-NS, configurer audit policy avancée, déployer LAPS, activer Credential Guard, configurer AppLocker/WDAC, restreindre PowerShell (CLM), activer Windows Firewall sur tous les profils, désactiver les comptes invité/administrateur par défaut, configurer le verrouillage de compte.

**Linux (top 10) :** SSH — PasswordAuthentication no + PermitRootLogin no, désactiver les services inutiles (systemctl disable), configurer auditd, activer SELinux/AppArmor enforcing, configurer fail2ban, permissions 600 sur /etc/shadow, désactiver le core dump, configurer les umask, restreindre les binaires SUID, configurer le logging (rsyslog/journald → syslog central).

**VMware ESXi/vCenter :** mot de passe robuste ESXi et vCenter, désactiver SSH sur ESXi (sauf maintenance), réseau de management isolé, activer le lockdown mode, configurer le syslog vers le SIEM, limiter les accès vCenter (RBAC), nettoyer les snapshots, patcher les CVE ESXi/vCenter en priorité.

**Docker :** utiliser des images officielles et les scanner, exécuter les containers en non-root, filesystem read-only, ne pas monter le Docker socket, utiliser un registry privé, limiter les capabilities (--cap-drop ALL), configurer les user namespaces, ne pas utiliser --privileged.

---


## Annexe D — OWASP Top 10 résumé

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


## Annexe E — Logs essentiels par technologie

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


## Annexe F — Mapping de la bibliothèque

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


## Annexe G — Glossaire et ressources

### Glossaire (sélection)

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

### Ressources

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

### Formations

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
