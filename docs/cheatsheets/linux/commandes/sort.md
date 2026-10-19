---
title: "sort"
commande: "sort"
---
# `sort`

Trie des **lignes**. Après extraction d'une valeur, c'est l'étape qui regroupe les valeurs identiques pour `uniq`, ou les déduplique avec `-u`.

```bash title="Syntaxe"
sort <options> <fichier>   # ou : <commande> | sort <options>
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Rôle |
|---|---|
| `-n` · `-h` · `-V` | Tri numérique · tailles lisibles (`K`, `M`, `G`) · numéros de version |
| `-r` | Ordre inverse |
| `-u` | Une ligne par valeur de tri distincte |
| `-t '|' -k1,1` | Séparateur `|`, tri sur le premier champ seulement |
| `-k2,2n` | Tri numérique sur le deuxième champ |
| `-c` | Vérifie qu'un fichier est déjà trié |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `… | sort -n -u` | Tri numérique, chaque valeur une fois : une liste de ports, d'UID… |
| `… | sort | uniq -c | sort -rn` | Regroupe, compte, puis classe les comptes du plus grand au plus petit |
| `sort -t '|' -k1,1 evenements.txt` | Trie sur le 1er champ séparé par `|` (un horodatage) |
| `du -h /var/log/* | sort -hr | head` | Les tailles lisibles, de la plus grande à la plus petite |
| `sort -t ':' -k3,3n /etc/passwd` | Les comptes par UID croissant |

## Pièges

- Sans `-n`, `sort` trie du texte : `100` passe avant `20`.
- Sans clé `-k`, c'est la **ligne entière** qui compte.
- `sort -u` déduplique selon les clés choisies : avec une seule colonne pour clé, des lignes différentes peuvent être fusionnées.
- Avant `uniq -c`, toujours trier : `uniq` ne regroupe que les doublons voisins.
- Trier **avant** `column` : les espaces d'alignement changent les clés.

## Exemples

??? example kw-cs-more "Texte, nombres, tailles"
    ```bash
    sort utilisateurs.txt                         # ordre alphabétique
    sort -u utilisateurs.txt                      # chaque ligne une seule fois
    sort -nr scores.txt                           # plus grand nombre d'abord
    du -h /var/log/* | sort -hr | head            # tailles les plus grandes
    sort -t ':' -k3,3n /etc/passwd | head         # UID croissant
    ```

## Cas concrets

??? example kw-cs-cas "Pare-feu : quels ports distincts ont été visés, et combien ?"
    ```bash
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u          # -n : 80 avant 443 ; -u : sans répétition
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u | wc -l  # leur nombre
    ```

??? example kw-cs-cas "Pare-feu : ports autorisés, du plus fréquent au moins fréquent"
    ```bash
    grep -F '|action=allow|' firewall.log |
      grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
      sort -n | uniq -c | sort -rn      # 1er tri : rassemble ; uniq -c : compte ; 2e tri : plus grands comptes en tête
    ```

??? example kw-cs-cas "Événements : les remettre dans l'ordre chronologique"
    ```bash
    sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S   # horodatage ISO en 1er champ
    ```
    Chronologique seulement si tous les horodatages ont le même format ISO et le **même fuseau**. Événements collés sur une ligne : les séparer d'abord avec [`sed`](sed.md#cas-concrets).

??? example kw-cs-cas "Zeek `http.log` : sources les plus actives, codes les plus fréquents"
    ```bash
    zeek-cut id.orig_h < http.log | sort | uniq -c | sort -rn | head   # IP sources
    zeek-cut status_code < http.log | sort | uniq -c | sort -rn        # codes HTTP
    zeek-cut uri < http.log | sort -u                                  # autre question : quelles URI distinctes ?
    ```
    Le cas complet : [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

Voir aussi : [`uniq`](uniq.md) · [`wc`](wc.md) · [Trier des lignes](../fondamentaux/texte-filtres.md#trier-des-lignes)
