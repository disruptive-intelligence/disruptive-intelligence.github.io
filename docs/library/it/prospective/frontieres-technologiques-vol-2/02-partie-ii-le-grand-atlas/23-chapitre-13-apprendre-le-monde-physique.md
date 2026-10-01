---
title: Chapitre 13 — Apprendre le monde physique
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Ce que ce chapitre ajoute.** Les chapitres 11 et 12 traitaient de systèmes agissant sur de l'information. Celui-ci traite de systèmes qui produisent **des commandes destinées à des actionneurs** — et cela change la nature des contraintes.
>
> **Trois différences avec le monde logiciel.** Une erreur n'est pas toujours rattrapable. Les données ne se collectent pas en ligne mais s'acquièrent une interaction à la fois. Et le monde ne se réinitialise pas.
>
> **Sept entrées.** C'est le chapitre le plus directement lié au dossier de convergence 36.

---

## ◆◆◆ Modèles du monde

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Un modèle qui apprend à prédire l'évolution d'un environnement, de sorte qu'un système puisse anticiper les conséquences d'une action avant de l'exécuter.

**Pourquoi on en parle.** Parce que c'est la réponse proposée au problème de coût des données physiques : si un système peut simuler intérieurement les conséquences de ses actions, il peut apprendre sans agir.

**Comment ça fonctionne.** Le modèle est entraîné à prédire l'état suivant à partir de l'état courant et de l'action envisagée. Une fois cette prédiction assez fiable, le système peut **dérouler mentalement** plusieurs séquences d'actions et choisir celle dont le résultat prédit est le meilleur — sans les exécuter.

**Ce que ça permet.** Réduire le nombre d'interactions réelles nécessaires · anticiper au lieu de réagir · évaluer une action risquée sans la tenter.

**Ce qui bloque.** **L'accumulation d'erreur de prédiction.** Chaque pas prédit introduit une erreur, et prédire loin revient à composer ces erreurs : au-delà de quelques pas, la prédiction diverge. L'horizon utile est donc court, et l'étendre est le sujet actif.

**La physique du contact** est particulièrement difficile à prédire : au moment où deux objets se touchent, la dynamique change brutalement et de faibles écarts de position produisent des résultats très différents.

**Et une difficulté de fond** : le modèle prédit ce qu'il a observé. Face à une situation inhabituelle, il produit une prédiction plausible et fausse — sans le signaler.

**Ce que cela implique.** Un modèle du monde ne supprime pas le besoin de données réelles : **il l'exporte vers la validation**. Il faut vérifier que les prédictions correspondent au réel, ce qui exige d'agir dans le réel.

**À ne pas confondre avec.** **Un simulateur physique**, construit à partir d'équations connues et non appris. **Un jumeau numérique** (ch. 34), qui est synchronisé sur un système existant et n'a pas vocation à généraliser.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Résultats convaincants sur horizon court et environnements maîtrisés ; extension à des environnements ouverts non établie.
> 🔄 **À revoir si** un modèle du monde permet un apprentissage de manipulation en environnement varié avec un volume d'interactions réelles réduit d'un ordre de grandeur.

**Renvois** — Couche : apprendre et décider · Courants : Physical AI, embodied AI (ch. 33) · Convergences : robotique généraliste (36), autonomie mobile (39).

---

## ◆◆◆ VLA — Vision-Language-Action

**Niveau** — architecture · **Couche** — percevoir, apprendre et décider, agir

**En une phrase.** Une architecture qui prend en entrée une observation visuelle et une instruction en langage, et produit directement une commande motrice.

**Pourquoi on en parle.** Parce que c'est **l'objet technique concret derrière le cadrage « Physical AI »** — et parce que le terme circule largement sans que son contenu soit clair.

**Comment ça fonctionne.** Le principe est de traiter la commande motrice comme une modalité de sortie parmi d'autres. Le modèle reçoit une image et une instruction, les projette dans une représentation commune, et produit une séquence d'actions — positions articulaires, déplacements, ouvertures de préhenseur — de la même manière qu'un modèle de langage produit une suite de mots.

**Ce que cela change.** Auparavant, un robot enchaînait des modules séparés : perception, puis planification, puis contrôle. Chaque interface entre modules était un endroit où l'information se perdait. Une architecture VLA **supprime ces interfaces** en apprenant la correspondance de bout en bout — c'est le pari, et c'est aussi ce qui rend le comportement difficile à analyser quand il échoue.

**Où vous rencontrerez le terme.** Robotique · humanoïdes · manipulation · publications et communications sur la Physical AI.

**Ce que ça permet.** Exécuter une instruction formulée en langage naturel sur une tâche non spécifiquement programmée · transférer partiellement une compétence d'un objet à un objet similaire · réduire le travail d'ingénierie par tâche.

**Ce qui bloque.** **Les données.** Il faut des exemples associant observation, instruction et action réelle, et ils s'acquièrent une démonstration à la fois — par téléopération, le plus souvent. Il n'existe aucun équivalent physique d'un corpus textuel collecté en ligne, et **c'est le verrou central**.

