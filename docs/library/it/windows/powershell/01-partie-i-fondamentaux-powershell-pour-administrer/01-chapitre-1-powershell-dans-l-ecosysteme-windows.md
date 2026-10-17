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

Avant même d'apprendre la syntaxe, tape ces commandes pour voir la puissance de l'outil. Ne cherche pas encore à tout comprendre — c'est une bande-annonce. (Si tu n'as jamais ouvert PowerShell : menu Démarrer, tape « PowerShell », puis Entrée. On détaille un peu plus bas.)

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

> **🎯 La consigne pour ce cours : installe PowerShell 7 et apprends avec.**
>
> Ouvre la console PowerShell déjà présente sur ton Windows (la 5.1) et tape :
> ```powershell
> winget install --id Microsoft.PowerShell --source winget
> ```
> Ferme la console, puis ouvre **PowerShell 7** (dans le menu Démarrer, cherche « PowerShell 7 », ou utilise Windows Terminal, voir plus bas). Pour vérifier la version : `$PSVersionTable.PSVersion` doit afficher `7.x`.
>
> **Pourquoi ce choix ?** Les exemples du cours sont écrits pour PowerShell 7, et c'est la version activement développée. Tu évites ainsi les petites différences de comportement entre versions pendant que tu apprends.
>
> **Ce qu'il faut savoir quand même :** la 5.1 reste installée et tu la croiseras partout en entreprise, notamment sur les serveurs. La quasi-totalité de ce cours fonctionne aussi en 5.1, et les rares différences sont signalées dans le texte. Si un jour une commande d'administration se comporte bizarrement en 7, relance-la depuis la 5.1 (`powershell.exe`) : c'est le bon réflexe de dépannage.

### PowerShell vs CMD

