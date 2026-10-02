---
title: 'Chapitre 19 — Référentiels vulnérabilités utiles à la gouvernance : CVE, CWE, CVSS, EPSS, KEV'
source: Cyber/08 Gouvernance & résilience/Gouvernance & conformité/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - ../index.md
- - Partie IV — Sécurité opérationnelle vue GRC
  - index.md
---

_Avant de définir une politique de gestion des vulnérabilités, il faut parler le même langage. Ce chapitre pose les référentiels que la gouvernance utilise pour qualifier, prioriser, tracer et justifier les décisions. L’objectif n’est pas d’entrer dans la technique d’exploitation, mais de comprendre ce que chaque indicateur apporte — et ce qu’il n’apporte pas — dans une logique de pilotage, de conformité et d’auditabilité._

---

## 19.1 Pourquoi la gouvernance a besoin de ces référentiels

### Idée directrice

En GRC, le problème n’est pas seulement de “connaître les sigles”, mais de **disposer d’un vocabulaire commun** entre :

- RSSI,
- vulnerability manager,
- SOC,
- équipes infra / patching,
- auditeurs,
- direction.

### Points clés

- Les dashboards, rapports d’audit, tickets de remédiation, bulletins CTI et scans de vulnérabilités utilisent tous ces référentiels.
- Sans cadre commun, les arbitrages deviennent incohérents :
    - un CVSS élevé est pris comme une urgence absolue sans contexte ;
    - une CVE en KEV n’est pas traitée plus vite qu’une autre ;
    - EPSS est mal compris comme une preuve d’exploitation ;
    - la direction reçoit des chiffres sans lecture décisionnelle.
- La gouvernance a besoin de ces référentiels pour transformer des données techniques en **décisions traçables et défendables**.

### Message clé

**La GRC n’utilise pas ces référentiels pour faire de la technique ; elle les utilise pour encadrer la décision.**

---

## 19.2 CVE — l’identifiant de référence

### Points clés

- Une **CVE** est un identifiant unique associé à une vulnérabilité connue.
- Elle permet de relier :
    - bulletin éditeur,
    - scanner de vulnérabilités,
    - CTI,
    - ticket de remédiation,
    - exception,
    - audit,
    - incident éventuel.

### Angle GRC

- La CVE sert de **référence commune** dans les processus.
- C’est l’identifiant à conserver dans :
    - les rapports de vulnérabilités,
    - les décisions de traitement,
    - les exceptions,
    - les preuves d’audit,
    - les comptes rendus de comité.

### Message clé

**La CVE permet de parler exactement du même sujet dans toute la chaîne de gouvernance.**

---

## 19.3 CWE — la faiblesse sous-jacente et l’intérêt pour l’amélioration structurelle

### Points clés

- Une **CWE** décrit une catégorie de faiblesse :
    - contrôle d’accès insuffisant,
    - injection,
    - mauvaise validation d’entrée,
    - erreurs mémoire,
    - désérialisation, etc.
- Différence avec CVE :
    - **CVE** = vulnérabilité précise ;
    - **CWE** = famille de faiblesse.

### Angle GRC

- Très utile pour détecter des tendances :
    - plusieurs CVE sur une même famille de produits peuvent pointer vers la même faiblesse ;
    - plusieurs audits peuvent révéler un défaut systémique de développement, de configuration ou d’architecture.
- Intérêt pour :
    - plans d’action structurels,
    - secure by design,
    - exigences fournisseurs,
    - politique de développement sécurisé,
    - priorisation des efforts de remédiation à moyen terme.

### Message clé

**La CVE aide à traiter un cas ; la CWE aide à corriger une cause récurrente.**

---

## 19.4 CVSS — mesurer la sévérité technique d’une vulnérabilité

### Points clés

- Le **CVSS** est le référentiel de sévérité le plus utilisé pour exprimer la criticité technique d’une vulnérabilité.
- Expliquer simplement ce qu’il cherche à mesurer :
    - facilité d’exploitation,
    - conditions d’exploitation,
    - impact potentiel sur confidentialité, intégrité, disponibilité.
- Préciser qu’un score CVSS :
    - aide à comparer,
    - aide à prioriser,
    - mais ne suffit jamais seul.

### Angle GRC

- Le score CVSS est un **point de départ**, utile pour :
    - les dashboards,
    - la priorisation initiale,
    - la communication entre équipes,
    - la définition de seuils de rescoring.
- Mais la gouvernance doit explicitement empêcher une lecture naïve du type :
    - “9.8 = toujours urgence absolue”,
    - “5.5 = toujours secondaire”.

### Message clé

**CVSS donne une sévérité technique de référence ; la gouvernance décide ensuite comment l’utiliser.**

