---
title: Chapitre 7 — Acquisition réseau et captures de trafic
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie II — Acquisition de preuves
  - index.md
---

## 7.1 Quand et comment capturer du trafic

La capture de trafic réseau en temps réel n'est possible que si l'infrastructure le permet (port mirroring sur le switch, TAP réseau, ou NDR déployé). En forensic, la capture se fait rarement au moment de l'incident initial (on n'avait pas prévu de capturer) — on travaille plus souvent avec les logs réseau existants (proxy, pare-feu, DNS, VPN) et les captures historiques du NDR si disponible.

Si une capture live est possible, **tcpdump** est l'outil en ligne de commande de référence : `tcpdump -i eth0 -w capture.pcap -c 1000000` capture un million de paquets sur l'interface eth0. **Wireshark** offre une interface graphique pour la capture et l'analyse. **Zeek** (ex-Bro) ne capture pas les paquets bruts mais produit des logs structurés (connexions, requêtes DNS, requêtes HTTP, certificats TLS) beaucoup plus faciles à analyser à grande échelle.

Les captures doivent être filtrées par pertinence : capturer tout le trafic d'un réseau de 10 Gbit/s produit des téraoctets de données en quelques heures — inutilisable. Les filtres utiles : par IP suspecte (connue C2), par port (443 sortant vers des destinations inhabituelles), par machine source (la machine compromise), ou par protocole (DNS pour le tunneling, HTTP/HTTPS pour le C2).

## 7.2 Logs réseau existants

En pratique, les logs existants sont la source réseau principale. Les **logs proxy** (Squid, Zscaler, Blue Coat) contiennent les URLs visitées, les user-agents, les volumes de données, et les codes de retour HTTP — essentiels pour identifier l'exfiltration et le C2 web. Les **logs pare-feu** (Palo Alto, Fortinet, Check Point) contiennent les flux autorisés et refusés avec IP source, IP destination, port, protocole, et volume — essentiels pour identifier les communications inhabituelles. Les **logs DNS** (Infoblox, BIND, Windows DNS) contiennent les résolutions de domaine — essentiels pour identifier les domaines DGA, le DNS tunneling, et les résolutions vers des C2. Les **logs VPN** contiennent les connexions avec géolocalisation, horodatage, et durée — essentiels pour identifier les accès compromis.

Les **NetFlow** (métadonnées de flux réseau sans le contenu des paquets : source, destination, port, volume, durée) sont une source intermédiaire entre les logs et le PCAP — moins détaillée que le PCAP mais disponible en rétention longue et à grande échelle.

## 7.3 Fil rouge — MUSIC BOX : les logs réseau

> **🔬 MUSIC BOX — Épisode 7**
>
> NovaPharma n'a pas de NDR ni de capture PCAP historique. Les sources réseau disponibles sont le proxy Squid (6 mois de rétention), le pare-feu Palo Alto (12 mois), le DNS Infoblox (3 mois), et le VPN Fortinet (12 mois). Claire demande à l'IT d'exporter immédiatement ces logs vers le stockage forensic — avant que la rotation ne les efface.
>
> Premier résultat du proxy : le poste WKS-RD-047 a des connexions HTTPS régulières vers `103.xx.xx.xx:443` toutes les 30 minutes (pattern de beaconing) depuis 60 jours. Le user-agent est `Mozilla/5.0 NovaPharma` — l'attaquant a personnalisé le user-agent de son RAT.

---
