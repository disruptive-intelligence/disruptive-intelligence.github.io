---
title: Chapitre 23 — AdTech, tracking web,  fingerprinting et ADINT
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

mécanismes profonds

> **Niveau de posture (cf. Ch 2.6)** : ce chapitre concerne **tous les niveaux**. L’AdTech est l’adversaire avec lequel chaque lecteur a une interaction quotidienne, indépendamment de son threat model. Au N1, désactiver les MAID + uBlock Origin + DNS chiffré apporte un bénéfice immédiat. Au N2, ajout de la compartimentation des comptes et de Mullvad Browser. Au N3, ce chapitre devient essentiel par sa convergence avec l’ADINT (achats gouvernementaux de données publicitaires).

## 23.1 Pourquoi l’AdTech mérite son propre chapitre

L’industrie publicitaire numérique — l’**AdTech** — est, statistiquement, l’adversaire le plus actif de tout lecteur. Pas le plus dangereux dans une attaque ponctuelle, mais le plus _constant_ : à chaque page web chargée, à chaque application ouverte, à chaque session de streaming, des dizaines d’acteurs commerciaux observent, profilent, enchérissent sur ton attention en quelques dizaines de millisecondes.

Trois propriétés en font un sujet OPSEC à part entière :

- **Légalité majoritaire / Cadre commercial** : les données circulent souvent dans un cadre publicitaire présenté comme licite, sans intrusion technique directe. On ne te hacke pas, on t’achète. La formule est volontairement brutale : elle signifie que la menace vient souvent de l’achat légal ou semi-légal de données déjà collectées par l’écosystème publicitaire, plutôt que d’un piratage. Cette différence avec un malware est précisément ce qui rend la menace moins visible et plus durable.
- **Universalité** : à la différence d’un spyware mercenaire (qui cible des dizaines à quelques milliers de personnes par an), l’AdTech voit _des milliards_ d’utilisateurs en continu.
- **Convergence renseignement** : depuis 2020 environ, le pont entre données publicitaires et achats par agences gouvernementales est massivement documenté. C’est l’**ADINT** (Advertising Intelligence), traitée en 23.5.

Ce chapitre traite donc trois plans qui se complètent : l’**écosystème industriel** (acteurs, flux, identifiants) ; les **mécaniques techniques** (RTB, fingerprinting, tracking comportemental) ; et les **ponts vers le renseignement étatique**.

## 23.2 Architecture de l’écosystème AdTech

Le vocabulaire est barbare. Sans le maîtriser, on ne comprend pas où circulent les données.

**Acteurs centraux** :

- **Publisher** : l’éditeur du site ou de l’application qui vend de l’espace publicitaire (un média en ligne, un blog, une application gratuite, un service de streaming).
- **Annonceur** : l’organisation qui veut diffuser une publicité (constructeur automobile, grande distribution, éditeur de jeu mobile). Il paie pour atteindre une audience.
- **SSP (Supply-Side Platform)** : est la plateforme utilisée côté éditeur pour vendre automatiquement ses espaces publicitaires, qui gère l’inventaire publicitaire du publisher. Elle met aux enchères les emplacements disponibles. Acteurs principaux : Google Ad Manager, Magnite (ex-Rubicon Project), Index Exchange, OpenX, PubMatic, Xandr (Microsoft).
- **DSP (Demand-Side Platform)**  est la plateforme utilisée côté annonceur pour acheter automatiquement des emplacements publicitaires pour le compte des annonceurs. Acteurs : The Trade Desk, Google DV360, Amazon DSP, Yahoo, Adform, Criteo.
- **Ad Exchange** :  la place de marché automatisée où se rencontrent l’offre publicitaire des éditeurs et la demande des annonceurs. Google AdX, AppNexus (devenu Xandr), exchanges open-RTB-compatibles.
- **Les DMP/CDP** (_Data Management Platform_ / _Customer Data Platform_) servent à centraliser, segmenter et activer des données utilisateur pour mieux cibler les campagnes.
- **DMP (Data Management Platform)** : enrichit les profils avec des données tierces. Oracle BlueKai (retrait annoncé fin 2024), Adobe Audience Manager, Lotame.
- **CDP (Customer Data Platform)** : centralise les données _first-party_ d’un annonceur ou publisher. Segment (Twilio), Tealium, mParticle.
- **CMP (Consent Management Platform)** : sont les bandeaux et interfaces qui gèrent le consentement RGPD et qui demandent à l’utilisateur d’accepter ou refuser certains traitements publicitaires. Elles sont censées formaliser le consentement, mais elles peuvent aussi devenir un point de passage supplémentaire dans la chaîne du tracking. OneTrust, Didomi, Sourcepoint, Quantcast Choice.
- **Ad Server** : est le système qui décide quelle publicité afficher, à quel moment, à quel emplacement, et qui mesure l’affichage ou le clic. Google Campaign Manager, Adform, Equativ.
- **Verification / Brand Safety** : vérifie que la publicité a bien été affichée à un humain, dans un contexte adapté. IAS (Integral Ad Science), DoubleVerify, Moat (Oracle).
- **Data brokers** :  et fournisseurs de données enrichissent les profils avec des informations issues de sources multiples : navigation, achats, localisation, données déclaratives, programmes de fidélité, applications mobiles, fuites de données, registres publics. Agrégateurs tiers (LiveRamp, Acxiom, Experian, Equifax). Cf. Ch 6 — voisinage proche, recouvrement partiel.
- **Les SDK publicitaires** sont des composants intégrés dans les applications mobiles. Une application gratuite peut contenir plusieurs SDK tiers, chacun capable de collecter des signaux techniques, publicitaires ou comportementaux.

L’utilisateur final ne voit presque rien de cette chaîne. Il voit une publicité. En arrière-plan, plusieurs dizaines d’acteurs peuvent avoir participé à la décision d’affichage, à la mesure ou à l’enrichissement du profil.

**Header bidding vs waterfall** :

- _Waterfall_ : la SSP appelle les DSP les unes après les autres jusqu’à trouver un acheteur. Lent, moins rentable pour le publisher.
- _Header bidding_ : appel parallèle à plusieurs DSP simultanément. Plus rentable pour le publisher, mais structurellement plus de fuites de données — chaque DSP non-gagnante a quand même vu tes données et les conserve dans ses logs.

Le passage massif au header bidding dans les années 2017-2020 a _augmenté_ la dispersion du bidstream data. Ce qu’on appelait alors un « gain pour les éditeurs » est aussi mécaniquement un gain d’exposition pour les utilisateurs.

### 23.3 RTB et bidstream data : enchères publicitaires en temps réel

Le mécanisme central de l’AdTech moderne est le **RTB** (_Real-Time Bidding_), c’est-à-dire les enchères publicitaires en temps réel.

Lorsqu’un utilisateur ouvre une page web ou une application financée par la publicité, un espace publicitaire devient disponible. En quelques millisecondes, une enchère automatisée peut être déclenchée. Des informations sur l’utilisateur, le contexte et l’appareil sont transmises à différents acteurs publicitaires, qui décident s’ils veulent enchérir pour afficher une publicité.

Dans une logique marketing, ces données servent à cibler un segment : âge estimé, zone géographique, type d’appareil, langue, centres d’intérêt supposés ou contexte de navigation. Dans une logique ADINT, ces mêmes signaux peuvent devenir une source de renseignement. L’objectif n’est plus nécessairement de vendre un produit, mais de repérer un appareil, confirmer une présence, suivre une routine ou enrichir un profil.

Les signaux transmis peuvent inclure :

- l’adresse IP ou une localisation approximative ;
- le type d’appareil ;
- le système d’exploitation ;
- le navigateur ou l’application utilisée ;
- la langue et le fuseau horaire ;
- le contexte de la page ou de l’application ;
- un identifiant publicitaire mobile ;
- un cookie ou identifiant pseudonyme ;
- des segments d’intérêt supposés ;
- des informations de localisation plus ou moins précises selon le contexte ;
- des signaux issus de partenaires, courtiers ou plateformes tierces.

