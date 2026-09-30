---
title: Chapitre 36 — Les outils
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

> Chapitre volontairement placé en trente-sixième position sur quarante, et volontairement resserré. **Vous savez désormais pourquoi ces outils existent** — c'est ce qui permet de les traiter en quelques pages plutôt qu'en un tiers du cours.

## 36.1 Ce qu'une plateforme de renseignement fait, et ne fait pas

| Elle fait | Elle ne fait pas |
|---|---|
| Ingérer, normaliser, dédoublonner | **Décider ce qui vous concerne** |
| Enrichir automatiquement | Évaluer une source (§10) |
| Conserver un historique | Produire un jugement (§11) |
| Diffuser vers d'autres outils | Formuler un besoin (§14) |
| Gérer des marquages de diffusion | Écrire pour un destinataire (§26) |

**La colonne de droite contient l'essentiel du métier.** Une plateforme est un outil de gestion de matière première ; elle ne remplace aucun des chapitres 4 à 13.

**Ce qui justifie d'en avoir une** : le volume. En dessous d'un certain seuil — quelques centaines d'éléments par mois — un tableur et une discipline suffisent, et coûtent infiniment moins cher à maintenir.

## 36.2 Les formats structurés

**Pourquoi structurer** : permettre l'échange machine à machine et l'automatisation. C'est tout.

| Format | Rôle | Ce qu'il exprime bien | Ce qu'il exprime mal |
|---|---|---|---|
| **STIX** | Représentation d'objets de renseignement et de leurs relations | Indicateurs, campagnes, acteurs, relations | **Le raisonnement, la nuance, le niveau de confiance argumenté** |
| **TAXII** | Protocole d'échange | Collections, canaux, abonnements | — |
| **Formats d'analyste alternatifs** | Représentation de contexte et d'opinion | L'appréciation, la note d'analyste | Standardisation moindre |

**La limite structurelle à retenir**, et elle vaut au-delà de tout format particulier :

> **Un format structuré transporte des objets, pas des jugements.** La phrase *« nous estimons probable X — confiance moyenne, parce que les deux sources ne sont pas indépendantes »* ne se met dans aucun champ. Elle se transporte en prose, dans un produit écrit.

**La conséquence pratique** : les formats structurés servent le niveau tactique (§3.3) et le partage automatisé. Ils ne servent pas les niveaux opérationnel et stratégique, qui restent affaire d'écriture.

## 36.3 Collecte, normalisation, déduplication, enrichissement

**Ce qui s'automatise bien** :

| Tâche | Gain |
|---|---|
| Ingérer plusieurs formats | Élevé |
| Dédoublonner | Élevé |
| Enrichir techniquement — résolution, réputation, géographie | Moyen |
| **Rapprocher avec l'inventaire** | **Très élevé — et c'est le plus négligé** |
| Diffuser vers la détection | Élevé |
| Appliquer une date d'expiration | **Élevé, et rarement fait** (§30.6) |

**La quatrième ligne est celle qui produit le plus de valeur** : rapprocher automatiquement un élément entrant avec l'inventaire répond au nœud ① de l'arbre d'exploitation (§29.2) — *est-ce applicable chez nous ?* — qui est la question la plus fréquente et la plus mécanique du métier.

## 36.4 ⚠️ Automatiser un raisonnement absent

**Le risque central du chapitre.**

| Ce qu'on automatise | Ce qui se passe si le raisonnement manque |
|---|---|
| L'ingestion | On accumule (§14.6) |
| Le blocage automatique | On bloque des ressources légitimes (§24.5) |
| La diffusion automatique | On sature les destinataires |
| Le scoring automatique | On prend un chiffre pour un jugement |

**La formulation qui résume** :

> **Un outil accélère ce que vous faites. Si ce que vous faites est mal fondé, il accélère l'erreur.**

C'est la même conclusion qu'au cours MCS, et pour la même raison : l'automatisation ne crée aucune capacité de décision.

## 36.5 L'assistance automatisée à l'analyse

**Les usages réellement utiles aujourd'hui, dans le périmètre de ce cours** :

