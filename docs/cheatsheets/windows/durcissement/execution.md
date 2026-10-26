---
title: "Exécution et applications"
cours:
  - library/it/windows/powershell/index.md
---

# Exécution et applications

Décider de ce qui a le droit de s'exécuter : contrôle applicatif (AppLocker, App Control / WDAC), PowerShell restreint et signé, chaîne de protection des fichiers téléchargés (Mark of the Web, SmartScreen, macros), logiciels réduits au nécessaire.

Les incontournables : `Get-AppLockerPolicy` · `Test-AppLockerPolicy` · `$ExecutionContext.SessionState.LanguageMode` · `Get-ExecutionPolicy -List` · `Get-AuthenticodeSignature` · `Get-Item -Stream`
{ .kw-cs-top }

## Contrôle applicatif

### Autoriser seulement les programmes prévus (AppLocker)

AppLocker filtre les exécutables, scripts, installeurs (MSI), DLL et applications empaquetées par règles d'**éditeur** (signature), de **chemin** ou de **hash**. Il se contourne (binaires système détournables, chargement latéral de DLL) mais ralentit fortement l'attaquant. Toujours commencer en **mode audit**.

```powershell title="Vérifier"
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections
Get-Service AppIDSvc   # « Identité de l'application » : sans lui, aucune règle n'est appliquée
```

```powershell title="Exemple — tester une décision"
Get-AppLockerPolicy -Effective |
    Test-AppLockerPolicy -Path C:\Windows\System32\cmd.exe -User "$env:USERDOMAIN\$env:USERNAME"
```

```text title="GPO"
Paramètres de sécurité → Stratégies de contrôle de l'application → AppLocker
→ pour chaque collection : Créer des règles par défaut, puis « Configurer l'application des règles » → Auditer uniquement
→ une fois les journaux propres : Appliquer les règles
Services : Identité de l'application (AppIDSvc) → démarrage automatique
```

Une règle de **chemin** sur un dossier où un utilisateur peut écrire annule la protection : c'est le point à vérifier sur les règles par défaut (`%PROGRAMFILES%`, `%WINDIR%` et leurs sous-dossiers inscriptibles). Les décisions sont dans *Journaux des applications et des services → Microsoft → Windows → AppLocker → EXE and DLL* : 8003 (serait bloqué, mode audit), 8004 (bloqué).

