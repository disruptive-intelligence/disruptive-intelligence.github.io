---
title: Révision de l'approfondissement
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 15. Mini checklists cyber

### 15.1 Analyse rapide d’un processus suspect

À vérifier :

- nom du processus ;
    
- PID / PPID ;
    
- processus parent ;
    
- chemin du binaire ;
    
- ligne de commande ;
    
- utilisateur ;
    
- niveau d’intégrité ;
    
- signature ;
    
- DLL chargées ;
    
- connexions réseau ;
    
- date de création/modification du fichier.
    

Commandes/outils :

```powershell
Get-Process
Get-CimInstance Win32_Process | Select ProcessId,ParentProcessId,Name,ExecutablePath,CommandLine
```


```cmd
tasklist /svc
netstat -ano
```


Outils :

```text
Process Explorer
Process Monitor
TCPView
Sigcheck
```


---

### 15.2 Analyse rapide d’un service suspect

À vérifier :

- nom du service ;
    
- display name ;
    
- état ;
    
- mode de démarrage ;
    
- compte d’exécution ;
    
- chemin du binaire ;
    
- permissions du service ;
    
- permissions du dossier ;
    
- signature du binaire ;
    
- date de création/modification ;
    
- recovery actions.
    

Commandes :

```cmd
sc qc <service>
sc sdshow <service>
```


```powershell
Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName
Get-Acl "C:\chemin\du\dossier"
```


---

### 15.3 Analyse rapide d’une persistance

À vérifier :

- Run Keys ;
    
- RunOnce ;
    
- services ;
    
- tâches planifiées ;
    
- Startup folders ;
    
- WMI persistence ;
    
- drivers ;
    
- extensions shell ;
    
- Winlogon ;
    
- AppInit DLLs.
    

Commandes :

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
schtasks /query /fo LIST /v
```


```powershell
Get-ScheduledTask
Get-CimInstance Win32_Service | Select Name,StartMode,StartName,PathName
```


Outil recommandé :

```text
Autoruns
```


---

## 16. Résumé mental

### Chaîne d’exécution

```text
Programme sur disque
   ↓
Processus en mémoire
   ↓
Threads exécutent le code
   ↓
Le processus possède un token
   ↓
Le token contient SID, groupes, privilèges, intégrité
   ↓
Windows compare le token aux ACL des objets
   ↓
Accès autorisé ou refusé
```


### Chaîne services

```text
Service configuré dans le registre
   ↓
Géré par le SCM
   ↓
Lancé via services.exe
   ↓
Tourne sous un compte défini
   ↓
Exécute un binaire ou une DLL via svchost.exe
   ↓
Peut devenir un vecteur de persistance ou privesc si mal configuré
```


### Chaîne authentification

```text
Utilisateur saisit ses identifiants
   ↓
LSASS vérifie l’identité
   ↓
Windows crée un access token
   ↓
Les processus héritent du token
   ↓
Les accès sont décidés via les DACL
```


---

## 17. Commandes à retenir

### Processus

```powershell
Get-Process
Get-Process -Id <PID> | Format-List *
Get-CimInstance Win32_Process | Select ProcessId,ParentProcessId,Name,ExecutablePath,CommandLine
```


```cmd
tasklist
tasklist /svc
wmic process get processid,parentprocessid,executablepath,commandline
```


### Identité / token

```cmd
whoami
whoami /user
whoami /groups
whoami /priv
```


### Services

```powershell
Get-Service
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName
```


```cmd
sc query
sc qc <service>
sc start <service>
sc stop <service>
sc sdshow <service>
```


### Permissions

```cmd
icacls "C:\chemin"
```


```powershell
Get-Acl "C:\chemin" | Format-List
Get-Acl HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


