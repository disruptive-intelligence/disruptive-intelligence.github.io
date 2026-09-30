---
title: Annexe E — Templates
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Annexes
  - index.md
---

## Formulaire de chaîne de custody

```
CHAÎNE DE CUSTODY — PIÈCE N° [XX]

Affaire : [Nom de l'affaire / Nom de code]
Description de la pièce : [Type de support, modèle, numéro de série]
État à la collecte : [Allumé/éteint, état physique, connexions]

COLLECTE
  Date/Heure : [JJ/MM/AAAA HH:MM:SS, fuseau horaire]
  Collecté par : [Nom, qualité, organisme]
  Méthode : [Outil utilisé, version, paramètres]
  Hash MD5 : [________________________]
  Hash SHA-256 : [________________________]
  Lieu de stockage : [Coffre, numéro de casier]

TRANSFERTS
  | Date | De | À | Motif | Signature |
  |------|-----|-----|-------|-----------|
  | | | | | |

ANALYSES
  | Date | Analyste | Action | Outil | Hash vérifié ? |
  |------|----------|--------|-------|----------------|
  | | | | | |

Signature du responsable : _____________ Date : _____________
```


## Template rapport forensic (structure)

```
RAPPORT D'INVESTIGATION FORENSIC
[CONFIDENTIEL — DIFFUSION RESTREINTE]

1. RÉSUMÉ EXÉCUTIF (1-2 pages)
   - Contexte, mandat, conclusions principales, impact, recommandations

2. CADRE DE L'INVESTIGATION
   - Mandataire, périmètre, questions investigatives
   - Méthodologie, outils (noms, versions), environnement d'analyse

3. CHRONOLOGIE DES OPÉRATIONS
   - Acquisitions réalisées (avec hash et chaîne de custody)
   - Analyses menées (séquence chronologique)

4. FAITS CONSTATÉS
   - Chaque constatation : source, date, description, niveau de confiance
   - Distinction explicite : fait / déduction / hypothèse

5. ANALYSE ET INTERPRÉTATION
   - Timeline de l'intrusion
   - Mapping MITRE ATT&CK
   - Hypothèses concurrentes et test

6. CONCLUSIONS
   - Réponses aux questions investigatives
   - Niveaux de confiance explicites
   - Ce qui n'a pas pu être déterminé (angles morts)

7. RECOMMANDATIONS
   - Mesures correctives et préventives
   - Suggestions pour la procédure judiciaire (si applicable)

ANNEXES
  A. IoC complets (hash, domaines, IP, artefacts)
  B. Timeline détaillée
  C. Captures d'écran annotées
  D. Chaîne de custody de chaque pièce
  E. Configuration de l'environnement d'analyse
```


---
