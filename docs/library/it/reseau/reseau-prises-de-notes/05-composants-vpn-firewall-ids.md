---
title: Composants [VPN, Firewall, IDS…]
source: IT/04 Réseau/Réseau — prises de notes.md
note: Réseau — prises de notes
up:
- - Réseau — prises de notes
  - index.md
---

### VPN & SSL/TLS IPsec

<details markdown="1">
<summary>🔸 Couche Présentation et Session</summary>

<details markdown="1">
<summary>▫️ SSL/TLS</summary>

<details markdown="1">
<summary>• Protocoles pour chiffrer les données échangées entre un client et un serveur. SSL historique, TLS l’a remplacé.</summary>

</details>

<details markdown="1">
<summary>• Fonctionnement, handshake TLS ;</summary>

> > > > > 1. Client Hello message : Client envoie un message ClientHello au serveur, contenant version TLS, liste des cypher crypto supportés, nombre aléatoire (client random)
> > > > > 2. Server Hello message : Serveur envoie un message ServerHello, indique suite crypto choisie, son propre nombre aléatoire (server random), certificat numérique (X.509, qui contient clé publique
> > > > > 3. Authentification du serveur : Le client vérifie que le certificat présenté par le serveur est valide. Signé àar CA de confiance, correspond au domaine, n’est pas expiré ni révoqué.
> > > > > 4. Echange de secret (clé de pré-maître) : Client génère premaster secret (valeur aléatoire). Il chiffre ce premaster secret avec clé publique du serveur (extraite de son certificat), serveur peut alors déchiffrer grâce à sa clé privée. 
> > > > > 5. Génération de la clé de session : Client et serveur combinent le client random, server random et le presmaster secret. Grâce à une dérivation, obtiennent même clé de session symétrique. Clé jamais transmisse, calculée indépendamment des deux côtés.
> > > > > 6. Message “Finished” : Client et serveur s’envoient un message de confirmation, chiffré avec la clé de session. 
                
> > > > > >
                
> > > > > - Négociation des paramètres (version, chiffrements)
> > > > > - Authentification (certificat serveur)
> > > > > - Échange de secret (RSA ou Diffie-Hellman)
> > > > > - Génération d’une clé de session partagée
> > > > > - Communication chiffrée avec cette clé
</details>

</details>

</details>

<details markdown="1">
<summary>🔸 Couche réseau</summary>

<details markdown="1">
<summary>▫️ IPsec</summary>

<details markdown="1">
<summary>• Internet Protocol Security, utilise les protocoles suivants</summary>

> > > > > - Authentification Header (AH) : Fournit l’authentification et l’intégrité, ne protège pas la confidentialité.
> > > > > - Deux modes de fonctionnement :
> > > > > - Transport mode : Fournit l’authentification pour les TCP/UDP header et data
> > > > > - Tunnel mode : Fournit l’authentification pour les IP header, TCP/UDP header et data
> > > > > - Encapsulating Security Payload (ESP) : Assure le chiffrement, et fournit l’authentification, l’intégrité et la confidentialité
> > > > > - Deux modes de fonctionnement :
> > > > > - Transport mode : Assure la sécurité (confidentialité et intégrité) des TCP/UDP header et data
> > > > > - Tunnel mode : Assure la sécurité  (confidentialité et intégrité) pour les IP header et TCP/UDP header et data
> > > > > - Security Association (SA) : Responsable de la négociation les clés de chiffrement et les algo. Par exemple IKE.
> > > > > - VPN :
> > > > > - Permet de créer un tunnel sécurisé entre deux réseaux.
> > > > > - **VPN IPsec** : **IPsec (Internet Protocol Security)** fonctionne **au niveau 3 (couche réseau - IP)**. Il protège directement les paquets IP.
> > > > > - Fonctionnement, deux modes :
> > > > > - *Transport* → chiffre uniquement la **charge utile** (payload) du paquet IP, pas l’en-tête.
> > > > > - *Tunnel* → chiffre le **paquet entier** (en-tête + données), puis l’encapsule dans un nouveau paquet IP → idéal pour VPN.
> > > > > - **Protocoles de sécurité** :
> > > > > - **AH (Authentication Header)** : garantit l’intégrité et l’authenticité, mais pas la confidentialité.
> > > > > - **ESP (Encapsulating Security Payload)** : chiffre les données + garantit l’intégrité et l’authenticité (c’est le plus utilisé).
> > > > > - **Établissement de connexion** :
> > > > > - Utilise **IKE (Internet Key Exchange)**, souvent IKEv2.
> > > > > - IKE négocie les algorithmes de chiffrement (AES, ChaCha20…), les clés (via Diffie-Hellman), et gère la création des **SA (Security Associations)**
> > > > > - **VPN SSL/TLS** ; **SSL/TLS VPN** fonctionne **au niveau 5-7 (couche session/application)**. Il repose sur le protocole **TLS**, le même que pour HTTPS.
> > > > > - Fonctionnement :
> > > > > - Le client (souvent via un navigateur ou un agent dédié) se connecte au **serveur VPN** en HTTPS.
> > > > > - Une session TLS est établie (handshake TLS).
> > > > > - Le trafic applicatif (HTTP, RDP, SSH, etc.) est transporté à travers ce tunnel chiffré.
> > > > > - Deux modes principaux :
> > > > > - *SSL Portal VPN* → accès via un portail web sécurisé (ex. applications internes accessibles depuis le navigateur).
> > > > > - *SSL Tunnel VPN* → client logiciel qui encapsule d’autres protocoles (ex. RDP, SMB) dans TLS.
> > > > > - Différences principales
            
> > > > > | Critère | VPN IPsec | VPN SSL/TLS |
> > > > > | --- | --- | --- |
> > > > > | **Couche OSI** | Réseau (couche 3 - IP) | Application/Session (couche 5-7) |
> > > > > | **Type de trafic** | Tout le trafic IP | Généralement applicatif (HTTP, RDP, etc.) |
> > > > > | **Complexité** | Plus complexe à configurer | Plus simple (HTTPS) |
> > > > > | **Pare-feux/NAT** | Difficile à traverser | Passe facilement (443/TCP) |
> > > > > | **Usage typique** | Site-to-site, interconnexion réseaux | Accès distant utilisateur |
</details>

<details markdown="1">
<summary>• Cas d’usage concrets</summary>

> > > > > - **IPsec VPN** :
> > > > > - Connexion **site-to-site** entre deux réseaux d’entreprise. Connexion sécurisée de filiales vers le siège. VPN **client-to-site** pour employés fixes.
> > > > > - **SSL/TLS VPN** :
> > > > > - Accès distant des utilisateurs nomades. Télétravail avec accès au portail applicatif interne. Solution privilégiée quand les utilisateurs passent par des réseaux inconnus (Wi-Fi public, hôtel, etc.).
    
> > > > > - VPN en détails
    
> > > > > [Cours_VPN_Complet](https://www.notion.so/Cours_VPN_Complet-3033297e159780378dbeffe5434f9bde?pvs=21) 
    
> > > > > - Entretien
> > > > > - **Question 1 : « Différence entre VPN IPsec et VPN SSL/TLS ? »**
        
> > > > > IPsec opère au niveau IP (couche 3) : il chiffre les paquets IP directement via ESP, négocie via IKE sur UDP/500, et nécessite plusieurs protocoles/ports distincts (UDP/500, ESP proto 50, UDP/4500 pour le NAT-T). C'est le standard en site-to-site grâce à son interopérabilité multi-constructeurs et son accélération matérielle.
        
> > > > > TLS/SSL opère au-dessus de TCP (couche 4+) : il encapsule le trafic dans une session TLS sur TCP/443, le même port que HTTPS. Ça le rend quasi impossible à bloquer par un firewall. C'est souvent privilégié pour le remote-access parce que c'est plus simple à déployer et ça passe partout.
        
> > > > > En résumé : IPsec = couche IP, multi-protocoles, standard inter-constructeurs, idéal site-to-site. TLS = couche transport, un seul flux sur 443, passe partout, idéal remote-access.
        
> > > > > ---
        
> > > > > - **Question 2 : « Comment fonctionne un VPN IPsec ? »**
        
> > > > > L'établissement passe par IKE en deux phases. En Phase 1 (UDP/500), les deux pairs négocient les algorithmes, font un échange Diffie-Hellman pour générer un secret partagé, et s'authentifient mutuellement (PSK ou certificats). Ça crée un canal sécurisé (IKE SA). En Phase 2, à l'intérieur de ce canal, ils négocient les paramètres du tunnel de données : quels sous-réseaux protéger, quels algorithmes pour ESP, durée de vie des clés. Si un NAT est détecté, tout bascule sur UDP/4500 (NAT-T). Une fois le tunnel actif, ESP chiffre le paquet IP original en entier (mode tunnel), l'encapsule dans un nouveau paquet IP avec les adresses publiques, et l'autre extrémité déchiffre et route en interne.
        
> > > > > ---
        
> > > > > - **Question 3 : « Comment fonctionne un VPN SSL/TLS ? »**
        
> > > > > Le client se connecte à la passerelle sur TCP/443. Un handshake TLS standard a lieu : négociation des algorithmes, vérification du certificat serveur, échange Diffie-Hellman pour les clés de session. Une fois le canal TLS établi, l'utilisateur s'authentifie à l'intérieur (login + MFA). La passerelle attribue alors une IP interne au client, crée une interface virtuelle (tun0), et pousse les routes (split ou full tunnel). Le trafic vers le réseau interne est ensuite capté par l'interface virtuelle, chiffré dans la session TLS, et envoyé comme données dans le flux TCP/443. La passerelle déchiffre et route en interne. Pour la performance, beaucoup d'implémentations utilisent DTLS (TLS sur UDP) afin d'éviter le problème du TCP-over-TCP.
        
> > > > > - **Question 1 : « Quelle est la différence entre un VPN IPsec et un VPN SSL/TLS ? »**
        
> > > > > La différence fondamentale, c'est le **niveau auquel ils opèrent dans la pile réseau**.
        
> > > > > Un VPN IPsec travaille au **niveau IP, couche 3**. Il protège directement les paquets IP eux-mêmes : le paquet IP original est chiffré par ESP, puis encapsulé dans un nouveau paquet IP avec les adresses publiques des deux extrémités. La négociation se fait via IKE sur UDP/500, le trafic chiffré transite via ESP (protocole IP 50), et si un NAT est détecté, tout bascule sur UDP/4500 via NAT-T. Ça implique donc plusieurs protocoles et ports distincts sur le réseau.
        
> > > > > Un VPN SSL/TLS travaille **au-dessus de TCP ou UDP, couche 4+**. Il encapsule le trafic IP du client dans une session TLS, typiquement sur TCP/443 — le même port que HTTPS. Pour le réseau, ça ressemble à du trafic web normal. La négociation se fait via le handshake TLS standard, et tout passe dans un seul flux.
        
> > > > > En termes de conséquences pratiques, ça donne trois grandes différences :
        
> > > > > Premièrement, la **traversée réseau** : le TLS VPN passe quasi partout parce que le port 443 est rarement bloqué. IPsec peut poser problème dans des environnements restrictifs — les firewalls d'hôtels ou de hotspots ne laissent pas toujours passer ESP ou UDP/500.
        
> > > > > Deuxièmement, l'**interopérabilité** : IPsec est un standard RFC, donc un équipement Cisco peut monter un tunnel avec un Fortinet sans problème. C'est pour ça qu'IPsec est le choix quasi systématique en site-to-site. Les VPN TLS sont plus liés à un produit — un client OpenVPN ne se connectera pas à un serveur AnyConnect.
        
> > > > > Troisièmement, la **performance** : IPsec bénéficie souvent d'accélération matérielle dans les firewalls et n'a pas le problème du TCP-over-TCP. En TLS pur sur TCP, si un paquet est perdu, les deux couches TCP retransmettent indépendamment, ce qui peut dégrader les performances. DTLS sur UDP résout ce point.
        
> > > > > En résumé : IPsec est plus adapté au site-to-site et aux environnements contrôlés, TLS/SSL est souvent préféré pour le remote-access parce qu'il passe partout et qu'il est plus simple à déployer côté utilisateur.
        
> > > > > ---
        
> > > > > - **Question 2 : « Comment fonctionne un VPN IPsec ? »**
        
> > > > > Un VPN IPsec repose sur trois briques principales : **IKE** pour la négociation, **ESP** pour le chiffrement du trafic, et **NAT-T** si un NAT est présent.
        
> > > > > L'établissement du tunnel se fait en deux phases via IKE.
        
> > > > > **En Phase 1**, les deux extrémités — que ce soient deux passerelles en site-to-site ou un client et une passerelle en remote-access — négocient les paramètres de sécurité : algorithmes de chiffrement, algorithmes d'intégrité, groupe Diffie-Hellman. Elles font un échange Diffie-Hellman pour générer un secret partagé sans jamais l'envoyer sur le réseau, puis s'authentifient mutuellement, soit par clé pré-partagée (PSK), soit par certificats. Le résultat de cette phase, c'est un canal sécurisé appelé IKE SA, qui sert uniquement à protéger la suite de la négociation. Tout ça se passe sur UDP/500.
        
> > > > > **En Phase 2**, à l'intérieur de ce canal sécurisé, elles négocient les paramètres du tunnel de données : quels sous-réseaux protéger (les traffic selectors), quel algorithme pour ESP, la durée de vie des clés, et éventuellement un nouvel échange Diffie-Hellman pour du Perfect Forward Secrecy. Le résultat, c'est une paire d'IPsec SA — une par direction — avec des clés de session dédiées.
        
> > > > > Pendant la Phase 1, les pairs détectent aussi automatiquement s'il y a un NAT entre eux. Si c'est le cas, ils basculent sur **UDP/4500** et encapsulent les paquets ESP dans de l'UDP, parce qu'ESP est un protocole IP (numéro 50), pas du TCP ou UDP — le NAT ne sait pas le router nativement.
        
> > > > > Une fois le tunnel actif, le **transport des données** fonctionne comme suit : quand un paquet IP doit traverser le tunnel, la passerelle le chiffre intégralement via ESP en mode tunnel — l'en-tête IP original et le payload sont chiffrés — puis l'encapsule dans un nouveau paquet IP avec les adresses publiques des passerelles. L'autre extrémité déchiffre, extrait le paquet original, et le route sur son réseau interne.
        
> > > > > Le tunnel est ensuite maintenu par du **rekeying** automatique quand les clés expirent, et du **Dead Peer Detection** pour détecter si l'autre extrémité tombe.
        
> > > > > ---
        
> > > > > - **Question 3 : « Comment fonctionne un VPN SSL/TLS ? »**
        
> > > > > Un VPN SSL/TLS crée un tunnel chiffré en utilisant le protocole TLS — le même que HTTPS — typiquement sur TCP/443.
        
> > > > > L'établissement commence par un **handshake TLS** classique. Le client contacte la passerelle VPN sur le port 443. Ils négocient la version TLS et la cipher suite, la passerelle présente son certificat serveur que le client vérifie (signature, CA, validité, nom), et éventuellement le client présente aussi un certificat client si l'entreprise l'exige. Ensuite, un échange Diffie-Hellman (ECDHE en TLS 1.3) permet de dériver les clés de session. À la fin du handshake, un canal TLS chiffré est établi — indiscernable d'une connexion HTTPS pour un observateur sur le réseau.
        
> > > > > Ensuite vient l'**authentification utilisateur**, qui se fait à l'intérieur du tunnel TLS déjà chiffré : login/mot de passe vérifié contre un annuaire AD ou LDAP, puis MFA si configuré, et éventuellement un contrôle de posture du poste.
        
> > > > > Une fois authentifié, la passerelle **configure le tunnel** : elle attribue au client une IP interne depuis un pool, le client crée une interface réseau virtuelle (tun0 ou équivalent), et la passerelle pousse les routes (split tunnel ou full tunnel) ainsi que les DNS internes.
        
> > > > > Le **transport** fonctionne ensuite ainsi : quand le poste génère un paquet IP à destination du réseau interne, ce paquet est capté par l'interface virtuelle, chiffré via TLS, et envoyé comme données à l'intérieur de la session TCP/443 existante vers la passerelle. La passerelle déchiffre, extrait le paquet IP, et le route en interne. Le retour suit le chemin inverse.
        
> > > > > Un point technique important : en mode TCP pur, on a du **TCP-over-TCP** — le trafic applicatif (souvent TCP) est encapsulé dans une session TLS elle-même sur TCP. Si un paquet est perdu, les deux couches TCP retransmettent indépendamment, ce qui peut dégrader les performances. C'est pour ça que beaucoup d'implémentations utilisent **DTLS** (TLS sur UDP) quand c'est possible, avec un fallback sur TCP si UDP est bloqué.
        
> > > > > Il existe aussi un **mode clientless** ou portail web, où il n'y a pas de tunnel réseau : l'utilisateur accède aux applications internes via un portail HTTPS, et c'est la passerelle qui fait le reverse proxy. C'est plus limité — pas d'accès réseau complet — mais ça ne nécessite aucune installation sur le poste.
        
</details>

</details>

</details>

<details markdown="1">
<summary>🔸 Concrètement Remote access / Site to site (EASY BG)</summary>

        
> > > **Remote-access** : c’est l’utilisateur individuel qui se connecte. Soit il lance manuellement son client VPN (GlobalProtect, AnyConnect, FortiClient…), soit le client est configuré pour se lancer automatiquement dès que le poste détecte qu’il est hors du réseau d’entreprise (c’est ce qu’on appelle l’always-on VPN). Dans les deux cas, c’est un tunnel entre son poste et la passerelle de l’entreprise. L’utilisateur est conscient qu’il y a un VPN (il voit l’icône, il s’authentifie).
> > > **Site-to-site** : l’utilisateur ne sait même pas que ça existe. C’est configuré une fois entre les deux routeurs/firewalls des deux sites, et ça tourne en permanence. Un employé à Paris qui accède à un serveur à Marseille, pour lui c’est juste une IP interne qui répond. Il ne lance rien, il ne s’authentifie à rien côté VPN — c’est l’infrastructure qui gère. Son poste envoie un paquet vers 10.2.0.x, le firewall de Paris détecte que c’est pour le réseau de Marseille, il chiffre et envoie au firewall de Marseille via le tunnel, et c’est transparent.
> > > La distinction simple à retenir : remote-access = le tunnel part du poste de l’utilisateur. Site-to-site = le tunnel part du firewall/routeur, les utilisateurs sont juste derrière sans le savoir.
        
</details>

<details markdown="1">
<summary>🔸 Concrètement VPN grand public</summary>

        
> > > C’est exactement ça.
> > > Techniquement c’est du remote-access classique : ton poste (client) → serveur du fournisseur (passerelle). Sauf qu’au lieu de te donner accès à un réseau privé interne, la passerelle te sert de point de sortie vers Internet. Ton trafic entre dans le tunnel chiffré jusqu’au serveur du fournisseur, et c’est ce serveur qui fait la requête vers le site web à ta place. Le site voit l’IP du serveur (à Amsterdam, Tokyo, New York… selon ce que tu choisis), pas la tienne.
> > > Le fournisseur (NordVPN, ProtonVPN, Mullvad…) gère une infrastructure de serveurs répartis dans des dizaines de pays. Chaque serveur a ses propres IP publiques. Quand tu choisis “se connecter au Japon”, ton client VPN établit un tunnel remote-access vers un serveur au Japon, et tout ton trafic Internet sort avec une IP japonaise.
> > > Le point important à garder en tête : tu ne deviens pas invisible. Tu déplaces juste la confiance. Sans VPN, ton FAI voit vers où tu te connectes. Avec un VPN grand public, c’est le fournisseur VPN qui voit ce trafic à la place. Les politiques “no-log” sont un engagement contractuel, pas une garantie technique — tu n’as aucun moyen de vérifier ce qui tourne sur leurs serveurs.
        
</details>

<details markdown="1">
<summary>🔸 Quand choisir IPsec ? Quand choisir SSL/TLS ?</summary>

        
> > > **choisis IPsec quand :**
        
> > > Tu fais du **site-to-site**. Tu relies deux sites (Paris ↔ Marseille), les deux firewalls se parlent, c'est permanent, c'est configuré une fois. IPsec est le standard ici parce que tous les constructeurs le supportent (un FortiGate parle IPsec avec un Cisco sans problème), il y a souvent de l'accélération matérielle dans les firewalls donc c'est très performant, et en mode tunnel il est conçu exactement pour transporter des sous-réseaux entiers. Tu n'as pas de contrainte de traversée de firewall restrictif puisque les deux extrémités sont des infras que tu contrôles — tu ouvres les ports nécessaires (UDP/500, ESP, UDP/4500) et c'est réglé.
        
> > > Tu peux aussi choisir IPsec en remote-access (IKEv2) quand tes utilisateurs sont sur **mobile** (IKEv2 gère très bien les changements de réseau Wi-Fi ↔ 4G sans couper la session) ou quand tu maîtrises l'environnement réseau de tes utilisateurs (postes d'entreprise, réseaux contrôlés) et que tu n'as pas de problème de ports bloqués.
        
> > > **Tu choisis TLS/SSL quand :**
        
> > > Tu fais du **remote-access** et tes utilisateurs se connectent depuis **des réseaux que tu ne contrôles pas** : hôtels, Wi-Fi publics, réseaux clients, pays avec du filtrage… TCP/443 passe partout. Un firewall d'hôtel qui bloque UDP/500 ou ESP ne bloquera jamais le port 443 — sinon plus personne ne pourrait naviguer sur le web. C'est l'argument massue du TLS VPN en remote-access.
        
> > > Tu choisis aussi TLS/SSL quand tu veux de la **flexibilité d'accès** : tu peux proposer un mode clientless (portail web) pour des prestataires ou des postes non gérés qui n'ont pas le droit d'installer un client VPN, et un mode tunnel complet pour tes employés avec le client installé. Avec IPsec, tu n'as pas cette option portail web.
        
> > > Et tu le choisis quand tu veux une **authentification en couches** plus granulaire : le certificat TLS authentifie la machine pendant le handshake, puis le login + MFA authentifie l'utilisateur après. Ça permet de refuser un poste non certifié avant même qu'il puisse tenter un login.
        
> > > **En résumé, la logique décisionnelle :**
        
> > > Site-to-site → IPsec, quasi systématiquement. Remote-access depuis des réseaux maîtrisés → IPsec (IKEv2) fonctionne très bien. Remote-access depuis n'importe où / réseaux non maîtrisés → TLS/SSL, parce que ça passe partout. Besoin d'un accès sans client (portail web) → TLS/SSL, c'est la seule option. Et dans la réalité, beaucoup d'entreprises **déploient les deux** : IPsec pour le site-to-site entre leurs sites, et TLS/SSL pour le remote-access de leurs employés.
        
<details markdown="1">
<summary>▫️ Clientless / portail web</summary>

            
> > > > Imagine qu'un prestataire externe (un auditeur, un consultant, un développeur freelance) doit accéder à une application interne de ton entreprise — disons un outil de ticketing hébergé en interne sur `http://tickets.interne.local`. Ce prestataire utilise **son propre PC**. Tu ne gères pas ce PC, tu n'as pas le droit d'installer un logiciel dessus, et tu ne veux pas non plus donner un accès réseau complet à quelqu'un d'externe.
            
> > > > Avec un VPN TLS en mode clientless, tu lui donnes juste une URL : `https://vpn.entreprise.com`. Il ouvre son navigateur, va sur cette URL, tombe sur une page de login, s'authentifie (login + MFA). Une fois connecté, il voit un **portail web** qui liste les applications auxquelles il a droit — dans son cas, juste le ticketing. Il clique dessus, et la passerelle VPN joue le rôle de **reverse proxy** : le navigateur du prestataire communique en HTTPS avec la passerelle, et la passerelle va chercher les pages de `tickets.interne.local` en interne et les lui renvoie.
            
> > > > Le prestataire n'a **rien installé**, n'a **pas d'IP interne**, n'a **pas d'accès réseau**. Il ne peut pas faire de ping, de SSH, de scan réseau. Il voit uniquement l'application qu'on lui a autorisée, à travers son navigateur. Si demain tu lui retires l'accès, tu désactives son compte et c'est fini.
            
> > > > À côté de ça, ton employé avec un poste géré par l'entreprise a **le client VPN installé** (AnyConnect, GlobalProtect…), un certificat machine, un tunnel complet avec une IP interne et des routes → il a un accès réseau réel vers tout ce que sa politique autorise.
            
> > > > C'est cette **dualité** (portail web sans rien installer pour les externes, tunnel complet avec client pour les internes) qui est un avantage propre au TLS/SSL VPN. IPsec ne peut pas faire ça — il n'a pas de mode "navigateur uniquement".
            
</details>

</details>

<details markdown="1">
<summary>🔸 Fonctionnement étapes par étapes (IPsec & SSL/TLS)</summary>

        
<details markdown="1">
<summary>▫️ 1 Comment fonctionne une connexion VPN IPsec — étape par étape</summary>

        
> > > > Prenons un cas concret : un tunnel IPsec site-to-site entre le siège (passerelle A, IP publique 203.0.113.1, réseau interne 10.1.0.0/24) et une agence (passerelle B, IP publique 198.51.100.1, réseau interne 10.2.0.0/24). Le déroulé est quasiment identique pour du remote-access IPsec (IKEv2), sauf que côté client c’est un logiciel sur un PC au lieu d’un routeur.
        
</details>

<details markdown="1">
<summary>▫️ Étape 1 — Déclenchement</summary>

        
> > > > Le tunnel peut être déclenché de deux manières :
> > > > - **À la demande** : un paquet arrive sur passerelle A à destination de 10.2.0.0/24. La passerelle détecte qu’il correspond à une politique IPsec (une règle qui dit “le trafic 10.1.0.0/24 → 10.2.0.0/24 doit être protégé par IPsec”). Elle lance la négociation IKE.
> > > > - **En permanence** : la passerelle est configurée pour établir et maintenir le tunnel dès le démarrage (keep-alive).
        
</details>

<details markdown="1">
<summary>▫️ Étape 2 — IKE Phase 1 (établir un canal sécurisé pour négocier)</summary>

        
> > > > Le but de cette phase est que A et B se mettent d’accord sur **comment ils vont communiquer de manière sécurisée** pour la suite de la négociation. C’est la négociation de la négociation.
        
> > > > 1. **Passerelle A envoie une proposition** à passerelle B sur **UDP/500**. Cette proposition contient : les algorithmes de chiffrement supportés (ex : AES-256), les algorithmes d’intégrité (ex : SHA-256), le groupe Diffie-Hellman à utiliser (ex : groupe 14 = 2048 bits), la durée de vie souhaitée pour cette SA (Security Association).
> > > > 2. **Passerelle B répond** en sélectionnant les paramètres qui lui conviennent parmi ceux proposés. Si rien ne correspond (pas d’algorithme commun), la négociation échoue.
> > > > 3. **Échange Diffie-Hellman** : les deux parties échangent des valeurs publiques qui leur permettent de calculer indépendamment un **secret partagé** (la clé maîtresse), sans jamais l’envoyer sur le réseau. Un attaquant qui intercepte l’échange DH ne peut pas recalculer ce secret (c’est la propriété mathématique de Diffie-Hellman).
> > > > 4. **Authentification mutuelle** : chaque passerelle prouve son identité à l’autre. Deux méthodes principales :
> > > > - **PSK (Pre-Shared Key)** : les deux passerelles connaissent un mot de passe secret configuré à l’avance des deux côtés. Elles prouvent qu’elles le connaissent via un hash (sans l’envoyer en clair).
> > > > - **Certificats** : chaque passerelle présente un certificat X.509 signé par une autorité de certification (CA) que l’autre reconnaît. Plus sécurisé que PSK, mais nécessite une PKI.
        
> > > > **Résultat de la Phase 1** : un canal sécurisé (IKE SA) existe entre A et B. Tout ce qui suit est chiffré et authentifié à l’intérieur de ce canal. Ce canal sert uniquement à la gestion (négociation, rekeying), pas au transport des données utilisateur.
        
</details>

<details markdown="1">
<summary>▫️ Étape 3 — IKE Phase 2 (négocier le tunnel de données)</summary>

        
> > > > À l’intérieur du canal IKE SA sécurisé, les deux passerelles négocient maintenant les paramètres du **tunnel de données** (IPsec SA) :
        
> > > > 1. **Quels sous-réseaux protéger** : “le trafic entre 10.1.0.0/24 et 10.2.0.0/24 doit être chiffré”. Ce sont les **traffic selectors** (ou proxy IDs).
> > > > 2. **Quel protocole** : ESP (quasi toujours) ou AH.
> > > > 3. **Quels algorithmes** pour le tunnel de données : chiffrement (AES-256-GCM, par ex.), intégrité (SHA-256), etc.
> > > > 4. **Durée de vie** de l’IPsec SA : au bout de X secondes ou Y octets, les clés seront renouvelées (rekeying) pour limiter l’impact d’une compromission de clé.
> > > > 5. **Nouvelles clés de session** sont dérivées (éventuellement avec un nouvel échange DH pour du Perfect Forward Secrecy — PFS — qui garantit que même si la clé maîtresse de Phase 1 est compromise plus tard, les clés de Phase 2 passées restent sûres).
        
> > > > **Résultat de la Phase 2** : une paire d’IPsec SA (une dans chaque direction, car chaque sens a ses propres clés et son propre SPI — Security Parameter Index) est active. Le tunnel de données est prêt.
        
</details>

<details markdown="1">
<summary>▫️ Étape 4 — Détection du NAT et bascule NAT-T (si nécessaire)</summary>

        
> > > > Pendant la Phase 1, les passerelles testent automatiquement si un NAT est présent entre elles (en comparant les adresses IP vues dans les paquets IKE avec les adresses attendues).
        
> > > > - **Si pas de NAT** : ESP circule directement (IP protocol 50). Pas de changement.
> > > > - **Si NAT détecté** : les deux parties basculent toute la communication (IKE + ESP) sur **UDP/4500**. Les paquets ESP sont encapsulés dans des paquets UDP, ce qui permet au NAT de les router correctement. C’est transparent pour le reste du fonctionnement.
        
</details>

<details markdown="1">
<summary>▫️ Étape 5 — Transport des données (le tunnel fonctionne)</summary>

        
> > > > Le tunnel est actif. Voici ce qui se passe quand un poste 10.1.0.50 (site A) veut joindre un serveur 10.2.0.10 (site B) :
        
> > > > 1. Le poste 10.1.0.50 envoie un paquet IP normal : source 10.1.0.50, destination 10.2.0.10.
> > > > 2. Ce paquet arrive à la passerelle A (c’est sa route par défaut ou une route spécifique).
> > > > 3. La passerelle A **vérifie ses politiques IPsec** : ce trafic (10.1.0.0/24 → 10.2.0.0/24) correspond à un traffic selector → il doit être protégé.
> > > > 4. La passerelle A **chiffre le paquet IP entier** (en-tête IP + payload) avec les clés de l’IPsec SA en cours, via ESP. Elle ajoute l’en-tête ESP (qui contient le SPI pour que B sache quelle SA utiliser) et un trailer d’intégrité.
> > > > 5. Elle **encapsule le tout dans un nouveau paquet IP** : source 203.0.113.1 (IP publique de A), destination 198.51.100.1 (IP publique de B), protocole: ESP (50). En mode tunnel, le paquet original est entièrement à l’intérieur.
> > > > 6. Ce paquet traverse Internet. Les routeurs intermédiaires ne voient que les adresses publiques et “protocole ESP”. Ils ne peuvent ni lire ni modifier le contenu chiffré.
> > > > 7. **Passerelle B reçoit le paquet**, identifie l’IPsec SA grâce au SPI dans l’en-tête ESP.
> > > > 8. Elle **déchiffre**, vérifie l’intégrité (le paquet n’a pas été altéré), extrait le paquet IP original (10.1.0.50 → 10.2.0.10).
> > > > 9. Elle **route** ce paquet vers son réseau interne 10.2.0.0/24. Le serveur 10.2.0.10 reçoit le paquet comme s’il venait directement du réseau local.
        
> > > > Le retour (10.2.0.10 → 10.1.0.50) suit exactement le même processus dans l’autre sens, avec l’IPsec SA dans la direction inverse.
        
</details>

<details markdown="1">
<summary>▫️ Étape 6 — Maintenance du tunnel</summary>

        
> > > > - **Rekeying** : quand la durée de vie d’une SA expire, les passerelles renégocient de nouvelles clés automatiquement (Phase 2 uniquement si la Phase 1 est encore valide, sinon les deux). L’utilisateur ne voit rien.
> > > > - **Dead Peer Detection (DPD)** : les passerelles envoient périodiquement des messages “es-tu encore vivant ?” pour détecter si l’autre extrémité est tombée. Si pas de réponse → le tunnel est marqué comme mort et les SA sont supprimées.
> > > > - **Keep-alive** : en site-to-site permanent, des mécanismes maintiennent le tunnel actif même sans trafic utilisateur.
        
</details>

<details markdown="1">
<summary>▫️ Schéma récapitulatif de l’encapsulation (mode tunnel)</summary>

        
> > > > ```
> > > > Paquet original (privé) :
> > > > [IP Header: 10.1.0.50 → 10.2.0.10] [TCP Header] [Données]
        
> > > > Après chiffrement ESP + encapsulation tunnel :
> > > > [Nouvel IP Header: 203.0.113.1 → 198.51.100.1] [ESP Header (SPI)] [████████████████████████] [ESP Trailer + Auth]
> > > > ↑ tout ceci est chiffré ↑
> > > > (IP original + TCP + données)
> > > > ```
        
> > > > Les routeurs Internet ne voient que l’enveloppe extérieure (adresses publiques, protocole ESP). Le contenu est opaque.
        
</details>

<details markdown="1">
<summary>▫️ 2 Comment fonctionne une connexion VPN TLS/SSL — étape par étape</summary>

        
> > > > Prenons un cas concret : un employé en télétravail se connecte au réseau de son entreprise via un VPN TLS/SSL (type OpenVPN ou AnyConnect). La passerelle VPN de l’entreprise est vpn.entreprise.com (IP publique 203.0.113.50), et le réseau interne est 10.0.0.0/8.
        
</details>

<details markdown="1">
<summary>▫️ Étape 1 — Résolution DNS et connexion TCP</summary>

        
> > > > 1. Le client VPN (OpenVPN, AnyConnect, FortiClient…) est lancé sur le poste de l’employé.
> > > > 2. Le client résout le nom `vpn.entreprise.com` en adresse IP via DNS.
> > > > 3. Le client établit une **connexion TCP vers le port 443** (ou UDP/443 pour DTLS, ou UDP/1194 pour OpenVPN par défaut — dépend de la config). On va prendre TCP/443 comme exemple principal.
        
> > > > Le fait que ce soit du TCP/443 est crucial : pour tout équipement intermédiaire (routeur, firewall d’hôtel, proxy d’entreprise), ce trafic ressemble à une connexion HTTPS banale. Il ne sera quasiment jamais bloqué.
        
</details>

<details markdown="1">
<summary>▫️ Étape 2 — Handshake TLS (négociation cryptographique)</summary>

        
> > > > C’est exactement le même processus que quand ton navigateur se connecte à un site HTTPS. Les deux parties négocient les paramètres de sécurité :
        
> > > > 1. **Client Hello** : le client envoie la liste des versions TLS supportées (TLS 1.2, TLS 1.3…) et les cipher suites qu’il propose (ex : TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256…).
> > > > 2. **Server Hello** : la passerelle choisit la version TLS et la cipher suite qu’elle préfère parmi celles proposées.
> > > > 3. **Certificat serveur** : la passerelle envoie son certificat X.509 (signé par une CA reconnue ou par la CA interne de l’entreprise). Le client **vérifie** ce certificat :
<details markdown="1">
<summary>• La signature est-elle valide ?</summary>

</details>

<details markdown="1">
<summary>• Le certificat est-il expiré ?</summary>

</details>

<details markdown="1">
<summary>• Le nom dans le certificat correspond-il au nom du serveur contacté (`vpn.entreprise.com`) ?</summary>

</details>

<details markdown="1">
<summary>• La CA est-elle dans le magasin de confiance du client ?</summary>

            
> > > > > Si la vérification échoue → le client refuse la connexion (protection contre le man-in-the-middle).
            
> > > > > 4. **Certificat client (optionnel)** : dans beaucoup de déploiements entreprise, le client doit aussi présenter un certificat. Ça garantit que seuls les postes ayant un certificat valide (délivré par la PKI de l’entreprise) peuvent se connecter. C’est une couche d’authentification forte avant même le login/mot de passe.
> > > > > 5. **Échange de clés** : via un échange Diffie-Hellman (ECDHE en TLS 1.3), les deux parties génèrent un **secret partagé** sans l’envoyer sur le réseau. Ce secret sert à dériver les clés de chiffrement symétriques pour la session.
> > > > > 6. **Finished** : les deux parties confirment que le handshake est complet et intègre.
        
> > > > > **Résultat** : un canal TLS chiffré existe entre le client et la passerelle. À partir de maintenant, tout ce qui circule dans cette connexion TCP est chiffré et authentifié. Un observateur sur le réseau ne voit que du trafic TCP/443 chiffré — exactement comme du HTTPS.
        
> > > > > **Différence clé avec IPsec** : en TLS, la négociation se fait en un seul flux sur un seul port (TCP/443). Pas de Phase 1 / Phase 2 séparées, pas de protocoles multiples (IKE, ESP, AH). C’est plus simple côté réseau, mais le tunnel TLS est au-dessus de TCP (ou DTLS pour UDP), pas au niveau IP directement.
        
</details>

</details>

<details markdown="1">
<summary>▫️ Étape 3 — Authentification utilisateur</summary>

        
> > > > Une fois le canal TLS établi, la passerelle VPN demande à l’utilisateur de s’authentifier. Cette étape se déroule **à l’intérieur du tunnel TLS** (donc déjà chiffrée) :
        
> > > > 1. **Login / mot de passe** : l’utilisateur entre ses identifiants (souvent les mêmes que son compte d’entreprise AD/LDAP).
> > > > 2. **MFA** (si configuré) : un second facteur est demandé — code OTP (Google Authenticator, Microsoft Authenticator), push notification, clé FIDO2…
> > > > 3. **La passerelle vérifie** les identifiants auprès de l’annuaire (AD, LDAP, RADIUS…) et le second facteur auprès du serveur MFA.
> > > > 4. **Contrôle de posture** (si configuré) : la passerelle peut vérifier l’état du poste avant d’autoriser la connexion — antivirus à jour ? OS patché ? Disque chiffré ? Poste dans le domaine ? Si le poste n’est pas conforme → connexion refusée ou accès restreint.
        
> > > > **Résultat** : l’utilisateur est authentifié. La passerelle sait qui il est et quels droits lui accorder.
        
> > > > **Différence avec IPsec** : en IPsec, l’authentification se fait pendant IKE Phase 1 (PSK ou certificats). En TLS VPN, l’authentification a deux couches distinctes : d’abord le certificat (pendant le handshake TLS), puis le login utilisateur (après le handshake). Ça permet une granularité plus fine (le certificat prouve que le poste est légitime, le login prouve que l’utilisateur est légitime).
        
</details>

<details markdown="1">
<summary>▫️ Étape 4 — Attribution de l’IP et des routes (configuration du tunnel)</summary>

        
> > > > Une fois authentifié, la passerelle configure le tunnel :
        
> > > > 1. **Attribution d’une IP interne** : la passerelle attribue au client une adresse IP dans un pool dédié (ex : 10.0.100.50). Cette IP appartient logiquement au réseau de l’entreprise.
> > > > 2. **Création de l’interface virtuelle** : le client VPN crée une interface réseau virtuelle sur le poste (ex : `tun0` sous Linux, un adaptateur virtuel sous Windows/macOS).
> > > > 3. **Push des routes** : la passerelle envoie au client les routes à installer :
<details markdown="1">
<summary>• En **split tunnel**</summary>

> “route 10.0.0.0/8 via tun0” → seul le trafic vers le réseau interne passe dans le tunnel.

</details>

<details markdown="1">
<summary>• En **full tunnel**</summary>

> “route 0.0.0.0/0 via tun0” → tout le trafic passe dans le tunnel (la route par défaut est redirigée).

> > > > > 4. **Push DNS** (souvent) : la passerelle indique au client d’utiliser les serveurs DNS internes de l’entreprise (pour résoudre les noms des serveurs internes comme `intranet.entreprise.local`).
        
> > > > > **Résultat** : le poste a maintenant une interface réseau virtuelle avec une IP interne, des routes vers les réseaux de l’entreprise, et les DNS internes. Du point de vue réseau, il se comporte comme s’il était branché sur le LAN de l’entreprise.
        
</details>

</details>

<details markdown="1">
<summary>▫️ Étape 5 — Transport des données (le tunnel fonctionne)</summary>

        
> > > > Le tunnel est actif. Voici ce qui se passe quand l’employé veut accéder au serveur intranet 10.0.1.20 :
        
> > > > 1. L’application (navigateur, client SSH, etc.) génère un paquet IP : source 10.0.100.50 (IP VPN du poste), destination 10.0.1.20.
> > > > 2. Le système vérifie la table de routage : 10.0.1.20 correspond à la route “10.0.0.0/8 via tun0” → le paquet est envoyé à l’interface virtuelle tun0.
> > > > 3. Le logiciel client VPN **récupère le paquet** sur tun0, le **chiffre via TLS** (avec les clés de session négociées au handshake), et l’envoie à la passerelle via la connexion TCP/443 existante (ou DTLS/UDP).
            
> > > > Concrètement, le paquet IP interne (10.0.100.50 → 10.0.1.20) est encapsulé comme **données** à l’intérieur de la session TLS, qui elle-même circule dans des segments TCP, qui eux-mêmes sont dans des paquets IP avec les adresses publiques du client et de la passerelle.
            
> > > > 4. La passerelle **reçoit les données TLS**, les **déchiffre**, extrait le paquet IP interne (10.0.100.50 → 10.0.1.20).
> > > > 5. Elle **route** ce paquet vers le réseau interne. Le serveur 10.0.1.20 reçoit le paquet et voit qu’il vient de 10.0.100.50 (l’IP VPN du poste).
> > > > 6. La réponse du serveur (10.0.1.20 → 10.0.100.50) arrive à la passerelle, qui la chiffre dans la session TLS et la renvoie au client.
        
</details>

<details markdown="1">
<summary>▫️ Schéma récapitulatif de l’encapsulation (TLS VPN en mode tunnel)</summary>

        
> > > > ```
> > > > Paquet original (privé) :
> > > > [IP: 10.0.100.50 → 10.0.1.20] [TCP: port 80] [HTTP request...]
        
> > > > Après encapsulation TLS :
> > > > [IP: 82.x.x.x → 203.0.113.50] [TCP: port 443] [TLS Record: ████████████████████]
> > > > ↑ chiffré par TLS ↑
> > > > (paquet IP original entier)
> > > > ```
        
> > > > Un observateur sur le réseau ne voit qu’une connexion TCP/443 vers vpn.entreprise.com, indiscernable d’une visite HTTPS normale. Il ne peut pas savoir ce qu’il y a à l’intérieur, ni même que c’est un VPN.
        
</details>

<details markdown="1">
<summary>▫️ Étape 6 — Cas du mode Clientless / Portail web (variante sans tunnel)</summary>

        
> > > > Dans ce mode, il n’y a pas d’interface virtuelle ni de tunnel IP :
        
> > > > 1. L’utilisateur ouvre son navigateur et va sur `https://vpn.entreprise.com`.
> > > > 2. Il s’authentifie (login/MFA) sur le portail web.
> > > > 3. Le portail affiche une liste d’applications autorisées : webmail, intranet, console d’administration, partage de fichiers…
> > > > 4. Quand l’utilisateur clique sur une appli, **c’est la passerelle qui fait le relais** (reverse proxy). Le navigateur communique en HTTPS avec la passerelle, et la passerelle communique avec le serveur interne au nom de l’utilisateur.
> > > > 5. **Aucun logiciel n’est installé** sur le poste. L’accès est purement applicatif (web) et non réseau.
        
> > > > C’est plus limité (pas d’accès réseau complet, pas de ping, pas de SSH direct), mais c’est très pratique pour un accès rapide depuis un poste non maîtrisé.
        
</details>

<details markdown="1">
<summary>▫️ Étape 7 — DTLS : la variante UDP (performance)</summary>

> la variante UDP (performance)

        
> > > > Le problème du **TCP-over-TCP** expliqué en détail :
        
> > > > En mode TCP classique, la pile réseau ressemble à ça :
        
> > > > ```
> > > > [Application] → [TCP interne] → [IP interne] → [TLS (chiffrement)] → [TCP externe (443)] → [IP externe] → Internet
> > > > ```
        
> > > > Si un paquet est perdu sur Internet, le TCP externe retransmet. Mais le TCP interne (celui de l’application) ne le sait pas — il a son propre timer. Si le retard du TCP externe cause un timeout du TCP interne, celui-ci retransmet aussi. Résultat : **deux retransmissions pour une seule perte**, ce qui dégrade les performances, surtout sur des liaisons instables (Wi-Fi, 4G).
        
> > > > **DTLS (Datagram TLS)** résout ça en utilisant UDP au lieu de TCP pour la couche externe :
        
> > > > ```
> > > > [Application] → [TCP interne] → [IP interne] → [DTLS (chiffrement)] → [UDP externe (443)] → [IP externe] → Internet
> > > > ```
        
> > > > UDP ne retransmet pas. Si un paquet est perdu, seul le TCP interne gère la retransmission. Plus de conflit entre deux couches TCP. C’est pour ça que beaucoup de solutions (AnyConnect, FortiClient) utilisent DTLS par défaut quand c’est possible, avec un fallback sur TCP/TLS si UDP est bloqué.
        
</details>

<details markdown="1">
<summary>▫️ 6.7 Comparaison directe : établissement IPsec vs TLS/SSL</summary>

> établissement IPsec vs TLS/SSL

        
> > > > | Aspect | IPsec | TLS/SSL VPN |
> > > > | --- | --- | --- |
> > > > | **Négociation** | IKE Phase 1 (canal sécurisé) puis Phase 2 (tunnel données) — 2 étapes distinctes, protocole dédié | Handshake TLS en une passe — même protocole que HTTPS |
> > > > | **Authentification machine** | PSK ou certificat pendant IKE Phase 1 | Certificat serveur (+ client optionnel) pendant handshake TLS |
> > > > | **Authentification utilisateur** | Possible dans IKEv2 (EAP), ou séparée | Après le handshake TLS, dans le tunnel (login + MFA) |
> > > > | **Protocoles sur le réseau** | UDP/500 (IKE) + IP proto 50 (ESP) + UDP/4500 (NAT-T) — 3 flux distincts | TCP/443 (ou UDP/443 DTLS) — 1 seul flux |
> > > > | **Traversée NAT/firewall** | Nécessite NAT-T, peut être bloqué par certains firewalls restrictifs | Passe quasi partout (port 443 = web) |
> > > > | **Niveau d’opération** | Couche IP (couche 3) : protège les paquets IP directement | Au-dessus de TCP/UDP (couche 4+) : encapsule le trafic IP dans une session TLS |
> > > > | **Encapsulation** | Nouvel en-tête IP + ESP autour du paquet original | Paquet original envoyé comme données dans un flux TCP/TLS |
> > > > | **Performance** | Très bonne (accélération matérielle, pas de TCP-over-TCP) | Bonne avec DTLS ; risque TCP-over-TCP en mode TLS pur |
> > > > | **Interopérabilité** | Standard (RFC), multi-constructeurs | Dépend du produit (OpenVPN ≠ AnyConnect ≠ FortiSSL) |
    
</details>

</details>

<details markdown="1">
<summary>🔸 1 - Principe du VPN</summary>

    
</details>

<details markdown="1">
<summary>🔸 Définition</summary>

> Technologie permettant une connexion sécurisée et chiffrée entre un réseau privé et un appareil distant en créant un tunnel chiffré pour protéger les transferts de données, l’appareil distant recevant une IP locale (interne) pour accèder aux ressources du réseau.

</details>

<details markdown="1">
<summary>🔸 Ports standards utilisés</summary>

        
        
> > > | **Protocole** | **Port** | **Usage** |
> > > | --- | --- | --- |
> > > | PPTP | TCP/1723 | Connexions VPN Point-to-Point Tunneling Protocol |
> > > | IKEv1 / IKEv2 | UDP/500 | Connexions VPN IPsec |
> > > | L2TP | UDP/1701 | Connexions VPN L2TP (+ IPSec sur UDP/500 et UDP/4500) |
> > > | SSL/TLS VPN | TCP/443 | Connexions VPN via HTTPS (OpenVPN, portail SSL) |
> > > | WireGuard | UPD/51820 | Connexions VPN WireGuard (port par défaut, configurable) |
</details>

<details markdown="1">
<summary>🔸 Composants et requirement d’un VPN</summary>

        
        
> > > | **Composant** | **Description** |
> > > | --- | --- |
> > > | VPN Client | Installé sur appareil distant. Etablit et maintient co avec serveur (ex : client OpenVPN) |
> > > | VPN Server | Ordi ou équipement réseau qui accepte les connexions des clients VPN et route trafic entre clients VPN ↔ réseau privé |
> > > | Encryption (chiffrement) | Utilise divers algo et proto pour secure la co et protéger données transmises |
> > > | Authentication | Client et serveur s’authentifient mutuellement |
</details>

<details markdown="1">
<summary>🔸 Protocole au niveau TCP/IP</summary>

<details markdown="1">
<summary>▫️ Utilise ESP pour chiffrer et authentifier le trafic VPN</summary>

> > > > - Permet l’échange sécurisé de données entre client et serveur via Internet public
    
</details>

</details>

<details markdown="1">
<summary>🔸 IPsec (Internet Protocol Security)</summary>

    
> > > - 
> > > - Firewall
    
> > > Va analyser et filtrer le trafic entrant et sortant d’un réseau 
    
</details>

<details markdown="1">
<summary>🔸 Types de firewall</summary>

<details markdown="1">
<summary>▫️ Stateless firewall</summary>

> Opèrent sur la couche 3 et 4. Se base uniquement sur des règles prédéterminées. Ne peut pas appliquer de politique complexe, va recevoir un paquet si source illégitime, ne prendra pas en compte les relations avec les précédentes co.

</details>

<details markdown="1">
<summary>▫️ Stateful Firewall</summary>

> Va au-delà du filtrage par règle prédéterminées. Garde et conserve trace des connexions précédentes dans une table d’état. Inspecte les paquets en se basant sur leurs historiques.

> > > > - Ex : Permet uniquement des données entrantes qui correspondent à une demande sortante déjà établie.
</details>

<details markdown="1">
<summary>▫️ Proxy firewall</summary>

> Servent d'intermédiaires entre le réseau privé et Internet et fonctionnent sur la couche 7. Inspectent tous les paquets, les requêtes des users sont transmisses par ce proxy après inspection et masque adresse IP.

> > > > - Ex : Proxy Web qui filtre les demandes HTTP malveillantes contenant des motifs suspects.
</details>

<details markdown="1">
<summary>▫️ NGFW</summary>

> Combine stateful inspection avec des fonctionnalités avancées telles que l'inspection profonde des paquets, la détection / prévention des intrusions et le contrôle des appli. Ex : Peut bloquer IP malveillantes connues, inspecter trafic chiffré pour les menaces et appliquer des politiques spécifiques à l'application.

</details>

</details>

<details markdown="1">
<summary>🔸 Règles dans un firewall</summary>

<details markdown="1">
<summary>▫️ Source address / Destination address / Port / Protocol / Action / Direction.</summary>

</details>

<details markdown="1">
<summary>▫️ Types d’actions</summary>

<details markdown="1">
<summary>• Allow / Deny / Forward (Redirige trafic vers un segment différent du réseau, par exemple rediriger tout le trafic qui vient du port 80 vers l’adresse IP XX)</summary>

</details>

</details>

<details markdown="1">
<summary>▫️ Direction des règles</summary>

<details markdown="1">
<summary>• Inbound</summary>

> S’applique uniquement au trafic entrant. Par exemple, autoriser le trafic HTTP entrant (port 80) sur serveur web.

</details>

<details markdown="1">
<summary>• Outbound</summary>

> S’applique pour le trafic sortant. Exemple, bloquer tous les trafic SMTP sortant excepté depuis notre serveur de mail

</details>

<details markdown="1">
<summary>• Forward</summary>

> Redirige trafic spécifique à l’intérieur du réseau. Par exemple, transférer tout le trafic HTTP entrant vers notre web serveur dans notre réseau.

                
> > > > > ![Pasted image 20250928143834.png](../../../assets/reseau-prises-de-notes-pasted-image-20250928143834.png)
                
> > > > > - Proxies
    
> > > > > Appareil / service qui se trouve au milieu d'une connexion et agit comme un intermédiaire. Couche 7.
    
</details>

</details>

</details>

<details markdown="1">
<summary>🔸 Dedicated Proxy / Forward Proxy</summary>

> Ce que les gens imaginent, intermédiaire classique, conçus pour filtrer les demandes sortantes.

        
> > > ![Pasted image 20250929231520.png](../../../assets/reseau-prises-de-notes-pasted-image-20250929231520.png)
        
</details>

<details markdown="1">
<summary>🔸 Reverse Proxy</summary>

> A l'inverse du Forward Proxy, il filtre les demandes entrantes. Objectif principal est d'écouter une adresse et de transférer à un réseau fermé.

        
> > > ![Pasted image 20250929232236.png](../../../assets/reseau-prises-de-notes-pasted-image-20250929232236.png)
        
> > > - (Non) Transparent Proxy
> > > - IDS / IPS
    
> > > A la différence du firewall qui filtre le trafic entrant et sortant, cependant, il faut mettre une sécurité permettant de détecter les activités de co ayant déjà passé le firewall.
    
> > > - IDS : Observe événements de trafic pour identifier le comportement malveillant ou les violations des politiques et générer des alertes mais ne pas bloquer.
> > > - IPS : Fonctionne comme IDS mais bloque en rejetant le trafic malveillant en temps réel.
    
> > > | Techniques | Description |
> > > | --- | --- |
> > > | Signature-based detection | Matches trafic en fonction d'une base de données d'exploits connus. Chaque attaques a des patterns uniques qu’on nomment signatures |
> > > | Anomaly-based detection | Va apprendre ce qu’est un comportement dit “normal” puis va détecter déviances et anomalies. |
</details>

<details markdown="1">
<summary>🔸 Type d’IDS</summary>

<details markdown="1">
<summary>▫️ HIDS</summary>

> Installé individuellement sur un hôte.

</details>

<details markdown="1">
<summary>▫️ NIDS</summary>

> Détecte activité malveillante sur l’ensemble du réseau. Monitor le trafic réseau de tous les hôtes, offre vue centralisée.

        
> > > > ![Pasted image 20250928145518.png](../../../assets/reseau-prises-de-notes-pasted-image-20250928145518.png)
        
</details>

</details>

<details markdown="1">
<summary>🔸 Snort</summary>

> > > - Formats de règles
        
> > > ![image.png](../../../assets/reseau-prises-de-notes-image-25.png)
        
<details markdown="1">
<summary>▫️ Créer règle lorsque l’on ping la loopback</summary>

> > > > - **`sudo nano /etc/snort/rules/local.rules`**
<details markdown="1">
<summary>• `alert icmp any any -> 127.0.0.1 any (msg</summary>

> "Loopback Ping Detected"; sid:10003; rev:1;)`

</details>

</details>

<details markdown="1">
<summary>▫️ Lancer snort</summary>

> **`sudo snort -q -l /var/log/snort -i lo -A console -c /etc/snort/snort.conf`**

<details markdown="1">
<summary>• Attention, bien voir le nom de l’interface, pas forcément lo</summary>

        
> > > > > ![image.png](../../../assets/reseau-prises-de-notes-image-26.png)
        

> > > > > ## How the web works

> > > > > Lorsque site web consulté, l’ordi doit connaitre l’ip du serveur web, pour ça il utilise le DNS. Ensuite l’ordi communique avec le serveur web à l’aide du protocole HTTP, le serveur web retourne le contenu de la page (HTML, JavaScript, Images…). 

</details>

</details>

</details>

### Requête le site web dans navigateur > Trouve l’IP du serveur web avec DNS > Connecte serveur web > Voit site web

> > - DNS : Mappe adresse IP à un nom
> > - Résumé
> > 1. **Cache Local :** Ton OS (Windows/Linux) regarde d'abord dans sa poche (son cache DNS ou le fichier `/etc/hosts`). S'il l'a, c'est fini.
> > 2. **Le Resolver :** S'il ne l'a pas, il crie à travers le réseau vers le serveur DNS configuré (souvent ta Box ou le 8.8.8.8 de Google).
> > 3. **La Récursion :** Si ta Box ne sait pas, elle va demander aux chefs :
<details markdown="1">
<summary>• Aux serveurs **Racines** (.)</summary>

> *"Qui gère .com ?"*

</details>

<details markdown="1">
<summary>• Aux serveurs **TLD** (.com)</summary>

> *"Qui gère banque.com ?"*

</details>

<details markdown="1">
<summary>• Au serveur **Authoritative** (celui de la banque)</summary>

> *"Quelle est l'IP de www ?"*

> > > 4. **Réponse :** L'IP revient à ton PC.
        
> > > > Note Hacker : C'est ici qu'on fait du DNS Spoofing. Si je suis sur ton réseau local, je peux répondre à ton PC avant le vrai serveur DNS et dire : "L'IP de la banque, c'est MOI (ma machine Kali)".
> > > > 
> > > - Permet communication des équipements vers internet, traduit adresse IP en nom humainement lisible.
    
> > > Le système DNS est comme le répertoire d'Internet, comme une BDD. Il aide à trouver le bon numéro (adresse IP) pour un nom donnée (un domaine tel que [google.com](http://google.com/)). Sans DNS, nous aurions besoin de mémoriser des adresses IP longues et souvent complexes pour chaque site Web que nous visitons.
    
</details>

<details markdown="1">
<summary>🔸 DNS Hierarchy ou hiérarchie de domaine</summary>

> Le DNS est organisé comme un arbre, commence par la racine et se ramifiant en différentes couches :

    
> > > | Couche | Description |
> > > | --- | --- |
> > > | Root Servers (Serveur racine) | Le haut de la hiérarchie DNS. Géré par l’ICANNIl en existe 13. Utilisent l'adressage **Anycast**, permettant à une adresse IP unique d'être routée vers le serveur physique le plus proche géographiquement. |
> > > | TLD | Comme .com, .org, .net, ou country codes .uk, .fr |
> > > | Second-level domains | Pour exemple, tryhackme(.com)  |
> > > | Sous-domain ou hostname | [admin.tryhackme.com](http://admin.tryhackme.com)  : Permet créer nom plus long et sur des sujets spécifiques. |
    
</details>

<details markdown="1">
<summary>🔸 Résolution DNS</summary>

    
> > > | Etape | Description |
> > > | --- | --- |
> > > | Step 1 | On écrit [www.google.com](http://www.google.com/) dans notre navigateur |
> > > | Step 2 | Notre ordinateur va check dans le cache du DNS local pour voir si il connait déjà l'adresse IP |
> > > | Step 3 | Si pas trouvé localement, il questionne un serveur DNS récursif, généralement fournit par notre FAI ou un tier comme le service DNS de Google. |
> > > | Step 4 | Si toujours pas, elle va contacter un root serveur (serveur racine) qui va pointer vers le serveur TLD approprié (comme .com) |
> > > | Step 5 | TLD serveur va redirige la demande au serveur de nom faisant autorité pour [google.com](http://google.com/) |
> > > | Step 6 | Le serveur de nom faisant autorité va répondre avec l'adresse IP de [google.com](http://google.com/) |
> > > | Step 7 | Le serveur récursif va retourner l'adresse IP vers l'ordinateur qui peut maintenant se connecter sur le serveur web directement. |
</details>

<details markdown="1">
<summary>🔸 Requête DNS</summary>

> > > 1. Lorsque requête nom de domaine, PC va check dans cache local pour voir si adresse déjà visité, si non, requête au serveur récursif DNS.
> > > 2. Serveur récursif DNS généralement fournit par FAI, mais peut être conf manuellement. Ce serveur a un cache local, si adresse trouvée localement, résultat renvoyé à l’ordi et se termine. Sinon, recherche pour trouver réponse avec serveur DNS root d’internet.
> > > 3. Serveur DNS root consiste à rediriger vers bon serveur TLD server. Par exemple demande www.tryhackme.com, serveur root reconnaîtra TLD .com et renverra vers bon serveur TLD qui gère les adresses .com
> > > 4. Serveur TLD détient enregistrements indiquant où trouver serveur faisant autorité pour répondre à la requête DNS.  Serveur d’autorité aussi connu sous le nom de serveur de nom. Serveur de nom pour tryhackme est kip/ns/cloudflare.com… Multiple serveur de noms pour un nom de domaine utile pour backup.
> > > 5. Serveur DNS d’autorité est le serveur responsable de stocker les enregistrements DNS pour des nom de domaine particulier. En fonction du record type, l’enregistrement DNS est retourné au serveur DNS récursif, où une copie local sera placé en cache pour les futures requêtes puis transmis au client original. Enregistrements DNS livrés avec TTL, valeur représenté en seconde, stocké localement jusqu’à qu’elle soit recherchée à nouveau. 
    
</details>

<details markdown="1">
<summary>🔸 DNS Record types</summary>

    
> > > | Field | Description |
> > > | --- | --- |
> > > | A | Résoud IPv4 |
> > > | AAAA  | IPv6 |
> > > | CNAME  | Résoud un autre nom de domaine. TryHackMe shop a le sous-domaine [store.tryhackme.com](http://store.tryhackme.com) qui retourne un enregistrement CNAME shop.shopify.com. |
> > > | MX  | Renvoient adresse des serveurs qui traitent les mails pour le domaine questionné. MX record réponse pour [tryhackme.com](http://tryhackme.com) sera alt1.aspmx.l.google.com.  |
> > > | TXT  | Champ de texte libre qui permette de stocker tout type de donnée de texte |
</details>

### HTTP

> Défini communication entre navigateur et web servers

    
> > HyperText Transfert Protocol, protocole qui est utilisé à chaque consultation de page web.
    
<details markdown="1">
<summary>🔸 Requêtes et réponses</summary>

<details markdown="1">
<summary>▫️ URL (Uniform Resource Locator)</summary>

> Instruction pour accéder à une ressource sur internet.

</details>

<details markdown="1">
<summary>▫️ Faire une requête</summary>

<details markdown="1">
<summary>• Possible juste en une ligne GET / HTTP/1.1</summary>

</details>

<details markdown="1">
<summary>• Header HTTP = requête avec données, contient données à donner au serveur web avec qui on communique.</summary>

            
> > > > > ```jsx
> > > > > GET / HTTP/1.1 : Envoie la méthode GET), demande la page and dit au serveur web qu'on utilise protocole et version.
            
> > > > > Host: tryhackme.com 
> > > > > User-Agent: Mozilla/5.0 Firefox/87.0
> > > > > Referer: https://tryhackme.com/
> > > > > ```
            
</details>

</details>

<details markdown="1">
<summary>▫️ Réponse</summary>

            
> > > > ```jsx
> > > > HTTP/1.1 200 OK
            
> > > > Server: nginx/1.15.8
> > > > Date: Fri, 09 Apr 2021 13:34:03 GMT
> > > > Content-Type: text/html
> > > > Content-Length: 98
            
> > > > <html>
> > > > <head>
> > > > <title>TryHackMe</title>
> > > > </head>
> > > > <body>
> > > > Welcome To TryHackMe.com
> > > > </body>
> > > > </html>
> > > > ```
            
</details>

</details>

<details markdown="1">
<summary>🔸 Méthode HTTP</summary>

> > > - GET : Avoir information d’un serveur web
<details markdown="1">
<summary>▫️ POST</summary>

> Pour soumettre donnée au serveur web et créer potentiellement un nouvel enregistrement

> > > > - PUT : Pour soumettre donnée au serveur web pour mettre à jour des information
</details>

<details markdown="1">
<summary>▫️ DELETE</summary>

> Supprimer info / enregistrements

</details>

</details>

<details markdown="1">
<summary>🔸 HTTP status codes</summary>

<details markdown="1">
<summary>▫️ 200 - 299</summary>

> Success

</details>

<details markdown="1">
<summary>▫️ 300 -399</summary>

> Redirection

</details>

<details markdown="1">
<summary>▫️ 400 - 499</summary>

> Clients errors : Informe client qu’il y a une erreur dans sa requête

</details>

<details markdown="1">
<summary>▫️ 500 - 599</summary>

> Servers errors :

</details>

</details>

<details markdown="1">
<summary>🔸 Headers</summary>

<details markdown="1">
<summary>▫️ Eléments de données additionnels envoyés au serveur web pour faire des requêtes</summary>

</details>

<details markdown="1">
<summary>▫️ En-têtes de requêtes courantes</summary>

<details markdown="1">
<summary>• Host</summary>

> Certains serveurs web hébergent de multiples sites web. Donc en précisant host headers permet de recevoir celui choisi sinon page par défaut.

</details>

<details markdown="1">
<summary>• User-agent</summary>

> Notre moteur de recherche et version number, indique au web server pour avoir le bon format et bons éléments HTML, JavaScript et CSS valables que sur certains navigateurs.

</details>

<details markdown="1">
<summary>• Content-Length</summary>

> Taille de contenue permet de s’assurer qu’il n’y pas de perte de données

</details>

<details markdown="1">
<summary>• Cookie</summary>

> Donnée envoyée au server pour aider à la mémorisation de nos informations.

</details>

</details>

<details markdown="1">
<summary>▫️ En-têtes de réponses courantes</summary>

<details markdown="1">
<summary>• Set-cookie</summary>

> Informations stockées qui sont renvoyés au serveur web à chaque requêtes/

</details>

<details markdown="1">
<summary>• Cache-control</summary>

> Combien de temps faut il stocker le contenu avant de devoir faire à nouveau la requête.

</details>

<details markdown="1">
<summary>• Content-type</summary>

> Dit au client quels types de données est retournées, HTML, PDF…

</details>

</details>

</details>

<details markdown="1">
<summary>🔸 Cookie</summary>

<details markdown="1">
<summary>▫️ Petite pièce de donnée qui est stocké dans l’ordinateur. Save quand reçoit une en-tête Set-cookie d’un server web. À chaque nouvelle requête, renvoit données du cookie au serveur web. Les cookies peuvent être utilisés pour rappeler au serveur web votre identité, certains paramètres personnels du site web ou si vous avez déjà visité le site.</summary>

> > > > - Websites
</details>

</details>

<details markdown="1">
<summary>🔸 Fonctionnement</summary>

<details markdown="1">
<summary>▫️ Visite site web, navigateur envoie requête au serveur web demande information à propos de la page visité. répond en fournissant données que navigateur utilise pour afficher la page. Serveur web est simplement ordinateur dédié situé ailleurs qui traite les requêtes</summary>

</details>

</details>

<details markdown="1">
<summary>🔸 HTML</summary>

        
> > > ![image.png](../../../assets/reseau-prises-de-notes-image-27.png)
        
<details markdown="1">
<summary>▫️ <!DOCTYPE html></summary>

> Défini que la page est un document HTML, aide à la standardisation pour les navigateurs.

</details>

<details markdown="1">
<summary>▫️ <html></summary>

> Element racine de la page HTML, tous les autres éléments viennent après

</details>

<details markdown="1">
<summary>▫️ <head></summary>

> Element qui contient les info à propos de la page (comme le titre)

</details>

<details markdown="1">
<summary>▫️ <body></summary>

> Défini le corps du document HTML, seuls le contenu dans le body apparait dans le navigateur

</details>

<details markdown="1">
<summary>▫️ <h1></summary>

> Défini un gros titre

> > > > - <p> : paragraphe
</details>

</details>

<details markdown="1">
<summary>🔸 JavaCript</summary>

    
</details>

### Naviguer sur Internet

> > 1. DNS Lookup : Ordinateur tente de résoudre le nom de domaine à une adresse IP (Ex : 92..184.216.34 pour [example.com](http://example.com/))
> > 2. Data Encapsulation :
<details markdown="1">
<summary>▫️ Navigateur génère requête HTTP</summary>

</details>

<details markdown="1">
<summary>▫️ Requête encapsulée avec TCP, spécifie 80 ou 443.</summary>

</details>

<details markdown="1">
<summary>▫️ Paquet inclut l'adresse IP de destination 92..184.216.34</summary>

</details>

<details markdown="1">
<summary>▫️ Sur le réseau local, notre ordinateur utilise ARP pour trouver la MAC adresses de la gateway (routeur)</summary>

> > > 3. Data transmission
</details>

<details markdown="1">
<summary>▫️ Data frame est envoyé à l'adresse MAC du routeur</summary>

</details>

<details markdown="1">
<summary>▫️ Le routeur transfère le paquet à l'adresse IP de destination.</summary>

</details>

<details markdown="1">
<summary>▫️ Routeurs intermédiaire continue le transfert du paquet basé sur l'IP</summary>

> > > 4. Server processing
</details>

<details markdown="1">
<summary>▫️ Le serveur reçoit le paquet et le dirige vers le port d'écoute de l'application 80 ou 443</summary>

</details>

<details markdown="1">
<summary>▫️ Le serveur traite la demande HTTP et renvoie une réponse en suivant le même chemin à l'envers.</summary>

> > > 5. Response transmission
</details>

<details markdown="1">
<summary>▫️ Le serveur renvoie la réponse au port temporaire du client qui a été sélectionné au hasard par l'OS du client au début de la session.</summary>

</details>

<details markdown="1">
<summary>▫️ La réponse suit le chemin inverse via le réseau, dirigée de routeur en routeur en fonction de l'adresse IP source et des informations du port jusqu'à qu'elle atteigne le client</summary>

</details>


## Technique
