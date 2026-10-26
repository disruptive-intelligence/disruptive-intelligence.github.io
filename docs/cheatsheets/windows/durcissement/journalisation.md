---
title: "Journalisation et surveillance"
cours:
  - library/cyber/hardening/securite-systeme-windows/index.md
---

# Journalisation et surveillance

Voir ce qui se passe sur le poste, et le garder hors de portée d'un attaquant : stratégie d'audit avancée, ligne de commande des processus, journalisation PowerShell, Sysmon, journaux assez grands, centralisation, alerte sur l'effacement.

Les incontournables : `auditpol` · `wevtutil sl` · `Get-WinEvent` · `sysmon64` · `EnableScriptBlockLogging`
{ .kw-cs-top }

Sans journalisation, aucune investigation n'est possible : c'est la première mesure du plan de durcissement, avant même les autres. Les Event IDs n'existent que si l'audit correspondant est activé.

## Audit

### Activer la stratégie d'audit avancée

La stratégie d'audit décide de ce que Windows écrit dans le journal Security. Par défaut, elle ne suffit pas.

```bat title="Vérifier"
auditpol /get /category:*
```

```bat title="Appliquer — une sous-catégorie"
auditpol /set /subcategory:"Création du processus" /success:enable
auditpol /set /subcategory:"Ouvrir la session" /success:enable /failure:enable
```

```text title="GPO"
Configuration ordinateur → Stratégies → Paramètres Windows → Paramètres de sécurité
→ Configuration avancée de la stratégie d'audit → Stratégies d'audit
```

| Catégorie | Sous-catégorie | Audit |
|---|---|---|
| **Account Logon** | Credential Validation | Succès + échec |
| **Account Management** | Application Group Management · Computer Account Management · Other Account Management Events · Security Group Management · User Account Management | Succès + échec |
| **Detailed Tracking** | PnP Activity · Process Creation | Succès |
| **Logon/Logoff** | Account Lockout · Logon · Other Logon/Logoff Events | Succès + échec |
|  | Group Membership · Logoff · Special Logon | Succès |
| **Object Access** | Removable Storage | Succès + échec |
| **Policy Change** | Audit Policy Change | Succès + échec |
|  | Authentication Policy Change · Authorization Policy Change | Succès |
| **Privilege Use** | Sensitive Privilege Use | Succès + échec |
| **System** | IPsec Driver · Other System Events · Security System Extension · System Integrity | Succès + échec |
|  | Security State Change | Succès |

Les noms suivent la langue du système : dans `auditpol` et la GPO d'un Windows français, *Process Creation* devient « Création du processus », *Logon* « Ouvrir la session ». Sur les contrôleurs de domaine, ajouter Kerberos (service d'authentification, opérations de ticket) et l'accès au service d'annuaire.

