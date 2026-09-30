---
title: 1. Programmes, processus et threads
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

### 1.1 Programme vs processus

Un **programme** est un fichier présent sur le disque, par exemple :

```text
C:\Windows\System32\notepad.exe
C:\Windows\System32\cmd.exe
C:\Program Files\Google\Chrome\Application\chrome.exe
```


Un programme ne fait rien tant qu’il n’est pas exécuté.

Quand Windows lance ce programme, il crée un **processus**.

Un **processus** est donc une instance d’un programme en cours d’exécution.

Exemple :

- `notepad.exe` sur disque = programme.
    
- `notepad.exe` lancé en mémoire = processus.
    

Un même programme peut avoir plusieurs processus en même temps. Exemple : plusieurs fenêtres Chrome peuvent correspondre à plusieurs processus `chrome.exe`.

---

### 1.2 Ce que contient un processus

|Élément|Rôle|
|---|---|
|**PID**|Identifiant unique du processus.|
|**PPID**|PID du processus parent.|
|**Nom**|Nom du processus, ex : `lsass.exe`, `svchost.exe`.|
|**Chemin**|Emplacement du binaire lancé.|
|**Command line**|Commande complète utilisée pour lancer le processus.|
|**Utilisateur**|Compte sous lequel le processus tourne.|
|**Access token**|Droits et privilèges du processus.|
|**Threads**|Unités d’exécution à l’intérieur du processus.|
|**Handles**|Références vers fichiers, clés registre, sockets, mutex, etc.|
|**DLL chargées**|Bibliothèques utilisées par le processus.|

---

### 1.3 Thread

Un **thread** est une unité d’exécution à l’intérieur d’un processus.

Un processus peut contenir un ou plusieurs threads.

Résumé simple :

- **Programme** = fichier sur disque.
    
- **Processus** = programme en cours d’exécution.
    
- **Thread** = fil d’exécution à l’intérieur du processus.
    

Exemple mental :

```text
Programme = recette de cuisine
Processus = cuisinier qui exécute la recette
Thread = tâche précise effectuée par le cuisinier
```


---

### 1.4 Processus parent / enfant

Quand un processus lance un autre processus, il devient son **parent**.

Exemple :

```text
explorer.exe → cmd.exe → powershell.exe
```


Ici :

- `explorer.exe` lance `cmd.exe` ;
    
- `cmd.exe` lance `powershell.exe`.
    

Cette relation parent/enfant est très importante en analyse SOC et forensic.

Exemples suspects :

```text
winword.exe → powershell.exe
excel.exe → cmd.exe
outlook.exe → wscript.exe
browser.exe → rundll32.exe
```


Ce type de chaîne peut indiquer une macro malveillante, un phishing ou une exécution indirecte de payload.

---

### 1.5 Commandes utiles pour les processus

```powershell
Get-Process
Get-Process -Id <PID> | Format-List *
```


```cmd
tasklist
tasklist /svc
```


```powershell
Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```


```cmd
wmic process get processid,parentprocessid,executablepath,commandline
```


---

### 1.6 Intérêt cyber des processus

Comprendre les processus permet de :

- repérer un processus suspect ;
    
- analyser une chaîne parent/enfant ;
    
- identifier un faux processus système ;
    
- voir quel utilisateur a lancé quoi ;
    
- comprendre les privilèges associés à un processus ;
    
- repérer des processus qui communiquent sur le réseau ;
    
- détecter une exécution anormale, par exemple `powershell.exe` lancé par Word ;
    
- comprendre les attaques sur LSASS ou les abus de services.
    

---


## 2. Processus système critiques

|Processus|Rôle|
|---|---|
|`System`|Processus système lié au noyau Windows.|
|`smss.exe`|Session Manager Subsystem. Gère l’initialisation des sessions.|
|`csrss.exe`|Client/Server Runtime Subsystem. Partie user-mode du sous-système Windows.|
|`wininit.exe`|Lance des composants critiques au démarrage du système.|
|`services.exe`|Processus du Service Control Manager. Gère le démarrage et l’arrêt des services.|
|`winlogon.exe`|Gère la connexion utilisateur, le verrouillage et le chargement du profil.|
|`lsass.exe`|Local Security Authority Subsystem Service. Authentification, politique de sécurité, tokens.|
|`svchost.exe`|Hôte de services Windows basés sur des DLL.|
|`explorer.exe`|Shell utilisateur : bureau, barre des tâches, explorateur.|

---

### 2.1 svchost.exe

`svchost.exe` signifie **Service Host**.

Son rôle : héberger des services Windows qui sont fournis sous forme de DLL.

Problème : une DLL ne peut pas se lancer toute seule comme un `.exe`.

Solution : Windows utilise `svchost.exe` comme processus hôte pour charger et exécuter ces services.

Exemples de services pouvant être hébergés via `svchost.exe` :

- Windows Update ;
    
- pare-feu Windows ;
    
- Plug and Play ;
    
- services réseau ;
    
- RPC ;
    
- DCOM.
    

Voir les services associés à chaque `svchost.exe` :

```cmd
tasklist /svc
```


Avec PowerShell :

```powershell
Get-CimInstance Win32_Service | Select-Object Name, ProcessId, State, StartName, PathName
```


#### Focus cyber

`svchost.exe` est souvent imité par des malwares.

Exemples de faux noms :

```text
scvhost.exe
svhost.exe
svch0st.exe
svchosts.exe
```


Points à vérifier :

- chemin du binaire ;
    
- signature numérique ;
    
- processus parent ;
    
- compte utilisateur ;
    
- connexions réseau ;
    
- services hébergés.
    

Un vrai `svchost.exe` se trouve normalement ici :

```text
C:\Windows\System32\svchost.exe
```


---
