---
title: Lab 4 — Évaluation finale (Skills Assessment)
source: IT/02 Windows/Journaux & investigation/Sysmon et ETW.md
note: Sysmon et ETW
up:
- - Sysmon et ETW
  - ../index.md
- - Labs
  - index.md
---

Le SOC confie des dossiers de journaux exportés d'une machine compromise : un dossier par question, et dans chaque dossier un Event ID à chercher. Les réponses ne sont pas publiées ; la méthode suit les write-ups de [Casee Hill](https://medium.com/@clh0011/windows-event-logs-finding-evil-skills-assesment-18dab17adaf8) et de [faresbltagy](https://faresbltagy.gitbook.io/footprintinglabs/soc-hackthebox-notes-and-labs/windows-event-logs-and-finding-evil-module).

Réflexe commun : `Path='C:\Logs\<dossier>\*.evtx'` lit tous les fichiers du dossier d'un coup ; `Id=` garde l'Event ID utile ; `Where-Object` cherche un mot dans le message.

## Question 1 — DLL hijacking : le processus responsable

**Énoncé HTB Academy.** Dans `C:\Logs\DLLHijack`, déterminer le processus qui a mené le DLL hijacking.

1. Garder les chargements de DLL (Sysmon `7`) du dossier :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\*.evtx'; Id=7} | Format-List
    ```


    Beaucoup de bruit, surtout celui du navigateur.

2. Réduire le bruit : les DLL non signées.

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\*.evtx'; Id=7} |
        Where-Object { $_.Message -match 'Signed: false' } |
        Format-List
    ```


3. Une DLL suspecte revient : la chercher par son nom.

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\*.evtx'; Id=7} |
        Where-Object { $_.Message -like "*NOM_DLL.dll*" } |
        Format-List
    ```


4. Deux processus chargent la même DLL : comparer leur `Image` (chemin) et leur heure. L'un sert de véhicule, l'autre est le responsable.

Démarche détaillée : [Analyser un fichier .evtx : l'exemple du DLL hijacking](../../analyse-des-journaux-d-evenements-windows-event-logs/03-lire-et-filtrer-les-journaux.md#analyser-un-fichier-evtx-lexemple-du-dll-hijacking).

## Question 2 — PowerShell non managé : le processus victime

**Énoncé HTB Academy.** Dans `C:\Logs\PowershellExec`, trouver le processus qui a exécuté du PowerShell non managé.

1. Chercher les chargements de `clrjit.dll` (runtime .NET) :

    ```powershell
    Get-WinEvent -Path "C:\Logs\PowershellExec\*.evtx" |
        Where-Object { $_.Id -eq 7 -and $_.Message -match "clrjit.dll" } |
        Select-Object -ExpandProperty Message
    ```


2. Lire `Image` dans chaque résultat : `powershell.exe` charge normalement `clrjit.dll` ; un autre processus qui le charge est la victime.

Observateur : *Filter Current Log…* → `7`, puis *Find* sur `clrjit.dll` ou `clr.dll`.

## Question 3 — Qui a injecté le code ?

**Énoncé HTB Academy.** Même dossier : trouver le processus qui a injecté le code dans la victime de la question 2.

1. L'injection laisse un Sysmon `8` (CreateRemoteThread) : un processus crée un thread dans un autre.

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\PowershellExec\*.evtx'; Id=8} | Format-List
    ```


2. Dans le message : `SourceImage` = le processus qui injecte, `TargetImage` = la victime (celle de la question 2).

Observateur : *Filter Current Log…* → `8`, puis lire `SourceImage` et `TargetImage`.

## Question 4 — Qui a dumpé LSASS ?

**Énoncé HTB Academy.** Dans `C:\Logs\Dump`, trouver le processus qui a accédé à la mémoire de LSASS.

1. Garder les accès à un processus (Sysmon `10`) qui visent `lsass.exe` :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=10} |
        Where-Object { $_.Message -match "lsass.exe" } |
        Format-List
    ```


2. Beaucoup d'accès sont normaux (processus système). Pour en écarter une partie :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=10} |
        Where-Object { $_.Message -match "lsass.exe" -and $_.Message -notmatch "svchost.exe" } |
        Format-List
    ```


3. Le suspect : un `SourceImage` lancé depuis un dossier utilisateur. Relever aussi l'heure (`TimeCreated`) pour la question 5.

## Question 5 — Une connexion malveillante après le dump ?

**Énoncé HTB Academy.** Même dossier : une connexion suspecte a-t-elle suivi l'accès à LSASS ?

1. Ranger l'heure de l'accès à LSASS (question 4) dans une variable :

    ```powershell
    $dumpTime = Get-Date "AAAA-MM-JJ HH:MM:SS"
    ```


2. Garder les ouvertures de session (`4624`) postérieures :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\Dump\*.evtx'; Id=4624} |
        Where-Object { $_.TimeCreated -gt $dumpTime } |
        Format-List
    ```


3. Lire le Logon Type et le compte de chaque connexion : `5` (service, compte `SYSTEM`) relève du fonctionnement normal ; `2` (interactive), `3` (réseau), `9` (NewCredentials) ou `10` (RDP) après un dump méritent d'être examinés. Rappel des Logon Types : [Logon Types](../../analyse-des-journaux-d-evenements-windows-event-logs/04-authentification-et-ouvertures-de-session.md#logon-types).

## Question 6 — Une filiation étrange

**Énoncé HTB Academy.** Dans `C:\Logs\StrangePPID`, trouver le processus parent qui n'aurait pas dû lancer son enfant.

1. Garder les créations de processus (Sysmon `1`) :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\StrangePPID\*.evtx'; Id=1} | Format-List
    ```


2. Chercher les lancements d'invite de commandes :

    ```powershell
    Get-WinEvent -FilterHashtable @{Path='C:\Logs\StrangePPID\*.evtx'; Id=1} |
        Where-Object { $_.Message -like "*cmd.exe*" } |
        Format-List
    ```


3. Dans chaque résultat, lire `ParentImage`, `Image`, `CommandLine`, `User` et `CurrentDirectory` : un parent qui n'a pas vocation à lancer `cmd.exe` est la réponse.

Observateur : *Filter Current Log…* → `1`, puis lire les mêmes champs.