Ces informations sont souvent appelées **bidstream data**. Leur fonction officielle est publicitaire : permettre aux annonceurs de décider s’ils souhaitent acheter l’emplacement. Leur sensibilité vient du fait qu’elles peuvent révéler, directement ou indirectement, où se trouve un appareil, quelles applications il utilise, à quels moments il est actif et dans quels contextes il apparaît.

### 23.4 Pourquoi l’AdTech est un problème privacy

L’AdTech pose un problème privacy parce qu’elle repose sur une logique d’identification probabiliste et de corrélation continue.

L’utilisateur n’a pas besoin de donner son nom pour être suivi. Il suffit parfois qu’un identifiant stable, un fingerprint, une adresse IP, un identifiant publicitaire mobile ou un jeton opérateur soit réobservé dans différents contextes.

Un signal isolé peut sembler anodin. Mais une répétition de signaux permet de reconstruire des habitudes :

- lieux de vie ;
- lieux de travail ;
- horaires d’activité ;
- centres d’intérêt ;
- applications utilisées ;
- sites consultés ;
- sensibilité politique ou religieuse supposée ;
- situation familiale ;
- niveau socio-économique ;
- état de santé probable ;
- déplacements réguliers.

L’AdTech ne produit donc pas seulement de la publicité ciblée. Elle produit des profils.
## 23.5 Cycle de vie d’une impression et bidstream data

Voici ce qui se passe à chaque chargement de page financée par la publicité :

1. **T+0 ms** : tu charges une page (par exemple un article de presse).
2. **T+5–20 ms** : le JavaScript adtech démarre. Il lit les cookies first-party, le contexte de la page, identifie le navigateur, peut commencer le fingerprinting (cf. 23.10).
3. **T+20 ms** : envoi d’une _bid request_ au SSP. Cette requête contient typiquement :
    - IP source (et donc géolocalisation approximative à la ville voire au quartier) ;
    - User-Agent, taille d’écran, langue, fuseau horaire ;
    - Cookie ID (ou un identifiant de remplacement, cf. 23.4) ;
    - URL de la page, mots-clés contextuels, position de l’emplacement publicitaire ;
    - sur mobile : MAID (IDFA/AAID), modèle d’appareil, app ID.
4. **T+30–80 ms** : la SSP propage la bid request à 10 à 30 DSP en parallèle (header bidding). Chaque DSP peut interroger sa DMP pour enrichir le profil.
5. **T+80–120 ms** : les DSP retournent leurs enchères. La SSP désigne le gagnant.
6. **T+120–200 ms** : la créative est servie, le pixel d’impression est chargé, l’impression est validée.

**Conséquence opérationnelle** : à _chaque_ page chargée, **30+ acteurs voient tes données** — pas seulement le DSP qui gagne l’enchère. Les _losers_ gardent les données dans leurs logs pour segmentation, modélisation, identity resolution, revente. C’est le **bidstream data leak structurel**. En pratique, l’industrie l’opère sous couvert de consentement utilisateur via des CMP, mais sa conformité réelle dépend de la validité du consentement, des finalités déclarées, de la durée de conservation et des responsabilités de chaque acteur. C’est précisément l’un des points les plus contestés de l’AdTech européenne.

Sur 24 heures, un utilisateur actif peut déclencher des centaines, voire davantage, de bid requests selon ses usages web, mobiles et CTV, et expose ses signaux à plusieurs centaines de serveurs adtech distincts. Multiplié par la durée d’une vie numérique active, le volume cumulé est astronomique.

Ce flux de bid requests produit ce qu’on appelle les **bidstream data** : des données techniques, contextuelles et comportementales générées à chaque enchère publicitaire. Leur finalité officielle est marketing, mais leur valeur réelle dépasse largement la publicité : elles deviennent une matière première pour la corrélation, le profilage et, dans certains cas, l’ADINT.

## 23.6 First-party, third-party et illusion du consentement

Une donnée **first-party** est collectée directement par le service que l’utilisateur utilise : par exemple, un média qui observe les articles lus sur son propre site.

Une donnée **third-party** est collectée ou exploitée par un tiers : régie publicitaire, tracker, SDK, data broker, plateforme d’analyse, outil de mesure.

La frontière est devenue moins lisible. Beaucoup de sites et d’applications utilisent des dizaines de partenaires tiers. L’utilisateur croit souvent interagir avec un seul service, alors qu’il alimente indirectement une chaîne d’acteurs.

Le consentement est censé redonner du contrôle. En pratique, les bandeaux de consentement sont souvent complexes, asymétriques, fatigants ou conçus pour pousser à l’acceptation. Le problème n’est donc pas seulement technique, mais aussi ergonomique et politique : un consentement obtenu par friction, fatigue ou obscurité n’a pas la même valeur qu’un consentement réellement éclairé.

## 23.7 Identifiants publicitaires

cookies, MAID, hashed email, identity resolution

Historiquement, le web publicitaire s’est largement appuyé sur les **cookies tiers**. Un cookie tiers permettait à un acteur publicitaire de reconnaître un navigateur sur plusieurs sites différents. Les navigateurs modernes les bloquent de plus en plus, ou les rendent moins efficaces.

**Cookies tiers** : en déclin. Bloqués par défaut sur Safari (ITP depuis 2017), Firefox (ETP depuis 2019), Brave. Pour Chrome, Google a successivement annoncé leur dépréciation, puis a reculé en juillet 2024, et a confirmé en avril 2025 le maintien d’une approche par « choix utilisateur » sans dépréciation par défaut (cf. 23.6).

**Cookies first-party détournés** : utilisés pour profiler et partagés entre acteurs via des techniques de contournement (CNAME cloaking, server-side tracking via sous-domaine, etc.). De plus en plus courants pour compenser la perte des cookies tiers, et juridiquement plus difficiles à attaquer parce qu’ils semblent légitimes.

**MAID (Mobile Advertising ID)** :
Sur mobile, l’équivalent fonctionnel est l’**identifiant publicitaire mobile**, souvent appelé **MAID** (_Mobile Advertising ID_). Sur iOS, on parle d’IDFA ; sur Android, d’AAID. 
Ces identifiants sont conçus pour permettre le suivi publicitaire entre applications sans utiliser directement le nom civil de l’utilisateur. Mais cette pseudonymisation a des limites. Un identifiant publicitaire observé régulièrement la nuit dans une zone résidentielle, en journée dans un bâtiment professionnel, puis ponctuellement dans un lieu sensible — manifestation, lieu de culte, bâtiment administratif, base militaire, cabinet d’avocat, rédaction, ambassade — peut parfois être rattaché à une personne ou à une fonction avec un niveau de confiance significatif..

- **IDFA** (iOS) : désactivable depuis iOS 14.5 (App Tracking Transparency, ATT). En pratique, une majorité importante des utilisateurs iOS refuse le suivi lorsqu’une invite ATT s’affiche, ce qui a fortement réduit l’accès effectif à l’IDFA depuis 2021. Effet massif sur les revenus publicitaires mobiles à partir de 2021-2022, notamment pour Meta (pertes estimées à plusieurs milliards de dollars annuels).
- **AAID** (Android) : encore actif par défaut sur Android stock. Désactivable manuellement (Paramètres → Confidentialité → Annonces → Supprimer l’ID publicitaire). Google a introduit un Privacy Sandbox mobile en 2024-2025, mais l’AAID reste central pour la majorité des apps.

**Hashed Email** : ton email transformé en SHA-256 (ou autre fonction de hachage). Présenté comme « pseudonyme » mais en réalité c’est un identifiant déterministe et stable. L’espace des emails effectivement utilisés est fini et largement connu — tout courtier disposant d’une grande base peut faire la jointure trivialement. Vecteur dominant 2023-2026 pour les _people-based identifiers_.

**Identity resolution** : les _cookies tiers_ de nouvelle génération qui prennent le relais.

