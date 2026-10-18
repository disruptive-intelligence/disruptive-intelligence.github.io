---
title: 'Synthèse : verrouillage et patterns SOC'
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

## Account Lockout Policy

- Une **Account Lockout Policy** peut limiter certaines attaques par password guessing :
    - nombre maximal d’échecs ;
    - durée du lockout ;
    - délai avant reset du compteur.

```text
Repeated Failed Logons
→ Threshold reached
→ Account Locked
```


Mais il faut trouver un équilibre :

```text
Threshold too low
→ Attacker can intentionally lock accounts
→ Denial of Service
```


> Le lockout protège surtout contre les attaques de **password guessing**. Il ne bloque pas directement des techniques utilisant des credentials déjà compromis, comme **Pass-the-Hash**.

---

## Patterns SOC importants

### Brute Force

```text
One Account
+
Many 4625
+
Same Source
+
Short Time Window
→ Brute Force Suspicion
```


### Password Spray

```text
Many Accounts
+
Same Source
+
Few Password Attempts
→ Password Spray Suspicion
```


### Successful compromise

```text
Many 4625
        ↓
4624
        ↓
Suspicious Activity
→ High-Priority Investigation
```


### RDP Lateral Movement

```text
Compromised Host
+
RDPClient Events
+
4624 Type 10 on destination
+
1149
→ Possible Lateral Movement
```


---

## Vue d’ensemble

```text
Authentication Analysis
│
├─ 4624
│  → Successful Logon
│
├─ 4625
│  → Failed Logon
│
├─ Logon Type
│  ├─ 2  → Interactive
│  ├─ 3  → Network
│  ├─ 5  → Service
│  └─ 10 → RemoteInteractive / RDP
│
└─ RDP
   ├─ 261  → TCP connection
   ├─ 1149 → RDP authentication success
   ├─ 4624 Type 10 → Successful RDP logon
   ├─ 4625 Type 10 → Failed RDP logon
   ├─ 4648 → Explicit credentials
   └─ RDPClient 1102 → Destination information
```


Le point important est de ne jamais analyser uniquement **un Event ID** : pour reconstruire une authentification ou un lateral movement fiable, il faut corréler **Event ID + Provider + Logon Type + utilisateur + source IP + machine cible + timeline**.

Récapitulatif du cours, thème par thème :

| Thème | Journal | Event IDs |
|---|---|---|
| Authentification | Security | 4624, 4625 (+ Logon Type) |
| RDP, machine cible | Security · TerminalServices-RemoteConnectionManager | 4624 / 4625 Type 10 · 261, 1149 |
| RDP, machine source | TerminalServices-RDPClient · Security | 1102 · 4648 |
| Tâches planifiées | Security (si audit) · TaskScheduler/Operational | 4698, 4702, 4699, 4700 / 4701 · 106, 140, 141, 200, 201 |
| Services | System (Service Control Manager) · Security (si audit) | 7045, 7040, 7036 · 4697 |
| Gestion des comptes | Security | 4720, 4722, 4725, 4726, 4738, 4723 / 4724 · 4728 / 4732 / 4756 · 4729 / 4733 / 4757 |
| Manipulation des journaux | Security · System | 1102, 1100 · 104 |
| Pare-feu Windows | Windows Firewall With Advanced Security / Firewall · `pfirewall.log` | 2004, 2005, 2003 · ALLOW / DROP |
| Windows Defender | Windows Defender/Operational | 1116, 1117, 5001, 5007 |
| Exécution PowerShell | PowerShell/Operational · Security | 4104, 4103 · 4688 |
| Arrêt, redémarrage | System | 1074, 6005, 6006, 6013 |
| Privilèges et identifiants | Security | 4672, 4648 · Kerberos 4771 · NTLM 4776 |
| Audit et accès aux objets | Security | 4719, 4907 (SACL), 4656 |
| Partages réseau et filtrage | Security | 5140, 5142, 5145 · 5157 (WFP) |
| Remédiation antivirus | Windows Defender/Operational | 1118, 1119, 1120 |

## Event IDs utiles, journal par journal

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

Les Windows Event Logs constituent une source centrale pour reconstruire une activité suspecte : un Event ID s'analyse toujours avec ses champs détaillés, son contexte utilisateur, la chronologie et les autres sources de télémétrie.

Captures « HTB Windows Event Logs » : [Hack The Box Academy - Windows Event Logs & Finding Evil](https://academy.hackthebox.com/app/module/216)
