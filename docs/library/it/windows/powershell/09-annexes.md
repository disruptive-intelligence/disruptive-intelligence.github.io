---
title: Annexes
source: IT/02 Windows/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - index.md
---

---

## Annexe A — Correspondance PowerShell / Bash / Python

Pour ceux qui viennent de Linux ou de Python. **Rappel fondamental :** Bash et la plupart des pipelines Unix manipulent du **texte** ; PowerShell manipule des **objets**. L'analogie aide à démarrer mais ne doit pas faire oublier cette différence.

| Tâche | PowerShell | Bash | Python |
|-------|-----------|------|--------|
| Lister un dossier | `Get-ChildItem` | `ls` | `os.listdir` / `pathlib` |
| Chemin existe ? | `Test-Path` | `[[ -e ]]` | `Path.exists()` |
| Lire un fichier | `Get-Content` | `cat` | `open().read()` |
| Filtrer | `Where-Object` | `grep` / `awk` | `filter` / compréhension |
| Transformer | `ForEach-Object` | boucle / `sed` | `map` / compréhension |
| Trier | `Sort-Object` | `sort` | `sorted()` |
| Compter | `Measure-Object` / `.Count` | `wc` | `len()` |
| Longueur d'une chaîne | `$s.Length` | `${#s}` | `len(s)` |
| Découper une chaîne | `-split` / `.Split()` | `cut` / IFS | `str.split()` |
| Recoller | `-join` | `paste` | `str.join()` |
| Remplacer | `-replace` / `.Replace()` | `sed` | `str.replace()` / `re.sub` |
| Variable | `$x = 1` | `x=1` | `x = 1` |
| Dictionnaire | `@{ k = v }` | `declare -A` | `{ "k": v }` |
| Condition | `if () {}` | `if [[ ]]; then` | `if:` |
| Boucle | `foreach () {}` | `for … do` | `for … in` |
| Fonction | `function f {}` | `f() {}` | `def f():` |
| Ping | `Test-Connection` | `ping` | `subprocess` |
| Requête HTTP | `Invoke-RestMethod` | `curl` | `requests` |
| Exécution distante | `Invoke-Command` | `ssh` | `paramiko` |
| JSON → objet | `ConvertFrom-Json` | `jq` | `json.loads` |

---

## Annexe B — Cmdlets essentielles par domaine

### Découverte
`Get-Command`, `Get-Help`, `Get-Member`, `Get-Module`, `Get-Verb`

### Système & infos
`Get-CimInstance`, `Get-ComputerInfo`, `Get-Date`, `$env:`, `$PSVersionTable`

### Fichiers
`Get-ChildItem`, `Get/Set/Add-Content`, `Copy/Move/Remove-Item`, `New-Item`, `Test-Path`, `Join-Path`, `Get-Acl`, `Set-Acl`, `Select-String`

### Comptes locaux
`Get/New/Set/Disable/Enable-LocalUser`, `Get-LocalGroup`, `Get-LocalGroupMember`, `Add/Remove-LocalGroupMember`

### Processus & services
`Get/Start/Stop-Process`, `Get/Start/Stop/Restart/Set-Service`, `Get-CimInstance Win32_Service`

### Registre
`Get-ChildItem`, `Get-ItemProperty`, `Get-ItemPropertyValue`, `New/Set/Remove-ItemProperty`, `Test-Path`

### Tâches planifiées
`Get-ScheduledTask`, `Get-ScheduledTaskInfo`, `New-ScheduledTaskAction/Trigger/Principal`, `Register/Unregister-ScheduledTask`

### Stockage
`Get-Disk`, `Get-Partition`, `Get-Volume`, `Get-PSDrive`, `Get-WindowsFeature` (Server)

### Réseau
`Get-NetIPConfiguration`, `Get-NetAdapter`, `Get-NetIPAddress`, `New-NetIPAddress`, `Get/Set-DnsClientServerAddress`, `Resolve-DnsName`, `Get-NetRoute`, `Get-NetTCPConnection`, `Test-Connection`, `Test-NetConnection`, `Get/New/Set/Remove-NetFirewallRule`

