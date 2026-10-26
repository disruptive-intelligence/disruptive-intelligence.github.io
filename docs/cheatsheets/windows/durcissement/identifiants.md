---
title: "Identifiants et secrets"
cours:
  - library/it/windows/windows-en-profondeur/index.md
---

# Identifiants et secrets

Protéger chaque endroit où Windows garde un secret : mémoire de LSASS, SAM, secrets LSA, identifiants mis en cache, protocoles anciens ; ne pas exposer ses identifiants en administration à distance ; chasser les mots de passe laissés en clair.

Les incontournables : `Win32_DeviceGuard` · `RunAsPPL` · `UseLogonCredential` · `LmCompatibilityLevel` · `CachedLogonsCount` · `cmdkey /list` · `Set-Secret`
{ .kw-cs-top }

## Le principe

Chaque mesure ferme une source précise : aucune ne les couvre toutes, il faut les combiner.

| Où vit le secret | Ce qu'il contient | Ce qui le protège |
|---|---|---|
| Mémoire de `lsass.exe` | Hashes NTLM, tickets Kerberos des sessions ouvertes ; mot de passe en clair si WDigest | Credential Guard, LSA Protection (RunAsPPL), WDigest coupé, EDR, peu d'administrateurs |
| SAM (+ SYSTEM) | Hashes des comptes **locaux** | LAPS, peu d'administrateurs locaux, BitLocker (copie hors ligne) |
| SECURITY (secrets LSA) | Mots de passe des comptes de service, compte machine | Comptes de service gMSA et moindre privilège |
| Cache (DCC2) | Empreintes des derniers comptes de domaine connectés | Cache réduit sur les serveurs |
| DPAPI | Mots de passe des navigateurs, Wi-Fi, Gestionnaire d'identification | Mot de passe de session fort, sessions d'administration ailleurs |
| Fichiers, scripts, SYSVOL | Mots de passe écrits en clair | Coffre de secrets, recherche régulière |

Pour comprendre : [Windows en profondeur, ch. 11 à 13 (où vit chaque secret, extraction, protections)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md)
{ .kw-cs-meta }

## Mémoire de LSASS

### Activer Credential Guard

Les secrets d'authentification quittent LSASS pour un environnement isolé par l'hyperviseur (VBS) : même SYSTEM ne peut plus les lire. La protection la plus forte, sur matériel compatible (virtualisation, Secure Boot, TPM recommandé). Elle ne protège ni la SAM, ni les secrets LSA, ni le cache.

```powershell title="Vérifier"
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard |
    Select-Object VirtualizationBasedSecurityStatus, SecurityServicesConfigured, SecurityServicesRunning
```

??? example "Sortie"
    ```text
    VirtualizationBasedSecurityStatus SecurityServicesConfigured SecurityServicesRunning
    --------------------------------- -------------------------- -----------------------
                                    2 {1, 2}                     {1, 2}
    ```

```text title="GPO"
Configuration ordinateur → Modèles d'administration → Système → Device Guard
→ Activer la sécurité basée sur la virtualisation → Activé
   Configuration de Credential Guard : Activé avec verrou UEFI
```

`SecurityServicesRunning` contient `1` : Credential Guard tourne ; `2` : intégrité de la mémoire (HVCI). `VirtualizationBasedSecurityStatus = 2` : VBS actif. Même information dans `msinfo32` (« Sécurité basée sur la virtualisation »). Il est activé par défaut sur les Windows 11 Entreprise récents dont le matériel le permet.

