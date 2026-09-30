---
title: Partie 3 — Réseau et TCP
source: IT/Culture/Fiche_How-The-Web-Works.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
---

## 8. Avant HTTP : réseau, IP, ARP, gateway et encapsulation

### À retenir
HTTP ne flotte pas dans le vide : il repose sur **plusieurs couches réseau** en dessous.

### Comment ça fonctionne

1. Le navigateur **génère** la requête HTTP.
2. Elle est **encapsulée** dans TCP (port 80 ou 443), lui-même dans un paquet IP portant l'**IP destination**.
3. Sur le **réseau local**, la machine utilise **ARP** pour trouver l'**adresse MAC de la gateway** (le routeur).
4. La trame part vers le routeur, qui **transfère** le paquet selon l'IP destination.
5. Les routeurs intermédiaires **font suivre** de proche en proche.
6. Le serveur reçoit le paquet et l'oriente vers le **port applicatif** (80/443).
7. La réponse revient vers le **port source temporaire** du client (choisi aléatoirement par l'OS).

### Pourquoi c'est important en cyber
ARP est lui-même attaquable (**ARP spoofing** → MiTM local). Comprendre l'encapsulation explique pourquoi une capture réseau voit des couches empilées (Ethernet → IP → TCP → HTTP).

### Point clé à mémoriser
HTTP s'appuie sur IP + ARP + routage. Le client écoute sur un port temporaire ; le serveur, sur 80/443.

---

## 9. TCP : établir la connexion

### À retenir
HTTP et HTTPS utilisent classiquement **TCP**, qui garantit une connexion fiable avant tout échange applicatif.

### Comment ça fonctionne

- **HTTP = port 80**, **HTTPS = port 443**.
- Le client utilise un **port source temporaire** (éphémère).
- **Handshake TCP en 3 étapes** :

```
Client  ──── SYN ───▶  Serveur
Client  ◀── SYN-ACK ─  Serveur
Client  ──── ACK ───▶  Serveur
```


Après ce handshake, les **données applicatives** (HTTP, ou TLS si HTTPS) peuvent circuler.

### Pourquoi c'est important en cyber
Le handshake TCP est la base du **scan de ports** (un SYN-ACK = port ouvert). Comprendre l'état de connexion aide à lire Wireshark et à interpréter les scans Nmap.

### Point clé à mémoriser
SYN → SYN-ACK → ACK, puis les données circulent. Port 80 HTTP, 443 HTTPS, port source client temporaire.

---
