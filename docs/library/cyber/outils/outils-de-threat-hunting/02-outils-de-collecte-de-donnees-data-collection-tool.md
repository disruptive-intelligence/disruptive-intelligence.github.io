---
title: Outils de collecte de données — Data Collection Tools
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les Data Collection Tools permettent de collecter, centraliser et transmettre la télémétrie des systèmes et réseaux pour alimenter les activités de Threat Hunting, SOC et Incident Response.

Ils contribuent à :

- Collecter les événements de sécurité.
    
- Centraliser les logs de plusieurs endpoints.
    
- Filtrer, transformer et normaliser les données.
    
- Faciliter les recherches et corrélations dans les plateformes d'analyse.
    

Il faut distinguer les outils qui génèrent de la télémétrie, ceux qui collectent et transportent les logs, et les plateformes qui les stockent et les analysent.

## 1. Sysmon — System Monitor

Sysmon est un outil Microsoft Sysinternals fournissant une télémétrie détaillée sur les activités Windows.

Il fonctionne comme un service système et enregistre les événements dans :

```
Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```


### Fonctionnalités

- Process Creation : création de processus, command line, utilisateur et processus parent.
    
- Network Connections : connexions réseau associées aux processus.
    
- File Activity : certains événements de création, suppression et modification de fichiers selon la configuration.
    
- Registry Activity : modifications de clés et valeurs du registre.
    
- DNS Queries : requêtes DNS et processus associés.
    
- Event Correlation : fournit des identifiants et métadonnées facilitant la corrélation entre événements.
    

### Event IDs utiles

|Event ID|Événement|
|---|---|
|1|Process Creation|
|3|Network Connection|
|7|Image/DLL Loaded|
|11|File Created|
|12 / 13 / 14|Registry Events|
|22|DNS Query|

Complément technique : ces Event IDs sont particulièrement utiles pour le Threat Hunting ; leur collecte dépend de la configuration Sysmon.

### Utilisation en Threat Hunting

Exemples :

- Exécution de PowerShell avec une command line suspecte.
    
- Processus système lançant un exécutable inattendu.
    
- Connexion réseau établie par un processus inconnu.
    
- Création d'un mécanisme de persistence.
    

Les champs `ProcessGuid` et `ParentProcessGuid` permettent notamment de reconstruire les relations entre processus.

Précision :

- Sysmon génère des événements, mais n'est pas un SIEM et n'effectue pas lui-même des corrélations analytiques avancées.
    
- Il ne surveille pas automatiquement toutes les modifications de fichiers.
    
- Sa configuration est essentielle pour déterminer les événements collectés et limiter le bruit.
    

## 2. Winlogbeat

Winlogbeat, développé par Elastic, est un agent léger permettant de collecter et transmettre les Windows Event Logs vers une infrastructure centralisée.

### Fonctionnalités

- Log Collection : collecte des événements Windows.
    
- Lightweight Agent : conçu pour limiter la consommation de ressources.
    
- ELK Integration : intégration avec Elasticsearch et Logstash.
    
- Event Filtering : sélection des journaux ou événements à transmettre.
    
- Timestamp Preservation : conservation des informations temporelles pour l'analyse.
    

### Sources collectées

- Security ;
    
- System ;
    
- Application ;
    
- Sysmon/Operational ;
    
- autres journaux Windows configurés.
    

### Utilisation en Threat Hunting

```
Windows Event Logs + Sysmon
             ↓
          Winlogbeat
             ↓
    Logstash / Elasticsearch
             ↓
           Kibana
             ↓
        Threat Hunting
```


Il permet notamment :

- la centralisation des événements provenant de nombreux endpoints ;
    
- l'analyse des authentifications ;
    
- la recherche de processus suspects ;
    
- l'identification de comportements anormaux sur plusieurs machines.
    

Distinction importante :

- Sysmon → produit de la télémétrie.
    
- Winlogbeat → collecte et transmet cette télémétrie.
    

