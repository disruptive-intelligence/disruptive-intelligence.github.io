---
title: "Journaux et événements"
cours:
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Journaux et événements

Lire les journaux Windows, filtrer par identifiant et par période, retrouver les ouvertures de session, les processus lancés, les services, tâches et comptes créés, les changements du pare-feu et de Defender, les scripts PowerShell ; exporter pour analyse.

Les incontournables : `Get-WinEvent -FilterHashtable` · `wevtutil` · `eventvwr.msc` · `auditpol /get` · `Get-WinEvent -Path`
{ .kw-cs-top }

## Sous-rubriques

| Sous-rubrique | Ce qu'on y trouve |
|---|---|
| [**Lire, filtrer et exporter**](lire.md) | Ouvrir un journal, le lister, le lire, le filtrer par identifiant et par période, en extraire les champs ; l'exporter, voir la politique d'audit, l'agrandir. |
| [**Ouvertures de session et RDP**](sessions-rdp.md) | Qui s'est connecté, comment (Logon Type), et les connexions RDP reçues, échouées ou émises. |
| [**Processus et PowerShell**](processus-powershell.md) | Les processus lancés (4688) et le code PowerShell exécuté (4104, 4103). |
| [**Services, tâches et comptes**](persistance.md) | Ce qu'un attaquant installe pour rester : services, tâches planifiées, comptes créés ou ajoutés à un groupe d'administration. |
| [**Pare-feu et Defender**](pare-feu-defender.md) | Les règles de pare-feu ajoutées ou modifiées, le pare-feu désactivé ; les détections de Defender, sa désactivation et ses exclusions. |
| [**Effacement des traces**](effacement.md) | Journaux effacés et journalisation arrêtée. |

## Tous les besoins

- [Lire, filtrer et exporter](lire.md) — [Ouvrir un journal dans l'Observateur d'événements](lire.md#ouvrir-un-journal-dans-lobservateur-devenements) · [Lister les journaux et leur taille](lire.md#lister-les-journaux-et-leur-taille) · [Lire les derniers événements d'un journal](lire.md#lire-les-derniers-evenements-dun-journal) · [Filtrer par identifiant et par période](lire.md#filtrer-par-identifiant-et-par-periode) · [Extraire les champs d'un événement](lire.md#extraire-les-champs-dun-evenement) · [Exporter un journal pour l'analyser ailleurs](lire.md#exporter-un-journal-pour-lanalyser-ailleurs) · [Voir la politique d'audit active](lire.md#voir-la-politique-daudit-active) · [Agrandir un journal](lire.md#agrandir-un-journal)
- [Ouvertures de session et RDP](sessions-rdp.md) — [Retrouver les ouvertures de session](sessions-rdp.md#retrouver-les-ouvertures-de-session) · [Retrouver les connexions RDP reçues](sessions-rdp.md#retrouver-les-connexions-rdp-recues) · [Repérer les connexions RDP et les échecs d'authentification](sessions-rdp.md#reperer-les-connexions-rdp-et-les-echecs-dauthentification) · [Savoir vers quelles machines un poste s'est connecté en RDP](sessions-rdp.md#savoir-vers-quelles-machines-un-poste-sest-connecte-en-rdp)
- [Processus et PowerShell](processus-powershell.md) — [Retrouver les processus lancés](processus-powershell.md#retrouver-les-processus-lances) · [Retrouver les scripts PowerShell exécutés](processus-powershell.md#retrouver-les-scripts-powershell-executes)
- [Services, tâches et comptes](persistance.md) — [Retrouver les services installés ou modifiés](persistance.md#retrouver-les-services-installes-ou-modifies) · [Retracer la vie d'une tâche planifiée](persistance.md#retracer-la-vie-dune-tache-planifiee) · [Retracer la création d'un compte et ses privilèges](persistance.md#retracer-la-creation-dun-compte-et-ses-privileges)
- [Pare-feu et Defender](pare-feu-defender.md) — [Retracer les changements du pare-feu](pare-feu-defender.md#retracer-les-changements-du-pare-feu) · [Retracer les détections et l'altération de Defender](pare-feu-defender.md#retracer-les-detections-et-lalteration-de-defender)
- [Effacement des traces](effacement.md) — [Repérer un effacement de journal](effacement.md#reperer-un-effacement-de-journal)

## Vue d'ensemble : quel événement pour quoi

| Event ID | Journal | Signification |
|---|---|---|
| 4624 / 4625 | Journaux Windows → Security | Ouverture de session réussie / échouée |
| 4648 | Journaux Windows → Security | Ouverture avec identifiants explicites |
| 4672 | Journaux Windows → Security | Session avec privilèges spéciaux (admin) |
| 4688 | Journaux Windows → Security | Processus créé |
| 7045 / 4697 | Journaux Windows → System / Journaux Windows → Security | Service installé (7040 : démarrage modifié ; 7036 : démarré / arrêté) |
| 4698 / 4702 / 4699 | Journaux Windows → Security | Tâche planifiée créée / modifiée / supprimée (4700 / 4701 : activée / désactivée) |
| 4720 / 4726 | Journaux Windows → Security | Compte créé / supprimé (4722 : réactivé ; 4738 : modifié ; 4724 : mot de passe réinitialisé) |
| 4732 / 4728 / 4756 | Journaux Windows → Security | Membre ajouté à un groupe local / global / universel |
| 4740 | Journaux Windows → Security | Compte verrouillé |
| 4768 / 4769 / 4771 / 4776 | Journaux Windows → Security (contrôleur de domaine) | Kerberos TGT / ticket de service / échec de pré-auth / validation NTLM |
| 1102 / 104 | Journaux Windows → Security / Journaux Windows → System | Journal effacé (1100 : service de journalisation arrêté) |
| 2004 / 2005 / 2003 | Journaux des applications et des services → Microsoft → Windows → Windows Firewall With Advanced Security → Firewall | Règle de pare-feu ajoutée / modifiée / paramètre global changé |
| 1116 / 1117 | Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational | Menace détectée / action prise |
| 5001 / 5007 | Journaux des applications et des services → Microsoft → Windows → Windows Defender → Operational | Protection en temps réel désactivée / configuration (exclusions) modifiée |
| 4104 / 4103 | Journaux des applications et des services → Microsoft → Windows → PowerShell → Operational | Bloc de script exécuté / Module Logging |
| 1, 3, 11, 13, 22 | Journaux des applications et des services → Microsoft → Windows → Sysmon → Operational | Processus, réseau, fichier, registre, DNS |
| 1149 / 261 | Journaux des applications et des services → Microsoft → Windows → TerminalServices-RemoteConnectionManager → Operational | Authentification RDP réussie / connexion TCP reçue sur l'écouteur RDP |
| 21 / 24 / 25 | Journaux des applications et des services → Microsoft → Windows → TerminalServices-LocalSessionManager → Operational | Session RDP ouverte / déconnectée / reconnectée |
| 1102 | Journaux des applications et des services → Microsoft → Windows → TerminalServices-RDPClient → Operational | Connexion RDP **émise** par le poste (≠ 1102 de Security) |
| 106 / 140 / 141 / 200 / 201 | Journaux des applications et des services → Microsoft → Windows → TaskScheduler → Operational | Tâche enregistrée / modifiée / supprimée / action lancée / terminée |

Pour la méthode complète (approche SOC, corrélations, brute force, password spray, RDP), voir le cours [Analyse des journaux d'événements Windows](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md).
{ .kw-cs-meta }
