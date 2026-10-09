---
title: "column"
commande: "column"
---
# `column`

Aligne un texte délimité en tableau pour le lire dans le terminal. Elle change **l'affichage**, pas le fichier ni la signification de ses champs.

```bash title="Syntaxe"
column -t -s '<séparateur>' <fichier>   # ou : <commande> | column -t -s '<séparateur>'
```

## Les options utiles

| Option | Rôle |
|---|---|
| `-t` | Détecte la largeur des champs et les aligne |
| `-s '|'` | Séparateur des champs d'entrée ; remplace `|` selon le fichier |
| `-o ' | '` | Séparateur affiché entre les colonnes (util-linux) |

## Cas concrets déjà rencontrés

### Lire un export VPN à séparateur `|`

```bash title="Un événement par ligne, puis des colonnes"
sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log |
  column -t -s '|' | less -S
```

Le `sed` est utile **seulement** si plusieurs événements ISO sont collés sur une même ligne avec un espace entre eux. `column` aligne après séparation, puis `less -S` permet de défiler sur une ligne large. Pour un fichier déjà à une ligne par événement :

```bash title="Sans étape sed"
column -t -s '|' vpn.log | less -S
```

### Choisir quatre informations avant l'alignement

```bash title="Positions vérifiées dans le fichier"
awk -F'|' '{print $1 "|" $5 "|" $7 "|" $9}' vpn.log | column -t -s '|'
```

Ici, les numéros viennent **après inspection** d'une ligne. Si l'ordre de `srcuser`, `publicip` et `status` varie, la [fiche `awk`](awk.md#vpn-construire-une-vue-lisible-sans-supposer-lordre-des-champs) montre une extraction par nom de champ.

### Comparer les ports d'un pare-feu

```bash title="Préparer puis présenter"
grep -F '|action=allow|' firewall.log |
  grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
  sort -n | uniq -c | sort -rn |
  column -t
```

Le comptage se fait **avant** `column` ; les colonnes rendent les résultats plus lisibles. Si seul le nombre de ports distincts t'intéresse, utilise [`sort -u | wc -l`](sort.md#ports-distincts-dun-journal-de-pare-feu) à la place.

### Zeek HTTP : une vue lisible des requêtes

```bash title="Colonnes choisies par nom, puis alignées"
zeek-cut ts id.orig_h method uri status_code < http.log |
  head -n 20 | column -t -s $'\t'
```

Le séparateur `$'\t'` représente une tabulation dans Bash. `head` limite l'entrée **avant** `column` ; pour parcourir tout le résultat, retire `head -n 20` et ajoute `| less -S` **après** `column`. Pour une [investigation Zeek complète](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog), conserve l'IP et le code avec l'URI.

## Autres exemples

```bash title="Fichiers délimités"
column -t -s ':' /etc/passwd | less -S          # comptes, UID, dossier, shell
awk -F: '{print $1 "|" $3 "|" $7}' /etc/passwd | column -t -s '|'
sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S
```

## Pièges

- `column` ne sait pas interpréter correctement un CSV avec des séparateurs **entre guillemets** ; emploie un parseur CSV pour ce cas.
- Les colonnes sont alignées en mémoire : sur un très gros fichier, filtre d'abord avec `grep`, `head` ou `awk`.
- Trie et compte **avant** d'aligner : les espaces ajoutés par `column` peuvent fausser une comparaison de texte.

À voir aussi : [mise en forme générale](../fondamentaux/texte-filtres.md#mettre-en-forme-et-trier-un-fichier-texte) et [scénario VPN dans Forensic réseau](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).
