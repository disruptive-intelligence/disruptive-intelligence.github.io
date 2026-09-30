---
title: Chapitre 2 — Naviguer dans le système de fichiers
source: IT/02_Windows/Windows_Command-Line.md
note: Windows Command Line
up:
- - Windows Command Line
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## Le minimum à savoir

### L’arborescence Windows

Windows organise ses fichiers en **arbre**, à partir d’un lecteur (généralement `C:\`) :

```
C:\
├── Users\
│   ├── Lea\
│   │   ├── Desktop\
│   │   ├── Documents\
│   │   └── Downloads\
│   └── Public\
├── Windows\              ← Le système d'exploitation
│   └── System32\         ← Les outils système (cmd.exe, notepad.exe...)
├── Program Files\        ← Les programmes installés (64 bits)
├── Program Files (x86)\  ← Les programmes installés (32 bits)
└── Temp\                 ← Les fichiers temporaires
```


### Chemin absolu et chemin relatif

Un **chemin absolu** part de la racine du lecteur :

```
C:\Users\Lea\Documents\rapport.txt
```


Un **chemin relatif** part du dossier où tu te trouves :

```
Documents\rapport.txt     (si tu es dans C:\Users\Lea)
```


### Les chemins avec des espaces

Si un dossier ou fichier contient un espace dans son nom, il faut l’entourer de guillemets :

```cmd
cd "C:\Program Files"       REM ✅ Correct
cd C:\Program Files          REM ❌ CMD croit que "Files" est un argument séparé
```


### Naviguer avec CMD

```cmd
cd                           REM Affiche le dossier actuel
cd Desktop                   REM Aller dans le sous-dossier Desktop
cd ..                        REM Remonter d'un niveau (dossier parent)
cd \                         REM Aller à la racine du lecteur
cd %USERPROFILE%             REM Aller dans le profil utilisateur (C:\Users\Lea)

dir                          REM Lister le contenu du dossier actuel
dir /a                       REM Inclure les fichiers cachés et système
dir /s                       REM Lister récursivement (sous-dossiers inclus)

tree                         REM Afficher l'arborescence visuellement

D:                           REM Changer de lecteur (pas de cd nécessaire)
```


### Naviguer avec PowerShell

```powershell
Get-Location                 # Affiche le dossier actuel (alias : pwd)
Set-Location Desktop         # Aller dans Desktop (alias : cd)
Set-Location ..              # Remonter d'un niveau
Set-Location \               # Aller à la racine
Set-Location ~               # Aller dans le profil utilisateur

Get-ChildItem                # Lister le contenu (alias : dir, ls)
Get-ChildItem -Force         # Inclure les fichiers cachés
Get-ChildItem -Recurse       # Lister récursivement
```


### Les raccourcis de navigation

|Raccourci|Signification                                |
|---------|---------------------------------------------|
|`.`      |Le dossier courant                           |
|`..`     |Le dossier parent                            |
|`\`      |La racine du lecteur                         |
|`~`      |Le profil utilisateur (PowerShell uniquement)|

### L’auto-complétion avec Tab

Tape le début d’un nom et appuie sur `Tab` — le terminal complète automatiquement :

```cmd
cd Docu[Tab]     → cd Documents
cd "C:\Prog[Tab] → cd "C:\Program Files"
```


C’est un gain de temps énorme et ça évite les fautes de frappe.

> **📋 FIL ROUGE — Épisode 2**
> 
> L’utilisateur dit “j’ai perdu un fichier, il était dans Documents ou peut-être le Bureau”. Léa navigue dans son profil avec `cd`, liste les fichiers avec `dir /s *.xlsx` pour chercher tous les fichiers Excel récursivement, et retrouve le fichier dans un sous-dossier.

## Très utile en pratique

### L’historique des commandes

Tu n’as pas besoin de retaper les commandes — utilise les flèches :

```cmd
REM CMD
doskey /history              REM Affiche l'historique complet
```


```powershell
# PowerShell
Get-History                  # Affiche l'historique
```


### Les dossiers importants de Windows

|Chemin               |Contenu                                                      |
|---------------------|-------------------------------------------------------------|
|`C:\Users\[Nom]`     |Profil de l’utilisateur (Bureau, Documents, Téléchargements…)|
|`C:\Windows`         |Le système d’exploitation                                    |
|`C:\Windows\System32`|Les outils système (cmd.exe, notepad.exe, drivers…)          |
|`C:\Program Files`   |Les programmes installés (64 bits)                           |
|`C:\Temp` ou `%TEMP%`|Les fichiers temporaires                                     |
|`C:\Windows\Logs`    |Certains logs du système                                     |

## ❌ Erreur classique

```cmd
REM Oublier les guillemets sur un chemin avec espaces
cd C:\Program Files          REM ❌ "Files" est interprété comme un argument
cd "C:\Program Files"        REM ✅ Correct

REM Confondre \ (racine) et .. (parent)
cd \                         REM Va à C:\ (la racine)
cd ..                        REM Remonte d'un niveau

REM Oublier de changer de lecteur avant de naviguer
cd D:\Donnees                REM ❌ CMD ne change pas de lecteur avec cd seul
D:                           REM ✅ D'abord changer de lecteur
cd Donnees                   REM ✅ Puis naviguer

REM Astuce : cd /d fait les deux d'un coup
cd /d D:\Donnees             REM ✅ Change de lecteur ET de dossier en une commande
```
