---
title: ◆◆◆ Preuves à divulgation nulle
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Prouver qu'une affirmation est vraie sans révéler pourquoi elle l'est.

**Pourquoi cette entrée est majeure.** Parce que **c'est une capacité contre-intuitive dont les usages dépassent largement le domaine où le terme est né** — et parce qu'elle est très mal comprise.

**Le principe, en une image.** Prouver qu'on connaît un secret sans le dire. Prouver qu'on a plus de dix-huit ans sans révéler sa date de naissance. Prouver qu'un calcul a été effectué correctement sans refaire le calcul ni montrer les données d'entrée.

**Comment ça fonctionne, au niveau utile.** Le prouveur transforme son affirmation et son secret en un objet mathématique — la preuve — que le vérifieur peut contrôler. La vérification est **beaucoup plus rapide que le calcul d'origine**, et elle ne révèle rien d'autre que la validité de l'affirmation.

**Deux propriétés distinctes**, souvent confondues sous le même terme. La **divulgation nulle** — la preuve ne révèle rien du secret. La **succinctité** — la preuve est courte et rapide à vérifier, même si le calcul prouvé était long. **La seconde est souvent la plus utile**, et elle est indépendante de la première : on peut vouloir une preuve courte sans avoir de secret à protéger.

**Où vous rencontrerez le terme.** Systèmes d'identité · conformité réglementaire · registres distribués · vérification de calcul délégué · authentification préservant la vie privée.

**Ce que ça permet.** Déléguer un calcul à un tiers non fiable et vérifier son résultat à faible coût · prouver une conformité sans divulguer les données sous-jacentes · établir une propriété d'un ensemble de données sans le publier.

**Ce qui bloque.** **Le coût de génération**, très supérieur au calcul prouvé — c'est le compromis central : on rend la vérification très bon marché en rendant la production très chère. **La complexité de conception** : traduire un problème en une forme prouvable est un travail d'expert. Et **l'hypothèse de sécurité**, ces constructions reposant sur des hypothèses mathématiques dont certaines ne résistent pas à un attaquant quantique — ce qui relie cette entrée à la première du chapitre.

**Ce que cela implique.** L'usage le plus structurant n'est pas la confidentialité mais **la vérifiabilité du calcul délégué**. Dans un monde où l'on confie des traitements à des tiers, pouvoir vérifier un résultat sans le recalculer change l'économie de la confiance.

**À ne pas confondre avec.** Le **chiffrement**, qui rend illisible ; ici, on ne cache pas une donnée, on prouve une propriété. Et avec les **registres distribués**, où ces techniques sont employées mais dont elles sont indépendantes.

> ⏱ **État au 23/08/2026** — 🔬 émergent en diffusion. Déploiements établis dans certains écosystèmes ; extension aux usages d'identité et de conformité en cours ; coût de génération en baisse continue.
> 🔄 **À revoir si** la génération de preuve devient assez peu coûteuse pour être appliquée à des calculs de grande taille en production.

**Renvois** — Couche : vérifier · Courant : Trust Technologies (ch. 35).

---
