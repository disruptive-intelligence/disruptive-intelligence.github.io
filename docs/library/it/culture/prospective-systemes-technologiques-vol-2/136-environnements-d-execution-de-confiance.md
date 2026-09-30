---
title: ◆◆◆ Environnements d'exécution de confiance
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier, calculer

**En une phrase.** Exécuter un traitement dans une zone isolée du processeur, protégée du reste du système — y compris du système d'exploitation et de l'administrateur de la machine.

**Pourquoi cette entrée est majeure.** Parce qu'elle rend possible quelque chose de contre-intuitif : **utiliser une machine sans faire confiance à celui qui l'exploite** — et parce que la confusion avec le chiffrement classique est documentée et coûteuse.

**Comment ça fonctionne.** Le processeur maintient une zone dont la mémoire est chiffrée et dont l'accès est refusé au reste du système. Le code qui s'y exécute peut ensuite **attester** de ce qu'il est : produire une preuve, signée par le matériel, indiquant quel code s'exécute dans quel environnement. Un tiers distant peut vérifier cette attestation avant de confier des données.

**Ce que cela change.** Sans cette capacité, confier un traitement à une infrastructure tierce suppose de faire confiance à son exploitant. Avec elle, **on peut vérifier ce qui s'exécute avant d'envoyer les données** — la confiance se déplace de l'organisation vers le fabricant du processeur.

**Où vous rencontrerez le terme.** Cloud · traitement de données réglementées · santé · finance · collaboration entre organisations concurrentes · protection de modèles d'apprentissage.

**Ce que ça permet.** Traiter des données sensibles sur une infrastructure qu'on ne contrôle pas · faire collaborer plusieurs parties sur des données qu'aucune ne veut divulguer · protéger un modèle ou un algorithme de celui qui l'exécute.

**Ce qui bloque.** **Les attaques par canaux auxiliaires.** L'isolation logique n'empêche pas d'observer des effets indirects — temps d'exécution, consommation, comportement des caches — dont on peut parfois déduire de l'information. Plusieurs vulnérabilités de cette nature ont été démontrées, et la protection reste une course.

**La performance**, avec un surcoût variable selon l'implémentation. **L'hétérogénéité** : les mécanismes diffèrent selon les fabricants, ce qui complique la portabilité. Et **la confiance déplacée, non supprimée** : on cesse de faire confiance à l'exploitant pour faire confiance au fabricant du processeur.

**À ne pas confondre avec — et c'est la confusion la plus fréquente du chapitre.** Le **chiffrement des données au repos ou en transit**, qui protège les données stockées ou transmises. Ces environnements protègent les données **pendant leur traitement**, c'est-à-dire au moment où elles doivent nécessairement être en clair pour être calculées. C'est un troisième état, longtemps sans protection.

**Termes voisins.** *TEE*, *enclave*, *confidential computing* désignent la même famille — le dernier terme insistant sur l'usage, les deux premiers sur le mécanisme.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Disponible chez les principaux fournisseurs de cloud et sur les processeurs récents ; adoption croissante pour les données réglementées.
> 🔄 **À revoir si** une catégorie d'attaque par canal auxiliaire remet en cause l'isolation d'une génération largement déployée.

**Renvois** — Couche : vérifier, calculer · Courant : Trust Technologies (ch. 35).

---
