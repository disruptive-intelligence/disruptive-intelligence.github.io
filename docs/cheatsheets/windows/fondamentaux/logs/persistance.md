---
title: "Services, tâches et comptes"
---

# Services, tâches et comptes

Ce qu'un attaquant installe pour rester : services, tâches planifiées, comptes créés ou ajoutés à un groupe d'administration.

Les incontournables : `7045` · `4697` · `4698` · `TaskScheduler/Operational` · `4720` · `4732`
{ .kw-cs-top }

## Services et tâches planifiées

### Retrouver les services installés ou modifiés

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Service Control Manager'; Id=7045,7040,7036}   # installé, démarrage modifié, état changé
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4697}                                                  # service installé (si l'audit est activé)
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7045} -MaxEvents 2 | Select-Object TimeCreated, Message | Format-List
```

??? example "Sortie"
    ```text
    TimeCreated : 01/10/2026 23:12:40
    Message     : Un service a été installé sur le système.
                  Nom du service :  WindowsUpdateCritical
                  Nom du fichier du service :  C:\Users\alice\Documents\Windows Update.exe
                  Type de service :  service en mode utilisateur
                  Type de démarrage du service :  démarrage automatique
                  Compte du service :  LocalSystem
    ```

```powershell title="Exemple 2"
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7040} -MaxEvents 5 | Select-Object TimeCreated, Message   # type de démarrage changé (ex. antivirus passé en « désactivé »)
```

| Event ID | Journal | Ce qu'il dit |
|---|---|---|
| **7045** | Journaux Windows → System (Service Control Manager) | Service installé : nom, binaire, type de démarrage, compte |
| **4697** | Journaux Windows → Security | Même information, si l'audit est activé : complète le 7045 |
| **7040** | Journaux Windows → System | Type de démarrage modifié (manuel → automatique : persistance ; automatique → désactivé : antivirus ou EDR neutralisé) |
| **7036** | Journaux Windows → System | Service démarré ou arrêté |

À regarder dans un 7045 : un **nom qui imite Windows** + un **binaire dans un dossier inscriptible par l'utilisateur** (`Documents`, `%TEMP%`, `%APPDATA%`, `C:\Users\Public`) + un **démarrage automatique** + le compte **LocalSystem** = investigation prioritaire. Le champ « type de service » dit comment le service s'exécute, pas qui l'a installé.

Pour comprendre : [Services Windows : 7045, binaire, compte, 7040, 7036](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/07-services-windows.md) · [Corrélation 7045 → 4688 → 7036 → C2](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/07-services-windows.md#correlation-recommandee-services) — Ensuite : [voir le binaire, le compte et le mode de démarrage d'un service](../processus.md#voir-le-binaire-le-compte-et-le-mode-de-demarrage-dun-service)
{ .kw-cs-meta }

### Retracer la vie d'une tâche planifiée

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4698,4699,4700,4701,4702}   # créée, supprimée, activée, désactivée, modifiée (audit requis)
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TaskScheduler/Operational'; Id=106,140,141,200,201}   # enregistrée, modifiée, supprimée, action lancée, terminée
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-TaskScheduler/Operational'; Id=106,140,141,200,201} -MaxEvents 5 |
    Select-Object TimeCreated, Id, @{n='Message';e={($_.Message -split "`r?`n")[0]}}
```

??? example "Sortie"
    ```text
    TimeCreated          Id Message
    -----------          -- -------
    02/10/2026 15:47:02 141 L'utilisateur « MERIDIAN\alice » a supprimé la tâche « \Windows Update Task ».
    02/10/2026 12:03:10 140 L'utilisateur « MERIDIAN\alice » a mis à jour la tâche « \Windows Update Task ».
    02/10/2026 10:15:04 201 Le Planificateur de tâches a terminé l'action « powershell.exe » de la tâche « \Windows Update Task ».
    02/10/2026 10:15:01 200 Le Planificateur de tâches a lancé l'action « powershell.exe » de la tâche « \Windows Update Task ».
    02/10/2026 10:14:22 106 L'utilisateur « MERIDIAN\alice » a inscrit la tâche « \Windows Update Task ».
    ```

Une tâche supprimée a disparu du système, pas des journaux. Le 4698 donne l'auteur, le déclencheur, le compte et la commande ; 200/201 prouvent que l'action a réellement tourné ; comparer 4698 et 4702 montre ce qui a été modifié.

