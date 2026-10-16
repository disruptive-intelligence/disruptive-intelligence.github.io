---
title: Threat Hunting Methodologies
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting — introduction et méthodes.md
note: Threat hunting — introduction et méthodes
up:
- - Threat hunting — introduction et méthodes
  - index.md
---

Les Threat Hunting Methodologies regroupent différentes approches permettant de rechercher proactivement des activités malveillantes qui n'ont pas été détectées par les contrôles de sécurité existants.

Principales méthodologies :

- Adversary-Centric : recherche basée sur les comportements et techniques des attaquants.
    
- Hypothesis-Driven : recherche guidée par une hypothèse de compromission.
    
- IOC-Based : recherche d'indicateurs techniques associés à des menaces connues.
    

Cette section se concentre sur l'approche Adversary-Centric.

## 1. Adversary-Centric Approach

L'approche Adversary-Centric consiste à étudier les attaques du point de vue de l'adversaire afin d'identifier les comportements qu'il pourrait reproduire dans notre environnement.

Objectifs :

- Comprendre les méthodes employées par les Threat Actors.
    
- Identifier leurs TTPs.
    
- Déterminer quelles techniques pourraient cibler l'organisation.
    
- Rechercher leurs traces dans les logs et la télémétrie de sécurité.
    
- Améliorer les capacités de détection des techniques identifiées.
    

```
Threat Actor / Campaign
         ↓
Identify TTPs
         ↓
Map to MITRE ATT&CK
         ↓
Identify Relevant Data Sources
         ↓
Hunt for Adversary Behaviors
         ↓
Validate Findings
```


Cette méthodologie s'appuie notamment sur :

- Threat Intelligence Reports ;
    
- analyses de campagnes historiques ;
    
- Malware Analysis ;
    
- MITRE ATT&CK ;
    
- renseignements sur les outils et infrastructures adverses.
    

L'intérêt est de rechercher des comportements associés à une menace, plutôt que de se limiter aux IOCs connus.

## 2. TTPs — Tactics, Techniques & Procedures

Les TTPs décrivent les objectifs, méthodes et implémentations concrètes des attaquants.

|Élément|Définition|Question|
|---|---|---|
|Tactic|Objectif tactique poursuivi|WHY|
|Technique|Méthode utilisée pour atteindre cet objectif|HOW|
|Sub-technique|Variante plus précise d'une technique|HOW, more specifically|
|Procedure|Implémentation concrète observée lors d'une attaque|HOW exactly|

### Exemple : Phishing

```
Tactic
→ Initial Access (TA0001)

Technique
→ Phishing (T1566)

Sub-technique
→ Spearphishing Attachment (T1566.001)

Procedure
→ Envoi d'un email contenant une pièce jointe
  malveillante spécifique
```


⚠️ Le phishing est une Technique dans MITRE ATT&CK, et non une Tactic. De même, l'utilisation d'un outil précis ne constitue une Procedure que lorsqu'elle décrit une implémentation concrète de la technique.

### Intérêt des TTPs dans le Threat Hunting

Les attaquants peuvent facilement modifier :

- leur infrastructure C2 ;
    
- les IP/domaines utilisés ;
    
- les hashes de leurs payloads.
    

Cependant, ils peuvent continuer à employer des comportements similaires :

- phishing ;
    
- credential dumping ;
    
- persistence ;
    
- lateral movement ;
    
- exfiltration.
    

```
New Malware Hash
+
New C2 Domain
+
Same Credential Dumping Technique
→ Behavioral Detection Still Relevant
```


La recherche basée sur les TTPs est donc généralement plus durable que celle reposant uniquement sur des IOCs.

## 3. MITRE ATT&CK Framework

MITRE ATT&CK est une base de connaissances documentant les comportements adverses observés.

Elle organise les attaques autour de :

- Tactics : objectifs de l'attaquant.
    
- Techniques : méthodes utilisées.
    
- Sub-techniques : variantes plus spécifiques.
    
- Procedures : exemples concrets d'utilisation par des Threat Actors.
    

Exemples :

|Tactic|Technique|
|---|---|
|Initial Access|Phishing — T1566|
|Execution|PowerShell — T1059.001|
|Persistence|Scheduled Task — T1053.005|
|Credential Access|OS Credential Dumping — T1003|
|Lateral Movement|Remote Services — T1021|