### Active Directory
`Get/New/Set/Remove-ADUser`, `Enable/Disable/Unlock-ADAccount`, `Set-ADAccountPassword`, `Get/New-ADGroup`, `Get/Add/Remove-ADGroupMember`, `Get-ADPrincipalGroupMembership`, `Get/New/Set/Remove-ADComputer`, `Get/New-ADOrganizationalUnit`, `Move-ADObject`, `Search-ADAccount`, `Get-ADDomain`

### GPO & Server
`Get/New/Remove-GPO`, `New/Set-GPLink`, `Get-GPOReport`, `Backup/Restore-GPO`, `Get-GPResultantSetOfPolicy`, `Get-DnsServerZone`, `*-DnsServerResourceRecord*`, `Get-DhcpServerv4Scope/Lease`, `Add-DhcpServerv4Reservation`, `Get/New-SmbShare`, `Get-SmbSession`, `Get-SmbShareAccess`

### Distant & API
`Enter-PSSession`, `Invoke-Command`, `New/Remove-PSSession`, `Enable-PSRemoting`, `Invoke-RestMethod`, `Invoke-WebRequest`, `ConvertTo/From-Json`, `Connect-MgGraph`, `Get-MgUser`, `Get-MgGroup`

### Industrialisation
`Export-ModuleMember`, `Import-Module`, `Get/Set-Secret`, `Start/Stop-Transcript`, `Invoke-Pester`

### Sécurité & triage
`Get-WinEvent`, `Get-FileHash`, `Get-AuthenticodeSignature`, `Set-AuthenticodeSignature`, `Get-Item -Stream`

---

## Annexe C — Event IDs de référence

| Event ID | Journal | Signification |
|----------|---------|--------------|
| 4624 | Security | Connexion réussie |
| 4625 | Security | Échec de connexion (brute-force si répété) |
| 4634 / 4647 | Security | Déconnexion |
| 4648 | Security | Connexion avec identifiants explicites |
| 4672 | Security | Privilèges spéciaux attribués (compte à privilèges) |
| 4688 | Security | Création d'un processus |
| 4720 | Security | Création d'un compte |
| 4722 / 4725 | Security | Compte activé / désactivé |
| 4726 | Security | Suppression d'un compte |
| 4728 / 4732 | Security | Ajout à un groupe (global / local) |
| 4740 | Security | Compte verrouillé |
| 1102 | Security | Journal de sécurité effacé (signal fort) |
| 7045 | System | Nouveau service installé |
| 7040 | System | Type de démarrage d'un service modifié |
| 4104 | PowerShell/Operational | Bloc de script exécuté (Script Block Logging) |

---

## Annexe D — Droits, versions et modules requis

| Opération | Droits | Version / Environnement | Module |
|-----------|--------|------------------------|--------|
| Lire services/processus | Standard | 5.1 / 7 | intégré |
| Modifier services, écrire `HKLM:` | **Admin** | 5.1 / 7 | intégré |
| Lire journal Security | **Admin** | 5.1 / 7 | intégré |
| `Get-WmiObject` | — | **5.1 seulement** (absent en 7) | intégré |
| `Get-CimInstance` | selon classe | 5.1 / 7 | intégré |
| Cmdlets `*-LocalUser` | Admin (modif) | Win 10/11 & Server | LocalAccounts |
| Cmdlets `*-AD*` | délégué/Admin | 5.1 / 7 + **RSAT** ou DC | ActiveDirectory |
| Cmdlets `*-GPO`, `*-GPLink` | Admin | **RSAT** ou DC | GroupPolicy |
| `Install-WindowsFeature` | Admin | **Windows Server uniquement** | ServerManager |
| Cmdlets `*-DnsServer*` | Admin | Serveur DNS ou RSAT | DnsServer |
| Cmdlets `*-DhcpServer*` | Admin | Serveur DHCP ou RSAT | DhcpServer |
| `Enable-PSRemoting` | **Admin** | 5.1 / 7 | intégré |
| `Connect-MgGraph`, `Get-Mg*` | selon scopes | 5.1 / 7 | Microsoft.Graph |
| `Invoke-Pester` | Standard | 5.1 / 7 | Pester |
| `ForEach-Object -Parallel` | Standard | **7 uniquement** | intégré |
| Opérateur ternaire `? :` | Standard | **7 uniquement** | intégré |

