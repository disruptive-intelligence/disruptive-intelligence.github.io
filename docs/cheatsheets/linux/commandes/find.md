---
title: "find"
commande: "find"
---
# `find`

Parcourt une arborescence et sélectionne les fichiers selon leur nom, leur type, leur taille, leur date, leur propriétaire ou leurs droits ; peut ensuite agir sur chacun.

```bash title="Syntaxe"
find <où> <critères> <action>   # sans action : affiche les chemins
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Option | Ce qu'elle fait |
|---|---|
| `-name "<motif>"` · `-iname` | Nom (motif du shell, entre guillemets) · sans tenir compte des majuscules |
| `-type f` · `d` · `l` | Fichier ordinaire · dossier · lien symbolique |
| `-size +100M` · `-size -1k` | Plus de 100 Mo · moins de 1 Ko (unités `k`, `M`, `G`) |
| `-mtime -7` · `-mmin -60` | Modifié il y a moins de 7 jours · moins de 60 minutes |
| `-newermt "<date>"` | Modifié après cette date (`! -newermt` : avant) |
| `-user <nom>` · `-group <nom>` | Appartient à cet utilisateur · à ce groupe |
| `-perm -4000` · `-perm -o+w` | Bit SUID présent · modifiable par tous |
| `-maxdepth <N>` | Pas plus de N niveaux sous le point de départ |
| `-xdev` | Reste sur ce système de fichiers (ne descend pas dans `/proc`, les disques montés…) |
| `!` · `-o` | Négation · OU (par défaut les critères s'enchaînent en ET) |
| `-ls` | Affiche le détail de chaque fichier (droits, taille, date) |
| `-exec <cmd> {} \;` · `{} +` | Lance la commande pour chaque fichier · une seule fois avec tous |
| `-delete` | Supprime les fichiers trouvés |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `find / -perm -4000 -type f 2>/dev/null` | Depuis la racine, les fichiers ordinaires qui ont le bit SUID ; les « Permission denied » sont jetés |
| `find /var/www -type f -mmin -60 -ls` | Les fichiers de `/var/www` modifiés dans la dernière heure, avec leur détail |
| `find / -xdev -newermt "2026-10-01 08:00" ! -newermt "2026-10-01 12:00"` | Modifiés entre 8 h et 12 h, sur ce disque seulement |
| `find /var/log -name "*.log" -size +100M -exec ls -lh {} \;` | Les journaux de plus de 100 Mo, listés avec leur taille |
| `find /home -type f \( -name "*.sh" -o -name "*.py" \)` | Les scripts shell OU Python (parenthèses échappées) |

## Pièges

- Le motif se met **entre guillemets** : sans, le shell remplace `*.conf` par les fichiers du dossier courant avant que `find` ne le voie.
- `-delete` placé avant les critères supprime tout ce qui est parcouru : tester d'abord la même commande sans `-delete`.
- `-mtime -1` = moins de 24 h ; `-mtime 1` = entre 24 et 48 h ; `-mtime +1` = plus de 48 h.
- `-maxdepth` se place juste après le point de départ, avant les autres critères.

## Exemples

??? example kw-cs-more "Par nom et par type"
    ```bash
    find . -name "*.log"                             # les .log sous le dossier courant
    find / -type f -iname "*passw*" 2>/dev/null      # nom qui contient « passw », sans casse
    find /etc -maxdepth 1 -type f -name "*.conf"     # dans /etc seulement, pas les sous-dossiers
    find / -type f -name "access.log*" 2>/dev/null   # journaux d'accès, rotations comprises
    find / -type d -name ".git" 2>/dev/null          # dépôts Git (dossiers .git)
    find . -type l -ls                               # liens symboliques et leur cible
    ```

??? example kw-cs-more "Par date"
    ```bash
    find /var/log -type f -mtime -1                  # modifiés depuis moins de 24 h
    find /home -type f -mmin -30                     # modifiés dans les 30 dernières minutes
    find /tmp -type f -mtime +7                      # pas modifiés depuis plus de 7 jours
    find / -xdev -type f -newer /etc/passwd 2>/dev/null   # plus récents que /etc/passwd
    find / -xdev -type f -newermt "2026-10-01" ! -newermt "2026-10-02" 2>/dev/null   # modifiés le 1er octobre
    find /var/www -type f -cmin -60                  # droits ou propriétaire changés dans l'heure
    ```

??? example kw-cs-more "Par taille, propriétaire et droits"
    ```bash
    find / -xdev -type f -size +500M 2>/dev/null     # plus de 500 Mo
    find . -type f -empty                            # fichiers vides
    find / -user www-data -type f 2>/dev/null        # fichiers de www-data
    find / -nouser 2>/dev/null                       # propriétaire disparu (compte supprimé)
    find / -perm -4000 -type f 2>/dev/null           # SUID
    find / -perm -2000 -type f 2>/dev/null           # SGID
    find /etc -type f -perm -o+w 2>/dev/null         # configuration modifiable par tous
    find / -xdev -type d -perm -o+w ! -perm -1000 2>/dev/null   # dossiers modifiables par tous, sans sticky bit
    ```

??? example kw-cs-more "Agir sur les résultats"
    ```bash
    find . -name "*.sh" -exec chmod +x {} \;                    # rendre les scripts exécutables
    find . -type f -name "*.php" -exec grep -l "eval(" {} +      # fichiers PHP qui contiennent eval(
    find / -type f -name "*.conf" -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
    find . -type f -print0 | xargs -0 sha256sum > empreintes.txt  # empreintes de tous les fichiers (espaces gérés)
    find . -type f | wc -l                                       # nombre de fichiers
    find /var/log -name "*.gz" -mtime +30 -delete                # supprimer les archives de plus de 30 jours
    ```

??? example kw-cs-more "Investigation et CTF"
    ```bash
    find / -name "flag*" 2>/dev/null                              # un flag (CTF)
    find / -type f \( -name "id_rsa*" -o -name "*.kdbx" -o -name "*.pem" \) 2>/dev/null   # clés, coffres de mots de passe
    find / -type f \( -name "*.bak" -o -name "*.old" -o -name "*~" \) 2>/dev/null         # sauvegardes oubliées
    find /home /root -name ".*_history" -type f 2>/dev/null       # historiques de commandes
    find /tmp /var/tmp /dev/shm -type f -perm -u+x 2>/dev/null    # exécutables dans les dossiers temporaires
    find / -xdev -type f -mmin -10 2>/dev/null                    # ce qui vient de bouger
    ```
