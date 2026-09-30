---
title: Windows Command Line
source: IT/02_Windows/Windows_Command-Line.md
---

### CMD et PowerShell pour naviguer, diagnostiquer et administrer Windows

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu’un qui n’a jamais ouvert un terminal de sa vie.
> Tout ce dont tu as besoin, c’est un ordinateur sous Windows 10 ou 11.

-----

### Ce que ce cours est — et ce qu’il n’est pas

Ce cours t’apprend à **utiliser** la ligne de commande Windows au quotidien :

- naviguer dans le système de fichiers
- manipuler des fichiers et dossiers
- récupérer des informations système
- diagnostiquer le réseau
- comprendre les processus, services, utilisateurs et groupes
- consulter les journaux Windows
- découvrir le registre et les tâches planifiées
- faire une première collecte d’informations utile en administration ou cybersécurité

Ce cours **n’est pas** un cours de programmation PowerShell. Les variables, boucles, fonctions, scripts avancés, `param()`, pipeline d’objets en profondeur — tout ça est couvert dans le **cours PowerShell** de la bibliothèque, qui prend le relais une fois que tu es à l’aise avec la ligne de commande.

**L’analogie :** c’est la différence entre “apprendre à utiliser le terminal Linux” et “apprendre à écrire des scripts Bash”. Les deux se complètent, mais l’angle n’est pas le même.

-----

### Guide de lecture

|Section                   |Niveau           |Objectif                                          |
|--------------------------|-----------------|--------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel      |Ce qu’il faut retenir pour ne pas être perdu      |
|**Très utile en pratique**|🟡 Bon à connaître|Ce qui te rend opérationnel au quotidien          |
|**Bonus**                 |🔴 Avancé         |Pour aller plus loin — tu peux y revenir plus tard|

#### Parcours recommandés

|Parcours                    |Chapitres                |Objectif                                                        |
|----------------------------|-------------------------|----------------------------------------------------------------|
|**🎯 Découverte / entretien**|Ch.1-8, 10-11, 17, 25    |Comprendre la CLI Windows, être crédible en entretien           |
|**🔧 Administration**        |Tous sauf Ch.23-24       |Être autonome pour diagnostiquer et administrer un poste Windows|
|**🛡️ Cyber / blue team**     |Tout, focus Ch.16, 21, 24|Triage, collecte d’informations, investigation de base          |

-----

### Glossaire — Les mots à connaître

