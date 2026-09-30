---
title: Chapitre 24 — Communications
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé la contrainte dominante : la latence due à la distance ne s'achète pas. Ce chapitre traite des **moyens de transporter l'information** et de ce qui les borne.
>
> **Une observation qui vaut pour les six entrées.** Les systèmes modernes fonctionnent près de la limite théorique fixée par la bande passante disponible et le rapport signal sur bruit. **Les gains futurs viendront de l'élargissement de la bande, de la multiplication des canaux ou du rapprochement des points — non d'un meilleur décodage.**
>
> **Six entrées.**

---

## ◆◆◆ Réseaux mobiles avancés

**Niveau** — infrastructure · **Couche** — relier

**En une phrase.** Les générations successives de réseaux cellulaires, dont chacune est présentée comme une rupture et dont l'apport réel se mesure sur plusieurs années.

**Pourquoi on en parle.** Parce que **c'est le terme technique que vous entendrez le plus souvent sans qu'il désigne quelque chose de précis** — et parce que le décalage entre les capacités annoncées d'une génération et son déploiement réel est un cas d'école pour ce volume.

**Comment ça fonctionne.** Une génération n'est pas une technologie mais un **ensemble de spécifications** produit par un organisme de normalisation, publié par versions successives. Une même génération recouvre donc des capacités très différentes selon la version implémentée et selon ce que l'opérateur a réellement déployé.

**Trois leviers d'amélioration, indépendants les uns des autres.** L'**élargissement de la bande** — utiliser davantage de spectre, notamment dans des fréquences plus élevées, au prix d'une portée réduite. La **densification** — multiplier les points d'émission, ce qui rapproche l'utilisateur et améliore le débit disponible. Et l'**efficacité spectrale** — transmettre davantage d'information par unité de spectre, par des techniques d'antennes multiples.

**Où vous rencontrerez le terme.** Télécommunications · industrie et réseaux privés · véhicules · objets connectés · discours stratégiques sur la souveraineté.

**Ce que ça permet.** Des débits élevés · une latence réduite dans certaines configurations · la possibilité de dédier une portion du réseau à un usage avec des garanties de service · la connexion d'un très grand nombre d'objets à faible débit.

**Ce qui bloque.** **L'écart entre spécification et déploiement.** Les capacités les plus mises en avant — latence très faible, garanties de service — exigent une architecture que la plupart des déploiements n'ont pas mise en œuvre. **Une génération se juge à ce qui est activé, pas à ce qui est spécifié.**

S'y ajoutent le **coût de densification**, qui croît fortement dans les fréquences élevées ; le **modèle économique**, les revenus par abonné ne suivant pas les investissements ; et la **disponibilité du spectre**, ressource attribuée par des procédures longues.

**Ce que cela implique.** La génération suivante est en cours de définition et fait l'objet d'annonces de capacités. **Le décalage entre annonce et service disponible se compte en années**, et la question utile devant toute affirmation de génération est : quelle version, quelle architecture, et déployée où.

**À ne pas confondre avec.** Les **réseaux privés**, qui utilisent les mêmes technologies sur un périmètre restreint avec des exigences différentes — souvent la latence et la fiabilité plutôt que le débit.

> ⏱ **État au 23/08/2026** — 🏭 déployé, avec une hétérogénéité forte entre marchés et entre versions activées. Travaux de normalisation engagés sur la génération suivante.
> 🔄 **À revoir si** les architectures permettant des garanties de service sont déployées à grande échelle dans un marché majeur.

**Renvois** — Couche : relier · Courant : software-defined everything (ch. 34).

---

## ◆◆◆ Réseaux non terrestres

**Niveau** — infrastructure · **Couche** — relier

**En une phrase.** L'intégration des liaisons satellitaires aux réseaux de télécommunications, jusqu'à permettre à un terminal ordinaire de communiquer directement avec un satellite.

**Pourquoi on en parle.** Parce que c'est **une rupture d'architecture réelle**, et non une amélioration incrémentale : la couverture cesse de dépendre d'une infrastructure au sol.

**Comment ça fonctionne.** Historiquement, une liaison satellitaire exigeait un terminal spécifique — antenne directive, puissance d'émission élevée. Deux évolutions ont changé cela : les **constellations en orbite basse**, qui réduisent la distance d'un facteur considérable par rapport à l'orbite géostationnaire, et donc l'affaiblissement du signal ; et l'**intégration aux normes terrestres**, qui permet à un terminal standard de dialoguer avec un satellite comme avec une station au sol.

