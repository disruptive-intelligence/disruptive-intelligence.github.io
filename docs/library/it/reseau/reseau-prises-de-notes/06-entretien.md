---
title: Entretien
source: IT/04 Réseau/Réseau — prises de notes.md
note: Réseau — prises de notes
up:
- - Réseau — prises de notes
  - index.md
---

### Pourquoi plusieurs couches ?

    
> > Les couches séparent les responsabilités pour créer de l’abstraction. Chaque couche fournit un service à la couche supérieure et masque la complexité de son implémentation. Ca permet de modifier une couche sans impacter les couches supérieures.
    
> > - MAC vs IP
    
> > MAC est une adresse L2 pour la communication sur un segment local, IP est une adresse L3 pour la communication entre réseaux. MAC change à chaque saut (routeur), IP reste fixe de bout en bout (sauf NAT). MAC identifie une interfacec physique, IP identifie un hôte sur un réseau logique.
    

### Que se passe-t-il qd OS doit envoyer paquet vers une IP qui n’est pas dans son réseau local ?

> > 1. Calcul de masque : OS fait un ET logique entre l’IP destination et masque réseau pour déterminer si IP dest est dans même réseau.
<details markdown="1">
<summary>▫️ IP src</summary>

> 192.168.1.10/24 (Masque 255.255.255.0) & IP dest : 8.8.8.8

</details>

<details markdown="1">
<summary>▫️ Calcul 8.8.8.8 & 255.255.255.0 = 8.8.8.0 /=/ 192.168.1.0 → pas dans le même réseau</summary>

> > > 2. Consultation de la table de routage : 8.8.8.8 ne matche aucune route spécifique → utilise route default
> > > 3. ARP pour la passerelle 
</details>

<details markdown="1">
<summary>▫️ OS a besoin de MAC de la passerelle</summary>

</details>

<details markdown="1">
<summary>▫️ Vérifie son cache ARP</summary>

<details markdown="1">
<summary>• Si absent</summary>

> envoi ARP request en broadcast “Qui a IP?

</details>

<details markdown="1">
<summary>• Routeur répond “C’est moi, ma MAC est XXX”</summary>

</details>

<details markdown="1">
<summary>• Mise en cache dans la table ARP</summary>

> > > > 4. Encapsulation 
</details>

</details>

<details markdown="1">
<summary>▫️ Trame Ethernet ; MAC source</summary>

> le demandant & MAC dest (routeur)

</details>

<details markdown="1">
<summary>▫️ Paquet IP</summary>

> IP source : le demandant) & IP dest : hôte extérieur 8.8.8.8

> > > 5. Routeur recoit trame, désencapsule, voit IP dest, consulte sa table de routage, trouve next-hop fait ARP pour nhext-hop, réencapsule avec nouvelles MAC…. 
    
> > > L’OS calcule (IP dest & masque réseau) pour déterminer si l’IP dest est locale. Si non, il consulte sa table de routage pour trouver la passerelle par défaut. Il fait consulte sa table ARP pour obtenir la MAC de la gateway. Il encapsule paquet IP (avec IP dest finale) dans une trame Ethernet (avec MAC dest = passerelle). Routeur reçoit, désencapsule, consulte sa table de routage, et réencapsule avec de nouvelles MAC pour next hop/
    

</details>


## Commandes de diagnostic de base

### Vérifier que machine a bien reçu réponse ICMP

    
> > ```powershell
> > ping -c 4 8.8.8.8
> > arp -a 
> > ip route show / route print : voir table de routage
> > tcpdump -i eth0 -nn icmp 
> > ```
    
> > ![image.png](../../../assets/reseau-prises-de-notes-image-28.png)
    


## Cheat sheet - Ports


