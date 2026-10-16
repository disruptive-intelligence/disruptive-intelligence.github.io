---
title: Hypothesis-Driven Approach
source: Cyber/06 Détection & réponse/Threat hunting/Threat hunting — introduction et méthodes.md
note: Threat hunting — introduction et méthodes
up:
- - Threat hunting — introduction et méthodes
  - index.md
---

L'approche Hypothesis-Driven est une méthodologie de Threat Hunting consistant à formuler puis tester une hypothèse concernant une activité malveillante potentielle.

Contrairement à une recherche exploratoire sans objectif précis, elle permet de concentrer les investigations sur un scénario déterminé.

- Hypothesis Generation : formuler une supposition à partir d'observations, de données historiques ou de Threat Intelligence.
    
- Hypothesis Testing : collecter et analyser les données permettant de vérifier cette supposition.
    
- Analytical Models : utiliser des méthodes statistiques ou analytiques pour identifier des anomalies et interpréter les résultats.
    

```
Observation / Threat Intelligence
            ↓
     Hypothesis Creation
            ↓
       Data Collection
            ↓
     Analysis / Testing
            ↓
  Confirm / Reject / Inconclusive
            ↓
 Detection Improvement / Response
```


## 1. Creating a Hypothesis

Une hypothèse est une supposition argumentée concernant une menace ou un comportement potentiellement malveillant.

Elle peut être construite à partir de :

- Threat Intelligence : campagnes, IOCs, TTPs.
    
- Historical Data : incidents et comportements précédemment observés.
    
- Network / Endpoint Telemetry : trafic ou activités inhabituelles.
    
- Security Baselines : comparaison avec le fonctionnement habituel.
    

### Exemple

Observation : augmentation anormale du trafic réseau sur une période donnée.

Hypothèse : cette augmentation pourrait correspondre à une attaque DDoS.

```
Unusual Network Traffic
          ↓
Hypothesis:
"Potential DDoS Attack"
```


Une hypothèse efficace doit être :

- Specific : viser un comportement identifiable.
    
- Testable : pouvoir être vérifiée avec les données disponibles.
    
- Falsifiable : permettre d'identifier des éléments susceptibles de la réfuter.
    

L'objectif est d'éviter de rechercher des activités suspectes sans disposer d'une question précise à laquelle répondre.

## 2. Hypothesis Testing

Le Hypothesis Testing consiste à examiner les données pour déterminer si elles soutiennent ou contredisent l'hypothèse.

Étapes principales :

1. Data Collection : récupérer les logs pertinents.
    
2. Data Analysis : rechercher les comportements attendus.
    
3. Correlation : comparer les résultats avec d'autres sources.
    
4. Conclusion : évaluer si les observations soutiennent l'hypothèse.
    

### Exemple — Trafic réseau anormal

Sources pertinentes :

- Firewall Logs ;
    
- NetFlow ;
    
- IDS/IPS ;
    
- Network Monitoring.
    

Éléments à examiner :

- Source / Destination IP ;
    
- Packet Rate / Traffic Volume ;
    
- Protocol / Port ;
    
- Time Window ;
    
- Traffic Patterns.
    

```
Hypothesis: DDoS
       ↓
Analyze Network Traffic
       ↓
Abnormal Volume / Request Rate?
       ↓
Suspicious Traffic Pattern?
       ↓
Evaluate Hypothesis
```


⚠️ Une anomalie ne confirme pas automatiquement une attaque. Une hausse du trafic peut également provenir d'un backup, d'un transfert massif ou d'une activité légitime.

De même, l'absence d'éléments concluants ne signifie pas nécessairement que l'hypothèse est fausse : la télémétrie peut être insuffisante.

## 3. Using Analytical Models

Les Analytical Models utilisent des méthodes mathématiques et statistiques pour extraire des informations exploitables à partir de grands volumes de données.

Ils peuvent notamment servir à :

- identifier les comportements habituels (Baseline) ;
    
- détecter les écarts significatifs ;
    
- analyser les tendances ;
    
- repérer des anomalies ;
    
- faciliter la validation d'hypothèses.
    

### Machine Learning

Le Machine Learning sert à apprendre les patterns habituels du trafic réseau et identifier leurs variations.

```
Historical Network Traffic
          ↓
     Learn Baseline
          ↓
   Current Traffic
          ↓
 Anomaly Detection
          ↓
  Analyst Validation
```


Le Machine Learning est une méthode possible, mais pas une condition nécessaire au Hypothesis-Driven Hunting. Des requêtes SIEM, des seuils statistiques et des analyses manuelles peuvent également suffire.

## 4. Case Study — DDoS Attack

### Scénario

Une organisation observe une forte augmentation du trafic réseau pendant une période spécifique.

Hypothesis : cette activité pourrait indiquer une attaque Distributed Denial of Service (DDoS).

### Data Collection

Collecte des logs de trafic réseau afin d'examiner :

- les adresses IP sources ;
    
- les systèmes ciblés ;
    
- les volumes et fréquences des communications ;
    
- les périodes d'activité.
    

### Analysis

Des algorithmes de Machine Learning servent à :

- déterminer le trafic normal ;
    
- détecter les écarts ;
    
- identifier des volumes anormalement élevés provenant de certaines IP.
    

### Conclusion

L'analyse fait apparaître un trafic anormal provenant d'adresses IP spécifiques, interprété dans le scénario comme une attaque DDoS.

Précision technique : un volume élevé provenant de plusieurs IP est un indicateur potentiel, mais ne suffit pas à confirmer un DDoS.

Pour renforcer cette conclusion, examiner notamment :

- la répartition des sources ;
    
- le nombre de requêtes ou paquets par seconde ;
    
- le service ciblé ;
    
- les erreurs, timeouts ou dégradations de disponibilité ;
    
- les patterns réseau compatibles avec une attaque.
    

### Intervention

Mesures proposées :

- le blocage des IP identifiées ;
    
- le renforcement des mesures de sécurité réseau.
    

Dans un véritable scénario DDoS, le blocage individuel des IP peut être insuffisant. Selon la nature de l'attaque, des mesures de Rate Limiting, de filtrage en amont ou de protection anti-DDoS peuvent être nécessaires.

```
Traffic Spike
     ↓
DDoS Hypothesis
     ↓
Network Logs + Baseline Analysis
     ↓
Suspicious Traffic Confirmed?
     ↓
Assess Service Impact
     ↓
Containment / Mitigation
```


## 5. Résultats d'un Hypothesis-Driven Hunt

Une investigation peut aboutir à trois résultats :

| Résultat              | Interprétation                                                                       |     |
| --------------------- | ------------------------------------------------------------------------------------ | --- |
| Supported / Confirmed | Les preuves soutiennent l'hypothèse ; une activité malveillante peut être identifiée |     |
| Rejected              | Les données permettent d'expliquer l'activité autrement                              |     |
| Inconclusive          | Les preuves sont insuffisantes pour conclure                                         |     |

Le résultat d'un hunt doit être documenté et peut conduire à :

- l'ouverture d'une investigation ou d'un incident ;
    
- la création ou l'amélioration de règles de détection ;
    
- l'ajustement des baselines ;
    
- l'identification de données manquantes ;
    
- la formulation de nouvelles hypothèses.
    

Hypothesis-Driven Hunting : une hypothèse précise → des données pertinentes → une analyse vérifiable → une conclusion fondée sur les preuves.
