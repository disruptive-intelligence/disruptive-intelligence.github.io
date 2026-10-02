---
title: "ss"
commande: "ss"
---
# `ss`

Liste les sockets : ports en écoute et connexions, avec le processus derrière. Remplace `netstat`.

```bash title="Syntaxe"
ss -<options> [state <état>] [filtre]
```

Pour comprendre : [Administration Linux, ch. 17](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `-t` · `-u` | TCP · UDP |
| `-l` · `-a` | En écoute seulement · tout (écoute et connexions) |
| `-n` | Adresses et ports en chiffres (pas de résolution, plus rapide) |
| `-p` | Processus propriétaire (tous les processus avec sudo) |
| `-e` | Détails : utilisateur (uid), inode |
| `-s` | Résumé : nombre de connexions par état |
| `-4` · `-6` | IPv4 · IPv6 seulement |
| `state established` | Connexions établies seulement (`listening`, `time-wait`…) |
| `dst <IP>` · `'( sport = :22 )'` | Vers cette IP · port local 22 |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `sudo ss -tulpn` | **T**CP et **U**DP, en écoute (**l**), avec le **p**rocessus, en chiffres (**n**) : qui écoute sur quel port |
| `sudo ss -tnp state established` | Les connexions TCP en cours et le processus de chacune |
| `ss -tn dst 203.0.113.10` | Mes connexions vers cette adresse |
| `ss -tn '( sport = :22 )'` | Les connexions sur mon port 22 : qui est connecté en SSH |
| `ss -s` | Le résumé, pour repérer un nombre anormal de connexions |

## Pièges

- Lire l'adresse locale : `0.0.0.0:22` ou `*:22` = écoute sur toutes les interfaces (joignable depuis le réseau) ; `127.0.0.1:3306` = seulement depuis la machine.
- Sans `sudo`, la colonne Process reste vide pour les processus des autres utilisateurs.
- `netstat -tulpn` (paquet net-tools) prend les mêmes lettres, sur les vieux systèmes.
