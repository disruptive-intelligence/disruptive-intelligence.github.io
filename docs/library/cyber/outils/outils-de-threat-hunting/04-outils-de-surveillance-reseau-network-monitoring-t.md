---
title: Outils de surveillance réseau — Network Monitoring Tools
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les Network Monitoring Tools permettent de surveiller, capturer et analyser les communications réseau afin de détecter des activités anormales ou malveillantes.

En Threat Hunting, ils contribuent notamment à identifier :

- les communications Command & Control (C2) ;
    
- les tentatives d'exploitation et les scans réseau ;
    
- les mouvements latéraux (Lateral Movement) ;
    
- les transferts de données inhabituels (Potential Exfiltration) ;
    
- les comportements réseau s'écartant de la baseline.
    

Tous les outils présentés ne sont pas dédiés à la cybersécurité : certains surveillent principalement la disponibilité et les performances du réseau.

## 1. Wireshark — Packet Analysis

Wireshark est un analyseur de protocoles réseau, gratuit et open source, permettant de capturer et d'examiner les paquets.

### Fonctionnalités

- Packet Capture : capture de trafic en temps réel ou analyse de fichiers PCAP.
    
- Protocol Analysis : TCP, UDP, HTTP, DNS, TLS, etc.
    
- Filtering : sélection des paquets selon différents critères.
    
- Visualization : statistiques, conversations, graphiques et suivi des flux TCP/UDP.
    

Deux types de filtres importants :

|Filtre|Fonction|Exemple|
|---|---|---|
|Capture Filter|Limiter les paquets capturés|`host 192.168.1.10`|
|Display Filter|Filtrer les paquets déjà capturés|`ip.addr == 192.168.1.10`|

Autres exemples de Display Filters :

```
dns
tcp.port == 443
http.request
```


### Utilisation en Threat Hunting

- Examiner une connexion suspecte.
    
- Analyser les requêtes DNS.
    
- Identifier des protocoles ou destinations inhabituels.
    
- Étudier les détails d'une communication potentiellement malveillante.
    

Limites : Wireshark ne constitue pas un IDS/IPS et ne bloque pas les attaques. L'analyse dépend du point de capture ; les payloads TLS chiffrés ne sont pas automatiquement lisibles.

## 2. Snort — IDS / IPS

Snort est un moteur open source de détection et de prévention d'intrusions réseau.

Il inspecte le trafic et utilise principalement des règles de détection pour identifier les activités suspectes ou les attaques.

### Fonctionnalités

- Signature-Based Detection : détection de patterns d'attaque connus.
    
- Custom Rules : création de règles adaptées à des menaces spécifiques.
    
- Real-Time Monitoring : inspection du trafic en temps réel.
    
- IDS/IPS Deployment : détection ou prévention selon le mode de déploiement.
    
- Security Integration : transmission des alertes aux outils de sécurité.
    

### Exemple de règle Snort

```
alert tcp any any -> 192.168.1.10 22 (msg:"SSH connection attempt"; sid:1000001; rev:1;)
```


Cette règle illustrative génère une alerte lorsqu'un paquet TCP destiné au port 22 de `192.168.1.10` correspond aux conditions définies.

Elle ne démontre ni une attaque SSH ni une authentification réussie : elle signale uniquement une correspondance réseau.

### Utilisation en Threat Hunting

- Rechercher des signatures d'exploitation.
    
- Identifier des scans et communications suspectes.
    
- Développer de nouvelles règles à partir de renseignements CTI.
    
- Corréler les alertes IDS avec les logs firewall et endpoint.
    

IDS ≠ IPS : une alerte Snort ne signifie pas que la communication a été bloquée. La prévention nécessite un déploiement et une configuration adaptés.

## 3. Zeek — Network Security Monitoring

Zeek, anciennement Bro, est une plateforme open source de Network Security Monitoring (NSM) qui analyse les protocoles réseau et produit des journaux structurés.

Contrairement à Wireshark, Zeek est particulièrement adapté à l'analyse de grandes quantités de communications sur la durée.

### Fonctionnalités

- Protocol Analysis : HTTP, DNS, FTP, SMTP, TLS, etc.
    
- Structured Logging : génération de logs détaillés.
    
- Event Detection : événements exploitables pour rechercher des activités suspectes.
    
- Scalability : déploiement adapté aux environnements réseau importants.
    

### Principaux logs Zeek

|Log|Informations|
|---|---|
|`conn.log`|IP, ports, protocole, durée, volume des connexions|
|`dns.log`|Requêtes et réponses DNS|
|`http.log`|Métadonnées des échanges HTTP|
|`ssl.log`|Métadonnées TLS, selon la version/configuration|
|`files.log`|Métadonnées des fichiers observés dans le trafic|

### Utilisation en Threat Hunting

- Détection de communications C2 récurrentes.
    
- Recherche de domaines suspects.
    
