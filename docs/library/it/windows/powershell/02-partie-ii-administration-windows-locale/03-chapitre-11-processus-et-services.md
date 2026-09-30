---
title: Chapitre 11 — Processus et services
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie II — Administration windows locale
  - index.md
---

## 🟢 Le minimum à savoir

### Processus vs services : la distinction

- Un **processus** est un programme en cours d'exécution (une instance de `chrome.exe`, `notepad.exe`…). Il a un **PID** (identifiant numérique).
- Un **service** est un programme qui tourne en **arrière-plan**, souvent sans interface, géré par Windows (démarrage automatique, redémarrage en cas d'échec…). Le pare-feu, Windows Update, le spouleur d'impression sont des services.

Un service, quand il tourne, s'exécute *via* un ou plusieurs processus — mais on les gère avec des cmdlets différentes.

### Gérer les processus

```powershell
Get-Process                          # tous les processus
Get-Process -Name chrome             # par nom
Get-Process -Id 1234                 # par PID

# Les 5 plus gros consommateurs de mémoire
Get-Process | Sort-Object WorkingSet64 -Descending |
    Select-Object Name, Id, @{N="RAM(Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 5

# Lancer / arrêter
Start-Process notepad
Start-Process "C:\outil.exe" -ArgumentList "/silent"
Stop-Process -Name notepad
Stop-Process -Id 1234 -Force
```


> **📌 Réflexe `Get-Member` :** `Get-Process | Get-Member` révèle `Id`, `Name`, `CPU`, `WorkingSet64` (mémoire), `Path`, `StartTime`, et des méthodes comme `.Kill()`. Un processus est un objet riche — on peut trier, filtrer, corréler.

> **⚠️ `Stop-Process` est brutal :** il tue le processus sans sauvegarde (comme `kill -9`). Vérifie le PID/nom avant. Certains processus système protégés nécessitent `[🔑 Admin]`.

### Gérer les services

```powershell
Get-Service                           # tous les services
Get-Service -Name wuauserv            # un service précis (Windows Update)
Get-Service | Where-Object Status -eq "Running"    # ceux qui tournent

# Contrôler un service                                   [🔑 Admin]
Start-Service   -Name wuauserv
Stop-Service    -Name wuauserv
Restart-Service -Name wuauserv

# Changer le type de démarrage                           [🔑 Admin]
Set-Service -Name wuauserv -StartupType Automatic   # Automatic / Manual / Disabled
```


Les propriétés clés d'un service : `Name`, `DisplayName`, `Status` (Running/Stopped), `StartType` (Automatic/Manual/Disabled), `DependentServices`, `ServicesDependedOn`.

### Le point à investiguer : Automatic + Stopped

Un service configuré en démarrage **automatique** mais actuellement **arrêté** est un **point à investiguer** — pas nécessairement une panne :

```powershell
# Version portable 5.1 et 7 via CIM (StartMode = "Auto" pour les services automatiques)
Get-CimInstance Win32_Service |
    Where-Object { $_.StartMode -eq "Auto" -and $_.State -eq "Stopped" } |
    Select-Object Name, DisplayName, StartMode, State
```


> **⚠️ Nuance importante — « Automatic + Stopped » n'est pas toujours une anomalie.** Windows gère des services **déclenchés par événement** (*trigger-start*) : un service peut être configuré en automatique (ou automatique-différé), démarrer quand un événement survient, puis **s'arrêter légitimement** quand il n'a plus de travail. Le voir `Stopped` à un instant donné peut être parfaitement normal. Microsoft recommande même ce modèle *trigger-start* dans certains scénarios.
>
> La bonne façon de raisonner la **conformité** n'est donc pas « tout service Automatic doit être Running », mais : **comparer l'état observé à une baseline attendue** (la liste des services qui, chez toi, *doivent* tourner en permanence). Un service critique attendu en fonctionnement continu et trouvé arrêté = à investiguer ; un service *trigger-start* arrêté = souvent normal.

C'est un contrôle de santé que tout administrateur fait régulièrement — en gardant cette nuance à l'esprit.

### Les dépendances de services

Certains services en requièrent d'autres. Le savoir évite les mauvaises surprises quand on en arrête un :

```powershell
(Get-Service -Name wuauserv).ServicesDependedOn    # ce dont dépend Windows Update
(Get-Service -Name rpcss).DependentServices         # ce qui dépend de RPCSS
```


> **Piège :** arrêter un service dont dépendent d'autres services les arrête aussi (avec `-Force`) ou échoue (sans). Toujours vérifier `DependentServices` avant un `Stop-Service`.

## 🟡 Très utile en pratique

### `Get-Service` vs `Get-CimInstance Win32_Service`

`Get-Service` est simple mais limité. Pour obtenir le **compte de service**, le **chemin de l'exécutable** ou le **PID**, on passe par CIM :

```powershell
Get-CimInstance Win32_Service |
    Select-Object Name, State, StartMode, StartName, PathName |
    Where-Object { $_.StartName -notlike "*LocalSystem*" }
```


`StartName` (le compte sous lequel tourne le service) et `PathName` (le binaire) sont essentiels en administration **et** en sécurité — un service tournant depuis un chemin inhabituel est suspect (on approfondit au Ch.34).

### Un contrôle de santé de services critiques

```powershell
function Test-CriticalServices {
    [CmdletBinding()]
    param([string[]]$Services = @("wuauserv","WinDefend","EventLog","Spooler"))

    foreach ($nom in $Services) {
        $svc = Get-Service -Name $nom -ErrorAction SilentlyContinue
        # StartMode via CIM = portable 5.1 et 7 (contrairement à $svc.StartType, PS7 seulement)
        $cim = Get-CimInstance Win32_Service -Filter "Name='$nom'" -ErrorAction SilentlyContinue
        [PSCustomObject]@{
            Service   = $nom
            Present   = [bool]$svc
            Statut    = if ($svc) { $svc.Status } else { "ABSENT" }
            Demarrage = if ($cim) { $cim.StartMode } else { "-" }   # Auto / Manual / Disabled
        }
    }
}

Test-CriticalServices | Format-Table -AutoSize
```


Ce petit outil réunit fonctions (Ch.7), gestion d'absence (Ch.8), collections (Ch.6) et PSCustomObject. Il utilise `Win32_Service`.`StartMode` pour rester portable entre Windows PowerShell 5.1 et PowerShell 7.

## 🔴 Bonus

### Processus et leur ligne de commande complète

La ligne de commande exacte d'un processus (arguments inclus) est précieuse pour le diagnostic :

```powershell
Get-CimInstance Win32_Process -Filter "Name = 'powershell.exe'" |
    Select-Object ProcessId, CommandLine
```


Un `powershell.exe` lancé avec des arguments encodés en base64 est un signal d'alerte (Ch.34).

## ❌ Erreur classique

```powershell
# Arrêter un service sans vérifier ses dépendances
Stop-Service RPCSS            # ❌ échoue ou casse une cascade de services
(Get-Service RPCSS).DependentServices   # ✅ vérifier d'abord

# Utiliser Get-Service quand on a besoin du chemin/compte du service
Get-Service wuauserv | Select-Object Path    # ❌ pas de propriété Path
Get-CimInstance Win32_Service -Filter "Name='wuauserv'" | Select PathName, StartName  # ✅

# Tuer un processus par nom alors que plusieurs instances tournent
Stop-Process -Name chrome     # ⚠️ tue TOUTES les instances de Chrome
```


## 💡 Exercices

**Guidé :** Affiche les services en démarrage automatique actuellement arrêtés, triés par nom.

**Autonome :** Écris un script qui prend un `-ServiceName`, vérifie ses dépendances (`ServicesDependedOn`), et n'affiche un message de redémarrage possible que si toutes ses dépendances sont `Running`.

## 🧩 Mini-projet — Rapport de services critiques

Étends `Test-CriticalServices` : la conformité se juge **par rapport à une baseline** que tu définis (les services qui, chez toi, doivent tourner en permanence). Ajoute une colonne `Conforme` (True si un service **attendu en fonctionnement** est bien `Running`), affiche en couleur les non-conformes, et exporte le rapport complet en CSV horodaté (`services_$(Get-Date -Format yyyyMMdd).csv`). Note que « Automatic + Stopped » seul ne suffit pas à conclure : compare à ta liste attendue.

## ✅ Tu sais maintenant...

- La différence processus / service
- Gérer les processus (`Get/Start/Stop-Process`) et les services (`Get/Start/Stop/Restart/Set-Service`)
- Repérer le point à investiguer « Automatic + Stopped » — en le comparant à une baseline (pas une anomalie automatique, à cause des services *trigger-start*)
- Vérifier les dépendances avant d'arrêter un service
- Passer par `Win32_Service` pour le compte et le chemin d'un service

## 💬 Questions d'entretien typiques

- **Différence entre un processus et un service ?** → Un processus est un programme en cours ; un service tourne en arrière-plan sous le contrôle du gestionnaire de services (démarrage auto, resilience).
- **Comment obtenir le chemin du binaire d'un service ?** → `Get-CimInstance Win32_Service` (propriété `PathName`), car `Get-Service` ne l'expose pas.
- **Quel contrôle de santé faire sur les services ?** → Comparer l'état à une baseline : les services *attendus en fonctionnement continu* doivent être `Running`. « Automatic + Stopped » est un point à investiguer, mais pas une anomalie en soi (services *trigger-start*).

---
