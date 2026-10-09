---
title: "Texte et filtres"
cours:
  - library/it/linux/administration-linux/index.md
---

# Texte et filtres

Découper, trier, compter et transformer la sortie d'une commande ou le contenu d'un fichier.

Les incontournables : `cut` · `sort | uniq -c` · `grep -oE` · `sort -u | wc -l` · `sed` · `awk` · `| tee`
{ .kw-cs-top }

## Extraire

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

### Extraire et compter des ports de destination distincts

Dans un journal de pare-feu où les champs sont écrits `clé=valeur` (par exemple `srcport=20036|dstport=443|action=allow`), **`dstport`** est le port visé ; `srcport` est le port utilisé par la source. Lis d'abord quelques lignes pour vérifier le nom du champ et le séparateur :

```bash title="Repérer le format"
head -n 3 firewall.log
grep -oE 'dstport=[0-9]+' firewall.log | head
```

Puis garde seulement la valeur numérique, supprime les doublons et affiche la liste :

```bash title="Lister les ports distincts"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n -u
```

```bash title="Compter les ports distincts"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n -u | wc -l
```

`grep -oE` extrait chaque champ correspondant, `cut` retire `dstport=`, `sort -n -u` trie numériquement et ne garde qu'une ligne par port, puis `wc -l` compte ces lignes. Pour voir **combien d'entrées** concernent chaque port, utilise plutôt :

```bash title="Fréquence par port"
grep -oE 'dstport=[0-9]+' firewall.log | cut -d= -f2 | sort -n | uniq -c | sort -rn
```

Si le journal contient plusieurs sources et que la question porte sur une seule, sélectionne d'abord ses lignes (ici, les champs sont séparés par `|`) :

```bash title="Ports distincts pour une seule source"
grep -F '|src=198.51.100.23|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u
```

Remplace `198.51.100.23` par la source recherchée. Pour compter **toutes les tentatives**, garde les actions autorisées et refusées : une connexion autorisée vise elle aussi un port. Pour un autre format de journal, adapte `src=` et `dstport=` aux noms de champs réellement présents.

### Filtrer par action avant de compter

Pour ne regarder que les connexions **autorisées** dans ce journal à champs séparés par `|`, filtre d'abord les lignes sur le champ entier `|action=allow|` :

```bash title="Lister les ports autorisés distincts"
grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u
```

```bash title="Compter les ports autorisés distincts"
grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n -u | wc -l
```

```bash title="Nombre d'entrées autorisées par port"
grep -F '|action=allow|' firewall.log | grep -oE 'dstport=[0-9]+' | cut -d= -f2 | sort -n | uniq -c | sort -rn
```

Le premier `grep` garde les lignes autorisées ; le second extrait `dstport=…` ; `cut` ne conserve que le numéro. Ensuite, `sort -u` liste chaque port une fois, `wc -l` compte ces ports distincts, tandis que `uniq -c` compte les occurrences de chaque port **après le tri**. Une occurrence correspond ici à un champ trouvé dans le journal, pas forcément à une connexion distincte. Pour étudier une seule source *et* une seule action, ajoute le filtre `grep -F '|src=<IP>|'` avant l'extraction, en remplaçant `<IP>`.

### Gabarits pour d'autres journaux ou fichiers texte

Remplace les trois valeurs de départ : `FICHIER` est le chemin du fichier, `CRITERE` est le texte fixe qui doit figurer dans la ligne, et `MOTIF` est l'expression régulière à extraire. Par exemple, le critère pourrait être `ERROR` et le motif `code=[0-9]+` dans un journal d'application. Ces gabarits conservent la correspondance entière, avec son éventuel préfixe (`code=`) ; ajoute `cut -d= -f2` avant le tri si tu veux seulement la valeur d'un champ `clé=valeur`.

```bash title="À adapter une fois"
FICHIER='chemin/vers/fichier.log'
CRITERE='texte-à-garder'
MOTIF='expression-régulière-à-extraire'
```

