---
title: "Université de Montréal : la géolocalisation, une donnée à part qui appelle un « droit de ne pas être suivi »"
date: 2026-11-22
kind: analysis
theme: "cyber"
slug: "universite-de-montreal-la-geolocalisation-une-donnee-a-part-qui-appelle-un-droit-de-ne-pas-etre-suivi"
author: "Laurence Béland-Cousineau"
organization: "Université de Montréal, Faculté de droit"
rubriques:
  - rens-opsec
  - justice-droit
  - rens-osint
tags:
  - géolocalisation
  - données de localisation
  - vie privée
  - surveillance
  - courtiers en données
  - réidentification
  - anonymisation
  - GNSS
---

# Université de Montréal : la géolocalisation, une donnée à part qui appelle un « droit de ne pas être suivi »

## Métadonnées

- **Titre original :** *Le droit de ne pas être suivi : analyse juridique de la surveillance par géolocalisation*.
- **Auteure :** Laurence Béland-Cousineau.
- **Affiliation :** Université de Montréal, Faculté de droit ; mémoire présenté en vue de la maîtrise en droit des technologies de l'information, sous la direction de Nicolas Vermeys, évalué par un jury présidé par Vincent Gautrais (page de titre et page du jury).
- **Date :** novembre 2026.
- **Source analysée :** PDF original.
- **Volume :** 136 pages, dont une introduction (p. 1-10), une première partie technique et sociologique (p. 11-45), une seconde partie juridique (p. 46-100), une conclusion (p. 101-105), une annexe sur les usages (p. 106-112) et une bibliographie (p. 113 et suivantes).
- **Périmètre :** droit québécois de la protection des renseignements personnels appliqué aux entreprises privées ; le secteur public, la police et la surveillance d'État sont exclus, sauf mentions ponctuelles (p. 8-9).
- **Thématique :** géolocalisation, données de localisation, surveillance commerciale et vie privée.
- **Méthode de la fiche :** la fiche restitue l'ensemble du mémoire mais s'attarde sur la première partie, les solutions techniques et l'annexe, transposables hors du Canada ; le régime juridique québécois est résumé. Les pages citées sont celles imprimées en pied de page. La dernière section confronte le mémoire aux recherches et enquêtes publiées ailleurs.

## Repères pour comprendre le document

Le mémoire a deux étages. Le premier explique ce qu'est la géolocalisation, comment elle est produite et à quoi elle sert ; il s'appuie surtout sur la doctrine canadienne (Teresa Scassa, Colin Bennett), l'Electronic Frontier Foundation (EFF) et quelques articles techniques. Le second démontre que le droit québécois, malgré la réforme de 2021 dite « loi 25 », traite la localisation comme un renseignement personnel parmi d'autres et propose d'y ajouter un droit autonome « de ne pas être suivi ». Pour un lecteur hors du Québec, l'intérêt tient surtout au premier étage et à l'inventaire des solutions techniques, qui ne dépendent pas d'un droit national.

Trois distinctions traversent le texte. La géolocalisation situe d'abord **un appareil**, pas une personne : c'est un indice de présence, que le vol ou le prêt du téléphone peut tromper (p. 12). Ensuite, une **observation** ponctuelle n'a pas la même portée qu'un **enregistrement** continu : c'est l'accumulation des points qui reconstitue une vie (p. 57). Enfin, la collecte **active** (l'utilisateur partage sa position) se distingue de la collecte **passive** (en arrière-plan, sans qu'il le sache), qui pose les vrais problèmes de consentement (p. 58). Les définitions ci-dessous sont pédagogiques ; celles qui reprennent le mémoire le signalent.

