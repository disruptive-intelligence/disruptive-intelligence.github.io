---
title: ◆◆◆ Les bandes infrarouges — NIR, SWIR, MWIR, LWIR
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — percevoir

**En une phrase.** Selon la longueur d'onde observée, on ne voit pas la même chose : dans certaines bandes on voit ce qui est éclairé, dans d'autres on voit ce qui est chaud.

**Pourquoi on en parle.** C'est la distinction la plus utile de toute la couche, et la plus mal maîtrisée. Elle explique pourquoi il existe plusieurs familles de capteurs qui semblent faire la même chose, pourquoi leurs prix diffèrent d'un facteur cent, et pourquoi aucune ne remplace les autres.

**Comment ça fonctionne.** Tout corps émet un rayonnement du seul fait de sa température, et **plus il est chaud, plus ce rayonnement se déplace vers les courtes longueurs d'onde**. Un corps à température ambiante émet principalement autour de dix micromètres ; un moteur chaud dans l'infrarouge moyen ; le soleil dans le visible.

Il en découle deux manières de voir, radicalement différentes :

**Voir par réflexion** — une source éclaire la scène, les objets renvoient une partie du rayonnement. C'est le cas du visible, du proche infrarouge et du SWIR. Sans source, pas d'image.

**Voir par émission** — le capteur capte ce que les objets émettent eux-mêmes. C'est le cas du MWIR et du LWIR. **Aucun éclairage n'est nécessaire.**

| Bande | Domaine approximatif | Ce qu'on voit | Particularité |
|---|---|---|---|
| Visible | 0,4 – 0,7 µm | scène éclairée | proche de la perception humaine |
| NIR | 0,7 – 1 µm | scène faiblement éclairée | détecteurs silicium, peu coûteux |
| SWIR | 1 – 2,5 µm | réflexion, avec meilleure pénétration de brume | discrimination de matériaux, lecture à travers certains matériaux |
| MWIR | 3 – 5 µm | émission de corps chauds | fort contraste thermique, détecteurs souvent refroidis |
| LWIR | 8 – 14 µm | émission de corps à température ambiante | vision nocturne sans éclairage, détecteurs non refroidis possibles |

**L'atmosphère n'est pas transparente partout.** Certaines longueurs d'onde sont fortement absorbées par la vapeur d'eau et le dioxyde de carbone. Les bandes utilisées correspondent aux **fenêtres** où l'absorption est faible — ce n'est pas un choix technique mais une contrainte physique, et elle explique les intervalles du tableau ci-dessus.

**Où vous rencontrerez le terme.** Vision nocturne · maintenance prédictive et thermographie de bâtiment · agriculture · tri industriel · sécurité incendie · observation spatiale · véhicules · applications médicales.

**Ce que ça permet.** Voir sans éclairage · détecter un échauffement anormal avant qu'il ne soit visible · distinguer des matériaux d'apparence identique · voir partiellement à travers brume ou fumée selon la bande.

**Ce qui bloque.** **Le refroidissement**, pour les bandes moyennes : atteindre une sensibilité utile suppose souvent de descendre le détecteur à très basse température, ce qui ajoute un cryogénérateur — masse, consommation, bruit, durée de vie de quelques milliers d'heures. **La résolution**, bornée par le rapport entre longueur d'onde et diamètre d'optique : à ouverture égale, plus la longueur d'onde est grande, plus le détail accessible est grossier. Et **le coût des matériaux de détection** hors silicium.

**De quoi ça dépend.** Matériaux semi-conducteurs spécifiques à chaque bande · optiques transparentes dans la bande visée — le verre ordinaire ne l'est pas au-delà du proche infrarouge · cryogénie pour certaines applications.

**Ce que cela implique.** Un système de perception sérieux **combine plusieurs bandes**, parce qu'aucune n'est bonne partout. Et une performance annoncée n'a de sens qu'accompagnée de la bande : « voit dans le noir » peut désigner un dispositif à quelques centaines d'euros ou à plusieurs dizaines de milliers.

**À ne pas confondre avec.** **La vision nocturne par intensification**, qui amplifie la lumière résiduelle et exige donc qu'il en reste — voir l'entrée dédiée. **Le thermique et l'infrarouge en général** : tout thermique est infrarouge, tout infrarouge n'est pas thermique.

**Termes voisins.** *Imagerie thermique* désigne l'usage des bandes d'émission. *Bolométrie* désigne une technologie de détection, pas une bande.

> ⏱ **État au 23/08/2026** — 🏭 déployé, avec des maturités inégales selon les bandes. LWIR non refroidi : diffusion large, y compris grand public. SWIR : coût encore élevé, applications industrielles en croissance. MWIR refroidi : réservé aux hautes performances.
> 🔄 **À revoir si** une technologie de détection SWIR compatible avec les procédés silicium standard atteint la production série — cela déplacerait le coût de cette bande d'un ordre de grandeur.

**Renvois** — Couche : percevoir · Courant : optronique (ch. 35) · Convergences : autonomie mobile (39).

---
