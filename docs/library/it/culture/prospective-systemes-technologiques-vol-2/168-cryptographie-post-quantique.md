---
title: ◆◆◆ Cryptographie post-quantique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Des algorithmes cryptographiques classiques, conçus pour résister à un attaquant disposant d'un calculateur quantique.

**Pourquoi cette entrée est majeure.** Parce que **c'est une migration d'infrastructure à l'échelle mondiale**, et parce que sa temporalité est contre-intuitive : l'action requise ne dépend pas de la date à laquelle la menace se matérialiserait.

**Le raisonnement, et il tient en trois propositions.**

**Un.** La sécurité de la cryptographie à clé publique déployée aujourd'hui repose sur des **hypothèses de difficulté calculatoire** — on suppose que certains problèmes mathématiques demanderaient un temps de calcul déraisonnable. Ce ne sont pas des impossibilités physiques.

**Deux.** Un calculateur quantique suffisamment grand et fiable affaiblirait certaines de ces hypothèses. La question de savoir si et quand une telle machine existera est ouverte — le chapitre 10 la traite.

**Trois, et c'est le point.** **Une donnée capturée aujourd'hui peut être déchiffrée plus tard.** Un adversaire peut collecter du trafic chiffré maintenant et attendre. **La date pertinente n'est donc pas celle où la machine existerait, mais celle où vos données cesseraient d'avoir de la valeur.**

Si une donnée doit rester confidentielle vingt ans, elle est déjà exposée à cette hypothèse — indépendamment de tout calendrier.

**Comment ça fonctionne.** Les nouveaux algorithmes reposent sur des problèmes mathématiques différents, pour lesquels aucun avantage quantique n'est connu. Plusieurs ont été normalisés à l'issue d'un processus public de sélection. **Ce sont des algorithmes classiques** : ils s'exécutent sur des machines ordinaires.

**Où vous rencontrerez le terme.** Télécommunications · finance · santé · défense · fournisseurs de cloud · navigateurs et systèmes d'exploitation · équipements industriels à longue durée de vie.

**Ce qui bloque — et le verrou n'est pas l'algorithme.** **La migration.** Il faut remplacer des mécanismes présents dans des équipements, des protocoles, des certificats, des cartes, des dispositifs embarqués — dont certains ont une durée de vie de plusieurs décennies et **ne seront jamais mis à jour**. C'est un problème de base installée au sens du volume 1, et de renouvellement de parc.

S'y ajoutent la **taille des clés et des signatures**, supérieure, ce qui pose des difficultés dans les protocoles contraints et sur les équipements à faible mémoire ; la **performance** sur les dispositifs embarqués ; et le **risque de transition**, les nouveaux algorithmes étant moins éprouvés par le temps — d'où des approches hybrides combinant ancien et nouveau.

**Ce que cela implique.** La compétence à acquérir n'est pas cryptographique mais **inventoriale** : savoir où la cryptographie est utilisée dans son système d'information, avec quelle durée de vie des données, et quels équipements ne pourront pas être mis à jour. **Cette cartographie est le vrai travail, et elle prend des années.**

**À ne pas confondre avec.** La **cryptographie quantique** (ch. 10), qui utilise des propriétés physiques et exige du matériel dédié. Ce sont deux réponses de natures opposées au même risque — l'une logicielle et déployable, l'autre physique et contrainte par la distance.

> ⏱ **État au 23/08/2026** — 🔬 émergent en déploiement. Algorithmes normalisés disponibles, intégration engagée dans les protocoles majeurs et chez les grands fournisseurs, migration du parc à peine commencée.
> 🔄 **À revoir si** une vulnérabilité mathématique est découverte dans un algorithme normalisé, ou si une échéance réglementaire de migration est fixée dans une juridiction majeure.

**Renvois** — Couche : vérifier · Courant : Trust Technologies (ch. 35) · Voir aussi : calcul quantique (ch. 10).

---


## ◆◆ Crypto-agilité

**Niveau** — doctrine · **Couche** — vérifier

**En une phrase.** Concevoir un système de sorte qu'un algorithme cryptographique puisse y être remplacé sans reconstruire l'ensemble.

**Pourquoi cette entrée suit la précédente.** Parce que **la migration post-quantique n'est pas la dernière** : d'autres suivront, et un système conçu pour une seule migration devra être repris à chaque fois.

**Ce que cela suppose.** Ne pas figer un algorithme dans le code · négocier les algorithmes plutôt que les imposer · disposer d'un inventaire de ce qui est utilisé où · et pouvoir révoquer et remplacer sans interruption de service.

**Ce qui bloque.** **Le coût immédiat pour un bénéfice différé** — configuration classique de sous-investissement. **Les protocoles figés** dans des normes anciennes. Et **les équipements sans mécanisme de mise à jour**, pour lesquels aucune agilité n'est possible : ils devront être remplacés.

**Ce que cela implique.** L'agilité est une **propriété d'architecture, décidée à la conception**. On ne la rétrofit pas — ce qui en fait une décision à prendre maintenant pour des systèmes dont la migration surviendra dans dix ans.

> ⏱ **État au 23/08/2026** — 🔬 émergent comme exigence explicite dans les référentiels et les cahiers des charges.
> 🔄 **À revoir si** l'agilité devient une exigence normalisée pour les équipements à longue durée de vie.

**Renvois** — Couche : vérifier.

---
