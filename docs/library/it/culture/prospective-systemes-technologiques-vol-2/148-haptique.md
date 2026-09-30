---
title: ◆◆ Haptique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — interagir

**En une phrase.** Restituer à l'utilisateur des sensations de contact, de texture ou de force.

**Pourquoi c'est déterminant.** Parce que **c'est le verrou de la téléopération**, et parce que la perception du contact est ce qui manque le plus dans toute manipulation à distance — le chapitre 15 l'a établi.

**Comment ça fonctionne — deux familles très différentes.** Le **retour tactile** stimule la peau — vibration, pression locale, texture — et il est relativement accessible. Le **retour de force** s'oppose au mouvement de l'utilisateur pour simuler la rigidité d'un objet ; il exige des actionneurs capables de produire des efforts significatifs, avec toutes les contraintes de la couche *agir*.

**Ce qui bloque.** **La bande passante de la sensation.** La peau et les récepteurs profonds perçoivent des variations très rapides ; restituer une sensation crédible exige une boucle de contrôle à haute fréquence, faute de quoi le contact paraît mou ou instable.

**La stabilité.** Un système de retour de force est une boucle fermée avec un humain dedans : mal réglée, elle oscille — et le chapitre 16 du volume 1 a montré pourquoi le délai en est l'ennemi.

**Et l'encombrement** : produire une force nécessite des actionneurs, donc de la masse portée sur la main ou le bras.

**Ce que cela implique.** L'haptique progresse nettement en **tactile** et reste difficile en **force**. C'est pourquoi les usages qui se déploient sont ceux où l'information de contact suffit — alerter, confirmer, texturer — et non ceux qui exigent de sentir une résistance.

**À ne pas confondre avec.** La **vibration** simple, qui est une forme de retour tactile mais ne restitue ni texture ni force.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour le tactile, 🔬 émergent pour le retour de force hors applications spécialisées.
> 🔄 **À revoir si** un dispositif de retour de force porté atteint une fidélité utile dans un volume et une masse compatibles avec un usage prolongé.

**Renvois** — Couche : interagir · Voir aussi : téléopération (ch. 15), peau électronique (ch. 7).

---


## ◆◆ Lunettes connectées

**Niveau** — plateforme · **Couche** — interagir

**En une phrase.** Des lunettes de forme ordinaire intégrant capteurs, audio et parfois un affichage minimal.

**Pourquoi cette entrée est distincte de la première.** Parce que ces dispositifs font **le pari inverse** : renoncer à l'affichage riche pour obtenir un objet portable toute la journée. Ce n'est pas une version simplifiée d'un casque, c'est une autre proposition.

**Ce que ça permet.** Capter — photo, vidéo, son — sans sortir un appareil · restituer par audio ou par un affichage sommaire · disposer d'un assistant contextuel voyant ce que l'utilisateur voit.

**Ce qui bloque.** **L'autonomie et la chaleur**, dans un volume qui n'autorise ni batterie significative ni dissipation. **L'acceptabilité sociale** d'un dispositif de capture porté en permanence — obstacle qui a fait échouer une vague antérieure et n'est pas résolu. Et **l'utilité marginale** face à un téléphone déjà présent.

**Ce que cela implique.** Le déplacement récent le plus significatif n'est pas l'affichage mais **l'assistant contextuel** : un dispositif qui voit et entend ce que l'utilisateur perçoit change la nature de l'interaction, indépendamment de sa capacité d'affichage. **C'est là que se joue la trajectoire, pas dans l'optique.**

**À ne pas confondre avec.** Les casques de réalité mixte, dont l'usage est sessionnel et non continu.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Produits sans affichage disponibles avec une adoption réelle ; produits avec affichage encore limités.
> 🔄 **À revoir si** un dispositif porté en continu atteint une base d'utilisateurs quotidiens significative sur plusieurs années.

**Renvois** — Couche : interagir.

---


