---
title: Partie II — Systèmes, virtualisation et hardening
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

*Les systèmes d'exploitation, les hyperviseurs et leur durcissement — la couche sur laquelle tout repose.*

---


## Chapitre 7 — Systèmes d'exploitation

Windows et Linux vue infrastructure

*Vue d'ensemble — les cours Windows et Linux de la bibliothèque traitent chaque OS en profondeur.*

### 7.1 Windows Server

Les rôles principaux : **AD DS** (Active Directory Domain Services — le cœur de l'identité, traité au Ch.21), **DNS** (résolution de noms, intégré à l'AD), **DHCP** (attribution d'adresses), **File Server** (partages SMB), **IIS** (serveur web Microsoft), **WSUS** (Windows Server Update Services — distribution des patches). Les versions et le cycle de vie : Windows Server 2012 R2 (fin de support octobre 2023 — plus de mises à jour de sécurité = risque critique), Windows Server 2016 (support étendu jusqu'en 2027), Windows Server 2019 et 2022 (versions actuelles). Les logs essentiels : Event Logs (Security — authentification, accès objets ; System — services, erreurs ; Application — applicatif), et Sysmon (Event ID 1 — création de processus, 3 — connexions réseau, 7 — chargement de DLL, 11 — création de fichiers, 13 — modification du registre — indispensable pour la détection, cf. cours SOC).

### 7.2 Linux Server

Les distributions enterprise : **RHEL/CentOS/Rocky/AlmaLinux** (entreprise, stabilité, support long), **Ubuntu Server** (le plus utilisé en cloud et en conteneurs), **Debian** (stabilité, communautaire). Le filesystem (/ = racine, /etc = configuration, /var/log = logs, /home = utilisateurs, /tmp = temporaire — world-writable, souvent utilisé par les attaquants pour déposer des outils). Les permissions (rwx, owner/group/others, SUID/SGID — des binaires SUID mal configurés = escalade de privilèges). Les processus et services (systemd — systemctl, journald). Les logs : journald (journal structuré systemd), syslog (/var/log/syslog ou /var/log/messages), auth.log (authentification — SSH, sudo), et auditd (audit kernel — syscalls, fichiers, exécutables, le pendant Linux de Sysmon).

La coexistence dans l'entreprise : la majorité des infrastructures sont mixtes — Windows pour l'AD, les applications métier, les postes de travail ; Linux pour les serveurs web, les bases de données, les containers, et les appliances réseau. L'analyste SOC et l'IR doivent maîtriser les deux.

---


## Chapitre 8 — Virtualisation

hyperviseurs, réseaux virtuels et sécurité

*La couche de virtualisation porte la quasi-totalité de l'infrastructure de beaucoup d'entreprises — si l'hyperviseur est compromis, tout le SI tombe.*

### 8.1 Les hyperviseurs

