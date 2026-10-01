---
title: Chapitre 37 — Dark web, influence et opérations informationnelles
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VII — Cas d'usage, tendances et prospective
  - index.md
---

Le dark web sert aussi de plateforme pour des **opérations d'influence** — désinformation, campagnes coordonnées, manipulation de l'opinion. Ce chapitre cartographie ce volet moins visible mais d'importance croissante.

## 37.1 Les types d'opérations d'influence

**Hack-and-leak**. Technique classique : compromission de cibles politiques ou commerciales, puis publication sélective de données pour influencer narratif. Exemples emblématiques :

- **DNC hack (2016)** : GRU compromet le Democratic National Committee, publie via DCLeaks / Guccifer 2.0 / WikiLeaks. Impact élection présidentielle US.
- **Macron Leaks (2017)** : compromission campagne Macron, publication massive à 48h du second tour.
- **Multiple cas** ciblant partis politiques, campagnes, ONG, journalistes.

**Amplification coordonnée**. Réseaux de comptes (sock puppets, bots) qui amplifient certains messages sur réseaux sociaux. Le dark web sert de canal de coordination, de marché d'achat de comptes, d'outils.

**Fabrication de contenus**. Articles fabriqués, deepfakes, fake leaks. Le dark web héberge parfois la production et la distribution initiale.

**Doxing coordonné**. Publication d'informations personnelles de cibles (journalistes, politiques, activistes) pour les harceler, intimider, faire taire. Forums dédiés au doxing existent.

**Opérations « false flag ».** Attribution trompeuse d'une opération à un tiers pour le discréditer ou créer tensions.

## 37.2 Les acteurs

**Services de renseignement étatiques**. Les opérations d'influence étatiques ont une dimension cyber importante. Russie (GRU, IRA/St. Petersburg troll farm — Prigojine historique), Chine (réseaux amplifiés), Iran, autres.

**Groupes hacktivistes**. Idéologiques, opérations revendiquées. Ch.38.

**Prestataires commerciaux d'influence**. Entreprises vendant des services d'influence (parfois légitimes, souvent gris). Plusieurs entreprises ont été exposées par journalistes (Team Jorge en 2023, Cambridge Analytica avant 2018).

**Opérateurs individuels**. Anonymous, Ghost Security, individus opérant selon leurs convictions.

**Opérations hybrides** : coordination multi-acteurs. Un État finance, un prestataire opérationnalise, des proxies exécutent, des sous-traitants amplifient.

## 37.3 Les canaux

**Telegram**. Plateforme centrale pour les opérations d'influence russophones depuis 2022. Canaux pro-russes avec millions d'abonnés cumulés, coordination de narratifs, diffusion de contenus fabriqués. Arrestation Durov août 2024 a modifié la donne — modération durcie, partiellement contournée par migration.

**Forums dark web**. Coordination et mise en relation entre acteurs. Moins de diffusion publique (pas accessible à grand public) mais plus de discussion opérationnelle.

**Canaux dédiés**. KillNet (Telegram + sites annexes), NoName057(16) (canal DDoS revendiqué pro-russe), groupes Anonymous, IT Army of Ukraine.

**Réseaux sociaux mainstream**. La diffusion finale passe par X, Facebook, Instagram, TikTok, YouTube. Les plateformes font des efforts de modération mais restent débordées.

**Médias alternatifs et faux médias**. Sites qui imitent apparence de vrais médias (« Info-France »), sans journalisme réel, diffusant contenus alignés avec narratifs spécifiques. Parfois reliés à opérations étatiques (plusieurs démasquages documentés par EU DisinfoLab).

## 37.4 La désinformation russe et l'opération Doppelganger

**Opération Doppelganger** (documentée par EU DisinfoLab, Meta, Microsoft depuis 2022) : réseau russe qui crée de fausses versions de médias occidentaux (faux Le Monde, Der Spiegel, Bild, The Guardian, Washington Post, NYT) pour diffuser narratifs pro-russes avec apparence crédible.

**Modus operandi** :