> **Note sur la compatibilité des modules Windows en PowerShell 7.** Les modules d'administration Windows n'ont pas tous le même statut en PS7. Certains sont **nativement compatibles** ; d'autres (historiquement liés à Windows PowerShell) sont chargés via la **couche de compatibilité Windows PowerShell** : PS7 les exécute en réalité dans une session Windows PowerShell 5.1 en arrière-plan et **sérialise** les objets échangés — ce qui fonctionne dans la grande majorité des cas, mais peut entraîner des **limitations** (objets « désérialisés » sans leurs méthodes, quelques différences de comportement). En pratique, pour ce cours : `ActiveDirectory`, `DnsServer`, `DhcpServer`, `GroupPolicy`, `ServerManager` fonctionnent en 7, parfois via cette couche de compatibilité. En cas de comportement inattendu sur un objet renvoyé par un de ces modules, vérifie s'il n'est pas désérialisé (un `Get-Member` montrera des types préfixés `Deserialized.`) et, au besoin, exécute la commande depuis une console Windows PowerShell 5.1. La liste exacte évolue : consulte la matrice de compatibilité Microsoft si un module précis pose problème.

---

## Annexe E — Pièges classiques et corrections

| Piège | ❌ Incorrect | ✅ Correct |
|-------|-------------|-----------|
| Comparaison | `if ($a == $b)` | `if ($a -eq $b)` |
| Interpolation de propriété | `"$obj.Prop"` | `"$($obj.Prop)"` |
| Concaténer deux caractères | `$s[0] + $s[1]` (→ addition **numérique** : 195) | `-join @($s[0], $s[1])` ou `"$($s[0])$($s[1])"` |
| Plage calculée pouvant valoir 0 | `1..($n - 4)` (si `$n=4` → `1..0` = **@(1,0)**, 2 éléments !) | tester `if ($n -gt 4) { 1..($n - 4) }` |
| Format avant traitement | `... \| Format-Table \| Export-Csv` | `... \| Export-Csv` (Format en dernier) |
| Filtrer côté client | `Get-ADUser -Filter * \| Where …` | `Get-ADUser -Filter "…"` |
| Encodage fichier | `Set-Content x` | `Set-Content x -Encoding UTF8` |
| `Get-WmiObject` en PS7 | `Get-WmiObject …` | `Get-CimInstance …` |
| Inventaire logiciels | `Win32_Product` | clés `Uninstall` du registre |
| Variable distante | `{ Get-Service $nom }` | `{ Get-Service $using:nom }` |
| try/catch sans Stop | `try { Get-… }` | `try { Get-… -ErrorAction Stop }` |
| `$?` après un .exe | `ping…; if (-not $?)` | `ping…; if ($LASTEXITCODE -ne 0)` |
| Créer sans vérifier | `New-ADUser …` | `if (-not (Get-ADUser …)) { New-ADUser … }` |
| Masse sans simuler | `New-ADUser …` (en boucle) | `… -WhatIf` d'abord |
| Secret en clair | `$token = "abc"` | SecretManagement / SecureString |
| Execution Policy = sécurité | s'y fier | contrôle applicatif (App Control/WDAC) → CLM + signature |
| WinRM « toujours chiffré » | affirmation brute | nuancer (Kerberos domaine / NTLM-HTTPS hors domaine) |
| `LastLogonDate` exact | s'y fier à la minute | approximatif (réplication différée) |
| Permissions fichiers | ne voir que SMB ou que NTFS | l'intersection des deux gagne |

---

## Annexe F — Les deux réflexes transversaux

Tout le cours repose sur deux habitudes. Si tu ne retiens que ça :

### Réflexe 1 — Explorer avec `Get-Member`

