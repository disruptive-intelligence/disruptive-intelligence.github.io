---
title: Chapitre 28 — Le matériel comme racine de confiance
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
chapter: 10
chapters: 14
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : la sécurité cryptographique repose sur des hypothèses de difficulté et non sur des impossibilités physiques, et l'on ne peut pas énumérer les entrées d'un système ouvert. Ce chapitre traite de **ce sur quoi une chaîne de confiance peut s'ancrer**.
>
> **Le principe qui organise le chapitre.** Toute vérification suppose de faire confiance à quelque chose. Si un logiciel vérifie un autre logiciel, qui vérifie le premier ? **La chaîne doit s'arrêter quelque part**, et l'ancrage matériel est la réponse dominante.
>
> **Quatre entrées.**

---

### ◆◆◆ Racine de confiance matérielle

**Niveau** — composant · **Couche** — vérifier

**En une phrase.** Un élément matériel, difficile à modifier et à observer, qui détient des secrets et effectue des opérations sur lesquelles tout le reste de la chaîne de confiance s'appuie.

**Pourquoi cette entrée est majeure.** Parce que **c'est le point de départ de toute vérification** — et parce que le raisonnement qu'elle porte, la nécessité d'un ancrage, s'applique bien au-delà de la sécurité informatique.

**Comment ça fonctionne.** Le composant détient une clé unique, inscrite à la fabrication, qui ne sort jamais. Il peut ainsi prouver son identité, chiffrer et signer sans exposer le secret. Il vérifie également, au démarrage, que chaque étage logiciel est conforme avant de lui passer la main — **chaque maillon mesure le suivant avant de l'exécuter**, ce qui constitue la chaîne de démarrage vérifié.

**Trois formes coexistent**, du plus intégré au plus autonome : un bloc intégré au processeur ; un composant dédié soudé à la carte ; ou un module externe résistant aux tentatives d'ouverture, employé là où les enjeux le justifient.

**Où vous rencontrerez le terme.** Terminaux · serveurs · véhicules · équipements industriels · objets connectés · infrastructures de paiement · systèmes d'identité.

**Ce que ça permet.** Attester qu'un équipement est bien celui qu'il prétend être · garantir qu'un logiciel n'a pas été modifié · protéger des clés contre un attaquant ayant obtenu des droits élevés · lier un secret à une machine physique donnée.

**Ce qui bloque.** **La confiance dans le fabricant.** La racine est posée à la fabrication : sa sécurité dépend entièrement de l'intégrité du procédé et de celui qui l'exécute. **On ne peut pas vérifier une racine de confiance sans faire confiance à quelqu'un** — le raisonnement est circulaire par construction, et il se résout par des audits et des attestations, non par une preuve.

S'y ajoutent **l'impossibilité de corriger** un défaut matériel autrement qu'en remplaçant l'équipement ; **les attaques physiques**, qui exigent un accès mais restent possibles ; et **la gestion du cycle de vie** — que faire d'une racine compromise sur un parc déployé.

**Ce que cela implique.** La confiance n'est jamais absolue : **elle est déplacée** vers un point où on la juge acceptable. La question utile n'est donc pas « ce système est-il sûr ? » mais **« à qui et à quoi ce système me demande-t-il de faire confiance ? »** — reformulation qui s'applique bien au-delà du matériel.

**À ne pas confondre avec.** Le **chiffrement** des données, qui est un usage de la racine et non la racine elle-même.

**Termes voisins.** *Secure element*, *TPM*, *HSM* désignent trois formes du même principe, à des niveaux d'intégration et de résistance différents.

> ⏱ **État au 23/08/2026** — 🏭 déployé, présent dans la quasi-totalité des équipements récents. Extension aux équipements industriels et aux objets connectés plus lente, portée par des exigences réglementaires.
> 🔄 **À revoir si** une exigence réglementaire impose un ancrage matériel vérifiable sur une classe large d'équipements connectés.

**Renvois** — Couche : vérifier · Courant : Trust Technologies (ch. 35) · Convergence : intelligence distribuée (38).

---

### ◆◆◆ Environnements d'exécution de confiance

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Exécuter un traitement dans une zone isolée du processeur, protégée du reste du système — y compris du système d'exploitation et de l'administrateur de la machine.

**Pourquoi cette entrée est majeure.** Parce qu'elle rend possible quelque chose de contre-intuitif : **utiliser une machine sans faire confiance à celui qui l'exploite** — et parce que la confusion avec le chiffrement classique est documentée et coûteuse.

**Comment ça fonctionne.** Le processeur maintient une zone dont la mémoire est chiffrée et dont l'accès est refusé au reste du système. Le code qui s'y exécute peut ensuite **attester** de ce qu'il est : produire une preuve, signée par le matériel, indiquant quel code s'exécute dans quel environnement. Un tiers distant peut vérifier cette attestation avant de confier des données.

**Ce que cela change.** Sans cette capacité, confier un traitement à une infrastructure tierce suppose de faire confiance à son exploitant. Avec elle, **on peut vérifier ce qui s'exécute avant d'envoyer les données** — la confiance se déplace de l'organisation vers le fabricant du processeur.

**Où vous rencontrerez le terme.** Cloud · traitement de données réglementées · santé · finance · collaboration entre organisations concurrentes · protection de modèles d'apprentissage.

**Ce que ça permet.** Traiter des données sensibles sur une infrastructure qu'on ne contrôle pas · faire collaborer plusieurs parties sur des données qu'aucune ne veut divulguer · protéger un modèle ou un algorithme de celui qui l'exécute.

**Ce qui bloque.** **Les attaques par canaux auxiliaires.** L'isolation logique n'empêche pas d'observer des effets indirects — temps d'exécution, consommation, comportement des caches — dont on peut parfois déduire de l'information. Plusieurs vulnérabilités de cette nature ont été démontrées, et la protection reste une course.

**La performance**, avec un surcoût variable selon l'implémentation. **L'hétérogénéité** : les mécanismes diffèrent selon les fabricants, ce qui complique la portabilité. Et **la confiance déplacée, non supprimée** : on cesse de faire confiance à l'exploitant pour faire confiance au fabricant du processeur.

**À ne pas confondre avec — et c'est la confusion la plus fréquente du chapitre.** Le **chiffrement des données au repos ou en transit**, qui protège les données stockées ou transmises. Ces environnements protègent les données **pendant leur traitement**, c'est-à-dire au moment où elles doivent nécessairement être en clair pour être calculées. C'est un troisième état, longtemps sans protection.

**Termes voisins.** *TEE*, *enclave*, *confidential computing* désignent la même famille — le dernier terme insistant sur l'usage, les deux premiers sur le mécanisme.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Disponible chez les principaux fournisseurs de cloud et sur les processeurs récents ; adoption croissante pour les données réglementées.
> 🔄 **À revoir si** une catégorie d'attaque par canal auxiliaire remet en cause l'isolation d'une génération largement déployée.

**Renvois** — Couche : vérifier, calculer · Courant : Trust Technologies (ch. 35).

---

### ◆◆ Attestation

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Produire une preuve vérifiable de l'état d'un système — quel matériel, quel logiciel, dans quelle configuration.

**Comment ça fonctionne.** Le système mesure son propre état — empreintes des composants logiciels chargés — et fait signer ces mesures par sa racine de confiance. Un tiers reçoit cette attestation, vérifie la signature et compare les mesures à des valeurs attendues.

**Deux formes.** L'attestation **locale**, où un composant vérifie un autre sur la même machine. L'attestation **à distance**, où un tiers vérifie une machine qu'il ne contrôle pas — c'est la forme qui change les architectures possibles.

