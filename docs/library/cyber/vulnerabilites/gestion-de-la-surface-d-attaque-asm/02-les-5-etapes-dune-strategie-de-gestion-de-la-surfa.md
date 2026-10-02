---
title: Les 5 étapes d’une stratégie de Gestion de la Surface d’Attaque — ASM
source: Cyber/07 Vulnérabilités & MCS/Connaître & prioriser/Gestion de la surface d'attaque (ASM).md
note: Gestion de la surface d'attaque (ASM)
up:
- - Gestion de la surface d'attaque (ASM)
  - index.md
---

- Le cycle peut être résumé en **5 étapes fondamentales** :

```
1. Discovery & Mapping
        ↓
2. Classification & Risk Assessment
        ↓
3. Prioritization
        ↓
4. Remediation
        ↓
5. Continuous Monitoring
        ↺
```


> L’ASM est un **cycle continu** : la surveillance peut révéler de nouveaux actifs ou risques, ce qui relance le processus depuis la découverte.
### 1. Découverte & cartographie des actifs — Discovery & Mapping

- Identifier **tout ce qui constitue la surface d’attaque** de l’organisation.
- Nous devons d'abord savoir ce qu'il faut protéger du point de vue de la cybersécurité.
- Nous dressons une liste de tous les actifs (serveurs, équipements réseau, applications, bases de données, appareils IoT, etc.) lors de l'étape de découverte des actifs.
- Inclure les actifs :
    - internes ;
    - Internet-facing ;
    - cloud ;
    - SaaS ;
    - applications ;
    - APIs ;
    - serveurs ;
    - endpoints ;
    - network devices ;
    - domaines / sous-domaines ;
    - IoT ;
    - services exposés.

```
Asset Discovery
→ What do we own?
→ What is exposed?
→ What did we not know existed?
```


- L’objectif est d’obtenir un **inventaire aussi complet que possible** et de cartographier :
    - actifs ;
    - services ;
    - dépendances ;
    - points d’exposition.
#### Shadow IT

- La découverte doit également identifier les actifs :
    - inconnus ;
    - oubliés ;
    - non gérés ;
    - créés sans validation IT.

```
Unknown Asset
→ Unmanaged
→ Unpatched
→ Potential Entry Point
```

> Un actif que l’équipe sécurité ne connaît pas ne peut pas être correctement protégé.
### 2. Classification & Évaluation du risque — Classification & Risk Assessment

- Une fois les actifs découverts, ils doivent être **classifiés et analysés**.
- La classification permet de déterminer :
    - propriétaire ;
    - fonction ;
    - criticité métier ;
    - sensibilité des données ;
    - exposition réseau.

```
Asset
→ Owner
→ Business Function
→ Criticality
→ Exposure
```


Ensuite, analyser les risques associés :

- CVE ;
- software versions ;
- mauvaises configurations ;
- ports/services exposés ;
- credentials faibles ;
- permissions excessives ;
- technologies EOL/EOS ;
- absence de protections ;
- chemins d’attaque potentiels.
#### Évaluation contextuelle

- Une vulnérabilité ne doit pas être évaluée uniquement avec son score CVSS.

Il faut également considérer :

```
Risk
≈ Vulnerability
+ Exploitability
+ Exposure
+ Business Impact
+ Asset Criticality
```


Exemple :

```
CVSS 9.8
+
Internet-facing
+
Known Exploit
+
Critical Server
→ Very High Priority Risk
```

> **Vulnerability ≠ Risk** : le risque dépend aussi du contexte dans lequel la vulnérabilité existe.
### 3. Priorisation — Prioritization

- Tous les risques ne peuvent pas forcément être corrigés immédiatement.
- Il faut déterminer **ce qui doit être traité en premier**.

Critères importants :

- severity ;
- exploitability ;
- active exploitation ;
- exploit public ;
- Internet exposure ;
- business criticality ;
- données accessibles ;
- impact potentiel ;
- présence de compensating controls.

```
Detected Risks
→ Context
→ Ranking
→ Remediation Priority
```

#### Objectif

- Concentrer les ressources sur les risques les plus importants :

```
Critical + Exploitable + Exposed
→ Fix First
```

plutôt que :

```
High CVSS only
→ Automatically Fix First
```

> Une vulnérabilité moyenne sur un serveur directement exposé à Internet peut être plus urgente qu’une vulnérabilité critique sur un système isolé.
### 4. Remédiation — Remediation

- Corriger ou réduire les risques identifiés et priorisés.

Les actions peuvent inclure :

