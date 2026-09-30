---
title: Fichiers, recherche et flux
source: IT/01_Linux/Notion_Linux.md
note: Linux — prises de notes
up:
- - Linux — prises de notes
  - index.md
---

## Recherche & gérer fichiers / répertoires [which, find, locate]

| Commande | Description |
| --- | --- |
| which | Retourne chemin du binaire exécuté pour vérifier si un programme est présent |
| find | Permet de trouver fichiers/répertoires et de filtrer (taille, date…) puis d’agir sur les résultats |
| locate | Chercher avec find peut-être long. Locate s’appuie sur base locale de chemins (index) donc bien plus rapide. |

- which : Retourne chemin du binaire exécuté pour vérifier si un programme est présent
    
    ```bash
    which binaire
    
    - Ex : which python
    ```
    
- find : Permet de trouver fichier et de filtrer (taille, date…) puis d’agir sur les résultats
    
    ```bash
    find location options
    
    - Ex : find / -type f -name *.conf -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
    
    - Option : 
    	-Type recherché (fichier) : -type f 
    	-name "*.conf" : tous fichiers finissant par .conf
    	-user root : Filtre sur le propriétaire
    	-size +20k : Taille > 20 KiB
    	-newermt 2020-03-03 : Plus récent que date
    	-exec ls -al {} \; : Exécute la commande pour chaque résultat ({} = placeholder). Le \; échappe le ;.
    	2>/dev/null : Redirige erreur pour pas polluer
    	/ est la racine, peut faire . pour dossier courant
    ```
    
    ```bash
    # Trouver tous les fichiers access.log
    find / -type f -name access.log* # 	/ est la racine, peut faire . pour dossier courant
    
    # Trouver IP de multiples fichiers 
    find . -type f -name access.log* | grep -ro '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'
    
    # Trouver sans sensibilité à la case iname
    find / -type f -iname "$file" 2>/dev/null
    ```
    
- locate : Locate s’appuie sur base locale de chemins (index) donc bien plus rapide.
    
    ```bash
    sudo updatedb # Met à jour l'index
    
    locate *.conf
    ```
    

### Supprimer fichiers

| Commandes | Description |
| --- | --- |
| rm | remove (supprimer) |
| -f | force (pas de confirmation, ignore certains messages d’erreur) |
| -r | recursive (descend dans les sous-dossiers et supprime tout) |
| Find | Supprimer de manière sûre  |
| ls -la "/chemin/vers/dossier"
 | Reflexe sécu pour vérifier ce que * va cibler |

- Supprimer dossier avec tout contenu (y compris sous-dossiers)
    
    ```bash
    rm -rf /path/to/directory
    ```
    
- Supprimer tout contenu d’un dossier sans supprimer dossier
    
    ```bash
    rm -rf /chemin/vers/dossier/*
    
    # Inclure aussi fichiers/dossiers cachés
    
    rm -rf /chemin/vers/dossier/{*,.*}
    ```
    
- Supprimer uniquement fichiers d’un dossier (sans sous-dossier)
    
    ```bash
    rm -f /chemin/vers/dossier/{*,.*}
    ```
    
- Supprimer avec espace dans chemin
    
    ```bash
    rm -rf "/path/to the/directory/"*
    ```
    
- Supprimer **récursivement** tous les fichiers avec extension .ext puis le répertoire courant
    
    ```bash
    find . -name "*.doc" -type f -delete
    
    rm **/*.doc
    ```
    

### Divers

- Afficher uniquement nom des fichiers contenant string spécifiques
    
    ```bash
    grep "500" * -l
    
    grep -l "500" * 2>/dev/null 
    ```
    
- Afficher chemin relatif fichiers
    
    ```bash
    ls -rt
    ```
    
- Afficher toutes les lignes contenant string sans afficher nom fichiers
    
    ```bash
    grep -rh "XXX"
    
    grep -Rh --include='access.log*' '500' .
    ```
    
- Trouver IP de multiples fichiers
    
    ```bash
    find . -type f -name access.log* | grep -ro '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'
    ```
    
- Compter nombre de fichiers dans directory
    
    ```bash
    ls -l | wc -l 
    find . -type f | wc -l
    ```
    
