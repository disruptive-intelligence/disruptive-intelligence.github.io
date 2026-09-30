---
title: Questions essentielles
source: IT/03_Networking/networking_notion.md
note: Notions réseau
up:
- - Notions réseau
  - ../index.md
- - Annexe — Questions types d'entretien et réponses types
  - index.md
---

- **Question :** Expliquez la différence entre TCP et UDP.
  - **Réponse type :** TCP est orienté connexion : il établit une session (three-way handshake), garantit la livraison des données dans l'ordre, et retransmet en cas de perte. C'est fiable mais plus lent. UDP est sans connexion : il envoie les données sans vérification, sans garantie d'ordre ni de livraison. C'est plus rapide et utilisé quand la vitesse prime sur la fiabilité — DNS, streaming, VoIP.

- **Question :** À quoi servent les couches du modèle OSI les plus importantes en pratique ?
  - **Réponse type :** En pratique, on travaille surtout avec la couche 2 (liaison — adresses MAC, switches), la couche 3 (réseau — adresses IP, routage), la couche 4 (transport — TCP/UDP, ports) et la couche 7 (application — HTTP, DNS, SMTP). La couche 2 gère la communication locale sur un segment, la couche 3 le routage entre réseaux, la couche 4 identifie les applications via les ports, et la couche 7 c'est le protocole applicatif.

- **Question :** Comment fonctionne le DNS ?
  - **Réponse type :** Le DNS traduit un nom de domaine en adresse IP. Quand un client veut joindre un site, il interroge son serveur DNS récursif. Si celui-ci n'a pas la réponse en cache, il remonte la hiérarchie : serveur racine, puis serveur TLD (.com, .fr), puis serveur autoritaire du domaine. La réponse est mise en cache avec un TTL. Le DNS utilise le port 53, principalement en UDP.

- **Question :** Quelle est la différence entre une adresse MAC et une adresse IP ?
  - **Réponse type :** L'adresse MAC est une adresse physique de 48 bits, unique par interface réseau, qui sert à la communication sur un segment local (couche 2). L'adresse IP est une adresse logique (32 bits en IPv4) qui permet le routage entre réseaux (couche 3). Le switch utilise les MAC pour aiguiller les trames localement, le routeur utilise les IP pour router les paquets entre réseaux.

- **Question :** Qu'est-ce qu'un VLAN et à quoi ça sert ?
  - **Réponse type :** Un VLAN (Virtual LAN) segmente logiquement un réseau physique en plusieurs domaines de broadcast distincts. Ça permet d'isoler les flux — par exemple séparer les postes utilisateurs, les serveurs et les imprimantes — sans avoir besoin de matériel dédié. C'est une mesure de sécurité de base en entreprise pour limiter la propagation latérale.


## Questions complémentaires

- **Question :** Expliquez le three-way handshake TCP.
  - **Réponse type :** C'est le mécanisme d'établissement d'une connexion TCP en trois étapes : le client envoie un SYN, le serveur répond SYN-ACK, et le client confirme avec un ACK. À ce stade la connexion est établie et les données peuvent circuler. Ce handshake permet aux deux parties de synchroniser leurs numéros de séquence.

- **Question :** Quels sont les ports à connaître absolument en sécurité ?
  - **Réponse type :** Les incontournables : 22 (SSH), 53 (DNS), 80/443 (HTTP/HTTPS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP), 5985/5986 (WinRM). En environnement AD, les ports Kerberos, LDAP et SMB sont critiques. Savoir associer un port à un service aide beaucoup en analyse de flux ou en pentest.

- **Question :** Qu'est-ce qu'ARP et quel risque de sécurité y est associé ?
  - **Réponse type :** ARP traduit une adresse IP en adresse MAC sur un réseau local. Le risque c'est l'ARP spoofing : un attaquant envoie de fausses réponses ARP pour associer son adresse MAC à l'IP d'une autre machine — typiquement la gateway. Ça lui permet de se positionner en man-in-the-middle et d'intercepter ou modifier le trafic.


## Questions les plus probables en entretien

1. TCP vs UDP ?
2. Modèle OSI : couches clés en pratique ?
3. Comment fonctionne DNS ?
4. MAC vs IP ?
5. Ports essentiels à connaître ?
6. C'est quoi un VLAN ?


## Réponses flash

- **TCP vs UDP** → TCP = connexion, fiable, ordonné, handshake. UDP = sans connexion, rapide, pas de garantie.
- **OSI pratique** → L2 (MAC/switch), L3 (IP/routage), L4 (ports/TCP-UDP), L7 (HTTP/DNS).
- **DNS** → Nom → IP. Port 53/UDP. Récursif → racine → TLD → autoritaire. Cache + TTL.
- **MAC vs IP** → MAC = physique, locale (L2). IP = logique, routable (L3).
- **Ports clés** → 22 SSH, 53 DNS, 80/443 HTTP(S), 88 Kerberos, 389 LDAP, 445 SMB, 3389 RDP.
- **VLAN** → Segmentation logique du réseau, isolation des domaines de broadcast.
- **ARP** → IP → MAC en local. Risque = ARP spoofing → MITM.

---

</details>


</details>
