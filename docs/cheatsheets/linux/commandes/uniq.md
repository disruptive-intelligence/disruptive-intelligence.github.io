---
title: "uniq"
commande: "uniq"
---
# `uniq`

Regroupe les **lignes identiques voisines**. Pour compter les occurrences d'une valeur dans tout un fichier, il faut presque toujours trier d'abord.

```bash title="Syntaxe"
sort <fichier> | uniq <options>   # ou : <commande> | sort | uniq -c
```

## Les options utiles

| Option | Rôle |
|---|---|
| `-c` | Affiche le nombre d'occurrences de chaque ligne |
| `-d` | N'affiche que les valeurs répétées |
| `-u` | N'affiche que les valeurs présentes une seule fois |
| `-i` | Ignore la casse lors de la comparaison |

## Cas concrets déjà rencontrés

### Fréquence des ports autorisés

```bash title="Compter les événements par port"
grep -F '|action=allow|' firewall.log |
  grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
  sort -n | uniq -c | sort -rn
```

Le premier tri rapproche les ports identiques, `uniq -c` donne leur **nombre d'apparitions**, puis `sort -rn` place les plus fréquents en haut. Une ligne de log peut représenter un événement agrégé ; la fréquence est ici celle des **champs extraits**, pas nécessairement celle des paquets réseau.

### Sources d'un journal les plus fréquentes

```bash title="Compter les IP source"
grep -oE 'src=[0-9.]+' firewall.log | cut -d '=' -f 2 |
  sort | uniq -c | sort -rn | head -10
```

Adapte `src=` si ton format emploie `srcip=`. La regex trouve une **forme** d'adresse, pas une validation complète d'IPv4.

### Zeek HTTP : compter les méthodes et les réponses

```bash title="Répartition des méthodes et codes HTTP"
zeek-cut method < http.log | sort | uniq -c | sort -rn
zeek-cut status_code < http.log | sort | uniq -c | sort -rn
```

Pour la liste des URI différentes : `zeek-cut uri < http.log | sort -u`. Pour leur nombre, ajoute `| wc -l`. Un `404` fréquent est une piste d'énumération à examiner dans la [fiche Forensic réseau](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog).

## Autres exemples

```bash title="Doublons et valeurs isolées"
sort noms.txt | uniq                    # liste dédupliquée
sort noms.txt | uniq -d                 # noms répétés au moins deux fois
sort noms.txt | uniq -u                 # noms présents exactement une fois
cut -d ':' -f 7 /etc/passwd | sort | uniq -c | sort -rn   # shells par fréquence
```

## `sort -u`, `uniq -c`, `wc -l` : trois questions

| Question | Fin de pipeline |
|---|---|
| Quelles valeurs différentes ? | `sort -u` |
| Combien de valeurs différentes ? | `sort -u | wc -l` |
| Combien d'occurrences par valeur ? | `sort | uniq -c | sort -rn` |

## Pièges

- `uniq` seul ne retire que les **doublons consécutifs** : `A`, `B`, `A` reste inchangé.
- `uniq -u` veut dire « présent une seule fois », pas « liste de valeurs distinctes » ; pour cette dernière, utilise `sort -u`.
- Un `sort -n` est adapté aux ports ; un `sort` simple suffit aux noms et aux IP textuelles.

Voir aussi : [`sort`](sort.md), [`wc`](wc.md) et [filtrage par action dans Linux fondamentaux](../fondamentaux/texte-filtres.md#filtrer-par-action-avant-de-compter).