**Ce que ça permet.** N'accorder un accès qu'à une machine dans un état vérifié · établir une confiance entre organisations sans audit préalable · détecter une modification non autorisée · conditionner la livraison d'une donnée à l'état du destinataire.

**Ce qui bloque.** **La gestion des valeurs attendues.** Vérifier une attestation suppose de savoir à quoi la comparer, pour toutes les versions légitimes de tous les composants — c'est un problème d'infrastructure considérable et sous-estimé. **La granularité** : une attestation dit ce qui a été chargé, pas ce que le système fait maintenant. Et **la révocation** : que faire quand une version attestée s'avère vulnérable.

**Ce que cela implique.** L'attestation atteste **un état, à un instant** — pas un comportement. Un système attesté conforme peut avoir été compromis après la mesure. C'est une garantie plus faible qu'il n'y paraît, et il faut le savoir.

**À ne pas confondre avec.** L'**authentification**, qui établit une identité ; l'attestation établit un état.

> ⏱ **État au 23/08/2026** — 🔬 émergent en généralisation. Mécanismes disponibles largement, infrastructure de vérification à l'échelle encore en construction.
> 🔄 **À revoir si** un service d'attestation interopérable entre fabricants et fournisseurs devient largement disponible.

**Renvois** — Couche : vérifier.

---

### ◆ Sûreté mémoire matérielle

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Des mécanismes matériels empêchant qu'un programme accède à une zone mémoire à laquelle il n'a pas droit.

**Pourquoi cette entrée existe.** Parce qu'une part importante et documentée des vulnérabilités logicielles graves relève de la gestion mémoire, et parce que traiter ce problème dans le matériel plutôt que dans le langage est une approche complémentaire aux langages sûrs.

**Ce qui bloque.** **Le coût en performance et en surface**, et surtout **la base installée** : ces mécanismes n'ont d'effet que si le logiciel est recompilé pour en tirer parti, ce qui suppose de reprendre des chaînes de compilation et des bibliothèques accumulées sur des décennies. **C'est un problème de dépendance de sentier au sens du volume 1**, non un problème technique.

**À ne pas confondre avec.** Les **langages à sûreté mémoire**, qui traitent le même problème à la source. Les deux approches sont complémentaires et progressent à des rythmes différents.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Mécanismes disponibles sur certaines architectures, adoption progressive.
> 🔄 **À revoir si** une exigence réglementaire impose la sûreté mémoire sur une classe de logiciels critiques.

**Renvois** — Couche : vérifier, calculer.

---


## Chapitre 29 — Cryptographie et confiance émergentes

> **Ce que ce chapitre ajoute.** Le chapitre 28 traitait de l'ancrage. Celui-ci traite des **mécanismes qui produisent des garanties** — et de ce qui se passe quand leurs hypothèses fondatrices sont remises en cause.
>
> **Six entrées**, dont quatre majeures. C'est la proportion la plus élevée de l'atlas, et elle reflète un fait : cette couche est celle où le plus grand nombre de capacités nouvelles sont apparues récemment.

---

### ◆◆◆ Cryptographie post-quantique

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

### ◆◆ Crypto-agilité

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

### ◆◆ Chiffrement homomorphe et calcul multipartite

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

### ◆◆◆ Preuves à divulgation nulle

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

### ◆◆◆ Provenance et authenticité des contenus

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

### ◆◆◆ Identité machine

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


## Chapitre 30 — Sûreté des systèmes autonomes

> **Ce que ce chapitre ajoute.** Les chapitres 28 et 29 traitaient de la confiance dans **ce qu'un système est**. Celui-ci traite de la confiance dans **ce qu'un système fait** — et particulièrement lorsqu'il décide.
>
> **La première entrée absorbe six termes du marché.** Runtime monitoring, runtime verification, runtime assurance, architecture Simplex, safety envelope, shield layer : ce ne sont pas six technologies mais **les couches d'une même architecture**. Les traiter séparément les rendrait incompréhensibles.
>
> **Cinq entrées.**

---

### ◆◆◆ Architecture de sûreté d'un système autonome — *entrée comparative*

**Niveau** — système · **Couche** — vérifier

**En une phrase.** L'ensemble des dispositifs qui permettent de faire confiance à un système qui décide — organisés en quatre couches complémentaires.

**Pourquoi cette entrée est comparative.** Parce que les termes du domaine circulent comme s'ils désignaient des technologies concurrentes, alors qu'ils désignent **des étages d'une même construction**. Comprendre l'ordre est plus utile que connaître les définitions.

**Le problème à résoudre.** Un système classique se vérifie avant déploiement : on démontre qu'il se comporte correctement sur toutes les entrées possibles. Un système apprenant ne le permet pas — **on ne peut pas énumérer les entrées d'un système ouvert sur le monde**. La vérification exhaustive étant impossible, il faut lui substituer autre chose.

#### Les quatre couches, dans l'ordre

**① OBSERVER — la surveillance en exploitation.**
Un dispositif indépendant observe le système pendant qu'il fonctionne et enregistre son état, ses entrées, ses sorties. Il ne juge pas : il constate. C'est la base de tout le reste, et c'est aussi ce qui permet le retour d'expérience.
*Terme du domaine : runtime monitoring.*

**② VÉRIFIER — le contrôle de propriétés en temps réel.**
On exprime des propriétés qui doivent rester vraies — « la distance à l'obstacle ne descend jamais sous ce seuil », « la commande reste dans cette plage » — et un dispositif vérifie en continu qu'elles le sont. **Il détecte une violation, il ne l'empêche pas.**
*Terme du domaine : runtime verification.*

**③ CONTRAINDRE — l'intervention qui garantit.**
Un dispositif simple, vérifiable par les méthodes classiques, s'interpose entre le système apprenant et les actionneurs. Il laisse passer les commandes qui préservent la sûreté et **substitue une commande sûre à celles qui ne le font pas**. Le système apprenant propose ; le dispositif de contrainte dispose.

C'est le principe le plus important de cette entrée : **on ne cherche pas à prouver que le système apprenant est sûr, on l'entoure d'un dispositif dont on peut prouver qu'il l'est.** La garantie ne porte pas sur l'intelligence mais sur son enveloppe.

*Termes du domaine : shield layer, architecture Simplex, safety envelope, runtime assurance.*

**④ DÉMONTRER — l'argumentation opposable.**
Un dossier structuré qui expose la revendication de sûreté, les arguments qui la soutiennent et les preuves qui étayent chaque argument. C'est ce qu'on présente à un régulateur, à un assureur, à un tribunal.
*Termes du domaine : safety case, assurance case.*

#### Ce que l'architecture permet

**Déployer un système dont on ne peut pas démontrer le comportement**, en garantissant non pas ce qu'il fera mais ce qu'il ne pourra pas faire. **C'est le déplacement conceptuel décisif** du domaine : de la preuve du système à la preuve de son enveloppe.

#### Ce qui bloque

**La définition des propriétés à garantir.** Écrire ce qui ne doit jamais arriver est plus difficile qu'il n'y paraît, et une propriété mal formulée produit soit des interventions incessantes qui rendent le système inutilisable, soit une garantie vide.

**Le conservatisme du dispositif de contrainte.** Plus il est prudent, plus il intervient, plus le système perd de sa capacité. **L'arbitrage entre sûreté et performance se joue entièrement ici**, et il est explicite — ce qui est préférable à un arbitrage implicite.

**La détection de sortie de domaine**, qui conditionne le déclenchement et fait l'objet de l'entrée suivante.

