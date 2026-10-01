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
journalctl -u <service>
```

```bash title="Exemple"
journalctl -u ssh --no-pager -n 50   # les 50 dernières lignes
```

Pour comprendre : [Administration Linux, ch. 15](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/03-chapitre-15-les-logs-et-journaux.md)
{ .kw-cs-meta }

### Suivre les journaux en direct

```bash title="Commande"
journalctl -f
```

```bash title="Exemple"
journalctl -fu nginx   # en direct, pour nginx seulement
```

### Filtrer les journaux par période

```bash title="Commande"
journalctl --since "<début>" --until "<fin>"
```

```bash title="Exemple"
journalctl --since "2026-10-01 08:00" --until "2026-10-01 12:00"
```

```bash title="Exemple 2"
journalctl --since "1 hour ago" -p err   # erreurs de la dernière heure
```

### Voir seulement les erreurs depuis le démarrage

```bash title="Commande"
journalctl -p err -b
```

```bash title="Exemple"
journalctl -p err -b --no-pager | tail -30
```

### Voir les messages du noyau

```bash title="Commande"
sudo dmesg -T
```

```bash title="Exemple"
sudo dmesg -T | tail -30   # matériel, disques, OOM killer
```

## Fichiers de /var/log

### Trouver les échecs de connexion

```bash title="Commande"
sudo grep "Failed password" /var/log/auth.log
```

```bash title="Exemple"
sudo grep "Failed password" /var/log/auth.log | tail
```

```bash title="Exemple 2"
sudo grep "Failed password" /var/log/auth.log | grep -oE 'from [0-9.]+' | sort | uniq -c | sort -rn
# IP qui échouent le plus
```

Pour comprendre : [Linux — prises de notes, investigation](../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

### Retrouver l'usage de sudo

```bash title="Commande"
sudo grep "COMMAND=" /var/log/auth.log
```

```bash title="Exemple"
sudo grep "COMMAND=" /var/log/auth.log | tail
```

```bash title="Exemple 2"
journalctl _COMM=sudo --no-pager | tail   # même chose depuis journald
```

### Chercher dans les logs archivés (rotation)

```bash title="Commande"
zgrep "<motif>" /var/log/<journal>*
```

```bash title="Exemple"
sudo zgrep -h "sudo:" /var/log/auth.log*   # fichiers .gz compris
```

### Voir la place prise par les journaux

```bash title="Commande"
journalctl --disk-usage
```

```bash title="Exemple"
sudo du -sh /var/log/* | sort -h
```

## Repères : quel journal pour quoi

| Fichier | Contenu |
|---|---|
| `/var/log/syslog` (Debian) · `/var/log/messages` (RHEL) | Journal général |
| `/var/log/auth.log` (Debian) · `/var/log/secure` (RHEL) | Authentifications, `sudo`, SSH |
| `/var/log/kern.log` | Noyau |
| `/var/log/wtmp` · `/var/log/btmp` | Connexions réussies (`last`) · échouées (`lastb`) |
| `/var/log/apt/history.log` | Paquets installés ou supprimés |
| `~/.bash_history` | Commandes d'un utilisateur (écrites à la déconnexion) |
