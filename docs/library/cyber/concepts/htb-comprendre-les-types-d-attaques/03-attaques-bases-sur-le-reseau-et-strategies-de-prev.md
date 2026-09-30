---
title: Attaques basés sur le réseau et stratégies de prévention
source: Cyber/99_Concepts/HTB_Comprendre les types d'attaques.md
note: HTB — Comprendre les types d'attaques
up:
- - HTB — Comprendre les types d'attaques
  - index.md
---

## Attaques de la couche 2
### ARP Poisoning

- ARP associe une adresse IP <-> MAC sur un LAN.
- ARP Poisoning / ARP Spoofing : envoyer de fausses réponses ARP pour modifier le cache ARP d'une victime.
- L'attaquant associe sa propre MAC à l'IP d'un équipement légitime, souvent la gateway.
- Victime pense : 192.168.1.1 (Gateway) → MAC Attaquant → Le trafic peut alors passer par l’attaquant : **MITM**, sniffing, modification/redirection du trafic.
### MAC Flooding

- Un switch maintient une CAM/MAC table pour associer : MAC Address -> Switch port
- L'attaquant envoie énormément de trames avec de fausses MAC pour saturer cette table.
- Sur certains équipements/comportements, le switch peut alors flooder les frames inconnues sur plusieurs ports, facilitant le sniffing.
### MAC Cloning / MAC Spoofing

- Modifier sa MAC pour imiter un autre équipement.
- Peut contourner des contrôles faibles basés uniquement sur la MAC :
	- MAC filtering Wi-FI ;
	- port security mal configurée ;
	- restrictions d'accès simples.

## Attaques DNS
### DNS Poisoning

- Manipuler des données DNS pour faire résoudre un domaine légitime vers une IP contrôlée par l'attaquant.
- bank.com -> DNS compromis -> 10.0.10.50 (attaquant) : → permet phishing, interception ou distribution de malware.
### DNS Cache Poisoning

- Corrompre le cache DNS d'un resolver/client afin qu'il conserve une fausse résolution.
- Même si le DNS autoritaire est sain, le client peut continuer à recevoir la mauvaise IP tant que l'entrée empoisonnée reste en cache.
### Pharming

- Redirection silencieuse vers un faux site en manipulant :
	- DNS ;
	- cache DNS ;
	- fichier local **host**
- → le système utilisera cette résolution locale sans interroger le DNS normalement.
### Domain Hijacking

- Prendre le contrôle d'un domaine sans autorisation du propriétaire.
- Peut passer par : 
	- Compromission du compte registrar ;
	- social engineering ;
	- vol de credentials ;
	- mauvaise conf.
- Attaquant peut modifier DNS, mail, site Web...
### URL Redirection

- Faire rediriger un user d'une URL légitime vers une destination malveillante.
- Peut être réalisée via :
	- DNS compromis ;
	- site Web compromis ;
	- redirection HTTP ;
	- configuration applicative malveillante.
### Domain Reputation

- éputation associée à l'historique d'un domaine basé sur : spam, phishing, malware, ancienneté, comportement email...
- Un domaine ayant une mauvaise réputation peut être placé sur des **blocklists**, et ses emails seront filtrés.
- Maintenir une bonne réputation de domaine est important pour assurer la délivrabilité des e-mails et prévenir les problèmes de sécurité liés au spam.

## Pass-the-Hash (PtH)

- Technique principalement liée à l'authentification NTLM sous Windows.
- L'attaquant récupère un hash NTLM puis l'utilise directement pour s'authentifier sans connaître le MDP en clair.
- Les hashes peuvent provenir de différentes sources : SAM, mémoire, dumps de credentials, etc.
- Kerberos réduit certains usages de NTLM mais ne “supprime” pas automatiquement le risque PtH.
- La vraie défense passe aussi par limitation NTLM, segmentation, Credential Guard, comptes admins séparés, LAPS/Windows LAPS, etc.
## Amplification

