---
title: Partie VII — Opérations, monitoring ET cas de synthèse
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

---


## Chapitre 29 — Supervision, monitoring et automatisation

**SNMP** (Simple Network Management Protocol — supervision des équipements réseau, switches, routeurs, firewalls) : SNMPv1 et v2c utilisent des community strings comme mots de passe, en clair sur le réseau — si elles n'ont pas été changées (« public », « private »), un attaquant peut lire toute la configuration ou la modifier. SNMPv3 ajoute l'authentification et le chiffrement.

**Syslog** (centralisation des logs) : port 514 (UDP, historique — non fiable, pas de chiffrement) → port 6514 (TCP + TLS, recommandé). Format : facility (origine : auth, kern, mail) + severity (emerg→debug) + timestamp + hostname + message. La centralisation des logs est critique : un attaquant root peut effacer les logs locaux, mais pas les logs déjà envoyés au serveur syslog distant.

Les **NMS** (Network Monitoring Systems) : Nagios (historique, stable), Zabbix (plus moderne, interface web), Prometheus + Grafana (métriques + dashboards, cloud-native, containers), PRTG (supervision réseau, interface simple). La collecte de logs pour le SIEM : les sources à connecter (firewall, proxy, AD, endpoints/EDR, applications, cloud, email gateway) — la qualité de la détection SOC dépend de la qualité de la collecte. Le cours SOC couvre l'analyse ; le cours Infra couvre l'infrastructure de collecte.

**Automatisation et IaC** : **Ansible** (configuration management — agentless, SSH, playbooks YAML ; l'outil idéal pour le hardening automatisé — appliquer les CIS Benchmarks sur 100 serveurs en un playbook ; risque : playbooks avec secrets → Ansible Vault, inventaire = cartographie complète). **Terraform** (provisioning cloud — déclaratif, cloud-agnostic ; risque : state files avec secrets → backend chiffré). **Git** pour le versioning de tout (playbooks, configurations, documentation). L'automatisation comme outil de sécurité : hardening automatisé, déploiement de baseline, compliance as code.

---


## Chapitre 30 — Cas complet

audit d'infrastructure et plan de hardening

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


## Chapitre 31 — Cas complet

investigation d'un incident sur une infrastructure hybride

Un affilié ransomware cible une infrastructure similaire à CargoPlex. **Vecteur d'accès** : exploitation d'une vulnérabilité Fortinet non patchée sur le VPN (CVE publiée 3 semaines avant, patch disponible mais non déployé — SLA critique 48h non respecté). **Mouvement latéral** : l'attaquant compromet un poste d'administration (pas de bastion, RDP direct depuis le VPN), dump les credentials avec Mimikatz (pas de Credential Guard), et utilise pass-the-hash pour se déplacer latéralement dans le flat network. **Escalade** : accès au vCenter avec le mot de passe par défaut (réseau de management non isolé), puis accès aux interfaces iLO (credentials par défaut). **Impact** : l'attaquant chiffre les VMs directement au niveau du datastore ESXi (variante Linux du ransomware — plus rapide et plus dévastateur que de chiffrer chaque VM individuellement). Les sauvegardes sur le NAS joint au domaine sont chiffrées en même temps.

**L'investigation** : logs VPN (accès initial — adresse IP source, timestamp, CVE exploitée), logs AD (mouvement latéral — Event 4624 type 10 RDP, Event 4672 privilèges spéciaux, Event 4769 Kerberos service ticket), logs Sysmon (exécution Mimikatz — Event 1 process creation avec hash connu, PsExec — Event 1 + Event 13 registre), logs firewall (C2 beaconing — connexions sortantes régulières vers une IP externe), logs vCenter (accès admin, opérations sur les VMs — mais les logs n'étaient pas envoyés au SIEM → reconstitution partielle depuis les logs locaux vCenter), et NTP désynchronisé (7 minutes d'écart entre les serveurs Windows et Linux → les timestamps des logs ne correspondent pas entre les sources → corrélation manuelle nécessaire, chronologie de l'intrusion reconstituée avec incertitude).

**La restauration** : les sauvegardes locales (NAS) sont chiffrées — inutilisables. Seules les sauvegardes cloud Azure (non jointes au domaine AD, dans un tenant séparé) sont intactes — mais elles ne couvrent que 40 % des systèmes (la migration cloud n'était pas terminée). RTO réel : 5 jours au lieu des 48h attendus. Perte de données : 3 jours de transactions ERP (RPO non respecté).

**Le retex** : chaque chapitre du cours compte. La segmentation (Ch.3) aurait limité la propagation. Le bastion (Ch.5) aurait empêché l'accès RDP direct. Le NTP synchronisé (Ch.6) aurait permis la corrélation des logs. Le hardening vSphere (Ch.8) aurait protégé le vCenter. Le patching dans les SLA (Ch.11) aurait fermé le vecteur initial. Les sauvegardes hors domaine et immuables (Ch.14) auraient permis la restauration. Le réseau de management isolé (Ch.2) aurait protégé les iLO et le vCenter. Et la collecte de logs centralisée (Ch.29) aurait permis la détection en heures, pas en jours.

---
