---
title: ◆◆ Attestation
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Produire une preuve vérifiable de l'état d'un système — quel matériel, quel logiciel, dans quelle configuration.

**Comment ça fonctionne.** Le système mesure son propre état — empreintes des composants logiciels chargés — et fait signer ces mesures par sa racine de confiance. Un tiers reçoit cette attestation, vérifie la signature et compare les mesures à des valeurs attendues.

**Deux formes.** L'attestation **locale**, où un composant vérifie un autre sur la même machine. L'attestation **à distance**, où un tiers vérifie une machine qu'il ne contrôle pas — c'est la forme qui change les architectures possibles.

**Ce que ça permet.** N'accorder un accès qu'à une machine dans un état vérifié · établir une confiance entre organisations sans audit préalable · détecter une modification non autorisée · conditionner la livraison d'une donnée à l'état du destinataire.

**Ce qui bloque.** **La gestion des valeurs attendues.** Vérifier une attestation suppose de savoir à quoi la comparer, pour toutes les versions légitimes de tous les composants — c'est un problème d'infrastructure considérable et sous-estimé. **La granularité** : une attestation dit ce qui a été chargé, pas ce que le système fait maintenant. Et **la révocation** : que faire quand une version attestée s'avère vulnérable.

**Ce que cela implique.** L'attestation atteste **un état, à un instant** — pas un comportement. Un système attesté conforme peut avoir été compromis après la mesure. C'est une garantie plus faible qu'il n'y paraît, et il faut le savoir.

**À ne pas confondre avec.** L'**authentification**, qui établit une identité ; l'attestation établit un état.

> ⏱ **État au 23/08/2026** — 🔬 émergent en généralisation. Mécanismes disponibles largement, infrastructure de vérification à l'échelle encore en construction.
> 🔄 **À revoir si** un service d'attestation interopérable entre fabricants et fournisseurs devient largement disponible.

**Renvois** — Couche : vérifier.

---


## ◆ Sûreté mémoire matérielle

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Des mécanismes matériels empêchant qu'un programme accède à une zone mémoire à laquelle il n'a pas droit.

**Pourquoi cette entrée existe.** Parce qu'une part importante et documentée des vulnérabilités logicielles graves relève de la gestion mémoire, et parce que traiter ce problème dans le matériel plutôt que dans le langage est une approche complémentaire aux langages sûrs.

**Ce qui bloque.** **Le coût en performance et en surface**, et surtout **la base installée** : ces mécanismes n'ont d'effet que si le logiciel est recompilé pour en tirer parti, ce qui suppose de reprendre des chaînes de compilation et des bibliothèques accumulées sur des décennies. **C'est un problème de dépendance de sentier au sens du volume 1**, non un problème technique.

**À ne pas confondre avec.** Les **langages à sûreté mémoire**, qui traitent le même problème à la source. Les deux approches sont complémentaires et progressent à des rythmes différents.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Mécanismes disponibles sur certaines architectures, adoption progressive.
> 🔄 **À revoir si** une exigence réglementaire impose la sûreté mémoire sur une classe de logiciels critiques.

**Renvois** — Couche : vérifier, calculer.

---
