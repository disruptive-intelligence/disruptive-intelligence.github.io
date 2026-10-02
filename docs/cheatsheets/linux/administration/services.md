---
title: "Services et démarrage"
cours:
  - library/it/linux/administration-linux/index.md
---

# Services et démarrage

Démarrer, arrêter, activer un service ; créer un service pour un script ; voir ce qui démarre avec la machine.

Les incontournables : `systemctl restart` · `systemctl enable --now` · `daemon-reload` · `list-unit-files --state=enabled`
{ .kw-cs-top }

## Piloter

### Démarrer, arrêter ou redémarrer un service

```bash title="Commande"
sudo systemctl start <service>     # démarrer
sudo systemctl stop <service>      # arrêter
sudo systemctl restart <service>   # redémarrer
sudo systemctl reload <service>    # relire la configuration
```

```bash title="Exemple"
sudo systemctl restart nginx
```

```bash title="Exemple 2"
sudo systemctl reload nginx
```

Pour comprendre : [Administration Linux, ch. 14](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
{ .kw-cs-meta }

### Activer ou désactiver un service au démarrage

```bash title="Commande"
sudo systemctl enable --now <service>    # au démarrage + maintenant
sudo systemctl disable --now <service>   # plus au démarrage + arrêt
```

```bash title="Exemple"
sudo systemctl enable --now ssh
```

??? example "Sortie"
    ```text
    Created symlink /etc/systemd/system/multi-user.target.wants/ssh.service → /usr/lib/systemd/system/ssh.service.
    ```

### Empêcher complètement un service de démarrer

```bash title="Commande"
sudo systemctl mask <service>     # bloquer
sudo systemctl unmask <service>   # débloquer
```

```bash title="Exemple"
sudo systemctl mask cups
```

??? example "Sortie"
    ```text
    Created symlink /etc/systemd/system/cups.service → /dev/null.
    ```

## Créer et inspecter

### Créer un service pour un script

```bash title="Commande"
sudo nano /etc/systemd/system/<nom>.service   # puis daemon-reload et enable
```

```ini title="Exemple"
[Unit]
Description=Mon script

[Service]
ExecStart=/opt/scripts/mon-script.sh
User=svc-script

[Install]
WantedBy=multi-user.target
```

```bash title="Exemple 2"
sudo systemctl daemon-reload && sudo systemctl enable --now mon-script
```

Ensuite : [recharger systemd après une modification](#recharger-systemd-apres-une-modification)
{ .kw-cs-meta }

### Recharger systemd après une modification

```bash title="Commande"
sudo systemctl daemon-reload   # à faire après chaque modification d'un .service ou .timer
```

```bash title="Exemple"
sudo systemctl daemon-reload && sudo systemctl restart nginx
```

### Lister ce qui démarre avec la machine

```bash title="Commande"
systemctl list-unit-files --state=enabled   # --type=service : seulement les services
```

```bash title="Exemple"
systemctl list-unit-files --type=service --state=enabled --no-pager | head -4
```

??? example "Sortie"
    ```text
    UNIT FILE           STATE   PRESET
    cron.service        enabled enabled
    nginx.service       enabled enabled
    ssh.service         enabled enabled
    ```

Ensuite : [lister les timers systemd](taches.md#lister-les-timers-systemd)
{ .kw-cs-meta }
