---
title: "Durcissement"
cours:
  - library/cyber/hardening/securite-systeme-windows/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Durcissement d'un poste Windows

Réduire la surface d'attaque d'un poste de travail sans casser les usages : comptes et privilèges, identifiants et secrets, exécution, services, réseau, protections, démarrage et chiffrement, journalisation, maintien dans la durée. Pour chaque mesure : à quoi elle sert, comment la **vérifier**, comment l'**appliquer** (commande ou GPO), et le cours qui l'explique.

Les incontournables : `Get-LocalGroupMember` · `net accounts` · `Win32_DeviceGuard` · `Get-MpComputerStatus` · `Get-NetFirewallProfile` · `Get-SmbServerConfiguration` · `auditpol` · `manage-bde -status` · `gpresult /h`
{ .kw-cs-top }

Sur un poste joint au domaine, tout se pose par **GPO** (ou Intune) : une modification locale se perd ou se défait. Les commandes servent d'abord à vérifier l'état réel du poste, avant et après. Les entrées marquées « Ajout hors cours » complètent mes cours avec des réglages élémentaires.

## La méthode

1. **Inventorier** : quels postes, quels usages, quelles applications métier.
2. **Choisir une baseline** : un seul référentiel (Microsoft Security Baselines, ANSSI, CIS), dérivé et versionné.
3. **Mesurer avant** : l'état du poste avec les commandes « Vérifier » de chaque fiche.
4. **Tester sur un pilote** : en mode audit quand il existe (AppLocker, ASR, accès contrôlé aux dossiers, NTLM).
5. **Déployer par vagues** : par lots de mesures, par anneaux, avec un retour arrière par mesure.
6. **Mesurer après** : conformité, incidents ; documenter les exceptions (justifiées, bornées, compensées, revues).

Pour comprendre : [Windows en profondeur, ch. 27 (hardening P0 / P1 / P2)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md) · [MCS, ch. 22 (durcissement et référentiels)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/04-partie-iv-configuration-dependances-et-couches-oub/01-chapitre-22-durcissement-et-referentiels-de-config.md) · [Sécurité système Windows](../../../library/cyber/hardening/securite-systeme-windows/index.md)
{ .kw-cs-meta }

## Par où commencer

**Le socle**, à vérifier avant tout : système encore supporté et à jour, compte du quotidien sans droits d'administration, administrateurs locaux réduits, mot de passe administrateur local unique, pare-feu et Defender actifs, journalisation en place.

