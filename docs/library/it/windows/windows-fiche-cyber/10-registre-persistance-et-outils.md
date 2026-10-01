---
title: Registre, persistance et outils
source: IT/02 Windows/Windows — fiche cyber.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 10. Registre Windows

### 10.1 Définition

Le **registre Windows** est une base de données hiérarchique qui stocke la configuration de Windows et de nombreuses applications.

Il contient :

- paramètres système ;
    
- configuration logicielle ;
    
- services ;
    
- pilotes ;
    
- profils utilisateurs ;
    
- paramètres de sécurité ;
    
- mécanismes de démarrage automatique.
    

Ouvrir l’éditeur de registre :

```cmd
regedit
```


Interroger le registre en ligne de commande :

```cmd
reg query <clé>
```


---

### 10.2 Vocabulaire

|Terme|Définition simple|
|---|---|
|Ruche / Hive|Grande racine logique du registre.|
|Key / clé|Équivalent d’un dossier.|
|Subkey / sous-clé|Sous-dossier dans une clé.|
|Value / valeur|Entrée contenant une donnée.|
|Data / donnée|Contenu de la valeur.|

Image mentale :

```text
Ruche = disque
Clé = dossier
Valeur = fichier
Donnée = contenu du fichier
```


---

### 10.3 Ruches principales

|Ruche|Abréviation|Contenu principal|
|---|---|---|
|`HKEY_LOCAL_MACHINE`|`HKLM`|Configuration globale machine : services, pilotes, logiciels, sécurité.|
|`HKEY_CURRENT_USER`|`HKCU`|Configuration du profil utilisateur courant.|
|`HKEY_CLASSES_ROOT`|`HKCR`|Associations de fichiers, COM, classes.|
|`HKEY_USERS`|`HKU`|Profils utilisateurs chargés, identifiés par SID.|
|`HKEY_CURRENT_CONFIG`|`HKCC`|Configuration matérielle courante.|

À retenir :

```text
HKLM = machine
HKCU = utilisateur courant
HKU  = tous les profils utilisateurs chargés
```


---

### 10.4 Fichiers physiques du registre

Les ruches système sont stockées dans :

```text
C:\Windows\System32\config\
```


|Fichier|Rôle|
|---|---|
|`SAM`|Comptes locaux.|
|`SYSTEM`|Configuration système.|
|`SECURITY`|Secrets et politiques de sécurité.|
|`SOFTWARE`|Configuration logicielle.|
|`DEFAULT`|Profil par défaut.|

La ruche utilisateur courante est stockée dans :

```text
C:\Users\<USERNAME>\NTUSER.DAT
```


---

### 10.5 Services dans le registre

Les services sont configurés dans :

```text
HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>
```


Exemple :

```powershell
Get-Acl -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


Interroger avec `reg` :

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\wuauserv
```


---

## 11. Persistance Windows

### 11.1 Définition

La **persistance** désigne les mécanismes permettant à un programme ou à un attaquant de survivre à :

- un redémarrage ;
    
- une déconnexion ;
    
- une reconnexion utilisateur ;
    
- un arrêt temporaire du processus.
    

---

### 11.2 Run et RunOnce Registry Keys

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

### 11.3 Services comme persistance

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

### 11.4 Tâches planifiées

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

### 11.5 Startup folder

Dossier de démarrage utilisateur :

```text
C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```


Dossier de démarrage commun :

```text
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```


---

### 11.6 Autoruns

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

## 12. Outils Windows et Sysinternals

### 12.1 Task Manager

Le **Task Manager** permet d’observer rapidement :

- processus ;
    
- performance CPU/RAM/disque/réseau ;
    
- utilisateurs connectés ;
    
- applications au démarrage ;
    
- services ;
    
- PID ;
    
- consommation des ressources.
    

Raccourcis :

```text
Ctrl + Shift + Esc
Ctrl + Alt + Del → Task Manager
taskmgr
```


---

### 12.2 Resource Monitor

Resource Monitor donne plus de détails sur :

- CPU ;
    
- mémoire ;
    
- disque ;
    
- réseau.
    

Lancement :

```cmd
resmon
```


---

### 12.3 Sysinternals

Sysinternals est une suite d’outils Microsoft pour l’administration, le diagnostic et l’analyse Windows.

Accès possible via :

```text
\\live.sysinternals.com\tools
```


Exemple :

```cmd
\\live.sysinternals.com\tools\procdump.exe -accepteula
```


---

### 12.4 Process Explorer

`Process Explorer` est une version avancée du Task Manager.

Utile pour voir :

- hiérarchie parent/enfant ;
    
- chemin du binaire ;
    
- utilisateur ;
    
- niveau d’intégrité ;
    
- DLL chargées ;
    
- handles ;
    
- signature ;
    
- services hébergés par `svchost.exe`.
    

Outil :

```text
procexp.exe
```


---

### 12.5 Process Monitor — Procmon

`Procmon` permet de surveiller en temps réel :

- accès fichiers ;
    
- accès registre ;
    
- activité réseau ;
    
- création de processus/threads.
    

Outil :

```text
procmon.exe
```


Filtres utiles :

```text
Process Name is <process.exe>
Operation is RegSetValue
Operation is CreateFile
Result is ACCESS DENIED
Result is NAME NOT FOUND
Path ends with .dll
```


---

### 12.6 TCPView

`TCPView` affiche les connexions réseau actives par processus.

Outil :

```text
tcpview.exe
```


Commandes natives alternatives :

```cmd
netstat -ano
```


```powershell
Get-NetTCPConnection
```


---

### 12.7 AccessChk

`AccessChk` permet d’auditer les permissions.

Outil :

```text
accesschk.exe
```


Exemple :

```cmd
accesschk.exe -uwcqv "Authenticated Users" *
```


---

### 12.8 Sigcheck

`Sigcheck` permet de vérifier les signatures de fichiers.

Outil :

```text
sigcheck.exe
```


Exemple :

```cmd
sigcheck.exe -m C:\Windows\System32\svchost.exe
```


---
