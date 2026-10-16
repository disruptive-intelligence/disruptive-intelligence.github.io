---
title: Outils EDR — Endpoint Detection & Response
source: Cyber/10 Outils & solutions/EDR, XDR & threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les EDR (Endpoint Detection & Response) sont des solutions de sécurité permettant de surveiller, détecter, investiguer et répondre aux activités malveillantes sur les endpoints : postes de travail, serveurs et autres terminaux compatibles.

Ils jouent un rôle essentiel dans le Threat Hunting grâce à leur visibilité sur les comportements exécutés directement sur les systèmes.

## Fonctionnalités principales

- Real-Time Monitoring : surveillance continue des activités endpoint.
    
- Behavioral Analysis : détection de comportements suspects ou malveillants.
    
- Threat Intelligence : enrichissement des détections avec des renseignements sur les menaces.
    
- Machine Learning : analyse automatisée pour identifier certaines menaces.
    
- Incident Investigation : reconstruction des activités et des chaînes d'attaque.
    
- Response Actions : confinement et remédiation des menaces détectées.
    

## 1. CrowdStrike Falcon

CrowdStrike Falcon est une plateforme de sécurité endpoint reposant sur un agent local et une infrastructure de gestion et d'analyse cloud.

### Fonctionnalités

- Real-Time Monitoring : surveillance des activités endpoint.
    
- Threat Intelligence Integration : identification de comportements associés aux Threat Actors et à leurs TTPs.
    
- Machine Learning : détection automatisée de menaces.
    
- Rapid Response : intervention sur les endpoints compromis.
    
- Cloud-Based Management : administration et analyse centralisées via le cloud.
    

### Utilisation en Threat Hunting

CrowdStrike Falcon permet notamment de :

- rechercher des processus suspects ;
    
- analyser les comportements associés à une attaque ;
    
- corréler les activités de plusieurs endpoints ;
    
- exploiter la Threat Intelligence pour orienter les investigations ;
    
- déclencher des actions de réponse.
    

L'intérêt principal est de combiner Endpoint Telemetry + Behavioral Detection + Threat Intelligence pour identifier des menaces non détectées par les mécanismes de protection classiques.

## 2. SentinelOne

SentinelOne est une solution EDR mettant l'accent sur l'analyse comportementale, la détection automatisée et les capacités de réponse.

### Fonctionnalités

- Automated Threat Detection : identification automatisée de menaces.
    
- Behavioral Analysis : analyse des activités et comportements suspects.
    
- Real-Time Response : intervention rapide sur les endpoints.
    
- Continuous Monitoring : collecte et suivi des activités système.
    
- Threat Intelligence Integration : enrichissement des détections.
    
- Automation & Orchestration : automatisation de certaines actions de sécurité.
    
- Attack Visualization : visualisation des événements et des chaînes d'attaque.
    
- Cross-Platform Support : prise en charge de Windows, macOS et Linux.
    

### Utilisation en Threat Hunting

SentinelOne permet :

- d'analyser des comportements suspects ;
    
- de reconstruire une séquence d'attaque ;
    
- d'identifier des activités de malware ;
    
- de rechercher des événements similaires sur d'autres endpoints ;
    
- d'isoler et de remédier aux menaces selon les fonctionnalités disponibles.
    

Sa visualisation des chaînes d'attaque facilite l'analyse des relations entre processus et événements.

## 3. Microsoft Defender for Endpoint

Microsoft Defender for Endpoint (MDE) est la solution EDR de Microsoft, intégrée à son écosystème de sécurité.

### Fonctionnalités

- Advanced Threat Protection : protection et détection avancées.
    
- Threat Intelligence Integration : exploitation des renseignements Microsoft.
    
- Behavioral Analysis & ML : détection de comportements suspects.
    
- Incident Response : investigation et actions de réponse.
    
- Microsoft Security Integration : intégration avec Microsoft 365 et les autres solutions de sécurité Microsoft.
    

