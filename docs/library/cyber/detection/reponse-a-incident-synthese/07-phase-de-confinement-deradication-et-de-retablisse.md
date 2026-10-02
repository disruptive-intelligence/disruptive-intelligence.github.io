---
title: Phase de confinement, d’éradication et de rétablissement
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident — synthèse.md
note: Réponse à incident — synthèse
up:
- - Réponse à incident — synthèse
  - index.md
---

Après avoir suffisamment compris :

- la nature de l’incident ;
- son impact ;
- les systèmes concernés ;
- le comportement de l’adversaire ;
- les principales pistes de compromission ;

on passe à la phase de **Containment → Eradication → Recovery**.

```
Detection & Analysis
        ↓
Containment
        ↓
Eradication
        ↓
Recovery
        ↓
Normal Operations
```


> ⚠️ En pratique, le confinement ne nécessite pas toujours d’attendre la fin complète de l’investigation. Si l’incident est actif ou menace de se propager, certaines actions de confinement peuvent être prises immédiatement, tout en poursuivant l’analyse.

## Confinement — Containment

- Objectif : **empêcher l’incident de continuer à se propager ou à causer davantage de dégâts**.
- Le confinement doit idéalement être :
    - coordonné ;
    - simultané sur les systèmes concernés ;
    - documenté ;
    - proportionné à l’impact métier.

```
Compromised Systems
→ Containment
→ Spread / Damage ↓
```


Un confinement mal coordonné peut alerter l’adversaire :

```
Attacker detects defensive action
→ Changes TTPs
→ Removes traces
→ Establishes new persistence
```


### Stratégie de confinement

Avant d’agir, il faut considérer :

- criticité du système ;
- impact métier d’une isolation ;
- propagation possible ;
- nécessité de préserver des preuves ;
- activité encore en cours ;
- capacité de l’adversaire à conserver un accès ;
- disponibilité de systèmes de remplacement.

```
Security Need
+
Business Impact
+
Evidence Preservation
→ Containment Decision
```

## Confinement à court terme — Short-Term Containment

- Actions rapides et généralement réversibles.
- Objectif :
    - stopper ou ralentir l’attaquant ;
    - limiter le blast radius ;
    - gagner du temps pour préparer une remédiation durable.

Exemples :

- isoler l’endpoint via EDR ;
- placer le système dans un VLAN isolé ;
- débrancher le réseau ;
- bloquer une IP / domaine ;
- appliquer temporairement une règle firewall ;
- désactiver temporairement un compte compromis ;
- rediriger un domaine C2 vers un **sinkhole**.

```
Compromised Host
→ Network Isolation
→ Attacker Communication X
```

### DNS Sinkholing

- Consiste à rediriger un domaine malveillant vers :
    - une adresse contrôlée par les défenseurs ;
    - une adresse non routable / inexistante.

```
Malware
→ c2.attacker.com
→ DNS Sinkhole
→ Controlled / Null Destination
```


Utilités :

- couper le C2 ;
- identifier d’autres machines infectées ;
- observer les tentatives de communication.
## Préservation des preuves

- Le confinement doit éviter autant que possible de détruire les artefacts utiles à l’investigation.

Avant une action destructive, envisager :

- memory dump ;
- disk image ;
- logs ;
- active connections ;
- process list ;
- volatile data.

```
Contain
≠
Destroy Evidence
```

- Le cours parle d’une sous-phase de **backup**, mais dans une logique DFIR il est plus précis de parler de :

```
Evidence Preservation
+
Forensic Acquisition
```

## Arrêt d’un système

- Éteindre une machine peut être nécessaire, mais entraîne la perte de données volatiles :

```
Shutdown
→ RAM lost
→ Active Connections lost
→ Processes lost
```

Avant un shutdown :

- évaluer la valeur des données volatiles ;
- obtenir l’autorisation nécessaire ;
- coordonner avec le métier ;
- documenter l’action.
## Confinement à long terme — Long-Term Containment

- Mesures plus durables permettant de maintenir l’environnement sécurisé jusqu’à l’éradication complète.

Exemples :

- changement / rotation de passwords ;
- révocation de sessions ;
- suppression de tokens ;
- firewall rules permanentes ;
- patching ;
- host-based IDS / EDR controls ;
- désactivation d’un service vulnérable ;
- arrêt d’un système à risque.

```
Temporary Containment
→ Stable Defensive State
→ Eradication
```

> Patcher un système compromis ne signifie pas que l’incident est terminé : l’attaquant peut déjà avoir installé une persistence, créé des comptes ou compromis d’autres systèmes.
## Rotation des credentials
Si une compromission d’identité est possible :

```
Password Reset Only
≠ Always Enough
```


Selon le cas, il peut être nécessaire de :

- changer passwords ;
- révoquer sessions ;
- invalider tokens ;
- renouveler secrets/API keys ;
- révoquer certificats ;
- désactiver comptes compromis.

Particulièrement important pour :

- privileged accounts ;
- service accounts ;
- domain accounts ;
- cloud identities.
## Éradication — Eradication

- Une fois l’incident contenu, l’objectif devient :

```
Remove Attacker
+
Remove Persistence
+
Remove Root Cause
```

L’éradication doit supprimer :

- malware ;
- backdoors ;
- webshells ;
- scheduled tasks ;
- malicious services ;
- comptes créés par l’attaquant ;
- persistence mechanisms ;
- fichiers malveillants ;
- configurations compromises.
### Root Cause