Face à **tout** objet inconnu (service, utilisateur AD, tâche, réponse d'API, événement…) :

```powershell
<commande> | Get-Member
```


Tu découvres ses propriétés (informations) et méthodes (actions). Tu n'as pas à mémoriser PowerShell — tu l'explores. On l'a appliqué à chaque nouveau type d'objet du cours.

### Réflexe 2 — `Get`/`Test` avant `Set`/`New`/`Remove`

On regarde **toujours** avant de modifier :

```powershell
Get-…    /  Test-…        # 1. observer l'état actuel
# … décision …
Set-… / New-… / Remove-…  # 2. agir en connaissance de cause
-WhatIf                    # 3. et pour les opérations sensibles/en masse, simuler d'abord
```


Cette discipline — vérifier, simuler, sauvegarder avant d'agir — traverse toute l'administration, de la création d'un dossier (Ch.9) à l'onboarding de masse (Ch.24) en passant par les GPO (Ch.25) et le registre (Ch.12).

---

## Annexe G — Parcours de certification et ressources

### Certifications utiles (à jour 2025-2026)

| Certification | Éditeur | Portée |
|--------------|---------|--------|
| **AZ-104** (Azure Administrator) | Microsoft | Administration cloud, inclut PowerShell/Graph |
| **MD-102** (Endpoint Administrator) | Microsoft | Postes de travail, Intune |
| **AZ-802** (Windows Server Administrator Associate) | Microsoft | Windows Server, AD, hybride — successeur 2026, remplace AZ-800/AZ-801 (retirés le 30/09/2026) |
| **SC-300** (Identity and Access) | Microsoft | Entra ID, identité |
| **Sec+** (Security+) | CompTIA | Fondamentaux sécurité (utile Partie VIII) |

> Les certifications Microsoft évoluent régulièrement (noms, codes, contenus). Vérifie les intitulés actuels sur le site officiel Microsoft Learn avant de t'engager.

### Ressources d'apprentissage

- **Microsoft Learn** — documentation officielle et parcours gratuits
- **`Get-Help` et `Get-Command`** — ta première documentation, toujours à portée
- **PowerShell Gallery** ([powershellgallery.com](https://www.powershellgallery.com/)) — modules communautaires
- **Le dépôt GitHub PowerShell** — source, discussions, nouveautés
- **Communautés** : r/PowerShell, PowerShell.org, les forums Microsoft Q&A

### Pour approfondir séparément

Ce cours t'a donné les fondations PowerShell pour piloter Windows. Pour aller plus loin sur chaque technologie **en tant que telle**, oriente-toi vers des cours dédiés :

- **Active Directory** (conception, réplication, FSMO, approbations, sécurité AD)
- **Windows Server** (rôles avancés, clustering, stockage)
- **Réseau Windows** (routage, VLAN, VPN)
- **Entra ID / Microsoft 365 / Intune** (identité et gestion cloud)
- **Cybersécurité Windows / Digital Forensics** (investigation approfondie)
- **PowerShell avancé** (classes, DSC, modules binaires, CI/CD)

---

## Conclusion

Tu es parti de zéro et tu sais maintenant :

- **Comprendre PowerShell** : cmdlets `Verbe-Nom`, pipeline **objet**, variables, conditions, boucles, fonctions, gestion d'erreurs
- **Administrer un poste Windows** : fichiers et permissions NTFS, comptes locaux, processus, services, registre, tâches, disques, logiciels
- **Gérer le réseau** : IP, DNS, routage, connexions, pare-feu
- **Automatiser Active Directory** : utilisateurs, groupes, ordinateurs, OU, recherche filtrée, onboarding de masse
- **Piloter GPO et services serveur** : stratégies de groupe, DNS, DHCP, partages SMB
- **Administrer à distance et via API** : Remoting nuancé, authentification/tokens, REST, Microsoft Graph
- **Industrialiser** : modules, secrets, idempotence, `-WhatIf`, tests
- **Défendre** : diagnostic, triage, journalisation, durcissement

Et surtout, tu as acquis les **deux réflexes** qui te rendront autonome bien au-delà de ce cours : **explorer avec `Get-Member`** tout objet inconnu, et **observer avant d'agir** (`Get`/`Test` → `Set`/`New`/`Remove`, puis `-WhatIf`).

Le niveau atteint est celui d'un **administrateur Windows PowerShell junior solide** : capable d'administrer, d'automatiser, de diagnostiquer, et de s'appuyer sur ces bases pour se spécialiser. PowerShell n'est pas une fin en soi — c'est le **fil conducteur** qui relie toute l'administration Windows. Tu tiens maintenant ce fil. À toi de tirer.

**Bon scripting, et bonne administration !**