- Compter nombre de lignes dans fichier qui contiennent la chaîne XX
    
    ```bash
    grep -c "GET" access.log
    grep "GET" access.log | wc -l
    ```
    

 

## Filtrer contenus fichiers [grep, tail, more, less…]

| Commande | Description |
| --- | --- |
| **more** | Affiche un fichier page par page. |
| **less** | Pager avancé : navigation avant/arrière, recherche, aide intégrée. |
| **head** | Affiche début fichier |
| **tail** | Affiche la fin d’un fichier |
| **sort** | Trie lignes (alpha/num). Options : `-n` numérique, `-r` inverse. |
| uniq  | supprimer les doublons consécutifs |
| **grep** | Filtre par motif . `-i` insensible casse,  |
| **cut** | Extrait des champs par délimiteur. Options : `-d <sep>`, `-f <cols>`. |
| **tr** | Transforme/supprime des caractères. Options : remplacer, `-d` supprimer. |
| **column** | Formate en tableau aligné. Option : `-t` (table). |
| **awk** | Traitement en colonnes (sélection, formatage). Option : `-F <sep>`. |
| **sed** | Éditeur de flux (substitutions, suppressions). Syntaxe : `s/old/new/g`. |
| **wc** | Compte lignes/mots/octets. Options : `-l`, `-w`, `-c`. |
| nl | numéroter les lignes  |
| paste | Peut prendre plusieurs fichiers et les ouvrir côte à côte |
| expand / unexpand | Permet de ré ajuster les tabulations / espaces pour éviter certains problèmes d’affichages de fichiers mal formatés au niveau de l’allignement du texte |
| join  | Fusionne lignes de deux fichiers en se basant sur un champ commun |
| split | Divise fichier volumineux en morceaux plus petits plus faciles à gérezr |

- more : Affiche fichier page par page
    
    ```bash
    cat /etc/passwd | more
    ```
    
- less : Affiche exclusivement contenu du fichier
    
    ```bash
    less /etc/passwd
    ```
    
- head : Affiche 10 premières lignes (Par défaut)
    
    ```bash
    head /etc/passwd
    
    head -n 15 /var/log/syslog # Affiche 15 lignes
    ```
    
- Tail : Affiche 10 dernières lignes
    
    ```bash
    tail /etc/passwd
    
    tail -n 20 /var/log/syslog # Affiche 20 lignes
    
    tail -f /var/log/syslog # Affiche en temps réels
    ```
    
- sort : Permet de trier par ordre alphabétique/numérique
    
    ```bash
    sort fichier.txt
    cat /etc/passwd | sort
    
    # Affiche début pas par root mais part chiffres puis majuscule...
    -n : tri numérique
    -r : ordre inverse
    -u supprimer doublon (équivaut sort | uniq
    
    sort fichier.txt | uniq -c | sort -nr # Top lignes plus fréquentes
    ```
    
- uniq : supprimer les doublons consécutifs
    - Supprime ligne identique qui se suivent uniquement, donc presque toujours avec sort parce que si doublon séparée tjrs là : book paper book, donc sort
    
    ```bash
    uniq fichier.txt 
    sort fichier.txt | uniq 
    
    -c : Compte les occurences
    -d : Ne montrer que lignes dupliquées
    -u : Ne montrer que lignes uniques (une seule fois)
    
    sort fichier.txt | uniq -c | sort -nr # Top lignes plus fréquentes
    
    ```
    
- grep : Filtrer par motif
    
    ```bash
    grep fox fichier.txt
    
    cat /etc/passwd | grep "/bin/bash"
    # Exclure :
    cat /etc/passwd | grep -v "false\|nologin"
    
    - Option :
    	# -i : Insensible à la case
    grep -i somepattern fichier
    	# -e : Explicitement modèle suivant (utile si tiret pour évider confusion avec paramêtre)
    grep -e "-v" /path/to/some/file.conf
    	# -o : Voir ligne partie exacte de la ligne qui correspond
    grep -o fox fichier.txt
    	# -f : Recherches plusieurs patterns à partir d'un fichier
    grep -f patterns.txt fichier.txt
    	# -c : Compter lignes ont le patterns
    grep -c fox fichier.txt
    
    ```
    
    - Divers exemples
    
    ```bash
    # Afficher uniquement nom des fichiers contenant string spécifiques	
    grep "500" * -l 
    
    # Afficher toutes les lignes contenant string sans afficher nom fichiers
    grep -rh "XXX"
    grep -Rh --include='access.log*' '500' .
    
    # Compter nombre de lignes dans fichier qui contiennent la chaîne XX
    grep -c "GET" access.log
    grep "GET" access.log | wc -l
    
    # Trouver tous les fichiers qui se terminent par .txt
    ls /somedir | grep '.txt$'
    ```
    
