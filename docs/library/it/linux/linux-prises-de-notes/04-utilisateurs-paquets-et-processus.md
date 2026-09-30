---
title: Utilisateurs, paquets et processus
source: IT/01_Linux/Notion_Linux.md
note: Linux — prises de notes
up:
- - Linux — prises de notes
  - index.md
---

## Gestion du système

## Gestions des users [passwd, shadow…]

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

### Gestion des packages

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

### DPKG

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
    

### APT (Advanced Package Manager)

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


### Process install complet

### Le Processus "Bout en Bout" 🔄

Prenons un exemple concret : Tu veux installer **Nmap**.

### Étape 1 : La Mise à Jour du Catalogue (`apt update`)

Tu tapes `sudo apt update`. Que se passe-t-il **réellement** ?

Ton PC ne télécharge **pas** de logiciels. Il télécharge des **listes de textes**.

1. APT lit `/etc/apt/sources.list`.
2. Il contacte les serveurs.
3. Il télécharge des fichiers compressés (ex: `Packages.gz`) qui contiennent la liste de tous les logiciels disponibles, leurs versions, et leurs **sommes de contrôle (Hashs)**.
4. Il stocke ces listes dans **`/var/lib/apt/lists/`**.

> ⚠️ Point Sécu : Si tu ne fais pas ça, ton PC pense que la version de Nmap disponible est la 7.80, alors que le serveur a la 7.90. Si tu essaies d'installer, le serveur dira "404 Not Found" car l'ancien fichier n'existe plus.
> 

### Étape 2 : La Résolution de Dépendances (`apt install nmap`)

Tu tapes `sudo apt install nmap`.

1. APT regarde dans sa base locale (`/var/lib/apt/lists/`).
2. Il voit : "Ok, Nmap v7.90".
3. **Le Calcul :** Il vérifie les besoins de Nmap. *"Ah, Nmap a besoin de la librairie `liblua` et `libpcap`"*.
4. Est-ce que tu les as déjà ? Non ? Alors APT décide de télécharger Nmap **ET** ses dépendances.

### Étape 3 : Le Téléchargement et le Stockage

APT télécharge les fichiers `.deb` (le paquet Nmap et les paquets des librairies).
Il ne les installe pas tout de suite ! Il les stocke dans une zone tampon (cache) :
📍 **`/var/cache/apt/archives/`**

### Étape 4 : La Vérification de Sécurité (CRITIQUE) 🛡️

C'est ici que la magie opère. Comment être sûr que le serveur n'a pas été piraté ou que tu n'as pas subi une attaque "Man-in-the-Middle" ?

1. Chaque dépôt officiel possède une paire de clés **GPG**.
2. La **Clé Publique** du dépôt est stockée sur ton PC (dans `/etc/apt/trusted.gpg.d/`).
3. Le fichier "Catalogue" que tu as téléchargé est **signé numériquement** avec la Clé Privée du dépôt.
4. APT vérifie la signature. Si elle est valide ➡️ Le catalogue est authentique.
5. APT calcule le **Hash (SHA256)** du fichier `.deb` téléchargé et le compare avec le Hash écrit dans le catalogue authentifié.

Si ça matche : C'est le vrai Nmap.
Si ça ne matche pas : **ALERTE ROUGE**, APT stoppe tout : *"Hash Sum Mismatch"*.

### Étape 5 : L'Extraction (Le passage de relais à DPKG) 📦

APT a fini son boulot (télécharger et vérifier). Il passe le fichier `.deb` à **DPKG**.

Un fichier `.deb`, c'est en réalité une archive (comme un Zip). DPKG l'ouvre. À l'intérieur, il y a deux archives :

1. **`control.tar.gz`** : Les instructions (Méta-données).
2. **`data.tar.gz`** : Les vrais fichiers du logiciel.

DPKG extrait `data.tar.gz` et copie les fichiers aux bons endroits :

- Le binaire `nmap` va dans `/usr/bin/`.
- La doc va dans `/usr/share/man/`.

### Étape 6 : La Configuration (Post-Install Scripts) ⚙️

Une fois les fichiers copiés, DPKG exécute les **scripts de post-installation** contenus dans le paquet.

- *Exemple :* Si tu installes un serveur web, le script va créer l'utilisateur `www-data`, générer les certificats par défaut, et lancer le service avec `systemctl`.

### Git (cloner outil)

```bash
git clone https:...
```


### PIP (Python Package Installer)

```bash
python3 -m pip install <paquet>
```


## Gestion des process et service [daemons, Systemd, SIGTERM…]

### Linux Process / Services

### System profiling

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


### Hunting for processes

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

### Services

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


## Lister / chercher [PS, PSTREE, SS -lntp]

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


### Kill process & signaux

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

### Mettre process en arrière-plan / avant-plan

Parfois nécessaire de mettre scan en arrière plan le temps de continuer d’autres choses

```bash
CTRL + Z # Suspend process en cours
jobs # Lister 
bg %X # Permet de relancer jobs souhaité en arrière
command & # Esperluète à la fin permet de mettre en arrière
fg X # Permet de relancer en avant
```


### Exécuter multiple commandes

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