Pour comprendre : [Journaux des tâches planifiées : 4698, 106, 200/201, 4702, 4699 et chronologie d'une tâche malveillante](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/06-taches-planifiees.md) — Voir aussi : [lister les tâches et ce qu'elles lancent](../../administration/taches.md#lister-les-taches-et-ce-quelles-lancent)
{ .kw-cs-meta }

## Comptes et groupes

### Retracer la création d'un compte et ses privilèges

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720,4722,4725,4726,4738}        # compte créé, activé, désactivé, supprimé, modifié
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4732,4728,4756,4733,4729,4757}   # ajouté à / retiré d'un groupe local, global, universel
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4720,4732} -MaxEvents 10 |
    Select-Object TimeCreated, Id, @{n='Auteur';e={$_.Properties[$(if ($_.Id -eq 4720) {4} else {6})].Value}},
                  @{n='Compte ou groupe';e={$_.Properties[$(if ($_.Id -eq 4720) {0} else {2})].Value}}   # 4720 : compte créé ; 4732 : groupe
```

??? example "Sortie"
    ```text
    TimeCreated            Id Auteur Compte ou groupe
    -----------            -- ------ ----------------
    02/10/2026 14:03:11  4732 alice  Administrateurs
    02/10/2026 14:02:47  4720 alice  backupsvc
    ```

```powershell title="Exemple 2"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} | Where-Object { $_.Properties[5].Value -eq 'backupsvc' } |
    Select-Object -First 3 TimeCreated, @{n='Type';e={$_.Properties[8].Value}}   # le nouveau compte s'est-il connecté, et comment ?
```

| Event ID | Ce qu'il dit |
|---|---|
| **4720** | Compte créé : **Subject** = qui l'a créé, **New Account** = le compte créé |
| **4732** / **4728** / **4756** | Membre ajouté à un groupe local / global / universel (**4728** + Domain Admins = enquête critique) |
| **4722** / **4738** | Compte réactivé / modifié (un compte dormant réactivé puis utilisé est suspect) |
| **4723** / **4724** | Mot de passe changé / réinitialisé |
| **4725** / **4726** | Compte désactivé / supprimé (créé → utilisé → supprimé : nettoyage) |
| **4733** / **4729** / **4757** | Membre retiré d'un groupe local / global / universel |

À regarder : un **4720** suivi de près d'un **4732** vers Administrateurs, puis d'un **4624** du même compte = persistance avec accès privilégié. Ne pas confondre l'auteur (**Subject**) et le compte qui reçoit les droits (**Target / Member**). Ces événements demandent l'audit « Gestion des comptes d'utilisateur » et « Gestion des groupes de sécurité » (`auditpol /get /category:"Gestion des comptes"`).

Pour comprendre : [Gestion des comptes : 4720, 4732, cycle de vie d'un compte et patterns SOC](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/08-gestion-des-comptes.md) — Voir aussi : [retrouver les ouvertures de session](sessions-rdp.md#retrouver-les-ouvertures-de-session)
{ .kw-cs-meta }

## Vue d'ensemble

| Thème | Event ID | Journal | Signification |
|---|---|---|---|
| Services | **7045** | Journaux Windows → System | Service installé (nom, binaire, démarrage, compte) |
| Services | **4697** | Journaux Windows → Security (si l'audit est activé) | Service installé |
| Services | **7040** | Journaux Windows → System | Type de démarrage modifié |
| Services | **7036** | Journaux Windows → System | Service démarré / arrêté |
| Tâches | **4698** / **4702** / **4699** | Journaux Windows → Security (si l'audit est activé) | Tâche créée / modifiée / supprimée |
| Tâches | **4700** / **4701** | Journaux Windows → Security (si l'audit est activé) | Tâche activée / désactivée |
| Tâches | **106** / **140** / **141** | Journaux des applications et des services → Microsoft → Windows → TaskScheduler → Operational | Tâche enregistrée / modifiée / supprimée |
| Tâches | **200** / **201** | Journaux des applications et des services → Microsoft → Windows → TaskScheduler → Operational | Action lancée / terminée : la tâche a vraiment tourné |
| Comptes | **4720** / **4726** | Journaux Windows → Security | Compte créé / supprimé |
| Comptes | **4722** / **4725** / **4738** | Journaux Windows → Security | Compte réactivé / désactivé / modifié |
| Comptes | **4723** / **4724** | Journaux Windows → Security | Mot de passe changé / réinitialisé |
| Groupes | **4732** / **4728** / **4756** | Journaux Windows → Security | Membre ajouté à un groupe local / global / universel |
| Groupes | **4733** / **4729** / **4757** | Journaux Windows → Security | Membre retiré d'un groupe local / global / universel |

Patterns : 7045 avec un binaire dans un dossier inscriptible + démarrage automatique + LocalSystem ; 4698 puis 200/201 puis 4699 (tâche créée, exécutée, effacée) ; 4720 → 4732 Administrateurs → 4624 du nouveau compte.