Ensuite : [voir la politique d'audit active](../fondamentaux/logs/lire.md#voir-la-politique-daudit-active) — Pour comprendre : [Sécurité système Windows, Audit Policy (le tableau)](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#strategie-daudit-audit-policy) · [Active Directory, ch. 12.1](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/04-chapitre-12-journalisation-et-audit-ad.md#121-activer-la-bonne-politique-daudit) — Ajout hors cours : `auditpol /set`
{ .kw-cs-meta }

### Enregistrer la ligne de commande des processus (4688)

Sans elle, 4688 dit qu'un programme a été lancé, pas ce qu'il a fait : `powershell.exe` seul, au lieu de la commande encodée qui l'accompagnait.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit' -Name ProcessCreationIncludeCmdLine_Enabled -ErrorAction SilentlyContinue   # 1 : activé
```

```text title="GPO"
Modèles d'administration → Système → Audit de création de processus
→ Inclure la ligne de commande dans les événements de création de processus → Activé
(avec la sous-catégorie « Création du processus » en succès)
```

La ligne de commande peut contenir des secrets tapés par les utilisateurs : l'accès au journal Security doit rester restreint.

Ensuite : [retrouver les processus lancés](../fondamentaux/logs/processus-powershell.md#retrouver-les-processus-lances) — Pour comprendre : [Windows en profondeur, ch. 21.3 (configurer correctement)](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#213-configurer-correctement) · [ch. 27.1 (P0, mesure 1)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#271-p0-actions-immediates-premiere-semaine) — Ajout hors cours : la valeur `ProcessCreationIncludeCmdLine_Enabled`
{ .kw-cs-meta }

![[cheatsheets/windows/fondamentaux/logs/processus-powershell#Activer la journalisation des scripts PowerShell]]

Les trois mécanismes, à activer par GPO : **Script Block Logging** (4104, le code exécuté après désobfuscation), **Module Logging** (4103, les commandes et leurs paramètres), **Transcription** (entrées et sorties dans des fichiers texte, le plus complet et le plus volumineux). Ranger les transcriptions dans un dossier où les utilisateurs ne peuvent ni lire ni effacer.
{ .kw-cs-meta }

## Télémétrie

### Déployer Sysmon

Sysmon enrichit la journalisation native : hash des binaires, processus parent, connexions réseau par processus, chargements de DLL, accès à LSASS, requêtes DNS, modifications du registre. Il observe, il ne bloque pas : il complète un EDR.

```bat title="Appliquer"
sysmon64.exe -accepteula -i config.xml   :: installation
sysmon64.exe -c config.xml               :: mise à jour de la configuration
```

```powershell title="Vérifier"
Get-Service Sysmon64 | Select-Object Status, StartType
```

Partir d'une configuration de référence (SwiftOnSecurity/sysmon-config, olafhartong/sysmon-modular) et l'ajuster : trop large, elle noie le SIEM ; trop étroite, elle laisse des angles morts. Déploiement par GPO, SCCM ou Intune. Un administrateur peut l'arrêter : la disparition de ses événements est elle-même un signal.

Ensuite : [vérifier que Sysmon tourne](../fondamentaux/logs/sysmon.md#verifier-que-sysmon-tourne-et-lire-ses-evenements) · [configurer ce que Sysmon collecte](../fondamentaux/logs/sysmon.md#configurer-ce-que-sysmon-collecte) — Pour comprendre : [Windows en profondeur, ch. 22 (Sysmon)](../../../library/it/windows/windows-en-profondeur/06-partie-vi-event-logs-artefacts-et-forensic.md#222-la-configuration) · [Sysmon et ETW](../../../library/it/windows/sysmon-et-etw/index.md)
{ .kw-cs-meta }

## Conservation

![[cheatsheets/windows/fondamentaux/logs/lire#Agrandir un journal]]

Les tailles par défaut font écraser les événements en quelques heures sur une machine active : Security à plusieurs centaines de Mo au moins, PowerShell et Sysmon aussi. Les valeurs se fixent par GPO (*Modèles d'administration → Composants Windows → Service Journal des événements*) et se vérifient avec `wevtutil gl Security`.
{ .kw-cs-meta }

### Centraliser les journaux hors du poste

Un journal local peut être effacé, écrasé ou perdu avec la machine. Les événements doivent partir vers un collecteur : **Windows Event Forwarding** (abonnements vers un serveur collecteur) ou agent du SIEM. Le SIEM corrèle (utilisateur + machine + heure + processus + adresse source) : un Event ID seul ne prouve pas une attaque.

```text title="Schéma"
Postes et serveurs → Windows Event Forwarding (ou agent) → collecteur → SIEM → corrélation, alertes
```

Protéger les journaux : accès restreint (ils contiennent noms, adresses, lignes de commande), stockage protégé, rétention définie pour l'investigation et la conformité, alerte sur l'espace disque.

Pour comprendre : [Sécurité système Windows, politique de journalisation](../../../library/cyber/hardening/securite-systeme-windows/07-infrastructure-de-journalisation-windows.md#politique-de-journalisation) · [Active Directory, ch. 12.4](../../../library/it/active-directory/active-directory/03-partie-iii-administration-et-controle/04-chapitre-12-journalisation-et-audit-ad.md#124-centraliser-et-dimensionner)
{ .kw-cs-meta }

### Alerter sur l'effacement et l'arrêt de la journalisation

Un attaquant privilégié efface les journaux pour masquer son passage. 1102 et 1100 doivent déclencher une alerte côté SIEM : localement, le signal arrive trop tard.

| Event ID | Journal | Signification |
|---|---|---|
| 1102 | Journaux Windows → Security | Journal de sécurité effacé |
| 104 | Journaux Windows → System | Un autre journal effacé |
| 1100 | Journaux Windows → Security | Service de journalisation arrêté |

Ensuite : [repérer un effacement de journal](../fondamentaux/logs/effacement.md#reperer-un-effacement-de-journal) — Pour comprendre : [Sécurité système Windows, protection contre la suppression des traces](../../../library/cyber/hardening/securite-systeme-windows/07-infrastructure-de-journalisation-windows.md#protection-contre-la-suppression-des-traces) · [Analyse des journaux, manipulation des journaux](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/09-manipulation-des-journaux.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Stratégie d'audit avancée | `auditpol /get /category:*` | Le tableau ci-dessus, par GPO |
| Ligne de commande dans 4688 | `…\Policies\System\Audit\ProcessCreationIncludeCmdLine_Enabled` | `1` |
| Script Block Logging | `…\PowerShell\ScriptBlockLogging\EnableScriptBlockLogging` | `1` |
| Module Logging, transcription | GPO Windows PowerShell | Activés, transcriptions protégées |
| Sysmon | `Get-Service Sysmon64` | `Running`, configuration de référence ajustée |
| Taille des journaux | `wevtutil gl Security` | Plusieurs centaines de Mo au moins |
| Centralisation | Collecteur WEF ou agent SIEM | Événements reçus hors du poste |
| Effacement | Alerte SIEM | 1102, 104, 1100 alertés |

| À surveiller | Event ID | Journal |
|---|---|---|
| Ouverture de session réussie / échouée | 4624 / 4625 | Journaux Windows → Security |
| Ouverture avec identifiants explicites | 4648 | Journaux Windows → Security |
| Session avec privilèges spéciaux | 4672 | Journaux Windows → Security |
| Création de processus | 4688 | Journaux Windows → Security |
| Compte créé, activé, désactivé, supprimé | 4720, 4722, 4725, 4726 | Journaux Windows → Security |
| Mot de passe changé / réinitialisé | 4723 / 4724 | Journaux Windows → Security |
| Ajout à un groupe global / local / universel | 4728 / 4732 / 4756 | Journaux Windows → Security |
| Compte verrouillé | 4740 | Journaux Windows → Security |
| Service installé | 4697 / 7045 | Journaux Windows → Security / System |
| Tâche planifiée créée | 4698 | Journaux Windows → Security |
| Bloc de script PowerShell | 4104 | Journaux des applications et des services → Microsoft → Windows → PowerShell → Operational |
| Connexion RDP reçue | 1149 ; 4624 type 10 | Journaux des applications et des services → Microsoft → Windows → TerminalServices-RemoteConnectionManager → Operational ; Security |
| Protection Defender coupée / configuration changée | 5001 / 5007 | Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational |
| Règle de pare-feu ajoutée / modifiée | 2004 / 2005 | Journaux des applications et des services → Microsoft → Windows → Windows Firewall With Advanced Security → Firewall |

Le détail de chaque événement : [Journaux et événements](../fondamentaux/logs/index.md).