- **LiveRamp RampID** : identifiant déterministe lié aux emails hachés. Présent dans les principaux DSP et CDP.
- **The Trade Desk Unified ID 2.0 (UID2)** : standard ouvert porté par The Trade Desk, basé sur emails hachés. Adoption massive côté DSP en 2023-2025.
- **ID5** : société européenne, identifiant probabiliste agrégant plusieurs signaux.
- **Yahoo ConnectID, Criteo ID, Lotame Panorama ID, Merkle Merkury ID**, et autres.

Ces identifiants reposent sur ton email (ou ton numéro de téléphone) que tu as donné à des sites — et qui circule maintenant comme un _cookie permanent_ à travers l’écosystème, indépendamment de tout navigateur ou appareil.

**Conversion API (CAPI) côté serveur** : flux server-to-server qui contournent le navigateur.

- **Meta CAPI** : les marchands envoient les conversions (achats, inscriptions, etc.) directement aux serveurs Meta, sans passer par le navigateur. Bypass des bloqueurs de publicité et des restrictions navigateur. Déploiement explosif depuis 2021 en réponse à ATT.
- **Google Enhanced Conversions** : équivalent.
- **TikTok Events API, LinkedIn CAPI** : idem.

Ces flux sont structurellement invisibles côté utilisateur. Bloquer les trackers dans son navigateur ne suffit plus : ce qui circule entre le serveur du marchand et celui de Meta ou Google ne passe pas par ton appareil.

### 23.8 AdTech, data brokers et plateformes

L’AdTech ne fonctionne pas seule. Elle s’articule avec trois autres écosystèmes.

D’abord, les **plateformes** : Google, Meta, TikTok, Amazon, Microsoft, Apple. Elles disposent de données first-party massives et de capacités de ciblage internes. Elles n’ont pas toujours besoin de cookies tiers, car elles contrôlent directement l’environnement utilisateur.

Ensuite, les **data brokers** : ils agrègent des données issues de multiples sources et revendent des segments, scores ou profils. Ils peuvent enrichir la publicité, mais aussi alimenter l’assurance, le crédit, le recrutement, l’investigation privée ou la surveillance commerciale.

Enfin, les **applications mobiles** : beaucoup d’applications gratuites intègrent des SDK publicitaires et analytiques. Ces SDK peuvent collecter des signaux très sensibles : localisation, modèle d’appareil, identifiant publicitaire, événements d’usage, horaires, langue, réseau, parfois données déclaratives.

C’est cette combinaison qui rend le modèle si robuste : même si un canal de tracking devient moins efficace, un autre prend le relais.

## 23.10 ADINT

De la publicité au renseignement, exploitation opérationnelle des données publicitaires

L’**ADINT** (_Advertising Intelligence_) apparaît lorsque les mécanismes de l’écosystème publicitaire sont utilisés comme source de renseignement plutôt que comme support marketing. Les mêmes bid requests, les mêmes MAID, les mêmes bases de localisation qui servent à cibler une publicité peuvent servir à **identifier, suivre, corréler ou caractériser une personne, un groupe ou un lieu**.

Dans une logique marketing, ces données servent à vendre une publicité. Dans une logique ADINT, elles peuvent servir à identifier un appareil, suivre une routine, cartographier une présence dans un lieu sensible, enrichir un profil ou préparer une attaque ciblée.

La différence n’est pas toujours dans la donnée collectée, mais dans l’usage qui en est fait. Un identifiant publicitaire mobile, une donnée de localisation ou une bidstream data peuvent être banals dans un tableau de bord marketing, mais sensibles dans les mains d’un acteur qui cherche à identifier une source, un diplomate, un militaire, un activiste ou un journaliste.

L’ADINT illustre une idée centrale en OPSEC : une donnée collectée pour une finalité commerciale peut devenir exploitable pour une finalité de renseignement.

* géolocaliser ou suivre un appareil à partir de signaux publicitaires ;
* identifier des routines : domicile, travail, déplacements, lieux fréquentés ;
* cartographier des présences dans un lieu donné : institution, site militaire, événement politique, manifestation, lieu de culte ;
* déduire des attributs sensibles à partir des applications utilisées ou des lieux visités ;
* enrichir un profil avant une attaque ciblée : phishing, harcèlement, surveillance, compromission ;
* diffuser une publicité piégée ou rediriger vers un site malveillant dans certains scénarios de malvertising ou de watering hole.

Le sujet est devenu massif à partir de 2020. Le sénateur démocrate **Ron Wyden** (Oregon), membre du Senate Intelligence Committee, a été le premier élu américain à documenter publiquement, par lettres officielles aux agences, l’achat de données de localisation auprès de courtiers privés par DHS, ICE, IRS, FBI, DEA, US Military et d’autres entités fédérales. Sa série d’investigations 2020-2025 a fait sortir publiquement l’ampleur du phénomène.
### 23.10.1 Le contournement juridique au cœur de l’ADINT

Aux États-Unis, l’arrêt **Carpenter v. United States (2018)** de la Cour suprême a établi que les forces de l’ordre doivent obtenir un mandat pour accéder aux Cell Site Location Information (CSLI) c’est-à-dire les données de localisation cellulaire détenues par les opérateurs téléphoniques.

**Mais Carpenter ne couvre pas les achats de données auprès de brokers privés.** Les agences ont rapidement identifié ce contournement : pourquoi demander un mandat pour obtenir des données auprès de Verizon, AT&T ou T-Mobile, alors qu’on peut acheter des données similaires (parfois plus précises) auprès de courtiers qui les ont collectées via des SDK publicitaires dans des applications mobiles ?

Le résultat : entre 2017 et 2024, plusieurs dizaines de millions de dollars de contrats publics américains ont été identifiés pour l’achat de données de localisation provenant de l’écosystème adtech. Le sénateur Wyden a introduit le **Fourth Amendment Is Not For Sale Act (FANFSA)** pour fermer ce contournement, voté à la Chambre en 2024 mais bloqué au Sénat à la rédaction de ce cours.

En Europe, le cadre RGPD diffère structurellement : le traitement à des fins de renseignement par les autorités publiques est encadré par des directives sectorielles (LED — Law Enforcement Directive) et par les législations nationales sur le renseignement. Mais le problème n’est pas absent, des zones grises persistent, notamment sur les transferts hors UE et sur le statut des achats par des services de renseignement nationaux auprès de courtiers américains. Les achats, transferts, recoupements ou traitements secondaires de données publicitaires par des acteurs publics ou privés restent difficiles à documenter, notamment lorsque les données proviennent de courtiers non européens, de places de marché opaques ou de chaînes de sous-traitance internationales.

**A — Exploitations observées : ce que les données permettent concrètement**
### 23.10.2 Démonstration journalistique - Le Monde

personnels sensibles français ré-identifiés par données publicitaires
Source : https://www.lemonde.fr/pixels/article/2025/12/10/espions-policiers-ou-militaires-d-elite-francais-trahis-par-les-donnees-publicitaires-de-leurs-smartphones_6656694_4408996.html

En décembre 2025, **Le Monde** a publié une enquête montrant que des données publicitaires géolocalisées permettaient d’identifier ou de suivre des personnels français particulièrement sensibles : agents liés au renseignement, policiers spécialisés, militaires d’élite, membres de dispositifs de protection, salariés de l’industrie de défense ou personnels liés à des sites critiques.

L’intérêt de ce cas est qu’il ne repose pas sur une compromission technique. Les téléphones n’ont pas été piratés. Les applications n’ont pas forcément été détournées de manière visible. L’exposition provient de données déjà collectées par l’écosystème publicitaire : identifiants publicitaires, points de localisation, traces d’usage d’applications, horaires et répétition des présences dans certains lieux.

L’enquête illustre un principe central : il n’est pas nécessaire de connaître immédiatement le nom civil d’une personne pour l’identifier. Un appareil observé régulièrement la nuit dans une zone résidentielle, en journée près d’un site sensible, puis à intervalles réguliers dans certains lieux professionnels ou institutionnels, peut être rattaché à une personne, une fonction ou une unité avec un niveau de confiance élevé.

Le risque dépasse donc la vie privée individuelle. Il touche la sécurité des missions, la protection des agents, la confidentialité des sites, la sûreté des familles et la sécurité opérationnelle des institutions. Une donnée présentée comme pseudonyme dans un contexte publicitaire peut devenir identifiante lorsqu’elle est croisée avec des lieux, des horaires et des routines.

