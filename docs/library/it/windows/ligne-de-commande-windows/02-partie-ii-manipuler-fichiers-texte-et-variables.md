---
title: Partie II — Manipuler fichiers, texte et variables
source: IT/02 Windows/Ligne de commande/Ligne de commande Windows.md
note: Ligne de commande Windows
up:
- - Ligne de commande Windows
  - index.md
---

-----


## Chapitre 4 — Gérer les fichiers et dossiers avec CMD

### Le minimum à savoir

#### Créer un dossier

```cmd
mkdir LabCMD
md LabCMD                    REM md est un raccourci de mkdir
mkdir "Mon Dossier"          REM Avec des espaces → guillemets
```


#### Créer un fichier texte

```cmd
echo Bonjour > fichier.txt          REM Crée le fichier avec "Bonjour"
echo Deuxieme ligne >> fichier.txt  REM Ajoute à la fin (>> = ajouter)
```


#### Lire un fichier

```cmd
type fichier.txt             REM Affiche le contenu du fichier
more fichier.txt             REM Affiche page par page (barre espace pour avancer)
```


#### Copier un fichier

```cmd
copy fichier.txt copie.txt                REM Copie simple
xcopy dossier sauvegarde /E              REM Copie un dossier et ses sous-dossiers
```


#### `robocopy` : l’outil de copie robuste

`robocopy` est l’outil professionnel de copie sous Windows — fiable, rapide, capable de reprendre après une interruption :

```cmd
robocopy source destination /E           REM Copie tout, y compris les sous-dossiers vides
robocopy source destination /MIR         REM Miroir : la destination devient identique à la source
```


> **Note :** `robocopy` est conçu pour les copies volumineuses, les sauvegardes et les migrations. Pour copier un seul fichier, `copy` suffit.

#### Déplacer, renommer, supprimer

```cmd
move fichier.txt C:\Temp\               REM Déplacer
ren ancien.txt nouveau.txt              REM Renommer (ren = rename)
del fichier.txt                          REM Supprimer un fichier
rmdir dossier                            REM Supprimer un dossier vide
rmdir /s dossier                         REM Supprimer un dossier et tout son contenu
```


> **⚠️ Attention :** `del` et `rmdir /s` ne passent **pas** par la corbeille. La suppression est définitive.

#### Afficher l’arborescence

```cmd
tree                         REM Arborescence des dossiers
tree /f                      REM Arborescence avec les fichiers
```


> **📋 FIL ROUGE — Épisode 3**
> 
> Léa retrouve les fichiers perdus de l’utilisateur dans `C:\Users\dupont\AppData\Local\Temp`. Elle les copie vers son Bureau avec `copy`, vérifie le contenu avec `type`, puis nettoie les temporaires.

### ❌ Erreur classique

```cmd
REM Confondre > (écrase) et >> (ajoute)
echo nouveau > rapport.txt     REM ❌ Tout l'ancien contenu est perdu !
echo nouveau >> rapport.txt    REM ✅ Ajoute à la fin

REM Supprimer sans vérifier
del *.*                        REM ❌ Supprime TOUT dans le dossier courant
REM → Toujours vérifier avec dir avant de supprimer
```



## Chapitre 5 — Gérer les fichiers et dossiers avec PowerShell

### Le minimum à savoir

#### Lister le contenu d’un dossier

```powershell
Get-ChildItem                        # Lister (alias : dir, ls)
Get-ChildItem -Force                 # Inclure les fichiers cachés
Get-ChildItem -Recurse               # Lister récursivement
Get-ChildItem -File                  # Fichiers uniquement (pas les dossiers)
Get-ChildItem -Directory             # Dossiers uniquement
```


#### Créer un fichier ou un dossier

```powershell
New-Item -ItemType Directory -Name "LabPS"
New-Item -ItemType File -Name "fichier.txt"
```


#### Écrire dans un fichier

```powershell
Set-Content fichier.txt "Bonjour"                # Écrase (comme >)
Add-Content fichier.txt "Nouvelle ligne"          # Ajoute à la fin (comme >>)
```


#### Lire un fichier

```powershell
Get-Content fichier.txt              # Lire tout le contenu (alias : cat)
Get-Content fichier.txt -First 10    # Les 10 premières lignes
Get-Content fichier.txt -Tail 5      # Les 5 dernières lignes (comme tail)
Get-Content fichier.txt -Tail 5 -Wait  # Suivre en temps réel (comme tail -f)
```


#### Copier, déplacer, renommer, supprimer

