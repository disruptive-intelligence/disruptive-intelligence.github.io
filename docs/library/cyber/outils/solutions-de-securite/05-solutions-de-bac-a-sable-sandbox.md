---
title: Solutions de bac à sable — Sandbox
source: Cyber/04_Hardening/HTB_Solutions de sécurité.md
note: Solutions de sécurité
up:
- - Solutions de sécurité
  - index.md
---

## Sandbox

- Environnement **isolé** utilisé pour exécuter/ouvrir des fichiers suspects sans exposer directement un système de production.
- Peut analyser différents types de fichiers :
    - `.exe`
    - `.pdf`
    - `.docx`
    - `.xlsx`
    - etc.

```
Fichier suspect
→ Sandbox isolée
→ exécution / ouverture
→ observation du comportement
```

## Avantages du Sandboxing

- Protège les hôtes et OS de production.
- Permet de détecter des fichiers potentiellement dangereux.
- Permet de tester des logiciels / mises à jour avant déploiement.
- Peut aider à détecter des menaces **zero-day** ou inconnues via leur comportement.

> Le sandboxing ne “corrige” pas une zero-day : il permet surtout d’**observer un comportement malveillant même sans signature connue**.
## Analyse comportementale

- La sandbox exécute le fichier et observe ses actions.
- Exemples :

```
sample.exe
→ crée un fichier
→ modifie le registre
→ lance un processus
→ contacte une IP
→ télécharge un payload
```

- Cela permet d’identifier des comportements suspects même lorsque l’antivirus ne possède pas encore de signature correspondante.
## Données / résultats fournis

- Une sandbox peut enregistrer notamment :

|Information|Exemple|
|---|---|
|**Execution Time**|durée / heure d’exécution|
|**File Access**|fichiers lus, créés ou modifiés|
|**Behavior**|actions effectuées|
|**Date / Time**|timestamp des événements|
|**Hash**|MD5 / SHA1 / SHA256 du fichier|
|**Process Activity**|processus lancés|
|**Network Activity**|connexions réseau effectuées|

- **Complément utile :** selon le produit, on peut également retrouver :
	- domaines contactés ;
	- IP ;
	- URLs ;
	- clés registre modifiées ;
	- processus parent/enfant ;
	- fichiers dropped.
## Importance en sécurité

- Les malwares modernes utilisent souvent des techniques plus complexes pour éviter les détections classiques.

```
Signature AV inconnue
        ↓
Sandbox
        ↓
Comportement observé
        ↓
Détection possible
```

- Le sandboxing complète donc bien :

```
AV
+ EDR
+ Sandbox
+ SIEM
```

## Limites

- Certains malwares tentent de détecter qu’ils s’exécutent dans une sandbox.
- Techniques possibles :
	- attendre plusieurs minutes avant d’agir ;
	- vérifier la présence de processus/artefacts de VM ;
	- détecter peu d’activité utilisateur ;
	- ne s’activer que sous certaines conditions.

```
Malware détecte Sandbox
→ reste dormant
→ analyse potentiellement faussée
```