**Et le cadre.** Ces architectures sont reconnues dans certains référentiels sectoriels et pas dans d'autres. **Leur acceptation par les autorités est le facteur limitant du déploiement**, non leur disponibilité technique.

**Ce que cela implique.** La question à poser devant tout système autonome n'est pas « son modèle est-il fiable ? » mais **« quelle est son architecture de sûreté, et sur quelles propriétés porte la garantie ? »**

**À ne pas confondre avec.** La **sécurité informatique**, qui protège contre un adversaire — la carte de couche a établi que les hypothèses des deux disciplines sont opposées. Et les **essais**, qui vérifient avant déploiement ce que ces dispositifs vérifient pendant.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Architectures établies dans l'aéronautique et l'industrie ; extension aux systèmes apprenants en cours d'intégration dans les référentiels.
> 🔄 **À revoir si** un référentiel de certification accepte explicitement une architecture de ce type comme démonstration de sûreté pour un système apprenant.

**Renvois** — Couche : vérifier · Convergence : autonomie mobile (39) · Voir aussi : domaine de conception opérationnelle (ch. 17), volume 1 chapitre 16.

---

### ◆◆◆ Détection de sortie de domaine

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Reconnaître qu'une situation s'écarte de celles pour lesquelles le système a été validé — avant qu'il ne produise une réponse erronée avec assurance.

**Pourquoi cette entrée est majeure.** Parce que **c'est le verrou de l'autonomie apprenante**, et parce que le problème est plus difficile qu'il n'y paraît : il s'agit de reconnaître ce qu'on n'a jamais vu.

**Le problème.** Un système appris est bon là où ses données sont denses. Confronté à une entrée éloignée, **il ne produit pas d'erreur : il produit une sortie plausible avec la même assurance apparente**. Rien dans la forme du résultat ne distingue une interpolation d'une extrapolation.

**Les approches, et leurs limites.** Estimer une **incertitude** et alerter quand elle est élevée — mais un modèle peut être confiant à tort, et l'est précisément là où il extrapole. Mesurer une **distance à la distribution d'entraînement** — mais cette distance est difficile à définir dans un espace de grande dimension. Comparer les sorties de **plusieurs modèles** entraînés différemment, en supposant qu'ils divergeront sur les cas inhabituels — hypothèse d'indépendance qui n'est pas garantie. Ou surveiller des **propriétés physiques** de la situation plutôt que la sortie du modèle, ce qui est souvent la voie la plus robuste.

**Ce qui bloque.** **La définition même du domaine.** Décrire exhaustivement les conditions de validité d'un système est difficile ; un domaine trop étroit rend le système inutilisable, un domaine trop large ne peut pas être validé.

**Le compromis fausses alertes contre détections manquées.** Un détecteur trop sensible déclenche constamment ; un détecteur trop permissif laisse passer les cas dangereux. **Il n'existe pas de réglage sans arbitrage.**

**Et le fait qu'on ne peut pas tester ce qu'on n'a pas.** Évaluer un détecteur de situations inconnues suppose de disposer de situations inconnues — contradiction pratique qui rend l'évaluation partielle par construction.

**Ce que cela implique.** C'est le même problème sous trois noms dans ce volume : **la panne silencieuse du capteur, l'échec silencieux du modèle, la sortie de domaine du système autonome**. Un système qui cesse de fonctionner correctement mais continue de produire quelque chose de crédible est plus dangereux qu'un système qui s'arrête.

**À ne pas confondre avec.** La **détection d'anomalie** dans les données, qui cherche un événement inhabituel dans un flux ; ici, on cherche à savoir si le système lui-même est hors de sa zone de compétence.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Méthodes nombreuses, aucune dominante, évaluation comparative difficile faute de références partagées.
> 🔄 **À revoir si** une méthode d'évaluation standardisée de la détection hors domaine est adoptée dans un secteur réglementé.

**Renvois** — Couche : vérifier · Convergences : autonomie mobile (39), robotique généraliste (36) · Voir aussi : modèles du monde (ch. 13), capteurs inertiels (ch. 6).

---

### ◆◆ Vérification formelle

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Démontrer mathématiquement qu'un système satisfait une propriété, pour toutes les entrées possibles.

**Ce que ça permet.** Une garantie d'une nature différente de celle des essais : **les essais montrent l'absence de défaut sur les cas testés, la vérification formelle montre l'absence de défaut sur tous les cas** — dans les limites de ce qui a été modélisé.

**Ce qui bloque — et il faut être précis sur la portée.** **La taille.** La complexité de la vérification croît rapidement avec celle du système ; au-delà d'une certaine taille, elle devient impraticable. On vérifie donc des composants, pas des systèmes entiers.

**La modélisation.** On vérifie un modèle du système, pas le système. **Si le modèle omet un aspect, la preuve ne dit rien de cet aspect** — c'est la limite la plus importante et la moins comprise.

**Les systèmes apprenants.** Vérifier formellement un réseau de neurones est possible sur des propriétés simples et des tailles modestes, et reste hors de portée pour les modèles de grande taille. **C'est pourquoi l'architecture de sûreté ne cherche pas à vérifier le modèle mais son enveloppe** — dispositif simple, donc vérifiable.

**Ce que cela implique.** La vérification formelle est **un outil de composant, pas de système** — et c'est précisément ce qui la rend utile dans l'architecture de la première entrée : elle prouve la couche de contrainte, qui est simple par conception.

**À ne pas confondre avec.** Les **essais exhaustifs**, qui ne le sont jamais. Et l'**analyse statique**, qui détecte des classes d'erreurs sans démontrer une propriété.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour des composants critiques dans l'aéronautique, le ferroviaire et le matériel ; 🔬 émergent pour les composants d'autonomie.
> 🔄 **À revoir si** la vérification de propriétés utiles devient praticable sur des modèles de taille industrielle.

**Renvois** — Couche : vérifier.

---

### ◆◆ Dossiers de sûreté

**Niveau** — doctrine · **Couche** — vérifier

**En une phrase.** Un document structuré qui argumente qu'un système est suffisamment sûr pour son usage, en reliant explicitement revendications, arguments et preuves.

**Pourquoi cette entrée existe.** Parce que **c'est la forme sous laquelle la sûreté devient opposable** — à un régulateur, à un assureur, à un tribunal. Sans elle, une architecture technique ne se traduit pas en autorisation.

**Comment ça fonctionne.** Le document part d'une revendication — « ce système est acceptablement sûr dans ce domaine d'emploi » — la décompose en sous-revendications, et rattache à chacune des éléments de preuve : essais, analyses, vérifications formelles, retours d'exploitation. **La structure de l'argumentation est explicite**, ce qui permet de la contester point par point.

**Ce que ça permet.** Rendre discutable un raisonnement de sûreté · identifier les points faibles de l'argumentation · faire évoluer le dossier quand le système évolue.

**Ce qui bloque.** **La subjectivité du seuil.** « Suffisamment sûr » suppose un référentiel d'acceptabilité, qui relève d'un choix de société et non d'une mesure technique. **La confiance dans les preuves**, dont la qualité varie. Et **la mise à jour** : un système qui évolue exige un dossier qui évolue, ce qui est lourd et constitue un frein direct à l'amélioration continue.

**Ce que cela implique.** Le dossier de sûreté est **le point de rencontre entre technique et institution**. C'est là que se manifeste le verrou identifié tout au long de ce volume : la capacité technique existe, la démonstration opposable manque.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les secteurs réglementés, 🔬 émergent pour les systèmes apprenants.
> 🔄 **À revoir si** une méthodologie de dossier de sûreté pour système apprenant est reconnue par une autorité sectorielle.

