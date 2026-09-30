---
title: ◆◆◆ Neuromorphique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — famille · **Couche** — calculer

**En une phrase.** Des architectures inspirées de l'organisation du système nerveux : calcul et mémoire colocalisés, communication par impulsions brèves, activité déclenchée par l'événement plutôt que par une horloge.

**Pourquoi on en parle.** Parce que le terme est employé pour des objets très différents, et parce que l'approche attaque simultanément les deux contraintes de la couche : le déplacement des données et l'énergie.

**Comment ça fonctionne.** Trois principes, qui peuvent être adoptés séparément — d'où la confusion.

**La colocalisation** : chaque unité de calcul possède sa propre mémoire locale, supprimant les transferts longue distance.

**La communication par impulsions** : les unités n'échangent pas des valeurs continues mais des impulsions brèves, dont l'information réside dans l'instant d'émission. Une unité qui n'a rien à dire ne consomme rien.

**Le fonctionnement événementiel** : il n'y a pas d'horloge globale ; l'activité se déclenche à l'arrivée d'un événement. Sur des données naturellement éparses, la consommation chute d'un ou deux ordres de grandeur.

**Ce que ça permet.** Un traitement continu à très faible consommation, particulièrement adapté aux flux d'événements — reconnaissance de motifs sur signaux, traitement de sorties de caméras événementielles, surveillance permanente sur alimentation contrainte.

**Ce qui bloque.** **L'entraînement.** Les méthodes qui ont fait le succès de l'apprentissage profond supposent des grandeurs continues et différentiables ; les impulsions ne le sont pas. On contourne par conversion depuis un réseau classique, au prix d'une partie du gain, ou par des méthodes spécifiques encore moins matures.

S'y ajoute **l'absence complète d'écosystème** : outils, formats, jeux de données, métriques et compétences ont tous été construits pour le paradigme dominant.

**Ce que cela implique.** C'est l'entrée qui illustre le mieux l'observation d'ouverture du chapitre : **le verrou n'est pas physique, il est écosystémique.** Les composants existent et fonctionnent ; ce qui manque est tout ce qui permettrait de les utiliser sans être spécialiste.

**À ne pas confondre avec.** **Les réseaux de neurones artificiels courants**, qui s'exécutent sur du matériel conventionnel et n'ont d'inspiration biologique que le nom. **Le calcul analogique**, avec lequel le neuromorphique se combine souvent sans se confondre.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Puces disponibles auprès de plusieurs acteurs, applications de niche établies en traitement de signal à très faible consommation, adoption générale absente.
> 🔄 **À revoir si** une méthode d'entraînement native atteint des performances comparables au paradigme dominant sur une tâche de référence reconnue.

**Renvois** — Couche : calculer · Convergence : intelligence distribuée (38) · Voir aussi : caméras événementielles (ch. 6).

---