Ce cas français est particulièrement important pour un cours OPSEC : il montre que l’ADINT ne concerne pas seulement les États-Unis ou les courtiers américains. Des personnels sensibles européens peuvent également être exposés par des données commerciales de localisation, parfois sans en avoir conscience.
### 23.10.3 Cas d'exploitation - Reuters

militaires américains ciblés via données commerciales de localisation
Source : https://www.reuters.com/business/media-telecom/pentagon-says-us-military-personnel-are-reportedly-being-targeted-using-location-2026-05-28/

En mai 2026, **Reuters** a rapporté que l’US Central Command avait reçu des signalements selon lesquels des adversaires exploitaient des données commerciales de localisation pour surveiller ou cibler du personnel militaire américain déployé en zone d’opération.

Ce cas marque un seuil supplémentaire. Il ne s’agit plus seulement d’identifier des personnes sensibles ou de reconstruire leurs routines. Dans un contexte militaire, les données de localisation peuvent contribuer à une menace physique : repérer des rassemblements de militaires, identifier des déplacements récurrents, localiser des lieux de passage, observer des pauses logistiques, suivre des rotations ou déduire des patterns of life exploitables.

Là encore, le point critique est l’absence de piratage. L’adversaire n’a pas nécessairement besoin de compromettre les téléphones. Il peut exploiter des données issues d’applications, de SDK publicitaires, de courtiers de localisation ou de chaînes de revente commerciales. Ce qui était initialement collecté pour mesurer, cibler ou monétiser une audience devient une source de renseignement opérationnel.

Dans un théâtre de guerre ou une zone de tension, ce basculement change la nature du risque. Une fuite de localisation n’est pas seulement une atteinte à la privacy : elle peut contribuer à la préparation d’une attaque, à du contre-renseignement, à la surveillance d’un personnel exposé, voire à du ciblage cinétique.

Ce cas confirme que l’ADINT doit être pensée comme une question de sécurité opérationnelle, pas seulement comme une question de conformité publicitaire ou de protection des données personnelles.
### 23.10.4 Lecture croisée de la privacy au risque physique

Les cas Le Monde et Reuters montrent deux niveaux complémentaires du même problème.

Le premier niveau est la **ré-identification** : à partir de données publicitaires, il devient possible de relier un appareil à une personne, une fonction, un domicile, un lieu de travail ou une routine. C’est ce que montre le cas français : les données publicitaires peuvent exposer des personnels sensibles, leurs lieux de vie et leurs habitudes.

Le second niveau est le **ciblage opérationnel** : lorsque les mêmes données sont utilisées dans un contexte militaire, conflictuel ou hostile, elles peuvent aider un adversaire à préparer une surveillance, une intimidation, une attaque physique ou une opération de renseignement.

La chaîne de risque est donc la suivante :

1. une application mobile collecte des signaux techniques ou de localisation ;
2. ces signaux sont transmis à des SDK, plateformes publicitaires ou courtiers ;
3. les données sont agrégées, revendues ou rendues accessibles via des intermédiaires ;
4. un acteur tiers peut isoler un lieu sensible, suivre un appareil ou reconstruire une routine ;
5. l’appareil devient un capteur involontaire au profit d’un adversaire.

Ces cas imposent une conclusion OPSEC simple : pour les profils sensibles, il ne suffit pas de protéger le contenu des communications. Il faut aussi empêcher que les appareils révèlent des présences, des trajets, des horaires, des lieux sensibles et des patterns of life.
### 23.10.5 Du cas d’usage au marché de l’ADINT

Les cas Le Monde et Reuters montrent les **effets observables** de l’ADINT : ré-identification de personnes sensibles, reconstruction de routines, exposition de domiciles, suivi de lieux sensibles et, dans certains contextes, ciblage opérationnel.

La suite de cette section change d’angle. Elle ne décrit plus seulement ce que les données permettent de faire, mais **qui rend cette exploitation possible** : courtiers de localisation, plateformes d’analyse, sociétés d’intelligence privée, fournisseurs de données et outils commerciaux capables d’agréger des signaux issus de l’écosystème publicitaire.

Il faut donc distinguer deux niveaux :

- **les cas d’exploitation** : ils montrent l’impact réel ou démontrable des données publicitaires lorsqu’elles sont utilisées pour identifier, surveiller ou cibler ;
- **les acteurs d’industrialisation** : ils collectent, achètent, agrègent, retraitent, vendent ou rendent consultables ces données à grande échelle.

**B — Acteurs d’industrialisation : qui collecte, agrège et monétise**
### 23.10.6 Acteurs d’industrialisation : Babel Street / Locate X

**Babel Street** est une société d’analyse de données fondée en 2014, basée en Virginie. Son produit phare **Locate X** agrège des données de localisation provenant de SDK adtech intégrés dans des applications mobiles, et permet à des analystes (typiquement gouvernementaux) de retracer les déplacements d’appareils dans le temps et l’espace.

Documenté pour la première fois par le journaliste Joseph Cox (Motherboard, puis 404 Media) en 2020 : Locate X était utilisé par CBP (US Customs and Border Protection), ICE (Immigration and Customs Enforcement), Secret Service, US Marshals, US Army, **sans mandat judiciaire**.

En 2024, 404 Media et l’EFF ont publié des enquêtes documentant que Locate X reste accessible à des acteurs n’ayant pas toujours fait l’objet de vérifications strictes, et qu’il a été utilisé pour démontrer publiquement la capacité à retracer :

- les déplacements d’un Marine vers les abords d’une base classifiée ;
- les habitudes hebdomadaires d’un juge fédéral ;
- les visites de personnes vers des cliniques d’avortement, dans un contexte post-arrêt Dobbs où ces déplacements sont devenus pénalement sensibles dans plusieurs États.

L’objectif éditorial de ces démonstrations journalistiques était de montrer publiquement qu’un outil officiellement commercial permet à toute partie disposant des bons accès d’atteindre des données de surveillance qui requerraient autrement un mandat judiciaire.

### 23.10.7 Acteurs d’industrialisation : Anomaly Six (A6)

**Anomaly Six**, société de Virginie fondée par d’anciens membres de la communauté du renseignement américaine, opère dans un registre similaire : agréger des données de SDK adtech mobiles à grande échelle.

L’investigation marquante est celle publiée par le **Wall Street Journal en avril 2022**. Lors d’une démonstration à des journalistes, A6 a montré sa capacité à :

- géolocaliser un téléphone _à Moscou_ (vraisemblablement un téléphone russe) ;
- tracer un appareil dont les déplacements correspondaient à ceux d’un employé d’une agence de renseignement américaine ;
- le tout en exploitant **environ trois milliards de mouvements** d’appareils par jour dans sa base.

A6 est l’exemple paradigmatique de l’« intelligence-as-a-service » : une entreprise commerciale qui vend à des États (ou à d’autres entreprises) ce qui aurait autrefois nécessité une agence de renseignement entière. Le tout sans hacker quoi que ce soit — purement par exploitation de l’écosystème adtech légal.

### 23.10.8 Acteurs d’industrialisation

Venntel / Gravy Analytics et sanction FTC 2024

**Venntel** est une filiale de **Gravy Analytics**, société de location data agrégeant les flux de centaines d’applications mobiles via SDK. Vendait géolocalisation à CBP, ICE, DEA, IRS, FBI, Département de la Défense américain.

L’IRS Inspector General (TIGTA) a publié en 2023 un rapport critique sur les achats sans mandat. La FTC a sanctionné Gravy Analytics et sa concurrente **Mobilewalla** par consent order en décembre 2024 — première sanction publique majeure contre des location brokers en lien avec le contournement de mandats.

