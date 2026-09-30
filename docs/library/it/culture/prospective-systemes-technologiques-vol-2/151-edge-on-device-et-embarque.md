---
title: ◆◆◆ Edge, on-device et embarqué
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — doctrine et capacité · **Couche** — calculer, relier

**En une phrase.** Trois termes qui désignent le fait de traiter l'information près de sa source plutôt que dans une infrastructure distante — et qui ne sont pas interchangeables.

**Pourquoi cette entrée est comparative.** Parce que ces trois mots circulent comme des synonymes, qu'ils se recouvrent largement, et que **la frontière entre eux détermine des choix de conception très différents**. C'est le cas le plus net de l'atlas où la distinction vaut plus que la description.

**Où passent les frontières.**

**Edge** désigne une **position dans une architecture** : le traitement s'effectue à la périphérie du réseau, entre l'objet et le centre de données. Cela peut être une passerelle industrielle, une armoire en pied d'antenne, un serveur local. **Le critère est la position réseau**, pas la nature de la machine.

**On-device** désigne une **exécution sur l'appareil de l'utilisateur final** — téléphone, ordinateur, véhicule. Le critère est la propriété de la machine, et la conséquence est que **la donnée ne quitte pas l'appareil**, ce qui est un argument de confidentialité autant que de latence.

**Embarqué** désigne une **contrainte de ressources et souvent de temps réel** : calculateur intégré à un équipement, avec une enveloppe de mémoire, d'énergie et de dissipation figée à la conception, et parfois une exigence de déterminisme.

**Les recouvrements.** Un modèle exécuté sur un téléphone est à la fois *on-device* et *embarqué*. Un calculateur de véhicule est *embarqué* et peut être considéré comme *edge* dans une architecture de flotte. Un serveur en pied d'antenne est *edge* sans être ni l'un ni l'autre. **Aucun des trois n'implique les deux autres.**

**Les quatre motifs de rapprocher le calcul**, et ils n'ont pas les mêmes conséquences. La **latence** — la borne physique du chapitre 24 ne se négocie pas, seul le rapprochement la réduit. Le **coût par appel** — un traitement local ne se facture pas. La **confidentialité** — la donnée qui ne part pas ne peut pas être interceptée en transit. L'**indépendance** — fonctionner sans liaison.

**Ce qui bloque.** **La mise à jour.** Un modèle distant se corrige en une opération ; un modèle déployé sur un million d'appareils se corrige au rythme du parc, avec des versions hétérogènes en service simultanément. **C'est la dette de maintenance que le cadrage « edge » masque systématiquement.**

**Les ressources** : mémoire disponible avant puissance de calcul, comme l'a établi la couche *calculer*. **L'énergie**, sur un appareil alimenté par batterie. Et **l'observabilité** : un traitement local est plus difficile à superviser et à diagnostiquer.

**Ce que cela implique.** Le placement du calcul est un **arbitrage à quatre variables** — latence, coût, confidentialité, maintenabilité — et non une tendance. Les architectures qui réussissent combinent les deux : traitement local pour la réaction, traitement distant pour l'apprentissage et la mise à jour.

**À ne pas confondre avec.** Le **cloud**, qui est également un modèle de déploiement et non une technologie. Les deux sont complémentaires, et l'opposition entre eux est un artefact de vocabulaire.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Exécution locale de modèles disponible sur des appareils courants ; architectures mixtes devenues la norme.
> 🔄 **À revoir si** un mécanisme de mise à jour de modèles sur parc dispersé devient assez fiable pour supprimer la contrainte de maintenance.

**Renvois** — Couche : calculer, relier · Courant : edge AI (ch. 32) · Convergences : intelligence distribuée (38), énergie et calcul (40) · **Support du lab 5.**

---


## ◆◆ Continuum cloud-edge

**Niveau** — doctrine · **Couche** — calculer, relier

**En une phrase.** Traiter l'ensemble des ressources de calcul — appareil, périphérie, centre de données — comme un continuum sur lequel on place dynamiquement les traitements.

**Ce que ça permet.** Adapter le placement aux conditions du moment · basculer un traitement quand la liaison se dégrade · optimiser le coût en déplaçant les charges non urgentes.

**Ce qui bloque.** **L'hétérogénéité.** Les ressources diffèrent par leur architecture, leur mémoire, leur système ; un traitement portable sur tout le continuum suppose une abstraction coûteuse. **La supervision** d'un système dont les composants s'exécutent en des lieux variables. Et **la donnée** : déplacer un traitement suppose de déplacer ou de répliquer ce sur quoi il travaille, ce qui coûte souvent plus que le traitement lui-même.

**Ce que cela implique.** Le continuum est **une ambition d'architecture plus qu'une réalité déployée**. Les systèmes existants placent les traitements à la conception et non dynamiquement — et la question du déplacement de la donnée reste le principal obstacle.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Orchestration entre périphérie et centre disponible, placement dynamique en fonction des conditions encore limité.
> 🔄 **À revoir si** un déplacement automatique de traitement en fonction des conditions réseau devient une pratique courante en production.

**Renvois** — Couche : calculer, relier.

---
