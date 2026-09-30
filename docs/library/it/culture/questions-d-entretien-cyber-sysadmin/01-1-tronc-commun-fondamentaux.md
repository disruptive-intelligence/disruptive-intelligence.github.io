---
title: 1) Tronc commun — Fondamentaux
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

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