- Il ne suffit pas de supprimer le malware.
- Il faut éliminer **la cause ayant permis la compromission**.
- Exemple :

```
Malware Removed
+
Vulnerability Still Present
→ Reinfection Possible
```


La remédiation peut donc inclure :

- patch ;
- correction de configuration ;
- fermeture d’un service exposé ;
- suppression d’un compte faible ;
- activation MFA ;
- changement de credentials ;
- correction d’ACL ;
- durcissement ;
- segmentation supplémentaire.
## Reconstruction vs nettoyage

Selon le niveau de compromission :

```
Minor / Well-understood compromise
→ Clean / Remediate

Deep / Privileged compromise
→ Rebuild
```


Une reconstruction complète peut être préférable lorsque :

- Domain Admin / root compromis ;
- persistence inconnue ;
- rootkit ;
- intégrité du système impossible à garantir ;
- nombreux changements non maîtrisés.

```
Trusted Golden Image
→ Rebuild
→ Patch
→ Harden
→ Restore Data
```


---

## Restauration depuis backup

- Certains systèmes peuvent être restaurés depuis des sauvegardes fiables.

Mais :

```
Backup
→ Must be known-good
```


Il faut vérifier :

- date de compromission ;
- date du backup ;
- présence éventuelle du malware dans la sauvegarde ;
- intégrité des données restaurées.

> Restaurer un backup déjà compromis peut réintroduire l’attaquant.

---

## Hardening après compromission

L’éradication peut également servir à renforcer :

- système affecté ;
- systèmes similaires ;
- parfois l’ensemble de l’environnement.

Exemples :

- supprimer services inutiles ;
- appliquer patches ;
- renforcer ACL ;
- appliquer MFA ;
- activer EDR ;
- revoir segmentation ;
- renforcer logging.

```
Incident Findings
→ Hardening
→ Future Attack Surface ↓
```


---

## Rétablissement — Recovery

- Objectif : remettre les systèmes dans un **état de fonctionnement normal et fiable**.

```
Eradicated System
→ Validate
→ Restore
→ Production
```


Avant réintégration :

- vérifier que le système fonctionne ;
- vérifier l’intégrité des données ;
- confirmer que les malwares / persistence ont disparu ;
- vérifier patches et hardening ;
- tester services et dépendances.

---

## Réintégration progressive

Pour un incident important, il est préférable de restaurer progressivement :

```
Critical Services
→ Controlled Restoration
→ Validation
→ Additional Systems
→ Full Production
```


Cela limite le risque de remettre simultanément en production des systèmes encore compromis.

---

## Monitoring renforcé

Les systèmes restaurés doivent être surveillés plus intensivement.

À rechercher :

### Connexions inhabituelles

- utilisateur jamais vu sur l’hôte ;
- service account inhabituel ;
- authentification depuis une nouvelle source ;
- connexions à des horaires atypiques.

### Processus inhabituels

```
Unexpected Process
Unexpected Parent/Child
Unknown Binary
Suspicious Script
```


### Modifications système

- registry keys ;
- scheduled tasks ;
- services ;
- autoruns ;
- firewall rules ;
- startup folders.

```
Recovered Host
→ Enhanced Monitoring
→ Detect Recompromise
```


---

## Recompromise

Un système récemment restauré constitue une cible importante si l’attaquant possède encore :

- credentials valides ;
- persistence ailleurs ;
- accès C2 ;
- système compromis adjacent ;
- vulnerability non corrigée.

```
Attacker Still Present Elsewhere
        ↓
Recovered System
        ↓
Recompromise
```


→ le recovery doit donc être évalué à l’échelle de **tout l’environnement**, pas uniquement machine par machine.

---

## Recovery à grande échelle

Lors d’un incident majeur, le rétablissement peut durer :

- plusieurs jours ;
- plusieurs semaines ;
- parfois plusieurs mois.

### Première phase

Priorité aux **Quick Wins** :

- fermer expositions critiques ;
- rotation credentials ;
- MFA ;
- patching urgent ;
- segmentation ;
- suppression des easy targets.

### Phases suivantes

Changements structurels :

- redesign réseau ;
- amélioration IAM ;
- PAM ;
- nouvelles baselines ;
- hardening généralisé ;
- amélioration monitoring / detection ;
- refonte de certains systèmes.

```
Immediate Recovery
→ Quick Wins

Long-Term Recovery
→ Structural Improvements
```


---

## Différence entre les trois phases

|Phase|Objectif|
|---|---|
|**Containment**|Stopper la propagation et limiter les dégâts|
|**Eradication**|Supprimer l’attaquant, la persistence et la cause racine|
|**Recovery**|Restaurer les systèmes et reprendre les opérations normales|

```
Containment
→ Stop it

Eradication
→ Remove it

Recovery
→ Restore safely
```


## Workflow global

```
Incident Confirmed
        ↓
Containment Strategy
        ↓
Preserve Evidence
        ↓
Short-Term Containment
        ↓
Long-Term Containment
        ↓
Eradication
        ↓
Root Cause Remediation
        ↓
Rebuild / Restore
        ↓
Validation
        ↓
Recovery
        ↓
Enhanced Monitoring
        ↓
Normal Operations
```


Le point important est que **Containment, Eradication et Recovery ne sont pas simplement “isoler → nettoyer → rallumer”** : il faut préserver les preuves, empêcher l’adversaire de réagir, supprimer son accès et la cause racine, puis remettre progressivement les systèmes en production avec une surveillance renforcée.
