---
title: Incident Response on Windows
source: IT/02 Windows/Journaux & investigation/Réponse à incident sous Windows (Windows Incident Response).md
note: Réponse à incident sous Windows (Windows Incident Response)
up:
- - Réponse à incident sous Windows (Windows Incident Response)
  - index.md
---

L'Incident Response (IR) est un processus structuré permettant d'identifier, contenir, éliminer et gérer les conséquences d'un incident de sécurité.

Un Incident Response Plan (IRP) définit les responsabilités, procédures et moyens nécessaires pour traiter un incident de manière cohérente et efficace.

Six phases principales :
	1- Préparation
	2- Identification
	3- Périmètre
	4- Éradication
	5- Rétablissement
	6- Leçons apprises
## 1. Preparation — Préparation

La phase de préparation consiste à mettre en place les ressources techniques, organisationnelles et procédurales nécessaires avant qu'un incident ne survienne.

### Centralisation des logs

Mettre en place un système centralisé de collecte et de consultation des logs.

Objectifs :

- Accéder rapidement aux événements de plusieurs systèmes.
    
- Faciliter les recherches et les corrélations.
    
- Gérer de grands volumes de données.
    
- Réduire le temps nécessaire aux investigations.
    

### Synchronisation de l'heure — NTP

Synchroniser les horloges des équipements avec NTP (Network Time Protocol).

L'objectif est de pouvoir corréler les événements provenant de différents systèmes et reconstruire une timeline cohérente.

Précision opérationnelle : les logs peuvent utiliser des fuseaux horaires différents ; leur normalisation en UTC facilite les investigations.

### Gestion des comptes utilisateurs

Organiser les comptes utilisateurs pour pouvoir identifier leurs activités.

Recommandations :

- une convention de nommage cohérente ;
    
- des identifiants permettant de distinguer les utilisateurs ;
    
- la possibilité de relier les différents comptes appartenant à une même personne.
    

Cette organisation améliore la traçabilité pendant les investigations.

### Gestion des comptes système et de service

Documenter les comptes système et de service, ainsi que les responsables des systèmes associés.

Les équipes IR doivent pouvoir identifier et contacter rapidement les administrateurs concernés.

### Gestion des actifs

Maintenir un inventaire contenant notamment :

- les équipements et systèmes ;
    
- les systèmes d'exploitation ;
    
- les versions de correctifs ;
    
- la criticité des actifs.
    

Ces informations facilitent l'identification des systèmes affectés et la priorisation des interventions.

### Communication sécurisée

Prévoir des moyens de communication indépendants de l'infrastructure potentiellement compromise.

Exemples :

- téléphones mobiles ;
    
- adresses email secondaires.
    

Ces canaux doivent être suffisamment sécurisés pour permettre la coordination de l'Incident Response.

### Legal Procedures

Définir à l'avance :

- les circonstances nécessitant une procédure judiciaire ;
    
- les personnes habilitées à la déclencher ;
    
- les responsabilités associées.
    

## 2. Identification

La phase d'Identification vise à déterminer si un événement suspect constitue réellement un incident de sécurité.

### Initial Examination

Collecter les premières informations concernant l'événement.

L'objectif est de comprendre :

- ce qui a été observé ;
    
- quels systèmes sont concernés ;
    
- quels éléments rendent l'événement suspect ;
    
- si une investigation plus approfondie est nécessaire.
    

Security Event ≠ Security Incident : un événement suspect doit être évalué avant d'être qualifié d'incident.

### Incident Assignment

Désigner une personne responsable de la première analyse.

Cette personne doit documenter ses observations et les actions réalisées.

### Investigation Checklists

Utiliser des checklists pour standardiser l'analyse.

Elles permettent :

- d'éviter les oublis ;
    
- d'assurer la cohérence des investigations ;
    
- de faciliter le transfert du dossier entre analystes.
    

## 3. Scoping & Containment — Périmètre

La phase Périmètre regroupe l'évaluation de l'incident, la collecte de preuves et les premières actions de confinement.

L'objectif est de déterminer les systèmes affectés et d'empêcher la propagation de l'attaque.

### Caractériser l'événement
Identifier la nature de l'incident afin de sélectionner les actions adaptées.

Exemples :

- DDoS ;
- Malware Infection ;
- Data Breach ;
- Account Compromise.

### Prise de mesures

Appliquer des mesures correspondant aux techniques de l'attaquant.

Exemples mentionnés :

- désactiver un compte compromis ;
    
- bloquer une adresse IP malveillante ;
    
- limiter les communications suspectes ;
    
- isoler un système compromis.
    

L'isolation est préférable à un simple débranchement du système.

L'isolation permet de limiter les communications de l'attaquant tout en conservant, selon la méthode utilisée, certaines possibilités d'investigation à distance.

