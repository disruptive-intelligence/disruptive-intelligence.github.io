---
title: "Tâches planifiées"
cours:
  - library/it/linux/administration-linux/index.md
---

# Tâches planifiées

Lister et créer des tâches cron, lire une ligne cron, créer un timer systemd, programmer une commande unique.

Les incontournables : `crontab -l` · `crontab -e` · `/etc/cron.*` · `systemctl list-timers` · `at`
{ .kw-cs-top }

## Cron

### Lister les tâches cron d'un utilisateur

```bash title="Commande"
crontab -l                           # les miennes
sudo crontab -l -u <utilisateur>     # celles d'un autre
```

```bash title="Exemple"
sudo crontab -l -u www-data
```

??? example "Sortie"
    ```text
    # m h  dom mon dow   command
    */5 * * * * /usr/bin/php /var/www/site/cron.php > /dev/null 2>&1
    ```

Pour comprendre : [Administration Linux, ch. 16](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/04-chapitre-16-taches-planifiees.md)
{ .kw-cs-meta }

### Ajouter une tâche cron

```bash title="Commande"
crontab -e   # une ligne = minute heure jour mois jour_semaine commande
```

```bash title="Exemple"
0 2 * * * /opt/scripts/sauvegarde.sh >> /var/log/sauvegarde.log 2>&1
# tous les jours à 2 h, sortie et erreurs dans un journal
```

!!! warning "Attention"
    cron a un environnement minimal : chemins absolus partout, et tester le script à la main d'abord.

### Voir toutes les tâches planifiées du système

```bash title="Commande"
ls -la /etc/cron.*    # dossiers cron du système
cat /etc/crontab      # crontab système
```

```bash title="Exemple"
sudo grep -R . /etc/cron* /var/spool/cron 2>/dev/null | grep -v '#'
```

??? example "Sortie"
    ```text
    /etc/cron.d/certbot:0 */12 * * * root test -x /usr/bin/certbot && certbot -q renew
    /etc/crontab:17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
    /var/spool/cron/crontabs/www-data:*/5 * * * * /usr/bin/php /var/www/site/cron.php
    ```

## systemd et at

### Lister les timers systemd

```bash title="Commande"
systemctl list-timers --all   # NEXT, LEFT, LAST, PASSED, UNIT
```

```bash title="Exemple"
systemctl list-timers --no-pager | head -3
```

??? example "Sortie"
    ```text
    NEXT                        LEFT        LAST                        PASSED     UNIT                ACTIVATES
    Thu 2026-10-02 10:39:00 UTC 18min       Thu 2026-10-02 10:09:00 UTC 11min ago  phpsessionclean.timer phpsessionclean.service
    Fri 2026-10-03 00:00:00 UTC 13h         Thu 2026-10-02 00:00:00 UTC 10h ago    logrotate.timer     logrotate.service
    ```

### Créer un timer systemd

```bash title="Commande"
sudo nano /etc/systemd/system/<nom>.timer   # lance <nom>.service, du même nom
```

```ini title="Exemple"
[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash title="Exemple 2"
sudo systemctl daemon-reload && sudo systemctl enable --now sauvegarde.timer
```

Ensuite : [créer un service pour un script](services.md#creer-un-service-pour-un-script)
{ .kw-cs-meta }

### Programmer une commande une seule fois

```bash title="Commande"
echo "<commande>" | at <heure>   # atq : tâches en attente, atrm : en supprimer
```

```bash title="Exemple"
echo "/opt/scripts/rapport.sh" | at 18:00
```

??? example "Sortie"
    ```text
    warning: commands will be executed using /bin/sh
    job 3 at Thu Oct  2 18:00:00 2026
    ```

```bash title="Exemple 2"
atq
```

## Vue d'ensemble : lire une ligne cron

```
┌ minute (0-59)
│ ┌ heure (0-23)
│ │ ┌ jour du mois (1-31)
│ │ │ ┌ mois (1-12)
│ │ │ │ ┌ jour de la semaine (0-7, 0 et 7 = dimanche)
* * * * * commande
```

| Ligne | Quand |
|---|---|
| `*/15 * * * *` | toutes les 15 minutes |
| `0 */6 * * *` | toutes les 6 heures |
| `0 0 * * 0` | chaque dimanche à minuit |
| `0 0 1 * *` | le 1er de chaque mois |
| `@reboot` | à chaque démarrage |
