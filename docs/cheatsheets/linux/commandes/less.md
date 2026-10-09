---
title: "less"
commande: "less"
---
# `less`

Parcourt un fichier ou une sortie de commande **sans tout afficher d'un coup**. La lecture est interactive et ne modifie pas le fichier.

```bash title="Syntaxe"
less <fichier>   # ou : <commande> | less -S
```

## Les options et touches utiles

| Option ou touche | Rôle |
|---|---|
| `-S` | Garde les longues lignes sur une seule ligne ; flèches gauche/droite pour défiler |
| `-N` | Montre les numéros de ligne |
| `/motif`, `n`, `N` | Cherche vers l'avant, occurrence suivante, occurrence précédente |
| `g`, `G` | Début, fin du fichier |
| `+F` | Suit un fichier qui grossit ; `Ctrl+C` arrête le suivi, `q` quitte |
| `q` | Quitte le lecteur |

## Cas concrets déjà rencontrés

### Lire un export large

```bash title="VPN : événements en colonnes"
sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log |
  column -t -s '|' | less -S
```

`less -S` évite que les nombreux champs d'un événement fassent plusieurs lignes à l'écran. Cherche `/status=failure`, passe au suivant avec `n`, puis vérifie l'éventuel `/status=success` dans la chronologie.

### Lire seulement ce qui t'intéresse

```bash title="Pare-feu : événements autorisés"
grep -F '|action=allow|' firewall.log | less -S
```

Pour garder **seulement certains champs** plutôt que des lignes complètes, projette-les d'abord avec [`awk`](awk.md#vpn-construire-une-vue-lisible-sans-supposer-lordre-des-champs), puis pipe le résultat vers `less -S`.

## Autres exemples

```bash title="Fichiers, sorties et suivi"
less -N /var/log/auth.log                     # numéros de ligne
grep -n -C 2 'Failed password' /var/log/auth.log | less -S
zcat /var/log/auth.log.1.gz | less            # archive compressée, sans extraction sur disque
less +F /var/log/auth.log                    # nouvelles lignes en direct
```

## Pièges

- `less` ne trie pas les résultats : applique `sort` **avant** `less` si l'ordre doit changer.
- `-S` cache visuellement la fin d'une ligne jusqu'au défilement horizontal ; elle n'est pas supprimée.
- La recherche `/motif` parcourt ce qui a été transmis à `less` ; pour réduire les données dès le départ, filtre avec `grep`.

Voir aussi : [lecture des fichiers dans Linux fondamentaux](../fondamentaux/fichiers-recherche.md#lire-un-fichier-long) et [mise en forme des journaux VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).
