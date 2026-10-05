---
title: Questions d'entretien cyber & sysadmin
revision: transverse
domaine: ''
sources:
- Révision/Questions d'entretien cyber & sysadmin.md
---

*Préparation complète — Réponses orales, claires, professionnelles*

---

## 1) Tronc commun — Fondamentaux

---

- **Question : Qu'est-ce que le principe du moindre privilège ?**
    **Réponse type :** C'est le principe qui consiste à donner à chaque utilisateur, application ou processus uniquement les droits strictement nécessaires pour accomplir sa tâche, rien de plus. Un développeur n'a pas besoin d'être admin du domaine. Un compte de service n'a pas besoin d'accéder à toutes les bases de données. L'idée c'est de réduire la surface d'attaque : si un compte est compromis, l'attaquant n'a accès qu'à un périmètre limité. C'est un pilier de la sécurité qui s'applique partout — RBAC dans Kubernetes, IAM dans le cloud, GPO dans AD.

- **Question : Qu'est-ce que le principe de défense en profondeur ?**
    **Réponse type :** C'est le fait de superposer plusieurs couches de sécurité plutôt que de compter sur un seul mécanisme. Si une couche est contournée, la suivante prend le relais. Par exemple : un firewall périmétrique + une segmentation réseau + un EDR sur les postes + du MFA sur les comptes + du chiffrement des données au repos. Aucune mesure seule ne suffit — un attaquant qui contourne le firewall sera détecté par l'EDR, et même s'il contourne l'EDR, les données chiffrées limitent l'impact.

- **Question : Qu'est-ce qu'une adresse IP ?**
    **Réponse type :** C'est un identifiant logique attribué à une interface réseau pour permettre la communication entre machines sur un réseau IP. C'est l'équivalent d'une adresse postale : elle permet aux routeurs de savoir où acheminer les paquets. Il en existe deux versions : IPv4 (32 bits, notée en décimal — 192.168.1.10) et IPv6 (128 bits, notée en hexadécimal — 2001:db8::1). L'adresse IP fonctionne à la couche 3 (réseau) du modèle OSI.

- **Question : Quelle différence entre IPv4 et IPv6 ?**
    **Réponse type :** IPv4 utilise 32 bits, soit environ 4,3 milliards d'adresses — on est en pénurie depuis des années, d'où le NAT. IPv6 utilise 128 bits, soit un espace d'adressage quasi illimité, ce qui élimine le besoin de NAT. IPv6 est noté en hexadécimal (8 groupes de 4 caractères), intègre IPsec nativement, simplifie l'auto-configuration (SLAAC), et a des headers simplifiés. En pratique, la plupart des réseaux d'entreprise sont encore principalement en IPv4, avec une coexistence progressive.

- **Question : Quelle différence entre hexadécimal et binaire ?**
    **Réponse type :** Ce sont deux systèmes de numération. Le binaire (base 2) utilise uniquement 0 et 1 — c'est le langage natif des machines. L'hexadécimal (base 16) utilise 0-9 puis A-F, et c'est une notation plus compacte du binaire : chaque chiffre hexa représente exactement 4 bits. Par exemple, FF en hexa = 11111111 en binaire = 255 en décimal. L'hexa est utilisé pour les adresses MAC, IPv6, les hash, les couleurs web — partout où le binaire brut serait trop long à lire.