| Terme                        | Définition simple                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| **Terminal**                 | La fenêtre où tu tapes des commandes texte                                               |
| **Shell**                    | Le programme qui lit et exécute tes commandes (CMD et PowerShell sont des shells)        |
| **Commande**                 | Une instruction que le shell sait exécuter (`dir`, `ping`, `Get-Process`…)               |
| **Argument**                 | Une info que tu donnes à une commande (`ping 8.8.8.8` — `8.8.8.8` est l’argument)        |
| **Option / Flag**            | Un modificateur qui change le comportement d’une commande (`dir /s` — `/s` est l’option) |
| **Prompt**                   | Le texte affiché par le terminal qui attend ta commande (`C:\Users\Lea>`)                |
| **Chemin (path)**            | L’adresse d’un fichier ou dossier dans le système (`C:\Users\Lea\Documents`)             |
| **Variable d’environnement** | Une information système stockée sous un nom (`%USERNAME%`, `$env:COMPUTERNAME`)          |
| **Processus**                | Un programme en cours d’exécution                                                        |
| **Service**                  | Un programme qui tourne en arrière-plan, souvent sans fenêtre visible                    |
| **Registre**                 | La base de données de configuration de Windows                                           |
| **Tâche planifiée**          | Une action programmée pour s’exécuter automatiquement (au démarrage, à une heure…)       |
| **Journal d’événements**     | Les logs de Windows — ce qui s’est passé sur la machine                                  |
| **Event ID**                 | Un numéro qui identifie un type d’événement dans les journaux Windows                    |
| **PID**                      | Process ID — le numéro unique d’un processus en cours d’exécution                        |
| **Port**                     | Un numéro qui identifie un service réseau sur une machine (80 = web, 443 = HTTPS…)       |
| **DNS**                      | Le système qui traduit les noms de domaine en adresses IP (`google.com` → `142.250.x.x`) |
| **Cmdlet**                   | Une commande PowerShell native, nommée `Verbe-Nom` (`Get-Process`, `Set-Location`)       |
| **Pipeline**                 | Le mécanisme qui envoie la sortie d’une commande vers une autre, avec le caractère `     |
| **Redirection**              | Envoyer la sortie d’une commande dans un fichier au lieu de l’écran (`>`, `>>`)          |
| **Batch (.bat)**             | Un fichier contenant des commandes CMD exécutées dans l’ordre                            |
| **Remoting**                 | La capacité d’exécuter des commandes sur une machine distante                            |

-----

### Fil rouge : Léa, technicienne support

> **Contexte narratif**
> 
> **Léa**, 26 ans, technicienne support niveau 2 dans une PME de 200 postes Windows. Un lundi matin, plusieurs problèmes remontent en même temps : un poste ne se connecte plus au réseau, un utilisateur ne retrouve plus certains fichiers, un processus consomme trop de ressources, un service semble arrêté, le responsable demande des informations système, et un comportement suspect doit être vérifié rapidement.
> 
> Léa va utiliser CMD et PowerShell pour diagnostiquer et résoudre chaque problème, chapitre après chapitre.

-----

### Table des matières

**PARTIE I — FONDATIONS (Ch.1-3)**

1. [Comprendre la ligne de commande Windows](#chapitre-1-comprendre-la-ligne-de-commande-windows)
1. [Naviguer dans le système de fichiers](#chapitre-2-naviguer-dans-le-systeme-de-fichiers)
1. [Obtenir de l’aide et devenir autonome](#chapitre-3-obtenir-de-laide-et-devenir-autonome)

**PARTIE II — MANIPULER FICHIERS, TEXTE ET VARIABLES (Ch.4-8)**

1. [Gérer les fichiers et dossiers avec CMD](#chapitre-4-gerer-les-fichiers-et-dossiers-avec-cmd)
1. [Gérer les fichiers et dossiers avec PowerShell](#chapitre-5-gerer-les-fichiers-et-dossiers-avec-powershell)
1. [Rechercher des fichiers et du contenu](#chapitre-6-rechercher-des-fichiers-et-du-contenu)
1. [Variables d’environnement, PATH et repères système](#chapitre-7-variables-denvironnement-path-et-reperes-systeme)
1. [Redirections, pipes et sorties de commandes](#chapitre-8-redirections-pipes-et-sorties-de-commandes)

**PARTIE III — ADMINISTRER ET DIAGNOSTIQUER (Ch.9-18)**

1. [CMD vs PowerShell : comprendre la différence](#chapitre-9-cmd-vs-powershell-comprendre-la-difference)
1. [Informations système et diagnostic de base](#chapitre-10-informations-systeme-et-diagnostic-de-base)
1. [Processus](#chapitre-11-processus)
1. [Services Windows](#chapitre-12-services-windows)
1. [Utilisateurs et groupes locaux](#chapitre-13-utilisateurs-et-groupes-locaux)
1. [Tâches planifiées](#chapitre-14-taches-planifiees)
1. [Le registre Windows](#chapitre-15-le-registre-windows)
1. [Journaux Windows (Event Logs)](#chapitre-16-journaux-windows-event-logs)
1. [Réseau avec CMD et PowerShell](#chapitre-17-reseau-avec-cmd-et-powershell)
1. [Interagir avec le Web depuis la CLI](#chapitre-18-interagir-avec-le-web-depuis-la-cli)

**PARTIE IV — AUTOMATISATION ET TRIAGE (Ch.19-22)**

1. [Introduction aux scripts batch (.bat)](#chapitre-19-introduction-aux-scripts-batch-bat)
1. [Introduction à l’automatisation PowerShell](#chapitre-20-introduction-a-lautomatisation-powershell)
1. [Sécurité et triage depuis la ligne de commande](#chapitre-21-securite-et-triage-depuis-la-ligne-de-commande)
1. [PowerShell Remoting : aperçu](#chapitre-22-powershell-remoting-apercu)

**PARTIE V — LABS, ÉVALUATION ET SYNTHÈSE (Ch.23-25)**

1. [Labs progressifs](#chapitre-23-labs-progressifs)
1. [Skills Assessment — Évaluation finale](#chapitre-24-skills-assessment-evaluation-finale)
1. [Synthèse et boîte à outils du praticien](#chapitre-25-synthese-et-boite-a-outils-du-praticien)

**ANNEXES**

-----

## PARTIE I — FONDATIONS

-----

## Chapitre 1 — Comprendre la ligne de commande Windows

### Le minimum à savoir

#### Interface graphique vs ligne de commande

Tu utilises Windows tous les jours en cliquant sur des icônes, des menus, des fenêtres. C’est l’**interface graphique** (GUI — Graphical User Interface). C’est intuitif, visuel, confortable.

La **ligne de commande** (CLI — Command Line Interface), c’est l’autre façon de parler à Windows : tu tapes des commandes en texte, et Windows exécute.

Pourquoi utiliser la ligne de commande alors que le GUI existe ?

- **Aller plus vite :** certaines opérations prennent 3 secondes en CLI et 2 minutes en cliquant dans des menus
- **Diagnostiquer un problème :** quand le réseau ne marche pas, un `ipconfig` donne la réponse en 1 seconde
- **Administrer à distance :** pas d’interface graphique sur un serveur distant ? La CLI est la seule option
- **Automatiser :** renommer 500 fichiers, vérifier l’état de 50 machines → un script le fait en 10 secondes
- **Collecter des informations :** en cybersécurité, la CLI est l’outil principal pour le triage et l’investigation
- **Travailler sur Server Core :** certains serveurs Windows n’ont pas d’interface graphique du tout

#### Les deux outils : CMD et PowerShell

Windows a **deux** lignes de commande :

|Outil         |Nom complet                               |Depuis               |Nature                           |
|--------------|------------------------------------------|---------------------|---------------------------------|
|**CMD**       |Command Prompt (`cmd.exe`)                |DOS / Windows 95     |Ancien, simple, orienté texte    |
|**PowerShell**|PowerShell (`powershell.exe` / `pwsh.exe`)|2006 (v1) / 2016 (v7)|Moderne, puissant, orienté objets|

CMD est l’héritage de l’ère DOS. Il est simple, rapide pour les tâches basiques, et encore très utilisé pour le dépannage réseau. PowerShell est son successeur moderne — beaucoup plus puissant, avec une logique différente (les objets au lieu du texte brut).

**On n’a pas besoin de choisir l’un ou l’autre.** Dans la vraie vie, on utilise les deux selon le contexte. Ce cours t’apprend les deux.

#### Ouvrir un terminal

**Méthode 1 — Menu Démarrer :**

- Tape “cmd” → **Invite de commandes**
- Tape “powershell” → **Windows PowerShell**
- Tape “terminal” → **Windows Terminal** (regroupe les deux — recommandé)

**Méthode 2 — Win + R :**

- `Win + R` → tape `cmd` → Entrée
- `Win + R` → tape `powershell` → Entrée

**Méthode 3 — Depuis l’Explorateur de fichiers :**

- Dans la barre d’adresse de l’Explorateur, tape `cmd` → ouvre CMD dans le dossier actuel

#### Exécuter en tant qu’administrateur

Certaines commandes nécessitent des **droits administrateur** (gérer les services, lire les logs de sécurité, modifier la configuration réseau). Pour ça :

- Menu Démarrer → tape “cmd” ou “powershell” → clic droit → **Exécuter en tant qu’administrateur**
- Ou dans Windows Terminal : clic droit sur l’onglet → **Ouvrir en tant qu’administrateur**

> **Comment savoir si tu es admin ?** Le titre de la fenêtre indique souvent “Administrateur”. Pour être sûr, certaines commandes système renverront “Accès refusé” si le terminal n’est pas élevé. Une astuce simple : lance `net session`. Si la commande renvoie “Accès refusé”, ton terminal n’est généralement pas lancé en administrateur.

#### Comprendre le prompt

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

#### Les toutes premières commandes

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

### Très utile en pratique

#### Windows Terminal : l’outil moderne

**Windows Terminal** est l’application qui regroupe CMD, PowerShell et WSL (Linux) dans une seule fenêtre avec des onglets. C’est l’outil recommandé :

- Onglets (comme un navigateur web)
- Coloration syntaxique
- Copier/coller avec Ctrl+C / Ctrl+V
- Split de fenêtre (CMD à gauche, PowerShell à droite)
- Personnalisable (thèmes, transparence, police)

Si tu ne l’as pas : cherche “Windows Terminal” dans le Microsoft Store (gratuit).

#### Les raccourcis clavier du terminal

|Raccourci          |Effet                                                |
|-------------------|-----------------------------------------------------|
|`Flèche haut / bas`|Rappeler la commande précédente / suivante           |
|`Tab`              |Auto-compléter un nom de fichier, dossier ou commande|
|`Ctrl + C`         |Annuler la commande en cours                         |
|`Ctrl + V`         |Coller du texte (Windows Terminal)                   |
|`F7`               |Afficher l’historique des commandes (CMD)            |

### ❌ Erreur classique

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

## Chapitre 2 — Naviguer dans le système de fichiers

### Le minimum à savoir

#### L’arborescence Windows

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

#### Chemin absolu et chemin relatif

Un **chemin absolu** part de la racine du lecteur :

```
C:\Users\Lea\Documents\rapport.txt
```

Un **chemin relatif** part du dossier où tu te trouves :

```
Documents\rapport.txt     (si tu es dans C:\Users\Lea)
```

#### Les chemins avec des espaces

Si un dossier ou fichier contient un espace dans son nom, il faut l’entourer de guillemets :

```cmd
cd "C:\Program Files"       REM ✅ Correct
cd C:\Program Files          REM ❌ CMD croit que "Files" est un argument séparé
```

#### Naviguer avec CMD

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

#### Naviguer avec PowerShell

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

#### Les raccourcis de navigation

|Raccourci|Signification                                |
|---------|---------------------------------------------|
|`.`      |Le dossier courant                           |
|`..`     |Le dossier parent                            |
|`\`      |La racine du lecteur                         |
|`~`      |Le profil utilisateur (PowerShell uniquement)|

#### L’auto-complétion avec Tab

Tape le début d’un nom et appuie sur `Tab` — le terminal complète automatiquement :

```cmd
cd Docu[Tab]     → cd Documents
cd "C:\Prog[Tab] → cd "C:\Program Files"
```

C’est un gain de temps énorme et ça évite les fautes de frappe.

> **📋 FIL ROUGE — Épisode 2**
> 
> L’utilisateur dit “j’ai perdu un fichier, il était dans Documents ou peut-être le Bureau”. Léa navigue dans son profil avec `cd`, liste les fichiers avec `dir /s *.xlsx` pour chercher tous les fichiers Excel récursivement, et retrouve le fichier dans un sous-dossier.

### Très utile en pratique

#### L’historique des commandes

Tu n’as pas besoin de retaper les commandes — utilise les flèches :

```cmd
REM CMD
doskey /history              REM Affiche l'historique complet
```

```powershell
# PowerShell
Get-History                  # Affiche l'historique
```

#### Les dossiers importants de Windows

|Chemin               |Contenu                                                      |
|---------------------|-------------------------------------------------------------|
|`C:\Users\[Nom]`     |Profil de l’utilisateur (Bureau, Documents, Téléchargements…)|
|`C:\Windows`         |Le système d’exploitation                                    |
|`C:\Windows\System32`|Les outils système (cmd.exe, notepad.exe, drivers…)          |
|`C:\Program Files`   |Les programmes installés (64 bits)                           |
|`C:\Temp` ou `%TEMP%`|Les fichiers temporaires                                     |
|`C:\Windows\Logs`    |Certains logs du système                                     |

### ❌ Erreur classique

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

## Chapitre 3 — Obtenir de l’aide et devenir autonome

### Le minimum à savoir

Ce chapitre est **fondamental**. Si tu sais obtenir de l’aide tout seul, tu n’as plus besoin de mémoriser des centaines de commandes — tu les retrouves quand tu en as besoin.

#### L’aide dans CMD

Chaque commande CMD a une aide intégrée, accessible avec `/?` :

```cmd
dir /?              REM Affiche l'aide de la commande dir
ipconfig /?         REM Affiche l'aide de ipconfig
xcopy /?            REM Affiche l'aide de xcopy

