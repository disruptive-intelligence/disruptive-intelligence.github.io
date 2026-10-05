---
title: Backup — Sauvegarde
source: Cyber/08 Gouvernance & résilience/Résilience/Sauvegardes et reprise d'activité.md
note: Sauvegardes et reprise d'activité
up:
- - Sauvegardes et reprise d'activité
  - index.md
---

- Un **backup** est une copie des données conservée afin de pouvoir les restaurer si les données originales deviennent indisponibles, corrompues ou détruites.
- Les sauvegardes protègent notamment contre :
    - erreur humaine ;
    - panne matérielle / système ;
    - corruption de données ;
    - cyberattaque ;
    - catastrophe naturelle.

```
Original Data
    ↓
  Backup
    ↓
Restore si perte / corruption
```


> Un backup ne supprime pas le risque d’incident : il fournit surtout une **capacité de récupération** lorsque l’incident a déjà eu un impact sur les données.
## Importance des sauvegardes
### Protection contre la perte de données

- Une perte de données peut résulter de :
    - suppression accidentelle ;
    - panne système ;
    - attaque informatique ;
    - ransomware ;
    - corruption ;
    - destruction physique de l’infrastructure.

```
Data Loss
→ Backup disponible
→ Restore
→ réduction de l'impact
```

### Continuité des activités - Business Continuity

- Les organisations dépendent fortement de la disponibilité de leurs données et services.
- Une perte importante peut interrompre :
    - applications métier ;
    - production ;
    - services clients ;
    - opérations internes.
- Les backups contribuent donc à la **Business Continuity** en permettant de reprendre les opérations après un incident.
### Conformité réglementaire - Regulatory Compliance

- Certains secteurs imposent des exigences concernant :
    - sauvegarde des données ;
    - conservation ;
    - protection ;
    - capacité de restauration.
- Une stratégie correctement documentée facilite également les **audits**.

> Les exigences exactes de conservation et de sauvegarde dépendent de la réglementation et du contexte de l’organisation.
### Customer Trust

- Une perte de données peut entraîner :
    - perte de confiance des clients ;
    - atteinte à la réputation ;
    - interruption de service ;
    - impacts financiers.
- Les sauvegardes permettent de réduire l’impact opérationnel d’un incident, même si elles ne peuvent pas empêcher à elles seules une fuite de données.

```
Backup → protège contre la perte
Backup ≠ empêche l'exfiltration
```

### Reprise des données (Reprise après sinistre) - Disaster Recovery

- Les sauvegardes constituent un élément essentiel du **Disaster Recovery (DR)**.
- Exemples de scénarios :

```
Datacenter détruit
Cyberattaque majeure
Ransomware
Panne critique
    ↓
Backup
    ↓
Recovery
```


> **Backup ≠ Disaster Recovery** : le backup correspond principalement aux copies des données, alors que le DR englobe l’ensemble des procédures, infrastructures et priorités permettant de remettre les systèmes en fonctionnement.
## Stratégie de sauvegarde

- Une sauvegarde efficace doit être :
    - réalisée régulièrement ;
    - protégée contre les accès non autorisés ;
    - suffisamment indépendante de la production ;
    - conservée pendant une durée adaptée ;
    - **testée en restauration**.

```
Backup créé
≠ données réellement récupérables

Restore Test
→ vérifie que le backup fonctionne
```

- Une stratégie de récupération prend généralement en compte :

```
RPO → quantité maximale de données acceptable à perdre
RTO → durée maximale acceptable avant restauration
```

- Ces objectifs déterminent notamment la fréquence des backups et la rapidité attendue du processus de recovery.
