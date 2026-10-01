---
title: Chapitre 17 — Mobilité autonome
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute.** Le chapitre 16 traitait de plateformes opérant loin de leur opérateur, mais dans des espaces généralement réservés. Celui-ci traite du cas le plus difficile : **opérer dans un espace partagé avec des humains non prévenus**.
>
> **Quatre entrées**, dont deux majeures. La seconde — le domaine de conception opérationnelle — est la notion la plus utile et la moins connue de tout le chapitre.

---

## ◆◆◆ Véhicules autonomes

**Niveau** — plateforme · **Couche** — agir, percevoir, décider

**En une phrase.** Des véhicules routiers capables d'assurer la conduite sans intervention humaine, dans des conditions définies.

**Pourquoi on en parle.** Parce que c'est **le cas d'école de l'écart entre annonce et déploiement** — le volume 1 l'a instruit — et parce que la capacité est désormais démontrée en exploitation commerciale, ce qui déplace la question.

**Comment ça fonctionne.** Une chaîne en quatre étages : **perception** — combiner caméras, radars et souvent lidars pour construire une représentation de l'environnement ; **localisation** — se situer précisément, généralement par rapport à une carte préétablie ; **prédiction et planification** — anticiper le comportement des autres usagers et choisir une trajectoire ; **contrôle** — exécuter cette trajectoire.

**Les niveaux d'automatisation.** Une échelle normalisée à six niveaux structure le vocabulaire du secteur. Le point qui compte : **la frontière décisive se situe entre le niveau où l'humain doit rester prêt à reprendre et celui où il ne le doit plus**. En dessous, la responsabilité reste au conducteur ; au-dessus, elle bascule vers le système et son exploitant — ce qui change entièrement l'économie, l'assurance et les exigences de preuve.

**Où vous rencontrerez le terme.** Automobile · transport de personnes · logistique et camionnage · navettes · assistance à la conduite.

**Ce que ça permet.** Un service de transport dont le coût marginal ne comprend pas de conducteur · une réduction potentielle des accidents liés à l'inattention · une mobilité pour des personnes qui ne conduisent pas.

**Ce qui bloque.** **La démonstration de sûreté, très loin devant la perception.** Le volume 1 l'a établi : on ne peut pas énumérer les situations d'un système ouvert sur le monde, donc on ne peut pas démontrer exhaustivement, donc l'assureur ne peut pas tarifer facilement le risque. **L'assurabilité est un meilleur indicateur avancé de déploiement que n'importe quelle annonce technique.**

S'y ajoutent l'**extension du domaine d'exploitation**, qui se fait ville par ville et condition par condition ; le **coût de la supervision à distance**, dont le ratio détermine l'économie réelle ; et le **renouvellement du parc** pour les véhicules particuliers, qui borne toute transformation à l'échelle du parc quel que soit le succès sur le flux.

**Ce que cela implique.** La question n'est plus « est-ce que ça marche » mais **« dans quel domaine, à quel ratio de supervision, et sous quel régime de responsabilité »**. Ces trois grandeurs sont observables et rarement publiées ensemble.

**Sûreté et sécurité.** Le logiciel agit sur le monde physique ; l'intégrité des commandes et la disponibilité du contrôle priment sur la confidentialité · dépendance à une cartographie et à une référence de positionnement · comportement en cas de perte de liaison de supervision.

**À ne pas confondre avec.** **L'assistance à la conduite**, où le conducteur reste responsable et doit rester prêt — la confusion entre les deux est la plus dangereuse du domaine, et elle a des conséquences documentées.

> ⏱ **État au 23/08/2026** — 🔬 émergent en exploitation. Services commerciaux sans conducteur opérationnels dans un nombre limité de villes, avec extension progressive du domaine d'exploitation. Le camionnage sur axes dédiés progresse. Aucune généralisation au véhicule particulier.
> 🔄 **À revoir si** un référentiel de démonstration de sûreté applicable aux systèmes apprenants devient opposable dans une juridiction majeure — ce qui rendrait l'assurabilité traitable et permettrait une extension par cadre plutôt que par négociation locale.

**Renvois** — Couche : agir · Courant : autonomous mobility (ch. 33) · Convergence : autonomie mobile (39).

---

## ◆◆◆ Domaine de conception opérationnelle

**Niveau** — capacité et notion de conception · **Couche** — décider, vérifier

**En une phrase.** L'ensemble des conditions dans lesquelles un système automatisé a été conçu, testé et validé — et hors desquelles son comportement n'est pas caractérisé.

**Pourquoi cette entrée existe.** Parce que **c'est la notion la plus utile et la moins connue de toute la couche**, et parce qu'elle transforme une question sans réponse — « ce système est-il sûr ? » — en trois questions qui en ont.

**Ce qu'un domaine d'emploi spécifie.** Types de voies · plages de vitesse · conditions météorologiques · luminosité · densité de trafic · zones géographiques · état de l'infrastructure · présence ou non de piétons. Un système peut être parfaitement validé sur autoroute par temps clair et n'avoir aucun comportement caractérisé en ville sous la pluie.

**Les trois questions qui définissent une conception sûre.**

**Un — le système sait-il quand il sort de son domaine ?** C'est le problème le plus difficile, et c'est exactement la détection de sortie de distribution du chapitre 13. Un système qui ne sait pas qu'il est hors domaine continue d'agir avec la même assurance apparente.

**Deux — que fait-il alors ?** Quatre réponses possibles, aux coûts très différents : s'arrêter en sécurité, si l'arrêt est sûr ; continuer malgré la défaillance, ce qui exige de la redondance sur toute la chaîne et coûte considérablement plus ; rendre la main, ce qui suppose un humain disponible et attentif — voir l'entrée précédente ; ou réduire ses capacités, souvent la meilleure réponse et la plus difficile à concevoir, puisqu'il faut avoir prévu à l'avance ce qui peut être abandonné.

