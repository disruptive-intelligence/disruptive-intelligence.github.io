---
title: 'Chapitre 14 — De l’indice au graphe : chaîne de raisonnement'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

Une fois l’indice initial exploité, l’enquête entre dans sa **phase exploratoire**. Construire le graphe de l’écosystème de l’acteur. Ce chapitre couvre la chaîne de raisonnement de l’analyste pour passer méthodiquement de l’indice au graphe documenté.

## 14.1 La distinction critique : observation, inférence, attribution

Trois niveaux à ne jamais confondre.

**Observation** : ce qu’on **voit** directement sur la blockchain. « L’adresse A a envoyé 10 BTC à l’adresse B le [date] ». Vérifiable, factuel.

**Inférence** : ce qu’on **déduit** des observations via raisonnement et heuristiques. « L’adresse B est probablement contrôlée par la même entité que A (heuristique de change) ». Probabiliste, justifiable.

**Attribution** : ce qu’on **affirme** sur l’identité ou la nature de l’entité. « Le cluster A-B est un wallet du groupe ransomware Akira ». Nécessite des **éléments externes** (recoupements OSINT, labels propriétaires, données KYC obtenues légalement).

**L’analyste sérieux** :

- Distingue ces niveaux dans son journal et ses rapports.
- Ne **promeut** pas une inférence en attribution sans preuve additionnelle.
- Calibre la confiance à chaque niveau.

## 14.2 La chaîne de raisonnement type

**Étape 1 — Identifier l’actif et la chaîne** (observation immédiate).

L’indice est sur quelle blockchain ? Quel actif ? Vérifications de base avant tout autre travail.

**Étape 2 — Vérifier l’existence de la transaction / activité de l’adresse** (observation).

L’indice n’est pas une fabrication. La transaction existe bien, l’adresse a bien l’historique attendu.

**Étape 3 — Lire la transaction / activité initiale en détail** (observation).

Toutes les composantes (inputs, outputs, value, logs, internal). Pas de raccourci.

**Étape 4 — Identifier les contreparties** (observation).

Qui sont les autres adresses dans la transaction. Lister sans interpréter encore.

**Étape 5 — Catégoriser les contreparties** (inférence).

Pour chaque contrepartie : est-ce un service connu (label) ? Une nouvelle adresse fraîche ? Une adresse à activité passée ? Catégorie initiale : exchange / mixer / bridge / wallet personnel inconnu / etc.

**Étape 6 — Suivre les flux pertinents** (observation + inférence).

Pour chaque contrepartie pertinente, lire ses transactions sortantes. Reconstituer le **chemin des fonds** post-réception.

**Étape 7 — Identifier les patterns** (inférence).

Peeling chain ? Consolidation ? Split ? Dépôt exchange ? Bridge ? Mixer ? Caractériser le type d’opération.

**Étape 8 — Formuler hypothèses** (inférence calibrée).

À partir des patterns, proposer des hypothèses sur la nature de l’activité (« blanchiment post-rançon », « collecte de victimes », « préparation cashout »).

**Étape 9 — Croiser avec sources externes** (recoupement).

Recherche OSINT sur les adresses, labels propriétaires, mentions publiques, base CTI Athéna interne.

**Étape 10 — Mettre à jour les fiches et le graphe** (documentation).

Synthétiser dans les fiches d’adresses + graphe global.

**Étape 11 — Itérer** (cycle).

Chaque nouvelle adresse identifiée comme pertinente devient indice de Étape 1. Le graphe s’étend.

## 14.3 Le piège de l’expansion sans bornes

**Erreur classique** : suivre **toutes** les adresses, à toutes les profondeurs. Le graphe explose. Au bout de 5 hops, on a des dizaines de milliers d’adresses, dont 99% sans rapport avec l’enquête initiale.

**Stratégie de bornage** :

**Profondeur limitée**. Ne pas dépasser 5-7 hops typiquement, sauf cas spécifique. Au-delà, le signal se perd dans le bruit.

**Filtrage par pertinence**. Ne suivre les adresses dont les flux sont significatifs (gros montants, patterns suspects). Ignorer les flux poussiéreux (dust).

**Stop conditions**. Arrêter sur :

- Dépôt exchange identifié → angle de coopération autorité, suivi terminé pour cette branche.
- Mixer / privacy coin → rupture de visibilité, documenter et passer.
- Adresse dormante (pas de mouvement depuis longtemps) → pas de progrès attendu.
- Cluster déjà attribué → information acquise.

**Priorisation continue**. Réévaluer hebdomadairement quelles branches méritent encore l’effort.

## 14.4 Distinguer un service d’un wallet utilisateur

