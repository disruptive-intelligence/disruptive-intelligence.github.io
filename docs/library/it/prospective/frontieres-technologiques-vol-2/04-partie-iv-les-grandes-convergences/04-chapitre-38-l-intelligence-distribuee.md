---
title: Chapitre 38 — L'intelligence distribuée
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie IV — Les grandes convergences
  - index.md
---

## ① La capacité recherchée

**Formulation courante, et son défaut.** « Mettre de l'intelligence partout » ne dit ni quelle intelligence, ni ce que « partout » coûte à exploiter.

**Formulation retenue.**

> **Percevoir, décider et agir localement, en très grand nombre, sans dépendre d'une infrastructure distante pour chaque décision — et pendant une durée compatible avec le coût d'installation.**

**Ce que cette formulation ajoute.** La dernière clause. Un dispositif installé pour cinq ans et qu'il faut visiter deux fois par an ne remplit pas la promesse, quelle que soit sa capacité de traitement. **La durée sans intervention est la variable qui décide, et elle est absente de tous les récits du domaine.**

**Le récit associé.** *Edge AI*, *IoT*, *ambient computing*. Les fiches des chapitres 32 et 34 les situent ; ce dossier analyse ce qu'ils supposent.

---

## ② Les briques nécessaires

| Couche | Ce que la convergence en attend | Entrées d'atlas |
|---|---|---|
| **Percevoir** | coût unitaire, étalonnage à grande échelle | MEMS avancés (7) · perception distribuée (7) · fibre-capteur (7) · caméras événementielles (6) |
| **Calculer** | traitement dans une enveloppe énergétique minuscule | accélérateurs (8) · calcul faible précision (8) · compute-in-memory (8) · neuromorphique (9) |
| **Apprendre** | ce qui tient dans la mémoire disponible | modèles compacts (11) · multimodalité (11) |
| **Relier** | placement du calcul, couverture, coût par message | edge/on-device/embarqué (25) · continuum (25) · réseaux non terrestres (24) |
| **Alimenter** | budget énergétique unitaire | récupération d'énergie (23) |
| **Vérifier** | confiance dans une donnée produite hors surveillance | identité machine (29) · attestation (28) · racine de confiance (28) |

**Seize entrées, six couches** — c'est la convergence la plus transversale des six.

---

## ③ Ce qui empêche encore

**Premier — l'exploitation d'un parc dispersé.** Le volume 1 l'a démontré par le calcul : un parc d'un million d'unités avec une intervention annuelle par unité représente plusieurs centaines de techniciens à temps plein. **Ni le capteur, ni le modèle, ni la liaison ne limitent — c'est l'exploitation.**

**Deuxième — la dérive silencieuse.** Un capteur qui dérive continue de produire des valeurs plausibles. À l'unité, on l'étalonne. À un million, **on ne sait pas lequel a dérivé**, et la qualité de la donnée agrégée se dégrade sans signal.

**Troisième — la mise à jour.** Un modèle déployé sur un parc se corrige au rythme du parc, avec des versions hétérogènes en service simultanément. Un dispositif alimenté par récupération d'énergie peut n'avoir aucune fenêtre de communication suffisante pour recevoir une mise à jour.

**Quatrième — la confiance dans la donnée.** Un dispositif physiquement accessible, non surveillé, peut être remplacé, déplacé ou manipulé. **Et une signature n'atteste pas la véracité** : un capteur compromis produit une donnée authentique et fausse.

---

## ④ Le maillon le plus en retard

**L'exploitation du parc — étalonnage, maintenance, mise à jour.**

**L'argument.** Les trois autres verrous se traitent par la conception : on peut concevoir un dispositif frugal, un modèle compact, une liaison économe. **L'exploitation, elle, croît linéairement avec le nombre d'unités** et ne bénéficie d'aucune économie d'échelle — c'est même l'inverse, puisque la dispersion géographique augmente le coût de chaque intervention.

**Le calcul qui le montre.** Si le coût d'exploitation annuel par unité ne descend pas sous une fraction du coût d'acquisition, un déploiement massif est économiquement impossible quelle que soit la baisse du prix du capteur. **La grandeur qui décide n'est pas le prix du dispositif mais le coût annuel de sa possession** — et elle est presque jamais publiée.