**Renvois** — Couche : vérifier.

---

### ◆◆ Dégradation maîtrisée

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Continuer à fonctionner de manière réduite mais sûre lorsqu'une partie du système est défaillante ou hors de son domaine.

**Les quatre réponses possibles**, avec leur coût, établies au volume 1 et reprises ici comme référence.

**S'arrêter en sécurité.** Le moins coûteux, valable seulement si l'arrêt est effectivement sûr — ce qui n'est pas le cas d'un véhicule sur voie rapide ni d'un aéronef en vol.

**Continuer malgré la défaillance.** Exige une redondance sur toute la chaîne — perception, calcul, alimentation, actionneurs — et non sur le seul composant jugé fragile. **Le saut de coût est considérable** et régulièrement sous-estimé.

**Rendre la main.** Suppose un humain disponible, attentif et capable de reprendre en quelques secondes — ce que la couche *agir* a montré être une hypothèse fragile.

**Réduire les capacités.** Souvent la meilleure réponse et la plus difficile à concevoir : il faut avoir prévu à l'avance **ce qui peut être abandonné** et dans quel ordre.

**Ce qui bloque.** **La conception a priori.** Un mode dégradé ne s'improvise pas : il se conçoit, se spécifie et se teste — et tester un mode dégradé suppose de provoquer la défaillance, ce qui est coûteux et parfois impossible.

**Et l'information.** Un système qui se dégrade doit le signaler — à l'opérateur, à l'exploitant, aux autres systèmes qui en dépendent. **Une dégradation silencieuse est le pire des cas**, et c'est le fil rouge de tout ce volume.

**À ne pas confondre avec.** La **redondance**, qui est un moyen ; la dégradation maîtrisée est une propriété du comportement d'ensemble.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les secteurs à sûreté ancienne, 🔬 émergent ailleurs.
> 🔄 **À revoir si** la spécification d'un mode dégradé devient une exigence explicite pour les systèmes autonomes dans un secteur civil.

**Renvois** — Couche : vérifier · Voir aussi : autonomie supervisée (ch. 16), volume 1 chapitre 21.

---


## Clôture de la couche H — Vérifier

### Ce que les quinze entrées font apparaître

**Un. Toute vérification suppose un ancrage, et l'ancrage est toujours un déplacement de confiance.** Racine matérielle, enclave, attestation : dans les trois cas, on ne supprime pas la confiance, on la déplace vers un point jugé acceptable. **La question utile n'est jamais « ce système est-il sûr ? » mais « à qui ce système me demande-t-il de faire confiance ? »**

**Deux. Le déplacement conceptuel majeur de la couche est de renoncer à prouver le système pour prouver son enveloppe.** C'est ce que fait l'architecture de sûreté, et c'est ce qui rend déployable un système dont on ne peut démontrer le comportement. **La garantie ne porte pas sur ce que le système fera, mais sur ce qu'il ne pourra pas faire.**

**Trois. Le verrou est institutionnel dans cinq entrées sur quinze.** Architecture de sûreté, dossiers de sûreté, dégradation maîtrisée, sûreté mémoire, crypto-agilité : dans chaque cas, les dispositifs techniques existent et **leur reconnaissance par un référentiel est le facteur limitant**.

**Quatre. Une signature n'atteste jamais la véracité.** Cette limite apparaît dans trois entrées — provenance, attestation, identité machine — et elle avait été posée à la couche *percevoir*. **C'est probablement la formulation la plus utile de tout l'atlas pour un lecteur venant de la sécurité des systèmes d'information.**

### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | racine de confiance, attestation, identité machine |
| **39 — Autonomie mobile** | architecture de sûreté, détection de sortie de domaine, vérification formelle, dossiers de sûreté, dégradation maîtrisée |
| **41 — Biologie programmable** | *voir biosécurité, ch. 20* |

**Le dossier 39 mobilise cinq entrées de cette couche — et son maillon en retard est ici.** C'est la vérification la plus nette de la thèse du volume : la convergence la plus dépendante des couches *percevoir* et *agir* a son verrou dans *vérifier*.

---

---

---

### Couche I — Interagir

---


## Chapitre 31 — Interfaces humain-machine

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte dominante : **la bande passante d'entrée est facile, celle de sortie est difficile.** Un système peut présenter à un humain une quantité considérable d'information ; capter une intention humaine avec précision, rapidité et sans effort reste limité. C'est le verrou commun à toute la couche.
>
> **Une seconde contrainte, qui décide de l'adoption.** Le corps humain impose des limites qui ne se négocient pas : latence en dessous de laquelle l'inconfort apparaît, masse tolérable sur la tête, durée de port acceptable, chaleur dissipable au contact de la peau, et — pour les dispositifs implantés — durabilité dans un milieu biologique hostile.
>
> **Douze entrées**, réparties en deux ensembles : les interfaces qui s'adressent aux sens, et celles qui s'adressent au système nerveux.

---

### ◆◆◆ Réalité augmentée, mixte et virtuelle

**Niveau** — plateforme · **Couche** — interagir

**En une phrase.** Des dispositifs qui superposent une information numérique à la perception du monde réel, ou qui la remplacent entièrement.

**Pourquoi cette entrée est comparative.** Parce que trois termes circulent pour désigner un continuum, et que **la frontière entre eux n'est pas technologique mais fonctionnelle** — elle porte sur le degré auquel le monde réel reste perçu.

**Où passent les frontières.**

**La réalité virtuelle** remplace entièrement la perception visuelle par une scène synthétique. L'utilisateur ne voit plus son environnement.

**La réalité augmentée** superpose des éléments à la vision du monde réel, qui reste perçu directement.

**La réalité mixte** ajoute une exigence : les éléments virtuels sont **ancrés dans la géométrie du lieu** et interagissent avec elle — un objet virtuel posé sur une table réelle y reste quand l'utilisateur se déplace. Cela suppose une compréhension tridimensionnelle de l'environnement, donc de la perception.

**Une distinction technique transversale** : l'affichage peut être **transparent** — l'utilisateur voit directement le monde à travers un guide optique, sur lequel on projette — ou **par restitution vidéo**, l'environnement étant capté par des caméras et réaffiché. La seconde est plus simple et plus polyvalente ; elle introduit une latence entre le monde et sa perception, et fait dépendre la vision de l'électronique.

**Où vous rencontrerez le terme.** Formation et simulation · maintenance assistée · conception industrielle · santé · divertissement · vente · collaboration à distance.

**Ce que ça permet.** Superposer une information au point où elle est utile — schéma sur l'équipement à réparer, trajectoire sur le champ opératoire · s'entraîner à un geste sans risque ni consommable · visualiser un objet à l'échelle avant de le construire · partager un espace de travail entre personnes distantes.

**Ce qui bloque — et le verrou a changé de nature.** Les obstacles techniques de la vague précédente ont été largement levés : latence, résolution, poids et champ de vision ont progressé de plusieurs ordres de grandeur. **La diffusion n'a pourtant pas suivi** — ce qui, selon le raisonnement du volume 1, signifie que le verrou était masqué et se situe ailleurs.

**Il se situe dans l'usage.** Quel problème le dispositif résout-il, pour qui, à la place de quoi ? Dans les cas professionnels où la réponse est nette — formation à un geste coûteux, maintenance d'équipement complexe — l'adoption est réelle. Dans les usages généraux, la réponse reste faible face à un écran, qui ne demande rien à porter.