```powershell
Copy-Item fichier.txt copie.txt
Copy-Item dossier destination -Recurse        # Copier un dossier entier
Move-Item fichier.txt C:\Temp\
Rename-Item ancien.txt nouveau.txt
Remove-Item fichier.txt
Remove-Item dossier -Recurse                  # Supprimer un dossier et son contenu
```


#### Supprimer prudemment

PowerShell offre deux options de sécurité que CMD n’a pas :

```powershell
Remove-Item fichier.txt -WhatIf      # Simule : affiche ce qui SERAIT fait sans le faire
Remove-Item fichier.txt -Confirm     # Demande confirmation avant chaque suppression
```


> **Bonne pratique :** utilise `-WhatIf` pour vérifier avant de lancer une suppression en masse. C’est un filet de sécurité précieux.

### Très utile en pratique

#### Aperçu des permissions NTFS

Tu peux voir qui a le droit de lire ou modifier un fichier :

```cmd
REM CMD
icacls fichier.txt                   REM Affiche les permissions du fichier
icacls C:\Users\Lea\Documents        REM Permissions d'un dossier
```


```powershell
# PowerShell
Get-Acl fichier.txt                  # Affiche les permissions
(Get-Acl fichier.txt).Access         # Détaille les entrées d'accès
```


> **Note :** dans ce cours, on apprend à **lire** les permissions. La modification (`Set-Acl`, `icacls /grant`) est un sujet d’administration avancé.


## Chapitre 6 — Rechercher des fichiers et du contenu

### Le minimum à savoir

#### Rechercher un fichier avec CMD

```cmd
dir /s fichier.txt                   REM Cherche "fichier.txt" récursivement
dir /s /b *.log                      REM Cherche tous les .log (/b = chemin seul, sans détails)
```


#### Rechercher un exécutable

```cmd
where notepad                        REM Où se trouve notepad.exe ?
where powershell                     REM Où se trouve PowerShell ?
```


> **Pourquoi c’est utile :** quand une commande est “introuvable”, `where` te dit si elle existe et où.

#### Rechercher un fichier avec PowerShell

```powershell
Get-ChildItem -Path C:\Users -Filter "*.txt" -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\ -Filter "rapport.xlsx" -Recurse -ErrorAction SilentlyContinue
```


> **Note :** `-ErrorAction SilentlyContinue` évite les messages d’erreur pour les dossiers auxquels tu n’as pas accès.

#### Rechercher du texte dans des fichiers

**CMD — `findstr` :**

```cmd
findstr "erreur" fichier.txt             REM Cherche "erreur" dans un fichier
findstr /s "erreur" *.txt               REM Cherche dans tous les .txt récursivement
findstr /i "erreur" fichier.txt         REM Insensible à la casse
```


**PowerShell — `Select-String` :**

```powershell
Select-String -Path fichier.txt -Pattern "erreur"
Select-String -Path *.txt -Pattern "erreur"
Select-String -Path *.log -Pattern "error|warning"    # Recherche avec regex
```


> **Comparaison :** `findstr` (CMD) est l’équivalent de `grep` en Bash. `Select-String` (PowerShell) est plus puissant car il retourne des objets avec le numéro de ligne, le fichier, le contenu matché.

> **📋 FIL ROUGE — Épisode 4**
> 
> Léa doit trouver tous les fichiers de logs contenant le mot “critical” dans `C:\Logs`. Un `findstr /s "critical" C:\Logs\*.log` lui donne la liste en 2 secondes.


## Chapitre 7 — Variables d’environnement, PATH et repères système

### Le minimum à savoir

#### Qu’est-ce qu’une variable d’environnement ?

Une variable d’environnement stocke une information utilisée par Windows ou par les programmes. C’est comme une étiquette posée sur une information système.

#### Les variables les plus utiles

|Variable      |Contenu                |Exemple                          |
|--------------|-----------------------|---------------------------------|
|`USERNAME`    |Nom de l’utilisateur   |`Lea`                            |
|`USERPROFILE` |Chemin du profil       |`C:\Users\Lea`                   |
|`COMPUTERNAME`|Nom de la machine      |`PC-SUPPORT-02`                  |
|`TEMP` / `TMP`|Dossier temporaire     |`C:\Users\Lea\AppData\Local\Temp`|
|`SYSTEMROOT`  |Dossier Windows        |`C:\Windows`                     |
|`PATH`        |Chemins des exécutables|(voir ci-dessous)                |

#### Afficher les variables avec CMD

```cmd
set                          REM Toutes les variables d'environnement
echo %USERNAME%              REM Le nom de l'utilisateur
echo %USERPROFILE%           REM Le chemin du profil
echo %TEMP%                  REM Le dossier temporaire
echo %PATH%                  REM Le PATH
```


