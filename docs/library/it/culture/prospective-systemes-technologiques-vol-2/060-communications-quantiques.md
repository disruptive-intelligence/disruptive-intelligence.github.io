---
title: ◆◆ Communications quantiques
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — relier, vérifier

**En une phrase.** Utiliser des propriétés quantiques pour transmettre de l'information de manière dont la sécurité repose sur la physique plutôt que sur une hypothèse calculatoire.

**Comment ça fonctionne.** L'application principale est la **distribution quantique de clés**. Deux parties échangent des états quantiques ; toute tentative d'interception les perturbe de façon détectable. Les parties comparent un échantillon, détectent une éventuelle écoute et, en son absence, disposent d'une clé partagée dont la confidentialité repose sur les lois physiques.

**Ce qui bloque.** **La distance.** Les signaux s'atténuent et **on ne peut pas amplifier un état quantique** — un répéteur classique le détruirait. La portée est donc limitée à quelques centaines de kilomètres en fibre, ce qui impose soit des relais de confiance, qui affaiblissent la garantie, soit des liaisons satellitaires, soit des répéteurs quantiques encore expérimentaux.

S'y ajoutent le **débit**, faible, et le fait que **cela ne résout qu'un problème** : l'échange de clés. L'authentification, l'intégrité et la signature restent à assurer par d'autres moyens.

**Ce que cela implique.** La distribution quantique de clés et la cryptographie post-quantique sont deux réponses au même risque, de natures différentes : l'une repose sur la physique et exige du matériel dédié, l'autre repose sur de nouvelles hypothèses mathématiques et se déploie logiciellement.

**Les positions publiques des autorités nationales de sécurité convergent davantage qu'on ne le dit, et c'est un point de vocabulaire à tenir.** Une prise de position commune de plusieurs agences européennes — dont les agences française, allemande, néerlandaise et suédoise — conclut que la technologie actuelle ne convient qu'à des usages de niche et que la cryptographie post-quantique et les clés symétriques prépartagées doivent être les solutions principales. Les agences américaine et britannique vont plus loin et ne soutiennent pas son emploi pour leurs systèmes gouvernementaux ou de sécurité nationale tant que ses limites ne sont pas levées.

**Trois arguments reviennent dans tous ces textes**, et ils sont techniques et non doctrinaux : la distribution quantique de clés **n'assure pas l'authentification**, qui reste à fournir par de la cryptographie classique ou post-quantique ; elle exige un **matériel spécialisé** et des liaisons dédiées, là où la seconde est une mise à jour logicielle ; et les **relais de confiance** réintroduisent une hypothèse de confiance physique que la garantie théorique prétendait supprimer.

**Ce que ce désaccord n'est pas.** Un débat sur la physique, qui n'est pas contestée. **C'est un désaccord sur le rapport entre le bénéfice et le coût d'infrastructure** — exactement la forme de verrou décrite au chapitre 3, et la raison pour laquelle des politiques publiques de soutien à des infrastructures de communication quantique coexistent sans contradiction avec ces réserves techniques.

**À ne pas confondre avec.** **Le calcul quantique**, dont c'est un domaine entièrement distinct. **La cryptographie post-quantique** (ch. 29), qui n'a rien de quantique — c'est de la cryptographie classique résistante à un attaquant quantique.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Liaisons opérationnelles sur des périmètres restreints et démonstrations satellitaires ; répéteurs quantiques en recherche.
> 🔄 **À revoir si** un répéteur quantique fonctionnel permet une liaison longue distance sans relais de confiance.

**Renvois** — Couche : relier, vérifier · Voir aussi : cryptographie post-quantique (ch. 29).

---


## Clôture de la couche B — Calculer


### Ce que les quinze entrées font apparaître

**Un. Le verrou de cette couche est presque toujours l'écosystème, pas la physique.** Sur les six entrées du chapitre 9, six butent principalement sur les outils, les compilateurs, les méthodes de test et les compétences. Une alternative doit être meilleure **d'un facteur** pour absorber ce coût — ce qui explique pourquoi elles percent d'abord dans des niches où le calcul classique est particulièrement mauvais, jamais en concurrence frontale.

**Deux. Le mur de la mémoire structure tout le chapitre 8.** Cinq entrées sur six l'attaquent : l'assemblage rapproche, la mémoire empilée élargit, le calcul en mémoire supprime le déplacement, la faible précision réduit le volume à déplacer. Seul le FPGA relève d'une autre logique. **C'est la démonstration la plus nette de l'atlas qu'une contrainte unique peut organiser un domaine entier.**

**Trois. Trois entrées de cette couche sont classées 🔭 prospectif** — calcul photonique, calcul supraconducteur, calcul quantique. C'est la proportion la plus élevée de tout l'atlas, et elle est cohérente : c'est la couche où l'on tente de sortir d'un paradigme qui fonctionne.

**Quatre. Le déplacement du goulet est observable à l'intérieur même de la couche.** La fabrication a cédé la place à l'assemblage, qui a cédé la place à la mémoire, qui cède la place à l'énergie et au refroidissement — et, à l'échelle du bâtiment, au raccordement électrique. **Le dossier 40 traitera cette chaîne complète.**


### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | accélérateurs, calcul en mémoire, faible précision, neuromorphique, mémoires à forte bande passante |
| **40 — Énergie et calcul** | accélérateurs, chiplets, mémoires, calcul en mémoire, photonique intégrée, calcul photonique |

**Le dossier 40 mobilise six entrées de cette seule couche** — et son maillon en retard est pourtant le raccordement électrique, qui relève de la couche *alimenter*. **Deuxième vérification de la thèse du volume.**

---

---

---


### Couche C — Apprendre et décider

---
