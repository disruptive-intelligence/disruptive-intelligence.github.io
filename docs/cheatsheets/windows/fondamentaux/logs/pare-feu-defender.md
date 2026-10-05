---
title: "Pare-feu et Defender"
---

# Pare-feu et Defender

Les règles de pare-feu ajoutées ou modifiées, le pare-feu désactivé ; les détections de Defender, sa désactivation et ses exclusions.

Les incontournables : `2004` · `2005` · `2003` · `1116` · `1117` · `5001` · `5007`
{ .kw-cs-top }

## Pare-feu et antivirus

### Retracer les changements du pare-feu

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'; Id=2004,2005,2003}   # règle ajoutée, modifiée ; paramètre global changé
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'; Id=2004; StartTime=(Get-Date).AddHours(-1)} |
    Select-Object -First 2 TimeCreated, Message | Format-List   # la dernière heure seulement : Windows ajoute sans cesse des règles
```

??? example "Sortie"
    ```text
    TimeCreated : 02/10/2026 14:12:05
    Message     : Une règle a été ajoutée à la liste d'exceptions du Pare-feu Windows Defender.
                  Nom de la règle :  Windows Update
                  Direction :  Sortant
                  Chemin d'accès de l'application :  C:\Users\alice\Documents\Windows Update.exe
                  Utilisateur ayant effectué la modification :  MERIDIAN\alice
                  Application ayant effectué la modification :  C:\Windows\System32\mmc.exe
    ```

```powershell title="Exemple 2"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'; Id=2003} |
    Where-Object Message -match 'Enable Windows Defender Firewall|Activer le Pare-feu' | Select-Object -First 5 TimeCreated, Message   # pare-feu désactivé / réactivé
```

| Event ID | Ce qu'il dit |
|---|---|
| **2004** | Règle ajoutée : nom, direction, programme, ports, utilisateur et application à l'origine du changement |
| **2005** | Règle modifiée (le **Rule ID** ne change pas : il retrouve la règle d'origine dans un 2004 antérieur) |
| **2003** | Paramètre global changé (« Enable Windows Defender Firewall » = **No** : pare-feu désactivé) |

À regarder : une règle **sortante** pour un exécutable dans un dossier inscriptible (`Documents`, `%TEMP%`, `C:\Users\Public`), ajoutée par `mmc.exe`, `powershell.exe`, `cmd.exe` ou `netsh.exe` (action humaine ou script) pendant la fenêtre d'incident. **SYSTEM** n'est pas un gage de légitimité. Le trafic autorisé ou refusé n'est pas dans ce journal mais dans `%SystemRoot%\System32\LogFiles\Firewall\pfirewall.log`, si la journalisation est activée.

Pour comprendre : [Pare-feu Windows : 2004, 2005, 2003, Rule ID, dropped packets](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/10-pare-feu-windows.md) — Voir aussi : [voir le profil et l'état du pare-feu](../reseau.md#voir-le-profil-et-letat-du-pare-feu)
{ .kw-cs-meta }

### Retracer les détections et l'altération de Defender

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1116,1117}   # menace détectée, action prise
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; Id=5001,5007}   # protection en temps réel désactivée, configuration changée
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; Id=5007} |
    Where-Object Message -match 'Exclusions\\Paths' | Select-Object -First 3 TimeCreated, Message   # exclusions ajoutées
```

??? example "Sortie"
    ```text
    TimeCreated          Message
    -----------          -------
    02/10/2026 14:01:37  La configuration de Microsoft Defender Antivirus a été modifiée. … Nouvelle valeur : HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths\C:\Users\Public\Tools = 0x0
    ```

| Event ID | Ce qu'il dit |
|---|---|
| **1116** | Menace détectée : nom, gravité, chemin, processus impliqué |
| **1117** | Action prise (quarantaine, suppression…) et son **résultat** : une détection n'est pas une neutralisation |
| **5001** | Protection en temps réel désactivée |
| **5007** | Configuration modifiée ; avec `Exclusions\Paths` : exclusion ajoutée (beaucoup de bruit sinon) |

À regarder : un **5001** ou une exclusion large (profil utilisateur, `C:\Users\Public`, `C:\`) pendant la fenêtre d'incident, puis un exécutable lancé depuis ce chemin (4688). Un 1117 en échec signifie que le fichier peut encore être là.

Pour comprendre : [Windows Defender : 1116, 1117, 5001, 5007 et exclusions](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/11-windows-defender.md) — Voir aussi : [voir les exclusions de Defender](../../administration/logiciels.md#voir-les-exclusions-de-defender)
{ .kw-cs-meta }
