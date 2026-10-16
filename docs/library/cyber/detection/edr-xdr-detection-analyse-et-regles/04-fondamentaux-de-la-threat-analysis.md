---
title: Fondamentaux de la Threat Analysis
source: Cyber/06 Détection & réponse/Threat hunting/EDR & XDR — détection, analyse et règles.md
note: EDR & XDR — détection, analyse et règles
up:
- - EDR & XDR — détection, analyse et règles
  - index.md
---

La Threat Analysis est un processus d'identification et d'évaluation des cybermenaces susceptibles d'affecter les actifs d'une organisation.

Elle permet de comprendre :

- WHO : quels Threat Actors représentent une menace ?
    
- HOW : quels vecteurs d'attaque peuvent être utilisés ?
    
- WHAT : quels actifs sont exposés ?
    
- HOW LIKELY : quelle est la probabilité d'une attaque ?
    
- HOW SEVERE : quelles seraient ses conséquences ?
    

Son objectif est de prioriser les risques et d'adapter les stratégies de protection, de détection et de réponse.

## 1. Threat — Définition d'une menace

Une Threat désigne une activité, un acteur ou un événement susceptible de compromettre les actifs numériques d'une organisation.

Exemples :

- Cyberespionage ;
    
- Cybercrime / Ransomware ;
    
- Hacktivism ;
    
- Insider Threats ;
    
- exploitation de vulnérabilités.
    

### Insider Threat

Une Insider Threat est une menace provenant d'une personne disposant d'un accès légitime aux ressources de l'organisation.

Deux situations possibles :

- Malicious Insider : employé utilisant volontairement ses accès à des fins malveillantes.
    
- Negligent / Accidental Insider : employé provoquant involontairement un incident par erreur ou négligence.
    

L'accès légitime ne signifie donc pas automatiquement que toutes les actions réalisées sont autorisées ou sûres.

## 2. Threat Actors

Les Threat Actors sont les individus, groupes ou organisations susceptibles de mener des activités malveillantes.

|Threat Actor|Motivations principales|
|---|---|
|State-Sponsored / APT|Espionnage, intérêts stratégiques, sabotage|
|Cybercriminals|Gain financier, fraude, extorsion|
|Hacktivists|Motivations politiques ou idéologiques|
|Malicious Insiders|Vol de données, sabotage, intérêts personnels|

Chaque Threat Actor possède :

- des motivations ;
    
- des capacités techniques ;
    
- des ressources ;
    
- des outils ;
    
- des TTPs (Tactics, Techniques & Procedures).
    

Comprendre ces caractéristiques aide à déterminer quels adversaires et scénarios d'attaque sont pertinents pour l'organisation.

Précision : une APT désigne généralement un acteur ou une campagne caractérisée par des capacités et une persistance avancées ; cela n'implique pas systématiquement une attribution étatique confirmée.

## 3. Threat Vectors — Vecteurs d'attaque

Un Threat Vector / Attack Vector correspond au moyen ou chemin utilisé par un attaquant pour atteindre ou compromettre une cible.

Exemples :

- Email Attachments : pièces jointes malveillantes.
    
- Browser Exploitation : exploitation de vulnérabilités du navigateur.
    
- Removable Media : clés USB compromises.
    
- Social Engineering : manipulation d'utilisateurs pour obtenir un accès ou des informations.
    

Identifier les vecteurs d'attaque permet de sélectionner des mesures défensives adaptées : filtrage des emails, patching, contrôles d'accès, sensibilisation, etc.

## 4. Asset Evaluation

L'Asset Evaluation consiste à identifier, classifier et déterminer la valeur des actifs d'une organisation.

Actifs concernés :

- serveurs et endpoints ;
    
- applications ;
    
- bases de données ;
    
- infrastructures réseau ;
    
- informations sensibles ;
    
- propriété intellectuelle et secrets commerciaux.
    

L'évaluation doit déterminer :

- Asset Inventory : quels actifs existent ?
    
- Asset Location : où se trouvent-ils ?
    
- Asset Criticality : quelle est leur importance ?
    
- Business Impact : quelles seraient les conséquences de leur compromission ?
    

Une base de données contenant des informations critiques peut nécessiter une priorité de protection supérieure à un environnement de test peu sensible.

La criticité dépend du contexte métier, pas uniquement de la valeur technique de l'actif.

## 5. Threat Probability & Impact Assessment

### Threat Probability — Probabilité

La Threat Probability représente la probabilité qu'une menace affecte un actif ou un système.

Facteurs pris en compte :

- capacités des Threat Actors ;
    
- mesures de sécurité existantes ;
    
- caractéristiques et criticité de la cible.
    

En pratique, l'exposition de l'actif et l'exploitation active de vulnérabilités peuvent également influencer cette estimation.

### Impact Assessment — Impact