### Collecte de données

Collecter les informations nécessaires à l'investigation :

- Memory Acquisition : image de la mémoire volatile ;
    
- Firewall Logs ;
    
- Network Traffic ;
    
- autres journaux pertinents.
    

La mémoire volatile peut contenir des informations qui disparaissent lors d'un arrêt ou redémarrage du système.

Précision opérationnelle : la collecte des preuves et les actions de confinement doivent être coordonnées selon l'urgence. En présence d'une attaque active, il peut être nécessaire de contenir immédiatement la menace, même si toutes les preuves volatiles n'ont pas encore été préservées.

### Conditions de passage à l'éradication

Il faut avoir :

- identifié les systèmes affectés ;
    
- empêché la propagation de l'attaquant ;
    
- collecté les informations volatiles nécessaires.
    

## 4. Eradication — Éradication

L'Eradication vise à supprimer la menace et à traiter les faiblesses qui ont permis la compromission.

### Identification de la cause racine

Identifier la Root Cause à partir des éléments collectés pendant les phases précédentes.

Questions essentielles :

- Comment l'attaquant a-t-il obtenu l'accès ?
    
- Quelles vulnérabilités ou faiblesses ont été exploitées ?
    
- Quels mécanismes malveillants restent présents ?
    

L'objectif est d'éliminer la menace, pas uniquement de supprimer le premier fichier malveillant identifié.

### Rootkit Investigation

Lorsqu'un Rootkit est suspecté, il faut nettoyer le disque et de réinstaller le système à partir d'une source saine, puis d'appliquer les mises à jour nécessaires.

Une compromission profonde peut rendre le système insuffisamment fiable pour un simple nettoyage.

### Security Hardening

Identifier et corriger les faiblesses défensives concernant :

- systèmes d'exploitation ;
    
- applications ;
    
- réseau interne ;
    
- DMZ ;
    
- autres composants exposés.
    

### Vulnerability Assessment

Effectuer des analyses de vulnérabilités afin d'identifier et de corriger les points d'attaque potentiels.

La phase d'éradication doit réduire le risque que l'attaquant exploite de nouveau les mêmes faiblesses.

## 5. Recovery — Rétablissement

La Recovery consiste à restaurer les services et systèmes dans un état opérationnel et sûr.

### System Verification

Vérifier le fonctionnement des composants concernés :

- journalisation ;
    
- systèmes d'exploitation ;
    
- applications ;
    
- bases de données ;
    
- services et opérations métier.
    

### Restoration

Coordonner les opérations nécessaires au rétablissement :

- restauration des systèmes ;
    
- récupération des données ;
    
- remise en service des composants affectés.
    

### Post-Recovery Monitoring

Surveiller les systèmes restaurés pour identifier :

- une réapparition de l'activité malveillante ;
    
- de nouvelles anomalies ;
    
- une éventuelle persistance de l'attaquant.
    

Le passage à la phase suivante intervient lorsque les activités suspectes ont été traitées et que le fonctionnement de l'environnement est jugé satisfaisant.

## 6. Lessons Learned — Leçons apprises

La dernière phase vise à analyser le déroulement de l'incident afin d'améliorer les futures réponses.

### Post-Incident Report

Rédiger un rapport de suivi comprenant :

- les résultats de l'investigation ;
    
- les échanges et conclusions avec les experts et la direction ;
    
- les procédures qui ont bien fonctionné ;
    
- les difficultés rencontrées ;
    
- les améliorations recommandées ;
    
- la justification de la clôture de l'incident.
    

Le rapport doit permettre aux responsables de comprendre pourquoi l'incident peut être considéré comme clôturé.

### Process Improvement

Les conclusions du rapport servent à améliorer :

- les procédures d'Incident Response ;
    
- les checklists ;
    
- la préparation organisationnelle ;
    
- les mesures de protection ;
    
- les capacités de détection.
    

## 7. Synthèse du processus

|Phase|Objectif|
|---|---|
|Preparation|Préparer les outils, responsabilités et procédures|
|Identification|Examiner et qualifier l'événement suspect|
|Scoping / Containment|Déterminer le périmètre, préserver les preuves et limiter la propagation|
|Eradication|Supprimer la menace et corriger la cause racine|
|Recovery|Restaurer et surveiller les systèmes affectés|
|Lessons Learned|Documenter l'incident et améliorer les processus|

Le principe fondamental de l'Incident Response est de traiter l'incident dans son ensemble, depuis l'identification initiale jusqu'à la restauration et l'amélioration des défenses.

Dans un environnement Windows, les éléments de préparation les plus importants pour les investigations sont notamment la centralisation des logs, la synchronisation temporelle, la gestion des identités et l'inventaire des actifs.
