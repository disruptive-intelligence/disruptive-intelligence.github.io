---
title: Annexe G — Grilles d'évaluation et RACI
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

## Grille de gravité des incidents

| Niveau | Critères techniques | Critères métier | Exemples |
|--------|-------------------|----------------|----------|
| **P4 — Mineur** | 1-2 postes impactés, malware isolé, pas de mouvement latéral | Pas d'impact production, pas de données sensibles | Phishing bloqué, PUA détecté, malware contenu par AV |
| **P3 — Significatif** | Compromission confirmée sur quelques systèmes, mouvement latéral limité | Impact limité sur un service non critique | Compromission d'un compte utilisateur, malware avec C2 actif sur 2-3 postes |
| **P2 — Majeur** | Compromission de serveurs critiques, mouvement latéral étendu, exfiltration possible | Impact sur un service critique, données sensibles potentiellement exposées | Compromission de serveur de fichiers, accès admin non autorisé, exfiltration détectée |
| **P1 — Critique** | Compromission AD (DC, krbtgt), ransomware déployé, exfiltration massive | Production arrêtée, données sensibles confirmées exfiltrées, site OIV impacté | Ransomware à grande échelle, Golden Ticket, exfiltration R&D/RH |

## Grille de décision de confinement

| Situation | Confinement immédiat ? | Observation contrôlée possible ? | Critère de décision |
|-----------|----------------------|-------------------------------|-------------------|
| Ransomware en cours de déploiement | **OUI — immédiat** | NON | Chaque minute = machines chiffrées |
| Espionnage discret (attaquant non alerté) | Différé possible | **OUI — si l'attaquant ne sait pas** | Comprendre l'étendue avant de couper |
| Compromission de compte sans activité destructrice | **OUI — désactivation du compte** | NON | L'impact est limité et réversible |
| Exfiltration en cours | **OUI — blocage du canal** | Éventuellement, si plusieurs canaux suspectés | Arrêter la fuite est prioritaire |
| Compromission OT avec risque physique | **OUI — isolation IT/OT** | NON | La sécurité physique prime |

## Matrice RACI type — Réponse à incident

| Action | SOC | IR Lead | Forensic | RSSI | DSI | DG | Juridique | Communication | DPO |
|--------|-----|---------|----------|------|-----|-----|-----------|--------------|-----|
| Détection et escalade | **R** | I | | I | | | | | |
| Classification et triage | C | **R/A** | C | I | | | | | |
| Décision de confinement | | **R** | C | **A** | I | I | | | |
| Collecte forensic | | C | **R** | I | | | | | |
| Investigation technique | | **A** | **R** | I | C | | | | |
| Notification ANSSI | | C | | **R/A** | | I | C | | |
| Notification CNIL | | C | | C | | I | C | | **R/A** |
| Communication interne | | I | | C | C | **A** | C | **R** | |
| Communication externe | | I | | C | | **A** | C | **R** | |
| Décision rançon | | C | | C | C | **A** | **R** | C | |
| Dépôt de plainte | | C | C | C | | I | **R/A** | | |
| RETEX | C | **R** | C | **A** | C | I | I | I | I |

R = Responsible (exécute), A = Accountable (valide), C = Consulted, I = Informed.

---

---
