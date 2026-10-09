---
title: "cut"
commande: "cut"
---
# `cut`

Garde certains champs ou caractères d'une ligne. Pour un format simple à séparateur fixe, c'est souvent plus court qu'`awk`.

```bash title="Syntaxe"
cut -d '<séparateur>' -f <numéros> <fichier>   # ou : <commande> | cut -d '=' -f 2
```

## Les options utiles

| Option | Rôle |
|---|---|
| `-d ':'` | Caractère qui sépare les champs ; **un seul caractère** |
| `-f 1,3` · `-f 2-4` | Champs 1 et 3 · champs 2 à 4 |
| `-s` | Omet les lignes sans le séparateur |
| `-c 1-10` | Dix premiers caractères (selon l'encodage et la locale) |
| `--complement` | Tous les champs sauf ceux demandés (GNU) |

## Repérer les positions avant `-f`

Sur une ligne tabulée simple, mets les champs à la verticale et numérote-les ; avec `awk`, affiche aussi `$1`, `$2`… directement :

```bash title="Première ligne d'un TSV"
head -n 1 fichier.tsv | tr '\t' '\n' | nl -ba
awk -F '\t' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' fichier.tsv
```

Si le journal comporte des métadonnées `#` comme Zeek, remplace `head -n 1` par `grep -m1 -v '^#'`. `nl -ba` numérote les lignes vides, utiles pour voir un champ vide. Ces méthodes ne décodent ni le JSON ni un CSV avec séparateurs entre guillemets.

## Cas concrets déjà rencontrés

### Enlever `dstport=` après extraction

```bash title="Ports visés, sans doublons"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 | sort -n -u
```

`grep -oE` produit des lignes comme `dstport=443` ; `cut` garde la valeur du champ 2 ; `sort -n -u` donne une liste numérique de ports différents. Ajoute `| wc -l` pour leur nombre. Pour les ports **autorisés** seulement, place `grep -F '|action=allow|' firewall.log |` au début.

### Lire des champs séparés par `:` ou `|`

```bash title="Champs à position connue"
cut -d ':' -f 1,3,7 /etc/passwd          # nom, UID, shell
cut -d '|' -f 1,5,7,9 vpn.log           # exemple après vérification des positions
```

Si les champs `srcuser`, `publicip` ou `status` ne sont pas toujours aux mêmes positions, utilise [`awk`](awk.md#vpn-construire-une-vue-lisible-sans-supposer-lordre-des-champs) pour chercher leurs noms.

### Zeek HTTP : extraire des colonnes tabulées

`cut -f` utilise les tabulations par défaut. Dans `http.log`, lis d'abord `grep '^#fields' http.log` : ces positions ne valent que si l'en-tête confirme `id.orig_h` en 3, `method` en 8 et `status_code` en 15.

```bash title="IP, méthodes et codes par fréquence"
grep -v '^#' http.log | cut -f3  | sort | uniq -c | sort -rn | head
grep -v '^#' http.log | cut -f8  | sort | uniq -c | sort -rn
grep -v '^#' http.log | cut -f15 | sort | uniq -c | sort -rn
```

Les lignes `#` sont des métadonnées Zeek, pas des requêtes. Pour éviter de dépendre des positions, utilise `zeek-cut id.orig_h < http.log`, puis les mêmes étapes de tri et comptage. Voir le [scénario HTTP complet](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog).

## Autres exemples

```bash title="Découper puis compter"
cut -d ':' -f 7 /etc/passwd | sort | uniq -c | sort -rn    # shells les plus fréquents
cut -d '|' -f 1 evenements.txt | sort -u                   # premiers champs distincts
printf '%s\n' 'code=401' 'code=403' | cut -d '=' -f 2      # 401 puis 403
```

## Pièges

- Sans `-s`, une ligne **sans séparateur** ressort entière ; `-s` l'écarte.
- `cut -d ','` ne parse pas un CSV avec des virgules entre guillemets.
- `cut` sélectionne par **position**, jamais par nom de champ ; inspecte le fichier avant de choisir `-f`.

Voir aussi : [filtrage d'un fichier texte](../fondamentaux/texte-filtres.md#extraire-une-colonne) et [journal de pare-feu dans Forensic réseau](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal).
