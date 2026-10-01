---
title: Annexes
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

---


## Annexe A — Glossaire SOC

| Terme               | Définition                                                                       |
| ------------------- | -------------------------------------------------------------------------------- |
| **ATT&CK**          | Framework MITRE des tactiques, techniques et procédures adverses                 |
| **Beaconing**       | Pattern de communication périodique entre un malware et son C2                   |
| **BEC**             | Business Email Compromise — fraude par compromission de messagerie               |
| **BTP**             | Benign True Positive — alerte techniquement correcte sur une action légitime     |
| **C2**              | Command and Control — infrastructure de commande d'un malware                    |
| **CIM**             | Common Information Model — modèle de normalisation des données (Splunk)          |
| **CMDB**            | Configuration Management Database — inventaire des assets IT                     |
| **Containment**     | Actions de confinement pour limiter la propagation d'un incident                 |
| **DGA**             | Domain Generation Algorithm — algorithme de génération de domaines C2            |
| **DLL sideloading** | Chargement d'une DLL malveillante via le search order d'une application légitime |
| **EDR**             | Endpoint Detection and Response — détection et réponse sur les endpoints         |
| **EQL**             | Event Query Language — langage Elastic pour les séquences d'événements           |
| **EPSS**            | Exploit Prediction Scoring System — probabilité d'exploitation d'une CVE         |
| **FP**              | False Positive — alerte sans menace réelle                                       |
| **FN**              | False Negative — menace non détectée                                             |
| **Golden hour**     | Fenêtre critique entre le mouvement latéral et le déploiement du ransomware      |
| **Hunting**         | Recherche proactive de menaces non détectées par les règles                      |
| **IoC**             | Indicator of Compromise — artefact technique d'une compromission                 |
| **JA3/JA4**         | Fingerprint TLS pour identifier des clients réseau par leur négociation          |
| **Kerberoasting**   | Attaque AD consistant à craquer les mots de passe via les tickets Kerberos       |
| **KEV**             | Known Exploited Vulnerabilities — catalogue CISA des CVE exploitées ITW          |
| **KQL**             | Kusto Query Language (Sentinel) ou Kibana Query Language (Elastic)               |
| **LOLBin**          | Living Off the Land Binary — binaire système légitime détourné                   |
| **MDR**             | Managed Detection and Response — service managé de détection                     |
| **MTTD**            | Mean Time to Detect — temps moyen de détection                                   |
| **MTTR**            | Mean Time to Respond — temps moyen de réponse                                    |
| **MSSP**            | Managed Security Service Provider — prestataire de services de sécurité          |
| **NDR**             | Network Detection and Response — détection réseau                                |
| **NTP**             | Network Time Protocol — synchronisation horaire                                  |
| **Playbook**        | Procédure structurée de réponse à un type d'incident                             |
| **Purple team**     | Collaboration offensive-défensive pour valider les détections                    |
| **REX**             | Retour d'Expérience — analyse post-incident pour l'amélioration                  |
| **Sigma**           | Format universel de règles de détection (YAML), convertible en SPL/KQL/EQL       |
| **SIEM**            | Security Information and Event Management — outil central du SOC                 |
| **SITREP**          | Situation Report — rapport de situation lors d'une escalade                      |
| **SOAR**            | Security Orchestration, Automation and Response                                  |
| **SPL**             | Search Processing Language — langage de requête Splunk                           |
| **Stacking**        | Technique de hunting par agrégation et comptage pour trouver les outliers        |
| **Sysmon**          | System Monitor — outil Microsoft de télémétrie avancée                           |
| **TLP**             | Traffic Light Protocol — classification de la diffusion du renseignement         |
| **TTP**             | Tactics, Techniques, and Procedures — comportements de l'attaquant               |
| **UAL**             | Unified Audit Log — journal d'audit Microsoft 365                                |
| **UEBA**            | User and Entity Behavior Analytics — détection d'anomalies comportementales      |
| **VOC**             | Vulnerability Operations Center — gestion opérationnelle des vulnérabilités      |
| **VP**              | Vrai Positif (True Positive) — alerte confirmée comme menace réelle              |
| **VQL**             | Velociraptor Query Language — langage de Velociraptor pour le hunting            |
| **XDR**             | Extended Detection and Response — détection multi-sources                        |
| **YARA**            | Langage de règles pour l'identification de fichiers malveillants                 |
| **CVE**             | Identifiant de la vulnérabilité                                                  |
| **CWE**             | Faiblesse de conception sous-jacente                                             |
| **CVSS**            | Score de sévérité                                                                |
| **EPSS**            | Probabilité d'exploitation                                                       |
| **KEV**             | Vuln exploitées activement ?                                                     |

---


## Annexe B — Event IDs Windows : référence rapide

