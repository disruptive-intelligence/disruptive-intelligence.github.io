---
title: 3 Choses Importantes
source: IT/02 Windows/Journaux & investigation/Réponse à incident sous Windows (Windows Incident Response).md
note: Réponse à incident sous Windows (Windows Incident Response)
up:
- - Réponse à incident sous Windows (Windows Incident Response)
  - index.md
---

Lorsqu'un système est compromis ou suspecté de l'être, l'analyste doit répondre à 3 questions fondamentales pour orienter son investigation.

1. Active Malware : un logiciel malveillant est-il actuellement en cours d'exécution ?
    
2. Suspicious Network Communication : existe-t-il des communications internes ou externes suspectes ?
    
3. Persistence : l'attaquant a-t-il mis en place un mécanisme permettant de conserver son accès ?
    

Ces trois axes permettent d'identifier une activité malveillante active, d'analyser les interactions réseau et de rechercher d'éventuelles backdoors.

## 1. Active Malware — Analyse des processus

Objectif : déterminer si un malware ou un processus malveillant s'exécute actuellement sur le système.

La méthode principale est la Process Analysis.

Elle consiste notamment à examiner :

- les processus actifs ;
    
- leurs relations Parent / Child Process ;
    
- les exécutions inhabituelles ;
    
- les comportements pouvant indiquer une activité malveillante.
    

### Exemple — Excel → PowerShell

```
excel.exe
    └── powershell.exe
```


Un processus `powershell.exe` lancé par `excel.exe` constitue une activité suspecte à investiguer.

Cette relation peut notamment indiquer qu'un document Office a déclenché l'exécution d'une commande.

Point d'analyse : une relation parent/enfant inhabituelle est un indicateur, pas une preuve suffisante de compromission.

### Analyse rétrospective

Si un processus malveillant est identifié, l'analyste peut effectuer une Retroactive Analysis pour déterminer :

- comment le malware est arrivé sur le système ;
    
- quel processus a déclenché son exécution ;
    
- quelles activités ont précédé son lancement.
    

## 2. Suspicious Network Communication

Objectif : identifier d'éventuelles communications utilisées par l'attaquant pour contrôler le système, interagir avec d'autres machines ou exfiltrer des données.

L'analyse concerne les connexions :

- Internal / East-West : entre systèmes du réseau interne.
    
- External / North-South : entre le système et des destinations externes.
    

Il faut examiner les connexions actuelles et, lorsque les données sont disponibles, les communications historiques.

### Indicateurs à rechercher

|Indicateur|Investigation|
|---|---|
|Malicious IP Reputation|Connexion vers une IP connue pour être associée à des activités malveillantes|
|Unusual Data Volume|Transfert de plusieurs Go vers une destination inhabituelle|
|Abnormal Ports|Connexions sur des ports inattendus|
|Unexpected Communications|Connexions non cohérentes avec le rôle du système|

### Activités potentielles

- Command & Control (C2) : communication avec une infrastructure contrôlée par l'attaquant.
    
- Data Exfiltration : transfert non autorisé de données.
    
- Internal Communication : interactions suspectes avec d'autres machines internes.
    

Point d'analyse : une IP de mauvaise réputation, un volume important ou un port inhabituel justifient une investigation, mais ne confirment pas individuellement une attaque.

La corrélation avec les processus, utilisateurs et événements endpoint permet d'évaluer ces communications.

## 3. Persistence — Maintien de l'accès

Objectif : déterminer si l'attaquant a installé un mécanisme permettant de conserver ou de retrouver l'accès au système.

Après une compromission, un attaquant peut souhaiter :

- revenir ultérieurement sur le système ;
    
- poursuivre une opération interrompue ;
    
- conserver une Backdoor pour un accès futur.
    

### Pourquoi rechercher la Persistence ?

L'absence de malware actif ou de trafic réseau suspect ne garantit pas qu'un système soit sain.

Exemple : une backdoor peut être configurée pour s'exécuter seulement une fois par semaine.

```
System Compromised
        ↓
Persistence Installed
        ↓
No Current Malicious Activity
        ↓
Delayed Execution
        ↓
Attacker Regains Access
```


Il est donc nécessaire de rechercher les mécanismes de persistence, même lorsqu'aucune activité malveillante n'est visible au moment de l'analyse.

### Complément Windows — Artefacts à examiner

Quelques emplacements et mécanismes pertinents pour cette recherche :

- Scheduled Tasks : tâches planifiées suspectes.
    
- Windows Services : services nouvellement installés ou modifiés.
    
- Registry Run Keys : exécution automatique à l'ouverture d'une session.
    
- Startup Folders : programmes lancés automatiquement.
    
- Backdoor Accounts : comptes ou accès créés pour conserver une présence.
    

Les procédures techniques détaillées sont abordées dans les sections suivantes.

## 4. Workflow d'investigation

```
Suspected Compromise
         ↓
1. Active Malware?
   → Process Analysis
         ↓
2. Suspicious Communications?
   → Network Analysis
         ↓
3. Persistence?
   → Persistence Analysis
         ↓
Correlate Findings
         ↓
Determine Next Investigation Steps
```


|Question|Analyse principale|Ce qu'on cherche|
|---|---|---|
|Active Malware ?|Process Analysis|Processus malveillants ou exécutions suspectes|
|Suspicious Communication ?|Network Analysis|C2, transferts inhabituels, connexions suspectes|
|Persistence ?|Persistence Analysis|Backdoors et mécanismes d'exécution différée|

Ces trois questions sont complémentaires. Un attaquant peut avoir quitté le système, interrompu ses communications ou programmé une exécution future.

La recherche doit donc porter à la fois sur les activités présentes, les traces historiques et les mécanismes susceptibles de réactiver la menace.
