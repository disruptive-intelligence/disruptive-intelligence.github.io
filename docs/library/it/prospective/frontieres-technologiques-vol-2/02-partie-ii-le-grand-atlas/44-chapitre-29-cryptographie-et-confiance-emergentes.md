---
title: Chapitre 29 — Cryptographie et confiance émergentes
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute.** Le chapitre 28 traitait de l'ancrage. Celui-ci traite des **mécanismes qui produisent des garanties** — et de ce qui se passe quand leurs hypothèses fondatrices sont remises en cause.
>
> **Six entrées**, dont quatre majeures. C'est la proportion la plus élevée de l'atlas, et elle reflète un fait : cette couche est celle où le plus grand nombre de capacités nouvelles sont apparues récemment.

---

## ◆◆◆ Cryptographie post-quantique

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

## ◆◆ Chiffrement homomorphe et calcul multipartite

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Calculer sur des données sans les déchiffrer, ou faire calculer plusieurs parties sur leurs données respectives sans qu'aucune ne révèle les siennes.

**Comment ça fonctionne.** Le **chiffrement homomorphe** permet d'effectuer des opérations sur des données chiffrées, le résultat déchiffré étant celui qu'on aurait obtenu sur les données en clair. Le **calcul multipartite** répartit le calcul entre plusieurs participants de telle sorte qu'aucun ne dispose d'assez d'information pour reconstituer les entrées des autres.

**Ce que ça permet.** Confier un traitement sans confier les données · croiser des jeux de données entre organisations qui ne peuvent pas les partager · établir une statistique sur une population sans exposer les individus.

**Ce qui bloque.** **Le coût en calcul**, encore très supérieur au traitement en clair — plusieurs ordres de grandeur selon les opérations, malgré des progrès continus. **La complexité de mise en œuvre**, qui exige une expertise rare. Et **la concurrence des enclaves** (ch. 28), qui offrent une garantie de nature différente — matérielle plutôt que mathématique — à un coût de performance bien inférieur.

**Ce que cela implique.** Ces techniques ont une garantie **plus forte** que les enclaves, puisqu'elles ne supposent aucune confiance dans un fabricant. Elles ont un coût bien supérieur. **L'arbitrage se joue sur le degré de confiance que l'on accepte de déplacer**, et non sur la performance seule.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des déploiements sur des cas où la sensibilité justifie le coût.
> 🔄 **À revoir si** le surcoût de calcul descend sous un ordre de grandeur pour des opérations courantes.

**Renvois** — Couche : vérifier, calculer.

---

## ◆◆◆ Preuves à divulgation nulle

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Prouver qu'une affirmation est vraie sans révéler pourquoi elle l'est.

**Pourquoi cette entrée est majeure.** Parce que **c'est une capacité contre-intuitive dont les usages dépassent largement le domaine où le terme est né** — et parce qu'elle est très mal comprise.

**Le principe, en une image.** Prouver qu'on connaît un secret sans le dire. Prouver qu'on a plus de dix-huit ans sans révéler sa date de naissance. Prouver qu'un calcul a été effectué correctement sans refaire le calcul ni montrer les données d'entrée.

**Comment ça fonctionne, au niveau utile.** Le prouveur transforme son affirmation et son secret en un objet mathématique — la preuve — que le vérifieur peut contrôler. La vérification est **beaucoup plus rapide que le calcul d'origine**, et elle ne révèle rien d'autre que la validité de l'affirmation.

**Deux propriétés distinctes**, souvent confondues sous le même terme. La **divulgation nulle** — la preuve ne révèle rien du secret. La **succinctité** — la preuve est courte et rapide à vérifier, même si le calcul prouvé était long. **La seconde est souvent la plus utile**, et elle est indépendante de la première : on peut vouloir une preuve courte sans avoir de secret à protéger.

**Où vous rencontrerez le terme.** Systèmes d'identité · conformité réglementaire · registres distribués · vérification de calcul délégué · authentification préservant la vie privée.

**Ce que ça permet.** Déléguer un calcul à un tiers non fiable et vérifier son résultat à faible coût · prouver une conformité sans divulguer les données sous-jacentes · établir une propriété d'un ensemble de données sans le publier.

**Ce qui bloque.** **Le coût de génération**, très supérieur au calcul prouvé — c'est le compromis central : on rend la vérification très bon marché en rendant la production très chère. **La complexité de conception** : traduire un problème en une forme prouvable est un travail d'expert. Et **l'hypothèse de sécurité**, ces constructions reposant sur des hypothèses mathématiques dont certaines ne résistent pas à un attaquant quantique — ce qui relie cette entrée à la première du chapitre.

**Ce que cela implique.** L'usage le plus structurant n'est pas la confidentialité mais **la vérifiabilité du calcul délégué**. Dans un monde où l'on confie des traitements à des tiers, pouvoir vérifier un résultat sans le recalculer change l'économie de la confiance.

**À ne pas confondre avec.** Le **chiffrement**, qui rend illisible ; ici, on ne cache pas une donnée, on prouve une propriété. Et avec les **registres distribués**, où ces techniques sont employées mais dont elles sont indépendantes.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Déploiements établis dans certains écosystèmes ; extension aux usages d'identité et de conformité en cours ; coût de génération en baisse continue.
> 🔄 **À revoir si** la génération de preuve devient assez peu coûteuse pour être appliquée à des calculs de grande taille en production.

**Renvois** — Couche : vérifier · Courant : Trust Technologies (ch. 35).

---

## ◆◆◆ Provenance et authenticité des contenus

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Établir l'origine d'un contenu et l'historique de ses modifications, de manière vérifiable.