**Position par rapport à la thèse du volume.** Les couches éponymes sont *calculer* et *relier* ; le maillon en retard est **institutionnel et opérationnel**, hors de toute couche technique. **La thèse est vérifiée.**

---

## ⑤ Quel mur domine

**La défaillance silencieuse**, très nettement, et sous sa forme la plus difficile : **à grande échelle, on ne sait pas quelles unités ont dérivé**. Le mur n'est pas qu'un capteur dérive — c'est qu'on ne peut pas le savoir.

**Le rendement de production**, au sens de la proportion d'unités effectivement fonctionnelles à un instant donné. Un parc à 85 % de disponibilité produit une donnée dont la représentativité spatiale est inconnue.

---

## ⑥ Ce qui est en train de changer

**L'exécution locale de modèles est devenue possible sur des appareils ordinaires**, ce qui supprime le coût par appel et la dépendance à une liaison.

**Les architectures événementielles** — capteurs et traitement ne consommant que lorsqu'il se passe quelque chose — abaissent le budget énergétique d'un ordre de grandeur sur des données éparses.

**L'attestation au niveau du dispositif** se généralise, ce qui rend traitable la question de l'origine de la donnée.

**La couverture** s'étend par les réseaux non terrestres, ce qui ouvre les zones sans infrastructure.

**Ce qui n'a pas changé.** Le coût d'une intervention humaine sur site. Le vieillissement des capteurs. Et le fait qu'une dérive ne se signale pas.

---

## ⑦ Ce que la convergence débloquerait

**Une mesure continue là où l'on mesurait ponctuellement.** Infrastructures, agriculture, environnement, industrie, santé : le passage d'un relevé périodique à une observation permanente change la nature de ce qu'on peut détecter — les dérives lentes, les événements brefs, les corrélations spatiales.

**Une décision locale sans aller-retour.** Ce qui compte moins pour la latence que pour l'autonomie : un système qui décide seul continue de fonctionner quand la liaison tombe.

**Ce qui resterait hors de portée.** Les usages exigeant une donnée opposable — mesure réglementaire, preuve — tant que l'authenticité à la source n'est pas démontrable.

---

## ⑧ Le verrou suivant

**La confiance dans la mesure.**

Si l'exploitation s'automatise — auto-diagnostic, étalonnage croisé entre unités voisines, détection de dérive par comparaison —, le goulet devient : **que vaut une mesure produite par un dispositif non surveillé, physiquement accessible, dont la signature atteste l'origine mais jamais la véracité ?**

C'est la question du chapitre 29, et elle conditionne tous les usages où la donnée doit être opposable.

**Et un verrou de second ordre.** Un parc massif de capteurs devient une infrastructure dont d'autres systèmes dépendent sans l'avoir choisie — **exactement le mécanisme du chapitre 45**.

---

## ⑨ La chronologie conditionnelle

```text
① si le coût unitaire et le budget énergétique permettent un déploiement massif
        → alors l'exploitation du parc devient limitante

② si l'exploitation s'automatise — auto-diagnostic, étalonnage croisé,
   mise à jour sans intervention
        → alors la confiance dans la mesure devient limitante

③ si l'authenticité de la mesure à la source reste indémontrable
        → les usages restent confinés à ceux qui tolèrent
          une donnée non opposable

④ si l'exploitation ne s'automatise pas
        → les déploiements plafonnent à l'échelle où
          la maintenance manuelle reste supportable
```


---

## ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** Le **coût complet d'exploitation par unité et par an**, publié par un exploitant — c'est le signal décisif. L'apparition de mécanismes d'**étalonnage croisé automatique** entre unités voisines. La normalisation d'une **attestation au niveau capteur**. Et la **durée moyenne sans intervention** observée sur un parc réel.

**Signaux non informatifs.** Le nombre d'unités déployées. Le prix unitaire du capteur. La consommation annoncée en veille. Les annonces de partenariat.

**Ce qui réfuterait l'analyse.** Les déploiements dépassent durablement le million d'unités avec un coût d'exploitation par unité en baisse — ce qui indiquerait que l'exploitation n'était pas le verrou. Ou bien les projets sont abandonnés au premier renouvellement de parc, ce qui confirmerait l'analyse par l'échec plutôt que par le blocage.

---