**Ce que ça permet.** Une couverture des zones sans infrastructure — océans, déserts, montagnes, zones peu peuplées · une continuité de service en cas de destruction ou de défaillance du réseau terrestre · des services de messagerie ou d'urgence sur des terminaux ordinaires · une connectivité pour des objets isolés.

**Ce qui bloque.** **Le bilan de liaison.** Un terminal ordinaire émet peu et possède une antenne non directive : la liaison montante est le maillon faible, ce qui limite les débits et impose des satellites à très grandes antennes. **La capacité par zone** : un satellite couvre une surface étendue et partage sa capacité entre tous les utilisateurs de cette surface — l'architecture convient aux zones peu denses et sature dans les zones peuplées.

S'y ajoutent le **spectre**, dont l'usage partagé entre terrestre et spatial exige une coordination internationale ; le **coût du segment spatial**, qui doit être renouvelé au rythme de la durée de vie des satellites en orbite basse ; et la **latence**, faible en orbite basse mais non nulle.

**Ce que cela implique.** Ces réseaux ne remplacent pas le terrestre : ils le **complètent là où il n'est pas rentable**. L'économie change entièrement selon la densité de population, ce qui en fait une technologie de couverture et non de capacité.

**À ne pas confondre avec.** Les **communications satellitaires classiques**, qui exigent un terminal dédié et dont la latence géostationnaire interdit certains usages.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion rapide. Services de messagerie et d'urgence disponibles sur terminaux courants ; services à débit en extension ; intégration aux normes terrestres en cours de généralisation.
> 🔄 **À revoir si** un service à haut débit sur terminal ordinaire, sans antenne spécifique, devient disponible commercialement à grande échelle.

**Renvois** — Couche : relier · Voir aussi : constellations en orbite basse (ch. 26).

---

## ◆◆ Communications optiques

**Niveau** — capacité · **Couche** — relier

**En une phrase.** Transmettre l'information par faisceau lumineux à travers l'atmosphère ou le vide, plutôt que par onde radio ou par fibre.

**Pourquoi les traiter ensemble.** Parce que les liaisons en espace libre, atmosphériques et intersatellitaires reposent sur le même principe et se distinguent par le milieu traversé — **les traiter séparément suggérerait deux technologies distinctes qui n'existent pas**.

**Ce que ça permet.** Des débits très élevés, la bande disponible dans le domaine optique étant sans commune mesure avec celle du spectre radio · **aucune attribution de spectre nécessaire**, ce qui supprime une procédure longue · une directivité extrême, donc une discrétion et une résistance aux interférences · et, entre satellites, une liaison sans les contraintes atmosphériques.

**Ce qui bloque.** **L'atmosphère**, dans les liaisons sol-espace ou sol-sol : nuages, brouillard et turbulence interrompent ou dégradent la liaison. Cela impose soit une redondance de sites géographiquement distants, soit un usage limité aux liaisons où l'interruption est tolérable. **Le pointage** : la directivité qui fait la force impose un alignement d'une précision extrême entre objets mobiles.

**Ce que cela implique.** L'usage qui a le plus progressé est **intersatellitaire** — hors atmosphère, la contrainte principale disparaît, et la liaison optique devient nettement supérieure à la radio. Cela change l'architecture des constellations, qui peuvent acheminer le trafic en orbite plutôt que de redescendre à chaque saut.

**À ne pas confondre avec.** La **fibre optique**, où le faisceau est guidé et l'atmosphère absente. **L'éclairage communicant**, qui utilise la lumière visible sur de très courtes distances.

> ⏱ **État au 23/08/2026** — 🏭 déployé en intersatellitaire, 🔬 émergent pour les liaisons sol-espace à haut débit.
> 🔄 **À revoir si** une liaison optique sol-espace atteint une disponibilité comparable à celle d'une liaison radio dans un climat tempéré.

**Renvois** — Couche : relier · Voir aussi : photonique intégrée (ch. 9), constellations (ch. 26).

---

## ◆◆ Réseaux déterministes

**Niveau** — capacité · **Couche** — relier

**En une phrase.** Des réseaux garantissant qu'un message arrivera dans un délai borné, et non seulement qu'il arrivera.

**Pourquoi on en parle.** Parce que **c'est la condition des systèmes cyber-physiques** : une boucle de contrôle ne tolère pas un délai imprévisible, et la gigue est souvent plus gênante que la latence elle-même.

**Comment ça fonctionne.** Un réseau ordinaire fonctionne au mieux : les messages sont acheminés dès que possible, et un encombrement produit un retard variable. Un réseau déterministe **réserve des ressources** — créneaux temporels, chemins, priorités — de sorte qu'un flux critique dispose d'une garantie indépendante de la charge du reste.