**Le transfert entre plateformes.** Les données collectées sur un robot ne se transposent pas directement sur un autre, dont la géométrie et la dynamique diffèrent. Cela fragmente l'effort de collecte.

**La fiabilité.** Les taux de succès démontrés sur des tâches variées restent très en dessous de ce qu'exige une exploitation sans surveillance, et l'écart se creuse quand l'environnement s'écarte des conditions d'entraînement.

**Ce que cela implique.** Un VLA est **une architecture, pas un robot** — c'est la confusion à éviter absolument. Et sa progression se mesure moins par les démonstrations que par deux grandeurs : le volume de données d'interaction disponible et le degré de transfert entre plateformes.

**À ne pas confondre avec.** **Un modèle vision-langage**, qui décrit une scène sans produire d'action. **Un humanoïde** (ch. 15), qui est une plateforme. **Physical AI** (ch. 33), qui est un cadrage englobant.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrations nombreuses sur des tâches variées en environnement maîtrisé ; efforts de constitution de jeux de données partagés entre laboratoires et industriels ; pas de déploiement autonome en exploitation.
> 🔄 **À revoir si** un jeu de données d'interaction physique partagé entre plusieurs plateformes atteint une taille permettant un transfert mesurable d'une plateforme à une autre.

**Renvois** — Couche : percevoir, apprendre, agir · Courants : Physical AI, embodied AI (ch. 33) · Convergence : robotique généraliste (36).

---

## ◆◆ Embodied AI

**Niveau** — cadrage · **Couche** — percevoir, apprendre, agir

**En une phrase.** La thèse selon laquelle un système apprenant doté d'un corps et interagissant avec un environnement acquiert des capacités qu'un système traitant uniquement des données ne peut acquérir.

**Ce qu'il faut en savoir.** C'est **une hypothèse scientifique avant d'être une catégorie de produits**, et elle a une histoire académique de plusieurs décennies. Son intérêt pratique est de rappeler que certaines compétences — anticiper une conséquence physique, adapter une force, comprendre une occlusion — s'apprennent difficilement sans agir.

**Ce qui bloque.** **Le coût de l'incarnation.** Apprendre par interaction suppose du matériel, du temps réel, de l'usure et des erreurs coûteuses. C'est ce qui rend le domaine lent comparé à l'apprentissage sur données.

**À ne pas confondre avec.** **Humanoïde.** Un bras fixe, un drone, un véhicule sont des systèmes incarnés. **C'est la confusion la plus fréquente du domaine**, et elle conduit à surestimer l'importance de la forme.

> ⏱ **État au 23/08/2026** — cadrage, avec des travaux actifs. Les résultats les plus solides restent obtenus en environnement contraint.
> 🔄 **À revoir si** un apprentissage par interaction produit une capacité qu'aucun apprentissage sur données n'a permis d'obtenir, de façon reproductible.

**Renvois** — Couche : percevoir, apprendre, agir.

---

## ◆◆ Apprentissage par imitation

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Apprendre une tâche en reproduisant des démonstrations effectuées par un opérateur humain.

**Comment ça fonctionne.** Un opérateur exécute la tâche, souvent par téléopération, pendant que le système enregistre observations et actions. Le modèle apprend ensuite à produire l'action associée à chaque observation.

**Ce que ça permet.** Acquérir une compétence sans la spécifier · exploiter le savoir-faire d'un opérateur qui ne saurait pas l'expliciter · démarrer un apprentissage sans définir de fonction de récompense.

**Ce qui bloque.** **La dérive.** Le système apprend à agir dans les situations que l'humain a rencontrées ; dès qu'il s'en écarte un peu, il se retrouve dans des situations non démontrées, où il agit mal, ce qui l'en écarte davantage. **L'erreur s'auto-amplifie**, et c'est le problème structurel de la méthode.

S'y ajoutent le **coût de collecte** — une démonstration à la fois — et le fait que les démonstrations humaines contiennent des corrections implicites difficiles à reproduire.

**Ce que cela implique.** C'est **la source principale des données physiques** aujourd'hui, et donc le facteur limitant des architectures du chapitre. La téléopération n'est pas un pis-aller : c'est l'infrastructure de collecte.

**À ne pas confondre avec.** **L'apprentissage par renforcement**, qui apprend par essai et récompense sans démonstration.

> ⏱ **État au 23/08/2026** — 🏭 déployé en recherche et en pré-industrialisation, méthode dominante pour la manipulation.
> 🔄 **À revoir si** une méthode de collecte permet d'acquérir des démonstrations à un coût significativement inférieur à la téléopération individuelle.

**Renvois** — Convergence : robotique généraliste (36) · Voir aussi : téléopération (ch. 15).

---

## ◆◆ Apprentissage par renforcement

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Apprendre par essais successifs, guidé par un signal de récompense qui indique si le résultat est meilleur ou moins bon.

**Ce que ça permet.** Découvrir des stratégies qu'aucun humain n'aurait démontrées · optimiser un comportement selon un critère explicite · s'améliorer au-delà de la performance des démonstrations.

