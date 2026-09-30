---
title: Notions Linux
source: IT/01_Linux/Notion_Linux.md
format: synthese
---

### Usages courants

#### Linux Structure

#### Composants

| **Composants** | **Description** |
| --- | --- |
| Bootloarder | Morceau de code qui guide process de démarrage pour lancer OS. Ex : GRUB, charge noyau et ses paramètres avant de passer la main au système; |
| Noyau (OS Kernel) | Composant principal de l’OS. Gère ressources des périphériques au niveau hardware.  |
| Daemons | Service en arrière-plan. Assure bon fonctionnement de fonctions clés (plannification, impression, multimédias…). Se chargent après le démarrage, gérés par ***systemd***. |
| OS Shell | Interface entre l’OS et l’user. Permet d’intérragir  |
| Serveur graphique | Fournit sous système graphique appelé “X” ou “X-server”. Permettant exécution de programmes graphiques localement ou à distance sur système de fenêtrage. Ex : Wayland ou X11. |
| Gestionnaire de fenêtres (Window manager) | Appelé interface graphique (GUI). Environnement de bureau inclut souvent appli (fichiers, navigateur web…). Ex : GNOME, KDE… |
| Utilitaire | Programmes qui remplissent fonctions particulières pour l’user. Ex : ls, cp, find, curl… |

#### Architecture Linux

| **Couche** | **Description** |
| --- | --- |
| Hardware | Périphériques matériels comme la RAM, CPU, disque…  |
| Kernel | Coeur de l’OS. Fonction de virtualiser et contrôler les ressources matérielles,  CPU, mémoire allouée, données… Donne à chaque processus ressources virtuelles. Fait interface entre programmes et le matériel via appels système. |
| Shell | CLI dans laquelle user saisit commandes pour effectuer fonctions du kernel. Lance des processus et permet de chainer outils. |
| Utilitaires système | Mettent à disposition de l’user l’ensemble des fonctionnalités de l’OS.  |

#### Hiérarchie du système de fichier

| **Chemin** | **Description** |
| --- | --- |
| / | Répertoire racine, contient fichiers nécessaires pour boot l’OS avant que les autres filesystems soient montés. |
| /bin | Contient les binaires de commandes essentiels Ex : ls, cp, mv… |
| /boot | Contient bootloader, exécutable du noyau et les fichiers requis pour démarrer. Ex : Config GRUB… |
| /dev | Contient fichiers de périphériques pour accéder aux périphériques matériel connectés. |
| /etc | Fichiers de configuration systèmes locaux et des apps. |
| /home | Chaque user possède sous-dossier. Ex : /home/cam |
| /lib | Bibliothèques partagées nécessaires au démarrage du système. |
| /media | Point de montage des médias amovibles. |
| /mnt | Point de montage temporaire pour systèmes de fichiers. |
| /opt | Fichiers optionnels, comme outils tiers. |
| /root | Dossier perso de l’user root. |
| /sbin | Exécutable utilisés pour l’admin système. Ex : ip, mount, fsck… |
| /tmp | Dossier pour fichiers temporaires du système & des programmes. |
| /usr | Contient exécutables, bibliothèques, pages de manuels… |
| /var | Données variables : logs, mail, fichiers d’apps web, cron… Ex : /var/log |

#### Boot Process

Lorsque l’on appuie sur le bouton “Power” :

