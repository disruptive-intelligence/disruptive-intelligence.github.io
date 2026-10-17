---
title: Incident Detection and Response with EDR
source: Cyber/04 Forensic/DFIR avec l'EDR.md
note: DFIR avec l'EDR
up:
- - DFIR avec l'EDR
  - index.md
---

Les solutions EDR (Endpoint Detection & Response) jouent un rôle essentiel dans les opérations de Digital Forensics & Incident Response (DFIR).

Elles permettent de collecter la télémétrie des endpoints, de détecter les activités potentiellement malveillantes et d'appliquer des mesures de réponse.

Trois capacités principales :

|Fonction|Objectif|
|---|---|
|Telemetry Collection|Collecter les logs, processus, connexions réseau et événements système|
|Incident Detection|Identifier les menaces connues ou suspectes|
|Incident Response|Contenir et neutraliser les activités malveillantes|

Ces fonctions facilitent l'investigation, l'analyse des causes racines et la réduction du temps de réponse aux incidents.

## 1. Incident Detection

L'Incident Detection consiste à identifier rapidement les menaces et événements de sécurité pouvant affecter une organisation.

### Detection Methods

|Méthode|Fonctionnement|
|---|---|
|Signature-Based Detection|Recherche des signatures et caractéristiques de menaces connues|
|Behavioral Detection|Analyse des comportements des utilisateurs, processus et systèmes|
|Anomaly-Based Detection|Identification des écarts par rapport à une activité considérée comme normale|

#### Signature-Based Detection

Cette méthode repose sur des bases de signatures permettant de reconnaître des malwares et techniques d'attaque déjà identifiés.

Elle nécessite une mise à jour régulière des signatures.

#### Behavioral Detection

Elle examine les comportements observés sur les endpoints pour identifier des activités potentiellement malveillantes, notamment lorsque les signatures traditionnelles sont insuffisantes.

#### Anomaly-Based Detection

Elle recherche des comportements inhabituels dans les activités système, utilisateur ou réseau.

Elle peut contribuer à identifier des menaces nouvelles ou inconnues, notamment certaines attaques zero-day.

Une anomalie ou une détection comportementale ne constitue toutefois pas, à elle seule, une preuve de compromission.

## 2. SentinelOne — Detection Engines

SentinelOne utilise plusieurs moteurs spécialisés pour analyser différents types de menaces.

|Detection Engine|Fonction|
|---|---|
|Reputation|Évalue la réputation des fichiers et applications à partir de sources de sécurité|
|Static AI|Analyse la structure et le contenu des fichiers sans nécessiter leur exécution|
|Static AI — Suspicious|Identifie les fichiers présentant des caractéristiques statiques suspectes|
|Behavioral AI — Executables|Surveille le comportement des exécutables pendant leur activité|
|Documents / Scripts|Détecte les activités malveillantes associées aux documents, macros et scripts|
|Lateral Movement|Recherche les activités compatibles avec une progression entre systèmes du réseau|
|Anti-Exploitation / Fileless|Détecte certaines techniques d'exploitation et activités malveillantes en mémoire|
|Potentially Unwanted Applications (PUA)|Identifie les applications potentiellement indésirables|
|Detect Interactive Threats|Recherche des comportements associés aux menaces interactives et aux actions manuelles d'attaquants|

### Complémentarité des moteurs

Les moteurs de SentinelOne combinent plusieurs approches :

- Reputation Analysis : identification à partir d'informations de réputation.
    
- Static Analysis : examen des caractéristiques d'un fichier.
    
- Behavioral Analysis : observation des actions effectuées.
    
- Attack Technique Detection : recherche de comportements associés à des techniques d'attaque.
    

Cette combinaison permet d'élargir la couverture de détection aux menaces connues et à certaines menaces inconnues.

Les moteurs disponibles et leur fonctionnement précis peuvent varier selon la version et la configuration de SentinelOne.

## 3. Incident Response avec EDR

