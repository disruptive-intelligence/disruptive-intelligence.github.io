---
title: Catégories d’outils de Threat Hunting
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les Threat Hunting Tools regroupent les solutions permettant de collecter, analyser et corréler des données de sécurité afin d'identifier des menaces non détectées par les contrôles existants.

Cinq catégories principales :

1. Data Collection Tools : collecte de télémétrie.
    
2. Data Analysis Tools : analyse et corrélation des données.
    
3. Network Monitoring Tools : surveillance du trafic réseau.
    
4. EDR — Endpoint Detection & Response : visibilité et réponse sur les endpoints.
    
5. CTI — Cyber Threat Intelligence Tools : renseignement sur les menaces.
    

## 1. Data Collection Tools

Outils permettant de collecter les événements produits par les systèmes et les réseaux.

|Outil|Fonction|
|---|---|
|Sysmon|Génère des événements Windows détaillés sur les processus, connexions réseau, fichiers, registre, etc.|
|Winlogbeat|Collecte et transmet les Windows Event Logs vers une plateforme de centralisation, notamment Elasticsearch.|

Distinction importante :

- Sysmon → génère de la télémétrie supplémentaire.
    
- Winlogbeat → collecte et transporte les événements existants, sans être lui-même leur source.
    

Ces données permettent notamment de rechercher des traces d'exécution suspecte, de persistence ou de lateral movement.

## 2. Data Analysis Tools

Outils permettant de centraliser, rechercher, analyser et corréler de grands volumes de données.

|Outil|Fonction|
|---|---|
|Splunk|Indexation, recherche, corrélation et analyse des logs|
|ELK Stack|Collecte, stockage, recherche et visualisation des données|

ELK Stack :

- Elasticsearch : stockage, indexation et recherche.
    
- Logstash : ingestion et transformation des données.
    
- Kibana : exploration et visualisation.
    

Ces plateformes facilitent :

- IOC hunting ;
    
- recherche de comportements anormaux ;
    
- corrélation d'événements ;
    
- reconstruction de timelines ;
    
- développement de détections.
    

## 3. Network Monitoring Tools

Outils permettant d'observer et d'analyser les communications réseau pour identifier des activités suspectes.

|Outil|Fonction|
|---|---|
|Wireshark|Capture et analyse détaillée des paquets réseau (PCAP)|
|Snort|IDS/IPS open source utilisant notamment des signatures pour détecter des attaques réseau|

Distinction :

- Wireshark → analyse du trafic, sans fonctionnalité native de prévention.
    
- Snort en mode IDS → détection et alerting.
    
- Snort en mode IPS → possibilité de bloquer le trafic lorsqu'il est déployé en conséquence.
    

Applications en Threat Hunting :

- identification de communications C2 ;
    
- détection de scans ;
    
- analyse de protocoles suspects ;
    
- investigation de tentatives d'exploitation ;
    
- recherche de mouvements latéraux.
    

## 4. EDR — Endpoint Detection & Response

Les EDR surveillent l'activité des endpoints et permettent d'investiguer ou de répondre aux comportements suspects.

Exemples :

- SentinelOne
    
- CrowdStrike Falcon
    

Fonctionnalités typiques :

- surveillance des processus et de leurs relations parent/enfant ;
    
- collecte de télémétrie endpoint ;
    
- détection de comportements malveillants ;
    
- investigation des activités suspectes ;
    
- réponse à incident : isolation réseau, terminaison de processus ou quarantaine selon le produit.
    

```
Suspicious Process
       ↓
EDR Telemetry
       ↓
Behavioral Analysis
       ↓
Investigation / Response
```


L'EDR est particulièrement utile pour relier un événement suspect à son processus d'origine et aux actions réalisées sur l'endpoint.

## 5. CTI — Cyber Threat Intelligence Tools

Plateformes permettant de collecter, analyser et enrichir les renseignements sur les cybermenaces.

|Outil|Fonction|
|---|---|
|ThreatConnect|Threat Intelligence Platform : centralisation, enrichissement et exploitation des renseignements|
|Recorded Future|Renseignement sur les Threat Actors, campagnes, vulnérabilités, IOCs et infrastructures malveillantes|

Les plateformes CTI permettent notamment :

- d'identifier les Threat Actors et leurs TTPs ;
    
- d'enrichir les IOCs ;
    
- de suivre les campagnes d'attaque ;
    
- d'orienter les hypothèses de Threat Hunting ;
    
- de prioriser les menaces pertinentes pour l'organisation.
    

La CTI fournit le contexte de menace, tandis que les outils d'analyse et de détection permettent de rechercher les traces correspondantes dans l'environnement.

## Complémentarité des outils

```
Sysmon / Windows Logs / Network Telemetry
                    ↓
          Data Collection
             (Winlogbeat)
                    ↓
         SIEM / Data Analysis
          (Splunk / ELK)
                    ↑
        CTI / Threat Intelligence
                    ↓
              Threat Hunting
                    ↓
          Investigation / EDR
                    ↓
        Detection Improvement / IR
```


|Catégorie|Question principale|
|---|---|
|Data Collection|Quelles données peut-on collecter ?|
|Data Analysis|Quels comportements peut-on identifier et corréler ?|
|Network Monitoring|Quelles communications ont eu lieu ?|
|EDR|Quelles actions ont été effectuées sur les endpoints ?|
|CTI|Quelles menaces, techniques et infrastructures faut-il rechercher ?|

Ces catégories ne sont pas totalement exclusives : certains produits combinent plusieurs fonctionnalités.

L'efficacité du Threat Hunting repose sur la complémentarité entre visibilité système, télémétrie réseau, analyse centralisée et Threat Intelligence, plutôt que sur un outil unique.
