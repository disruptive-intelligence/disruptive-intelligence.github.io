---
title: "less"
commande: "less"
---
# `less`

Parcourt un fichier ou une sortie de commande **sans tout afficher d'un coup**. La lecture est interactive et ne modifie pas le fichier.

```bash title="Syntaxe"
less <fichier>   # ou : <commande> | less -S
```

Pour comprendre : [Administration Linux, ch. 3](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
{ .kw-cs-meta }

## Les options et touches utiles

| Option ou touche | Rôle |
|---|---|
| `-S` | Garde les longues lignes sur une seule ligne ; flèches gauche/droite pour défiler |
| `-N` | Montre les numéros de ligne |
| `/motif`, `n`, `N` | Cherche vers l'avant, occurrence suivante, occurrence précédente |
| `g`, `G` | Début, fin du fichier |
| `+F` | Suit un fichier qui grossit ; `Ctrl+C` arrête le suivi, `q` quitte |
| `q` | Quitte le lecteur |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `less -S fichier` | Sans retour à la ligne : on défile à l'horizontale |
| `less -N /var/log/auth.log` | Avec les numéros de ligne |
| `less +F /var/log/auth.log` | Suit le fichier comme `tail -f` ; `Ctrl+C` pour revenir à la lecture |
| `zcat /var/log/auth.log.1.gz | less` | Lit une archive compressée sans l'extraire sur le disque |
| `grep -n -C 2 'motif' fichier | less -S` | Les correspondances et leur contexte, à parcourir |

## Pièges

- `less` ne trie rien : `sort` **avant** `less`.
- `-S` cache la fin d'une ligne jusqu'au défilement ; elle n'est pas supprimée.
- `/motif` cherche dans ce qui a été transmis à `less` : pour réduire les données dès le départ, filtrer avec `grep`.

## Exemples

??? example kw-cs-more "Fichiers, sorties et suivi"
    ```bash
    less -N /var/log/auth.log                     # numéros de ligne
    grep -n -C 2 'Failed password' /var/log/auth.log | less -S
    zcat /var/log/auth.log.1.gz | less            # archive compressée, sans extraction sur disque
    less +F /var/log/auth.log                     # nouvelles lignes en direct
    ```

## Cas concrets

??? example kw-cs-cas "VPN : lire un export large et retrouver les échecs"
    ```bash
    sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log |
      column -t -s '|' | less -S
    ```
    Dans `less` : `/status=failure`, `n` pour le suivant, puis chercher un éventuel `/status=success` dans la chronologie.

??? example kw-cs-cas "Pare-feu : parcourir seulement les événements autorisés"
    ```bash
    grep -F '|action=allow|' firewall.log | less -S
    ```
    Seulement certains champs : les extraire d'abord avec [`awk`](awk.md#cas-concrets), puis `| less -S`.

Voir aussi : [Lire un fichier long](../fondamentaux/fichiers-recherche.md#lire-un-fichier-long) · [Forensic › VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par)
