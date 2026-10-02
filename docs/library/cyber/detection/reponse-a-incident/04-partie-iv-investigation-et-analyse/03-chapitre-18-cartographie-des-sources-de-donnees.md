---
title: Chapitre 18 — Cartographie des sources de données
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation et analyse
  - index.md
---

*Ce chapitre est un référentiel : il recense et décrit les sources de données disponibles pour l'investigation IR, avec leurs forces, leurs limites, et leur localisation. Il ne traite pas de l'analyse concrète des artefacts (c'est l'objet des Ch.19-22) mais de la cartographie de ce qui existe et de ce qu'on peut en attendre.*

## 18.1 Sources endpoint (Windows)

Les **Windows Event Logs** sont la source primaire pour l'investigation Windows. Les Event IDs critiques pour l'IR sont référencés en Annexe D avec leur interprétation détaillée. Les catégories les plus importantes : Security (authentification 4624/4625, privilèges 4672, création de processus 4688, création de compte 4720, modification de groupe 4728/4732), System (installation de service 7045), PowerShell (script block logging 4104, module logging 4103), Sysmon (si déployé — fournit une granularité très supérieure aux Event Logs natifs : création de processus avec hash et ligne de commande, connexions réseau par processus, chargement de DLL).

Les **artefacts forensic Windows** incluent le Prefetch (historique des exécutions de programmes), l'Amcache et le ShimCache (historique des programmes exécutés avec hash), la MFT et le USN Journal (journal du système de fichiers — création, modification, suppression), le registre (persistence, configuration, activité utilisateur), le SRUM (consommation réseau par processus), et les Jump Lists et Shellbags (activité de navigation dans l'explorateur). Ces artefacts sont détaillés au Ch.19.

Les **logs EDR** fournissent une telemetry riche et centralisée : exécution de processus avec arbre de parenté, connexions réseau par processus, modifications système, et détections comportementales. La rétention varie selon l'EDR (typiquement 7 à 90 jours selon la licence).

## 18.2 Sources endpoint (Linux)

Les fichiers de log système (`/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog`), les journaux d'authentification (`wtmp`, `btmp`, `lastlog`), les historiques de commandes (`bash_history`, `zsh_history`), les tâches planifiées (`crontab`, `systemd timers`), et les fichiers de configuration modifiés récemment.

## 18.3 Sources réseau

Les logs pare-feu (flux autorisés et refusés, volumes, destinations), les logs proxy (URLs visitées, user-agents, volumes de données sortantes, codes de retour HTTP), les logs DNS (résolutions vers des domaines suspects, patterns DGA, tunneling DNS), les logs VPN (connexions, géolocalisation, durée), le NetFlow (profils de communication entre IP internes et externes, volumes), et les PCAP (captures complètes de paquets — si le NDR ou une capacité de capture existe).

## 18.4 Sources Active Directory

Les Event Logs des contrôleurs de domaine (authentification, réplication, modifications d'objets), les logs d'Azure AD Connect (si synchronisation hybride), et les métadonnées AD (date de création et de modification des objets, membres des groupes, ACL, GPO).

## 18.5 Sources cloud

Microsoft 365 : Unified Audit Log (rétention variable selon licence), Sign-in Logs (Entra ID), Azure Activity Log, Mailbox Audit Log. AWS : CloudTrail (API calls), VPC Flow Logs, S3 Access Logs. GCP : Cloud Audit Logs, VPC Flow Logs. Azure IaaS : Activity Log, NSG Flow Logs.

## 18.6 Sources externes

Les feeds de threat intelligence (IoC partagés par la communauté), les bases de malware (VirusTotal, MalwareBazaar, ANY.RUN), les rapports d'éditeurs CTI (Mandiant, CrowdStrike, Recorded Future, Secureworks), et les notifications du CERT-FR.

## 18.7 Fil rouge — BLACKTIDE : les sources mobilisées

> **🔍 BLACKTIDE — Épisode 18**
>
> Sources disponibles et exploitées : EDR CrowdStrike Falcon (telemetry 90 jours sur 92 % du parc), SIEM Splunk (9 mois de rétention — Event Logs Windows, proxy Squid, DNS Infoblox, pare-feu Palo Alto, VPN Fortinet), logs VPN Fortinet (180 jours), logs pare-feu Palo Alto (12 mois), Microsoft 365 UAL (180 jours — licence E3).
>
> Sources manquantes : pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu — pas de capture de paquets, pas de détection de beaconing sur le trafic chiffré). Pas de Sysmon (les Event Logs natifs sont moins granulaires). PowerShell script block logging activé sur les serveurs mais pas sur les postes de travail (angle mort sur l'exécution de scripts sur les postes).

---
