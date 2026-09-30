---
title: ◆◆ Autonomie supervisée
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — doctrine · **Couche** — décider

**En une phrase.** Une machine décide et agit ; un humain surveille et peut intervenir.

**Pourquoi on en parle.** Parce que **c'est le régime réel de la quasi-totalité des systèmes déployés**, et parce que son économie dépend d'un paramètre rarement publié.

**Comment ça fonctionne — trois configurations à distinguer.**

**Humain dans la boucle** : la machine propose, l'humain valide avant exécution. Sûr, mais le débit est borné par l'humain.

**Humain sur la boucle** : la machine agit, l'humain observe et peut interrompre. C'est le régime le plus courant, et le plus délicat.

**Humain en réserve** : la machine agit seule et sollicite l'humain uniquement en cas de blocage. C'est le régime qui permet à un opérateur de superviser plusieurs machines — et donc le seul qui produise un gain économique net.

**Ce qui bloque — et c'est un problème humain, pas technique.** **La vigilance.** Un opérateur qui surveille un système fiable pendant des heures n'est pas dans un état permettant de reprendre le contrôle en quelques secondes. Plus le système est fiable, moins l'humain est prêt — **la fiabilité dégrade la supervision qu'elle rend nécessaire**.

**Ce paradoxe n'est pas une intuition : il est établi dans la littérature des facteurs humains depuis les années 1980**, sous le nom d'*ironies de l'automatisation* — l'article fondateur de Lisanne Bainbridge, publié en 1983 dans *Automatica*, reste l'une des références les plus citées du domaine. Il décrit trois effets que quarante ans de travaux ont confirmés plutôt qu'infirmés : **la vigilance décroît** lors d'une surveillance prolongée d'un système qui ne défaille pas ; **les compétences s'atrophient** faute d'être exercées, précisément celles qu'exige la reprise ; et **la confiance excessive** conduit à suivre le système quand il se trompe et à ne pas voir qu'il a échoué — un mécanisme attentionnel que l'expérience et la formation ne suppriment pas.

**Ce que la littérature ne dit pas**, et qu'il faut se garder de lui faire dire : elle n'a pas produit de loi quantitative transposable. **Les durées au-delà desquelles la vigilance se dégrade dépendent de la tâche, du taux d'événements et de l'organisation** ; elles se mesurent sur un déploiement, elles ne se lisent pas dans un tableau. La conséquence pratique est en revanche stable : **on conçoit contre ce paradoxe** — par la rotation, la charge de travail maintenue, la conception des alertes — plutôt qu'on ne le résout par un supplément de fiabilité.

S'y ajoute **le délai de reprise** : entre l'alerte et l'action correcte, il faut comprendre la situation, ce qui prend du temps même pour un opérateur attentif.

**Ce que cela implique.** **Le ratio d'opérateurs par machine est la grandeur économique décisive** de tout déploiement autonome. Un ratio de un pour un ne réduit pas le coût du travail : il le déplace, éventuellement vers un lieu moins cher, ce qui est une décision différente de l'automatisation.

**À ne pas confondre avec.** **La téléopération** (ch. 15), où l'humain décide. Ici, la machine décide.

> ⏱ **État au 23/08/2026** — 🏭 déployé, régime dominant de tous les systèmes autonomes en exploitation.
> 🔄 **À revoir si** des exploitants publient couramment leur ratio de supervision, ce qui rendrait comparables les économies annoncées.

**Renvois** — Couche : décider · Convergence : autonomie mobile (39) · Voir aussi : automatisation, agentivité, autonomie (ch. 12).

---
