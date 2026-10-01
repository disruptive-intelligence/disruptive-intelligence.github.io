---
title: Chapitre 11 — Marchés du dark web
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

histoire, fonctionnement, évolution

Les **marchés** (marketplaces) sont les plateformes d'e-commerce clandestin — la couche la plus visible et la plus médiatisée du dark web. Après Silk Road, plusieurs dizaines ont existé et disparu.

## 11.1 Anatomie d'un marché

Un marché dark web typique présente une interface familière. Comparable à Amazon ou eBay dans son ergonomie, avec des différences structurantes.

**Catégories de produits** :

- Drogues (cannabis, cocaïne, MDMA, amphétamines, opioïdes, psychédéliques) — catégorie historique dominante.
- Digital goods : comptes, credentials, accès, exploits, malware, guides.
- Documents : faux permis, faux passeports, modèles de factures, templates.
- Services : hacking sur commande, DDoS, escrow, physical services (rares).
- Armes : présent sur certains marchés mais marginalement, majoritairement scam.
- Fraude : carding tools, dumps, fullz.

**Fonctionnalités** : listings avec photos, descriptions, stock, prix (multiple devises crypto) ; panier et checkout ; **escrow** ; dispute resolution ; ratings et reviews ; messagerie interne ; 2FA et PGP obligatoires sur les marchés sérieux.

**Accès** : adresse .onion communiquée via listes communautaires, forums affiliés. Inscription : email jetable, pseudonyme, création de compte. Authentification : login + password + 2FA PIN + parfois PGP challenge.

## 11.2 Les grands marchés historiques et actuels

**Silk Road (2011-2013)** — pionnier, traité Ch.2.

**Silk Road 2.0 (2013-2014)** — successeur immédiat, saisi lors d'operation Onymous.

**Evolution Market (2014-2015)** — grand marché de son époque, exit scam retentissant en mars 2015 (~12 M USD).

**Agora (2013-2015)** — longévité notable, fermeture volontaire par ses opérateurs.

**AlphaBay (2014-2017)** — plus grand marché de l'histoire au moment de sa saisie (Ch.2).

**Hansa (2013-2017)** — « capté » par la police néerlandaise pendant 30 jours après la saisie d'AlphaBay.

**Dream Market (2013-2019)** — longue durée de vie, fermeture volontaire des opérateurs avril 2019.

**Wall Street Market (2016-2019)** — exit scam suivi d'arrestations allemandes.

**Empire Market (2018-2020)** — exit scam août 2020, ~30 M USD.

**Hydra (2015-2022)** — dominant russophone, traité Ch.2.

**Marchés actuels 2025-2026** (listes susceptibles d'évolution rapide) :

- **Abacus Market** : généraliste anglophone, actif depuis ~2022.
- **TorZon** : anglophone, en croissance 2023-2024.
- **MGM Grand / MGM Gold Market** : anglophone.
- **BlackSprut, OMG!OMG!, Mega, Kraken Market** : marchés russophones post-Hydra.
- **DarkDock, Vice City, Incognito** : statuts variables.

## 11.3 Le modèle économique d'un marché

**Revenue** : commissions 2-5% sur transactions (parfois jusqu'à 10%) prélevées via l'escrow ; fees vendor (inscription 100-1 000 USD, fees mensuels, promotion payante) ; fees acheteur (dépôt minimum) ; advertising.

**Coûts** : hosting bulletproof (5 000-30 000 USD/mois selon scale), développement, modération, sécurité (audits, DDoS), marketing.

Un grand marché génère plusieurs millions à plusieurs dizaines de millions USD par an. Hydra à son apogée : estimations 5-10% du volume crypto transactionnel mondial lié aux darknet markets.

## 11.4 La dynamique de l'exit scam

**Phase 1 — Build-up**. Les opérateurs construisent la confiance et font croître le volume d'escrow. Plus le volume est haut, plus la « prime de départ » est attrayante.

**Phase 2 — Signals**. Dégradation qualité — support moins réactif, disputes mal résolues, retards de déblocage. Certains vendeurs s'alarment sur les forums.

**Phase 3 — Retention**. Ralentissement des withdrawals — délais accrus, vérifications supplémentaires. Les fonds s'accumulent.

**Phase 4 — Disappearance**. Le marché devient inaccessible. Les opérateurs ont transféré les fonds et disparu.

**Phase 5 — Succession**. Parfois, des « rescue » se proposent de racheter la base. Rarement efficace — la confiance est cassée.

Exit scams majeurs : Evolution (~12 M USD, 2015), Empire (~30 M USD, 2020). La probabilité d'exit scam augmente quand le marché grandit, que les FdO pressent, que les opérateurs vieillissent. Règle pour acheteurs avertis : **ne pas laisser plus que nécessaire sur le marché**.

## 11.5 Les marchés spécialisés 2024-2026

L'époque des grands marchés généralistes AlphaBay décline au profit de marchés **spécialisés**.

- **Marchés de logs** : Russian Market leader. Spécialisation totale sur les stealer logs (Ch.15). Croissance massive depuis 2023.
- **Marchés de fraude** : cartes bancaires, comptes bancaires, accès PayPal/Venmo, fullz. BriansClub, WWH Club, Joker's Stash historique (saisi 2021).
- **Marchés de SaaS criminel** : RaaS, PhaaS, DDoS-aaS. Interface orientée services avec abonnements.
- **Marchés d'accès** : IAB sur leurs propres plateformes ou via forums. Annonces et négociations plutôt que catalogue.
- **Marchés de malware** : vente de malware spécifique, crypters, loaders. Souvent intégrés aux forums.

Cette spécialisation reflète la **professionnalisation** de la cybercriminalité : chaque segment a ses acteurs, ses codes, ses mécanismes de confiance.

## 11.6 Investigation sur un marché : ce qu'on peut observer

Pour un analyste CTI, un marché offre plusieurs types d'observations utiles.

**Pricing intelligence** : prix observés donnent une grille pour évaluer les signals (Ch.14 sur les données, Ch.15 pour les stealer logs).

**Vendor profiling** : histoire d'un vendeur (ancienneté, transactions, ratings, spécialisations). Profils anciens avec beaucoup de transactions = acteurs établis, annonces plus susceptibles d'être authentiques.

**Victim signaling** : annonces mentionnant des cibles nommées (entreprises, secteurs, géographies) donnent des signaux pour le monitoring défensif.

**Trends** : évolution du volume de certains types de produits (hausse des ventes credentials cloud AWS depuis 2022 = signal industry-wide).

**Indicators** : adresses crypto observées comme paiements, pseudonymes vendeurs/acheteurs, infrastructures mentionnées.

**Limites** : tout ce qui est sur un marché n'est pas authentique. Scams, recyclages, agit-prop — l'analyste doit rester critique (Ch.32).

---
