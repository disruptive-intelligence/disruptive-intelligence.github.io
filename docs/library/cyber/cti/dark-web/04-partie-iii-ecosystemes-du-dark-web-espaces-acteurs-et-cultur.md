---
title: 'PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE'
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 4
chapters: 10
---

> **Ce que cette partie apprend.** Connaître concrètement les types d'espaces (forums, marchés, leak sites, messageries, marchés spécialisés) et les acteurs qui les peuplent. Comprendre leurs codes, leurs dynamiques, leurs économies. Maîtriser les objets d'investigation que rencontrera l'analyste.
>
> **Ce qu'elle ne couvre pas.** L'économie clandestine dans son ensemble (Partie IV), les méthodes de collecte (Partie V), les mécanismes d'attribution (Partie VI).
>
> **Ce que vous saurez faire après cette partie.** Reconnaître un forum sérieux d'un forum scam, lire un post de leak site ransomware avec discernement, comprendre ce qu'achètent vraiment les acheteurs sur Russian Market, et situer un vendeur de 0-day dans la chaîne d'attaque.

---

## Chapitre 10 — Forums clandestins : culture, hiérarchie et codes

Les forums sont l'ossature sociale du dark web. Contrairement aux marchés qui sont des points de transaction et aux messageries qui sont des canaux éphémères, les forums sont des **espaces de communauté persistants** où se construisent les réputations, se partagent les connaissances, et se recrutent les collaborations.

### 10.1 Typologie des forums

Les forums varient par leur **spécialité** et leur **langue**.