**Janvier 2025 — la fuite Gravy Analytics** : un attaquant a exfiltré des dizaines de téraoctets de logs de localisation depuis l’infrastructure de Gravy. Révélation publique par 404 Media. Les données exposées permettaient de cartographier les déplacements de millions d’appareils, et d’identifier les apps sources — révélant par effet de bord la liste partielle des partenaires SDK de Gravy : applications météo, jeux mobiles, dating, applications religieuses ou de prière, traduction, fitness, et d’autres catégories grand public.

Cet incident a deux portées :

1. confirmer empiriquement que les données circulant dans l’adtech sont sensibles et identifiantes — pas seulement « pseudonymes » ;
2. démontrer que ces données sont elles-mêmes mal sécurisées chez les courtiers, exposant les utilisateurs à un risque double : commercial _et_ en cas de compromission du broker.

### 23.10.9 Acteurs d’industrialisation

X-Mode / Outlogic et la sanction FTC 2024

**X-Mode Social** était l’un des principaux brokers de location data SDK. Bannie par Apple et Google en décembre 2020 après une enquête de Motherboard révélant des contrats avec des sous-traitants militaires et des ventes à des organismes gouvernementaux. Rebrand en **Outlogic** en 2021, qui a continué l’activité.

**Janvier 2024 — sanction FTC contre X-Mode/Outlogic** : _première fois_ qu’une autorité de régulation interdisait à un broker de vendre des données de localisation sensibles (visites à des cliniques de santé reproductive, lieux de culte, manifestations, locaux syndicaux, etc.). Consent order incluant l’effacement de catalogues entiers de données et l’interdiction permanente de vendre certaines catégories de localisation sensible.

Cette sanction a marqué un tournant régulatoire, mais l’écosystème reste massif et la majorité des acteurs continuent d’opérer.

### 23.10.10 Synthèse des cas — deux dimensions de l’ADINT

Les cas Le Monde et Reuters montrent la **dimension opérationnelle** de l’ADINT : les données publicitaires peuvent exposer des agents, militaires, policiers, personnels de renseignement, cadres de l’industrie de défense ou salariés de sites critiques. Elles permettent de reconstruire des domiciles probables, des trajets, des habitudes, des lieux fréquentés et des patterns of life. Dans certains contextes, cette exposition peut devenir un risque physique.

Les cas Babel Street, Anomaly Six, Venntel/Gravy Analytics et X-Mode/Outlogic montrent la **dimension industrielle** de l’ADINT : des sociétés collectent, agrègent, enrichissent et commercialisent des données issues d’applications ordinaires, de SDK publicitaires, de bid requests, de MAID et de courtiers. Elles transforment des traces dispersées en outils de recherche, de surveillance, de géolocalisation ou d’analyse comportementale.

La chaîne complète est donc la suivante :

1. des applications banales collectent des signaux techniques, publicitaires ou de localisation ;
2. ces signaux alimentent des SDK, exchanges, courtiers ou plateformes d’analyse ;
3. des entreprises spécialisées agrègent et rendent ces données exploitables ;
4. des clients publics, privés ou para-publics peuvent y accéder ;
5. un adversaire peut alors identifier une personne, suivre une routine, cartographier un lieu sensible ou préparer une action ciblée.

Le point critique n’est pas la précision d’une donnée isolée. C’est l’agrégation dans le temps. Une localisation ponctuelle peut être anodine ; des centaines de localisations répétées deviennent une signature de vie.

### 23.10.11 Profils particulièrement exposés et limites des contre-mesures

Tous les utilisateurs peuvent être concernés par l’ADINT, mais certains profils sont structurellement plus sensibles : journalistes d’investigation et sources ; diplomates, militaires, policiers, magistrats ; dirigeants d’entreprise et cadres exposés ; activistes et opposants politiques ; chercheurs en cybersécurité ; personnels d’ONG travaillant dans des zones sensibles ; personnes victimes de harcèlement ou d’un adversaire de proximité.

Le risque devient particulièrement important lorsque l’appareil personnel est emporté dans des lieux sensibles. Un téléphone contenant de nombreuses applications gratuites financées par la publicité peut devenir un traceur involontaire, sans qu’il soit nécessaire de compromettre techniquement l’appareil.

### 23.10.12 Pourquoi l'ADINT est difficile à contrer

L’ADINT est difficile à neutraliser parce qu’elle exploite un écosystème **légal, massif et opaque**. Les acteurs publicitaires collectent déjà ces données pour le ciblage commercial. Des acteurs spécialisés peuvent ensuite s’insérer dans cette chaîne comme annonceurs, intermédiaires, courtiers ou prestataires d’analyse.

Le problème ne vient donc pas uniquement d’un malware ou d’une intrusion technique classique. Il vient aussi du modèle économique lui-même : applications financées par la publicité, SDK tiers, courtiers de données, enchères en temps réel, revente et agrégation de signaux.

Il n’existe pas de protection technique clé en main permettant de neutraliser totalement ce risque ; les mesures disponibles relèvent de la **réduction d’exposition**, de la **compartimentation** et, pour les profils les plus exposés, du **contrôle physique des appareils** (cf. 23.14). C’est précisément l’illustration que **ce n’est pas toujours une donnée isolée qui identifie, mais la répétition et la corrélation des signaux**.

## 23.11 Privacy Sandbox, cookies tiers et recomposition post-cookie

Annoncée en 2019, la **Privacy Sandbox** de Google se présentait comme la réponse technologique au déclin des cookies tiers. Plutôt que tracker via des cookies cross-site, Chrome devait proposer des API on-device :

- **Topics API** : Chrome catégorise ton historique en « topics » (intérêts : sport, cuisine, voyages, etc., environ 380 catégories) et expose chaque semaine 3-5 topics aux sites.
- **Protected Audience API** (ex-FLEDGE) : enchères publicitaires _on-device_ basées sur tes « interest groups ».
- **Attribution Reporting API** : mesure des conversions sans tracking cross-site, avec bruit différentiel.

**La trajectoire 2024-2025 est celle d’un abandon partiel de l’ambition initiale** :

- **Juillet 2024** : Google annonce que Chrome **ne déprécie plus les cookies tiers par défaut**. La proposition est de basculer vers un choix utilisateur, sans précision sur la forme exacte.
- **Avril 2025** : Google confirme officiellement le maintien de cette approche « choix utilisateur ». Aucune dépréciation des cookies tiers n’est planifiée. Les API Privacy Sandbox restent disponibles en coexistence.
- **Octobre 2025** : Google annonce le **retrait progressif de plusieurs API Privacy Sandbox** — notamment Topics, Protected Audience et Attribution Reporting — pour faible adoption industrielle. D’autres briques de la Sandbox (notamment **CHIPS** pour les cookies partitionnés et **FedCM** pour la fédération d’identité) restent maintenues. La transition annoncée en 2019 comme une refondation de la publicité web se solde donc en abandon partiel de son ambition initiale, plutôt qu’en démantèlement complet.

Cette trajectoire est instructive en soi. Elle montre que **les standards de privacy poussés par les acteurs dominants restent dépendants de leurs intérêts commerciaux**. L’industrie publicitaire a refusé d’adopter massivement Privacy Sandbox, jugée trop limitante ; les autorités antitrust (notamment la CMA britannique) ont par ailleurs maintenu une pression critique sur le risque de renforcement du monopole Google. Résultat net : les cookies tiers persistent sur Chrome (environ 60-65 % du marché web mondial), l’identity resolution par hashed email progresse (cf. 23.4), et le fingerprinting reste un vecteur structurel.

**Critiques permanentes de la Privacy Sandbox** :

- **EFF, Brave, Mozilla** : Topics API peut servir de signal supplémentaire dans le fingerprint, et la catégorisation n’est pas anonyme à l’usage. Brave et Mozilla n’ont jamais implémenté Topics côté navigateur.
- **CMA (Competition and Markets Authority, UK)** : enquête depuis 2021 sur le risque que Privacy Sandbox renforce la position dominante de Google dans la publicité numérique.
- **Apple** : a refusé d’adopter ces standards, préférant son propre modèle (ITP, ATT, Private Relay).

**Pour l’utilisateur** : les API Privacy Sandbox encore actives peuvent être désactivées dans les paramètres Chrome (Paramètres → Confidentialité et sécurité → Confidentialité des publicités). Sur Brave, désactivées par défaut. Sur Firefox et Safari, non implémentées.

