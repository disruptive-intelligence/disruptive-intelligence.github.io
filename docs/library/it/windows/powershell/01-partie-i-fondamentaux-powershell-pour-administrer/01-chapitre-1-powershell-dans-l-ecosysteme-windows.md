---
title: Chapitre 1 — PowerShell dans l'écosystème Windows
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie I — Fondamentaux PowerShell pour administrer Windows
  - index.md
---

## 🟢 Le minimum à savoir

### Qu'est-ce que PowerShell ?

PowerShell est **trois choses à la fois** :

1. **Un terminal (un shell)** — tu tapes des commandes, il les exécute
2. **Un langage de scripting** — tu écris des scripts pour automatiser
3. **Un outil d'administration Windows** — tu pilotes services, processus, utilisateurs, registre, réseau, Active Directory…

C'est ce troisième point qui nous intéresse le plus. Tout ce que tu peux faire dans les interfaces graphiques de Windows (le Gestionnaire des tâches, les Services, l'Observateur d'événements, la console AD…), tu peux le faire en PowerShell — plus vite, de façon reproductible, et surtout **automatisable** et applicable à **des centaines de machines à la fois**.

### Un aperçu de ce qu'on va pouvoir faire

Avant même d'apprendre la syntaxe, tape ces commandes pour voir la puissance de l'outil. Ne cherche pas encore à tout comprendre — c'est une bande-annonce :

```powershell
Get-Service                     # Tous les services Windows et leur état
Get-Process                     # Tous les programmes en cours d'exécution
Get-ComputerInfo                # Une fiche complète de la machine
Get-CimInstance Win32_OperatingSystem   # Infos sur le système d'exploitation
Get-NetIPAddress                # Les adresses IP de la machine
```


Chacune de ces commandes t'a renvoyé des informations structurées. C'est le cœur de PowerShell, et on va apprendre à l'exploiter méthodiquement.

### La convention Verbe-Nom

Toutes les commandes PowerShell (les **cmdlets**) suivent le même pattern : **`Verbe-Nom`**.

| Verbe | Signification | Exemples d'administration |
|-------|--------------|--------------------------|
| `Get` | Obtenir, lire | `Get-Service`, `Get-Process`, `Get-ADUser` |
| `Set` | Modifier, configurer | `Set-Service`, `Set-ADUser` |
| `New` | Créer | `New-LocalUser`, `New-ADUser`, `New-Item` |
| `Remove` | Supprimer | `Remove-Item`, `Remove-ADUser` |
| `Start` / `Stop` | Démarrer / arrêter | `Start-Service`, `Stop-Process` |
| `Restart` | Redémarrer | `Restart-Service`, `Restart-Computer` |
| `Test` | Vérifier | `Test-Path`, `Test-Connection`, `Test-NetConnection` |
| `Enable` / `Disable` | Activer / désactiver | `Enable-ADAccount`, `Disable-LocalUser` |

C'est la grande force de PowerShell : la convention est **prédictible**. Tu ne connais pas la commande pour lister les services ? Essaie `Get-Service`. Pour en arrêter un ? `Stop-Service`. Pour changer sa configuration ? `Set-Service`. Ça marche presque toujours.

> **Comparaison avec Bash :** en Bash, les noms sont courts et souvent cryptiques (`ls`, `ps`, `grep`, `awk`). En PowerShell, ils sont longs mais explicites. C'est plus verbeux à taper, mais tu **devines** la commande au lieu de la mémoriser — un énorme avantage quand tu débutes.

> **La discipline `Get` d'abord :** remarque que la moitié des verbes ci-dessus ne font que **lire** (`Get`, `Test`). C'est voulu. En administration, on regarde toujours avant de modifier. On y reviendra sans cesse.

### Les 3 commandes pour tout découvrir

Ces trois cmdlets sont ta porte d'entrée vers tout le reste de PowerShell. Retiens-les avant tout :

```powershell
# 1. TROUVER une commande
Get-Command *Service*        # Toutes les cmdlets contenant "Service"
Get-Command -Verb Get        # Toutes les cmdlets qui commencent par "Get"
Get-Command -Noun ADUser     # Toutes les cmdlets qui agissent sur "ADUser"

# 2. COMPRENDRE une commande
Get-Help Get-Service                 # L'aide
Get-Help Get-Service -Examples       # Des exemples concrets (le plus utile !)
Get-Help Get-Service -Online         # L'aide complète dans le navigateur

# 3. EXPLORER ce qu'une commande retourne
Get-Service | Get-Member     # Les propriétés et méthodes d'un objet "service"
```