- **Question : Est-ce qu'un hôte qui n'a que de l'IPv4 peut communiquer directement avec un hôte qui n'a que de l'IPv6 ?**
    **Réponse type :** Non, pas directement. Les deux protocoles sont incompatibles — un paquet IPv4 ne peut pas être routé vers une destination IPv6 et vice versa. Pour les faire communiquer, il faut des mécanismes de transition : le dual-stack (les deux protocoles sur la même machine), le tunneling (encapsuler IPv6 dans IPv4 ou l'inverse), ou la translation (NAT64/DNS64 qui traduit entre les deux). En entreprise, la solution la plus courante c'est le dual-stack.

- **Question : Qu'est-ce que le DNS et comment fonctionne-t-il ?**
    **Réponse type :** Le DNS traduit un nom de domaine en adresse IP — c'est l'annuaire d'Internet. Quand tu tapes google.com dans le navigateur, voici ce qui se passe : d'abord le navigateur vérifie son propre cache, puis l'OS vérifie le fichier hosts local et le cache DNS système. Si pas de réponse, la requête part vers le serveur DNS récursif (celui configuré sur la machine ou attribué par le DHCP, souvent celui du FAI ou 8.8.8.8). Si le récursif n'a pas la réponse en cache, il interroge un serveur racine, qui le redirige vers le serveur TLD (.com, .fr), qui le redirige vers le serveur autoritaire du domaine (celui qui détient la zone). Le serveur autoritaire répond avec l'IP. La réponse remonte au récursif, qui la met en cache avec le TTL, puis au client. Tout ça utilise le port 53, principalement en UDP.

- **Question : Quand tu ouvres une page web dans ton navigateur, que se passe-t-il de bout en bout ?**
    **Réponse type :** Plusieurs étapes. D'abord la résolution DNS pour trouver l'IP du serveur — cache navigateur, cache OS, serveur récursif, racine, TLD, autoritaire. Ensuite, le navigateur établit une connexion TCP avec le three-way handshake (SYN, SYN-ACK, ACK). Si c'est HTTPS, le handshake TLS se met en place : le serveur présente son certificat, le navigateur vérifie la chaîne de confiance, ils négocient une cipher suite et échangent une clé de session via ECDHE. Puis le navigateur envoie une requête HTTP GET avec les headers (Host, User-Agent, Cookie). Le serveur traite la requête et renvoie la réponse (code 200, headers, body HTML). Le navigateur parse le HTML, télécharge les ressources référencées (CSS, JS, images — chacune peut nécessiter une nouvelle résolution DNS et connexion), construit le DOM et le CSSOM, exécute le JavaScript, et affiche la page.

- **Question : Quelle différence entre HTTP et HTTPS ?**
    **Réponse type :** HTTP transmet les données en clair — n'importe qui sur le réseau peut lire le trafic (credentials, cookies, données). HTTPS c'est HTTP encapsulé dans un tunnel TLS qui chiffre la communication entre le client et le serveur. HTTPS garantit la confidentialité (personne ne peut lire les données en transit), l'intégrité (les données ne sont pas altérées), et l'authentification du serveur (via le certificat). HTTP utilise le port 80, HTTPS le port 443. Aujourd'hui, tout doit être en HTTPS.

- **Question : Comment fonctionne HTTPS ?**
    **Réponse type :** HTTPS repose sur TLS. Lors du handshake : le client envoie un ClientHello avec les cipher suites supportées, le serveur répond avec son certificat et la cipher suite choisie. Le client vérifie la chaîne de confiance du certificat (signé par une CA intermédiaire, elle-même signée par une CA racine dans le trust store). Ensuite, client et serveur font un échange de clés Diffie-Hellman éphémère (ECDHE) pour calculer un secret partagé — la clé de session. À partir de là, tout le trafic est chiffré en symétrique (AES-GCM typiquement) avec cette clé de session. La clé privée du serveur ne sert qu'à signer le DH, pas à chiffrer — c'est ce qui permet la Forward Secrecy.

- **Question : Qu'est-ce qu'un hash ?**
    **Réponse type :** Un hash c'est une empreinte numérique de taille fixe calculée à partir de données de taille quelconque, via une fonction mathématique à sens unique. Propriétés essentielles : c'est déterministe (la même entrée donne toujours le même hash), irréversible (on ne peut pas retrouver l'entrée à partir du hash), et résistant aux collisions (extrêmement difficile de trouver deux entrées différentes qui produisent le même hash). Un changement d'un seul bit en entrée change radicalement le hash (effet avalanche). Exemples : SHA-256 (sûr), MD5 (cassé — collisions trouvées). Usages : vérification d'intégrité de fichiers, stockage de mots de passe (avec salt), signatures numériques, forensic.

- **Question : Quelle différence entre chiffrement symétrique et asymétrique ?**
    **Réponse type :** Le symétrique utilise la même clé pour chiffrer et déchiffrer — c'est rapide (AES, ChaCha20), mais il faut résoudre le problème de l'échange de clé : comment transmettre la clé secrète de manière sécurisée ? L'asymétrique utilise une paire de clés : publique pour chiffrer, privée pour déchiffrer (RSA, ECC). C'est plus lent mais résout le problème de l'échange. En pratique, on combine les deux — c'est le modèle hybride : l'asymétrique (ou Diffie-Hellman) sert à échanger la clé symétrique, puis le symétrique fait le gros du travail. C'est ce que font TLS, SSH, et GPG.

---

## 2) Admin systèmes / réseaux

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

## 3) Cybersécurité

---

- **Question : Qu'est-ce qu'une vulnérabilité ?**
    **Réponse type :** C'est une faiblesse dans un système, un logiciel, une configuration ou un processus, qui peut être exploitée pour compromettre la sécurité. Ça peut être un bug logiciel (buffer overflow), une configuration par défaut non durcie (mot de passe admin/admin), un composant non patché (CVE connue), ou une erreur de design (IDOR dans une API). Une vulnérabilité en soi ne cause pas de dommage — c'est son exploitation qui le fait.

- **Question : Qu'est-ce qu'une menace ?**
    **Réponse type :** C'est tout événement ou acteur susceptible d'exploiter une vulnérabilité et de causer un dommage. Ça peut être un acteur humain (un attaquant, un insider malveillant), un groupe organisé (APT, ransomware gang), ou un événement naturel (incendie, inondation). La menace est définie par sa capacité, son intention et son opportunité.

- **Question : Qu'est-ce qu'un risque ?**
    **Réponse type :** C'est la combinaison d'une menace exploitant une vulnérabilité, multipliée par l'impact potentiel. En gestion des risques, on l'évalue souvent comme : risque = probabilité × impact. Un risque élevé c'est quand une vulnérabilité est facilement exploitable, qu'une menace crédible existe, et que l'impact serait important. Le risque se gère de 4 façons : le réduire (patch, hardening), l'accepter (si le coût de protection dépasse l'impact), le transférer (assurance cyber), ou l'éviter (supprimer le service).

- **Question : Qu'est-ce qu'un SIEM et à quoi sert-il ?**
    **Réponse type :** Un SIEM (Security Information and Event Management) centralise et corrèle les logs de toute l'infrastructure — postes, serveurs, firewalls, proxy, AD, cloud. Il permet de détecter les incidents en temps réel via des règles de corrélation (par exemple : 50 échecs de connexion depuis la même IP en 5 minutes = probable brute force). Il fournit une vue unifiée pour l'investigation, le stockage longue durée pour la conformité, et des dashboards pour le reporting. Exemples : Splunk, Microsoft Sentinel, Elastic Security.

- **Question : Qu'est-ce qu'un IOC ?**
    **Réponse type :** Un IOC (Indicator of Compromise) est un artefact observable qui indique qu'une compromission a eu lieu ou est en cours. Ça peut être un hash de fichier malveillant, une adresse IP ou un domaine C2, une clé de registre suspecte, un user-agent inhabituel. Les IOC sont utiles pour la détection immédiate mais ils sont fragiles — l'attaquant les change facilement entre chaque campagne. C'est pour ça que la détection basée sur les TTP (comportements) est plus durable.

- **Question : Qu'est-ce que le threat hunting ?**
    **Réponse type :** C'est la recherche proactive de menaces dans le SI, guidée par une hypothèse — pas par une alerte. Le hunter cherche ce que les règles du SIEM et de l'EDR ne voient pas : les attaquants qui ont délibérément évité de déclencher les alertes. L'objectif c'est de réduire le dwell time. On part d'une hypothèse liée à une technique ATT&CK, on construit une requête, on cherche dans la télémétrie, et on documente la conclusion. Un hunt négatif n'est pas un échec — ça confirme l'absence de la menace avec le scope donné.

- **Question : Quelles sont les grandes étapes d'une réponse à incident ?**
    **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (playbooks, outillage, exercices — c'est avant l'incident), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping, timeline), Confinement-Éradication-Restauration (isoler la menace, nettoyer les persistances, reconstruire, vérifier), et Post-Incident (retex, root cause analysis, amélioration). En réalité c'est itératif — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication.

- **Question : Que fais-tu en premier face à un poste suspecté compromis ?**
    **Réponse type :** D'abord : ne PAS éteindre la machine — la mémoire RAM contient des preuves critiques (processus malveillants, clés de chiffrement, connexions C2). Je vérifie via l'EDR ou en consultant les logs si l'activité est confirmée suspecte. Si oui, je fais un dump mémoire (DumpIt) avant toute autre action. Ensuite j'isole le poste du réseau (sans l'éteindre), je lance un triage KAPE pour collecter les artefacts, et je vérifie si l'attaquant est présent ailleurs dans le SI. La préservation des preuves dès le début est essentielle.

- **Question : Comment vérifier rapidement si un fichier est suspect ?**
    **Réponse type :** Plusieurs vérifications rapides. D'abord le hash : calculer le SHA-256 du fichier et le chercher sur VirusTotal. Vérifier la signature numérique (sur Windows : clic droit → Propriétés → Signatures numériques, ou `Get-AuthenticodeSignature` en PowerShell) — un fichier non signé ou avec une signature invalide dans System32 est suspect. Regarder les métadonnées (date de création, taille, nom) et comparer avec ce qui est attendu. Sur un système live, vérifier avec Process Explorer si le processus associé charge des DLLs inhabituelles. Et utiliser l'outil `strings` pour extraire les chaînes lisibles — les URLs, les IPs, les clés de registre peuvent révéler la nature du fichier.

- **Question : Pourquoi la centralisation des logs est-elle importante en sécurité ?**
    **Réponse type :** Parce que la première chose qu'un attaquant fait après avoir compromis un système, c'est effacer les logs locaux. Si les logs sont centralisés dans un SIEM, il ne peut pas les supprimer. La centralisation permet aussi la corrélation : un événement isolé sur un poste ne semble pas suspect, mais corrélé avec d'autres événements sur d'autres systèmes, ça révèle un mouvement latéral ou une chaîne d'attaque. Enfin, c'est indispensable pour le forensic et la conformité — reconstituer une timeline d'attaque sur 60 jours est impossible si les logs n'ont pas été conservés.

- **Question : Quels sont les moyens de persistance d'un malware sur Linux et sur Windows ?**
    **Réponse type :** Sur Windows : clés de registre Run/RunOnce (exécution au logon), services (gérés par SCM), tâches planifiées (schtasks), DLL hijacking, COM hijacking, WMI event subscriptions, Winlogon Shell/Userinit, et des mécanismes plus avancés comme les bootkit UEFI. Autoruns de Sysinternals les recense tous. Sur Linux : cron jobs (`/etc/crontab`, `crontab -l`), services systemd (systemctl enable), scripts dans `/etc/init.d/`, fichiers `.bashrc` ou `.profile` (exécutés à l'ouverture de shell), clés SSH dans `authorized_keys`, et des modules kernel malveillants (rootkits).

- **Question : Comment est effectué un mouvement latéral ?**
    **Réponse type :** L'attaquant utilise des credentials volés pour se déplacer d'un système à un autre dans le réseau. Les techniques principales : Pass-the-Hash (utiliser un hash NTLM sans connaître le mot de passe — Mimikatz), PsExec (exécution à distance via SMB — crée un service temporaire), WMI (exécution à distance via WMI), WinRM/PowerShell Remoting, RDP, et les tâches planifiées à distance. Chaque technique laisse des traces différentes dans les logs (4624 logon type 3, 7045 création de service, etc.). C'est pourquoi la segmentation réseau, le tiering AD, et LAPS sont essentiels — ils limitent les possibilités de mouvement latéral.

- **Question : Comment faire de la reconnaissance sur une cible ?**
    **Réponse type :** En OSINT passif d'abord : Whois pour le propriétaire du domaine et les contacts, les enregistrements DNS (A, MX, TXT — SPF/DKIM/DMARC révèlent l'infrastructure mail), crt.sh pour les certificats SSL (révèle les sous-domaines), Shodan/Censys pour les services exposés, Google dorks pour les fichiers et pages indexées. LinkedIn pour les employés et la stack technique. Ensuite en actif (avec autorisation) : scan Nmap pour les ports et services, énumération DNS (transferts de zone, brute force de sous-domaines), scan de répertoires web (gobuster, dirsearch). En environnement AD interne : BloodHound/SharpHound pour les chemins d'attaque, LDAP pour l'énumération des objets AD.

- **Question : Qu'est-ce que le Kerberoasting et comment s'en protéger ?**
    **Réponse type :** Le Kerberoasting exploite le fait que tout utilisateur du domaine peut demander un ticket de service (TGS) pour n'importe quel SPN. Ce ticket est chiffré avec le hash du compte de service — si le mot de passe est faible, on le cracke en offline avec hashcat ou john. La défense principale c'est d'utiliser des gMSA (Group Managed Service Accounts) avec des mots de passe de 240 caractères rotés automatiquement. Sinon : mots de passe 25+ caractères sur les comptes de service et forcer l'AES au lieu de RC4.

- **Question : C'est quoi un DCSync et comment le détecter ?**
    **Réponse type :** Un DCSync simule un contrôleur de domaine pour demander la réplication des hashes via le protocole de réplication AD. L'attaquant a besoin des droits DS-Replication-Get-Changes et DS-Replication-Get-Changes-All. Côté détection, c'est l'Event ID 4662 avec des droits de réplication depuis une machine qui n'est PAS un DC — ça doit être une alerte critique.

---

## 4) Réseau / Infra / Virtualisation

---

- **Question : Qu'est-ce qu'un RAID ?**
    **Réponse type :** RAID (Redundant Array of Independent Disks) est une technologie qui combine plusieurs disques physiques pour améliorer la performance, la redondance, ou les deux. L'idée c'est soit d'aller plus vite en répartissant les données (striping), soit de résister à la panne d'un disque (mirroring/parité), soit un mix des deux.

- **Question : Quelle différence entre RAID 0, RAID 1, RAID 5, RAID 6 et RAID 10 ?**
    **Réponse type :** RAID 0 (striping) répartit les données sur tous les disques sans redondance — ça double les performances mais si un seul disque tombe, tout est perdu. RAID 1 (mirroring) duplique les données sur deux disques — redondance totale, perte de 50% de la capacité. RAID 5 répartit les données avec de la parité distribuée sur au moins 3 disques — tolère la perte d'un disque, bonne capacité utile (n-1 disques). RAID 6 c'est comme le RAID 5 mais avec double parité — tolère la perte de 2 disques simultanément. RAID 10 (1+0) combine mirroring et striping — performance et redondance, mais coûteux (50% de la capacité utile, minimum 4 disques). En production critique, RAID 6 ou RAID 10 sont recommandés.

- **Question : Qu'est-ce que le kernel space et le user space ?**
    **Réponse type :** Le kernel space (Ring 0) c'est la zone mémoire où s'exécutent le noyau du système d'exploitation et les drivers — accès total au matériel et à toute la mémoire. Un crash ici provoque un écran bleu (Windows) ou un kernel panic (Linux). Le user space (Ring 3, ou userland) c'est la zone où tournent les applications normales — accès limité et contrôlé. Un crash en user space ne fait planter que le processus concerné. Cette séparation est la base de la sécurité : un processus utilisateur ne peut pas accéder directement au matériel ou à la mémoire d'un autre processus — il doit passer par des syscalls contrôlés par le noyau.

- **Question : Quelle différence concrète entre une machine virtuelle et un conteneur ?**
    **Réponse type :** La VM embarque un OS complet avec son propre kernel, au-dessus d'un hyperviseur. Chaque VM est fortement isolée mais consomme des Go de RAM et met des minutes à démarrer. Le container partage le kernel de l'hôte et n'embarque que l'application et ses dépendances — il démarre en secondes et consomme très peu. L'isolation d'un container est moins forte (kernel partagé) mais suffisante pour la plupart des usages. En sécurité : un escape de container donne accès au kernel de l'hôte, un escape de VM est beaucoup plus difficile.

- **Question : Quelle différence entre un NAS et un SAN ?**
    **Réponse type :** Un NAS (Network Attached Storage) est un serveur de fichiers accessible via le réseau IP (protocoles SMB, NFS). Il partage des fichiers — c'est simple à déployer, utilisé pour le partage de fichiers classique et les sauvegardes. Un SAN (Storage Area Network) est un réseau de stockage dédié qui fournit des volumes de blocs bruts (protocoles Fibre Channel, iSCSI). Le serveur voit le stockage SAN comme un disque local. Le SAN est utilisé pour les bases de données, la virtualisation — là où les performances I/O sont critiques. En résumé : le NAS partage des fichiers, le SAN partage du stockage bloc.

- **Question : Quelle différence entre vCenter et vSphere ?**
    **Réponse type :** vSphere c'est la suite complète de virtualisation VMware — c'est le nom commercial de l'ensemble. ESXi est l'hyperviseur bare-metal qui s'installe sur chaque serveur physique. vCenter est la console d'administration centralisée qui permet de gérer plusieurs ESXi : migration de VMs (vMotion), HA, DRS, templates, snapshots. Sans vCenter, on administre chaque ESXi individuellement. En sécurité, vCenter est un composant Tier 0 — sa compromission donne le contrôle total sur toute l'infrastructure virtualisée.

- **Question : Comment fonctionne le swap ?**
    **Réponse type :** Le swap c'est une zone du disque utilisée comme extension de la RAM quand la mémoire physique est pleine. Quand le système manque de RAM, il déplace les pages mémoire les moins utilisées (pages inactives) vers le swap sur le disque pour libérer de la RAM pour les processus actifs. C'est beaucoup plus lent que la RAM. Sous Linux, c'est soit une partition swap soit un fichier swap (`swapon`, `swapoff`). En forensic, le swap (pagefile.sys sur Windows, swap sur Linux) peut contenir des fragments de données sensibles — credentials, code malveillant — car la mémoire y a été copiée.

---

## 5) DNS / VPN / Protocoles

---

- **Question : Quels sont les différents mécanismes autour du DNS : DNSSEC, DoH, DoT ?**
    **Réponse type :** DNSSEC (DNS Security Extensions) ajoute de la signature cryptographique aux réponses DNS — ça garantit l'authenticité et l'intégrité de la réponse (pas de spoofing), mais ça ne chiffre PAS la requête. DoT (DNS over TLS, port 853) chiffre les requêtes DNS dans un tunnel TLS — le contenu est confidentiel, mais le FAI voit qu'on utilise le port 853. DoH (DNS over HTTPS, port 443) encapsule les requêtes DNS dans du HTTPS — le trafic se mélange avec le trafic web normal, impossible à distinguer et à bloquer. En résumé : DNSSEC = intégrité, DoT/DoH = confidentialité. Ils sont complémentaires.

- **Question : Quelle différence entre un VPN IPsec et un VPN SSL ?**
    **Réponse type :** IPsec fonctionne au niveau réseau (couche 3) — il crée un tunnel entre deux réseaux et donne accès à tout le réseau distant comme si on était branché localement. C'est utilisé pour le site-to-site et le remote access d'entreprise. Le VPN SSL/TLS fonctionne au niveau applicatif (couche 7) — il donne accès à des applications spécifiques via le navigateur ou un client léger. C'est plus simple à déployer (passe les firewalls car c'est du HTTPS sur le port 443) mais moins flexible. IPsec offre un accès réseau complet, SSL/TLS offre un accès granulaire par application.

- **Question : Comment fonctionne un VPN IPsec dans les grandes lignes ?**
    **Réponse type :** En deux phases. Phase 1 (IKE SA) : les deux extrémités négocient les paramètres de sécurité (algorithmes, authentification), s'authentifient mutuellement (clé pré-partagée ou certificat), et établissent un canal sécurisé pour la négociation. Phase 2 (IPsec SA) : dans ce canal sécurisé, elles négocient les paramètres du tunnel de données (algorithmes de chiffrement et d'intégrité, durée de vie). Ensuite le tunnel est établi et le trafic est chiffré — soit en mode tunnel (tout le paquet IP est encapsulé — utilisé pour le site-to-site), soit en mode transport (seul le payload est chiffré — utilisé entre deux hôtes).

- **Question : Comment fonctionne un VPN SSL/TLS dans les grandes lignes ?**
    **Réponse type :** Il établit un tunnel chiffré au-dessus de TLS, comme un site HTTPS. Le client se connecte au concentrateur VPN sur le port 443, le handshake TLS s'effectue (certificat serveur, échange de clés ECDHE, clé de session). Une fois le tunnel établi, le trafic est chiffré en AES-GCM. Deux modes : le portail web (accès à des applications via le navigateur, sans client) ou le tunnel complet (avec un client comme OpenVPN ou AnyConnect, qui route tout le trafic ou une partie via le tunnel). L'avantage c'est que le port 443 est rarement bloqué par les firewalls.

---

## 6) Forensic / Windows / Triage

---

- **Question : Comment vérifier la signature d'un fichier avec PowerShell ?**
    **Réponse type :** `Get-AuthenticodeSignature -FilePath C:\chemin\fichier.exe`. Ça retourne le statut de la signature : Valid (signée et chaîne de confiance valide), NotSigned (pas de signature — suspect si c'est dans System32), HashMismatch (fichier modifié après signature — très suspect), ou UnknownError. Pour vérifier en ligne : calculer le hash avec `Get-FileHash` et le soumettre à VirusTotal.

- **Question : Qu'est-ce qu'un dump de la base SAM ?**
    **Réponse type :** La SAM (Security Accounts Manager) est la base de données qui stocke les hashes NTLM des comptes locaux Windows. Un dump SAM permet à un attaquant de récupérer ces hashes pour les craquer offline ou les utiliser en Pass-the-Hash. La SAM est verrouillée quand Windows tourne — l'attaquant utilise des outils comme Mimikatz, reg save, ou boot depuis un live USB pour y accéder.

- **Question : Pour exploiter un dump SAM, quelles ruches faut-il récupérer en plus ?**
    **Réponse type :** Il faut aussi la ruche SYSTEM. La commande classique : `reg save HKLM\SAM sam.save` et `reg save HKLM\SYSTEM system.save`. Ensuite, on utilise un outil comme `secretsdump.py` (Impacket) ou `samdump2` pour extraire les hashes.

- **Question : Pourquoi la ruche SYSTEM est-elle nécessaire avec la SAM ?**
    **Réponse type :** Parce que les hashes dans la SAM sont chiffrés avec la Boot Key (aussi appelée SysKey), qui est stockée dans la ruche SYSTEM. Sans cette clé de déchiffrement, les hashes extraits de la SAM sont illisibles. L'outil d'extraction utilise le SYSTEM pour récupérer la Boot Key, déchiffrer la SAM, et obtenir les hashes NTLM exploitables.

- **Question : Quels sont les principaux artefacts forensic Windows ?**
    **Réponse type :** Pour l'exécution : Prefetch (programmes exécutés avec dates), Amcache et ShimCache (historique avec hash SHA1), Event Logs (4688 process creation, Sysmon). Pour l'activité utilisateur : ShellBags (navigation explorateur), Jump Lists (fichiers récents par application), LNK (raccourcis avec chemins et dates). Pour la persistence : clés Run/RunOnce du registre, services, tâches planifiées. La MFT pour la timeline complète de tous les fichiers. Les outils Eric Zimmerman (MFTECmd, PECmd, AmcacheParser) sont la référence pour parser tout ça.

- **Question : Qu'est-ce que l'arbre de processus normal de Windows et comment l'utiliser pour la détection ?**
    **Réponse type :** L'arbre normal suit une chaîne précise : System → smss.exe → csrss.exe + wininit.exe → services.exe → svchost.exe. En parallèle, winlogon.exe → explorer.exe → applications utilisateur. Pour chaque processus critique, je vérifie quatre choses : le parent est-il le bon (svchost doit avoir services.exe comme parent), le chemin d'image est-il le bon (System32), le nombre d'instances est-il normal (un seul lsass.exe), et l'utilisateur est-il attendu (services.exe sous SYSTEM). Si un critère ne colle pas, c'est suspect.

- **Question : C'est quoi un LOLBin ?**
    **Réponse type :** Un LOLBin (Living-off-the-Land Binary) est un binaire légitime de Windows détourné par un attaquant — certutil pour télécharger un payload, rundll32 pour exécuter une DLL malveillante, mshta pour lancer un script distant. Le problème c'est que ces binaires sont signés Microsoft, présents partout, et passent souvent sous le radar des antivirus. La détection repose sur Sysmon et les Event Logs — on cherche des command lines suspectes sur des binaires légitimes.

---

## 7) Gouvernance / RSSI / AD

---

- **Question : Quelles sont les fonctions d'un RSSI ?**
    **Réponse type :** Le RSSI (Responsable de la Sécurité des Systèmes d'Information) pilote la stratégie de cybersécurité de l'organisation. Ses missions principales : définir et faire appliquer la politique de sécurité (PSSI), gérer les risques (cartographie, analyse, traitement), assurer la conformité réglementaire (NIS 2, RGPD, LPM), piloter la réponse à incident, gérer les budgets sécurité, sensibiliser les collaborateurs, et reporter à la direction. Il fait le lien entre la technique et le business — il doit traduire les risques techniques en impacts métier compréhensibles par le COMEX.

- **Question : Quand on arrive sur une fonction RSSI, quelles sont les premières choses qu'on demande ou qu'on fait ?**
    **Réponse type :** D'abord un état des lieux : existe-t-il une PSSI ? Un inventaire des actifs ? Une cartographie des risques ? Un PRA/PCA ? Quels sont les contrats de sécurité en place (SOC, PRIS, assurance cyber) ? Ensuite la visibilité technique : quel est le niveau de couverture EDR ? Les logs sont-ils centralisés ? L'AD est-il audité (PingCastle) ? Les sauvegardes sont-elles testées et hors réseau ? Les patchs sont-ils à jour ? Puis les quick wins : activer le MFA partout, lancer un audit AD, vérifier les accès admin, tester la restauration des sauvegardes. Enfin, construire la roadmap de maturité en priorisant par impact et faisabilité.

- **Question : Quelles sont les premières mesures à prendre pour sécuriser un Active Directory ?**
    **Réponse type :** Par impact décroissant : activer l'Advanced Audit Policy sur tous les DC (visibilité), déployer LAPS pour avoir un mot de passe admin local unique par machine (supprime le Pass-the-Hash via admin local), séparer les comptes admin et utilisateur (pas de Domain Admin sur les postes), activer le SMB signing obligatoire (bloque le NTLM relay), désactiver LLMNR et NBT-NS (bloque le poisoning Responder), rotater le krbtgt (double rotation espacée — invalide tout Golden Ticket), auditer les ACLs avec BloodHound (identifier et couper les chemins d'attaque), supprimer les comptes inactifs et SPNs inutiles (réduire la surface de Kerberoasting), activer Protected Users pour les comptes Tier 0, et durcir les templates AD CS.

- **Question : C'est quoi le tiering model AD ?**
    **Réponse type :** Le tiering sépare l'environnement en trois niveaux : Tier 0 pour les DC et comptes Domain Admin (criticité maximale, isolation réseau, PAW obligatoire), Tier 1 pour les serveurs (comptes admin serveur), Tier 2 pour les postes utilisateurs. La règle fondamentale : un compte d'un tier supérieur ne se connecte JAMAIS à un tier inférieur. Si un DA a une session sur un serveur Tier 1 et que ce serveur est compromis, l'attaquant récupère le hash DA. Le tiering casse cette chaîne.

- **Question : C'est quoi BloodHound et à quoi ça sert ?**
    **Réponse type :** BloodHound modélise l'AD comme un graphe : les objets (users, machines, groupes) sont des nœuds, les relations et droits sont des arêtes. Il collecte les données avec SharpHound et visualise les chemins d'attaque vers Domain Admin. C'est aussi un outil défensif puissant : en le lançant sur son propre AD, on identifie les chemins avant l'attaquant et on coupe les nœuds de convergence — un seul nœud corrigé peut fermer des dizaines de chemins.

---

## 8) Réponses flash — Synthèse ultra rapide

---

| Thème | Réponse flash |
|-------|---------------|
| **Moindre privilège** | Uniquement les droits nécessaires, rien de plus |
| **Défense en profondeur** | Plusieurs couches de sécurité superposées |
| **TCP vs UDP** | TCP = connexion, fiable. UDP = sans connexion, rapide |
| **DNS** | Nom → IP. Cache → récursif → racine → TLD → autoritaire. Port 53/UDP |
| **HTTPS** | HTTP + TLS. Handshake → certificat → ECDHE → clé session → AES-GCM |
| **Hash** | Empreinte fixe, irréversible, déterministe. SHA-256 sûr, MD5 cassé |
| **Sym vs Asym** | Sym = même clé, rapide (AES). Asym = paire clés, lent (RSA). Hybride = les deux |
| **Switch vs Routeur** | Switch = L2, MAC, même réseau. Routeur = L3, IP, entre réseaux |
| **ARP** | IP → MAC en local. Risque = ARP spoofing → MITM |
| **VLAN** | Segmentation logique, domaines de broadcast séparés |
| **Container vs VM** | Container = partage kernel, léger. VM = OS complet, isolation forte |
| **RAID 0/1/5/6/10** | 0=perf. 1=miroir. 5=parité(1 disque). 6=double parité. 10=miroir+stripe |
| **NAS vs SAN** | NAS = fichiers (SMB/NFS). SAN = blocs (FC/iSCSI) |
| **SIEM** | Centralise logs, corrèle, détecte, investigue |
| **IOC** | Artefact de compromission (hash, IP, domaine). Fragile, facile à changer |
| **Phases IR (NIST)** | Préparation → Détection/Analyse → Confinement/Éradication/Restauration → Post-Incident |
| **Ransomware : premières actions** | Confiner, NE PAS éteindre, protéger les backups, scoper |
| **Persistence Windows** | Run keys, services, tasks, DLL hijack, COM hijack, WMI, Winlogon |
| **Persistence Linux** | Cron, systemd, init.d, .bashrc, authorized_keys, modules kernel |
| **Mouvement latéral** | PtH, PsExec, WMI, WinRM, RDP, schtasks — avec credentials volés |
| **SAM + SYSTEM** | SAM = hashes chiffrés. SYSTEM = Boot Key pour déchiffrer |
| **Arbre processus Windows** | System → smss → csrss + wininit → services → svchost. Vérifier parent, chemin, instances, user |
| **LOLBin** | Binaire légitime détourné (certutil, rundll32). Détection = Sysmon + command line |
| **Hardening AD top 5** | Audit Policy, LAPS, séparation comptes, SMB signing, désactiver LLMNR |
| **Kerberoasting** | TGS pour SPN → crack offline. Défense = gMSA, 25+ chars, AES |
| **Forward Secrecy** | ECDHE, clés éphémères. Compromise future ≠ déchiffrement du passé |
| **IPsec vs SSL VPN** | IPsec = couche 3, accès réseau complet. SSL = couche 7, accès applicatif |
| **DNSSEC/DoH/DoT** | DNSSEC = intégrité. DoT/DoH = confidentialité. Complémentaires |
