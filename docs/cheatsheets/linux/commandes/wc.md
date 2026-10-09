---
title: "wc"
commande: "wc"
---
# `wc`

Compte les lignes, les mots, les octets ou les caractères d'un fichier ou d'une sortie de commande. Très utile **après** un filtre ou une déduplication.

```bash title="Syntaxe"
wc -l <fichier>   # ou : <commande> | wc -l
```

Pour comprendre : [Administration Linux, ch. 3](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/03-chapitre-3-lire-le-contenu-des-fichiers.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qui est compté |
|---|---|
| `-l` | Retours à la ligne |
| `-w` | Mots séparés par des blancs |
| `-c` | Octets |
| `-m` | Caractères (peuvent différer des octets en UTF-8) |
| `-L` | Longueur de la plus longue ligne affichée |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `wc -l /var/log/auth.log` | Nombre de lignes, suivi du nom du fichier |
| `… | sort -u | wc -l` | Nombre de valeurs **différentes** |
| `grep -c 'motif' fichier` | Nombre de lignes qui contiennent le motif, sans `wc` |
| `grep -oE 'motif' fichier | wc -l` | Nombre d'**occurrences** du motif (plusieurs possibles par ligne) |

## Pièges

- `wc -l` compte les **fins de ligne** : sans retour final, la dernière ligne n'est pas comptée.
- Sur un fichier en argument, `wc` affiche aussi son nom ; derrière un pipe, seulement le nombre.
- Sans `sort -u` avant, `wc -l` compte les occurrences, pas les valeurs distinctes.
- Compter des lignes de log n'est pas compter des connexions : un événement peut résumer plusieurs paquets ou sessions.

## Exemples

??? example kw-cs-more "Fichiers et sorties"
    ```bash
    wc -l /var/log/auth.log                # retours à la ligne du fichier
    find /etc -type f 2>/dev/null | wc -l  # chemins de fichiers trouvés
    wc -c rapport.txt                      # taille en octets
    wc -m rapport.txt                      # nombre de caractères
    ```

## Cas concrets

??? example kw-cs-cas "Pare-feu : combien de ports de destination différents ?"
    ```bash
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 |
      sort -n -u | wc -l                 # tout le journal
    grep -F '|action=allow|' firewall.log |
      grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
      sort -n -u | wc -l                 # seulement action=allow
    ```
    Retirer `| wc -l` pour voir la liste avant de la compter.

??? example kw-cs-cas "VPN : combien d'échecs d'authentification ?"
    ```bash
    grep -F 'status=failure' vpn.log | wc -l     # lignes qui contiennent un échec
    ```
    Juste seulement avec **un événement par ligne** : sinon, [les séparer d'abord](sed.md#cas-concrets). `grep -c` donne le même nombre ; `grep -oE 'status=failure' vpn.log | wc -l` compte les occurrences, même collées sur une ligne.

Voir aussi : [`grep`](grep.md) · [`sort`](sort.md) · [Compter les valeurs distinctes d'un champ](../fondamentaux/texte-filtres.md#compter-les-valeurs-distinctes-dun-champ)
