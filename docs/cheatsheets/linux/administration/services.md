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
sudo systemctl start|stop|restart <service>
```

```bash title="Exemple"
sudo systemctl restart nginx
```

```bash title="Exemple 2"
sudo systemctl reload nginx   # relit la configuration sans couper les connexions
```

Pour comprendre : [Administration Linux, ch. 14](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
{ .kw-cs-meta }

### Activer ou désactiver un service au démarrage

```bash title="Commande"
sudo systemctl enable --now <service>
sudo systemctl disable --now <service>
```

```bash title="Exemple"
sudo systemctl enable --now ssh   # active au démarrage et démarre tout de suite
```

### Empêcher complètement un service de démarrer

```bash title="Commande"
sudo systemctl mask <service>
```

```bash title="Exemple"
sudo systemctl mask cups
```

```bash title="Exemple 2"
sudo systemctl unmask cups   # annuler
```

## Créer et inspecter

### Créer un service pour un script

```bash title="Commande"
sudo nano /etc/systemd/system/<nom>.service
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
sudo systemctl daemon-reload
```

```bash title="Exemple"
sudo systemctl daemon-reload && sudo systemctl restart nginx
```

### Lister ce qui démarre avec la machine

```bash title="Commande"
systemctl list-unit-files --state=enabled
```

```bash title="Exemple"
systemctl list-unit-files --type=service --state=enabled --no-pager
```

Ensuite : [lister les timers systemd](taches.md#lister-les-timers-systemd)
{ .kw-cs-meta }