### Utilisation en Threat Hunting

MDE permet notamment de :

- rechercher des événements suspects sur les endpoints ;
    
- analyser les processus, fichiers et connexions réseau ;
    
- investiguer les alertes et incidents ;
    
- corréler les activités endpoint avec d'autres signaux Microsoft ;
    
- effectuer des actions de remédiation.
    

Complément pratique : MDE propose notamment Advanced Hunting, qui utilise KQL (Kusto Query Language) pour interroger la télémétrie de sécurité.

Exemple illustratif :

```
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| project Timestamp, DeviceName, AccountName,
          ProcessCommandLine, InitiatingProcessFileName
```


Cette requête recherche les événements d'exécution de `powershell.exe` dans les données disponibles. Elle ne détecte pas, à elle seule, une activité malveillante.

## 4. Comparaison des solutions

|Solution|Caractéristiques mises en avant|
|---|---|
|CrowdStrike Falcon|Gestion cloud, Threat Intelligence, ML, investigation et réponse|
|SentinelOne|Behavioral Analysis, automatisation, visualisation des chaînes d'attaque|
|Microsoft Defender for Endpoint|Protection endpoint, Advanced Hunting, intégration à l'écosystème Microsoft|

Ces trois produits possèdent de nombreuses fonctionnalités communes. Leurs capacités précises dépendent des éditions, licences, systèmes et configurations.

## 5. Utilisation opérationnelle en Threat Hunting

Exemple : recherche d'une exécution PowerShell suspecte.

```
Threat Hunting Hypothesis
        ↓
Search EDR Telemetry
        ↓
Suspicious PowerShell Execution
        ↓
Analyze Process Tree / Command Line
        ↓
Check File & Network Activity
        ↓
Correlate with User / Host Context
        ↓
Validate Potential Compromise
        ↓
Response / Detection Improvement
```


L'analyse peut porter sur :

- Process Tree : quel processus a lancé PowerShell ?
    
- Command Line : quelles commandes ont été exécutées ?
    
- User Context : quel compte était impliqué ?
    
- Network Activity : quelles connexions ont été initiées ?
    
- File / Registry Activity : quels artefacts ont été créés ou modifiés ?
    
- Timeline : quelle succession d'événements peut être reconstruite ?
    

### Actions de réponse possibles

Selon le produit et sa configuration :

- Host Isolation : isoler un endpoint du réseau.
    
- Process Termination : arrêter un processus malveillant.
    
- File Quarantine : placer un fichier en quarantaine.
    
- Remediation : supprimer ou neutraliser certains artefacts.
    
- Remote Investigation : approfondir l'analyse à distance.
    

Points de vigilance :

- Une alerte EDR ne constitue pas automatiquement une compromission confirmée.
    
- L'absence d'alerte ne garantit pas qu'un endpoint soit sain.
    
- L'isolation d'un serveur critique peut avoir un impact opérationnel important.
    
- Avant une action destructive, préserver les preuves nécessaires à l'investigation lorsque la situation le permet.
    

## EDR vs Antivirus traditionnel

|Antivirus traditionnel|EDR|
|---|---|
|Principalement orienté prévention et détection des malwares|Détection, investigation et réponse endpoint|
|Analyse de fichiers et de comportements selon le produit|Télémétrie approfondie sur les activités système|
|Quarantaine et suppression des menaces|Investigation des chaînes d'attaque et actions de réponse|
|Visibilité historique parfois limitée|Recherche rétrospective selon la rétention disponible|

Cette distinction n'est pas absolue : les antivirus modernes intègrent également des mécanismes comportementaux et certaines fonctionnalités avancées.

En Threat Hunting, la valeur principale de l'EDR réside dans sa capacité à relier les comportements suspects à leur contexte d'exécution, afin de reconstruire une attaque, évaluer son étendue et guider l'Incident Response.
