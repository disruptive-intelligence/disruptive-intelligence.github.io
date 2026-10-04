---
title: Révision — Réseau
revision: it/reseau
domaine: IT
sources:
- IT/04 Réseau/Réseau.md
---

*D'après le cours [Réseau](../it/reseau/reseau/index.md)*

## Questions essentielles

- **Question :** Expliquez la différence entre TCP et UDP.
  - **Réponse type :** TCP est orienté connexion : il établit une session (three-way handshake), garantit la livraison des données dans l'ordre et retransmet en cas de perte. C'est fiable mais plus lent. UDP est sans connexion : il envoie sans vérification, sans garantie d'ordre ni de livraison. Il est plus rapide et utilisé quand la vitesse prime : DNS, streaming, VoIP.

- **Question :** À quoi servent en pratique les couches du modèle OSI ?
  - **Réponse type :** On travaille surtout avec la couche 2 (adresses MAC, switchs, communication sur un segment), la couche 3 (adresses IP, routage entre réseaux), la couche 4 (TCP/UDP et ports, qui identifient l'application) et la couche 7 (protocoles applicatifs : HTTP, DNS, SMTP). Le découpage en couches isole les responsabilités : on change de support physique sans toucher à HTTP.

- **Question :** Comment fonctionne le DNS ?
  - **Réponse type :** Le DNS traduit un nom en adresse IP. Le client regarde son cache et le fichier hosts, puis interroge son résolveur récursif. Sans réponse en cache, celui-ci remonte la hiérarchie : serveur racine, serveur du TLD, puis serveur faisant autorité du domaine. La réponse est mise en cache pour la durée de son TTL. Port 53, surtout en UDP.

- **Question :** Quelle est la différence entre une adresse MAC et une adresse IP ?
  - **Réponse type :** La MAC est une adresse physique de 48 bits, propre à une interface, utilisée sur le segment local (couche 2). L'IP est une adresse logique qui permet le routage entre réseaux (couche 3). La MAC change à chaque saut, puisque chaque routeur réécrit la trame ; l'IP reste la même de bout en bout, sauf NAT.

- **Question :** Que se passe-t-il quand un poste envoie un paquet vers une IP hors de son réseau ?
  - **Réponse type :** Il fait un ET logique entre l'IP de destination et son masque : le résultat diffère de son réseau, la destination est distante. Il consulte sa table de routage, trouve la passerelle par défaut, obtient sa MAC par ARP, puis encapsule le paquet — avec l'IP de destination finale — dans une trame adressée à la MAC de la passerelle. Chaque routeur décapsule, consulte sa table et réencapsule pour le saut suivant.

- **Question :** Qu'est-ce qu'un VLAN et à quoi ça sert ?
  - **Réponse type :** Un VLAN segmente logiquement un réseau physique en plusieurs domaines de diffusion isolés. On sépare ainsi postes, serveurs, imprimantes et invités sans matériel dédié. C'est une mesure de sécurité de base : une machine compromise ne voit que son segment, ce qui limite la propagation latérale.

## Questions complémentaires

- **Question :** Expliquez le three-way handshake TCP.
  - **Réponse type :** Le client envoie un SYN avec son numéro de séquence initial, le serveur répond SYN-ACK avec le sien, le client confirme par un ACK. Les deux côtés ont synchronisé leurs numéros de séquence et la connexion est établie.

- **Question :** Comment fonctionne HTTPS ?
  - **Réponse type :** C'est HTTP dans TLS. Lors du handshake, client et serveur négocient la version et les algorithmes, le serveur présente son certificat que le client vérifie (CA de confiance, nom, validité), puis ils dérivent une clé de session symétrique, aujourd'hui par un échange Diffie-Hellman éphémère. Tout le reste est chiffré avec cette clé, beaucoup plus rapide que l'asymétrique.

- **Question :** Différence entre VPN IPsec et VPN SSL/TLS ?
  - **Réponse type :** IPsec opère au niveau IP : il chiffre les paquets via ESP après une négociation IKE sur UDP 500, avec plusieurs flux. C'est le standard du site à site. Le VPN TLS encapsule le trafic dans une session TLS sur TCP 443, comme du HTTPS : il passe presque partout et convient à l'accès distant, avec une authentification en deux temps.

- **Question :** Qu'est-ce qu'ARP et quel risque y est associé ?
  - **Réponse type :** ARP traduit une IP en adresse MAC sur le réseau local, par une requête en broadcast. Il ne vérifie pas les réponses : une machine peut se faire passer pour une autre, typiquement la passerelle, et intercepter le trafic. On s'en protège par l'inspection ARP sur les switchs et la segmentation.

- **Question :** Quels ports faut-il connaître absolument ?
  - **Réponse type :** 22 SSH, 53 DNS, 80/443 HTTP(S), 88 Kerberos, 135 RPC, 389/636 LDAP(S), 445 SMB, 3389 RDP, 5985/5986 WinRM, plus les ports de messagerie (25, 587, 993). Associer un port à un service fait gagner beaucoup de temps en analyse de flux.

## Questions les plus probables en entretien

1. TCP vs UDP ?
2. Les couches OSI utiles en pratique ?
3. Comment fonctionne le DNS ?
4. MAC vs IP ?
5. Paquet vers une IP hors du réseau local ?
6. Qu'est-ce qu'un VLAN ?
7. Comment fonctionne HTTPS ?

## Réponses flash

- **TCP vs UDP** → TCP = connexion, fiable, ordonné, handshake. UDP = sans connexion, rapide, sans garantie.
- **OSI pratique** → L2 (MAC/switch), L3 (IP/routage), L4 (ports TCP/UDP), L7 (HTTP/DNS).
- **DNS** → Nom → IP. Port 53. Cache → résolveur → racine → TLD → faisant autorité. TTL.
- **MAC vs IP** → MAC = physique, locale, change à chaque saut. IP = logique, routable, de bout en bout.
- **Hors réseau** → ET logique → table de routage → ARP de la passerelle → trame vers la passerelle.
- **VLAN** → Segmentation logique, domaines de diffusion isolés.
- **HTTPS** → HTTP + TLS : certificat vérifié, clé de session (ECDHE), chiffrement symétrique.
- **ARP** → IP → MAC en local. Risque : usurpation et interception.
- **Ports clés** → 22, 53, 80/443, 88, 389, 445, 3389.