- Création de **clones** de sites de grands médias, avec URL similaires (un caractère différent).
- Publication d'articles fabriqués sur ces clones, avec design identique aux vrais.
- Amplification sur réseaux sociaux (bots, sock puppets, acteurs coordonnés).
- Liens partagés depuis comptes Telegram, Facebook, X — le lecteur voit « Der Spiegel » et ne vérifie pas l'URL exacte.

**Impact** : plusieurs vagues documentées. Ciblage : opinion publique allemande, française, américaine, sur narratifs liés à la guerre en Ukraine, aux sanctions, aux dirigeants démocratiques.

**Attribution** : liens avec entités russes identifiés (Structura et Social Design Agency — deux entreprises russes sanctionnées par UE en 2023, et par US Treasury en 2024).

**Défense** : sensibilisation du public, détection automatique par plateformes, sanctions ciblées sur acteurs identifiés.

## 37.5 L'IRA et les opérations de troll

**Internet Research Agency (IRA)**, basée à St. Petersburg, historiquement financée par Yevgeny Prigojine (mort accidentellement en août 2023). Opérations de troll farm documentées sur plusieurs continents.

**Opérations documentées** :

- **Élections US 2016** (inculpations DOJ Mueller février 2018).
- **Influence en Afrique francophone** (Mali, RCA, autres — stratégie russe d'influence post-retraits français).
- **Divers conflits internes dans pays occidentaux** (race, immigration, divisions sociales).

**Modus operandi** :

- **Personas soigneusement construits** — pas simples bots, mais comptes faux avec identité fabriquée, activité cohérente sur années.
- **Coordination sur plateformes multiples** — X, Facebook, Instagram, Reddit.
- **Amplification de vrais contenus divisifs** autant que création de faux.
- **Mixage avec influenceurs locaux** parfois conscients, parfois manipulés.

**Post-Prigojine** : réorganisations internes russes, continuation avec autres structures. Les opérations persistent.

## 37.6 Les opérations d'influence côté cybercrime

Les opérations d'influence ne sont pas que étatiques — le dark web cybercriminel produit aussi :

**Manipulation de réputation**. Groupes qui dénigrent concurrents, promeuvent leurs services, manipulent ratings sur forums.

**Doxing de rivaux**. Publication d'identité civile d'un opérateur concurrent par un autre. Classique dans guerres inter-groupes.

**Leaks stratégiques**. Fuite sélective de données pour embarasser un acteur (victime, concurrent, ex-partenaire).

**Faux témoignages**. Comptes qui prétendent être victimes satisfaites ou insatisfaites pour influencer marchés.

## 37.7 Les deepfakes

**Deepfakes vidéo** et **deepfakes audio** émergent comme vecteurs :

- **Deepfakes de dirigeants** pour simuler déclarations, provoquer crises.
- **Voix truquées** pour fraude (cas documentés de CFO qui reçoivent appels « du CEO » avec voix clonée demandant transfert urgent).
- **Vidéos de « preuve » de scandales** inventés.

**Marchés** : les kits de deepfake et services de création sont disponibles sur dark web, prix variables. Certains services vendent « 1 minute de deepfake video » pour quelques centaines de dollars.

**Défense** : outils de détection (Microsoft Video Authenticator, Intel FakeCatcher, autres), watermarking des contenus légitimes, sensibilisation.

## 37.8 Implications défensives pour organisations

**Monitoring réputation**. Veille sur mentions de la marque dans contextes d'influence — sites clones, fake accounts amplifiant narratifs contre l'organisation, deepfakes de dirigeants.

**Protection des dirigeants**. Monitoring de l'exposition publique des dirigeants, alerte sur deepfakes, procédures de vérification en cas de demande urgente « venant du CEO ».

**Procédures anti-fraude**. Pour éviter les CEO fraud via deepfake, procédures de double vérification sur transactions importantes (canal indépendant, code secret, confirmation multi-personnes).

**Sensibilisation**. Formations sur reconnaissance des opérations d'influence, vérification des sources, identification des narratifs coordonnés.

**Coopération sectorielle et autorités**. Signalement aux autorités (VIGINUM en France pour la contre-ingérence informationnelle), partage via ISAC.

---
