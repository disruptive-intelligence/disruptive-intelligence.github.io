---
title: 2) Admin systèmes / réseaux
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Quelle différence entre un switch et un routeur ?**
  **Réponse type :** Le switch fonctionne à la couche 2 (liaison) — il connecte les machines d'un même réseau local en utilisant les adresses MAC. Il consulte sa table CAM pour savoir sur quel port envoyer la trame. Le routeur fonctionne à la couche 3 (réseau) — il connecte des réseaux différents en utilisant les adresses IP. Il consulte sa table de routage pour acheminer les paquets entre sous-réseaux. En résumé : le switch commute les trames localement, le routeur route les paquets entre réseaux.

- **Question : Qu'est-ce qu'ARP et à quoi ça sert ?**
  **Réponse type :** ARP (Address Resolution Protocol) traduit une adresse IP en adresse MAC sur un réseau local. Quand une machine veut communiquer avec une IP locale, elle a besoin de la MAC pour construire la trame Ethernet. Elle envoie une requête ARP en broadcast : « Qui a l'IP 192.168.1.20 ? ». La machine concernée répond avec sa MAC. Le résultat est mis en cache dans la table ARP. Le risque de sécurité c'est l'ARP spoofing : un attaquant envoie de fausses réponses ARP pour associer sa MAC à l'IP de la gateway — il se positionne en man-in-the-middle et intercepte tout le trafic.

- **Question : Sur un réseau Ethernet classique, comment une machine A (192.168.1.9) communique avec une machine B (192.168.1.3) ?**
  **Réponse type :** Les deux sont sur le même sous-réseau, donc la communication est locale. Machine A vérifie d'abord sa table ARP pour trouver la MAC de 192.168.1.3. Si elle ne l'a pas, elle envoie une requête ARP broadcast (« Qui a 192.168.1.3 ? »). Machine B répond avec sa MAC. Machine A construit alors une trame Ethernet avec la MAC de B en destination, encapsule le paquet IP dedans, et l'envoie sur le réseau. Le switch reçoit la trame, consulte sa table CAM pour trouver sur quel port est la MAC de B, et transmet la trame uniquement sur ce port. Pas besoin de routeur ici car les deux machines sont dans le même réseau.

- **Question : Qu'est-ce qu'un VLAN ?**
  **Réponse type :** Un VLAN (Virtual LAN) segmente logiquement un réseau physique en plusieurs domaines de broadcast distincts. Des machines branchées sur le même switch physique peuvent être dans des VLANs différents et ne se voient pas — c'est comme si elles étaient sur des réseaux physiques séparés. Pour communiquer entre VLANs, il faut passer par un routeur (ou un switch L3). C'est une mesure de sécurité de base en entreprise pour isoler les flux : un VLAN utilisateurs, un VLAN serveurs, un VLAN admin, un VLAN guest.

- **Question : Quelle différence entre un VLAN et une DMZ ?**
  **Réponse type :** Un VLAN est un mécanisme technique de segmentation réseau au niveau 2. Une DMZ est un concept d'architecture : c'est une zone réseau tampon entre Internet et le réseau interne, qui héberge les services exposés (reverse proxy, bastion, serveurs web publics). En pratique, une DMZ est souvent implémentée avec des VLANs et des firewalls. La différence c'est le niveau d'abstraction : le VLAN est l'outil, la DMZ est le design.

