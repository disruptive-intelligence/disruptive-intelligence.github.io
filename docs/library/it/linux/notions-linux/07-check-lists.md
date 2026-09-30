---
title: Check-lists
source: IT/01_Linux/Notion_Linux.md
note: Notions Linux
up:
- - Notions Linux
  - index.md
---

## Mini check-list

- Savoir **ce que tu autorises** (services/ports) et **pourquoi** (politique claire).
- **iptables** : vider (`F`), écrire les règles, **DROP** en fin si tu veux un mode strict.
- **nftables** : créer **table → chains → rules** ; éventuellement `policy drop`.
- **ufw** : `default deny incoming`, `default allow outgoing`, puis `allow <port>/tcp`.
- Penser à la **persistance** des règles (selon ta distro/outils).
- Pour du contrôle “par application”, regarder **SELinux/AppArmor** (complémentaire au firewall).

### Remote Access

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


### Securiser User Accounts

Ne pas utiliser le compte root

### Utiliser sudo

```bash
usermod -aG sudo username
# usermod : modifie un compte
# -aG     : ajoute (-a) au(x) groupe(s) (-G)
# sudo    : groupe des utilisateurs autorisés à utiliser sudo
# username: le compte à modifier
```


### Disable root

Une fois compte admin prêt, désactiver root en changeant son shell dans /etc/passwd

```bash
# Avant
root:x:0:0:root:/root:/bin/bash

# Après
root:x:0:0:root:/root:/sbin/nologin
```


### Politique de MDP forte

Bibliothèque **libpwquality impose contrainte de mot de passe**

### Disable Unused Accounts

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

### Containerisation

Permet d’emballer et exécuter appli dans env isolé appelé conteneur, ils partagent noyay de l’hôte (contrairement aux VM) → légers et scalable.

### Docker

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

### Linux Containers (LXC)

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
    

### Shortcuts

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

### Audit de sécurité

### Linux 101

### Arborescence Linux



### Gestion des permissions



### Méthodologie

### Suggestion d’outils

- Lynis : remonte des points non conf
- CIS-CAT Pro : Prend benchmark et check la conformité
- ss ; netstat’
- Scripts bash maison

### Utilisateurs et permissions

- Permissions sur les fichiers de compte
- Cassage des MDP
    - passwd, shadow
- Fichiers sans propriétaires, ni groupes
- Comptes sans MDP
- Exécutable avec bit SUID, GUID
    - SUID : Binaire va être exec avec les droits de l’user proprio

### Authentification et autorisation

- Politique de MDP
- Robustesse des algo de hash
- Conf SSH
- Activation et conf des Crons

### Configurations

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

### Élévation de privilège

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

### Recommandations

### Idées et reco

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
