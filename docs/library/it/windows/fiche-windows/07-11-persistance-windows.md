---
title: 11. Persistance Windows
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 11.1 Définition

La **persistance** désigne les mécanismes permettant à un programme ou à un attaquant de survivre à :

- un redémarrage ;
    
- une déconnexion ;
    
- une reconnexion utilisateur ;
    
- un arrêt temporaire du processus.
    

---

## 11.2 Run et RunOnce Registry Keys

Les clés `Run` et `RunOnce` permettent de lancer automatiquement des programmes.

Clés principales :

```text
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```


Différence :

|Clé|Effet|
|---|---|
|`Run`|Lance le programme à chaque ouverture de session.|
|`RunOnce`|Lance le programme une seule fois puis supprime l’entrée.|
|`HKLM`|S’applique à la machine / tous les utilisateurs.|
|`HKCU`|S’applique à l’utilisateur courant.|

Exemple d’interrogation :

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```


Focus forensic : ces clés sont parmi les premiers endroits à vérifier en cas de suspicion de persistance.

---

## 11.3 Services comme persistance

Un attaquant peut chercher à créer ou modifier un service pour exécuter un programme au démarrage.

À vérifier :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
```


Points suspects :

- service récemment créé ;
    
- nom imitant un service Windows ;
    
- chemin dans `Temp`, `AppData`, `Public` ;
    
- service en `Automatic` ;
    
- binaire non signé ;
    
- compte d’exécution très privilégié.
    

---

## 11.4 Tâches planifiées

Les tâches planifiées sont un mécanisme très fréquent de persistance.

Lister les tâches :

```cmd
schtasks /query /fo LIST /v
```


Avec PowerShell :

```powershell
Get-ScheduledTask
```


Points à regarder :

- déclencheur ;
    
- action exécutée ;
    
- compte utilisé ;
    
- chemin du binaire ;
    
- date de création/modification ;
    
- tâche cachée ou nom trompeur.
    

---

## 11.5 Startup folder

Dossier de démarrage utilisateur :

```text
C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```


Dossier de démarrage commun :

```text
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```


---

## 11.6 Autoruns

`Autoruns` est un outil Sysinternals très utile pour analyser la persistance Windows.

Il permet de voir :

- Run Keys ;
    
- services ;
    
- drivers ;
    
- tâches planifiées ;
    
- DLL chargées automatiquement ;
    
- extensions shell ;
    
- AppInit ;
    
- Winlogon ;
    
- WMI ;
    
- codecs ;
    
- composants navigateur.
    

Outil recommandé :

```text
autoruns.exe
```


---