## ◆◆ Informatique portée

**Niveau** — plateforme · **Couche** — interagir, percevoir

**En une phrase.** Les dispositifs portés au poignet, au doigt, à l'oreille ou sur le corps, qui mesurent en continu et notifient.

**Pourquoi cette entrée compte.** Parce que **c'est la seule famille de cette couche dont la diffusion est massive et établie** — et parce qu'elle démontre ce qui fonctionne : un dispositif qui ne demande aucune attention et rend un service continu.

**Ce que ça permet.** Mesurer des paramètres physiologiques en continu · détecter un événement — chute, arythmie, apnée · notifier discrètement · servir de moyen d'identification ou de paiement.

**Ce qui bloque.** **La qualité de la mesure.** Un capteur porté au poignet mesure dans des conditions défavorables — mouvement, contact variable, pigmentation, transpiration. **La dérive de mesure y est structurelle**, et c'est la limite de la couche *percevoir* appliquée au corps.

**Le statut de la donnée** : entre le bien-être et le dispositif médical, la frontière réglementaire est nette et les exigences sans commune mesure. Un même capteur peut relever de l'un ou de l'autre selon ce qu'on en revendique.

**Et l'exploitation** : mesurer en continu produit un volume de données dont l'interprétation clinique n'est pas établie pour la plupart des paramètres.

**Ce que cela implique.** Le succès de cette famille tient à ce que **le dispositif ne demande rien à l'utilisateur** — c'est l'inverse exact de ce que demandent les casques. **C'est probablement l'enseignement le plus utile de la couche pour évaluer toute interface future.**

> ⏱ **État au 23/08/2026** — 🏭 déployé, diffusion de masse. Extension progressive des paramètres mesurés et des reconnaissances réglementaires.
> 🔄 **À revoir si** un paramètre mesuré en continu par un dispositif grand public devient un critère de décision clinique reconnu.

**Renvois** — Couche : interagir, percevoir.

---


## ◆◆ Interfaces neuromusculaires

**Niveau** — capacité · **Couche** — interagir

**En une phrase.** Capter les signaux électriques envoyés par le système nerveux aux muscles, avant même que le mouvement soit visible.

**Pourquoi cette entrée est importante.** Parce que **c'est la voie non invasive la plus crédible** pour capter une intention motrice — et parce qu'elle contourne le verrou de la couche par un chemin inattendu.

**Comment ça fonctionne.** Des électrodes placées sur la peau — au poignet, sur l'avant-bras — détectent l'activité électrique musculaire. Comme cette activité précède le mouvement, on peut détecter une intention de geste **même minime**, voire un geste seulement esquissé.

**Ce que ça permet.** Une commande discrète, sans mouvement visible ni effort · une interaction utilisable quand les mains sont occupées ou hors de vue · **une voie d'usage pour des personnes ayant perdu la mobilité mais conservé l'activité nerveuse**.

**Ce qui bloque.** **La variabilité entre individus et entre sessions** : la position des électrodes, l'anatomie et l'état de la peau modifient le signal, ce qui impose un étalonnage. **Le nombre de commandes distinctes**, limité. Et **la fatigue**, l'activation répétée de petits muscles étant inconfortable sur la durée.

**Ce que cela implique.** C'est une modalité **complémentaire**, adaptée à un petit nombre de commandes discrètes et discrètes — et non un remplacement d'un dispositif de pointage.

**À ne pas confondre avec.** Les **interfaces cerveau-machine**, qui captent l'activité cérébrale. Ici, on capte le signal **en aval du cerveau**, sur le trajet nerveux vers le muscle — ce qui est bien plus accessible et bien moins ambitieux.

> ⏱ **État au 23/08/2026** — 🔬 émergent, avec des premiers produits portés au poignet.
> 🔄 **À revoir si** une interface de ce type devient une modalité d'entrée par défaut sur un dispositif grand public.

**Renvois** — Couche : interagir.

---