```bash title="Lister les valeurs distinctes"
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort -u
```

```bash title="Compter les valeurs distinctes"
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort -u | wc -l
```

```bash title="Compter les occurrences par valeur"
grep -F "$CRITERE" "$FICHIER" | grep -oE "$MOTIF" | sort | uniq -c | sort -rn
```

Si tu n'as **aucun critère de ligne**, commence directement par `grep -oE "$MOTIF" "$FICHIER"` et garde la fin du pipeline voulue (`sort -u`, `sort -u | wc -l` ou `sort | uniq -c | sort -rn`). Vérifie d'abord quelques correspondances avec `grep -oE "$MOTIF" "$FICHIER" | head` : un motif trop large fausse tous les comptes.

Si tu veux compter des **lignes entières distinctes** au lieu d'une valeur extraite, utilise `grep -F "$CRITERE" "$FICHIER" | sort -u | wc -l`. Deux lignes qui diffèrent seulement par leur horodatage seront alors comptées séparément.

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

Pour remettre en lignes un export dont les événements sont collés, puis aligner les champs `|` et isoler les informations utiles, voir [l'exemple VPN de la fiche journaux réseau](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).

## Mettre en forme et trier un fichier texte

### Aligner des champs délimités

Regarde d'abord quelques lignes : `head -n 3 fichier.txt` ou `head -c 500 fichier.txt` si elles sont très longues. Si les champs sont séparés par `|`, affiche-les en tableau et parcours les lignes larges :

```bash title="Afficher en colonnes"
column -t -s '|' fichier.txt | less -S
```

Pour ne voir que certains champs, vérifie leur position sur une ligne, puis sélectionne-les **avant** d'aligner :

```bash title="Garder les colonnes 1, 3 et 5"
awk -F'|' '{print $1 "|" $3 "|" $5}' fichier.txt | column -t -s '|'
```

`awk -F'|'` découpe la ligne sur `|` ; `$1`, `$3` et `$5` désignent les champs choisis. Si l'ordre varie mais que les champs sont nommés (`clé=valeur`), cherche plutôt les **noms** comme dans [l'exemple VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).

### Trier avant d'aligner

```bash title="Tri alphabétique, numérique et par première colonne"
sort fichier.txt
sort -n nombres.txt
sort -t '|' -k1,1 evenements.txt | column -t -s '|' | less -S
```

`sort` compare le texte ; `sort -n` compare des nombres ; `-t '|' -k1,1` trie sur le premier champ. **Trie avant `column`** : l'alignement ajoute des espaces qui peuvent changer les clés de tri. Un tri textuel sur des horodatages ISO donne l'ordre chronologique seulement si leur format et leur fuseau horaire sont identiques.

### Séparer des événements collés

Si plusieurs événements commencent par `AAAA-MM-JJT` et sont séparés par **un espace** sur la même ligne, GNU `sed` peut remettre chaque événement sur sa propre ligne avant l'affichage :

```bash title="Un événement par ligne, sans modifier le fichier"
sed -E 's/ ([0-9]{4}-[0-9]{2}-[0-9]{2}T)/\n\1/g' evenements.txt | column -t -s '|' | less -S
```

Vérifie que ce motif marque bien le début d'un événement dans ton fichier ; s'il possède déjà une ligne par événement, garde seulement `column -t -s '|' fichier.txt | less -S`. Le cas SOC complet figure dans [Journaux réseau — VPN](../../forensic/reseau/journaux/pare-feu-vpn.md#rendre-lisible-un-export-vpn-separe-par).

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
| `sed 's/a/b/g'` | Remplacer | `-i` : modifie le fichier |
| `tr` | Changer ou supprimer des caractères | `tr 'a-z' 'A-Z'` |
| `column -t` | Aligner en tableau | `column -t -s':'` |
