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