| Usage | Valeur | Précaution |
|---|---|---|
| Résumer un rapport long | Élevée | Vérifier les affirmations reprises **à la source** |
| Traduire | Élevée | Attention aux nuances de calibrage |
| Reformuler pour un destinataire | Moyenne | La conclusion ne doit pas bouger (§26.1) |
| Générer des hypothèses alternatives | **Élevée** | Contre le biais de confirmation, c'est un usage pertinent |
| Extraire des indicateurs d'un texte | Élevée | Vérifier le contexte et la date |
| Rédiger une première version | Moyenne | La relecture reste entière |

**Le risque spécifique**, et il faut le nommer précisément :

> **Une sortie plausible mais fausse est plus dangereuse qu'une absence de réponse, parce qu'elle ne déclenche aucune vérification.**

Une version affectée inexacte, une source inventée, une affirmation attribuée à tort à un rapport : ces erreurs ont la forme d'une information correcte. Elles passent les relectures rapides.

✅ **BONNE PRATIQUE (P0)** — Toute affirmation issue d'une assistance automatisée et destinée à fonder une décision est **vérifiée à la source**. Le statut du §4.6 s'applique intégralement : une sortie d'outil n'est pas un fait, c'est une source — et une source dont la chaîne de provenance est opaque.

⚠️ **Le point aveugle** : ces outils sont particulièrement enclins à produire des synthèses cohérentes à partir de sources circulaires, parce qu'ils ne distinguent pas trois reprises d'une source unique de trois observations indépendantes. Le §10.4 s'applique avec une acuité accrue.

## 36.6 📌 Coût d'intégration et dette d'outillage

| Coût | Ordre de grandeur |
|---|---|
| Licence | Visible, souvent le plus faible |
| **Intégration initiale** | Souvent supérieur à la licence |
| **Maintenance des connecteurs** | Récurrent, croissant avec le nombre de sources |
| Formation | Ponctuel |
| **Migration en cas de changement** | Élevé, et l'historique est rarement portable |

**La dette d'outillage** : chaque connecteur, chaque règle de normalisation, chaque automatisme est un actif à maintenir. Une chaîne non maintenue casse silencieusement — et personne ne s'en aperçoit avant qu'une information importante ne soit pas passée.

✅ **BONNE PRATIQUE (P1)** — Surveillez vos automatismes : date de dernière exécution réussie, volume traité, taux d'échec. Un automatisme arrêté est plus dangereux qu'un processus manuel, parce qu'on croit qu'il fonctionne.

🎯 **ET MAINTENANT ?**
*On vous propose une plateforme de renseignement à 45 k€ par an. Votre fonction traite environ 200 éléments par mois. Que répondez-vous ?*
**Réponse** : que le volume ne justifie pas l'outil. Deux cents éléments par mois se gèrent dans un tableur structuré avec cinq états (§15.4) et un rapprochement mensuel avec l'inventaire. Ce que vous demandez à la place, si le budget existe : la surveillance des fuites et des mentions de vos produits (§22.2), qui couvre un besoin que rien d'autre ne couvre. La plateforme deviendra justifiée quand le volume, le nombre de sources et le besoin d'échange automatisé l'imposeront — et vous saurez le dire, parce que vous aurez mesuré.

## Synthèse mentale du chapitre 36

Une plateforme ingère, normalise, dédoublonne et diffuse ; elle ne décide pas ce qui vous concerne, n'évalue pas une source et ne produit pas de jugement — la colonne de ce qu'elle ne fait pas contient l'essentiel du métier. Un format structuré transporte des objets, pas des jugements : la phrase qui exprime une confiance argumentée ne se met dans aucun champ, et c'est pourquoi les formats servent le tactique et pas l'opérationnel. Ce qui s'automatise le mieux et se fait le moins, c'est le rapprochement avec l'inventaire — la question la plus fréquente et la plus mécanique du métier. Un outil accélère ce que vous faites, donc il accélère l'erreur si le raisonnement manque. Enfin, l'assistance automatisée produit un risque spécifique : une sortie plausible mais fausse ne déclenche aucune vérification, et ces outils sont particulièrement enclins à synthétiser des sources circulaires en ignorant leur dépendance.

**Trois questions de vérification**

1. Votre organisation traite deux cents éléments par mois. Une plateforme se justifie-t-elle ? Que demandez-vous à la place ?
2. Pourquoi un format structuré ne peut-il pas transporter un jugement analytique ?
3. Quel risque spécifique présente une assistance automatisée face à des sources circulaires ?

---
