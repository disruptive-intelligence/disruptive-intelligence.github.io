---
title: "Defender et protections du système"
cours:
  - library/cyber/hardening/securite-systeme-windows/index.md
---

# Defender et protections du système

Vérifier que chaque composant de Microsoft Defender est réellement actif et verrouillé, surveiller les exclusions, ajouter les règles de réduction de la surface d'attaque (ASR) et la protection des dossiers contre les rançongiciels ; puis les protections du système : atténuations d'exploits, intégrité de la mémoire (HVCI), liste de blocage des pilotes vulnérables.

Les incontournables : `Get-MpComputerStatus` · `Get-MpPreference` · `Set-MpPreference` · `Add-MpPreference` · `Get-ProcessMitigation` · `Win32_DeviceGuard`
{ .kw-cs-top }

```text
Microsoft Defender Antivirus   → prévention et détection de logiciels malveillants
Pare-feu Windows Defender      → contrôle du trafic (fiche Réseau)
Microsoft Defender for Endpoint (ou un autre EDR) → détection comportementale, investigation, réponse
```

Un antivirus ne remplace ni le pare-feu, ni l'EDR, ni les correctifs, ni le moindre privilège : ces contrôles se complètent.

## Microsoft Defender

![[cheatsheets/windows/administration/logiciels#Voir l'état de Microsoft Defender]]

### Verrouiller Defender contre la désactivation (protection contre les falsifications)

Un attaquant administrateur commence souvent par couper la protection en temps réel ou ajouter une exclusion. La protection contre les falsifications (*Tamper Protection*) empêche ces changements, même par un administrateur local ou PowerShell.

```powershell title="Vérifier"
Get-MpComputerStatus | Select-Object IsTamperProtected, RealTimeProtectionEnabled
```

Elle s'active dans *Sécurité Windows → Protection contre les virus et menaces → Gérer les paramètres → Protection contre les falsifications*, ou de façon centrale par Intune / Defender for Endpoint (pas par PowerShell ni par GPO locale). `False` sur un poste géré : à investiguer.

Pour comprendre : [Fiche cyber, Windows Defender](../../../library/it/windows/windows-fiche-cyber/11-approfondir-uac-et-protections.md) · [Analyse des journaux, altération de Defender (5001, 5007)](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/11-windows-defender.md) — Ajout hors cours : où l'activer
{ .kw-cs-meta }

### Garder la protection cloud et l'envoi d'échantillons

La protection cloud consulte Microsoft pour un fichier ou un comportement inconnu : détection plus rapide des menaces récentes. L'envoi automatique d'échantillons l'alimente ; une organisation peut le limiter pour des raisons de confidentialité, mais **par politique**, pas en le coupant au hasard.

```powershell title="Vérifier"
Get-MpPreference | Select-Object DisableRealtimeMonitoring, MAPSReporting, SubmitSamplesConsent, PUAProtection
```

| Valeur | Attendu |
|---|---|
| `DisableRealtimeMonitoring` | `False` |
| `MAPSReporting` (protection cloud) | `2` (avancée) ; `0` = coupée |
| `SubmitSamplesConsent` | `1` (échantillons sûrs) ou `3` (tous), selon la politique ; `2` = jamais |
| `PUAProtection` (applications potentiellement indésirables) | `1` (bloquer) |

Pour comprendre : [Sécurité système Windows, Microsoft Defender Antivirus](../../../library/cyber/hardening/securite-systeme-windows/06-protection-antivirus-anti-malware-et-contre-les-me.md#cloud-delivered-protection) — Ajout hors cours : les noms des valeurs et `PUAProtection`
{ .kw-cs-meta }

![[cheatsheets/windows/administration/logiciels#Voir les exclusions de Defender]]

Une exclusion ajoutée laisse un événement 5007 (*Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational*), une protection coupée un 5001. Retirer une exclusion injustifiée : `Remove-MpPreference -ExclusionPath "<dossier>"`.
{ .kw-cs-meta }

![[cheatsheets/windows/administration/logiciels#Mettre à jour les signatures et lancer une analyse]]

## Réduction de la surface d'attaque

### Activer les règles de réduction de la surface d'attaque (ASR)

Les règles ASR bloquent des **comportements** même quand le code s'exécute : Office qui lance un processus enfant, macro qui appelle l'API Win32, script obfusqué, vol d'identifiants dans LSASS, exécutable téléchargé par un script. Toujours en **audit** d'abord, puis en blocage règle par règle.

```powershell title="Vérifier"
$p = Get-MpPreference
for ($i = 0; $i -lt $p.AttackSurfaceReductionRules_Ids.Count; $i++) {
    [PSCustomObject]@{ Regle = $p.AttackSurfaceReductionRules_Ids[$i]; Action = $p.AttackSurfaceReductionRules_Actions[$i] }
}
```

```powershell title="Appliquer — en audit"
Add-MpPreference -AttackSurfaceReductionRules_Ids <GUID> -AttackSurfaceReductionRules_Actions AuditMode
```

```powershell title="Exemple — bloquer les processus enfants d'Office"
Add-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC-AADC-AD5F3C50688A -AttackSurfaceReductionRules_Actions Enabled
```

| GUID | Règle |
|---|---|
| `D4F940AB-401B-4EFC-AADC-AD5F3C50688A` | Bloquer la création de processus enfants par les applications Office |
| `9E6C4E1F-7D60-472F-BA1A-A39EF669E4B2` | Bloquer le vol d'identifiants depuis LSASS |
| `92E97FA1-2EDF-4476-BDD6-9DD0B4DDDC7B` | Bloquer les appels d'API Win32 depuis les macros Office |
| `5BEB7EFE-FD9A-4556-801D-275E5FFC04CC` | Bloquer l'exécution de scripts potentiellement obfusqués |
| `D3E037E1-3EB8-44C8-A917-57927947596D` | Bloquer le lancement de contenu exécutable téléchargé par JavaScript ou VBScript |

Action : `0` désactivée, `1` blocage, `2` audit, `6` avertissement. GPO : *Composants Windows → Antivirus Microsoft Defender → Microsoft Defender Exploit Guard → Réduction de la surface d'attaque*. Les décisions sont dans le journal Defender (1121 bloqué, 1122 audit).

Pour comprendre : [Windows en profondeur, ch. 26.3 (règles ASR)](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#263-la-chaine-de-defense-motw-smartscreen-protected-view-asr) · [ch. 27.2 (P1, mesure 12)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#272-p1-sous-trois-mois) — Ajout hors cours : les commandes, les GUID, les événements 1121 et 1122
{ .kw-cs-meta }

### Protéger les dossiers contre les rançongiciels (accès contrôlé aux dossiers)

L'accès contrôlé aux dossiers empêche les applications non approuvées de modifier Documents, Images, Vidéos et les dossiers ajoutés. Une application légitime bloquée s'ajoute à la liste des autorisées ; trop d'exceptions vident la protection.

```powershell title="Vérifier"
Get-MpPreference | Select-Object EnableControlledFolderAccess, ControlledFolderAccessProtectedFolders, ControlledFolderAccessAllowedApplications
```

```powershell title="Appliquer"
Set-MpPreference -EnableControlledFolderAccess AuditMode   # puis Enabled une fois les journaux lus
Add-MpPreference -ControlledFolderAccessAllowedApplications "<chemin\application.exe>"
```

`EnableControlledFolderAccess` : `0` désactivé, `1` activé, `2` audit. Interface : *Sécurité Windows → Protection contre les virus et menaces → Protection contre les ransomwares*.

Pour comprendre : [Sécurité système Windows, Controlled Folder Access](../../../library/cyber/hardening/securite-systeme-windows/06-protection-antivirus-anti-malware-et-contre-les-me.md#controlled-folder-access) — Ajout hors cours : les commandes
{ .kw-cs-meta }

## Protections du système

### Vérifier la protection contre les exploits (DEP, ASLR, CFG)

Ces atténuations rendent l'exploitation d'une vulnérabilité plus coûteuse : un exploit moderne doit en contourner plusieurs. Elles sont actives par défaut au niveau du système ; un réglage `OFF` est un écart.

```powershell title="Vérifier"
Get-ProcessMitigation -System
```

```powershell title="Exemple — un programme précis"
Get-ProcessMitigation -Name winword.exe
```

| Atténuation | Contre quoi |
|---|---|
| DEP | Exécution de code injecté dans la pile ou le tas |
| ASLR | Prédiction des adresses en mémoire |
| CFG | Détournement du flux d'exécution |
| CET (*shadow stack*) | Corruption des adresses de retour |

Interface : *Sécurité Windows → Contrôle des applications et du navigateur → Protection contre les exploits*.

Pour comprendre : [Windows en profondeur, ch. 17.5 (mitigations mémoire)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/01-chapitre-17-modele-de-securite-integrite-et-mitiga.md#175-mitigations-memoire-et-code)
{ .kw-cs-meta }

### Activer l'intégrité de la mémoire (HVCI) et la liste de blocage des pilotes vulnérables

Un pilote signé mais vulnérable (*BYOVD*) donne l'accès au noyau : de quoi couper l'EDR ou lire LSASS malgré RunAsPPL. HVCI fait vérifier le code noyau par l'hyperviseur ; la liste de blocage de Microsoft refuse les pilotes vulnérables connus.

```powershell title="Vérifier"
(Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard).SecurityServicesRunning   # contient 2 : HVCI actif
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\CI\Config -Name VulnerableDriverBlocklistEnable -ErrorAction SilentlyContinue
```

Interface : *Sécurité Windows → Sécurité de l'appareil → Isolation du noyau* → **Intégrité de la mémoire** et **Liste de blocage des pilotes vulnérables de Microsoft**. Activer d'abord sur un pilote : un ancien pilote incompatible empêche HVCI de s'activer. Le chargement des pilotes se surveille avec Sysmon 6 et l'événement 7045.

Pour comprendre : [Windows en profondeur, ch. 20.4 (BYOVD)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/04-chapitre-20-detection-moderne-amsi-etw-edr-et-byov.md#204-byovd-bring-your-own-vulnerable-driver) · [ch. 27.3 (P2, mesures 16 et 17)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#273-p2-a-six-mois) — Ajout hors cours : la valeur `VulnerableDriverBlocklistEnable` et le chemin de l'interface
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Composants de Defender | `Get-MpComputerStatus` | `RealTimeProtectionEnabled`, `BehaviorMonitorEnabled`, `OnAccessProtectionEnabled`, `IoavProtectionEnabled` à `True` |
| Signatures | `AntivirusSignatureAge` | 0 ou 1 jour |
| Protection contre les falsifications | `IsTamperProtected` | `True` |
| Protection cloud | `Get-MpPreference` → `MAPSReporting` | `2` |
| Exclusions | `ExclusionPath`, `ExclusionProcess`, `ExclusionExtension` | Aucune injustifiée |
| Règles ASR | `AttackSurfaceReductionRules_Ids` / `_Actions` | Règles en audit puis en blocage |
| Accès contrôlé aux dossiers | `EnableControlledFolderAccess` | `1` (ou `2` le temps de l'audit) |
| Protection contre les exploits | `Get-ProcessMitigation -System` | Aucun `OFF` |
| HVCI | `Win32_DeviceGuard` → `SecurityServicesRunning` | Contient `2` |
| Pilotes vulnérables | `…\Control\CI\Config\VulnerableDriverBlocklistEnable` | `1` |
| EDR | — | Déployé, remonte, protégé contre l'arrêt |

| Événement | Journal | Ce qu'il signale |
|---|---|---|
| 1116 / 1117 | Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational | Menace détectée / action prise |
| 5001 | idem | Protection en temps réel désactivée |
| 5007 | idem | Configuration modifiée (exclusions comprises) |
| 1121 / 1122 | idem | Règle ASR : bloqué / audit |
| 6 | Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | Pilote chargé |

Pour retrouver ces événements : [Pare-feu et Defender](../fondamentaux/logs/pare-feu-defender.md#retracer-les-detections-et-lalteration-de-defender).
