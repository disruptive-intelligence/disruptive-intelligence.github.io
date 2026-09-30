---
title: Réseau et services
source: IT/01_Linux/Notion_Linux.md
note: Linux — prises de notes
up:
- - Linux — prises de notes
  - index.md
---

## Gestion réseau [netstat, ss -tulnp, resolv.conf, interfaces…]

### Connaitre infos

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


### Configurer interfaces

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
    

### DNS

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

### Monitoring

- Syslog/rsyslog/journald : Logs système/service

### Troubleshooting

```bash
ping 8.8.8.8
traceroute example.com
dig example.com @8.8.8.8
tcpdump -i eth0 -n host <ip>
nmap -sS -sV -O -Pn <cible>
```


### Network Access Control (NAC)

- DAC (Discretionary Access Control) : Propriétaire choisit qui accède à la ressource.
- MAC (Mandatory Access Control) : L’OS impose politique
- RBAC : Droits via rôles

### Durcissement

- SELinux : Chaque process et chaque objet (fichier, socket, port…) a un contexte (type/role/domain). Une politique décrit quelles iinteractions sont permises.
- AppArmor : Attache un profil à un binaire (par chemin) décrivant ce qu’il peut lire/écrire/exécuter, quels capabilities il a, à quelles adresses il parle…
- TCP Wrappers : Deux fichiers /etc/hosts.allow & /etc/hosts.deny, décident une IP source a le droit d’accéder à un service.

### Planification de tâches

### Systemd (timer et service)

Principe : 

1. Créer un timer (planifie quand mytimer.service doit s’exécuter)
2. Créer un service (exécute commande / script)
3. Activer le timer 

### Créer timer

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

### Créer service

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


### Cron

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
    

## Service réseau [SSH, NFS, Python]

### SSH

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


### NFS

Permet de stocker et gérer fichiers sur systèmes distants comme s’ils étaient locaux (collaboration, centralisation). Aussi utile pour répliquer systèmes de fichiers entre serveurs. NFS-UTILS (Ubuntu)

```bash
# Installer serveur NFS
sudo apt install nfs-kernel-server -y

# Vérifier service 
systemctl status nfs-kernel-server
```


### Créer et configurer NFS

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


## Serveur Web [Python, NPM, PHP…]

Serveurs web (Apache, Nginx…), délivrent contenu/app via HTTP(S). Pour pentest, transfert de fichiers, points d’entrée applicatifs, phishin (pages leurres), tests config…

- Fichier conf :
    - /etc/apache2/apache2.conf

```bash
# Install
sudo apt install apache2 -y
```


### Serveur Web Python

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
    
    
    

### VPN

Crée un tunnel chiffré pour accéder à un réseau distant. OpenVPN.

- Fichier de conf
    - /etc/openvpn/server.conf

```bash
# Install
sudo apt install openvpn -y

# Connect au VPN
sudo openvpn --config internal.ovpn
```


### Divers

```bash
# NPM
http-server -p XX

# php
php -S 127.0.0.1:8080
```


## Services Web [Apache, cURL, WGET]

- Communication entre navigateur et serveur web est centrale. Peut héberger avec Apache l’un des plus répandus, grâce à sa modularité.
    - Modules utiles : mod_ssl (chiffre échanges HHTPS), mod_proxy (proxy, reverse-proxy, redirection de trafic), mod_headers (ajuster en-têtes HTTP), mod_rewrite (réécritures d’URL)
    - Permet statique et dynamique via langages côtés serveur (PHP, Perl, Ruby, Python…)

### Apache

- Install et démarrer Apache
    - page par défaut http://localhost
    - Apache écoute HTTP/80 par défaut.

```bash
sudo apt install apache2 -y
sudo systemctl start apache2
```


- Modifier conf / changer le port
    - /etc/apache2/ports.conf

### Intéragir avec serveur Web

### cURL (inspecter / automatiser)

Permet de récupérer pages/ressources et observer requêtes/réponses

```bash
curl http://localhost

# Divers
curl -I http://localhost            # en-têtes uniquement
curl -L http://exemple.tld          # suivre redirections
curl -k https://localhost           # ignorer cert non valide
```


### Wget (télécharger / fichiers)

Pratique pour télécharger et faire des récupérations récursives simples.

```bash
wget http://localhost
```
