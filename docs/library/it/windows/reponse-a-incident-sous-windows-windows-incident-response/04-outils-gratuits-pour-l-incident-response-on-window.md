---
title: Outils gratuits pour l'Incident Response on Windows
source: IT/02 Windows/Journaux & investigation/Réponse à incident sous Windows (Windows Incident Response).md
note: Réponse à incident sous Windows (Windows Incident Response)
up:
- - Réponse à incident sous Windows (Windows Incident Response)
  - index.md
---

Lors d'une investigation sur un système Windows compromis ou suspecté de l'être, plusieurs outils gratuits permettent d'accélérer la collecte et l'analyse des informations.

L'objectif est de réduire le temps d'investigation, notamment lorsqu'une attaque est toujours en cours, et de faciliter l'identification des processus suspects, des événements Windows et des mécanismes de Persistence.

## 1. Process Hacker — Process Analysis

Process Hacker permet d'analyser en détail les processus actifs d'un système Windows.

Il est utilisé pour examiner l'activité des processus et rechercher d'éventuelles exécutions suspectes.

- Process Analysis : inspection des processus en cours d'exécution.
    
- Parent / Child Processes : analyse des relations entre processus.
    
- Suspicious Execution : recherche de processus ou comportements inhabituels.
    

Application IR : déterminer si un malware est actuellement actif sur le système.

Téléchargement : [Process Hacker](https://processhacker.sourceforge.io/downloads.php?utm_source=chatgpt.com)

## 2. FullEventLogView — Windows Event Log Analysis

FullEventLogView, développé par NirSoft, permet de consulter les Windows Event Logs dans une interface centralisée.

Il facilite l'examen des événements enregistrés par Windows.

- Regrouper les journaux Windows dans une seule interface.
    
- Appliquer des filtres pour réduire le volume d'événements à examiner.
    
- Rechercher les événements associés à une période d'attaque connue.
    

Application IR : reconstituer les activités enregistrées pendant une période suspecte et identifier les événements pertinents pour l'investigation.

Téléchargement : [FullEventLogView](https://www.nirsoft.net/utils/full_event_log_view.html?utm_source=chatgpt.com)

## 3. Autoruns — Persistence Analysis

Autoruns est un outil de la suite Microsoft Sysinternals, spécialisé dans l'analyse des mécanismes d'exécution automatique.

Il permet d'identifier des éléments susceptibles de lancer des programmes sans intervention directe de l'utilisateur.

Application IR : rechercher les mécanismes de Persistence qu'un attaquant pourrait avoir configurés afin de conserver son accès au système.

Il est particulièrement utile lorsque l'attaquant ne présente aucune activité malveillante visible au moment de l'investigation.

Téléchargement : [Autoruns — Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns?utm_source=chatgpt.com)

## 4. LastActivityView — User & System Activity

LastActivityView, développé par NirSoft, collecte des informations issues de plusieurs sources Windows afin de présenter les activités observées sur le système.

Il facilite l'analyse chronologique des événements.

- Regrouper les activités provenant de différentes sources.
    
- Examiner l'historique des actions réalisées.
    
- Filtrer les événements selon une période précise.
    

Application IR : identifier les activités qui se sont produites pendant la fenêtre temporelle suspectée de l'attaque.

Téléchargement : [LastActivityView](https://www.nirsoft.net/utils/computer_activity_view.html?utm_source=chatgpt.com)

## 5. BrowsingHistoryView — Browser History Analysis

BrowsingHistoryView, développé par NirSoft, permet de consulter les historiques de navigation web dans une interface unique.

Il est utile pour examiner les activités web potentiellement associées à une compromission.

- Phishing Investigation : rechercher des visites sur des sites de phishing.
    
- Web Exploit Investigation : examiner les sites consultés avant une activité suspecte.
    
- Browsing History Analysis : reconstruire les activités de navigation pertinentes.
    

Application IR : rechercher une éventuelle origine web de la compromission.

Téléchargement : [BrowsingHistoryView](https://www.nirsoft.net/utils/browsing_history_view.html?utm_source=chatgpt.com)

## 6. Récapitulatif des outils

|Outil|Fonction principale|Objectif IR|
|---|---|---|
|Process Hacker|Process Analysis|Identifier des processus suspects ou malveillants actifs|
|FullEventLogView|Windows Event Logs|Examiner et filtrer les événements Windows|
|Autoruns|Persistence Analysis|Identifier les mécanismes d'exécution automatique|
|LastActivityView|Activity Timeline|Analyser les activités système selon leur chronologie|
|BrowsingHistoryView|Browser History|Investiguer les activités de navigation, phishing et web exploits|

## 7. Application aux trois questions fondamentales de l'IR

Ces outils contribuent aux analyses présentées dans la section précédente :

|Question|Outils pertinents|
|---|---|
|Active Malware ?|Process Hacker|
|Suspicious Activity / Communications ?|FullEventLogView, LastActivityView, BrowsingHistoryView|
|Persistence ?|Autoruns|

Précision : ces outils ne constituent pas, à eux seuls, une solution complète d'analyse réseau. Les communications suspectes peuvent nécessiter des outils et journaux supplémentaires.

### Principe essentiel

Point essentiel : ce n'est pas le choix d'un outil particulier qui importe, mais les informations que l'analyste cherche à examiner.

Des outils équivalents ou des scripts développés en interne peuvent remplir les mêmes objectifs.

En pratique, il faut également garder à l'esprit que les outils exécutés directement sur une machine suspecte peuvent modifier certains artefacts : les actions de l'analyste doivent être documentées pour préserver la fiabilité de l'investigation.
