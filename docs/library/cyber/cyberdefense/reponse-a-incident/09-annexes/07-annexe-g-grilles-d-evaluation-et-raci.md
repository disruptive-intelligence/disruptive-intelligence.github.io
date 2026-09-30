---
title: Annexe G — Grilles d'évaluation et RACI
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

##### Grille de gravité des incidents

| Niveau | Critères techniques | Critères métier | Exemples |
|--------|-------------------|----------------|----------|
| **P4 — Mineur** | 1-2 postes impactés, malware isolé, pas de mouvement latéral | Pas d'impact production, pas de données sensibles | Phishing bloqué, PUA détecté, malware contenu par AV |
| **P3 — Significatif** | Compromission confirmée sur quelques systèmes, mouvement latéral limité | Impact limité sur un service non critique | Compromission d'un compte utilisateur, malware avec C2 actif sur 2-3 postes |
| **P2 — Majeur** | Compromission de serveurs critiques, mouvement latéral étendu, exfiltration possible | Impact sur un service critique, données sensibles potentiellement exposées | Compromission de serveur de fichiers, accès admin non autorisé, exfiltration détectée |
| **P1 — Critique** | Compromission AD (DC, krbtgt), ransomware déployé, exfiltration massive | Production arrêtée, données sensibles confirmées exfiltrées, site OIV impacté | Ransomware à grande échelle, Golden Ticket, exfiltration R&D/RH |

##### Grille de décision de confinement

| Situation | Confinement immédiat ? | Observation contrôlée possible ? | Critère de décision |
|-----------|----------------------|-------------------------------|-------------------|
| Ransomware en cours de déploiement | **OUI — immédiat** | NON | Chaque minute = machines chiffrées |
| Espionnage discret (attaquant non alerté) | Différé possible | **OUI — si l'attaquant ne sait pas** | Comprendre l'étendue avant de couper |
| Compromission de compte sans activité destructrice | **OUI — désactivation du compte** | NON | L'impact est limité et réversible |
| Exfiltration en cours | **OUI — blocage du canal** | Éventuellement, si plusieurs canaux suspectés | Arrêter la fuite est prioritaire |
| Compromission OT avec risque physique | **OUI — isolation IT/OT** | NON | La sécurité physique prime |

##### Matrice RACI type — Réponse à incident

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


## Annexe — Exemples de causes d’incidents réels (fiche HTB)


### Fuites d'identifiants - Credentials compromis

#### Rançongiciel contre Colonial Pipeline

- Le Colonial Pipeline, un important système d'oléoducs américain, a été victime d'une attaque par rançongiciel (ransomware).
- Cette [attaque](https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack) provenait d'un MDP personnel d'un employé qui avait été compromis, probablement trouvé sur le dark web, plutôt que d'une attaque directe sur le réseau de l'entreprise.
- Les attaquants ont accédé aux systèmes de l'entreprise en utilisant un mot de passe compromis pour un compte VPN inactif, qui n'avait pas la MFA activée.

```
- Compromission d’un compte VPN.
- Password compromis.
- Compte inactif.
- MFA non activée.

Compromised Password
+
No MFA
→ VPN Access
→ Incident
```


### Identifiants faibles / par défaut

#### Botnet Mirai (2016)

- Botnet Mirai scan d’équipements IoT utilisant des identifiants d'usine ou par défaut
- Les appareils compromis sont intégrés dans un botnet DDoS massif.
- La cause première était que les appareils étaient livrés avec des identifiants par défaut non modifiés.

#### Incident LogicMonitor (2023)

- Certains comptes clients avait été fournis avec des MDP par défaut faibles.
- Les clients concernés ont subi des incidents de rançongiciel consécutifs ou des accès non autorisés.
- Conséquences :
    - accès non autorisé ;
    - ransomware pour certains clients.

### Logiciels obsolètes / systèmes non patchés

#### Fuite de données d'Equifax — 2017

- Exploitation d'une vuln Apache Struts (CVE-2017-5638) dans l'application web d'Equifax.
- Le correctif était disponible mais n’avait pas été appliqué à temps.
- Résultat :
    - fuite massive de données personnelles.
    - Cette faille a exposé les données personnelles d'environ 143 à 147 millions de personnes, entraînant des conséquences réglementaires et juridiques majeures.

#### WannaCry — 2017

- Ransomware avec propagation de type worm en utilisant l'exploit SMB EternalBlue.
- Exploit :

```
EternalBlue
→ SMB
→ MS17-010
```

- Plus de 200 000 systèmes affectés dans plus de 150 pays.
- Cet incident était dû à des systèmes Windows non corrigés, bien que le correctif MS17-010 ait été disponible avant l'épidémie.

### Menace interne - Insider Threat

#### CCash App / Block Inc. (Divulgation en 2021 ; Avis public en 2022)

- Un ancien employé a accédé aux informations personnelles de millions d'utilisateurs de Cash App.
- Environ 8,2 millions de clients actuels et anciens ont été potentiellement touchés, ce qui a entraîné un examen réglementaire et des règlements.
- Cause principale :
    - abus d’un accès légitime ;
    - contrôles internes insuffisants ;
    - monitoring insuffisant.

```
Legitimate Access
→ Misuse
→ Data Exposure
```


### Phishing / Social Engineering

- Le phishing peut servir à :
    - voler des credentials ;
    - délivrer un malware ;
    - obtenir un foothold ;
    - faciliter la fraude.

#### Attaque par hameçonnage du Département de l'Intérieur des États-Unis

- Les attaquants ont utilisé une technique de "evil twin" pour inciter les individus à se connecter à un faux Wi-Fi, permettant aux pirates de voler des identifiants et d'accéder au réseau
- Cet incident a révélé un manque d'infrastructure de réseau sans fil sécurisée et des mesures de sécurité insuffisantes, notamment une authentification utilisateur faible et des tests de réseau inadéquats.

#### Twitter — 2020

- Compromission de comptes à forte visibilité pour promouvoir une arnaque au bitcoin.
 - Accès aux outils d'administration de Twitter, leur permettant de modifier les comptes et de publier directement des tweets.
- Social engineering contre des employés.

### Supply Chain Attack

#### SolarWinds Orion — 2020

- Compromission, par acteurs étatiques, de l’environnement de build/publication.
- Backdoor ajoutée aux updates Orion.
- Distribution à des milliers de clients de la mise à jour compromise à de nombreux clients.
- Cela a provoqué un espionnage et un accès non autorisé à grande échelle dans les secteurs gouvernemental et privé

```
Vendor Compromise
→ Malicious Update
→ Customers Install Update
→ Widespread Access
```


---



## Annexe — Questions types d'entretien et réponses types