| Event ID | Source | Description | Interprétation SOC | FP courants |
|----------|--------|-------------|-------------------|-------------|
| **4624** | Security | Logon réussi | Qui s'est connecté, depuis où, quel type (2=interactif, 3=réseau, 10=RDP) | Comptes de service (type 3 massif) |
| **4625** | Security | Logon échoué | Brute force, password spraying, credential stuffing | Apps mal configurées, mots de passe expirés |
| **4648** | Security | Logon explicit credentials | Mouvement latéral (runas, PsExec -u), pass-the-hash | Admin IT utilisant runas légitime |
| **4672** | Security | Privileges spéciaux | Connexion admin, élévation de privilèges | Comptes admin légitimes |
| **4688** | Security | Process creation | Exécution suspecte (avec command line si GPO activée) | Scripts d'administration légitimes |
| **4698** | Security | Scheduled task created | Persistence (tâche planifiée malveillante) | Tâches SCCM, GPO, admin |
| **4720** | Security | User account created | Création de compte par l'attaquant | Provisioning IT légitime |
| **4728/4732** | Security | Member added to group | Ajout à Domain Admins ou groupe privilégié | Changements IT documentés |
| **4769** | Security | Kerberos TGS request | Kerberoasting si encryption RC4 (0x17) en volume | Authentification Kerberos normale |
| **7045** | System | Service installed | PsExec (PSEXESVC), malware persistence | Installation de logiciels légitimes |
| **1102** | Security | Audit log cleared | Anti-forensics — effacement des traces | Rotation de logs planifiée (rare) |
| **1** | Sysmon | Process create | Process tree complet avec hash et parent | Volume élevé (filtrer par config) |
| **3** | Sysmon | Network connection | Quel processus contacte quelle IP | Volume élevé (filtrer par config) |
| **7** | Sysmon | Image loaded | DLL sideloading, DLL injection | DLL légitimes (filtrer par signature) |
| **10** | Sysmon | Process access | Accès LSASS (credential dumping) | AV, EDR accédant à LSASS |
| **11** | Sysmon | File create | Drop de malware, staging de fichiers | Création de fichiers légitimes (config) |
| **22** | Sysmon | DNS query | Résolution de domaine par processus | Volume élevé (filtrer par config) |

---


## Annexe C — Cheat sheets requêtes SIEM

*10 requêtes essentielles dans les 3 langages principaux.*

### 1. Brute force / Password spraying

**SPL :** `index=windows EventCode=4625 | stats count by src_ip, TargetUserName | where count > 10 | sort -count`

**KQL (Sentinel) :** `SecurityEvent | where EventID == 4625 | summarize count() by IpAddress, TargetAccount | where count_ > 10 | order by count_ desc`

**KQL (Elastic) :** `event.code: "4625"` puis agrégation dans Lens/Dashboard

### 2. Mouvement latéral PsExec

**SPL :** `index=windows EventCode=7045 ServiceName="PSEXESVC" | table _time host ServiceFileName AccountName`

**KQL (Sentinel) :** `Event | where EventID == 7045 | where RenderedDescription contains "PSEXESVC" | project TimeGenerated, Computer, RenderedDescription`

### 3. Kerberoasting

**SPL :** `index=windows EventCode=4769 TicketEncryptionType=0x17 | stats count values(ServiceName) by IpAddress | where count > 5`

**KQL (Sentinel) :** `SecurityEvent | where EventID == 4769 and TicketEncryptionType == "0x17" | summarize count(), make_set(ServiceName) by IpAddress | where count_ > 5`

### 4. Beaconing C2

**SPL :** `index=proxy src_ip="10.x.x.x" | sort _time | streamstats current=f last(_time) as prev by src_ip dest | eval interval=_time-prev | stats avg(interval) stdev(interval) count by src_ip dest | eval jitter=stdev/avg*100 | where jitter < 15 AND count > 50`

### 5. PowerShell obfusqué

**SPL :** `index=sysmon EventCode=1 Image="*powershell*" (CommandLine="*-enc*" OR CommandLine="*-nop*" OR CommandLine="*IEX*" OR CommandLine="*downloadstring*") | table _time host user CommandLine ParentImage`

### 6. Certutil download cradle

**SPL :** `index=sysmon EventCode=1 Image="*certutil*" (CommandLine="*urlcache*" OR CommandLine="*verifyctl*") | table _time host user CommandLine ParentImage`

### 7. Shadow copy deletion (pré-ransomware)

**SPL :** `index=sysmon EventCode=1 (CommandLine="*vssadmin*delete*shadow*" OR CommandLine="*wmic*shadowcopy*delete*") | table _time host user CommandLine`

### 8. Forwarding rule M365

**KQL (Sentinel) :** `OfficeActivity | where Operation in ("New-InboxRule", "Set-InboxRule") | where Parameters contains "ForwardTo" or Parameters contains "RedirectTo" | project TimeGenerated, UserId, Operation, Parameters`