## 23.12 SDK AdTech in-app mobile

Le tracking mobile diffère structurellement du tracking web. Sur le web, du JavaScript est injecté dans la page et peut être bloqué par uBlock Origin, NoScript, ou des configurations navigateur. Sur mobile, le tracking se fait via des **SDK natifs** embarqués dans l’application — du code compilé qui s’exécute avec les permissions de l’application elle-même.

**Top SDK adtech mobiles** :

- **AppsFlyer, Adjust, Singular, Branch** : attribution marketing (savoir d’où vient un utilisateur, mesurer l’efficacité d’une campagne).
- **OneSignal** : notifications push, intègre du tracking comportemental.
- **Mixpanel, Amplitude** : product analytics, avec capacités de fingerprinting et de cohort tracking.
- **Firebase Analytics / Google Analytics for Firebase** : par défaut dans la plupart des apps Android et iOS.
- **Meta SDK** : intégré dans des millions d’apps pour authentification Facebook + tracking conversion.
- **Smaato, Vungle, ironSource, AppLovin** : SDK de monétisation publicitaire.

Audit : **Exodus Privacy** (cf. Ch 15) liste les trackers présents dans une app Android donnée. Une application gratuite typique en intègre 5 à 30. Une application météo standard peut en intégrer plus de 20. Un jeu mobile « free-to-play » dépasse souvent 40 trackers actifs.

**iOS** : ATT (App Tracking Transparency) a réduit l’IDFA effectif, mais l’attribution probabiliste via fingerprint (SKAdNetwork est l’API officielle Apple, mais des techniques de probabilistic matching contournent partiellement le refus ATT) compense pour les annonceurs.

**Android** : AAID toujours actif par défaut sur Android stock. Le Privacy Sandbox for Android (annoncé 2022, déploiement progressif 2024-2025) propose des équivalents Topics API / Protected Audience API ; son avenir suit celui de la Privacy Sandbox web (cf. 23.6) et reste incertain à la rédaction.

**GrapheneOS** : pas de Google Play Services privilégiés, MAID minimisé, permission réseau granulaire par app, isolation forte entre apps via profils utilisateur. La plateforme mobile la mieux durcie contre les SDK adtech à 2026.

## 23.13 CTV, Smart TV, ACR et retail media

L’AdTech ne se limite plus au web et au mobile. Trois fronts récents méritent attention.

**CTV (Connected TV)** : les applications de streaming (Netflix avec ads, Prime Video, Hulu, Disney+, YouTube TV, Pluto TV, Tubi) sont devenues des supports publicitaires majeurs depuis 2022-2023. La CTV ad voit typiquement :

- IP du foyer ;
- compte utilisateur (identifié et nominatif) ;
- modèle de TV ou device (Chromecast, Apple TV, Roku, Fire Stick) ;
- historique de visionnage dans l’app ;
- sur certaines plateformes, des MAID dédiés CTV (Roku Advertising Identifier, Samsung TIFA, Vizio IFA, etc.).

**ACR (Automatic Content Recognition)** : la TV elle-même regarde ce que toi tu regardes. Elle capture régulièrement des images de l’écran, les compare à une base de fingerprints visuels, et identifie le contenu joué — y compris depuis une console de jeu, une clé USB, ou la TNT. Acteurs : **Samba TV, Inscape** (Vizio), **iSpot.tv**, **TVision**, **VIDAA** (Hisense).

**Cas FTC vs Vizio (2017)** : Vizio condamné à 2,2 M$ d’amende pour avoir collecté de l’ACR sans consentement et l’avoir revendu à des courtiers. Pratique persistante chez la plupart des fabricants ; généralement désactivable mais activée par défaut.

**Désactiver l’ACR** :

- Samsung : Réglages → Général → Confidentialité → Services Smart Hub → désactiver « Données de visionnage ».
- LG : Réglages → Général → À propos → Politiques d’utilisation et de confidentialité → Refuser.
- Vizio : Réglages → Système → Reset & Admin → Smart Interactivity → Off.
- Roku : Réglages → Confidentialité → Smart TV Experience → désactiver « Use info from TV inputs ».

Pour profils sensibles : préférer une TV utilisée comme moniteur passif (HDMI uniquement, sans connexion réseau), avec un Apple TV ou un Nvidia Shield séparé qui peut être plus facilement audité.

**Retail Media Networks** : l’AdTech qui colonise les enseignes physiques.

- **Amazon Ads** : plus grand retail media network mondial, croissance fulgurante depuis 2021.
- **Walmart Connect, Target Roundel, Kroger Precision Marketing** (US).
- **Carrefour Links, Casino RelevenC** (FR, déploiement croissant), Tesco Media, Sainsbury’s Nectar360 (UK).

Le modèle : le distributeur (qui sait _exactement_ ce que tu achètes via ta carte de fidélité) revend des segments d’audience à des marques, qui peuvent alors te toucher en publicité sur le site du distributeur _et_ via des partenariats off-site. Ton achat de paracétamol chez Carrefour peut influencer la publicité que tu vois ailleurs sur le web — non pas via le tracking web classique, mais via la jointure cookie/email côté distributeur.

**Pour l’utilisateur** : la carte de fidélité, longtemps perçue comme une question commerciale anodine, est devenue un identifiant adtech majeur. Pour profils sensibles : carte de fidélité au pseudonyme, ou pas de carte du tout, ou paiement cash systématique pour les achats à isoler (cf. Ch 32).

## 23.14 Le tracking n’est plus seulement les cookies

L’ère des cookies tiers se ferme (Chrome retarde mais Safari et Firefox les bloquent par défaut). En parallèle, le fingerprinting est devenu massif. Et l’identifiant publicitaire mobile reste actif.
Contrairement au cookie, qui est un fichier stocké localement et que l’utilisateur peut supprimer ou bloquer, le fingerprinting repose sur des caractéristiques plus structurelles de l’environnement : navigateur, système d’exploitation, résolution, paramètres régionaux, rendu graphique, configuration matérielle. L’utilisateur ne “supprime” donc pas son fingerprint comme il supprime un cookie ; il doit soit réduire les signaux collectables, soit se fondre dans un groupe d’utilisateurs au profil standardisé.
Le retour du fingerprinting s’inscrit dans la recomposition de l’AdTech post-cookies tiers. À mesure que les navigateurs limitent les cookies tiers, certains acteurs publicitaires cherchent des signaux alternatifs plus difficiles à bloquer. Le risque est de remplacer un tracking visible, stocké localement et partiellement contrôlable par l’utilisateur, par un tracking plus diffus, plus passif et moins maîtrisable.

## 23.15 Tracking par infrastructure opérateur : cas Utiq

Le développement récent des initiatives publicitaires fondées sur des signaux opérateur/télécom, comme **Utiq**, illustrent une évolution importante : le tracking ne se limite plus au navigateur.

Utiq est une plateforme AdTech européenne portée par plusieurs grands opérateurs télécoms. Son objectif affiché est de proposer une alternative européenne aux cookies tiers et aux identifiants publicitaires dominés par les grandes plateformes américaines, en s’appuyant sur des signaux opérateur et un mécanisme de consentement utilisateur.

Le point important, pour un cours OPSEC, n’est pas de savoir si Utiq est légal ou illégal, ni de le présenter comme un spyware. Le sujet est plus subtil : Utiq illustre le déplacement du tracking vers une couche plus basse de l’infrastructure. Là où les cookies tiers étaient stockés dans le navigateur, et où l’identifiant publicitaire mobile dépendait du système d’exploitation, les solutions de type Utiq s’appuient sur la relation entre l’abonné, l’opérateur télécom, l’accès réseau et les sites ou applications partenaires.

Cela confirme que supprimer ses cookies ou changer de navigateur ne suffit pas toujours à maîtriser son exposition. Le tracking moderne doit être pensé en couches : navigateur, application, appareil, identifiant publicitaire, réseau, opérateur, plateforme, courtier de données.

