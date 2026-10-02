---
title: "systemctl"
commande: "systemctl"
---
# `systemctl`

Pilote systemd : l'état, le démarrage et l'activation des services, et ce qui se lance avec la machine.

```bash title="Syntaxe"
systemctl <action> <unité>   # l'unité : nginx, nginx.service, sauvegarde.timer…
```

Pour comprendre : [Administration Linux, ch. 14](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/02-chapitre-14-les-services-avec-systemd.md)
{ .kw-cs-meta }

## Les options utiles

| Action | Ce qu'elle fait |
|---|---|
| `status` | État, PID principal, mémoire, dernières lignes du journal |
| `start` · `stop` · `restart` · `reload` | Démarrer · arrêter · redémarrer · relire la configuration |
| `enable` · `disable` (`--now`) | Lancer ou non au démarrage (et tout de suite avec `--now`) |
| `is-active` · `is-enabled` · `is-failed` | Réponse courte, pour un script |
| `mask` · `unmask` | Interdire tout démarrage, même manuel · lever l'interdiction |
| `cat` · `edit` | Afficher le fichier d'unité · créer une surcharge (`override.conf`) |
| `daemon-reload` | Relire les fichiers d'unités après une modification |
| `list-units --type=service --state=running` | Services en cours |
| `list-unit-files --state=enabled` · `--failed` · `list-timers` | Activés au démarrage · en échec · minuteries |
| `show <unité> -p <propriété>` | Une propriété précise (`MainPID`, `ExecStart`, `User`…) |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `sudo systemctl enable --now nginx` | Lancer nginx à chaque démarrage, et tout de suite |
| `systemctl list-units --type=service --state=running --no-pager` | Tous les services qui tournent, sans pagination |
| `systemctl show ssh -p MainPID -p ActiveEnterTimestamp` | Le PID de sshd et depuis quand le service tourne |
| `sudo systemctl edit nginx` | Surcharge propre : le fichier d'origine reste intact |

## Pièges

- `enable` ne démarre pas (sauf `--now`) ; `start` n'active pas au démarrage.
- Après avoir modifié un `.service` ou un `.timer` : `daemon-reload`, sinon systemd garde l'ancienne version.
- Lire `status` : **Loaded** (fichier d'unité, `enabled`/`disabled`), **Active** (`running`, `exited`, `failed` et depuis quand), **Main PID**.

## Exemples

??? example kw-cs-more "Voir l'état"
    ```bash
    systemctl status nginx --no-pager -l         # état complet, lignes non tronquées
    systemctl is-active nginx                    # active, inactive ou failed
    systemctl --failed                           # services en échec
    systemctl list-units --type=service --state=running
    systemctl list-unit-files --state=enabled    # ce qui démarre avec la machine
    systemctl list-dependencies nginx            # ce dont le service dépend
    ```

??? example kw-cs-more "Piloter"
    ```bash
    sudo systemctl restart nginx
    sudo systemctl reload nginx || sudo systemctl restart nginx   # relire, sinon redémarrer
    sudo systemctl enable --now fail2ban         # activer et démarrer
    sudo systemctl disable --now cups            # désactiver et arrêter
    sudo systemctl mask --now bluetooth          # interdire complètement
    sudo systemctl reboot
    ```

??? example kw-cs-more "Inspecter et modifier"
    ```bash
    systemctl cat ssh                            # fichier d'unité et surcharges
    systemctl show nginx -p ExecStart -p User -p MainPID
    sudo systemctl edit nginx                    # surcharge propre (override.conf)
    sudo systemctl edit --full nginx             # copie complète, modifiable
    sudo systemctl daemon-reload                 # après toute modification
    systemd-analyze blame | head                 # les services les plus lents au démarrage
    ```

??? example kw-cs-more "Investigation : persistance"
    ```bash
    systemctl list-unit-files --type=service --state=enabled --no-pager   # tout ce qui démarre
    sudo find /etc/systemd/system -name "*.service" -newermt "2026-09-25" -ls   # unités créées récemment
    grep -r "ExecStart" /etc/systemd/system/*.service                          # ce que lance chaque service ajouté
    systemctl list-timers --all                  # minuteries
    systemctl --user list-units --type=service   # services de l'utilisateur courant
    ```
