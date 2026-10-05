---
title: "Tâches planifiées"
cours:
  - library/it/windows/powershell/index.md
---

# Tâches planifiées

Lister les tâches et voir ce qu'elles lancent ; créer une tâche ; désactiver ou supprimer une tâche.

Les incontournables : `Get-ScheduledTask` · `Register-ScheduledTask` · `schtasks /query` · `Disable-ScheduledTask`
{ .kw-cs-top }

### Lister les tâches et ce qu'elles lancent

```powershell title="Commande"
Get-ScheduledTask | Select-Object TaskPath, TaskName, State, @{n='Action';e={$_.Actions.Execute + ' ' + $_.Actions.Arguments}}
```

```powershell title="Exemple"
Get-ScheduledTask | Where-Object TaskPath -notlike '\Microsoft\*' |
    Select-Object TaskName, State, @{n='Action';e={$_.Actions.Execute + ' ' + $_.Actions.Arguments}}
```

??? example "Sortie"
    ```text
    TaskName              State Action
    --------              ----- ------
    GoogleUpdateTaskUser  Ready C:\Users\alice\AppData\Local\Google\Update\GoogleUpdate.exe /ua
    WindowsUpdateCheck    Ready powershell.exe -nop -w hidden -enc SQBFAFgA…
    ```

Une tâche hors de `\Microsoft\` qui lance PowerShell masqué et encodé mérite un examen immédiat.

```bat title="Exemple 2"
schtasks /query /fo LIST /v | findstr /i "TaskName Exécuter Auteur"
```

### Voir quand une tâche a tourné

```powershell title="Commande"
Get-ScheduledTaskInfo -TaskName <nom> [-TaskPath <chemin>]
```

```powershell title="Exemple"
Get-ScheduledTaskInfo -TaskName WindowsUpdateCheck | Select-Object LastRunTime, LastTaskResult, NextRunTime
```

??? example "Sortie"
    ```text
    LastRunTime          LastTaskResult NextRunTime
    -----------          -------------- -----------
    02/10/2026 09:00:01               0 02/10/2026 10:00:00
    ```

Les fichiers de définition sont dans `C:\Windows\System32\Tasks` ; la création est journalisée en 4698 (audit) et dans `Microsoft-Windows-TaskScheduler/Operational` (106).

Pour comprendre : [Journaux des tâches planifiées (4698, 106, 200/201, 4702, 4699)](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/06-taches-planifiees.md) · [retracer la vie d'une tâche](../fondamentaux/logs/persistance.md#retracer-la-vie-dune-tache-planifiee)
{ .kw-cs-meta }

### Créer une tâche planifiée

```powershell title="Commande"
$a = New-ScheduledTaskAction -Execute '<programme>' -Argument '<arguments>'
$t = New-ScheduledTaskTrigger -Daily -At <heure>
Register-ScheduledTask -TaskName '<nom>' -Action $a -Trigger $t -User '<compte>' -RunLevel Limited
```

```powershell title="Exemple"
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-NoProfile -File C:\Scripts\nettoyage-temp.ps1'
$t = New-ScheduledTaskTrigger -Daily -At 22:00
Register-ScheduledTask -TaskName 'Nettoyage Temp' -Action $a -Trigger $t -User 'NT AUTHORITY\LocalService'
```

```bat title="Exemple 2"
schtasks /create /tn "Nettoyage Temp" /tr "powershell.exe -NoProfile -File C:\Scripts\nettoyage-temp.ps1" /sc daily /st 22:00 /ru "NT AUTHORITY\LocalService"
```

!!! warning "Attention"
    Le script appelé doit être dans un dossier que seuls les administrateurs peuvent modifier : sinon, n'importe qui peut changer ce que la tâche exécute avec ses droits.

### Désactiver ou supprimer une tâche

```powershell title="Commande"
Disable-ScheduledTask -TaskName <nom>
Unregister-ScheduledTask -TaskName <nom> -Confirm:$false
```

```bat title="Exemple"
schtasks /change /tn "WindowsUpdateCheck" /disable
```

En réponse à incident : exporter d'abord la définition (`Export-ScheduledTask -TaskName <nom> > tache.xml`), puis désactiver.

Pour comprendre : [PowerShell, ch. 13 (tâches planifiées)](../../../library/it/windows/powershell/02-partie-ii-administration-windows-locale/05-chapitre-13-taches-planifiees.md)
{ .kw-cs-meta }
