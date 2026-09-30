---
title: Chapitre 8 — Acquisition des logs, des données d'identité et du cloud
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie II — Acquisition de preuves
  - index.md
---

## 8.1 Acquisition des Event Logs Windows

Les Event Logs Windows (format `.evtx`) sont stockés dans `C:\Windows\System32\winevt\Logs\`. Méthodes d'acquisition : copie directe des fichiers `.evtx` (possible sur une machine éteinte ou via un partage réseau), export via PowerShell (`wevtutil epl Security C:\export\Security.evtx`), collecte via KAPE (target `EventLogs` — collecte automatiquement tous les fichiers evtx), ou collecte centralisée depuis le SIEM (si les logs ont été envoyés à un SIEM, ils y sont préservés même si l'attaquant efface les logs locaux — c'est l'une des défenses les plus efficaces contre l'anti-forensics).

Les canaux critiques à collecter : Security (authentification, audit), System (services, pilotes), Application, PowerShell/Operational (script block logging — Event ID 4104), Microsoft-Windows-Sysmon/Operational (si Sysmon est déployé), Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational (RDP), et Microsoft-Windows-TaskScheduler/Operational (tâches planifiées).

## 8.2 Acquisition des logs Linux

Les logs Linux sont stockés dans `/var/log/` et via systemd-journald. Les fichiers clés : `auth.log` ou `secure` (authentifications, sudo, SSH), `syslog` (événements système), `kern.log` (événements noyau), les logs applicatifs (`/var/log/apache2/`, `/var/log/nginx/`, `/var/log/mysql/`), et les fichiers de session (`wtmp`, `btmp`, `lastlog`).

Pour le journald : `journalctl --since "2026-01-01" --until "2026-03-08" -o json > journal_export.json` exporte les logs systemd au format JSON, exploitable par les outils de timeline.

La collecte des historiques de commandes (`.bash_history`, `.zsh_history`) doit inclure non seulement les fichiers dans les home directories mais aussi la recherche dans la mémoire et les fichiers supprimés — l'attaquant supprime souvent son historique, mais des traces peuvent persister en mémoire, dans le swap, ou dans les secteurs non alloués du disque.

## 8.3 Acquisition des données Active Directory

L'AD est une source critique souvent sous-exploitée en forensic. Le fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) contient tous les objets AD (utilisateurs, groupes, GPO, ACL) et les hashes NTLM de tous les comptes. Son acquisition se fait via volume shadow copy (`vssadmin create shadow /for=C:`) puis copie du ntds.dit depuis le shadow, ou via `ntdsutil` en mode snapshot. L'analyse avec `secretsdump.py` (Impacket) ou DSInternals (PowerShell) permet d'extraire les hashes et de comprendre la compromission AD (Ch.20).

Les **logs de réplication AD** sont essentiels pour détecter le DCSync (Event ID 4662 avec les GUID de réplication). Les **métadonnées AD** (date de création et de modification des objets, via `repadmin /showmeta` ou ADRecon) révèlent les modifications récentes — comptes créés, groupes modifiés, GPO ajoutées.

**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD.

## 8.4 Acquisition des données cloud

**Microsoft 365 :** l'Unified Audit Log (UAL) est exportable via PowerShell (`Search-UnifiedAuditLog`) ou via le portail Purview Compliance. La rétention dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5). Le Sign-in Log est exportable via le portail Entra ID ou via l'API Microsoft Graph. L'eDiscovery permet de placer un **legal hold** sur des boîtes mail (préservation contre suppression) et d'exporter des données ciblées.

**AWS :** CloudTrail enregistre chaque appel API (exportable en JSON — `aws cloudtrail lookup-events`). Les VPC Flow Logs capturent les métadonnées réseau. Les S3 Access Logs tracent les accès aux buckets. Les EBS Snapshots permettent de capturer l'état d'un volume sans arrêter l'instance.

Les **limitations de rétention** sont un piège fréquent : si le dwell time dépasse la rétention des logs cloud, les premières actions de l'attaquant sont perdues. La vérification de la rétention effective (pas théorique) doit être faite dès le début de l'investigation.

## 8.5 Fil rouge — MUSIC BOX : les logs AD et cloud

> **🔬 MUSIC BOX — Épisode 8**
>
> Samedi 10h00. Claire lance la collecte des données d'identité et cloud.
>
> **AD :** Export des Event Logs Security et System de DC01 via PowerShell (wevtutil). Snapshot volume shadow copy de DC01 pour acquisition du ntds.dit. Exécution d'ADTimeline pour reconstituer la chronologie des modifications AD.
>
> **Cloud :** NovaPharma utilise AWS pour le stockage des données R&D (S3) et Microsoft 365 (E3) pour la messagerie. Export du UAL M365 via PowerShell (180 jours disponibles — suffisant pour couvrir la fenêtre J-60 à J). Export de CloudTrail AWS (90 jours par défaut, mais NovaPharma avait configuré un trail vers S3 avec rétention longue — les 12 derniers mois sont disponibles).
>
> Premier résultat CloudTrail : 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours (J-5 à J-1), depuis un rôle IAM légitime (`svc-backup-role`) mais utilisé depuis l'IP externe `103.xx.xx.xx` — le C2. Les access keys ont été exfiltrées du serveur R&D Linux par l'attaquant.

---
