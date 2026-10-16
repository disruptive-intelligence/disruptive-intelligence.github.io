---
title: Intégration et Automatisation des Outils de Threat Hunting
source: Cyber/06 Détection & réponse/Threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

L'efficacité du Threat Hunting repose sur la capacité à combiner plusieurs sources de télémétrie et à automatiser certaines tâches d'analyse et de réponse.

Deux concepts fondamentaux :

- Integration : connecter les outils de sécurité pour centraliser et corréler leurs données.
    
- Automation : automatiser les tâches répétitives à l'aide de workflows et de playbooks.
    

Objectifs : améliorer la visibilité, accélérer les investigations, réduire les tâches manuelles et faciliter la réponse aux menaces.

## 1. Security Tools Integration

L'intégration permet de corréler les informations issues des solutions SIEM, EDR, CTI et Network Monitoring.

|Outil|Rôle dans l'intégration|
|---|---|
|SIEM|Centralise, recherche et corrèle les événements de sécurité|
|EDR|Fournit la télémétrie endpoint : processus, fichiers, connexions et alertes|
|CTI Platform|Enrichit les événements avec des IOCs, TTPs et renseignements sur les menaces|
|Network Monitoring / NDR|Fournit les informations sur les communications et comportements réseau|

### SIEM Integration

Le SIEM (Security Information and Event Management) constitue un point central d'analyse.

Il peut recevoir :

- les alertes EDR ;
    
- les logs firewall, IDS/IPS et NDR ;
    
- les Windows Event Logs ;
    
- les informations CTI.
    

L'objectif est de corréler plusieurs signaux plutôt que de les examiner isolément.

### EDR Integration

L'intégration EDR permet de relier une activité réseau à son contexte endpoint.

Exemple :

- le firewall observe une connexion vers une IP suspecte ;
    
- l'EDR identifie le processus à l'origine de cette connexion ;
    
- le SIEM corrèle ces événements pour faciliter l'investigation.
    

### CTI Integration

La Threat Intelligence apporte du contexte aux événements internes.

Elle peut notamment permettre :

- l'enrichissement d'IP, domaines et hashes ;
    
- la recherche d'IOCs connus ;
    
- l'identification de campagnes et TTPs associées ;
    
- la priorisation des événements suspects.
    

### Network Monitoring Integration

Les outils réseau fournissent des informations sur :

- les connexions entre systèmes ;
    
- les communications sortantes ;
    
- les protocoles utilisés ;
    
- les volumes de trafic ;
    
- les anomalies réseau.
    

Leur corrélation avec l'EDR et le SIEM améliore la visibilité sur les attaques susceptibles d'impliquer plusieurs machines.

### Exemple d'architecture intégrée

```
              CTI Platform
              (Threat Context)
                    ↓
EDR ─────────────── SIEM ───────── Network Monitoring
(Endpoint)       (Correlation)        (Traffic)
                    ↓
             Threat Hunting
                    ↓
           Investigation / IR
```


Précision : connecter les outils ne suffit pas. Une corrélation fiable dépend aussi de la normalisation des champs, de la synchronisation des timestamps et de la qualité des données collectées.

## 2. Threat Hunting Automation

L'Automation consiste à exécuter automatiquement certaines étapes d'une investigation ou d'un processus de sécurité.

Applications :

- collecte d'événements ;
    
- recherche d'IOCs ;
    
- enrichissement CTI ;
    
- corrélation de résultats ;
    
- création de tickets d'investigation ;
    
- déclenchement d'actions de réponse.
    

L'automatisation permet aux analystes de consacrer davantage de temps à l'analyse complexe et à la validation des hypothèses.

## 3. SOAR — Security Orchestration, Automation & Response

Une plateforme SOAR connecte différents outils de sécurité et coordonne leurs actions au moyen de workflows automatisés.

Ses trois composantes :

|Composante|Fonction|
|---|---|
|Orchestration|Coordonner plusieurs outils et systèmes de sécurité|
|Automation|Exécuter automatiquement des tâches prédéfinies|
|Response|Déclencher ou faciliter les actions de réponse aux incidents|

### Playbooks

Un Playbook est une séquence d'actions prédéfinies qui permet de traiter un scénario de sécurité.

Exemple : investigation d'une IP suspecte.

```
SIEM Alert: Suspicious IP
           ↓
SOAR Playbook
           ↓
Query CTI Reputation
           ↓
Search Firewall / EDR Events
           ↓
Identify Affected Hosts
           ↓
Create Investigation Ticket
           ↓
Analyst Validation
           ↓
Response Action if Approved
```


L'intérêt est d'automatiser les tâches répétitives tout en conservant la possibilité d'une validation humaine avant les décisions sensibles.

### Solutions SOAR présentées

|Solution|Fonctionnalités|
|---|---|
|Splunk Phantom|Playbooks automatisés, intégrations avec les outils de sécurité, Incident Response|
|IBM Resilient|Gestion des incidents, workflows et orchestration des réponses|
|Demisto / Cortex XSOAR|Automatisation des playbooks, intégration CTI et coordination des investigations|

Appellations actuelles : Splunk Phantom est devenu Splunk SOAR, IBM Resilient a été intégré à IBM QRadar SOAR, et Demisto est devenu Palo Alto Networks Cortex XSOAR.

## 4. Application au Threat Hunting

L'intégration et l'automatisation facilitent plusieurs étapes du hunt.

|Étape|Apport de l'automatisation|
|---|---|
|Data Collection|Collecte et centralisation des logs|
|IOC Hunting|Recherche automatisée d'indicateurs|
|Enrichment|Consultation de sources CTI|
|Investigation|Rassemblement des événements pertinents|
|Reporting|Génération de tickets et rapports|
|Incident Response|Exécution d'actions de remédiation selon les règles définies|

### Exemple : recherche d'un malware connu

Un rapport CTI publie de nouveaux hashes malveillants.

1. Les hashes sont intégrés à la plateforme CTI.
    
2. Le SIEM ou l'EDR recherche les correspondances dans la télémétrie disponible.
    
3. Les résultats sont enrichis avec le contexte des machines concernées.
    
4. Un playbook peut préparer un dossier d'investigation.
    
5. L'analyste valide les résultats et détermine les actions nécessaires.
    

Cela réduit le temps consacré aux recherches et enrichissements manuels.

## 5. Limites et précautions

- Automation ≠ Threat Hunting complet : les hypothèses, l'interprétation des résultats et les décisions complexes restent des activités analytiques.
    
- False Positives : une détection incorrecte peut entraîner une mauvaise décision automatisée.
    
- Response Impact : bloquer une IP ou isoler un serveur critique peut perturber les opérations.
    
- Data Quality : des données incomplètes ou mal normalisées produisent des corrélations peu fiables.
    
- Human Validation : les actions à fort impact doivent être soumises à des contrôles adaptés.
    

La distinction essentielle :

- SIEM : centralise et corrèle les événements.
    
- SOAR : orchestre et automatise les workflows.
    
- EDR / NDR : fournissent la télémétrie et certaines capacités de détection ou de réponse.
    
- CTI : apporte le contexte externe sur les menaces.
    

En Threat Hunting, l'intégration améliore la visibilité, tandis que l'automatisation accélère la collecte, l'enrichissement et les investigations, sans remplacer le jugement du Threat Hunter.