- **Géolocalisation** — « détermination plus ou moins précise, par des moyens technologiques, de la position géographique d'un appareil électronique à un moment donné » (définition de l'Office québécois de la langue française reprise p. 12).
- **Information géospatiale, civique et descriptive** — les trois formes de donnée de localisation selon le mémoire : coordonnées brutes (latitude, longitude, altitude), découpages humains (pays, code postal, adresse) et nature du lieu (église, école, clinique) ; c'est la troisième qui rend la donnée sensible (p. 12-13).
- **Géomarquage** — ajout d'une position à un contenu numérique (photo, message, publication).
- **Géocodage** — conversion d'une description lisible (adresse, nom de commerce) en coordonnées ; l'inverse, le géocodage inverse, transforme des coordonnées en adresse.
- **Géoréférencement** — fait de situer précisément une entité (objet, personne) sur une carte, par exemple avec un bracelet électronique (p. 16).
- **Géorepérage (*geofencing*)** — déclenchement d'une action quand un appareil franchit une frontière virtuelle (p. 26-27).
- **Trilatération / multilatération / triangulation** — calcul d'une position à partir de distances à des points connus, de différences de temps d'arrivée ou d'angles ; le mémoire les présente toutes trois comme des méthodes GPS, ce qui est inexact pour la triangulation (voir les limites).
- **Positionnement Wi-Fi (WPS)** — estimation de la position à partir des bornes Wi-Fi visibles, comparées à une base de bornes géolocalisées.
- **Empreinte radio (*fingerprinting*)** — comparaison des signaux mesurés à une carte de signaux relevée à l'avance.
- **Marché primaire / secondaire** — usage de la donnée pour rendre le service demandé, puis revente ou réutilisation à d'autres fins, notamment le profilage (p. 28-30).
- **Surplus comportemental** — notion de Shoshana Zuboff reprise p. 31 : les traces laissées au-delà du besoin du service, exploitées pour prédire les comportements.
- **Unicité des traces de mobilité** — propriété démontrée par la recherche : quelques points spatio-temporels suffisent à distinguer une personne parmi des millions (p. 59-60).
- **LPPM (*Location Privacy Preserving Mechanisms*)** — famille de techniques visant à rendre un service de localisation en protégeant la vie privée (p. 81).

## Résumé exécutif

Le mémoire soutient que la géolocalisation n'est plus une fonction accessoire mais le centre d'un réseau de données qui permet de suivre les personnes en continu, et que le droit québécois ne sait pas l'encadrer. Sa première partie décrit les technologies (GNSS, Wi-Fi, réseau cellulaire, Bluetooth, bande ultra-large, adresse IP et cookies, RFID, géorepérage, navigateur, localisation inférée), les usages et un inventaire des risques : atteintes à la vie privée, surveillance au travail et commerciale, violences conjugales, exposition des enfants, discrimination et erreurs. Sa seconde partie qualifie la donnée de localisation de renseignement personnel, souvent sensible, puis montre les failles du cadre québécois et propose un droit de ne pas être suivi fondé sur la désactivation par défaut.

Le raisonnement repose sur un constat empirique décisif, la **quasi-impossibilité d'anonymiser des traces de mobilité** : quatre points spatio-temporels suffisent à réidentifier 95 % des individus d'une base de 1,5 million de personnes (p. 59-60). Il en découle que l'anonymisation, qui soustrait les données au droit, ne protège pas vraiment, et que le consentement, conçu pour des collectes ponctuelles, ne convient pas à une collecte continue et invisible. Le mémoire passe en revue six familles de solutions techniques (minimisation dès la conception, réduction de précision, limitation dans le temps, traitement local, anonymisation, cryptographie) et conclut que leur efficacité dépend de la volonté d'acteurs dont le modèle économique repose sur la donnée.

Pour la veille, le document vaut comme synthèse pédagogique et comme catalogue de cas (LocationSmart, chasseur de primes payé 300 dollars, Family Locator, enquête du *New York Times* de 2018, Street Bump, Evolv), utile bien au-delà du Québec. Ses limites sont celles d'un mémoire de droit : une partie technique qui comporte des approximations, des sources souvent anciennes (2009-2019), et un angle mort assumé sur la surveillance d'État, le renseignement et la sécurité nationale.

## Thèse principale

Le texte est une **démonstration juridique suivie d'une proposition normative**. L'hypothèse est que le droit québécois de la protection des renseignements personnels est « conceptuellement insuffisant pour appréhender la dimension spatiale continue » des données de localisation (p. 4). La démonstration enchaîne quatre idées : la donnée de localisation est presque toujours personnelle ; elle est souvent sensible, parce que le lieu révèle la santé, la religion ou l'orientation sexuelle ; son unicité rend l'anonymisation illusoire ; le consentement, la transparence et les sanctions actuels sont inadaptés à une collecte continue, passive et multi-acteurs.

La proposition qui en découle est un **droit de ne pas être suivi**, conçu comme préventif : non une interdiction de la géolocalisation, mais une désactivation du suivi par défaut, une transparence renforcée, un contrôle continu de l'utilisateur et un régime de responsabilité aggravé, avec présomption d'atteinte et dommages punitifs (p. 6, 95-100).

## Informations et arguments importants

### Nature de la géolocalisation et de ses données

Le mémoire pose d'abord que la géolocalisation est omniprésente et banalisée : les utilisateurs la traitent comme une donnée aussi anodine qu'une adresse électronique (p. 1-2). Il en donne une grille de lecture en quatre volets (p. 11-14) :

