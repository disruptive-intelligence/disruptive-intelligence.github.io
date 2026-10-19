---
title: "uniq"
commande: "uniq"
---
# `uniq`

Regroupe les **lignes identiques voisines**. Pour compter les occurrences d'une valeur dans tout un fichier, il faut presque toujours trier d'abord.

```bash title="Syntaxe"
sort <fichier> | uniq <options>   # ou : <commande> | sort | uniq -c
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Rôle |
|---|---|
| `-c` | Affiche le nombre d'occurrences de chaque ligne |
| `-d` | N'affiche que les valeurs répétées |
| `-u` | N'affiche que les valeurs présentes une seule fois |
| `-i` | Ignore la casse lors de la comparaison |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `sort noms.txt | uniq` | Liste dédupliquée (comme `sort -u`) |
| `… | sort | uniq -c | sort -rn` | Nombre d'occurrences de chaque valeur, les plus fréquentes en tête |
| `sort noms.txt | uniq -d` | Seulement les valeurs répétées |
| `sort noms.txt | uniq -u` | Seulement les valeurs présentes une seule fois |

## `sort -u`, `uniq -c`, `wc -l` : trois questions

| Question | Fin de pipeline |
|---|---|
| Quelles valeurs différentes ? | `sort -u` |
| Combien de valeurs différentes ? | `sort -u | wc -l` |
| Combien d'occurrences par valeur ? | `sort | uniq -c | sort -rn` |

## Pièges

- `uniq` seul ne retire que les **doublons consécutifs** : `A`, `B`, `A` reste inchangé.
- `uniq -u` = « présent une seule fois », pas « valeurs distinctes » : pour celles-ci, `sort -u`.
- `sort -n` pour des ports ; un `sort` simple suffit aux noms et aux IP.
- Une ligne de journal peut résumer plusieurs paquets : `uniq -c` compte des lignes ou des champs, pas forcément des connexions.

## Exemples

??? example kw-cs-more "Doublons et valeurs isolées"
    ```bash
    sort noms.txt | uniq                    # liste dédupliquée
    sort noms.txt | uniq -d                 # noms répétés au moins deux fois
    sort noms.txt | uniq -u                 # noms présents exactement une fois
    cut -d ':' -f 7 /etc/passwd | sort | uniq -c | sort -rn   # shells par fréquence
    ```

## Cas concrets

??? example kw-cs-cas "Pare-feu : quels ports autorisés reviennent le plus ?"
    ```bash
    grep -F '|action=allow|' firewall.log |
      grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
      sort -n | uniq -c | sort -rn      # trier, compter, classer
    ```

??? example kw-cs-cas "Pare-feu : quelles IP sources apparaissent le plus ?"
    ```bash
    grep -oE 'src=[0-9.]+' firewall.log | cut -d '=' -f 2 |
      sort | uniq -c | sort -rn | head -10
    ```
    `srcip=` dans d'autres formats. La regex reconnaît une forme d'adresse, elle ne valide pas l'IPv4.

??? example kw-cs-cas "Zeek `http.log` : répartition des méthodes et des codes HTTP"
    ```bash
    zeek-cut method < http.log | sort | uniq -c | sort -rn
    zeek-cut status_code < http.log | sort | uniq -c | sort -rn
    ```
    URI différentes : `zeek-cut uri < http.log | sort -u` (`| wc -l` pour leur nombre). Beaucoup de `404` : piste d'énumération, voir [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog).

Voir aussi : [`sort`](sort.md) · [`wc`](wc.md) · [Compter les valeurs distinctes d'un champ](../fondamentaux/texte-filtres.md#compter-les-valeurs-distinctes-dun-champ)
