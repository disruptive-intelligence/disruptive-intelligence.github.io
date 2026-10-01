---
title: Chapitre 15 — Linux forensics
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

## 15.1 Les particularités du forensic Linux

Linux est omniprésent en serveur (web, base de données, stockage, cloud) mais ses artefacts forensic sont moins riches et moins standardisés que ceux de Windows. Il n'y a pas d'équivalent du Prefetch, de l'Amcache, ou des ShellBags. L'investigation Linux repose davantage sur les logs système, les historiques de commandes, les tâches planifiées, et l'analyse du système de fichiers ext4.

## 15.2 Artefacts système Linux

**auth.log / secure** (`/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` sur RHEL/CentOS) : chaque authentification (login, sudo, SSH, su) est enregistrée. Les connexions SSH montrent l'IP source, le compte utilisé, et le résultat (accepté/refusé). Les commandes sudo montrent quelle commande a été exécutée par quel utilisateur.

**wtmp / btmp / lastlog** : fichiers binaires enregistrant les sessions utilisateur. `wtmp` contient les connexions réussies (lisible avec la commande `last`). `btmp` contient les tentatives échouées (lisible avec `lastb`). `lastlog` contient la dernière connexion de chaque utilisateur.

**bash_history / zsh_history** (`~/.bash_history`, `~/.zsh_history`) : historique des commandes exécutées. C'est souvent la source la plus directement exploitable — l'attaquant peut y avoir laissé ses commandes de reconnaissance, de mouvement latéral, et d'exfiltration. Le piège : l'attaquant supprime souvent son historique (`history -c`, `rm ~/.bash_history`), mais des traces peuvent persister en mémoire (dans le dump RAM), dans le swap, ou dans les secteurs non alloués du disque (le fichier supprimé peut être récupéré si le disque est un HDD).

**journald** (systemd) : le journal système de systemd, exploitable avec `journalctl`. Plus structuré que syslog, il inclut des métadonnées riches (PID, UID, unité systemd). Exportable en JSON pour l'analyse : `journalctl --since "2026-01-01" -o json > journal.json`.

**crontab et systemd timers** : les tâches planifiées sont un mécanisme de persistance courant sous Linux. Les crontab utilisateur (`crontab -l -u <user>`) et système (`/etc/crontab`, `/etc/cron.d/`) doivent être vérifiés. Les systemd timers (`.timer` + `.service` dans `/etc/systemd/system/`) sont une alternative plus moderne.

## 15.3 Investigation serveur web et conteneurs

Les **logs Apache/Nginx** (`/var/log/apache2/access.log`, `/var/log/nginx/access.log`) sont essentiels pour l'investigation de compromission de serveur web. La détection de webshells (fichiers PHP/ASP déposés par l'attaquant pour maintenir un accès distant) passe par l'analyse des requêtes POST vers des fichiers inhabituels, l'identification de user-agents suspects, et la recherche de fichiers récemment créés dans les répertoires web.

Les **conteneurs Docker** posent des défis spécifiques : l'éphémérité des conteneurs (un conteneur détruit emporte ses données), la superposition des layers (le filesystem du conteneur est une superposition de couches en lecture seule + une couche en lecture/écriture), et l'absence de logs centralisés par défaut. L'investigation de conteneurs passe par l'examen des layers (`docker history`, `docker inspect`), des logs (`docker logs`), et des volumes montés. Sans logs externalisés vers un SIEM ou un système de log centralisé, le forensic de conteneurs est souvent impossible.

## 15.4 Outils Linux forensics

**The Sleuth Kit / Autopsy** supporte ext4. **extundelete** et **ext4magic** permettent la récupération de fichiers supprimés sur ext4 (avec des limitations — ext4 réinitialise les pointeurs d'inode). **Plaso** (log2timeline) supporte les artefacts Linux (syslog, wtmp, bash_history, etc.). Les outils de la suite Eric Zimmerman ne sont pas disponibles nativement sous Linux (ils sont conçus pour les artefacts Windows), mais ils fonctionnent via Wine ou sur une station Windows.

## 15.5 Fil rouge — MUSIC BOX : le serveur R&D Linux

> **🔬 MUSIC BOX — Épisode 14**
>
> L'investigation de SRV-RD-01 (Ubuntu 22.04, serveur de données R&D) révèle :
>
> **auth.log :** connexion SSH réussie depuis WKS-RD-047 (IP interne 10.xx.xx.47) avec le compte `svc-backup` à J-28, J-21, J-14, J-7, et J-1. Le compte `svc-backup` avait un authorized_key SSH ajouté par l'attaquant à J-30 — c'est le mécanisme de persistance sur le serveur Linux.
>
> **bash_history :** l'attaquant a exécuté `find /opt/research/molecule-np427 -name "*.xlsx" -o -name "*.pdf" -o -name "*.docx"` (reconnaissance des fichiers de recherche), puis `tar czf /tmp/research_backup.tar.gz /opt/research/molecule-np427/` (staging des données pour exfiltration), puis `rm -f /tmp/research_backup.tar.gz` (nettoyage après exfiltration — mais le fichier tar apparaît dans les secteurs non alloués du disque, récupérable par carving).
>
> **authorized_keys :** une clé SSH non autorisée a été ajoutée dans `/home/svc-backup/.ssh/authorized_keys` à J-30 — la clé publique est différente de celles des administrateurs légitimes. C'est le mécanisme de persistance.

---
