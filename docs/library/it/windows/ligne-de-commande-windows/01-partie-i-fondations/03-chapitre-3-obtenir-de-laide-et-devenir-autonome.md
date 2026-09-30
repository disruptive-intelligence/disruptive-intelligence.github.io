---
title: Chapitre 3 — Obtenir de l’aide et devenir autonome
source: IT/02_Windows/Windows_Command-Line.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

Ce chapitre est **fondamental**. Si tu sais obtenir de l’aide tout seul, tu n’as plus besoin de mémoriser des centaines de commandes — tu les retrouves quand tu en as besoin.

### L’aide dans CMD

Chaque commande CMD a une aide intégrée, accessible avec `/?` :

```cmd
dir /?              REM Affiche l'aide de la commande dir
ipconfig /?         REM Affiche l'aide de ipconfig
xcopy /?            REM Affiche l'aide de xcopy

help                REM Liste les commandes CMD de base
help dir            REM Aide détaillée sur dir (même chose que dir /?)
```


### L’aide dans PowerShell : le trio de survie

PowerShell a un système d’aide beaucoup plus riche. Trois commandes à retenir absolument :

**1. `Get-Help` — comprendre une commande :**

```powershell
Get-Help Get-Process              # Aide de base
Get-Help Get-Process -Examples    # Des exemples concrets (le plus utile !)
Get-Help Get-Process -Detailed    # Aide détaillée avec paramètres
Get-Help Get-Process -Online      # Ouvre l'aide en ligne dans le navigateur
```


> **Première utilisation :** PowerShell peut te demander de mettre à jour les fichiers d’aide. Tape `Update-Help -ErrorAction SilentlyContinue` une première fois (nécessite Internet).

**2. `Get-Command` — trouver une commande :**

```powershell
Get-Command *Process*            # Quelles commandes contiennent "Process" ?
Get-Command *Service*            # Tout ce qui touche aux services
Get-Command -Verb Get            # Toutes les commandes qui commencent par "Get"
Get-Command -Noun Item           # Toutes les commandes qui concernent "Item"
```


Tu ne connais pas la commande pour gérer les services ? `Get-Command *Service*` te donne `Get-Service`, `Start-Service`, `Stop-Service`, `Restart-Service`…

**3. `Get-Member` — explorer ce que retourne une commande :**

```powershell
Get-Process | Get-Member         # Quelles propriétés a un objet "processus" ?
```


`Get-Member` montre les **propriétés** (informations) et **méthodes** (actions) d’un objet PowerShell. C’est comme ça que tu découvres ce que tu peux faire avec un résultat. On y reviendra au chapitre 9.

### Comprendre les alias PowerShell

PowerShell fournit des **alias** (des raccourcis) pour les commandes courantes :

```powershell
Get-Alias               # Voir tous les alias
Get-Alias dir            # dir = Get-ChildItem
Get-Alias ls             # ls = Get-ChildItem aussi
Get-Alias cd             # cd = Set-Location
Get-Alias cat            # cat = Get-Content
```


Les alias sont pratiques pour taper vite dans le terminal. Mais dans un script ou un document, utilise toujours les noms complets pour la lisibilité.

> **Note :** certains alias comme `man`, `ls`, `cat` peuvent exister pour faciliter la transition depuis Linux. Mais pour apprendre proprement, privilégie les commandes explicites (`Get-Help`, `Get-ChildItem`, `Get-Content`). Tu sauras toujours ce que tu fais, et ton code sera lisible par n’importe qui.

## Très utile en pratique

### La stratégie de recherche

Tu ne connais pas une commande ? Voici la démarche :

```
1. "Je veux faire quelque chose avec les services"
2. Get-Command *Service*          → trouve Get-Service, Stop-Service, etc.
3. Get-Help Get-Service -Examples → comprend comment l'utiliser
4. Get-Service | Get-Member       → découvre les propriétés disponibles
```


Cette démarche fonctionne pour **tout** dans PowerShell. C’est ce qui le rend découvrable.

### Chercher sur Internet

Quand l’aide intégrée ne suffit pas :

- **Microsoft Learn** : la documentation officielle (docs.microsoft.com)
- **Stack Overflow** : les questions/réponses de la communauté
- Formule de recherche efficace : `powershell [ce que tu veux faire]` ou `cmd [commande] [ce que tu veux faire]`

## ❌ Erreur classique

```powershell
# Utiliser Get-Help sans avoir mis à jour l'aide
Get-Help Get-Process    # → aide minimale si les fichiers d'aide n'ont jamais été téléchargés
Update-Help -ErrorAction SilentlyContinue    # ← Fait-le une fois

# Chercher une commande PowerShell en tapant le nom Linux
man                     # Peut fonctionner comme alias de Get-Help selon l'environnement
                        # → Préfère Get-Help, c'est la forme PowerShell explicite
grep                    # ❌ Utilise Select-String ou findstr
ifconfig                # ❌ Utilise ipconfig (CMD) ou Get-NetIPAddress (PowerShell)
```