#### Afficher les variables avec PowerShell

```powershell
Get-ChildItem Env:           # Toutes les variables d'environnement
$env:USERNAME                # Le nom de l'utilisateur
$env:USERPROFILE             # Le chemin du profil
$env:TEMP                    # Le dossier temporaire
$env:PATH                    # Le PATH
```


#### Comprendre le PATH

Le **PATH** est la variable la plus importante. Elle contient la liste des dossiers où Windows cherche les programmes quand tu tapes une commande.

Quand tu tapes `notepad`, Windows ne cherche pas dans tout le disque. Il cherche `notepad.exe` uniquement dans les dossiers listés dans le PATH.

```cmd
where notepad                REM Montre où Windows trouve notepad.exe
```


```powershell
Get-Command notepad          # Même chose en PowerShell
```


Si une commande est “introuvable”, c’est probablement parce que le dossier qui la contient n’est pas dans le PATH.

### Très utile en pratique

#### Modifier une variable d’environnement

```cmd
REM Temporaire (disparaît quand tu fermes le terminal)
set MON_VAR=valeur

REM Persistant (modifie le registre — utiliser avec prudence)
setx MON_VAR "valeur"
```


> **⚠️ Attention :** `setx` modifie la variable de manière **permanente** dans le profil utilisateur. Utilise avec prudence, surtout pour le PATH.


## Chapitre 8 — Redirections, pipes et sorties de commandes

### Le minimum à savoir

#### Les redirections dans CMD

```cmd
ipconfig > ip.txt                    REM Sortie dans un fichier (écrase)
ipconfig >> ip.txt                   REM Sortie dans un fichier (ajoute)
commande 2> erreurs.txt              REM Erreurs dans un fichier séparé
commande > resultat.txt 2>&1         REM Tout (sortie + erreurs) dans un fichier
commande > NUL                       REM Ignorer la sortie (le "trou noir")
```


> **Rappel :** `>` écrase, `>>` ajoute. Confondre les deux = perdre des données.

#### Les redirections dans PowerShell

```powershell
Get-Process > process.txt                    # Redirige vers un fichier
Get-Process | Out-File process.txt           # Équivalent avec un cmdlet
Get-Process | Out-File process.txt -Append   # Ajoute au lieu d'écraser
```


#### Le pipe : enchaîner des commandes

Le **pipe** (`|`) envoie la sortie d’une commande comme entrée de la suivante.

**En CMD :**

```cmd
tasklist | findstr chrome            REM Liste les processus, filtre ceux qui contiennent "chrome"
dir | find ".log"                    REM Liste les fichiers, filtre ceux avec ".log"
```


**En PowerShell :**

```powershell
Get-Process | Where-Object { $_.Name -like "*chrome*" }
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU -First 5
```


> **La grande différence (aperçu) :** en CMD, le pipe transporte du **texte** — tu filtres des lignes avec `findstr`. En PowerShell, le pipe transporte des **objets** — tu accèdes directement aux propriétés (`Name`, `CPU`, `Status`). C’est beaucoup plus fiable. On verra ça en détail au chapitre 9.

#### Exporter les résultats

PowerShell peut exporter dans plusieurs formats natifs :

```powershell
Get-Process | Export-Csv process.csv -NoTypeInformation                          # En CSV
Get-Process | Select-Object Name, Id, CPU | ConvertTo-Json | Out-File process.json   # En JSON (sélection des propriétés utiles)
Get-Process | Out-File process.txt                                                # En texte brut
```


> **Astuce :** pour `ConvertTo-Json`, sélectionne d’abord les propriétés qui t’intéressent avec `Select-Object`. Sinon, l’export contient des dizaines de propriétés par objet et le fichier devient illisible.

> **📋 FIL ROUGE — Épisode 5**
> 
> Léa doit documenter l’état du système. Elle redirige la sortie de `systeminfo`, `ipconfig /all`, `tasklist` et `netstat -ano` dans des fichiers séparés dans un dossier de collecte. Son N+1 pourra analyser les résultats sans avoir accès à la machine.

### ❌ Erreur classique

```cmd
REM Confondre > et >>
echo "lundi" > journal.txt          REM Crée/écrase
echo "mardi" > journal.txt          REM ❌ Écrase "lundi" !
echo "mardi" >> journal.txt         REM ✅ Ajoute après "lundi"

REM Croire que le pipe CMD et le pipe PowerShell fonctionnent pareil
tasklist | findstr chrome            REM CMD : filtre du TEXTE
Get-Process | Where-Object Name -eq "chrome"   REM PowerShell : filtre des OBJETS
```


-----
