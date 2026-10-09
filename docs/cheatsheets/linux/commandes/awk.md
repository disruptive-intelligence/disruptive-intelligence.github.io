---
title: "awk"
commande: "awk"
---
# `awk`

Découpe chaque ligne en champs et permet de filtrer, réarranger ou calculer — là où `cut` ne fait que découper.

```bash title="Syntaxe"
awk -F'<séparateur>' '<condition> {<action>}' <fichier>   # séparateur par défaut : espaces et tabulations
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Élément | Ce qu'il représente |
|---|---|
| `-F':'` | Séparateur de champs (ici `:`) |
| `$1`, `$2`… · `$0` · `$NF` | Champ 1, 2… · la ligne entière · le dernier champ |
| `NR` · `NF` | Numéro de la ligne en cours · nombre de champs de cette ligne |
| `FS` · `OFS` | Séparateur des champs en entrée · séparateur des champs en sortie |
| `{print $1, $3}` | Affiche les champs 1 et 3, séparés par un espace |
| `$3 >= 1000` · `/motif/` · `$7 ~ /bash$/` | Condition : comparaison · ligne qui contient · champ qui correspond à une regex |
| `!~` · `&&` · `||` | Ne correspond pas · ET · OU |
| `BEGIN {…}` · `END {…}` | Avant la première ligne · après la dernière (totaux) |
| `-v seuil=1000` | Passe une variable du shell au programme |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `awk -F: '$3 >= 1000 {print $1, $6}' /etc/passwd` | Séparateur `:` ; lignes dont l'UID (champ 3) vaut au moins 1000 ; affiche le nom et le dossier personnel |
| `awk -F: '$7 !~ /(nologin|false)$/ {print $1}' /etc/passwd` | Les comptes dont le shell n'est ni `nologin` ni `false` : ceux qui peuvent se connecter |
| `awk '{print $1}' access.log` | La première colonne de chaque ligne : l'IP du client |
| `awk '{s += $10} END {print s}' access.log` | Additionne la 10e colonne (octets envoyés) et affiche le total à la fin |
| `awk 'NR==10, NR==20' fichier` | Les lignes 10 à 20 |

## Pièges

- Le programme se met entre **guillemets simples** : entre guillemets doubles, le shell remplace `$1` avant awk.
- Par défaut, plusieurs espaces de suite comptent pour un seul séparateur (`cut -d' '`, lui, compte chaque espace).
- `print $1, $2` sépare par un espace ; `print $1 $2` colle les deux champs.

## Exemples

??? example kw-cs-more "Découvrir les colonnes d'un fichier"
    ```bash
    awk -F '\t' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' fichier.log   # $1, $2… et leur valeur
    awk -F '\t' 'NR==1 {print NF; exit}' fichier.log                                            # nombre de champs
    ```
    `NR==1` : la première ligne ; `exit` arrête la lecture. `-F '\t'` fixe `FS` ; `BEGIN {OFS="\t"}` fixe le séparateur de sortie. `|` : `-F '|'` ; espaces successifs : pas de `-F`.

??? example kw-cs-more "Extraire et compter le champ 3 d'un TSV simple"
    ```bash
    awk -F '\t' '{print $3}' fichier.log                               # le champ
    awk -F '\t' '{print $3}' fichier.log | sort -u | wc -l             # nombre de valeurs différentes
    awk -F '\t' '{print $3}' fichier.log | sort | uniq -c | sort -rn   # occurrences par valeur
    ```
    Une entrée par ligne, pas de séparateur dans les valeurs. CSV à guillemets ou JSON : un parseur adapté.

??? example kw-cs-more "Afficher des colonnes"
    ```bash
    awk '{print $1}' access.log                 # 1re colonne (l'IP du client)
    awk '{print $NF}' fichier                   # dernière colonne
    awk -F: '{print $1, $7}' /etc/passwd        # nom et shell
    awk -F: '{print $1 " -> " $6}' /etc/passwd  # nom et dossier, avec un séparateur choisi
    awk -F, '{print $2}' export.csv             # 2e colonne d'un CSV simple
    awk '{print NR ": " $0}' fichier            # numérote les lignes
    ```

??? example kw-cs-more "Filtrer des lignes"
    ```bash
    awk -F: '$3 == 0 {print $1}' /etc/passwd                      # comptes d'UID 0
    awk -F: '$3 >= 1000 && $7 ~ /bash/ {print $1}' /etc/passwd     # comptes humains avec bash
    awk '$9 == 404 {print $7}' access.log                          # URL en 404 (journal nginx/apache)
    awk '$9 >= 500' access.log                                     # requêtes en erreur serveur
    awk '/Failed password/ {print $(NF-3)}' /var/log/auth.log      # IP des échecs SSH (4e champ depuis la fin)
    awk 'NR > 1' export.csv                                        # tout sauf l'en-tête
    awk 'length($0) > 200' fichier                                 # lignes de plus de 200 caractères
    ```

??? example kw-cs-more "Compter et additionner"
    ```bash
    awk '{n[$1]++} END {for (ip in n) print n[ip], ip}' access.log | sort -rn | head   # requêtes par IP
    awk '{s += $10} END {print s/1024/1024 " Mo"}' access.log      # volume envoyé
    awk '{s += $2} END {print s/NR}' mesures.txt                   # moyenne de la 2e colonne
    df -h | awk 'NR > 1 && $5+0 > 80 {print $6, $5}'               # partitions remplies à plus de 80 %
    ```

??? example kw-cs-more "Avec d'autres commandes"
    ```bash
    ps aux | awk '$3 > 50 {print $2, $11}'                 # PID et programme à plus de 50 % de CPU
    ip -4 -o addr show | awk '{print $2, $4}'               # interface et adresse
    last | awk '{print $1}' | sort | uniq -c | sort -rn     # connexions par utilisateur
    cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'   # comptes qui ont un shell, et lequel
    ```

## Cas concrets

??? example kw-cs-cas "VPN : heure, utilisateur, IP publique, résultat, sans connaître l'ordre des champs"
    ```bash
    awk -F'|' '{
      ts=$1; user=ip=status="-"
      for (i=2; i<=NF; i++) {
        if ($i ~ /^srcuser=/) user=$i
        else if ($i ~ /^publicip=/) ip=$i
        else if ($i ~ /^status=/) status=$i
      }
      print ts "|" user "|" ip "|" status
    }' vpn.log | column -t -s '|'
    ```
    La boucle examine les `NF` champs et garde ceux qui portent le bon nom ; `-` = champ absent. Ordre connu et stable : `awk -F'|' '{print $1 "|" $5 "|" $7 "|" $9}' vpn.log | column -t -s '|'`. Événements collés : [`sed`](sed.md#cas-concrets) d'abord.

??? example kw-cs-cas "Pare-feu : combien de ports distincts chaque source a-t-elle visés ?"
    ```bash
    awk -F '|' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' firewall.log   # vérifier le format
    awk -F'|' '{
      src=port=""
      for (i=1; i<=NF; i++) {
        if ($i ~ /^src=/) src=substr($i, 5)
        else if ($i ~ /^dstport=/) port=substr($i, 9)
      }
      if (src != "" && port != "") print src, port
    }' firewall.log | sort -u | awk '{n[$1]++} END {for (src in n) print n[src], src}' | sort -rn
    ```
    `substr($i, 5)` retire `src=`, `substr($i, 9)` retire `dstport=`. `sort -u` sur la paire « source port » : plusieurs connexions vers le même port ne comptent qu'une fois. Le cas complet : [Forensic › Pare-feu](../../forensic/reseau/journaux/pare-feu-vpn.md)

??? example kw-cs-cas "VPN : combien de réussites et d'échecs ?"
    ```bash
    awk -F'|' '{
      for (i=1; i<=NF; i++)
        if ($i ~ /^status=/) n[$i]++
    } END {
      for (status in n) print n[status], status
    }' vpn.log | sort -rn
    ```
    Un événement par ligne (sinon `sed` d'abord). Pour la chronologie d'une source, garder aussi horodatage et IP plutôt que des totaux.

??? example kw-cs-cas "Zeek `http.log` : filtrer et présenter des colonnes"
    ```bash
    awk -F '\t' '/^#fields/ {for (i=2; i<=NF; i++) printf "$%d %s\n", i-1, $i; exit}' http.log   # positions déclarées
    awk -F '\t' '!/^#/ {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' http.log         # valeurs de la 1re requête
    awk -F '\t' 'BEGIN {OFS="\t"} !/^#/ {print $3, $8, $10, $15}' http.log |
      head -n 20 | column -t -s $'\t'                                    # client, méthode, URI, code (positions Bro)
    awk -F '\t' '!/^#/ && $15 == 200 {print $3, $8, $10, $15}' http.log  # réponses 200
    ```
    `#fields` commence par un libellé : le 1er nom correspond à `$1`. `!/^#/` saute les métadonnées. `$15` = `status_code` dans l'ancien Bro de l'exercice, `$17` dans Zeek actuel : vérifier, ou passer par les noms, `zeek-cut id.orig_h method uri status_code < http.log`, puis `awk -F '\t' '$4 == 200'`. Le cas complet : [Forensic › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

Voir aussi : [Forensic › Pare-feu et VPN](../../forensic/reseau/journaux/pare-feu-vpn.md) · [Repérer les champs d'un fichier](../fondamentaux/texte-filtres.md#reperer-les-champs-dun-fichier)
