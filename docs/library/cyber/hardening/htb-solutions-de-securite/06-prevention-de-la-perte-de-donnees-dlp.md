---
title: Prévention de la perte de données — DLP
source: Cyber/99_Concepts/HTB_Solutions de sécurité.md
note: HTB — Solutions de sécurité
up:
- - HTB — Solutions de sécurité
  - index.md
---

## DLP — Data Loss Prevention

- Technologie destinée à **empêcher les données sensibles ou critiques de quitter l’organisation** de manière non autorisée.
- Peut :
    - détecter des données sensibles ;
    - bloquer leur transfert ;
    - chiffrer la transmission ;
    - générer une alerte/log pour investigation.

```
Sensitive Data
→ DLP Rule
→ Allow / Block / Encrypt / Alert
```

## Types de DLP

|Type|Principe|
|---|---|
|**Network DLP**|Surveille les données quittant l’organisation via le réseau|
|**Endpoint DLP**|Surveille les activités et données sur un endpoint spécifique|
|**Cloud DLP**|Protège les données utilisées/transférées dans les services cloud|

## Network DLP

- Surveille les flux réseau afin d’empêcher la sortie de données sensibles.
- Peut par exemple :
    - bloquer l’upload d’un fichier vers un serveur FTP ;
    - demander une validation/audit ;
    - générer un log ;
    - alerter l’administrateur.

```
Endpoint
   ↓
Network DLP
   ↓
Internet / FTP / Email
```

L’action dépend des règles configurées.
## Endpoint DLP

- Agent installé directement sur un appareil.
- Surveille les activités locales plutôt que seulement les flux réseau.
- Particulièrement utile pour les **utilisateurs distants**.
- Peut notamment contrôler :
	- copie de fichiers ;
	- stockage local ;
	- chiffrement des données ;
	- utilisation de périphériques amovibles ;
	- autres actions sur des données sensibles.

```
Sensitive File
→ Copy to USB
→ Endpoint DLP
→ Block / Alert
```

## Cloud DLP

- Protège les données utilisées dans les **services et applications cloud**.
- Cherche à empêcher :
    - fuite de données ;
    - partage non autorisé ;
    - transfert vers des services cloud non approuvés.

```
User
→ Cloud App
→ DLP Policy
→ Data protected
```

## Fonctionnement d’un DLP

- Le DLP compare le contenu aux **règles/patterns définis**.
- Exemple :

```
Email contient un numéro de carte bancaire
        ↓
DLP reconnaît le format
        ↓
Block / Encrypt / Alert
```

- Les règles peuvent donc s’appuyer sur des formats de données connus.
- Exemples :
	- numéros de carte bancaire ;
	- données personnelles ;
	- informations financières ;
	- documents confidentiels.
- Les DLP modernes peuvent aussi utiliser des classifications, labels, mots-clés ou fingerprinting de documents, pas uniquement des patterns simples.
## Actions possibles

- Selon la politique :
	- **Block** → empêcher le transfert ;
	- **Encrypt** → sécuriser la transmission ;
	- **Alert** → prévenir l’administrateur/SOC ;
	- **Log** → conserver l’événement ;
	- **Audit** → permettre l’action mais la tracer.
## Importance du DLP

- Une fuite de données peut entraîner :
	- exposition d’informations confidentielles ;
	- violation réglementaire ;
	- pertes financières ;
	- atteinte à la réputation.
- Le DLP est donc particulièrement important pour les organisations manipulant des **données sensibles ou critiques**.
