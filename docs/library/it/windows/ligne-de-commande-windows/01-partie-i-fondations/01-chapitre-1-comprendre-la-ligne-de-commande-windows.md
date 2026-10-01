---
title: Chapitre 1 — Comprendre la ligne de commande Windows
source: IT/02 Windows/Ligne de commande Windows.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### Interface graphique vs ligne de commande

Tu utilises Windows tous les jours en cliquant sur des icônes, des menus, des fenêtres. C’est l’**interface graphique** (GUI — Graphical User Interface). C’est intuitif, visuel, confortable.

La **ligne de commande** (CLI — Command Line Interface), c’est l’autre façon de parler à Windows : tu tapes des commandes en texte, et Windows exécute.

Pourquoi utiliser la ligne de commande alors que le GUI existe ?

- **Aller plus vite :** certaines opérations prennent 3 secondes en CLI et 2 minutes en cliquant dans des menus
- **Diagnostiquer un problème :** quand le réseau ne marche pas, un `ipconfig` donne la réponse en 1 seconde
- **Administrer à distance :** pas d’interface graphique sur un serveur distant ? La CLI est la seule option
- **Automatiser :** renommer 500 fichiers, vérifier l’état de 50 machines → un script le fait en 10 secondes
- **Collecter des informations :** en cybersécurité, la CLI est l’outil principal pour le triage et l’investigation
- **Travailler sur Server Core :** certains serveurs Windows n’ont pas d’interface graphique du tout

### Les deux outils : CMD et PowerShell

Windows a **deux** lignes de commande :

|Outil         |Nom complet                               |Depuis               |Nature                           |
|--------------|------------------------------------------|---------------------|---------------------------------|
|**CMD**       |Command Prompt (`cmd.exe`)                |DOS / Windows 95     |Ancien, simple, orienté texte    |
|**PowerShell**|PowerShell (`powershell.exe` / `pwsh.exe`)|2006 (v1) / 2016 (v7)|Moderne, puissant, orienté objets|

CMD est l’héritage de l’ère DOS. Il est simple, rapide pour les tâches basiques, et encore très utilisé pour le dépannage réseau. PowerShell est son successeur moderne — beaucoup plus puissant, avec une logique différente (les objets au lieu du texte brut).

**On n’a pas besoin de choisir l’un ou l’autre.** Dans la vraie vie, on utilise les deux selon le contexte. Ce cours t’apprend les deux.

### Ouvrir un terminal

**Méthode 1 — Menu Démarrer :**

- Tape “cmd” → **Invite de commandes**
- Tape “powershell” → **Windows PowerShell**
- Tape “terminal” → **Windows Terminal** (regroupe les deux — recommandé)

**Méthode 2 — Win + R :**

- `Win + R` → tape `cmd` → Entrée
- `Win + R` → tape `powershell` → Entrée

**Méthode 3 — Depuis l’Explorateur de fichiers :**

- Dans la barre d’adresse de l’Explorateur, tape `cmd` → ouvre CMD dans le dossier actuel

### Exécuter en tant qu’administrateur

Certaines commandes nécessitent des **droits administrateur** (gérer les services, lire les logs de sécurité, modifier la configuration réseau). Pour ça :

- Menu Démarrer → tape “cmd” ou “powershell” → clic droit → **Exécuter en tant qu’administrateur**
- Ou dans Windows Terminal : clic droit sur l’onglet → **Ouvrir en tant qu’administrateur**

> **Comment savoir si tu es admin ?** Le titre de la fenêtre indique souvent “Administrateur”. Pour être sûr, certaines commandes système renverront “Accès refusé” si le terminal n’est pas élevé. Une astuce simple : lance `net session`. Si la commande renvoie “Accès refusé”, ton terminal n’est généralement pas lancé en administrateur.

### Comprendre le prompt

Le **prompt**, c’est le texte que le terminal affiche en attendant ta commande.

**CMD :**

```
C:\Users\Lea>
```


Ça te dit : “tu es dans le dossier `C:\Users\Lea`, et j’attends ta commande.”

**PowerShell :**

```
PS C:\Users\Lea>
```


Le `PS` au début indique que c’est PowerShell.

### Les toutes premières commandes

Tape ces commandes pour te familiariser :

**En CMD :**

```cmd
whoami          REM Qui suis-je ? (nom d'utilisateur)
hostname        REM Comment s'appelle cette machine ?
ver             REM Quelle version de Windows ?
date /t         REM Quelle date ?
time /t         REM Quelle heure ?
cls             REM Effacer l'écran
```


**En PowerShell :**

```powershell
whoami                  # Qui suis-je ?
hostname                # Nom de la machine
Get-Date                # Date et heure
$env:USERNAME           # Nom de l'utilisateur (via variable d'environnement)
$env:COMPUTERNAME       # Nom de la machine (via variable d'environnement)
Clear-Host              # Effacer l'écran
```


> **Note :** `whoami` et `hostname` fonctionnent dans les deux. Beaucoup de commandes CMD classiques fonctionnent aussi dans PowerShell (ce sont des alias ou des exécutables Windows).

> **📋 FIL ROUGE — Épisode 1**
> 
> Léa arrive au bureau. Premier problème signalé : un serveur de fichiers ne répond plus. Pas d’interface graphique — c’est un Windows Server Core. Elle ouvre une session distante et tombe sur un prompt `C:\Windows\System32>`. Tout va se passer en ligne de commande.

## Très utile en pratique

### Windows Terminal : l’outil moderne

**Windows Terminal** est l’application qui regroupe CMD, PowerShell et WSL (Linux) dans une seule fenêtre avec des onglets. C’est l’outil recommandé :

- Onglets (comme un navigateur web)
- Coloration syntaxique
- Copier/coller avec Ctrl+C / Ctrl+V
- Split de fenêtre (CMD à gauche, PowerShell à droite)
- Personnalisable (thèmes, transparence, police)

Si tu ne l’as pas : cherche “Windows Terminal” dans le Microsoft Store (gratuit).

### Les raccourcis clavier du terminal

|Raccourci          |Effet                                                |
|-------------------|-----------------------------------------------------|
|`Flèche haut / bas`|Rappeler la commande précédente / suivante           |
|`Tab`              |Auto-compléter un nom de fichier, dossier ou commande|
|`Ctrl + C`         |Annuler la commande en cours                         |
|`Ctrl + V`         |Coller du texte (Windows Terminal)                   |
|`F7`               |Afficher l’historique des commandes (CMD)            |

## ❌ Erreur classique

```
# Confondre CMD et PowerShell
# Les commandes PowerShell (Get-Process, Get-Service) ne fonctionnent PAS dans CMD
# Les options CMD (/s, /a) ne fonctionnent PAS dans PowerShell

# Oublier d'ouvrir en administrateur
# → "Accès refusé" sur les commandes système

# Croire que la ligne de commande est dangereuse
# → La ligne de commande ne fait rien que tu ne lui demandes. Si tu ne tapes rien,
#   il ne se passe rien. Tu peux explorer sans risque.
```