help                REM Liste les commandes CMD de base
help dir            REM Aide détaillée sur dir (même chose que dir /?)
```

#### L’aide dans PowerShell : le trio de survie

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

#### Comprendre les alias PowerShell

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

### Très utile en pratique

#### La stratégie de recherche

Tu ne connais pas une commande ? Voici la démarche :

```
1. "Je veux faire quelque chose avec les services"
2. Get-Command *Service*          → trouve Get-Service, Stop-Service, etc.
3. Get-Help Get-Service -Examples → comprend comment l'utiliser
4. Get-Service | Get-Member       → découvre les propriétés disponibles
```

Cette démarche fonctionne pour **tout** dans PowerShell. C’est ce qui le rend découvrable.

#### Chercher sur Internet

Quand l’aide intégrée ne suffit pas :

- **Microsoft Learn** : la documentation officielle (docs.microsoft.com)
- **Stack Overflow** : les questions/réponses de la communauté
- Formule de recherche efficace : `powershell [ce que tu veux faire]` ou `cmd [commande] [ce que tu veux faire]`

### ❌ Erreur classique

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

## PARTIE II — MANIPULER FICHIERS, TEXTE ET VARIABLES

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

## PARTIE III — ADMINISTRER ET DIAGNOSTIQUER

-----

## Chapitre 9 — CMD vs PowerShell : comprendre la différence

### Le minimum à savoir

#### CMD : historique, simple, orienté texte

CMD traite tout comme du **texte brut**. Quand tu fais `tasklist`, le résultat est un bloc de texte formaté. Pour en extraire une information, tu dois chercher des mots dans ce texte avec `findstr` — comme chercher un mot dans un livre.

```cmd
tasklist | findstr chrome
```

#### PowerShell : moderne, orienté objets

PowerShell traite tout comme des **objets structurés**. Quand tu fais `Get-Process`, chaque processus est un objet avec des propriétés nommées (`Name`, `Id`, `CPU`, `WorkingSet64`…). Tu accèdes directement aux propriétés — pas besoin de parser du texte.

```powershell
Get-Process chrome
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5
```

#### La comparaison concrète

**La même tâche : trouver les 5 processus les plus gourmands en CPU.**

CMD :

```cmd
REM Pas de commande simple pour trier par CPU en CMD
REM Il faudrait exporter, parser avec des outils externes...
tasklist /v
```

PowerShell :

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5
```

#### Quand utiliser CMD ?

- Commandes réseau classiques (`ipconfig`, `ping`, `tracert`, `netstat`)
- Dépannage rapide sur n’importe quel Windows
- Scripts batch (.bat) existants
- Compatibilité avec des environnements anciens
- Quand tu veux une réponse rapide sans charger PowerShell

#### Quand utiliser PowerShell ?

- Administration moderne (processus, services, utilisateurs, registre)
- Filtrage et tri avancés (`Where-Object`, `Sort-Object`, `Select-Object`)
- Export structuré (CSV, JSON)
- Automatisation et scripting
- Collecte d’informations système
- Tout ce qui nécessite de traiter des données de manière structurée

#### La règle simple

> **En pratique :** utilise CMD pour les commandes réseau classiques et les tâches ponctuelles rapides. Utilise PowerShell pour tout ce qui nécessite de filtrer, trier, exporter ou automatiser.


-----

## Chapitre 10 — Informations système et diagnostic de base

### Le minimum à savoir

#### Identifier la machine

```cmd
REM CMD
whoami                       REM Utilisateur actuel (DOMAINE\utilisateur)
hostname                     REM Nom de la machine
ver                          REM Version de Windows (courte)
systeminfo                   REM Informations détaillées (OS, RAM, patchs, boot time...)
```

```powershell
# PowerShell
whoami
hostname
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsArchitecture
```

#### `systeminfo` en détail

`systeminfo` est une mine d’or — elle affiche en une seule commande :

- Le nom et la version de l’OS
- La date d’installation
- La date du dernier démarrage (uptime)
- La mémoire totale et disponible
- Les cartes réseau
- Les correctifs (hotfixes) installés

```cmd
systeminfo
systeminfo | findstr /i "boot"       REM Depuis quand la machine tourne-t-elle ?
systeminfo | findstr /i "hotfix"     REM Quels patchs sont installés ?
```

#### Informations système via PowerShell (CIM)

PowerShell accède à des informations système détaillées via **CIM** (Common Information Model) :

```powershell
# Informations sur le système d'exploitation
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, LastBootUpTime

# Informations sur le matériel
Get-CimInstance Win32_ComputerSystem | Select-Object Name, Manufacturer, Model, TotalPhysicalMemory

# Espace disque
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, @{N="Taille (Go)";E={[math]::Round($_.Size/1GB)}}, @{N="Libre (Go)";E={[math]::Round($_.FreeSpace/1GB)}}
```

> **Note :** `Get-CimInstance` remplace l’ancien `Get-WmiObject` (qui fonctionne encore mais est déprécié). CIM est la méthode moderne pour interroger le système.

#### Espace disque avec CMD

```cmd
wmic logicaldisk get name,size,freespace
```

> **⚠️ wmic est déprécié.** Microsoft a marqué `wmic` comme obsolète depuis Windows 10 21H1 / Windows Server 21H1, et il peut ne pas être disponible sur certaines versions récentes de Windows 11. Il reste utile à connaître pour lire d’anciens scripts, mais pour tout nouveau travail, utilise PowerShell avec `Get-CimInstance` (méthode moderne, supportée et plus puissante).

> **📋 FIL ROUGE — Épisode 6**
> 
> Le responsable IT demande un état des lieux rapide du serveur de fichiers. Léa lance `systeminfo` et note : Windows Server 2022, 32 Go de RAM, uptime de 45 jours, 12 hotfixes installés. Elle vérifie l’espace disque avec `Get-CimInstance Win32_LogicalDisk` : il reste 15 Go libres sur 500 — c’est peut-être la cause des problèmes.


-----

## Chapitre 11 — Processus

### Le minimum à savoir

#### Qu’est-ce qu’un processus ?

Un **processus** est un programme en cours d’exécution. Chaque fois que tu ouvres Chrome, Word, ou même le terminal, Windows crée un processus avec un numéro unique (le **PID** — Process ID).

#### Lister les processus

```cmd
REM CMD
tasklist                             REM Liste tous les processus
tasklist | findstr chrome            REM Filtrer par nom
```

```powershell
# PowerShell
Get-Process                          # Liste tous les processus
Get-Process chrome                   # Filtrer par nom
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object Name, Id, @{N="RAM (Mo)";E={[math]::Round($_.WorkingSet64/1MB)}} -First 10
```

#### Arrêter un processus

```cmd
REM CMD
taskkill /PID 1234                   REM Arrêter par PID
taskkill /IM notepad.exe             REM Arrêter par nom
taskkill /PID 1234 /F                REM Forcer l'arrêt (/F = force)
```

```powershell
# PowerShell
Stop-Process -Id 1234                # Arrêter par PID
Stop-Process -Name notepad           # Arrêter par nom
```

> **⚠️ Attention :** arrêter un processus système peut rendre la machine instable. Ne tue que les processus que tu connais.

#### Point sécurité

Un processus peut être suspect si :

