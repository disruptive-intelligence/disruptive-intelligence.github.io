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
| `NR` · `NF` | Numéro de la ligne · nombre de champs de la ligne |
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

## Cas concrets déjà rencontrés

### VPN : construire une vue lisible sans supposer l'ordre des champs

Dans un export `|` avec `srcuser=…`, `publicip=…` et `status=…`, les numéros de colonnes peuvent changer. Cherche plutôt chaque **nom de champ**. Si plusieurs événements sont collés sur une ligne, sépare-les d'abord avec [`sed`](sed.md#separer-des-evenements-vpn-colles).

```bash title="Heure, utilisateur, IP publique, résultat"
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

`NF` est le nombre de champs de la ligne ; la boucle les examine tous. Les valeurs `-` rendent visible un champ manquant. `column` aligne **après** l'extraction. Si l'ordre est connu et stable, `awk -F'|' '{print $1 "|" $5 "|" $7 "|" $9}' vpn.log | column -t -s '|'` est plus court ; vérifie d'abord les positions.

### Pare-feu : ports distincts par source

Pour le format `|src=…|dstport=…|`, produis une paire « source port » par événement, supprime les paires répétées, puis compte les ports distincts de chaque source :

```bash title="Nombre de ports distincts par source"
awk -F'|' '{
  src=port=""
  for (i=1; i<=NF; i++) {
    if ($i ~ /^src=/) src=substr($i, 5)
    else if ($i ~ /^dstport=/) port=substr($i, 9)
  }
  if (src != "" && port != "") print src, port
}' firewall.log | sort -u | awk '{n[$1]++} END {for (src in n) print n[src], src}' | sort -rn
```

`substr($i, 5)` retire `src=` ; `substr($i, 9)` retire `dstport=`. `sort -u` agit sur la paire entière : plusieurs connexions vers le même port par la même source ne comptent qu'une fois. La sortie est classée par nombre de ports décroissant.

### Compter des réussites et des échecs

```bash title="Répartition par statut dans un export |"
awk -F'|' '{
  for (i=1; i<=NF; i++)
    if ($i ~ /^status=/) n[$i]++
} END {
  for (status in n) print n[status], status
}' vpn.log | sort -rn
```

Ce comptage suppose **un événement par ligne**. Si ce n'est pas le cas, passe d'abord par le `sed` de l'exemple VPN. Pour examiner la chronologie d'une source précise, conserve aussi l'horodatage et l'IP plutôt que de te limiter aux totaux.

Voir les scénarios complets : [pare-feu et VPN dans Forensic réseau](../../forensic/reseau/journaux/pare-feu-vpn.md).

### Zeek HTTP : filtrer et présenter des champs TSV

Un `http.log` Zeek texte est séparé par des tabulations. Ses lignes `#fields` décrivent les colonnes : inspecte-les avant d'utiliser `$3`, `$8`, `$10` ou `$15`. `!/^#/` ignore les métadonnées.

```bash title="Afficher les positions déclarées par Zeek"
awk -F '\t' '/^#fields/ {for (i=2; i<=NF; i++) printf "$%d %s\n", i-1, $i; exit}' http.log
```

```bash title="Client, méthode, URI, code : positions confirmées"
awk -F '\t' 'BEGIN {OFS="\t"} !/^#/ {print $3, $8, $10, $15}' http.log |
  head -n 20 | column -t -s $'\t'
```

```bash title="Requêtes ayant reçu un code 200"
awk -F '\t' '!/^#/ && $15 == 200 {print $3, $8, $10, $15}' http.log
```

Quand le schéma change, `zeek-cut id.orig_h method uri status_code < http.log` sélectionne les champs par **nom**. Tu peux ensuite filtrer sa sortie avec `awk -F '\t' '$4 == 200'`. Le scénario complet et ses précautions sont dans [Forensic réseau : Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog).