**S'y ajoutent** l'inconfort sur des durées longues, la difficulté d'usage prolongé, et le fait que ces dispositifs isolent — ce qui est un obstacle social autant qu'ergonomique.

**Ce que cela implique.** C'est **le cas de promesse récurrente le mieux documenté de cette couche** : plusieurs vagues, des verrous techniques réellement levés, et une diffusion qui n'a pas suivi. **La leçon est celle du volume 1 : quand un verrou identifié est levé et que rien ne se passe, le verrou était ailleurs.**

**À ne pas confondre avec.** L'**informatique spatiale**, terme plus récent qui désigne le cadrage plutôt que le dispositif. Et la **projection**, qui affiche sur des surfaces sans dispositif porté.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les usages professionnels ciblés, 🔬 émergent pour l'usage général. Progrès continus sur le poids et l'affichage ; adoption grand public inférieure aux prévisions successives.
> 🔄 **À revoir si** un usage quotidien non professionnel émerge et se maintient sur une base d'utilisateurs significative pendant plusieurs années.

**Renvois** — Couche : interagir · Courant : spatial computing (ch. 34).

---

### ◆◆ Informatique spatiale

**Niveau** — cadrage · **Couche** — interagir, percevoir, calculer

**En une phrase.** L'idée que l'interface entre humain et machine cesse d'être un écran plat pour devenir l'espace physique lui-même.

**Ce que le cadrage regroupe.** Les dispositifs portés du chapitre, mais aussi la compréhension tridimensionnelle de l'environnement, le suivi de position, la persistance d'objets virtuels d'une session à l'autre, et le partage d'un même espace entre plusieurs utilisateurs.

**Ce qu'il apporte réellement.** Il déplace l'attention **du dispositif vers la représentation partagée de l'espace** — ce qui est un cadrage utile, puisque c'est cette représentation qui rend possible la persistance et la collaboration, non le casque.

**Ce qu'il vous fait manquer.** **La question de la source de vérité géométrique.** Un objet virtuel ancré dans un lieu suppose que plusieurs dispositifs partagent la même compréhension de ce lieu, et que cette compréhension reste valide quand le lieu change. C'est le problème de cartographie du chapitre 17, transposé — et il est rarement évoqué.

**À ne pas confondre avec.** Les dispositifs eux-mêmes, dont le cadrage n'est pas synonyme.

> ⏱ **État au 23/08/2026** — cadrage en cours de stabilisation, adopté par plusieurs acteurs pour désigner leur offre.
> 🔄 **À revoir si** un format d'ancrage spatial interopérable entre fabricants est adopté.

**Renvois** — Couche : interagir, percevoir, calculer.

---

### ◆◆ Affichages avancés

**Niveau** — composant · **Couche** — interagir

**En une phrase.** Les dispositifs optiques qui délivrent une image à l'œil dans un volume et une consommation compatibles avec le port prolongé.

**Pourquoi cette entrée est déterminante.** Parce que **c'est le verrou physique de toute la première moitié du chapitre** : le confort, l'autonomie, le champ de vision et le coût des dispositifs portés sont commandés par l'affichage.

**Comment ça fonctionne.** Deux sous-ensembles. Une **source d'image**, qui doit être extrêmement lumineuse pour rester visible en superposition à la lumière du jour, et minuscule. Un **système optique** qui achemine cette image jusqu'à l'œil — typiquement un guide d'onde, plaque transparente dans laquelle la lumière se propage par réflexions avant d'être extraite devant la pupille.

**Le compromis qui borne tout.** **Champ de vision, luminosité, encombrement et rendement optique s'opposent deux à deux.** Élargir le champ de vision réduit la luminosité disponible ; améliorer le rendement complique la fabrication ; réduire l'encombrement limite le champ. **Aucune conception ne maximise les quatre**, et c'est la contrainte structurelle du domaine.

**Ce qui bloque.** **Le rendement optique**, très faible dans les guides d'onde : une fraction seulement de la lumière produite atteint l'œil, ce qui impose des sources très puissantes et donc de la consommation et de la chaleur. **Les artefacts optiques** — irisations, images fantômes — inhérents à ces architectures. Et **le coût de fabrication**, ces composants exigeant des tolérances très fines sur des surfaces étendues.

**Ce que cela implique.** **Le progrès du domaine se mesure au rendement optique et à la luminosité par watt**, non au champ de vision annoncé. C'est la grandeur à surveiller, et elle est rarement publiée.

**À ne pas confondre avec.** Les **écrans** classiques, dont les contraintes n'ont rien de commun : un écran est regardé à distance, un affichage porté est traversé.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Progrès continus sur les sources et les guides d'onde ; le compromis fondamental n'est pas levé.
> 🔄 **À revoir si** un affichage porté atteint simultanément un large champ de vision, une luminosité utilisable en extérieur et une autonomie d'une journée.

**Renvois** — Couche : interagir.

---

### ◆◆ Suivi oculaire et gestuel

**Niveau** — capacité · **Couche** — interagir, percevoir

**En une phrase.** Déterminer où l'utilisateur regarde et ce que font ses mains, pour en faire des modalités d'entrée.

**Pourquoi c'est important.** Parce que **c'est l'une des rares réponses au verrou de la couche** : capter une intention sans effort conscient ni dispositif tenu en main.

**Comment ça fonctionne.** Le suivi oculaire éclaire l'œil en infrarouge et analyse les reflets pour estimer la direction du regard. Le suivi gestuel utilise des caméras et un modèle de la main pour estimer la position des articulations.

**Ce que ça permet.** Une désignation naturelle — regarder ce qu'on veut sélectionner · une interaction sans dispositif tenu · **et une optimisation majeure du calcul** : n'afficher en haute résolution que la zone regardée, l'œil ne percevant les détails que dans une petite région centrale. Cette technique divise significativement la charge de rendu.

**Ce qui bloque.** **La désignation n'est pas la commande.** Regarder un objet ne signifie pas vouloir agir sur lui ; il faut un geste ou un signal de validation, ce qui ramène le problème initial. **La fatigue** : maintenir un geste dans le vide est épuisant sur la durée, phénomène bien documenté. **La robustesse** du suivi gestuel selon l'éclairage et les occultations. Et **la vie privée** : le regard révèle l'attention, l'intérêt et parfois l'état cognitif — c'est une donnée d'une sensibilité particulière.

**Ce que cela implique.** Ces modalités fonctionnent **en combinaison** et non isolément : regard pour désigner, geste ou voix pour confirmer. Aucune ne remplace à elle seule un dispositif de pointage.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les dispositifs portés récents.
> 🔄 **À revoir si** une modalité de confirmation sans geste ni voix atteint une fiabilité utilisable.

**Renvois** — Couche : interagir, percevoir.

---

### ◆◆ Haptique

**Niveau** — capacité · **Couche** — interagir

**En une phrase.** Restituer à l'utilisateur des sensations de contact, de texture ou de force.

**Pourquoi c'est déterminant.** Parce que **c'est le verrou de la téléopération**, et parce que la perception du contact est ce qui manque le plus dans toute manipulation à distance — le chapitre 15 l'a établi.

**Comment ça fonctionne — deux familles très différentes.** Le **retour tactile** stimule la peau — vibration, pression locale, texture — et il est relativement accessible. Le **retour de force** s'oppose au mouvement de l'utilisateur pour simuler la rigidité d'un objet ; il exige des actionneurs capables de produire des efforts significatifs, avec toutes les contraintes de la couche *agir*.

**Ce qui bloque.** **La bande passante de la sensation.** La peau et les récepteurs profonds perçoivent des variations très rapides ; restituer une sensation crédible exige une boucle de contrôle à haute fréquence, faute de quoi le contact paraît mou ou instable.