---

## 19.5 EPSS — introduire la probabilité d’exploitation dans la décision

### Points clés

- **EPSS** estime la probabilité qu’une vulnérabilité soit exploitée dans un horizon proche.
- Il ne mesure pas la sévérité technique, mais la **pression d’exploitation probable**.
- Deux CVE proches en CVSS peuvent avoir des profils EPSS très différents.

### Angle GRC

- EPSS est utile pour :
    - enrichir les règles de priorisation,
    - arbitrer entre plusieurs remédiations concurrentes,
    - alimenter les comités de sécurité,
    - justifier une accélération de traitement.
- Important de préciser :
    - EPSS n’est pas une preuve d’exploitation ;
    - c’est un **facteur de priorisation** parmi d’autres.

### Message clé

**CVSS dit “c’est grave techniquement”, EPSS aide à dire “ça risque d’être exploité bientôt”.**

---

## 19.6 KEV — quand la menace n’est plus théorique

### Points clés

- Le **KEV** recense les vulnérabilités connues comme exploitées dans le monde réel.
- Là, on ne parle plus de potentiel, mais d’**exploitation observée**.

### Angle GRC

- La présence en KEV change la posture de gouvernance :
    - raccourcissement des SLA,
    - priorisation au comité,
    - demande de suivi renforcé,
    - revue immédiate des actifs exposés,
    - potentiellement note d’alerte RSSI / DSI / COMEX selon le contexte.
- C’est un marqueur fort de **proportionnalité** et de **diligence** dans un contexte audit/conformité.

### Message clé

**KEV transforme une vulnérabilité théorique en sujet de gouvernance prioritaire.**

---

## 19.7 Bien distinguer les rôles de chaque référentiel

### Tableau de synthèse

|Référentiel|Ce qu’il dit|Ce qu’il ne dit pas|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on|Si elle est grave ou exploitée|
|**CWE**|Quelle faiblesse est en cause|Si un système précis est compromis|
|**CVSS**|Quelle est la sévérité technique|Quelle priorité absolue retenir chez nous|
|**EPSS**|Quelle est la probabilité d’exploitation|Si la vulnérabilité est déjà exploitée chez nous|
|**KEV**|Qu’elle est exploitée dans le réel|Quel est le niveau de risque précis dans notre SI|

### Message clé

**Aucun de ces référentiels, pris seul, ne suffit à décider. Leur valeur est dans leur combinaison.**

---

## 19.8 Ce que la gouvernance doit en faire concrètement

### Points clés

La gouvernance doit définir :

- quels référentiels sont retenus officiellement ;
- quelles sources sont considérées comme de référence ;
- qui lit quoi et à quel moment ;
- comment les scores et signaux alimentent :
    - la priorisation,
    - les SLA,
    - les exceptions,
    - la traçabilité,
    - les revues de risque,
    - les audits.

### Vers le chapitre suivant

Le **chapitre 20 — Politique de gestion des vulnérabilités : du score brut au score contextualisé** traite ensuite :

- le problème du score Base brut ;
- CVSS v4 et ses groupes Base / Threat / Environmental / Supplemental ;
- les rôles de requalification ;
- les SLA par score contextualisé ;
- la documentation et l’articulation avec ISO 27001, EBIOS RM et NIS2.

### Message clé

**Ce chapitre pose le vocabulaire ; le suivant posera les règles de décision.**

---

## 19.9 Fil rouge — COMPLIANCE : lecture gouvernance d’une vulnérabilité

> **📊 COMPLIANCE — Épisode X**  
> Marine reçoit un rapport de scan mentionnant plusieurs CVE “critiques” sur des serveurs exposés et internes. Avant de demander une remédiation générale en urgence, elle fait clarifier les éléments de lecture : quelles CVE sont réellement concernées, quelles faiblesses reviennent de manière récurrente, quelles vulnérabilités sont déjà connues comme exploitées, et lesquelles présentent une forte probabilité d’exploitation. Ce premier cadrage ne décide pas encore du SLA, mais il permet d’éviter deux erreurs classiques : traiter toutes les vulnérabilités comme équivalentes, ou s’appuyer sur le seul score brut sans tenir compte du contexte de menace.

## 19.10 Transition vers le chapitre 20

> Connaître les référentiels ne suffit cependant pas à piloter une gestion des vulnérabilités. La question décisive pour la gouvernance n’est pas seulement de savoir ce que signifie une CVE ou un score CVSS, mais de définir comment ces éléments seront utilisés dans l’organisation : qui peut requalifier, selon quelles règles, avec quels SLA, et avec quelle traçabilité. C’est l’objet du chapitre suivant.

---

---
