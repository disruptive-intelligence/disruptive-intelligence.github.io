---
title: Endpoint Detection & Response — EDR
source: Cyber/99_Concepts/HTB_Solutions de sécurité.md
note: HTB — Solutions de sécurité
up:
- - HTB — Solutions de sécurité
  - index.md
---

## EDR — Endpoint Detection and Response

- Produit de sécurité installé sur les **endpoints** pour :
    - surveiller en continu leur activité ;
    - détecter des menaces comme malware/ransomware ;
    - prendre des mesures de réponse ;
    - fournir des données pour l’investigation.

```
Endpoint activity
→ EDR collecte
→ analyse
→ détecte
→ répond / alerte
```

## Composants principaux

|Composant|Rôle|
|---|---|
|**Endpoint Data Collection Agent**|Collecte la télémétrie sur l’hôte|
|**Automated Response**|Exécute certaines actions automatiquement|
|**Analysis & Digital Investigation**|Permet l’analyse et l’investigation d’un incident|

## Fonctions de l’EDR
### Monitoring / Collection

- L’EDR collecte les événements utiles à la détection :
	- processus lancés ;
	- fichiers accédés/modifiés ;
	- chemins de fichiers ;
	- hashes ;
	- relations entre processus ;
	- autres événements jugés pertinents pour la sécurité.
- Exemple :

```
winword.exe
    ↓
powershell.exe
    ↓
download malware.exe
```

→ une chaîne de processus anormale peut déclencher une alerte.
### Behavioral Analysis

- Analyse le **comportement** observé sur l’endpoint.
- Cherche à identifier :
    - malware ;
    - ransomware ;
    - activités suspectes ;
    - comportements correspondant à un attaquant.

```
Signature connue → détection possible
Comportement anormal → détection possible même sans signature exacte
```

## Response

- Lorsqu’une menace est détectée, l’EDR peut :
	- générer une alerte ;
	- notifier l’analyste ;
	- prendre certaines mesures automatiquement.
- **Complément utile :** selon le produit, la réponse peut inclure :
	- isoler l’endpoint du réseau ;
	- tuer un processus ;
	- mettre un fichier en quarantaine ;
	- supprimer/bloquer un artefact ;
	- lancer une investigation ou collecte supplémentaire.
### Digital Investigation

- L’EDR permet de mener une investigation approfondie directement à partir de la télémétrie de l’hôte.
- L’analyste peut notamment reconstruire :

```
Processus parent
   ↓
Processus enfant
   ↓
Fichier créé
   ↓
Connexion réseau
   ↓
Persistence
```

→ utile pour comprendre **ce qui s’est passé, comment et jusqu’où l’attaquant est allé**.
## Logs / Télémétrie EDR

- Les informations varient selon le produit, mais on retrouve souvent :

|Donnée|Exemple|
|---|---|
|**Process Name**|`powershell.exe`|
|**Process Path**|`C:\Windows\System32\...`|
|**Hash**|SHA256 du fichier|
|**File Access**|fichier lu/modifié|
|**File Size**|taille du fichier|
|**Process Execution**|programme exécuté|
|**Parent/Child Process**|relation entre processus|

- Le point fort de l’EDR est donc la **visibilité détaillée sur l’activité de l’endpoint**.
## EDR vs Antivirus

```
Antivirus
→ surtout prévention/détection malware

EDR
→ détection + télémétrie + investigation + réponse
```

- Un EDR apporte donc davantage de contexte sur :
	- comment le processus a démarré ;
	- quels fichiers ont été touchés ;
	- quels processus sont liés ;
	- quelles actions de réponse ont été prises.

> Un EDR ne remplace pas forcément l’antivirus : les solutions modernes combinent souvent plusieurs fonctions dans une même plateforme.
