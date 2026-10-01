---
title: 'Chapitre 3 — Le SIEM : pipeline, langages et requêtes'
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - Partie I — Fondations
  - index.md
---

*Ce chapitre traite le SIEM du point de vue de l'analyste — pas de l'architecte. L'objectif est de comprendre le pipeline (comment les logs deviennent des alertes), de maîtriser les langages de requête (pour investiguer), et de connaître les différences opérationnelles entre les SIEM majeurs (pour s'adapter rapidement à un nouvel environnement).*

## 3.1 Le pipeline SIEM

Le SIEM transforme des flux de logs bruts en alertes contextualisées. Le pipeline comprend 7 étapes.

La **collecte/ingestion** reçoit les logs depuis les sources via des agents (Splunk Forwarder, Elastic Agent, Beats), des protocoles réseau (syslog, SNMP), ou des APIs (connecteurs cloud). La **parsing** extrait les champs structurés du log brut (l'IP source, l'utilisateur, l'action, le résultat) à partir du texte brut — par regex, Grok patterns, ou parsers prédéfinis. La **normalisation** uniformise les noms de champs entre les sources (le champ « src_ip » dans une source, « SourceAddress » dans une autre, « srcip » dans une troisième → tous mappés vers un nom unique). Sans normalisation, la corrélation multi-sources est impossible. L'**enrichissement** ajoute du contexte (IP → géolocalisation + ASN + réputation, hostname → criticité depuis la CMDB, hash → score VirusTotal, utilisateur → département + niveau de privilège). L'**indexation** stocke les événements normalisés et enrichis pour une recherche rapide. La **corrélation** applique les règles de détection sur les événements indexés (une rafale de 4625 + un 4624 réussi depuis la même IP = brute force réussie). L'**alerting** génère une alerte quand les conditions d'une règle sont remplies, avec la sévérité, le contexte, et les entités concernées.

Le problème de la qualité du pipeline : si le parsing est mal configuré (un champ IP non extrait), la normalisation échoue, l'enrichissement est incomplet, et la corrélation ne matche pas — l'alerte ne se déclenche jamais. Le « data quality » est un enjeu permanent du SOC.

## 3.2 Splunk (SPL)

Splunk est le SIEM le plus répandu en entreprise. Son langage de requête — **SPL** (Search Processing Language) — est basé sur des pipes : chaque commande transforme les résultats et les passe à la suivante.

Requêtes essentielles pour l'analyste :

```
# Brute force : rafale de logons échoués par IP
index=windows EventCode=4625 
| stats count by src_ip, user 
| where count > 10 
| sort -count

# Process suspect : PowerShell encodé
index=sysmon EventCode=1 Image="*\\powershell.exe" CommandLine="*-enc*" 
| table _time host user CommandLine ParentImage

# Timeline utilisateur : toute l'activité d'un user
index=* user="marc.dubois" earliest=-24h 
| sort _time 
| table _time index sourcetype action src_ip dest_ip

# Connexions vers un C2 connu
index=firewall dest_ip="185.xx.xx.xx" 
| stats count values(src_ip) by dest_port 
| sort -count

# Beaconing : connexions régulières vers une destination
index=proxy dest="185.xx.xx.xx" 
| sort _time 
| streamstats current=f last(_time) as prev_time by src_ip 
| eval interval=_time-prev_time 
| stats avg(interval) stdev(interval) count by src_ip dest
```


Splunk ES (Enterprise Security) ajoute une couche SOC avec les **notable events** (alertes qualifiées), le **risk-based alerting** (agrégation de signaux faibles sur une entité — un utilisateur qui accumule des scores de risque dépasse un seuil et déclenche une alerte composite), les **investigations** (workspace collaboratif pour documenter les investigations), et les **data models** (CIM — Common Information Model, couche d'abstraction qui normalise les champs).

## 3.3 Elastic SIEM (KQL / EQL)

Elastic SIEM (Elastic Security) est la solution open-core basée sur la stack Elasticsearch + Kibana. Trois langages de requête coexistent.

**KQL** (Kibana Query Language) — simple, utilisé dans la barre de recherche :

```
event.code: "4625" and source.ip: 10.0.0.*
process.name: "powershell.exe" and process.args: "-enc"
```


**EQL** (Event Query Language) — le plus puissant pour les séquences d'événements (détection de chaînes d'attaque) :

```
sequence by host.name with maxspan=5m
  [process where process.name == "winword.exe"]
  [process where process.name == "cmd.exe" and process.parent.name == "winword.exe"]
  [process where process.name == "certutil.exe" and process.args : "*urlcache*"]
```


**ES|QL** — nouveau langage SQL-like :

```
FROM logs-* | WHERE event.code == "4625" | STATS count = COUNT(*) BY source.ip | WHERE count > 10
```


Elastic Security intègre des detection rules pré-construites mappées ATT&CK, un timeline view pour l'investigation, et un case management intégré.

## 3.4 Microsoft Sentinel (KQL Kusto)

Sentinel est le SIEM cloud-native de Microsoft, intégré à Azure. Son langage — **KQL** (Kusto Query Language, distinct du KQL Kibana) — est particulièrement puissant pour les agrégations et les jointures.

```
// Brute force réussi
SecurityEvent
| where EventID == 4625
| summarize FailCount=count() by TargetAccount, IpAddress
| where FailCount > 10
| join kind=inner (
    SecurityEvent | where EventID == 4624
) on TargetAccount, IpAddress

// Impossible travel
SigninLogs
| where ResultType == 0
| summarize by UserPrincipalName, IPAddress, Location, TimeGenerated
| sort by UserPrincipalName, TimeGenerated asc
```


Sentinel excelle dans les environnements Microsoft (connecteurs natifs M365, Azure, Defender) et propose des **analytics rules** (scheduled, NRT — near real-time, fusion — corrélation ML), des **workbooks** (dashboards), des **hunting queries** (KQL pour le hunting), et des **playbooks** via Logic Apps (SOAR intégré).

## 3.5 Comparaison opérationnelle pour l'analyste

Ce qui compte pour l'analyste au quotidien — pas pour l'architecte :

| Critère | Splunk | Elastic | Sentinel |
|---------|--------|---------|----------|
| Langage | SPL (pipe-based, très expressif) | KQL + EQL + ES\|QL (multiple) | KQL Kusto (SQL-like, puissant) |
| Force | Puissance SPL, écosystème mature, Splunk ES | EQL pour les séquences, open-core | Intégration Microsoft native, cloud |
| Faiblesse | Coût élevé (volume-based) | Complexité multi-langage | Azure only, dépendance cloud |
| EDR natif | Non (intégration via add-ons) | Elastic Defend | Microsoft Defender for Endpoint |
| SOAR natif | Splunk SOAR (séparé) | Via TheHive/Cortex | Logic Apps (intégré) |
| Transition | Si vous connaissez SPL, KQL s'apprend en 1 semaine | Si vous connaissez EQL, les séquences Sigma sont naturelles | Si vous connaissez SQL, KQL Kusto est intuitif |

L'analyste SOC moderne doit idéalement maîtriser **SPL + au moins un des deux KQL** (Kibana ou Kusto, selon l'environnement). Les annexes C fournissent les requêtes les plus courantes dans les 3 langages.

---
