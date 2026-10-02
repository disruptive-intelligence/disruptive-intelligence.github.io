---
title: Chapitre 1 — Modèle client-serveur, TCP/IP et protocoles fondamentaux
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

## 1.1 Le modèle client-serveur

Presque toute l'informatique d'entreprise repose sur un principe simple : un client demande, un serveur répond. Le navigateur web (client) envoie une requête HTTP au serveur web. L'application mobile (client) appelle une API (serveur). Le poste de travail (client) demande un ticket Kerberos au contrôleur de domaine (serveur). En investigation, on cherche toujours « qui a demandé quoi à qui ». En pentest, on cherche à envoyer des requêtes malformées pour obtenir une réponse inattendue.

## 1.2 TCP/IP

Tous les échanges réseau passent par la pile TCP/IP. **IP** (Internet Protocol) assure l'adressage des machines — IPv4 (192.168.1.10), IPv6 (2001:db8::1). **TCP** (Transmission Control Protocol) assure un transport fiable avec connexion en 3 étapes (SYN, SYN-ACK, ACK), garantit l'arrivée et l'ordre des données — utilisé par HTTP, SSH, SMTP, SQL. **UDP** (User Datagram Protocol) assure un transport rapide sans garantie — utilisé par DNS, SNMP, syslog, streaming. Les **ports** (0-65535) identifient le service sur une machine : HTTP=80, HTTPS=443, SSH=22, DNS=53, SMTP=25. Règle : un service qui écoute sur un port = une surface d'attaque. Moins de ports ouverts = moins de risque.

## 1.3 HTTP/HTTPS

HTTP est le protocole du web. Chaque requête a une méthode (GET — récupérer, POST — créer/envoyer, PUT — remplacer, DELETE — supprimer, PATCH — modifier partiellement, OPTIONS — lister les méthodes autorisées), un chemin, des headers, et éventuellement un body. Les codes de retour essentiels en sécurité : 200 OK, 301/302 redirection (open redirect → phishing), 401 Unauthorized (pas authentifié), 403 Forbidden (authentifié mais pas autorisé), 404 Not Found, 500 Internal Server Error (peut révéler des infos en mode debug).

**Cookies et sessions :** HTTP est stateless — chaque requête est indépendante. Pour « se souvenir » de l'utilisateur, le serveur envoie un cookie (Set-Cookie: session_id=abc123) que le navigateur renvoie à chaque requête. Ce cookie est la clé de la session — le voler (XSS) revient à voler l'identité de l'utilisateur.

## 1.4 TLS

HTTPS = HTTP + TLS. TLS chiffre le trafic entre le client et le serveur. Le serveur prouve son identité avec un **certificat** signé par une autorité de certification (CA). Le navigateur vérifie la chaîne de confiance. Ce que TLS fait : chiffrer en transit, authentifier le serveur. Ce que TLS ne fait PAS : protéger les données sur le serveur, authentifier l'utilisateur, empêcher les vulnérabilités applicatives.

## 1.5 DNS en profondeur

Le DNS traduit les noms de domaine en adresses IP — c'est l'annuaire d'Internet. Les types d'enregistrement : **A/AAAA** (nom → IP), **CNAME** (alias), **MX** (serveur mail), **TXT** (métadonnées — SPF, DKIM, DMARC, vérification de propriété), **CAA** (quelles CA peuvent émettre des certificats), **NS** (serveurs DNS autoritaires), **PTR** (reverse DNS, IP → nom).

Le TXT est le couteau suisse du DNS : SPF (qui peut envoyer des mails pour ce domaine), DKIM (signature cryptographique des mails), DMARC (politique anti-spoofing), vérification de propriété (Google, Microsoft, Let's Encrypt).

Par défaut, les requêtes DNS sont en clair — un attaquant sur le réseau voit tous les domaines visités. DNS-over-HTTPS (DoH) et DNS-over-TLS (DoT) chiffrent les requêtes. Le DNS est aussi utilisé pour l'exfiltration de données (DNS tunneling — données encodées dans les sous-domaines) et comme canal C2 par les APT (cf. cours APT Ch.3).

## 1.6 Fil rouge — BACKBONE : la cartographie protocolaire

> **🔧 BACKBONE — Épisode 1**
>
> Lucas lance un scan Nmap sur les plages IP de CargoPlex. Résultat : 47 services écoutent sur Internet (dont FTP 21 en clair, un vCenter 443 accessible, un Elasticsearch 9200 sans authentification, et 3 interfaces iLO/iDRAC en HTTPS avec credentials par défaut). 12 de ces services ne sont pas nécessaires et sont des surfaces d'attaque gratuites.

---
