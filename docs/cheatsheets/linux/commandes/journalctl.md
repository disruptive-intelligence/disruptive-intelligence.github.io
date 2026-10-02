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

## Exemples

??? example kw-cs-more "Lire"
    ```bash
    journalctl -e                       # ouvrir à la fin
    journalctl -n 50 --no-pager         # les 50 dernières lignes
    journalctl -r                       # plus récent d'abord
    journalctl -f                       # en direct
    journalctl -u nginx -u php8.3-fpm   # deux services ensemble
    journalctl -k                       # le noyau
    ```

??? example kw-cs-more "Par période"
    ```bash
    journalctl --since today
    journalctl --since yesterday --until today
    journalctl --since "2026-10-01 08:00" --until "2026-10-01 12:00"
    journalctl --since "30 min ago"
    journalctl -b -1                    # le démarrage précédent
    journalctl --list-boots             # la liste des démarrages
    ```

??? example kw-cs-more "Par gravité ou par source"
    ```bash
    journalctl -p err -b                # erreurs depuis le démarrage
    journalctl -p warning..err          # une plage de gravité
    journalctl _PID=1234                # un processus
    journalctl _UID=1000                # tout ce qui vient de l'utilisateur 1000
    journalctl _COMM=sshd -g "Failed"   # sshd, messages qui contiennent Failed
    journalctl /usr/sbin/sshd           # par binaire
    ```

??? example kw-cs-more "Investigation et export"
    ```bash
    journalctl _COMM=sudo --since today --no-pager          # usage de sudo aujourd'hui
    journalctl -u ssh -g "Accepted" --since "7 days ago"    # connexions SSH réussies sur 7 jours
    journalctl -u ssh -o json --since today > ssh.json      # export JSON (SIEM, jq)
    journalctl --utc -o short-iso --since today > journal-utc.log
    journalctl --disk-usage                                 # place occupée
    sudo journalctl --vacuum-size=500M                      # réduire à 500 Mo
    ```