Ensuite : [lire et tester la politique AppLocker](../fondamentaux/enumeration.md#lire-et-tester-la-politique-applocker) — Pour comprendre : [Élévation de privilèges, AppLocker](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/02-situational-awareness.md) · [Fiche cyber, AppLocker et WDAC](../../../library/it/windows/windows-fiche-cyber/11-approfondir-uac-et-protections.md) — Ajout hors cours : le service `AppIDSvc`, la GPO, les événements 8003 et 8004
{ .kw-cs-meta }

### Préférer App Control for Business (WDAC) pour un contrôle robuste

App Control (ex-WDAC) s'appuie sur l'intégrité du code du noyau : plus difficile à contourner qu'AppLocker, recommandé par Microsoft pour les nouveaux déploiements, plus exigeant à mettre en place. Même démarche : politique en mode audit, lecture des journaux, puis application.

| Outil | Usage |
|---|---|
| AppLocker | Plus simple à déployer, répandu dans l'existant ; règles par utilisateur ou groupe |
| App Control / WDAC | Plus fort (noyau), adapté aux environnements sensibles ; peut aussi bloquer des pilotes |
| SRP (*Software Restriction Policies*) | Ancien, remplacé par les deux précédents |

Quand l'un des deux est en place, PowerShell passe automatiquement le code non approuvé en *Constrained Language Mode*.

Pour comprendre : [Windows en profondeur, ch. 19.2 (contrôle d'exécution)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/03-chapitre-19-privileges-elevation-et-controle-d-exe.md) · [PowerShell, ch. 35](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md)
{ .kw-cs-meta }

## PowerShell

### Vérifier que PowerShell passe en mode restreint

Le *Constrained Language Mode* retire à PowerShell les appels .NET arbitraires, COM et les types complexes, tout en laissant l'administration courante. Il n'est pas un réglage : il est la **conséquence** du contrôle applicatif sur le code non approuvé.

```powershell title="Vérifier"
$ExecutionContext.SessionState.LanguageMode   # FullLanguage (normal) ou ConstrainedLanguage (restreint)
```

Pour comprendre : [PowerShell, ch. 35 (Constrained Language Mode)](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md#le-constrained-language-mode)
{ .kw-cs-meta }

### Régler la stratégie d'exécution, sans compter dessus

La stratégie d'exécution évite qu'un double-clic lance un script par erreur ; elle se contourne trivialement (`-ExecutionPolicy Bypass`, copier-coller). En entreprise : imposée par GPO, `RemoteSigned` ou `AllSigned` avec des scripts signés.

```powershell title="Vérifier"
Get-ExecutionPolicy -List   # MachinePolicy et UserPolicy = imposées par GPO
```

```text title="GPO"
Modèles d'administration → Composants Windows → Windows PowerShell
→ Activer l'exécution des scripts → Autoriser uniquement les scripts signés (AllSigned)
                                   ou Autoriser les scripts locaux et les scripts signés distants (RemoteSigned)
```

| Stratégie | Effet |
|---|---|
| `Restricted` | Aucun script (défaut sur les postes clients) |
| `RemoteSigned` | Scripts locaux autorisés ; ceux téléchargés doivent être signés |
| `AllSigned` | Tous les scripts doivent être signés |
| `Unrestricted` / `Bypass` | Tout passe : à éviter |

Ne pas mettre `-ExecutionPolicy Bypass` par réflexe dans les tâches planifiées : cela banalise le contournement.

Pour comprendre : [PowerShell, ch. 1 (la politique d'exécution)](../../../library/it/windows/powershell/01-partie-i-fondamentaux-powershell-pour-administrer/01-chapitre-1-powershell-dans-l-ecosysteme-windows.md#la-politique-dexecution-execution-policy) — Ajout hors cours : `-List` et le libellé de la GPO
{ .kw-cs-meta }

### Signer ses scripts d'administration

La signature garantit qu'un script n'a pas été modifié et dit d'où il vient. Avec `AllSigned` imposée par GPO, un script modifié ne passe plus dans les usages normaux.

```powershell title="Appliquer"
$cert = Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert
Set-AuthenticodeSignature -FilePath ".\MonScript.ps1" -Certificate $cert
```

```powershell title="Vérifier"
Get-AuthenticodeSignature ".\MonScript.ps1" | Select-Object Status, SignerCertificate
```

Ensuite : [vérifier la signature d'un exécutable](../fondamentaux/fichiers-recherche.md#verifier-la-signature-dun-executable) — Pour comprendre : [PowerShell, ch. 35 (la signature de scripts)](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md#la-signature-de-scripts)
{ .kw-cs-meta }

### Retirer PowerShell 2.0

PowerShell 2.0 n'a ni journalisation des blocs de script ni AMSI : un attaquant qui lance `powershell -Version 2` échappe à la visibilité installée. Il est retiré des versions récentes (Windows 11 24H2, Windows Server 2025) ; sur les autres, le désactiver.

```powershell title="Vérifier"
Get-WindowsOptionalFeature -Online -FeatureName MicrosoftWindowsPowerShellV2Root | Select-Object FeatureName, State
```

```powershell title="Appliquer"
Disable-WindowsOptionalFeature -Online -FeatureName MicrosoftWindowsPowerShellV2Root -NoRestart
```

Pour comprendre : [PowerShell, ch. 35 (AMSI et journalisation)](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md) — Ajout hors cours : toute l'entrée
{ .kw-cs-meta }

### Laisser AMSI inspecter les scripts

AMSI soumet le code de PowerShell, VBA, JavaScript, WSH et .NET à l'antivirus **au moment de l'exécution**, même chargé en mémoire sans toucher le disque. Actif par défaut avec Defender : ne pas le désactiver, et garder la journalisation 4104, qui enregistre aussi les tentatives de contournement.

Ensuite : [activer la journalisation PowerShell](journalisation.md#activer-la-journalisation-des-scripts-powershell) — Pour comprendre : [Windows en profondeur, ch. 20.1 (AMSI)](../../../library/it/windows/windows-en-profondeur/05-partie-v-modele-de-securite-et-protections/04-chapitre-20-detection-moderne-amsi-etw-edr-et-byov.md#201-amsi-anti-malware-scan-interface)
{ .kw-cs-meta }

## Fichiers téléchargés

La chaîne de défense contre l'hameçonnage, du téléchargement à l'exécution :

```text
Téléchargement → Mark of the Web → SmartScreen → Mode protégé d'Office → blocage des macros → règles ASR
```

Chaque maillon dépend du précédent : un fichier qui perd son marquage (extrait d'une image `.iso` ou de certaines archives) échappe à toute la suite.

### Vérifier qu'un fichier téléchargé porte la Mark of the Web

Windows écrit un flux `Zone.Identifier` sur tout fichier téléchargé ou reçu par messagerie (`ZoneId=3` = Internet) : c'est ce marquage qui déclenche SmartScreen, le mode protégé et le blocage des macros.

```powershell title="Vérifier"
Get-Content <fichier> -Stream Zone.Identifier
```

```powershell title="Exemple"
Get-Content $env:USERPROFILE\Downloads\facture.docx -Stream Zone.Identifier
```

??? example "Sortie"
    ```text
    [ZoneTransfer]
    ZoneId=3
    HostUrl=https://exemple.test/facture.docx
    ```

Retirer la marque (`Unblock-File`) désactive toute la chaîne pour ce fichier : à réserver aux fichiers vérifiés.

Ensuite : [voir les flux alternatifs d'un fichier](../fondamentaux/fichiers-recherche.md#voir-les-flux-de-donnees-alternatifs-ads-dun-fichier) — Pour comprendre : [Windows en profondeur, ch. 4.3 (ADS et MotW)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/04-chapitre-4-le-systeme-de-fichiers-ntfs.md#43-les-flux-de-donnees-alternatifs-ads) · [ch. 26.3 (la chaîne MotW → ASR)](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#263-la-chaine-de-defense-motw-smartscreen-protected-view-asr)
{ .kw-cs-meta }

### Garder SmartScreen actif

SmartScreen vérifie la réputation d'un fichier marqué et de son URL d'origine : inconnu ou malveillant, il avertit ou bloque.

```text title="GPO"
Modèles d'administration → Composants Windows → Explorateur de fichiers
→ Configurer Windows Defender SmartScreen → Activé, « Avertir et empêcher le contournement »
Modèles d'administration → Composants Windows → Microsoft Edge (ou modèles Edge) → SmartScreen activé
```

Interface : *Sécurité Windows → Contrôle des applications et du navigateur → Protection fondée sur la réputation*.

Pour comprendre : [Windows en profondeur, ch. 26.3](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#263-la-chaine-de-defense-motw-smartscreen-protected-view-asr) — Ajout hors cours : chemins de la GPO et de l'interface
{ .kw-cs-meta }

### Bloquer les macros des documents venus d'Internet

La mesure la plus efficace contre l'hameçonnage par macro. Microsoft bloque par défaut depuis 2022 les macros VBA des documents marqués ; l'imposer par GPO pour qu'un utilisateur ne puisse pas le défaire.

```text title="GPO (modèles d'administration Office)"
Configuration utilisateur → Modèles d'administration → Microsoft Word / Excel / PowerPoint … → Options → Sécurité → Centre de gestion de la confidentialité
→ Bloquer l'exécution des macros dans les fichiers Office provenant d'Internet → Activé
```

Le mode protégé (*Protected View*) ouvre en lecture seule, dans un bac à sable, les documents marqués : ne pas le désactiver.

Pour comprendre : [Windows en profondeur, ch. 26.3 et 27.1 (P0, mesure 6)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#271-p0-actions-immediates-premiere-semaine) — Ajout hors cours : le chemin exact de la GPO
{ .kw-cs-meta }

## Logiciels

### Ne garder que les logiciels nécessaires, et à jour

Chaque logiciel installé est une surface d'attaque : version ancienne vulnérable, service privilégié, fichier de configuration avec des identifiants, outil d'accès distant aux sessions enregistrées. Inventorier, désinstaller l'inutile, mettre à jour le reste.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
                 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*' -ErrorAction SilentlyContinue |
    Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher | Sort-Object DisplayName
```

```powershell title="Appliquer"
winget upgrade --all
```

Éviter `Win32_Product` (`wmic product`) en production : il peut déclencher des réparations MSI. Les outils d'administration (Sysinternals, clients SSH, consoles) n'ont leur place que sur les postes qui en ont besoin.

Ensuite : [inventorier les logiciels](../fondamentaux/enumeration.md#inventorier-les-logiciels-sans-interroger-win32_product) · [installer, mettre à jour avec winget](../administration/logiciels.md#chercher-installer-mettre-a-jour-un-logiciel) — Pour comprendre : [Élévation de privilèges, programmes installés](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Contrôle applicatif | `Get-AppLockerPolicy -Effective` ; `Get-Service AppIDSvc` | Règles en place, d'abord en audit ; service démarré |
| Règles de chemin | Droits sur les dossiers autorisés | Aucun dossier autorisé inscriptible par les utilisateurs |
| PowerShell restreint | `$ExecutionContext.SessionState.LanguageMode` | `ConstrainedLanguage` pour le code non approuvé |
| Stratégie d'exécution | `Get-ExecutionPolicy -List` | Imposée par GPO (`RemoteSigned` ou `AllSigned`) |
| Scripts d'administration | `Get-AuthenticodeSignature` | `Valid` |
| PowerShell 2.0 | `Get-WindowsOptionalFeature … PowerShellV2Root` | `Disabled` ou absent |
| AMSI | — | Actif (Defender), jamais désactivé |
| Mark of the Web | `Get-Content <fichier> -Stream Zone.Identifier` | `ZoneId=3` sur les fichiers téléchargés |
| SmartScreen | Sécurité Windows → Contrôle des applications | Activé, contournement empêché |
| Macros Office d'Internet | GPO Office | Bloquées |
| Logiciels | Clés `Uninstall` ; `winget upgrade` | Le nécessaire, à jour |

| Journal | Ce qu'il montre |
|---|---|
| Journaux des applications et des services → Microsoft → Windows → AppLocker → EXE and DLL | 8002 autorisé, 8003 serait bloqué (audit), 8004 bloqué |
| Journaux des applications et des services → Microsoft → Windows → PowerShell → Operational | 4104 : blocs de script, y compris en mode restreint |

Les règles ASR, qui bloquent des comportements même quand le code s'exécute : [Defender et protections du système](protections.md#activer-les-regles-de-reduction-de-la-surface-dattaque-asr).
