---
title: Chapitre 17 — Division du travail et sous-traitance criminelle
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre l'économie cybercriminelle
  - index.md
---

## 17.1 Les rôles spécialisés

L'écosystème cybercriminel mature de 2025-2026 comprend au moins une douzaine de rôles spécialisés, chacun avec ses compétences, ses risques, et sa rémunération.

Les **développeurs** codent les outils (ransomware, infostealers, loaders, crypters, builders, panels C2). Salaire typique : 5 000-15 000 $/mois. Risque : modéré (pas d'interaction directe avec les victimes). Les **opérateurs** gèrent l'infrastructure et la marque RaaS. Revenus : commissions sur chaque rançon (20-30 %). Risque : élevé stratégiquement (ils sont la cible prioritaire des forces de l'ordre). Les **affiliés** mènent les attaques. Revenus : 70-80 % de la rançon. Risque : élevé opérationnellement. Les **IAB** fournissent les accès initiaux. Revenus : 500-50 000 $ par accès. Risque : modéré. Les **fournisseurs de crypters** rendent les malwares indétectables. Revenus : 20-500 $ par obfuscation ou abonnement mensuel. Les **hébergeurs bulletproof** fournissent l'infrastructure. Revenus : abonnements premium. Les **blanchisseurs** convertissent la crypto en argent propre. Commission : 10-30 % du montant blanchi. Les **mules** reçoivent et transfèrent l'argent via le système bancaire traditionnel. Les **négociateurs** communiquent avec les victimes pour maximiser le paiement de la rançon. Les **modérateurs de forums** assurent la gouvernance des places de marché. Les **arbitres** résolvent les litiges commerciaux.

## 17.2 L'acteur menaçant comme assemblage de services

Dans la plupart des attaques de 2025-2026, « l'attaquant » n'est pas une personne ou un groupe unique mais un assemblage temporaire de services spécialisés. L'attaque contre Énergis dans le fil rouge implique au moins cinq prestataires distincts : l'opérateur PhantomCrypt (qui fournit le ransomware et l'infrastructure), l'affilié kr0n0s_ops (qui mène l'opération), l'IAB ghost_access (qui a vendu l'accès initial), l'hébergeur bulletproof moldave (qui héberge le C2 et le blog), et le service de mixing (qui blanchira les fonds).

Ces cinq prestataires n'ont pas besoin de se connaître personnellement. Ils n'ont pas besoin d'être dans le même pays. Ils n'ont pas besoin de partager une motivation commune au-delà du profit. Leur coopération est purement transactionnelle : chacun fournit son service, reçoit sa rémunération, et passe à l'opération suivante.

## 17.3 Répartition de la valeur et du risque

Qui capte quelle part du profit, et qui supporte quel risque ? La répartition est inégale et révélatrice.

L'affilié prend le plus de risque opérationnel (il interagit directement avec le réseau de la victime, déploie le malware, laisse des traces forensiques) mais capte la plus grande part du revenu (70-80 %). L'opérateur RaaS prend le moins de risque opérationnel (il ne touche jamais au réseau de la victime) mais un risque stratégique considérable (si la plateforme est compromised, tout l'édifice s'effondre) ; il capte 20-30 % de toutes les rançons payées par tous les affiliés. L'IAB prend un risque modéré (il compromet les réseaux mais n'est pas directement lié à l'extorsion) pour un revenu plus faible mais régulier. Le blanchisseur prend un risque judiciaire élevé (le blanchiment d'argent est sévèrement puni dans la plupart des juridictions) pour une commission de 10-30 %.

## 17.4 Fil rouge — NEXUS : le graphe des rôles

> **🔍 NEXUS — Épisode 16**
>
> Le graphe Maltego est enrichi avec les rôles identifiés. Chaque nœud reçoit un attribut « rôle » : kr0n0s_ops = affilié, ghost_access = IAB, PhantomCrypt = opérateur RaaS, nego_phantom = négociateur externalisé, l'hébergeur moldave = facilitateur technique, le service de mixing = facilitateur financier, l'exchange Dubaï = point de cash-out. La chaîne de sous-traitance est visible.

---
