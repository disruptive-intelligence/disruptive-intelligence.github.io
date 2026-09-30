---
title: Processus et services
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 1. Programmes, processus et threads

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

## 3. Focus LSASS

### 3.1 Définition

`lsass.exe` signifie **Local Security Authority Subsystem Service**.

C’est un processus critique de Windows chargé d’appliquer la politique de sécurité locale.

Il intervient notamment dans :

- l’authentification des utilisateurs ;
    
- la vérification des identifiants ;
    
- la création ou la gestion des access tokens ;
    
- les changements de mots de passe ;
    
- la journalisation des événements de connexion/déconnexion ;
    
- la gestion de certains secrets d’authentification.
    

---

### 3.2 LSASS et authentification

Quand un utilisateur se connecte :

1. l’utilisateur saisit ses identifiants ;
    
2. Windows transmet la demande au sous-système de sécurité ;
    
3. LSASS vérifie l’identité ;
    
4. si l’authentification réussit, Windows crée un access token ;
    
5. ce token est attaché aux processus de l’utilisateur.
    

Schéma simplifié :

```text
Login user
   ↓
LSASS vérifie l’identité
   ↓
Création d’un access token
   ↓
Lancement de la session utilisateur
   ↓
Les processus héritent du token
```


---

### 3.3 Pourquoi LSASS est une cible critique ?

LSASS peut contenir en mémoire des informations sensibles liées à l’authentification.

Selon la version de Windows, la configuration et les protections activées, on peut y trouver :

- hashes NTLM ;
    
- tickets Kerberos ;
    
- secrets liés au SSO ;
    
- informations de session ;
    
- parfois mots de passe en clair sur anciens systèmes ou configurations faibles.
    

C’est pourquoi LSASS est une cible majeure pour le vol d’identifiants.

---

### 3.4 Logs associés

Les événements liés aux connexions sont journalisés dans le journal **Security** de Windows.

|Event ID|Signification|
|---|---|
|4624|Connexion réussie.|
|4625|Échec de connexion.|
|4634|Déconnexion.|
|4648|Connexion avec identifiants explicites.|
|4672|Privilèges spéciaux attribués à une nouvelle connexion.|
|4688|Création de processus, si l’audit est activé.|

---

### 3.5 Protections autour de LSASS

Protections utiles :

- **Credential Guard** : isole certains secrets d’authentification via Virtualization-Based Security.
    
- **LSA Protection / RunAsPPL** : limite l’accès non autorisé à LSASS.
    
- **Defender / EDR** : surveille les tentatives de dump ou d’accès suspect à LSASS.
    
- **Réduction des privilèges admin** : moins d’utilisateurs capables d’interagir avec LSASS.
    
- **Désactivation de WDigest** sur anciens systèmes.
    

Commandes utiles :

```powershell
Get-Process lsass
Get-Process lsass | Format-List *
```


---

## 4. Services Windows

### 4.1 Définition

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

### 4.2 Service Control Manager — SCM

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

### 4.3 Où gérer les services ?

#### Interface graphique

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
    

#### Ligne de commande CMD

```cmd
sc query
sc qc <ServiceName>
sc start <ServiceName>
sc stop <ServiceName>
```


#### PowerShell

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

### 4.4 États d’un service

|État|Signification|
|---|---|
|`Running`|Service en cours d’exécution.|
|`Stopped`|Service arrêté.|
|`Paused`|Service suspendu.|
|`Start Pending`|Service en cours de démarrage.|
|`Stop Pending`|Service en cours d’arrêt.|

---

### 4.5 Modes de démarrage

|Mode|Signification|
|---|---|
|`Automatic`|Démarre automatiquement au boot.|
|`Automatic (Delayed Start)`|Démarre automatiquement avec un délai.|
|`Manual`|Démarre seulement si demandé.|
|`Disabled`|Ne peut pas démarrer tant qu’il reste désactivé.|

---

### 4.6 Comptes d’exécution des services

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

## 5. Permissions de services

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
