---
title: ◆◆◆ Domaine de conception opérationnelle
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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
