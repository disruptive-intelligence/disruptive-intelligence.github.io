---
title: Chapitre 3 — Ce que le FININT ne permet pas
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie I — Comprendre le renseignement financier
  - index.md
---

## Objectif du chapitre

Tracer la **frontière des limites** du FININT. Cette frontière n’est pas un défaut de la discipline — elle est sa marque de sérieux. Connaître ses limites est ce qui permet de produire un livrable défendable et de ne pas conduire un demandeur à des décisions disproportionnées.

## Le concept

Trois grandes catégories de limites se recoupent en pratique.

**Limites épistémiques** — des choses que le FININT ne peut pas savoir, faute de sources accessibles. Exemple : l’UBO d’un trust irrévocable régi par un droit étranger sans registre public.

**Limites légales** — des sources auxquelles l’analyste n’a pas accès en cadre ouvert (relevés bancaires détaillés, données fiscales individuelles, informations couvertes par le secret professionnel). Ces sources sont mobilisables uniquement par des autorités compétentes (CRF avec droits de communication, magistrats, services d’enquête).

**Limites méthodologiques** — un raisonnement par corrélation ne prouve pas la causalité. Un faisceau d’indices, même solide, n’est pas une preuve judiciaire.

## L’utilité opérationnelle

Connaître ces limites évite trois erreurs lourdes :

1. **Promettre ce qu’on ne livrera pas** — sape la crédibilité du service auprès du demandeur.
1. **Conduire à une décision disproportionnée** — un gel, une rupture de relation, une dénonciation publique fondés sur du renseignement présenté comme une preuve peuvent entraîner des contentieux.
1. **Affaiblir l’exploitabilité judiciaire** — un livrable mal calibré, qui mélange faits, inférences et opinions, est difficilement exploitable par un magistrat.

## Méthode — comment formaliser les limites dans un livrable

Toute note FININT comporte une section **« Lacunes »** explicite. Elle liste :

- Les **sources non consultées** (et pourquoi : indisponibilité, hors cadre légal, contrainte de temps).
- Les **juridictions non couvertes** (parce que l’enquête s’est bornée à un périmètre, ou parce qu’aucune coopération n’a été obtenue).
- Les **données manquantes** structurelles (registres opaques, secret bancaire local).
- Les **délais et conditions** sous lesquels certaines lacunes pourraient être levées (réquisition, MLA, dissémination Egmont).

Cette section n’est pas un aveu de faiblesse : c’est un **élément de qualité** qui permet au demandeur de calibrer ses propres décisions et qui rend l’analyste honnête.

## Mini-walkthrough — trois exemples concrets

**Exemple 1 — Identification UBO en juridiction opaque.** Sans coopération internationale ou sans accès à des leaks pertinents, l’identification du bénéficiaire effectif d’une société aux Îles Vierges Britanniques (BVI) est généralement *indéterminable* à partir des seules sources ouvertes. Mention explicite à porter dans le livrable : *« UBO non identifié à partir des sources mobilisées ; identification effective conditionnée à une coopération via Egmont avec la CRF locale »*.

**Exemple 2 — Origine des fonds.** Sans accès aux relevés bancaires en amont (réquisition), il n’est pas possible d’établir avec certitude l’origine d’un dépôt de 500 000 € sur un compte. On peut au mieux émettre des hypothèses calibrées. Mention : *« Les éléments observés sont compatibles avec H1 [revenus professionnels non déclarés], H2 [héritage non documenté], H3 [prête-nom]. La résolution requiert une réquisition judiciaire des relevés du compte source »*.

**Exemple 3 — Intentionnalité.** Le FININT décrit des comportements et leur compatibilité avec des schémas. Il ne décrit pas les intentions internes des personnes. Affirmer *« X savait qu’il blanchissait »* relève du tribunal, sur la base de preuves d’intention (correspondances, témoignages, expertises).

## Erreurs fréquentes

- **Présenter une corrélation comme une preuve** — *« Mr X et Mr Y figurent dans les Panama Papers, donc ils sont complices »*. Non — ils figurent dans une fuite documentaire ; cela alimente une hypothèse, pas une conclusion.
- **Attribuer une intention** sans preuve directe.
- **Considérer le silence comme une preuve** — l’absence de réponse à une sollicitation n’est pas un aveu.
- **Conclure à partir d’une seule source** — toute conclusion forte doit reposer sur **au moins deux sources indépendantes** (chapitre 33).

## Limites — méta

Même les limites évoluent : un registre fermé peut s’ouvrir (pression réglementaire, leak), une source nouvelle peut apparaître (DAC8 pour les transactions crypto, base UBO post-AMLA), une décision de justice peut élargir l’accès. L’analyste maintient une veille permanente sur l’évolution des sources (chapitre 30 — non, en l’occurrence chapitre 50).

## Lien avec le fil rouge

> **CLEARFLOW — Cartographier les zones d’ombre**
> 
> Avant même de commencer son analyse, Nassim dresse une carte des **zones d’ombre prévisibles** dans le dossier Haddad : (a) les UBO finaux des structures chypriote, émiratie et libanaise — accessibles seulement via Egmont ; (b) les flux non bancaires (espèces, hawala suspecté) — non observables directement ; (c) la qualification d’éventuels marchés publics ouest-africains opaques — accessible seulement via coopération locale. Il documente ces zones d’ombre dans son cadrage initial, ce qui permet au coordinateur de prioriser les coopérations à engager.

## Points clés à retenir

- Trois familles de limites : épistémiques, légales, méthodologiques.
- Toute note FININT comporte une section **Lacunes** explicite.
- Une corrélation n’est pas une preuve ; un silence n’est pas un aveu ; une présence dans un leak n’est pas une condamnation.
- Calibrer les limites au cadrage initial protège l’analyste, le service et le demandeur.

-----
