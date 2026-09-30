---
title: ◆◆ Vérification formelle
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Démontrer mathématiquement qu'un système satisfait une propriété, pour toutes les entrées possibles.

**Ce que ça permet.** Une garantie d'une nature différente de celle des essais : **les essais montrent l'absence de défaut sur les cas testés, la vérification formelle montre l'absence de défaut sur tous les cas** — dans les limites de ce qui a été modélisé.

**Ce qui bloque — et il faut être précis sur la portée.** **La taille.** La complexité de la vérification croît rapidement avec celle du système ; au-delà d'une certaine taille, elle devient impraticable. On vérifie donc des composants, pas des systèmes entiers.

**La modélisation.** On vérifie un modèle du système, pas le système. **Si le modèle omet un aspect, la preuve ne dit rien de cet aspect** — c'est la limite la plus importante et la moins comprise.

**Les systèmes apprenants.** Vérifier formellement un réseau de neurones est possible sur des propriétés simples et des tailles modestes, et reste hors de portée pour les modèles de grande taille. **C'est pourquoi l'architecture de sûreté ne cherche pas à vérifier le modèle mais son enveloppe** — dispositif simple, donc vérifiable.

**Ce que cela implique.** La vérification formelle est **un outil de composant, pas de système** — et c'est précisément ce qui la rend utile dans l'architecture de la première entrée : elle prouve la couche de contrainte, qui est simple par conception.

**À ne pas confondre avec.** Les **essais exhaustifs**, qui ne le sont jamais. Et l'**analyse statique**, qui détecte des classes d'erreurs sans démontrer une propriété.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour des composants critiques dans l'aéronautique, le ferroviaire et le matériel ; 🔬 émergent pour les composants d'autonomie.
> 🔄 **À revoir si** la vérification de propriétés utiles devient praticable sur des modèles de taille industrielle.

**Renvois** — Couche : vérifier.

---