**Trois — qui en est informé, et dans quel délai ?**

**Ce que cela implique — et c'est généralisable bien au-delà des véhicules.** La question utile devant tout système automatisé n'est jamais « est-il autonome ? » ni « est-il fiable ? », mais : **dans quelles conditions son comportement a-t-il été validé, sait-il quand il en sort, et que fait-il alors ?** Cette formulation s'applique à un robot, à un agent logiciel, à un système d'exploitation autonome, à un dispositif médical.

**Ce qui bloque.** **La spécification du domaine elle-même.** Décrire exhaustivement des conditions d'usage est difficile, et un domaine trop étroit limite l'usage tandis qu'un domaine trop large ne peut pas être validé. La normalisation de ces descriptions progresse et reste incomplète.

**À ne pas confondre avec.** **Les niveaux d'automatisation**, qui décrivent le partage de tâches entre humain et machine. Un système de niveau élevé sur un domaine étroit et un système de niveau modeste sur un domaine large sont deux propositions différentes, et le seul niveau ne permet pas de les comparer.

> ⏱ **État au 23/08/2026** — 🔬 émergent comme pratique formalisée. Notion adoptée dans les référentiels du secteur automobile, en cours d'extension à d'autres domaines d'autonomie.
> 🔄 **À revoir si** la description du domaine d'emploi devient une exigence normalisée dans un secteur hors automobile.

**Renvois** — Couche : décider, vérifier · Convergence : autonomie mobile (39) · Voir aussi : architecture de sûreté (ch. 30), détection de sortie de domaine (ch. 30).

---

## ◆◆ Autonomie maritime, aérienne et ferroviaire civiles

**Niveau** — plateforme · **Couche** — agir, décider

**En une phrase.** L'automatisation de la conduite dans des modes de transport autres que routier, dont les difficultés et les cadres n'ont rien de commun.

**Pourquoi les traiter ensemble.** Parce que la catégorie *autonomous mobility* les réunit alors que **leurs contraintes sont opposées**, et que la comparaison est instructive.

**Le ferroviaire** est le mode le plus avancé et le moins commenté : voie dédiée, absence d'obstacles imprévus, signalisation coopérative. Des lignes fonctionnent sans conducteur depuis des décennies. **La difficulté n'y est pas la conduite mais l'infrastructure** : équiper une ligne existante coûte cher, et la coexistence avec des trains non équipés complique tout.

**L'aérien** dispose d'un pilotage automatique très ancien pour les phases de croisière. La difficulté se concentre sur les phases critiques, la gestion des situations non nominales, et surtout **le cadre de certification**, qui est le plus exigeant de tous les modes.

**Le maritime** de surface bénéficie de temps de réaction longs et d'un environnement peu encombré, mais souffre d'un **vide juridique international** : les conventions supposent un équipage à bord.

**Ce que cela implique.** Sur les trois modes, **la difficulté dominante est institutionnelle et non technique** — infrastructure pour le rail, certification pour l'aérien, droit international pour le maritime. C'est l'inverse du routier, où la difficulté technique de l'environnement ouvert reste réelle.

**À ne pas confondre avec.** **Le pilotage automatique**, présent depuis longtemps dans l'aérien et le maritime, qui exécute une consigne sans gérer les situations imprévues.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour le ferroviaire sur lignes dédiées, 🔬 émergent pour le maritime de surface, cadre en construction pour l'aérien civil sans pilote.
> 🔄 **À revoir si** une convention internationale sur la navigation commerciale sans équipage aboutit.

**Renvois** — Couche : agir, décider.

---

## ◆◆ Localisation et cartographie

**Niveau** — capacité · **Couche** — percevoir, décider

**En une phrase.** Se situer précisément dans un environnement, et construire ou maintenir la représentation qui permet de le faire.

**Comment ça fonctionne — deux approches complémentaires.**

**La cartographie préétablie.** On relève au préalable l'environnement avec une précision élevée, et le véhicule s'y localise en comparant ce qu'il perçoit à cette carte. Précision excellente, mais **la carte doit être maintenue** : travaux, marquages effacés, signalisation modifiée. C'est un coût d'exploitation continu, et c'est ce qui limite l'extension géographique.

**La cartographie et localisation simultanées.** Le système construit sa carte en se déplaçant, tout en s'y localisant. Aucune préparation nécessaire, mais la position obtenue est relative et dérive — sauf recalage sur une référence externe.

**Ce qui bloque.** **Le coût de maintien de la carte**, qui croît avec la surface couverte et qui est le facteur limitant réel de l'extension. **La dérive** pour l'approche sans carte. **Les environnements peu texturés ou répétitifs**, où la localisation visuelle échoue — couloirs identiques, tunnels, champs.

**Ce que cela implique.** Le choix entre les deux approches est un arbitrage entre **coût de préparation** et **précision garantie**. C'est un cas où le verrou est logistique — qui relève la carte, à quelle fréquence, et qui paie — plutôt que technique.

**À ne pas confondre avec.** **Le positionnement par satellite** (ch. 6), qui donne une position absolue mais insuffisamment précise et indisponible en intérieur, en tunnel ou en environnement urbain dense.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Le maintien de cartographies fines à grande échelle reste un coût significatif et un frein à l'extension géographique.
> 🔄 **À revoir si** un système atteint des performances de localisation suffisantes sans cartographie préétablie dans un environnement urbain dense.

**Renvois** — Couche : percevoir, décider · Convergence : autonomie mobile (39).

---