Pour comprendre : [Windows en profondeur, ch. 13.2 et 13.3 (VBS, vérifier l'état)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#132-vbs-vsm-et-credential-guard) — Ajout hors cours : le chemin de la GPO, `VirtualizationBasedSecurityStatus`
{ .kw-cs-meta }

### Faire tourner LSASS en processus protégé (RunAsPPL)

LSASS devient un processus protégé : un processus non protégé, même administrateur, ne peut plus lire sa mémoire. Moins fort que Credential Guard (contournable depuis le noyau, par exemple avec un pilote vulnérable), mais plus compatible.

```powershell title="Vérifier"
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name RunAsPPL -ErrorAction SilentlyContinue
```

```bat title="Appliquer"
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL /t REG_DWORD /d 1 /f   :: puis redémarrer
```

`1` (ou `2`) : protégé ; rien : non configuré. Tester d'abord sur un pilote : un module de sécurité ou une carte à puce qui injecte une DLL non signée dans LSASS cesse de fonctionner.

Pour comprendre : [Windows en profondeur, ch. 13.1](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#131-les-protections-et-ce-quelles-couvrent) · [Fiche cyber, LSA Protection](../../../library/it/windows/windows-fiche-cyber/11-approfondir-uac-et-protections.md) — Ajout hors cours : la commande `reg add`
{ .kw-cs-meta }

### Désactiver WDigest

WDigest garde le mot de passe sous une forme réversible dans LSASS. Désactivé par défaut depuis Windows 8.1 / 2012 R2, mais un attaquant peut le réactiver pour récupérer les mots de passe en clair des prochaines connexions.

```powershell title="Vérifier"
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest -Name UseLogonCredential -ErrorAction SilentlyContinue
```

```bat title="Appliquer"
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 0 /f
```

`0` ou absent : désactivé. `1` : à corriger et à investiguer (qui l'a posé, et quand : Sysmon 13).

Pour comprendre : [Windows en profondeur, ch. 13.3 (vérifier l'état)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#133-verifier-letat) — Ajout hors cours : la commande `reg add`
{ .kw-cs-meta }

## Comptes locaux et cache

### Donner à chaque poste son propre mot de passe administrateur local (LAPS)

Sans LAPS, le compte administrateur local a souvent le même mot de passe sur tout le parc : un poste compromis ouvre `C$` sur tous les autres. Windows LAPS génère un mot de passe unique par machine, le range dans l'AD (ou Entra ID) et le renouvelle.

```powershell title="Vérifier (poste d'administration)"
Get-LapsADPassword -Identity <ordinateur> -AsPlainText | Select-Object ComputerName, Account, PasswordUpdateTime, ExpirationTimestamp
```

```text title="Sur le poste"
Journaux des applications et des services → Microsoft → Windows → LAPS → Operational
```

Points de contrôle : lecture du mot de passe réservée à un groupe restreint, consultation journalisée, rotation après usage, suivi des machines qui ne renouvellent plus leur secret. LAPS ne protège pas les comptes du domaine.

Ensuite : [lire le mot de passe LAPS d'un poste](../administration/active-directory/ou-ordinateurs-gpo.md#lire-le-mot-de-passe-laps-dun-poste) — Pour comprendre : [Sécurité système Windows, Windows LAPS](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#windows-laps) · [Active Directory, ch. 11.5](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md#115-laps) — Ajout hors cours : le journal LAPS du poste
{ .kw-cs-meta }

### Réduire les identifiants de domaine mis en cache

Windows garde une empreinte des derniers comptes de domaine connectés (10 par défaut) pour ouvrir une session sans contrôleur de domaine. Sur un serveur, c'est inutile : 0 à 2. Sur un portable nomade, garder une valeur raisonnable.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name CachedLogonsCount
```

```text title="GPO"
Paramètres de sécurité → Stratégies locales → Options de sécurité
→ Ouverture de session interactive : nombre d'ouvertures de session précédentes à mettre en cache
  (Interactive logon: Number of previous logons to cache)
```

Pour comprendre : [Active Directory, ch. 24.5 (protéger les secrets en mémoire)](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#245-proteger-les-secrets-en-memoire) — Ajout hors cours : la valeur `CachedLogonsCount`
{ .kw-cs-meta }

## Protocoles d'authentification

### Refuser LM et NTLMv1

LM et NTLMv1 sont cassables ; NTLMv2 reste nécessaire tant que des applications l'utilisent. Refuser LM et NTLMv1 est immédiat sur un parc récent.

```powershell title="Vérifier"
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name LmCompatibilityLevel -ErrorAction SilentlyContinue
```

```text title="GPO"
Paramètres de sécurité → Stratégies locales → Options de sécurité
→ Sécurité réseau : niveau d'authentification LAN Manager
→ Envoyer uniquement les réponses NTLMv2. Refuser LM et NTLM   (valeur 5)
```

`5` attendu. Absent : comportement par défaut du système (NTLMv2 envoyé, mais LM et NTLMv1 encore acceptés en réception).

Pour comprendre : [Active Directory, ch. 24.1 (réduire NTLM)](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#241-reduire-ntlm-progressivement) · [Sécurité système Windows, NTLMv1 vs NTLMv2](../../../library/cyber/hardening/securite-systeme-windows/04-authentification-et-autorisation-sous-windows.md#ntlmv1-vs-ntlmv2) — Ajout hors cours : la valeur `LmCompatibilityLevel`
{ .kw-cs-meta }

### Réduire NTLM, d'abord en audit

Couper NTLM d'un coup casse des applications. On audite, on corrige les causes (accès par adresse IP, SPN manquant ou en double, horloge, application ancienne), on documente les exceptions, puis on restreint.

```text title="GPO"
Options de sécurité → Sécurité réseau : restreindre NTLM : auditer le trafic NTLM entrant
                    (Network security: Restrict NTLM: Audit Incoming NTLM Traffic)
puis, une fois les exceptions connues : Restrict NTLM: Deny …
```

```powershell title="Vérifier — qui utilise encore NTLM"
Get-WinEvent -LogName 'Microsoft-Windows-NTLM/Operational' -MaxEvents 50 | Select-Object TimeCreated, Id, Message
```

Les événements 8001 à 8004 sont dans *Journaux des applications et des services → Microsoft → Windows → NTLM → Operational* ; côté contrôleur de domaine, 4776 (validation NTLM).

Pour comprendre : [Active Directory, ch. 5.4 (pourquoi NTLM persiste) et 24.1](../../../library/it/active-directory/active-directory/02-partie-ii-authentification/02-chapitre-5-ntlm-le-protocole-herite-qui-refuse-de.md#54-pourquoi-ntlm-persiste)
{ .kw-cs-meta }

### Protéger les comptes privilégiés du domaine

Les membres de **Protected Users** n'ont plus de NTLM, de DES/RC4, de délégation ni de cache, et leur TGT dure 4 heures. À réserver aux comptes humains privilégiés, après test (pas aux comptes de service ni d'ordinateur). Cocher aussi « Le compte est sensible et ne peut pas être délégué » sur les comptes d'administration.

```powershell title="Vérifier"
Get-ADGroupMember "Protected Users" | Select-Object Name, objectClass
```

Côté Kerberos : AES uniquement (RC4 et DES désactivés après inventaire), pré-authentification obligatoire, aucune délégation non contrainte hors des contrôleurs de domaine, horloge synchronisée.

Pour comprendre : [Active Directory, ch. 24.3 et 24.4 (Kerberos, Protected Users)](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#244-protected-users)
{ .kw-cs-meta }

## Administration à distance

### Ne pas laisser ses identifiants sur la machine administrée (RDP)

Une session RDP classique dépose les identifiants de l'administrateur sur le serveur : s'il est compromis, ils le sont aussi. *Remote Credential Guard* garde les identifiants sur le poste d'origine ; *Restricted Admin* n'en envoie pas du tout.

```bat title="Appliquer"
mstsc /remoteGuard /v:<machine>       :: Remote Credential Guard
mstsc /restrictedAdmin /v:<machine>   :: Restricted Admin (la session agit avec le compte de la machine cible)
```

```text title="GPO (poste d'origine)"
Modèles d'administration → Système → Délégation d'informations d'identification
→ Restreindre la délégation d'informations d'identification à des serveurs distants
```

Pour comprendre : [Windows en profondeur, ch. 13.1](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#131-les-protections-et-ce-quelles-couvrent) · [Active Directory, ch. 11.4](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/03-chapitre-11-tiering-model-et-separation-des-privil.md#114-les-outils-du-tiering) — Ajout hors cours : les options de `mstsc` et la GPO
{ .kw-cs-meta }

## Secrets en clair

### Chercher les mots de passe laissés dans des fichiers

Scripts, fichiers de configuration, partages et dossiers personnels contiennent souvent des identifiants : un attaquant n'a alors aucune faille à exploiter. Chercher, puis déplacer les secrets dans un coffre et les changer.

```powershell title="Vérifier"
Get-ChildItem <dossier> -Recurse -File -Include *.ps1,*.bat,*.cmd,*.vbs,*.xml,*.config,*.ini,*.txt -ErrorAction SilentlyContinue |
    Select-String -Pattern 'password|passwd|pwd=|mot de passe' -List | Select-Object Path, LineNumber, Line
```

```bat title="Exemple — anciens mots de passe de préférences de GPO dans SYSVOL"
findstr /S /I cpassword \\<domaine>\SYSVOL\<domaine>\Policies\*.xml
```

Un `cpassword` dans SYSVOL est déchiffrable par n'importe quel utilisateur du domaine (clé publiée par Microsoft) : supprimer le fichier et changer le mot de passe. SYSVOL et NETLOGON sont lisibles par tous : aucun secret ne doit y figurer.

Ensuite : [chercher un mot dans un dossier](../fondamentaux/fichiers-recherche.md#chercher-un-mot-dans-un-fichier-ou-un-dossier) — Pour comprendre : [Windows en profondeur, ch. 11.2 (GPP)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#112-les-autres-sources-de-secrets) · [Active Directory, ch. 9.6](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/01-chapitre-9-group-policy-gpo-configuration-et-secur.md#96-les-gpo-un-objet-sensible) · [Élévation de privilèges, identifiants exposés](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/01-outils-utiles.md) — Ajout hors cours : les deux commandes de recherche
{ .kw-cs-meta }

### Vérifier l'historique PowerShell et le Gestionnaire d'identification

Un secret tapé sur la ligne de commande finit dans l'historique PSReadLine ; des identifiants enregistrés pour RDP ou des partages restent dans le Gestionnaire d'identification (protégés par DPAPI, donc lisibles par qui contrôle la session).

```powershell title="Vérifier"
Select-String -Path (Get-PSReadLineOption).HistorySavePath -Pattern 'password|-Credential|ConvertTo-SecureString|Set-Secret' |
    Select-Object LineNumber, Line
```

```bat title="Exemple"
cmdkey /list
```

Supprimer une entrée inutile : `cmdkey /delete:<cible>`. Pour saisir un secret sans qu'il reste dans l'historique : `Read-Host -AsSecureString`.

Pour comprendre : [PowerShell, ch. 33 (gérer les secrets)](../../../library/it/windows/powershell/07-partie-vii-automatisation-et-industrialisation/01-chapitre-33-industrialiser-ses-scripts.md) · [Windows en profondeur, ch. 11.2 (DPAPI)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#112-les-autres-sources-de-secrets) — Ajout hors cours : `HistorySavePath` et `cmdkey`
{ .kw-cs-meta }

### Ranger les secrets des scripts dans un coffre

Un mot de passe, un jeton ou une clé d'API ne s'écrit jamais dans un script : un `.ps1` versionné dans Git, c'est une fuite garantie. Le module SecretManagement range le secret chiffré et le rend au moment de l'usage.

```powershell title="Appliquer"
Install-Module Microsoft.PowerShell.SecretManagement, Microsoft.PowerShell.SecretStore -Scope CurrentUser
Register-SecretVault -Name Coffre -ModuleName Microsoft.PowerShell.SecretStore -DefaultVault
$secret = Read-Host "Valeur du secret" -AsSecureString     # saisie masquée, hors historique
Set-Secret -Name "ApiToken" -SecureStringSecret $secret
```

```powershell title="Exemple — au moment de l'usage"
$token = Get-Secret -Name "ApiToken" -AsPlainText
```

Ne jamais écrire `Set-Secret -Secret "valeur"` : la valeur part dans l'historique. Pour un compte de service : gMSA plutôt qu'un mot de passe stocké.

Pour comprendre : [PowerShell, ch. 33 (le module SecretManagement)](../../../library/it/windows/powershell/07-partie-vii-automatisation-et-industrialisation/01-chapitre-33-industrialiser-ses-scripts.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Credential Guard | `Win32_DeviceGuard` → `SecurityServicesRunning` | Contient `1` |
| LSA Protection | `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL` | `1` ou `2` |
| WDigest | `…\SecurityProviders\WDigest\UseLogonCredential` | `0` ou absent |
| LAPS | `Get-LapsADPassword` ; journal LAPS du poste | Mot de passe unique, renouvelé, lecture restreinte |
| Cache des identifiants | `…\Winlogon\CachedLogonsCount` | 0 à 2 sur les serveurs, raisonnable sur les portables |
| LM et NTLMv1 | `…\Control\Lsa\LmCompatibilityLevel` | `5` |
| Usage de NTLM | Journal NTLM, événements 8001 à 8004 | Connu, exceptions documentées |
| Comptes privilégiés du domaine | `Get-ADGroupMember "Protected Users"` | Comptes humains Tier 0 membres |
| RDP d'administration | `mstsc /remoteGuard` | Identifiants non déposés sur la cible |
| Secrets dans les fichiers | `Select-String` ; `findstr cpassword` sur SYSVOL | Aucun |
| Historique et Gestionnaire d'identification | `HistorySavePath` ; `cmdkey /list` | Aucun secret, aucune entrée inutile |
| Secrets des scripts | `Get-SecretInfo` | Dans un coffre, jamais en clair |

| Journal | Ce qu'il montre |
|---|---|
| Journaux des applications et des services → Microsoft → Windows → NTLM → Operational | 8001 à 8004 : authentifications NTLM auditées |
| Journaux des applications et des services → Microsoft → Windows → LAPS → Operational | Rotations du mot de passe LAPS |
| Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | 10 : accès à `lsass.exe` ; 13 : modification de `UseLogonCredential` ou `RunAsPPL` |

Pour la détection d'un vol en cours : [Repérer un accès à LSASS](../reperer-une-attaque/reperer-un-acces-a-lsass.md).
