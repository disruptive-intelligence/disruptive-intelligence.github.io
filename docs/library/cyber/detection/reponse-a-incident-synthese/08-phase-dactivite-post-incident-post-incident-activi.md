---
title: Phase d’activité post-incident — Post-Incident Activity
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident — synthèse.md
note: Réponse à incident — synthèse
up:
- - Réponse à incident — synthèse
  - index.md
---

- Une fois l’incident résolu, l’objectif est de :
    - documenter ce qui s’est passé ;
    - évaluer l’efficacité de la réponse ;
    - identifier les causes profondes ;
    - améliorer les contrôles de sécurité ;
    - mettre à jour les procédures ;
    - capitaliser sur les **Lessons Learned**.

```
Incident Resolved
        ↓
Post-Incident Review
        ↓
Lessons Learned
        ↓
Root Cause Analysis
        ↓
Improvements
        ↓
Better Preparation
        ↺
```


- Cette phase permet de transformer un incident en **amélioration mesurable de la posture de sécurité**.

---

## Post-Incident Review — PIR

- Une réunion de **Post-Incident Review** est généralement organisée quelques jours après l’incident.
    
- Elle réunit les stakeholders impliqués :
    
    - Incident Response ;
    - SOC ;
    - IT / Infrastructure ;
    - Security Engineering ;
    - management ;
    - Legal / Compliance ;
    - éventuellement métiers concernés.

Objectifs :

```
What happened?
What worked?
What failed?
Why?
What should change?
```


> L’objectif n’est pas de rechercher un responsable individuel, mais d’identifier les défaillances de **processus, contrôles, architecture ou organisation** ayant contribué à l’incident.
## Rapport final d’incident

Le **Final Incident Report** constitue la référence officielle de l’incident.

Il doit permettre de comprendre :

- ce qui s’est passé ;
- quand ;
- comment ;
- quels systèmes ont été affectés ;
- quel impact a été observé ;
- comment l’organisation a répondu ;
- quelles mesures ont été prises ;
- quelles améliorations sont nécessaires.

### Contenu typique

```
Executive Summary
Incident Timeline
Technical Findings
Affected Assets
Root Cause
Containment Actions
Eradication Actions
Recovery Actions
Business Impact
Lessons Learned
Recommendations
```


---

### Questions auxquelles répondre

#### Que s’est-il passé ?

- vecteur initial ;
- actions adverses ;
- systèmes compromis ;
- données affectées ;
- timeline.

```
Initial Access
→ Execution
→ Persistence
→ Lateral Movement
→ Impact
```


---

#### Comment l’équipe a-t-elle répondu ?

Comparer les actions réalisées avec :

- Incident Response Plan ;
- playbooks ;
- procedures ;
- policies.

```
Expected Procedure
        vs
Actual Response
```


Identifier :

- procédures efficaces ;
- étapes manquantes ;
- actions trop lentes ;
- problèmes de coordination.

---

#### Les informations nécessaires étaient-elles disponibles ?

Évaluer notamment :

- asset inventory ;
- network diagrams ;
- logs ;
- baselines ;
- contacts ;
- accès privilégiés ;
- documentation.

Exemple :

```
Need firewall logs
→ logs unavailable
→ investigation delayed
```


→ devient un **gap à corriger**.

---

#### Quelles actions ont permis de contenir et éradiquer l’incident ?

Documenter :

- isolation des hosts ;
- firewall rules ;
- account disablement ;
- password / token rotation ;
- malware removal ;
- rebuild ;
- patching ;
- hardening.

---

#### Comment empêcher la récurrence ?

Exemples :

```
Root Cause
→ Weak Password
→ MFA + Password Policy

Root Cause
→ Vulnerable Internet-facing Service
→ Patch + Reduce Exposure

Root Cause
→ Excessive Privileges
→ Least Privilege + PAM
```


---

#### Que faut-il améliorer pour mieux détecter l’incident ?

Identifier les **detection gaps**.

Exemple :

```
Attacker used T1003.001
→ no alert generated
→ create LSASS access detection
→ validate with Purple Team
```


Améliorations possibles :

- nouvelles SIEM rules ;
- EDR detections ;
- additional logging ;
- Threat Intelligence ;
- monitoring réseau ;
- nouveaux IOC ;
- ATT&CK mappings.

---

## Root Cause Analysis — RCA

- La **Root Cause Analysis** cherche à identifier pourquoi l’incident a pu se produire, et pas uniquement ce que l’attaquant a fait.

```
Incident
→ Immediate Cause
→ Contributing Factors
→ Root Cause
```


Exemple :

```
Account Compromise
        ↓
Password stolen through phishing
        ↓
No MFA
        ↓
Privileged account usable remotely
        ↓
Insufficient identity controls
```


> Supprimer uniquement le malware traite un **symptôme**. Une RCA vise à éliminer les conditions ayant permis l’incident.

---

### Contributing Factors

Un incident possède rarement une seule cause.

Exemple :

```
Incident
├─ Unpatched System
├─ Internet Exposure
├─ Weak Credentials
├─ No MFA
├─ Excessive Privileges
└─ Insufficient Monitoring
```


→ la remédiation doit donc souvent porter sur plusieurs couches.

---

## Lessons Learned

Les **Lessons Learned** identifient :

```
What worked?
What did not work?
What was missing?
What should be changed?
```


Exemples :

### Ce qui a fonctionné

- EDR a détecté l’attaque ;
- segmentation a limité le lateral movement ;
- backups étaient utilisables ;
- équipe IR disponible rapidement.

### Ce qui doit être amélioré

- logs insuffisants ;
- playbook incomplet ;
- inventaire obsolète ;
- communication trop lente ;
- permissions excessives ;
- manque de formation.

