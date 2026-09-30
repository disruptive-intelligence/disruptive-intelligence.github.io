---
title: Annexe C — Grille de cotation et template de note d'analyse
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Annexes
  - index.md
---

## Grille de cotation (format standard OTAN adapté CTI)

**Fiabilité de la source :**

| Code | Signification | Exemples CTI |
|------|--------------|-------------|
| A | Fiabilité certaine | Registre officiel, blockchain publique, document judiciaire |
| B | Généralement fiable | Rapport CTI éditeur reconnu (Mandiant, CrowdStrike, Recorded Future), base commerciale de référence |
| C | Assez fiable | Rapport chercheur indépendant, information partiellement recoupée |
| D | Pas toujours fiable | Message sur forum underground, témoignage anonyme |
| E | Peu fiable | Rumeur, information non sourcée |
| F | Non évaluable | Source inconnue, première utilisation |

**Fiabilité de l'information :**

| Code | Signification |
|------|--------------|
| 1 | Confirmée par des sources indépendantes |
| 2 | Probablement vraie (cohérente, logique) |
| 3 | Peut-être vraie (ni confirmée ni contredite) |
| 4 | Douteuse (informations contradictoires) |
| 5 | Improbable (contredit par la majorité) |
| 6 | Non évaluable |

## Template de note d'analyse

```
# NOTE D'ANALYSE — [TITRE DE L'INVESTIGATION]
## Classification : [INTERNE / CONFIDENTIEL / TLP:xxx]
## Date : [JJ/MM/AAAA]    Version : [X.X]    Analyste(s) : [Noms]

---

## 1. RÉSUMÉ EXÉCUTIF (1 page max)
[Contexte, question, conclusion principale, confiance, recommandations clés]

## 2. QUESTION ANALYTIQUE
[Formulation explicite de la question à laquelle la note répond]

## 3. FAITS ÉTABLIS
[Chaque fait coté : source (A-F), fiabilité (1-6)]

## 4. ANALYSE
### 4.1 Hypothèses concurrentes
[H1, H2, H3... avec ACH]
### 4.2 Cartographie de l'écosystème
[Graphe simplifié + description des clusters, hubs, brokers]
### 4.3 Analyse économique
[Chaîne de valeur, business model, flux financiers]
### 4.4 Évaluation de la résilience
[Points de concentration, dépendances critiques, substituabilité]

## 5. ANGLES MORTS ET LIMITES
[Ce que l'investigation n'a pas pu établir]

## 6. RECOMMANDATIONS
[Classées par priorité et faisabilité, avec impact estimé]

## ANNEXES
- A : IoC techniques (hashes, domaines, IP, wallets)
- B : Graphe complet (Maltego export)
- C : Journal de collecte
- D : Mapping MITRE ATT&CK
```


## Checklist de validation avant livraison

- [ ] Tous les faits sont cotés (source + fiabilité)
- [ ] Les hypothèses concurrentes sont formulées et testées
- [ ] Les niveaux de confiance sont explicites pour chaque conclusion
- [ ] Les angles morts sont documentés
- [ ] Les renvois croisés sont cohérents
- [ ] Le vocabulaire est harmonisé (pas de mélange affilié/opérateur, pas de confusion wallet/adresse)
- [ ] Le graphe est lisible et légendé
- [ ] Les recommandations sont actionnables (qui fait quoi, avec quels moyens)
- [ ] Le rapport est adapté au destinataire (CERT vs direction vs autorités)
- [ ] Le fil rouge (si applicable) est cohérent de bout en bout

---