### Registre

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SYSTEM\CurrentControlSet\Services\wuauserv
```


### Ruches en lab

```cmd
reg save HKLM\SAM sam.save
reg save HKLM\SYSTEM system.save
reg save HKLM\SECURITY security.save
```


### Tâches planifiées

```cmd
schtasks /query /fo LIST /v
```


```powershell
Get-ScheduledTask
```


### Defender

```powershell
Get-MpComputerStatus
Get-MpPreference
```


---

## 18. Erreurs fréquentes à éviter

- Confondre **programme** et **processus**.
    
- Confondre **processus** et **service**.
    
- Dire que tous les `svchost.exe` sont suspects : il y en a beaucoup de légitimes.
    
- Oublier de vérifier le **chemin réel** du binaire.
    
- Se fier uniquement au nom du processus.
    
- Oublier le **compte d’exécution** d’un service.
    
- Regarder seulement les permissions du service, mais pas celles du dossier contenant le binaire.
    
- Croire qu’être administrateur signifie toujours avoir un token élevé.
    
- Confondre **DACL** et **SACL**.
    
- Oublier que les Run Keys peuvent exister en `HKCU` et `HKLM`.
    
- Ne pas vérifier les tâches planifiées dans une analyse de persistance.
    
- Négliger les signatures numériques des binaires.
    

---

## 19. Mini quiz

### Questions

1. Quelle est la différence entre un programme et un processus ?
    
2. Pourquoi faut-il regarder le PPID d’un processus suspect ?
    
3. À quoi sert `svchost.exe` ?
    
4. Pourquoi LSASS est-il une cible importante pour un attaquant ?
    
5. Quelle commande permet de voir le SID de l’utilisateur courant ?
    
6. Que contient un access token ?
    
7. Quelle est la différence entre DACL et SACL ?
    
8. Où sont stockés les services dans le registre ?
    
9. Pourquoi un service en `LocalSystem` avec un dossier modifiable est dangereux ?
    
10. Quelles clés registre vérifier pour une persistance simple ?
    
11. Quelle commande permet de lister les services avec leur chemin de binaire ?
    
12. Pourquoi UAC peut bloquer une action même si l’utilisateur est administrateur ?
    

### Réponses attendues

1. Un programme est un fichier sur disque ; un processus est une instance en cours d’exécution.
    
2. Le PPID permet de comprendre quel processus l’a lancé et de détecter des chaînes suspectes.
    
3. `svchost.exe` héberge des services Windows fournis sous forme de DLL.
    
4. LSASS peut contenir des secrets d’authentification comme hashes NTLM ou tickets Kerberos.
    
5. `whoami /user`.
    
6. SID utilisateur, SID des groupes, privilèges, niveau d’intégrité, informations de session.
    
7. DACL = autorisations/refus ; SACL = audit/journalisation.
    
8. `HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>`.
    
9. Un attaquant pourrait remplacer le binaire et le faire exécuter avec des privilèges élevés.
    
10. `HKCU/HKLM\Software\Microsoft\Windows\CurrentVersion\Run` et `RunOnce`.
    
11. `Get-CimInstance Win32_Service | Select Name,State,StartMode,StartName,PathName`.
    
12. Parce qu’un admin utilise souvent un token filtré tant qu’il n’a pas validé l’élévation UAC.
    

---

## 20. Réponse type entretien

> Sous Windows, un programme devient un processus lorsqu’il est exécuté. Ce processus possède un PID, un contexte utilisateur et un access token contenant les SID, groupes, privilèges et niveau d’intégrité. Lorsqu’il tente d’accéder à un objet comme un fichier, une clé de registre ou un service, Windows compare ce token à la DACL de l’objet pour autoriser ou refuser l’accès. Les services sont des processus particuliers, gérés par le Service Control Manager, qui peuvent démarrer automatiquement et tourner sous des comptes privilégiés comme LocalSystem. C’est pourquoi les permissions de services, le chemin du binaire, le compte d’exécution et les mécanismes de persistance comme les Run Keys ou les tâches planifiées sont des points essentiels à analyser en cybersécurité.
