---
title: IoC-Based Approach
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting — introduction et méthodes.md
note: Threat hunting — introduction et méthodes
up:
- - Threat hunting — introduction et méthodes
  - index.md
---

L'approche IOC-Based Threat Hunting consiste à rechercher, identifier et analyser les traces techniques associées à des attaques ou compromissions connues.

Un IOC (Indicator of Compromise) est un artefact observable pouvant indiquer qu'une activité malveillante s'est produite sur un système ou un réseau.

Objectifs :

- Identifier des systèmes potentiellement compromis.
    
- Retrouver les traces d'une attaque connue.
    
- Déterminer l'étendue d'une compromission (Incident Scoping).
    
- Corréler plusieurs événements à partir d'indicateurs communs.
    
- Améliorer les capacités de détection et de réponse.
    

```
Threat Intelligence / Investigation
              ↓
       IOC Identification
              ↓
     Search Internal Telemetry
              ↓
       Matches / Findings
              ↓
    Validation & Correlation
              ↓
      Investigation / IR
```


IOC Match ≠ Confirmed Compromise : une correspondance doit toujours être contextualisée.

## 1. Types d'IOCs

|Catégorie|Exemples|
|---|---|
|File-Based|Malware hashes, fichiers suspects, modifications de fichiers|
|Network-Based|IP C2, domaines malveillants, URLs, communications suspectes|
|Host-Based|Registry Keys, services, scheduled tasks, modifications système|
|Email-Based|Expéditeurs, URLs de phishing, pièces jointes, en-têtes spécifiques|

### File-Based IOCs

Exemples :

- SHA-256 d'un malware connu ;
    
- chemin d'un payload ;
    
- nom ou artefact spécifique laissé par un outil malveillant.
    

```
Known Malware Hash
       ↓
Search EDR / File Inventory
       ↓
Identify Matching Endpoints
```


Un hash exact est utile pour retrouver un fichier connu, mais une modification de son contenu peut produire une empreinte différente.

### Network-Based IOCs

Exemples :

- IP associée à un serveur C2 ;
    
- domaine de phishing ;
    
- URL distribuant un malware.
    

```
Malicious Domain
       ↓
Search DNS / Proxy Logs
       ↓
Identify Hosts
       ↓
Correlate Firewall / NetFlow / EDR
```


Une requête DNS vers un domaine malveillant ne prouve pas qu'une connexion a été établie.

### Host-Based IOCs

Exemples :

- Registry Key de persistance ;
    
- service malveillant ;
    
- scheduled task suspecte ;
    
- artefact spécifique dans les Event Logs.
    

Ces indicateurs permettent notamment d'identifier des mécanismes de Persistence ou de Defense Evasion.

### Email-Based IOCs

Exemples :

- adresse expéditrice ;
    
- sujet ou en-têtes caractéristiques ;
    
- URL de phishing ;
    
- hash d'une pièce jointe malveillante.
    

Ils sont principalement recherchés dans les logs email et les solutions de sécurité de messagerie.

Précision : une anomalie générique (trafic inhabituel, fichier modifié) n'est pas automatiquement un IOC. Elle devient plus exploitable lorsqu'un lien concret avec une menace est établi.

## 2. Identifying IOCs

L'identification d'IOCs repose principalement sur trois sources.

### Threat Intelligence

Les rapports et feeds CTI fournissent des indicateurs associés à :

- Threat Actors ;
    
- campagnes malveillantes ;
    
- malware families ;
    
- infrastructures C2 ;
    
- attaques précédemment observées.
    

Les IOCs doivent être évalués selon :

- la fiabilité de la source ;
    
- leur date d'observation ;
    
- leur pertinence pour l'organisation ;
    
- leur niveau de confiance.
    

### Log Analysis

Les IOCs peuvent être recherchés dans différentes sources de télémétrie :

|IOC|Sources pertinentes|
|---|---|
|IP / Domain / URL|DNS, Proxy, Firewall, NetFlow|
|File Hash / Path|EDR, Antivirus, File Inventory|
|Registry / Persistence|EDR, Sysmon, Windows Event Logs|
|Email Artifact|Email Gateway, Mail Security Logs|

### Automation & Security Tools

Les SIEM, EDR/XDR et plateformes CTI peuvent automatiser :

- IOC matching ;
    
- enrichment ;
    
- correlation ;
    
- alerting ;
    
- historical searches.
    

```
Threat Intelligence Feed
         ↓
SIEM / EDR Integration
         ↓
IOC Matching
         ↓
Security Alert
         ↓
Analyst Validation
```


L'automatisation accélère la recherche, mais ne remplace pas l'analyse humaine.

## 3. IoC Databases & Sharing Standards

Sous l'étiquette « IOC Databases » se rangent plusieurs outils et standards aux fonctions différentes.

|Outil / Standard|Fonction|
|---|---|
|OpenIOC|Format ouvert permettant de représenter des indicateurs de compromission|
|STIX|Modèle structuré de représentation de Threat Intelligence|
|TAXII|Protocole/API permettant l'échange automatisé de Threat Intelligence|
|VirusTotal|Plateforme d'analyse et d'enrichissement de fichiers, URLs, domaines et IP|