### 9. Timeline utilisateur

**SPL :** `index=* user="marc.dubois" earliest=-48h | sort _time | table _time index sourcetype action src_ip dest_ip dest CommandLine`

### 10. Scope IP (quels autres hosts contactent une IP suspecte)

**SPL :** `index=firewall dest_ip="185.xx.xx.xx" | stats count earliest(_time) latest(_time) by src_ip | sort -count`

---


## Annexe D — Règles Sigma de référence

*5 règles Sigma complètes commentées.*

**Règle 1 — Certutil Download Cradle :** (voir Ch.7 pour la règle complète commentée)

**Règle 2 — Kerberoasting (>5 comptes en 5 min) :**

```yaml
title: Potential Kerberoasting - Multiple RC4 TGS Requests
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4769
        TicketEncryptionType: '0x17'
    timeframe: 5m
    condition: selection | count(ServiceName) by IpAddress > 5
level: high
tags:
    - attack.credential_access
    - attack.t1558.003
```


**Règle 3 — Shadow Copy Deletion :**

```yaml
title: Shadow Copy Deletion - Ransomware Precursor
logsource:
    category: process_creation
    product: windows
detection:
    selection_vssadmin:
        Image|endswith: '\vssadmin.exe'
        CommandLine|contains|all:
            - 'delete'
            - 'shadows'
    selection_wmic:
        Image|endswith: '\wmic.exe'
        CommandLine|contains|all:
            - 'shadowcopy'
            - 'delete'
    condition: selection_vssadmin or selection_wmic
level: critical
tags:
    - attack.impact
    - attack.t1490
```


**Règle 4 — PsExec Remote Service :**

```yaml
title: PsExec Service Installation
logsource:
    product: windows
    service: system
detection:
    selection:
        EventID: 7045
        ServiceName: 'PSEXESVC'
    condition: selection
level: high
tags:
    - attack.lateral_movement
    - attack.t1021.002
```


**Règle 5 — Suspicious PowerShell Download :**

```yaml
title: Suspicious PowerShell Download Cradle
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\powershell.exe'
        CommandLine|contains:
            - 'Invoke-WebRequest'
            - 'wget'
            - 'curl'
            - 'DownloadString'
            - 'DownloadFile'
            - 'IWR'
    condition: selection
level: high
tags:
    - attack.execution
    - attack.t1059.001
    - attack.command_and_control
    - attack.t1105
```


---


## Annexe E — Templates SOC

### Template ticket d'incident

```
TICKET #[numéro] — [TITRE COURT]
Sévérité : [Critique/Haute/Moyenne/Basse]
Statut : [Ouvert/En investigation/Escalé/Clos]
Qualification : [VP/FP/BTP/Inconclusive]

RÉSUMÉ (2 lignes)
[Quoi — Qui — Quand]

CONTEXTE
  Règle : [nom de la règle, technique ATT&CK]
  Asset : [hostname, criticité]
  Utilisateur : [nom, département, niveau de privilège]

OBSERVATIONS (faits horodatés)
  [HH:MM:SS UTC — Source — Événement — Détail]

ANALYSE
  Hypothèse(s) : [description]
  Éléments confirmant/infirmant : [données]
  Conclusion : [VP/FP/BTP avec justification]

ACTIONS RÉALISÉES
  [Action — Horodatage — Résultat]

RECOMMANDATIONS
  [Actions restantes — Responsable — Délai]

ANALYSTE : [nom]    DATE : [date]    SHIFT : [horaire]
```


### Template SITREP d'escalade

```
⚠️ SITREP — [CLIENT] — [SÉVÉRITÉ]
Date/Heure : [UTC]    Analyste : [nom]

QUOI : [2 phrases résumant l'incident]
QUAND : [Timeline résumée]
QUI : [Comptes et systèmes impactés]
ACTIONS PRISES : [Ce qui a été fait]
ACTIONS RECOMMANDÉES : [Ce qui doit être fait]
CE QU'ON NE SAIT PAS : [Lacunes, incertitudes]

Prochaine mise à jour : [heure prévue]
```


---


## Annexe F — Playbooks de référence

### Playbook Phishing

1. Vérifier si l'email a été reçu par d'autres utilisateurs (email gateway → scope)
2. Vérifier les clics dans les logs proxy (URL visitée, POST effectué ?)
3. Si credentials soumis : reset mot de passe + révocation sessions Azure AD/M365 + vérification MFA
4. Vérifier les inbox rules (forwarding, redirection)
5. Vérifier les connexions suspectes post-clic (sign-in logs)
6. Bloquer domaine/URL au proxy et à l'email gateway
7. Vérifier SharePoint/OneDrive pour exfiltration
8. Notifier l'utilisateur et sensibiliser
9. Documenter et clôturer

