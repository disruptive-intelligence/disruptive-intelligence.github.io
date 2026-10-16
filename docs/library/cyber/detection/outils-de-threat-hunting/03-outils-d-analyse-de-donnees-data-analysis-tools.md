---
title: Outils d'analyse de données — Data Analysis Tools
source: Cyber/06 Détection & réponse/Threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les Data Analysis Tools permettent de traiter, rechercher, corréler et visualiser les données collectées afin d'identifier des activités suspectes lors des opérations de Threat Hunting.

Ils transforment les logs bruts en informations exploitables pour :

- Log Analysis : rechercher des événements spécifiques.
    
- Event Correlation : relier plusieurs événements ou sources de données.
    
- Anomaly Detection : identifier des comportements inhabituels.
    
- Alerting : déclencher des alertes selon des conditions définies.
    
- Reporting & Visualization : produire des dashboards et des rapports d'investigation.
    

Trois solutions présentées : Splunk, ELK Stack et LogRhythm.

## 1. Splunk

Splunk est une plateforme de recherche, de surveillance et d'analyse de grands volumes de données, notamment utilisée pour l'analyse des événements de sécurité.

### Fonctionnalités

- Real-Time Search : recherche et analyse des événements récents ou historiques.
    
- Event Correlation : rapprochement d'événements provenant de différentes sources.
    
- Data Visualization : graphiques, tableaux et dashboards.
    
- Alerting & Reporting : alertes configurables et rapports.
    
- Machine Learning : détection d'anomalies et analyses prédictives via les fonctionnalités ou extensions adaptées.
    

### SPL — Search Processing Language

Splunk utilise SPL, son langage de recherche, pour filtrer et analyser les événements.

Exemple complémentaire :

```
index=windows EventCode=4625
| stats count by Account_Name, Source_Network_Address
| sort -count
```


Cette recherche vise à compter les échecs d'authentification Windows (`4625`) par compte et IP source, sous réserve que ces champs existent dans les données indexées.

Elle peut aider à identifier :

- des tentatives répétées d'authentification ;
    
- des IP générant de nombreux échecs ;
    
- des comptes fréquemment ciblés.
    

Attention : un volume élevé de `4625` ne prouve pas à lui seul un brute-force. Il faut examiner la période, les comptes, le contexte et les éventuelles authentifications réussies.

### Utilisation en Threat Hunting

Splunk permet notamment de :

- rechercher des IOCs dans les logs ;
    
- reconstruire une timeline d'attaque ;
    
- analyser les authentifications et les activités réseau ;
    
- corréler plusieurs sources pour détecter des comportements suspects.
    

## 2. ELK Stack — Elasticsearch, Logstash, Kibana

La ELK Stack, développée par Elastic, est une plateforme de collecte, traitement, recherche et visualisation des données.

### Composants

|Composant|Fonction|
|---|---|
|Elasticsearch|Stockage, indexation, recherche et analyse des données|
|Logstash|Ingestion, parsing, transformation et transmission des logs|
|Kibana|Interface d'exploration, visualisation et création de dashboards|

### Fonctionnement

```
Windows / Linux / Network Logs
              ↓
       Logstash / Agents
              ↓
         Elasticsearch
              ↓
            Kibana
              ↓
          Threat Hunting
```


### Fonctionnalités

- Data Processing : collecte et transformation des événements.
    
- Search & Query : recherche rapide dans les données indexées.
    
- Visualization : dashboards, graphiques et tableaux.
    
- Scalability : gestion de volumes importants de logs.
    

### Utilisation en Threat Hunting

La stack ELK permet :

- d'explorer les logs centralisés ;
    
- d'identifier des anomalies ;
    
- de rechercher des activités suspectes sur plusieurs endpoints ;
    
- de corréler des informations système et réseau ;
    
- de visualiser des tendances et comportements.
    

Complément technique : Kibana prend notamment en charge KQL (Kibana Query Language) pour filtrer les événements.

Exemple :

```
event.code: "4625"
```


Cette recherche cible les événements portant le code `4625`, à condition que les données soient normalisées avec ce champ.

Précisions :

- La stack est aujourd'hui souvent appelée Elastic Stack, car son écosystème dépasse les trois composants historiques ELK.
    
- « Open source » dépend de la distribution : les licences et fonctionnalités varient selon les versions utilisées.
    

## 3. LogRhythm

LogRhythm est une plateforme SIEM (Security Information and Event Management) intégrant des fonctions de centralisation, d'analyse et de détection des événements de sécurité.

### Fonctionnalités

- Centralized Log Management : collecte et gestion des logs.
    
- Advanced Analytics : analyse et corrélation des événements.
    
- Real-Time Alerting : alertes sur des activités suspectes.
    
- Incident Response Support : assistance aux investigations et à la réponse.
    
- Security Integrations : connexion avec différents équipements et outils de sécurité.
    

### Utilisation en Threat Hunting

LogRhythm permet notamment de :

- rechercher des activités suspectes dans les logs ;
    
- corréler des événements provenant de différents systèmes ;
    
- détecter des comportements anormaux ;
    
- faciliter le triage et les investigations ;
    
- transmettre les résultats aux équipes d'Incident Response.
    

Précision : les capacités de réponse dépendent du produit, des intégrations et de la configuration. Une alerte SIEM ne signifie pas qu'une menace a automatiquement été bloquée.

## 4. Comparaison des solutions

|Critère|Splunk|ELK Stack|LogRhythm|
|---|---|---|---|
|Fonction principale|Recherche et analyse de données|Ingestion, recherche et visualisation|SIEM intégré|
|Recherche|SPL|Elasticsearch, KQL notamment|Recherche et analyse via la plateforme|
|Visualisation|Dashboards|Kibana|Dashboards|
|Corrélation|Oui|Selon les fonctionnalités configurées|Oui|
|Alerting|Oui|Selon les fonctionnalités configurées|Oui|
|Threat Hunting|Recherche et investigation|Exploration et analyse des logs|Hunting et investigation SIEM|

Les trois solutions peuvent contribuer au Threat Hunting, mais leur architecture, leur administration et leurs capacités de sécurité diffèrent.

## 5. Exemple d'utilisation en Threat Hunting

Hypothèse : un attaquant pourrait avoir compromis un compte après plusieurs tentatives d'authentification.

```
Windows Authentication Logs
           ↓
SIEM / Data Analysis Platform
           ↓
Multiple Failed Logons (4625)
           ↓
Successful Logon (4624)
           ↓
Correlate User / Source IP / Time
           ↓
Check Endpoint & Network Activity
           ↓
Investigate Possible Compromise
```


L'analyste peut utiliser Splunk, ELK ou LogRhythm pour corréler les événements et déterminer si l'activité nécessite une investigation approfondie.

Un enchaînement `4625 → 4624` peut être suspect, mais ne constitue pas une preuve suffisante de compromission : il faut examiner les utilisateurs, les sources, les types de logon et les activités qui suivent.

## Distinction essentielle

- Data Collection Tools : Sysmon, Winlogbeat et NXLog produisent ou transmettent les événements.
    
- Data Analysis Tools : Splunk, ELK et LogRhythm permettent de les rechercher, analyser et corréler.
    

La qualité des résultats dépend autant de la télémétrie disponible, de sa normalisation et de sa rétention que des fonctionnalités de la plateforme.

Un outil d'analyse performant ne peut pas détecter un comportement si les événements nécessaires ne sont pas collectés.
