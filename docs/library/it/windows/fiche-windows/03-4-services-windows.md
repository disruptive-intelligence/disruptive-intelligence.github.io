---
title: 4. Services Windows
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 4.1 Définition

Un **service Windows** est un composant conçu pour exécuter une tâche en arrière-plan, souvent pendant longtemps.

Un service peut :

- démarrer automatiquement au boot ;
    
- tourner sans utilisateur connecté ;
    
- continuer à fonctionner après la déconnexion d’un utilisateur ;
    
- exécuter des fonctions système critiques ;
    
- être lancé sous un compte spécifique.
    

Exemples de fonctions gérées par des services :

- réseau ;
    
- mises à jour Windows ;
    
- diagnostic système ;
    
- journalisation ;
    
- authentification ;
    
- impression ;
    
- antivirus ;
    
- supervision.
    

---

## 4.2 Service Control Manager — SCM

Les services sont gérés par le **Service Control Manager** ou **SCM**.

Le SCM permet de :

- lister les services ;
    
- démarrer un service ;
    
- arrêter un service ;
    
- modifier la configuration d’un service ;
    
- gérer les dépendances ;
    
- définir le compte d’exécution ;
    
- définir le mode de démarrage.
    

Le processus associé au SCM est :

```text
services.exe
```


---

## 4.3 Où gérer les services ?

### Interface graphique

```text
services.msc
```


Permet de voir :

- nom du service ;
    
- description ;
    
- état ;
    
- type de démarrage ;
    
- chemin de l’exécutable ;
    
- compte d’exécution ;
    
- dépendances ;
    
- options de récupération.
    

### Ligne de commande CMD

```cmd
sc query
sc qc <ServiceName>
sc start <ServiceName>
sc stop <ServiceName>
```


### PowerShell

```powershell
Get-Service
Start-Service <ServiceName>
Stop-Service <ServiceName>
Restart-Service <ServiceName>
```


Pour plus de détails que `Get-Service` :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
```


---

## 4.4 États d’un service

|État|Signification|
|---|---|
|`Running`|Service en cours d’exécution.|
|`Stopped`|Service arrêté.|
|`Paused`|Service suspendu.|
|`Start Pending`|Service en cours de démarrage.|
|`Stop Pending`|Service en cours d’arrêt.|

---

## 4.5 Modes de démarrage

|Mode|Signification|
|---|---|
|`Automatic`|Démarre automatiquement au boot.|
|`Automatic (Delayed Start)`|Démarre automatiquement avec un délai.|
|`Manual`|Démarre seulement si demandé.|
|`Disabled`|Ne peut pas démarrer tant qu’il reste désactivé.|

---

## 4.6 Comptes d’exécution des services

Un service tourne sous un compte. Ce compte détermine ses droits locaux et réseau.

|Compte|Description|
|---|---|
|`LocalSystem`|Privilèges très élevés sur la machine locale. À éviter si non nécessaire.|
|`NetworkService`|Droits locaux limités, identité de la machine sur le réseau.|
|`LocalService`|Droits locaux limités, identité anonyme sur le réseau.|
|Compte de service dédié|Compte spécifique créé pour faire tourner un service. Recommandé pour les services applicatifs.|
|gMSA|Group Managed Service Account. Utilisé en domaine AD pour mieux gérer les mots de passe de services.|

Bon réflexe : appliquer le **principe du moindre privilège**.

Un service n’a pas toujours besoin de tourner en `LocalSystem`.

---