### Playbook Ransomware (pré-déploiement détecté)

1. Isolation IMMÉDIATE des machines détectées (EDR containment)
2. Isolation réseau du segment (firewall — empêcher propagation)
3. Vérifier l'étendue (C2 contacté par d'autres machines ? shadow copies supprimées ailleurs ?)
4. Préserver les preuves (ne PAS redémarrer, ne PAS nettoyer)
5. Escalade IR immédiate + notification RSSI client
6. Identifier le vecteur d'accès initial (pour bloquer la re-infection)
7. Vérifier les backups (intégrité, accessibilité, non compromis)
8. NE PAS communiquer publiquement avant validation direction/juridique

---


## Annexe G — Ressources et formation

### Certifications

| Certification | Organisme | Focus | Niveau |
|--------------|-----------|-------|--------|
| CompTIA CySA+ | CompTIA | Analyse sécurité, SOC fondamental | Intermédiaire |
| BTL1 (Blue Team Level 1) | Security Blue Team | Investigation SOC, triage, SIEM | Intermédiaire |
| BTL2 (Blue Team Level 2) | Security Blue Team | Investigation avancée, hunting, IR | Avancé |
| SC-200 | Microsoft | Sentinel, MDE, M365 Defender | Intermédiaire |
| Splunk Core Certified User | Splunk | SPL fondamental | Débutant |
| GCIH (Incident Handler) | SANS/GIAC | IR et handling d'incidents | Avancé |
| GCIA (Intrusion Analyst) | SANS/GIAC | Analyse réseau et intrusion | Avancé |
| GCDA (Certified Detection Analyst) | SANS/GIAC | Detection engineering | Avancé |

### Plateformes d'entraînement

| Plateforme | Type | Focus |
|-----------|------|-------|
| CyberDefenders | CTF Blue Team | Investigations SOC avec datasets réels |
| LetsDefend | Simulation | Simulation SOC avec alertes, triage, investigation |
| TryHackMe | Parcours | Parcours SOC Analyst (L1 et L2) |
| Blue Team Labs Online | CTF | Investigations blue team variées |
| Boss of the SOC (BOTS) | Dataset Splunk | Compétition SOC sur datasets Splunk |
| SANS Cyber Ranges | Simulation | Exercices IR et SOC avancés |

### Datasets d'entraînement

| Dataset | Source | Contenu |
|---------|--------|---------|
| EVTX-ATTACK-SAMPLES | GitHub | Event Logs Windows simulant des attaques ATT&CK |
| SecurityDatasets (OTRF) | GitHub | Datasets multi-sources pour le hunting |
| Atomic Red Team | Red Canary | Tests unitaires par technique ATT&CK |
| SigmaHQ | GitHub | Règles Sigma communautaires (3000+) |

### Blogs et sources quotidiennes

| Source | Type | Pertinence SOC |
|--------|------|---------------|
| The DFIR Report | Blog | Intrusions complètes analysées pas à pas |
| Detection Engineering Weekly | Newsletter | Actualité du detection engineering |
| Sigma HQ Blog | Blog | Nouvelles règles, bonnes pratiques Sigma |
| Splunk Security Essentials | App Splunk | Use cases pré-construits avec SPL |
| Microsoft Sentinel Community | GitHub | Requêtes KQL, workbooks, playbooks |
| Elastic Security Labs | Blog | Recherche en détection, règles EQL |
| Red Canary Threat Detection Report | Rapport annuel | Techniques les plus observées par année |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former au métier d'analyste SOC tel qu'il se pratique réellement — pas dans sa version idéalisée des slides de certification, mais dans sa réalité quotidienne : le flux d'alertes, les faux positifs, les doutes, les pivots qui mènent à des impasses, et le moment où une alerte banale se révèle être le premier signal d'une intrusion critique.
>
> L'opération FALCONWATCH qui traverse les 34 premiers chapitres illustre cette réalité : Karim ne reçoit pas une alerte proprement packagée qui dit « vous êtes compromis par BlackBasta » — il reçoit une alerte sur un certutil + rundll32 qui pourrait être n'importe quoi, et il doit, couche après couche, requête après requête, pivot après pivot, reconstituer l'histoire de 48 heures d'intrusion pour comprendre que son client est à quelques heures d'un ransomware.
>
> Le Ch.38 (la journée de shift) est peut-être le chapitre le plus important du cours : il montre que le métier, c'est 80 % de FP traités avec rigueur et 20 % d'investigations qui comptent — et que la qualité du travail sur les 80 % de FP (documentation, tuning, recommandations) est ce qui permet de traiter les 20 % d'investigations critiques avec l'efficacité nécessaire.
>
> *Détecter • Investiguer • Répondre • Construire — avec rigueur et endurance.*
