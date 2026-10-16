---
title: Importance of EDR Data for Threat Hunting
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting avec l'EDR.md
note: Threat hunting avec l'EDR
up:
- - Threat hunting avec l'EDR
  - index.md
---

La télémétrie EDR regroupe les données collectées sur les endpoints afin de surveiller, détecter et investiguer les activités potentiellement malveillantes.

En Threat Hunting, elle permet de rechercher des menaces non détectées, de reconstruire leurs comportements et d'identifier les systèmes potentiellement compromis.

Principaux usages :

- Data Collection : collecte des événements endpoint.
    
- Data Enrichment : ajout de contexte aux événements.
    
- Data Analysis : recherche de comportements suspects.
    
- Visualization : reconstruction des activités et chaînes d'attaque.
    
- IOC / IOA Hunting : recherche d'indicateurs techniques et comportementaux.
    

## 1. Data Collection

Les EDR collectent différents types de télémétrie.

|Source|Informations collectées|
|---|---|
|Process Activity|Exécutions, command lines, relations parent/enfant|
|File Activity|Création, modification ou suppression de fichiers|
|Network Connections|Connexions et destinations associées aux processus|
|System Events|Activités et modifications du système|
|User Activity|Comptes et comportements utilisateurs observables|

### Real-Time Monitoring

La surveillance continue permet de détecter rapidement certaines activités suspectes et de conserver les éléments nécessaires aux investigations.

Précision : un EDR observe principalement les endpoints sur lesquels son agent est déployé. Il ne dispose pas nécessairement d'une visibilité complète sur tout le trafic réseau.

## 2. Data Enrichment & Correlation

### Data Enrichment

L'enrichissement consiste à ajouter des informations contextuelles aux événements collectés :

- Threat Intelligence : réputation d'une IP, d'un domaine ou d'un hash.
    
- User Context : identité et privilèges associés à un compte.
    
- Environmental Context : criticité et rôle de l'endpoint.
    

Exemple :

```
Suspicious Process
        ↓
EDR Telemetry
        ↓
User + Endpoint + File Hash + IP Reputation
        ↓
Contextualized Investigation
```


### Event Correlation

La corrélation permet de relier plusieurs événements pour comprendre leur contexte et leur éventuelle relation avec une attaque.

Exemple : un processus inconnu crée une tâche planifiée puis établit une connexion réseau inhabituelle.

L'ensemble peut être plus révélateur que chaque événement pris isolément.

## 3. Data Analysis

### Big Data Analytics

Les EDR peuvent centraliser et analyser de grands volumes de données endpoint.

Fonctionnalités :

- Rapid Search & Analysis : recherche rapide d'événements.
    
- Pattern Recognition : identification de séquences ou comportements récurrents.
    
- Behavioral Analysis : analyse des activités des utilisateurs et processus.
    
- Anomaly Detection : recherche d'écarts par rapport aux comportements attendus.
    

### Machine Learning & AI

Trois applications principales :

|Technique|Objectif|
|---|---|
|Behavioral Modeling|Modéliser les comportements habituels|
|Predictive Analysis|Estimer les risques ou comportements futurs à partir des données historiques|
|Anomaly Detection|Identifier des activités s'écartant de la baseline|

⚠️ Anomaly ≠ Malicious Activity. Une anomalie est une piste d'investigation. De même, l'IA/ML ne permet pas de prédire avec certitude les futures attaques.

## 4. Data Visualization

La visualisation facilite l'analyse de grandes quantités de données et la compréhension des relations entre événements.

### Techniques

- Graphs & Tables : synthèse et comparaison des activités.
    
- Relationship Maps : visualisation des liens entre processus, événements ou systèmes.
    
- Heatmaps : identification des périodes ou zones présentant une forte concentration d'événements.
    
- Timelines : représentation chronologique des événements.
    

### Timeline & Attack Reconstruction

Une Timeline permet de déterminer l'ordre dans lequel les activités se sont produites.

Exemple illustratif :

```
10:00 — Suspicious Process Execution
10:01 — New Scheduled Task
10:03 — Outbound Network Connection
10:05 — Additional Process Execution
```


Elle facilite :

- l'identification de l'activité initiale ;
    
- la reconstruction des actions suivantes ;
    
- la corrélation entre processus, fichiers et communications ;
    
- l'évaluation de l'étendue potentielle de l'attaque.
    

