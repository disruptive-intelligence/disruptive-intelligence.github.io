---
title: Chapitre 4 — TCP et UDP
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 4.1 Deux philosophies

| | **TCP** | **UDP** |
|---|---|---|
| Connexion | Orienté connexion (établissement préalable) | Sans connexion |
| Fiabilité | Livraison garantie, ordonnée, retransmission des pertes | Aucune garantie |
| Contrôle | Numéros de séquence, acquittements, contrôle de flux (fenêtre) | Aucun |
| En-tête | 20 à 60 octets | 8 octets |
| Vitesse | Plus lent | Plus rapide |
| Usages | Web, SSH, messagerie, transferts de fichiers | DNS, VoIP, streaming, jeux, DHCP |

TCP numérote chaque octet envoyé ; le récepteur acquitte en indiquant le prochain octet attendu. Une perte ou un doublon est ainsi détecté et corrigé.

## 4.2 L'établissement : le *three-way handshake*

```text
Client                         Serveur
  │ ── SYN (seq = x) ───────────▶ │   « je veux ouvrir une connexion »
  │ ◀──── SYN-ACK (seq = y, ack = x+1) │   « d'accord, voici mon numéro »
  │ ── ACK (ack = y+1) ─────────▶ │   « bien reçu » : connexion établie
```


Chaque côté choisit un numéro de séquence initial aléatoire ; le handshake les synchronise.

![Three-way handshake capturé dans Wireshark](../../../../assets/reseau-three-way-handshake.png)

## 4.3 La fermeture

Fermeture propre : chaque côté envoie un **FIN** et acquitte celui de l'autre (FIN/ACK → FIN/ACK → ACK). Un **RST** coupe brutalement la connexion.

![Fermeture d'une session TCP](../../../../assets/reseau-session-teardown.png)

| Flag | Notation tcpdump | Sens |
|---|---|---|
| SYN | `[S]` | Ouverture |
| ACK | `[.]` | Acquittement |
| PSH | `[P]` | Données à remettre immédiatement |
| FIN | `[F]` | Fin propre |
| RST | `[R]` | Coupure brutale — fréquente lors d'un scan de ports ou d'un refus de connexion |
| URG | `[U]` | Données urgentes (rare) |

## 4.4 Ports et sockets

Un **port** identifie le processus destinataire sur la machine. Un **socket** est la combinaison `IP:port` (ex. `192.168.1.10:443`) ; une connexion TCP est identifiée par la paire de sockets client et serveur.

| Plage | Nom | Usage |
|---|---|---|
| 0 – 1023 | Ports connus (*well-known*) | Services standard attribués par l'IANA : 22 SSH, 53 DNS, 80 HTTP, 443 HTTPS |
| 1024 – 49151 | Ports enregistrés | Applications enregistrées auprès de l'IANA : 1433 SQL Server, 3306 MySQL, 3389 RDP |
| 49152 – 65535 | Ports dynamiques (éphémères) | Choisis par le système du client pour chaque connexion, libérés ensuite |

Dans un flux, on voit donc presque toujours `client:49xxx → serveur:443`, puis la réponse en sens inverse. La liste des ports à connaître est en Annexe A.

---
