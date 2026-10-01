---
title: Chapitre 22 — Ordinateurs et unités d'organisation
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### Les comptes ordinateurs

Chaque machine jointe au domaine possède un **compte ordinateur** dans AD — comme les utilisateurs, mais pour les machines. On les gère avec `*-ADComputer`.

```powershell
Get-ADComputer -Identity "CLIENT01"
Get-ADComputer -Filter * | Select-Object Name, Enabled, OperatingSystem

# Avec des attributs utiles
Get-ADComputer -Filter * -Properties OperatingSystem, LastLogonDate |
    Select-Object Name, OperatingSystem, LastLogonDate
```


> **📌 Réflexe `Get-Member` :** `Get-ADComputer CLIENT01 -Properties * | Get-Member` révèle `OperatingSystem`, `OperatingSystemVersion`, `LastLogonDate`, `IPv4Address`, `Enabled`, `DistinguishedName`.

### Le cas d'usage : inventaire du parc machines

```powershell
# Inventaire des OS présents dans le domaine
Get-ADComputer -Filter * -Properties OperatingSystem |
    Group-Object OperatingSystem |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```


`Group-Object` regroupe les machines par OS et les compte — un inventaire instantané, très parlant pour repérer des OS obsolètes (ex : Windows 7 encore présent).

### Repérer les machines obsolètes ou inactives

```powershell
# Ordinateurs inactifs depuis 90 jours (rappel : LastLogonDate approximatif, Ch.20)
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -ComputersOnly |
    Select-Object Name, LastLogonDate
```


### Désactiver / supprimer un compte ordinateur `[🔑 Admin]`

```powershell
Disable-ADAccount -Identity "CLIENT01$"          # noter le $ pour un compte machine
Remove-ADComputer -Identity "CLIENT01" -Confirm:$false
```


> **Note :** le nom de compte machine se termine par `$` (ex : `CLIENT01$`). `Get-ADComputer` accepte le nom sans `$`, mais certaines opérations bas niveau l'exigent.

## 🟡 Les unités d'organisation (OU)

### À quoi servent les OU

Une **OU** (Organizational Unit) est un conteneur qui **range** les objets AD. Elle a deux rôles majeurs :

1. **Organiser** : ranger les objets par service, site, type (`OU=IT`, `OU=Compta`, `OU=Serveurs`)
2. **Cibler les GPO** : on lie une stratégie de groupe à une OU pour l'appliquer à tous ses objets (Ch.25)

Ce deuxième rôle est fondamental : la structure d'OU **conditionne** l'application des GPO.

### Lister et créer des OU `[🔑 Admin]`

```powershell
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName

New-ADOrganizationalUnit -Name "Comptabilité" -Path "OU=Services,DC=lab,DC=local"
```


> **Bonne pratique :** par défaut, une OU créée avec PowerShell est **protégée contre la suppression accidentelle** (`ProtectedFromAccidentalDeletion = $true`). C'est voulu : ça évite d'effacer d'un coup une OU pleine d'objets. Pour supprimer une OU, il faut d'abord retirer cette protection.

### Déplacer un objet : `Move-ADObject` `[🔑 Admin]`

Déplacer un objet le range dans une autre OU — et donc change les GPO qui s'y appliquent :

```powershell
# Déplacer un utilisateur vers l'OU Comptabilité
$dn = (Get-ADUser jdupont).DistinguishedName
Move-ADObject -Identity $dn -TargetPath "OU=Comptabilité,OU=Services,DC=lab,DC=local"
```


> **Cas concret (départ d'un employé) :** on désactive le compte, puis on le **déplace** vers une OU « Départs » (souvent liée à une GPO restrictive). Déplacer + désactiver plutôt que supprimer, c'est la procédure propre.

## 🔴 Bonus

### Retirer la protection avant suppression d'une OU

```powershell
Set-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" `
    -ProtectedFromAccidentalDeletion $false
Remove-ADOrganizationalUnit -Identity "OU=Obsolete,DC=lab,DC=local" -Confirm:$false
```


## ❌ Erreur classique

```powershell
# Essayer de supprimer une OU protégée directement
Remove-ADOrganizationalUnit "OU=X,..."    # ❌ échoue si protégée
# → retirer d'abord ProtectedFromAccidentalDeletion (voir bonus)

# Oublier que déplacer un objet change les GPO appliquées
Move-ADObject ...    # ⚠️ conséquence : nouvelles stratégies, nouveaux droits

# Confondre le conteneur "Computers" (par défaut) et une vraie OU
# Les objets du conteneur CN=Computers ne reçoivent pas les GPO liées aux OU
```


## 💡 Exercices

**Guidé :** Fais l'inventaire des systèmes d'exploitation des ordinateurs du domaine avec `Group-Object`. Identifie le plus répandu.

**Autonome :** Crée une OU `OU=Test`, crée un utilisateur dedans, déplace-le vers une autre OU avec `Move-ADObject`, vérifie son nouveau DN, puis nettoie (retire la protection et supprime l'OU).

## ✅ Tu sais maintenant...

- Gérer les comptes ordinateurs (`*-ADComputer`) et inventorier le parc (`Group-Object` par OS)
- Repérer machines obsolètes/inactives
- Le rôle double des **OU** (organiser + cibler les GPO)
- Créer des OU, déplacer des objets (`Move-ADObject`) et l'impact sur les GPO
- La protection contre la suppression accidentelle

## 💬 Questions d'entretien typiques

- **À quoi sert une OU ?** → Ranger les objets AD et servir de cible aux GPO (la structure d'OU conditionne les stratégies appliquées).
- **Que se passe-t-il quand on déplace un objet d'OU ?** → Il reçoit les GPO liées à sa nouvelle OU — ses stratégies et droits peuvent changer.
- **Comment inventorier les OS du parc ?** → `Get-ADComputer -Properties OperatingSystem | Group-Object OperatingSystem`.
- **Pourquoi une OU ne se supprime-t-elle pas directement ?** → Protection contre la suppression accidentelle activée par défaut ; il faut la retirer d'abord.

---