- **Question : Qu'est-ce que le mode access sur un switch ?**
  **Réponse type :** Un port en mode access est associé à un seul VLAN. Tout ce qui arrive sur ce port est automatiquement assigné à ce VLAN, et les trames sortent sans tag VLAN (le poste connecté ne sait même pas qu'il est dans un VLAN). C'est le mode utilisé pour connecter les postes de travail, les imprimantes, les serveurs — tout ce qui est un équipement terminal.

- **Question : Qu'est-ce que le mode trunk sur un switch ?**
  **Réponse type :** Un port en mode trunk transporte le trafic de plusieurs VLANs simultanément. Les trames sont taguées avec l'identifiant VLAN (tag 802.1Q) pour que le switch de l'autre côté sache à quel VLAN elles appartiennent. Le trunk est utilisé entre deux switches, entre un switch et un routeur, ou entre un switch et un hyperviseur qui héberge des VMs dans des VLANs différents.

- **Question : Où se trouve le fichier de configuration SSH ?**
  **Réponse type :** Côté serveur, c'est `/etc/ssh/sshd_config` — c'est là qu'on configure le port d'écoute, l'authentification par mot de passe ou par clé, la désactivation du root login, etc. Côté client, c'est `/etc/ssh/ssh_config` pour la config globale, ou `~/.ssh/config` pour la config par utilisateur. Les clés publiques autorisées sont dans `~/.ssh/authorized_keys`. Après modification de sshd_config, il faut redémarrer le service : `sudo systemctl restart sshd`.

- **Question : Où se trouvent les logs SSH ?**
  **Réponse type :** Sur les distributions Debian/Ubuntu, c'est `/var/log/auth.log`. Sur Red Hat/CentOS, c'est `/var/log/secure`. On peut aussi utiliser `journalctl -u sshd` pour les systèmes avec systemd. On y trouve les connexions réussies, échouées, les méthodes d'authentification utilisées. En forensic, c'est un artefact critique : `grep "Failed" /var/log/auth.log` pour voir les tentatives de brute force.

- **Question : Quelles commandes ou vérifications fais-tu en premier pour diagnostiquer un problème réseau ou système simple ?**
  **Réponse type :** Je procède par couches. D'abord la connectivité de base : `ip a` pour vérifier l'interface et l'adresse IP, `ping` vers la gateway puis vers une IP externe (8.8.8.8) pour isoler le problème. Ensuite le DNS : `nslookup` ou `dig` pour vérifier la résolution. Puis les routes : `ip route show` pour vérifier la table de routage. Les ports : `ss -natp` ou `netstat -natp` pour voir les connexions et les services en écoute. Les processus : `ps aux` pour vérifier que les services tournent. Les logs : `journalctl -xe` ou `/var/log/syslog` pour les erreurs récentes. Le disque : `df -h` pour l'espace. La mémoire et le CPU : `free -h` et `top`.

- **Question : Qu'est-ce que Kubernetes et ses grands principes ?**
  **Réponse type :** Kubernetes (K8s) est un orchestrateur de containers. Quand on a beaucoup de containers sur plusieurs serveurs, Docker seul ne suffit plus pour gérer le scaling, le self-healing, les mises à jour sans coupure, et le load balancing. Kubernetes automatise tout ça sur un cluster de nœuds. Les concepts clés : le Pod est la plus petite unité (un ou plusieurs containers ensemble), le Deployment gère le déploiement et le scaling des Pods, le Service donne une adresse réseau stable à un groupe de Pods, le Namespace sépare logiquement les ressources. L'architecture c'est un Control Plane (API Server, etcd, scheduler, controller manager) et des Worker Nodes (kubelet, container runtime). On décrit l'état souhaité dans des manifests YAML, et Kubernetes s'assure de maintenir cet état en permanence.

- **Question : Quelle différence entre un container et une VM ?**
  **Réponse type :** Un container partage le kernel de l'hôte et embarque uniquement l'application et ses dépendances. Il démarre en quelques secondes et consomme très peu de ressources. Une VM embarque un OS complet avec son propre kernel, ce qui offre une isolation plus forte mais la rend beaucoup plus lourde (Go de RAM, minutes au démarrage). En résumé : le container est plus léger et rapide, l'isolation est moindre car le kernel est partagé. La VM est plus lourde mais l'isolation est forte car chaque VM a son propre kernel.

- **Question : Quelle différence entre TCP et UDP ?**
  **Réponse type :** TCP est orienté connexion : il établit une session (three-way handshake), garantit la livraison dans l'ordre, et retransmet en cas de perte. C'est fiable mais plus lent. UDP est sans connexion : il envoie les données sans vérification ni garantie. C'est plus rapide et utilisé quand la vitesse prime — DNS, streaming, VoIP. En sécurité, savoir quel protocole utilise un service est essentiel pour le filtrage firewall et l'analyse de flux.

- **Question : Quels ports faut-il connaître absolument ?**
  **Réponse type :** 22 (SSH), 53 (DNS), 80/443 (HTTP/HTTPS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP), 5985/5986 (WinRM). En environnement AD, les ports Kerberos, LDAP et SMB sont critiques. En pentest : 21 (FTP), 25 (SMTP), 3306 (MySQL), 5432 (PostgreSQL), 8080 (HTTP alt).

---
