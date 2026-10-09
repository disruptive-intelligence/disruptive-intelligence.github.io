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

Remplace `198.51.100.23` par la source recherchée. Ne filtre pas sur `action=deny` si tu veux compter **toutes les tentatives** : une connexion autorisée vise elle aussi un port. Pour un autre format de journal, adapte `src=` et `dstport=` aux noms de champs réellement présents.

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