Une chronologie cohérente nécessite des timestamps fiables et une télémétrie suffisamment complète.

## 5. IOC — Indicators of Compromise

Un IOC est un artefact technique pouvant indiquer une activité malveillante ou une compromission.

Exemples :

- File Hash : hash de malware connu.
    
- IP Address : adresse associée à une infrastructure malveillante.
    
- Domain / URL : destination suspecte.
    
- File Path : emplacement associé à un artefact malveillant.
    

### IOC Hunting

Processus :

1. Collecter les événements endpoint.
    
2. Comparer les données aux IOCs connus.
    
3. Identifier les correspondances.
    
4. Analyser les résultats pour comprendre l'origine et l'étendue de la menace.
    

```
Known IOC
    ↓
Search EDR Telemetry
    ↓
Identify Matching Endpoints
    ↓
Validate & Investigate
```


### Avantages et limites

- Identification rapide de menaces déjà documentées.
    
- Recherche historique d'IOCs dans les endpoints.
    
- Enrichissement continu via les bases de Threat Intelligence.
    

Cependant, les attaquants peuvent modifier rapidement leurs IP, domaines et hashes.

IOC Match ≠ Confirmed Compromise. Une correspondance doit être vérifiée dans son contexte.

## 6. IOA — Indicators of Attack

Un IOA est un indicateur comportemental pouvant révéler une attaque en cours ou une méthode employée par un adversaire.

Il s'intéresse davantage aux actions et comportements qu'aux artefacts techniques précis.

Exemples :

- tentatives d'accès non autorisé ;
    
- suppressions de fichiers suspectes ;
    
- modifications inhabituelles de configuration ;
    
- activités associées à l'utilisation d'un compte compromis.
    

### IOA Hunting

L'analyse repose sur :

- Behavioral Analysis : examen des comportements.
    
- Anomaly Detection : identification d'activités inhabituelles.
    
- IOA Detection : recherche de séquences compatibles avec des techniques d'attaque.
    

Exemple illustratif :

```
Unexpected Script Execution
          ↓
Suspicious Credential Access
          ↓
Unusual Remote Connection
          ↓
Potential Attack Behavior
```


Cette approche permet d'identifier des comportements malveillants même lorsqu'aucun IOC connu n'est disponible.

Précision : supprimer un fichier ou modifier une configuration n'est pas automatiquement un IOA. L'activité doit être interprétée selon son contexte et sa correspondance avec une technique d'attaque.

## 7. IOC vs IOA

|Critère|IOC|IOA|
|---|---|---|
|Nature|Artefact technique|Comportement ou séquence d'activités|
|Focus|Traces associées à une menace|Méthode ou déroulement d'une attaque|
|Exemples|Hash, IP, domaine|Credential Access, comportements de Persistence|
|Hunting|IOC Matching|Behavioral Hunting|
|Limite|Indicateurs rapidement remplaçables|Comportements parfois légitimes selon le contexte|

### Complémentarité

```
EDR Telemetry
     ├── IOC Hunting → Known Malicious Artifacts
     └── IOA Hunting → Suspicious Attack Behaviors
                           ↓
                 Correlation & Validation
                           ↓
                  Threat Investigation
```


Les IOCs permettent de retrouver les traces de menaces connues, tandis que les IOAs contribuent à identifier des méthodes d'attaque potentiellement inconnues ou modifiées.

## 8. Application opérationnelle au Threat Hunting

Une investigation EDR peut suivre ce workflow :

1. Hypothesis : définir le comportement ou l'indicateur recherché.
    
2. Data Collection : sélectionner la télémétrie pertinente.
    
3. Enrichment : ajouter le contexte utilisateur, système et CTI.
    
4. Analysis : rechercher des IOCs ou comportements suspects.
    
5. Visualization : examiner les relations et reconstruire la timeline.
    
6. Validation : confirmer, réfuter ou laisser l'hypothèse inconclusive.
    
7. Detection Improvement : exploiter les résultats pour améliorer les règles de détection.
    

L'intérêt principal de l'EDR en Threat Hunting est de passer d'un événement isolé à une compréhension contextualisée des activités endpoint, grâce à la collecte, à la corrélation et à l'analyse des données.

La qualité d'un hunt dépend donc autant de la couverture, de la rétention et de la qualité de la télémétrie que des algorithmes de détection utilisés.
