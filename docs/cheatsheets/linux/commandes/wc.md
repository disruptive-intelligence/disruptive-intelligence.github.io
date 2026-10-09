---
title: "wc"
commande: "wc"
---
# `wc`

Compte les lignes, les mots, les octets ou les caractères d'un fichier ou d'une sortie de commande. Très utile **après** un filtre ou une déduplication.

```bash title="Syntaxe"
wc -l <fichier>   # ou : <commande> | wc -l
```

## Les options utiles

| Option | Ce qui est compté |
|---|---|
| `-l` | Retours à la ligne |
| `-w` | Mots séparés par des blancs |
| `-c` | Octets |
| `-m` | Caractères (peuvent différer des octets en UTF-8) |
| `-L` | Longueur de la plus longue ligne affichée |

## Cas concrets déjà rencontrés

### Combien de ports de destination différents ?

```bash title="Tout le pare-feu"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d '=' -f 2 |
  sort -n -u | wc -l
```

```bash title="Seulement action=allow"
grep -F '|action=allow|' firewall.log |
  grep -oE 'dstport=[0-9]+' | cut -d '=' -f 2 |
  sort -n -u | wc -l
```

`wc -l` compte ici les **lignes de la liste dédupliquée**. Sans `sort -u`, il compterait les occurrences, pas les ports distincts. Pour voir la liste avant de compter, enlève simplement `| wc -l`.

### Événements filtrés

```bash title="Lignes contenant un échec"
grep -F 'status=failure' vpn.log | wc -l
```

Ce nombre est juste **si un événement occupe une ligne**. Si plusieurs événements sont collés, [sépare-les d'abord](sed.md#separer-des-evenements-vpn-colles). `grep -c` compte les lignes correspondantes directement ; `grep -oE 'status=failure' vpn.log | wc -l` compterait les **occurrences du motif**, qui peuvent être plusieurs sur une ligne.

## Autres exemples

```bash title="Fichiers et sorties"
wc -l /var/log/auth.log                # retours à la ligne du fichier
find /etc -type f 2>/dev/null | wc -l  # chemins de fichiers trouvés
wc -c rapport.txt                      # taille en octets
wc -m rapport.txt                      # nombre de caractères
```

## Pièges

- `wc -l` compte les **caractères de fin de ligne** ; un fichier dont la dernière ligne n'a pas de retour final peut afficher un total inférieur au nombre de lignes visibles.
- Sur un fichier passé en argument, `wc` affiche aussi son nom ; sur un pipeline, il n'affiche que le nombre.
- Compter des lignes de log n'est pas forcément compter des connexions : un événement peut résumer plusieurs paquets ou sessions.

Voir aussi : [`grep`](grep.md), [`sort`](sort.md) et [l'analyse des ports dans Forensic réseau](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal).
