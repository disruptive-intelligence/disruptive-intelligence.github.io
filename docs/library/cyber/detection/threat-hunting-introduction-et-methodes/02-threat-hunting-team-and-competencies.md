---
title: Threat Hunting Team and Competencies
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting — introduction et méthodes.md
note: Threat hunting — introduction et méthodes
up:
- - Threat hunting — introduction et méthodes
  - index.md
---

Le Threat Hunting repose sur une équipe multidisciplinaire combinant des compétences en analyse des menaces, investigation, forensics, CTI et sécurité offensive.

L'objectif est de rechercher les menaces non détectées, comprendre leur fonctionnement et améliorer les capacités de détection de l'organisation.

## 1. Structure d'une Threat Hunting Team

| Rôle               | Responsabilités principales                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Threat Hunter      | Planifier et exécuter les hunts, analyser les comportements suspects, documenter les résultats                    |
| Incident Responder | Prendre en charge les menaces confirmées, coordonner le containment, l'éradication et la recovery                 |
| Malware Analyst    | Analyser les malwares, comprendre leurs fonctionnalités, identifier leurs comportements et artefacts              |
| Forensic Analyst   | Collecter et analyser les preuves numériques, reconstruire les actions de l'attaquant                             |
| Security Analyst   | Surveiller les systèmes/réseaux, analyser les événements de sécurité et contribuer à l'identification des menaces |

```
Threat Hunter
     ↓
Suspicious Activity Identified
     ↓
Investigation / Validation
     ├── Malware Analyst → Malware Behavior / IOCs
     ├── Forensic Analyst → Evidence / Timeline
     ├── Security Analyst → Logs / Correlation
     └── Incident Responder → Incident Handling
```


Ces rôles sont complémentaires, mais ne correspondent pas nécessairement à des postes distincts : selon la taille de l'organisation, une personne peut remplir plusieurs fonctions.

## 2. Positions et responsabilités

### Junior Threat Hunter

- Collecte et préparation des données.
    
- Analyse initiale des logs.
    
- Recherche d'IOCs et de comportements suspects.
    
- Assistance aux investigations.
    
- Documentation des résultats.
    

### Senior Threat Hunter

- Planification de hunts complexes.
    
- Analyse avancée des comportements adverses.
    
- Encadrement des analystes juniors.
    
- Coordination des investigations.
    
- Orientation des activités de Threat Hunting.
    

### Threat Intelligence Analyst

- Collecte et analyse du renseignement.
    
- Étude des Threat Actors, campagnes, outils et TTPs.
    
- Exploitation de sources CTI.
    
- Fourniture de renseignements utilisables pour orienter les hunts.
    

```
Threat Intelligence
→ Threat Actor / TTP Knowledge
→ Threat Hunting
```


### Red Team Member

- Simulation d'attaques réalistes.
    
- Reproduction de techniques offensives.
    
- Identification de vulnérabilités et de faiblesses.
    
- Recommandation de mesures défensives.
    

Complément pratique — Purple Teaming : la collaboration entre Red Team et défenseurs peut permettre de tester si les TTPs simulées sont effectivement visibles et détectées.

```
Red Team → Simulates TTPs
                 ↓
Threat Hunting / SOC → Investigates Visibility
                 ↓
Detection Gaps → Improvements
```


## 3. Compétences nécessaires

### Threat Analysis & Intelligence

- Comprendre les comportements des Threat Actors.
    
- Identifier les techniques et les outils utilisés.
    
- Utiliser MITRE ATT&CK pour analyser les TTPs.
    
- Évaluer la fiabilité et la pertinence des sources CTI.
    

### Network & System Knowledge

Connaissances approfondies de :

- protocoles et architectures réseau ;
    
- systèmes d'exploitation ;
    
- sécurité des applications ;
    
- fonctionnement des outils de sécurité.
    

Technologies mentionnées :

- IDS/IPS ;
    
- Firewall ;
    
- Antivirus.
    

Complément pratique : la maîtrise des logs, SIEM et EDR est également particulièrement utile pour rechercher et corréler des comportements suspects.

### Analytical Thinking & Problem-Solving

- Analyser des volumes importants de données.
    
- Identifier les anomalies et comportements inhabituels.
    
- Relier différents événements.
    
- Formuler des conclusions fondées sur les preuves.
    
- Résoudre efficacement des problèmes complexes.
    

Le Threat Hunting exige notamment de distinguer :

```
Anomaly
≠ Malicious Activity
≠ Confirmed Compromise
```


Une activité inhabituelle constitue une piste d'investigation, pas nécessairement une preuve d'intrusion.

### Communication & Reporting

- Documenter les investigations et résultats.
    
- Produire des rapports compréhensibles.
    
- Communiquer avec des interlocuteurs techniques et non techniques.
    
- Collaborer avec les autres équipes internes ou externes.
    

Un résultat de hunt doit pouvoir être transmis et exploité par les autres équipes de sécurité.

## 4. Certifications et formations

|Certification|Domaine principal|
|---|---|
|eCTHP — Certified Threat Hunting Professional|Méthodologies et techniques de Threat Hunting|
|GCIH — GIAC Certified Incident Handler|Incident Handling et analyse des techniques d'attaque|
|CTIA — Certified Threat Intelligence Analyst|Collecte et analyse de Threat Intelligence|
|CEH — Certified Ethical Hacker|Techniques offensives et compréhension des méthodes d'attaque|
|CISSP — Certified Information Systems Security Professional|Connaissances transversales en cybersécurité et gestion de la sécurité|

Ressources de formation continue citées :

- Plateformes : LetsDefend, Udemy.
    
- Conférences : Black Hat, DEF CON, SANS.
    
- Communautés professionnelles : ISACA, ISC2.
    

Ces certifications couvrent des domaines complémentaires : certaines sont spécialisées dans le Threat Hunting, tandis que d'autres apportent des compétences en Incident Response, CTI, sécurité offensive ou gouvernance.

## 5. Collaboration entre les équipes

Le Threat Hunting ne fonctionne pas de manière isolée.

```
Threat Intelligence Analyst
         ↓
Relevant Threat Information
         ↓
Threat Hunter
         ↓
Suspicious Findings
         ↓
Malware / Forensic Analysis
         ↓
Confirmed Threat?
         ↓
Incident Response
```


Les résultats peuvent également alimenter :

- les détections SOC ;
    
- les investigations futures ;
    
- l'amélioration des processus ;
    
- le partage de connaissances entre équipes.
    

Distinction essentielle : le Threat Hunter recherche proactivement des menaces non détectées, tandis que l'Incident Responder prend en charge la réponse opérationnelle lorsqu'un incident est identifié. Les deux fonctions peuvent collaborer tout au long d'une investigation.
