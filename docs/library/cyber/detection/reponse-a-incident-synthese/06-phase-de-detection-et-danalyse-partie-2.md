---
title: Phase de détection et d’analyse — Partie 2
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident — synthèse.md
note: Réponse à incident — synthèse
up:
- - Réponse à incident — synthèse
  - index.md
---

- Une investigation cherche principalement à répondre à deux questions :

```
What happened?
+
How did it happen?
```

- Comprendre uniquement **ce qui s’est passé** ne suffit pas.
- Il faut aussi déterminer :
    - comment l’attaquant est entré ;
    - quels systèmes ont été touchés ;
    - quels outils / techniques ont été utilisés ;
    - jusqu’où l’attaque s’est propagée.

Sans cela, une simple reconstruction des systèmes risque de laisser intact le **même attack path**, permettant à l’adversaire de revenir. Markdown collé

```
Initial Access
→ Attack Path
→ Compromise
→ Remediation

Si Attack Path non corrigé
→ Recompromise possible
```

## Investigation

- L’investigation fonctionne comme un **processus cyclique** :

```
Initial Investigation Data
        ↓
Create / Identify IOCs
        ↓
Search for New Leads
        ↓
Identify Impacted Systems
        ↓
Collect & Analyze Data
        ↓
New IOCs / New Leads
        ↺
```


Les trois activités principales sont :

- création et utilisation d’**IOC** ;
- identification de nouvelles pistes et nouveaux systèmes compromis ;
- collecte et analyse des données associées.

*Enquete*
### Données d'enquête initiales

- L’enquête commence avec les informations limitées obtenues pendant le triage initial.
- Les conclusions doivent être construites à partir de **pistes validées** au fur et à mesure de l’investigation.

Il faut éviter le **tunnel vision** :

```
Known Malicious Tool Found
        ↓
"Everything must be related to this tool"
        ↓
Premature Conclusion
        ↓
Incomplete Scope
```

- Une investigation ne doit pas se focaliser uniquement sur :
    - un malware connu ;
    - une IP ;
    - un hash ;
    - une alerte particulière.
- De nouvelles hypothèses doivent être continuellement recherchées.
## IOC — Indicators of Compromise

- Un **IOC — Indicator of Compromise** est un artefact pouvant indiquer qu’une compromission a eu lieu.

Exemples :

```
IP Address
Domain
URL
File Hash
Filename
File Path
Registry Key
Mutex
Email Address
```

- Un IOC ne doit pas être interprété seul.
- Une IP peut être :
    - réellement malveillante ;
    - partagée par plusieurs services ;
    - réattribuée ;
    - utilisée temporairement ;
    - issue d’un CDN / cloud provider.

> **IOC hit ≠ preuve définitive de compromission**.
## Formats et outils pour les IOC

- Il existe plusieurs mécanismes permettant de représenter, partager ou rechercher des artefacts. 
### OpenIOC

- Format permettant de représenter des indicateurs de compromission de manière structurée.
### STIX — Structured Threat Information eXpression

- Standard utilisé pour représenter et échanger des informations de **Cyber Threat Intelligence**.
- Format machine-readable, généralement sérialisé en JSON.
- Peut contenir :
    - IOC ;
    - threat actors ;
    - malware ;
    - attack patterns ;
    - relations entre objets.

Exemple conceptuel :

```
Threat Actor
→ Malware
→ Infrastructure
→ IOC
→ Victim
```

Le cours montre par exemple un objet STIX décrivant un fichier en se basant sur le rapport https://www.cisa.gov/news-events/alerts/2025/08/06/cisa-releases-malware-analysis-report-associated-microsoft-sharepoint-vulnerabilities :

- filename ;
- size ;
- MD5 ;
- SHA-1 ;
- SHA-256 ;
- SHA-512 ;
- SSDEEP ;
- informations PE. Markdown collé
### YARA

- **YARA** permet de rechercher des patterns dans :
    - fichiers ;
    - mémoire ;
    - malware samples.

Exemple conceptuel :

```
Strings
+
Binary Patterns
+
Conditions
→ YARA Rule
```

> ⚠️ YARA n’est pas réellement un **format d’échange d’IOC comparable à STIX**. C’est avant tout un langage de règles permettant d’identifier des fichiers ou contenus correspondant à certains patterns.

```
STIX
→ CTI representation / exchange

YARA
→ Pattern-based detection
```

## IOC Search / Enterprise-Wide Hunting

- Une fois un IOC identifié, il faut pouvoir le rechercher sur l’ensemble de l’environnement.

```
IOC discovered on HOST-A
        ↓
Search Enterprise-Wide
        ↓
HOST-B → Hit
HOST-C → Hit
HOST-D → No Hit
```

- Cela permet de déterminer le **scope** réel de l’incident.

Le cours mentionne notamment :

- PowerShell ;
- WMI ;
- outils natifs ;
- outils tiers ;
- plateformes de sécurité centralisées.

Aujourd’hui, cette recherche peut également être réalisée via :

```
EDR
SIEM
XDR
Threat Hunting Platform
```

## Credential Hygiene pendant l’investigation

- Les analystes doivent éviter d’exposer des **credentials privilégiés** sur des machines potentiellement compromises.

Problème :

```
IR Admin Credentials
→ Compromised Host
→ Credential Exposure
→ Attacker obtains IR privileges
```

Il faut donc :

