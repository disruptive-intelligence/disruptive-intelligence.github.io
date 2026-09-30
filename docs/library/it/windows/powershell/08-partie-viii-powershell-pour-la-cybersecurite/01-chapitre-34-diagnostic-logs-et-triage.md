---
title: Chapitre 34 — Diagnostic, logs et triage
source: IT/02_Windows/Powershell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie VIII — Powershell pour LA cybersécurité
  - index.md
---

## 🟢 Le minimum à savoir

### Les journaux d'événements Windows

Les **Event Logs** sont la mémoire de Windows : chaque événement notable (connexion, erreur, démarrage de service, création de compte…) y est enregistré. C'est **la** source d'information pour le diagnostic et la sécurité. La cmdlet moderne est `Get-WinEvent`.

```powershell
# Lister les journaux disponibles et leur volume
Get-WinEvent -ListLog * | Where-Object RecordCount -gt 0 |
    Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending

# Lire les derniers événements d'un journal
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20     # [🔑 Admin]
```


> **📌 Réflexe `Get-Member` :** `Get-WinEvent -LogName System -MaxEvents 1 | Get-Member` révèle `TimeCreated`, `Id`, `LevelDisplayName`, `Message`, `ProviderName`. Ces propriétés permettent de filtrer et corréler les événements.

### Filtrer efficacement avec `-FilterHashtable`

> **⚠️ Point de performance majeur.** Sur un journal de millions d'événements, filtrer **côté serveur** avec `-FilterHashtable` est incomparablement plus rapide que tout ramener puis filtrer avec `Where-Object` (même logique qu'`-Filter` en AD, Ch.23).

```powershell
# ✅ RAPIDE : le filtre est appliqué à la source
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625              # échecs de connexion
    StartTime = (Get-Date).AddHours(-24)
}

# ❌ LENT : ramène tout, puis filtre
Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }
```


### Les Event IDs à connaître

| Event ID | Journal | Signification |
|----------|---------|--------------|
| **4624** | Security | Connexion réussie |
| **4625** | Security | **Échec** de connexion (brute-force si répété) |
| **4634 / 4647** | Security | Déconnexion |
| **4720** | Security | **Création** d'un compte utilisateur |
| **4726** | Security | Suppression d'un compte |
| **4732 / 4728** | Security | Ajout à un groupe (local / global) — surveiller les groupes admin |
| **4688** | Security | Création d'un processus (traçabilité des exécutions) |
| **7045** | System | **Installation d'un nouveau service** (persistance possible) |
| **1102** | Security | **Effacement du journal de sécurité** (signal fort) |

> **⚠️ Les Event IDs dépendent de la stratégie d'audit — l'absence d'un événement ne prouve pas l'absence d'activité.** Windows ne génère la plupart de ces événements que si l'**audit correspondant est activé** (par GPO, Ch.25). Exemple concret : l'événement **4688** (création de processus) n'apparaît que si *Audit Process Creation* est activé ; et pour que la **ligne de commande** du processus soit renseignée dans l'événement, il faut **en plus** activer *Include command line in process creation events* — sinon le champ reste vide.
>
> C'est un piège conceptuel majeur en défense : conclure « aucun 4688 → aucun processus suspect créé » est un **faux négatif**. Le bon réflexe est celui du Ch.35 sur le 4104 : avant d'interpréter une absence, **vérifier que la journalisation est configurée**. Un journal muet peut signifier « rien ne s'est passé »… ou « on n'écoutait pas ».

### Détecter une attaque par brute-force

Un cas d'école, qui réunit filtrage, regroupement et seuil :

```powershell
# Compter les échecs de connexion (4625) par compte sur 24h
Get-WinEvent -FilterHashtable @{ LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24) } |
    ForEach-Object {
        # On convertit l'événement en XML pour lire le champ PAR SON NOM (TargetUserName),
        # plutôt que par une position d'index fragile.
        $xml = [xml]$_.ToXml()
        ($xml.Event.EventData.Data | Where-Object Name -eq 'TargetUserName').'#text'
    } |
    Group-Object |
    Where-Object Count -gt 10 |
    Select-Object @{N="Compte";E={$_.Name}}, Count |
    Sort-Object Count -Descending
```