- Identification de communications réseau inhabituelles.
    
- Analyse de volumes de données potentiellement exfiltrés.
    

Distinction importante : Zeek produit principalement des logs et métadonnées réseau ; il ne conserve pas automatiquement une capture PCAP complète de chaque communication. Une partie du contenu reste inaccessible lorsque le trafic est chiffré.

## 4. Vectra NDR — Network Detection & Response

Vectra NDR est une solution de Network Detection and Response utilisant notamment l'IA et le Machine Learning pour détecter des comportements réseau suspects.

### Fonctionnalités

- AI / Machine Learning : analyse comportementale et identification d'anomalies.
    
- Network Monitoring : surveillance des activités réseau.
    
- Automated Threat Detection : génération de détections.
    
- Visualization : contextualisation et représentation des menaces.
    
- Incident Response Integration : contribution aux investigations et aux actions de réponse.
    

### Utilisation en Threat Hunting

- Identifier des comportements associés au Lateral Movement.
    
- Rechercher des communications C2.
    
- Détecter des activités inhabituelles sur de grands réseaux.
    
- Prioriser les investigations selon les détections disponibles.
    

Précision : l'IA/ML ne garantit pas l'identification de toutes les attaques. Les actions de réponse effectives dépendent des fonctionnalités, des intégrations et de leur configuration.

## 5. PRTG Network Monitor

PRTG, développé par Paessler, est une solution de Network & Infrastructure Monitoring.

Son objectif principal est de surveiller le fonctionnement et les performances des équipements, services et applications.

### Fonctionnalités

- Device Monitoring : équipements et services réseau.
    
- Traffic Monitoring : bande passante et utilisation du réseau.
    
- Sensors : sondes configurables selon les besoins.
    
- Real-Time Alerting : alertes sur seuils et problèmes détectés.
    
- Dashboards / Mobile Access : visualisation et consultation à distance.
    

### Utilisation en Threat Hunting

PRTG peut aider à identifier :

- des pics de trafic ;
    
- une saturation inhabituelle de bande passante ;
    
- une indisponibilité soudaine ;
    
- des changements significatifs dans l'activité réseau.
    

Ces anomalies peuvent orienter une investigation, notamment lors d'un DDoS ou d'un transfert massif suspect.

PRTG est avant tout un outil de supervision réseau, pas un NDR spécialisé dans la détection des techniques d'attaque.

## 6. Nagios — Network & System Monitoring

Nagios est une solution de supervision des systèmes et réseaux, disposant notamment d'une édition open source.

### Fonctionnalités

- Network Monitoring : disponibilité des équipements et services.
    
- System Monitoring : surveillance de paramètres système.
    
- Threshold-Based Alerting : alertes selon les seuils configurés.
    
- Plugins : extensions et contrôles personnalisés.
    
- Integrations : connexion avec d'autres systèmes de supervision.
    

### Utilisation en Threat Hunting

Nagios peut signaler :

- une consommation CPU ou mémoire inhabituelle ;
    
- une dégradation des services ;
    
- une indisponibilité inattendue ;
    
- des anomalies de performance pouvant justifier une investigation.
    

Ces informations peuvent accompagner les données d'un SIEM, d'un IDS ou d'un EDR.

Une anomalie de performance n'est pas une preuve de compromission.

## 7. Comparaison des outils

|Outil|Catégorie|Visibilité principale|
|---|---|---|
|Wireshark|Packet Analyzer|Paquets et protocoles|
|Snort|IDS / IPS|Signatures et alertes d'attaque|
|Zeek|NSM|Logs et métadonnées réseau|
|Vectra NDR|NDR|Détection comportementale et investigation|
|PRTG|Network Monitoring|Disponibilité, bande passante et performances|
|Nagios|Infrastructure Monitoring|État des systèmes, services et équipements|

### Complémentarité en Threat Hunting

Exemple : recherche d'une communication C2 suspecte.

```
Zeek
→ Repeated Connections to Unknown Domain
                ↓
Snort / Vectra
→ Check Associated Detections
                ↓
Wireshark
→ Investigate Available PCAP
                ↓
SIEM / EDR
→ Identify Host, Process and User
                ↓
Validate Suspicious Activity
```


Les outils comme PRTG et Nagios peuvent compléter l'investigation en fournissant des informations sur les performances ou l'état des équipements au moment de l'activité.

La distinction essentielle est celle de la visibilité fournie :

- Wireshark : que contiennent les paquets observés ?
    
- Snort : le trafic correspond-il à une règle de détection ?
    
- Zeek : quelles communications et transactions réseau ont été observées ?
    
- Vectra NDR : quels comportements réseau sont jugés suspects ?
    
- PRTG / Nagios : le réseau et les systèmes fonctionnent-ils normalement ?
    

Le Threat Hunting gagne en précision lorsque ces informations sont corrélées avec les logs système, les données EDR et la Threat Intelligence.
