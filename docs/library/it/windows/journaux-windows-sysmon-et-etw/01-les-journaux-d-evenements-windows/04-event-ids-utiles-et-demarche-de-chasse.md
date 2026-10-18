---
title: Event IDs utiles et démarche de chasse
source: IT/02 Windows/Journaux & investigation/Journaux Windows, Sysmon et ETW.md
note: Journaux Windows, Sysmon et ETW
up:
- - Journaux Windows, Sysmon et ETW
  - ../index.md
- - Les journaux d'événements Windows
  - index.md
---

## 6. Event IDs Windows utiles

### Journal System — services, arrêt et redémarrage

| Event ID | Événement                    | Intérêt                                                     |
| -------- | ---------------------------- | ----------------------------------------------------------- |
| 1074     | Shutdown / Restart initié    | Identifier l'origine d'un arrêt ou redémarrage              |
| 6005     | Event Log Service Started    | Repérer un démarrage du service, souvent lié au boot        |
| 6006     | Event Log Service Stopped    | Repérer un arrêt du service, souvent lié au shutdown        |
| 6013     | System Uptime                | Consulter la durée de fonctionnement du système             |
| 7040     | Service Startup Type Changed | Détecter une modification du type de démarrage d'un service |
| 7045     | Service Installed            | Identifier l'installation d'un nouveau service              |

L'Event 7045 est un événement du journal System, pas du journal Security.

Ces événements permettent notamment d'investiguer des redémarrages inhabituels, l'installation de services suspects et certaines modifications pouvant soutenir la Persistence.

### Journal Security — authentification et privilèges

| Event ID | Événement                          | Intérêt                                                   |
| -------- | ---------------------------------- | --------------------------------------------------------- |
| 4624     | Successful Logon                   | Identifier les connexions réussies                        |
| 4625     | Failed Logon                       | Rechercher des tentatives d'authentification échouées     |
| 4648     | Explicit Credentials Used          | Examiner l'utilisation explicite d'identifiants           |
| 4672     | Special Privileges Assigned        | Surveiller les sessions disposant de privilèges sensibles |
| 4771     | Kerberos Pre-Authentication Failed | Rechercher des échecs de préauthentification Kerberos     |
| 4776     | Credential Validation Attempt      | Examiner les validations d'identifiants via NTLM          |

Les Events `4624`, `4625`, `4648`, `4771` et `4776` sont particulièrement utiles pour rechercher des activités suspectes d'authentification et de Lateral Movement.

### Journal Security — persistance et modifications de comptes

| Event ID | Événement               | Intérêt                                            |
| -------- | ----------------------- | -------------------------------------------------- |
| 4698     | Scheduled Task Created  | Détecter la création d'une tâche planifiée         |
| 4700     | Scheduled Task Enabled  | Identifier l'activation d'une tâche                |
| 4701     | Scheduled Task Disabled | Identifier la désactivation d'une tâche            |
| 4702     | Scheduled Task Updated  | Examiner les modifications de tâches planifiées    |
| 4738     | User Account Changed    | Détecter des modifications de comptes utilisateurs |

Les Scheduled Tasks peuvent être utilisées légitimement pour l'administration, mais également comme mécanismes de Persistence.

### Journal Security — audit et accès aux objets

| Event ID | Événement                        | Intérêt                                         |
| -------- | -------------------------------- | ----------------------------------------------- |
| 1102     | Security Audit Log Cleared       | Détecter l'effacement du journal Security       |
| 4656     | Handle to an Object Requested    | Rechercher des demandes d'accès à des objets    |
| 4719     | System Audit Policy Changed      | Identifier des changements de politique d'audit |
| 4907     | Object Auditing Settings Changed | Analyser les modifications de SACL              |

L'Event `4656` signale une demande de handle, pas nécessairement un accès effectivement réalisé.

Les Events `1102`, `4719` et `4907` peuvent révéler des tentatives de modification ou de suppression des traces d'audit, mais doivent être contextualisés.

### Journal Security — partages réseau et filtrage

| Event ID | Événement                                     | Intérêt                                                                  |
| -------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| 5140     | Network Share Accessed                        | Identifier les accès aux partages réseau                                 |
| 5142     | Network Share Created                         | Détecter la création de partages                                         |
| 5145     | Detailed File Share Access Check              | Examiner les demandes d'accès aux ressources partagées                   |
| 5157     | Windows Filtering Platform Blocked Connection | Identifier les connexions bloquées par la plateforme de filtrage Windows |

Ces événements peuvent soutenir les investigations liées aux accès SMB, aux partages non autorisés et aux communications suspectes.

### Journaux de Microsoft Defender Antivirus

Les événements suivants relèvent du journal Microsoft-Windows-Windows Defender/Operational, et non du journal Security :

| Event ID | Événement                     | Intérêt                                               |
| -------- | ----------------------------- | ----------------------------------------------------- |
| 1116     | Malware Detected              | Identifier une détection antivirus                    |
| 1118     | Remediation Started           | Suivre le début d'une action de remédiation           |
| 1119     | Remediation Succeeded         | Identifier une remédiation réussie                    |
| 1120     | Remediation Failed            | Identifier un échec de remédiation                    |
| 5001     | Real-Time Protection Disabled | Détecter la désactivation de la protection temps réel |

La distinction Detection / Remediation Started / Remediation Succeeded / Remediation Failed est essentielle : détecter un malware ne garantit pas qu'il ait été neutralisé.

## 7. Journaux Windows — démarche de threat hunting

```
Suspicious Activity
        ↓
Identify Relevant Event IDs
        ↓
Collect Windows Event Logs
        ↓
Filter by Time / User / Host
        ↓
Correlate Logon IDs & Events
        ↓
Reconstruct Event Timeline
        ↓
Investigate Suspicious Behavior
```


### Bonnes pratiques

- Baseline : connaître les comportements normaux des systèmes et utilisateurs.
- Centralized Logging : collecter les événements dans un SIEM ou une infrastructure centralisée.
- Log Correlation : rapprocher plusieurs Event IDs et sources de données.
- Time Synchronization : synchroniser les horloges pour faciliter l'analyse chronologique.
- Audit Configuration : activer les politiques d'audit nécessaires à la production des événements recherchés.
- Alert Tuning : adapter les règles de détection à l'environnement pour limiter les False Positives.

## 8. Synthèse

| Objectif d'investigation        | Événements utiles            |
| ------------------------------- | ---------------------------- |
| Authentication Analysis         | 4624, 4625, 4648, 4771, 4776 |
| Privileged Access               | 4672                         |
| Persistence                     | 4698, 4700–4702, 7040, 7045  |
| Account Modification            | 4738                         |
| Log Tampering                   | 1102, 4719, 4907             |
| Network Share Activity          | 5140, 5142, 5145             |
| Blocked Connections             | 5157                         |
| Malware Detection & Remediation | 1116, 1118–1120              |
| Security Protection Disabled    | 5001                         |
| Shutdown / Restart              | 1074, 6005, 6006, 6013       |

Les Windows Event Logs constituent une source centrale pour reconstruire une activité suspecte et identifier des traces d'attaque.

Le point essentiel est de ne pas interpréter un événement isolément : les Event IDs doivent être analysés avec leurs champs détaillés, leur contexte utilisateur, la chronologie des événements et les autres sources de télémétrie disponibles.

Source des captures : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