### Utilisation pour le Threat Hunting

Le Threat Hunter peut :

1. Identifier les techniques fréquemment utilisées par un Threat Actor.
    
2. Évaluer leur pertinence pour son environnement.
    
3. Déterminer quelles sources de télémétrie pourraient révéler ces techniques.
    
4. Rechercher des comportements correspondants.
    
5. Investiguer les résultats suspects.
    
6. Proposer de nouvelles détections en cas de lacunes.
    

Complément pratique — exemple de mapping :

|Technique|Sources de télémétrie possibles|
|---|---|
|PowerShell|Event IDs 4104, 4103, EDR|
|Scheduled Task|Security 4698, TaskScheduler/Operational|
|Remote Services / RDP|Security 4624 Type 10, TerminalServices logs|
|Credential Dumping|EDR, Sysmon Event ID 10 selon configuration|

La visibilité dépend toujours de la configuration des outils et de l'audit.

Attention : MITRE ATT&CK n'est pas un modèle strictement chronologique. Les Tactics représentent des objectifs et un attaquant peut employer plusieurs techniques simultanément ou revenir sur certaines activités.

## 4. Case Study — APT Attack

### Scénario

Un groupe state-sponsored mène une campagne APT contre une organisation pour voler des informations sensibles.

Déroulement :

```
Phishing Email
      ↓
Initial Access
      ↓
Backdoor Installation
      ↓
Persistence
      ↓
Lateral Movement
      ↓
Information Collection
      ↓
Exfiltration to Attacker Infrastructure
```


### Analyse des TTPs

|Activité observée|Interprétation|
|---|---|
|Email avec pièce jointe malveillante|Initial Access — Phishing|
|Installation d'une backdoor|Implantation d'un accès malveillant ; Persistence si un mécanisme de maintien d'accès est établi|
|Compromission d'autres machines|Lateral Movement|
|Collecte d'informations sensibles|Collection|
|Envoi des données vers un serveur contrôlé par l'attaquant|Exfiltration|

Sans détail sur les mécanismes techniques de la backdoor, du lateral movement ou de l'exfiltration, on ne peut pas les associer à des sub-techniques ATT&CK précises.

### Detection & Response

Le Threat Hunter peut rechercher les traces de ces comportements :

- Phishing : logs email, pièces jointes, exécution de processus suspects.
    
- Backdoor / Persistence : scheduled tasks, services, autoruns, connexions C2.
    
- Lateral Movement : authentifications inhabituelles, SMB, RDP, WinRM.
    
- Collection / Exfiltration : accès à des données sensibles, transferts réseau inhabituels.
    

Exemple de corrélation :

```
Suspicious Email
      ↓
Unexpected Process Execution
      ↓
Persistence Mechanism Created
      ↓
New Internal Connections
      ↓
Unusual Outbound Traffic
```


Cette séquence constitue une piste d'investigation plus solide que chacun des événements considéré isolément.

### Mesures défensives

À retenir notamment :

- sensibilisation au phishing ;
    
- détection des malwares ;
    
- surveillance du trafic réseau.
    

L'analyse des TTPs permet de cibler ces défenses en fonction des méthodes réellement employées par les attaquants.

## 5. Application opérationnelle

L'approche Adversary-Centric ne consiste pas à supposer qu'un groupe particulier est déjà présent. Elle consiste à utiliser ses comportements connus pour rechercher des activités similaires.

```
Threat Intelligence
→ Known Adversary TTPs
→ Hunt in Internal Telemetry
→ Suspicious Findings
→ Investigation
→ Detection Improvement
```


Deux résultats possibles :

- Activité suspecte identifiée : approfondir l'investigation et transmettre à l'Incident Response si une compromission est confirmée.
    
- Aucune activité identifiée : documenter le résultat et vérifier si les données disponibles permettent réellement de détecter la technique recherchée.
    

Absence de résultat ≠ absence de menace, notamment lorsque la télémétrie est incomplète.

L'approche Adversary-Centric permet donc d'utiliser les connaissances sur les Threat Actors et leurs TTPs pour orienter les hunts, vérifier la visibilité de l'organisation et améliorer les détections face aux comportements adverses connus.
