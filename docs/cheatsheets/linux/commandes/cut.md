---
title: "cut"
commande: "cut"
---
# `cut`

Garde certains champs ou caractères d'une ligne. Pour un format simple à séparateur fixe, c'est souvent plus court qu'`awk`.

```bash title="Syntaxe"
cut -d '<séparateur>' -f <numéros> <fichier>   # ou : <commande> | cut -d '=' -f 2
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Rôle |
|---|---|
| `-d ':'` | Caractère qui sépare les champs ; **un seul caractère** (tabulation par défaut) |
| `-f 1,3` · `-f 2-4` | Champs 1 et 3 · champs 2 à 4 |
| `-s` | Omet les lignes sans le séparateur |
| `-c 1-10` | Dix premiers caractères (selon l'encodage et la locale) |
| `--complement` | Tous les champs sauf ceux demandés (GNU) |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `cut -d ':' -f 1,3,7 /etc/passwd` | Séparateur `:` ; le nom, l'UID et le shell de chaque compte |
| `grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2` | Ce qui suit le `=` : la valeur d'un champ `clé=valeur` |
| `grep -v '^#' http.log | cut -f3` | 3e colonne d'un fichier à tabulations, sans les lignes de commentaire |
| `cut -c 1-15 /var/log/syslog` | Les 15 premiers caractères de chaque ligne : la date |

## Pièges

- `cut` sélectionne par **position**, jamais par nom de champ : repérer les positions avant de choisir `-f`.
- Sans `-s`, une ligne **sans séparateur** ressort entière ; `-s` l'écarte.
- `cut -d ' '` compte chaque espace : avec des espaces multiples, les champs se décalent ; prendre `awk`.
- `cut -d ','` ne parse pas un CSV avec des virgules entre guillemets.

## Exemples

??? example kw-cs-more "Repérer les positions avant `-f`"
    ```bash
    head -n 1 fichier.tsv | tr '\t' '\n' | nl -ba                                              # un champ par ligne, numéroté (champs vides compris)
    awk -F '\t' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' fichier.tsv   # $1, $2… et leur valeur
    ```
    Fichier avec des métadonnées `#` (Zeek) : remplacer `head -n 1` par `grep -m1 -v '^#'`. Ni JSON ni CSV à guillemets.

??? example kw-cs-more "Découper puis compter"
    ```bash
    cut -d ':' -f 7 /etc/passwd | sort | uniq -c | sort -rn    # shells les plus fréquents
    cut -d '|' -f 1 evenements.txt | sort -u                   # premiers champs distincts
    printf '%s\n' 'code=401' 'code=403' | cut -d '=' -f 2      # 401 puis 403
    ```

## Cas concrets

??? example kw-cs-cas "Pare-feu : ne garder que le numéro de port après `grep -oE`"
    ```bash
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u   # grep sort « dstport=443 », cut garde « 443 »
    ```
    `| wc -l` pour leur nombre ; seulement les autorisés : `grep -F '|action=allow|' firewall.log |` en tête. Le cas complet : [Forensic › Pare-feu](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal)

??? example kw-cs-cas "Export `|` ou fichier `:` : garder quelques champs à position connue"
    ```bash
    cut -d ':' -f 1,3,7 /etc/passwd          # nom, UID, shell
    cut -d '|' -f 1,5,7,9 vpn.log            # export VPN, positions vérifiées
    ```
    Si `srcuser`, `publicip` ou `status` changent de position d'un événement à l'autre : les chercher par nom avec [`awk`](awk.md#cas-concrets).

??? example kw-cs-cas "Zeek `http.log` : IP, méthodes et codes par fréquence"
    ```bash
    grep -v '^#' http.log | cut -f3  | sort | uniq -c | sort -rn | head   # IP sources (id.orig_h)
    grep -v '^#' http.log | cut -f8  | sort | uniq -c | sort -rn          # méthodes
    grep -v '^#' http.log | cut -f15 | sort | uniq -c | sort -rn          # codes HTTP (ancien Bro ; 17 dans Zeek actuel)
    ```
    `cut -f` coupe sur les tabulations par défaut ; `grep -v '^#'` retire les métadonnées. Vérifier les positions avec `grep '^#fields' http.log`, ou éviter le problème : `zeek-cut id.orig_h < http.log`. Le cas complet : [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

Voir aussi : [Extraire une colonne](../fondamentaux/texte-filtres.md#extraire-une-colonne) · [Compter les valeurs distinctes d'un champ](../fondamentaux/texte-filtres.md#compter-les-valeurs-distinctes-dun-champ)
