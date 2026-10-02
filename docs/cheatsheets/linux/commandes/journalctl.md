---
title: "journalctl"
commande: "journalctl"
---
# `journalctl`

Lit le journal de systemd : services, système, noyau — avec des filtres par service, période, gravité ou processus.

```bash title="Syntaxe"
journalctl [filtres] [options d'affichage]
```

Pour comprendre : [Administration Linux, ch. 15](../../../library/it/linux/administration-linux/04-partie-4-la-machine-vivante/03-chapitre-15-les-logs-et-journaux.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `-u <service>` | Un seul service (plusieurs `-u` possibles) |
| `-f` · `-n <N>` · `-e` | Suit en direct · les N dernières lignes · ouvre à la fin |
| `-b` · `-b -1` · `--list-boots` | Depuis le démarrage · le démarrage précédent · liste des démarrages |
| `-p err` | Gravité minimale : `emerg` `alert` `crit` `err` `warning` `notice` `info` `debug` |
| `--since` · `--until` | Période : `"2026-10-01 08:00"`, `"1 hour ago"`, `yesterday`, `today` |
| `-k` | Messages du noyau (comme `dmesg`) |
| `-g <motif>` | Seulement les messages qui contiennent le motif |
| `_PID=` · `_UID=` · `_COMM=` | Par processus · par utilisateur · par nom de programme |
| `-r` · `-o short-iso` · `-o json` | Plus récent d'abord · dates ISO · JSON |
| `--no-pager` · `--utc` | Sans pagination (pour un pipe) · heures en UTC |
| `--disk-usage` · `--vacuum-time=2weeks` | Place occupée · supprime ce qui a plus de 2 semaines |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `journalctl -u ssh --since "1 hour ago" -p warning` | Le service ssh, depuis une heure, avertissements et plus grave |
| `journalctl -b -1 -p err` | Les erreurs du démarrage précédent : utile après un plantage |
| `journalctl _COMM=sudo --since today` | Tout ce que `sudo` a journalisé aujourd'hui |
| `journalctl -k -g usb --since today` | Les messages du noyau qui parlent d'USB aujourd'hui |
| `journalctl -u nginx -o short-iso --utc --no-pager > nginx.log` | Export du journal nginx, horodaté en ISO et en UTC |

## Pièges

- Sans `sudo` (ni groupe `adm` ou `systemd-journal`), on ne voit que ses propres journaux.
- Sur certaines distributions le journal est **volatil** (en mémoire, perdu au redémarrage) : il devient persistant si `/var/log/journal` existe.
- Pour comparer avec d'autres sources (SIEM, autre machine), afficher en UTC : `--utc`.