> **⚠️ Ne lis pas les champs d'un event par index (`$_.Properties[5]`).** L'ordre et le nombre des propriétés d'un événement **varient** selon la version de Windows et le type d'événement : un index en dur casse silencieusement (tu lis le mauvais champ). La méthode robuste : convertir l'événement en XML (`$_.ToXml()`) et lire le champ **par son nom** (`TargetUserName` pour le compte ciblé, `IpAddress` pour la source…). C'est un peu plus verbeux, mais fiable dans le temps.

Un compte avec des dizaines d'échecs en peu de temps = tentative de brute-force à investiguer. C'est exactement le genre de détection qu'un analyste blue team automatise.

## 🟡 Le triage : appliquer ses connaissances d'admin

Le **triage** consiste à examiner rapidement un système suspect. Tout ce qu'on a appris devient un point de contrôle. La logique : **comparer à la normale**.

### Vérifier l'intégrité d'un fichier : `Get-FileHash`

```powershell
Get-FileHash "C:\Windows\System32\cmd.exe" -Algorithm SHA256
```


Comparer le hash d'un fichier à une référence connue détecte une altération. On vérifie aussi un téléchargement contre le hash publié par l'éditeur.

### Vérifier la signature : `Get-AuthenticodeSignature`

```powershell
Get-AuthenticodeSignature "C:\Windows\System32\cmd.exe" |
    Select-Object Status, SignerCertificate
```


Un binaire système **non signé** ou à signature **invalide** dans un emplacement système est très suspect. `Status = Valid` et un signataire Microsoft sont attendus pour les fichiers système.

### Détecter la persistance : les points de démarrage automatique

Un attaquant cherche à **survivre au redémarrage**. Les mécanismes de persistance sont exactement les objets qu'on sait déjà administrer :

```powershell
# 1. Clés Run/RunOnce du registre (rappel Ch.12)
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# 2. Tâches planifiées non-Microsoft (rappel Ch.13)
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, @{N="Action";E={$_.Actions.Execute}}

# 3. Services dont le binaire est dans un emplacement inhabituel (rappel Ch.11)
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -notlike "*\Windows\*" -and $_.PathName -notlike "*Program Files*" } |
    Select-Object Name, PathName, StartName

# 4. Nouveaux services récemment installés (Event ID 7045)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-7) } -ErrorAction SilentlyContinue
```


> **La bascule admin → sécurité :** remarque que ce sont **exactement** les mêmes cmdlets qu'en administration (Ch.11, 12, 13). La différence est l'**intention** : là où l'admin configure, l'analyste **compare à la normale** pour repérer l'anomalie. C'est pour ça qu'on a appris l'administration d'abord.

### Détecter les comptes et connexions suspects

```powershell
# Membres du groupe Administrateurs locaux — ciblé par SID pour être portable FR/EN (rappel Ch.10)
$grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"
Get-LocalGroupMember -Group $grpAdmins.Name

# Connexions établies HORS du réseau 192.168.x.x du lab (rappel Ch.17)
Get-NetTCPConnection -State Established |
    Where-Object { $_.RemoteAddress -notlike "192.168.*" -and $_.RemoteAddress -ne "127.0.0.1" } |
    ForEach-Object {
        [PSCustomObject]@{
            Distant = "$($_.RemoteAddress):$($_.RemotePort)"
            Process = (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name
        }
    }
```


> **⚠️ Heuristique volontairement simplifiée.** Ce filtre ne dit pas « connexion externe » mais « connexion hors du réseau `192.168.x.x` du lab ». D'autres plages **privées** (`10.0.0.0/8`, `172.16.0.0/12`) et l'IPv6 seraient classées à tort comme extérieures. En entreprise, compare aux **plages internes réellement utilisées** chez toi. C'est le principe général du triage : un filtre grossier sert à **réduire le bruit**, pas à produire un verdict — le tri fin reste humain.

### Les Alternate Data Streams (ADS)

NTFS permet de cacher des données dans des **flux alternatifs** attachés à un fichier — une technique de dissimulation classique :

```powershell
# Lister les flux alternatifs d'un fichier
Get-Item "C:\suspect.txt" -Stream * | Select-Object Stream, Length

# Lire un flux caché
Get-Content "C:\suspect.txt" -Stream "cache"
```


