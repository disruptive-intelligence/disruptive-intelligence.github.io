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

## Exemples

??? example kw-cs-more "Remplacer"
    ```bash
    sed 's/http:/https:/' fichier          # 1re occurrence de chaque ligne
    sed 's/http:/https:/g' fichier         # toutes les occurrences
    sed 's/erreur/ERREUR/gI' fichier       # sans casse (GNU)
    sed '3s/foo/bar/' fichier              # seulement à la ligne 3
    sed '/^Listen/s/80/8080/' ports.conf   # seulement sur les lignes qui commencent par Listen
    sed 's#/var/www#/srv/www#g' site.conf  # des chemins : autre séparateur
    ```

??? example kw-cs-more "Supprimer, extraire"
    ```bash
    sed '/^#/d' fichier                     # sans les commentaires
    sed '/^\s*$/d' fichier                  # sans les lignes vides ou blanches
    sed '1d' export.csv                     # sans la 1re ligne (en-tête)
    sed -n '5,10p' fichier                  # lignes 5 à 10
    sed -n '/BEGIN/,/END/p' fichier         # de la ligne BEGIN à la ligne END
    sed -n '$p' fichier                     # la dernière ligne
    ```

??? example kw-cs-more "Modifier un fichier"
    ```bash
    sudo sed -i.bak 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config   # décommente et change le port, copie .bak
    sudo sed -i '/intranet.local/d' /etc/hosts                         # retire une ligne
    sed -i '1i # Fichier généré automatiquement' config.ini            # ajoute une ligne au début
    sed -i '$a derniere_ligne' fichier                                 # ajoute une ligne à la fin
    sed -i 's/\r$//' script.sh                                         # retire les fins de ligne Windows (CRLF)
    ```

??? example kw-cs-more "Groupes et regex étendues"
    ```bash
    sed -E 's/([0-9]{1,3}\.){3}[0-9]{1,3}/x.x.x.x/g' access.log   # masque les adresses IP
    sed -E 's/^([^:]+):.*/\1/' /etc/passwd                        # garde ce qui précède le premier « : »
    sed -E 's/(.*)@(.*)/\2 \1/' emails.txt                        # domaine, puis utilisateur
    ```