Lorsqu'une menace est identifiée, les capacités de réponse EDR permettent de limiter son impact et de soutenir les investigations.

Plusieurs opérations successives.

### Isolation

L'Isolation consiste à empêcher une menace ou un endpoint compromis de poursuivre certaines interactions.

Exemples :

- isoler un endpoint du réseau ;
    
- arrêter un processus suspect ;
    
- limiter la propagation d'un malware.
    

### Containment

Le Containment vise à réduire les dommages réels ou potentiels de l'incident.

Il peut comprendre :

- la prévention de fuites de données ;
    
- la restriction des accès utilisateurs ;
    
- la sécurisation des données critiques ;
    
- le confinement des systèmes compromis.
    

L'isolation constitue donc une mesure possible de confinement, tandis que le containment représente l'objectif plus général de limitation de l'incident.

### Telemetry Data Collection

Collecter rapidement les informations pertinentes pour l'investigation :

- System Logs ;
    
- User Reports ;
    
- Network Traffic ;
    
- autres événements disponibles sur les endpoints.
    

### In-Depth Analysis

Analyser le déroulement de l'incident pour déterminer :

- le point d'entrée de l'attaque ;
    
- la méthode de compromission ;
    
- les systèmes affectés ;
    
- les éventuels mécanismes de propagation.
    

### Root Cause Analysis

Identifier les causes ayant permis la compromission afin de réduire les risques de récidive.

### Remediation & Recovery

Appliquer les mesures nécessaires pour neutraliser la menace et restaurer les opérations.

### System Optimization

Mettre à jour les systèmes et appliquer les correctifs permettant de traiter les faiblesses identifiées.

### Prevention of Future Incidents

Renforcer la sécurité par :

- l'amélioration des policies ;
    
- l'évolution des procédures ;
    
- la formation des utilisateurs ;
    
- l'évaluation continue des risques.
    

## 4. SentinelOne — Automated & Manual Response

SentinelOne permet de configurer des actions automatiques à travers les Security Policies, mais également d'effectuer des réponses manuelles depuis la console.

### Manual Response Actions

|Action|Fonction|
|---|---|
|Kill & Quarantine|Arrêter le processus concerné et mettre le fichier en quarantaine|
|Add Blacklist|Ajouter un élément aux mécanismes de blocage définis par le produit|
|Apply Exclusion|Exclure un élément de certaines détections ou protections|
|Isolate from Network|Isoler l'endpoint pour limiter ses communications réseau|

### Automated vs Manual Response

#### Automated Response

Les actions sont déclenchées automatiquement lorsque les conditions prévues par la policy sont satisfaites.

#### Manual Response

Un analyste examine la détection et décide des actions adaptées à la situation.

Points de vigilance

- Une détection ne signifie pas nécessairement que l'EDR a bloqué la menace.
    
- Quarantine ne garantit pas la suppression complète d'une compromission.
    
- Network Isolation peut perturber les services légitimes de l'endpoint.
    
- Apply Exclusion ne constitue pas une action d'éradication : elle peut réduire la couverture de sécurité et doit être utilisée avec précaution.
    

L'intérêt de ces mécanismes est de permettre aux équipes DFIR de choisir entre une intervention automatisée et une réponse contrôlée par l'analyste.

## 5. Digital Forensics

Le Digital Forensics consiste à collecter, examiner, analyser et préserver les preuves numériques associées à un incident.

Son objectif est de comprendre les événements survenus et de conserver des éléments exploitables pour les investigations, y compris dans un éventuel contexte judiciaire.

On distingue principalement :

- Forensic Data Collection
    
- Timeline Analysis
    
- Forensic Evidence Preservation
    

## 6. Collecte de données forensic

La collecte forensic consiste à récupérer les données pertinentes d'un incident de manière fiable et contrôlée.

### EDR Data Collection

Les EDR peuvent fournir des informations sur :

