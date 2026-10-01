---
title: Chapitre 25 — Group Policy (GPO)
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie V — GPO et services Windows server
  - index.md
---

## 🟢 Le minimum à savoir

### Comprendre le modèle AVANT les cmdlets

> **⚠️ Point pédagogique clé.** Administrer les GPO, ce n'est **pas** mémoriser `New-GPO`. C'est comprendre un **modèle** : comment une stratégie s'applique, à qui, dans quel ordre. Sans ce modèle, les cmdlets ne servent à rien. On pose donc d'abord les concepts.

Une **GPO** (Group Policy Object) est un ensemble de réglages appliqués automatiquement à des utilisateurs et/ou des ordinateurs : politique de mot de passe, fonds d'écran, restrictions, scripts de démarrage, déploiement de logiciels, réglages de sécurité (dont le Script Block Logging du Ch.35)…

### Les deux moitiés d'une GPO

Une GPO a deux sections :

- **Computer Configuration** : s'applique aux **ordinateurs** (au démarrage et périodiquement)
- **User Configuration** : s'applique aux **utilisateurs** (à la connexion et périodiquement)

Selon ce que tu veux régler, tu utilises l'une ou l'autre.

### Le mécanisme d'application : lien + héritage

Une GPO ne fait rien tant qu'elle n'est pas **liée** à un conteneur. On lie une GPO à :

- un **site**, un **domaine**, ou (le plus courant) une **OU**

Et elle s'applique à **tous les objets de ce conteneur et des OU en dessous** (héritage). D'où l'importance de la structure d'OU vue au Ch.22 : **c'est elle qui détermine qui reçoit quelles GPO**.

L'ordre d'application (le dernier gagne en cas de conflit) suit l'acronyme **LSDOU** : **L**ocal → **S**ite → **D**omaine → **OU** (de la plus haute à la plus basse). Une GPO liée à une OU proche de l'objet l'emporte donc sur une GPO de domaine.

### Les modificateurs d'héritage

Trois mécanismes altèrent cet ordre — à connaître pour comprendre ce qui s'applique vraiment :