- Il a un nom inhabituel ou qui ressemble à un processus légitime (ex : `svchost.exe` dans un dossier autre que `System32`)
- Il consomme anormalement le CPU ou la RAM
- Il est lancé depuis un chemin inhabituel (`C:\Temp\`, `%APPDATA%\...`)
- Il ouvre des connexions réseau vers des adresses inconnues
> **Attention :** un chemin hors `System32` n’est pas automatiquement suspect. C’est seulement un indice à croiser avec le nom du processus, sa signature, son comportement réseau et son contexte.

```powershell
# Voir le chemin de l'exécutable d'un processus
Get-Process | Select-Object Name, Id, Path | Where-Object Path -notlike "*System32*"
```

> **📋 FIL ROUGE — Épisode 7**
> 
> Un poste est anormalement lent. Léa lance `tasklist` puis `Get-Process | Sort-Object CPU -Descending`. Un processus `update_service.exe` consomme 95% du CPU depuis `C:\Users\dupont\AppData\Local\Temp`. Suspect. Elle vérifie qu’il ne correspond à aucun logiciel connu, note le PID, et le tue avec `taskkill /PID 4567 /F`.


-----

## Chapitre 12 — Services Windows

### Le minimum à savoir

#### Qu’est-ce qu’un service ?

Un **service** est un programme qui tourne en arrière-plan, souvent sans fenêtre visible. Windows en a des dizaines : le pare-feu, Windows Update, le spooler d’impression, le DNS client, etc.

#### Lister les services

```cmd
REM CMD
sc query                             REM Services en cours d'exécution
sc query state= all                  REM Tous les services (attention : espace avant "all")
```

```powershell
# PowerShell
Get-Service                          # Tous les services
Get-Service | Where-Object Status -eq "Running"    # En cours d'exécution
Get-Service | Where-Object Status -eq "Stopped"    # Arrêtés
Get-Service -Name "wuauserv"         # Un service spécifique (Windows Update)
```

#### Démarrer / arrêter un service

```cmd
REM CMD                                              [🔑 Admin]
net start wuauserv                   REM Démarrer Windows Update
net stop wuauserv                    REM Arrêter Windows Update
```

```powershell
# PowerShell                                         [🔑 Admin]
Start-Service -Name wuauserv
Stop-Service -Name wuauserv
Restart-Service -Name wuauserv
```

#### Mode de démarrage

```powershell
# Voir le mode de démarrage d'un service              [🔑 Admin]
Get-Service wuauserv | Select-Object Name, Status, StartType

# Modifier (avec prudence)
Set-Service -Name wuauserv -StartupType Manual
```

#### Point sécurité

Les services sont importants en cybersécurité pour détecter :

- Un service inconnu qui tourne
- Un service récemment installé (Event ID 7045)
- Un mécanisme de **persistance** (un malware qui s’installe comme service pour redémarrer automatiquement)

> **📋 FIL ROUGE — Épisode 8**
> 
> Le spooler d’impression est arrêté — les utilisateurs ne peuvent plus imprimer. Léa vérifie avec `Get-Service Spooler`, constate qu’il est “Stopped”, le redémarre avec `Start-Service Spooler`, et vérifie qu’il passe bien en “Running”.


-----

## Chapitre 13 — Utilisateurs et groupes locaux

### Le minimum à savoir

#### Identifier l’utilisateur actuel

```cmd
whoami                               REM Affiche DOMAINE\utilisateur ou MACHINE\utilisateur
```

#### Lister les utilisateurs locaux

```cmd
REM CMD
net user                             REM Liste les comptes locaux
net user alice                       REM Détails d'un compte (dernière connexion, expiration...)
```

```powershell
# PowerShell
Get-LocalUser                        # Liste les comptes locaux
Get-LocalUser -Name "alice"          # Détails d'un compte
```

#### Lister les groupes locaux

```cmd
REM CMD
net localgroup                       REM Liste les groupes
net localgroup Administrators        REM Membres du groupe Administrators
```

```powershell
# PowerShell
Get-LocalGroup                       # Liste les groupes
Get-LocalGroupMember Administrators  # Qui est administrateur ?
```

> **Pourquoi c’est important :** savoir qui est dans le groupe **Administrators** est une question de sécurité fondamentale. Trop de comptes admin = surface d’attaque trop large.

#### Actions de modification (aperçu)

La création d’utilisateurs (`New-LocalUser`), l’ajout à des groupes (`Add-LocalGroupMember`), et la suppression sont des opérations d’administration qui nécessitent des droits élevés et de la prudence. Elles sont couvertes en détail dans les cours d’administration Windows et Active Directory.


-----

## Chapitre 14 — Tâches planifiées

### Le minimum à savoir

#### Qu’est-ce qu’une tâche planifiée ?

Une **tâche planifiée** (scheduled task) est une action programmée pour s’exécuter automatiquement :

- Au démarrage de la machine
- À la connexion d’un utilisateur
- À une heure précise (tous les jours à 2h du matin)
- Selon un événement (quand un log spécifique apparaît)

#### Pourquoi c’est important ?

- **Administration :** sauvegardes automatiques, maintenance, nettoyage
- **Sécurité :** les tâches planifiées sont un **mécanisme de persistance** classique — un malware peut créer une tâche pour se relancer au démarrage

#### Lister les tâches

```cmd
REM CMD
schtasks                             REM Liste toutes les tâches planifiées
schtasks /query /tn "NomDeLaTache"   REM Détails d'une tâche spécifique
```

```powershell
# PowerShell
Get-ScheduledTask                    # Toutes les tâches
Get-ScheduledTask | Select-Object TaskName, State -First 20
Get-ScheduledTask | Where-Object State -eq "Ready"    # Tâches actives
```

> **Astuce sécurité :** une tâche planifiée qui exécute un programme depuis `C:\Temp`, `%APPDATA%` ou un chemin inhabituel mérite une vérification.

> **Note :** la création et la suppression de tâches planifiées (`Register-ScheduledTask`, `Unregister-ScheduledTask`) sont des opérations d’administration couvertes dans le cours PowerShell.


-----

## Chapitre 15 — Le registre Windows

### Le minimum à savoir

#### Qu’est-ce que le registre ?

Le **registre Windows** est une base de données hiérarchique qui stocke la configuration de Windows, des applications et des utilisateurs. Tout y est : les paramètres d’affichage, les programmes au démarrage, les associations de fichiers, les politiques de sécurité…

#### Les ruches principales

|Ruche              |Abréviation|Contenu                                                    |
|-------------------|-----------|-----------------------------------------------------------|
|HKEY_LOCAL_MACHINE |`HKLM`     |Configuration de la machine (matériel, logiciels, services)|
|HKEY_CURRENT_USER  |`HKCU`     |Configuration de l’utilisateur connecté                    |
|HKEY_CLASSES_ROOT  |`HKCR`     |Associations de fichiers                                   |
|HKEY_USERS         |`HKU`      |Tous les profils utilisateurs                              |
|HKEY_CURRENT_CONFIG|`HKCC`     |Configuration matérielle actuelle                          |

#### L’éditeur graphique

```cmd
regedit                              REM Ouvre l'éditeur de registre (GUI)
```

#### Lire le registre avec CMD

```cmd
reg query HKCU                       REM Lister les sous-clés de HKCU
reg query "HKCU\Software"            REM Naviguer dans Software
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"    REM Programmes au démarrage
```

#### Lire le registre avec PowerShell

PowerShell traite le registre comme un système de fichiers (un PSDrive) :

```powershell
Get-ChildItem HKCU:\                 # Naviguer dans HKCU
Get-ChildItem HKCU:\Software         # Sous-clés de Software

# Les programmes qui se lancent au démarrage de l'utilisateur
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Les programmes qui se lancent au démarrage de la machine      [🔑 Admin]
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
```

> **Point sécurité :** les clés `Run` et `RunOnce` dans le registre sont l’un des mécanismes de persistance les plus courants. Un programme listé ici se lance automatiquement à chaque connexion ou démarrage.

#### Précaution

> **⚠️ Dans ce cours, on apprend à LIRE le registre.** La modification du registre peut casser une configuration Windows si elle est mal faite. La modification est un sujet d’administration avancé.


-----

## Chapitre 16 — Journaux Windows (Event Logs)

### Le minimum à savoir

#### Qu’est-ce qu’un journal d’événements ?

Windows enregistre en permanence ce qui se passe sur la machine dans des **journaux** (Event Logs). C’est l’équivalent des logs sous Linux. Chaque événement a un **Event ID** — un numéro qui identifie le type d’événement.

#### Les journaux principaux

|Journal                                     |Contenu                                                         |
|--------------------------------------------|----------------------------------------------------------------|
|**System**                                  |Événements système (services, drivers, démarrage)               |
|**Application**                             |Événements des applications                                     |
|**Security**                                |Connexions, déconnexions, accès aux ressources (nécessite admin)|
|**Windows PowerShell**                      |Activité PowerShell classique                                   |
|**Microsoft-Windows-PowerShell/Operational**|Activité PowerShell détaillée (Script Block Logging)            |

#### Lire les événements

```powershell
# Les 20 derniers événements du journal System
Get-WinEvent -LogName System -MaxEvents 20

# Les 20 derniers du journal Application
Get-WinEvent -LogName Application -MaxEvents 20

# Les 20 derniers du journal Security                           [🔑 Admin]
Get-WinEvent -LogName Security -MaxEvents 20

# Lister tous les journaux disponibles
Get-WinEvent -ListLog * | Select-Object LogName, RecordCount | Sort-Object RecordCount -Descending -First 20
```

> **⚠️ Important :** toujours utiliser `-MaxEvents` pour limiter le nombre de résultats. Sans ça, PowerShell tente de charger TOUT le journal — ce qui peut être très long.

#### Filtrer les événements

```powershell
# Les erreurs parmi les 50 derniers événements du journal System
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object LevelDisplayName -eq "Error"

# Vraiment filtrer sur les dernières 24 heures (méthode efficace avec FilterHashtable)
Get-WinEvent -FilterHashtable @{
    LogName   = "System"
    Level     = 2                          # 2 = Error
    StartTime = (Get-Date).AddDays(-1)
}

# Filtrer par Event ID
Get-WinEvent -FilterHashtable @{LogName="Security"; Id=4625} -MaxEvents 10    # Échecs de connexion
```

> **Bonne pratique :** `-FilterHashtable` filtre **côté serveur** (au niveau du moteur d’événements Windows), bien plus performant que de tout récupérer puis filtrer avec `Where-Object`. Sur un journal volumineux, la différence peut être de plusieurs minutes. Microsoft recommande systématiquement cette approche pour `Get-WinEvent`.

> **Les niveaux d’événements (`Level`) :** `1` = Critical, `2` = Error, `3` = Warning, `4` = Information, `5` = Verbose.

#### Les Event IDs à connaître

|Event ID|Journal               |Signification                                     |
|--------|----------------------|--------------------------------------------------|
|4624    |Security              |Connexion réussie                                 |
|4625    |Security              |Échec de connexion                                |
|4720    |Security              |Création d’un compte utilisateur                  |
|7045    |System                |Installation d’un nouveau service                 |
|1102    |Security              |Journal de sécurité effacé (suspect !)            |
|4104    |PowerShell/Operational|Script Block Logging (contenu d’un script exécuté)|


> **📋 FIL ROUGE — Épisode 9**
> 
> Suspicion d’activité anormale sur un poste. Léa consulte les logs de sécurité : `Get-WinEvent -FilterHashtable @{LogName="Security"; Id=4625} -MaxEvents 20`. Elle trouve 47 échecs de connexion en 10 minutes sur le compte “admin” — c’est une tentative de brute-force. Elle note l’adresse IP source et remonte l’information à l’équipe sécurité.


-----

## Chapitre 17 — Réseau avec CMD et PowerShell

### Le minimum à savoir

C’est le chapitre le plus utilisé au quotidien. Les commandes réseau sont la raison n°1 pour laquelle beaucoup de gens ouvrent un terminal.

#### Configuration IP

```cmd
REM CMD
ipconfig                             REM Résumé (IP, masque, passerelle)
ipconfig /all                        REM Détail complet (DNS, DHCP, MAC...)
```

```powershell
# PowerShell
Get-NetIPAddress | Where-Object AddressFamily -eq "IPv4"
Get-NetIPConfiguration               # Configuration complète
Get-NetAdapter                       # Cartes réseau
```

#### Tester la connectivité

```cmd
REM CMD
ping 8.8.8.8                         REM Tester la connexion à une IP
ping google.com                      REM Tester la résolution DNS + la connexion
ping -n 1 8.8.8.8                    REM Un seul ping (par défaut : 4)
```

```powershell
# PowerShell
Test-Connection google.com           # Ping en objets
Test-Connection 8.8.8.8 -Count 1    # Un seul ping
```

#### Résolution DNS

```cmd
REM CMD
nslookup google.com                  REM Interroger le DNS
ipconfig /displaydns                 REM Voir le cache DNS local
ipconfig /flushdns                   REM Vider le cache DNS
```

```powershell
# PowerShell
Resolve-DnsName google.com
Get-DnsClientCache                   # Cache DNS
Clear-DnsClientCache                 # Vider le cache
```

#### Chemin réseau

```cmd
REM CMD
tracert google.com                   REM Tracer le chemin réseau
pathping google.com                  REM Ping + tracert combinés (plus lent, plus complet)
```

```powershell
# PowerShell
Test-NetConnection google.com -TraceRoute
```

#### Tester un port spécifique

```powershell
Test-NetConnection google.com -Port 443         # Le port 443 (HTTPS) est-il ouvert ?
Test-NetConnection serveur01 -Port 3389         # Le port RDP est-il accessible ?
```

#### Connexions actives

```cmd
REM CMD
netstat -ano                         REM Connexions actives avec PID
netstat -an                          REM Connexions sans résolution DNS (plus rapide)
```

```powershell
# PowerShell
Get-NetTCPConnection                 # Toutes les connexions TCP
Get-NetTCPConnection | Where-Object State -eq "Established"    # Connexions actives
```

#### Relier un port à un processus

```cmd
REM CMD : en deux étapes
netstat -ano                         REM 1. Trouver le PID qui utilise le port
tasklist | findstr 1234              REM 2. Trouver le nom du processus
```

```powershell
# PowerShell : en une seule commande
Get-NetTCPConnection | Select-Object LocalPort, RemoteAddress, State, OwningProcess |
    Where-Object LocalPort -eq 8080
Get-Process -Id 1234                 # Identifier le processus par son PID
```

#### Renouveler la configuration DHCP

```cmd
ipconfig /release                    REM Libérer l'adresse IP
ipconfig /renew                      REM Obtenir une nouvelle adresse
```

#### Pare-feu Windows (aperçu)

```powershell
# Voir les règles de pare-feu
Get-NetFirewallRule | Select-Object DisplayName, Direction, Action, Enabled -First 20
```

> **Note :** la création et la modification de règles de pare-feu (`New-NetFirewallRule`, etc.) sont des opérations d’administration avancées.

> **📋 FIL ROUGE — Épisode 10**
> 
> Le poste de l’utilisateur ne se connecte plus au réseau. Léa diagnostique pas à pas :
> 
> 1. `ipconfig` → l’IP est en 169.254.x.x (APIPA — pas de DHCP)
> 1. `ipconfig /renew` → timeout, pas de réponse du serveur DHCP
> 1. `ping 192.168.1.1` (passerelle) → pas de réponse
> 1. Vérification physique : le câble réseau était débranché. Problème résolu.


-----

## Chapitre 18 — Interagir avec le Web depuis la CLI

### Le minimum à savoir

#### Pourquoi interagir avec le web ?

- Tester l’accès à un site
- Télécharger un fichier
- Vérifier qu’un service web répond
- Diagnostiquer un problème de proxy ou de connectivité HTTPS

#### Avec `curl`

Windows 10/11 inclut `curl.exe`. Mais attention au piège : dans **Windows PowerShell 5.1**, `curl` (sans le `.exe`) est interprété comme un alias de `Invoke-WebRequest` — pas le vrai outil curl. Pour appeler explicitement le vrai `curl`, utilise toujours `curl.exe` :

```cmd
curl.exe https://example.com                           REM Récupérer le contenu d'une page
curl.exe -o page.html https://example.com              REM Télécharger dans un fichier
curl.exe -I https://example.com                        REM Voir les en-têtes HTTP seulement
```

> **Note :** dans PowerShell 7+, l’alias `curl` a été supprimé pour éviter cette confusion — `curl` y appelle bien le vrai `curl.exe`. Mais par sécurité, prends le réflexe d’écrire `curl.exe` partout.

#### Avec PowerShell

```powershell
Invoke-WebRequest https://example.com                  # Récupérer une page web
Invoke-WebRequest https://example.com -OutFile page.html   # Télécharger
(Invoke-WebRequest https://example.com).StatusCode     # Code HTTP (200 = OK)
```

#### Les codes HTTP à connaître

|Code     |Signification    |
|---------|-----------------|
|200      |OK — tout va bien|
|301 / 302|Redirection      |
|403      |Accès interdit   |
|404      |Page non trouvée |
|500      |Erreur serveur   |


-----

## PARTIE IV — AUTOMATISATION ET TRIAGE

-----

## Chapitre 19 — Introduction aux scripts batch (.bat)

### Le minimum à savoir

#### Qu’est-ce qu’un fichier batch ?

Un fichier `.bat` (ou `.cmd`) contient des commandes CMD exécutées dans l’ordre, comme un script Bash. C’est la forme de scripting la plus ancienne sous Windows.

#### Premier fichier batch

Crée un fichier `info.bat` avec un éditeur de texte :

```batch
@echo off
echo === Informations systeme ===
echo.
echo Utilisateur : %USERNAME%
echo Machine     : %COMPUTERNAME%
echo Date        : %DATE%
echo Heure       : %TIME%
echo.
pause
```

Double-clique sur le fichier ou lance-le avec `.\info.bat` dans le terminal.

- `@echo off` : empêche l’affichage de chaque commande avant son exécution
- `echo.` : affiche une ligne vide
- `pause` : attend que l’utilisateur appuie sur une touche

#### Variables dans un batch

```batch
@echo off
set NOM=Lea
echo Bonjour %NOM% !

set /p AGE=Quel est ton age ?
echo Tu as %AGE% ans.
```

#### Arguments

```batch
@echo off
echo Premier argument : %1
echo Deuxieme argument : %2
echo Tous les arguments : %*
```

```cmd
info.bat Alice 25
```

#### Conditions simples

```batch
@echo off
if exist "C:\Temp\fichier.txt" (
    echo Le fichier existe.
) else (
    echo Le fichier n'existe pas.
)

if "%1"=="" (
    echo Erreur : donne un argument.
    exit /b 1
)
```

#### Boucle simple

```batch
@echo off
for f
```

> **Note :** dans un fichier batch, les variables de boucle utilisent ``, les guillemets)
- Pas de gestion d’erreurs structurée
- Pas d’objets, pas de modules
- Pas de filtrage avancé
- Difficilement lisible pour les scripts complexes

**PowerShell remplace le batch pour tout ce qui dépasse 10-15 lignes.** Le batch reste utile pour les scripts de démarrage, les tâches très simples, et la compatibilité avec des environnements anciens.


-----

## Chapitre 20 — Introduction à l’automatisation PowerShell

### Le minimum à savoir

Ce chapitre est une **passerelle** vers le cours PowerShell complet de la bibliothèque. On ne fait ici qu’effleurer le scripting.

#### Commande vs script

- Une **commande** s’exécute directement dans le terminal : `Get-Process`
- Un **script** est un fichier `.ps1` qui contient plusieurs commandes

#### Premier mini-script PowerShell

Crée un fichier `rapport.ps1` :

```powershell
# rapport.ps1 — Collecte rapide d'informations
Write-Host "=== Rapport systeme ===" -ForegroundColor Cyan

Write-Output "Utilisateur : $env:USERNAME"
Write-Output "Machine     : $env:COMPUTERNAME"
Write-Output "Date        : $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Output ""

Write-Host "[Top 5 processus par CPU]" -ForegroundColor Yellow
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 5 | Format-Table

Write-Host "[Services arretes]" -ForegroundColor Yellow
Get-Service | Where-Object Status -eq "Stopped" | Select-Object Name, DisplayName -First 10 | Format-Table

Write-Host "[Espace disque]" -ForegroundColor Yellow
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, @{N="Libre (Go)";E={[math]::Round($_.FreeSpace/1GB)}} | Format-Table
```

#### Exécuter le script

```powershell
.\rapport.ps1
```

Si tu obtiens une erreur sur la politique d’exécution :

```powershell
Get-ExecutionPolicy                                    # Voir la politique actuelle
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser    # Autoriser les scripts locaux
```

> **Note :** le détail de la politique d’exécution, des variables, des boucles, des fonctions, de `param()`, du pipeline d’objets en profondeur — tout ça est couvert dans le **cours PowerShell** de la bibliothèque.

#### Exporter les résultats dans un fichier

```powershell
Get-Process | Out-File process.txt
Get-Service | Export-Csv services.csv -NoTypeInformation
```


-----

## Chapitre 21 — Sécurité et triage depuis la ligne de commande

### Le minimum à savoir

#### L’objectif du triage

Le **triage** consiste à collecter rapidement des informations sur une machine pour comprendre son état — est-elle saine ? Y a-t-il des indices de compromission ? C’est la première étape d’une investigation.

#### La collecte de base

```powershell
# Identité
whoami
hostname

# Réseau
ipconfig /all
netstat -ano

# Processus
tasklist
Get-Process

# Services
Get-Service

# Utilisateurs
net user
net localgroup Administrators

# Tâches planifiées
schtasks
Get-ScheduledTask

# Événements récents
Get-WinEvent -LogName System -MaxEvents 20
Get-WinEvent -LogName Security -MaxEvents 20    # [🔑 Admin]
```

#### Vérifier un fichier suspect

```powershell
# Hash du fichier (pour comparaison avec des bases d'IOC comme VirusTotal)
Get-FileHash "C:\Temp\suspect.exe" -Algorithm SHA256

# Signature numérique (signé par un éditeur de confiance ?)
Get-AuthenticodeSignature "C:\Temp\suspect.exe"

# Métadonnées (taille, dates de création/modification)
Get-Item "C:\Temp\suspect.exe" | Select-Object Name, Length, CreationTime, LastWriteTime
```

#### Vérifier les programmes au démarrage

```powershell
# Registre : clés Run
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue

# Tâches planifiées actives
Get-ScheduledTask | Where-Object State -eq "Ready" | Select-Object TaskName, TaskPath

# Services avec un chemin inhabituel
Get-CimInstance Win32_Service |
    Where-Object { $_.PathName -and $_.PathName -notlike "*System32*" -and $_.PathName -notlike "*SysWOW64*" } |
    Select-Object Name, State, PathName
```

#### Vérifier les connexions réseau suspectes

```powershell
# Connexions actives vers l'extérieur
Get-NetTCPConnection | Where-Object State -eq "Established" |
    Select-Object LocalPort, RemoteAddress, RemotePort, OwningProcess

# Identifier le processus derrière une connexion
Get-Process -Id (Get-NetTCPConnection | Where-Object RemotePort -eq 4444).OwningProcess

# Port `4444` souvent utilisé dans exemples de sécurité, mais port seul ne suffit jamais à conclure qu’une activité est malveillante. Elle fonctionne si une seule connexion correspond. Si plusieurs connexions correspondent, ou aucune, ça peut être moins propre. Préferer :

Get-NetTCPConnection | Where-Object RemotePort -eq 4444 |
ForEach-Object {
    Get-Process -Id $_.OwningProcess
}
```

#### Aperçu Sysinternals

Les **Sysinternals** sont une suite d’outils Microsoft gratuits, essentiels pour l’administration et l’investigation Windows :

|Outil               |Usage                                                                      |
|--------------------|---------------------------------------------------------------------------|
|**Autoruns**        |Voir TOUT ce qui se lance au démarrage (bien plus complet que les clés Run)|
|**Process Explorer**|Version améliorée du Gestionnaire des tâches                               |
|**TCPView**         |Voir les connexions réseau en temps réel par processus                     |
|**PsExec**          |Exécuter des commandes sur des machines distantes                          |


> **Note :** les Sysinternals sont des outils à part entière, pas des commandes PowerShell. Ils sont téléchargeables gratuitement sur [learn.microsoft.com/sysinternals](https://learn.microsoft.com/sysinternals).

> **📋 FIL ROUGE — Épisode 11**
> 
> Un fichier suspect `update_service.exe` a été trouvé sur un poste. Léa vérifie :
> 
> 1. `Get-FileHash` →  Elle vérifie le hash dans un outil de réputation ou une base IOC autorisée par son organisation. (Par exemple : Elle vérifie le hash sur VirusTotal, si la politique de l’organisation l’autorise) → 35 détections. C’est un malware.
> 2. `Get-AuthenticodeSignature` → “NotSigned”. Pas signé.
> 3. Elle vérifie les clés `Run` → le fichier est présent dans la clé de démarrage.
> 4. Elle vérifie `Get-NetTCPConnection` → le processus ouvre une connexion vers une IP étrangère sur le port 4444.
>    Conclusion : compromission confirmée. Elle isole le poste du réseau et remonte l’incident.


-----

## Chapitre 22 — PowerShell Remoting : aperçu

### Le minimum à savoir

#### Pourquoi administrer à distance ?

- 200 postes → on ne va pas se déplacer sur chaque machine
- Serveurs sans interface graphique (Server Core)
- Télétravail et intervention à distance
- Administration centralisée

#### Le principe

PowerShell Remoting (via **WinRM** — Windows Remote Management) permet d’exécuter des commandes PowerShell sur des machines distantes, comme SSH le fait sous Linux.

#### Les commandes à connaître

```powershell
# Ouvrir une session interactive sur une machine distante
Enter-PSSession -ComputerName SERVEUR01
# Tu es maintenant "sur" SERVEUR01 — les commandes s'exécutent là-bas
Exit-PSSession

# Exécuter une commande ponctuelle à distance
Invoke-Command -ComputerName SERVEUR01 -ScriptBlock { Get-Service }

# Exécuter sur PLUSIEURS machines en parallèle
Invoke-Command -ComputerName SERVEUR01, SERVEUR02, SERVEUR03 -ScriptBlock {
    hostname
    Get-CimInstance Win32_OperatingSystem | Select-Object Caption, LastBootUpTime
}
```
> **Important :** ces commandes ne fonctionnent que si PowerShell Remoting / WinRM est activé et autorisé sur la machine distante. En entreprise, cette configuration est souvent gérée par GPO ou par l’équipe infrastructure.
#### La sécurité du remoting

PowerShell Remoting s’appuie sur **WinRM** (Windows Remote Management).

- En environnement Active Directory, l’authentification se fait généralement avec **Kerberos** (le standard de sécurité Windows)
- Hors domaine, c’est **NTLM** par défaut, et il faut configurer manuellement la liste des hôtes de confiance (`TrustedHosts`)
- La communication peut passer en **HTTP** (par défaut, mais le contenu reste protégé entre machines de confiance) ou en **HTTPS** (recommandé pour les environnements sensibles, nécessite des certificats)
- Toute activité de remoting est journalisée dans les Event Logs

> **À retenir :** la configuration exacte dépend du contexte (domaine, workgroup, HTTP/HTTPS, TrustedHosts, certificats, GPO de sécurité). Dans un environnement professionnel, ces paramètres sont généralement gérés par l’équipe infrastructure.

> **Note :** la configuration avancée du remoting (JEA, CredSSP, certificats, TrustedHosts hors domaine) est un sujet d’administration avancé, couvert dans les cours d’infrastructure.


-----

## PARTIE V — LABS, ÉVALUATION ET SYNTHÈSE

-----

## Chapitre 23 — Labs progressifs

Ces labs sont conçus pour être exécutés directement dans ton terminal Windows.

### Lab 1 — Premiers pas

```cmd
whoami
hostname
ver
cd
dir
cls
```

### Lab 2 — Navigation

```cmd
cd %USERPROFILE%
dir
cd Desktop
cd ..
cd \
tree /f
```

```powershell
cd ~
Get-ChildItem
Get-ChildItem -Force
cd ..
```

### Lab 3 — Fichiers et dossiers CMD

```cmd
mkdir LabCMD
cd LabCMD
echo Bonjour Windows > test.txt
type test.txt
echo Deuxieme ligne >> test.txt
type test.txt
copy test.txt copie.txt
dir
del copie.txt
del test.txt
cd ..
rmdir LabCMD
```

### Lab 4 — Fichiers et dossiers PowerShell

```powershell
New-Item -ItemType Directory -Name "LabPS"
Set-Location LabPS
Set-Content test.txt "Bonjour PowerShell"
Get-Content test.txt
Add-Content test.txt "Deuxieme ligne"
Get-Content test.txt
Copy-Item test.txt copie.txt
Get-ChildItem
Remove-Item copie.txt
Set-Location ..
Remove-Item LabPS -Recurse
```

### Lab 5 — Variables d’environnement et PATH

```cmd
echo %USERNAME%
echo %USERPROFILE%
echo %TEMP%
echo %PATH%
where notepad
```

```powershell
$env:USERNAME
$env:USERPROFILE
$env:TEMP
$env:PATH
Get-Command notepad
```

### Lab 6 — Recherche

```cmd
mkdir LabRecherche
cd LabRecherche
echo "Tout va bien" > rapport1.txt
echo "Erreur critique" > rapport2.txt
echo "Tout va bien" > rapport3.txt
findstr "Erreur" *.txt
dir /s /b *.txt
```

```powershell
# (Reste dans le même dossier LabRecherche)
Select-String -Path *.txt -Pattern "Erreur"
Get-ChildItem -Filter *.txt
```

```cmd
REM Une fois les essais terminés, on nettoie
cd ..
rmdir /s LabRecherche
```

### Lab 7 — Réseau

```cmd
ipconfig /all
ping -n 2 8.8.8.8
ping -n 2 google.com
nslookup google.com
netstat -ano | findstr "ESTABLISHED"
```

```powershell
Test-NetConnection google.com -Port 443
Resolve-DnsName google.com
Get-NetTCPConnection | Where-Object State -eq "Established" | Select-Object -First 5
```

### Lab 8 — Processus et services

```cmd
tasklist | findstr "explorer"
```

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10
Get-Service | Where-Object Status -eq "Running" | Measure-Object
Get-Service | Where-Object Status -eq "Stopped" | Select-Object Name -First 10
```

### Lab 9 — Utilisateurs et groupes

```cmd
whoami
net user
net localgroup
net localgroup Administrators
```

```powershell
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember Administrators
```

### Lab 10 — Tâches planifiées et registre

```powershell
Get-ScheduledTask | Select-Object TaskName, State -First 15
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -ErrorAction SilentlyContinue
```

### Lab 11 — Journaux Windows

```powershell
Get-WinEvent -LogName System -MaxEvents 10 | Select-Object TimeCreated, LevelDisplayName, Message
Get-WinEvent -LogName Application -MaxEvents 10 | Select-Object TimeCreated, LevelDisplayName, Message
```

### Lab 12 — Mini collecte de triage

```powershell
$collecte = "$env:USERPROFILE\Collecte"
New-Item -ItemType Directory -Path $collecte -Force
Set-Location $collecte

whoami > identity.txt
hostname >> identity.txt
systeminfo > system.txt
ipconfig /all > network.txt
netstat -ano > connections.txt
tasklist > processes.txt
net user > users.txt
net localgroup Administrators > admins.txt

Get-Process | Out-File processes_ps.txt
Get-Service | Out-File services_ps.txt
Get-ScheduledTask | Out-File scheduled_tasks.txt
Get-WinEvent -LogName System -MaxEvents 20 | Out-File events_system.txt

Write-Host "Collecte terminee dans $collecte" -ForegroundColor Green
Get-ChildItem
```

> **Pourquoi `$env:USERPROFILE` plutôt que `C:\Temp` ?** Sur certains postes verrouillés, un utilisateur standard n’a pas le droit d’écrire à la racine de `C:\`. Utiliser le profil utilisateur (`C:\Users\TonNom\`) garantit que le lab fonctionne partout, sans droits admin.

-----

## Chapitre 24 — Skills Assessment — Évaluation finale

### Objectif

Tu dois être capable de créer un dossier de collecte et d’y stocker les résultats de commandes qui répondent aux questions ci-dessous.

### Consignes

```powershell
# Crée le dossier de collecte (dans ton profil utilisateur, pas besoin d'admin)
$assessment = "$env:USERPROFILE\WindowsCLI-Assessment"
New-Item -ItemType Directory -Path $assessment -Force
Set-Location $assessment
```

Utilise les commandes que tu as apprises pour répondre à chaque question et stocke les résultats dans des fichiers.

### Questions

1. **Quel utilisateur est connecté ?** Quel est son nom complet (DOMAINE\utilisateur ou MACHINE\utilisateur) ?
1. **Quel est le nom de la machine ?**
1. **Quelle est l’adresse IP de la machine ?** Quelle est sa passerelle par défaut ?
1. **Quels processus sont actifs ?** Lequel consomme le plus de CPU ?
1. **Quels services sont présents ?** Combien sont en cours d’exécution, combien sont arrêtés ?
1. **Quels utilisateurs locaux existent ?**
1. **Qui est administrateur local ?**
1. **Quelles tâches planifiées existent ?** Y en a-t-il dans un état inhabituel ?
1. **Quels événements système récents sont visibles ?** Y a-t-il des erreurs ?
1. **Quelle est la différence fondamentale entre CMD et PowerShell ?** (Réponse écrite, pas une commande.)

### Exemple de collecte attendue

```powershell
whoami > identity.txt
hostname >> identity.txt
systeminfo > system.txt
ipconfig /all > network.txt
tasklist > processes.txt
Get-Process | Sort-Object CPU -Descending | Select-Object Name, Id, CPU -First 10 | Out-File top_cpu.txt
Get-Service | Out-File services.txt
(Get-Service | Where-Object Status -eq "Running" | Measure-Object).Count | Out-File services_count.txt
net user > users.txt
net localgroup Administrators > admins.txt
Get-ScheduledTask | Out-File scheduled_tasks.txt
Get-WinEvent -LogName System -MaxEvents 30 | Out-File events_system.txt
Get-WinEvent -LogName System -MaxEvents 30 | Where-Object LevelDisplayName -eq "Error" | Out-File events_errors.txt
```

-----

## Chapitre 25 — Synthèse et boîte à outils du praticien

### Quand utiliser CMD ?

- Dépannage réseau rapide (`ipconfig`, `ping`, `tracert`, `netstat`)
- Compatibilité avec des environnements anciens
- Scripts batch existants
- Tâches très simples et ponctuelles

### Quand utiliser PowerShell ?

- Administration moderne (processus, services, utilisateurs, registre)
- Filtrage et tri avancés (`Where-Object`, `Sort-Object`, `Select-Object`)
- Export structuré (CSV, JSON)
- Collecte d’informations système (`Get-CimInstance`)
- Consultation des journaux (`Get-WinEvent`)
- Triage et investigation de sécurité
- Automatisation et scripting (→ cours PowerShell)

### Les prochaines étapes

|Cours de la bibliothèque       |Ce qu’il apporte                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------|
|**Cours PowerShell**           |Scripting avancé : variables, boucles, fonctions, param(), pipeline d’objets, automatisation|
|**Cours Active Directory**     |Administration d’un domaine Windows avec PowerShell                                         |
|**Cours Infrastructure IT**    |Architecture réseau, serveurs, virtualisation                                               |
|**Cours Windows en profondeur**|Internals Windows, sécurité, hardening                                                      |
|**Cours Digital Forensics**    |Investigation numérique (dont forensic Windows)                                             |
|**Cours Réponse à incident**   |Gestion d’un incident de sécurité de bout en bout                                           |

-----

## ANNEXES

-----

### Annexe A — Correspondance CMD / PowerShell / Linux

|Opération             |CMD                 |PowerShell                    |Linux (Bash)       |
|----------------------|--------------------|------------------------------|-------------------|
|Qui suis-je ?         |`whoami`            |`whoami`                      |`whoami`           |
|Nom de la machine     |`hostname`          |`hostname`                    |`hostname`         |
|Où suis-je ?          |`cd`                |`Get-Location`                |`pwd`              |
|Changer de dossier    |`cd dossier`        |`Set-Location dossier`        |`cd dossier`       |
|Lister les fichiers   |`dir`               |`Get-ChildItem`               |`ls`               |
|Créer un dossier      |`mkdir`             |`New-Item -ItemType Directory`|`mkdir`            |
|Copier un fichier     |`copy`              |`Copy-Item`                   |`cp`               |
|Déplacer un fichier   |`move`              |`Move-Item`                   |`mv`               |
|Supprimer un fichier  |`del`               |`Remove-Item`                 |`rm`               |
|Lire un fichier       |`type`              |`Get-Content`                 |`cat`              |
|Écrire dans un fichier|`echo texte > f`    |`Set-Content f "texte"`       |`echo texte > f`   |
|Rechercher du texte   |`findstr`           |`Select-String`               |`grep`             |
|Configuration réseau  |`ipconfig`          |`Get-NetIPConfiguration`      |`ip addr`          |
|Ping                  |`ping`              |`Test-Connection`             |`ping`             |
|DNS                   |`nslookup`          |`Resolve-DnsName`             |`dig` / `nslookup` |
|Connexions réseau     |`netstat -ano`      |`Get-NetTCPConnection`        |`ss` / `netstat`   |
|Processus             |`tasklist`          |`Get-Process`                 |`ps aux`           |
|Tuer un processus     |`taskkill /PID`     |`Stop-Process -Id`            |`kill`             |
|Services              |`sc query`          |`Get-Service`                 |`systemctl`        |
|Utilisateurs          |`net user`          |`Get-LocalUser`               |`cat /etc/passwd`  |
|Variables d’env       |`set` / `echo %VAR%`|`$env:VAR`                    |`env` / `echo $VAR`|
|Aide                  |`commande /?`       |`Get-Help commande`           |`man commande`     |
|Effacer l’écran       |`cls`               |`Clear-Host`                  |`clear`            |

-----

### Annexe B — Les commandes CMD essentielles

```
whoami               hostname             ver                  cls
cd                   dir                  tree                 mkdir
rmdir                copy                 xcopy                robocopy
move                 ren                  del                  type
echo                 set                  where                findstr
ipconfig             ping                 tracert              pathping
nslookup             netstat              tasklist             taskkill
sc query             net user             net localgroup       schtasks
systeminfo           reg query            icacls               curl
```

-----

### Annexe C — Les cmdlets PowerShell essentielles

```
Get-Help                  Get-Command               Get-Alias
Get-Member                Get-Location              Set-Location
Get-ChildItem             New-Item                  Remove-Item
Copy-Item                 Move-Item                 Rename-Item
Get-Content               Set-Content               Add-Content
Select-String             Get-ComputerInfo          Get-CimInstance
Get-Process               Stop-Process              Get-Service
Start-Service             Stop-Service              Restart-Service
Get-LocalUser             Get-LocalGroupMember      Get-ScheduledTask
Get-WinEvent              Get-NetIPConfiguration    Test-Connection
Test-NetConnection        Resolve-DnsName           Get-NetTCPConnection
Invoke-WebRequest         Get-FileHash              Get-AuthenticodeSignature
Out-File                  Export-Csv                ConvertTo-Json
```

-----

### Annexe D — Event IDs Windows essentiels

|Event ID|Journal               |Signification                                          |
|--------|----------------------|-------------------------------------------------------|
|4624    |Security              |Connexion réussie                                      |
|4625    |Security              |Échec de connexion                                     |
|4648    |Security              |Connexion avec des identifiants explicites             |
|4720    |Security              |Création d’un compte utilisateur                       |
|4726    |Security              |Suppression d’un compte utilisateur                    |
|4732    |Security              |Ajout d’un membre à un groupe de sécurité              |
|4688    |Security              |Création d’un processus (si activé par GPO)            |
|7045    |System                |Installation d’un nouveau service                      |
|1102    |Security              |Journal de sécurité effacé (suspect !)                 |
|4104    |PowerShell/Operational|Script Block Logging                                   |
|400     |Windows PowerShell    |Démarrage du moteur PowerShell                         |
|6005    |System                |Démarrage du service Event Log (= la machine a démarré)|
|6006    |System                |Arrêt du service Event Log (= la machine s’est éteinte)|

-----

### Annexe E — Outils Sysinternals essentiels (aperçu)

|Outil               |Usage                                                                     |Téléchargement                                        |
|--------------------|--------------------------------------------------------------------------|------------------------------------------------------|
|**Autoruns**        |Voir TOUT ce qui se lance au démarrage (registre, services, tâches, DLLs…)|[live.sysinternals.com](https://live.sysinternals.com)|
|**Process Explorer**|Gestionnaire de tâches avancé (arborescence, DLLs, handles)               |idem                                                  |
|**TCPView**         |Connexions réseau en temps réel, par processus                            |idem                                                  |
|**PsExec**          |Exécuter des commandes sur des machines distantes                         |idem                                                  |
|**ProcMon**         |Surveiller l’activité fichier/registre/réseau d’un processus en temps réel|idem                                                  |


> **Astuce :** tous les outils Sysinternals sont accessibles sans installation via `\\live.sysinternals.com\tools\` dans l’Explorateur de fichiers.

-----

### Annexe F — Pour aller plus loin

|Thème                     |Ressource recommandée                  |
|--------------------------|---------------------------------------|
|Scripting PowerShell      |Cours PowerShell de la bibliothèque    |
|Administration Windows    |Cours Windows en profondeur            |
|Active Directory          |Cours Active Directory                 |
|Forensic Windows          |Cours Digital Forensics                |
|Réponse à incident        |Cours Réponse à incident               |
|Sysinternals en profondeur|Livre “Windows Internals” (Russinovich)|
|Infrastructure réseau     |Cours Infrastructure IT                |
|SOC / SIEM                |Cours SOC + logs Windows               |

-----

## Conclusion

Tu sais maintenant utiliser la ligne de commande Windows pour naviguer, diagnostiquer, administrer et collecter des informations. Voici ce que tu peux faire :

- **Naviguer** dans le système de fichiers et manipuler des fichiers (Ch.2-6)
- **Diagnostiquer** le réseau avec `ipconfig`, `ping`, `tracert`, `netstat` (Ch.17)
- **Inspecter** les processus, services, utilisateurs, tâches planifiées (Ch.11-14)
- **Consulter** les journaux Windows et le registre (Ch.15-16)
- **Collecter** des informations pour un triage de sécurité (Ch.21)
- **Choisir** entre CMD et PowerShell selon le contexte (Ch.9)
- **Écrire** un script batch simple et un mini-script PowerShell (Ch.19-20)

**La suite logique :**

- Le **cours PowerShell** pour apprendre à scripter et automatiser
- Le **cours Active Directory** pour administrer un domaine
- Les cours de **cybersécurité** pour utiliser ces compétences en investigation et en défense

La ligne de commande n’est pas un outil du passé — c’est l’outil le plus puissant et le plus durable de l’administration Windows. Les interfaces graphiques changent à chaque version de Windows. Les commandes, elles, restent.

Bon apprentissage !
