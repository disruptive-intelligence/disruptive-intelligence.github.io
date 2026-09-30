---
title: Annexe F — Templates de livrables
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Annexes
  - index.md
---

## F.1 Template flash alert (1-2 pages)

```markdown
# FLASH ALERT — [Titre court]

**Référence** : FA-YYYYMMDD-NNN
**Date** : YYYY-MM-DD HH:MM (UTC+2)
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Synthèse (3-5 lignes)
[Que se passe-t-il ? Pourquoi maintenant ? Quel niveau de confiance ?]

## Observation
[Faits factuels, sources, timestamps]

## Implication immédiate
[Pourquoi ça concerne le destinataire]

## Action recommandée
- [Action 1, immédiat]
- [Action 2, dans la journée]
- [Action 3, dans la semaine]

## Limites
[Incertitudes, ce qu'on ne sait pas]

## Source(s)
[URL, plateforme, capture en annexe]

## Annexes
- A : Capture(s) horodatée(s) et hachée(s)
- B : Hashes (SHA-256)
```


## F.2 Template intel note (3-8 pages)

```markdown
# INTEL NOTE — [Titre]

**Référence** : IN-YYYYMMDD-NNN
**Date de rédaction** : YYYY-MM-DD
**Version** : 1.0
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Executive Summary (½ page max)
[Réponses aux questions : que s'est-il passé ? Pourquoi est-ce important ? Que faut-il faire ? Quel niveau de confiance ?]

## Contexte
[Pourquoi cette note ? Quel événement déclencheur ? Quelles observations antérieures pertinentes ?]

## Observations
### Observation 1 : [Titre]
- Source, date, capture
- Description factuelle

### Observation 2 : [Titre]
[...]

## Analyse
[Interprétation, attribution, hypothèses testées, conclusions calibrées]

## Implications
[Risques pour le destinataire, impacts potentiels]

## Recommandations
1. **Immédiat (24-48h)** : [Action]
2. **Court terme (7 jours)** : [Action]
3. **Moyen terme (30 jours)** : [Action]
4. **Long terme (90 jours)** : [Action]

## Limites et incertitudes
[Ce qui n'est pas connu, ce qui pourrait changer l'analyse]

## Indicators (IoC)
[Adresses, domaines, hashes, pseudonymes — selon TLP]

## Annexes
A. Captures horodatées
B. Communications archivées
C. Analyses techniques
D. Chain of custody
```


## F.3 Template bulletin sectoriel mensuel

```markdown
# BULLETIN MENSUEL — Menaces dark web — [Secteur] — [Mois Année]

**Auteur** : [Nom]
**Période** : [Mois] YYYY
**Classification** : TLP:[]
**Destinataires** : []

## Synthèse exécutive (1 page)
[Tendances majeures du mois, événements significatifs, recommandations stratégiques]

## Statistiques du mois
[Nombre revendications ransomware, top 5 acteurs, volumes leak detected, etc.]

## Événements significatifs
[Top 5-10 événements affectant le secteur ce mois]

## Acteurs en évolution
[Nouveaux groupes, disparitions, restructurations]

## Tendances observées
[Patterns émergents, vecteurs montants, géographies]

## Cas remarquables
[1-3 cas illustratifs avec leçons]

## Recommandations actionnables
[Priorisées par horizon temporel]

## Veille à venir
[Quoi surveiller le mois prochain]

## Annexes
[Détails par catégorie, IoC consolidés, statistiques détaillées]
```


## F.4 Template rapport d'investigation (cas type DARKSTREAM)

```markdown
# RAPPORT D'INVESTIGATION — [Nom de l'opération]

**Référence** : INV-YYYYMMDD-NNN
**Date** : YYYY-MM-DD
**Version** : [N.N]
**Auteur principal** : [Nom]
**Investigateurs associés** : [Noms]
**Classification** : TLP:[]
**Destinataires** : [Liste]

## Executive Summary
[½ - 1 page max — tout ce qui compte si rien d'autre n'est lu]

## Mandat et cadre
- Donneur d'ordre, objectifs, contraintes
- Cadre légal, autorités impliquées
- Périmètre d'investigation

## Méthodologie
- Outils, sources, période d'investigation
- Personas utilisées
- Limites méthodologiques connues

## Phase 1 — Reconnaissance
[Description détaillée, captures pertinentes]

## Phase 2 — Authentification
[Méthodes, résultats, niveau de confiance]

## Phase 3 — Pivoting et corrélation
[Pivots effectués, résultats, graphes]

## Phase 4 — Analyse et attribution
[Hypothèses testées, conclusion calibrée]

## Phase 5 — Vérifications anti-désinformation
[False flags écartés, biais identifiés]

## Conclusions
[Synthèse des constatations]

## Implications pour le client
[Risques, impacts, échéances]

## Recommandations
[Priorisées, avec délais et destinataires]

## Limites et incertitudes
[Ce qui ne peut être conclu avec les moyens employés]

## Annexes
A. Captures forum (avec hashes)
B. Communications archivées
C. Échantillons et analyses
D. Analyse blockchain
E. IoC structurés (MISP/STIX)
F. Chain of custody
G. Note méthodologique
H. Bibliographie / sources externes
```


## F.5 Template fiche IoC

```markdown
# FICHE IoC — [Identifiant ou pseudonyme]

**Type** : [Pseudonyme / Adresse crypto / Domaine / IP / Hash / etc.]
**Valeur** : [Indicator]
**Classification** : TLP:[]
**Date première observation** : YYYY-MM-DD
**Date dernière observation** : YYYY-MM-DD
**Confiance** : [WEP : très probable / probable / possible]

## Description
[Contexte, lien avec quel acteur/groupe/campagne]

## Sources de l'observation
[Forum/marché, URL, post ID, captures]

## Liens connus
[Autres IoC liés : autres pseudonymes, wallets, domaines]

## Recommandation
[Bloquer / Surveiller / Enquêter]

## Source originale
[Référence du rapport / investigation]
```


## F.6 Template note IAB (pour suivi)

```markdown
# FICHE IAB — [Pseudonyme]

**Pseudonymes connus** : [Liste cross-forum]
**Forums présents** : [XSS, Exploit, BreachForums, etc.]
**Première observation** : YYYY-MM-DD
**Dernière observation** : YYYY-MM-DD

## Profil
- Ancienneté
- Style et qualité des posts
- Réputation observée
- Langues utilisées
- Fuseau horaire estimé

## Spécialisation
- Types d'accès vendus (VPN/RDP/Citrix/AD)
- Secteurs ciblés
- Géographies
- Niveau de privilèges typique

## Tarification observée
- Prix moyens demandés
- Évolutions

## Wallet crypto
- Adresses observées
- Cluster (lien Chainalysis/TRM si applicable)
- Exchanges traversés

## Réseau
- Voucheurs
- Acheteurs identifiés
- Partenaires fréquents

## Risque pour client
[Évaluation actualisée]

## Recommandations
[Surveillance, détection préventive, etc.]
```


---
