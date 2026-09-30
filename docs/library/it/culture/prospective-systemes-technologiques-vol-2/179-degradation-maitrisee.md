---
title: ◆◆ Dégradation maîtrisée
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Continuer à fonctionner de manière réduite mais sûre lorsqu'une partie du système est défaillante ou hors de son domaine.

**Les quatre réponses possibles**, avec leur coût, établies au volume 1 et reprises ici comme référence.

**S'arrêter en sécurité.** Le moins coûteux, valable seulement si l'arrêt est effectivement sûr — ce qui n'est pas le cas d'un véhicule sur voie rapide ni d'un aéronef en vol.

**Continuer malgré la défaillance.** Exige une redondance sur toute la chaîne — perception, calcul, alimentation, actionneurs — et non sur le seul composant jugé fragile. **Le saut de coût est considérable** et régulièrement sous-estimé.

**Rendre la main.** Suppose un humain disponible, attentif et capable de reprendre en quelques secondes — ce que la couche *agir* a montré être une hypothèse fragile.

**Réduire les capacités.** Souvent la meilleure réponse et la plus difficile à concevoir : il faut avoir prévu à l'avance **ce qui peut être abandonné** et dans quel ordre.

**Ce qui bloque.** **La conception a priori.** Un mode dégradé ne s'improvise pas : il se conçoit, se spécifie et se teste — et tester un mode dégradé suppose de provoquer la défaillance, ce qui est coûteux et parfois impossible.

**Et l'information.** Un système qui se dégrade doit le signaler — à l'opérateur, à l'exploitant, aux autres systèmes qui en dépendent. **Une dégradation silencieuse est le pire des cas**, et c'est le fil rouge de tout ce volume.

**À ne pas confondre avec.** La **redondance**, qui est un moyen ; la dégradation maîtrisée est une propriété du comportement d'ensemble.

> ⏱ **État au 23/08/2026** — 🏭 déployé dans les secteurs à sûreté ancienne, 🔬 émergent ailleurs.
> 🔄 **À revoir si** la spécification d'un mode dégradé devient une exigence explicite pour les systèmes autonomes dans un secteur civil.

**Renvois** — Couche : vérifier · Voir aussi : autonomie supervisée (ch. 16), volume 1 chapitre 21.

---


## Clôture de la couche H — Vérifier


### Ce que les quinze entrées font apparaître

**Un. Toute vérification suppose un ancrage, et l'ancrage est toujours un déplacement de confiance.** Racine matérielle, enclave, attestation : dans les trois cas, on ne supprime pas la confiance, on la déplace vers un point jugé acceptable. **La question utile n'est jamais « ce système est-il sûr ? » mais « à qui ce système me demande-t-il de faire confiance ? »**

**Deux. Le déplacement conceptuel majeur de la couche est de renoncer à prouver le système pour prouver son enveloppe.** C'est ce que fait l'architecture de sûreté, et c'est ce qui rend déployable un système dont on ne peut démontrer le comportement. **La garantie ne porte pas sur ce que le système fera, mais sur ce qu'il ne pourra pas faire.**

**Trois. Le verrou est institutionnel dans cinq entrées sur quinze.** Architecture de sûreté, dossiers de sûreté, dégradation maîtrisée, sûreté mémoire, crypto-agilité : dans chaque cas, les dispositifs techniques existent et **leur reconnaissance par un référentiel est le facteur limitant**.

**Quatre. Une signature n'atteste jamais la véracité.** Cette limite apparaît dans trois entrées — provenance, attestation, identité machine — et elle avait été posée à la couche *percevoir*. **C'est probablement la formulation la plus utile de tout l'atlas pour un lecteur venant de la sécurité des systèmes d'information.**


### Ce que la couche livre aux convergences

| Dossier | Entrées mobilisées |
|---|---|
| **38 — Intelligence distribuée** | racine de confiance, attestation, identité machine |
| **39 — Autonomie mobile** | architecture de sûreté, détection de sortie de domaine, vérification formelle, dossiers de sûreté, dégradation maîtrisée |
| **41 — Biologie programmable** | *voir biosécurité, ch. 20* |

**Le dossier 39 mobilise cinq entrées de cette couche — et son maillon en retard est ici.** C'est la vérification la plus nette de la thèse du volume : la convergence la plus dépendante des couches *percevoir* et *agir* a son verrou dans *vérifier*.

---

---

---


### Couche I — Interagir

---