Windows a un autre shell historique, **CMD** (l'Invite de commandes). Ce sont deux outils différents :

- **CMD** manipule du **texte brut** et a un jeu de commandes limité (`dir`, `copy`, `ipconfig`…)
- **PowerShell** manipule des **objets** et a des milliers de cmdlets structurées

Beaucoup de commandes CMD et d'exécutables classiques (`ipconfig`, `ping`, `whoami`) fonctionnent aussi depuis PowerShell — mais l'inverse est faux : les cmdlets PowerShell ne fonctionnent pas dans CMD.

### Ouvrir PowerShell (et en administrateur)

- Menu Démarrer → tape « PowerShell 7 » (ou « Windows PowerShell » pour la 5.1)
- Pour les opérations d'administration : **clic droit → Exécuter en tant qu'administrateur**
- Recommandé : **Windows Terminal**, déjà installé sur Windows 11 (sur Windows 10, il est dans le Microsoft Store). Il regroupe PowerShell, CMD et WSL dans une fenêtre à onglets. Une fois PowerShell 7 installé, choisis-le comme profil par défaut : *Paramètres → Démarrage → Profil par défaut → PowerShell*.

> **🔑 Quand faut-il être administrateur ?** Lire est souvent possible sans privilèges (`Get-Service`, `Get-Process`). **Modifier** le système (arrêter un service, écrire dans `HKLM:`, lire le journal Security) nécessite en général une console élevée. Chaque fois que c'est le cas, ce cours l'indique avec `[🔑 Admin]`. Pour vérifier rapidement si ta console est élevée, une astuce : `net session` renvoie une erreur "Accès refusé" si tu n'es **pas** administrateur.

### Les trois gestes de base : se déplacer, créer un fichier, interrompre

Avant d'écrire ton premier script, trois gestes que personne ne pense à expliquer, et sur lesquels tous les débutants butent.

**Geste 1 — Savoir où tu es, et te déplacer.** La console travaille toujours **dans un dossier** : le « dossier courant ». Il est affiché au début de chaque ligne, dans l'invite : `PS C:\Users\toi>` signifie que tu es dans `C:\Users\toi`.

```powershell
Get-Location                  # Où suis-je ? (alias : pwd)
Get-ChildItem                 # Qu'y a-t-il ici ? (alias : ls, dir)
Set-Location C:\Windows       # Aller dans un dossier (alias : cd)
Set-Location ..               # Remonter d'un niveau
Set-Location ~                # Revenir à ton dossier personnel
```


Crée maintenant ton dossier de travail pour tout le cours, et va dedans :

```powershell
New-Item -ItemType Directory -Path "$HOME\Labs\PowerShell"   # $HOME = ton dossier personnel
Set-Location "$HOME\Labs\PowerShell"
```


> **Astuce :** tape `Set-Location $HOME\La` puis appuie sur `Tab` : PowerShell complète le chemin tout seul. La tab-complétion (détaillée plus bas) marche aussi sur les dossiers.

**Geste 2 — Créer un fichier de script sans tomber dans le piège.** Le piège classique du débutant : écrire un script dans le Bloc-notes et l'enregistrer sous `poste.ps1`… que Windows enregistre en réalité sous **`poste.ps1.txt`**. Comme l'Explorateur masque les extensions par défaut, tu vois « poste.ps1 », et rien ne fonctionne. La parade : **crée le fichier depuis PowerShell**, puis ouvre-le pour l'éditer.

```powershell
New-Item -ItemType File -Name poste.ps1    # crée le fichier vide, avec la bonne extension
notepad .\poste.ps1                        # l'ouvre dans le Bloc-notes
# ou, si tu as installé VS Code (recommandé, voir plus bas) :
code .\poste.ps1
```


Le Bloc-notes ouvre un fichier qui existe déjà : quand tu enregistres, il garde son nom exact. Pour vérifier les vrais noms, fais confiance à `Get-ChildItem`, qui affiche toujours l'extension complète. Et rends-toi service une fois pour toutes : dans l'Explorateur, *Affichage → Afficher → Extensions de noms de fichiers*.

**Geste 3 — Interrompre une commande.** Tôt ou tard, tu lanceras une commande qui tourne sans fin (essaie `Get-ChildItem C:\ -Recurse`, qui parcourt tout le disque). Pour l'arrêter : **`Ctrl+C`**. C'est aussi la sortie de secours si l'invite affiche **`>>`** au lieu de `PS C:\...>` : la console attend la suite d'une commande incomplète (un guillemet ou une accolade pas refermés). `Ctrl+C` abandonne et te rend la main.

> **Deux réflexes clavier en prime :** la **flèche du haut** rappelle les commandes précédentes (inutile de retaper), et `Clear-Host` (alias `cls`) nettoie l'écran.

### Ton premier script

Dans ton dossier `Labs\PowerShell`, crée `poste.ps1` comme on vient de le voir, et écris-y :

```powershell
# poste.ps1 — Premières infos sur la machine
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Date        : $(Get-Date)"
```


Enregistre, reviens dans la console (toujours dans le même dossier), et lance-le :

```powershell
.\poste.ps1
```


Le `.\` devant le nom dit à PowerShell « exécute le script du dossier courant » (comme `./` en Bash). C'est une mesure de sécurité : PowerShell ne lance pas un script juste parce qu'on tape son nom. C'est aussi pour ça que le geste 1 compte : si tu n'es pas dans le bon dossier, `.\poste.ps1` ne trouvera rien.

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

### Lire un message d'erreur rouge

Tu viens de croiser ta première erreur rouge. Tu vas en voir des centaines : c'est **normal**, et ce n'est presque jamais grave (surtout avec des commandes `Get-*`, qui ne modifient rien). Une erreur n'est pas un échec, c'est PowerShell qui t'explique ce qui ne va pas. Encore faut-il savoir la lire.

Provoque une erreur volontairement, avec une faute de frappe dans un nom de service :

```powershell
Get-Service -Name Spoolr
```


En **PowerShell 7**, l'erreur est courte :

```
Get-Service: Cannot find any service with service name 'Spoolr'.
```


En **Windows PowerShell 5.1**, elle est plus bavarde (le texte exact varie selon la langue de Windows) :

```
Get-Service : Impossible de trouver un service assorti du nom « Spoolr ».
Au caractère Ligne:1 : 1
+ Get-Service -Name Spoolr
+ ~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Spoolr:String) [Get-Service], ServiceCommandException
    + FullyQualifiedErrorId : NoServiceFoundForGivenName,...
