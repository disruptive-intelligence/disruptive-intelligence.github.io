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
crontab -l
sudo crontab -l -u <utilisateur>
```

```bash title="Exemple"
sudo crontab -l -u www-data
```

Pour comprendre : [Administration Linux, ch. 16](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/04-chapitre-16-taches-planifiees.md)
{ .kw-cs-meta }

### Ajouter une tâche cron

```bash title="Commande"
crontab -e
```

```bash title="Exemple"
0 2 * * * /opt/scripts/sauvegarde.sh >> /var/log/sauvegarde.log 2>&1
# tous les jours à 2 h, sortie et erreurs dans un journal
```

!!! warning "Attention"
    cron a un environnement minimal : chemins absolus partout, et tester le script à la main d'abord.

### Voir toutes les tâches planifiées du système

```bash title="Commande"
ls -la /etc/cron.*
cat /etc/crontab
```

```bash title="Exemple"
sudo grep -R . /etc/cron* /var/spool/cron 2>/dev/null   # tout le contenu, fichier par fichier
```

## systemd et at

### Lister les timers systemd

```bash title="Commande"
systemctl list-timers --all
```

```bash title="Exemple"
systemctl list-timers --all --no-pager
```

### Créer un timer systemd

```bash title="Commande"
sudo nano /etc/systemd/system/<nom>.timer
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
# le timer lance sauvegarde.service, du même nom
```

Ensuite : [créer un service pour un script](services.md#creer-un-service-pour-un-script)
{ .kw-cs-meta }

### Programmer une commande une seule fois

```bash title="Commande"
echo "<commande>" | at <heure>
```

```bash title="Exemple"
echo "/opt/scripts/rapport.sh" | at 18:00
```

```bash title="Exemple 2"
atq   # tâches en attente
```

## Repères : lire une ligne cron

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