**La stabilité.** Un système de retour de force est une boucle fermée avec un humain dedans : mal réglée, elle oscille — et le chapitre 16 du volume 1 a montré pourquoi le délai en est l'ennemi.

**Et l'encombrement** : produire une force nécessite des actionneurs, donc de la masse portée sur la main ou le bras.

**Ce que cela implique.** L'haptique progresse nettement en **tactile** et reste difficile en **force**. C'est pourquoi les usages qui se déploient sont ceux où l'information de contact suffit — alerter, confirmer, texturer — et non ceux qui exigent de sentir une résistance.

**À ne pas confondre avec.** La **vibration** simple, qui est une forme de retour tactile mais ne restitue ni texture ni force.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour le tactile, 🔬 émergent pour le retour de force hors applications spécialisées.
> 🔄 **À revoir si** un dispositif de retour de force porté atteint une fidélité utile dans un volume et une masse compatibles avec un usage prolongé.

**Renvois** — Couche : interagir · Voir aussi : téléopération (ch. 15), peau électronique (ch. 7).

---

### ◆◆ Lunettes connectées

**Niveau** — plateforme · **Couche** — interagir

**En une phrase.** Des lunettes de forme ordinaire intégrant capteurs, audio et parfois un affichage minimal.

**Pourquoi cette entrée est distincte de la première.** Parce que ces dispositifs font **le pari inverse** : renoncer à l'affichage riche pour obtenir un objet portable toute la journée. Ce n'est pas une version simplifiée d'un casque, c'est une autre proposition.

**Ce que ça permet.** Capter — photo, vidéo, son — sans sortir un appareil · restituer par audio ou par un affichage sommaire · disposer d'un assistant contextuel voyant ce que l'utilisateur voit.

**Ce qui bloque.** **L'autonomie et la chaleur**, dans un volume qui n'autorise ni batterie significative ni dissipation. **L'acceptabilité sociale** d'un dispositif de capture porté en permanence — obstacle qui a fait échouer une vague antérieure et n'est pas résolu. Et **l'utilité marginale** face à un téléphone déjà présent.

**Ce que cela implique.** Le déplacement récent le plus significatif n'est pas l'affichage mais **l'assistant contextuel** : un dispositif qui voit et entend ce que l'utilisateur perçoit change la nature de l'interaction, indépendamment de sa capacité d'affichage. **C'est là que se joue la trajectoire, pas dans l'optique.**

**À ne pas confondre avec.** Les casques de réalité mixte, dont l'usage est sessionnel et non continu.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Produits sans affichage disponibles avec une adoption réelle ; produits avec affichage encore limités.
> 🔄 **À revoir si** un dispositif porté en continu atteint une base d'utilisateurs quotidiens significative sur plusieurs années.

**Renvois** — Couche : interagir.

---

### ◆◆ Informatique portée

**Niveau** — plateforme · **Couche** — interagir, percevoir

**En une phrase.** Les dispositifs portés au poignet, au doigt, à l'oreille ou sur le corps, qui mesurent en continu et notifient.

**Pourquoi cette entrée compte.** Parce que **c'est la seule famille de cette couche dont la diffusion est massive et établie** — et parce qu'elle démontre ce qui fonctionne : un dispositif qui ne demande aucune attention et rend un service continu.

**Ce que ça permet.** Mesurer des paramètres physiologiques en continu · détecter un événement — chute, arythmie, apnée · notifier discrètement · servir de moyen d'identification ou de paiement.

**Ce qui bloque.** **La qualité de la mesure.** Un capteur porté au poignet mesure dans des conditions défavorables — mouvement, contact variable, pigmentation, transpiration. **La dérive de mesure y est structurelle**, et c'est la limite de la couche *percevoir* appliquée au corps.

**Le statut de la donnée** : entre le bien-être et le dispositif médical, la frontière réglementaire est nette et les exigences sans commune mesure. Un même capteur peut relever de l'un ou de l'autre selon ce qu'on en revendique.

**Et l'exploitation** : mesurer en continu produit un volume de données dont l'interprétation clinique n'est pas établie pour la plupart des paramètres.

**Ce que cela implique.** Le succès de cette famille tient à ce que **le dispositif ne demande rien à l'utilisateur** — c'est l'inverse exact de ce que demandent les casques. **C'est probablement l'enseignement le plus utile de la couche pour évaluer toute interface future.**

> ⏱ **État au 23/08/2026** — 🏭 déployé, diffusion de masse. Extension progressive des paramètres mesurés et des reconnaissances réglementaires.
> 🔄 **À revoir si** un paramètre mesuré en continu par un dispositif grand public devient un critère de décision clinique reconnu.

**Renvois** — Couche : interagir, percevoir.

---

### ◆◆ Interfaces neuromusculaires

**Niveau** — capacité · **Couche** — interagir

**En une phrase.** Capter les signaux électriques envoyés par le système nerveux aux muscles, avant même que le mouvement soit visible.

**Pourquoi cette entrée est importante.** Parce que **c'est la voie non invasive la plus crédible** pour capter une intention motrice — et parce qu'elle contourne le verrou de la couche par un chemin inattendu.

**Comment ça fonctionne.** Des électrodes placées sur la peau — au poignet, sur l'avant-bras — détectent l'activité électrique musculaire. Comme cette activité précède le mouvement, on peut détecter une intention de geste **même minime**, voire un geste seulement esquissé.

**Ce que ça permet.** Une commande discrète, sans mouvement visible ni effort · une interaction utilisable quand les mains sont occupées ou hors de vue · **une voie d'usage pour des personnes ayant perdu la mobilité mais conservé l'activité nerveuse**.

**Ce qui bloque.** **La variabilité entre individus et entre sessions** : la position des électrodes, l'anatomie et l'état de la peau modifient le signal, ce qui impose un étalonnage. **Le nombre de commandes distinctes**, limité. Et **la fatigue**, l'activation répétée de petits muscles étant inconfortable sur la durée.

**Ce que cela implique.** C'est une modalité **complémentaire**, adaptée à un petit nombre de commandes discrètes et discrètes — et non un remplacement d'un dispositif de pointage.

**À ne pas confondre avec.** Les **interfaces cerveau-machine**, qui captent l'activité cérébrale. Ici, on capte le signal **en aval du cerveau**, sur le trajet nerveux vers le muscle — ce qui est bien plus accessible et bien moins ambitieux.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des premiers produits portés au poignet.
> 🔄 **À revoir si** une interface de ce type devient une modalité d'entrée par défaut sur un dispositif grand public.

**Renvois** — Couche : interagir.

---

### ◆◆◆ Interfaces cerveau-machine

**Niveau** — capacité · **Couche** — interagir, percevoir

**En une phrase.** Établir un canal direct entre l'activité du système nerveux central et un dispositif, en lecture ou en écriture.

**Pourquoi cette entrée est majeure — et la plus prospective de l'atlas.** Parce que les résultats obtenus sont réels et spectaculaires, qu'ils portent sur un très petit nombre de personnes, et que **l'écart entre le thérapeutique démontré, l'augmentation plausible et la spéculation y est le plus grand et le plus souvent effacé** de tout ce volume.

**Comment ça fonctionne — deux grandes voies.**

**Les interfaces non invasives** captent l'activité électrique ou hémodynamique à travers le crâne. Sans risque chirurgical, mais **le signal est fortement atténué et brouillé** : le crâne et les tissus agissent comme un filtre. La résolution spatiale et le débit d'information restent faibles, et cette limite est physique.