```


**La méthode de lecture, en trois questions :**

1. **Quoi ?** Lis la **première ligne en entier**. Avant les deux-points : la commande qui a échoué. Après : la cause, en clair. Dans 90 % des cas, la réponse est là.
2. **Où ?** Dans un script, l'erreur indique la ligne et la position (`Ligne:12` / `line:12`), et souligne le passage fautif avec `~~~~`. Va directement voir cette ligne.
3. **Quel genre de problème ?** Quelques messages reviennent sans cesse, apprends à les reconnaître :

| Le message contient… | Cause probable | Que faire |
|---|---|---|
| « n'est pas reconnu » / *is not recognized* | Faute de frappe dans la commande, ou module absent | Vérifie l'orthographe, puis `Get-Command <nom>` |
| « Impossible de trouver » / *Cannot find* | Le nom donné n'existe pas (service, fichier, utilisateur…) | Vérifie le nom avec la commande `Get-*` correspondante |
| « Accès refusé » / *Access is denied* | Droits insuffisants | Relance la console **en administrateur** |
| « l'exécution de scripts est désactivée » / *running scripts is disabled* | Execution Policy | Voir la section précédente |

**Relire une erreur passée :** PowerShell garde toutes les erreurs de la session dans la variable `$Error`. La plus récente est `$Error[0]`. En PowerShell 7, `Get-Error` affiche **tous** les détails de la dernière erreur : pratique quand le message court ne suffit pas.

```powershell
$Error[0]        # la dernière erreur
Get-Error        # [⚡ PS7+] le détail complet de la dernière erreur
```


> **Le bon réflexe :** une erreur rouge, on la **lit**, en entier, avant de faire quoi que ce soit d'autre. La tentation du débutant est de la survoler et de retaper la commande au hasard. Prends dix secondes pour lire la première ligne : elle te fait presque toujours gagner dix minutes. Au Ch.8, on apprendra à **gérer** les erreurs dans un script ; ici, on apprend juste à les **comprendre**.

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

# Ne pas être dans le bon dossier
.\poste.ps1      # ❌ "non reconnu" alors que le fichier existe → vérifie avec Get-Location

# Le script enregistré en poste.ps1.txt par le Bloc-notes
Get-ChildItem    # ✅ affiche le vrai nom, extension comprise

# L'invite affiche >> et plus rien ne répond
# → commande incomplète (guillemet ou accolade non fermés) : Ctrl+C pour sortir

# Utiliser les options Linux avec les alias
ls -la           # ❌
Get-ChildItem -Force   # ✅

# Confondre PowerShell et CMD
# Les cmdlets (Get-Service…) ne fonctionnent PAS dans CMD
```


## 💡 Exercices

**Guidé :** Ouvre PowerShell, lance `Get-Command -Verb Get | Measure-Object` pour compter combien de cmdlets `Get-*` existent sur ta machine. Puis `Get-Command -Noun Service` pour voir toutes les commandes liées aux services.

**Guidé (erreurs) :** Provoque trois erreurs différentes : une commande mal orthographiée (`Get-Servise`), un nom inexistant (`Get-Service -Name Spoolr`), et un dossier inexistant (`Set-Location C:\Nulle\Part`). Pour chacune, applique la méthode : *quoi ?*, *où ?*, *quel genre ?*. Puis affiche la dernière avec `$Error[0]`.

**Autonome :** Utilise `Get-Help` pour trouver comment lister uniquement les services *arrêtés* avec `Get-Service`. (Indice : `Get-Help Get-Service -Examples`.)

## ✅ Tu sais maintenant...

- Installer PowerShell 7 et savoir pourquoi on apprend avec
- Te déplacer (`Get-Location`, `Set-Location`), créer un script sans le piège du `.txt`, interrompre une commande avec `Ctrl+C`
- Lire un message d'erreur rouge : *quoi ?*, *où ?*, *quel genre ?*, et le retrouver avec `$Error[0]`
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
