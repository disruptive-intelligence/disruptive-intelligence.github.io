---
title: "Services, droits et persistance"
cours:
  - library/it/windows/windows-fiche-cyber/index.md
---

# Services, droits et persistance

Fermer les mauvaises configurations qui mènent à SYSTEM : services inutiles ou trop privilégiés, chemins sans guillemets, binaires et dossiers modifiables, permissions de service trop larges, dossier inscriptible dans le `PATH` ; puis faire le ménage dans ce qui démarre tout seul.

Les incontournables : `Get-Service` · `Set-Service` · `Win32_Service` · `sc.exe sdshow` · `icacls` · `Get-ScheduledTask`
{ .kw-cs-top }

```text
Service en LocalSystem
→ son binaire est dans un dossier modifiable par un utilisateur
→ le binaire est remplacé
→ au prochain démarrage du service, le programme de l'attaquant tourne en SYSTEM
```

Une élévation de privilèges vient le plus souvent d'une **chaîne** de mauvaises configurations, pas d'une vulnérabilité isolée : ce sont elles qu'on ferme ici.

## Services

### Désactiver les services inutiles

Un service qui ne sert pas reste une porte : il écoute, il tourne avec des droits, il reçoit des correctifs qu'on oublie. Exemples courants : *Registre à distance* (`RemoteRegistry`) si personne n'administre le registre à distance, *Spouleur d'impression* (`Spooler`) sur une machine qui n'imprime pas.

```powershell title="Vérifier"
Get-Service RemoteRegistry, Spooler | Select-Object Name, Status, StartType
Get-Service | Where-Object { $_.StartType -eq 'Automatic' } | Sort-Object Name | Select-Object Name, DisplayName, Status
```

```powershell title="Appliquer"
Stop-Service RemoteRegistry
Set-Service -Name RemoteRegistry -StartupType Disabled
```

Vérifier les dépendances avant de couper (`Get-Service <nom> -DependentServices`) et tester sur un pilote : un service désactivé à tort se voit le lendemain matin.

Ensuite : [changer le mode de démarrage](../administration/services.md#changer-le-mode-de-demarrage) — Pour comprendre : [Windows en profondeur, ch. 5.4 (Remote Registry)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/05-chapitre-5-registre-windows-ruches-et-persistance.md#54-le-registre-en-investigation-et-en-defense) — Ajout hors cours : l'exemple du Spouleur d'impression
{ .kw-cs-meta }

### Faire tourner chaque service avec le moindre privilège

Un service n'a pas à tourner en `LocalSystem` s'il n'en a pas besoin : `LocalService` ou `NetworkService` suffisent souvent, sinon un compte dédié ou un gMSA. Sur chaque service, vérifier le binaire, le compte, le démarrage, les permissions du service, celles du dossier du binaire et les actions de récupération (programme lancé en cas d'échec).

```powershell title="Vérifier"
Get-CimInstance Win32_Service | Where-Object StartName -eq 'LocalSystem' |
    Where-Object PathName -notmatch '\\Windows\\' | Select-Object Name, StartMode, PathName
```

```bat title="Exemple — un service en détail"
sc.exe qc <service>
sc.exe qfailure <service>   :: actions de récupération
```