| Vague | # | Mesure | Fiche |
|---|---|---|---|
| **P0** — première semaine | 1 | Ligne de commande dans les créations de processus (4688) | [Journalisation](journalisation.md#enregistrer-la-ligne-de-commande-des-processus-4688) |
|  | 2 | Sysmon avec une configuration de référence | [Journalisation](journalisation.md#deployer-sysmon) |
|  | 3 | Centralisation des journaux (WEF ou agent SIEM) | [Journalisation](journalisation.md#centraliser-les-journaux-hors-du-poste) |
|  | 4 | LLMNR et NBT-NS désactivés | [Réseau](reseau.md#desactiver-llmnr-et-netbios) |
|  | 5 | SMBv1 désactivé | [Réseau](reseau.md#desactiver-smbv1-et-exiger-la-signature-smb) |
|  | 6 | Macros des documents venus d'Internet bloquées | [Exécution](execution.md#bloquer-les-macros-des-documents-venus-dinternet) |
|  | 7 | Script Block Logging PowerShell | [Journalisation](journalisation.md#activer-la-journalisation-des-scripts-powershell) |
| **P1** — sous trois mois | 8 | Windows LAPS | [Identifiants](identifiants.md#donner-a-chaque-poste-son-propre-mot-de-passe-administrateur-local-laps) |
|  | 9 | Credential Guard | [Identifiants](identifiants.md#activer-credential-guard) |
|  | 10 | LSA Protection (RunAsPPL) | [Identifiants](identifiants.md#faire-tourner-lsass-en-processus-protege-runasppl) |
|  | 11 | Signature SMB obligatoire | [Réseau](reseau.md#desactiver-smbv1-et-exiger-la-signature-smb) |
|  | 12 | Règles ASR de Defender | [Protections](protections.md#activer-les-regles-de-reduction-de-la-surface-dattaque-asr) |
|  | 13 | BitLocker sur tout le parc | [Démarrage et chiffrement](demarrage.md#chiffrer-le-disque-systeme-avec-bitlocker) |
|  | 14 | WDigest désactivé, LM et NTLMv1 refusés | [Identifiants](identifiants.md#desactiver-wdigest) · [LM / NTLMv1](identifiants.md#refuser-lm-et-ntlmv1) |
| **P2** — à six mois | 15 | AppLocker ou App Control (WDAC), d'abord en audit | [Exécution](execution.md#autoriser-seulement-les-programmes-prevus-applocker) |
|  | 16 | Intégrité de la mémoire (HVCI) | [Protections](protections.md#activer-lintegrite-de-la-memoire-hvci-et-la-liste-de-blocage-des-pilotes-vulnerables) |
|  | 17 | Liste de blocage des pilotes vulnérables | [Protections](protections.md#activer-lintegrite-de-la-memoire-hvci-et-la-liste-de-blocage-des-pilotes-vulnerables) |
|  | 18 | Transcription PowerShell | [Journalisation](journalisation.md#activer-la-journalisation-des-scripts-powershell) |
|  | 19 | SmartScreen et Mark of the Web préservée | [Exécution](execution.md#garder-smartscreen-actif) |
|  | 20 | Revue des points de persistance (Autoruns) | [Services](services.md#faire-le-menage-dans-ce-qui-demarre-avec-la-machine) |
|  | 21 | Règles SIEM sur les binaires système détournables (certutil, mshta, rundll32, regsvr32…) | [Windows en profondeur, ch. 26.1](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#261-les-lolbins-living-off-the-land-binaries) |

Pour comprendre : [Windows en profondeur, ch. 27.1 à 27.3](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#271-p0-actions-immediates-premiere-semaine)
{ .kw-cs-meta }

## Les fiches

| Fiche | Ce qu'on y trouve |
|---|---|
| [**Comptes et privilèges**](comptes.md) | Comptes à revoir, Invité et Administrateur intégré, administrateurs locaux, compte du quotidien séparé, tiering, mots de passe et verrouillage, MFA, verrouillage de session, UAC, privilèges sensibles, comptes de service. |
| [**Identifiants et secrets**](identifiants.md) | Credential Guard, RunAsPPL, WDigest, LAPS, cache des identifiants, LM et NTLMv1, audit de NTLM, Protected Users, RDP sans dépôt d'identifiants, secrets en clair, historique PowerShell, coffre de secrets. |
| [**Exécution et applications**](execution.md) | AppLocker, App Control (WDAC), mode restreint de PowerShell, stratégie d'exécution, signature, PowerShell 2.0, AMSI, Mark of the Web, SmartScreen, macros, logiciels installés. |
| [**Services, droits et persistance**](services.md) | Services inutiles, compte des services, chemins sans guillemets, permissions de service, dossiers modifiables, `PATH` inscriptible, ménage dans le démarrage, clés de registre sensibles. |
| [**Réseau et accès distant**](reseau.md) | Pare-feu (profils, règles entrantes, journal), LLMNR, NetBIOS, mDNS, WPAD, SMBv1, signature SMB, partages, bureau à distance, WinRM, ports en écoute. |
| [**Defender et protections du système**](protections.md) | Composants de Defender, protection contre les falsifications, protection cloud, exclusions, signatures, règles ASR, accès contrôlé aux dossiers, protection contre les exploits, HVCI, pilotes vulnérables. |
| [**Démarrage, chiffrement et périphériques**](demarrage.md) | UEFI et Secure Boot, TPM, micrologiciel, BitLocker et ses protecteurs, exécution automatique, supports amovibles. |
| [**Journalisation et surveillance**](journalisation.md) | Stratégie d'audit avancée, ligne de commande des processus, journalisation PowerShell, Sysmon, taille des journaux, centralisation, alerte sur l'effacement, événements à surveiller. |
| [**Mises à jour, référentiel et maintien**](maintien.md) | Version supportée, correctifs vérifiés, anneaux, logiciels tiers, baseline dérivée, durcir sans casser, GPO appliquées, conformité et dérive, exceptions, horloge, sauvegardes. |

## Carte mentale

<div class="kw-mindmap" markdown>

- **Durcir un poste Windows**
    - [Comptes et privilèges](comptes.md)
        - [Comptes à revoir](comptes.md#reperer-les-comptes-locaux-a-revoir) : `Get-LocalUser`
        - [Invité, Administrateur](comptes.md#neutraliser-les-comptes-par-defaut-invite-administrateur-integre) : SID `-501`, `-500`
        - [Administrateurs locaux](comptes.md#reduire-les-administrateurs-locaux-au-strict-necessaire) : `S-1-5-32-544`
        - [Compte du quotidien](comptes.md#separer-le-compte-du-quotidien-et-le-compte-dadministration) : sans droits
        - [Tiering](comptes.md#interdire-aux-comptes-privilegies-de-se-connecter-aux-postes) : *Deny log on…*
        - [Mots de passe](comptes.md#appliquer-une-politique-de-mot-de-passe-et-de-verrouillage) : `net accounts`
        - [MFA](comptes.md#exiger-le-mfa-pour-les-acces-privilegies)
        - [Verrouillage de session](comptes.md#verrouiller-la-session-apres-inactivite) : `InactivityTimeoutSecs`
        - [UAC](comptes.md#garder-le-controle-de-compte-dutilisateur-uac-actif) : `EnableLUA`
        - [Privilèges sensibles](comptes.md#reserver-les-privileges-sensibles) : `secedit /export`
        - [Comptes de service](comptes.md#restreindre-les-comptes-de-service) : gMSA
    - [Identifiants et secrets](identifiants.md)
        - [Credential Guard](identifiants.md#activer-credential-guard) : `Win32_DeviceGuard`
        - [RunAsPPL](identifiants.md#faire-tourner-lsass-en-processus-protege-runasppl)
        - [WDigest](identifiants.md#desactiver-wdigest) : `UseLogonCredential = 0`
        - [LAPS](identifiants.md#donner-a-chaque-poste-son-propre-mot-de-passe-administrateur-local-laps)
        - [Cache](identifiants.md#reduire-les-identifiants-de-domaine-mis-en-cache) : `CachedLogonsCount`
        - [LM, NTLMv1](identifiants.md#refuser-lm-et-ntlmv1) : `LmCompatibilityLevel = 5`
        - [Auditer NTLM](identifiants.md#reduire-ntlm-dabord-en-audit) : 8001-8004
        - [Protected Users](identifiants.md#proteger-les-comptes-privilegies-du-domaine)
        - [RDP d'administration](identifiants.md#ne-pas-laisser-ses-identifiants-sur-la-machine-administree-rdp) : `/remoteGuard`
        - [Secrets dans les fichiers](identifiants.md#chercher-les-mots-de-passe-laisses-dans-des-fichiers) : `Select-String`, `cpassword`
        - [Historique, cmdkey](identifiants.md#verifier-lhistorique-powershell-et-le-gestionnaire-didentification)
        - [Coffre](identifiants.md#ranger-les-secrets-des-scripts-dans-un-coffre) : `Set-Secret`
    - [Exécution et applications](execution.md)
        - [AppLocker](execution.md#autoriser-seulement-les-programmes-prevus-applocker) : audit, puis blocage
        - [App Control (WDAC)](execution.md#preferer-app-control-for-business-wdac-pour-un-controle-robuste)
        - [Mode restreint](execution.md#verifier-que-powershell-passe-en-mode-restreint) : `LanguageMode`
        - [Stratégie d'exécution](execution.md#regler-la-strategie-dexecution-sans-compter-dessus) : `-List`
        - [Signature](execution.md#signer-ses-scripts-dadministration) : `Set-AuthenticodeSignature`
        - [PowerShell 2.0](execution.md#retirer-powershell-20) : désactivé
        - [AMSI](execution.md#laisser-amsi-inspecter-les-scripts)
        - [Mark of the Web](execution.md#verifier-quun-fichier-telecharge-porte-la-mark-of-the-web) : `Zone.Identifier`
        - [SmartScreen](execution.md#garder-smartscreen-actif)
        - [Macros](execution.md#bloquer-les-macros-des-documents-venus-dinternet)
        - [Logiciels](execution.md#ne-garder-que-les-logiciels-necessaires-et-a-jour) : `winget upgrade`
    - [Services, droits et persistance](services.md)
        - [Services inutiles](services.md#desactiver-les-services-inutiles) : `Set-Service -StartupType Disabled`
        - [Moindre privilège](services.md#faire-tourner-chaque-service-avec-le-moindre-privilege) : `StartName`
        - [Service mal configuré](services.md#reperer-un-service-mal-configure) : guillemets, `icacls`
        - [Permissions de service](services.md#lire-les-permissions-dun-service) : `sc.exe sdshow`
        - [Permissions trop larges](services.md#reperer-les-permissions-trop-larges) : `Get-Acl`
        - [Retirer l'écriture](services.md#retirer-lecriture-aux-utilisateurs-sur-un-dossier-de-programme) : `icacls /remove:g`
        - [PATH inscriptible](services.md#verifier-que-le-path-systeme-ne-contient-pas-de-dossier-inscriptible)
        - [Démarrage](services.md#faire-le-menage-dans-ce-qui-demarre-avec-la-machine) : Autoruns
        - [Clés sensibles](services.md#surveiller-les-cles-de-registre-sensibles) : SACL, Sysmon 12-14
    - [Réseau et accès distant](reseau.md)
        - [Pare-feu actif](reseau.md#activer-le-pare-feu-sur-les-trois-profils) : trois profils
        - [Règles entrantes](reseau.md#reduire-les-regles-entrantes-au-strict-necessaire) : `-RemoteAddress`
        - [Journal du pare-feu](reseau.md#journaliser-les-connexions-refusees-par-le-pare-feu) : `-LogBlocked`
        - [LLMNR, NetBIOS](reseau.md#desactiver-llmnr-et-netbios)
        - [mDNS, WPAD](reseau.md#couper-aussi-mdns-et-wpad-sils-ne-servent-pas)
        - [SMBv1, signature](reseau.md#desactiver-smbv1-et-exiger-la-signature-smb)
        - [Partages](reseau.md#fermer-les-partages-inutiles-et-resserrer-leurs-droits) : pas d'`Everyone`
        - [Bureau à distance](reseau.md#fermer-le-bureau-a-distance-ou-le-borner) : `fDenyTSConnections`, NLA
        - [WinRM](reseau.md#restreindre-winrm-et-powershell-remoting) : `TrustedHosts`, JEA
        - [Ports en écoute](reseau.md#verifier-ce-qui-ecoute-sur-le-poste)
    - [Defender et protections](protections.md)
        - [État de Defender](protections.md#voir-letat-de-microsoft-defender) : `Get-MpComputerStatus`
        - [Falsifications](protections.md#verrouiller-defender-contre-la-desactivation-protection-contre-les-falsifications) : `IsTamperProtected`
        - [Cloud, échantillons](protections.md#garder-la-protection-cloud-et-lenvoi-dechantillons) : `MAPSReporting`
        - [Exclusions](protections.md#voir-les-exclusions-de-defender) : 5007
        - [Règles ASR](protections.md#activer-les-regles-de-reduction-de-la-surface-dattaque-asr) : `AuditMode`
        - [Rançongiciels](protections.md#proteger-les-dossiers-contre-les-rancongiciels-acces-controle-aux-dossiers) : accès contrôlé aux dossiers
        - [Exploits](protections.md#verifier-la-protection-contre-les-exploits-dep-aslr-cfg) : `Get-ProcessMitigation`
        - [HVCI, pilotes](protections.md#activer-lintegrite-de-la-memoire-hvci-et-la-liste-de-blocage-des-pilotes-vulnerables)
    - [Démarrage et chiffrement](demarrage.md)
        - [Secure Boot](demarrage.md#verifier-que-le-poste-demarre-en-uefi-avec-secure-boot) : `Confirm-SecureBootUEFI`
        - [TPM](demarrage.md#verifier-la-puce-tpm) : `Get-Tpm`
        - [Micrologiciel](demarrage.md#verrouiller-le-micrologiciel)
        - [BitLocker](demarrage.md#chiffrer-le-disque-systeme-avec-bitlocker) : TPM + PIN
        - [Exécution automatique](demarrage.md#couper-lexecution-automatique-des-supports-amovibles)
        - [Stockage amovible](demarrage.md#controler-les-supports-de-stockage-amovibles)
    - [Journalisation](journalisation.md)
        - [Audit avancé](journalisation.md#activer-la-strategie-daudit-avancee) : `auditpol`
        - [Ligne de commande](journalisation.md#enregistrer-la-ligne-de-commande-des-processus-4688) : 4688
        - [PowerShell](journalisation.md#activer-la-journalisation-des-scripts-powershell) : 4104, 4103
        - [Sysmon](journalisation.md#deployer-sysmon)
        - [Taille](journalisation.md#agrandir-un-journal) : `wevtutil sl`
        - [Centralisation](journalisation.md#centraliser-les-journaux-hors-du-poste) : WEF, SIEM
        - [Effacement](journalisation.md#alerter-sur-leffacement-et-larret-de-la-journalisation) : 1102, 1100
    - [Maintien](maintien.md)
        - [Version supportée](maintien.md#verifier-que-la-version-de-windows-est-encore-supportee) : build + UBR
        - [Correctifs installés](maintien.md#verifier-que-les-correctifs-sont-reellement-installes) : `RebootPending`
        - [Anneaux](maintien.md#deployer-les-correctifs-par-anneaux) : WSUS, MECM, Intune
        - [Baseline](maintien.md#partir-dun-referentiel-et-le-deriver) : dérivée, versionnée
        - [Sans casser](maintien.md#durcir-sans-casser-la-production) : audit, lots
        - [GPO appliquées](maintien.md#verifier-que-les-gpo-de-durcissement-sappliquent-vraiment) : `gpresult /h`
        - [Conformité, dérive](maintien.md#mesurer-la-conformite-et-reperer-la-derive)
        - [Exceptions](maintien.md#tracer-les-exceptions)
        - [Horloge](maintien.md#synchroniser-lhorloge) : `w32tm`
        - [Sauvegardes](maintien.md#sauvegarder-et-tester-la-restauration) : 3-2-1-1-0

</div>

## Check-list du poste

À dérouler sur un poste à durcir, fiche par fiche ; chaque ligne renvoie à l'entrée qui dit comment vérifier et appliquer.

**Comptes et privilèges**

- [ ] [Comptes locaux inconnus, inutilisés ou sans expiration traités](comptes.md#reperer-les-comptes-locaux-a-revoir)
- [ ] [Invité désactivé ; Administrateur intégré désactivé ou géré par LAPS](comptes.md#neutraliser-les-comptes-par-defaut-invite-administrateur-integre)
- [ ] [Administrateurs locaux réduits au nécessaire, fixés par GPO](comptes.md#reduire-les-administrateurs-locaux-au-strict-necessaire)
- [ ] [Compte du quotidien hors du groupe Administrateurs](comptes.md#separer-le-compte-du-quotidien-et-le-compte-dadministration)
- [ ] [Comptes Tier 0 interdits d'ouverture de session sur le poste](comptes.md#interdire-aux-comptes-privilegies-de-se-connecter-aux-postes)
- [ ] [Politique de mot de passe et de verrouillage en place](comptes.md#appliquer-une-politique-de-mot-de-passe-et-de-verrouillage)
- [ ] [MFA sur les comptes privilégiés et l'accès distant](comptes.md#exiger-le-mfa-pour-les-acces-privilegies)
- [ ] [Verrouillage de session après inactivité](comptes.md#verrouiller-la-session-apres-inactivite)
- [ ] [UAC actif, « Toujours notifier » pour les administrateurs](comptes.md#garder-le-controle-de-compte-dutilisateur-uac-actif)
- [ ] [Privilèges sensibles réservés](comptes.md#reserver-les-privileges-sensibles)
- [ ] [Comptes de service au moindre privilège, gMSA](comptes.md#restreindre-les-comptes-de-service)

**Identifiants et secrets**

- [ ] [Credential Guard actif](identifiants.md#activer-credential-guard)
- [ ] [LSASS en processus protégé](identifiants.md#faire-tourner-lsass-en-processus-protege-runasppl)
- [ ] [WDigest désactivé](identifiants.md#desactiver-wdigest)
- [ ] [LAPS déployé, lecture restreinte](identifiants.md#donner-a-chaque-poste-son-propre-mot-de-passe-administrateur-local-laps)
- [ ] [Cache des identifiants réduit](identifiants.md#reduire-les-identifiants-de-domaine-mis-en-cache)
- [ ] [LM et NTLMv1 refusés](identifiants.md#refuser-lm-et-ntlmv1)
- [ ] [NTLM audité, exceptions connues](identifiants.md#reduire-ntlm-dabord-en-audit)
- [ ] [Comptes privilégiés du domaine dans Protected Users](identifiants.md#proteger-les-comptes-privilegies-du-domaine)
- [ ] [RDP d'administration avec Remote Credential Guard](identifiants.md#ne-pas-laisser-ses-identifiants-sur-la-machine-administree-rdp)
- [ ] [Aucun mot de passe en clair dans les fichiers, scripts, SYSVOL](identifiants.md#chercher-les-mots-de-passe-laisses-dans-des-fichiers)
- [ ] [Historique PowerShell et Gestionnaire d'identification vérifiés](identifiants.md#verifier-lhistorique-powershell-et-le-gestionnaire-didentification)
- [ ] [Secrets des scripts dans un coffre](identifiants.md#ranger-les-secrets-des-scripts-dans-un-coffre)

**Exécution et applications**

- [ ] [Contrôle applicatif en audit, puis appliqué](execution.md#autoriser-seulement-les-programmes-prevus-applocker)
- [ ] [PowerShell en mode restreint pour le code non approuvé](execution.md#verifier-que-powershell-passe-en-mode-restreint)
- [ ] [Stratégie d'exécution imposée par GPO](execution.md#regler-la-strategie-dexecution-sans-compter-dessus)
- [ ] [Scripts d'administration signés](execution.md#signer-ses-scripts-dadministration)
- [ ] [PowerShell 2.0 absent ou désactivé](execution.md#retirer-powershell-20)
- [ ] [SmartScreen actif](execution.md#garder-smartscreen-actif)
- [ ] [Macros des documents venus d'Internet bloquées](execution.md#bloquer-les-macros-des-documents-venus-dinternet)
- [ ] [Logiciels inutiles retirés, les autres à jour](execution.md#ne-garder-que-les-logiciels-necessaires-et-a-jour)

**Services, droits et persistance**

- [ ] [Services inutiles désactivés](services.md#desactiver-les-services-inutiles)
- [ ] [Aucun service en `LocalSystem` sans besoin](services.md#faire-tourner-chaque-service-avec-le-moindre-privilege)
- [ ] [Chemins de services entre guillemets, dossiers des binaires protégés](services.md#reperer-un-service-mal-configure)
- [ ] [Permissions des services restreintes](services.md#lire-les-permissions-dun-service)
- [ ] [Aucun dossier de programme modifiable par les utilisateurs](services.md#reperer-les-permissions-trop-larges)
- [ ] [`PATH` système sans dossier inscriptible](services.md#verifier-que-le-path-systeme-ne-contient-pas-de-dossier-inscriptible)
- [ ] [Démarrage automatique passé en revue](services.md#faire-le-menage-dans-ce-qui-demarre-avec-la-machine)

**Réseau et accès distant**

- [ ] [Pare-feu actif sur les trois profils](reseau.md#activer-le-pare-feu-sur-les-trois-profils)
- [ ] [Règles entrantes réduites et restreintes à leur source](reseau.md#reduire-les-regles-entrantes-au-strict-necessaire)
- [ ] [Connexions refusées journalisées](reseau.md#journaliser-les-connexions-refusees-par-le-pare-feu)
- [ ] [LLMNR et NetBIOS désactivés](reseau.md#desactiver-llmnr-et-netbios)
- [ ] [mDNS et WPAD coupés s'ils ne servent pas](reseau.md#couper-aussi-mdns-et-wpad-sils-ne-servent-pas)
- [ ] [SMBv1 désactivé, signature SMB exigée](reseau.md#desactiver-smbv1-et-exiger-la-signature-smb)
- [ ] [Partages inutiles supprimés, pas d'`Everyone`](reseau.md#fermer-les-partages-inutiles-et-resserrer-leurs-droits)
- [ ] [Bureau à distance fermé, ou NLA et source restreinte](reseau.md#fermer-le-bureau-a-distance-ou-le-borner)
- [ ] [WinRM restreint, pas de `TrustedHosts = *`](reseau.md#restreindre-winrm-et-powershell-remoting)
- [ ] [Chaque port en écoute justifié](reseau.md#verifier-ce-qui-ecoute-sur-le-poste)

**Defender et protections**

- [ ] [Tous les composants de Defender actifs, signatures à jour](protections.md#voir-letat-de-microsoft-defender)
- [ ] [Protection contre les falsifications active](protections.md#verrouiller-defender-contre-la-desactivation-protection-contre-les-falsifications)
- [ ] [Protection cloud active](protections.md#garder-la-protection-cloud-et-lenvoi-dechantillons)
- [ ] [Aucune exclusion injustifiée](protections.md#voir-les-exclusions-de-defender)
- [ ] [Règles ASR en audit, puis en blocage](protections.md#activer-les-regles-de-reduction-de-la-surface-dattaque-asr)
- [ ] [Accès contrôlé aux dossiers](protections.md#proteger-les-dossiers-contre-les-rancongiciels-acces-controle-aux-dossiers)
- [ ] [Protection contre les exploits sans `OFF`](protections.md#verifier-la-protection-contre-les-exploits-dep-aslr-cfg)
- [ ] [HVCI et liste de blocage des pilotes vulnérables](protections.md#activer-lintegrite-de-la-memoire-hvci-et-la-liste-de-blocage-des-pilotes-vulnerables)

**Démarrage, chiffrement et périphériques**

- [ ] [UEFI et Secure Boot actifs, certificats à jour](demarrage.md#verifier-que-le-poste-demarre-en-uefi-avec-secure-boot)
- [ ] [TPM 2.0 prêt](demarrage.md#verifier-la-puce-tpm)
- [ ] [Micrologiciel protégé par mot de passe, à jour](demarrage.md#verrouiller-le-micrologiciel)
- [ ] [BitLocker actif, clé de récupération sauvegardée hors du poste](demarrage.md#chiffrer-le-disque-systeme-avec-bitlocker)
- [ ] [Exécution automatique désactivée](demarrage.md#couper-lexecution-automatique-des-supports-amovibles)
- [ ] [Stockage amovible contrôlé et audité](demarrage.md#controler-les-supports-de-stockage-amovibles)

**Journalisation et surveillance**

- [ ] [Stratégie d'audit avancée appliquée](journalisation.md#activer-la-strategie-daudit-avancee)
- [ ] [Ligne de commande dans 4688](journalisation.md#enregistrer-la-ligne-de-commande-des-processus-4688)
- [ ] [Script Block Logging, Module Logging, transcription](journalisation.md#activer-la-journalisation-des-scripts-powershell)
- [ ] [Sysmon déployé](journalisation.md#deployer-sysmon)
- [ ] [Journaux agrandis](journalisation.md#agrandir-un-journal)
- [ ] [Journaux centralisés hors du poste](journalisation.md#centraliser-les-journaux-hors-du-poste)
- [ ] [Alerte sur l'effacement des journaux](journalisation.md#alerter-sur-leffacement-et-larret-de-la-journalisation)

**Mises à jour et maintien**

- [ ] [Version de Windows encore supportée](maintien.md#verifier-que-la-version-de-windows-est-encore-supportee)
- [ ] [Dernier cumul installé, aucun redémarrage en attente](maintien.md#verifier-que-les-correctifs-sont-reellement-installes)
- [ ] [Poste dans un anneau de déploiement](maintien.md#deployer-les-correctifs-par-anneaux)
- [ ] [GPO de durcissement réellement appliquées](maintien.md#verifier-que-les-gpo-de-durcissement-sappliquent-vraiment)
- [ ] [Écarts à la baseline documentés](maintien.md#tracer-les-exceptions)
- [ ] [Horloge synchronisée](maintien.md#synchroniser-lhorloge)
- [ ] [Sauvegarde et restauration testées](maintien.md#sauvegarder-et-tester-la-restauration)

Pour voir si une mesure a été contournée sur un poste : [Repérer une attaque](../reperer-une-attaque/index.md) · [Journaux et événements](../fondamentaux/logs/index.md).
{ .kw-cs-meta }
