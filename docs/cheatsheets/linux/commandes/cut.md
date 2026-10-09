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
