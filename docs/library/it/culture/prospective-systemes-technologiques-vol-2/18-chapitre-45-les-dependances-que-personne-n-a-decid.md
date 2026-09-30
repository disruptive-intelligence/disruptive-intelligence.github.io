---
title: Chapitre 45 — Les dépendances que personne n'a décidées
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

## ① Ce qui devient abondant

**Les briques communes réutilisables**, disponibles à un coût si faible que les reconstruire n'est jamais le choix rationnel : une référence de temps et de position, un jeu de primitives cryptographiques, une identité machine, un modèle de fondation tiers, une bibliothèque, une capacité de calcul louée.

**Et c'est une bonne chose** — c'est même le mécanisme de diffusion décrit au chapitre 1. Chaque réutilisation est individuellement rationnelle, économe et sans alternative défendable au moment où elle est faite.

**Précision nécessaire, et elle définit le chapitre.** Il ne traite pas des dépendances **choisies** — un fournisseur, un contrat, un risque identifié et arbitré. Il traite de celles qui se constituent **par agrégation** : le chapitre 2 les nomme *infrastructures*, au sens de ce dont d'autres dépendent sans l'avoir choisi ni le contrôler. **Personne ne les a décidées, et pourtant elles existent.**

**Le volume 1 avait signalé ce phénomène comme un angle mort de sa propre méthode**, parce qu'une grille qui interroge une technologie à la fois ne peut pas voir une dépendance qui n'appartient à aucune d'entre elles. L'atlas en a produit cinq cas : positionnement et temps, congestion orbitale, cryptographie déployée, identité machine, modèles de fondation tiers.

---

## ② Ce qui devient rare

**La substituabilité.**

**Le mécanisme.** Une brique réutilisée par tout le monde cesse d'avoir des concurrents, non parce qu'elle les élimine, mais parce que **personne n'a plus intérêt à financer une alternative dont le seul usage serait de ne pas servir.** Le repli existe parfois techniquement — la navigation sans référence satellitaire en est l'exemple documenté au chapitre 6 — mais il est rarement entretenu, rarement exercé, et son coût réapparaît entièrement le jour où il faudrait s'en servir.

**La connaissance de sa propre dépendance.** Peu d'organisations savent dire de quelles briques leurs systèmes dépendent au troisième niveau. **Ce n'est pas de la négligence** : la dépendance est invisible dans les performances, elle n'apparaît dans aucune spécification, et elle ne se manifeste qu'à la défaillance.

**Le temps de sortie.** La cryptographie déployée en est le cas d'école : le chapitre 29 a établi qu'une migration porte sur un parc, des protocoles, des certifications et des produits embarqués dont la durée de vie dépasse la décennie. **Ce qui a été adopté en quelques années se remplace en quelques décennies** — et la crypto-agilité est précisément la reconnaissance de ce déséquilibre.

**Et l'autorité de gestion, dont le degré varie fortement selon les cas.** Le spectre fait exception : il dispose de régimes d'allocation et d'autorités de régulation nationales et internationales dotées d'un pouvoir contraignant réel. **Les quatre autres cas en sont dépourvus ou n'en ont qu'une forme coordinatrice sans sanction.** Les débris orbitaux le montrent sur un bien physique : chaque acteur a intérêt à utiliser la ressource, aucun n'a intérêt à en financer l'entretien, et la dégradation est le résultat agrégé de comportements dont aucun n'est fautif — **c'est un problème de bien commun mal gouverné, pas d'absence universelle de gouvernance.**

---

## ③ Ce qui ne change pas

**La structure d'incitation.** Prendre la brique la moins coûteuse reste, pour chaque acteur pris isolément, la bonne décision — y compris pour celui qui a parfaitement compris le mécanisme décrit ici. **Aucun progrès technique ne modifie cela**, parce que le problème n'est pas dans la brique.

**L'asymétrie entre constitution et sortie.** Une dépendance se constitue sans coordination, gratuitement, par addition de choix indépendants. Se défaire en suppose une : quelqu'un doit payer un coût présent et certain contre un risque futur et diffus, sans en tirer d'avantage compétitif. **Ce n'est pas une difficulté technique, c'est une difficulté d'agrégation** — et elle est aussi ancienne que la notion de bien commun.

**L'invisibilité tant que cela fonctionne.** Une infrastructure qui tient ne produit aucun signal. **La qualité d'une dépendance ne se lit jamais dans le fonctionnement nominal**, ce qui est la raison pour laquelle la Partie I recommandait d'interroger explicitement les briques d'une capacité plutôt que ses performances.

