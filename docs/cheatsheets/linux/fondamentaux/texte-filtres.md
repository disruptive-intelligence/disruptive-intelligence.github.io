---
title: "Texte et filtres"
cours:
  - library/it/linux/administration-linux/index.md
---

# Texte et filtres

Découper, trier, compter et transformer la sortie d'une commande ou le contenu d'un fichier.

Les incontournables : `cut` · `sort | uniq -c` · `grep -oE` · `sort -u | wc -l` · `sed` · `awk` · `| tee`
{ .kw-cs-top }

Chaque commande en détail, avec ses cas concrets : [`grep`](../commandes/grep.md), [`sed`](../commandes/sed.md), [`awk`](../commandes/awk.md), [`cut`](../commandes/cut.md), [`sort`](../commandes/sort.md), [`uniq`](../commandes/uniq.md), [`wc`](../commandes/wc.md), [`column`](../commandes/column.md) et [`less`](../commandes/less.md).

## Extraire

### Repérer les champs d'un fichier

```bash title="Commande"
head -n 3 <fichier>                                # le format, le séparateur (head -c 500 si les lignes sont très longues)
head -n 1 <fichier> | tr '<sép>' '\n' | nl -ba     # un champ par ligne, numéroté (champs vides compris)
awk -F '<sép>' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' <fichier>   # $1, $2… et leur valeur
```

```bash title="Exemple"
awk -F '\t' 'NR==1 {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' fichier.log
head -n 1 fichier.log | tr '\t' '\n' | nl -ba
awk -F '\t' 'NR==1 {print NF; exit}' fichier.log   # nombre de champs (NF ; NR = numéro de ligne)
```

| Séparateur | `awk` | `tr` |
|---|---|---|
| Tabulations (TSV) | `-F '\t'` | `tr '\t' '\n'` |
| Barre verticale (`|`) | `-F '|'` | `tr '|' '\n'` |
| Virgules sans guillemets (CSV simple) | `-F ','` | `tr ',' '\n'` |
| Deux-points | `-F ':'` | `tr ':' '\n'` |
| Espaces multiples | Sans `-F` | Préférer `awk` |

Un événement par ligne seulement. Le numéro ne donne pas le nom du champ : lire l'en-tête ou le schéma. CSV avec virgules entre guillemets, JSON : un parseur adapté.