**Forums généralistes cybercriminels**. XSS Forum (ex-DamageLab, russophone, historique), Exploit.in (russophone), BreachForums (anglophone — succession de plusieurs instances après saisies, la plus récente opérée par ShinyHunters après l'arrestation de Pompompurin en 2023 puis de Baphomet en 2024). Ces forums couvrent un spectre large : vente de données, discussions sur le hacking, recherche de partenaires, ventes d'outils.

**Forums spécialisés par thématique**. Carding (BriansClub, WWH Club), fraude bancaire, ransomware, drogue (forums adjacents aux marchés), armes (très rares, majoritairement scams), CSAM (priorité 1 des forces de l'ordre).

**Forums géographiques**. Marchés régionaux — forums ukrainien, polonais, chinois, coréen, persophone, arabophone. Chaque bloc avec ses codes et ses acteurs.

**Forums de niche**. **IndustrialLeaks** (fictif, DARKSTREAM) est un exemple de ces forums nichés — spécialisation sur un segment (données industrielles) permet de concentrer une communauté de confiance plus étroite.

**Forums « respectables »** vs **forums low-end**. Les forums sérieux (XSS, Exploit) ont un KYC interne fort — vouching, tests techniques, réputation durable. Les forums low-end sont ouverts à tous, majoritairement peuplés de script kiddies et scammers.

### 10.2 Hiérarchie de membres

Structure typique d'un forum sérieux.

**Newcomer / Noob** : membre nouvellement inscrit, peu ou pas de posts. Accès limité — consultation des zones publiques, pas d'accès aux zones premium, pas droit de poster dans certains canaux.

**Member** : membre établi, quelques mois d'ancienneté, posts réguliers. Accès élargi, peut répondre à des posts, commencer à construire une réputation.

**Trusted / Verified** : membre vérifié — soit par **vouching** (parrainage par un membre établi qui engage sa réputation), soit par des transactions réussies, soit par un test technique. Peut vendre, peut poster dans les zones premium.

**VIP / Senior** : membre de très long terme avec réputation solide. Souvent des acteurs impliqués dans les activités majeures (opérateurs ransomware, IAB de premier plan). Accès à toutes les zones, peut parrainer des newcomers.

**Moderator** : modérateurs nommés par les admins. Arbitrent les litiges, bannissent les comptes indésirables, surveillent l'activité. Leur identité réelle est souvent connue des admins uniquement.

**Admin** : opérateurs du forum. Peuvent voir tout, décider des règles, collecter les droits d'entrée et commissions.

**Lurkers** : lecteurs silencieux. Les forums sérieux les tolèrent avec réserve — un compte inactif pendant 6 mois peut être supprimé. Les acteurs défensifs (analystes CTI, forces de l'ordre) sont presque toujours des lurkers par défaut.

### 10.3 Règles internes et modération

Les forums sérieux ont des règles publiées et appliquées. Variations selon les forums, mais constantes récurrentes.

**Interdictions typiques** :
- **Pédopornographie** : universellement interdite, même dans les forums criminels. Raison : attraction maximale des forces de l'ordre, destruction potentielle du forum.
- **Cibles sensibles** : dans les forums russophones, ciblage d'entités CEI souvent interdit par règle (protection politique implicite du Kremlin envers ces acteurs, en échange tacite d'un ciblage exclusif hors-CEI).
- **Dox personnels** : publication d'informations personnelles sur des membres, sauf dispute résolue par arbitrage.
- **Scam** : membre scammant un autre membre est bannissable — mais prouver le scam est toujours l'objet de débats.
- **Multi-accounts** : création de plusieurs comptes pour simuler la popularité (sock puppets).

**Sanctions** : warning avec perte temporaire de privilèges, bannissement temporaire (jours/semaines) ou définitif, bannissement étendu cross-forum parmi forums partenaires.

**Arbitrage** : en cas de litige commercial, un modérateur ou admin arbitre. Peut imposer un remboursement partiel, valider le scam, ou déclarer l'affaire non-résolue. Le pouvoir d'arbitrage est considérable — un admin corrompu ou compromis peut basculer le destin d'une dispute.

### 10.4 Codes culturels et jargon

Chaque forum a ses codes. Certains se retrouvent largement dans l'écosystème.

**Salutations et conventions**. « Hi all », « Greetings », « Bro » selon le style. Les forums russophones utilisent **Привет** (privet), **Коллеги** (kollegi — « collègues »), **Уважаемые** (uvazhaemye — « estimés »). Les usages trahissent parfois l'origine : un anglophone qui écrit « Privet all » tente probablement de se faire passer pour russophone.

**Termes techniques**. **FUD** (Fully Undetected — se dit d'un malware indétectable par les AV), **stub**, **crypter**, **binder**, **loader**. **IAB** (Initial Access Broker), **RaaS**, **CaaS**. Les forums spécialisés ont un lexique dense ; maîtriser ce lexique est essentiel pour comprendre les posts et ne pas se trahir.

**Formats de post standardisés**. Vente de données : description du contenu, échantillon gratuit, méthode de paiement acceptée, méthode de contact (Jabber/XMPP, Telegram, TOX, messagerie du forum). Annonce IAB : pays, secteur, type d'accès (VPN, RDP, Citrix, Active Directory), niveau de privilèges (user, admin local, admin domaine), revenue annuel de la cible, prix demandé.

**Signature et PGP**. Membres sérieux signent leurs posts en PGP — garantit que le compte n'a pas été usurpé. Un vendeur établi change rarement sa clé PGP sur la durée. Une rotation de clé PGP est un signal de changement d'opérateur (rachat de compte, compromis).

### 10.5 Économie des forums

Sources de revenus pour les opérateurs :
- **Droits d'entrée** : 50-500 USD typiquement. IndustrialLeaks demanderait 0,005 BTC (~250 USD). Barrière à l'entrée qui filtre les simples curieux.
- **Abonnements premium** : accès VIP, 100-1 000 USD/mois.
- **Commissions sur ventes** : 1-5% via l'escrow du forum.
- **Vente de services** : hosting pour membres, advertising, slots prioritaires.
- **Droits de vouching** : certains forums monétisent les droits de parrainage.

Un forum sérieux actif peut générer 50 000 à 500 000 USD/an pour ses opérateurs, parfois davantage.

### 10.6 Cycle de vie typique

**Phase 1 — Lancement** : recrutement initial, 6-12 mois de réputation à construire.

**Phase 2 — Croissance** : traction, modération, résilience. Peut durer 2-5 ans.

**Phase 3 — Maturité** : forum reconnu dans son segment, communauté stable.

**Phase 4 — Rupture** : saisie (Hydra 2022, Genesis 2023, BreachForums multiple), exit scam, épuisement opérationnel, guerre interne, ou désertion vers concurrent.

**Phase 5 — Reconstitution** : successeurs émergent. RaidForums → BreachForums → BreachForums v2 illustre cette cyclicité.

Pour l'investigateur, le cycle implique : **un forum étudié aujourd'hui n'existera peut-être plus dans 6 mois**. La documentation et la capture préservent la trace ; l'expertise historique est un actif d'investigation durable.

### 10.7 Fil rouge — DARKSTREAM : lecture d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 6 : exploration initiale**
>
> Après accès validé par vouching (Athéna a un membre partenaire dans un forum affilié qui a accepté de vouch une persona d'investigation, sous encadrement DGSI), Lucas explore IndustrialLeaks.
>
> **Structure du forum** : 8 zones publiques + 3 zones premium. Les zones publiques couvrent annonces, ventes générales de données, recherche de partenaires, discussions techniques. Les zones premium (accessibles après paiement additionnel) couvrent « industrial espionage », « government access », « supply chain intrusion ».
>
> **Activité récente** : ~30-40 nouveaux posts par semaine en zone publique, ~10 en zones premium. Rythme soutenu, pas un forum mort.
>
> **Le post aero_source** : posté il y a 11 jours dans la zone « Data sales ». Titre : « EU aerospace supplier, 420GB, propulsion R&D, defense programs inside ». Corps du post : brève description, liste d'échantillons disponibles (5 fichiers), prix 65 000 USDT. Méthode de contact : XMPP (aero_source@xmpp.jp — serveur non-custodial classique).
>
> **Profil aero_source** : compte créé il y a **8 mois**. 12 posts au total. 2 transactions confirmées précédemment (petits dumps, 5 000-15 000 USD). Pas de vouching publicly affiché. Pas de rating négatif.
>
> Lucas note : profil **intermédiaire** — pas un scammer opportuniste (historique transactionnel), pas un vétéran majeur. Possiblement un acteur qui a gradé de petites ventes à un dump plus gros. Possiblement aussi un proxy pour un acteur plus sophistiqué qui ne veut pas utiliser son propre pseudo.
>
> La première tâche est maintenant de **demander un échantillon** (via XMPP, avec une persona crédible). Avant cela, Lucas va continuer à cartographier : activités aero_source sur d'autres forums (Ch.26 pivoting), monitoring des posts d'aujourd'hui, observation du comportement conversationnel en zone commune.

---

## Chapitre 11 — Marchés du dark web : histoire, fonctionnement, évolution

Les **marchés** (marketplaces) sont les plateformes d'e-commerce clandestin — la couche la plus visible et la plus médiatisée du dark web. Après Silk Road, plusieurs dizaines ont existé et disparu.

### 11.1 Anatomie d'un marché

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

### 11.2 Les grands marchés historiques et actuels

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

### 11.3 Le modèle économique d'un marché

**Revenue** : commissions 2-5% sur transactions (parfois jusqu'à 10%) prélevées via l'escrow ; fees vendor (inscription 100-1 000 USD, fees mensuels, promotion payante) ; fees acheteur (dépôt minimum) ; advertising.

**Coûts** : hosting bulletproof (5 000-30 000 USD/mois selon scale), développement, modération, sécurité (audits, DDoS), marketing.

Un grand marché génère plusieurs millions à plusieurs dizaines de millions USD par an. Hydra à son apogée : estimations 5-10% du volume crypto transactionnel mondial lié aux darknet markets.

### 11.4 La dynamique de l'exit scam

**Phase 1 — Build-up**. Les opérateurs construisent la confiance et font croître le volume d'escrow. Plus le volume est haut, plus la « prime de départ » est attrayante.

**Phase 2 — Signals**. Dégradation qualité — support moins réactif, disputes mal résolues, retards de déblocage. Certains vendeurs s'alarment sur les forums.

**Phase 3 — Retention**. Ralentissement des withdrawals — délais accrus, vérifications supplémentaires. Les fonds s'accumulent.

**Phase 4 — Disappearance**. Le marché devient inaccessible. Les opérateurs ont transféré les fonds et disparu.

**Phase 5 — Succession**. Parfois, des « rescue » se proposent de racheter la base. Rarement efficace — la confiance est cassée.

Exit scams majeurs : Evolution (~12 M USD, 2015), Empire (~30 M USD, 2020). La probabilité d'exit scam augmente quand le marché grandit, que les FdO pressent, que les opérateurs vieillissent. Règle pour acheteurs avertis : **ne pas laisser plus que nécessaire sur le marché**.

### 11.5 Les marchés spécialisés 2024-2026

L'époque des grands marchés généralistes AlphaBay décline au profit de marchés **spécialisés**.

- **Marchés de logs** : Russian Market leader. Spécialisation totale sur les stealer logs (Ch.15). Croissance massive depuis 2023.
- **Marchés de fraude** : cartes bancaires, comptes bancaires, accès PayPal/Venmo, fullz. BriansClub, WWH Club, Joker's Stash historique (saisi 2021).
- **Marchés de SaaS criminel** : RaaS, PhaaS, DDoS-aaS. Interface orientée services avec abonnements.
- **Marchés d'accès** : IAB sur leurs propres plateformes ou via forums. Annonces et négociations plutôt que catalogue.
- **Marchés de malware** : vente de malware spécifique, crypters, loaders. Souvent intégrés aux forums.

Cette spécialisation reflète la **professionnalisation** de la cybercriminalité : chaque segment a ses acteurs, ses codes, ses mécanismes de confiance.

### 11.6 Investigation sur un marché : ce qu'on peut observer

Pour un analyste CTI, un marché offre plusieurs types d'observations utiles.

**Pricing intelligence** : prix observés donnent une grille pour évaluer les signals (Ch.14 sur les données, Ch.15 pour les stealer logs).

**Vendor profiling** : histoire d'un vendeur (ancienneté, transactions, ratings, spécialisations). Profils anciens avec beaucoup de transactions = acteurs établis, annonces plus susceptibles d'être authentiques.

**Victim signaling** : annonces mentionnant des cibles nommées (entreprises, secteurs, géographies) donnent des signaux pour le monitoring défensif.

**Trends** : évolution du volume de certains types de produits (hausse des ventes credentials cloud AWS depuis 2022 = signal industry-wide).

**Indicators** : adresses crypto observées comme paiements, pseudonymes vendeurs/acheteurs, infrastructures mentionnées.

**Limites** : tout ce qui est sur un marché n'est pas authentique. Scams, recyclages, agit-prop — l'analyste doit rester critique (Ch.32).

---

## Chapitre 12 — Leak sites ransomware et vitrines de revendication

Les **leak sites** sont les vitrines publiques des groupes ransomware. C'est là que les groupes revendiquent les victimes, publient des échantillons de données volées, et menacent de publier l'intégralité si la rançon n'est pas payée. Depuis l'avènement du modèle « double extorsion » (chiffrement + menace de publication), les leak sites sont devenus un des objets d'investigation CTI les plus riches.

### 12.1 Le modèle de la double extorsion

Historiquement, un ransomware chiffrait les données et demandait une rançon pour la clé de déchiffrement. La victime avait deux options : payer, ou restaurer depuis des backups. Si les backups existaient et étaient intacts, la victime pouvait refuser de payer.

Le modèle **double extorsion** (popularisé par Maze en 2019-2020) ajoute une couche. L'attaquant **exfiltre les données avant de les chiffrer**, puis menace de les publier publiquement si la rançon n'est pas payée — même si la victime a des backups et peut restaurer. L'intérêt criminel : augmente la pression (risque réputationnel, légal, contractuel de la publication), élargit le levier (même les victimes avec backups sont touchées).

Le **leak site** est l'outil de cette menace. Plateforme publique où le groupe **revendique** la victime (nom, secteur, pays), **publie des échantillons** de données volées (documents sensibles, financiers, RH), **affiche un countdown** jusqu'à publication intégrale, et **publie intégralement** si non-paiement.

L'effet psychologique est considérable. Une victime qui voit son nom publié sur un leak site majeur est dans une position extrêmement inconfortable — ses clients, partenaires, journalistes, autorités voient le post. La pression au paiement est forte.

### 12.2 Anatomie d'un post de leak site

Un post typique contient :
- **Nom de la victime** : raison sociale, parfois logo.
- **Secteur d'activité** : aerospace, healthcare, manufacturing, etc.
- **Pays / région** : juridiction.
- **Taille** : chiffre d'affaires approximatif, nombre d'employés.
- **Description** : quelques paragraphes sur ce que le groupe a exfiltré, type de données, volumétrie.
- **Countdown** : temps restant avant publication intégrale (typiquement 1-4 semaines).
- **Échantillons** : 10-100 fichiers publiés comme preuve de compromission. Choisis pour maximiser l'impact réputationnel (docs financiers, contrats, emails de dirigeants, données RH).
- **Contact** : méthode pour initier la négociation (souvent un onion avec un chat ou un formulaire).

Certains leak sites permettent des **interactions** : vote de la communauté pour pousser à la publication, mise en vente des données à la pièce, achats « first-come first-served » pour les autres criminels intéressés.

### 12.3 Les principaux groupes et leurs leak sites en 2024-2026

*Liste non exhaustive et évolutive — plusieurs groupes disparaissent ou rebrandent.*

**LockBit** — historiquement le plus prolifique. Leak site très actif, interface sombre, countdown flashy. **Operation Cronos (février 2024)** a saisi l'infrastructure, identifié Dmitry Khoroshev comme LockBitSupp, rendu publiques des clés de déchiffrement. LockBit a tenté un relaunch mais sa crédibilité est entamée.

**ALPHV / BlackCat** — malware sophistiqué écrit en Rust. Disparition en mars 2024 suite à ce qui semble être un exit scam post-paiement Change Healthcare (~22 M USD présumés).

**Cl0p** — spécialisé dans l'exploitation de vulnérabilités d'edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Leak site moins visuel que LockBit mais attaques techniquement sophistiquées.

**Black Basta** — actif depuis 2022, ciblage enterprise. Leak data massives en 2024-2025.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié.

**Akira** — émergent fin 2023, croissance rapide.

**RansomHub** — émergent mi-2024, semble absorber des affiliés d'ALPHV post-disparition.

**Qilin** — anglophone malgré son nom, actif.

**BianLian** — historiquement hybrid chiffrement + exfiltration, en 2023 s'est tourné vers extorsion seule (sans chiffrement).

**8Base, Hunters International, Inc Ransom, Dragonforce, Medusa** — autres groupes actifs à surveiller.

La scène change **mensuellement** — des groupes disparaissent, rebrandent, émergent. Les outils de monitoring (Ransomfeed, Ransomwatch) suivent ces évolutions en temps réel.

### 12.4 La lecture analytique d'un leak site

Pour un analyste CTI, chaque revendication de leak site est une source de renseignement.

**Vérification de la compromission réelle**. Tous les posts ne correspondent pas à de vraies victimes.
- **True positives** : la victime confirme (rarement publiquement, souvent via comms privées).
- **False claims** : groupe re-publie des données d'un breach antérieur sous son nom (pattern récurrent), ou revendique une compromission inexistante pour gonfler sa réputation.
- **Doubles claims** : la même victime revendiquée par deux groupes (conflit d'affiliés, rachat d'accès).

**Signaux sur l'activité du groupe**. Volume de revendications par mois, secteurs ciblés, géographies, évolution du rythme. Un groupe qui passe de 5 à 50 revendications/mois signale une croissance significative ou un recrutement d'affiliés.

**Patterns de targeting**. Les secteurs / pays ciblés donnent des indications sur les priorités et les compétences du groupe. Un groupe avec beaucoup de santé US est différent d'un groupe avec beaucoup de manufacturing EU.

**TTP implicites**. Les leak sites ne publient pas les TTPs (pour protéger leurs accès), mais des patterns peuvent se déduire — affinité pour certaines tailles de victimes, certains vecteurs d'entrée inférables par crosscheck avec cas connus.

**Indicateurs de disruption**. Un leak site qui disparaît brutalement, dont le countdown se fige, dont les affiliés migrent vers un concurrent — signaux d'une operation law enforcement en cours ou d'un conflit interne.

### 12.5 Le monitoring automatisé

**Ransomfeed.it** (site public, gratuit) agrège les revendications de dizaines de leak sites en temps réel. Outils open source type **Ransomwatch** fournissent des archives.

**Vendors CTI** (Recorded Future, Mandiant, CrowdStrike, Flashpoint, SOCRadar, Flare) intègrent le monitoring dans leurs plateformes avec alerting sur marques, secteurs, géographies.

**Limites** : leak sites modernes implémentent protections anti-scraping (CAPTCHA, rate limiting, proof-of-work) ; leak sites « tiered » avec partie publique + partie accessible uniquement après interaction ; échantillons publiés pas toujours téléchargés / analysés.

### 12.6 Le paiement de rançon : angle d'investigation

Les paiements de rançon, quand ils surviennent, laissent des traces **on-chain** exploitables.

**Mécanisme** : le groupe fournit une adresse Bitcoin / Monero / autre dans un portail de négociation. La victime paie. Les fonds transitent vers le groupe, puis sont blanchis (mixers, Monero swaps, OTC).

**Pour l'investigation** : si l'adresse est connue, le paiement confirme une compromission ; les mouvements on-chain peuvent révéler des connexions à d'autres opérations du même groupe ; les tentatives d'off-ramp peuvent révéler des identités si passage par exchange KYC.

**Saisies de paiements** : le FBI a récupéré des portions de rançons dans plusieurs cas emblématiques — Colonial Pipeline (~2,3 M USD récupérés en juin 2021), autres cas plus récents. Nécessite coopération internationale et vitesse d'exécution (avant blanchiment complet).

**Sanctions OFAC** : payer un groupe sanctionné (certains groupes sont sur listes OFAC) peut exposer l'organisation payeuse à des sanctions américaines. Considération réglementaire importante, qui pèse dans les décisions de paiement.

### 12.7 Le débat sur le paiement

Question récurrente : faut-il payer une rançon ?

**Arguments contre le paiement** : finance l'activité criminelle ; ne garantit pas la non-publication (plusieurs cas de groupes publiant après paiement) ; ne garantit pas l'intégrité des données exfiltrées ; crée un précédent — organisation qui paie devient cible récurrente ; expose à sanctions (groupes OFAC).

**Arguments pour le paiement** : urgence opérationnelle (vie humaine en cause dans certains cas — hôpitaux) ; coût moindre que la perte business prolongée ; clé de déchiffrement peut accélérer la reprise.

**Positions officielles** : la plupart des agences nationales (FBI, ANSSI, NCSC) recommandent de **ne pas payer** comme principe, tout en acceptant pragmatiquement que la décision incombe à la victime.

**Les faits statistiques** (rapports Coveware, Chainalysis) : la proportion de victimes qui paient a **baissé** sur la décennie (de ~70% en 2018-2019 à ~25-30% en 2024). Le paiement moyen a augmenté (quelques millions de dollars par cas en moyenne sur les grandes victimes). La dynamique a changé : moins de payeurs, payeurs plus gros.

---

## Chapitre 13 — Canaux, chats et messageries clandestines

Les **messageries et canaux** sont la couche temps réel du dark web. Là où forums et marchés sont persistants, les messageries sont éphémères — ce qui leur confère à la fois un intérêt opérationnel (communication rapide, pas de traces longues) et un défi investigatif (capturer les flux avant qu'ils disparaissent).

### 13.1 Les plateformes dominantes

**Telegram**. Dominant dans la cybercriminalité 2020-2024. Facilité d'usage, canaux publics avec des milliers d'abonnés, canaux privés invitation-only, groupes de discussion, bots. Historiquement perçu comme plus tolérant que les alternatives — politique de modération limitée.

**Impact de l'arrestation de Pavel Durov (août 2024)**. Suite à l'interpellation en France, Telegram a durci significativement sa modération — suppression massive de canaux criminels, coopération accrue avec les autorités sur les requêtes légales. Résultat : **migration partielle** de certains acteurs vers d'autres plateformes (Session, Matrix sur Tor, XMPP, retour aux forums .onion), mais Telegram reste dominant en volume absolu.

**XMPP (Jabber)**. Historiquement central dans la cybercriminalité russophone. Chaque utilisateur un JID (jabber ID) type `username@domain.com`. Chiffrement de bout en bout via OMEMO ou OTR. Serveurs non-custodial (l'admin du serveur ne peut pas lire les messages chiffrés). Résilient — si un serveur tombe, l'utilisateur peut migrer en changeant de JID. Usage encore courant chez les acteurs sérieux.

**TOX**. Protocole peer-to-peer chiffré de bout en bout. Pas de serveur central, pas de registrations. Moins populaire que XMPP mais utilisé pour communications très sensibles.

**Matrix (+ Element)**. Protocole fédéré, chiffrement E2E, parfois opéré sur Tor via onion routing des homeservers. Adoption lente dans la cybercriminalité mais croissante post-Durov.

**Session**. Messagerie basée sur Oxen/Lokinet, conçue pour anonymat. Pas de numéro de téléphone requis (contrairement à Signal, WhatsApp), pas de metadata centrale. Usage croissant chez acteurs paranoïaques.

**Signal**. Messagerie chiffrée grand public. **Moins utilisée** par cybercriminalité sophistiquée car requiert numéro de téléphone, metadata potentiellement saisissables via Twilio, cible fréquente de requêtes légales. Utilisée par activistes et journalistes plutôt que cybercrime organisé.

**IRC historique**. Usage résiduel pour certaines communautés de niche.

**Discord**. Usage modeste en cybercrime sérieux (modération forte, liens avec identités réelles fréquents), mais présent pour les marchés jeunes/gaming.

### 13.2 Les canaux Telegram cybercriminels

Les canaux Telegram publics cybercriminels peuvent être classés :

- **Canaux de leak** : publient des leaks gratuits (combo lists, databases publiées), souvent comme teasers pour des services payants. Des centaines de canaux, cumul de millions d'abonnés.
- **Canaux de CaaS** : phishing kits, DDoS, logs access. Interface commerciale, avec prix et méthodes de paiement.
- **Canaux de coordination** : groupes privés pour coordination opérationnelle entre membres d'une campagne. Typiquement invite-only.
- **Canaux d'hacktivisme** : revendiquent des attaques, publient des données volées dans un contexte idéologique (pro-russe, anti-israélien, etc.).
- **Canaux d'influence** : désinformation, amplification de narratifs, coordination d'opérations informationnelles.

### 13.3 L'investigation des messageries

**Capture de canaux publics**. Telegram notamment permet d'archiver les messages de canaux publics avec des outils comme Telethon (bibliothèque Python). Les canaux privés nécessitent une invitation — soit obtenue légitimement via un contact, soit impossible à obtenir.

**Métadonnées**. Même les messageries chiffrées laissent des métadonnées (qui a parlé à qui, quand, volume). Sur Telegram, les numéros de téléphone des membres de groupes peuvent parfois être extraits selon les paramètres de confidentialité.

**Corrélation avec pseudonymes**. Un pseudonyme sur un forum .onion peut avoir un handle Telegram affiché dans les posts. Suivre ce handle sur Telegram permet d'élargir la collecte.

**Identification par patterns**. Analyse stylométrique (Ch.29), timing d'activité, patterns de langue — permettent parfois de corréler des comptes supposés distincts.

**Actions légales**. Les autorités peuvent, dans certaines juridictions, exiger la coopération des plateformes. Telegram post-Durov coopère plus activement avec les requêtes légales.

### 13.4 Les limites investigatives

Les messageries sont plus difficiles à investiguer que les forums pour plusieurs raisons.

**Éphémérité**. Messages supprimés, canaux fermés, comptes bannis — la trace est vite perdue. Un analyste qui ne capture pas en temps réel perd l'information.

**Chiffrement**. Les messages chiffrés de bout en bout ne sont accessibles qu'aux participants — ni le serveur, ni les investigateurs ne peuvent les lire sans compromettre un endpoint.

**Volatilité des plateformes**. Un canal peut déménager ou disparaître du jour au lendemain. Maintenir le tracking nécessite de l'automatisation et de la réactivité.

**Faux comptes et sybil**. Les plateformes ouvertes permettent la création massive de faux comptes pour simuler l'activité, booster des narratifs, ou confondre les investigations.

### 13.5 L'usage des messageries dans DARKSTREAM

> **🌐 DARKSTREAM — Épisode 7 : XMPP avec aero_source**
>
> Lucas contacte aero_source via son XMPP affiché : `aero_source@xmpp.jp`. Serveur classique, non-custodial, fréquent dans la cybercriminalité russophone. Session chiffrée OTR négociée.
>
> Premier message de Lucas (persona « mapletech », se présente comme acheteur potentiel d'une entreprise tech intéressée par des specs aéronautiques — légende crédible côté profil Athéna) : demande d'échantillons supplémentaires, vérification du volume réel, méthode de paiement préférée.
>
> aero_source répond en 6 heures (cohérent avec un opérateur à temps plein sur fuseau horaire moscovite). Fournit 3 fichiers sample additionnels (1 spec technique de propulsion, 1 liste de fournisseurs, 1 extrait de notes de design). Confirme 420 Go total, paiement XMR préféré mais BTC accepté.
>
> Lucas note : style de langue russophone anglicisé (« I have all the data, you see ? ») — cohérent avec profil russophone. Fuseau horaire des réponses (toutes entre 08:00 et 22:00 MSK) conforte. Pas de fautes de tournure inhabituelles — acteur probablement expérimenté, pas un débutant.
>
> L'échantillon reçu sera analysé (Ch.25 — authentification). En parallèle, Lucas documente les métadonnées de la session : timestamps exacts, clé OTR négociée, serveur. Ces éléments pourront servir au rapport et au cross-matching avec d'autres pseudonymes.

---

## Chapitre 14 — Données volées et marchés de la fuite

Les données volées sont l'un des produits les plus échangés sur le dark web. Credentials, identités, dossiers médicaux, données d'entreprise — chaque type a son marché, son prix, ses acheteurs.

### 14.1 Types de données en circulation

**Credentials**. Couples email/mot de passe issus de breaches. Vendus en bulk (combo lists de millions d'entrées pour 5-50 USD) ou au détail (5-50 USD/pièce pour des credentials vérifiés sur services spécifiques).

**Logs d'infostealers**. Sessions complètes avec credentials, cookies, données machine — traités au Ch.15 en détail.

**Données bancaires**. Numéros de carte, CVV, accès aux comptes. Marché organisé (BriansClub, WWH Club, successeurs). Prix selon fraîcheur et pays.

**Données personnelles (fullz)**. Identité complète : nom, adresse, SSN/NIR, date de naissance, documents d'identité scannés. Utilisées pour fraude à l'identité, ouverture de comptes frauduleux.

**Données d'entreprise**. Documents internes, propriété intellectuelle, emails, bases clients. Les volumes exfiltrés par ransomware alimentent cette catégorie.

**Données de santé**. Dossiers médicaux, très prisés pour la fraude à l'assurance (US), le chantage, et la fraude à l'identité. Prix relativement élevés par unité (50-250 USD/dossier).

**Données gouvernementales**. Accès ou exfiltrations concernant administrations. Rareté élevée, prix variables selon sensibilité.

**Données industrielles / défense**. Spécifications techniques, plans, documents classifiés. Niche — DARKSTREAM s'inscrit dans cette catégorie. Acheteurs : concurrents industriels, services de renseignement étrangers, parfois groupes ransomware cherchant un levier de revente.

### 14.2 Grille de prix indicative 2025-2026

Sources : rapports SOCRadar (Annual Dark Web Report 2025), Privacy Affairs (Dark Web Price Index), observations Recorded Future, Flare. **Fortement indicatif** — varie par fraîcheur, spécificité, vendeur, marché.

| Type de donnée | Prix indicatif |
|---|---|
| Combo list (millions d'entrées, dates variables) | 5-50 USD |
| Credentials vérifiés, service spécifique | 5-50 USD / pièce |
| Carte bancaire avec CVV (compte actif) | 5-30 USD |
| Carte bancaire avec PIN / full access | 30-150 USD |
| Compte PayPal vérifié | 20-200 USD selon balance |
| Compte bancaire vérifié avec online banking | 100-1 000 USD selon balance |
| Fullz (identité complète) | 10-70 USD |
| Passeport scanné | 20-150 USD |
| Permis de conduire scanné | 15-70 USD |
| Log d'infostealer basique | 1-15 USD |
| Log d'infostealer avec VPN corporate | 50-500 USD |
| Accès VPN/RDP corporate (IAB) | 500-50 000 USD |
| Base de données d'entreprise | 500-100 000 USD+ |
| Dossier médical US | 50-250 USD |
| 0-day exploit (selon plateforme) | 5 000 - 2 500 000 USD |
| RaaS affiliation (droit d'affiliation) | 1 000 - 100 000 USD |

> **⚠️ ALERTE ANALYSTE** : Ces prix sont des moyennes indicatives à date (2025-2026) et fluctuent selon la réputation du vendeur, la fraîcheur, la verification, et les dynamiques de marché. Les prix des données bancaires simples ont tendance à se stabiliser ou baisser (saturation) tandis que les credentials d'accès corporate et les stealer logs avec tokens de session augmentent (demande RaaS).

### 14.3 Le lifecycle d'un breach

Les données volées suivent un cycle prévisible.

**Phase 1 — Exploitation privée**. Le groupe auteur du breach exploite d'abord les données pour son propre compte — ransomware, fraude, chantage de la victime. Durée : jours à mois.

**Phase 2 — Vente exclusive**. Les données sont mises en vente à prix élevé, avec clause d'exclusivité (pas de revente par le vendeur). Acheteurs : autres groupes cybercriminels cherchant un levier, concurrents industriels (rare et risqué), services de renseignement (cas politiques).

**Phase 3 — Revente large**. Si les données ne sont pas exclusivement vendues, ou si les termes d'exclusivité sont violés, revente à multiple acheteurs avec prix décroissant.

**Phase 4 — Publication publique / gratuite**. Après que la valeur commerciale a été extraite, les données sont souvent publiées gratuitement sur des canaux Telegram, pastebins, forums. Sert à construire la réputation d'un vendeur ou à publier sous couvert idéologique.

**Phase 5 — Intégration dans les bases publiques**. Have I Been Pwned, DeHashed, et autres services indexent les données pour vérification défensive. Les données deviennent **un asset défensif** — les DSI peuvent vérifier si leurs emails sont compromis.

La durée entre phase 1 et phase 5 varie considérablement — quelques semaines pour des petits breaches de moindre intérêt, plusieurs années pour des breaches majeurs gardés exclusifs longtemps.

### 14.4 Vérification de l'authenticité

Les annonces de données volées sont **massivement polluées par des scams, des recyclages, et des fabrications**. La vérification d'authenticité est un skill central de l'analyste.

**Échantillons**. Un vendeur sérieux fournit des échantillons gratuits vérifiables — emails avec domaine cohérent, formats réalistes. Un vendeur refusant systématiquement tout échantillon est suspect.

**Fraîcheur**. Les données déjà vues dans des breaches publics (via HIBP, DeHashed) sont recyclées — pas un nouveau breach, valeur réduite.

**Spécificité**. Des données très spécifiques à une organisation (noms d'employés internes, codes produit internes, contrats signés) sont plus crédibles que des templates génériques.

**Corroboration externe**. La victime confirme-t-elle ? Un CERT ou prestataire IR est-il impliqué ? Des indices publics confirment-ils la compromission (notifications régulateurs, communiqué de presse) ?

**Cohérence interne**. Les formats, conventions, horodatages sont-ils cohérents ? Une base de données avec des inconsistances format (dates parfois US, parfois EU) signale potentiellement un assemblage factice.

**Échantillon ciblé**. Demander au vendeur un échantillon spécifique (par exemple, un fichier contenant un certain nom). S'il peut le produire, authenticité probable. S'il refuse ou produit quelque chose d'incohérent, probable scam.

Voir Annexe E pour une grille d'évaluation complète de crédibilité.

### 14.5 La dimension sectorielle

Les données volées ne sont pas distribuées uniformément. Rapport Cyberint 2025 documente une concentration sur les secteurs à forte valeur : institutions financières (cartes, credentials bancaires, accès systèmes de trading), santé (dossiers médicaux, chantage, fraude assurance), télécommunications (SIM swapping, accès réseaux), gouvernement (données classifiées, identités fonctionnaires). Chaque secteur a son **modèle de monétisation** propre — détaillé au Ch.35.

### 14.6 Fil rouge — DARKSTREAM : premiers échantillons

> **🌐 DARKSTREAM — Épisode 8 : analyse des échantillons**
>
> Lucas reçoit 5 fichiers d'échantillons initiaux + 3 additionnels via XMPP. Protocole Athéna strict : fichiers ouverts **uniquement** dans une VM isolée (Whonix + Windows 10 jetable), jamais sur la machine de production. Scan antivirus préalable. Extraction des métadonnées avec exiftool.
>
> **Fichier 1** — « Propulsion_specs_Rev7.pdf ». 14 pages, schémas techniques. Métadonnées internes : auteur « M. Dubois », entreprise « Vectris Aerospace », créé en Nov 2025, modifié en Dec 2025. Softare MS Word → PDF. Numéro de révision cohérent avec conventions Vectris.
>
> **Fichier 2** — « Supplier_list_2025.xlsx ». 340 lignes de fournisseurs. Formatage Excel, adresses cohérentes (pays UE, US, Asie). Contient un fournisseur de test interne reconnu par le RSSI de Vectris (confidentiel — nom de fantaisie utilisé comme marker).
>
> **Fichier 3** — extrait email. Export de boîte mail interne d'un ingénieur R&D. Discussions techniques, jamais publiées publiquement. Content cohérent avec un vol Office 365.
>
> Les 3 échantillons additionnels : d'autres spécifications techniques, notes de réunion, extrait budgétaire.
>
> **Verdict Lucas** : authenticité **confirmée** au niveau échantillon. Cohérence avec la compromission initiale identifiée par Mandiant chez Vectris. Le marker interne présent dans le fichier 2 est un signe fort que le dump provient bien de la compromission Vectris. Lucas escalade immédiatement à la cellule de crise Vectris et à la DGSI. Le post aero_source est authentique ; la compromission est confirmée ; l'exfiltration circule bien sur le dark web.
>
> Question suivante : qui est aero_source ? Est-ce l'attaquant initial, un proxy, un courtier ? Prochaine étape : élargir le profiling via les autres activités du pseudonyme et via l'analyse des flux crypto associés.

---

## Chapitre 15 — Stealer logs : anatomie, marchés, investigation défensive

*Ce chapitre traite en profondeur le vecteur de compromission initiale le plus courant en 2025-2026. Les stealer logs sont devenus la matière première de l'écosystème cybercriminel — l'équivalent du pétrole brut qui alimente toute la chaîne de valeur.*

### 15.1 Qu'est-ce qu'un stealer log ?

Un **stealer log** est le produit de l'exécution d'un **infostealer** (malware spécialisé dans le vol de données de sessions) sur la machine d'une victime. Contrairement à un breach de base de données (qui produit des listes de credentials en masse), un stealer log capture **l'intégralité de l'environnement de la session utilisateur** sur un poste spécifique.

Un log typique contient :
- **Credentials du navigateur** : tous les logins/mots de passe enregistrés dans Chrome, Firefox, Edge, Brave, Opera — des dizaines voire des centaines de comptes par victime.
- **Cookies de session actifs** : permettent de se connecter à un service **sans mot de passe**, en contournant même le MFA. C'est **le vecteur le plus dangereux** de 2024-2026.
- **Données d'autofill** : noms, adresses, téléphones, données de cartes bancaires stockées.
- **Wallets crypto** : clés privées ou seed phrases stockées dans des extensions navigateur (MetaMask, Phantom, Exodus).
- **Données machine** : hostname, IP, OS, logiciels installés, capture d'écran au moment de l'exécution.
- **Sessions de messagerie** : tokens Discord, Telegram Desktop, WhatsApp Desktop.
- **Données Steam, Epic Games** : sessions gaming, de plus en plus ciblées.
- **Fichiers sélectifs** : certains stealers exfiltrent des fichiers selon patterns (documents avec mots-clés, certains types de fichiers).

La **puissance destructrice** d'un stealer log tient à sa granularité : ce n'est pas un seul couple login/mot de passe — c'est **l'intégralité de l'identité numérique** d'un utilisateur, capturée à un instant T, sur un poste spécifique.

### 15.2 Les infostealers dominants en 2025-2026

**Lumma Stealer** (aussi « LummaC2 »). Modèle d'abonnement, ~250 USD/mois. Extrêmement répandu. Évolution constante pour éviter la détection (polymorphic, updates hebdomadaires). En 2024-2025, dominant en volume.

**RedLine**. Historiquement dominant, toujours actif malgré tentatives de disruption. Développé par un acteur russophone. Large écosystème d'affiliés.

**Vidar** (dérivé d'Arkei). Populaire pour le ciblage de wallets crypto — modules spécifiques pour MetaMask, Coinbase Wallet, etc.

**Raccoon Stealer v2**. Relancé après l'arrestation de son opérateur initial en 2022.

**StealC**. Émergent, léger et polyvalent.

**RisePro**. Ciblage spécifique des applications crypto et des gestionnaires de mots de passe (LastPass, 1Password, Bitwarden).

**Meta Stealer, Phemedrone, DarkCrystal RAT** : autres familles documentées.

**Point d'entrée économique**. SOCRadar 2025 : **dès 15 USD en version de base**, avec modèles d'abonnement qui rendent les stealers accessibles à pratiquement n'importe quel acteur. Cette accessibilité explique leur adoption massive.

**Vecteurs de distribution** :
- **Malvertising** : publicités Google/Bing malveillantes redirigeant vers des téléchargements piégés. Technique en forte croissance 2024-2025.
- **Faux sites de téléchargement logiciels crackés**. Vecteur historique dominant — particulièrement efficace sur utilisateurs cherchant cracks.
- **YouTube tutorials malveillants** : descriptions de tutoriels contenant des liens vers des malwares sous couvert d'outils légitimes.
- **Pièces jointes email** : documents Office avec macros, archives protégées par mot de passe.
- **Packages npm/PyPI malveillants** : supply chain logicielle.
- **Telegram groupes** : liens de téléchargement douteux.

### 15.3 Les marchés de stealer logs

**Russian Market**. Successeur de facto de Genesis Market (saisi avril 2023, Operation Cookie Monster). Plus grand marché de logs actif en 2025-2026. Logs vendus individuellement avec système de **recherche par domaine** — l'acheteur cherche des logs contenant des credentials pour un domaine spécifique (par exemple, un VPN d'entreprise cible). Prix : 1-15 USD pour log basique, 50-500 USD pour log avec accès corporate (VPN, Citrix, RDP).

**Genesis Market (historique, saisi 2023)** — modèle innovant qui mérite mention. Genesis ne vendait pas seulement des credentials, mais des **bots** — navigateurs virtuels répliquant l'empreinte exacte de la victime (fingerprint navigateur, cookies, résolution d'écran, timezone, liste des plugins). Permettait d'usurper la session sans déclencher les contrôles anti-fraude basés sur fingerprint. Modèle repris par d'autres marchés.

**Canaux Telegram**. De nombreux logs distribués en bulk via canaux spécialisés, souvent **gratuitement** (« free logs ») pour attirer vers des services premium. Canaux gratuits contiennent logs anciens ou faibles valeur, mais constituent point d'entrée pour acteurs peu sophistiqués.

**2easy.gg historique**. Marché spécialisé fermé, opérations law enforcement en 2024.

**StealC Marketplace, LummaC2 Shop** : marchés adossés à des familles de stealers spécifiques.

### 15.4 Investigation défensive : workflow

Pour un analyste défensif surveillant l'exposition de son organisation.

**Étape 1 — Monitoring des domaines**. Configurer des alertes sur marchés de logs (via plateformes commerciales type Flare, Hudson Rock, SOCRadar, Breach.ai, Flashpoint) pour les domaines de l'organisation. Chaque nouveau log contenant des credentials du domaine déclenche une alerte.

**Étape 2 — Évaluation du log**. Pour chaque log détecté, évaluer la criticité :
- **Log avec credentials webmail uniquement** : préoccupant mais gérable (reset mot de passe + vérif MFA).
- **Log avec credentials VPN/Citrix + cookies de session actifs** : **urgence** — l'attaquant peut accéder au SI sans connaître le mot de passe actuel si le cookie est encore valide.
- **Log avec credentials cloud (Azure, AWS, GCP)** : critique — impact potentiellement majeur sur l'infrastructure.

**Étape 3 — Identification du poste source**. Les métadonnées du log (hostname, IP, OS, softwares installés) permettent souvent d'identifier le poste compromis. Ce poste est **potentiellement toujours infecté** par le stealer — **changer le mot de passe sans éradiquer le stealer ne fait que fournir un nouveau mot de passe à l'attaquant**. C'est l'erreur la plus fréquente et la plus dangereuse.

**Étape 4 — Remédiation**. Le poste source doit être **isolé et réimaginé**. Tous les credentials contenus dans le log doivent être réinitialisés — pas seulement les credentials corporate, mais aussi les comptes personnels qui pourraient servir de pivot (compte GitHub personnel avec accès à des repos de l'entreprise). **Sessions actives révoquées** (tokens, cookies invalidés).

**Étape 5 — Hunting**. Le SOC vérifie si les credentials du log ont été utilisés pour des connexions suspectes depuis la date estimée de compromission. Recherche dans logs d'authentification (VPN, AD, applications cloud) pour connexions depuis IPs inhabituelles, user agents inconnus, horaires atypiques.

### 15.5 Statistiques et géographie

Données SOCRadar 2025 : concentration des logs sur grandes plateformes consumer :
- Facebook : 93M+ logs
- Google : 67M+
- Roblox : 66M+
- Instagram : 34M+
- Microsoft Live : 31M+
- Amazon : 22M+
- Netflix : 22M+
- PayPal : 19M+

Géographie : Inde domine (2,7M logs), Brésil (1,9M), Indonésie (1,3M), États-Unis (1,2M). La position basse des US suggère meilleure détection ou remédiation plus rapide plutôt que taux d'infection inférieur.

**Implications** : plateformes gaming (Roblox, Twitch, Epic Games — utilisateurs jeunes avec hygiène credentials faible) et e-commerce/streaming (Amazon, Netflix — données de paiement stockées) sont cibles privilégiées. PayPal se distingue comme facilitateur direct de fraude.

### 15.6 Limites et faux positifs

**Expiration**. Les cookies expirent (typiquement 30-90 jours), les mots de passe peuvent avoir été changés, le poste peut avoir été réimaginé. Log ancien (6+ mois) a une probabilité d'exploitation réussie **beaucoup plus faible** qu'un log frais.

**Faux positifs**. Domaine similaire (typosquatting), employé utilisant email pro sur site grand public, log recyclé déjà traité. Filtrage humain indispensable.

**Bruit**. Un grand compte monitoring génère des dizaines d'alertes par jour — priorisation nécessaire (criticité, fraîcheur).

### 15.7 Fil rouge — DARKSTREAM : les stealer logs Vectris

> **🌐 DARKSTREAM — Épisode 9 : découverte collatérale**
>
> En parallèle de son investigation sur aero_source, Lucas vérifie l'exposition Vectris sur les marchés de logs. Recherche sur Russian Market via l'accès monitoring Athéna : **12 logs** contenant des credentials du domaine `vectris-aerospace.eu`.
>
> Analyse des 12 logs :
> - 3 logs contiennent **credentials VPN (Fortinet FortiClient) avec cookies de session** — **urgence maximale**.
> - 4 logs avec credentials webmail Outlook 365.
> - 2 logs avec accès à une application SaaS RH.
> - 3 logs avec credentials divers (Jira, GitLab enterprise).
>
> Les 3 logs VPN datent de **2 à 4 mois** — compatible avec la timeline de la compromission Vectris. **Hypothèse** : l'attaquant initial aurait utilisé un infostealer comme vecteur d'accès, les logs ont ensuite été revendus sur Russian Market par un courtier (possiblement distinct de l'auteur de l'exfiltration finale), et aero_source est soit le même acteur, soit un acheteur final qui revend les données.
>
> Hostnames des 3 logs VPN :
> - VECTRIS-SALES-047 : laptop commercial.
> - VECTRIS-RD-112 : poste R&D — **celui-ci est particulièrement préoccupant**, potentiellement le vecteur de l'exfiltration initiale des 420 Go.
> - VECTRIS-IT-008 : poste IT.
>
> Lucas escalade immédiatement au RSSI Vectris. Mandiant (IR prestataire) confirme : VECTRIS-RD-112 est bien le poste central de la compromission, déjà identifié comme point d'entrée. Les deux autres sont des compromissions collatérales non identifiées jusqu'ici — actions immédiates enclenchées (isolement, forensics, reset massif).
>
> Découverte collatérale précieuse : la surveillance dark web a révélé **deux postes compromis supplémentaires** que l'investigation interne n'avait pas identifiés. Illustration concrète de la valeur défensive de la veille dark web.

---

## Chapitre 16 — Services criminels et profils d'acteurs

Au-delà des produits (données, credentials), le dark web est un marché de **services** — crime-as-a-service sous toutes ses formes. Ce chapitre cartographie les services majeurs et les profils d'acteurs.

### 16.1 Les services majeurs

**Ransomware-as-a-Service (RaaS)**. Modèle dominant de l'écosystème ransomware. L'opérateur développe et maintient le malware + l'infrastructure (leak site, portail de négociation). Les **affiliés** déploient le ransomware chez des victimes, moyennant partage des gains (typiquement 70/30 affilié/opérateur, parfois 80/20). Ce modèle a industrialisé le ransomware : LockBit, ALPHV, Conti historique, Black Basta, Play, RansomHub actuels.

**Initial Access-as-a-Service (IAaaS)**. Les IAB compromettent et **vendent l'accès** préqualifié. Modèle spécialisé : l'IAB ne ransomware pas lui-même, il vend à un opérateur ransomware (ou autre acheteur) un accès déjà installé. Prix : 500-50 000 USD selon la cible (CA, secteur, niveau de privilèges). Délai de monétisation : plus rapide que développer une intrusion soi-même.

**Phishing-as-a-Service (PhaaS)**. Kits de phishing prêts à l'emploi, avec interface de gestion, templates, hosting. LabHost (démantelé avril 2024), EvilProxy, Evilginx (open source mais utilisé massivement). PhaaS a popularisé l'**AiTM** (Adversary-in-the-Middle) qui contourne le MFA en capturant cookies de session.

**Malware-as-a-Service (MaaS)**. Location de malware — infostealers (Lumma, RedLine mensuel), loaders, RAT, cryptominers.

**DDoS-as-a-Service**. Booters et stressers. De quelques dollars par attaque à plusieurs centaines pour attaques soutenues.

**Hosting bulletproof**. Infrastructure pour héberger contenu illicite (Ch.9).

**Cryptage / Obfuscation-as-a-Service**. Crypters et obfuscateurs pour rendre malware FUD. Service essentiel pour les opérateurs malware.

**Money laundering-as-a-Service**. Services de blanchiment crypto. Commissions 10-30% (Ch.21).

**Account checker / cracking services**. Vérification en masse de combo lists contre des services cibles (valider quels credentials marchent réellement).

**Spam / SMS bombing services**. Services commerciaux d'envoi massif.

### 16.2 Profils d'acteurs typiques

**L'opérateur RaaS**. Figure centrale. Développe le malware, opère l'infrastructure, gère les affiliés, négocie les rançons. Équipe typique : 5-20 personnes. Revenu : plusieurs millions à dizaines de millions USD/an pour les groupes dominants. Exemple public : Dmitry Khoroshev / LockBitSupp (LockBit), autres en grande partie anonymes.

**L'affilié RaaS**. Exécutant opérationnel. Achète l'accès (via IAB ou compromet lui-même), déploie le ransomware, reçoit sa part des gains. Peut être indépendant ou partie d'une équipe. Skills : persistance, lateral movement, AD domination, parfois exfiltration. Turnover élevé — les affiliés changent de groupe selon conditions et opportunités.

**L'Initial Access Broker (IAB)**. Spécialisé dans la compromission initiale. Sources d'accès : exploitation d'edge devices (VPN, RDP exposés, vulnérabilités publiques), phishing, achat de logs, social engineering. Vend l'accès après qualification (confirmation des privilèges, cartographie minimale). Actifs connus : marées de posts sur XSS, Exploit, parfois accès de premier plan sur BreachForums.

**Le developer malware**. Écrit le code. Profil technique pur. Peut travailler pour un groupe, en freelance, ou vendre son malware comme produit. Certains devs sont très réputés dans l'écosystème pour des familles de malware spécifiques.

**Le courtier (broker) de données**. Collecte des données (achat, récupération de breaches publiés) et revend en les repackageant. Spécialisation par type (fullz, credentials bancaires, dossiers médicaux).

**Le money mule et le launderer**. Deux profils distincts. Le **mule** prête son compte bancaire ou son wallet crypto pour faire transiter des fonds — souvent recruté sous prétexte d'un emploi légitime, parfois consentant. Le **launderer** est professionnel, structure des opérations de blanchiment sophistiquées (multi-hop crypto, mixers, conversions off-chain).

**Le carder**. Spécialisé fraude cartes bancaires. Achète des dumps, les teste, les monétise (achats de biens revendables, cash advance, autres).

**Le script kiddie**. Amateur avec skills limités, utilise outils achetés. Majoritaire en nombre, minoritaire en impact. Dans les forums sérieux, traités avec condescendance.

**Le hacktiviste**. Motivation idéologique plus que financière. Opère souvent via canaux Telegram publics, moins sur forums .onion fermés. Anonymous historique, KillNet, Cyber Av3ngers, IT Army of Ukraine, etc. (Ch.38).

**L'agent étatique**. Opérateur qui utilise le dark web comme cover ou comme canal d'acquisition. APT29 a historiquement acheté des accès sur forums. La DPRK utilise le dark web pour vendre des données volées (Lazarus). Ces acteurs n'ont pas de « profil » simple — ils adaptent à chaque opération.

**L'analyste défensif / force de l'ordre / journaliste**. Observateur légitime (avec mandat). Se présente généralement comme lurker, parfois sous couverture avec persona active (Ch.22, Ch.23, Ch.30).

### 16.3 La chaîne de valeur d'une compromission moderne

Comprendre les acteurs permet de reconstituer la chaîne typique d'une attaque enterprise 2024-2026.

**Étape 1 — Vol initial de credentials**. Un utilisateur télécharge un logiciel crack piégé, son poste personnel est infecté par un infostealer (Lumma), ses credentials (y compris son compte pro utilisé sur le poste perso) sont exfiltrés.

**Étape 2 — Vente en bulk**. L'opérateur de stealer vend les logs en lot sur Russian Market. Log basique : 15 USD.

**Étape 3 — Achat par IAB**. Un IAB achète des logs en volume, les trie pour identifier ceux avec accès corporate intéressants (VPN, Citrix, tokens cloud).

**Étape 4 — Qualification par IAB**. L'IAB utilise les credentials pour entrer dans le SI cible, vérifier les privilèges, cartographier l'environnement, identifier les cibles de valeur (DC, fileservers, backups).

**Étape 5 — Vente à affilié RaaS**. L'IAB poste l'accès sur un forum : « Access RDP + AD domain admin, EU manufacturing company, CA 500M USD, 2 000 endpoints, backup Veeam visible ». Prix : 25 000 USD.

**Étape 6 — Déploiement ransomware**. L'affilié achète l'accès, déploie le ransomware du groupe (Black Basta, par exemple). Exfiltre d'abord 800 Go de données sensibles (double extorsion), puis chiffre.

**Étape 7 — Négociation et rançon**. La victime est contactée via portail de négociation. Rançon demandée : 3 M USD. Négociation éventuelle. Paiement en Bitcoin.

**Étape 8 — Partage des gains**. Affilié reçoit 70% (2,1 M USD), opérateur RaaS 30% (0,9 M USD). Transferts crypto vers wallets opérationnels.

**Étape 9 — Blanchiment**. Les fonds passent par mixers, swaps Monero, exchanges non-KYC, OTC desks. Après 3-6 mois de chaînes, partie des fonds est convertie en fiat utilisable.

**Étape 10 — Publication partielle ou totale si non-paiement**. Si la victime ne paie pas, le groupe RaaS publie tout ou partie des données sur son leak site. Certaines données valorisables peuvent être revendues en parallèle.

Toute cette chaîne — de l'infection initiale au blanchiment — peut prendre **3 à 6 mois**. Chaque étape est opérée par un acteur spécialisé, avec ses skills et ses marchés. La cybercriminalité est une **industrie structurée**, pas une activité individuelle.

Pour le défenseur, chaque étape de cette chaîne est une **opportunité d'interruption** : détecter le stealer avant l'exfiltration, le log avant l'achat par IAB, l'accès IAB avant la vente, l'affilié avant le déploiement, l'exfiltration avant le chiffrement, la rançon avant le paiement. Plus la détection est précoce, plus l'impact est limité.

### 16.4 Fil rouge — DARKSTREAM : la chaîne reconstituée

> **🌐 DARKSTREAM — Épisode 10 : cartographie de la chaîne**
>
> Au terme de 2 semaines d'investigation, Lucas reconstitue la chaîne probable de compromission Vectris.
>
> **Étape 1** — Infection initiale : un ingénieur R&D (VECTRIS-RD-112) a téléchargé un outil CAD crackéé depuis un site de warez. Infostealer Lumma déployé. Log exfiltré fin 2025.
>
> **Étape 2** — Vente du log sur Russian Market fin 2025, ~120 USD (tier « corporate VPN + tokens actifs », premium).
>
> **Étape 3** — Achat par un IAB russophone (pseudonyme identifié partiellement : **magnit_ru**, actif sur XSS Forum). Qualification : vérification que les credentials VPN fonctionnent, exploration réseau, identification que Vectris est un groupe industriel aerospace.
>
> **Étape 4** — Revente. magnit_ru poste l'accès sur XSS début 2026 : « Access aerospace EU, R&D network, defense programs ». Prix demandé : ~35 000 USD.
>
> **Étape 5** — Achat par aero_source (ou un commanditaire derrière lui). Hypothèse Lucas : aero_source est soit (a) un opérateur individuel qui a acheté l'accès et a exfiltré les 420 Go lui-même, soit (b) le front d'une équipe plus grande, soit (c) un revendeur qui a acheté le dump à un acteur qui lui a fait l'exfiltration.
>
> **Étape 6** — Exfiltration : ~12 semaines d'activité sur le réseau Vectris (traces cohérentes avec les logs Mandiant), 420 Go extraits, focus sur R&D propulsion et dossiers fournisseurs défense.
>
> **Étape 7** — Vente sur IndustrialLeaks : post public il y a 11 jours à 65 000 USDT.
>
> La chaîne implique donc **au moins 3 acteurs distincts** : opérateur Lumma (infection initiale, revente bulk), magnit_ru (IAB), aero_source (exfiltration ou revente finale). Complexifie l'attribution mais multiplie les angles d'investigation. Identifier un seul de ces acteurs précisément pourrait suffire à remonter la chaîne.

---

## Chapitre 17 — Marché des 0-day et chaîne exploit → attaque

Les **0-day** — vulnérabilités non connues de l'éditeur et donc non patchées — sont l'apex de l'écosystème offensif. Leur marché est structurant pour le dark web, avec des particularités qui distinguent ce segment du reste de la cybercriminalité.

### 17.1 Qu'est-ce qu'un 0-day

Terminologie précise.

**Vulnérabilité** : faille dans un logiciel, une configuration, un protocole permettant potentiellement une exploitation malveillante.

**0-day (zero-day)** : vulnérabilité non encore connue publiquement et non patchée par l'éditeur. Son exploitation est potentiellement **surprise** — aucune signature ne la détecte, aucune mitigation connue ne la bloque.

**N-day** : vulnérabilité récemment rendue publique et patchée, mais pas encore déployée largement. Les attaquants exploitent les N-day pendant la fenêtre entre publication du patch et déploiement généralisé.

**Exploit** : code qui exploite une vulnérabilité. Peut être théorique (proof-of-concept), fonctionnel (weaponisé), ou en production (stable, compatible multi-environnements).

**Exploit chain** : chaîne de plusieurs exploits combinés pour atteindre un objectif plus ambitieux (par exemple : escape sandbox navigateur + escalation privilèges kernel → RCE avec privilèges système).

### 17.2 Le marché légal : bug bounty et brokers

L'écosystème des vulnérabilités n'est pas uniquement illégal. Un marché légal existe, structuré.

**Bug bounty programs**. Les grands éditeurs (Google, Microsoft, Apple, Mozilla, Meta, Samsung, etc.) offrent des récompenses pour la déclaration responsable de vulnérabilités. Montants : de quelques centaines de dollars pour des bugs mineurs à plusieurs millions pour des chaînes d'exploits complètes sur iOS ou Android. **Apple Security Bounty** : jusqu'à 2 M USD pour une chaîne avec persistance sur iOS. **Google Vulnerability Reward Program** : jusqu'à 1,5 M USD pour certains cas Android.

**Plateformes bug bounty** : HackerOne, Bugcrowd, Intigriti, YesWeHack (français), Synack. Hébergent les programmes de dizaines de milliers d'organisations.

**Pwn2Own** : compétition annuelle (ZDI / Trend Micro, plusieurs éditions par an dans différentes villes) où des chercheurs exploitent des logiciels cibles pour des récompenses publiques. Moyen médiatisé de révéler des vulnérabilités.

**ZDI (Zero Day Initiative)** : programme de rachat de vulnérabilités par Trend Micro. Paye les chercheurs, travaille avec les éditeurs pour patch, publie les advisories.

**Brokers commerciaux** : entreprises qui achètent des vulnérabilités à des chercheurs et revendent à des clients (souvent gouvernementaux). **Zerodium** est la référence historique — prix publics depuis des années, jusqu'à 2,5 M USD pour des chaînes Android. **Crowdfense** : concurrent. **Intrepidus / ERNW / Vupen historique** : prédécesseurs. Ces brokers opèrent **légalement**, vendant à des gouvernements de démocraties (ou présentés comme tels — débats existent sur certains clients effectifs).

### 17.3 Le marché gris et noir

En parallèle du marché légal, un marché **gris** (légalité ambiguë) et **noir** (clairement illégal) existe.

**Marché gris** : vente à des gouvernements de régimes autoritaires, ou à des entreprises de surveillance. Le 0-day lui-même n'est pas illégal — la vulnérabilité est juste de l'information technique. Mais son usage ultérieur peut être problématique. NSO Group (Pegasus), Candiru, Intellexa / Predator achètent des 0-day et les intègrent dans leurs outils de surveillance. Leurs clients incluent parfois des États qui ciblent journalistes et dissidents.

**Marché noir** : vente à des acteurs cybercriminels ou à des services de renseignement hostiles qui exploitent pour opérations offensives. Moins médiatisé, moins structuré, mais actif. Les prix peuvent rivaliser avec le marché légal pour les vulnérabilités les plus précieuses.

**Disruption** : les 0-day disparaissent du marché après publication. Leur valeur chute de 90%+ dans les semaines suivant un patch public. Les acteurs du marché noir cherchent donc à acheter des 0-day avec **exclusivité** et à les utiliser **rapidement** avant découverte et patching.

### 17.4 Prix indicatifs

Sources : Zerodium price list publique, Crowdfense, rapports Atlantic Council, observations marché noir.

| Cible | Marché légal bug bounty | Marché broker (Zerodium, Crowdfense) | Marché gris/noir |
|---|---|---|---|
| Chrome RCE | 250 k USD (Google VRP) | 500 k - 1,5 M USD | 500 k - 2 M USD |
| iOS complete chain avec persistance | 2 M USD (Apple) | 2 - 2,5 M USD | 5 - 10 M USD (rumeurs) |
| Android complete chain | 1,5 M USD (Google) | 1,5 - 2,5 M USD | 3 - 8 M USD |
| WhatsApp RCE 1-click | N/A | 1,5 M USD | Plus |
| Windows LPE | ~30 k USD | ~80 k - 200 k USD | Comparable |
| Exchange Server RCE | ~30 k USD | ~100 k USD | Plus |
| Safari RCE | 100 k USD | ~300 k USD | Plus |
| Tor Browser exploit | — | Jusqu'à 1 M USD | Demande forte renseignement |

Variation par :
- **Fiabilité** : exploit stable qui marche à 100% vaut plus qu'un exploit probabiliste.
- **Fraîcheur** : exploit qui vient d'être découvert vs exploit avec risque de découverte imminente.
- **Contexte d'exploitation** : nécessite interaction utilisateur vs fully remote, 1-click vs 0-click.
- **Persistance** : survit aux reboot ou non.
- **Compatibilité** : fonctionne sur multiple versions du logiciel cible.

### 17.5 La chaîne 0-day → attaque

Comment un 0-day devient une attaque concrète.

**Étape 1 — Découverte**. Un chercheur identifie une vulnérabilité. Peut venir de fuzzing automatisé (AFL, libFuzzer), de reverse engineering de patches (« 1-day research » — étudier un patch pour identifier la vuln qu'il corrige), d'audit manuel de code source.

**Étape 2 — Weaponisation**. Développement d'un exploit fonctionnel. Fiabilisation, test sur multiples versions, contournement des mitigations (ASLR, DEP, CFI, PAC, etc.). Peut prendre des semaines à des mois.

**Étape 3 — Décision économique**. Le chercheur choisit un canal : responsible disclosure (bug bounty, gratuit jusqu'à 2 M USD chez Apple), broker légal (Zerodium), broker gris, vente privée à un acteur offensif.

**Étape 4 — Intégration dans un outil**. L'acheteur intègre l'exploit dans son framework. NSO l'intègre dans Pegasus ; un APT l'intègre dans sa toolchain ; un opérateur ransomware l'intègre dans son loader.

**Étape 5 — Déploiement**. L'outil est utilisé contre des cibles. La vulnérabilité commence à être exploitée dans la nature.

**Étape 6 — Détection**. Tôt ou tard, un défenseur détecte l'attaque. Peut prendre des jours (attaque bruyante, nombreuses victimes) ou des années (opération ciblée discrète, peu de victimes).

**Étape 7 — Publication / patching**. Après détection, l'éditeur est notifié (par le défenseur, par un chercheur ayant découvert indépendamment, par le vendor observant les attaques), patche, publie l'advisory. La vuln devient N-day.

**Étape 8 — Exploitation N-day**. Fenêtre de quelques jours à semaines où le patch existe mais pas partout. Acteurs moins sophistiqués exploitent massivement.

**Étape 9 — Oubli**. La vuln devient partie de l'histoire. Son usage continue longtemps contre les systèmes non patchés (certains systèmes hérités jamais patchés sont vulnérables à des bugs découverts il y a 10 ans).

### 17.6 Les vagues récentes exploitant des 0-day

Illustrations récentes de la chaîne 0-day → attaque dans la nature.

**MOVEit Transfer (mai-juin 2023)** — Cl0p exploite CVE-2023-34362 (0-day SQL injection dans MOVEit) massivement, impacte des milliers d'organisations (santé, gouvernements, entreprises) via leurs prestataires utilisant MOVEit.

**Citrix Bleed (CVE-2023-4966, octobre 2023)** — vulnérabilité Citrix Netscaler exploitée par LockBit, autres acteurs. Permet bypass MFA via leak de sessions.

**Ivanti Connect Secure (CVE-2023-46805, CVE-2024-21887, janvier 2024)** — exploitation par Volt Typhoon (Chine, APT) et d'autres.

**Palo Alto GlobalProtect (CVE-2024-3400, avril 2024)** — exploité par UTA0218 (possible APT).

**Oracle EBS (2025)** — exploité par Cl0p comme continuation de leur stratégie d'exploitation edge devices.

Ces vagues illustrent une tendance : les APT et groupes ransomware sophistiqués ont progressivement adopté l'exploitation de 0-day sur edge devices comme vecteur privilégié — plus discret qu'un phishing (qui génère des alertes), plus scalable qu'une intrusion manuelle, et ciblant des dispositifs souvent dépourvus de visibilité défensive.

### 17.7 Les ventes de 0-day sur forums

Sur les forums cybercriminels, les ventes de 0-day sont **rares publiquement** mais existent. Patterns observés :

**Posts discrets**. Annonce sur XSS ou Exploit avec minimum d'info publique, négociation en privé. L'annonce mentionne classe de vulnérabilité (RCE, LPE, sandbox escape), cible (Chrome, Firefox, iOS, Android, produit spécifique), prix plancher.

**Escrow par forum**. Les forums sérieux proposent un escrow qualifié pour ces transactions — admin prend la clé du buyer et du seller, valide l'exploit fonctionne, libère après validation.

**Réputation extrême**. Seuls les vendeurs les plus établis font des ventes visibles — un nouveau compte qui prétend vendre un iOS 0-day est presque certainement scammer.

**Screenshots de démonstration**. Certains vendeurs fournissent preuve de fonctionnement (vidéo, screenshot) sous NDA avant achat. D'autres refusent toute démo sans paiement préalable (difficile à contourner mais classique).

**Clients typiques forums** : affiliés RaaS, APT moins dotés, acteurs étatiques moyens — pas les grands (qui ont leurs propres canaux).

### 17.8 Investigation et renseignement sur les 0-day

Pour un analyste CTI défensif.

**Veille des annonces**. Monitoring de XSS, Exploit, BreachForums pour posts liés à des 0-day cibles (produits utilisés par son organisation). Alerting sur mots-clés.

**Détection des exploitations dans la nature**. Anomalies comportementales sur les edge devices (VPN, firewalls, serveurs exposés) même sans signature existante. Threat hunting proactif sur les produits historiquement ciblés.

**Collaboration avec éditeurs**. Remontée rapide à l'éditeur en cas de détection d'exploitation suspecte, pour accélérer potentiel patching.

**Analyse de patches**. Étude des patches publiés pour identifier les vulns patchées (1-day research en usage défensif) et anticiper les exploitations massives dans la fenêtre N-day.

### 17.9 Fil rouge — DARKSTREAM : pas de 0-day impliqué

> **🌐 DARKSTREAM — Épisode 11 : angle 0-day écarté**
>
> Lucas a initialement envisagé que la compromission Vectris aurait pu impliquer un 0-day (cible industrielle de valeur). Son investigation croisée (forensics Mandiant côté Vectris, observations dark web) confirme : **pas de 0-day**. Le vecteur était un **stealer log** classique, un accès VPN corporate acheté sur Russian Market, exploité sur plusieurs semaines pour cartographier et exfiltrer.
>
> Cette absence de 0-day est en soi un renseignement important. Elle place l'attaquant dans la catégorie **« cybercriminel sophistiqué avec moyens limités »** plutôt que **« APT étatique avec capacités offensives haut de gamme »**. Un APT étatique ciblant Vectris pour ses secrets aerospace/défense aurait probablement utilisé un vecteur plus discret (0-day sur edge device, spear-phishing sophistiqué), pas une chaîne commoditisée stealer log → IAB → exfiltrateur.
>
> Conséquence pour le rapport final : l'attribution pointe vers **criminalité organisée à motivation financière** plutôt que **espionnage étatique**. La DGSI confirme cette lecture. Les données exfiltrées pourraient finir entre les mains d'un acteur étatique in fine (si elles sont achetées sur IndustrialLeaks par un acheteur intermédiaire), mais le vol initial et sa commercialisation sont de profil cybercriminel.

---
