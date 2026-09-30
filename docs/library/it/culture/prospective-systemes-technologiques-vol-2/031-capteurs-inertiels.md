---
title: ◆◆ Capteurs inertiels
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — percevoir

**En une phrase.** Mesurer ses propres accélérations et rotations, pour en déduire son déplacement sans aucune référence extérieure.

**Pourquoi on en parle.** Parce que c'est le seul moyen de continuer à savoir où l'on est quand toute référence externe disparaît — et parce que ce moyen se dégrade inexorablement.

**Comment ça fonctionne.** Des accéléromètres mesurent les accélérations selon trois axes, des gyromètres les vitesses de rotation. En intégrant ces mesures dans le temps, on estime vitesse puis position.

**La difficulté est dans l'intégration.** Chaque petite erreur de mesure s'accumule : une erreur d'accélération devient une erreur de vitesse qui croît linéairement, puis une erreur de position qui croît quadratiquement. **Une centrale inertielle ne se trompe pas de plus en plus vite : elle se trompe de plus en plus, et de manière accélérée.**

**Où vous rencontrerez le terme.** Téléphones · véhicules · aéronautique · robotique · plateformes stabilisées · forage · sous-marin.

**Ce que ça permet.** Une navigation totalement autonome, insensible au brouillage, disponible en intérieur, sous l'eau et sous terre — **pendant un temps limité**.

**Ce qui bloque.** **La dérive.** L'écart entre les classes de performance couvre plusieurs ordres de grandeur. La grandeur usuelle est la **stabilité de biais du gyromètre**, exprimée en degrés par heure : de l'ordre de la dizaine à la centaine de degrés par heure pour un capteur de grande diffusion, de l'ordre de l'unité au dixième de degré par heure pour un capteur dit tactique, et en deçà du centième pour un équipement de navigation de haut de gamme — au prix d'un coût, d'une masse et d'un volume sans commune mesure.

**Trois précautions de lecture, et elles comptent plus que les chiffres.** Les noms de classes — grand public, industriel, tactique, navigation — sont des **conventions commerciales sans définition normative**, et leurs bornes varient d'un fournisseur à l'autre. La stabilité de biais *en fonctionnement* n'est pas la **répétabilité au démarrage**, souvent bien plus mauvaise et rarement mise en avant. Et une bonne stabilité de biais ne borne pas seule la dérive : la marche aléatoire angulaire et la sensibilité thermique y contribuent autant. **Un chiffre unique de dérive, sans le protocole qui l'a produit, n'est pas une information exploitable** — c'est le cas d'école du chapitre 4.

**Ce que cela implique.** L'inertiel est presque toujours **couplé** à une source de recalage périodique. Cette architecture — un système précis à court terme associé à un système stable à long terme — est un motif que l'on retrouve dans de nombreux domaines de la mesure.

**À ne pas confondre avec.** **Le positionnement satellitaire**, qui est une référence externe. Les deux sont complémentaires et non substituables.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Les capteurs microfabriqués ont diffusé massivement à bas coût ; les technologies de haute performance restent coûteuses et soumises à contrôle à l'exportation dans certaines classes.
> 🔄 **À revoir si** une technologie de gyromètre de haute performance devient fabricable par les procédés de la microélectronique de masse.

**Renvois** — Couche : percevoir · Convergences : autonomie mobile (39), robotique généraliste (36).

---