??? example kw-cs-cas "Zeek `http.log` : quelle colonne contient l'IP source ?"
    Champs séparés par des tabulations ; les premières lignes sont des métadonnées `#`, pas des requêtes (`NR==1` ne marche donc pas).
    ```bash
    grep -m1 '^#fields' http.log                                       # noms des champs, dans l'ordre
    awk -F '\t' '/^#fields/ {for (i=2; i<=NF; i++) printf "$%d = %s\n", i-1, $i; exit}' http.log   # numéro de chaque nom
    grep -m1 -v '^#' http.log | tr '\t' '\n' | nl -ba                  # valeurs de la première requête
    zeek-cut id.orig_h < http.log | sort | uniq -c | sort -rn | head  # IP sources, par nom de champ
    grep -v '^#' fichier.tsv | cut -f3 | sort | uniq -c | sort -rn     # TSV générique, IP vérifiée en colonne 3
    ```
    Scénario complet : [Forensic réseau › Zeek HTTP](../../forensic/reseau/journaux/web.md#zeek-bro-analyser-httplog)

### Extraire une colonne

```bash title="Commande"
cut -d'<séparateur>' -f<N> <fichier>   # -d séparateur, -f numéro du champ
```

```bash title="Exemple"
cut -d: -f1 /etc/passwd | head -4
```

??? example "Sortie"
    ```text
    root
    daemon
    bin
    sys
    ```

```bash title="Exemple 2"
awk -F: '$3 >= 1000 {print $1, $6}' /etc/passwd   # comptes « humains » et leur dossier
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

### Extraire avec une expression régulière

```bash title="Commande"
grep -oE '<regex>' <fichier>   # -o : seulement la correspondance, -E : regex étendue
```

```bash title="Exemple"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' /var/log/auth.log | sort -u
```

??? example "Sortie"
    ```text
    192.168.1.23
    192.168.1.40
    203.0.113.7
    ```

### Exclure des lignes (commentaires, lignes vides)

```bash title="Commande"
grep -v '<motif>' <fichier>   # -v : inverse la sélection
```

```bash title="Exemple"
grep -vE '^\s*(#|$)' /etc/ssh/sshd_config
```

??? example "Sortie"
    ```text
    Include /etc/ssh/sshd_config.d/*.conf
    KbdInteractiveAuthentication no
    UsePAM yes
    X11Forwarding yes
    Subsystem sftp /usr/lib/openssh/sftp-server
    ```

## Compter et trier

### Trier des lignes

```bash title="Commande"
sort <fichier>                        # alphabétique ; -n numérique, -r inverse, -u sans doublons
sort -t '<sép>' -k<N>,<N> <fichier>   # sur le champ N seulement
```

```bash title="Exemple"
sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S   # par horodatage (1er champ), puis aligné
```

```bash title="Exemple 2"
sort fichier.txt        # ordre alphabétique
sort -n nombres.txt     # ordre numérique
```

Trier **avant** `column` : les espaces d'alignement changent les clés. Un tri textuel d'horodatages ISO n'est chronologique que si format et fuseau sont identiques.

### Trier et compter les occurrences

```bash title="Commande"
<commande> | sort | uniq -c | sort -rn   # uniq ne regroupe que des lignes voisines : sort d'abord
```

```bash title="Exemple"
cut -d' ' -f1 /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
       4821 203.0.113.7
        312 192.168.1.23
         41 192.168.1.40
    ```

### Compter les valeurs distinctes d'un champ

```bash title="Commande"
grep -oE '<champ>=[^|]+' <fichier> | cut -d= -f2 | sort -u                     # quelles valeurs ?
grep -oE '<champ>=[^|]+' <fichier> | cut -d= -f2 | sort -u | wc -l             # combien de valeurs différentes ?
grep -oE '<champ>=[^|]+' <fichier> | cut -d= -f2 | sort | uniq -c | sort -rn   # combien de fois chacune ?
```

```bash title="Exemple"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n -u | wc -l   # nombre de ports de destination différents
```

| Question | Fin de pipeline |
|---|---|
| Quelles valeurs différentes ? | `sort -u` (`sort -n -u` pour des nombres) |
| Combien de valeurs différentes ? | `sort -u | wc -l` |
| Combien d'occurrences par valeur ? | `sort | uniq -c | sort -rn` |
| Combien de lignes entières différentes ? | `sort -u | wc -l` sans extraction (un horodatage différent = une ligne différente) |

Filtrer les lignes **avant** d'extraire (`grep -F '<texte>' <fichier> |` en tête). Vérifier le motif avec `| head` : un motif trop large fausse tous les comptes.

```bash title="Gabarit à adapter"
FICHIER='chemin/vers/fichier.log'           # le fichier
CRITERE='texte-à-garder'                    # texte fixe que la ligne doit contenir (ex. ERROR)
MOTIF='expression-régulière-à-extraire'     # ce qu'on extrait (ex. code=[0-9]+)
grep -oE "$MOTIF" "$FICHIER" | head                                             # vérifier le motif
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort -u                     # valeurs distinctes
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort -u | wc -l             # leur nombre
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort | uniq -c | sort -rn   # occurrences par valeur
grep -F "$CRITERE" "$FICHIER" | sort -u | wc -l                                 # lignes entières distinctes
```

Sans critère de ligne : commencer par `grep -oE "$MOTIF" "$FICHIER"`. Le motif garde son préfixe (`code=`) : ajouter `| cut -d= -f2` avant le tri pour la seule valeur.

??? example kw-cs-cas "Pare-feu : combien de ports différents ont été visés ?"
    Journal `…|src=…|srcport=20036|dstport=443|action=allow|…` : `dstport` = port visé, `srcport` = port de la source.
    ```bash
    head -n 3 firewall.log                                                          # vérifier noms de champs et séparateur
    grep -oE 'dstport=[0-9]+' firewall.log | head                                   # le motif trouve bien le champ
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n -u               # liste des ports
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n -u | wc -l       # leur nombre
    grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n | uniq -c | sort -rn   # entrées par port
    ```

??? example kw-cs-cas "Pare-feu : quels ports une seule source a-t-elle visés ?"
    ```bash
    grep -F '|src=198.51.100.23|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u
    ```
    Toutes les tentatives comptent : une connexion autorisée vise aussi un port, ne pas filtrer sur `action`.

??? example kw-cs-cas "Pare-feu : seulement les connexions autorisées"
    ```bash
    grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u             # ports autorisés
    grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u | wc -l     # leur nombre
    grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n | uniq -c | sort -rn   # entrées par port
    ```
    `|action=allow|` avec ses `|` : le champ entier, pas un bout de valeur. Une source *et* une action : ajouter `grep -F '|src=<IP>|' |` en tête. Une occurrence = un champ trouvé dans le journal, pas forcément une connexion.

Scénario complet : [Forensic réseau › Pare-feu](../../forensic/reseau/journaux/pare-feu-vpn.md#lister-et-compter-les-ports-vises-dans-un-journal)
{ .kw-cs-meta }

### Compter des lignes

```bash title="Commande"
wc -l <fichier>   # -w mots, -c octets
```

```bash title="Exemple"
grep -c "Failed password" /var/log/auth.log
```

??? example "Sortie"
    ```text
    137
    ```

## Transformer

### Remplacer du texte

```bash title="Commande"
sed 's/<ancien>/<nouveau>/g' <fichier>   # affiche le résultat sans modifier le fichier
```

```bash title="Exemple"
echo "http://intranet.local/rapport" | sed 's/http:/https:/g'
```

??? example "Sortie"
    ```text
    https://intranet.local/rapport
    ```

```bash title="Exemple 2"
sudo sed -i.bak 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
# modifie le fichier sur place et garde une copie .bak
```

!!! warning "Attention"
    `sed -i` modifie le fichier : toujours `-i.bak` pour garder l'original.

### Changer un séparateur ou la casse

```bash title="Commande"
tr '<de>' '<vers>'   # tr -d '<car>' : supprime le caractère
```

```bash title="Exemple"
head -2 /etc/passwd | tr ':' ' '
```

??? example "Sortie"
    ```text
    root x 0 0 root /root /bin/bash
    daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
    ```

```bash title="Exemple 2"
tr 'A-Z' 'a-z' < liste.txt   # tout en minuscules
```

### Afficher en tableau aligné

```bash title="Commande"
column -t -s'<séparateur>'   # -t : tableau, -s : séparateur d'entrée
```

```bash title="Exemple"
head -3 /etc/passwd | column -t -s:
```

??? example "Sortie"
    ```text
    root    x  0  0  root    /root      /bin/bash
    daemon  x  1  1  daemon  /usr/sbin  /usr/sbin/nologin
    bin     x  2  2  bin     /bin       /usr/sbin/nologin
    ```

```bash title="Exemple 2"
column -t -s '|' fichier.txt | less -S                                 # champs séparés par |, lignes larges défilables
awk -F'|' '{print $1 "|" $3 "|" $5}' fichier.txt | column -t -s '|'   # seulement les champs 1, 3 et 5 (positions vérifiées)
```

Choisir les champs **avant** d'aligner. Si leur ordre varie mais qu'ils sont nommés (`clé=valeur`) : chercher les noms, comme dans le [cas VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).

### Séparer des événements collés sur une ligne

```bash title="Commande"
sed -E 's/ (<début d'un événement>)/\n\1/g' <fichier>   # retour à la ligne avant chaque début d'événement (GNU sed)
```

```bash title="Exemple"
sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' evenements.txt | column -t -s '|' | less -S   # événements qui commencent par AAAA-MM-JJT
```

Vérifier d'abord que le motif marque bien un début d'événement (`head -c 500`). Déjà une ligne par événement : `column -t -s '|' fichier.txt | less -S` suffit.

??? example kw-cs-cas "VPN : export `|` illisible, événements collés"
    Le cas complet (séparer, aligner, garder heure, utilisateur, IP et résultat) : [Forensic réseau › VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par)

## Enchaîner et enregistrer

### Envoyer la sortie dans un fichier

```bash title="Commande"
<commande> > <fichier>    # remplace le contenu du fichier
<commande> >> <fichier>   # ajoute à la fin
<commande> 2>/dev/null    # jette les messages d'erreur
```

```bash title="Exemple"
find / -perm -4000 2>/dev/null > suid.txt
```

Pour comprendre : [Administration Linux, ch. 7](../../../library/it/linux/administration-linux/02-partie-2-manipuler-le-systeme-de-fichiers/03-chapitre-7-liens-redirections-et-tuyaux.md)
{ .kw-cs-meta }

### Voir la sortie et l'enregistrer en même temps

```bash title="Commande"
<commande> | tee <fichier>   # -a : ajoute au lieu de remplacer
```

```bash title="Exemple"
sudo ss -tunap | tee connexions.txt
```

??? example "Sortie"
    ```text
    Netid State  Recv-Q Send-Q Local Address:Port  Peer Address:Port Process
    tcp   ESTAB  0      0      192.168.1.50:22     192.168.1.23:51544 users:(("sshd",pid=5123,fd=4))
    ```

```bash title="Exemple 2"
sudo ss -tunap | tee -a journal-intervention.txt
```

## Vue d'ensemble

| Opérateur | Effet |
|---|---|
| `>` | Écrit la sortie dans un fichier (le remplace) |
| `>>` | Ajoute la sortie à la fin du fichier |
| `2>` | Envoie les erreurs ailleurs (`2>/dev/null` : les jette) |
| `2>&1` | Envoie les erreurs au même endroit que la sortie |
| `|` | Passe la sortie à la commande suivante |
| `| tee <fichier>` | Affiche et enregistre en même temps (`-a` : ajoute) |

| Outil | Rôle | Exemple |
|---|---|---|
| `cut` | Garder une colonne | `cut -d':' -f1 /etc/passwd` |
| `grep -oE` / `grep -v` | Extraire un motif / exclure des lignes | `grep -v '^#'` |
| `sort | uniq -c | sort -rn` | Compter les occurrences, les plus fréquentes en tête | Top des IP d'un journal |
| `wc -l` | Compter les lignes | — |
| `sort -u | wc -l` | Compter les valeurs différentes | Ports distincts d'un pare-feu |
| `tr '<sép>' '\n' | nl -ba` | Numéroter les champs d'une ligne | Repérer la colonne voulue |
| `sort -t '<sép>' -k1,1` | Trier sur un champ | Événements par horodatage |
| `sed -E 's/ (…)/\n\1/g'` | Remettre un événement par ligne | Export VPN collé |
| `sed 's/a/b/g'` | Remplacer | `-i` : modifie le fichier |
| `tr` | Changer ou supprimer des caractères | `tr 'a-z' 'A-Z'` |
| `column -t` | Aligner en tableau | `column -t -s':'` ; `| less -S` pour les lignes larges |