### OpenIOC

Format développé initialement par Mandiant pour décrire des indicateurs techniques.

Peut servir à représenter des conditions sur :

- files ;
    
- processes ;
    
- registry artifacts ;
    
- network indicators.
    

OpenIOC est un format, pas une base de données.

### STIX & TAXII

Deux standards complémentaires :

```
STIX
→ Structure / Represent Threat Intelligence

TAXII
→ Transport / Exchange Threat Intelligence
```


Ils facilitent l'interopérabilité entre outils et organisations.

STIX et TAXII ne sont pas des bases d'IOCs en eux-mêmes.

### VirusTotal

Permet notamment de :

- rechercher un hash ;
    
- analyser un fichier suspect ;
    
- consulter des détections antivirus ;
    
- examiner les relations entre fichiers, domaines, URLs et IP ;
    
- enrichir une investigation.
    

Précautions :

- `0 detections` ne signifie pas qu'un fichier est légitime.
    
- Une détection isolée peut être un false positive.
    
- Privilégier la recherche par hash avant d'envisager l'envoi d'un fichier.
    
- Éviter de téléverser des fichiers internes ou sensibles vers un service public sans autorisation.
    

### IOC Feed Maintenance

Les IOCs doivent être régulièrement actualisés :

- nouveaux indicateurs ;
    
- indicateurs obsolètes ;
    
- changements de réputation ;
    
- suppression de false positives ;
    
- expiration des règles temporaires.
    

Une IP malveillante aujourd'hui peut être réattribuée ultérieurement à un service légitime.

## 4. Case Study — IOC-Based Threat Hunting

### Scénario

Une organisation détecte :

- du trafic réseau anormal ;
    
- des modifications suspectes de fichiers ;
    
- une connexion potentiellement associée à un malware.
    

### Identification

Les analystes examinent :

- System / Endpoint Logs ;
    
- Network Traffic ;
    
- Suspicious File Artifacts.
    

Ils découvrent qu'un malware communique avec une IP spécifique.

```
Suspicious Endpoint
       ↓
Malware Activity
       ↓
Connection to External IP
       ↓
Potential Network IOC
```


### Enrichment & Validation

L'IOC est comparé aux informations provenant de sources CTI et d'outils comme VirusTotal.

Questions essentielles :

- L'IP est-elle associée à une infrastructure malveillante connue ?
    
- Quand cette association a-t-elle été observée ?
    
- Quels autres endpoints ont communiqué avec cette IP ?
    
- Quels processus ont initié les connexions ?
    
- Existe-t-il d'autres artefacts confirmant l'activité malveillante ?
    

### Hunting

```
Known Suspicious IP
        ↓
Search Firewall / NetFlow / Proxy
        ↓
Identify Matching Hosts
        ↓
Analyze EDR / System Logs
        ↓
Correlate with Malware Activity
        ↓
Determine Incident Scope
```


L'analyste peut ainsi identifier d'autres systèmes potentiellement concernés.

### Response

Si l'activité malveillante est confirmée :

- bloquer les communications pertinentes ;
    
- isoler les endpoints si nécessaire ;
    
- supprimer les composants malveillants ;
    
- traiter la cause de compromission ;
    
- renforcer les règles de détection.
    

Le blocage d'une IP doit tenir compte des infrastructures partagées (CDN, cloud, NAT), afin d'éviter des interruptions injustifiées.

## 5. Limites de l'IOC-Based Hunting

L'approche IOC-Based est particulièrement efficace pour rechercher des traces d'attaques déjà documentées, mais présente plusieurs limites :

- dépend de la qualité et de la fraîcheur du renseignement ;
    
- identifie difficilement des attaques ne disposant pas encore d'IOCs connus ;
    
- les attaquants peuvent remplacer rapidement leurs domaines, IP et hashes ;
    
- certains IOCs sont partagés avec des activités légitimes ;
    
- l'absence de correspondance ne garantit pas l'absence de compromission.
    

### Comparaison avec les autres méthodologies

|Approche|Point de départ|
|---|---|
|Adversary-Centric|TTPs et comportements de Threat Actors|
|Hypothesis-Driven|Hypothèse spécifique à tester|
|IOC-Based|Artefacts associés à des menaces connues|

Ces approches sont complémentaires : un hunt basé sur des IOCs peut révéler de nouveaux comportements, qui serviront ensuite à formuler une hypothèse ou à développer des détections basées sur les TTPs.

## Workflow IOC-Based Hunting

```
Threat Intelligence / Known Attack
              ↓
        Extract IOCs
              ↓
    Validate & Enrich IOCs
              ↓
      Search SIEM / EDR
              ↓
       Correlate Matches
              ↓
    Determine Affected Hosts
              ↓
       Confirm / Reject
              ↓
   Incident Response if Needed
              ↓
    Update Detection Content
```


L'IOC-Based Threat Hunting sert principalement à retrouver les traces techniques de menaces connues et à évaluer leur présence dans l'environnement. Sa fiabilité repose sur la qualité des indicateurs, leur contextualisation et leur corrélation avec d'autres preuves techniques.