Ensuite : [voir le binaire, le compte et le démarrage d'un service](../fondamentaux/processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service) — Pour comprendre : [Fiche cyber, permissions de services](../../../library/it/windows/windows-fiche-cyber/08-approfondir-processus-et-services.md) · [Windows en profondeur, ch. 7.1](../../../library/it/windows/windows-en-profondeur/02-partie-ii-processus-execution-et-code.md#71-les-services-windows) — Ajout hors cours : le filtre sur les binaires hors de `\Windows\`, `sc.exe qfailure`
{ .kw-cs-meta }

![[cheatsheets/windows/fondamentaux/processus#Repérer un service mal configuré]]

![[cheatsheets/windows/fondamentaux/processus#Lire les permissions d'un service]]

Le droit le plus dangereux sur un service est `SERVICE_CHANGE_CONFIG` (`DC` en SDDL) : il permet de changer le binaire lancé et le compte d'exécution. Il doit rester à `BA` (administrateurs) et `SY` (SYSTEM).
{ .kw-cs-meta }

## Fichiers et dossiers

![[cheatsheets/windows/fondamentaux/droits#Repérer les permissions trop larges]]

### Retirer l'écriture aux utilisateurs sur un dossier de programme

Les dossiers de programmes, les binaires de services et les scripts lancés par un compte privilégié ne doivent être modifiables que par les administrateurs et SYSTEM.

```bat title="Appliquer"
icacls "<dossier>" /remove:g "<groupe>"
icacls "<dossier>" /grant "<groupe>:(OI)(CI)RX"
```

```bat title="Exemple"
icacls "C:\Program Files\Updater" /remove:g "BUILTIN\Utilisateurs"
icacls "C:\Program Files\Updater" /grant "BUILTIN\Utilisateurs:(OI)(CI)RX"
```

Sauvegarder l'ACL avant (`icacls "<dossier>" /save acl.txt /t`) et travailler par groupes : une erreur peut verrouiller le dossier pour tout le monde. Un droit hérité (`(I)`) se corrige sur le dossier parent.

Ensuite : [accorder ou retirer un droit](../fondamentaux/droits.md#accorder-ou-retirer-un-droit) — Pour comprendre : [Windows en profondeur, ch. 4.5 (permissions NTFS)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/04-chapitre-4-le-systeme-de-fichiers-ntfs.md#45-permissions-ntfs) · [PowerShell, ch. 9 (sauvegarder l'ACL avant)](../../../library/it/windows/powershell/02-partie-ii-administration-windows-locale/01-chapitre-9-fichiers-dossiers-et-permissions-ntfs.md) — Ajout hors cours : `/remove:g` et `/save`
{ .kw-cs-meta }

### Vérifier que le PATH système ne contient pas de dossier inscriptible

Quand un programme est cherché par son nom, Windows parcourt les dossiers du `PATH` dans l'ordre. Un dossier inhabituel et modifiable par un utilisateur, placé dans le `PATH` système, peut faire charger un exécutable ou une DLL à la place du bon par un processus privilégié.

```powershell title="Vérifier"
[Environment]::GetEnvironmentVariable('Path', 'Machine') -split ';' | Where-Object { $_ } |
    ForEach-Object { icacls $_ 2>$null | Select-String -Pattern 'Utilisateurs|Users|Everyone|Tout le monde|Authenticated' }
```

Toute ligne avec `(M)`, `(W)` ou `(F)` pour un groupe large est à corriger, ou le dossier à retirer du `PATH` système. Les DLL système protégées (*Known DLLs*) échappent au détournement de l'ordre de recherche.

Ensuite : [examiner les chemins de recherche](../fondamentaux/systeme.md#examiner-les-chemins-de-recherche-et-de-demarrage) — Pour comprendre : [Élévation de privilèges, PATH Enumeration](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md) · [Windows en profondeur, ch. 7.2 (DLL Search Order)](../../../library/it/windows/windows-en-profondeur/02-partie-ii-processus-execution-et-code.md#72-les-dll) — Ajout hors cours : la boucle `icacls` sur le `PATH`
{ .kw-cs-meta }

## Ce qui démarre tout seul

### Faire le ménage dans ce qui démarre avec la machine

Clés `Run` / `RunOnce`, services, tâches planifiées, dossiers de démarrage, Winlogon, abonnements WMI : chaque entrée inutile est retirée, chaque entrée inconnue est investiguée. **Autoruns** (Sysinternals) les montre toutes ; masquer les entrées Microsoft signées pour voir le reste.

```powershell title="Vérifier"
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike "\Microsoft\*" } |
    Select-Object TaskName, TaskPath, State, @{n='Action';e={$_.Actions.Execute}}
```

```bat title="Exemple — les clés Run"
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

Ensuite : [voir tout ce qui démarre avec la machine](../administration/services.md#voir-tout-ce-qui-demarre-avec-la-machine) · [lister les tâches et ce qu'elles lancent](../administration/taches.md#lister-les-taches-et-ce-quelles-lancent) — Pour comprendre : [Windows en profondeur, ch. 27.3 (P2, mesure 20)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#273-p2-a-six-mois) · [Fiche cyber, persistance et Autoruns](../../../library/it/windows/windows-fiche-cyber/10-approfondir-registre-persistance-et-outils.md)
{ .kw-cs-meta }

### Surveiller les clés de registre sensibles

Les clés de services et de persistance ont des ACL : une permission faible sur la clé d'un service privilégié est une faille. Poser une **SACL** sur les clés sensibles et surveiller leurs modifications (Sysmon 12, 13, 14) : `Run`, `RunOnce`, `Services`, `Winlogon`, liste des *Security Packages* de LSA.

```powershell title="Vérifier — qui peut modifier la clé d'un service"
(Get-Acl "HKLM:\SYSTEM\CurrentControlSet\Services\<service>").Access |
    Where-Object { $_.RegistryRights -match 'FullControl|SetValue|WriteKey' } | Select-Object IdentityReference, RegistryRights
```

Pour comprendre : [Windows en profondeur, ch. 5.4 (le registre en défense)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/05-chapitre-5-registre-windows-ruches-et-persistance.md#54-le-registre-en-investigation-et-en-defense) — Ajout hors cours : la commande `Get-Acl` sur la clé
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Services inutiles | `Get-Service` (`StartType`) | `RemoteRegistry` désactivé s'il ne sert pas ; aucun service sans usage |
| Compte des services | `Win32_Service` → `StartName` | Pas de `LocalSystem` sans besoin |
| Chemins sans guillemets | `Win32_Service` → `PathName` | Tous entre guillemets |
| Dossier du binaire | `icacls "<dossier>"` | Écriture réservée à `Administrateurs` et `SYSTEM` |
| Permissions du service | `sc.exe sdshow <service>` | `DC`, `WD`, `WO` seulement pour `BA` et `SY` |
| Dossiers de programmes | `Get-Acl` (boucle) | Aucun `Modify` / `Write` / `FullControl` pour un groupe large |
| `PATH` système | `icacls` sur chaque dossier | Aucun dossier inscriptible par les utilisateurs |
| Démarrage automatique | Autoruns ; `Win32_StartupCommand` ; tâches hors `\Microsoft\` | Chaque entrée connue et utile |
| Clés sensibles | `Get-Acl HKLM:\…\Services\<service>` ; Sysmon 12-14 | ACL strictes, modifications journalisées |

| Événement | Journal | Ce qu'il signale |
|---|---|---|
| 7045 | Journaux Windows → System | Nouveau service installé |
| 4697 | Journaux Windows → Security | Service installé (si l'audit est activé) |
| 4698 | Journaux Windows → Security | Tâche planifiée créée |
| 12 / 13 / 14 | Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | Clé de registre créée, modifiée, renommée |

Pour retrouver ces événements : [Services, tâches et comptes](../fondamentaux/logs/persistance.md).