|Donnée|Intérêt forensic|
|---|---|
|Malware Activity|Identifier les activités malveillantes observées|
|User Commands|Examiner les commandes exécutées|
|System Changes|Retrouver les modifications effectuées sur le système|
|Process Events|Reconstituer les exécutions de programmes|
|Network Activity|Examiner certaines communications liées à l'incident|

Ces informations permettent de déterminer comment et quand certaines activités se sont produites.

### Data Collection Techniques
#### Memory Dumps

Capture de la mémoire vive afin d'examiner les informations présentes en mémoire au moment de l'acquisition.

#### Network Traffic Capture

Collecte de trafic réseau pour analyser les communications associées à l'incident.

#### Log File Storage

Conservation des journaux pertinents pour permettre leur analyse ultérieure.

La disponibilité de ces capacités dépend de l'EDR utilisé et des outils de collecte complémentaires.

### Timeline Analysis

La reconstruction chronologique permet de replacer les événements dans leur ordre d'apparition afin d'étudier le déroulement de l'attaque.

```
Suspicious Activity Detected
             ↓
      Collect EDR Data
             ↓
     Correlate Events
             ↓
     Build Attack Timeline
             ↓
      Forensic Analysis
```


## 7. Préservation des Preuves Forensiques

La préservation des preuves numériques vise à maintenir leur intégrité, leur fiabilité et leur recevabilité éventuelle dans une procédure judiciaire.

### Evidence Integrity

Les preuves doivent être conservées sans altération non documentée.

Notamment :

- Hashing : calcul d'empreintes pour vérifier l'intégrité.
    
- Sealing / Signing : mécanismes permettant de protéger ou attester les preuves.
    
- Secure Storage : stockage sécurisé des éléments collectés.
    

Le hash permet de vérifier qu'un élément n'a pas été modifié entre deux contrôles, mais ne prouve pas à lui seul son origine ou l'intégralité de son historique.

### Legal Requirements

Les preuves numériques doivent être collectées, conservées et présentées conformément aux exigences légales applicables.

Cela implique de documenter les étapes de l'analyse et les opérations réalisées sur les preuves.

### Chain of Custody

La Chain of Custody désigne la traçabilité de la collecte, du transfert, de la conservation et de la manipulation des preuves.

Elle permet notamment de documenter :

- l'identité de la personne ayant collecté les éléments ;
    
- la date et les circonstances de collecte ;
    
- les transferts et accès aux preuves ;
    
- les opérations effectuées pendant l'investigation.
    

Cette traçabilité contribue à préserver la crédibilité et la valeur probante des éléments forensic.

## 8. Workflow — Incident Detection, Response & Forensics

```
EDR Telemetry Collection
          ↓
    Incident Detection
          ↓
     Threat Validation
          ↓
  Isolation / Containment
          ↓
  Forensic Data Collection
          ↓
      Investigation
          ↓
   Root Cause Analysis
          ↓
   Remediation / Recovery
          ↓
  Security Improvements
```


Les activités de collecte, d'analyse et de confinement peuvent se dérouler en parallèle selon l'urgence de l'incident.

## 9. Synthèse

|Fonction|Rôle dans le DFIR|
|---|---|
|Incident Detection|Détecter les menaces à l'aide de signatures, comportements et anomalies|
|Detection Engines|Analyser différents types d'activités malveillantes|
|Automated Response|Exécuter les actions prévues par les policies|
|Manual Response|Permettre à l'analyste de contenir ou neutraliser une menace|
|Forensic Collection|Récupérer les données nécessaires à l'investigation|
|Timeline Analysis|Reconstituer la chronologie de l'incident|
|Evidence Preservation|Garantir l'intégrité et la traçabilité des preuves|

La valeur de l'EDR dans le DFIR réside dans l'association de trois capacités complémentaires : détecter les menaces, agir sur les endpoints et conserver les informations nécessaires à leur investigation.

Le volet Digital Forensics exige en plus une collecte méthodique et une préservation rigoureuse des preuves, afin que les conclusions de l'investigation soient techniquement fiables et documentées.