- patcher ;
- reconfigurer ;
- mettre à jour ;
- fermer un port ;
- désactiver un service ;
- supprimer une application ;
- réduire des permissions ;
- segmenter un système ;
- révoquer des credentials ;
- appliquer un compensating control ;
- retirer complètement un actif.

```
Risk Identified
→ Fix / Mitigate / Remove
→ Exposure ↓
```

#### Réduction de la surface d’attaque

- La remédiation ne consiste pas uniquement à patcher.

Exemple :

```
Unused Service
→ Disable

Unused Port
→ Close

Unused Application
→ Remove

Obsolete Server
→ Decommission
```

→ moins de composants exposés = moins de possibilités d’attaque.
#### Ownership

- Identifier clairement :
    - propriétaire de l’actif ;
    - équipe responsable ;
    - action à réaliser ;
    - délai de remédiation.

```
Finding
→ Owner
→ Action
→ Deadline
→ Verification
```

### 5. Surveillance continue — Continuous Monitoring

- La surface d’attaque change constamment.
- Il faut donc surveiller en continu :
    - nouveaux actifs ;
    - nouveaux services ;
    - nouvelles vulnérabilités ;
    - configuration drift ;
    - changements DNS ;
    - nouvelles expositions Internet ;
    - nouveaux cloud resources ;
    - changements de permissions.

```
Environment Changes
→ Detect
→ Reassess
→ Reprioritize
→ Remediate
```

#### Configuration Drift

- Un système correctement sécurisé aujourd’hui peut devenir vulnérable après :
    - changement de configuration ;
    - nouvelle application ;
    - ouverture de port ;
    - ajout d’un compte ;
    - changement d’architecture.

```
Secure Baseline
→ Change
→ Drift
→ New Exposure
```

#### Après remédiation

- Il faut également vérifier que la correction est réellement efficace :

```
Remediation
→ Rescan
→ Validate
→ Risk Reduced?
```


Puis le cycle recommence :

```
Continuous Monitoring
        ↓
New Asset / New Risk
        ↓
Discovery
        ↓
Assessment
        ↓
Prioritization
        ↓
Remediation
        ↺
```

### Automatisation — élément transversal

- L’automatisation intervient dans l’ensemble du cycle.

```
Discovery
Assessment
Prioritization
Remediation
Monitoring
      ↑
  Automation
```


Elle peut automatiser :

- asset discovery ;
- vulnerability scanning ;
- exposure detection ;
- risk scoring ;
- alerting ;
- ticket creation ;
- rescan après correction ;
- reporting.
### Résumé

```
1. Discovery & Mapping
→ Qu'est-ce que nous possédons et qu'est-ce qui est exposé ?

2. Classification & Risk Assessment
→ Quelles faiblesses existent et quel risque représentent-elles ?

3. Prioritization
→ Que devons-nous traiter en premier ?

4. Remediation
→ Comment supprimons-nous ou réduisons-nous le risque ?

5. Continuous Monitoring
→ Qu'est-ce qui a changé et quels nouveaux risques apparaissent ?
```


## Pourquoi l'ASM est important ?

- Lors de la phase de **Reconnaissance** de la Cyber Kill Chain, l’attaquant cherche à identifier :
    - systèmes exposés ;
    - services ;
    - technologies ;
    - vulnérabilités ;
    - points d’entrée potentiels.

```
Attacker Recon
→ Discover Attack Surface
→ Identify Weakness
→ Select Target
```

- Plus la surface exposée est grande, plus il existe de possibilités d’attaque.

```
Attack Surface ↑
→ Opportunities for Attack ↑
→ Cyber Risk ↑
```

> L’objectif de l’ASM est donc aussi de **voir son environnement comme un attaquant pourrait le voir**, notamment pour les actifs exposés publiquement.

## Avantages de l'ASM
### Réduction du risque de cyberattaque

- Identifier les vulnérabilités et situations à risque avant qu’un attaquant ne les exploite.
- Réduire les points d’entrée inutiles.
- Améliorer la visibilité sur les actifs.

```
Find Weakness First
→ Remediate
→ Attacker Opportunity ↓
```

### Réduction des pertes de données et financières

- Une meilleure visibilité et une réduction des faiblesses peuvent limiter :
    - data breaches ;
    - interruption de services ;
    - pertes financières ;
    - coûts de remediation.
### Protection de la réputation

- Une cyberattaque peut affecter :
    - confiance des clients ;
    - réputation ;
    - relations commerciales ;
    - revenus à long terme.
### Confiance des clients et partenaires

- Une organisation capable de démontrer une gestion rigoureuse de sa surface d’attaque renforce la confiance de ses :
    - clients ;
    - fournisseurs ;
    - partenaires.