- cut : Extraire des champs avec délimiteur
    
    ```bash
    cat /etc/passwd | cut -d":" -f1
    
    - Option : 
    	-d : Délimiteur du contenu à enlever après
    	-f : Position de la ligne que l'on veut sortir
    	
    # Sortir contenu 2ème ligne 
    cut -f 2 file.txt
    
    # Utiliser délémiteur, permet de prendre symbole comme "fin"
    # Fichier The quick brown; fox jumps over the lazy  dog
    cut -f 1 -d ";" sample.txt # Affiche que jusqua The quick brown
    ```
    
- tr : Remplacer / Supprimer caractères
    
    ```bash
    cat /etc/passwd | tr ":" " " # Remplace : par rien
    
    # Dans un premier temps on prend caractères qu'on veut remplacer "caractère_à_remplacer" puis contenu par quoi le remplacer " " rien pour ne rien mettre
    
    tr 'a-z' 'A-Z' # Passe tout en maj
    
    tr -d '0-9' # Supprimer des caractères
    
    tr -s ' ' # Supprimer espaces inutiles
    ```
    
- Column : Présenter proprement en tableau
    
    ```bash
    cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | column -t
    ```
    
- awk : Langage de traitement de textes en colonnes
    
    ```bash
    cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'
    
    # $1 = 1re colonne, $NF = dernière
    ```
    
- sed : Editeur de flux (substitutions)
    
    ```bash
    cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'
    
    # "s/ancien/nouveau/g remplace partout sur la ligne
    ```
    
- wc : Compter lignes/mots/octets
    
    ```bash
    wc fichier.txt # Nombre lignes mots octets
    cat /etc/passwd | wc
    
    -l : nombre de lignes
    -w : seulement les mots
    -c : seulement les octets
    -m : caractères (UTF-8)
    
    # Compter nombre de fichiers dans directory 
    ls -l | wc -l 
    find . -type f | wc -l
    
    # Compter nombre de lignes dans fichier qui contiennent la chaîne XX
    grep "GET" access.log | wc -l
    ```
    
- nl : Numéroter les lignes
    
    ```bash
    nl fichier.txt # Ajoute numéros de ligne devant chaque ligne
    ```
    
- paste : sortie côte à côte
    
    ```bash
    paste fichier1.txt fichier2.txt  
    paste -d ':' fichier1.txt fichier2.txt # ajoute délimiteur
    paste -s fichier.txt # Colle ligne sur une seule ligne
    ```
    
- expand / unexpand : Re ajuster tabulation et espace
    
    ```bash
    expand -t 4 fichiers.txt # Chaque tab vaut 4 espaces
    expand fichier.txt > result.txt # Save sortie
    
    unexpand -t 4 fichier.txt 
    unexpand -a fichier.txt # -a Indique convertir toutes occurences de 8 espaces en tab
    ```
    
- join : Joindre fichiers sur même ligne
    
    ```bash
    join file1.txt file2.txt 
    ```
    
- split : Découpe fichier en plusieurs morceaux
    - Crée part_aa, part_ab …
    
    ```bash
    # Par nombre de lignes
    split -l 1000 grand_fichier.txt part_
    
    # Par taille en octets
    split -b 10M grosse.iso part_
    
    -l N : N lignes par fichier
    -b N : N octets par fichier (k, M, G)
    -d : utiliser suffixes numériques (part_00...)
    ```
    

### REGEX

Permet de grouper et de contrôler répétition de motif

