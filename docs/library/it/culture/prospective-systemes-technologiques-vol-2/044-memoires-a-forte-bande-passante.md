---
title: ◆◆ Mémoires à forte bande passante
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — composant · **Couche** — calculer

**En une phrase.** Des mémoires empilées et connectées très largement au processeur, conçues pour livrer beaucoup de données par seconde plutôt que pour stocker beaucoup.

**Pourquoi on en parle.** Parce que **c'est le vrai goulet de l'inférence**, et parce que leur disponibilité conditionne celle des accélérateurs.

**Comment ça fonctionne.** Plutôt que de placer la mémoire à côté du processeur et de la relier par un nombre limité de connexions, on empile plusieurs couches de mémoire et on les relie par un très grand nombre de liaisons courtes traversant les couches. La bande passante augmente d'un ordre de grandeur, et l'énergie par donnée transférée diminue.

**Ce que ça permet.** Alimenter un accélérateur assez vite pour qu'il soit effectivement utilisé — sans quoi la puissance de calcul annoncée reste théorique.

**Ce qui bloque.** **La fabrication et le rendement de l'empilement**, qui exigent un alignement de très haute précision. **Le coût**, sensiblement supérieur à celui d'une mémoire classique à capacité égale. **La thermique**, la mémoire empilée se trouvant à proximité immédiate d'une source de chaleur importante. Et **la capacité** : ces mémoires offrent moins de gigaoctets qu'une mémoire classique de même prix.

**Ce que cela implique.** Le dimensionnement d'un système d'inférence est souvent commandé par la mémoire disponible, non par la puissance de calcul — ce qui explique pourquoi la taille d'un modèle exécutable dépend d'abord de ce paramètre.

**À ne pas confondre avec.** **La mémoire vive classique**, dont l'objectif est la capacité. **Le cache**, intégré au processeur, bien plus rapide et bien plus petit.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Capacité de production identifiée comme facteur limitant de l'ensemble de la filière des accélérateurs.
> 🔄 **À revoir si** une technologie de mémoire offre simultanément la bande passante de l'empilement et la capacité de la mémoire classique.

**Renvois** — Couche : calculer · Convergences : énergie et calcul (40), intelligence distribuée (38).

---
