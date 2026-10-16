---
title: Outils EDR — Endpoint Detection & Response
source: Cyber/06 Détection & réponse/Threat hunting/Outils de threat hunting.md
note: Outils de threat hunting
up:
- - Outils de threat hunting
  - index.md
---

Les EDR (Endpoint Detection & Response) sont des solutions de sécurité permettant de surveiller, détecter, investiguer et répondre aux activités malveillantes sur les endpoints : postes de travail, serveurs et autres terminaux compatibles.

Ils jouent un rôle essentiel dans le Threat Hunting grâce à leur visibilité sur les comportements exécutés directement sur les systèmes.

Les fonctionnalités d'un EDR et les principales solutions du marché (CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint, Cybereason, Cortex XDR) sont détaillées à l'étape 3 du parcours : [fonctionnalités d'un EDR](../edr-xdr-detection-analyse-et-regles/01-xdr-edr-introduction.md) et [comparaison des produits EDR/XDR](../edr-xdr-detection-analyse-et-regles/02-common-xdr-edr-products.md).

## 1. Utilisation opérationnelle en Threat Hunting

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

Isolation, arrêt de processus, quarantaine, remédiation, investigation à distance : voir [les capacités de réponse d'un EDR](../edr-xdr-detection-analyse-et-regles/01-xdr-edr-introduction.md#edr-response-capabilities) (étape 3).

Points de vigilance :

- Une alerte EDR ne constitue pas automatiquement une compromission confirmée.
    
- L'absence d'alerte ne garantit pas qu'un endpoint soit sain.
    
- L'isolation d'un serveur critique peut avoir un impact opérationnel important.
    
- Avant une action destructive, préserver les preuves nécessaires à l'investigation lorsque la situation le permet.
    

## 2. EDR vs Antivirus traditionnel

|Antivirus traditionnel|EDR|
|---|---|
|Principalement orienté prévention et détection des malwares|Détection, investigation et réponse endpoint|
|Analyse de fichiers et de comportements selon le produit|Télémétrie approfondie sur les activités système|
|Quarantaine et suppression des menaces|Investigation des chaînes d'attaque et actions de réponse|
|Visibilité historique parfois limitée|Recherche rétrospective selon la rétention disponible|

Cette distinction n'est pas absolue : les antivirus modernes intègrent également des mécanismes comportementaux et certaines fonctionnalités avancées.

En Threat Hunting, la valeur principale de l'EDR réside dans sa capacité à relier les comportements suspects à leur contexte d'exécution, afin de reconstruire une attaque, évaluer son étendue et guider l'Incident Response.
