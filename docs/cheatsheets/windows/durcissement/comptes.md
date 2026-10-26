---
title: "Comptes et privilèges"
cours:
  - library/cyber/hardening/securite-systeme-windows/index.md
---

# Comptes et privilèges

Réduire ce qu'un compte compromis permet : peu d'administrateurs, comptes par défaut neutralisés, compte du quotidien sans droits, mots de passe longs et verrouillage, élévation contrôlée, session qui se verrouille, privilèges sensibles réservés.

Les incontournables : `Get-LocalUser` · `Get-LocalGroupMember` · `net accounts` · `secpol.msc` · `whoami /priv` · `secedit /export`
{ .kw-cs-top }

```text
Identité → compte → groupes → permissions / privilèges
Compte du quotidien compromis      → privilèges limités
Compte administrateur compromis    → désactiver les protections, voler des identifiants,
                                     s'installer, rebondir sur d'autres machines
```

Sur un poste joint au domaine, ces réglages se posent par **GPO** (sinon une modification locale les défait) ; les commandes servent à vérifier l'état réel du poste.

## Comptes locaux

### Repérer les comptes locaux à revoir

Un compte activé jamais utilisé, inconnu, ou dont le mot de passe n'expire jamais sans raison écrite est une identité oubliée mais toujours valide.

```powershell title="Vérifier"
Get-LocalUser | Where-Object Enabled |
    Select-Object Name, LastLogon, PasswordExpires, PasswordLastSet | Sort-Object LastLogon
```

```powershell title="Exemple — mots de passe qui n'expirent jamais"
Get-LocalUser | Where-Object { $_.Enabled -and -not $_.PasswordExpires } | Select-Object Name, LastLogon
```

