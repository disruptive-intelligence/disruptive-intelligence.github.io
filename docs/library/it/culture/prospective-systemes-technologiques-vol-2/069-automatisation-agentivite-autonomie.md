---
title: ◆◆◆ Automatisation, agentivité, autonomie
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — cadrage analytique · **Couche** — décider

**En une phrase.** Trois régimes distincts, qui n'appellent ni les mêmes preuves, ni les mêmes garanties, ni les mêmes responsabilités — et que le vocabulaire courant confond.

**Pourquoi cette entrée existe.** Parce que c'est la distinction la plus opérationnelle de toute la couche, et qu'aucun terme du marché ne la porte.

**Les trois régimes.**

**L'automatisation.** Le système exécute une séquence définie à l'avance. Toutes les situations prévues ont une réponse spécifiée ; les autres provoquent un arrêt ou une alerte. **Ce qu'il faut prouver** : que la séquence est correcte et que les situations non prévues sont bien détectées. C'est un problème de vérification classique, et il se traite.

**L'agentivité.** Le système décompose un objectif en étapes qu'il choisit, dans un espace d'actions défini par son concepteur. Il ne sort pas de cet espace, mais l'enchaînement n'est pas prévu à l'avance. **Ce qu'il faut prouver** : que l'espace d'actions est correctement borné, et qu'aucune combinaison d'actions autorisées ne produit un effet inacceptable. **C'est beaucoup plus difficile**, parce que le nombre de combinaisons croît de façon explosive.

**L'autonomie.** Le système décide dans des situations non prévues, y compris celle de s'arrêter, de renoncer ou d'alerter. **Ce qu'il faut prouver** : qu'il reconnaît qu'il sort du domaine où son comportement a été validé — ce qui est le problème le plus difficile de la couche, et le sujet du chapitre 30.

**Où passe la frontière, en pratique.** La question à poser n'est pas « ce système est-il autonome ? » mais : **que fait-il quand il rencontre une situation à laquelle il n'a pas de réponse ?** Un système qui s'arrête est automatisé. Un système qui essaie autre chose dans son répertoire est agentique. Un système qui décide d'une action hors répertoire — y compris ne rien faire et prévenir — est autonome.

**Ce que cela implique.** Chaque régime déplace la charge de la preuve, et l'écart de coût entre les trois est considérable. **Beaucoup de produits présentés comme autonomes sont agentiques ; beaucoup de produits présentés comme agentiques sont automatisés** avec une interface en langage naturel.

**À ne pas confondre avec.** **Les niveaux d'autonomie** définis dans certains secteurs, qui décrivent le partage de tâches entre humain et machine plutôt que la nature de la décision. Les deux grilles sont utiles et ne mesurent pas la même chose.

> ⏱ **État au 23/08/2026** — cadrage, sans état de maturité. La confusion des trois régimes est répandue et s'aggrave avec la diffusion du terme « agentique ».
> 🔄 **À revoir si** un référentiel sectoriel adopte une distinction équivalente, ce qui la rendrait opposable.

**Renvois** — Couche : décider · Courants : Agentic AI, autonomous systems, machine autonomy (ch. 32-33) · Convergence : autonomie mobile (39) · Voir aussi : architecture de sûreté (ch. 30).

---