**Ce que ça permet.** Faire coexister sur une même infrastructure des flux critiques et des flux ordinaires · remplacer des réseaux industriels propriétaires et cloisonnés par une infrastructure commune · piloter à distance des systèmes exigeant une réactivité bornée.

**Ce qui bloque.** **La configuration.** Garantir un délai suppose de connaître à l'avance les flux, leurs besoins et leur ordonnancement — ce qui est lourd à établir et fragile aux changements. **L'interopérabilité** entre équipements de fournisseurs différents. Et **la borne physique** : aucun mécanisme ne réduit le temps de propagation, seulement l'attente.

**Ce que cela implique.** Le déterminisme est **une propriété d'ingénierie de réseau, pas de technologie** : il s'obtient en renonçant à l'usage opportuniste des ressources, donc en acceptant un moindre taux d'utilisation.

**À ne pas confondre avec.** La **basse latence**, qui est une moyenne ; le déterminisme est une garantie de borne supérieure — c'est une propriété qualitativement différente.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Normes disponibles, déploiements en environnement industriel, généralisation limitée par la complexité de configuration.
> 🔄 **À revoir si** la configuration devient assez automatisée pour être déployée sans expertise réseau spécialisée.

**Renvois** — Couche : relier.

---

## ◆◆ Communications en environnement dégradé

**Niveau** — capacité · **Couche** — relier

**En une phrase.** Maintenir une liaison lorsque les conditions de propagation sont mauvaises, que l'infrastructure est indisponible ou que le spectre est encombré.

**Périmètre de traitement.** Ce volume traite les **principes, les architectures et les conséquences systémiques**. Il ne décrit aucune technique de perturbation, aucune contre-mesure opérationnelle, aucun paramètre d'emploi.

**Les principes généraux, au niveau où ils sont analysables.** La **redondance de chemins** — plusieurs liaisons de natures différentes, dont les conditions de défaillance ne sont pas corrélées. La **tolérance au délai** — des protocoles capables de stocker et de retransmettre plus tard, adaptés aux liaisons intermittentes. La **réduction du débit** — transmettre moins, mais sûrement, en dégradant volontairement la qualité pour préserver la continuité. Et la **communication indirecte** — relais par des nœuds intermédiaires quand la liaison directe est impossible.

**Ce que cela permet.** Poursuivre une mission ou maintenir un service quand la liaison nominale est indisponible · détecter une dégradation et basculer avant l'interruption.

**Ce qui bloque.** **La corrélation des défaillances.** Une redondance ne vaut que si les liaisons ne tombent pas ensemble — or elles partagent souvent une infrastructure, une source d'énergie ou une référence de temps. **C'est la défaillance de mode commun du volume 1**, appliquée aux communications.

S'y ajoutent le **coût** de maintenir plusieurs moyens rarement utilisés, et la **complexité de bascule**, qui devient elle-même un composant critique.

**Ce que cela implique.** La question utile n'est pas « ce système résiste-t-il ? » mais **« qu'est-ce qui est commun à toutes ses liaisons ? »** — alimentation, référence de temps, opérateur, chemin physique.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les domaines où l'exigence est ancienne — maritime, aéronautique, secours. 🔬 émergent comme préoccupation dans les infrastructures civiles.
> 🔄 **À revoir si** la redondance de moyens de communication devient une exigence réglementaire pour des infrastructures civiles critiques.

**Renvois** — Couche : relier.

---

## ◆ Réseaux privés

**Niveau** — doctrine · **Couche** — relier

**En une phrase.** Déployer un réseau cellulaire sur un périmètre restreint — usine, port, hôpital, campus — sous le contrôle de l'organisation qui l'exploite.

**Ce que ça permet.** Une maîtrise de la couverture et de la capacité · des garanties de service impossibles à obtenir d'un réseau public partagé · le maintien des données sur le site · une infrastructure unique remplaçant plusieurs réseaux industriels hétérogènes.

**Ce qui bloque.** **L'accès au spectre**, dont les modalités varient fortement selon les juridictions — certaines réservent des bandes à cet usage, d'autres non, ce qui rend le sujet très inégal d'un pays à l'autre. **Les compétences** : exploiter un réseau cellulaire est un métier qu'une industrie ne possède pas nécessairement. Et **la concurrence** des solutions sans licence, souvent suffisantes et bien moins coûteuses.

**À ne pas confondre avec.** Un **réseau local sans fil**, dont les caractéristiques de couverture, de mobilité et de gestion de la charge sont différentes.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec un déploiement très inégal selon la disponibilité du spectre dédié.
> 🔄 **À revoir si** des bandes dédiées deviennent largement disponibles dans les principales juridictions industrielles.

**Renvois** — Couche : relier.

---