| Opérateurs | Description |
| --- | --- |
| `(a)` | Parenthèse : Groupent une partie de la regex, le groupe est traité comme une unité |
| `[a-z]` | Crochets : Classe de caractères (Liste à faire correspondre) |
| `{1,10}` | Accolades : Quantificateur, répéter motif précdent n à m fois. |
| `|` | OR operator, montre résultat quand un des deux expressions matchent |
| `.*` | Affiche résultats uniquement lorsque les deux expressions sont présentes et correspondent dans l’ordre spécifié. |

### Opérateur OR

Chercher ligne contenant motif spécifique

```bash
grep -E "(my|false)" /etc/passwd
```


### Opérateur ET

Chercher ligne contenant mot1 puis plus loin mot2 (dans cet ordre)

```bash
grep -E "(my.*false)" /etc/passwd
```


## Gestion des permissions [chmod, SUID…]

### Introduction

Chaque objets a un propriétaire (user) et un groupe, les droits définissent ce que chacun peut lire (r), écrire (w) ou exécuter (x). 

- Pour entrer dans répertoire (le “traverser”) nécessite droit exécuter (x) sur répertoire. X sur répertoire n’autorise pas à exécuter fichiers, seulement à le traverser.
- Pour exéc fichier, il faut exéc sur fichier.
- Pour modifier contenu d’un répertoire (créer/supp/rename), il faut w sur le rep (et x pour y entrer)
- Trois différents types de permissions :
    - (`r`) - Read
    - (`w`) - Write
    - (`x`) - Execute
    
    ```bash
    cry0l1t3@htb[/htb]$ ls -l /etc/passwd- rwx rw- r--   1 root root 1641 May  4 23:42 /etc/passwd
    - --- --- ---   |  |    |    |   |__________|
    |  |   |   |    |  |    |    |        |_ Date
    |  |   |   |    |  |    |    |__________ File Size
    |  |   |   |    |  |    |_______________ Group
    |  |   |   |    |  |____________________ User
    |  |   |   |    |_______________________ Number of hard links
    |  |   |   |_ Permission of others (read)
    |  |   |_____ Permissions of the group (read, write)
    |  |_________ Permissions of the owner (read, write, execute)
    |____________ File type (- = File, d = Directory, l = Link, ... )
    ```
    
    
    
    ### Système Octal (r=4, w=2, x=1)
    
    Trois permissions possibles par classe : **r (4)**, **w (2)**, **x (1)**.
    On additionne pour chaque triplet → octal
    
    ```bash
    Binary Notation:                4 2 1  |  4 2 1  |  4 2 1
    ----------------------------------------------------------
    Binary Representation:          1 1 1  |  1 0 1  |  1 0 0
    ----------------------------------------------------------
    Octal Value:                      7    |    5    |    4
    ----------------------------------------------------------
    Permission Representation:      r w x  |  r - x  |  r - -
    ```
    
    ```
    rwx  rw-  r--   →  7    6    4
    111  110  100   →  7    6    4
    
    Si on veut que other ait r et x alors 755
    ```
    

### Modifier permissions (chmod)

Références de groupes de permissions  :

- **u** = owner
- **g** = group
- **o** = others
- **a** = all
    - et les opérateurs **`+`** (ajouter) / **`-`** (retirer).

```bash
cry0l1t3@htb[/htb]$ ls -l shell

-rwxr-x--x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```


```bash
chmod a+r shell : ajoute lecture pour tous

Ex : 

cry0l1t3@htb[/htb]$ chmod a+r shell && ls -l shell
-rwxr-xr-x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```


```bash
chmod 754 shell : Fixer via notation octale (lecture seule pour other)
```


- Compréhension droits
    
    aaaah punaise je pensais qu'entre l'owner, le groupe, et other il y avait toujours un - donc - : fichier rwx : droit proprio - : séparation r-x : droit groupe sans write - : séparation rw- : droit other sans exéc mais noooon je pensais à mal en pensant au - de séparation -rwxr-xr-x : est donc bon en effet tous les rwx des différentes personnes et groupes senchaines !
    
    Il n’y a **aucun tiret de séparation** entre owner / group / others. C’est un **bloc continu de 10 caractères** :
    
    ```
    [type][u r w x][g r w x][o r w x]
       1      2-4      5-7      8-10
    
    ```
    
    - 1er caractère = **type** ( fichier, `d` dossier, `l` lien…)
    - ensuite **9 positions fixes** : `rwx` du **proprio (u)**, puis `rwx` du **groupe (g)**, puis `rwx` des **autres (o)**
    - un droit **absent** s’affiche par  **à la place** (ce n’est pas un séparateur)
    
    Donc :
    
    ```
    -rwxr-xr-x
     ^  ^^^ ^^^ ^^^
     |   u   g   o
    type
    
    ```
    
    Mini-mémo:
    
    - ordre **toujours** `r w x` par bloc
    - ON/OFF par position (pas de “déplacement” des lettres)
    - numéros utiles : `r=4, w=2, x=1` → `u g o` (ex: 7=111=rwx, 5=101=r-x, 4=100=r--)

