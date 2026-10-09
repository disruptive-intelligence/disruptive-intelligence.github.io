---
title: "sort"
commande: "sort"
---
# `sort`

Trie des **lignes**. Après extraction d'une valeur, c'est l'étape qui permet de regrouper les mêmes valeurs pour `uniq`, ou de les dédupliquer avec `-u`.

```bash title="Syntaxe"
sort <options> <fichier>   # ou : <commande> | sort <options>
```

## Les options utiles

| Option | Rôle |
|---|---|
| `-n` · `-h` · `-V` | Tri numérique · tailles lisibles (`K`, `M`, `G`) · numéros de version |
| `-r` | Ordre inverse |
| `-u` | N'affiche qu'une ligne par valeur de tri distincte |
| `-t '|' -k1,1` | Séparateur `|`, tri sur le premier champ seulement |
| `-k2,2n` | Tri numérique sur le deuxième champ |
| `-c` | Vérifie qu'un fichier est déjà trié |

## Cas concrets déjà rencontrés

### Ports distincts d'un journal de pare-feu

```bash title="Liste numérique puis nombre de ports"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u
grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u | wc -l
```

`-n` place `80` avant `443` ; `-u` enlève les répétitions. Pour les ports autorisés seulement, filtre **avant** l'extraction :

```bash title="Ports autorisés et fréquence"
grep -F '|action=allow|' firewall.log |
  grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
  sort -n | uniq -c | sort -rn
```

Le premier tri rassemble les ports égaux ; `uniq -c` compte leurs occurrences ; le dernier tri met les nombres les plus élevés en tête.

### Remettre des événements dans l'ordre

```bash title="Horodatage ISO en premier champ"
sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S
```

Ce tri est chronologique seulement si les horodatages ont le même format ISO et le **même fuseau**. Si des événements sont collés sur une ligne, sépare-les d'abord avec [`sed`](sed.md#separer-des-evenements-vpn-colles). Trie **avant** `column`.

## Autres exemples

```bash title="Texte, nombres, tailles"
sort utilisateurs.txt                         # ordre alphabétique
sort -u utilisateurs.txt                      # chaque ligne une seule fois
sort -nr scores.txt                           # plus grand nombre d'abord
du -h /var/log/* | sort -hr | head            # tailles les plus grandes
sort -t ':' -k3,3n /etc/passwd | head         # UID croissant
```

## Pièges

- `sort` traite la **ligne entière** si tu ne donnes pas de clé `-k`.
- `sort -u` déduplique selon les clés de tri choisies ; si seule une colonne est clé, des lignes différentes peuvent être fusionnées.
- `sort` sans `-n` trie du texte : `100` peut apparaître avant `20`.
- Avec `uniq -c`, trie d'abord ; `uniq` ne regroupe que les doublons voisins.

Voir aussi : [`uniq`](uniq.md), [`wc`](wc.md) et [cas de pare-feu dans Forensic réseau](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal).