L'Impact Assessment évalue les conséquences potentielles si une menace se réalise.

|Type d'impact|Exemples|
|---|---|
|Financial|Pertes financières, coûts de remédiation|
|Operational|Interruption des services et processus métier|
|Reputational|Perte de confiance, atteinte à l'image|
|Legal / Regulatory|Sanctions, obligations réglementaires|
|Data Loss|Perte, divulgation ou altération d'informations|

### Risk Assessment

La combinaison de la probabilité et de l'impact permet d'estimer le niveau de risque.

Risk = probabilité x Impact

Cette relation est un modèle simplifié de priorisation, et non une formule universelle de mesure du risque.

Deux menaces peuvent présenter une probabilité similaire mais des impacts très différents.

## 6. Threat–Vulnerability Relationship

Une vulnérabilité est une faiblesse pouvant être exploitée par une menace.

Il est important de déterminer si une menace peut réellement exploiter une vulnérabilité présente dans l'organisation.

Exemple :

- Un Threat Actor exploite une vulnérabilité dans une version précise d'un logiciel.
    
- L'organisation utilise cette version vulnérable.
    
- Le système concerné est accessible par un chemin permettant l'exploitation.
    
- Le risque d'attaque devient pertinent et doit être évalué.
    

À l'inverse, si la version vulnérable n'est pas présente, ce scénario d'exploitation précis ne s'applique pas directement.

Précision : une attaque ne nécessite pas toujours une vulnérabilité logicielle de type CVE. Des credentials volés, des mauvaises configurations ou des abus d'accès légitimes peuvent également permettre une compromission.

### Distinctions fondamentales

|Concept|Signification|
|---|---|
|Threat|Source potentielle de dommage|
|Vulnerability|Faiblesse exploitable|
|Risk|Possibilité de conséquences négatives compte tenu du contexte|
|Impact|Gravité des conséquences si l'événement se produit|

## 7. Threat Rate

Le Threat Rate désigne la fréquence à laquelle un type d'événement de menace est observé sur une période donnée.

Exemple :

- Nombre de campagnes de phishing observées par mois.
    
- Fréquence d'événements de sécurité associés à une menace.
    
- Évolution des activités malveillantes dans un secteur.
    

Les données peuvent provenir :

- des logs et incidents internes ;
    
- de rapports CTI ;
    
- de renseignements externes.
    

### Threat Rate vs Threat Probability

- Threat Rate : fréquence observée d'événements sur une période.
    
- Threat Probability : estimation de la probabilité qu'une menace affecte un actif donné.
    

Un Threat Rate élevé n'implique pas automatiquement un risque élevé. Il faut également examiner l'exposition, les protections existantes et l'impact potentiel.

Par exemple, une organisation peut observer un très grand nombre de tentatives de scan bloquées sans subir de compromission.

## 8. Preventive & Mitigation Strategies

La Threat Analysis doit déboucher sur des mesures défensives concrètes.

### Preventive Strategies

Les mesures préventives visent à réduire la probabilité qu'une menace aboutisse.

Exemples :

- Firewall ;
    
- MFA / Authentication Controls ;
    
- Patch Management ;
    
- Hardening ;
    
- contrôles d'accès ;
    
- surveillance proactive.
    

### Mitigation Strategies

Les mesures de mitigation visent à limiter les conséquences d'une menace lorsqu'un incident survient.

Exemples complémentaires :

- isolation d'endpoints compromis ;
    
- containment réseau ;
    
- révocation de credentials ;
    
- sauvegardes et restauration ;
    
- procédures d'Incident Response.
    

Les deux approches sont complémentaires : Prevention réduit la probabilité de succès, tandis que Mitigation cherche à limiter l'impact.

## 9. Application à l'EDR/XDR

Application opérationnelle de ces concepts.

La Threat Analysis aide les équipes SOC à adapter leurs recherches et leurs détections aux risques réels de l'organisation.

Exemple : une organisation utilise une application critique exposée à Internet et menacée par une campagne d'exploitation connue.

|Étape|Application|
|---|---|
|Threat Identification|Identifier la campagne et les Threat Actors associés|
|Asset Evaluation|Déterminer les serveurs et données concernés|
|Vulnerability Assessment|Vérifier la version utilisée, l'exposition et les protections|
|Probability & Impact|Évaluer la vraisemblance de l'attaque et ses conséquences|
|Threat Hunting|Rechercher des comportements d'exploitation et de post-exploitation|
|Detection & Response|Adapter les règles et prévoir les actions de containment|

L'EDR permet d'investiguer les comportements observés sur les endpoints, tandis que le XDR peut les corréler avec d'autres événements réseau, applicatifs ou cloud.

La Threat Analysis permet ainsi de passer d'une menace théorique à une priorisation fondée sur les actifs, l'exposition, la probabilité et l'impact, puis à des actions défensives adaptées.