## Web / API / Proxy

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 80 | TCP | HTTP | Web non chiffré | Navigation web “classique” sans TLS (souvent redirigée vers 443) |
> | 443 | TCP | HTTPS (TLS) | Web chiffré | HTTP encapsulé dans TLS ; standard pour sites et API sécurisées |
> | 8080 | TCP | HTTP alt | Web/app internes | Alternative fréquente à 80 (apps internes, consoles, reverse proxy) |
> | 8443 | TCP | HTTPS alt | Web/app internes | Alternative fréquente à 443 (interfaces web d’admin, apps) |
> | 3128 | TCP | Proxy (Squid) | Proxy explicite | Proxy HTTP/HTTPS utilisé pour sortir sur Internet via une passerelle |
> | 1080 | TCP | SOCKS | Proxy SOCKS | Proxy générique (TCP), souvent pour tunnel/pivot (SOCKS4/5) |


## Accès distant / Administration

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 22 | TCP | SSH | Admin distante Linux/network | Accès shell distant sécurisé (auth par mot de passe ou clé) |
> | 23 | TCP | Telnet | Admin distante legacy | Accès distant non chiffré (ancien, rare en environnements modernes) |
> | 3389 | TCP | RDP | Bureau à distance Windows | Accès graphique à un poste/serveur Windows à distance |
> | 5985 | TCP | WinRM HTTP | Remote mgmt Windows | Administration distante Windows via WS-Management en HTTP |
> | 5986 | TCP | WinRM HTTPS | Remote mgmt Windows chiffré | Administration distante Windows via WS-Management en HTTPS |
> | 5900 | TCP | VNC | Prise en main distante | Contrôle d’écran distant multi-OS (souvent utilisé sur postes/serveurs) |
> | 69 | UDP | TFTP | Transfert simple (network) | Transfert de fichiers minimaliste (souvent pour équipements réseau/boot) |


## Partage de fichiers / Impression

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 445 | TCP | SMB | Partages + auth Windows | Accès aux partages Windows, échanges fichiers, impression, auth intégrée |
> | 139 | TCP | NetBIOS Session | SMB legacy | Ancienne couche de session pour SMB (environnements legacy) |
> | 2049 | TCP/UDP | NFS | Partages Unix/Linux | Partage de fichiers côté Unix/Linux (montages NFS) |
> | 631 | TCP | IPP | Impression | Impression via IPP (protocole moderne d’impression réseau) |
> | 515 | TCP | LPD/LPR | Impression legacy | Impression “ancienne génération” (souvent présent sur parcs historiques) |


## Résolution / Adressage / Temps

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 53 | UDP/TCP | DNS | Résolution de noms | Résolution noms↔IP (UDP majoritaire ; TCP pour certains cas) |
> | 67/68 | UDP | DHCP | Attribution IP | Attribution d’IP et paramètres réseau (67 serveur, 68 client) |
> | 123 | UDP | NTP | Synchronisation temps | Mise à l’heure des systèmes (essentiel pour logs et authentification) |


## Email (à associer à ton cours SMTP/POP/IMAP)

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 25 | TCP | SMTP | Serveur↔serveur (relay) | Transport SMTP entre serveurs mail (MTA à MTA) |
> | 587 | TCP | Submission | Client → serveur mail | Envoi depuis client vers serveur (souvent avec auth, standard moderne) |
> | 465 | TCP | SMTPS | SMTP sur TLS (implicite) | Variante SMTP avec TLS implicite (très utilisée en pratique) |
> | 110 | TCP | POP3 | Réception legacy | Récupération des mails côté client (historique) |
> | 995 | TCP | POP3S | POP3 sur TLS | POP3 chiffré via TLS |
> | 143 | TCP | IMAP | Réception | Accès aux mails en restant synchronisé avec le serveur |
> | 993 | TCP | IMAPS | IMAP sur TLS | IMAP chiffré via TLS |


## Supervision / Logs

> | Port | Proto | Service | À quoi ça sert | Description (mini) |
> | --- | --- | --- | --- | --- |
> | 161/162 | UDP | SNMP | Supervision / traps | Supervision équipements (161 requêtes ; 162 traps/alertes) |
> | 514 | UDP | Syslog | Logs réseau | Envoi de logs (souvent équipements réseau/sécurité) en UDP |
> | 6514 | TCP | Syslog TLS | Syslog chiffré | Syslog au-dessus de TLS (version sécurisée/fiable) |