---

## Mise à jour des procédures

Après l’incident, mettre à jour si nécessaire :

- Incident Response Plan ;
- policies ;
- procedures ;
- playbooks ;
- escalation paths ;
- contact lists ;
- forensic procedures.

```
Incident Experience
→ Update Playbooks
→ Future Response Faster
```


Exemple :

```
Ransomware Incident
→ missing isolation procedure
→ update Ransomware Playbook
```


---

## Amélioration des règles de détection

Les artefacts découverts pendant l’enquête peuvent devenir de nouvelles capacités de détection.

```
Incident Evidence
→ IOC / TTP
→ Detection Engineering
→ New Detection Rule
```


Exemples :

- Sigma rules ;
- SIEM queries ;
- YARA rules ;
- EDR detections ;
- network signatures.

---

### IOC vs TTP

```
IOC
→ hash / IP / domain
→ utile immédiatement
→ souvent facilement modifiable

TTP Detection
→ comportement
→ plus durable
```


Les techniques MITRE ATT&CK observées pendant l’incident peuvent donc servir à mesurer la couverture défensive.

---

## Validation des nouvelles détections

Une règle créée après l’incident doit être **testée**.

```
Incident TTP
→ Create Detection
→ Purple Team / Replay
→ Detection Works?
├─ Yes → Deploy
└─ No  → Tune
```


→ évite de considérer une nouvelle règle comme efficace sans validation.

---

## Knowledge Sharing

- Les connaissances acquises doivent être partagées avec les équipes appropriées.

Exemples :

- SOC ;
- Incident Response ;
- Detection Engineering ;
- IT ;
- Threat Hunting ;
- Vulnerability Management ;
- Red / Purple Team.

```
Incident Knowledge
→ Documentation
→ Team Training
→ Future Investigations
```


Un ancien incident peut devenir :

- training material ;
- playbook ;
- hunting hypothesis ;
- detection use case.

---

## Formation des analystes

Les rapports d’incident sont particulièrement utiles pour former les nouveaux membres.

Ils permettent d’étudier :

```
Alert
→ Investigation
→ Evidence
→ Decision
→ Containment
→ Recovery
```


et de comprendre **pourquoi** certaines décisions ont été prises.

---

## Évaluation de la capacité IR

La phase post-incident doit également évaluer :

### People

- compétences ;
- disponibilité ;
- staffing ;
- répartition des rôles.

### Processes

- playbooks ;
- escalation ;
- communication ;
- coordination.

### Technology

- SIEM ;
- EDR ;
- forensic tools ;
- logging ;
- case management.

```
People
+
Processes
+
Technology
→ Incident Response Capability
```


---

## Metrics — Mesure de la réponse

Les rapports permettent de produire des métriques sur l’efficacité du programme IR.

Exemples :

```
Number of Incidents
Time to Detect
Time to Contain
Time to Recover
Incident Severity
Systems Affected
```


### MTTD — Mean Time To Detect

```
Compromise
→ Detection
```


Temps moyen nécessaire pour détecter un incident.

### MTTC — Mean Time To Contain

```
Detection
→ Containment
```


Temps nécessaire pour limiter la propagation.

### MTTR

Selon l’organisation, `MTTR` peut désigner :

- Mean Time To Respond ;
- Mean Time To Remediate ;
- Mean Time To Recover.

> Toujours préciser la définition utilisée, car l’acronyme n’est pas interprété de manière uniforme.

### Mean Time to Inventory (MTTI)

## Impact & coûts

Le rapport peut également servir à évaluer :

- downtime ;
- pertes de données ;
- heures de travail ;
- coûts forensiques ;
- coût de restauration ;
- pertes commerciales ;
- coûts juridiques ;
- impact réputationnel.

```
Technical Impact
+
Operational Impact
+
Financial Impact
→ Business Impact
```


---

## Aspects juridiques

Un rapport d’incident peut devenir une pièce importante lors :

- d’une enquête ;
- d’un audit ;
- d’un contentieux ;
- d’une procédure réglementaire.

Il faut donc conserver :

- timeline ;
- preuves ;
- Chain of Custody ;
- décisions ;
- actions effectuées ;
- responsables des actions.

```
Evidence
+
Chain of Custody
+
Incident Report
→ Defensible Investigation
```


---

## Reporting à la direction

Le rapport destiné au management ne nécessite généralement pas le même niveau de détail qu’un rapport technique.

### Rapport technique

```
Logs
IOCs
TTPs
Timeline
Forensics
Hosts
Commands
```


### Executive Report

```
What happened?
Business impact?
Is the threat removed?
What remains at risk?
What must be improved?
```


→ adapter le niveau d’information au public cible.

---

## Clôture de l’incident

Un incident ne devrait être clôturé qu’après avoir vérifié que :

- containment terminé ;
- eradication terminée ;
- recovery validé ;
- monitoring renforcé effectué ;
- documentation terminée ;
- actions correctives identifiées ;
- responsables désignés.

```
Incident Resolved
        ↓
Final Report
        ↓
Lessons Learned
        ↓
Corrective Actions
        ↓
Owners + Deadlines
        ↓
Case Closure
```


> Les recommandations sans responsable ni échéance risquent de ne jamais être appliquées.

---

## Boucle d’amélioration continue

La phase post-incident revient directement alimenter la phase de préparation :

```
Preparation
    ↓
Detection & Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Post-Incident Activity
    ↓
Lessons Learned
    ↓
Improved Preparation
    ↺
```


Le but n’est donc pas simplement de déclarer **« incident terminé »**, mais de s’assurer que l’organisation ressort de l’incident avec de meilleurs **contrôles, détections, procédures, outils et compétences** qu’avant celui-ci.