| Mécanisme | Effet |
|-----------|-------|
| **Enforced** (Appliqué) | Force la GPO à gagner, même sur les OU enfants qui bloquent l'héritage |
| **Block Inheritance** (Bloquer l'héritage) | Une OU refuse les GPO héritées des niveaux supérieurs (sauf Enforced) |
| **Security Filtering** | Restreint l'application de la GPO à certains utilisateurs/groupes seulement |
| **WMI Filtering** | Applique la GPO seulement si une condition WMI est vraie (ex : « seulement les portables ») |

### Les cmdlets GPO `[🖥️ Server]` `[🔑 Admin]`

Elles viennent du module **GroupPolicy** (présent sur un DC ou via RSAT) :

```powershell
Import-Module GroupPolicy

Get-GPO -All                          # lister toutes les GPO
Get-GPO -Name "Politique Mot de Passe"

New-GPO -Name "Restrictions USB" -Comment "Bloque les clés USB"    # créer (vide)

# Lier une GPO à une OU (c'est le lien qui la rend active)
New-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local"

# Modifier un lien (ordre, activation, enforced)
Set-GPLink -Name "Restrictions USB" -Target "OU=Postes,DC=lab,DC=local" -Enforced Yes

Remove-GPO -Name "Restrictions USB"   # supprimer
```


> **📌 Le piège du débutant :** `New-GPO` crée une GPO **vide et non liée** — elle ne fait rien. Il faut ensuite (1) **configurer** ses réglages (souvent via la console graphique GPMC, car PowerShell ne couvre pas tous les réglages nativement) et (2) la **lier** à une OU avec `New-GPLink`. Créer ≠ appliquer.

## 🟡 Très utile en pratique

### Documenter et sauvegarder les GPO

```powershell
# Générer un rapport HTML lisible d'une GPO (ce qu'elle contient)
Get-GPOReport -Name "Politique Mot de Passe" -ReportType Html -Path "C:\rapports\GPO_MDP.html"

# Rapport de TOUTES les GPO
Get-GPOReport -All -ReportType Html -Path "C:\rapports\Toutes_GPO.html"

# Sauvegarder / restaurer (indispensable avant toute modification)
Backup-GPO -All -Path "C:\backup\gpo"
Restore-GPO -Name "Politique Mot de Passe" -Path "C:\backup\gpo"
```


> **📌 Discipline `Get`/backup avant modification :** avant de toucher à une GPO, on la **sauvegarde** (`Backup-GPO`) et on **documente** l'existant (`Get-GPOReport`). Une GPO mal réglée peut affecter des milliers de postes d'un coup.

### Diagnostiquer ce qui s'applique réellement : RSOP

La question fréquente « pourquoi ce réglage ne s'applique-t-il pas ? » se résout avec le **Resultant Set of Policy** — l'ensemble des stratégies effectivement appliquées à un utilisateur/ordinateur :

```powershell
# Rapport RSOP pour un utilisateur sur une machine
Get-GPResultantSetOfPolicy -User lab\jdupont -Computer CLIENT01 -ReportType Html -Path "C:\rapports\rsop.html"

# En ligne de commande rapide (sur la machine cible)
gpresult /r                    # résumé des GPO appliquées
gpresult /h rsop.html          # rapport HTML complet

# Forcer la réapplication immédiate des GPO
gpupdate /force
```


## 🔴 Bonus

### Les limites de PowerShell pour les GPO

PowerShell gère très bien le **cycle de vie** des GPO (créer, lier, sauvegarder, rapporter, déléguer). Mais **modifier le contenu** d'une GPO (les milliers de réglages individuels) est partiellement couvert : `Set-GPRegistryValue` permet de piloter les réglages basés sur le registre, mais beaucoup de réglages passent encore par la console graphique (GPMC) ou des modèles ADMX. C'est une limite à connaître : PowerShell orchestre, la GPMC affine.

```powershell
# Exemple de réglage basé sur le registre via PowerShell
Set-GPRegistryValue -Name "Restrictions USB" `
    -Key "HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR" `
    -ValueName "Start" -Type DWord -Value 4
```


## ❌ Erreur classique

```powershell
# Croire que New-GPO applique quelque chose
New-GPO -Name "X"           # ❌ crée une GPO VIDE et NON LIÉE (sans effet)
# → il faut la configurer PUIS New-GPLink vers une OU

# Modifier une GPO sans sauvegarde
Set-GPRegistryValue ...     # ❌ sans filet
Backup-GPO -Name "X" -Path C:\backup ; Set-GPRegistryValue ...   # ✅

# Ne pas comprendre pourquoi une GPO ne s'applique pas
# → vérifier : lien actif ? Block Inheritance ? Security Filtering ? → RSOP / gpresult
```


## 💡 Exercices

**Guidé :** Liste toutes les GPO du domaine, puis génère un rapport HTML de l'une d'elles avec `Get-GPOReport`.

**Autonome :** Crée une GPO de test, lie-la à une OU, sauvegarde-la avec `Backup-GPO`, génère son rapport, puis nettoie (supprime le lien et la GPO).

## ✅ Tu sais maintenant...

- Le **modèle** GPO (Computer/User Config, lien, héritage LSDOU, Enforced, Block Inheritance, filtres)
- Piloter le cycle de vie des GPO (`Get`/`New`/`Remove-GPO`, `New`/`Set-GPLink`)
- Documenter (`Get-GPOReport`) et sauvegarder (`Backup`/`Restore-GPO`)
- Diagnostiquer l'application réelle (RSOP, `gpresult`, `gpupdate`)
- Que `New-GPO` ne suffit pas (créer ≠ configurer ≠ lier) et les limites de PowerShell

## 💬 Questions d'entretien typiques

- **Que fait `New-GPO` exactement ?** → Crée une GPO vide et non liée ; il faut la configurer puis la lier à une OU pour qu'elle s'applique.
- **Dans quel ordre les GPO s'appliquent-elles ?** → LSDOU : Local, Site, Domaine, OU — la dernière (OU la plus proche) l'emporte, sauf Enforced.
- **Comment savoir quelles GPO s'appliquent à un poste ?** → RSOP (`Get-GPResultantSetOfPolicy`) ou `gpresult /r` sur la machine.
- **Que faire avant de modifier une GPO ?** → La sauvegarder (`Backup-GPO`) et documenter l'existant (`Get-GPOReport`).

---