Erreur fréquente : confondre une adresse de **service** (exchange, processeur de paiement, mixer) avec une adresse de **wallet utilisateur**.

**Signaux qu’une adresse est un service** :

**Volume très élevé**. Service principal d’exchange peut traiter des milliers de transactions par jour. Wallet utilisateur typique a quelques transactions par mois.

**Multi-counterparties**. Service interagit avec des centaines/milliers d’adresses différentes. Wallet utilisateur a un nombre limité de contreparties.

**Patterns automatisés**. Service consolide/dispatche selon patterns programmés (chaque 6h, chaque seuil atteint, etc.). Wallet utilisateur a des patterns plus erratiques.

**Solde stable ou cyclique**. Service maintient solde dans une fourchette opérationnelle. Wallet utilisateur peut avoir solde très variable.

**Labellisation**. Service souvent labellisé par les outils. Wallet rarement.

**Erreur si confusion** : analyser un service comme s’il était un acteur permet de l’attribuer à tort à l’acteur enquêté. Toutes les transactions d’un exchange ne sont pas des transactions de l’enquêteur — c’est l’**utilisateur final** dans le service qui compte.

## 14.5 Le raisonnement face à l’incertitude

Beaucoup d’observations sont **ambiguës**. L’analyste doit calibrer.

**Exemple typique** : adresse A envoie à adresse B 0,5 BTC. Adresse B est nouvelle, jamais vue.

Hypothèses possibles :

- B est une adresse de change de A (continuation interne).
- B est un wallet personnel de la même entité, géré séparément.
- B est un destinataire externe (paiement à un autre acteur).
- B est un dépôt exchange (bientôt vidé vers hot wallet de l’exchange).

Sans information additionnelle, **on ne peut pas trancher**. On documente toutes les hypothèses, on attend l’évolution (B fait quoi ensuite ?), on enrichit avec labels.

**Discipline** : ne pas trancher prématurément. Garder les hypothèses ouvertes. Ne refermer que quand des éléments solides arrivent.

## 14.6 Calibration WEP en pratique

L’analyste utilise un vocabulaire calibré (Words of Estimative Probability).

**Échelle type** (voir Annexe F pour matrice complète) :

|WEP              |Probabilité|Usage                                                               |
|-----------------|-----------|--------------------------------------------------------------------|
|Quasi-certain    |>95%       |Preuve directe, multiple corroboration. Rare dans l’OSINT pur.      |
|Très probable    |80-95%     |Multiple convergence, peu d’alternatives plausibles                 |
|Probable         |60-80%     |Convergence majoritaire, alternatives possibles mais moins probables|
|Possible         |40-60%     |Hypothèse parmi d’autres, pas dominante                             |
|Peu probable     |15-40%     |Possible mais des alternatives plus plausibles                      |
|Très peu probable|<15%       |Hypothèse marginale                                                 |
|Indéterminable   |N/A        |Données insuffisantes pour évaluer                                  |

**Bonne pratique** : utiliser **systématiquement** un WEP à chaque hypothèse formulée. Et expliciter ce qui pourrait faire évoluer le WEP (« si on apprend X, le WEP passerait à Y »).

## 14.7 Le journal d’enquête

Le **journal d’enquête** est la trace écrite quotidienne de la chaîne de raisonnement.

**Format type (Markdown)** :

```markdown
# Journal MIXSHADOW

## 2026-03-19

### 14:23 UTC — Suivi adresse Akira-BTC-007
- Observation : adresse a fait nouvelle transaction sortante.
- TXID : [hash]
- Lecture : peeling pattern continue, 0,4 BTC à external + 32,7 BTC à change.
- External destination : adresse fraîche, jamais vue.
- Action : créer fiche Akira-BTC-008 (external) et Akira-BTC-Change-008 (change).

### 14:45 UTC — Hypothèse sur Akira-BTC-008
- Pas encore d'activité sortante.
- Hypothèse : possible dépôt exchange (probable, 60%).
- Alternative : wallet personnel intermédiaire (possible, 30%).
- Alternative : OTC desk (possible, 20%).
- Surveillance : alerte Chainalysis activée pour mouvements futurs.

### 16:12 UTC — Réflexion sur progression globale
- 5 branches actives en parallèle.
- Branche peeling principale : 18 hops, 7,5 BTC dispersés, 27,5 BTC en circulation.
- Branche Ethereum/Tornado : 12 ETH déposés, sorties non analysées encore.
- Branche TRON/USDT : 290k USDT en dispersion.
- Décision : prioriser TRON + Bitcoin pour cette semaine. Tornado attend.
```


Ce journal **n’est pas le rapport final**. C’est la matière brute qui alimentera le rapport, mais aussi la **trace** pour reproduire/contester l’analyse plus tard.

-----
