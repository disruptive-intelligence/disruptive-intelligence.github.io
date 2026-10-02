---
title: "sed"
commande: "sed"
---
# `sed`

Transforme du texte ligne par ligne : remplacer, supprimer, n'afficher qu'une partie — dans la sortie, ou dans le fichier avec `-i`.

```bash title="Syntaxe"
sed '<adresse><commande>' <fichier>   # affiche le résultat ; -i modifie le fichier
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Élément | Ce qu'il fait |
|---|---|
| `s/<ancien>/<nouveau>/` · `…/g` | Remplace la première occurrence de chaque ligne · toutes |
| `s/<ancien>/<nouveau>/I` | Sans tenir compte des majuscules (GNU) |
| `s#/var/www#/srv/www#` | Même chose avec un autre séparateur : pratique pour des chemins |
| `/<motif>/d` · `5d` · `$d` | Supprime les lignes qui contiennent le motif · la ligne 5 · la dernière |
| `-n '10,20p'` | N'affiche que les lignes 10 à 20 |
| `-i` · `-i.bak` | Modifie le fichier · en gardant une copie `.bak` |
| `-E` | Expression régulière étendue (groupes `( )` réutilisables avec `\1`) |
| `-e … -e …` · `;` | Plusieurs commandes à la suite |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `sed -i.bak 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config` | Dans le fichier (copie `.bak` gardée), la ligne qui commence par `PermitRootLogin yes` devient `no` |
| `sed '/^#/d; /^$/d' fichier` | Retire les commentaires et les lignes vides |
| `sed -n '/Oct  2 03:/p' auth.log` | N'affiche que les lignes du 2 octobre entre 3 h et 4 h |
| `sed -E 's/([0-9]+)\.([0-9]+)/\2.\1/' fichier` | Inverse les deux nombres de part et d'autre d'un point (groupes `\1`, `\2`) |

## Pièges

- Sans `-i`, **rien n'est modifié** : sed affiche seulement le résultat — pratique pour vérifier avant.
- `-i` sans suffixe est irréversible : toujours `-i.bak` sur un fichier de configuration.
- Les `/` d'un chemin cassent `s/…/…/` : les échapper (`\/`) ou changer de séparateur (`s#…#…#`).
