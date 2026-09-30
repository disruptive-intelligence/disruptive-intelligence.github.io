---
title: Investigation (forensics)
source: IT/01_Linux/Notion_Linux.md
note: Notions Linux
up:
- - Notions Linux
  - index.md
---

## Linux Forensics

### OS et information compte

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


### System configuration

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


### Mécanismes de persistance

```bash
Cron jobs : cat /etc/crontab

Service startup : ls /etc/init.d/
	- Permet de voir les services qui se lancent au démarrage comme sur Windows
	- Voir services systemd activés : systemctl list-unit-files --type=service 
	
.Bashrc : cat ~/.bashrc 
	- Fichier de conf exécuté automatiquement à l'ouverture d'un shell bash
```


### Evidence d’exécution

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


### Log files

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


### Processus/Services

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

### Identité

- PID (Process ID) : Chaque programme qui tourne a un numéro unique
    - PID 1 = Systemd
- UID (User ID) : Matricule d’utilisateur
    - UID 0 = root
    - UID 1 à 999 = Réservé aux Services/Daemons (ex : user www-data pour serveur web). N’ont pas le droit de se connecter à un écran, servent juste à faire tourner process en fond.
    - UID 1000+ = Utilisateurs normaux
- GID (Group ID) : Chaque utilisateur appartient à un groupe principal (souvent le même nom que l'utilisateur). Ça permet de partager des fichiers entre collègues.
