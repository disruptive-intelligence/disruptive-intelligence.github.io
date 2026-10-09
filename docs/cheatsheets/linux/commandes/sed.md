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

## Cas concrets

??? example kw-cs-cas "VPN : séparer des événements collés sur une même ligne"
    ```bash
    sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log            # un événement par ligne, vpn.log inchangé
    sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' vpn.log |
      column -t -s '|' | less -S                                       # puis aligné et défilable
    ```
    Le motif : un espace suivi d'une date ISO ; `\1` remet la date capturée, `\n` crée la ligne (GNU sed). Vérifier avant avec `head -c 500 vpn.log` : si chaque événement a déjà sa ligne, inutile.

??? example kw-cs-cas "Pare-feu : extraire les ports avec `sed -n …p`"
    ```bash
    sed -nE 's/.*[|]dstport=([0-9]+).*/\1/p' firewall.log | sort -n -u   # -n + p : seulement les lignes où la substitution a réussi
    ```
    Même logique pour tout champ `clé=valeur` : adapter le nom du champ et le séparateur.

??? example kw-cs-cas "Partager un extrait sans les adresses IP"
    ```bash
    sed -E 's/([0-9]{1,3}\.){3}[0-9]{1,3}/[IP]/g' firewall.log | head   # copie affichée, fichier inchangé
    ```
    La regex repère une forme IPv4, sans vérifier que chaque octet est entre 0 et 255.

??? example kw-cs-cas "Export Windows ou gros fichier : nettoyer et sélectionner avant d'analyser"
    ```bash
    sed 's/\r$//' export.txt | sed '/^[[:space:]]*$/d' | less   # sans fins de ligne Windows ni lignes vides
    sed -n '1,20p' vpn.log                                      # les 20 premières lignes seulement
    sed -n '/status=failure/p' vpn.log                          # lignes qui contiennent un échec
    ```
    Événements collés : les séparer d'abord pour traiter chacun.

Voir aussi : [Forensic › VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par) · [Séparer des événements collés](../fondamentaux/texte-filtres.md#separer-des-evenements-colles-sur-une-ligne)
