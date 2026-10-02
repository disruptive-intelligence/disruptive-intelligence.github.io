---
title: "find"
commande: "find"
---
# `find`

Parcourt une arborescence et sélectionne les fichiers selon leur nom, leur type, leur taille, leur date, leur propriétaire ou leurs droits ; peut ensuite agir sur chacun.

```bash title="Syntaxe"
find <où> <critères> <action>   # sans action : affiche les chemins
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `-name "<motif>"` · `-iname` | Nom (motif du shell, entre guillemets) · sans tenir compte des majuscules |
| `-type f` · `d` · `l` | Fichier ordinaire · dossier · lien symbolique |
| `-size +100M` · `-size -1k` | Plus de 100 Mo · moins de 1 Ko (unités `k`, `M`, `G`) |
| `-mtime -7` · `-mmin -60` | Modifié il y a moins de 7 jours · moins de 60 minutes |
| `-newermt "<date>"` | Modifié après cette date (`! -newermt` : avant) |
| `-user <nom>` · `-group <nom>` | Appartient à cet utilisateur · à ce groupe |
| `-perm -4000` · `-perm -o+w` | Bit SUID présent · modifiable par tous |
| `-maxdepth <N>` | Pas plus de N niveaux sous le point de départ |
| `-xdev` | Reste sur ce système de fichiers (ne descend pas dans `/proc`, les disques montés…) |
| `!` · `-o` | Négation · OU (par défaut les critères s'enchaînent en ET) |
| `-ls` | Affiche le détail de chaque fichier (droits, taille, date) |
| `-exec <cmd> {} \;` · `{} +` | Lance la commande pour chaque fichier · une seule fois avec tous |
| `-delete` | Supprime les fichiers trouvés |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `find / -perm -4000 -type f 2>/dev/null` | Depuis la racine, les fichiers ordinaires qui ont le bit SUID ; les « Permission denied » sont jetés |
| `find /var/www -type f -mmin -60 -ls` | Les fichiers de `/var/www` modifiés dans la dernière heure, avec leur détail |
| `find / -xdev -newermt "2026-10-01 08:00" ! -newermt "2026-10-01 12:00"` | Modifiés entre 8 h et 12 h, sur ce disque seulement |
| `find /var/log -name "*.log" -size +100M -exec ls -lh {} \;` | Les journaux de plus de 100 Mo, listés avec leur taille |
| `find /home -type f \( -name "*.sh" -o -name "*.py" \)` | Les scripts shell OU Python (parenthèses échappées) |

## Pièges

- Le motif se met **entre guillemets** : sans, le shell remplace `*.conf` par les fichiers du dossier courant avant que `find` ne le voie.
- `-delete` placé avant les critères supprime tout ce qui est parcouru : tester d'abord la même commande sans `-delete`.
- `-mtime -1` = moins de 24 h ; `-mtime 1` = entre 24 et 48 h ; `-mtime +1` = plus de 48 h.
- `-maxdepth` se place juste après le point de départ, avant les autres critères.