> **📌 Réflexe transversal — `Get-Member` :** `Get-Service | Get-Member` te montre **tout** ce que contient un objet service : ses propriétés (`Name`, `Status`, `StartType`…) et ses méthodes (`.Start()`, `.Stop()`…). Chaque fois que ce cours introduira un nouvel objet (un utilisateur AD, une tâche planifiée, une réponse d'API…), le réflexe sera le même : le passer dans `Get-Member` pour l'explorer. On ne mémorise pas PowerShell, on l'explore.

> **Première utilisation de l'aide :** PowerShell peut te proposer de télécharger les fichiers d'aide détaillés. Lance une fois `Update-Help -ErrorAction SilentlyContinue` (nécessite Internet et, selon la version, des droits admin). Sans ça, `Get-Help` reste minimal.

### Windows PowerShell 5.1 vs PowerShell 7

Il existe **deux** versions qui coexistent, et c'est important de le comprendre :

| | Windows PowerShell **5.1** | PowerShell **7+** |
|---|---|---|
| Exécutable | `powershell.exe` | `pwsh.exe` |
| Installé par défaut sur Windows ? | ✅ Oui | ❌ Non (à installer) |
| Multi-plateforme (Linux/Mac) ? | ❌ Non | ✅ Oui |
| Basé sur | .NET Framework | .NET (Core) |
| Modules AD, GPO, DNS Server… | ✅ Oui (via RSAT) | ✅ Oui (compatibilité) |

**Pour ce cours :** Windows PowerShell 5.1, déjà présent sur ton Windows, suffit pour la quasi-totalité du contenu. C'est aussi souvent la seule version disponible sur les serveurs en production. Les points spécifiques à PowerShell 7 sont signalés `[⚡ PS7+]`.

> **Où télécharger PowerShell 7 :** sur le dépôt officiel [github.com/PowerShell/PowerShell](https://github.com/PowerShell/PowerShell). Utile surtout si tu veux les nouveautés du langage ou travailler aussi sous Linux/Mac.

### PowerShell vs CMD

Windows a un autre shell historique, **CMD** (l'Invite de commandes). Ce sont deux outils différents :

- **CMD** manipule du **texte brut** et a un jeu de commandes limité (`dir`, `copy`, `ipconfig`…)
- **PowerShell** manipule des **objets** et a des milliers de cmdlets structurées

Beaucoup de commandes CMD et d'exécutables classiques (`ipconfig`, `ping`, `whoami`) fonctionnent aussi depuis PowerShell — mais l'inverse est faux : les cmdlets PowerShell ne fonctionnent pas dans CMD.

### Ouvrir PowerShell (et en administrateur)

- Menu Démarrer → tape "PowerShell" → **Windows PowerShell**
- Pour les opérations d'administration : **clic droit → Exécuter en tant qu'administrateur**
- Recommandé : **Windows Terminal** (depuis le Microsoft Store), qui regroupe PowerShell, CMD et WSL dans une fenêtre à onglets

> **🔑 Quand faut-il être administrateur ?** Lire est souvent possible sans privilèges (`Get-Service`, `Get-Process`). **Modifier** le système (arrêter un service, écrire dans `HKLM:`, lire le journal Security) nécessite en général une console élevée. Chaque fois que c'est le cas, ce cours l'indique avec `[🔑 Admin]`. Pour vérifier rapidement si ta console est élevée, une astuce : `net session` renvoie une erreur "Accès refusé" si tu n'es **pas** administrateur.

### Ton premier script

Crée un dossier de travail et un fichier `poste.ps1` :

```powershell
# poste.ps1 — Premières infos sur la machine
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Date        : $(Get-Date)"
```


Pour le lancer :

```powershell
.\poste.ps1
```


Le `.\` devant le nom dit à PowerShell « exécute le script du dossier courant » (comme `./` en Bash). C'est une mesure de sécurité : PowerShell ne lance pas un script juste parce qu'on tape son nom.

Tu obtiens probablement une **erreur rouge** parlant de politique d'exécution. C'est le prochain point.

### La politique d'exécution (Execution Policy)

Par défaut, Windows bloque l'exécution des scripts `.ps1`. Pour l'autoriser :

```powershell
# Voir la politique actuelle
Get-ExecutionPolicy

# Autoriser les scripts locaux pour ton compte utilisateur
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


| Politique | Effet |
|-----------|-------|
| `Restricted` | Aucun script ne s'exécute (défaut sur les clients Windows) |
| `RemoteSigned` | Les scripts locaux fonctionnent ; ceux téléchargés doivent être signés |
| `Unrestricted` / `Bypass` | Tout passe (à éviter) |

> **⚠️ Point technique important — l'Execution Policy n'est PAS une barrière de sécurité.** C'est un **garde-fou anti-erreur**, pas une protection contre un attaquant. Elle empêche un double-clic accidentel de lancer un script, mais elle se contourne trivialement — par exemple `powershell -ExecutionPolicy Bypass -File script.ps1`, ou en copiant-collant le contenu du script dans la console. Ne compte jamais dessus pour te protéger d'un code malveillant. Les vraies protections d'exécution (contrôle applicatif App Control/WDAC ou AppLocker, qui déclenche le Constrained Language Mode, et signature de code) sont vues en Partie VIII. Retiens : `RemoteSigned` en `CurrentUser` est le bon réglage **de confort** pour apprendre. En entreprise, cette politique est généralement imposée par GPO.

### Les commentaires

```powershell
# Commentaire sur une ligne

<#
Commentaire
sur plusieurs lignes
#>

Write-Output "Ceci s'affiche"   # Commentaire en fin de ligne
```


## 🟡 Très utile en pratique

### Les alias : passerelle avec Bash et CMD

PowerShell fournit des raccourcis (**alias**) pour les commandes courantes :

| Tu tapes | PowerShell exécute | Équivalent Bash |
|----------|-------------------|-----------------|
| `ls` / `dir` | `Get-ChildItem` | `ls` |
| `cd` | `Set-Location` | `cd` |
| `cat` / `type` | `Get-Content` | `cat` |
| `cp` | `Copy-Item` | `cp` |
| `rm` / `del` | `Remove-Item` | `rm` |
| `cls` | `Clear-Host` | `clear` |

Pratiques pour taper vite dans la console. **Mais dans un script, utilise toujours les noms complets** (`Get-ChildItem` plutôt que `ls`) : c'est plus lisible et portable.

> **Attention :** ces alias appellent des cmdlets PowerShell, pas les vraies commandes Linux. `ls -la` ne fonctionne pas ; l'équivalent est `Get-ChildItem -Force`.

### Un éditeur : VS Code

Pour écrire des scripts confortablement, installe **Visual Studio Code** avec l'extension **PowerShell** (gratuit, multi-plateforme). Il offre coloration, autocomplétion et débogage. L'ancien **PowerShell ISE** (intégré à Windows) fonctionne aussi mais n'est plus développé.

### La tab-complétion

Tape le début d'une cmdlet et appuie sur `Tab` : PowerShell complète. Ça marche aussi sur les paramètres (`Get-Service -N` + Tab → `-Name`). Indispensable et anti-fautes de frappe.

## 🔴 Bonus

### Le profil PowerShell

Le profil est un script qui s'exécute à chaque ouverture de PowerShell (comme le `.bashrc` de Bash). Utile pour définir des raccourcis ou des fonctions perso :

```powershell
$PROFILE            # Le chemin de ton profil
notepad $PROFILE    # L'éditer
```


### PowerShell Gallery

Le dépôt public de modules ([powershellgallery.com](https://www.powershellgallery.com/)), équivalent de PyPI ou npm :

```powershell
Install-Module -Name <NomDuModule> -Scope CurrentUser
```


## ❌ Erreur classique

```powershell
# Croire que l'Execution Policy sécurise le système
# → NON : c'est un garde-fou anti-erreur, contournable trivialement

# Oublier le .\ devant un script
poste.ps1        # ❌ "terme non reconnu"
.\poste.ps1      # ✅

# Utiliser les options Linux avec les alias
ls -la           # ❌
Get-ChildItem -Force   # ✅

# Confondre PowerShell et CMD
# Les cmdlets (Get-Service…) ne fonctionnent PAS dans CMD
```


## 💡 Exercices

**Guidé :** Ouvre PowerShell, lance `Get-Command -Verb Get | Measure-Object` pour compter combien de cmdlets `Get-*` existent sur ta machine. Puis `Get-Command -Noun Service` pour voir toutes les commandes liées aux services.

**Autonome :** Utilise `Get-Help` pour trouver comment lister uniquement les services *arrêtés* avec `Get-Service`. (Indice : `Get-Help Get-Service -Examples`.)

## ✅ Tu sais maintenant...

- Ce qu'est PowerShell (shell + langage + outil d'administration)
- La convention `Verbe-Nom` et pourquoi elle rend PowerShell prédictible
- Le trio `Get-Command` / `Get-Help` / `Get-Member` pour tout découvrir
- Le réflexe `Get-Member` pour explorer n'importe quel objet
- La différence 5.1 vs 7, PowerShell vs CMD
- Exécuter un script et régler l'Execution Policy — **en sachant qu'elle n'est pas une sécurité**

## 💬 Questions d'entretien typiques

- **Qu'est-ce qu'une cmdlet ?** → Une commande native PowerShell nommée `Verbe-Nom`, qui retourne des objets (pas du texte).
- **Comment découvrir une commande inconnue ?** → `Get-Command` pour la trouver, `Get-Help -Examples` pour l'utiliser, `Get-Member` pour explorer ce qu'elle retourne.
- **L'Execution Policy protège-t-elle des malwares ?** → Non. C'est un garde-fou anti-exécution accidentelle, contournable trivialement (`-ExecutionPolicy Bypass`, copier-coller…). Les vraies protections sont le contrôle applicatif (App Control/WDAC ou AppLocker) qui déclenche le Constrained Language Mode, plus la signature.
- **Différence Windows PowerShell 5.1 / PowerShell 7 ?** → 5.1 est intégré à Windows, basé sur .NET Framework, Windows uniquement. 7 est à installer, basé sur .NET, multi-plateforme.

---