1. **Définition** : la position d'un appareil à un instant donné, qui ne vaut que comme indice de la présence de son utilisateur.
2. **Trois formes de données** : géospatiale, civique et descriptive. La forme descriptive, qui dit ce qu'est le lieu, transforme un point en information intime : la fréquentation d'une clinique de santé sexuelle ou d'un bar homosexuel, croisée avec d'autres données, peut révéler l'état de santé ou l'orientation sexuelle (p. 13).
3. **Sujets** : objets (colis, conteneurs, matériel médical), objets mobiles (voitures, avions, métros) et personnes, identifiables ou suivies dans leur fonction (policier, camionneur, facteur), ce dernier cas étant le plus sensible (p. 13-14).
4. **Mode de calcul** : par le terminal (le GPS du téléphone) ou par le réseau (point d'accès Wi-Fi, commutateur), dans lequel l'utilisateur a peu de contrôle et de connaissance (p. 14).

Trois catégories d'usage complètent ce cadre (p. 14-16). Le **géomarquage** est en principe volontaire, mais la donnée partagée peut être revendue à des annonceurs ou à des fonds d'investissement. Le **géocodage**, très courant (une recherche sur Google Maps ou Waze), est piloté par l'utilisateur mais nourrit lui aussi des profils lorsqu'il est enregistré dans la durée. Le **géoréférencement**, illustré par le bracelet électronique, est le plus directement lié à la surveillance.

### Dix technologies de localisation

La partie C (p. 16-28) passe en revue dix procédés. Le mémoire insiste moins sur la physique que sur ce que chacun implique pour la vie privée :

- **GPS et GNSS.** Le récepteur calcule sa position à partir des signaux de plusieurs satellites ; précision d'environ 4 à 15 mètres par ciel dégagé selon le Groupe de l'article 29 (2011), dégradée en ville, d'où le GPS assisté (A-GPS). L'intégration au téléphone a permis des collectes massives à l'insu des utilisateurs (p. 17-18).
- **Positionnement Wi-Fi.** L'appareil relève les identifiants (adresses MAC) et la puissance des bornes voisines et les compare à une base de bornes géolocalisées ; l'empreinte radio, le temps de vol (ToF) et l'angle d'arrivée (AoA) améliorent la précision, jusqu'à quelques mètres, voire quelques centimètres, en intérieur. Le procédé fonctionne en arrière-plan (p. 18-20).
- **Réseau cellulaire.** Le téléphone reste en contact avec les antennes ; la position est estimée à quelques centaines de mètres en ville et à plusieurs kilomètres à la campagne, sans action de l'utilisateur, d'où son intérêt pour les urgences. Les tribunaux québécois admettent ces données comme preuve approximative, et le Commissariat fédéral a enquêté sur leur usage « dépersonnalisé » pendant la pandémie (p. 20-21).
- **Balises Bluetooth et bande ultra-large (UWB).** Précision métrique ou submétrique en espace fermé ; l'UWB, plus précis et plus résistant aux interférences mais plus coûteux, est illustré par l'AirTag d'Apple (p. 22-23).
- **Adresse IP et cookies.** L'IP ne situe en général qu'à l'échelle de la ville ou du pays, mais le fournisseur d'accès peut la relier à un abonné ; la Cour suprême du Canada a reconnu en 2024 (*R. c. Bykovets*) une attente raisonnable de vie privée sur l'adresse IP. Associée aux cookies, elle permet de suivre la navigation (p. 23-24).
- **Localisation inférée.** Déduite d'un achat par carte, d'une entrée d'agenda ou d'un historique, elle peut servir à contourner les restrictions qui visent les autres technologies (p. 24-25).
- **RFID.** Lecteur, étiquette et base de données ; étiquettes passives (moins de 5 mètres) ou actives ; outil logistique qui peut aussi suivre un client dans un magasin et même après sa sortie (p. 25-26).
- **Géorepérage.** Frontière virtuelle qui déclenche promotions, alertes ou contrôles d'employés ; il repose sur les autres technologies (p. 26-27).
- **Navigation web géolocalisée.** Des scripts permettent aux sites de demander la position de l'internaute, par exemple pour afficher la météo ou un rabais local (p. 27-28).

La conclusion de cette partie est que les technologies diffèrent par la précision, la continuité et le mode de collecte, ce qui complique un cadre juridique uniforme, mais qu'elles permettent presque toutes de reconstituer les comportements (p. 27-28).

### Usages : marché primaire et marché secondaire

Le mémoire distingue l'usage qui rend le service demandé et la revente (p. 28-33). Le marché primaire couvre onze secteurs détaillés en annexe A : navigation, marketing, santé et bien-être, assurance automobile, banques et lutte contre la fraude, systèmes de transport intelligents, urgences, suivi des employés, traceurs grand public, justice pénale, télématique et véhicules autonomes (p. 106-112). Le marché secondaire vend la donnée sous forme individualisée ou « anonymisée » via des agrégateurs. L'exemple type est celui d'une application de navigation qui revend des densités de piétons pour choisir l'emplacement d'un magasin ; mais chaque utilisateur y porte un identifiant persistant, ce qui permet de recouper les bases (p. 30-31). Le profilage, nourri du « surplus comportemental », combine la localisation à des données de transaction ou sociodémographiques et en tire sa valeur commerciale (p. 31-32).

### Inventaire des risques

Le mémoire classe les risques en cinq familles (p. 33-45) :

1. **Vie privée et surveillance non consentie.** L'inférence transforme des déplacements en domicile, religion ou orientation. L'outil d'IA GeoLocator a déterminé l'adresse exacte d'une personne dans 54 % des cas à partir de photos sans métadonnées (p. 33-34). Les failles techniques aggravent le risque : un défaut du site de LocationSmart permettait de localiser n'importe quel téléphone à partir de son numéro, et un chasseur de primes a localisé un téléphone contre 300 dollars (p. 34-35). La réidentification est démontrée par les travaux sur le triplet code postal, date de naissance et sexe et sur la paire domicile-travail (p. 35).
2. **Surveillance dans des contextes précis.** Au travail, l'affaire *Teamsters Québec* (2025) porte sur une application imposée sur le téléphone personnel des employés pour calculer les kilomètres ; l'affaire *Hydro-Québec* (2024) juge au contraire légitime un GPS de véhicule de service limité à la sécurité (p. 36-38). En matière commerciale, l'enquête du *New York Times* de 2018 recense plus de 75 entreprises traitant des positions précises, certaines suivant jusqu'à 200 millions d'appareils et relevant une position jusqu'à plus de 14 000 fois par jour (p. 38-39).
3. **Sécurité physique.** Contrôle coercitif dans le couple, y compris via le véhicule connecté (p. 40) ; fuite de l'application Family Locator, qui exposait en temps réel la position de familles et permettait de savoir si un enfant était seul (p. 41) ; données de fréquentation des cliniques d'avortement aux États-Unis après l'arrêt *Dobbs* (p. 41-42).
4. **Discrimination.** Prix modulés selon le lieu (jusqu'à 166 % d'écart pour des livres Kindle entre pays, 11 % au sein d'un même État américain sur Staples.com) ; refus de la société Evolv d'utiliser la distance domicile-travail dans le recrutement par crainte d'une discrimination raciale ; biais de participation, illustré par l'application Street Bump de Boston, qui détectait surtout les nids-de-poule des quartiers aisés (p. 42-44).
5. **Qualité des données.** Une position erronée peut fonder une hausse de prime d'assurance que l'intéressé ne pourra ni connaître ni contester (p. 44-45).

### Unicité et limites de l'anonymisation

Dans la partie juridique, une section a une portée universelle (p. 57-61). Le mémoire y distingue observation et enregistrement, collecte active et passive, puis s'appuie sur deux études. Celle de de Montjoye et ses coauteurs (2013), sur 1,5 million de personnes suivies 15 mois avec une précision de l'ordre de l'antenne et une position par heure, montre que **quatre points spatio-temporels réidentifient 95 % des individus** et deux points environ la moitié, et que réduire la résolution ne fait baisser l'unicité que lentement. Celle de Zang et Bolot (2011) montre que les lieux les plus fréquentés suffisent à réidentifier, même à une granularité grossière. Le mémoire ajoute que l'autorité québécoise de protection des données (CAI) juge elle-même quasi impossible l'anonymisation des données de localisation (p. 78).

### Le régime juridique québécois, en bref

La seconde partie, centrale pour l'auteure, est résumée ici parce qu'elle concerne surtout le droit québécois. Elle qualifie la donnée de localisation de renseignement personnel et, dans de nombreux contextes, de renseignement sensible, en s'appuyant sur le Commissariat fédéral et sur l'enquête Tim Hortons (p. 46-57). Elle montre ensuite un cadre fragmenté entre Chartes, Code civil, loi sur le secteur privé et loi sur les technologies de l'information, qui ne définit pas la géolocalisation ; un consentement « illusoire » face à une collecte continue ; un règlement sur l'anonymisation inadapté ; des sanctions réactives (p. 61-80). Les pistes juridiques générales (consentement et transparence renforcés, responsabilisation de l'écosystème, gouvernance interne) précèdent la proposition d'un régime spécialisé et du droit de ne pas être suivi (p. 88-100).

### Six solutions techniques

La section la plus transposable inventorie les mécanismes de protection (p. 81-88), regroupés sous le nom de LPPM :

1. **Minimisation dès la conception.** Ne collecter que ce qu'exige la requête, limiter le transfert aux tiers, mettre la position en cache sur l'appareil pour réduire les interrogations des services de localisation (p. 82-83).
2. **Réduction de la précision.** Transmettre un quartier ou un code postal plutôt que des coordonnées, par masquage de localisation (*location cloaking*) ou ajustement de granularité ; le risque de réidentification subsiste par recoupement (p. 83-84).
3. **Limitation temporelle.** Conservation courte, segmentation des traces, collecte ponctuelle ; c'est l'accumulation qui permet le profilage, mais elle fait aussi la valeur analytique (p. 84).
4. **Traitement local.** Calculer sur l'appareil, réduire les échanges avec les serveurs, et confier la donnée à des coffres-forts personnels ou fiducies de données qui n'ouvrent l'accès que sur autorisation (p. 84-86).
5. **Anonymisation et dépersonnalisation.** Randomisation (bruit, permutation, confidentialité différentielle) et généralisation (k-anonymat, l-diversité, t-proximité), justificatifs anonymes ; mesures d'atténuation, pas garanties, à cause de l'unicité des traces (p. 86-87).
6. **Cryptographie.** Empreintes et chiffrement, calcul multipartite sécurisé pour prouver la proximité sans révéler la position ; efficaces mais difficiles à déployer à grande échelle sur mobile (p. 87-88).

## Points particulièrement intéressants pour la veille

- **La localisation inférée échappe aux règles visant les capteurs.** Le mémoire relève qu'une position déduite d'achats ou d'agendas peut contourner les restrictions qui visent le GPS (p. 24-25). *Inférence pour la veille :* toute régulation fondée sur les capteurs ou les permissions du téléphone laisse ouverte la porte de l'inférence, que l'IA élargit.
- **L'IA géolocalise sans métadonnées.** GeoLocator retrouve une adresse exacte dans 54 % des cas à partir d'images ordinaires (p. 33-34). *Inférence pour la veille :* retirer les données EXIF ne suffit plus ; les règles d'OPSEC sur les photos publiées doivent porter sur leur contenu.
- **L'anonymisation est démentie par l'autorité qui l'encadre.** La CAI juge quasi impossible l'anonymisation de la localisation (p. 78). *Inférence pour la veille :* tout jeu de données de mobilité présenté comme anonyme doit être traité comme réidentifiable, y compris pour l'évaluation de la menace sur le personnel sensible.
- **Le traceur et le partage familial sont des outils de contrôle coercitif.** Le mémoire documente l'usage de la localisation dans les violences conjugales et via les véhicules connectés (p. 40). *Inférence pour la veille :* les fonctions de partage de position et les traceurs Bluetooth entrent dans le périmètre de la cybersécurité des personnes, pas seulement de la vie privée.
- **Le marché secondaire repose sur l'identifiant persistant.** Les données « anonymisées » revendues portent un identifiant stable qui permet de suivre l'appareil et de recouper les bases (p. 30-31). *Inférence pour la veille :* l'identifiant publicitaire et les SDK des applications sont le point d'entrée à surveiller, plus que la donnée GPS elle-même.
- **La géolocalisation sert de preuve, mais approximative.** Les juridictions québécoises admettent les données d'antennes comme indices de présence dans un périmètre, avec expertise (p. 20-21). *Inférence pour la veille :* la valeur probante dépend de la technologie, et une erreur de position peut conduire à une arrestation injustifiée (p. 111).

## Faits, opinions et interprétations

### Faits rapportés par la source

Le mémoire rapporte des résultats de recherche et des cas documentés : **95 % des individus réidentifiés avec quatre points** dans l'étude de 2013, plus de **75 entreprises** et jusqu'à **200 millions d'appareils** suivis selon le *New York Times* en 2018, **54 %** d'adresses exactes retrouvées par GeoLocator, des écarts de prix de **166 %** selon le pays pour des livres Kindle, une localisation obtenue pour **300 dollars** par un chasseur de primes, la fuite de Family Locator. Il rapporte aussi des précisions techniques (GPS de 4 à 15 mètres, antennes de quelques centaines de mètres à plusieurs kilomètres, Bluetooth et UWB au mètre près, IP à l'échelle de la ville) et une jurisprudence québécoise et canadienne abondante (*Bykovets*, *Teamsters Québec*, *Hydro-Québec*, *Araghoune*). Ces faits viennent de sources secondaires citées, que le mémoire ne vérifie pas lui-même.

### Opinions ou positions de l'auteure

L'auteure juge que le cadre québécois est **fragmenté, inadapté et réactif**, que le consentement est une **« garantie illusoire »**, que l'anonymisation fonctionne comme un **« passe-droit réglementaire »** et que la géolocalisation doit devenir une catégorie autonome de renseignements personnels. Elle plaide pour un droit de ne pas être suivi, une désactivation par défaut, une présomption d'atteinte et des dommages punitifs. Elle estime aussi que les solutions techniques dépendent de la bonne volonté d'acteurs économiquement intéressés à la collecte.

### Interprétations et inférences

L'interprétation centrale est que **la continuité et l'unicité** font de la localisation une donnée d'une autre nature que les renseignements personnels ordinaires : le danger ne tient pas au point, mais à la trace. *Inférence de l'analyse :* cette thèse dépasse le droit québécois ; elle vaut pour tout régime qui fait reposer la protection sur le consentement et l'anonymisation. En revanche, la proposition d'un droit autonome de ne pas être suivi recoupe largement des principes déjà présents ailleurs (protection par défaut, minimisation) ; son apport tient surtout à la désactivation par défaut et au renversement de la charge de la preuve.

## Limites et points à vérifier

1. **Des approximations techniques.** Le mémoire présente la triangulation (mesure d'angles) comme une méthode GPS, alors que le GPS repose sur des mesures de temps de parcours depuis au moins quatre satellites ; il dit le Wi-Fi « généralement préféré au GPS », alors que les téléphones fusionnent les sources ; il attribue à l'UWB la localisation de l'AirTag « en tout temps », qui repose en fait sur le réseau Bluetooth des appareils Apple voisins, l'UWB ne servant qu'à la recherche de proximité. Ces erreurs ne changent pas la thèse mais fragilisent la partie descriptive.
2. **Des sources techniques datées ou faibles.** La précision du GPS vient d'un avis européen de 2011, celle des antennes d'une étude de 2009, et le géorepérage est décrit d'après un article peu connu sur les fuites de données. Les progrès récents (GNSS bifréquence, positionnement 5G, Bluetooth à mesure de distance) sont absents.
3. **La navigation web décrite de manière trop alarmante.** Le mémoire indique que la localisation peut être « poussée » à l'internaute sans requête active ; or l'interface de géolocalisation des navigateurs impose une autorisation. Le risque réel est ailleurs : la géolocalisation silencieuse par adresse IP et la diffusion de la position dans les enchères publicitaires.
4. **Un angle mort assumé sur l'État.** La surveillance policière, le renseignement, l'achat de données par les administrations et les mandats de géorepérage sont exclus (p. 8-9). C'est cohérent avec un mémoire de droit privé, mais cela laisse de côté une part majeure des usages et des risques.
5. **Un marché secondaire décrit sans ses mécanismes actuels.** Les SDK de monétisation, l'identifiant publicitaire et les flux d'enchères en temps réel, qui alimentent l'essentiel des courtiers, ne sont pas expliqués ; les exemples datent de 2018-2019 et précèdent les enquêtes et sanctions de 2024-2025.
6. **Des chiffres repris sans mise en perspective.** Les 21 milliards de dollars attribués au « marché » de la localisation en 2018 désignent, dans l'enquête citée, la publicité ciblée par la localisation, pas la vente de données. Le résultat de 54 % de GeoLocator dépend du jeu d'images testé.
7. **Une proposition dont la mise en œuvre reste floue.** La désactivation par défaut se heurte aux services qui exigent la localisation (urgences, navigation, antifraude) ; le mémoire ne précise pas les exceptions, ni comment la présomption d'atteinte s'articulerait avec une collecte réseau que l'utilisateur ne peut pas désactiver.

## Sources et références mentionnées

La bibliographie est surtout juridique et canadienne : la doctrine de Teresa Scassa (2006-2020) et de Colin Bennett, le rapport de Bennett et Crowe pour le Commissariat fédéral (2005), les lignes directrices de la CAI et du Commissariat, une jurisprudence québécoise nombreuse et quelques avis européens du Groupe de l'article 29 (2005, 2011, 2014). La partie technique s'appuie sur le texte de l'EFF *On Locational Privacy* (2009), l'étude de Zandbergen sur la précision de l'iPhone (2009), des revues de littérature sur le Wi-Fi, le Bluetooth et l'UWB, et sur des études de référence en vie privée : de Montjoye *et al.* (2013), Zang et Bolot (2011), Paul Ohm (2010), Barocas et Selbst (2016), Zuboff (2015, 2019). Les cas proviennent de la presse (*New York Times*, *Vice*, *TechCrunch*, *Wired*). L'ensemble est solide sur la doctrine de la vie privée, plus mince et plus ancien sur la technique.

## Cinq éléments essentiels à retenir

1. La géolocalisation situe **un appareil, pas une personne**, mais l'enregistrement continu de ses positions reconstitue une vie entière.
2. Les dix technologies décrites (GNSS, Wi-Fi, antennes, Bluetooth, UWB, IP, RFID, géorepérage, navigateur, inférence) diffèrent par la précision et le mode de collecte, mais **presque toutes permettent le suivi**.
3. **Quatre points spatio-temporels réidentifient 95 % des personnes** : l'anonymisation des traces de mobilité est, en pratique, illusoire.
4. Les risques dépassent la vie privée : **contrôle coercitif, exposition des enfants, discrimination tarifaire, biais de données et erreurs** aux conséquences financières.
5. Les **solutions techniques** (minimisation, précision réduite, conservation courte, traitement local, cryptographie) existent mais dépendent de la volonté des acteurs, d'où la proposition d'un **droit de ne pas être suivi** par défaut.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-11-22. Les constats ci-dessous ne modifient pas les sections précédentes, fondées sur le seul mémoire.

### Travaux de référence

- **L'unicité des traces, démontrée dès 2009.** [Golle et Partridge — « On the Anonymity of Home/Work Location Pairs »](https://crypto.stanford.edu/~pgolle/papers/commute.html) (Pervasive 2009) estiment, à partir des données du recensement américain, que la paire domicile-travail connue à l'échelle de l'îlot laisse un ensemble d'anonymat médian de **1** personne, de 21 à l'échelle du secteur de recensement et de près de 35 000 à celle du comté. Ce travail, antérieur aux deux études citées par le mémoire, montre que la granularité, et non la seule suppression des noms, gouverne la réidentification.
- **Une protection formelle de la position.** [Andrés, Bordenabe, Chatzikokolakis et Palamidessi — « Geo-Indistinguishability »](https://arxiv.org/abs/1212.1984) (CCS 2013) transposent la confidentialité différentielle à la localisation : la position est perturbée par un bruit de Laplace planaire calibré, de sorte que deux points proches restent indiscernables. C'est la formalisation la plus citée du « masquage » que le mémoire décrit qualitativement ; les auteurs montrent aussi que la protection s'érode lorsque les traces s'allongent.

### Compléments sur le sujet

Le mémoire décrit l'économie de la localisation telle qu'elle apparaissait vers 2018. Les enquêtes et décisions récentes en précisent les mécanismes et l'ampleur ; elles sont développées dans le dossier du site consacré à la géolocalisation, et seuls les points qui éclairent directement le mémoire sont résumés ici.

- **Les courtiers ont été sanctionnés et piratés.** La Federal Trade Commission américaine a interdit en 2024 à plusieurs courtiers (X-Mode, InMarket, Gravy Analytics et Venntel, Mobilewalla) de vendre des données de fréquentation de lieux sensibles comme les cliniques ou les lieux de culte ([The Record](https://therecord.media/ftc-location-data-brokers-gravy-venntel-mobilewalla), décembre 2024 ; [EFF — X-Mode](https://www.eff.org/deeplinks/2024/01/ftc-bars-x-mode-selling-sensitive-location-data), janvier 2024). En janvier 2025, Gravy Analytics a subi un vol de données dont l'échantillon publié citait des milliers d'applications sources, dont des applications de rencontre et de santé reproductive ([TechCrunch](https://techcrunch.com/2025/01/13/gravy-analytics-data-broker-breach-trove-of-location-data-threatens-privacy-millions/), 13 janvier 2025). Le risque de « défaillance technique » évoqué p. 34 a donc frappé le cœur du marché secondaire.
- **L'affaire du chasseur de primes a eu une suite.** Le cas cité p. 34-35 a conduit la Federal Communications Commission à infliger près de **200 millions de dollars** d'amendes à quatre opérateurs américains pour avoir vendu la localisation de leurs clients à des agrégateurs sans consentement ([TechCrunch](https://techcrunch.com/2024/04/30/us-fines-telcos-200m-for-sharing-customer-location-data-without-consent), 30 avril 2024).
- **Les bornes Wi-Fi sont elles-mêmes traçables.** Des chercheurs de l'université du Maryland ont montré que la base de positionnement Wi-Fi d'Apple pouvait être interrogée massivement pour cartographier des centaines de millions de bornes et suivre leurs déplacements, y compris en Ukraine et à Gaza ; la parade proposée est d'ajouter « _nomap » au nom du réseau, en attendant une randomisation des identifiants de borne ([Rye et Levin, arXiv](https://arxiv.org/abs/2405.14975), 23 mai 2024). Le positionnement Wi-Fi décrit p. 18-20 expose donc aussi ceux qui ne le demandent pas : les propriétaires des bornes.
- **L'IA rend la géolocalisation d'images accessible à tous.** En avril 2025, des utilisateurs ont détourné le modèle o3 d'OpenAI pour retrouver le lieu de photos ordinaires sans métadonnées ([TechCrunch](https://techcrunch.com/2025/04/17/the-latest-viral-chatgpt-trend-is-doing-reverse-location-search-from-photos), 17 avril 2025), et une étude a montré qu'un tel modèle pouvait estimer l'adresse d'une résidence privée ([« Doxing via the Lens », arXiv](https://arxiv.org/abs/2504.19373v1), avril 2025). Le cas GeoLocator du mémoire n'était donc pas un prototype isolé.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| Quatre points spatio-temporels réidentifient 95 % des individus (p. 59-60) | **Confirmé** : étude sur 1,5 million d'abonnés mobiles, 15 mois | [de Montjoye *et al.*, *Scientific Reports*](https://www.nature.com/articles/srep01376), 2013 |
| La paire domicile-travail suffit à réidentifier (p. 35) | **Confirmé**, et établi dès 2009 | [Golle et Partridge](https://crypto.stanford.edu/~pgolle/papers/commute.html), 2009 |
| Le GPS utilise la trilatération, la triangulation et la multilatération (p. 17) | **Contredit** pour la triangulation : le GPS mesure des temps de parcours (pseudo-distances), non des angles | Principe documenté par le gouvernement américain : [GPS.gov — performance](https://www.gps.gov/gps-accuracy) |
| L'AirTag est localisé « en tout temps » grâce à l'UWB (p. 22) | **Nuancé** : la localisation à distance passe par le réseau Bluetooth Localiser ; l'UWB sert à la recherche de proximité | Documentation des constructeurs ; protocole de détection des traceurs : [IETF DULT](https://datatracker.ietf.org/group/dult/about/) |
| Un site peut localiser l'internaute via le navigateur sans requête active (p. 27) | **Nuancé** : l'API de géolocalisation exige une autorisation de l'utilisateur ; la localisation silencieuse passe par l'adresse IP | [W3C — Geolocation API](https://www.w3.org/TR/geolocation-api/) |
| Plus de 75 entreprises, 200 millions d'appareils, un marché de 21 milliards de dollars (p. 38-39) | **Nuancé** : chiffres de l'enquête du *New York Times* ; les 21 milliards désignent la publicité ciblée par la localisation | [*New York Times*](https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html), 10 décembre 2018 |
| Google ne stocke plus l'historique de localisation de façon centralisée (p. 111, note) | **Confirmé** : historique déplacé sur l'appareil, réponse aux mandats de géorepérage devenue impossible | [9to5Google](https://9to5google.com/2023/12/12/google-location-history-timeline-device/), 12 décembre 2023 |
| Le chasseur de primes a obtenu une localisation pour 300 dollars (p. 34) | **Confirmé**, suivi de sanctions fédérales en 2024 | [TechCrunch](https://techcrunch.com/2024/04/30/us-fines-telcos-200m-for-sharing-customer-location-data-without-consent), 30 avril 2024 |

### Contrepoints et critiques

- **La désactivation par défaut se heurte aux usages vitaux.** La localisation des appels d'urgence fonctionne justement sans action de l'appelant : en Europe, la localisation fournie par le téléphone (AML) est transmise automatiquement aux centres de secours ([EENA — Advanced Mobile Location](https://eena.org/advanced-mobile-location/)). Un droit de ne pas être suivi devrait prévoir ces exceptions, que le mémoire ne détaille pas.
- **Les permissions des systèmes ont déjà évolué.** Depuis Android 12, l'utilisateur peut n'accorder qu'une position approximative, et l'application ne reçoit alors qu'une localisation dégradée, y compris en arrière-plan ([Android Developers — approximate location](https://developer.android.com/codelabs/approximate-location)), à l'image de ce qu'Apple avait introduit auparavant. La « réduction de précision » que le mémoire présente comme une piste est donc déjà proposée par défaut aux utilisateurs ; le problème restant tient aux données collectées hors du téléphone (réseau, enchères publicitaires).

### Évolutions depuis la publication

Le mémoire date de novembre 2026 ; aucun fait postérieur n'a été trouvé. Une décision antérieure, absente du texte parce qu'il exclut l'État, mérite d'être signalée : le 29 juin 2026, la Cour suprême des États-Unis a jugé, par six voix contre trois, que l'obtention d'un historique de localisation par un mandat de géorepérage constitue une perquisition au sens du quatrième amendement ([Just Security — « Unpacking the Supreme Court's Chatrie Decision »](https://www.justsecurity.org/145214/chatrie-fourth-amendment-supreme-court/), 2026).

### Pour aller plus loin

- [EFF — « On Locational Privacy, and How to Avoid Losing it Forever »](https://www.eff.org/wp/locational-privacy) — le texte de 2009 qui structure la réflexion du mémoire, toujours éclairant sur l'enjeu de la trace.
- [Rye et Levin — « Surveilling the Masses with Wi-Fi-Based Positioning Systems »](https://arxiv.org/abs/2405.14975) — la démonstration la plus concrète des risques du positionnement Wi-Fi.
- [Andrés *et al.* — « Geo-Indistinguishability »](https://arxiv.org/abs/1212.1984) — le fondement théorique des techniques de brouillage de position.
