---
title: 5. Permissions de services
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

### 5.1 Pourquoi c’est important ?

Les services sont sensibles car :

- ils tournent souvent avec des privilèges élevés ;
    
- ils peuvent démarrer automatiquement ;
    
- ils peuvent être modifiés par des administrateurs ;
    
- ils peuvent utiliser des comptes de service ;
    
- leur mauvaise configuration peut causer une panne ou une élévation de privilèges.
    

Bonnes pratiques :

- utiliser des comptes de service dédiés ;
    
- éviter `LocalSystem` si inutile ;
    
- contrôler les permissions sur le service ;
    
- contrôler les permissions sur le dossier du binaire ;
    
- vérifier les actions de récupération ;
    
- documenter les comptes de service.
    

---

### 5.2 Points à vérifier sur un service

|Élément|Pourquoi c’est important ?|
|---|---|
|Nom du service|Nécessaire pour les commandes `sc`, PowerShell, logs.|
|Display Name|Nom lisible dans l’interface graphique.|
|État|Savoir si le service tourne ou non.|
|Mode de démarrage|Persistance potentielle si démarrage automatique.|
|Compte d’exécution|Détermine les privilèges du service.|
|Chemin du binaire|Permet de voir ce qui est exécuté.|
|Permissions du service|Qui peut démarrer, arrêter, modifier le service.|
|Permissions du dossier|Qui peut remplacer le binaire exécuté.|
|Recovery actions|Peut exécuter un programme en cas d’échec.|

---

### 5.3 Interroger la configuration d’un service

```cmd
sc qc wuauserv
```


Champs importants :

```text
BINARY_PATH_NAME     → binaire lancé
SERVICE_START_NAME   → compte d’exécution
START_TYPE           → mode de démarrage
DEPENDENCIES         → dépendances
```


---

### 5.4 Examiner les permissions d’un service avec SDDL

```cmd
sc sdshow wuauserv
```


Exemple :

```text
D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)
```


Ce format est appelé **SDDL** : Security Descriptor Definition Language.

Exemple simplifié :

```text
(A;;CCLCSWRPLORC;;;AU)
 ^  ^-------------^   ^
 |       droits       principal cible
 |
 A = Allow
```


|Élément|Signification|
|---|---|
|`D:`|Indique la DACL.|
|`( ... )`|Une ACE.|
|`A`|Allow.|
|`D`|Deny.|
|`AU`|Authenticated Users.|
|`BA`|Built-in Administrators.|
|`SY`|SYSTEM.|
|`BU`|Built-in Users.|

---


## 6. Abus cyber liés aux services

### 6.1 Mauvaises permissions de service

Une mauvaise permission peut permettre à un utilisateur non privilégié de :

- démarrer un service ;
    
- arrêter un service ;
    
- modifier le chemin du binaire ;
    
- modifier le compte d’exécution ;
    
- remplacer le programme lancé ;
    
- obtenir une élévation de privilèges si le service tourne en `LocalSystem`.
    

Droit particulièrement sensible :

```text
SERVICE_CHANGE_CONFIG
```


---

### 6.2 Binaire de service modifiable

Cas typique :

```text
Service tourne en LocalSystem
        ↓
Le binaire est dans un dossier modifiable par un user standard
        ↓
L’attaquant remplace le binaire
        ↓
Au redémarrage du service, le binaire modifié tourne en LocalSystem
```


Vérifier :

```cmd
icacls "C:\Program Files\Application\"
```


---

### 6.3 Unquoted Service Path

Un **Unquoted Service Path** apparaît quand le chemin du binaire contient des espaces mais n’est pas entouré par des guillemets.

Exemple vulnérable :

```text
C:\Program Files\My App\service.exe
```


Au lieu de :

```text
"C:\Program Files\My App\service.exe"
```


Windows peut tenter d’interpréter le chemin par étapes :

```text
C:\Program.exe
C:\Program Files\My.exe
C:\Program Files\My App\service.exe
```


Recherche avec PowerShell :

```powershell
Get-CimInstance Win32_Service |
Where-Object {$_.PathName -match ' ' -and $_.PathName -notmatch '"'} |
Select-Object Name, StartName, PathName
```


---