- Augmenter puissance/gain d'une carte ou antenne Wi-Fi permet d'atteindre un réseau plus loin.
- Un attaquant peut donc tenter de se connecter sans être physiquement proche du bâtiment.
- C’est davantage une **capacité radio/physique** qu’une attaque réseau à elle seule.
- Défense possible :
	- ajuster correctement la puissance des AP ;
	- placer les AP intelligemment ;
	- utiliser WPA2/WPA3 + authentification forte.
## Spam

- Envoi massif de messages non sollicités.
- Peut servir à :
	- pub ;
	- phishing ;
	- diffusion de malware ;
	- escroquerie.
- Défense :
	- antispam ;
	- réputation domaine/IP ;
	- filtrage URL/PJ.
## Privilege Escalation

- Passer d'un niveau de privilège faible vers un niveau supérieur. User → Administrator → SYSTEM
- Peut exploiter :
	- vulnérabilité OS/software ;
	- permissions faibles ;
	- service mal configuré ;
	- credentials privilégiés.
- Prévention : patching, least privilege, hardening, contrôle des permissions.
## Port Scanning

- Permet d'identifier les ports ouverts et donc les services potentiellement attaquables.
- Différents types de scans de ports incluent :
	- Scan de connexion TCP : Initie une poignée de main TCP complète avec chaque port pour déterminer s'il est ouvert.
	- SYN scan / Half-Open : Envoie un SYN sans terminer la poignée de main, réduisant la détectabilité en générant moins de trafic.
	- XMAS scan : Envoie paquets avec des flags spécifiques (PSH, URG, FIN), pour sonder les ports.
## Antiquated / Insecure Protocols

- Protocoles historiques conçus sans chiffrement ou protections modernes.
- Ex : 
	- HTTP  → HTTPS
	- FTP   → SFTP / FTPS
	- POP3  → POP3S / TLS
	- SMTP  → SMTP avec TLS / STARTTLS
	- Telnet → SSH
- Nuance : HTTP, FTP, SMTP ou POP3 existent toujours ; ce sont surtout leurs **utilisations non chiffrées** qui posent problème.
## Session Hijacking

- Vol ou réutilisation d'une session déjà authentifiée afin d'usurper l'utilisateur.
- Exemple web : Victime login -> Session Cookie -> Cookie volé -> Attaquant réutilise la session
## CLient-Side Attack

- Exploitent une vulnérabilité présente dans une application utilisée par la victime.
- Ex : navigateur, client mail, lecteur PDF, application de messagerie, Office.
## Watering Hole Attack

- Compromettre un site web fréquemment visité par la population ciblée.
- Le site légitime devient le vecteur de compromission.
- Attaquant -> Site utilisé par la cible compromis -> victimes visitent naturellement le site -> code/payload malveillant.
## Typosquatting / URL Hijacking

- Enregistrer des domaines ressemblant à un domaine légitime en anticipant les fautes de frappe.
- Ex : 
	- google.com
	- gogle.com
	- gooogle.com
- Peut servir à :
	- phishing ;
	- malware ;
	- pub ;
	- credential harvesting.

## Prévention
### Sécurité physique

- Empêcher qu’un individu non autorisé puisse connecter directement un équipement au réseau.
- Contrôle d’accès, visiteurs, salles réseau sécurisées.
### Switch Hardening

- Désactiver les ports inutilisés.
- Utiliser **Port Security** pour limiter les MAC autorisées par port.
- Autres protections pertinentes selon infrastructure :
    - DHCP Snooping ;
    - Dynamic ARP Inspection (DAI) ;
    - VLAN segmentation ;
    - 802.1X / NAC.
### DNS

- protéger les comptes registrar ;
- MFA ;
- surveiller les changements DNS ;
- DNSSEC lorsqu’applicable ;
- sécuriser les resolvers.
### Network Monitoring

- IDS/IPS ;
- firewall ;
- SIEM ;
- NetFlow ;
- détection scans / anomalies ;
- segmentation réseau.