**Et le fait que le stock physique d'un bien commun ne s'étend pas.** Le nombre d'orbites utiles et la largeur du spectre sont bornés par la physique. **Ce qui augmente n'est pas le stock, c'est le service qu'on en tire** : efficacité spectrale, réutilisation spatiale des fréquences, coordination d'usage. Cette marge est réelle et considérable — elle repousse la contrainte, elle ne la supprime pas, et elle se paie en complexité de coordination, c'est-à-dire en gouvernance.

---

## ④ Le rythme imposé

**Constitution : quelques années.** Le temps qu'une brique devienne le choix par défaut.

**Révélation : instantanée.** La dépendance devient visible au moment exact où elle défaille, et pas avant.

**Sortie : de quelques mois à plusieurs décennies**, selon ce qui porte la dépendance. Une brique purement logicielle peut se remplacer vite quand une alternative existe ; **dès qu'un parc matériel, un protocole déployé ou une certification sont en jeu, l'ordre de grandeur devient la décennie**, et c'est le cas des cinq exemples traités ici.

**La conséquence est le résultat central du chapitre.** La fenêtre où l'on pourrait décider quelque chose est ouverte **avant** l'incident, quand rien ne l'indique ; elle se referme quand l'incident survient, puisqu'il ne reste alors que la durée de sortie. **L'attention et la décision sont systématiquement en décalage de phase**, et c'est structurel : ce n'est pas un défaut d'organisation, c'est la forme du problème.

---

## ⑤ Les positions en présence

**Le marché produira les alternatives.** Argument : dès qu'une dépendance devient une rente ou un risque assurable, un fournisseur concurrent apparaît. **Hypothèse sous-jacente** : le coût de commutation reste franchissable et l'alternative peut atteindre l'échelle où elle devient crédible — ce qui est plausible pour un service logiciel, douteux pour une constellation ou une référence de temps.

**Il faut une obligation publique de résilience.** Argument : le coût est présent, le bénéfice est diffus, donc seul un mandat le fait porter. **Hypothèses sous-jacentes**, au nombre de deux : qu'un régulateur puisse imposer un coût certain contre un risque incertain, et que le périmètre réglementaire coïncide avec celui de la dépendance — or il ne coïncide pas, puisqu'elle est transnationale par construction.

**La redondance technique suffit.** Argument : doubler les sources traite le problème. **Hypothèse sous-jacente** : les redondances sont indépendantes. **Elle est fausse dès qu'elles partagent une brique commune** — deux constellations distinctes peuvent dépendre de la même référence de temps, deux fournisseurs distincts d'un même modèle sous-jacent. La redondance apparente est le mode de défaillance le plus fréquent de ce chapitre.

**Ce que ce volume constate.** Les cinq cas ont été identifiés séparément, dans des couches différentes, et présentent **le même mécanisme** : agrégation de décisions individuellement rationnelles, absence d'autorité, invisibilité jusqu'à la défaillance, asymétrie entre constitution et sortie. C'est un constat, pas une position.

**Et il faut signaler le déséquilibre de preuve.** L'existence des dépendances est documentée et vérifiable cas par cas. **L'efficacité comparée des remèdes ne l'est pas** : aucun des trois n'a été mis à l'épreuve à l'échelle où il prétend agir.

---

## ⑥ Ce qu'il faudrait observer

**L'exercice réel d'un repli**, et non son existence sur le papier : une opération conduite sans référence satellitaire, une bascule vers un fournisseur alternatif effectivement réalisée. **Un plan de continuité non exercé n'est pas une information.**

**La part d'un parc effectivement migrée** vers des primitives cryptographiques de remplacement, par secteur. C'est la grandeur la plus directement mesurable du chapitre, et elle mesure une vitesse de sortie.

**Le nombre d'acteurs capables de fournir une brique**, à distinguer soigneusement du nombre d'offres commerciales : plusieurs offres peuvent reposer sur un fournisseur unique.

**L'apparition d'un mandat de gestion contraignant** sur un bien commun — orbites, spectre, source de temps. **Ce serait l'événement le plus significatif de ce chapitre**, et il n'est pas survenu.

**Le prix de l'assurance** couvrant l'indisponibilité d'une brique commune, quand il existe : un assureur estime ce qu'un discours de résilience ne dit pas.

**Signaux non informatifs.** Les annonces de souveraineté. Le nombre de fournisseurs listés dans un catalogue. Les déclarations d'indépendance technologique non assorties d'un calendrier de migration.

---
