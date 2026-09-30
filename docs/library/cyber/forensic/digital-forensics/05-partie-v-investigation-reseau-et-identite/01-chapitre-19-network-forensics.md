---
title: Chapitre 19 — Network forensics
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie V — Investigation réseau ET identité
  - index.md
---

## 19.1 Ce que le réseau raconte

Le réseau est le terrain de jeu de l'attaquant pour la communication C2 (commandes envoyées au malware), le mouvement latéral (progression entre machines), et l'exfiltration (envoi des données volées vers l'extérieur). L'analyse réseau répond à des questions que le forensic endpoint seul ne peut pas couvrir : avec qui la machine compromise communique-t-elle ? quel volume de données a été transféré ? quels autres systèmes ont été contactés ?

## 19.2 Analyse PCAP avec Wireshark

Wireshark est l'outil de référence pour l'analyse de captures de paquets. Les filtres les plus utiles pour le forensic : `ip.addr == 103.xx.xx.xx` (isoler le trafic vers/depuis le C2), `http.request.method == POST` (identifier les données envoyées en HTTP — potentielle exfiltration), `dns.qry.name contains "suspect"` (résolutions DNS suspectes), `tcp.flags.syn == 1 && tcp.flags.ack == 0` (nouvelles connexions TCP — identifier les scans), et `tls.handshake.type == 1` (Client Hello — pour l'analyse JA3). La reconstruction de sessions TCP (`Follow TCP Stream`) permet de lire le contenu des communications non chiffrées. L'extraction de fichiers (`File > Export Objects > HTTP/SMB/...`) récupère les fichiers transférés via le réseau.

## 19.3 Détection de C2 et beaconing

Le beaconing est le pattern de communication le plus courant des malwares C2 : le malware contacte le serveur de l'attaquant à intervalles réguliers pour recevoir des instructions. La détection repose sur l'analyse statistique des intervalles de connexion : un processus qui contacte la même IP toutes les 30 minutes (± un jitter de 10 %) pendant 60 jours n'est pas un comportement humain — c'est un automate. L'outil **RITA** (Real Intelligence Threat Analytics, open source) automatise la détection de beaconing dans les logs Zeek. Les **fingerprints JA3/JA4** (hash de la négociation TLS Client Hello) identifient des clients TLS spécifiques même sur du trafic chiffré — le JA3 d'un RAT custom est différent de celui d'un navigateur Chrome.

## 19.4 Reconstruction de l'exfiltration

L'estimation du volume exfiltré est une question à laquelle le network forensics doit répondre. L'analyse des logs proxy (user-agent `rclone/v1.65.0`, volume cumulé vers des endpoints S3), des NetFlow (volume de données sortantes par destination), et des PCAP (si disponibles — extraction des fichiers transférés) permet de quantifier l'exfiltration. Le DNS tunneling est une technique d'exfiltration plus discrète — les données sont encodées dans les sous-domaines des requêtes DNS (`encoded-data.c2-domain.com`). La détection repose sur la longueur anormale des requêtes, l'entropie élevée des sous-domaines, et le volume de requêtes vers un même domaine.

## 19.5 Outils complémentaires

**Zeek** (ex-Bro) produit des logs structurés à partir du trafic réseau — conn.log (connexions), dns.log (requêtes DNS), http.log (requêtes HTTP), ssl.log (certificats TLS), files.log (fichiers transférés). Ces logs sont beaucoup plus faciles à analyser à grande échelle que les PCAP bruts. **NetworkMiner** (open source) extrait automatiquement les fichiers, les images, et les metadata des captures réseau. **Arkime** (ex-Moloch) est une plateforme de capture et d'analyse réseau à grande échelle, avec indexation full-text et interface web.

---
