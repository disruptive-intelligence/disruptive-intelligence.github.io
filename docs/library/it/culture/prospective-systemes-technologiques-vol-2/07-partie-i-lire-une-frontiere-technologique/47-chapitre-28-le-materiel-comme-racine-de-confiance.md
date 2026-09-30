---
title: Chapitre 28 — Le matériel comme racine de confiance
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

> **Ce que ce chapitre ajoute à la carte de couche.** La carte a posé deux contraintes : la sécurité cryptographique repose sur des hypothèses de difficulté et non sur des impossibilités physiques, et l'on ne peut pas énumérer les entrées d'un système ouvert. Ce chapitre traite de **ce sur quoi une chaîne de confiance peut s'ancrer**.
>
> **Le principe qui organise le chapitre.** Toute vérification suppose de faire confiance à quelque chose. Si un logiciel vérifie un autre logiciel, qui vérifie le premier ? **La chaîne doit s'arrêter quelque part**, et l'ancrage matériel est la réponse dominante.
>
> **Quatre entrées.**

---

## ◆◆◆ Racine de confiance matérielle

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

## ◆◆◆ Environnements d'exécution de confiance

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

## ◆◆ Attestation

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

## ◆ Sûreté mémoire matérielle

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Des mécanismes matériels empêchant qu'un programme accède à une zone mémoire à laquelle il n'a pas droit.

**Pourquoi cette entrée existe.** Parce qu'une part importante et documentée des vulnérabilités logicielles graves relève de la gestion mémoire, et parce que traiter ce problème dans le matériel plutôt que dans le langage est une approche complémentaire aux langages sûrs.

**Ce qui bloque.** **Le coût en performance et en surface**, et surtout **la base installée** : ces mécanismes n'ont d'effet que si le logiciel est recompilé pour en tirer parti, ce qui suppose de reprendre des chaînes de compilation et des bibliothèques accumulées sur des décennies. **C'est un problème de dépendance de sentier au sens du volume 1**, non un problème technique.

**À ne pas confondre avec.** Les **langages à sûreté mémoire**, qui traitent le même problème à la source. Les deux approches sont complémentaires et progressent à des rythmes différents.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Mécanismes disponibles sur certaines architectures, adoption progressive.
> 🔄 **À revoir si** une exigence réglementaire impose la sûreté mémoire sur une classe de logiciels critiques.

**Renvois** — Couche : vérifier, calculer.

---