Un fichier anodin portant un flux `:` volumineux ou exécutable mérite attention.

## 🔴 Bonus

### Un script de triage synthétique

En pratique, on regroupe ces contrôles dans un script de triage qui produit un rapport horodaté — réutilisant fonctions (Ch.7), objets (Ch.6) et gestion d'erreurs (Ch.8) :

```powershell
function Invoke-QuickTriage {
    [CmdletBinding()]
    param([string]$OutputPath = "C:\triage")

    # Test avant d'agir : le dossier de sortie doit exister
    if (-not (Test-Path $OutputPath)) { New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null }

    # Groupe Administrateurs ciblé par SID → portable FR/EN (rappel Ch.10)
    $grpAdmins = Get-LocalGroup | Where-Object SID -eq "S-1-5-32-544"

    $rapport = [ordered]@{
        Date            = Get-Date
        AdminsLocaux    = (Get-LocalGroupMember -Group $grpAdmins.Name -ErrorAction SilentlyContinue).Name
        TachesNonMs     = (Get-ScheduledTask | Where-Object TaskPath -notlike "\Microsoft\*").TaskName
        RunKeys         = (Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue)
        # Nom honnête : c'est "hors 192.168.x.x", pas "externe" au sens strict
        ConnexionsHorsLAN = (Get-NetTCPConnection -State Established |
            Where-Object RemoteAddress -notlike "192.168.*").RemoteAddress
    }
    $rapport | ConvertTo-Json -Depth 4 |
        Set-Content "$OutputPath\triage_$(Get-Date -Format yyyyMMdd_HHmmss).json" -Encoding UTF8
}
```


C'est un point de départ de triage, pas un outil forensic complet — mais il montre comment tes compétences d'admin se convertissent directement en capacité défensive.

## ❌ Erreur classique

```powershell
# Filtrer les logs côté client (très lent)
Get-WinEvent -LogName Security | Where-Object Id -eq 4625   # ❌
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625}  # ✅

# Conclure trop vite ("un service hors Windows = malware")
# → un binaire hors chemin standard est un SIGNAL à investiguer, pas une preuve
# → toujours corréler (hash, signature, date, contexte) avant de conclure

# Lire le journal Security sans droits admin
Get-WinEvent -LogName Security    # ❌ sans admin → accès refusé
```


## 💡 Exercices

**Guidé :** Compte les échecs de connexion (Event ID 4625) des dernières 24 h et affiche les comptes ayant plus de 5 échecs.

**Autonome :** Écris `Get-PersistenceReport.ps1` qui collecte les clés Run (HKLM + HKCU), les tâches planifiées non-Microsoft et les services hors chemins standard, puis exporte le tout en JSON horodaté. Réutilise ce que tu sais des Ch.11-13.

## ✅ Tu sais maintenant...

- Lire et **filtrer efficacement** les Event Logs (`Get-WinEvent -FilterHashtable`)
- Les Event IDs clés (4624/4625/4720/7045/1102…)
- Détecter une attaque par brute-force
- Vérifier intégrité (`Get-FileHash`) et signature (`Get-AuthenticodeSignature`)
- Trier la persistance (Run, tâches, services) — les **mêmes cmdlets qu'en admin, avec l'intention de détecter**
- Repérer connexions suspectes et flux alternatifs (ADS)

## 💬 Questions d'entretien typiques

- **Comment détecter une attaque par brute-force en PowerShell ?** → Filtrer les Event ID 4625 sur une période, regrouper par compte, alerter au-dessus d'un seuil.
- **Pourquoi `-FilterHashtable` plutôt que `Where-Object` sur les logs ?** → Le filtrage est appliqué à la source : indispensable sur des journaux volumineux.
- **Où un malware cherche-t-il à persister ?** → Clés Run/RunOnce, tâches planifiées, services, dossiers de démarrage — tout ce qu'on sait déjà administrer.
- **Comment vérifier qu'un binaire système est légitime ?** → Sa signature (`Get-AuthenticodeSignature`, statut Valid + signataire attendu) et son hash (`Get-FileHash`) comparé à une référence.

---