### Modifier propriétaire (chown)

```bash
chown <user>:<group> <file/directory>

- Ex : 
	chown root:root shell && ls -l shell
```


### Identité : UID, GID, PID

- PID (Process ID) : Chaque programme qui tourne a un numéro unique
    - PID 1 = Systemd
- UID (User ID) : Matricule d’utilisateur
    - UID 0 = root
    - UID 1 à 999 = Réservé aux Services/Daemons (ex : user www-data pour serveur web). N’ont pas le droit de se connecter à un écran, servent juste à faire tourner process en fond.
    - UID 1000+ = Utilisateurs normaux
- GID (Group ID) : Chaque utilisateur appartient à un groupe principal (souvent le même nom que l'utilisateur). Ça permet de partager des fichiers entre collègues.

### SUID et SGID

Linux permet permissions spéciales sur fichiers via bits Set User ID (SUID) et Set Group ID (SGID). Fonctionnent comme accès temporaires. Font s’exécuter programme avec droit du owner du fichier (SUID) ou du groupe du fichier (SGID) et non avec ceux de l’user qui lance. Ex : admin autorise actions précises nécessitant privilèges, même si user n’a pas normalement les droits. Visuellement, présence indiquée par s au lieu de x :

- SUID remplace le x du bloc propriétaire (u)
- SGID remplace le x du bloc groupe (g)
- Trouver SUID
    
    ```bash
    find / -perm -u=s -type f 2>/dev/null
    ```
    

### Sticky bit

Protège fichiers dans un répertoire partagé, seul propriétaire du fichier, proprio du répertoire ou root peut supp/rename. 

## File descriptors et redirections [STDIN, STDOUT, STDERR]

File descriptor (FD) sous Unix/Linux est une référence, gérée par noyau qui identifie ressource ouverte (fichier, socket…). Sous Windows, on parle de file handle. “Ticket” que l’OS utilise pour savoir quelle ressource lire/écrire.

- STDIN - 0 : Entrée standard
- STDOUT - 1 : Sortie standard
- STDERR - 2 : Sortie d’erreur

### STDIN et STDOUT

On dnne une entrée (STDIN) à cat, une fois “entrée”, ressort sur la sortie standard (STDOUT) 



### STDOUT et STDERR

Les résultats “normaux” sur STDOUT, les erreurs sur STDERR, ex : Permission denied

- On peut rediriger erreur 2>/dev/null.



### Rediriger STDOUT dans un fichier

```bash
find /etc/ -name shadow 2>/dev/null > results.txt
cat results.txt

# Ici, seules lignes réussies sont envoyées
# Attention : > : écrase fichier s'il existe
```




### Rediriger STDOUT et STDERR vers fichiers séparés

```bash
find /etc/ -name shadow 2> stderr.txt 1> stdout.txt
```




### Redirection de STDIN

< Sert à rediriger l’entrée standard, grossièrement, fait comme cat mais utile quand commande exige l’entrée via STDIN.

```bash
cat < stdout.txt
```




### Rediriger STDOUT ajouter au lieu d’écraser

>> ajoute à la fin du fichier (au lieu d’écraser)

```bash
find /etc/ -name passwd >> stdout.txt 2>/dev/null
cat stdout.txt
```




### Rediriger flux STDIN vers fichier

<<  Envoie flux d’entrée jusqu’au marqueur. (EOF, END, TXT..)

```bash
cat << EOF > stream.txt
```




## Pipe

```bash
- | grep mot
- | wc : Permet de compter nombre de mot
	- Nombre package : dpkg -l | grep '^ii' | wc -l
```