À traiter : désactiver plutôt que supprimer (la suppression perd le SID, donc l'historique des droits), ou documenter pourquoi le compte reste.

Ensuite : [désactiver un compte](../administration/utilisateurs.md#desactiver-reactiver-ou-supprimer-un-compte) — Pour comprendre : [PowerShell, ch. 10 (auditer les comptes locaux)](../../../library/it/windows/powershell/02-partie-ii-administration-windows-locale/02-chapitre-10-utilisateurs-et-groupes-locaux.md)
{ .kw-cs-meta }

### Neutraliser les comptes par défaut (Invité, Administrateur intégré)

`Administrator` (SID en `-500`) et `Guest` (`-501`) existent partout et portent un nom prévisible : cibles évidentes. Le problème vient surtout de leurs privilèges, d'un mot de passe faible ou d'un usage quotidien.

```powershell title="Vérifier"
Get-LocalUser | Where-Object { $_.SID -like "*-500" -or $_.SID -like "*-501" } | Select-Object Name, Enabled, SID
```

```powershell title="Appliquer"
Get-LocalUser | Where-Object { $_.SID -like "*-501" } | Disable-LocalUser    # Invité
```

Le compte `-500` est désactivé par défaut sur les postes récents. S'il reste actif (souvent pour LAPS), son mot de passe doit être unique et renouvelé ; un `-500` activé et renommé mérite une vérification.

Pour comprendre : [Sécurité système Windows, comptes par défaut](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#comptes-par-defaut-default-accounts) — Ajout hors cours : le SID `-501` d'Invité
{ .kw-cs-meta }

## Groupes et administration

### Réduire les administrateurs locaux au strict nécessaire

Un membre du groupe Administrateurs peut installer, désactiver des protections, lire les secrets locaux et s'installer durablement. Un utilisateur standard n'y a pas sa place sans besoin métier.

```powershell title="Vérifier"
Get-LocalGroupMember -SID S-1-5-32-544 | Select-Object Name, ObjectClass, PrincipalSource
```

```powershell title="Appliquer"
Remove-LocalGroupMember -Group "Administrateurs" -Member "<compte>"
```

```powershell title="Exemple — les autres groupes sensibles"
Get-LocalGroupMember -SID S-1-5-32-555   # Utilisateurs du Bureau à distance
Get-LocalGroupMember -SID S-1-5-32-551   # Opérateurs de sauvegarde
```

En parc, l'appartenance au groupe Administrateurs se fixe par GPO (*Groupes restreints*, ou *Préférences → Paramètres du Panneau de configuration → Utilisateurs et groupes locaux*) : sinon un ajout local réintroduit les droits retirés.

Ensuite : [savoir qui est administrateur](../fondamentaux/droits.md#savoir-qui-est-administrateur-de-la-machine) — Pour comprendre : [Sécurité système Windows, admins locaux](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#controle-de-lappartenance-au-groupe-dadmin-locaux) — Ajout hors cours : SID des groupes Bureau à distance et Opérateurs de sauvegarde
{ .kw-cs-meta }

### Séparer le compte du quotidien et le compte d'administration

Messagerie, navigation et bureautique avec un compte **sans droits** ; administration avec un compte dédié, jamais l'inverse. Les droits élevés ne s'accordent que le temps de l'opération (*Just-In-Time*), puis se retirent.

```text title="Modèle"
prenom.nom          → bureautique, messagerie, navigation (aucun droit d'administration)
prenom.nom.adm.t2   → administration des postes
prenom.nom.adm.t1   → administration des serveurs
prenom.nom.adm.t0   → administration de l'AD, depuis un poste d'administration dédié uniquement
```

```bat title="Vérifier — mon compte du quotidien est-il administrateur ?"
whoami /groups | findstr /i "S-1-5-32-544"
```

Une ligne `BUILTIN\Administrateurs` signale un compte administrateur, même non élevé (« Groupe utilisé pour refus uniquement » : jeton filtré par l'UAC). Le poste d'administration (SAW / PAW) n'a ni messagerie ni navigation, peu de logiciels, le MFA et tous les correctifs.

Pour comprendre : [Sécurité système Windows, séparer les comptes et SAW](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#separer-compte-utilisateur-et-compte-administrateur) · [Active Directory, ch. 11 (tiering)](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md)
{ .kw-cs-meta }

### Interdire aux comptes privilégiés de se connecter aux postes

Un administrateur du domaine qui ouvre une session sur un poste y laisse de quoi agir en son nom. Le *tiering* l'en empêche techniquement : un compte d'un niveau ne se connecte qu'aux machines de ce niveau.

```text title="GPO"
Configuration ordinateur → Stratégies → Paramètres Windows → Paramètres de sécurité
→ Stratégies locales → Attribution des droits utilisateur
   Interdire l'ouverture d'une session locale                         (Deny log on locally)
   Interdire l'ouverture de session par les services Bureau à distance (Deny log on through Remote Desktop Services)
   Interdire l'ouverture de session en tant que tâche                  (Deny log on as a batch job)
   Interdire l'ouverture de session en tant que service                (Deny log on as a service)
→ y placer les groupes Tier 0 (Admins du domaine, Administrateurs de l'entreprise…) sur les GPO des postes
```

Pour comprendre : [Active Directory, ch. 11 (les outils du tiering)](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md#114-les-outils-du-tiering)
{ .kw-cs-meta }

## Mots de passe et sessions

### Appliquer une politique de mot de passe et de verrouillage

Longueur minimale `0` ou verrouillage `Jamais` : n'importe quel mot de passe passe et les essais sont illimités. La longueur et le refus des mots de passe connus comptent plus qu'une complexité artificielle ; changer de mot de passe surtout en cas de fuite ou de soupçon, pas à date fixe.

```bat title="Vérifier"
net accounts
```

```bat title="Appliquer (comptes locaux)"
net accounts /minpwlen:12 /uniquepw:24 /lockoutthreshold:10 /lockoutduration:10 /lockoutwindow:10
```

```text title="GPO"
Paramètres de sécurité → Stratégies de comptes → Stratégie de mot de passe
                                               → Stratégie de verrouillage du compte
```

Un seuil de verrouillage trop bas permet à un attaquant de bloquer tous les comptes (déni de service) ; `10` essais sur `10` minutes est la valeur par défaut des Windows 11 récents. Le verrouillage freine les essais de mots de passe, pas la réutilisation d'un hash déjà volé (*Pass-the-Hash*). Sur un poste du domaine, la politique du domaine (`net accounts /domain`) s'applique aux comptes du domaine ; les FGPP imposent plus aux administrateurs et aux comptes de service.

Ensuite : [lire la politique (net accounts)](../fondamentaux/enumeration.md#lire-la-politique-de-mot-de-passe-et-de-verrouillage) — Pour comprendre : [Sécurité système Windows, Password Policy et Account Lockout](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#password-policy-dans-active-directory) · [Active Directory, ch. 24.6](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#246-politiques-de-mots-de-passe) — Ajout hors cours : les options de `net accounts` et les valeurs d'exemple
{ .kw-cs-meta }

### Exiger le MFA pour les accès privilégiés

Un second facteur rend un mot de passe volé insuffisant. Priorité aux comptes d'administration, à l'accès distant et aux consoles sensibles (sauvegardes, EDR, annuaire) : carte à puce + PIN, clé de sécurité, application d'authentification.

Pour comprendre : [Sécurité système Windows, 2FA / MFA et carte à puce](../../../library/cyber/hardening/securite-systeme-windows/01-gestion-des-utilisateurs-et-des-groupes.md#2fa-mfa) · [Fiche MFA](../../../library/cyber/notions/mfa.md)
{ .kw-cs-meta }

### Verrouiller la session après inactivité

Une session ouverte sans surveillance donne l'accès sans mot de passe. Verrouillage automatique, authentification au retour, et le réflexe `Win + L` à chaque départ.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name InactivityTimeoutSecs -ErrorAction SilentlyContinue
```

```text title="GPO"
Paramètres de sécurité → Stratégies locales → Options de sécurité
→ Ouverture de session interactive : limite d'inactivité de l'ordinateur → 900 secondes (15 min)
```

Rien en retour : aucune limite n'est imposée.

Pour comprendre : [Sécurité système Windows, Session Timeout / Screen Lock](../../../library/cyber/hardening/securite-systeme-windows/01-gestion-des-utilisateurs-et-des-groupes.md#session-timeout-screen-lock) — Ajout hors cours : la valeur `InactivityTimeoutSecs` et le paramètre de GPO
{ .kw-cs-meta }

## Élévation et privilèges

### Garder le contrôle de compte d'utilisateur (UAC) actif

L'UAC donne à un administrateur un jeton filtré au quotidien et ne l'élève qu'après confirmation : il freine les élévations involontaires, sans être une frontière de sécurité (des contournements existent). Ne jamais le désactiver ; « Toujours notifier » pour les comptes d'administration.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' |
    Select-Object EnableLUA, ConsentPromptBehaviorAdmin, PromptOnSecureDesktop
```

??? example "Sortie"
    ```text
    EnableLUA ConsentPromptBehaviorAdmin PromptOnSecureDesktop
    --------- -------------------------- ---------------------
            1                          5                     1
    ```

| Niveau UAC | `ConsentPromptBehaviorAdmin` | `PromptOnSecureDesktop` |
|---|---|---|
| Toujours notifier (le plus strict) | `2` | `1` |
| Notifier quand une application tente des changements (défaut) | `5` | `1` |
| Idem, sans assombrir le Bureau (pas de Bureau sécurisé) | `5` | `0` |
| Ne jamais notifier (à proscrire) | `0` | `0` |

`EnableLUA = 0` : UAC désactivé, à corriger. Interface : `UserAccountControlSettings.exe`. GPO : *Options de sécurité → Contrôle de compte d'utilisateur : …*. Une modification de ces valeurs (Sysmon 13) est à surveiller.

Ensuite : [savoir si la session est élevée](../fondamentaux/droits.md#savoir-si-la-session-est-elevee-uac) — Pour comprendre : [Sécurité système Windows, niveaux UAC](../../../library/cyber/hardening/securite-systeme-windows/03-strategie-de-securite-locale-group-policy-et-uac.md#niveaux-uac) · [Windows en profondeur, ch. 17.4](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/01-chapitre-17-modele-de-securite-integrite-et-mitiga.md#174-uac-user-account-control) — Ajout hors cours : les valeurs de registre de chaque niveau
{ .kw-cs-meta }

### Réserver les privilèges sensibles

Certains privilèges suffisent à prendre la machine : `SeDebugPrivilege` (lire la mémoire de tout processus, dont LSASS), `SeImpersonatePrivilege` (attaques « Potato » vers SYSTEM), `SeBackupPrivilege` / `SeRestorePrivilege` (lire ou écrire tout fichier, SAM et NTDS.dit compris), `SeLoadDriverPrivilege` (charger un pilote), `SeTcbPrivilege` (agir comme le système).

```bat title="Vérifier — qui les détient sur la machine"
secedit /export /cfg %TEMP%\droits.inf /areas USER_RIGHTS
findstr /i "SeDebugPrivilege SeImpersonatePrivilege SeBackupPrivilege SeRestorePrivilege SeLoadDriverPrivilege SeTcbPrivilege" %TEMP%\droits.inf
```

??? example "Sortie"
    ```text
    SeBackupPrivilege = *S-1-5-32-544,*S-1-5-32-551
    SeDebugPrivilege = *S-1-5-32-544
    SeImpersonatePrivilege = *S-1-5-19,*S-1-5-20,*S-1-5-32-544,*S-1-5-6
    ```

```bat title="Exemple — dans le jeton courant"
whoami /priv
```

Attendu : `SeDebugPrivilege` aux seuls administrateurs (`S-1-5-32-544`), `SeImpersonatePrivilege` aux administrateurs et comptes de service (`S-1-5-19`, `-20`, `-6`), `SeTcbPrivilege` à personne. Un compte utilisateur ou un compte de service applicatif dans ces listes est à retirer : *Paramètres de sécurité → Stratégies locales → Attribution des droits utilisateur*.

Ensuite : [voir mes privilèges](../fondamentaux/droits.md#voir-mon-sid-mes-groupes-et-mes-privileges) — Pour comprendre : [Windows en profondeur, ch. 19.1 (privilèges)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/03-chapitre-19-privileges-elevation-et-controle-d-exe.md) · [Élévation de privilèges, whoami /priv](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md) — Ajout hors cours : l'export `secedit`
{ .kw-cs-meta }

### Restreindre les comptes de service

Un compte par service, avec les seuls droits utiles, un secret fort et renouvelé (gMSA quand c'est possible), un accès réseau limité, et une surveillance de ses connexions (nouvelle machine source, horaire inhabituel).

```powershell title="Vérifier — sous quel compte tourne chaque service"
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName | Sort-Object StartName
```

| Compte | Droits locaux | Sur le réseau |
|---|---|---|
| `LocalSystem` | Les plus élevés, au-dessus des administrateurs | Compte machine |
| `NetworkService` | Limités | Compte machine |
| `LocalService` | Limités | Anonyme |
| Compte dédié / gMSA | Ceux qu'on lui donne | Le compte (mot de passe géré par l'AD pour le gMSA) |

Un service applicatif en `LocalSystem` sans nécessité, ou sous un compte nominatif d'administrateur, est à revoir : un service mal protégé devient un tremplin vers SYSTEM, et le mot de passe d'un compte de domaine utilisé par un service reste lisible dans les secrets LSA de la machine.

Ensuite : [créer un gMSA](../administration/active-directory/kerberos-dc.md#creer-un-compte-de-service-gere-gmsa) — Pour comprendre : [Sécurité système Windows, gestion des comptes de service](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#gestion-des-comptes-de-service) · [Windows en profondeur, ch. 7.1](../../../library/it/windows/windows-en-profondeur/02-partie-ii-processus-execution-et-code.md#71-les-services-windows)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Comptes locaux à revoir | `Get-LocalUser \| Where-Object Enabled` | Aucun compte inconnu, jamais connecté ou sans expiration injustifiée |
| Invité, Administrateur intégré | `Get-LocalUser` (SID `-501`, `-500`) | Invité désactivé ; `-500` désactivé ou géré par LAPS |
| Administrateurs locaux | `Get-LocalGroupMember -SID S-1-5-32-544` | Le strict nécessaire, fixé par GPO |
| Groupes sensibles | `Get-LocalGroupMember -SID S-1-5-32-555` (RDP), `-551` (sauvegarde) | Vides ou justifiés |
| Compte du quotidien | `whoami /groups \| findstr S-1-5-32-544` | Absent du groupe Administrateurs |
| Comptes privilégiés sur les postes | GPO *Interdire l'ouverture de session…* | Groupes Tier 0 refusés |
| Mots de passe et verrouillage | `net accounts` | Longueur ≥ 12, historique, seuil de verrouillage défini |
| MFA | — | Comptes d'administration et accès distant |
| Verrouillage de session | `InactivityTimeoutSecs` | Défini (par exemple 900 s) |
| UAC | `EnableLUA`, `ConsentPromptBehaviorAdmin` | `1` ; `2` pour les administrateurs, `5` au minimum |
| Privilèges sensibles | `secedit /export /areas USER_RIGHTS` | `SeDebug` aux administrateurs, `SeTcb` à personne |
| Comptes de service | `Win32_Service` → `StartName` | Pas de `LocalSystem` ni de compte d'administrateur sans besoin ; gMSA |

| Chemin de GPO | Contenu |
|---|---|
| Paramètres de sécurité → Stratégies de comptes | Mot de passe, verrouillage |
| Paramètres de sécurité → Stratégies locales → Attribution des droits utilisateur | Privilèges, droits et interdictions d'ouverture de session |
| Paramètres de sécurité → Stratégies locales → Options de sécurité | UAC, comptes Invité / Administrateur, limite d'inactivité |
| Préférences → Utilisateurs et groupes locaux (ou Groupes restreints) | Membres du groupe Administrateurs |