Les hyperviseurs **Type 1** (bare-metal — directement sur le hardware) : **VMware ESXi** (le plus répandu en entreprise, géré par vCenter Server), **Microsoft Hyper-V** (intégré à Windows Server, géré par SCVMM ou Windows Admin Center), **Proxmox VE** (open source, KVM + LXC, interface web), **KVM** (Kernel-based Virtual Machine — hyperviseur Linux natif, base de Proxmox et d'OpenStack). Les hyperviseurs **Type 2** (sur un OS hôte) : VirtualBox, VMware Workstation — pour le lab et le développement, pas pour la production. L'isolation entre VMs est matérielle (via le processeur — Intel VT-x/AMD-V) — plus solide qu'un container mais plus lourde en ressources.

### 8.2 L'architecture vSphere

**ESXi** est l'hyperviseur installé sur chaque serveur physique — il gère les VMs locales. **vCenter Server** est la console d'administration centralisée qui gère tous les ESXi d'un cluster — c'est le single point of control… et de compromission. Depuis vCenter, un administrateur peut créer, supprimer, migrer, snapshotter n'importe quelle VM. Si vCenter est compromis, l'attaquant contrôle l'ensemble du SI virtualisé.

### 8.3 Les réseaux virtuels

Les **vSwitches** (switches virtuels dans l'hyperviseur) connectent les VMs entre elles et avec le réseau physique. Les **port groups** définissent les VLANs virtuels. La segmentation réseau commence à l'hyperviseur : si les vSwitches sont mal configurés, des VMs de zones de sécurité différentes (DMZ et LAN, par exemple) peuvent communiquer directement via le vSwitch sans passer par le firewall. Les **distributed vSwitches** (vDS) étendent la configuration réseau sur tout le cluster vSphere.

### 8.4 Les fonctionnalités et leurs risques

Les **snapshots** capturent l'état complet d'une VM à un instant T (disque + mémoire). Pratiques pour les rollbacks avant un patch, mais un snapshot contient la mémoire vive avec potentiellement des credentials en clair (tickets Kerberos, tokens, mots de passe en mémoire). Les snapshots « oubliés » grossissent jusqu'à saturer le datastore — et chaque snapshot est une copie analysable par un attaquant. Les **templates** permettent le déploiement rapide de VMs pré-configurées — le risque : le template contient un compte admin local avec un mot de passe par défaut que personne ne change après clonage, ou des clés SSH pré-générées identiques sur toutes les VMs clonées. Les **datastores** sont les volumes de stockage partagés qui contiennent les fichiers des VMs (VMDK = disques virtuels, VMX = configuration). Si un attaquant accède au datastore, il peut copier, monter, et analyser n'importe quel disque virtuel.

### 8.5 Les risques majeurs

Le **vCenter exposé** avec un mot de passe par défaut ou faible est le scénario le plus critique : l'attaquant obtient le contrôle total de toute l'infrastructure virtualisée. Les CVE vCenter sont régulièrement exploitées (CVE-2021-21985, CVE-2023-34048 — exploitées par des APT et des groupes ransomware). Le **mot de passe root ESXi par défaut** est rarement changé dans beaucoup d'organisations. Le **VM escape** (s'échapper de la VM vers l'hyperviseur) est rare mais critique (CVE-2023-20867 VMware Tools). L'**administration centralisée compromise** crée un effet domino : vCenter compromis = accès à toutes les VMs = l'équivalent d'un Domain Admin mais pour l'infrastructure physique. Et les **groupes ransomware ciblent désormais directement ESXi** (variantes Linux de LockBit, BlackBasta, Royal qui chiffrent les VMDK sur les datastores — plus rapide et plus dévastateur que de chiffrer chaque VM individuellement).

### 8.6 Le hardening de la virtualisation

Mot de passe robuste et unique sur chaque ESXi et sur vCenter. MFA sur l'accès vCenter. Patching de l'hyperviseur en priorité (les CVE ESXi/vCenter sont exploitées dans les jours suivant la publication). Réseau de management dédié (vCenter et les interfaces ESXi accessibles uniquement depuis le réseau d'administration via le bastion — jamais depuis le réseau utilisateur). Désactivation des services inutiles sur ESXi (SSH désactivé sauf maintenance, shell interactif désactivé). Logging vers le SIEM (vCenter génère des logs d'audit — connexions, opérations sur les VMs, modifications de configuration). Nettoyage des snapshots (pas de snapshot de plus de 72h en production sauf justification documentée).

> **🔧 BACKBONE — Épisode 4**
>
> Lucas accède au vCenter de CargoPlex avec le mot de passe par défaut VMware (admin/VMware1!). Il constate : 12 snapshots « temporaires » dont le plus ancien date de 14 mois (2,1 To de stockage gaspillé), le réseau de management n'existe pas (vCenter accessible depuis les postes utilisateurs), 3 VMs de production sont encore sur ESXi 6.7 (fin de support), et aucun log vCenter n'est envoyé au SIEM. Il ajoute le hardening vSphere aux quick wins P0.

---


## Chapitre 9 — Hardening : durcir les systèmes et les services

Le hardening est la réduction de la surface d'attaque par la configuration sécurisée. Principes : désactiver ce qui n'est pas nécessaire, changer les configurations par défaut, appliquer le moindre privilège, mettre à jour. Les benchmarks de référence : **CIS Benchmarks** (guides détaillés par système — Windows Server, Linux, Docker, Kubernetes, VMware, cloud — chaque recommandation avec justification et commande d'implémentation), **guides ANSSI** (recommandations de durcissement — Active Directory, Linux, Windows).

**Hardening Windows** : désactivation de SMBv1 (EternalBlue), désactivation de LLMNR et NBT-NS (résolution de noms broadcast → poisoning → capture de hashes NTLM), PowerShell Constrained Language Mode (limite les commandes PowerShell disponibles aux utilisateurs), AppLocker ou WDAC (contrôle d'exécution — seuls les exécutables autorisés peuvent s'exécuter), audit policy avancée (Event Logs détaillés), Sysmon déployé et configuré (cf. cours SOC), LAPS (Local Administrator Password Solution — mot de passe admin local unique et roté sur chaque poste, stocké dans l'AD), Credential Guard (isolation des credentials en mémoire — empêche Mimikatz).

**Hardening Linux** : SSH hardening (PasswordAuthentication no, PermitRootLogin no, port non standard, AllowUsers/AllowGroups), désactivation des services inutiles (systemctl disable), permissions des fichiers (chmod 600 sur les fichiers sensibles, pas de world-writable sauf /tmp), SELinux/AppArmor (contrôle d'accès obligatoire — MAC), auditd (monitoring des syscalls, fichiers, exécutables), fail2ban (blocage automatique après N tentatives échouées).

**Hardening des services** : serveurs web (headers de sécurité, version masquée, directory listing désactivé — cf. Ch.17), bases de données (authentification obligatoire, bind sur 127.0.0.1 sauf nécessité, audit activé — cf. Ch.12-13), DNS (zone transfers restreints, recursion limitée).

---


## Chapitre 10 — Cryptographie : les fondamentaux pour l'infrastructure

**Chiffrement symétrique** (AES-256 — même clé pour chiffrer et déchiffrer, rapide, utilisé pour les données au repos et le trafic en transit ; le problème : comment transmettre la clé de manière sécurisée ?). **Chiffrement asymétrique** (RSA, ECC — paire clé publique/clé privée ; la clé publique chiffre, la clé privée déchiffre ; lent, utilisé pour l'échange de clés et la signature numérique ; le fondement de TLS et SSH). **Hachage** (SHA-256, SHA-3 — empreinte irréversible de taille fixe, utilisée pour vérifier l'intégrité des fichiers et les signatures ; bcrypt, Argon2 — fonctions de hachage adaptatives pour les mots de passe, conçues pour être lentes → résistantes au brute force ; MD5 et SHA-1 sont obsolètes — collisions démontrées, ne plus utiliser).

**PKI** (Public Key Infrastructure — l'infrastructure de confiance pour les certificats) : les autorités de certification (CA) émettent des certificats qui lient une identité à une clé publique. La chaîne de confiance (Root CA → Intermediate CA → certificat serveur). La révocation (CRL — Certificate Revocation List, OCSP — Online Certificate Status Protocol). Let's Encrypt et l'automatisation ACME (certificats gratuits, renouvelés automatiquement).

**Certificats X.509** : SAN (Subject Alternative Name — un certificat peut couvrir plusieurs domaines), wildcard (*.example.com), durée de validité (90 jours Let's Encrypt, 1 an maximum pour les CA commerciales). Erreurs courantes : certificats expirés en production (alerte ignorée → les utilisateurs cliquent « continuer » → perte de l'habitude de vérifier les certificats), certificats auto-signés en production (pas de chaîne de confiance vérifiable), clés privées stockées sur le serveur web sans protection.

**Chiffrement au repos** : FDE (Full Disk Encryption — BitLocker sur Windows, LUKS sur Linux), TDE (Transparent Data Encryption — chiffrement de la base de données au niveau du moteur), chiffrement de fichiers. **Chiffrement en transit** : TLS 1.2/1.3 (le handshake — échange de clés via asymétrique, trafic chiffré via symétrique ; cipher suites — combinaisons d'algorithmes ; PFS — Perfect Forward Secrecy — même si la clé privée est compromise plus tard, les sessions passées restent protégées), mTLS (authentification mutuelle — le client ET le serveur présentent un certificat, utilisé entre microservices et dans les architectures Zero Trust).

---


## Chapitre 11 — Gestion des vulnérabilités et patching

Le cycle de vie d'une vulnérabilité : découverte (chercheur, vendor, attaquant) → attribution CVE (MITRE) → publication d'un advisory (vendor, CERT) → publication d'un patch → déploiement → vérification. La fenêtre entre la publication de l'advisory et le déploiement du patch est la surface d'attaque — les APT exploitent les CVE dans les heures suivant la publication (cf. cours APT Ch.3 — Ivanti, Fortinet, Citrix).

Le scoring : **CVSS** (Common Vulnerability Scoring System — Base score 0-10 + Temporal + Environmental ; les limites : un CVSS 9.8 sur un système isolé sans données sensibles est moins urgent qu'un CVSS 7.5 sur le contrôleur de domaine), **EPSS** (Exploit Prediction Scoring System — probabilité qu'une vulnérabilité soit exploitée dans les 30 prochains jours — plus opérationnel que le CVSS seul), **CISA KEV** (Known Exploited Vulnerabilities — la liste des vulnérabilités activement exploitées in the wild, la priorité absolue indépendamment du CVSS).

Les outils de scan : **Nessus/Tenable** (le plus répandu), **Qualys** (cloud-native), **OpenVAS** (open source). Scan authentifié (avec des credentials — voit les vulnérabilités internes, les patches manquants, les configurations) vs non authentifié (depuis l'extérieur — voit ce qu'un attaquant voit). Le processus de patching : WSUS/SCCM/Intune pour Windows, apt/yum pour Linux, Ansible pour l'automatisation multi-plateforme. SLA par criticité : critique < 48h, élevé < 15 jours, moyen < 30 jours, faible trimestriel. La gestion des assets end-of-life (les Windows Server 2012 de CargoPlex : pas de patch disponible → seules options : isoler, surveiller, et migrer).

---