Winlogbeat n'est donc pas lui-même une source de détection comportementale.

## 3. NXLog

NXLog est un agent polyvalent de Log Collection & Forwarding compatible avec plusieurs systèmes d'exploitation.

### Fonctionnalités

- Cross-Platform Support : Windows, Linux, Unix selon l'édition.
    
- Log Collection : collecte de journaux provenant de différentes applications et systèmes.
    
- Data Processing : filtrage, transformation et normalisation.
    
- High-Volume Processing : traitement de volumes importants.
    
- Multiple Formats : Syslog, JSON, CSV, GELF et autres formats pris en charge.
    

### Fonctionnement

```
Windows / Linux / Unix Logs
             ↓
           NXLog
             ↓
   Filter / Parse / Transform
             ↓
       SIEM / Log Server
```


NXLog peut notamment être utilisé pour :

- centraliser les logs d'environnements hétérogènes ;
    
- convertir plusieurs formats en une structure cohérente ;
    
- filtrer les événements inutiles ;
    
- transmettre les données vers une plateforme d'analyse.
    

### Intérêt en Threat Hunting

La normalisation facilite la recherche d'un même comportement sur des systèmes différents.

Exemple : analyser les activités d'authentification Windows et Linux dans une plateforme centralisée.

## 4. Graylog

Graylog est une plateforme centralisée de Log Management & Analysis, initialement développée par Lennart Koopmann en 2009.

Contrairement à Winlogbeat ou NXLog, Graylog ne se limite pas au transport des logs : il fournit également des fonctionnalités de recherche, d'analyse et de visualisation.

### Fonctionnalités

- Centralized Log Management : ingestion et stockage centralisé.
    
- Real-Time Search : recherche et analyse des événements.
    
- Data Processing : parsing, extraction et transformation.
    
- Dashboards : visualisation des activités et tendances.
    
- Extensibility : intégrations et extensions selon les besoins.
    

### Utilisation en Threat Hunting

Graylog permet de :

- rechercher des événements suspects à grande échelle ;
    
- identifier des anomalies dans les logs ;
    
- analyser l'activité de plusieurs systèmes ;
    
- créer des visualisations et rapports ;
    
- faciliter les investigations à partir de données centralisées.
    

Il peut recevoir des événements provenant d'agents, de systèmes et d'équipements réseau.

## 5. Comparaison des outils

|Outil|Fonction principale|Catégorie|
|---|---|---|
|Sysmon|Génération de télémétrie Windows détaillée|Event Generation|
|Winlogbeat|Collecte et transmission des Windows Event Logs|Log Collector / Shipper|
|NXLog|Collecte, transformation et transmission multiplateforme|Log Collector / Shipper|
|Graylog|Centralisation, stockage, recherche et analyse des logs|Log Management Platform|

Ces outils sont complémentaires, mais ne remplissent pas exactement les mêmes fonctions.

### Exemple d'architecture

```
Windows Endpoint
   ├─ Native Event Logs
   └─ Sysmon
        ↓
   Winlogbeat / NXLog
        ↓
   Central Log Platform
   (Graylog / ELK / SIEM)
        ↓
   Search / Correlation
        ↓
   Threat Hunting
```


### Points importants pour la collecte

La qualité du Threat Hunting dépend aussi :

- Log Coverage : quels événements sont réellement collectés ?
    
- Data Quality : les événements contiennent-ils les champs nécessaires ?
    
- Time Synchronization : horodatages cohérents entre les systèmes.
    
- Retention : durée pendant laquelle les logs restent accessibles.
    
- Noise Reduction : filtrage du bruit sans supprimer de données critiques.
    

Une collecte insuffisante peut empêcher de vérifier une hypothèse de Threat Hunting, même avec une plateforme d'analyse performante.

À distinguer : Sysmon améliore la visibilité endpoint, Winlogbeat et NXLog transportent les événements, tandis que Graylog permet leur exploitation centralisée.
