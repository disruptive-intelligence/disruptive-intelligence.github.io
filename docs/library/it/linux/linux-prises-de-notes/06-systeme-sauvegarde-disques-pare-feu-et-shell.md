---
title: 'Système : sauvegarde, disques, pare-feu et shell'
source: IT/01 Linux/Linux — prises de notes.md
note: Linux — prises de notes
up:
- - Linux — prises de notes
  - index.md
---

## Backup et restauration [Rsync, Deja Dup]

- Rsync : Synchro rapide/fiable (local ↔ distant). Transfère uniquement les différences (delta). Idéal pour sauvegardes incrémentales et transferts réseau.
- Duplicity : S’appuie sur rsync mais ajoute chiffrement et archives incrémentales (vers S3, FTP, SSH…)
- Deja Dup : Interface graphique simple (utilise duplicity), gère planification et sauvegardes chiffrées.
- Bonnes pratiques : Chiffrer sauvegardes avec outils supp GnuPG/LUKS, tester réguliérement restauration (échantillon de fichiers), éviter root si inutile (compte dédié + clés SSH), logguez jobs (rediriger sortie/erreurs).

### Rsync

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
    

### Rsync chiffré

Pour assurer sécurité, coupler avec SSH pour transfert secure.

```bash
rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```


- Authentification par clé
    
    ```bash
    ssh-keygen -t rsa -b 2048 # Générer paire de clés
    ssh-copy-id user@backup_server # Copier clé public au serveur distant
    ```
    

### Auto-sync

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
    

## Gestion file system [ext4, NTFS, fdisk, gpart…]

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

### Inodes

```bash
ls -il                      # lister avec n° d’inode
stat <fichier>              # détails inode/blocs/timestamps
df -h                       # espace disque par FS
df -i                       # inodes libres/utilisés par FS
du -sh <chemin>             # taille d’un dossier/fichier
```


### Liens symboliques

```bash
ln -s <cible> <lien>        # créer un symlink
	ln -s tmp/files/take-the-command-challenge take-the-command-challenge 
readlink -f <lien>          # résoudre la cible
```


### Disque et partitions

```bash
sudo fdisk -l               # lister tables/partitions
lsblk -f                    # arborescence disques/FS/labels/UUID
blkid                       # UUID et types FS
sudo parted -l              # idem, GPT-friendly
```


### Montage

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
    

### SWAP

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
    

## Desktop Environments [Gnome, KDE, X11…]

Linux est un noyau (texte). L'interface graphique n'est qu'un programme par-dessus. On peut la tuer sans éteindre l'ordinateur !

On appelle ça un **Environnement de Bureau (DE)**.

- **GNOME :** Le standard (Ubuntu, Fedora). Moderne, épuré, un peu lourd.
- **KDE Plasma :** Très personnalisable, ressemble plus à Windows.
- **XFCE :** Très léger, moche mais rapide (utilisé par défaut sur Kali Linux pour la perf).

C'est géré par un serveur d'affichage (historiquement **X11**, qui est en train d'être remplacé par **Wayland** plus sécurisé).

### RDP sur Linux

- RDP : Principalement utilisé dans env Windows. Permet aux admin de se co à distance et intéragir avec bureau d’une machine W.
- VNC : Protocole dans env Linux. Fournit accès graphique aux PdT distants.

### XServer

Partie user-side du système XWindows (X11). X11 système qui constitue ensemble de protocoles et d’app qui permettent d’avoir des fenêtres avec GUI.

## Firewall setup [Iptables, Nftables, UFW…]

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
        

### Logs système

### Linux Logs Investigation

### Explorer /var/log

### Logs Kernel : kern.log & dmesg

```bash
- Simule chargement rootkit : sudo insmod /home/ubuntu/exploit/custom_kernel.ko

sudo tail -f /var/log/kern.log
sudo tail /var/log/dmesg
sudo dmesg -T | grep 'custom_kernel'
```


### Authentification : auth.log

Tout ce qui touche à l’authent (SSH, sudo, succès/echecs)

```bash
ssh root@localhost -p 22
# Permission denied (publickey)

sudo tail -f /var/log/auth.log

- Co réussies : grep 'Accepted password' /var/log/auth.log
- Historique commande sudo : grep 'sudo' /var/log/auth.log
```


### Journal syslog

Messages système généraux (cron, noyau, services…) 

```bash
- Tâches CRON : grep 'CRON' /var/log/syslog

- Message kernel visibles : grep 'kernel' /var/log/syslog
```


### Traces de connexions : btmp & wtmp

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


### Logging levels & Kernel logs

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


### Journalctl

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


### Cas d’usage typiques en IR/DFIR

- **Surveillance live** d’un incident : `journalctl -f -u <service>`
- **Corréler un incident dans une fenêtre temporelle** : `S ... -U ...`
- **Isoler erreurs graves** : `p err` ou `p crit`
- **Focaliser sur un composant** : `u apache.service`, `k` (noyau)

### Logs du noyau (Kernel)

- Fichier : `/var/log/kern.log`
- Contenu : hardware drivers, appels systèmes, kernel events
- Ce qu’on y cherche : pilotes vulns, crashs, erreurs I/O, anomalies, traces rootkits…

### Logs système

- Fichier : `/var/log/syslog`
- Contenu : events “OS” (démarrage, arrêt de services, connexions, reboot…)

### Authentification logs

- Fichier : `/var/log/auth.log`
- Contenu : Tentatives d’authent user réussies/échouées.

### Logs applicatifs

- Contenu : erreur et accès des services
- Exemples :
    - Apache : `/var/log/apache2/error.log`, `/var/log/apache2/access.log`
    - Nginx : `/var/log/nginx/error.log`, `/var/log/nginx/access.log`
    - OpenSSH : **auth** dans `/var/log/auth.log` (ou `/var/log/secure`)
    - MySQL : `/var/log/mysql/error.log`
    - PostgreSQL : `/var/log/postgresql/postgresql-<version>-main.log`
    - systemd (binaire) : `/var/log/journal/` (si persisté)

### Logs sécurité

- Exemples :
    - Fail2ban : `/var/log/fail2ban.log`
    - UFW : `/var/log/ufw.log`
    - Événements sécurité génériques : souvent **syslog** et **auth.log**

### Mémo

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

### Lire et fouiller

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


## Shell [Instable, Alias, env…]

- Maintenir Shell instable
    
    ```bash
    python3 -c 'import pty; pty.spawn("/bin/bash")'
    ```
    

### Alias

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
    

### env

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
    

 

### Linux Hardening

### Sécurité physique

- Boot access = Root access : Si quelqu’un a un accès physique, il peut souvent modifier GRUB et booter en root.
- Solutions :
    - Mot de passe GRUB : Bloque l’édition du menu et les modes de secours
    - Chiffrement du disque (LUKS) : Si disque volé, données restent illisibles
    - Hygiène BIOS / UEFI : Mot de passe Setup, désactiver boot sur USB, activer Secure Boot/TPM…

```bash
sudo grub-mkpasswd-pbkdf2 
```


### Partition et chiffrement filesystem

### Firewall

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
