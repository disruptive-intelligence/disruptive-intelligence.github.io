---
title: "Logs et journaux"
cours:
  - library/it/linux/administration-linux/index.md
---

# Logs et journaux

Lire les journaux d'un service, filtrer par période et par gravité, retrouver les authentifications et l'usage de sudo.

Les incontournables : `journalctl -u` · `journalctl -f` · `journalctl --since` · `/var/log/auth.log` · `zgrep` · `dmesg -T`
{ .kw-cs-top }

## journalctl (systemd)

### Lire le journal d'un service

```bash title="Commande"
journalctl -u <service>   # -n N : N dernières lignes, --no-pager : sans pagination
```

```bash title="Exemple"
journalctl -u ssh --no-pager -n 3
```

??? example "Sortie"
    ```text
    Oct 02 09:12:01 srv-web-01 sshd[5123]: Accepted publickey for alice from 192.168.1.23 port 51544 ssh2
    Oct 02 09:12:01 srv-web-01 sshd[5123]: pam_unix(sshd:session): session opened for user alice(uid=1000)
    Oct 02 09:30:44 srv-web-01 sshd[5123]: pam_unix(sshd:session): session closed for user alice
    ```

Pour comprendre : [Administration Linux, ch. 15](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/03-chapitre-15-les-logs-et-journaux.md)
{ .kw-cs-meta }

### Suivre les journaux en direct

```bash title="Commande"
journalctl -f              # tout le système
journalctl -fu <service>   # un seul service
```

```bash title="Exemple"
journalctl -fu nginx
```

### Filtrer les journaux par période

```bash title="Commande"
journalctl --since "<début>" --until "<fin>"   # format AAAA-MM-JJ HH:MM
```

```bash title="Exemple"
journalctl --since "2026-10-01 08:00" --until "2026-10-01 12:00" -u cron --no-pager | head -2
```

??? example "Sortie"
    ```text
    Oct 01 08:17:01 srv-web-01 CRON[3301]: pam_unix(cron:session): session opened for user root(uid=0)
    Oct 01 08:17:01 srv-web-01 CRON[3302]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
    ```

```bash title="Exemple 2"
journalctl --since "1 hour ago" -p err   # erreurs de la dernière heure
```

### Voir seulement les erreurs depuis le démarrage

```bash title="Commande"
journalctl -p err -b   # -p gravité minimale, -b depuis le démarrage
```

```bash title="Exemple"
journalctl -p err -b --no-pager | tail -2
```

??? example "Sortie"
    ```text
    Oct 02 02:00:05 srv-web-01 backup-db.sh[2210]: mysqldump: Got error: 1045: Access denied for user 'backup'@'localhost'
    Oct 02 02:00:05 srv-web-01 systemd[1]: Failed to start backup-db.service - Sauvegarde de la base.
    ```

### Voir les messages du noyau

```bash title="Commande"
sudo dmesg -T   # -T : dates lisibles
```

```bash title="Exemple"
sudo dmesg -T | tail -2
```

??? example "Sortie"
    ```text
    [Thu Oct  2 01:12:44 2026] usb 1-1: new high-speed USB device number 3 using xhci_hcd
    [Thu Oct  2 01:12:45 2026] sd 2:0:0:0: [sdb] 30031872 512-byte logical blocks: (15.4 GB/14.3 GiB)
    ```

## Fichiers de /var/log

### Trouver les échecs de connexion

```bash title="Commande"
sudo grep "Failed password" /var/log/auth.log   # /var/log/secure sur RHEL
```

```bash title="Exemple"
sudo grep "Failed password" /var/log/auth.log | tail -2
```

??? example "Sortie"
    ```text
    Oct  2 03:11:06 srv-web-01 sshd[7781]: Failed password for invalid user admin from 203.0.113.7 port 40122 ssh2
    Oct  2 03:11:14 srv-web-01 sshd[7790]: Failed password for root from 203.0.113.7 port 40188 ssh2
    ```

```bash title="Exemple 2"
sudo grep "Failed password" /var/log/auth.log | grep -oE 'from [0-9.]+' | sort | uniq -c | sort -rn
# IP qui échouent le plus
```

Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

### Retrouver l'usage de sudo

```bash title="Commande"
sudo grep "COMMAND=" /var/log/auth.log   # ou journalctl _COMM=sudo
```

```bash title="Exemple"
sudo grep "COMMAND=" /var/log/auth.log | tail -1
```

??? example "Sortie"
    ```text
    Oct  2 09:14:37 srv-web-01 sudo:    alice : TTY=pts/0 ; PWD=/home/alice ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx
    ```

```bash title="Exemple 2"
journalctl _COMM=sudo --no-pager | tail
```

### Chercher dans les logs archivés (rotation)

```bash title="Commande"
zgrep "<motif>" /var/log/<journal>*   # -h : sans le nom du fichier
```

```bash title="Exemple"
sudo zgrep -c "Failed password" /var/log/auth.log*
```

??? example "Sortie"
    ```text
    /var/log/auth.log:137
    /var/log/auth.log.1:982
    /var/log/auth.log.2.gz:1204
    ```

### Voir la place prise par les journaux

```bash title="Commande"
journalctl --disk-usage   # journald
sudo du -sh /var/log/*     # fichiers de /var/log
```

```bash title="Exemple"
sudo du -sh /var/log/* | sort -h | tail -3
```

??? example "Sortie"
    ```text
    38M	/var/log/auth.log
    412M	/var/log/syslog
    1.2G	/var/log/journal
    ```

## Vue d'ensemble : quel journal pour quoi

| Fichier | Contenu |
|---|---|
| `/var/log/syslog` (Debian) · `/var/log/messages` (RHEL) | Journal général |
| `/var/log/auth.log` (Debian) · `/var/log/secure` (RHEL) | Authentifications, `sudo`, SSH |
| `/var/log/kern.log` | Noyau |
| `/var/log/wtmp` · `/var/log/btmp` | Connexions réussies (`last`) · échouées (`lastb`) |
| `/var/log/apt/history.log` | Paquets installés ou supprimés |
| `~/.bash_history` | Commandes d'un utilisateur (écrites à la déconnexion) |
