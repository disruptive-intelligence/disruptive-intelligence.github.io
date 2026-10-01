---
title: 'Chapitre 3 — Sécurité réseau : firewalls, segmentation et détection'
source: IT/06 Infrastructure & architecture/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

Les **firewalls** en profondeur : le firewall **stateless** filtre chaque paquet indépendamment (ACL basique sur IP/port — rapide mais limité), le firewall **stateful** suit les connexions (autorise les réponses aux requêtes initiées de l'intérieur), et le **NGFW** (Next-Generation Firewall) ajoute l'inspection applicative (filtrage URL, IPS intégré, inspection TLS, sandboxing — Palo Alto, Fortinet, Check Point). Politique de filtrage : **deny by default** — tout ce qui n'est pas explicitement autorisé est bloqué. Les règles de firewall (ordre — les règles sont évaluées séquentiellement, la première qui match s'applique ; logging — chaque règle de deny doit logger ; revue périodique — les règles obsolètes s'accumulent et créent des trous).

La **segmentation réseau** est le contrôle de sécurité le plus fondamental contre le mouvement latéral. VLANs (séparation logique au niveau 2 — utilisateurs, serveurs, admin, OT, guest, chaque VLAN dans son sous-réseau), sous-réseaux (séparation au niveau 3 avec filtrage inter-sous-réseaux par le firewall), et micro-segmentation (filtrage au niveau de chaque workload — NSG en cloud, Network Policies en Kubernetes). Pourquoi le flat network est un cadeau pour l'attaquant : sans segmentation, un ransomware ou un attaquant qui compromet un poste utilisateur peut atteindre directement le DC, le vCenter, les sauvegardes, et l'OT — tout le blast radius est maximal.

Les **IDS/IPS** (Intrusion Detection/Prevention System) : network-based (Snort, Suricata — analyse du trafic réseau) et host-based (OSSEC, Wazuh — analyse des logs et de l'intégrité). Détection par signatures (patterns connus — rapide mais aveugle aux attaques nouvelles) vs par anomalies (baseline comportementale — détecte l'inconnu mais génère des faux positifs). Le **NDR** (Network Detection and Response) analyse le trafic réseau de manière comportementale — détection de beaconing C2, mouvement latéral, exfiltration. Le **802.1X** (NAC — Network Access Control) authentifie les postes avant de leur accorder l'accès réseau — un poste non connu est placé dans un VLAN de quarantaine.

---