Ce changement est important pour trois raisons.

Premièrement, l’opérateur télécom occupe une position privilégiée dans la chaîne réseau. Il connaît l’abonné, la ligne, la carte SIM, l’adresse IP attribuée, le type d’accès et certains paramètres de connexion. Même si le système prétend utiliser des jetons pseudonymes et un consentement explicite, la logique reste sensible : l’infrastructure d’accès à Internet devient aussi une infrastructure publicitaire.

Deuxièmement, la pseudonymisation ne doit pas être confondue avec l’anonymat. Un jeton publicitaire, même temporaire ou spécifique à un site, peut devenir un pivot de corrélation s’il est associé à des horaires, des lieux, des habitudes de navigation, des applications utilisées ou des événements récurrents. Comme toujours en privacy, le risque ne vient pas seulement de la donnée isolée, mais de sa répétition et de sa corrélation.

Troisièmement, ce type de mécanisme contourne partiellement l’intuition classique de l’utilisateur : supprimer ses cookies, changer de navigateur ou bloquer certains scripts ne suffit plus nécessairement à comprendre toute la chaîne de tracking. Le tracking moderne peut combiner plusieurs couches : navigateur, application, identifiant publicitaire mobile, fingerprint, IP, opérateur, consent management platform, bidstream data et données de courtage.

Utiq doit donc être compris comme un exemple de **tracking post-cookie** : un modèle où l’industrie publicitaire cherche de nouveaux identifiants parce que les cookies tiers deviennent moins fiables. Utiq revendique de son côté un modèle fondé sur le consentement utilisateur, des jetons spécifiques par site et un service de gestion (« Consenthub ») permettant de retirer son consentement. Le sujet OPSEC n’est donc pas d’assimiler Utiq à un spyware, mais de constater que l’identification publicitaire remonte vers une couche télécom — plus difficile à percevoir et à neutraliser pour l’utilisateur qu’un cookie navigateur.

Pour un utilisateur courant, le risque principal est l’extension du profilage publicitaire à une couche d’infrastructure plus difficile à percevoir. Pour un profil exposé — journaliste, source, activiste, dirigeant, diplomate, militaire, chercheur cyber — l’enjeu est que les signaux opérateur peuvent contribuer à la corrélation entre identité civile, appareil, localisation approximative, comportement réseau et consultation de contenus sensibles.

## 23.16 Fingerprinting : mécanique

Un **fingerprint** est une signature dérivée de caractéristiques de ton navigateur ou de ton appareil, ramassées par un script JavaScript ou un SDK. Caractéristiques typiques :

- **User-Agent** : navigateur, version, OS.
- **Résolution écran**, profondeur de couleur.
- **Liste de polices installées** (par énumération CSS ou test).
- **Langue, fuseau horaire, locale**.
- **Plugins installés**.
- **Canvas fingerprint** : rendu d’une image cachée, qui varie par GPU et drivers.
- **WebGL fingerprint** : rendu 3D, qui varie selon le GPU.
- **AudioContext fingerprint** : signature audio produite par l’API AudioContext.
- **TLS fingerprint** (JA3/JA4) : combinaison de paramètres TLS qui identifie ton implémentation.
- **HTTP/2 fingerprint** : structure des frames.

Combinées, ces caractéristiques produisent une signature largement unique. EFF Cover Your Tracks et AmIUnique mesurent ce caractère unique. L’EFF avait montré dès 2010 (étude Panopticlick devenue Cover Your Tracks) que la quasi-totalité des navigateurs sont uniquement identifiables, ce qui rend le fingerprinting structurellement efficace.

Contrairement aux cookies, qui sont stockés localement et peuvent être supprimés, le fingerprint repose sur des caractéristiques structurelles. L’utilisateur ne peut donc pas simplement « effacer » son fingerprint ; il doit soit limiter les signaux exposés, soit utiliser un navigateur conçu pour se fondre dans un groupe d’utilisateurs standardisé.

Pour un tracker, un fingerprint utile doit être :

- **Unique** : distinguer les utilisateurs.
- **Stable** : durer dans le temps (sinon, perte de continuité).
- **Difficile à modifier** : sinon, l’utilisateur s’en échappe trivialement.

Le fingerprinting peut aussi servir des finalités légitimes — détection de fraude bancaire, statistiques de crash applicatif — ce qui rend la frontière entre fonctionnement légitime, sécurité antifraude et tracking publicitaire souvent invisible pour l’utilisateur.

L’EFF avait montré dès 2010 (étude Panopticlick devenue Cover Your Tracks) que la quasi-totalité des navigateurs sont uniquement identifiables, ce qui rend le fingerprinting structurellement efficace.

## 23.17 Tracking comportemental

Au-delà des caractéristiques techniques, l’analyse comportementale exploite :

- **Mouvements de souris** : signature gestuelle.
- **Rythme de frappe** : keystroke dynamics.
- **Patterns de scrolling**.
- **Temps passé par section**.

Utilisé en détection de fraude (bonne intention) et en tracking publicitaire (intention plus ambiguë).

## 23.18 Stratégies anti-fingerprint : blend in ou block

**Intuition fausse** : « si je change mon User-Agent pour celui de Chrome standard, je ressemble à plein de monde ». En réalité : Safari iOS est _intrinsèquement_ peu identifiable (peu de variation hardware). Si tu changes ton User-Agent vers Chrome Windows mais que ton canvas fingerprint reste Safari iOS, tu deviens **plus** unique, pas moins.

D’où la règle : **ne pas personnaliser les paramètres anti-fingerprint sauf si tu sais exactement ce que tu fais**. Utiliser des navigateurs conçus pour blend in (Ch 24).

Deux stratégies complémentaires :

**Stratégie 1 — Blend in** : ressembler à la masse. Tor Browser et Mullvad Browser appliquent : tous les utilisateurs ont la même résolution écran (par redimensionnement), la même police, le même User-Agent, le même fuseau horaire (UTC), le même canvas (rendu uniformisé). Chaque utilisateur est interchangeable, donc non identifiable individuellement.

**Stratégie 2 — Block** : bloquer les scripts de tracking. uBlock Origin, Privacy Badger, etc. Bloque la majorité des trackers connus. Mais ne bloque pas le fingerprinting first-party (par le site lui-même), et certains trackers passent.

Les deux stratégies sont complémentaires en théorie ; en pratique, Tor Browser / Mullvad Browser appliquent la première, et la seconde est utile pour navigateurs quotidiens.

## 23.19 Cadre juridique : RGPD, TCF, DSA, DMA

L’écosystème adtech est encadré par plusieurs strates juridiques en Europe. Cette section donne les repères principaux ; le détail des décisions et le cadre comparé international sont traités au Ch 37.

**RGPD** : tout traitement à des fins publicitaires repose normalement sur le consentement (art. 6(1)(a)) ou l’intérêt légitime (art. 6(1)(f), interprétation restrictive). Le consentement doit être libre, spécifique, éclairé, univoque. En pratique, l’industrie a développé le **TCF** pour gérer ces consentements à l’échelle.

**TCF (Transparency and Consent Framework)** de IAB Europe : standard de facto pour les bannières de consentement adtech en Europe. La **version 2.2** (mai 2023) inclut 11 finalités et 10 fonctionnalités spéciales, communiquées via une chaîne technique standardisée (**TC String**) qui voyage avec les bid requests.

**CJUE, 7 mars 2024, C-604/22 — IAB Europe** : décision majeure. La Cour a jugé que la TC String peut constituer une donnée personnelle lorsqu’elle peut être associée à un identifiant comme l’adresse IP ou un cookie, et a précisé les conditions dans lesquelles IAB Europe peut être considérée comme responsable conjoint du traitement. Conséquences en cascade : les acteurs adtech qui s’appuient sur TCF doivent traiter chaque TC String comme une donnée personnelle, avec les obligations associées (information, finalité, durée de conservation, droit d’accès). La décision a été renvoyée à la juridiction belge pour application.

