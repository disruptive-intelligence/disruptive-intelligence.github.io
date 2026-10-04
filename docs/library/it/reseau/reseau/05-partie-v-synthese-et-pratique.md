---
title: Partie V — Synthèse et pratique
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - index.md
---

*Tout assembler sur un cas concret, puis savoir diagnostiquer quand ça ne marche pas.*

---


## Chapitre 19 — Du navigateur au site web : la vie d'une requête

On tape `https://www.example.com` dans le navigateur. Voici tout ce qui se passe, en reprenant les chapitres précédents.

### 19.1 Avant d'émettre : trouver l'adresse

1. **DNS** (Ch.10) — le système cherche `www.example.com` dans son cache et le fichier hosts, puis interroge son résolveur, qui remonte si besoin racine → `.com` → serveur faisant autorité. Réponse : `93.184.216.34`.
2. **Local ou distant ?** (Ch.5, 8) — `93.184.216.34 ET 255.255.255.0` ≠ `192.168.1.0` : la destination est distante, le paquet ira à la **passerelle** `192.168.1.1`.
3. **ARP** (Ch.8) — le poste obtient la MAC de la passerelle (cache ou requête ARP en broadcast).

### 19.2 Établir la connexion

4. **TCP** (Ch.4) — *three-way handshake* entre `192.168.1.10:51432` (port éphémère) et `93.184.216.34:443`.
5. **TLS** (Ch.14) — ClientHello, ServerHello, certificat vérifié, clés de session dérivées : le canal est chiffré.

### 19.3 Envoyer la requête

6. **HTTP** (Ch.11) — le navigateur construit `GET / HTTP/1.1`, `Host: www.example.com`, chiffré par TLS.
7. **Encapsulation** (Ch.3) — segment TCP (ports) → paquet IP (IP source `192.168.1.10`, destination `93.184.216.34`, TTL 128) → trame Ethernet (MAC source du poste, **MAC destination de la passerelle**).
8. **NAT** (Ch.7) — la box remplace l'IP source privée par son IP publique et note la correspondance.
9. **Routage** (Ch.8) — chaque routeur décapsule, consulte sa table, décrémente le TTL, réencapsule avec les MAC du saut suivant. L'IP de destination ne change pas ; les MAC changent à chaque saut.

### 19.4 Côté serveur et retour

10. Le serveur reçoit la trame, décapsule jusqu'au port **443**, où écoute le serveur web ; il déchiffre, traite la requête et renvoie `HTTP/1.1 200 OK` avec la page.
11. La réponse revient vers l'IP publique de la box et le **port éphémère** du client ; la box retraduit vers `192.168.1.10:51432`.
12. Le navigateur déchiffre, lit le HTML, puis émet d'autres requêtes pour les CSS, scripts et images — souvent sur la même connexion.

> **À retenir.** DNS donne l'adresse, ARP donne la MAC du prochain saut, TCP ouvre le canal, TLS le chiffre, HTTP porte la demande, IP l'achemine de routeur en routeur, et les ports remettent la réponse à la bonne application.

---


## Chapitre 20 — Diagnostiquer un problème réseau

### 20.1 La méthode : remonter les couches

On teste du bas vers le haut ; la première étape qui échoue localise la panne.

| Étape | Question | Linux | Windows |
|---|---|---|---|
| 1 — Interface | Ai-je une adresse, le bon masque, une passerelle ? | `ip a`, `ip route` | `ipconfig /all`, `route print` |
| 2 — Réseau local | La passerelle répond-elle ? Sa MAC est-elle connue ? | `ping <passerelle>`, `ip neigh` | `ping <passerelle>`, `arp -a` |
| 3 — Au-delà | Une IP externe répond-elle ? Où ça s'arrête ? | `ping 1.1.1.1`, `traceroute 1.1.1.1` | `ping 1.1.1.1`, `tracert 1.1.1.1` |
| 4 — Noms | Le nom se résout-il, et vers la bonne IP ? | `dig www.example.com`, `cat /etc/resolv.conf` | `Resolve-DnsName www.example.com`, `nslookup` |
| 5 — Port | Le service écoute-t-il, le flux est-il filtré ? | `nc -zv <hôte> 443`, `ss -tlnp` | `Test-NetConnection <hôte> -Port 443`, `netstat -ano` |
| 6 — Application | La réponse est-elle correcte ? | `curl -v https://<hôte>` | `curl.exe -v https://<hôte>`, `Invoke-WebRequest` |
| Capture | Que se passe-t-il vraiment sur le fil ? | `tcpdump -i eth0 -nn host <ip>` | Wireshark, `pktmon` |

### 20.2 Symptômes fréquents

| Symptôme | Piste |
|---|---|
| Adresse en `169.254.x.x` | Pas de réponse DHCP : câble, VLAN, serveur DHCP |
| Ping de la passerelle OK, Internet KO | Route par défaut, NAT, pare-feu en sortie |
| Accès par IP OK, par nom KO | DNS : serveurs configurés, fichier hosts, suffixe de domaine |
| Une machine du même switch injoignable | Masques différents (Ch.6.5), VLAN différent, pare-feu local |
| Connexion qui s'ouvre puis se fige sur les gros transferts | MTU / fragmentation (ICMP bloqué casse le PMTUD) |
| `Connection refused` immédiat | Port fermé : le service n'écoute pas (RST) |
| Délai d'attente sans réponse | Flux filtré par un pare-feu (paquets ignorés) |

### 20.3 Lire une capture

```bash
ping -c 4 8.8.8.8                       # quatre Echo Request
sudo tcpdump -i eth0 -nn icmp           # voir passer requêtes et réponses
```


![Ping et capture tcpdump correspondante](../../../assets/reseau-image-28.png)

Les commandes détaillées, avec exemples et sorties, sont dans les cheat sheets *Linux — Réseau* et *Windows — Réseau*.

---