- utiliser des comptes IR dédiés ;
- réduire l’usage de credentials très privilégiés ;
- privilégier des mécanismes d’administration adaptés ;
- connaître précisément le comportement des outils utilisés.

- Le cours souligne notamment que différents modes d’utilisation d’un même outil peuvent laisser des artefacts ou exposer différemment les credentials.

> Principe : **Know Your Tools**. Une action d’investigation ne doit pas elle-même faciliter la compromission.
## Identification de nouvelles pistes et systèmes impactés
Après avoir recherché les IOC :

```
IOC Search
→ Hits
→ Validate
→ True Positive / False Positive
```

- Certains IOC peuvent être trop génériques.
- Tous les hits ne sont donc pas forcément liés à l’incident étudié.

Exemple :

```
filename = update.exe
→ beaucoup trop générique
→ nombreux False Positives possibles
```

Il faut :

- contextualiser les résultats ;
- éliminer les False Positives ;
- identifier les systèmes réellement compromis ;
- prioriser les systèmes susceptibles de fournir de nouvelles preuves.
## Identification de nouvelles pistes et systèmes impactés

Après avoir recherché les IOC :

```
IOC Search
→ Hits
→ Validate
→ True Positive / False Positive
```


- Certains IOC peuvent être trop génériques.
- Tous les hits ne sont donc pas forcément liés à l’incident étudié.

Exemple :

```
filename = update.exe
→ beaucoup trop générique
→ nombreux False Positives possibles
```


Il faut :

- contextualiser les résultats ;
- éliminer les False Positives ;
- identifier les systèmes réellement compromis ;
- prioriser les systèmes susceptibles de fournir de nouvelles preuves
## Cycle complet d’investigation

```
Initial Alert
      ↓
Initial Investigation
      ↓
IOC Creation
      ↓
Enterprise Search
      ↓
New Compromised Hosts
      ↓
Evidence Collection
      ↓
Forensic Analysis
      ↓
New IOC / Lead
      ↺
```


Ce cycle continue jusqu’à ce que l’équipe puisse raisonnablement déterminer :

```
How did they get in?
What did they do?
Which systems were affected?
What access do they still have?
How can we prevent recurrence?
```

## Utilisation de l’IA dans la détection et l’Incident Response
L’**Artificial Intelligence** pour assister les analystes dans le traitement d’un grand volume d’alertes et de données. Markdown collé
### Automated Triage & Alert Prioritization

```
Thousands of Alerts
→ AI Analysis
→ Correlation
→ Prioritized Cases
```


L’IA peut aider à :

- regrouper des alertes similaires ;
- identifier les systèmes impliqués ;
- mettre en évidence les événements importants ;
- réduire le bruit.
### Incident Correlation

Plusieurs alertes isolées peuvent appartenir à une seule attaque :

```
Alert 1 → Suspicious File
Alert 2 → chmod
Alert 3 → Execution
Alert 4 → Network Connection
          ↓
       Correlation
          ↓
      Attack Story
```


Le cours donne l’exemple d’**Elastic Attack Discovery**, qui utilise des LLM pour regrouper et résumer plusieurs alertes dans une vue cohérente de l’attaque. Markdown collé
### Timeline Reconstruction

L’IA peut aider à transformer :

```
Logs
+
Alerts
+
Hosts
+
Users
+
Timestamps
```


en :

```
Chronological Attack Sequence
```


et à associer certains comportements à **MITRE ATT&CK**.
### Automated Response Playbooks

Le cours mentionne aussi l’utilisation de l’IA dans l’automatisation de certaines réponses :

```
Detection
→ Analysis
→ Recommended / Automated Action
```


par exemple :

- enrichissement d’IOC ;
- triage ;
- création de case ;
- regroupement d’alertes ;
- déclenchement de playbooks.

Markdown collé
### Post-Incident Analysis

L’IA peut également assister dans :

- résumé de l’incident ;
- reconstruction de timeline ;
- corrélation de données ;
- identification de patterns ;
- préparation des lessons learned.

```
Incident Data
→ AI-assisted Analysis
→ Findings
→ Lessons Learned
```

### Limites de l’IA

À garder en tête dans tes notes :

```
AI
→ Assistance
≠ Ground Truth
```


- Les conclusions doivent être validées par l’analyste.
- Un modèle peut :
    - mal corréler des événements ;
    - produire des False Positives ;
    - manquer du contexte ;
    - halluciner une relation inexistante.

Donc :

```
AI Output
→ Analyst Validation
→ Evidence
→ Decision
```


L’IA accélère l’investigation, mais **ne remplace pas la validation forensique ni le raisonnement de l’analyste**.
## Vue globale — Detection & Analysis

```
Detection
   ↓
Initial Triage
   ↓
Contextualization
   ↓
IOC Creation
   ↓
Enterprise Search
   ↓
Identify Scope
   ↓
Collect Evidence
   ↓
Forensic Analysis
   ↓
Timeline Update
   ↓
New Leads / IOCs
   ↺
```


Le point central de cette partie est que l’investigation n’est **pas une recherche linéaire** : chaque preuve peut révéler de nouveaux IOC, de nouveaux systèmes ou de nouvelles pistes, ce qui relance le cycle jusqu’à obtenir une compréhension suffisamment complète de **l’accès initial, du comportement de l’adversaire, du scope et de l’impact réel de l’incident**.