1. BIOS / UEFI (Firmware) : La carte mère se réveille, vérifie que le matériel (RAM, CPU, Disque) fonctionne (c'est le POST - *Power-On Self-Test*) et cherche un périphérique sur lequel démarrer.
2. Bootloader (GRUB) : Le système charge un petit programme (souvent GRUB) situé au tout début du disque. Son rôle est de laisser l'utilisateur choisir l'OS et de charger le noyau en mémoire.
    - Rôle : Menu bleu au démarrage, demande si on veut lancer Linux, Mode récup…
3. Kernel : Le noyau Linux se décompresse, prend le contrôle du processeur, monte un système de fichiers temporaire (initramfs) pour charger les pilotes nécessaires, puis monte le vrai disque dur.
4. Init (Systemd) : Le Kernel initialise le matériel puis lance le tout premier programme. Son identifiant (PID) est 1.

#### BIOS / MBR & UEFI / GPT

- **L'Ancienne École (Legacy) : BIOS + MBR**
    - **BIOS (Basic Input/Output System) :** C'est le vieux logiciel de la carte mère (souvent un écran bleu/gris avec du texte pixelisé). Il est simple mais limité.
    - **MBR (Master Boot Record) :** C'est la façon dont le BIOS note les adresses sur le disque dur. C'est comme un vieux carnet d'adresses papier : il n'a pas beaucoup de pages.
- **La Nouvelle Technologie : UEFI + GPT**
    - **UEFI (Unified Extensible Firmware Interface) :** C'est le remplaçant moderne. Il supporte la souris, les graphismes, et il est beaucoup plus intelligent.
    - **GPT (GUID Partition Table) :** C'est le système de classement moderne. C'est comme une base de données numérique immense et sécurisée.

#### Informations système

### Linux Forensics

#### OS et information compte

```bash
OS informations : cat /etc/os-release

User accounts : cat /etc/passwd| column -t -s :
	x : mot de passe stocké dans /etc/shadow/
	
Group information : cat /etc/group

Sudpers List : sudo cat /etc/sudoers

Login Information : sudo last -f /var/log/wtmp
	Fichier binaires dans /var/log/ 
		wtmp : Historique de connexions 
		btmp : tentatives de connexions échouées
		
Authentification Logs : cat /var/log/auth.log |tail
```


#### System configuration

```bash
Hostname : cat /etc/hostname 

Timezone : cat /etc/timezone

Network configuration : 
	- ip a 
	- cat /etc/network/interfaces
	
Active network connections : netstat -natp
	- Permet de voir quel program écoute sur adress/port

Running processes : ps aux 
	- Permet de voir fullpath program

DNS Information : 
	- cat /etc/hosts
	- cat /etc/resolv.conf
```


#### Mécanismes de persistance

```bash
Cron jobs : cat /etc/crontab

Service startup : ls /etc/init.d/
	- Permet de voir les services qui se lancent au démarrage comme sur Windows
	- Voir services systemd activés : systemctl list-unit-files --type=service 
	
.Bashrc : cat ~/.bashrc 
	- Fichier de conf exécuté automatiquement à l'ouverture d'un shell bash
```


#### Evidence d’exécution

```bash
Sudo execution history : 
	- Ressort activités sudo : cat /var/log/auth.log | grep -i "sudo"
	- Ressort toutes les commandes exécutées : cat /var/log/auth.log | grep -i "COMMAND"
	
Bash history : cat ~/.bash_history 
	- Voir bash_history d'un autre user : sudo cat /home/user/.bash_history
	- history : historique en mémoire (session courante) se save après logout
	- .bash_history : sauvegarde sur disque (sessions précédentes)
	  # sudo grep -i '/home' /root/.bash_history

Files accessed using Vim : cat ~/.viminfo
	- Contient historique des fichiers ouverts avec VIM, historiques des commandes...
f
```


#### Log files

```bash
Syslog : cat /var/log/syslog 
	- Messages généraux du système (lancement de services, cronjob suspect, erreur système...)
	- Gros fichier, use tail, head, more, less...
	- Voir ancien historique : zgrep -i "hostname" /var/log/syslog*
	
Auth log : cat /var/log/auth.log
	- Voir tentatives de co échouée : | grep "Failed" 
	- Co réussies/échouées, création/supp d'users/groupes, modif privilèges

Third-Party Logs (/var/log/...) : ls /var/log
	- Chaque service/appli a ses propres logs
```


#### Processus/Services

- systemctl → gérer systemd et ses units (services, timers, sockets, etc.). “commande d’administration” : démarrer/arrêter, activer au boot, vérifier l’état.

```bash
systemctl (gestion) 

sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx     # démarrer au boot
sudo systemctl disable nginx
sudo systemctl is-active nginx  # actif/inactif ?
sudo systemctl is-enabled nginx # activé au boot ?
sudo systemctl list-units --type=service

```


- journalctl → consulter les journaux collectés par systemd-journald.

“visionneuse de logs” : filtre par service, priorité, période, boot, etc.

```bash
journalctl (logs) 

sudo journalctl -u nginx.service           # logs de nginx
sudo journalctl -u nginx.service -f        # en temps réel
sudo journalctl -p err                     # erreurs et + grave
sudo journalctl -b                         # logs du boot courant
sudo journalctl -S "2024-09-01" -U "now"   # fenêtre temporelle
```


| **Description** | **Command** |
| --- | --- |
| Affiche le nom de l’user courant. | `whoami` |
| Retourne l’identité de l’user. (UID, GID, groupes…) | `id` |
| Affiche nom de la machine. | `hostname` |
| Affiche des infos sur l’OS et le matériel. -a pour détails. | `uname` |
| Affiche répertoire de travail courant. | `pwd` |
| Assigne/affiche adresse interface réseau. Ancien, préférer ip. | `ifconfig` |
| Affiche/manipule conf réseau. Affiche interface et leurs MTU ip link. | `ip` |
| Affiche l’état réseau (connexions, ports). Préférer ss. | `netstat` |
| Inspecte sockets. Ex : ss -tulpen pour ports + PIDs. | `ss` |
| Affiche l’état des processus.  | `ps` |
| Connaître SHELL | `echo $SHELL` |
| Affiche user connectés. | `who` |
| Affiche variables d’environnement. | `env` |
| Liste les périphériques blocs (disques/partitions) | `lsblk` |
| Liste USB devices | `lsusb` |
| Liste fichiers ouverts. lsof -i pour co réseau. | `lsof` |
| Lists PCI devices. | `lspci` |
| Connaitre chemin mail | `echo $MAIL` |
| Lister ports utilisés | ss -tunlp |
| Depuis combien de temps l’hôte est alluùé | uptime |
| Lister users co (et depuis quand) | who / w |
| Info sur l’OS | `cat /etc/os-release` |
| Services actifs (si systemd) | `systemctl list-units --type=service` |
| Taille des dossiers dans le dossier courant | `du -sh *` |
| Utilisation des disques montés | `df -h` |
| liste utilisateurs | `cat /etc/passwd| column -t -s :` |
| sudo last -f /var/log/fichier_de_log | wtmp : Historique de connexion 

btmp : connexion échouée |

#### Identité

- PID (Process ID) : Chaque programme qui tourne a un numéro unique
    - PID 1 = Systemd
- UID (User ID) : Matricule d’utilisateur
    - UID 0 = root
    - UID 1 à 999 = Réservé aux Services/Daemons (ex : user www-data pour serveur web). N’ont pas le droit de se connecter à un écran, servent juste à faire tourner process en fond.
    - UID 1000+ = Utilisateurs normaux
- GID (Group ID) : Chaque utilisateur appartient à un groupe principal (souvent le même nom que l'utilisateur). Ça permet de partager des fichiers entre collègues.

#### Recherche & gérer fichiers / répertoires [which, find, locate]

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
    

#### Supprimer fichiers

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
    

#### Divers

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
    

 

#### Filtrer contenus fichiers [grep, tail, more, less…]

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
    

#### REGEX

Permet de grouper et de contrôler répétition de motif

| Opérateurs | Description |
| --- | --- |
| `(a)` | Parenthèse : Groupent une partie de la regex, le groupe est traité comme une unité |
| `[a-z]` | Crochets : Classe de caractères (Liste à faire correspondre) |
| `{1,10}` | Accolades : Quantificateur, répéter motif précdent n à m fois. |
| `|` | OR operator, montre résultat quand un des deux expressions matchent |
| `.*` | Affiche résultats uniquement lorsque les deux expressions sont présentes et correspondent dans l’ordre spécifié. |

#### Opérateur OR

Chercher ligne contenant motif spécifique

```bash
grep -E "(my|false)" /etc/passwd
```


#### Opérateur ET

Chercher ligne contenant mot1 puis plus loin mot2 (dans cet ordre)

```bash
grep -E "(my.*false)" /etc/passwd
```


#### Gestion des permissions [chmod, SUID…]

#### Introduction

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
    

#### Modifier permissions (chmod)

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

#### Modifier propriétaire (chown)

```bash
chown <user>:<group> <file/directory>

- Ex : 
	chown root:root shell && ls -l shell
```


#### Identité : UID, GID, PID

- PID (Process ID) : Chaque programme qui tourne a un numéro unique
    - PID 1 = Systemd
- UID (User ID) : Matricule d’utilisateur
    - UID 0 = root
    - UID 1 à 999 = Réservé aux Services/Daemons (ex : user www-data pour serveur web). N’ont pas le droit de se connecter à un écran, servent juste à faire tourner process en fond.
    - UID 1000+ = Utilisateurs normaux
- GID (Group ID) : Chaque utilisateur appartient à un groupe principal (souvent le même nom que l'utilisateur). Ça permet de partager des fichiers entre collègues.

#### SUID et SGID

Linux permet permissions spéciales sur fichiers via bits Set User ID (SUID) et Set Group ID (SGID). Fonctionnent comme accès temporaires. Font s’exécuter programme avec droit du owner du fichier (SUID) ou du groupe du fichier (SGID) et non avec ceux de l’user qui lance. Ex : admin autorise actions précises nécessitant privilèges, même si user n’a pas normalement les droits. Visuellement, présence indiquée par s au lieu de x :

- SUID remplace le x du bloc propriétaire (u)
- SGID remplace le x du bloc groupe (g)
- Trouver SUID
    
    ```bash
    find / -perm -u=s -type f 2>/dev/null
    ```
    

#### Sticky bit

Protège fichiers dans un répertoire partagé, seul propriétaire du fichier, proprio du répertoire ou root peut supp/rename. 

#### File descriptors et redirections [STDIN, STDOUT, STDERR]

File descriptor (FD) sous Unix/Linux est une référence, gérée par noyau qui identifie ressource ouverte (fichier, socket…). Sous Windows, on parle de file handle. “Ticket” que l’OS utilise pour savoir quelle ressource lire/écrire.

- STDIN - 0 : Entrée standard
- STDOUT - 1 : Sortie standard
- STDERR - 2 : Sortie d’erreur

#### STDIN et STDOUT

On dnne une entrée (STDIN) à cat, une fois “entrée”, ressort sur la sortie standard (STDOUT) 



#### STDOUT et STDERR

Les résultats “normaux” sur STDOUT, les erreurs sur STDERR, ex : Permission denied

- On peut rediriger erreur 2>/dev/null.



#### Rediriger STDOUT dans un fichier

```bash
find /etc/ -name shadow 2>/dev/null > results.txt
cat results.txt

# Ici, seules lignes réussies sont envoyées
# Attention : > : écrase fichier s'il existe
```




#### Rediriger STDOUT et STDERR vers fichiers séparés

```bash
find /etc/ -name shadow 2> stderr.txt 1> stdout.txt
```




#### Redirection de STDIN

< Sert à rediriger l’entrée standard, grossièrement, fait comme cat mais utile quand commande exige l’entrée via STDIN.

```bash
cat < stdout.txt
```




#### Rediriger STDOUT ajouter au lieu d’écraser

>> ajoute à la fin du fichier (au lieu d’écraser)

```bash
find /etc/ -name passwd >> stdout.txt 2>/dev/null
cat stdout.txt
```




#### Rediriger flux STDIN vers fichier

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


#### Gestion du système

#### Gestions des users [passwd, shadow…]

| Commande | Description |
| --- | --- |
| `sudo` | Exécuter commande en tant qu’un autre utilisateur (par défaut root). |
| `su` | Changer d’user après authent (par défaut vers **root**) et ouvrir un shell. |
| `useradd` | Créer un utilisateur. |
| `userdel` | Supprimer un utilisateur. |
| `usermod` | Modifier un compte utilisateur existant. |
| `addgroup` | Créer groupe. |
| `delgroup` | Supprimer groupe. |
| `passwd` | Changer MDP. |
| `cat /etc/passwd| column -t -s` | Liste utilisateurs |
| sudo last -f /var/log/fichier_de_log | wtmp : Historique de connexion 

btmp : connexion échouée |

- /etc/passwd
    
    Ligne type :
    
    ```
    login:x:UID:GID:GECOS:/home/login:/bin/bash
    
    ```
    
    - **login** : nom du compte (ex. `alice`, `root`).
    - **x** : indique que le **hash est dans /etc/shadow**.
        - ou `!` ici → compte **verrouillé / sans mot de passe** (selon distro).
    - **UID** : identifiant utilisateur.
        - `0` = **root** ; `1–999` ≈ comptes système ; `≥1000` = comptes humains (valeurs variables selon distro).
    - **GID** : groupe primaire (ID numérique).
        - Le nom du groupe se voit via `getent group <GID>`.
    - **GECOS** : infos “humaines” (nom complet, bureau, tel…), champs séparés par des virgules.
        - Ex. `Alice Dupont,2B-314,0123456789`.
    - **home** : répertoire personnel (ex. `/home/alice`, `/root`).
    - **shell** : programme lancé à la connexion.
        - `/bin/bash`, `/bin/zsh`, …
        - **/usr/sbin/nologin** ou **/bin/false** → empêche la connexion interactive.
- /etc/shadow
    
    Ligne type :
    
    ```
    login:$id$[params$]salt$hash:last:min:max:warn:inactive:expire:reserved
    
    ```
    
    - **login** : doit correspondre à celui de /etc/passwd.
    - **$id$…** : **algorithme + hash**.
        - **$6$** = **sha512crypt**, **$5$** = sha256crypt, **$2y$** = bcrypt, **$y$** = yescrypt.
        - Peut contenir des paramètres, ex. **`$6$rounds=10000$`**.
        - Préfixe **`!`** ou  → **compte verrouillé** (login par mot de passe impossible).
    - **salt** : sel (random) utilisé par l’algo.
    - **hash** : résultat chiffré du mot de passe.
    - **last** : **jour depuis 1970** du **dernier changement** de mot de passe (entier).
        - Vide = inconnu.
    - **min** : **âge minimum** (en jours) avant de pouvoir rechanger le mot de passe.
        - `0` = pas de minimum.
    - **max** : **âge maximum** (en jours) avant expiration du mot de passe.
        - Ex. `99999` ≈ “quasi jamais”.
    - **warn** : nb de **jours d’avertissement** avant l’expiration.
    - **inactive** : nb de jours **après expiration** pendant lesquels le compte reste utilisable avant **désactivation**.
        - Vide = pas d’inactivité définie.
    - **expire** : **date de désactivation du compte** (jour depuis 1970).
        - Vide = jamais.
    - **reserved** : champ réservé (souvent vide).

#### Gestion des packages

- Paquet : archive contenant fichiers .deb, fichiers de conf, méta-données (dépendances, version…)
- Dépôt : Serveur qui contient milliers de logiciels validés
    - `/etc/apt/sources.list`
- Distribution s’appuie sur des dépôts logiciels, lorsqu’on installe programme, système interroge ces dépôts.
    - Liste des dépôts : /etc/apt/sources.list

| Commande | Description |
| --- | --- |
| `dpkg` | Installer / construire / enlever paquets **Debian**. Pour `.deb`. |
| `apt` | APT fournit interface user-friendly du système de paquets. Gère la résolution des **dépendances**. |
| `aptitude` | Alternative à `apt` (interface semi-graphique/TUI). |
| `snap` | Installer/configurer/mettre à jour des **snaps** (paquets confinés, multi-versions). |
| `gem` | Front-end de **RubyGems** (gestionnaire Ruby). |
| `pip` | Installateur de paquets **Python.** |
| `git` | Système de **contrôle de version** distribué (clonage de projets/outils). |

#### DPKG

Outil bas niveau, installe fichier .deb (équivalent de .exe) déjà sur disque. 

Problème : Si le logiciel a besoin d’une autre librairie pour marcher (dépendance), dpkg va juste planter et dire il qu’il manque quelque chose. C’est pour ça qu’APT est intéressant.

- Télécharger .deb et l’installer directement
    
    ```bash
    wget http...
    ```
    
- Installer avec DPKG
    
    ```bash
    sudo dpkg -i fichier.deb
    ```
    

#### APT (Advanced Package Manager)

L’outil dpkg installe un .deb local mais ne résout pas dépendances. 

APT simplifie l’install car télécharge et installe automatiquement dépendances requises.

APT maintient base locale appelée cache APT, permet de consulter hors-ligne infos des paquets installés.

Pour télécharger les logiciels, lit `/etc/apt/sources.list`. 

Surcouche au-dessus de dpkg, si l’on veut installer Firefox

1. Regarder dans sa liste de courses (les dépôts).
2. Télécharger Firefox.
3. Vérifier de quoi Firefox a besoin pour marcher.
4. Télécharger toutes les dépendances.
5. Appeler `dpkg` pour tout installer dans le bon ordre.

```bash
# Cherche dans le cache
apt-cache search impacket

# Voir infos d'un paquet 
apt-cache show <paquet>

# Lister tous les paquets installés
apt list --installed

# Installer paquet manquant
sudo apt install <paquet> -y
```


#### Process install complet

#### Le Processus "Bout en Bout" 🔄

Prenons un exemple concret : Tu veux installer **Nmap**.

#### Étape 1 : La Mise à Jour du Catalogue (`apt update`)

Tu tapes `sudo apt update`. Que se passe-t-il **réellement** ?

Ton PC ne télécharge **pas** de logiciels. Il télécharge des **listes de textes**.

1. APT lit `/etc/apt/sources.list`.
2. Il contacte les serveurs.
3. Il télécharge des fichiers compressés (ex: `Packages.gz`) qui contiennent la liste de tous les logiciels disponibles, leurs versions, et leurs **sommes de contrôle (Hashs)**.
4. Il stocke ces listes dans **`/var/lib/apt/lists/`**.

> ⚠️ Point Sécu : Si tu ne fais pas ça, ton PC pense que la version de Nmap disponible est la 7.80, alors que le serveur a la 7.90. Si tu essaies d'installer, le serveur dira "404 Not Found" car l'ancien fichier n'existe plus.
> 

#### Étape 2 : La Résolution de Dépendances (`apt install nmap`)

Tu tapes `sudo apt install nmap`.

1. APT regarde dans sa base locale (`/var/lib/apt/lists/`).
2. Il voit : "Ok, Nmap v7.90".
3. **Le Calcul :** Il vérifie les besoins de Nmap. *"Ah, Nmap a besoin de la librairie `liblua` et `libpcap`"*.
4. Est-ce que tu les as déjà ? Non ? Alors APT décide de télécharger Nmap **ET** ses dépendances.

#### Étape 3 : Le Téléchargement et le Stockage

APT télécharge les fichiers `.deb` (le paquet Nmap et les paquets des librairies).
Il ne les installe pas tout de suite ! Il les stocke dans une zone tampon (cache) :
📍 **`/var/cache/apt/archives/`**

#### Étape 4 : La Vérification de Sécurité (CRITIQUE) 🛡️

C'est ici que la magie opère. Comment être sûr que le serveur n'a pas été piraté ou que tu n'as pas subi une attaque "Man-in-the-Middle" ?

1. Chaque dépôt officiel possède une paire de clés **GPG**.
2. La **Clé Publique** du dépôt est stockée sur ton PC (dans `/etc/apt/trusted.gpg.d/`).
3. Le fichier "Catalogue" que tu as téléchargé est **signé numériquement** avec la Clé Privée du dépôt.
4. APT vérifie la signature. Si elle est valide ➡️ Le catalogue est authentique.
5. APT calcule le **Hash (SHA256)** du fichier `.deb` téléchargé et le compare avec le Hash écrit dans le catalogue authentifié.

Si ça matche : C'est le vrai Nmap.
Si ça ne matche pas : **ALERTE ROUGE**, APT stoppe tout : *"Hash Sum Mismatch"*.

#### Étape 5 : L'Extraction (Le passage de relais à DPKG) 📦

APT a fini son boulot (télécharger et vérifier). Il passe le fichier `.deb` à **DPKG**.

Un fichier `.deb`, c'est en réalité une archive (comme un Zip). DPKG l'ouvre. À l'intérieur, il y a deux archives :

1. **`control.tar.gz`** : Les instructions (Méta-données).
2. **`data.tar.gz`** : Les vrais fichiers du logiciel.

DPKG extrait `data.tar.gz` et copie les fichiers aux bons endroits :

- Le binaire `nmap` va dans `/usr/bin/`.
- La doc va dans `/usr/share/man/`.

#### Étape 6 : La Configuration (Post-Install Scripts) ⚙️

Une fois les fichiers copiés, DPKG exécute les **scripts de post-installation** contenus dans le paquet.

- *Exemple :* Si tu installes un serveur web, le script va créer l'utilisateur `www-data`, générer les certificats par défaut, et lancer le service avec `systemctl`.

#### Git (cloner outil)

```bash
git clone https:...
```


#### PIP (Python Package Installer)

```bash
python3 -m pip install <paquet>
```


#### Gestion des process et service [daemons, Systemd, SIGTERM…]

#### Linux Process / Services

#### System profiling

- Infos système

```bash
- Version noyau / archi / build : uname -a 
	- Donne : OS, hostname, version du kernel (5.15.0-1063-aws), build Ubuntu, date de compilation, archi (x86_64), etc.
	
- Identité de la machine : hostnamectl
	- Donne : Static hostname, Machine ID, Boot ID, Virtualization (ex. Xen), OS (Ubuntu 20.04.6 LTS), Kernel, Architecture.

- Dispo et charge : uptime
```


- Matériel & ressources

```bash
- CPU / Archi : lscpu
	- Donne : Architecture, nb de CPU(s)/cœurs, Model name, hyperviseur, et infos vulnérabilités/mitigations exposées par le kernel.

df -h        # occupation disque, lisible (humain)
lsblk        # topologie des block devices (disques/partitions, tailles, points de montage)
- Mémoire : free -h

```


- Logiciels installés

```bash
- Inventaire bas niveau : dpkg -l 
	- Liste tous les paquets .deb installés. Utile pour repérer un paquet suspect par nom/version/date (corrélation à faire ensuite dans les logs dpkg.log si besoin)
	
- Inventaire via APT : apt list --installed | head -n 30
	- Affiche les 30 premiers paquets installés (et leur provenance/canal). Même usage : survol rapide, détection d’éléments inattendus.
```


- Profil réseau

```bash
- Interfaces & adresses : ip a 

- Routage : ip r

- Connexions & sockets : ss
```


#### Hunting for processes

```bash
ps : instantané des processus (options utiles : ps aux).

top / htop : vue temps réel (CPU/Mem les plus gourmands).

pstree : arbre des processus (relations parent/enfant).

pidof / pgrep : retrouver un PID par nom/critères.

lsof : fichiers/sockets ouverts par un processus.

netstat : connexions réseau et ports en écoute.

strace : appels système d’un processus (très verbeux).

vmstat : perf globale (ordonnancement/mémoire).
```


```bash
# Vue large + hiérarchie détaillée
ps -eFH | less

# Processus d’un user + commandes complètes
ps -u <user> -o pid,ppid,user,%cpu,%mem,stat,start,time,cmd

# Trier par CPU puis afficher 20 plus gourmands
ps -eo pid,user,%cpu,%mem,stat,time,cmd --sort=-%cpu | head -n 20

# Arbre avec PIDs
pstree -p

# Temps réel (commandes complètes)
top -c

# Trouver PID d’un programme
pgrep -fl <nom>

# Fichiers/sockets ouverts par un PID
sudo lsof -p <PID>

# Qui écoute sur le réseau (et par quel processus)
ss -tulpen

```


| Besoin | Outil | Commande rapide | Idée clé |
| --- | --- | --- | --- |
| Photo instantanée | `ps` | `ps aux` | Vue large de tous les processus |
| Vue hiérarchique | `ps` (forest) | `ps -eFH` | Détail + hiérarchie dans un seul tableau |
| Arbre lisible | `pstree` | `pstree -p` | Affiche parentés de façon visuelle |
| Temps réel | `top` | `top -c` | Tri interactif CPU/MEM, commandes en direct |
| Temps réel amélioré | `htop` | `htop` | Interface plus claire, recherche/kill faciles |
| Trouver PID par nom | `pidof` / `pgrep` | `pidof nginx` / `pgrep -fl nginx` | Ciblage rapide |
| Fichiers/sockets ouverts | `lsof` | `sudo lsof -p <PID>` | Ce que touche un processus |
| Connexions/ports | `ss` (ou `netstat`) | `ss -tulpen` | Qui écoute, sur quel port |
| Appels système | `strace` | `sudo strace -p <PID>` | Débogage fin (avancé) |
| Perf système | `vmstat` | `vmstat 1` | Vue synthétique CPU/mémoire/process |

#### Services

- **Service/daemon** = programme qui tourne en arrière-plan (ex : `sshd`, `cron`, `apache2`).
- Sert à : fournir des services réseau, tâches planifiées, gestion du système.
- **Gestionnaire courant** : `systemd` (commande **`systemctl`**).

### Savoir lister et piloter (avec `systemctl`)

Lister :

```bash
# Tous les services (quelque soit l’état)
sudo systemctl list-units --all --type=service

# Uniquement ceux en cours d’exécution
sudo systemctl list-units --type=service --state=running

# Tous les fichiers d’unité connus + s’ils sont activés au boot
sudo systemctl list-unit-files --type=service

```


Piloter :

```bash
sudo systemctl start <service>      # démarrer
sudo systemctl stop <service>       # arrêter
sudo systemctl restart <service>    # redémarrer
sudo systemctl enable <service>     # activer au démarrage
sudo systemctl disable <service>    # désactiver au démarrage
sudo systemctl status <service>     # état + PID + dernier log

```


Inspecter un service précis :

```bash
# Voir l’état et le binaire lancé
sudo systemctl status <service>

# Afficher le fichier d’unité effectif (chemin ExecStart, etc.)
sudo systemctl cat <service>

# Extraire juste certaines propriétés
sudo systemctl show <service> -p ExecStart -p FragmentPath -p User -p Group -p Restart

```


---

### Où sont les fichiers d’unité ?

- **Système (distro)** : `/lib/systemd/system/*.service`
- **Local (admin/custom)** : `/etc/systemd/system/*.service` ← souvent là que se cache la persistance
- **Utilisateur (mode user)** : `~/.config/systemd/user/*.service`

Astuce repérage “suspect” :

```bash
# Tous les services activés au boot (vue courte)
sudo systemctl list-unit-files --type=service | grep enabled

# Lister uniquement les unités locales (custom)
ls -l /etc/systemd/system/*.service

# Chercher ExecStart qui pointe hors des chemins habituels (/usr/bin, /usr/sbin,…)
sudo grep -R "^ExecStart=" /etc/systemd/system /lib/systemd/system | grep -vE "/usr/(s)?bin|/bin"

```


---

### Voir les logs d’un service (avec `journalctl`)

```bash
# Logs du service (ancien → récent)
sudo journalctl -u <service>

# Suivre en temps réel (Ctrl+C pour quitter)
sudo journalctl -f -u <service>

# Filtrer par priorité (erreurs et + grave)
sudo journalctl -p err -u <service>

# Dernier démarrage
sudo journalctl -u <service> -b

```


> Si besoin de conserver les journaux après reboot, dans /etc/systemd/journald.conf : Storage=persistent (puis redémarrer systemd-journald).
> 

---

### Checklist “analyse express” (IR/Hygiène)

1. **Qu’est-ce qui tourne ?**
    
    `sudo systemctl list-units --type=service --state=running`
    
2. **Qu’est activé au boot ?**
    
    `sudo systemctl list-unit-files --type=service | grep enabled`
    
3. **Unités locales (custom) ?**
    
    `ls -l /etc/systemd/system/*.service`
    
4. **Binaire exact et options ?**
    
    `sudo systemctl status <service>` → regarder **ExecStart**, **Main PID**
    
5. **Logs associés ?**
    
    `sudo journalctl -u <service> -r` (du plus récent au plus ancien)
    
6. **Nom/chemin “bizarre” ?**
    
    Chercher ExecStart hors répertoires classiques, `Restart=always` suspect, exécution en `User=root` inutilement, timers/sockets associés.
    
7. **Ne pas oublier** : `timers` et `sockets` (autres vecteurs de persistance)
    
    `systemctl list-timers`, `systemctl list-sockets`
    

---

### Mini mémo (copier/coller)

```bash
# Inventaire rapide
sudo systemctl list-units --type=service --state=running
sudo systemctl list-unit-files --type=service

# Inspection ciblée
sudo systemctl status <service>
sudo systemctl cat <service>
sudo journalctl -f -u <service>

# Hygiène
sudo systemctl disable <service>  # si inutile
sudo systemctl stop <service>     # si à bloquer

```


#### Investiguer connexions réseau

```bash
netstat / ss : connexions actives + ports en écoute.

lsof : fichiers et sockets ouverts par un PID.

tcpdump : capture paquet (filtrable).

iftop : bande passante temps réel par flux.

iptables : règles pare-feu (contexte).

Autres vus : nmap, ping, traceroute, dig/nslookup, hostname, ifconfig/ip, arp, route, curl/wget, netcat, whois.
```


#### Linux incident surface

#### Processus et connexion réseau

- Instantanné des process : ps aux

```bash
- Ex :
ubuntu@tryhackme:~$ ps aux | grep simple
ubuntu      2267  0.0  0.0   2496   576 pts/0    S+   23:22   0:00 /tmp/simple

- Champs : 
USER propriétaire · PID identifiant · %CPU/%MEM ressources

VSZ/RSS mémoire · TTY terminal · STAT état (R/S/Z…)

START heure de démarrage · COMMAND binaire + arguments

- Inspecter ressources d’un processus : Récup PID lsof -p 2267 

- Lister connexions réseau actives : lsof -i -P -n
	- -i connexions réseau · -P afficher numéros de ports · -n ne pas résoudre les hôtes.

```


- Osquery : Outil pour explorer process et ses connexions réseau.

```bash
- Lancer Osquery : osqueryi 

- Interroger sockets ouverts par PID précis : SELECT pid, fd, socket, local_address, remote_address FROM process_open_sockets WHERE pid = 2372;

```


#### Persistance

#### Création de compte

```bash
# Créer un compte et l’ajouter au groupe sudo
sudo useradd attacker -G sudo
sudo passwd attacker

# (optionnel) lui donner des droits sudo explicites
echo "attacker ALL=(ALL:ALL) ALL" | sudo tee -a /etc/sudoers

- Traces à chercher : sudo grep useradd /var/log/auth.log
- Emplacement compte : grep attacker /etc/passwd
```


#### Cron jobs

```bash
- Editer cron tab : crontab -e 

# Exemple : relancer un script à chaque reboot
@reboot /path/to/malicious/script.sh
# Exemple : toutes les minutes (root)
* * * * * root /path/to/malicious/script.sh

- Crontab par users : /var/spool/cron/crontabs/<user>
- Chercher exécution : grep CRON /var/log/syslog
```


#### Services systemd

```bash
Créer un fichier de conf pour test : sudo nano /etc/systemd/system/suspicious.service

# /etc/systemd/system/suspicious.service
[Unit]
Description=Suspicious_Service
After=network.target

[Service]
ExecStart=/home/activities/processes/suspicious
Restart=on-failure
User=nobody
Group=nogroup

[Install]
WantedBy=multi-user.target

Activer / lancer : 

sudo systemctl daemon-reload
sudo systemctl enable suspicious.service
sudo systemctl start  suspicious.service
sudo systemctl status suspicious.service
```


```bash
Trace : 

- Unit files installés/activés : ls -l /etc/systemd/system

- Syslog (event lié au service) : grep suspicious /var/log/syslog

- Journal systemd : sudo journalctl -u suspicious

```


### Où regarder globalement

- **Répertoire des logs** : `/var/log/` (auth.log, syslog, …)
- **Comptes** : `/etc/passwd`
- **Cron** : `/var/spool/cron/crontabs/<user>`
- **Services** : `/etc/systemd/system` (+ `systemctl status …`, `journalctl -u …`)

---

### Mini check-list détection (rapide)

- Un **nouvel utilisateur** admin ? → `auth.log` + `/etc/passwd`
- Des **tâches planifiées** anormales ? → crontabs + `grep CRON /var/log/syslog`
- Un **service** inconnu/manuel ? → `/etc/systemd/system` + `systemctl status` + `journalctl -u`

> Objectif : relier l’action (compte/cron/service) à ses empreintes (fichiers de config + logs) pour confirmer une persistance.
> 

- `Service`, aussi appelé `daemon`, effectuent tâches pour fonctionnement du système et fournit fonctionnalités supp, tournent en arrière-plan. Par convention, finit souvent par d (sshd, httpd..) Classer en deux catégories :
    - Services système : Interne requis lors du démarrage (init matériel, composants…)
    - Services installés par user : applis serveur, tâches en fond
- `Systemd` et `systemctl` : Systemd est le gestionnaire qui lance et surveille ces daemons, pour travailler avec on utilise la commande systemctl
- Moderne distrib utilisent systemd lors de l’initialisation du système (init init). Premier process qui démarre au boot et 1er Process ID (PID). Chaque process a un PID et un PPID (parent) visibles sous /proc/.

#### Systemctl (services systemd)

Permet de lancer, d’arrêter les services.

```bash
# Usage commun
systemctl start <service> / pgrep service
systemctl status <service> / ps -p 3162 -o pid,ppid,user,cmd
systemctl enable <service>
ps -aux | grep <service>
systemctl list-units --type=service
kill XXX
```


```bash
# Démarrer / arrêter / redémarrer / recharger
systemctl start ssh
systemctl stop ssh
systemctl restart ssh
systemctl reload ssh
```


```bash
# Etat / logs récents / liste / Echecs (failed & journalctl)
systemctl status ssh
systemctl list-units --type=service
systemctl --failed 
journalctl -u ssh.service --no-pager
```


```bash
# Activer au démarrage / désactiver / Check
systemctl enable ssh
systemctl disable ssh
ps -aux | grep ssh
```


#### Lister / chercher [PS, PSTREE, SS -lntp]

```bash
# Lister / Filtrer / Arbre / Ports
ps aux 
ps aux | grep ssh
pstree -p
ss -lntp / ss -tulpn

# Trouver service / binaire / unit file
systemctl | grep -i ssh
systemctl cat ssh.service
which sshd
systemctl list-units --type=service
```


#### Kill process & signaux

- Process peut-être dans états suivants :
    - Running
    - Waiting (attends évent ou ressource système)
    - Stopped
    - Zombie (Stop mais a toujours une entrée dans la table des process, -9 ne marche pas, il faut tuer son père pour que Kernel nettoie désordre)
        - Déjà mort (il a fini son travail). Il reste dans la liste (RAM) uniquement parce que son **Père** (Parent Process) n'a pas encore lu son "code de sortie" (son rapport de fin de mission).
- Lister signaux et trouver PID de process

```bash
kill -i : Lister tous signaux
pgrep <nom_process> # Donne PID
```


- Envoyer signaux (par PID)

```bash
kill -TERM <PID> / kill 15 <PID> # Arrêt propre
kill -KILL <PID> / kill 9 <PID> # Force brute
kill XX

```


- Par nom de process

```bash
pkill -TERM -x nom_process
pkill -KILL -x nom_process
```


| **Signal** | **Description** |
| --- | --- |
| `1` | `SIGHUP` - This is sent to a process when the terminal that controls it is closed. |
| `2` | `SIGINT` - Sent when a user presses `[Ctrl] + C` in the controlling terminal to interrupt a process. |
| `3` | `SIGQUIT` - Sent when a user presses `[Ctrl] + D` to quit. |
| `9` | `SIGKILL` - Immediately kill a process with no clean-up operations. |
| `15` | `SIGTERM` - Program termination. |
| `19` | `SIGSTOP` - Stop the program. It cannot be handled anymore. |
| `20` | `SIGTSTP` - Sent when a user presses `[Ctrl] + Z` to request for a service to suspend. The user can handle it afterward. |

#### Mettre process en arrière-plan / avant-plan

Parfois nécessaire de mettre scan en arrière plan le temps de continuer d’autres choses

```bash
CTRL + Z # Suspend process en cours
jobs # Lister 
bg %X # Permet de relancer jobs souhaité en arrière
command & # Esperluète à la fin permet de mettre en arrière
fg X # Permet de relancer en avant
```


#### Exécuter multiple commandes

- Trois possibilités
    - Séparateur `;` : enchaîne sans condition
        
        ```bash
        cmd1 ; cmd2 ; cmd3
        
        echo '1'; echo '2'; echo '3'
        echo '1'; ls MISSING_FILE; echo '3'
        ```
        
    - `&&` : Exécute si la précédente réussit
        
        ```bash
        cmd1 && cmd2 && cmd3
        
        echo '1' && ls MISSING_FILE && echo '3' # Prend en compte que MISSING_FILE : "No such file or directory" donc pas echo 3
        ```
        
    - Pipes | : redirige STDOUT de gauche vers commande de droite
        
        ```bash
        cmd1 | cmd2 | cmd3
        ```
        

#### Gestion réseau [netstat, ss -tulnp, resolv.conf, interfaces…]

#### Connaitre infos

```powershell
ip a               # IP & MAC des interfaces
ip link            # état (UP/DOWN), MTU…
ip route           # table routage
ifconfig           # Afficher all interfaces 
ip r
cat /etc/resolv.conf
ss -tulpn          # Connaitre ports
	-tulpn4          # IPv3 uniquement
netstat -tulnp4    # Connaitre ports (legacy)
```


#### Configurer interfaces

- Inspecter
    
    ```bash
    ip a               # IP & MAC des interfaces
    ip link            # état (UP/DOWN), MTU…
    ip route           # table routage
    ifconfig           # Afficher all interfaces 
    ```
    
- Activer / Désactiver
    
    ```bash
    sudo ip link set eth0 up # OR sudo ifconfig eth0 up
    sudo ip link set eth0 down
    ```
    
- Assigner IP adr (statique, non persistant)
    
    ```bash
    sudo ip addr add 192.168.1.2/24 dev eth0
    sudo ip route add default via 192.168.1.1 dev eth0
    ```
    
- Editer conf de manière persistante
    
    ```bash
    sudo vim /etc/network/interfaces
    
    # File
    auto eth0
    iface eth0 inet static
      address 192.168.1.2
      netmask 255.255.255.0
      gateway 192.168.1.1
      dns-nameservers 8.8.8.8 8.8.4.4
      
    sudo systemctl restart networking 
    ```
    
- Identifier machines sur résea
    
    ```bash
    for i in {1..254}; do (ping -c 1 192.168.1.$i | grep "bytes from" &); done
    ```
    

#### DNS

- Fichier texte lu avant :
    - /etc/hosts
- Fichier de conf :
    - /etc/resolv.conf
- Editer configuration (manuellement pas persistant)
    
    ```bash
    sudo nano /etc/resolv.conf
    ```
    
- **`/etc/resolv.conf`** : C'est la liste des serveurs DNS à contacter (ex: `nameserver 8.8.8.8`). C'est "L'adresse de l'annuaire".
- **`/etc/hosts`** : C'est le fichier que je cherchais. C'est un petit fichier texte lu **AVANT** de contacter le DNS. C'est comme un Post-it collé sur ton écran.
- *Pourquoi c'est important :* Si un malware écrit `1.2.3.4 facebook.com` dans `/etc/hosts`, ton PC ira *directement* sur l'IP 1.2.3.4 sans jamais demander au serveur DNS. C'est une interception absolue.

#### Monitoring

- Syslog/rsyslog/journald : Logs système/service

#### Troubleshooting

```bash
ping 8.8.8.8
traceroute example.com
dig example.com @8.8.8.8
tcpdump -i eth0 -n host <ip>
nmap -sS -sV -O -Pn <cible>
```


#### Network Access Control (NAC)

- DAC (Discretionary Access Control) : Propriétaire choisit qui accède à la ressource.
- MAC (Mandatory Access Control) : L’OS impose politique
- RBAC : Droits via rôles

#### Durcissement

- SELinux : Chaque process et chaque objet (fichier, socket, port…) a un contexte (type/role/domain). Une politique décrit quelles iinteractions sont permises.
- AppArmor : Attache un profil à un binaire (par chemin) décrivant ce qu’il peut lire/écrire/exécuter, quels capabilities il a, à quelles adresses il parle…
- TCP Wrappers : Deux fichiers /etc/hosts.allow & /etc/hosts.deny, décident une IP source a le droit d’accéder à un service.

#### Planification de tâches

#### Systemd (timer et service)

Principe : 

1. Créer un timer (planifie quand mytimer.service doit s’exécuter)
2. Créer un service (exécute commande / script)
3. Activer le timer 

#### Créer timer

- Pour commencer, doit créer un répertoire

```bash
sudo mkdir /etc/systemd/system/mytimer.timer.d
sudo vim /etc/systemd/system/mytimer.timer
```


- Créer script pour timer, doit contenir trois éléments :
    - Unit : Description pour timer
    - Timer : Spécifier quand commencer timer et quand l’activer
    - Install : Spécifie où installer timer

```bash
[Unit]
Description=My Timer

[Timer]
OnBootSec=3min
OnUnitActiveSec=1hour

[Install]
WantedBy=timers.target
```


- OnBootSec : délai après boot (s’exécute qu’une fois)
- OnUnitActiveSec : Fréquence après dernière exécution (régulier)

#### Créer service

- Créer le service

```bash
sudo vim /etc/systemd/system/mytimer.service
```


- Contenu de mytimer.service
    - Path complet du script

```bash
[Unit]
Description=My Service

[Service]
ExecStart=/full/path/to/my/script.sh

[Install]
WantedBy=multi-user.target
```


- Reload systemd, puis lancer et activer le timer

```bash
sudo systemctl daemon-reload
sudo systemctl start mytimer.timer
sudo systemctl enable mytimer.timer
```


#### Cron

- Principe : Écrire des lignes dans fichier crontab pour renseigner path des scripts et quand les exécuter
- Champs d’une ligne cron :
    
    ```bash
    * * * * *  /chemin/vers/script.sh
    | | | | |
    | | | | └─ Jour de la semaine (0-7, 0 et 7 = dimanche)
    | | | └─── Mois (1-12)
    | | └───── Jour du mois (1-31)
    | └─────── Heure (0-23)
    └───────── Minute (0-59)
    ```
    
- Éditer crontab
    
    ```bash
    crontab -e
    ```
    
    - Exemple crontab
    
    ```bash
    # System Update toutes les 6h
    0 */6 * * * /path/to/update_software.sh
    
    # Exécuter des scripts le 1er du mois à minuit
    0 0 1 * * /path/to/scripts/run_scripts.sh
    
    # Nettoyage DB chaque dimanche à minuit (0 ou 7)
    0 0 * * 0 /path/to/scripts/clean_database.sh
    
    # Backups chaque dimanche à minuit
    0 0 * * 7 /path/to/scripts/backup.sh
    ```
    
    - Lister, éditer, ajouter mail…
    
    ```bash
    crontab -l                  # lister la crontab utilisateur
    sudo crontab -e             # crontab de root
    sudo vim /etc/crontab       # crontab système (champ 'user' en plus)
    sudo ls /etc/cron.d/        # jobs cron drop-in
    
    # Notifications e-mail : définir MAILTO=user@domaine en tête de crontab
    ```
    
    - Sécurité / Forensic pour chercher persistence
    
    ```bash
    systemctl list-timers --all
    systemctl cat <timer> <service>
    journalctl -u <service>
    crontab -l
    sudo crontab -l
    sudo grep -R . /etc/cron.* /etc/crontab
    ```
    
    ### Connaitre type de service
    
    ```bash
    # le plus courant : unité utilisateur
    systemctl --user show -p Type dconf.service
    
    # ou afficher l’unité
    systemctl --user cat dconf.service  | grep -i '^Type='
    ```
    

#### Service réseau [SSH, NFS, Python]

#### SSH

Permet administration distante chiffrée (commandes, transferts, tunnels). Port 22. Serveur OpenSSH le plus répandu.

- Config OpenSSH
    - Fichier /etc/ssh/sshd_config.

```bash
# Installer serveur
sudo apt install openssh-server -y

# Vérifier service
systemctl status ssh

# Se connecter 
ssh user@ip
```


#### NFS

Permet de stocker et gérer fichiers sur systèmes distants comme s’ils étaient locaux (collaboration, centralisation). Aussi utile pour répliquer systèmes de fichiers entre serveurs. NFS-UTILS (Ubuntu)

```bash
# Installer serveur NFS
sudo apt install nfs-kernel-server -y

# Vérifier service 
systemctl status nfs-kernel-server
```


#### Créer et configurer NFS

- Configurer exports
    - Fichier : /etc/exports

| **Permissions** | **Description** |
| --- | --- |
| `rw` | Gives users and systems read and write permissions to the shared directory. |
| `ro` | Gives users and systems read-only access to the shared directory. |
| `no_root_squash` | Prevents the root user on the client from being restricted to the rights of a normal user. |
| `root_squash` | Restricts the rights of the root user on the client to the rights of a normal user. |
| `sync` | Synchronizes the transfer of data to ensure that changes are only transferred after they have been saved on the file system. |
| `async` | Transfers data asynchronously, which makes the transfer faster, but may cause inconsistencies in the file system if changes have not been fully committed. |

- Créer NFS Share

```bash
mkdir nfs_sharing
echo '/home/cry0l1t3/nfs_sharing hostname(rw,sync,no_root_squash)' >> /etc/exports
cat /etc/exports | grep -v "#"
```


- Mount NFS Share
    - Pour travailler avec le partage, doit le monter.
        - Ex : Monte partage /dev_scripts de cible (10.1.12.17) localement dans point de montage ~/target_nfs sur réseau et peut afficher contenu comme si on était sur système cible.

```bash
mkdir ~/target_nfs
mount 10.1.12.17:/home/john/dev_scripts ~/target_nfs
```


#### Serveur Web [Python, NPM, PHP…]

Serveurs web (Apache, Nginx…), délivrent contenu/app via HTTP(S). Pour pentest, transfert de fichiers, points d’entrée applicatifs, phishin (pages leurres), tests config…

- Fichier conf :
    - /etc/apache2/apache2.conf

```bash
# Install
sudo apt install apache2 -y
```


#### Serveur Web Python

- Install Python & Web server

```bash
sudo apt install python3 -y
python3 -m http.server # Par défaut port TCP/8000 et dossier où c'est lancé
```


- Host dossier spécifique / Port spécifique
    
    ```bash
    python3 -m http.server --directory /home/cry0l1t3/target_files
    python3 -m http.server 443
    ```
    
    
    

#### VPN

Crée un tunnel chiffré pour accéder à un réseau distant. OpenVPN.

- Fichier de conf
    - /etc/openvpn/server.conf

```bash
# Install
sudo apt install openvpn -y

# Connect au VPN
sudo openvpn --config internal.ovpn
```


#### Divers

```bash
# NPM
http-server -p XX

# php
php -S 127.0.0.1:8080
```


#### Services Web [Apache, cURL, WGET]

- Communication entre navigateur et serveur web est centrale. Peut héberger avec Apache l’un des plus répandus, grâce à sa modularité.
    - Modules utiles : mod_ssl (chiffre échanges HHTPS), mod_proxy (proxy, reverse-proxy, redirection de trafic), mod_headers (ajuster en-têtes HTTP), mod_rewrite (réécritures d’URL)
    - Permet statique et dynamique via langages côtés serveur (PHP, Perl, Ruby, Python…)

#### Apache

- Install et démarrer Apache
    - page par défaut http://localhost
    - Apache écoute HTTP/80 par défaut.

```bash
sudo apt install apache2 -y
sudo systemctl start apache2
```


- Modifier conf / changer le port
    - /etc/apache2/ports.conf

#### Intéragir avec serveur Web

#### cURL (inspecter / automatiser)

Permet de récupérer pages/ressources et observer requêtes/réponses

```bash
curl http://localhost

# Divers
curl -I http://localhost            # en-têtes uniquement
curl -L http://exemple.tld          # suivre redirections
curl -k https://localhost           # ignorer cert non valide
```


#### Wget (télécharger / fichiers)

Pratique pour télécharger et faire des récupérations récursives simples.

```bash
wget http://localhost
```


#### Backup et restauration [Rsync, Deja Dup]

- Rsync : Synchro rapide/fiable (local ↔ distant). Transfère uniquement les différences (delta). Idéal pour sauvegardes incrémentales et transferts réseau.
- Duplicity : S’appuie sur rsync mais ajoute chiffrement et archives incrémentales (vers S3, FTP, SSH…)
- Deja Dup : Interface graphique simple (utilise duplicity), gère planification et sauvegardes chiffrées.
- Bonnes pratiques : Chiffrer sauvegardes avec outils supp GnuPG/LUKS, tester réguliérement restauration (échantillon de fichiers), éviter root si inutile (compte dédié + clés SSH), logguez jobs (rediriger sortie/erreurs).

#### Rsync

- Installer Rsync
    
    ```bash
    sudo apt install rsync -y
    ```
    
- Backup répertoire local vers serveur de backup
    
    ```bash
    rsync -av /path/to/mydirectory user@backup_server:/path/to/backup/directory
    # -a : archive : préserve attributs (permissions, timestamp...)
    # -v : verbose : Sortie précise de l'opération
    ```
    
- Backup avec compression et incrémentale
    
    ```bash
    rsync -avz --backup --backup-dir=/path/to/backup/folder --delete /path/to/mydirectory user@backup_server:/path/to/backup/directory
    
    # -z : compression
    # --delete : supprime fichiers de l'hôte distant qui ne sont plus présents dans source
    ```
    
- Restaurer backup serveur → local
    
    ```bash
    rsync -av user@remote_host:/path/to/backup/directory /path/to/mydirectory
    ```
    
- Vers support externe
    
    ```bash
    lsblk -f  #trouve point de montage
    rsync -a --delete /home/kali/mon_projet/ /media/kali/NOM_DU_DISQUE/backups/mon_projet/
    rsync -a /media/kali/NOM_DU_DISQUE/backups/mon_projet/ /home/kali/mon_projet/
    
    # Automatiser cron
    crontab -e
    # toutes les heures :
    0 * * * * rsync -a --delete /home/kali/mon_projet/ /media/kali/NOM_DU_DISQUE/backups/mon_projet/ >/tmp/rsync.log 2>&1
    ```
    

#### Rsync chiffré

Pour assurer sécurité, coupler avec SSH pour transfert secure.

```bash
rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```


- Authentification par clé
    
    ```bash
    ssh-keygen -t rsa -b 2048 # Générer paire de clés
    ssh-copy-id user@backup_server # Copier clé public au serveur distant
    ```
    

#### Auto-sync

Combiner rsync et cron.

- Créer script : RSYNC_Backup.sh
    - Si souhait de transfert à serveur distant, générer clés comme ci-dessus.

```bash
#!/bin/bash

rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```


- Ajouter permissions
    
    ```bash
    chmod -x RSYNC_Backup.sh
    ```
    
- Plannification cron (toutes les h)
    
    ```bash
    crontab -e
    ```
    
- Ligne à ajouter
    
    ```bash
    0 * * * * /path/to/RSYNC_Backup.sh
    ```
    
- Journaliser
    
    ```bash
    >> /var/log/rsync-backup.log 2>&1
    ```
    

#### Gestion file system [ext4, NTFS, fdisk, gpart…]

- Différents systèmes de fichiers
    - ext2 & ext3 : ancien sans journalisation, mais tjrs utile pour petits scénarios comme clés USB
    - ext4 : choix par défaut pour plupart systèmes Linux modernes, offre équilibre et performances, fiabilité et prise en charge fichiers volumineux.
    - Btrfs : Fonctions avancées comme instantanées et contrôles de l’intégrité des données.
    - XFS : Excelle dans gestion fichiers volumineux et perf élevées
    - NTFS : Initialement pour Windows, utile pour compatibilité lors de dual-boot ou de disques externes qui doivent fonctionner sur Linux et Windows
- Archi file system sur Linux organisé selon structure hiérarchique, plusieurs composants, les plus critiques inodes.
    - Inodes structures de données qui stockent métadata sur chaque fichiers et répertoire, y compris autorisations, propriété, taille et horodatages. Ne stockent pas données ou nom réels du fichier, mais contiennent pointeurs vers blocs où données du fichier sont stockées sur le disque.
    - Tables inodes : Collection de ces inodes, comme BDD que noyau Linux utilise pour suivre fichier/répertoire. Permet à l’OS d’accéder et de gérer fichiers.
- Sur Linux, fichiers peuvent être stockés dans ces types :
    - Regular files : Fichiers normaux type le plus courant généralement constitués de données texte (ASCII) et/ou données binaires (images, audio, exe).
    - Directories (répertoire) : Types spéciaux de fichiers qui servent de conteneux pour d’autres fichiers (normaux et autres répertoires).
    - Liens symboliques : Agissent comme raccourcis ou références vers d’autres fichiers situés dans différentes parties du système sans dupliquer le fichier en lui-même. Peut être utilisé pour rationaliser accès ou organiser structures de répertoires complexes en pointant vers fichiers importants.
- Chemin Absolu vs Relatif
    - Absolu : Adresse complète, commence toujours par /
        - Ex : /home/user/Documents/fichier.txt
    - Relatif : Itinérare depuis “là où je suis” (pwd)
        - Ex : Si je suis dans /home/user, chemin relatif est Documents/Fichier.txt

#### Inodes

```bash
ls -il                      # lister avec n° d’inode
stat <fichier>              # détails inode/blocs/timestamps
df -h                       # espace disque par FS
df -i                       # inodes libres/utilisés par FS
du -sh <chemin>             # taille d’un dossier/fichier
```


#### Liens symboliques

```bash
ln -s <cible> <lien>        # créer un symlink
	ln -s tmp/files/take-the-command-challenge take-the-command-challenge 
readlink -f <lien>          # résoudre la cible
```


#### Disque et partitions

```bash
sudo fdisk -l               # lister tables/partitions
lsblk -f                    # arborescence disques/FS/labels/UUID
blkid                       # UUID et types FS
sudo parted -l              # idem, GPT-friendly
```


#### Montage

- Lister montage
    
    ```bash
    mount
    findmnt -a
    ```
    
- Monter manuellement USB drive
    
    ```bash
    sudo mkdir -p /mnt/usb
    sudo mount /dev/sdb1 /mnt/usb # Détection auto du type
    cd /mnt/usb && ls -l
    ```
    
- Démonter (Umount)
    
    ```bash
    sudo umount /mnt/usb
    lsof +f -- /mnt/usb # Si occupé
    ```
    
- Mounted file systems au boot
    
    ```bash
    cat /etc/fstab
    
    UUID=<uuid>  <point_de_montage>  <type>  <options>  0  <pass>
    
    /dev/sda1 / ext4 defaults 0 0
    /dev/sda2 /home ext4 defaults 0 0
    /dev/sdb1 /mnt/usb ext4 rw,noauto,user 0 0
    ```
    

#### SWAP

- Gestion de la mémoire, garantit performances système fluides,
    - Extension RAM : quand la RAM est pleine, le noyau déplace des pages **inactives** vers la swap → libère de la RAM pour les processus actifs.
    - Hibernation : Etat complet de la mémoire écrit en swap, puis machine s’éteint.
- Voir état actuel

```bash
swapon --show # Liste swap actifs
free -h # Vue RAM/Swap
cat /proc/swaps # Détail noyau
```


- Créer swapfile
    
    ```bash
    # Créer le fichier (ex. 4 Go)
    sudo fallocate -l 4G /swapfile    # si indispo: sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
    
    # Sécuriser les droits
    sudo chmod 600 /swapfile
    
    # Formater en swap et activer
    sudo mkswap /swapfile
    sudo swapon /swapfile
    
    # Vérifier
    swapon --show && free -h
    ```
    

#### Desktop Environments [Gnome, KDE, X11…]

Linux est un noyau (texte). L'interface graphique n'est qu'un programme par-dessus. On peut la tuer sans éteindre l'ordinateur !

On appelle ça un **Environnement de Bureau (DE)**.

- **GNOME :** Le standard (Ubuntu, Fedora). Moderne, épuré, un peu lourd.
- **KDE Plasma :** Très personnalisable, ressemble plus à Windows.
- **XFCE :** Très léger, moche mais rapide (utilisé par défaut sur Kali Linux pour la perf).

C'est géré par un serveur d'affichage (historiquement **X11**, qui est en train d'être remplacé par **Wayland** plus sécurisé).

#### RDP sur Linux

- RDP : Principalement utilisé dans env Windows. Permet aux admin de se co à distance et intéragir avec bureau d’une machine W.
- VNC : Protocole dans env Linux. Fournit accès graphique aux PdT distants.

#### XServer

Partie user-side du système XWindows (X11). X11 système qui constitue ensemble de protocoles et d’app qui permettent d’avoir des fenêtres avec GUI.

#### Firewall setup [Iptables, Nftables, UFW…]

- Nftables : fournit syntaxe plus moderne et performances améliorées par rapport à iptables. Syntaxe nftables pas compatible avec iptables.
- UFW : fournit interface simple pour conf règles de pare-feu. Il est construit sur framework iptables.
- FirewallD : fournit solution de FW dynamique et flexible, peut gérer conf complexes.
- Iptables : Utilitaire qui fournit ensemble de règles pour filtrer trafic réseau. Composants principaux :
    
    
    | Composants | Description |
    | --- | --- |
    | Tables | Utilisé pour organiser et catégoriser les règles |
    | Chains | Utilisé pour grouper ensemble de règles appliquées à un type spécifique de traffic |
    | Règles | Définissent critères de filtrage du trafic réseau et actions à entreprendre |
    | Matches | Utilisé pour correspondre à critères spécifiques pour filtrage, tels que IP source/dest, port… |
    | Targets | Spécifient action pour paquets qui correspondent à règles spécifiques. peut être utilisé pour accept, drop ou reject paquet |
    
    ### Tables
    
    Catégorisent règles selon le type de traitement. Majorité du temps travail sur filter.
    
    | Nom table | Description | Chaînes intégrées |
    | --- | --- | --- |
    | filter | Filtrage “classique” (qui peut entrer/sortir/passer) basé sur IP, ports, protocoles. | INPUT, OUTPUT, FORWARD |
    | nat | Modifie source ou dest IP adresses d’un paquet | PREROUTING, POSTROUTING |
    | mangle | Ajuster en-têtes (cas avancés) | PREROUTING, OUTPUT, INPUT, FORWARD, POSTROUTING |
    | raw | Options spéciales (bypass, conntrack…) | PREROUTING, OUTPUT |
    
    ### Chaînes
    
    File de règles lues dans l’ordre
    
    - INPUT : Trafic vers la machine locale
    - OUTPUT : Trafic depuis la machine locale
    - FORWARD : Tarfic qui traverse la machine (routeur)
    - PREROUTING/POSTROUTING : avant/après routage (souvent par nat)
    
    ### Règles & Cibles (Targets)
    
    Règle = Critères (matches) + action (target)
    
    - Targets courants :
        - ACCEPT : laisser passer jusqu’à dest
        - DROP : Supprime paquet
        - REJECT : Supprime + renvoyer msg d’erreur à l’adresse source
        - LOG : journaliser
        - SNAT/DNAT/MASQUERADE/REDIRECT/MARK : NAT & usages avancés
    
    ### Matches
    
    Utilisées pour spécifier critères qui déterminent si règles de FW doit être appliquée à un paquet ou une co particulière.
    
    | **Match Name** | **Description** |
    | --- | --- |
    | `-p` or `--protocol` | Specifies the protocol to match (e.g. tcp, udp, icmp) |
    | `--dport` | Specifies the destination port to match |
    | `--sport` | Specifies the source port to match |
    | `-s` or `--source` | Specifies the source IP address to match |
    | `-d` or `--destination` | Specifies the destination IP address to match |
    | `-m state` | Matches the state of a connection (e.g. NEW, ESTABLISHED, RELATED) |
    | `-m mac` | Matches packets based on their MAC address |
    | `-m iprange` | Matches packets based on a range of IP addresses |
    
    ### Exemples :
    
    - Autoriser SSH en entrée
        
        ```bash
        sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
        ```
        
    - Lister règles
        
        ```bash
        sudo iptables -L -n -v
        ```
        

#### Logs système

#### Linux Logs Investigation

#### Explorer /var/log

#### Logs Kernel : kern.log & dmesg

```bash
- Simule chargement rootkit : sudo insmod /home/ubuntu/exploit/custom_kernel.ko

sudo tail -f /var/log/kern.log
sudo tail /var/log/dmesg
sudo dmesg -T | grep 'custom_kernel'
```


#### Authentification : auth.log

Tout ce qui touche à l’authent (SSH, sudo, succès/echecs)

```bash
ssh root@localhost -p 22
# Permission denied (publickey)

sudo tail -f /var/log/auth.log

- Co réussies : grep 'Accepted password' /var/log/auth.log
- Historique commande sudo : grep 'sudo' /var/log/auth.log
```


#### Journal syslog

Messages système généraux (cron, noyau, services…) 

```bash
- Tâches CRON : grep 'CRON' /var/log/syslog

- Message kernel visibles : grep 'kernel' /var/log/syslog
```


#### Traces de connexions : btmp & wtmp

```bash
Echecs de connexion : **/var/log/btmp

C**onnexions/déconnexions (qui, quand). **: /var/log/wtmp**
```


```bash
# Noyau (buffer mémoire)
sudo dmesg
sudo dmesg -T | grep 'motif'

# Noyau (persisté)
sudo tail -f /var/log/kern.log
sudo tail /var/log/dmesg

# Authentification
sudo tail -f /var/log/auth.log
grep 'Accepted password' /var/log/auth.log
grep 'sudo' /var/log/auth.log

# Système général
grep 'CRON' /var/log/syslog
grep 'kernel' /var/log/syslog
```


#### Logging levels & Kernel logs

- Deux familles de logs :
    - Kernel logs : Matériel, pilotes, erreirs système → Tout ce qui touche au coeur de l’OS
    - User logs : Interactions user/appli/OS → Connexions, exécutions de commandes, journaux applicatifs…
- Dans fichier /var/log/kern.log

```bash
# Vue volatile en mémoire (évolue et s'écrase)
sudo dmesg

# Voir tout (attention à la taille)
sudo cat /var/log/kern.log

# Lire confortablement, avec navigation
sudo less /var/log/kern.log

# Les 200 dernières lignes (vue rapide)
sudo tail -n 200 /var/log/kern.log
```


#### Journalctl

Système de logs binaire et structuré. Par défaut volatiles, rendre persistant via via /etc/systemd/journald.conf en définissant Storage=persistent, puis redémarrer le démon du journal.

```bash
Lire les logs : sudo journalctl

- Suivre en temps réel : journalctl -f

- Messages du noyau : journalctl -k

- Par boot (ex. boot précédent) : journalctl -b -1

- Par unité/service : journalctl -u apache.service

- Par priorité : journalctl -p err

- Inverser l’affichage (plus récents d’abord) : journalctl -r

- Limiter le nombre de lignes : journalctl -n 20

- Sans pager : journalctl --no-pager
```


```bash
Filtre : 

-Par date/heure (absolu) : sudo journalctl -S "2024-02-06 15:30:00" -U "2024-02-17 15:29:59"

- Par date/heure (relatif) : sudo journalctl -S "2 hours ago"

- Par service/unité : sudo journalctl -u nginx.service

- Par priorité : sudo journalctl -p crit

```


#### Cas d’usage typiques en IR/DFIR

- **Surveillance live** d’un incident : `journalctl -f -u <service>`
- **Corréler un incident dans une fenêtre temporelle** : `S ... -U ...`
- **Isoler erreurs graves** : `p err` ou `p crit`
- **Focaliser sur un composant** : `u apache.service`, `k` (noyau)

#### Logs du noyau (Kernel)

- Fichier : `/var/log/kern.log`
- Contenu : hardware drivers, appels systèmes, kernel events
- Ce qu’on y cherche : pilotes vulns, crashs, erreurs I/O, anomalies, traces rootkits…

#### Logs système

- Fichier : `/var/log/syslog`
- Contenu : events “OS” (démarrage, arrêt de services, connexions, reboot…)

#### Authentification logs

- Fichier : `/var/log/auth.log`
- Contenu : Tentatives d’authent user réussies/échouées.

#### Logs applicatifs

- Contenu : erreur et accès des services
- Exemples :
    - Apache : `/var/log/apache2/error.log`, `/var/log/apache2/access.log`
    - Nginx : `/var/log/nginx/error.log`, `/var/log/nginx/access.log`
    - OpenSSH : **auth** dans `/var/log/auth.log` (ou `/var/log/secure`)
    - MySQL : `/var/log/mysql/error.log`
    - PostgreSQL : `/var/log/postgresql/postgresql-<version>-main.log`
    - systemd (binaire) : `/var/log/journal/` (si persisté)

#### Logs sécurité

- Exemples :
    - Fail2ban : `/var/log/fail2ban.log`
    - UFW : `/var/log/ufw.log`
    - Événements sécurité génériques : souvent **syslog** et **auth.log**

#### Mémo

| Catégorie | Emplacement type |
| --- | --- |
| Kernel | `/var/log/kern.log` |
| Système | `/var/log/syslog` ou `/var/log/messages` |
| Authentification | `/var/log/auth.log` (Deb/Ub) / `/var/log/secure` (RHEL) |
| Apache | `/var/log/apache2/{access,error}.log` |
| Nginx | `/var/log/nginx/{access,error}.log` |
| SSH | dans **auth.log/secure** |
| MySQL | `/var/log/mysql/error.log` |
| PostgreSQL | `/var/log/postgresql/postgresql-*-main.log` |
| UFW | `/var/log/ufw.log` |
| Fail2ban | `/var/log/fail2ban.log` |
| journald (binaire) | `/var/log/journal/` (si stockage persistant activé) |

#### Lire et fouiller

```bash
# Suivre en live
tail -f /var/log/syslog

# Dernière lignes
tail -n 200 /var/log/auth.log

# Filtrer par motif
grep -i "failed password" /var/log/auth.log

# Avec horodatage système (journald)
journalctl -xe (erreurs récentes)
journalctl -u ssh --since "today" (service donné)
journalctl -k (messages kernel)
```


#### Shell [Instable, Alias, env…]

- Maintenir Shell instable
    
    ```bash
    python3 -c 'import pty; pty.spawn("/bin/bash")'
    ```
    

#### Alias

- Créer un alias temporaire
    - Dure pour session en cours, permet de définir nom pour commande ou séquence de commande
    
    ```bash
    # Créer alias nommé ll pour comande ls -la 
    alias ll='ls -la'
    ```
    
- Alias permanent
    - Ajout dans fichier de conf du shell (pour Basg ~/.bashrc
    
    ```bash
    nano ~/.bashrc
    alias ll='ls -la'
    alias update='sudo apt update && sudo apt upgrade'
    # Save fichier
    # Relancer shell ou mettre à jour avec source
    source ~/.bashrc
    ```
    

#### env

Fichier de conf : 

- Lister env ~/.bashrc ou **~/.zshrc**
    
    ```bash
    env
    ```
    
- Explorer des variables d’env
    
    ```bash
    echo $XXX
    echo $HOME # Affiche répertoire personnel
    echo $USER # Nom d'user actuel
    echo $SHELL # Affiche type de shell
    ```
    
- 🔺 Variable $PATH
    - Important car liste des dossiers dans lesquels le shell va chercher les programmes qd on tape une comande.
    - Quand on tape commande, shell parcourt cette liste dans l’ordre et exéc premier binaire trouvé avec ce nom.
    
    ```bash
    echo $PATH
    ```
    
    - Si installation dans repértoire non standard (ex : /opt/coolapp/bin) et essaye de l’exéc, probable d’avoir erreur, alors modif variable PATH en ajoutant répertoire.
- Définir variable d’env session en cours
    
    ```bash
    export TEST=test
    echo $TEST 
    ```
    
- Définir variable d’env persistente
    
    ```bash
    nano ~/.bashrc
    
    # Ajouter ligne export à la fin du fichier
    export TEST=test
    
    source ~/.bashrc
    ```
    

 

#### Linux Hardening

#### Sécurité physique

- Boot access = Root access : Si quelqu’un a un accès physique, il peut souvent modifier GRUB et booter en root.
- Solutions :
    - Mot de passe GRUB : Bloque l’édition du menu et les modes de secours
    - Chiffrement du disque (LUKS) : Si disque volé, données restent illisibles
    - Hygiène BIOS / UEFI : Mot de passe Setup, désactiver boot sur USB, activer Secure Boot/TPM…

```bash
sudo grub-mkpasswd-pbkdf2 
```


#### Partition et chiffrement filesystem

#### Firewall

- Netfilter
    - Moteur dans le kernel Linux
    - Font-ends pour le piloter : iptables, nftables; ufw, firwalld…
- iptables :

```bash
# 1) Autoriser SSH entrant (dport 22)
sudo iptables -A INPUT  -p tcp --dport 22 -j ACCEPT

# 2) Autoriser les réponses SSH sortantes (sport 22)
sudo iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

# 3) Tout le reste BLOQUÉ
sudo iptables -A INPUT  -j DROP
sudo iptables -A OUTPUT -j DROP
```


- nftables
    - Remplace progressivement iptables. On crée d’abord une table puis des chains (intput/output) puis des rules

```bash
# Chaîne input (hook input) et output (hook output)
sudo nft add chain ip fwfilter fwinput  '{ type filter hook input  priority 0; }'
sudo nft add chain ip fwfilter fwoutput '{ type filter hook output priority 0; }'

# Autoriser SSH vers la machine (destination port 22)
sudo nft add rule ip fwfilter fwinput  tcp dport 22 accept

# Autoriser réponses SSH sortantes (source port 22)
sudo nft add rule ip fwfilter fwoutput tcp sport 22 accept

# Vérifier
sudo nft list table ip fwfilter

```


- UFW
    - Très simple, gère iptables/nftables

```bash
# Activer ufw (si pas encore fait)
sudo ufw enable

# Politique par défaut (exemples)
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Autoriser SSH
sudo ufw allow 22/tcp

# Vérifier l’état
sudo ufw status verbose
```


### Mini check-list

- Savoir **ce que tu autorises** (services/ports) et **pourquoi** (politique claire).
- **iptables** : vider (`F`), écrire les règles, **DROP** en fin si tu veux un mode strict.
- **nftables** : créer **table → chains → rules** ; éventuellement `policy drop`.
- **ufw** : `default deny incoming`, `default allow outgoing`, puis `allow <port>/tcp`.
- Penser à la **persistance** des règles (selon ta distro/outils).
- Pour du contrôle “par application”, regarder **SELinux/AppArmor** (complémentaire au firewall).

#### Remote Access

```bash
Fichier de config OpenSSH : /etc/ssh/sshd_config

- empêcher connexions directes en root : PermitTootLogin no

- Générer / Déployer clé SSH : ssh-keygen -t rsa
- Coper la clé publique sur le serveur : ssh-copy-id username@server
# username = ton utilisateur ; server = IP ou hostname du serveur SSH

Activer clé et couper les mdp : 
PubkeyAuthentication yes   # active l’authentification par clé publique
PasswordAuthentication no  # désactive l’authentification par mot de passe

```


#### Securiser User Accounts

Ne pas utiliser le compte root

#### Utiliser sudo

```bash
usermod -aG sudo username
# usermod : modifie un compte
# -aG     : ajoute (-a) au(x) groupe(s) (-G)
# sudo    : groupe des utilisateurs autorisés à utiliser sudo
# username: le compte à modifier
```


#### Disable root

Une fois compte admin prêt, désactiver root en changeant son shell dans /etc/passwd

```bash
# Avant
root:x:0:0:root:/root:/bin/bash

# Après
root:x:0:0:root:/root:/sbin/nologin
```


#### Politique de MDP forte

Bibliothèque **libpwquality impose contrainte de mot de passe**

#### Disable Unused Accounts

En changeant son shell dans /etc/passwd

```bash
# Activé
michael:x:1000:1000:Michael:/home/michael:/usr/bin/fish

# Désactivé
michael:x:1000:1000:Michael:/home/michael:/sbin/nologin

```


Notions diverses :

- UID (User Identifier) : Identifiant numérique unique attribué à chaque utilisateur.
    - Permissions sur fichiers et processus ne sont pas basées sur le nom mais sur l’UID/
    - 0 = root
    - 1-999 = comptes systèmes
    - `≥1000` = comptes utilisateurs créés.
- GUID (Globally Unique Identifier) :
    - Identifiant global unique qui identifie de manière universelle un objet, indépendamment du domaine)
- GID (Group Identifier) : Identifiant numérique unique attribué à chaque groupe d’utilisateurs.
    - Permet de gérer des droits communs pour un ensemble d’utilisateurs
    - Groupe sudo = 27
    - Groupe ubuntu = GID 1000
- SID (Security Identifier) :
    - Identifiant unique attribué à chaque objet de sécurité (utilisateur, groupe, ordinateur…)

#### Containerisation

Permet d’emballer et exécuter appli dans env isolé appelé conteneur, ils partagent noyay de l’hôte (contrairement aux VM) → légers et scalable.

#### Docker

Outil pour automatiser déploiement d’applications.

| **Command** | **Description** |
| --- | --- |
| `docker ps` | List all running containers |
| `docker stop` | Stop a running container. |
| `docker start` | Start a stopped container. |
| `docker restart` | Restart a running container. |
| `docker rm` | Remove a container. |
| `docker rmi` | Remove a Docker image. |
| `docker logs` | View the logs of a container. |

#### Linux Containers (LXC)

Techno de vritualisation légère permet d’exécuter plusieurs systèmes Linux sur un hôte.

- Installation & création
    
    ```bash
    sudo apt install -y lxc
    sudo lxc-create -n linuxcontainer -t ubuntu
    ```
    
- Gestion de base
    
    ```bash
    lxc-ls
    lxc-start  -n linuxcontainer
    lxc-stop   -n linuxcontainer
    lxc-attach -n linuxcontainer   # entrer dans le conteneur
    ```
    

#### Shortcuts

| Catégorie | Raccourci | Action |
| --- | --- | --- |
| Auto-complétion | **TAB** | Complète noms de commandes/fichiers, affiche les choix. |
| Déplacement curseur | **Ctrl + A** | Début de ligne. |
|  | **Ctrl + E** | Fin de ligne. |
|  | **Ctrl + ← / →** | Saut au début du mot précédent/suivant (terminal selon config). |
|  | **Alt + B / Alt + F** | Mot précédent / mot suivant (readline). |
| Effacer | **Ctrl + U** | Efface du curseur au **début** de ligne. |
|  | **Ctrl + K** | Efface du curseur à la **fin** de ligne. |
|  | **Ctrl + W** | Efface le mot **avant** le curseur. |
| Coller (yank) | **Ctrl + Y** | Colle le dernier texte effacé via U/K/W. |
| Contrôle des tâches | **Ctrl + C** | Interrompt le processus courant (SIGINT). |
|  | **Ctrl + Z** | Met en pause au background (SIGTSTP). Reprendre : `fg` / `bg`. |
| Entrée/fin de flux | **Ctrl + D** | Envoie EOF (ferme l’entrée). En shell interactif : déconnexion si ligne vide. |
| Terminal | **Ctrl + L** | Efface l’affichage (équivalent `clear`). |
| Historique | **Ctrl + R** | Recherche dans l’historique (incrémental). |
|  | **↑ / ↓** | Parcourt commandes précédentes/suivantes. |
| Fenêtres | **Alt + Tab** | Bascule entre applications (environnement graphique). |
| Zoom terminal | **Ctrl + +** / **Ctrl + -** | Zoom avant / arrière (selon terminal). |
| Copie/Coller (terminal graphique) | **Ctrl + Shift + C / V** | Copier / coller (utile dans GNOME Terminal, Konsole, etc.). |

#### Audit de sécurité

#### Linux 101

#### Arborescence Linux



#### Gestion des permissions



#### Méthodologie

#### Suggestion d’outils

- Lynis : remonte des points non conf
- CIS-CAT Pro : Prend benchmark et check la conformité
- ss ; netstat’
- Scripts bash maison

#### Utilisateurs et permissions

- Permissions sur les fichiers de compte
- Cassage des MDP
    - passwd, shadow
- Fichiers sans propriétaires, ni groupes
- Comptes sans MDP
- Exécutable avec bit SUID, GUID
    - SUID : Binaire va être exec avec les droits de l’user proprio

#### Authentification et autorisation

- Politique de MDP
- Robustesse des algo de hash
- Conf SSH
- Activation et conf des Crons

#### Configurations

- Configuration des services
    - Limitation des services locaux
        - Voir si DB accessible depuis l’ext sinon que local
    - Relevé des services dangereux
        - xz dans certaines versions…
    - Lister interfaces en écoute : netstat
- Configuration réseau
    - Règles de pare-feu
    - Paramétrés réseaux IPv4 & IPv6
    - Mécanismes permettant le bannissement d’adresse IP
        - Fail2ban
- Système de journalisation
    - Activation des outils de journalisation
    - Politique des données journalisées
        - Fichiers remplis, peuvent saturer et écraser au fur et à mesure, mettre dans partition dédiée
    - Export de la journalisation

#### Élévation de privilège

- Environnements users
    - Exploitation de l’utilitaire “sudo”
    - Fichiers sensibles (historiques, clés privées)
        - History vidé à chaque session
    - Variables d’environnement et alias
    - Évasion de bash restreint
- Analyse du système de fichiers
    - Fichiers SUID & SGID
    - Fichiers et dossiers accessibles en écriture et lecture pour tous
    - Scripts et conf
- Compromission des applications et des services
    - Processus en cours d’exécution
    - Services et écoute
    - Conf et permissions des services
    - Version des paquets installés
- Propagation dans le réseau
    - Découverte de l’architecture réseau
    - Rejeu d’identifiants (mdp, clés privée)
    - Transfert de port et exfiltration de données

#### Recommandations

#### Idées et reco

- Utilisation d’image Linux minimale
- Téléchargement de version LTS
- Services au strict minimum
- Matrice des fluxs
- Affiner les droits au juste besoin
- Assurer le MCS
- S’assurer du bon fonctionnement du système de journalisation
- Bon à savoir
    - Investigation rapide
        
        # Identité & OS
        
        whoami
        id
        hostnamectl
        uname -a
        cat /etc/os-release
        
        # Uptime & logins
        
        uptime
        w
        who
        last
        
        # Réseau
        
        ip a
        ip r
        cat /etc/resolv.conf
        ss -tulpn
        
        # Disques
        
        lsblk
        df -h
        mount | column -t
        
        # Process & services
        
        ps aux --sort=-%mem | head
        ps aux --sort=-%cpu | head
        top
        systemctl list-units --type=service
        
        # Users & droits
        
        cat /etc/passwd
        cat /etc/group
        sudo -l
        lastlog
        
        # Périphériques / USB
        
        dmesg | grep -i usb | tail
        lsusb
        lsblk
        
        # Logs
        
        journalctl -xe
        journalctl -u ssh
        sudo less /var/log/auth.log
        sudo less /var/log/syslog
        
        # Cron
        
        crontab -l
        sudo crontab -l
        ls /etc/cron.*
        
    - Outils & Tips
        - Utiliser exa à la place de ls : plus joli
        - Accéder à un dossier (graphique) depuis shell : nautilus .
        - Capture zone spécifique : Shift + Impr écran
    - -Add nom pour adresse IP
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2210209e-8970-444f-bb22-a821220ae1c0/731c063a-c525-4923-b618-eff0bf3cd1ea/Untitled.png)
        
        .Nous allons éditer le fichier hosts en ajoutant l’adresse ip et le nom souhaité
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2210209e-8970-444f-bb22-a821220ae1c0/ff2f876e-02e4-4d20-94e1-9d35831e202e/Untitled.png)
        
        .Enregistrer le fichier, puis tester
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2210209e-8970-444f-bb22-a821220ae1c0/fe223f96-624b-4fc0-85c7-dcb7cbf6fbe6/Untitled.png)
        
        On peut voir que le ping vers camtest (nom rattaché à l’ip 8.8.8.8) fonctionne.
        
    - -Chercher mot dans le manuel : /mot
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2210209e-8970-444f-bb22-a821220ae1c0/4581e306-8a70-45a0-93ef-b21c2800d07b/Untitled.png)
        
    - su & sudo
        
        Bien sûr! `su` et `sudo` sont deux commandes utilisées pour exécuter des tâches avec des droits d'utilisateur différents de ceux de l'utilisateur actuel. Cependant, elles fonctionnent différemment et ont des usages distincts.
        
        ### `su` (Substitute User)
        
        - **Utilisation principale** : La commande `su` est utilisée pour changer d'utilisateur dans une session terminal.
        - **Comment ça marche** : Lorsque vous exécutez `su` suivi du nom d'un utilisateur, le système vous demande le mot de passe de cet utilisateur.
        - **Exemple** :
            
            ```
            su - john
            
            ```
            
            Cette commande vous demandera le mot de passe de `john` et vous donnera la session de `john` avec tous ses droits.
            
        - **Sans spécifier d'utilisateur** : Si vous exécutez `su` sans nom d'utilisateur, il assume par défaut que vous voulez devenir l'utilisateur `root` (le superutilisateur). Vous devrez donc fournir le mot de passe root.
        
        ### `sudo` (Super User Do)
        
        - **Utilisation principale** : La commande `sudo` permet à un utilisateur autorisé d'exécuter une commande en tant que superutilisateur ou un autre utilisateur, tel que défini dans le fichier `/etc/sudoers`.
        - **Comment ça marche** : Contrairement à `su`, lors de l'utilisation de `sudo`, vous entrez votre propre mot de passe, pas celui de l'utilisateur auquel vous essayez de changer ou celui de root. Si vous êtes autorisé (comme défini dans `/etc/sudoers`), la commande sera exécutée avec les privilèges du superutilisateur.
        - **Exemple** :
            
            ```
            sudo apt update
            
            ```
            
            Cette commande mettra à jour la liste des paquets en tant que superutilisateur, mais vous devrez entrer votre propre mot de passe.
            
        
        ### Différences clés entre `su` et `sudo`:
        
        1. **Mot de passe demandé** :
            - `su` demande le mot de passe de l'utilisateur auquel vous essayez de passer.
            - `sudo` demande votre propre mot de passe et vous autorise à exécuter une commande en tant que superutilisateur si vous êtes autorisé à le faire.
        2. **Contrôle granulaire** :
            - Avec `sudo`, vous pouvez définir des droits d'accès très spécifiques pour chaque utilisateur ou groupe d'utilisateurs. Par exemple, vous pouvez autoriser un utilisateur à exécuter seulement certaines commandes en tant que root.
        3. **Journalisation** :
            - Les actions effectuées avec `sudo` sont généralement enregistrées, ce qui est bénéfique pour savoir qui a fait quoi, surtout en cas de problème.
        
        ### Astuces et informations:
        
        1. **Éditer les autorisations sudo** : Le fichier `/etc/sudoers` définit qui peut utiliser `sudo` et comment. Il est recommandé d'utiliser `visudo` pour éditer ce fichier car cette commande vérifie la syntaxe avant de sauvegarder les modifications.
        2. **`sudo !!`** : Si vous oubliez de mettre `sudo` devant une commande nécessitant des droits root, tapez simplement `sudo !!`. Les deux points d'exclamation exécuteront la dernière commande entrée.
        3. **`sudo -i` ou `sudo -s`** : Ces commandes vous donnent un shell root. La première (`i`) vous donne un environnement de login root, tandis que la deuxième (`s`) vous donne un shell root avec votre environnement utilisateur actuel.
        4. **Sécurité** : Il est généralement considéré comme plus sûr de privilégier l'utilisation de `sudo` pour des tâches spécifiques plutôt que de se connecter en tant que `root` ou d'utiliser `su` pour devenir root. Ceci est principalement dû au contrôle granulaire et à la journalisation que `sudo` offre.
        
        J'espère que cette explication clarifie les choses et vous donne une bonne base pour comprendre et utiliser `su` et `sudo`!
        
    - Divers
        - vimtutor : Tuto VIM intégré
        - Chercher ligne contenant motif spécifique
            - grep -E "(my|false)" /etc/passwd
    - OverTheWire
        
        ### Level 0
        
        - Se connecter en SSH avec un port pas par défaut (bonne pratique sécurité changer port)
            - ssh -p port user@domain
        
        ### Level 0-1
        
        - ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
        
        
        
        ### Level 1-2
        
        - Ouvrir fichier “-”
            - cat ./- : mettre path
            - cat > -
        - 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
        
        
        
        ### Level 2-3
        
        - Lire fichier avec espace et —
            - cat "./--spaces in this filename--”
        - MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
        
        
        
        ### Level 3-4
        
        - Voir fichier caché : ls -la
        - 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
        
        ### Level 4-5
        
        - 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
        - Voir fichier humainement readable
            - file ./* | grep 'ASCII’
        
        ### Level 5-6
        
        HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
        
        - Trouver fichier avec caractéristiques spéficiques
            - find ./ -type f -size 1033c (Penser au c car correspond aux type bytes)
            - https://linuxize.com/post/how-to-find-files-in-linux-using-the-command-line/
        
        ### Level 6-7
        
        - Trouver fichier dans tous directories par user taille groupe
            - find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
                - 2>/devl/null masque les permissions denied
            - morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
        
        ### Level 7-8
        
        dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
        
        - Trouver mot fichier :
            - cat fichier.ext | grep -i mot
        
        ### Level 8-9
        
        4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
        
        - Trouver unique occurrence dans fichier, une seule ligne, mot unique :
            - sort data.txt | uniq -u
        
        ### Level 9-10
        
        FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
        
        - Trouver chaine de caractère strings humainement lisible avec entrée spécifique
            - strings data.txt | grep '=’
        
        ### Level 10-11
        
        dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
 

---

## Annexe — Questions types d'entretien et réponses types

### Questions essentielles

- **Question :** Décrivez la hiérarchie du système de fichiers Linux — les répertoires les plus importants.
  - **Réponse type :** Tout part de `/`, la racine. Les plus importants : `/etc` contient les fichiers de configuration système, `/var` les données variables comme les logs (`/var/log`), `/home` les dossiers personnels des utilisateurs, `/tmp` les fichiers temporaires, `/bin` et `/sbin` les binaires essentiels et d'administration. Pour un analyste sécurité, `/var/log` et `/etc` sont les répertoires critiques — c'est là qu'on trouve les traces d'activité et les configurations à auditer.

- **Question :** Quelle est la différence entre `su` et `sudo` ?
  - **Réponse type :** `su` change d'utilisateur — il demande le mot de passe de l'utilisateur cible. `sudo` exécute une commande avec les droits d'un autre utilisateur (souvent root), mais demande votre propre mot de passe. `sudo` est préférable en sécurité car il offre un contrôle granulaire via `/etc/sudoers`, une journalisation des actions, et n'oblige pas à partager le mot de passe root.

- **Question :** Quels fichiers de logs sont essentiels pour une investigation Linux ?
  - **Réponse type :** Les trois principaux : `/var/log/auth.log` pour toutes les authentifications (connexions SSH, sudo, création d'utilisateurs), `/var/log/syslog` pour les messages système généraux (services, cron, erreurs), et les logs applicatifs dans `/var/log/`. Pour les connexions, il y a aussi `wtmp` (historique des connexions réussies) et `btmp` (tentatives échouées), consultables avec la commande `last`.

- **Question :** Comment vérifier les mécanismes de persistence sur une machine Linux ?
  - **Réponse type :** Je regarderais les cron jobs (`/etc/crontab`, `crontab -l`), les services activés au démarrage (`systemctl list-unit-files --type=service`), les scripts d'initialisation dans `/etc/init.d/`, et les fichiers `.bashrc` de chaque utilisateur qui s'exécutent à l'ouverture d'un shell. Ce sont les endroits classiques où un attaquant peut placer de la persistence.

- **Question :** Expliquez le processus de démarrage Linux.
  - **Réponse type :** En quatre étapes : d'abord le firmware BIOS/UEFI fait le POST et trouve le disque de boot. Ensuite le bootloader (GRUB) charge le noyau en mémoire. Le kernel se décompresse, monte un système de fichiers temporaire, puis le vrai disque. Enfin, le premier processus (PID 1) est lancé — c'est systemd — qui démarre tous les services.

### Questions complémentaires

- **Question :** Quelles commandes utiliseriez-vous pour diagnostiquer un problème réseau sur Linux ?
  **Réponse type :** `ip a` pour voir les interfaces et adresses, `ip route show` pour la table de routage, `netstat -natp` ou `ss -natp` pour les connexions actives et les ports en écoute, `ping` pour tester la connectivité, et `tcpdump` pour capturer du trafic. En complément, `cat /etc/resolv.conf` pour vérifier le DNS configuré.

### Questions les plus probables en entretien

1. Hiérarchie du système de fichiers Linux ?
2. Différence `su` vs `sudo` ?
3. Logs essentiels pour une investigation ?
4. Où chercher la persistence sur Linux ?
5. Processus de démarrage Linux ?

### Réponses flash

- **Fichiers clés** → `/etc` (config), `/var/log` (logs), `/home` (users), `/tmp` (temporaire), `/bin` (binaires).
- **su vs sudo** → su = change d'user (mot de passe cible). sudo = exécute en tant que (votre mot de passe, journalisé, granulaire).
- **Logs investigation** → `auth.log` (auth), `syslog` (système), `wtmp`/`btmp` (connexions), `.bash_history` (commandes).
- **Persistence** → crontab, services systemd, /etc/init.d, .bashrc.
- **Boot** → BIOS/UEFI → GRUB → Kernel → systemd (PID 1).

---
        
        - Décoder base64
            - echo VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg== | base64 --decode

[Cheat sheet](https://www.notion.so/Cheat-sheet-2b73297e159781df9e28f265489a8e2e?pvs=21)