**Pourquoi cette entrée est majeure.** Parce que **le coût de production d'un contenu plausible s'est effondré**, et que la vérification n'a pas suivi. C'est le sujet du chapitre 42, et cette entrée en fournit l'outil.

**Comment ça fonctionne.** Le principe dominant consiste à attacher au contenu, dès sa création, des **métadonnées signées** : quel dispositif ou quel logiciel l'a produit, quand, et quelles modifications ont été appliquées ensuite. Chaque étape d'édition ajoute une entrée à cet historique, signée à son tour. Un vérificateur peut alors reconstituer la chaîne et contrôler les signatures.

**Une approche complémentaire** consiste à insérer dans le contenu lui-même une marque imperceptible, résistant à certaines transformations — recadrage, recompression. Elle survit à la perte des métadonnées, au prix d'une robustesse limitée.

**Ce que ça permet.** Distinguer un contenu dont l'origine est attestée d'un contenu sans historique · détecter une modification ultérieure · établir une chaîne de responsabilité éditoriale.

**Ce qui bloque — et il faut être précis, car les attentes sont mal placées.**

**L'absence de métadonnées ne prouve rien.** Un contenu sans historique peut être authentique ; une image simplement recadrée par un outil non compatible perd sa chaîne. **Le système permet d'affirmer une origine, pas de nier une origine** — et c'est une asymétrie fondamentale.

**La couverture.** Le mécanisme n'a de valeur que s'il est présent dans les appareils de capture, les logiciels d'édition et les plateformes de diffusion. **C'est un problème de complément et de standard**, au sens du volume 1, et il exige une coordination entre acteurs nombreux.

**Et la limite décisive, déjà rencontrée au chapitre 7.** Une signature atteste l'origine et l'intégrité. **Elle n'atteste jamais la véracité.** Un appareil authentique photographiant une scène mise en scène produit un contenu parfaitement authentique et trompeur. La provenance déplace la question de « ce contenu a-t-il été fabriqué ? » vers « qui l'a produit et lui fait-on confiance ? » — ce qui est un progrès, non une solution.

**À ne pas confondre avec.** La **détection de contenus synthétiques**, qui tente de reconnaître une origine artificielle par analyse du contenu. Approche opposée — l'une prouve l'origine, l'autre la devine — et dont la fiabilité se dégrade à mesure que les générateurs progressent.

**Termes voisins.** *Content credentials*, *provenance*, *filigrane* désignent des mécanismes distincts d'un même ensemble.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Norme technique disponible et adoptée par des fabricants d'appareils, des éditeurs de logiciels et des plateformes ; couverture du parc encore faible.
> 🔄 **À revoir si** l'affichage d'une provenance vérifiée devient une pratique par défaut sur une plateforme de diffusion majeure.

**Renvois** — Couche : vérifier · Convergence : voir chapitre 42 · Voir aussi : peau électronique et perception tactile (ch. 7).

---

## ◆◆◆ Identité machine

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Attribuer à une machine, un service ou un agent logiciel une identité vérifiable, avec des droits, une durée de vie et un mécanisme de révocation.

**Pourquoi cette entrée est majeure.** Parce que **le nombre d'identités non humaines a dépassé de loin celui des identités humaines** dans les systèmes d'information — et parce que l'arrivée d'agents logiciels agissant de façon autonome en fait un objet en constitution rapide.

**Comment ça fonctionne.** Une identité machine repose sur un secret cryptographique et sur une attestation de son porteur. Elle se distingue d'une identité humaine par trois propriétés : elle est **créée et détruite en grand nombre et rapidement** ; elle n'a **pas de facteur d'authentification humain** — pas de mot de passe mémorisé, pas de second facteur ; et **elle agit sans intention**, ce qui rend la notion de responsabilité différente.

**Ce que ça permet.** Contrôler ce qu'un service peut faire · tracer une action jusqu'à son auteur non humain · révoquer un accès sans interrompre les autres · établir une confiance entre systèmes appartenant à des organisations différentes.

**Ce qui bloque.** **La prolifération.** Le nombre d'identités croît plus vite que la capacité à les gouverner : secrets oubliés dans du code, certificats expirés, comptes de service surprivilégiés et jamais révoqués. **C'est l'une des causes documentées de compromission les plus fréquentes**, et elle est organisationnelle autant que technique.

**La durée de vie** : un secret à longue durée de vie est un risque, un secret à courte durée exige une infrastructure de renouvellement automatique.

**Et l'identité des agents.** Un agent logiciel qui agit pour le compte d'un utilisateur pose des questions nouvelles : **agit-il avec ses droits propres ou avec ceux de l'utilisateur ?** Comment tracer une chaîne d'actions passant par plusieurs agents ? Comment révoquer une délégation ? Ces questions sont ouvertes et se posent avec urgence.

**Ce que cela implique.** L'identité machine était un sujet d'exploitation ; elle devient un sujet d'architecture. **Un système où des agents agissent doit répondre, avant tout déploiement, à la question : qui a fait cela, avec quels droits, et qui en répond ?**

**À ne pas confondre avec.** L'**identité numérique** des personnes, dont les enjeux — vie privée, souveraineté, inclusion — sont d'une autre nature.

> ⏱ **État au 23/08/2026** — 🔬 émergent en structuration rapide. Pratiques établies pour les services et les charges de travail ; cadre pour les identités d'agents en construction.
> 🔄 **À revoir si** un standard d'identité et de délégation propre aux agents logiciels est adopté largement.

**Renvois** — Couche : vérifier · Courants : Trust Technologies (ch. 35), Agentic AI (ch. 32) · Voir aussi : agents IA (ch. 12).

---
