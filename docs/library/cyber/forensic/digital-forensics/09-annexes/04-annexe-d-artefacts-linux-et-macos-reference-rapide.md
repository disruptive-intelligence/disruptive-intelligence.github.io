---
title: 'Annexe D — Artefacts Linux et macOS : référence rapide'
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Annexes
  - index.md
---

## Linux

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| auth.log / secure | `/var/log/auth.log` ou `/var/log/secure` | grep, Plaso | Authentifications SSH, sudo, su |
| wtmp / btmp | `/var/log/wtmp`, `/var/log/btmp` | `last`, `lastb` | Sessions utilisateur (réussies / échouées) |
| lastlog | `/var/log/lastlog` | `lastlog` | Dernière connexion de chaque utilisateur |
| bash_history | `~/.bash_history` | cat, Plaso | Commandes exécutées (si non supprimé) |
| journald | `/var/log/journal/` | `journalctl` | Journal système structuré (systemd) |
| crontab | `/var/spool/cron/`, `/etc/crontab`, `/etc/cron.d/` | cat | Tâches planifiées (persistance) |
| SSH authorized_keys | `~/.ssh/authorized_keys` | cat | Clés SSH autorisées (persistance) |
| Apache/Nginx logs | `/var/log/apache2/`, `/var/log/nginx/` | grep, GoAccess | Requêtes web (détection webshell, injection) |

## macOS

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| Unified Logging | `/var/db/diagnostics/` | `log show`, Unified Log Parser | Tout : processus, réseau, système, apps |
| FSEvents | `.fseventsd/` (racine volume) | FSEventsParser, mac_apt | Modifications du système de fichiers |
| KnowledgeC.db | `~/Library/Application Support/Knowledge/` | APOLLO, mac_apt | Activité utilisateur (apps, durée, réseau) |
| Spotlight metadata | `.Spotlight-V100/` | mdls, mac_apt | Métadonnées de tous les fichiers indexés |
| TCC.db | `~/Library/Application Support/com.apple.TCC/` | sqlite3 | Permissions d'accès (caméra, micro, fichiers) |
| LaunchAgents/Daemons | `~/Library/LaunchAgents/`, `/Library/LaunchDaemons/` | plutil | Persistence (programmes au démarrage) |
| Keychain | `~/Library/Keychains/` | security (CLI) | Credentials stockés (avec autorisation) |
| Safari | `~/Library/Safari/` | mac_apt, Autopsy | Historique, downloads, tabs ouvertes |

---
