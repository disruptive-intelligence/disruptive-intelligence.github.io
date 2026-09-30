---
title: Chapitre 13 — Tâches planifiées
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### À quoi ça sert

Une **tâche planifiée** exécute un programme ou un script automatiquement : à heure fixe, au démarrage, à la connexion d'un utilisateur, ou sur événement. C'est l'équivalent Windows de `cron` sous Linux — et c'est ainsi qu'on **automatise** l'exécution de ses scripts PowerShell (sauvegardes, rapports, nettoyages).

### Lister et inspecter les tâches

```powershell
Get-ScheduledTask                                   # toutes les tâches
Get-ScheduledTask -TaskName "MaTache"               # une tâche
Get-ScheduledTask | Where-Object State -eq "Ready"  # les tâches actives

# Infos d'exécution (dernier/prochain lancement, dernier résultat)
Get-ScheduledTask -TaskName "MaTache" | Get-ScheduledTaskInfo
```


> **📌 Réflexe `Get-Member` :** `Get-ScheduledTask | Get-Member` montre `TaskName`, `TaskPath`, `State`, `Actions`, `Triggers`, `Principal`. Une tâche est un objet composé : elle contient des **actions** (quoi exécuter) et des **déclencheurs** (quand).

### Les 4 briques d'une tâche

Créer une tâche, c'est assembler quatre éléments :

1. **Action** — quoi exécuter (`New-ScheduledTaskAction`)
2. **Déclencheur (trigger)** — quand (`New-ScheduledTaskTrigger`)
3. **Principal** — sous quel compte et avec quels privilèges (`New-ScheduledTaskPrincipal`)
4. **Enregistrement** — assembler et créer (`Register-ScheduledTask`)

### Créer une tâche planifiée `[🔑 Admin]`

```powershell
# 1. Action : lancer un script PowerShell
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -File C:\Scripts\backup.ps1"

# 2. Déclencheur : tous les jours à 2h du matin
$trigger = New-ScheduledTaskTrigger -Daily -At "02:00"

# 3. Principal : exécuter en tant que SYSTEM, avec privilèges élevés
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

# 4. Enregistrer
Register-ScheduledTask -TaskName "BackupQuotidien" `
    -Action $action -Trigger $trigger -Principal $principal `
    -Description "Sauvegarde quotidienne à 2h"
```


> **Note sur l'argument :** pour lancer un script `.ps1`, on exécute `powershell.exe` (ou `pwsh.exe` en PS7) avec `-File`. `-NoProfile` (ignore le profil, pour un environnement prévisible) est une bonne habitude.
>
> **⚠️ À propos de `-ExecutionPolicy Bypass` :** on voit souvent `-ExecutionPolicy Bypass` ajouté ici par réflexe. **Ne l'utilise pas systématiquement.** Rappel du Ch.1 : l'Execution Policy n'est pas une frontière de sécurité, mais l'ajouter aveuglément dans chaque tâche est une mauvaise habitude qui banalise le contournement. La bonne approche : le script tourne sous une **policy correctement configurée** (souvent `RemoteSigned` imposée par GPO) ou, mieux, il est **signé** (Ch.35). Réserve `Bypass` à un choix **volontaire et justifié** dans un contexte contrôlé — pas à une recette copiée-collée partout.

### Supprimer une tâche

```powershell
Unregister-ScheduledTask -TaskName "BackupQuotidien" -Confirm:$false
```


## 🟡 Très utile en pratique

### Comprendre le contexte d'exécution

Une tâche s'exécute sous un **compte** avec un **niveau de privilège** — deux points cruciaux :

- **Le compte** (`-UserId`) : `SYSTEM` (tout-puissant local), un compte de service dédié, ou un utilisateur. Détermine les droits **et** l'accès réseau.
- **Le niveau** (`-RunLevel`) : `Limited` (normal) ou `Highest` (élevé). Un script qui touche à `HKLM:` ou aux services a besoin de `Highest`.
- **« Exécuter même si l'utilisateur n'est pas connecté »** : implique de stocker des identifiants — sujet sécurité (Ch.33).

> **Réflexe sécurité :** une tâche planifiée tournant en `SYSTEM` qui lance un script modifiable par tous est une porte d'entrée classique pour l'élévation de privilèges. On y revient au Ch.34 (triage de persistance) : les tâches planifiées sont un mécanisme de persistance très utilisé.

### Différents types de déclencheurs

```powershell
New-ScheduledTaskTrigger -Daily -At "02:00"                  # quotidien
New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At "8am"  # hebdomadaire
New-ScheduledTaskTrigger -AtStartup                          # au démarrage machine
New-ScheduledTaskTrigger -AtLogOn                            # à la connexion
```


## 🔴 Bonus

### Auditer les tâches non standard

```powershell
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, TaskPath, State,
        @{N="Action";E={$_.Actions.Execute}}
```


Filtrer les tâches hors `\Microsoft\*` fait ressortir celles ajoutées par des logiciels ou des humains — un bon point de départ pour un audit (et pour du triage de sécurité, Ch.34).

## ❌ Erreur classique

```powershell
# Ajouter -ExecutionPolicy Bypass par réflexe dans CHAQUE tâche
-Argument "-NoProfile -ExecutionPolicy Bypass -File C:\s.ps1"   # ⚠️ mauvaise habitude
# ✅ compter sur une policy correcte (GPO) ou un script signé ; Bypass = choix justifié seulement

# Créer une tâche SYSTEM lançant un script world-writable
# ❌ risque d'élévation de privilèges — protéger les ACL du script (Ch.9)

# Chemins relatifs dans une tâche
-Argument "-File .\backup.ps1"     # ❌ le dossier courant n'est pas garanti
-Argument "-File C:\Scripts\backup.ps1"   # ✅ chemin absolu
```


## 💡 Exercices

**Guidé :** Liste les tâches planifiées actives (`State -eq "Ready"`) qui ne sont pas dans `\Microsoft\`, avec leur nom et l'exécutable lancé.

**Autonome :** Crée une tâche `RapportHebdo` qui lance un script PowerShell tous les lundis à 8h, puis vérifie sa création avec `Get-ScheduledTaskInfo`, puis supprime-la.

## ✅ Tu sais maintenant...

- Le rôle des tâches planifiées (automatiser ses scripts, équivalent `cron`)
- Lister et inspecter (`Get-ScheduledTask`, `Get-ScheduledTaskInfo`)
- Les 4 briques : action, déclencheur, principal, enregistrement
- L'importance du **contexte d'exécution** (compte + niveau de privilège)
- Le lien avec la sécurité (persistance, à revoir Ch.34)

## 💬 Questions d'entretien typiques

- **Comment automatiser l'exécution quotidienne d'un script PowerShell ?** → Une tâche planifiée avec une action `powershell.exe -File ...` et un déclencheur `-Daily`.
- **Pourquoi le compte d'exécution d'une tâche est-il sensible ?** → Il détermine les privilèges ; une tâche `SYSTEM` lançant un script modifiable par tous permet une élévation de privilèges.
- **Équivalent de `cron` sous Windows ?** → Le Planificateur de tâches, piloté par les cmdlets `*-ScheduledTask*`.

---