**Les interfaces invasives** placent des électrodes au contact du tissu nerveux, ou à sa surface. Le signal est infiniment plus riche — on peut décoder des intentions motrices fines, et des travaux récents ont permis de restituer une parole à partir de l'activité corticale chez des personnes ayant perdu l'usage de la parole. Mais cela suppose une intervention chirurgicale.

**Ce qui est démontré, précisément.** Chez un petit nombre de patients, sur des durées limitées : la commande d'un curseur ou d'un dispositif par la pensée · la restitution partielle d'une parole ou d'un texte · le contrôle d'une prothèse. **Ce sont des résultats cliniques réels**, et ils changent la vie des personnes concernées.

**Ce qui n'est pas démontré.** La durabilité sur des décennies · le passage à un grand nombre de patients · l'écriture d'information complexe vers le cerveau · et tout usage d'augmentation chez des personnes en bonne santé.

**Ce qui bloque — quatre verrous, dans cet ordre.**

**La durabilité de l'implant.** C'est le verrou dominant. Le tissu nerveux réagit à un corps étranger : une réponse inflammatoire et une encapsulation progressive dégradent le signal au fil des mois et des années. **Aucun dispositif n'a démontré une stabilité sur des décennies**, et c'est ce qui sépare la démonstration de l'usage courant.

**La chirurgie.** Elle limite intrinsèquement la population concernée à celle pour qui le bénéfice justifie le risque — c'est-à-dire aujourd'hui des situations de handicap sévère.

**Le décodage.** Il exige un étalonnage individuel et se dégrade dans le temps, l'activité neuronale enregistrée n'étant pas stable d'un jour à l'autre.

**Et le cadre.** Essais cliniques, autorisation, responsabilité, et des questions nouvelles de protection des données neuronales que le droit traite mal.

**Ce que cela implique.** La trajectoire crédible à moyen terme est **thérapeutique**, sur des indications où le bénéfice justifie l'intervention. **L'augmentation chez des personnes en bonne santé suppose de résoudre la durabilité et de justifier un risque chirurgical pour un bénéfice non vital** — ce qui est un problème de nature différente, et non un prolongement du précédent.

**Traitement dans ce volume.** Principes, verrous, industrie et gouvernance. Les débats éthiques et sociaux que soulève cette famille sont légitimes et sérieux ; ce volume les signale sans les arbitrer.

**À ne pas confondre avec.** Les **interfaces neuromusculaires**, qui captent en aval du cerveau et sont sans commune mesure en accessibilité. Les **neuroprothèses**, qui stimulent pour restaurer une fonction et sont une famille distincte. Et les dispositifs **non invasifs grand public**, dont les capacités sont très inférieures à ce que leur nom suggère.

> ⏱ **État au 23/08/2026** — 🔭 prospectif hors thérapeutique. Essais cliniques en cours chez plusieurs acteurs sur un nombre limité de patients ; résultats de décodage significatifs ; durabilité à long terme non établie.
> 🔄 **À revoir si** un implant démontre une stabilité de signal sur plusieurs années chez plusieurs patients — c'est le seul signal qui déplacerait réellement la trajectoire.

**Renvois** — Couche : interagir · Courant : NeuroTech (ch. 35).

---

### ◆◆ Neuroprothèses

**Niveau** — plateforme · **Couche** — interagir

**En une phrase.** Des dispositifs qui stimulent le système nerveux pour restaurer une fonction perdue ou traiter un trouble.

**Pourquoi les distinguer des précédentes.** Parce qu'elles fonctionnent **en écriture plutôt qu'en lecture**, parce que plusieurs sont déployées depuis des décennies, et parce que cette antériorité est régulièrement oubliée dans les discussions sur les interfaces neuronales.

**Ce qui est établi.** Des implants cochléaires restaurent une perception auditive chez des personnes sourdes depuis des décennies, avec des centaines de milliers de porteurs. La stimulation cérébrale profonde traite certains troubles moteurs. Des stimulateurs traitent des douleurs chroniques ou certaines épilepsies. **Ce sont des dispositifs médicaux courants, pas des prototypes.**

**Ce qui est émergent.** La restauration partielle de fonctions motrices ou sensorielles plus complexes — vision, toucher, mouvement — qui exige une précision de stimulation et un nombre de voies bien supérieurs.

**Ce qui bloque.** **La résolution de la stimulation** : stimuler avec une électrode active de nombreux neurones à la fois, ce qui limite la finesse de ce qu'on peut restituer. **La durabilité** de l'interface, comme pour la lecture. Et **l'énergie**, un dispositif implanté devant fonctionner des années sans intervention.

**Ce que cela implique.** L'écriture vers le système nerveux est **plus ancienne et plus déployée que la lecture** — l'inverse de ce que suggère l'attention portée au sujet. Et la difficulté croît avec la finesse de l'information à transmettre, non avec le principe.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour les indications établies, 🔬 émergent pour la restauration de fonctions complexes.
> 🔄 **À revoir si** une restauration sensorielle à haute résolution est autorisée en usage clinique courant.

**Renvois** — Couche : interagir.

---

### ◆ Interfaces vocales persistantes

**Niveau** — capacité · **Couche** — interagir

**En une phrase.** Un système d'écoute continue capable de recevoir une instruction parlée à tout moment, sans activation explicite.

**Ce que ça permet.** Une interaction sans les mains et sans regarder · un accès à l'information dans des contextes où un écran est impraticable.

**Ce qui bloque.** **L'acceptabilité d'une écoute permanente**, qui est l'obstacle principal et n'est pas technique. **Le contexte** : distinguer une instruction d'une conversation ordinaire reste imparfait. Et **l'usage en public**, parler à un dispositif restant socialement contraint.

**Ce que cela implique.** Le progrès des modèles de langage a levé la barrière de compréhension ; **le verrou restant est social**. C'est une illustration nette du raisonnement de cette couche.

> ⏱ **État au 23/08/2026** — 🏭 déployé, avec un usage réel concentré sur des contextes spécifiques — domicile, véhicule.
> 🔄 **À revoir si** un dispositif d'écoute continue porté en public atteint une acceptation large.

**Renvois** — Couche : interagir.

---

### ◆◆ Augmentation humaine

**Niveau** — cadrage · **Couche** — interagir

**En une phrase.** L'idée d'améliorer une capacité humaine au-delà de son niveau habituel, par un dispositif porté, implanté ou pharmacologique.

**Pourquoi cette entrée est un cadrage et non une technologie.** Parce qu'elle regroupe des objets sans contrainte commune — un exosquelette, un implant, une aide cognitive — réunis par **une intention** et non par un mécanisme. C'est le test du cadrage du chapitre 2, et il échoue sur le premier critère.

**Ce que le cadrage fait voir.** Une question réelle : **où passe la frontière entre restaurer et augmenter ?** Un dispositif conçu pour compenser un déficit peut, appliqué à une personne sans déficit, améliorer une capacité. Cette frontière n'est pas technique, elle est réglementaire, éthique et sociale — et elle détermine des régimes d'autorisation entièrement différents.

**Ce qu'il vous fait manquer.** **Le rapport bénéfice-risque.** Pour une restauration, le bénéfice est élevé et le risque accepté. Pour une augmentation chez une personne en bonne santé, **le bénéfice doit être considérable pour justifier un risque non nul** — et cette asymétrie est ce qui explique l'écart entre les deux trajectoires, bien plus que la difficulté technique.

**Ce que cela implique.** Les technologies d'augmentation qui se diffusent sont celles dont le risque est **faible, non invasif et réversible** : dispositifs portés plutôt qu'implantés. Celles qui exigent une intervention restent confinées au thérapeutique, et cela ne tient pas à leur maturité.

