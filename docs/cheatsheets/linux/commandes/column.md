---
title: "column"
commande: "column"
---
# `column`

Aligne un texte délimité en tableau pour le lire dans le terminal. Elle change **l'affichage**, pas le fichier ni le sens de ses champs.

```bash title="Syntaxe"
column -t -s '<séparateur>' <fichier>   # ou : <commande> | column -t -s '<séparateur>'
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Rôle |
|---|---|
| `-t` | Détecte la largeur des champs et les aligne |
| `-s '|'` | Séparateur des champs d'entrée ; remplace `|` selon le fichier |
| `-s $'\t'` | Tabulation comme séparateur (syntaxe Bash) |
| `-o ' | '` | Séparateur affiché entre les colonnes (util-linux) |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `column -t -s ':' /etc/passwd` | Le fichier des comptes en tableau |
| `column -t -s '|' fichier.txt | less -S` | Champs `|` alignés ; les lignes larges défilent au lieu de se replier |
| `zeek-cut … < http.log | column -t -s $'\t'` | Une sortie tabulée (Zeek, TSV) alignée |
| `… | uniq -c | sort -rn | column -t` | Un comptage aligné en deux colonnes |

## Pièges

- Trier et compter **avant** d'aligner : les espaces ajoutés par `column` faussent une comparaison de texte.
- `column` ne comprend pas un CSV avec des séparateurs **entre guillemets** : prendre un parseur CSV.
- Tout est aligné en mémoire : sur un gros fichier, filtrer d'abord (`grep`, `head`, `awk`).
- `head` se place **avant** `column`, `less -S` **après**.

## Exemples

??? example kw-cs-more "Fichiers délimités"
    ```bash
    column -t -s ':' /etc/passwd | less -S          # comptes, UID, dossier, shell
    awk -F: '{print $1 "|" $3 "|" $7}' /etc/passwd | column -t -s '|'
    sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S
    ```

## Cas concrets

??? example kw-cs-cas "VPN : un export `|` illisible, événements collés sur une ligne"
    ```bash
    sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log |
      column -t -s '|' | less -S       # sed : un événement par ligne ; column : aligne ; less -S : défile
    column -t -s '|' vpn.log | less -S  # déjà une ligne par événement : sans sed
    ```

??? example kw-cs-cas "VPN : seulement heure, utilisateur, IP et résultat"
    ```bash
    awk -F'|' '{print $1 "|" $5 "|" $7 "|" $9}' vpn.log | column -t -s '|'   # positions vérifiées sur une ligne
    ```
    Si l'ordre de `srcuser`, `publicip` et `status` varie : extraction par nom de champ avec [`awk`](awk.md#cas-concrets).

??? example kw-cs-cas "Pare-feu : présenter le comptage des ports autorisés"
    ```bash
    grep -F '|action=allow|' firewall.log |
      grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
      sort -n | uniq -c | sort -rn |
      column -t
    ```
    Seulement le nombre de ports distincts : [`sort -u | wc -l`](sort.md#cas-concrets) à la place.

??? example kw-cs-cas "Zeek `http.log` : une vue lisible des requêtes"
    ```bash
    zeek-cut ts id.orig_h method uri status_code < http.log |
      head -n 20 | column -t -s $'\t'
    ```
    Tout le résultat : retirer `head -n 20`, ajouter `| less -S` après `column`. Le cas complet : [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

Voir aussi : [Afficher en tableau aligné](../fondamentaux/texte-filtres.md#afficher-en-tableau-aligne) · [Forensic › VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par)