**Ce qui bloque.** **La conception de la récompense.** Le système optimise exactement ce qu'on mesure, ce qui n'est jamais exactement ce qu'on veut — et il trouve des moyens inattendus de maximiser la mesure sans atteindre l'objectif. **Le nombre d'essais** : en environnement physique, les essais coûtent du temps, de l'usure et parfois du matériel, ce qui pousse à apprendre en simulation. Et **la sécurité pendant l'apprentissage**, qui interdit l'exploration libre sur un système réel.

**Ce que cela implique.** En robotique, le renforcement s'emploie presque toujours **en simulation puis transféré**, ce qui déplace la difficulté vers l'entrée suivante.

**À ne pas confondre avec.** **L'ajustement sur préférences** utilisé pour les modèles de langage, qui emploie des techniques voisines pour un problème différent.

> ⏱ **État au 23/08/2026** — 🏭 déployé, méthode établie. Emploi en environnement physique généralement médié par la simulation.
> 🔄 **À revoir si** un apprentissage direct sur système physique devient praticable en toute sécurité et en un nombre d'essais raisonnable.

**Renvois** — Couche : apprendre et décider.

---

## ◆◆◆ Sim-to-real

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Entraîner un système en simulation, puis transférer le comportement appris sur un système physique.

**Pourquoi on en parle.** Parce que c'est **la réponse principale au coût des données physiques** — et parce que l'écart entre simulation et réel est le verrou qui décide de son efficacité.

**Comment ça fonctionne.** On entraîne dans un simulateur, où les essais sont rapides, parallélisables, sans usure et sans risque. Puis on transfère.

**Le problème est l'écart de réalité.** Aucune simulation ne reproduit exactement les frottements, les jeux, les déformations, les délais de capteur et les propriétés des matériaux. Un comportement optimal en simulation exploite souvent des particularités du simulateur qui n'existent pas dans le monde.

**La parade principale est la randomisation.** Plutôt que de simuler précisément, on fait varier aléatoirement les paramètres — masses, frottements, éclairages, délais — pendant l'entraînement. Le système apprend alors un comportement qui fonctionne sur toute une famille de mondes possibles, dont le monde réel fait partie. **On renonce à l'exactitude pour obtenir de la robustesse** — c'est un compromis, et il coûte en performance de pointe.

**Ce que ça permet.** Réduire massivement le besoin d'interactions réelles · explorer des situations dangereuses sans risque · paralléliser l'apprentissage.

**Ce qui bloque.** **La physique du contact**, mal simulée : c'est là que l'écart est le plus grand, et c'est précisément ce dont la manipulation dépend. **La perception** : les images simulées diffèrent des images réelles de façon subtile. Et **la validation**, qui exige de toute façon des essais réels.

**Ce que cela implique.** Le transfert fonctionne bien pour la locomotion et le déplacement, où la physique est dominée par des effets bien modélisés. Il fonctionne mal pour la manipulation fine. **C'est cohérent avec le fait que manipuler soit plus difficile que se déplacer** — et cela indique où le progrès compte.

**À ne pas confondre avec.** **La simulation d'ingénierie**, qui vise la fidélité pour dimensionner. Ici, la fidélité n'est pas l'objectif : la robustesse l'est.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour la locomotion, 🔬 émergent pour la manipulation.
> 🔄 **À revoir si** un simulateur de contact atteint une fidélité permettant un transfert direct de comportements de manipulation fine sans réglage sur le système réel.

**Renvois** — Couche : apprendre et décider · Convergences : robotique généraliste (36), autonomie mobile (39).

---

## ◆◆ Modèles de fondation robotiques

**Niveau** — plateforme · **Couche** — apprendre et décider, agir

**En une phrase.** Un modèle pré-entraîné sur de larges volumes de données d'interaction physique, destiné à être adapté à des plateformes et des tâches variées.

**Ce que ça permet.** Mutualiser l'effort de collecte entre acteurs · réduire le travail d'adaptation par plateforme · faire bénéficier une tâche nouvelle de compétences acquises ailleurs.

**Ce qui bloque.** **L'hétérogénéité des plateformes.** Contrairement au texte, où un corpus est universel, les données physiques sont liées à une géométrie, une dynamique et un jeu de capteurs. Constituer un socle transférable suppose d'abstraire ces différences — et c'est un problème ouvert.

S'y ajoute la **taille des données disponibles**, sans commune mesure avec celle des corpus textuels.

**Ce que cela implique.** Si ce socle se constitue, il déplace le verrou du dossier 36 : la collecte cesserait d'être refaite par chaque acteur. **C'est le signal le plus important à surveiller dans toute cette couche.**

**À ne pas confondre avec.** **Un VLA**, qui est une architecture. Un modèle de fondation robotique peut employer une architecture VLA, ou une autre.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Plusieurs initiatives de mutualisation de données entre laboratoires et industriels ; transfert entre plateformes partiel.
> 🔄 **À revoir si** un modèle pré-entraîné sur données mutualisées surpasse, sur une plateforme donnée, un modèle entraîné uniquement sur les données de cette plateforme.

**Renvois** — Convergence : robotique généraliste (36).

---