**Traitement dans ce volume.** Les débats sur l'augmentation humaine — équité d'accès, consentement, pression sociale, définition de la norme — sont sérieux et n'appartiennent pas à ce volume, qui expose les positions sans arbitrer.

**À ne pas confondre avec.** Les **exosquelettes**, dispositifs concrets dont l'usage principal est l'assistance à l'effort en milieu professionnel, et qui relèvent de la couche *agir*.

> ⏱ **État au 23/08/2026** — cadrage. Les dispositifs concrets qu'il regroupe sont traités individuellement.
> 🔄 **À revoir si** un dispositif d'augmentation non thérapeutique fait l'objet d'un cadre d'autorisation spécifique.

**Renvois** — Couche : interagir.

---


## Clôture de la couche I — Interagir

### Ce que les douze entrées font apparaître

**Un. Le verrou de la couche est social et ergonomique, pas technique.** Sur douze entrées, huit butent principalement sur l'acceptabilité, la fatigue, le confort prolongé ou l'utilité marginale face à l'existant. **Les obstacles techniques de la décennie précédente ont été largement levés sans que la diffusion suive** — ce qui est la signature du verrou masqué du volume 1.

**Deux. La famille qui réussit est celle qui ne demande rien.** L'informatique portée se diffuse massivement parce qu'elle ne réclame ni attention, ni geste, ni posture. Les casques échouent en usage général pour la raison inverse. **C'est l'heuristique la plus utile de toute la couche** — une régularité observée, non un résultat prédictif établi — et elle mérite d'être appliquée à toute interface future.

**Trois. L'écriture vers le système nerveux est plus ancienne et plus déployée que la lecture.** Les implants cochléaires comptent des centaines de milliers de porteurs depuis des décennies, tandis que les interfaces en lecture concernent quelques dizaines de patients. **C'est l'inverse de ce que suggère l'attention portée au sujet.**

**Quatre. La frontière entre restaurer et augmenter n'est pas technique.** Elle est réglementaire et éthique, et elle explique l'écart entre les deux trajectoires bien mieux que la difficulté d'ingénierie : le rapport bénéfice-risque n'est pas le même, et cette asymétrie est structurelle.

---


## CLÔTURE DE L'ATLAS

### Ce que les 162 entrées font apparaître

L'atlas est complet : **neuf couches capacitaires, un plan d'infrastructure spatiale, vingt-sept chapitres, 162 entrées**. Voici ce que la mise à plat révèle, et qu'aucune couche prise isolément ne montrait.

#### Un — Le verrou est rarement technique

Sur l'ensemble des entrées, **la contrainte dominante est technique dans une minorité de cas**. Elle est plus souvent institutionnelle — autorisation, certification, assurabilité, droit international, cadre réglementaire —, industrielle — rendement de production, capacité qualifiée, délai de construction —, économique — demande solvable, coût de vérification, modèle de financement — ou temporelle — renouvellement de parc, délai de qualification, développement minier.

**Cela retrouve, sur 162 objets, le résultat obtenu sur 45 termes en Partie III et sur 15 trajectoires closes au volume 1.** Trois lectures différentes d'un même univers technologique, découpé selon trois unités d'analyse distinctes, un même constat. **Ce n'est pas une validation indépendante** — la sélection, le codage et la méthode sont les mêmes — mais une confrontation interne, et elle vaut ce que vaut sa cohérence.

#### Deux — Cinq murs traversent l'atlas, et le cinquième n'est pas physique

Le volume 1 avait établi cinq murs communs à toutes les technologies. Ils réapparaissent ici sous des noms de métier différents, et **la défaillance silencieuse est celui qui traverse le plus de couches** : dérive de capteur, sortie hors distribution d'un modèle, jeu mécanique en aval de la mesure, dérive d'un jumeau numérique, contamination de lot biologique, corruption non détectée, position fausse après perte de signal.

**C'est le seul mur qui ne soit pas physique**, et c'est celui qui produit le mode de défaillance le plus dangereux : un système qui cesse de fonctionner correctement mais continue de produire quelque chose de crédible.

#### Trois — Deux couches sont en amont de tout, une est en aval de tout

**Calculer** et **alimenter** sont les couches les plus transversales : la grande majorité des capacités de cet atlas en dépendent. **Vérifier** ne produit aucune capacité nouvelle mais conditionne le déploiement de celles que les autres produisent — c'est pourquoi elle est presque toujours traitée en dernier, et **fréquemment bloquante dans les déploiements critiques ou réglementés**.

#### Quatre — Six entrées décrivent une contrainte plutôt qu'un objet

Matériaux critiques · raccordement électrique · débris orbitaux · reproductibilité · biosécurité · domaine de conception opérationnelle. **Ce sont les entrées les plus transférables de l'atlas**, et cinq d'entre elles ont été classées majeures pour cette raison.

#### Cinq — Les dépendances non décidées sont concentrées dans deux couches

Positionnement et temps, congestion orbitale, cryptographie déployée, identité machine, modèles de fondation tiers : **cinq cas de dépendances constituées par agrégation de décisions individuellement rationnelles**, dont trois relèvent de l'infrastructure spatiale. C'est la matière du chapitre 45.

---

---


## Ouverture de la Partie III

L'atlas vous a donné **les choses**. Cette partie vous donne **les mots**.

Ce n'est pas la même chose, et c'est pourquoi elle existe. Vous savez maintenant ce qu'est un modèle de fondation, une architecture reliant vision, langage et action, un actionneur à entraînement quasi-direct. Vous n'entendrez presque jamais ces termes en réunion. Vous entendrez « IA générative », « Physical AI », « agentic », « autonomous systems », « Deep Tech » — des mots qui ne désignent aucun objet précis mais qui organisent les budgets, les appels d'offres, les stratégies et les conversations.

**Ces mots ne sont pas du bruit.** Un cadrage est utile s'il regroupe des objets partageant des contraintes réelles et s'il fait apparaître une relation qu'on ne voyait pas. Plusieurs de ceux qui suivent sont d'excellents cadrages. D'autres sont des catégories de marché sans contrainte partagée. Quelques-uns sont les deux selon qui les emploie.

**Ce que fait cette partie et que ne fait pas l'atlas.** Les chapitres 5 à 31 répondent à *comment ça marche et qu'est-ce qui bloque*. Les chapitres qui suivent répondent à *que recouvre ce mot, que ne recouvre-t-il pas, et que vous fait-il manquer*. Une phrase de cette partie ne pourrait pas figurer dans l'atlas sans y paraître déplacée — c'est le test de non-redite.

### Le format des fiches terminologiques

Chaque terme reçoit huit éléments, dans cet ordre constant :

**Niveau** — sur l'échelle du chapitre 2.
**Couches mobilisées** — quelles capacités le terme convoque réellement.
**Ce qu'il désigne** — l'extension du terme, aussi précisément que possible.
**Ce qu'il mélange** — les objets de natures différentes qu'il rassemble.
**Ce qu'il ne signifie pas** — les lectures fausses les plus fréquentes.
**Ce qu'il vous fait manquer** — la question que la catégorie masque.
**Pourquoi il est employé** — l'intérêt qu'il sert, sans procès d'intention.
**Où le chercher dans l'atlas** — les fiches correspondantes.

**Le sixième élément est le plus important.** Chaque catégorie éclaire quelque chose et en masque une autre. C'est cette face masquée qui coûte cher, et presque aucune définition ne la mentionne.

---