**Décisions nationales notables** : sanctions CNIL contre Google (150 M€, 2022) et Meta (60 M€, 2022) pour dark patterns dans les bannières cookies ; sanction APD belge contre IAB Europe (2022) à l’origine de la procédure CJUE ; multiples sanctions ultérieures 2023-2025 contre des CMP non conformes. **NOYB / Max Schrems** porte la majeure partie du contentieux par plaintes coordonnées multi-États.

**Digital Services Act (DSA, 2022, application 2024)** : transparence des publicités sur les _very large online platforms_ (VLOPs) — archives publicitaires publiques (Meta Ad Library, Google Ads Transparency Center), **interdiction du ciblage publicitaire des mineurs**, **interdiction du profilage publicitaire sur données sensibles** (religion, orientation sexuelle, opinion politique, santé).

**Digital Markets Act (DMA, 2022, application 2024)** : interdit aux _gatekeepers_ (Google, Meta, Apple, Amazon, Microsoft, ByteDance) certains croisements de données sans consentement explicite — notamment l’interdiction pour Meta de combiner les données de Facebook, Instagram et WhatsApp sans opt-in explicite. Effet réel partiel à 2026, contentieux en cours sur l’interprétation du « consentement libre » dans un contexte de gatekeepers.

**ePrivacy / dérogation CSAM** : le règlement ePrivacy attendu depuis 2017 n’est toujours pas adopté à 2026. Concernant la dérogation temporaire (règlement UE 2021/1232) permettant à certains services de communications interpersonnelles de détecter volontairement des contenus pédocriminels en ligne, le calendrier 2026 a été tendu : le Parlement européen a d’abord soutenu, le 11 mars 2026, une extension limitée jusqu’au 3 août 2027, avec un champ réduit et l’exclusion explicite des communications E2EE. Mais les négociations interinstitutionnelles avec le Conseil n’ont pas abouti : le 26 mars 2026, le Parlement a voté contre l’extension finale. **La dérogation a expiré le 3-4 avril 2026**, laissant les fournisseurs sans base juridique européenne harmonisée pour la détection volontaire de CSAM en communications privées. Les négociations sur le règlement permanent (« Chat Control 2.0 ») se poursuivent. Cf. Ch 26.12 sur Chat Control pour le suivi détaillé.

## 23.20 Stratégie défensive en couches

Aucune mesure isolée ne neutralise l’AdTech. La défense réaliste opère par couches superposées, chacune réduisant l’exposition sans la supprimer entièrement.

**Couche navigateur** :

- Firefox + uBlock Origin (+ arkenfox pour profil technique), Brave Shields à _Aggressive_, ou Safari durci — pour le **Niveau 1**.
- Mullvad Browser pour recherches sensibles ou navigation privée renforcée — **Niveau 2**.
- Tor Browser pour sessions où l’anonymat réseau est central — **Niveau 2-3**.
- Ne pas être connecté à ses comptes Google/Meta dans le navigateur quotidien — multi-comptes containers Firefox ou profils Chrome distincts.

**Couche OS** :

- iOS : ATT à « Demander aux apps de ne pas suivre » par défaut ; Réglages → Confidentialité → Publicité Apple → Annonces personnalisées désactivé.
- Android stock : Paramètres → Confidentialité → Annonces → Supprimer l’identifiant publicitaire (effacement définitif depuis Android 12-13 sur certains constructeurs).
- GrapheneOS : pas de Google Play Services par défaut (donc pas d’Advertising ID Google exposé par défaut via Play Services) ; si l’utilisateur installe les Google Play Services sandboxés, un AAID peut exister selon la configuration du profil — vérifier et réinitialiser dans ce cas, ou éviter d’installer GPS dans les profils sensibles. Permission réseau granulaire par app, profils utilisateur isolés.
- macOS / Windows : limiter la télémétrie (cf. Ch 14).

**Couche application** :

- Audit Exodus Privacy avant installation d’une app Android.
- Préférer apps payantes ou open source (F-Droid) aux apps gratuites financées par la publicité.
- Désinstaller les apps gratuites « pourries de SDK » : météo, lampe torche, jeux gratuits, applications de prière, applications de rencontre — toutes catégories sur-représentées dans les fuites Gravy Analytics et autres.
- Limiter strictement la géolocalisation en arrière-plan.

**Couche réseau** :

- DNS chiffré avec filtre adtech : **NextDNS** (configurable), **AdGuard DNS**, ou **Pi-hole** auto-hébergé.
- VPN ponctuel pour masquer l’IP sur sessions sensibles (mais le VPN ne bloque pas le tracking applicatif ni le fingerprinting).

**Couche compartimentation** :

- Profils navigateur séparés par usage.
- Comptes Apple/Google séparés entre identités si Niveau 2-3.
- Email distinct pour les services gratuits financés par la publicité — usage d’alias (SimpleLogin, Addy.io).

**Couche physique / lieux sensibles** :

- Pour les profils exposés : ne pas emporter le téléphone personnel dans les lieux sensibles lorsque ce n’est pas strictement nécessaire.
- Pour les environnements institutionnels, militaires, industriels ou journalistiques sensibles : définir explicitement quels appareils sont autorisés dans quels lieux.
- Pour le Niveau 3 : téléphone dédié ou burner sans compte personnel, sans applications publicitaires, sans MAID actif, sans géolocalisation en arrière-plan non indispensable.
- Téléphone principal laissé hors zone sensible, éteint ou en pochette Faraday selon le contexte.
- Pour les organisations : MDM/EMM, liste blanche applicative, interdiction des applications gratuites financées par la publicité sur les appareils opérationnels.
- Règle OPSEC : un téléphone n’a pas besoin d’être compromis pour trahir une présence, une routine ou un lieu sensible.
- Cf. Capstone 1 (compartimentation), Ch 15 (mobile), Ch 22 (Wi-Fi, Bluetooth, cellulaire) et Ch 38 (architectures par profil).

**Couche carte de fidélité / retail** :

- Pas de carte de fidélité au nom civil pour les achats à isoler.
- Cash pour les achats sensibles (Ch 32).
- Si carte indispensable, pseudonyme et adresse de domiciliation alternative (cf. Ch 7).

## 23.21 Contre-mesures réalistes

Il n’existe pas de bouton unique permettant de sortir totalement de l’AdTech. La défense repose sur la réduction d’exposition.

Mesures utiles :

- refuser les cookies et finalités publicitaires non nécessaires ;
- utiliser un bloqueur de contenus sérieux comme uBlock Origin ;
- limiter les applications gratuites financées par la publicité ;
- privilégier les applications open source, payantes ou sans SDK publicitaires ;
- désactiver ou limiter l’identifiant publicitaire mobile ;
- refuser le tracking inter-applications sur iOS ;
- réinitialiser périodiquement l’identifiant publicitaire sur Android si l’usage l’exige ;
- limiter strictement la géolocalisation en arrière-plan ;
- séparer les profils mobiles lorsque l’OS le permet ;
- utiliser des navigateurs distincts par usage ;
- éviter de rester connecté à ses comptes Google, Meta ou Microsoft dans le navigateur utilisé pour des recherches sensibles ;
- utiliser Tor Browser, Tails ou Whonix pour les sessions où l’anonymat réseau est central ;
- éviter d’emporter son téléphone personnel dans des lieux sensibles ;
- pour les profils exposés, utiliser un appareil dédié minimaliste sans applications publicitaires.

Le point clé est qu’aucune couche n’est suffisante seule, mais que **leur empilement réduit fortement l’exposition**. Un utilisateur Niveau 1 appliquant disciplinement les couches navigateur, OS, DNS filtrant et audit applicatif réduit déjà très significativement son exposition par rapport à une configuration par défaut, sans entrer dans la compartimentation avancée de Niveau 2 ou 3.

Le tracking ne se limite plus au navigateur : il s’étend à l’écosystème publicitaire, aux applications, aux courtiers de données, aux identifiants mobiles, à la TV connectée, aux distributeurs, et désormais à certains signaux issus de l’infrastructure télécom. Dans une logique OPSEC, il faut raisonner en couches : appareil, application, navigateur, réseau, opérateur, plateforme, courtier de données.

-----
