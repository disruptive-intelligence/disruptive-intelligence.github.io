---
title: Chapitre 21 — Modèles économiques criminels
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IV — Économie clandestine
  - index.md
---

Synthèse des modèles économiques observés sur le dark web. Ce chapitre articule les rôles de la Partie III en modèles financiers cohérents.

## 21.1 Le modèle du vendeur individuel

**Acteur** : individu ou petite équipe (1-5 personnes).

**Produit** : spécialisé — drogues, fullz, credentials, documents contrefaits, petits services.

**Volumes** : dizaines à centaines de transactions par mois.

**Revenus annuels** : 50 k - 500 k USD typiquement, jusqu'à quelques millions pour les meilleurs.

**Risques** : identification via patterns (timing, OPSEC faible), erreurs opérationnelles (réutilisation pseudonyme, leaks personnels), dispute avec un gros acheteur qui dox.

**Exemples publics** : les vendeurs condamnés sont légion dans la presse judiciaire US, UK, DE. Exemples emblématiques : « Xanax King » condamné pour vente de faux Xanax sur AlphaBay (2017-2019) ; multiples dealers saisis lors d'operations police.

## 21.2 Le modèle de l'opérateur de plateforme

**Acteur** : équipe structurée (5-20 personnes).

**Produit** : infrastructure + arbitrage pour la communauté.

**Revenus** : commissions sur transactions + fees + services premium. Quelques millions à dizaines de millions USD/an pour les grandes plateformes.

**Risques** : saisie (multiple précédents), exit scam devenant la sortie rationnelle, conflits internes, DDoS concurrents.

**Exemples** : Ulbricht (Silk Road), Cazes (AlphaBay), Khoroshev (LockBit). Plus récemment : Baphomet (BreachForums multiple).

## 21.3 Le modèle RaaS

**Acteur** : équipe opérationnelle (10-50 personnes au core).

**Produit** : ransomware + infrastructure + service aux affiliés.

**Revenus** : 20-30% des paiements de rançon perçus par les affiliés. Dizaines de millions USD/an pour les groupes dominants.

**Exemples** : LockBit (estimations 500 M+ USD cumulés 2020-2024 avant Cronos), Conti (estimé ~180 M USD dans la leak 2022), ALPHV (~22 M USD Change Healthcare avant disparition), Black Basta (estimations 100 M+ USD).

**Risques** : saisies d'infrastructure, inculpations nominales (LockBitSupp), conflits d'affiliés, érosion post-disruption (LockBit qui peine à rebondir).

## 21.4 Le modèle de l'IAB

**Acteur** : individu ou petite équipe.

**Produit** : accès préqualifiés.

**Volumes** : 10-50 accès vendus par an.

**Revenus** : 500-50 000 USD par accès, selon qualité. Revenus annuels typiques 200 k - 2 M USD.

**Risques** : identification via l'accès lui-même (si l'acheteur est infiltré, les comms peuvent remonter à l'IAB), erreurs d'OPSEC dans la compromission initiale.

## 21.5 Le modèle du service provider (CaaS)

**Acteur** : opérateur d'un service — phishing kit, DDoS booter, malware-as-service, etc.

**Produit** : service récurrent avec abonnement.

**Revenus** : abonnements (50-1 000 USD/mois par utilisateur), jusqu'à dizaines de milliers d'utilisateurs pour les plus grands. Revenus annuels de 100 k à 10 M USD selon scale.

**Exemples** : Lumma Stealer (estimation sur plusieurs milliers d'abonnés × 250 USD/mois), LabHost avant démantèlement.

**Risques** : saisies (LabHost démantelé avril 2024), inculpations d'opérateurs.

## 21.6 Le modèle de blanchiment

**Acteur** : spécialistes financiers, souvent liés à l'écosystème crypto.

**Produit** : conversion crypto → fiat utilisable.

**Revenus** : commissions 10-30% du montant blanchi. Volumes considérables possible — plusieurs entités (Suex, Bitzlato, Garantex historiquement, Chipmixer) ont traité des milliards USD avant saisie/sanction.

**Risques** : sanctions OFAC (Suex, Bitzlato, Garantex sanctionnés), saisies (Chipmixer mars 2023, Samourai avril 2024), inculpations (Larry Harmon condamné pour Helix, Alexey Pertsev pour Tornado Cash).

## 21.7 Le modèle de l'hébergeur bulletproof

**Acteur** : opérateur d'infrastructure.

**Produit** : hosting résistant.

**Revenus** : abonnements de hosting premium. Centaines à milliers de clients, 500-10 000 USD/mois chacun.

**Risques** : saisies (Cyberbunker 2019, multiples avant), pression upstream (de-peering, blocages).

## 21.8 La convergence des modèles

Les modèles se chevauchent et convergent. Un acteur peut opérer comme IAB **et** affilié RaaS, comme développeur malware **et** opérateur d'un service CaaS, comme plateforme **et** commanditaire de ransomware. Cette **polymorphie économique** rend l'attribution fine complexe.

Le dark web économique 2025-2026 est mieux décrit comme un **réseau de spécialistes interconnectés** que comme un écosystème de rôles purs. Un même individu ou groupe peut jouer plusieurs rôles selon les opportunités, les contraintes, les rythmes.

## 21.9 Implications analytiques

Pour l'analyste, cette structure économique suggère plusieurs focus.

**Suivre les flux financiers** : chaque modèle produit des patterns crypto distinctifs. Les IAB reçoivent des paiements moyens, les RaaS reçoivent de très gros paiements épisodiques, les stealer operators reçoivent des flux constants de petits paiements. Chainalysis et équivalents peuvent identifier le modèle économique par profil transactionnel.

**Reconstruire les chaînes de valeur** : identifier le modèle économique d'un acteur aide à identifier ses partenaires amont/aval. Un IAB « accès manufacturing EU » est probablement lié à un groupe RaaS anglophone ; un opérateur de stealer logs alimente des IAB multiples.

**Anticiper les transformations** : les modèles évoluent. Un vendeur individuel peut devenir IAB en montant en gamme, un IAB peut fonder son propre groupe RaaS, un opérateur RaaS peut se retirer en blanchisseur. L'analyste suit ces trajectoires pour anticiper les tendances.

**Calibrer l'attribution** : chaque modèle a ses OPSEC typiques. Un vendeur individuel fait plus d'erreurs personnelles ; un opérateur RaaS opère avec plus de rigueur ; un service provider a des infrastructures plus visibles. L'attribution est plus facile sur certains profils que sur d'autres.

---
