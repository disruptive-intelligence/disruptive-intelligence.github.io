---
title: "Géolocalisation : nature, techniques, usages et enjeux de surveillance"
date: 2026-11-22
kind: dossier
slug: "geolocalisation-nature-techniques-usages-et-enjeux-de-surveillance"
themes:
  - cyber
  - tech
  - geo-ie
rubriques:
  - rens-opsec
  - rens-osint
  - tech-infrastructures
tags:
  - géolocalisation
  - GNSS
  - positionnement Wi-Fi
  - données de localisation
  - courtiers en données
  - OPSEC
  - réidentification
  - vie privée
---

# Géolocalisation : nature, techniques, usages et enjeux de surveillance

Date de rédaction : 2026-11-22

## Sources de synthèse

- **[A1]** [Être localisé en permanence : techniques, usages et risques de la géolocalisation](../analyses/etre-localise-en-permanence-techniques-usages-et-risques-de-la-geolocalisation.md)
- **[A2]** [OTAN : la future plateforme OSINT, un achat de données et d'anonymat plus qu'un projet d'IA](../analyses/otan-la-future-plateforme-osint-un-achat-de-donnees-et-d-anonymat-plus-qu-un-projet-d-ia.md)
- **[A3]** [Analyse — SOCMINT : ce que l'IA change au renseignement sur les réseaux sociaux](../analyses/introduction-to-social-media-intelligence-socmint.md)
- **[A4]** [Europol : digital forensics en Europe, les lacunes qui fragilisent la preuve numérique](../analyses/europol-digital-forensic-en-europe-les-lacunes-qui-fragilisent-la-preuve-numerique.md)

Le dossier s'appuie principalement sur [A1], l'analyse d'un mémoire de maîtrise de l'Université de Montréal, et le complète par des sources primaires et des enquêtes récentes citées et datées au fil du texte. Les trois autres analyses éclairent les usages de renseignement, d'enquête et de preuve.

## Sujet et périmètre

La question est simple à poser : **comment sait-on où se trouve un appareil, donc une personne, et qu'en fait-on ?** Le dossier reprend la partie du mémoire analysé dans [A1](../analyses/etre-localise-en-permanence-techniques-usages-et-risques-de-la-geolocalisation.md) qui vaut partout (définitions, technologies, usages, risques, solutions techniques et annexe sur les usages) et laisse de côté son objet principal, le droit québécois. Il l'enrichit sur quatre plans que le mémoire traite peu ou pas : la physique et les performances réelles des technologies, l'économie des données de localisation telle qu'elle fonctionne en 2026, les usages d'État et de renseignement, et la géolocalisation comme risque de sécurité opérationnelle (OPSEC) pour les personnes et les organisations sensibles.

Le cadre juridique n'est abordé que lorsqu'une décision ou une sanction éclaire un fait technique ou un marché ; le dossier n'est pas une étude de droit comparé. Les recherches ont été menées le 22 novembre 2026. Les chiffres de précision sont des ordres de grandeur, qui varient fortement selon le matériel, l'environnement et la méthode de mesure. Les attributions aux analyses internes sont signalées par [A1] à [A4] ; une conclusion qui rapproche plusieurs sources est présentée comme synthèse du dossier.

## Résumé exécutif

La géolocalisation est la détermination de la position d'un appareil à un instant donné. Elle ne dit pas qui tient l'appareil, mais elle en est un très fort indice ; et comme elle se répète, elle produit des **traces** qui racontent une vie : domicile, travail, soins, culte, relations. Toute la difficulté du sujet tient à ce passage du point à la trace. Un point isolé est banal ; une trace est presque toujours unique. Quatre points dans le temps et l'espace suffisent à distinguer 95 % des personnes d'une base de 1,5 million d'abonnés mobiles, et l'anonymat de la paire domicile-travail s'effondre dès qu'on la connaît à l'échelle du pâté de maisons [A1].

Les technologies se répartissent en quelques principes physiques : la **proximité** (on est près de telle antenne ou de telle balise), la **mesure de distance** par le temps de parcours ou la puissance d'un signal, la **mesure d'angle**, et la **reconnaissance d'empreinte** radio. Les satellites (GPS, Galileo et autres GNSS) donnent quelques mètres en plein air ; le Wi-Fi prend le relais en ville et en intérieur ; le réseau mobile localise tout téléphone allumé, de façon plus grossière mais sans rien demander ; Bluetooth et ultra-large bande descendent au mètre, voire au décimètre ; l'adresse IP et l'inférence complètent le tableau. Un téléphone moderne fusionne ces sources en permanence. Chaque technologie laisse aussi une trace chez un acteur différent : le téléphone, l'éditeur du système, l'opérateur, le fournisseur d'accès, l'application, et derrière elle toute la chaîne publicitaire.

Les usages se divisent entre un **marché primaire**, où la position sert le service demandé (navigation, urgences, antifraude, logistique), et un **marché secondaire**, où elle est revendue. Ce second marché, alimenté par les kits de développement intégrés aux applications et par les enchères publicitaires en temps réel, a produit des bases de milliards de points vendues à des annonceurs, des fonds, des enquêteurs privés et des administrations. Les enquêtes de 2024-2025 ont montré qu'il permettait de suivre des militaires de l'OTAN, des agents de renseignement et des fonctionnaires européens. La géolocalisation est donc devenue un sujet de sécurité nationale autant que de vie privée.

Les risques sont multiples : profilage et inférence de données sensibles, surveillance au travail, contrôle coercitif dans le couple, traque par traceurs Bluetooth, fuites et piratages de courtiers, discrimination tarifaire, erreurs aux conséquences financières ou judiciaires, et vulnérabilité des systèmes eux-mêmes au brouillage et au leurrage. Les protections techniques existent (permissions fines, position approximative, traitement sur l'appareil, conservation courte, randomisation des identifiants, confidentialité différentielle, cryptographie, authentification des signaux), mais aucune ne neutralise seule le risque principal : **l'accumulation de traces par des acteurs que l'utilisateur ne voit pas**.

## 1. Ce qu'est la géolocalisation

### 1.1 Une position d'appareil, un indice de présence

Le mémoire reprend la définition de l'Office québécois de la langue française : la géolocalisation est la « détermination plus ou moins précise, par des moyens technologiques, de la position géographique d'un appareil électronique à un moment donné » [A1]. Trois mots comptent. **Appareil** : on localise un téléphone, une voiture, une étiquette, pas une personne ; la présence de l'utilisateur n'est qu'une présomption, que le prêt, l'oubli ou le vol du téléphone peuvent démentir. **Plus ou moins précise** : la même question, « où est cet appareil ? », reçoit selon la technologie une réponse au centimètre ou à la dizaine de kilomètres. **À un moment donné** : la donnée est spatio-temporelle ; sans horodatage, une position ne dit presque rien.

Quatre propriétés techniques permettent de comparer toutes les sources de localisation et reviennent tout au long du dossier :

- **La précision** est l'écart entre la position estimée et la position réelle, souvent exprimée comme un rayon contenant la vraie position dans 68 % ou 95 % des cas ; un téléphone affiche généralement ce rayon sous forme de cercle bleu autour du point.
- **La disponibilité** désigne les lieux et conditions où la technologie fonctionne : le satellite en plein air, le Wi-Fi en ville et en intérieur, le réseau mobile presque partout.
- **La fréquence** est le nombre de positions relevées par unité de temps ; c'est elle qui transforme des points en trajectoire.
- **La persistance** est la durée de conservation ; c'est elle qui transforme une trajectoire en historique de vie.

*Synthèse du dossier :* la précision fait le risque d'un point, la fréquence et la persistance font le risque d'une trace. Un relevé au kilomètre près, mais horaire et conservé un an, est plus intrusif qu'une position au mètre près relevée une seule fois.

### 1.2 Trois natures de l'information de localisation

Le mémoire distingue trois formes de données de localisation [A1] :

1. **L'information géospatiale** : des coordonnées (latitude, longitude, altitude) dans un système de référence ; c'est la forme que produisent les capteurs.
2. **L'information civique** : une position exprimée dans un découpage humain et politique (pays, fuseau horaire, code postal, commune, adresse).
3. **L'information descriptive** : la nature du lieu (église, école, restaurant, clinique).

C'est le passage de la première à la troisième qui rend la donnée sensible. Une coordonnée n'est qu'un nombre ; reliée par géocodage inverse à une adresse, puis à une base de « points d'intérêt », elle devient « clinique d'avortement », « mosquée », « bar homosexuel », « siège d'un syndicat » ou « entrée d'une base militaire ». Le mémoire donne l'exemple de la fréquentation d'une clinique de santé sexuelle, qui peut révéler l'état de santé ou l'orientation sexuelle [A1].

L'analyse des trajectoires ajoute une quatrième couche que le mémoire évoque sans la nommer : la **sémantique des séjours**. Les algorithmes de traitement des traces repèrent les « points de séjour » (lieux où l'appareil reste immobile un certain temps), puis les classent : lieu de la nuit (domicile probable), lieu des jours ouvrés (travail probable), lieux récurrents (sport, culte, soins), lieux rares (événements). C'est cette inférence automatique, peu coûteuse, qui fait de chaque jeu de données de mobilité un annuaire potentiel des habitudes.

### 1.3 Les sujets de la géolocalisation

Le mémoire distingue trois catégories de « sujets » localisés [A1] : les **objets** (colis, conteneurs, matériel médical, palettes), les **objets mobiles par nature** (voitures, camions, avions, rames de métro, bus) et les **personnes**, soit comme individus identifiables, soit dans le cadre de leur fonction (policier, camionneur, facteur). Le cas des personnes est le plus sensible, mais la frontière est poreuse : le traceur glissé dans un sac pour retrouver ses clés devient un outil de traque s'il est caché dans la voiture d'un tiers, et la télématique d'un véhicule de société suit en réalité son conducteur. *Synthèse du dossier :* en matière de risque, il faut raisonner sur la personne la plus probablement associée à l'objet, pas sur l'objet lui-même.

### 1.4 Qui calcule la position, et qui la voit

Le mémoire oppose la localisation **calculée par le terminal**, dont le GPS est l'exemple, et la localisation **calculée par le réseau**, sur laquelle l'utilisateur n'a ni contrôle ni visibilité [A1]. La réalité est plus fine, et la distinction pertinente pour la vie privée porte sur **qui détient le résultat** :

- **Calcul sur l'appareil, sans échange** : le récepteur GNSS calcule seul à partir de signaux reçus ; personne d'autre ne connaît la position tant que l'appareil ne la transmet pas.
- **Calcul assisté** : l'appareil envoie des informations (identifiants des bornes Wi-Fi et des antennes visibles) à un service de localisation qui lui renvoie une position ; l'éditeur de ce service apprend alors où se trouve l'appareil.
- **Calcul par le réseau** : l'opérateur mobile estime la position à partir de ses propres mesures, que le téléphone soit configuré ou non pour la localisation.
- **Calcul par des tiers** : un site web déduit une zone de l'adresse IP, une enseigne repère un téléphone grâce à ses capteurs Wi-Fi ou Bluetooth, une caméra lit une plaque d'immatriculation.

À cette distinction s'ajoute celle de la **collecte active ou passive**, que le mémoire juge déterminante [A1] : l'utilisateur qui partage sa position sait qu'il la transmet ; celui dont l'application relève la position en arrière-plan, ou dont le téléphone signale sa présence aux bornes voisines, ne le sait pas.

### 1.5 Les grandes catégories d'utilisation

Le mémoire regroupe les usages en trois catégories, auxquelles le dossier ajoute deux opérations voisines [A1] :

- **Le géomarquage** associe une position à un contenu : la photo dont le fichier contient des coordonnées dans ses métadonnées EXIF, la publication « à tel endroit », le message localisé. Il est en principe volontaire, mais la position peut être conservée et réutilisée par la plateforme, et les métadonnées d'une photo envoyée en pièce jointe accompagnent souvent le fichier à l'insu de son auteur.
- **Le géocodage** convertit une adresse ou un nom de lieu en coordonnées ; le **géocodage inverse** fait l'opération contraire. Chaque recherche sur un service de cartographie est un géocodage ; enregistrée, elle révèle les intentions de déplacement, avant même le déplacement.
- **Le géoréférencement** situe précisément une entité sur une carte. Le mémoire prend l'exemple du bracelet électronique judiciaire ; le terme désigne aussi, en cartographie, le calage d'une image ou d'un plan dans un système de coordonnées.
- **Le géorepérage** (*geofencing*) déclenche une action lorsqu'un appareil franchit une frontière virtuelle : promotion à l'entrée d'un magasin, alerte quand un enfant quitte l'école, pointage d'un salarié, verrouillage d'un appareil hors d'un périmètre [A1]. Il en existe une version policière, le « mandat de géorepérage », qui demande à un fournisseur la liste des appareils présents dans une zone à un moment donné (voir la partie 3).
- **La géolocalisation d'images**, discipline de l'OSINT, retrouve le lieu d'une photo ou d'une vidéo à partir de son contenu (relief, bâtiments, signalisation, végétation, ombres), souvent avec sa **chronolocalisation**, c'est-à-dire sa datation. [A3] rappelle que Bellingcat et le Centre for Information Resilience géolocalisent et datent ainsi les images de la guerre en Ukraine, puis les font vérifier par des enquêteurs confirmés.

### 1.6 Repères de vocabulaire

- **GNSS** — *Global Navigation Satellite System* : terme générique pour les constellations de navigation par satellite (GPS américain, Galileo européen, GLONASS russe, BeiDou chinois).
- **Pseudo-distance** — distance satellite-récepteur déduite du temps de parcours du signal, entachée de l'erreur d'horloge du récepteur ; c'est la mesure de base du GNSS.
- **Trilatération** — calcul d'une position à partir de distances à au moins trois points connus.
- **Multilatération** — calcul d'une position à partir de différences de temps d'arrivée d'un même signal en plusieurs points (TDoA).
- **Triangulation** — calcul d'une position à partir d'angles mesurés depuis des points connus ; c'est le principe de l'angle d'arrivée (AoA), pas celui du GNSS.
- **RSSI** — indicateur de puissance du signal reçu, utilisé pour estimer grossièrement une distance.
- **Temps de vol / temps d'aller-retour (ToF, RTT)** — mesure du temps de parcours d'un signal pour en déduire une distance, base de l'UWB et du Wi-Fi RTT.
- **Empreinte radio (*fingerprinting*)** — comparaison des signaux observés à une carte de signaux relevée à l'avance.
- **BSSID** — identifiant matériel unique d'une borne Wi-Fi, analogue à son adresse MAC ; c'est lui que les bases de positionnement Wi-Fi associent à une position.
- **Cell-ID** — identifiant de la cellule radio à laquelle un téléphone est rattaché ; la position de l'antenne donne une localisation grossière.
- **Identifiant publicitaire (MAID)** — identifiant d'appareil mis à disposition des applications pour la publicité (IDFA chez Apple, AAID chez Google) ; il sert de clé de jointure dans les bases des courtiers.
- **SDK** — kit de développement logiciel intégré à une application ; certains collectent la position pour le compte d'un tiers.
- **Enchères en temps réel (RTB)** — mécanisme publicitaire où chaque affichage est mis aux enchères en quelques millisecondes, la requête diffusée aux enchérisseurs contenant souvent la position de l'appareil.
- **Point de séjour (*stay point*)** — lieu où un appareil reste immobile assez longtemps pour être considéré comme une visite ; c'est l'unité de base de l'inférence des habitudes.
- **Brouillage / leurrage** — émission d'un bruit qui empêche la réception GNSS / émission de faux signaux qui font calculer une fausse position.
- **LPPM** — *Location Privacy Preserving Mechanisms*, mécanismes de protection de la vie privée de localisation [A1].

## 2. Comment on localise : panorama technique

### 2.1 Quatre principes physiques

Toutes les technologies reposent sur un petit nombre de principes, que le mémoire mélange parfois ; il présente notamment la triangulation comme une méthode GPS [A1], ce qui est inexact. Le principe détermine la précision atteignable et la trace laissée :

1. **La proximité** : on sait qu'un appareil est près d'un émetteur ou d'un capteur dont on connaît la position (antenne relais, borne Wi-Fi, balise Bluetooth, lecteur RFID, portique). Précision égale à la portée : de quelques centimètres pour le NFC à plusieurs kilomètres pour une antenne rurale.
2. **La mesure de distance** : on mesure le temps de parcours d'un signal (GNSS, ultra-large bande, Wi-Fi RTT, avance temporelle du réseau mobile) ou, moins bien, l'affaiblissement de sa puissance (RSSI). Trois distances à des points connus donnent une position dans un plan, quatre dans l'espace.
3. **La mesure d'angle** : un réseau d'antennes mesure la direction d'arrivée d'un signal (Bluetooth 5.1, ultra-large bande, 5G) ; deux directions suffisent à fixer un point.
4. **La reconnaissance d'empreinte** : on compare ce que l'appareil « voit » (liste de bornes et puissances, champ magnétique) à une carte relevée à l'avance ; c'est le principe du positionnement Wi-Fi et de nombreux systèmes d'intérieur.

À ces principes s'ajoute la **navigation à l'estime** : accéléromètre, gyroscope, magnétomètre et baromètre permettent de prolonger une trajectoire entre deux positions connues, de compter les pas ou de déterminer l'étage. Les systèmes d'exploitation combinent toutes ces mesures dans un service de **fusion** (par exemple le *Fused Location Provider* d'Android) qui choisit, selon la précision demandée et la batterie, la meilleure combinaison. *Synthèse du dossier :* l'utilisateur ne sait presque jamais quelle technologie l'a localisé ; il voit seulement l'interrupteur « localisation », qui ne couvre pas toutes les sources.

### 2.2 Les systèmes satellitaires (GNSS)

Chaque satellite GNSS diffuse en continu un signal horodaté par une horloge atomique et la description de son orbite. Le récepteur mesure le temps de parcours du signal, en déduit une pseudo-distance et résout un système d'équations à quatre inconnues (trois coordonnées et l'erreur de sa propre horloge), d'où le besoin de **quatre satellites** au moins. Le calcul se fait entièrement dans le récepteur, qui ne transmet rien : le GNSS est en soi la technologie la plus respectueuse de la vie privée, et c'est ce qui en est fait ensuite qui pose problème.

Le mémoire retient une précision de 4 à 15 mètres par ciel dégagé, d'après un avis européen de 2011, et souligne la dégradation en ville et la parade de l'**A-GPS**, qui fournit au téléphone, par le réseau mobile, les données d'orbite et une position approchée pour accélérer la première localisation [A1]. Les ordres de grandeur actuels sont plus fins et plus nuancés :

- **Le signal lui-même** : la norme de service du GPS fixe une erreur de distance satellite-utilisateur inférieure à 7 mètres dans 95 % des cas en moyenne mondiale, mais cet engagement porte sur le signal dans l'espace, pas sur le récepteur ([GPS.gov — accuracy](https://www.gps.gov/gps-accuracy)).
- **Le téléphone** : quelques mètres en plein air pour un récepteur ordinaire, beaucoup moins bien en « canyon urbain », où les signaux rebondissent sur les façades (multitrajets). Les puces **bifréquences** (L1 et L5) apparues à partir de 2018 réduisent ces erreurs ; des études mesurent de 1 à 5 mètres selon les conditions et les traitements ([revue sur le GNSS des smartphones](https://pmc.ncbi.nlm.nih.gov/articles/PMC9788430/), 2022).
- **Le haut de gamme** : le service de haute précision de Galileo (HAS), disponible depuis janvier 2023, vise **20 centimètres** à l'horizontale, mais ses corrections passent par une bande que les téléphones grand public ne reçoivent généralement pas ([ESA — « New Galileo service set to deliver 20 cm accuracy »](https://www.esa.int/Applications/Satellite_navigation/New_Galileo_service_set_to_deliver_20_cm_accuracy)).

Le GNSS a deux faiblesses structurelles que le mémoire ne traite pas. Ses signaux arrivent au sol avec une puissance infime, ce qui les rend faciles à **brouiller** ; et le signal civil n'était pas authentifié, ce qui permet de le **leurrer** en diffusant de faux signaux. Depuis 2022, ces interférences sont devenues massives autour de la mer Baltique, de la mer Noire et du Proche-Orient : un rapport de six pays à l'OACI fait état d'environ **123 000 vols perturbés** entre janvier et avril 2025 dans la région baltique, et la Suède a compté 733 incidents dans son espace aérien début septembre 2025, contre 55 en 2023 ([Moscow Times](https://www.themoscowtimes.com/2025/09/04/sweden-accuses-russia-of-widespread-gps-jamming-over-baltic-sea-a90427/pdf), 4 septembre 2025). L'Agence européenne de la sécurité aérienne suit le phénomène dans un bulletin régulièrement révisé ([EASA — GNSS outages and alterations](https://www.easa.europa.eu/en/domains/air-operations/global-navigation-satellite-system-outages-and-alterations)). La parade européenne est l'**authentification des messages de navigation** de Galileo (OSNMA), service gratuit déclaré opérationnel, qui permet au récepteur de vérifier qu'un signal provient bien de la constellation ([GPS World](https://www.gpsworld.com/galileo-osnma-authentification-service-now-operational/)). *Synthèse du dossier :* pour un usage de preuve ou de sécurité, une position GNSS n'est fiable que si l'on peut exclure le leurrage, ce qui n'est presque jamais documenté dans les données commerciales.

### 2.3 Le positionnement Wi-Fi

Le positionnement Wi-Fi (WPS) repose sur une base de données qui associe des millions de bornes, identifiées par leur BSSID, à une position. Le téléphone relève les bornes qu'il « voit » et leur puissance, interroge la base et reçoit une position, ou compare ce relevé à une empreinte radio enregistrée [A1]. Le mémoire souligne trois points : la technique marche bien en intérieur et en ville, là où le GNSS faiblit ; elle atteint quelques mètres, voire mieux dans des environnements équipés (temps de vol, angle d'arrivée) ; et elle fonctionne en arrière-plan, sans que l'utilisateur en ait conscience [A1].

Le mémoire n'explique pas comment ces bases sont constituées, ce qui est pourtant le cœur du sujet. Elles sont alimentées par la **collecte participative** : chaque téléphone dont la localisation est active transmet régulièrement à l'éditeur de son système la liste des bornes visibles et sa position GNSS ; quelques milliards d'appareils cartographient ainsi en continu les bornes du monde entier. Il en découle deux conséquences rarement perçues :

- **L'éditeur du service apprend la position de l'appareil qui l'interroge.** C'est le prix du calcul assisté ; il est encadré par les politiques des éditeurs, mais il existe.
- **Les bornes elles-mêmes deviennent traçables.** En 2024, Erik Rye et Dave Levin (université du Maryland) ont montré que la base d'Apple pouvait être interrogée massivement pour reconstituer la position de centaines de millions de bornes, puis suivre celles qui se déplacent, comme les routeurs de voyage ou les terminaux Starlink, y compris en Ukraine et à Gaza ([Rye et Levin, arXiv](https://arxiv.org/abs/2405.14975), 23 mai 2024 ; présentation à Black Hat USA 2024). La parade immédiate consiste à ajouter le suffixe « _nomap » au nom du réseau, que Google et Apple respectent pour exclure la borne de leurs bases ; la parade de fond, la randomisation des BSSID, n'est pas normalisée ([The Register](https://www.theregister.com/2024/05/23/apple_wifi_positioning_system), 23 mai 2024).

Le Wi-Fi sert aussi à la localisation **par l'infrastructure** : un réseau d'entreprise, de centre commercial ou d'aéroport peut repérer les téléphones qui le sondent. La randomisation des adresses MAC lors des recherches de réseaux, généralisée sur les téléphones récents, limite ce suivi passif ; elle ne l'empêche plus dès que l'appareil se connecte.

### 2.4 Le réseau mobile

Un téléphone allumé se signale en permanence à son réseau, qui doit savoir à quelle cellule acheminer les appels. Le mémoire décrit une localisation estimative, plus rapide et moins gourmande que le GNSS, de quelques centaines de mètres en ville à plusieurs kilomètres à la campagne, utilisable sans aucune action de l'utilisateur [A1]. Plusieurs méthodes coexistent, de la plus grossière à la plus fine :

- **Cell-ID** : la position de l'antenne et l'orientation du secteur.
- **Avance temporelle et mesures de puissance** (E-CID) : une distance à l'antenne qui réduit la zone à un anneau.
- **Différences de temps d'arrivée** (OTDOA) entre plusieurs antennes, et mesures du réseau lui-même.
- **Positionnement 5G** : la norme 3GPP a fixé des objectifs commerciaux de l'ordre de 3 mètres en intérieur pour la version 16, puis inférieurs au mètre pour la version 17, avec des cibles de quelques dizaines de centimètres pour l'industrie ([Nokia, livre blanc sur le positionnement 5G](https://www.nokia.com/asset/f/210289)). Le réseau mobile, historiquement grossier, devient un instrument de localisation précis.

Trois enjeux en découlent. **Les opérateurs détiennent un historique de localisation de tous leurs abonnés**, que l'utilisateur ne peut pas désactiver ; le mémoire rappelle l'enquête canadienne sur l'usage de ces données « dépersonnalisées » pendant la pandémie [A1]. **Ces données ont été vendues** : aux États-Unis, la Federal Communications Commission a infligé en avril 2024 près de 200 millions de dollars d'amendes à quatre opérateurs qui avaient revendu la localisation de leurs clients à des agrégateurs, chaîne qui avait permis à un chasseur de primes de localiser un téléphone contre 300 dollars ([TechCrunch](https://techcrunch.com/2024/04/30/us-fines-telcos-200m-for-sharing-customer-location-data-without-consent), 30 avril 2024). **La signalisation entre opérateurs est exploitable** : le protocole SS7, conçu pour l'itinérance, permet à qui accède au réseau d'interroger la position d'un abonné étranger. L'enquête « Surveillance Secrets » de Lighthouse Reports a documenté en octobre 2025 l'outil Altamides de la société First Wap, qui louait des adresses d'opérateurs pour localiser des téléphones ; ses 1,5 million de relevés fuités couvrent des milliers de numéros dans plus de 160 pays entre 2007 et 2014 ([Schneier on Security](https://www.schneier.com/blog/archives/2025/10/first-wap-a-surveillance-computer-youve-never-heard-of.html), octobre 2025). Les « IMSI-catchers », fausses antennes qui forcent les téléphones voisins à s'y rattacher, complètent l'arsenal des services et des criminels.

Le réseau mobile est enfin la colonne vertébrale de la **localisation des appels d'urgence**. En Europe, le système AML (*Advanced Mobile Location*) fait transmettre automatiquement par le téléphone sa position GNSS ou Wi-Fi au centre de secours, par SMS ou HTTPS, sans action de l'appelant ; les centres reçoivent cette position pour 30 à 97 % des appels mobiles selon les pays, alors que la localisation par le réseau seul ne situe l'appelant qu'entre 300 mètres et 25 kilomètres ([EENA — Advanced Mobile Location](https://eena.org/advanced-mobile-location/) ; [rapport 2023](https://eena.org/knowledge-hub/documents/aml-report-card-2023-update)).

### 2.5 Bluetooth, ultra-large bande et traceurs

Les **balises Bluetooth basse consommation** émettent à intervalles réguliers un identifiant ; un téléphone qui les capte estime la distance d'après la puissance du signal, ou la direction grâce à l'angle d'arrivée introduit par Bluetooth 5.1 [A1]. Elles servent au guidage en intérieur, au marketing de proximité et à l'inventaire. La version 6.0 de la norme (2024) ajoute la **mesure de distance par sondage de canal** (*Channel Sounding*), qui combine phase et temps d'aller-retour pour viser une précision décimétrique ([Bluetooth SIG — « True distance awareness with Bluetooth Channel Sounding »](https://www.bluetooth.com/blog/true-distance-awareness-with-bluetooth-channel-sounding/)).

L'**ultra-large bande** (UWB) émet des impulsions très brèves sur une large bande de fréquences ; leur temps de vol se mesure finement, d'où une précision de l'ordre de la dizaine de centimètres et une bonne résistance aux réflexions [A1]. Elle équipe les téléphones haut de gamme, les clés de voiture « mains libres » et les traceurs.

Le mémoire illustre l'UWB par l'AirTag d'Apple. La précision s'impose : un traceur de ce type est localisé à distance grâce au **réseau participatif** des téléphones voisins, qui captent son signal Bluetooth et remontent, chiffrée, leur propre position au propriétaire ; l'UWB ne sert qu'à la « recherche précise » dans les derniers mètres. Apple (réseau Localiser) et Google (réseau Find Hub, ex-Localiser mon appareil) disposent ainsi de réseaux de plusieurs centaines de millions de téléphones qui servent de capteurs. Ces traceurs bon marché ont été détournés pour suivre des personnes à leur insu ; Apple et Google ont proposé une spécification commune de détection des traceurs indésirables, reprise par le groupe de travail DULT de l'IETF, qui n'a pas encore abouti à une norme finalisée ([IETF — DULT](https://datatracker.ietf.org/group/dult/about/) ; [EFF](https://www.eff.org/deeplinks/2023/08/industry-discussion-about-standards-bluetooth-enabled-physical-trackers-finally), août 2023).

### 2.6 RFID et NFC

L'identification par radiofréquence associe une étiquette (puce et antenne), un lecteur et une base de données [A1]. Les étiquettes **passives**, sans batterie, ne répondent qu'à quelques centimètres ou quelques mètres du lecteur ; les étiquettes **actives**, alimentées, portent beaucoup plus loin. La RFID ne localise que par proximité d'un lecteur ; sa force est l'identification unique de chaque objet. Le mémoire montre comment elle glisse vers le suivi des personnes : une étiquette restée dans un vêtement ou un portefeuille peut être relue en magasin ou ailleurs, et rattachée à l'acheteur par son paiement [A1]. Les badges d'accès, les cartes de transport et les péages électroniques relèvent de la même logique : chaque passage devant un lecteur est un point horodaté.

### 2.7 Adresse IP, cookies et navigateur

L'adresse IP n'est pas une technologie de localisation, mais elle permet d'en faire. Des bases commerciales associent les plages d'adresses à un pays, une région ou une ville, à partir des registres, du routage, des déclarations des fournisseurs et de mesures ; leur précision est bonne au niveau du pays, médiocre au-delà [A1]. Elle suffit pour le blocage géographique, l'antifraude, la conformité réglementaire et la publicité locale. Le fournisseur d'accès, lui, sait relier une adresse à un abonné et à son adresse postale ; la Cour suprême du Canada a reconnu en 2024 une attente raisonnable de vie privée sur l'adresse IP pour cette raison [A1]. Associée aux cookies et aux autres identifiants de navigation, l'IP permet de suivre un internaute d'un site à l'autre et de rattacher ses sessions à des lieux.

Le mémoire décrit aussi la « navigation web géolocalisée », où des scripts demandent la position de l'internaute [A1]. La norme du W3C fait de la géolocalisation une fonction « puissante » soumise à l'autorisation de l'utilisateur, et interdit par défaut son usage aux contenus tiers intégrés dans une page ([W3C — Geolocation API](https://www.w3.org/TR/geolocation-api/)). Lorsqu'elle est accordée, le navigateur s'appuie sur le service de localisation du système (GNSS, Wi-Fi). *Synthèse du dossier :* la localisation web silencieuse passe moins par cette interface que par l'adresse IP et par la publicité, qui diffuse la position aux enchérisseurs (partie 3).

### 2.8 La localisation inférée et l'IA

Le mémoire range à part la **localisation inférée**, déduite d'éléments sans coordonnées : un paiement par carte, une entrée d'agenda, un historique, une publication [A1]. Il souligne qu'elle peut servir à contourner les restrictions qui visent les capteurs. Deux évolutions lui donnent une portée nouvelle :

- **L'inférence à partir des traces des autres.** Les réseaux sociaux, les photos de groupe, les réservations et les objets connectés d'un entourage situent une personne qui n'a rien partagé.
- **La géolocalisation d'images par l'IA.** Le mémoire cite GeoLocator, qui retrouvait l'adresse exacte dans 54 % des cas [A1]. En avril 2025, la « recherche de lieu inversée » avec le modèle o3 d'OpenAI est devenue une mode sur les réseaux, sans recours aux métadonnées ([TechCrunch](https://techcrunch.com/2025/04/17/the-latest-viral-chatgpt-trend-is-doing-reverse-location-search-from-photos), 17 avril 2025), et une étude a montré qu'un tel modèle pouvait estimer l'adresse d'une résidence privée à partir d'indices discrets ([« Doxing via the Lens », arXiv](https://arxiv.org/abs/2504.19373v1), avril 2025). L'OTAN liste d'ailleurs la « géolocalisation automatisée » parmi les fonctions attendues de sa future plateforme OSINT, sans exigence de fiabilité [A2].

### 2.9 Tableau récapitulatif

| Technologie | Principe | Précision typique | Fonctionne en intérieur | Qui connaît la position |
| --- | --- | --- | --- | --- |
| GNSS (GPS, Galileo…) | Temps de parcours depuis au moins 4 satellites | Quelques mètres en plein air ; 1 à 5 m en bifréquence ; décimétrique en haut de gamme | Mal | L'appareil seul, tant qu'il ne transmet pas |
| A-GPS / localisation assistée | GNSS aidé par le réseau ou un serveur | Celle du GNSS, plus vite | Mieux que le GNSS seul | Le serveur d'assistance apprend une position approchée |
| Wi-Fi (WPS) | Bornes visibles comparées à une base ou à une empreinte | Quelques mètres à quelques dizaines de mètres ; mieux en environnement équipé | Bien | L'éditeur de la base, si le calcul est assisté ; l'opérateur du réseau Wi-Fi |
| Réseau mobile 2G-4G | Cellule, avance temporelle, différences de temps | Centaines de mètres en ville, kilomètres à la campagne | Oui | L'opérateur, en permanence |
| Réseau 5G | Temps, angles, faisceaux | Objectifs normatifs de quelques mètres à moins d'un mètre | Oui | L'opérateur |
| Bluetooth basse consommation | Proximité, puissance, angle ; distance en Bluetooth 6.0 | Mètre ; décimétrique visé en 6.0 | Bien | L'application ou l'infrastructure qui capte |
| Ultra-large bande | Temps de vol d'impulsions brèves | Dizaine de centimètres | Bien | Les appareils qui mesurent |
| Traceurs à réseau participatif | Bluetooth relayé par les téléphones voisins | Celle du téléphone relais | Oui | Le propriétaire du traceur, l'éditeur du réseau (chiffré) |
| RFID / NFC | Proximité d'un lecteur | Portée du lecteur | Oui | L'exploitant des lecteurs |
| Adresse IP | Bases de correspondance | Pays, région, ville ; abonné pour le fournisseur d'accès | Sans objet | Sites, régies, fournisseur d'accès |
| Localisation inférée et IA | Déduction à partir de contenus et de transactions | Très variable, parfois l'adresse | Sans objet | Quiconque dispose des contenus |

## 3. Usages : du service rendu au marché de la trace

### 3.1 Le marché primaire : onze secteurs

Le mémoire appelle marché primaire l'usage de la position pour répondre à un besoin exprimé par l'utilisateur, et le décrit en annexe en onze secteurs [A1]. On peut les regrouper par finalité :

- **Se déplacer.** La navigation (Google Maps, Waze) exploite la position en temps réel pour calculer des itinéraires, estimer le trafic et proposer des résultats locaux ; les systèmes de transport intelligents relient infrastructures, véhicules et centres de gestion ; la télématique automobile ajoute l'assistance, le suivi des véhicules volés et, pour les véhicules autonomes, des volumes considérables de données de capteurs [A1]. [A4] rappelle que la police scientifique peine à acquérir ces données de véhicules, faute d'outils adaptés aux formats des constructeurs.
- **Être secouru ou protégé.** Les appels d'urgence transmettent automatiquement la position de l'appelant ; les applications de sécurité permettent de partager sa position avec des proches ; les traceurs retrouvent bagages et objets [A1].
- **Vendre et recommander.** Le marketing de proximité envoie une offre quand le client entre dans un magasin (géorepérage) ou cible une zone ; le profilage des lieux fréquentés personnalise les offres [A1].
- **Évaluer un risque.** Les assureurs proposent des tarifs fondés sur la conduite (vitesse, freinage, heures et lieux de déplacement), y compris au Québec ; les banques confrontent la position du téléphone à celle de la transaction pour détecter la fraude [A1].
- **Encadrer le travail.** Les employeurs suivent véhicules et salariés mobiles pour la productivité, la sécurité et les coûts, avec un risque de dérive vers le contrôle permanent [A1].
- **Se soigner et s'entraîner.** Montres, bracelets et applications sportives enregistrent les parcours et les partagent volontiers ; assureurs et employeurs peuvent offrir des avantages en échange de ces données [A1].
- **Juger et enquêter.** Le bracelet électronique contrôle une assignation à résidence ou une interdiction de lieu, mais « permet d'établir où un individu se trouve, il ne permet pas de savoir ce qu'il fait » ; les données de localisation servent aussi à situer un accusé, avec une valeur probante qui dépend de la technologie [A1].

### 3.2 Le marché secondaire : comment la position circule

Le mémoire décrit un marché secondaire où des agrégateurs revendent des données individualisées ou prétendument anonymes, et l'illustre par l'enquête du *New York Times* de 2018 : plus de 75 entreprises recevaient des positions précises d'applications, certaines suivant jusqu'à 200 millions d'appareils aux États-Unis, parfois plus de 14 000 fois par jour [A1] ([*New York Times*](https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html), 10 décembre 2018). Il ne détaille pas les tuyaux par lesquels la donnée sort des téléphones. Ils sont au nombre de trois :

1. **Les SDK intégrés aux applications.** Un éditeur d'application météo, de jeu ou de prière intègre un kit fourni par un courtier, qui relève la position et la lui transmet, souvent en échange d'une rémunération ; l'utilisateur a autorisé la localisation pour l'application, pas pour le courtier.
2. **Le flux des enchères publicitaires (RTB).** À chaque affichage publicitaire, une requête contenant l'identifiant publicitaire et souvent la position de l'appareil est diffusée à des centaines d'acteurs ; seul l'un d'eux gagne l'enchère, mais tous reçoivent la donnée. Selon l'Irish Council for Civil Liberties, Google diffusait ces données à plus de 2 000 entités, et l'outil Patternz, commercialisé par une société israélienne, revendique la localisation en temps réel de cibles à partir de ce flux ([CyberInsider, d'après l'ICCL](https://cyberinsider.com/rtb-data-leveraged-for-user-surveillance-by-non-state-agencies/)) ; le service américain des douanes (CBP) a reconnu acheter des positions issues des enchères publicitaires ([EFF](https://www.eff.org/deeplinks/2025/01/online-behavioral-ads-fuel-surveillance-industry-heres-how), janvier 2025 ; [EFF](https://www.eff.org/deeplinks/2026/03/targeted-advertising-gives-your-location-government-just-ask-cbp), mars 2026).
3. **Les opérateurs et les objets connectés.** Opérateurs mobiles (jusqu'aux sanctions américaines), constructeurs automobiles, fabricants d'objets connectés revendent ou partagent des données de position et de conduite.

La donnée est ensuite **agrégée et enrichie** : l'identifiant publicitaire sert de clé pour joindre les sources ; les points de séjour sont rapprochés de bases de lieux ; des « audiences » sont constituées (« visiteurs de concessionnaires », « personnes ayant fréquenté telle clinique »). Le mémoire montre que l'identifiant persistant attribué à chaque appareil, même sans nom, suffit à suivre la personne et à recouper les bases [A1]. Les acheteurs sont des annonceurs, des enseignes qui choisissent un emplacement, des fonds d'investissement qui comptent les visiteurs des magasins d'une entreprise cotée, des enquêteurs privés, et des administrations.

### 3.3 Ce que les enquêtes de 2024-2026 ont révélé

Les enquêtes récentes ont mesuré l'ampleur du phénomène et ses conséquences pour la sécurité :

- **Les « Databroker Files ».** En juillet 2024, netzpolitik.org et la radio publique bavaroise ont obtenu gratuitement, comme échantillon commercial d'un courtier américain, **3,6 milliards de positions** de quelque 11 millions d'appareils en Allemagne sur deux mois fin 2023. Elles permettaient de suivre des militaires sur des bases américaines et de l'OTAN, des agents de renseignement et des responsables politiques ; l'enquête a été étendue en 2025 au personnel des institutions européennes ([netzpolitik.org](https://netzpolitik.org/2024/data-broker-files-how-data-brokers-sell-our-location-data-and-jeopardise-national-security/), 2024 ; [netzpolitik.org — « Targeting the EU »](https://netzpolitik.org/2025/databroker-files-targeting-the-eu/), 2025).
- **Le piratage de Gravy Analytics.** En janvier 2025, ce courtier a perdu des données de localisation ; l'échantillon publié désignait des milliers d'applications sources, dont des applications de rencontre, de santé reproductive, de transport et des jeux grand public ([TechCrunch](https://techcrunch.com/2025/01/13/gravy-analytics-data-broker-breach-trove-of-location-data-threatens-privacy-millions/), 13 janvier 2025). Le mémoire évoquait le risque de piratage des bases de localisation [A1] ; il s'est réalisé au cœur du marché.
- **L'outing d'un prêtre.** En 2021, la lettre d'information catholique *The Pillar* a utilisé des « données de signal d'applications disponibles commercialement » pour établir qu'un haut responsable de la conférence des évêques américains fréquentait des lieux homosexuels via l'application Grindr ; il a démissionné ([NBC News](https://www.nbcnews.com/tech/security/priest-outed-grindr-app-highlights-rampant-%20data-tracking-rcna1493), 2021). C'est le cas d'école de l'inférence de données sensibles décrite par le mémoire [A1].
- **Les sanctions américaines.** La Federal Trade Commission a interdit en 2024 à X-Mode, InMarket, Gravy Analytics et sa filiale Venntel, puis Mobilewalla, de vendre des données relatives à des lieux sensibles ; Mobilewalla collectait des positions dans les enchères publicitaires sans y acheter d'espace ([EFF — X-Mode](https://www.eff.org/deeplinks/2024/01/ftc-bars-x-mode-selling-sensitive-location-data), janvier 2024 ; [The Record — Gravy, Venntel et Mobilewalla](https://therecord.media/ftc-location-data-brokers-gravy-venntel-mobilewalla), décembre 2024 ; [Hunton — ordonnances définitives](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-finalizes-orders-against-data-brokers-over-sensitive-location-data), janvier 2025).

*Synthèse du dossier, à partir de [A1] et [A2] :* le marché secondaire n'est pas un dérivé marginal de la publicité, c'est une **infrastructure de renseignement accessible à quiconque paie**. [A2] rappelle qu'un rapport du groupe consultatif du renseignement américain, rendu public en 2023, constatait l'achat croissant de données commerciales, dont la localisation, par les agences, et que l'OTAN veut intégrer ces données « commercialement disponibles » à sa plateforme OSINT. Le même gisement sert les annonceurs, les services de renseignement alliés et, potentiellement, les services adverses.

### 3.4 Les usages d'État, d'enquête et de renseignement

Le mémoire exclut volontairement le secteur public [A1]. Ces usages sont pourtant structurants, et ils utilisent les mêmes données :

- **Les réquisitions aux opérateurs** : historique des cellules, « bornage » des téléphones présents autour d'une antenne à une heure donnée, localisation en temps réel. Ce sont les outils les plus anciens et les plus courants de l'enquête judiciaire.
- **Les mandats de géorepérage** : la police demande à un fournisseur la liste des appareils présents dans une zone pendant une période. Google y répondait à partir de sa base d'historique de localisation, *Sensorvault* ; en déplaçant cet historique sur les téléphones à partir de fin 2023, il a cessé de pouvoir y répondre ([9to5Google](https://9to5google.com/2023/12/12/google-location-history-timeline-device/), 12 décembre 2023), ce que le mémoire mentionne en note [A1]. Le 29 juin 2026, la Cour suprême des États-Unis a jugé que l'obtention d'un tel historique par mandat de géorepérage est une perquisition au sens du quatrième amendement, sans interdire ces mandats ([Just Security](https://www.justsecurity.org/145214/chatrie-fourth-amendment-supreme-court/), 2026).
- **L'achat de données commerciales**, qui contourne les réquisitions : agences américaines clientes de Venntel, recours du CBP aux données des enchères publicitaires ([EFF](https://www.eff.org/deeplinks/2026/03/targeted-advertising-gives-your-location-government-just-ask-cbp), mars 2026), et réflexion de l'OTAN sur ces sources [A2].
- **La surveillance par la signalisation téléphonique** (SS7, fausses antennes), réservée en principe aux États mais commercialisée, comme l'a montré l'enquête sur First Wap.
- **L'OSINT** : géolocalisation d'images pour établir des crimes de guerre ou vérifier des informations [A3], cartographie des activités militaires à partir de données ouvertes, et désormais géolocalisation automatisée par l'IA [A2].
- **La criminalistique numérique** : extraction de positions des téléphones, des véhicules et des drones ; [A4] montre qu'Europol réclame des outils et des formations sur ces sources, notamment pour les horodatages et la géolocalisation.

## 4. Pourquoi la localisation est une donnée à part

### 4.1 L'inférence : ce que révèlent les lieux

Une position n'a de sens qu'avec le lieu qu'elle désigne. Le mémoire énumère ce que les déplacements permettent d'inférer : domicile, orientation sexuelle, religion, affiliations politiques, état de santé, habitudes [A1]. Cette inférence ne demande aucune compétence particulière : le lieu de la nuit est le domicile, celui des jours ouvrés le travail, le reste se lit sur une carte. La localisation est en outre une **donnée relationnelle** : deux appareils qui passent la nuit au même endroit révèlent un couple ; plusieurs qui se retrouvent régulièrement révèlent un réseau ; un appareil inconnu présent sur une base militaire révèle un visiteur.

### 4.2 L'unicité : pourquoi l'anonymisation échoue

Le mémoire fonde sa thèse sur deux études [A1]. Celle de de Montjoye et ses coauteurs, sur 1,5 million d'abonnés mobiles pendant 15 mois, montre que **quatre points spatio-temporels identifient de façon unique 95 % des personnes**, et que dégrader la précision ou la fréquence ne réduit cette unicité que lentement ([de Montjoye *et al.*, *Scientific Reports*](https://www.nature.com/articles/srep01376), 2013). Celle de Zang et Bolot montre que les lieux les plus fréquentés suffisent à réidentifier un abonné, même à une granularité grossière [A1]. Golle et Partridge l'avaient établi dès 2009 : connue à l'échelle de l'îlot de recensement, la paire domicile-travail laisse un ensemble d'anonymat médian d'**une seule personne** aux États-Unis, 21 à l'échelle du secteur, près de 35 000 à celle du comté ([Golle et Partridge](https://crypto.stanford.edu/~pgolle/papers/commute.html), 2009).

Il en découle trois règles pratiques. **Supprimer le nom ne rend pas anonyme** : l'identifiant d'appareil, même aléatoire, relie les points entre eux, et la trace se réidentifie par ses lieux. **Agréger aide, mais seulement fortement** : des comptes par zone et par heure, avec des seuils minimaux et du bruit, protègent ; des trajectoires individuelles « pseudonymisées » ne protègent pas. **Le risque croît avec le temps** : chaque jour de trace ajoutée rend la personne plus unique. Le mémoire rapporte que l'autorité québécoise de protection des données elle-même juge quasi impossible l'anonymisation des données de localisation [A1].

### 4.3 La trace comme renseignement

*Synthèse du dossier :* pour un service de renseignement, une trace de mobilité est une source de premier ordre. Elle permet d'identifier le personnel d'un site sensible (les appareils qui y passent la journée), de remonter à leurs domiciles (les lieux où ces appareils passent la nuit), de repérer les déplacements inhabituels (une délégation qui se rend dans un pays, un déploiement qui se prépare) et de cartographier les relations. Les Databroker Files l'ont démontré avec des données achetables ; le mémoire, centré sur la vie privée des consommateurs, n'aborde pas cette dimension, que [A2] situe au cœur des attentes de l'OTAN en matière de données commerciales.

## 5. Les risques

Le mémoire organise les risques en cinq familles [A1]. Le dossier les reprend et y ajoute deux familles qu'il ne traite pas : la sécurité opérationnelle des organisations et la fiabilité des systèmes eux-mêmes.

### 5.1 Vie privée, profilage et surveillance commerciale

Le premier risque est la perte de contrôle : même lorsque l'utilisateur consent, sa donnée lui échappe dès qu'elle circule entre les acteurs [A1]. Le profilage combine la position à des données de transaction, de comportement en ligne et sociodémographiques, ce que le mémoire, après Shoshana Zuboff, décrit comme l'exploitation d'un « surplus comportemental » [A1]. Les failles techniques aggravent ce risque : le défaut du site de LocationSmart permettait de localiser n'importe quel téléphone à partir de son numéro, et l'outil interne « God View » d'Uber permettait à des employés de suivre les trajets de clients [A1].

### 5.2 Surveillance au travail

Le mémoire distingue deux situations [A1]. Le GPS d'un véhicule de service, limité à la sécurité et aux actifs, est généralement admis ; une application imposée sur le téléphone personnel d'un salarié, qui peut continuer à relever sa position hors des heures de travail, pose problème. *Synthèse du dossier :* le critère pratique est la séparation des temps et des appareils ; une solution qui suit l'appareil personnel suit la vie privée.

### 5.3 Sécurité physique : couple, enfants, personnes vulnérables

Le mémoire décrit la géolocalisation comme instrument de **contrôle coercitif** dans le couple : surveillance du téléphone, détournement du partage de position, accès aux données du véhicule connecté [A1]. Les **traceurs Bluetooth** ajoutent un outil bon marché et discret, contre lequel les alertes des systèmes d'exploitation et le futur protocole DULT ne protègent qu'en partie, notamment entre plateformes différentes. Les applications de **suivi familial** exposent les enfants : celle de Family Locator a laissé en accès libre pendant des semaines la position en temps réel de milliers de personnes, permettant de savoir qu'un enfant était seul chez lui [A1]. Enfin, la fréquentation de **lieux sensibles**, comme les cliniques d'avortement aux États-Unis depuis 2022, expose les personnes à des poursuites ou à des représailles [A1].

### 5.4 Sécurité opérationnelle des organisations

Les applications de sport ont fourni les cas les plus spectaculaires. En janvier 2018, l'analyste Nathan Ruser a montré que la **carte de chaleur mondiale de Strava**, qui agrège les parcours de ses utilisateurs, révélait les contours de bases militaires et les patrouilles dans des zones de conflit ([NPR](https://www.npr.org/sections/thetwo-way/2018/01/29/581597949/pentagon-reviews-gps-data-after-soldiers-strava-tracks-are-seemingly-exposed), 29 janvier 2018 ; [Bellingcat](https://bellingcat.com/resources/how-tos/2018/01/29/strava-interpretation-guide), 29 janvier 2018). En octobre 2024, l'enquête **« StravaLeaks »** du *Monde* a identifié des membres du groupe de sécurité de la présidence française dont les profils publics permettaient de retrouver des hôtels et lieux de séjour d'Emmanuel Macron, puis de dirigeants américains et russes ([Semafor](https://semafor.com/article/10/28/2024/bodyguards-inadvertently-expose-french-president-macrons-location-on-strava), 28 octobre 2024). S'y ajoutent les données de courtiers décrites plus haut, qui ne demandent même pas que l'intéressé publie quoi que ce soit.

*Synthèse du dossier :* le risque OPSEC tient en trois mécanismes. **L'agrégation** fait apparaître un site que chaque individu ne révèle pas (carte de chaleur). **Le rattachement** relie un site sensible au domicile et à l'identité d'une personne (profil public, trace de courtier). **La prédiction** permet d'anticiper un déplacement à partir des habitudes. Les mesures efficaces visent les trois : interdire les objets connectés dans les zones sensibles, durcir les paramètres des applications, limiter les identifiants publicitaires, et former le personnel et ses proches.

### 5.5 Discrimination et inégalités

La localisation sert à moduler les prix et les résultats : une étude de 2012 relevait jusqu'à 166 % d'écart de prix pour des livres Kindle selon le pays, et jusqu'à 11 % sur Staples.com au sein d'un même État américain selon le code postal [A1]. Elle peut servir de variable de substitution à l'origine ethnique ou sociale : la société Evolv a renoncé à utiliser la distance domicile-travail dans ses algorithmes de recrutement parce qu'elle aurait désavantagé des minorités [A1]. Elle crée enfin des **biais de participation** : l'application Street Bump, qui détectait les nids-de-poule à Boston grâce aux téléphones, orientait les travaux vers les quartiers aisés, mieux équipés [A1].

### 5.6 Erreurs, fiabilité et preuve

La position est une estimation, et ses erreurs ont des conséquences. Le mémoire cite la hausse d'une prime d'assurance fondée sur des déplacements erronés, que l'intéressé ne peut ni connaître ni contester, et des arrestations injustifiées fondées sur des données de géorepérage [A1]. Les tribunaux admettent les données d'antennes comme indices de présence dans un périmètre, pas comme preuve d'une position exacte [A1]. *Synthèse du dossier :* toute décision fondée sur une position devrait en connaître la source, la précision et la possibilité d'un leurrage ; ces métadonnées manquent presque toujours dans les données commerciales.

### 5.7 Cybersécurité des données et des systèmes

Les bases de localisation sont des cibles : leur fuite expose à la fois la vie privée et la sécurité des personnes, et elles enrichissent l'hameçonnage ciblé et l'usurpation d'identité [A1]. Le piratage de Gravy Analytics en est l'illustration. Les systèmes de positionnement eux-mêmes sont attaquables : le brouillage et le leurrage GNSS perturbent l'aviation, la navigation maritime et les réseaux qui dépendent du temps GPS (télécommunications, énergie, finance), et les bases Wi-Fi peuvent être aspirées, comme l'ont montré Rye et Levin.

## 6. Les protections techniques

Le mémoire regroupe les solutions techniques sous l'appellation de LPPM et en décrit six familles, tout en concluant que leur efficacité dépend de la volonté d'acteurs intéressés à la collecte [A1]. Ces solutions ne dépendent d'aucun droit national ; le dossier les reprend, les illustre par leur déploiement réel et les complète.

### 6.1 Minimiser dès la conception

Le premier levier est de ne pas collecter : concevoir les services pour qu'ils reçoivent seulement la donnée nécessaire, limiter les transferts aux tiers et garder la position en cache sur l'appareil pour réduire les requêtes [A1]. Les systèmes d'exploitation ont traduit ce principe en **permissions graduées** : autorisation « une seule fois » ou « pendant l'utilisation » plutôt que permanente, rappels réguliers lorsqu'une application localise en arrière-plan, et position approximative au choix de l'utilisateur. Depuis Android 12, une application qui demande la position précise doit aussi demander la position approximative, et l'utilisateur peut n'accorder que la seconde, y compris pour l'arrière-plan ([Android Developers](https://developer.android.com/codelabs/approximate-location)), sur le modèle introduit auparavant par Apple. Côté organisations, minimiser signifie aussi **auditer les SDK** intégrés aux applications et refuser ceux qui monétisent la position.

### 6.2 Dégrader la précision

La plupart des services n'ont pas besoin de coordonnées exactes ; un quartier ou un code postal suffit [A1]. Le **masquage de localisation** cache la position réelle dans une région plus large ; l'**ajustement de granularité** arrondit les coordonnées [A1]. La version formelle de cette idée est la **géo-indiscernabilité** : la position est perturbée par un bruit calibré, de sorte qu'un observateur ne puisse pas distinguer deux points proches, garantie qui transpose la confidentialité différentielle à la localisation ([Andrés *et al.*, « Geo-Indistinguishability »](https://arxiv.org/abs/1212.1984), CCS 2013). Limite commune : une position approximative répétée dans le temps finit par trahir le lieu réel, et elle se recoupe avec d'autres données [A1].

### 6.3 Limiter dans le temps

C'est l'accumulation qui fait le profil ; conserver peu de temps, segmenter les traces, préférer la collecte ponctuelle réduisent le profilage longitudinal, au prix d'une valeur analytique moindre [A1]. Des pratiques concrètes en découlent : suppression automatique de l'historique après quelques mois, rotation fréquente des identifiants, découpage des trajets pour qu'ils ne se relient pas entre eux.

### 6.4 Traiter sur l'appareil

Calculer localement, réduire les échanges avec les serveurs et réserver la donnée à l'utilisateur réduisent l'exposition à la surveillance de masse [A1]. Le cas le plus significatif est le déplacement par Google de l'historique de localisation vers les téléphones à partir de fin 2023, avec une sauvegarde chiffrée facultative, qui a supprimé la base centrale interrogée par les mandats de géorepérage ([9to5Google](https://9to5google.com/2023/12/12/google-location-history-timeline-device/), 12 décembre 2023). Le mémoire évoque aussi les **coffres-forts de données personnelles** et fiducies de données, qui n'ouvrent l'accès qu'avec l'autorisation de l'utilisateur ; leur intérêt dépend de leur adoption réelle [A1].

### 6.5 Anonymiser, avec réalisme

Le mémoire distingue randomisation (bruit, permutation, confidentialité différentielle) et généralisation (k-anonymat, l-diversité, t-proximité), et ajoute les justificatifs anonymes, qui prouvent un droit d'accès sans révéler l'identité [A1]. Il conclut, à juste titre, que ce sont des mesures d'atténuation et non des garanties, à cause de l'unicité des traces [A1]. *Synthèse du dossier :* la seule anonymisation robuste pour la mobilité est l'**agrégation forte** (comptages par zone et par période, seuils minimaux, bruit calibré), qui renonce aux trajectoires individuelles ; tout jeu de trajectoires individuelles doit être traité comme personnel.

### 6.6 Recourir à la cryptographie

Des protocoles permettent de répondre à une question de localisation sans révéler la position : chiffrement et empreintes cryptographiques, **calcul multipartite sécurisé** pour vérifier qu'un utilisateur est proche d'un lieu, protocoles de proximité entre amis [A1]. Le mémoire les juge efficaces mais lourds à déployer sur mobile [A1]. Les réseaux participatifs de traceurs en offrent pourtant un exemple à grande échelle : les téléphones relais chiffrent la position qu'ils remontent avec une clé que seul le propriétaire du traceur détient, si bien que l'éditeur du réseau ne la connaît pas.

### 6.7 Protéger l'infrastructure et les identifiants

Le mémoire raisonne sur la donnée produite par l'utilisateur ; plusieurs protections portent sur les identifiants et les signaux eux-mêmes :

- **La randomisation des adresses MAC** des téléphones lors des recherches Wi-Fi limite le suivi passif par les capteurs des lieux publics.
- **Le suffixe « _nomap »** exclut une borne Wi-Fi des bases de positionnement de Google et d'Apple ; il est particulièrement indiqué pour les bornes mobiles et les sites sensibles.
- **La réinitialisation ou la désactivation de l'identifiant publicitaire**, et le refus du suivi entre applications, cassent la clé de jointure des courtiers.
- **L'authentification des signaux GNSS** (OSNMA de Galileo) et les récepteurs multi-constellations et multi-fréquences rendent le leurrage plus difficile à réussir sans être détecté.
- **La détection des traceurs indésirables**, intégrée aux systèmes et en cours de normalisation à l'IETF, alerte une personne qu'un traceur inconnu la suit.

### 6.8 Mesures concrètes par type d'acteur

| Acteur | Mesures prioritaires |
| --- | --- |
| Particulier | Autoriser la localisation « pendant l'utilisation » ou « une fois » ; choisir la position approximative quand elle suffit ; revoir les applications ayant accès en arrière-plan ; désactiver ou réinitialiser l'identifiant publicitaire ; mettre les profils d'applications sportives en privé et masquer le départ et l'arrivée des parcours ; retirer les métadonnées des photos et se méfier de leur contenu ; vérifier régulièrement la présence de traceurs inconnus. |
| Organisation qui collecte | Justifier chaque usage de la position et sa précision ; préférer le traitement local et l'agrégation ; fixer des durées de conservation courtes ; auditer et contractualiser les SDK tiers ; ne jamais revendre de trajectoires individuelles ; documenter source et précision des positions utilisées pour décider. |
| Organisation sensible (défense, sécurité, diplomatie, sites industriels) | Zones sans objets connectés ; flotte de téléphones professionnels sans applications grand public ; « _nomap » sur les bornes ; consignes sur les applications sportives et les réseaux sociaux étendues aux proches ; veille sur les jeux de données de courtiers mentionnant ses sites ; prise en compte du brouillage et du leurrage GNSS dans les plans de continuité. |
| Employeur | Équiper les véhicules plutôt que les téléphones personnels ; limiter la localisation aux heures et missions concernées ; informer clairement ; ne pas utiliser la position pour mesurer la productivité individuelle en continu. |

## 7. Enseignements transversaux

**La géolocalisation est un système, pas un capteur.** [A1] présente dix technologies distinctes ; le rapprochement avec les enquêtes récentes montre qu'elles alimentent un même gisement. Le GNSS, le Wi-Fi et le réseau mobile produisent la position ; le système d'exploitation, les applications et leurs SDK la transportent ; la publicité et les courtiers la diffusent ; les acheteurs l'enrichissent et l'exploitent. *Synthèse du dossier :* agir sur un maillon (les permissions du téléphone) ne suffit pas tant que les autres (enchères publicitaires, opérateurs, objets connectés) laissent passer la donnée.

**Le risque est passé de la vie privée à la sécurité nationale.** [A1] raisonne en termes de consommateurs et de salariés. Les Databroker Files, StravaLeaks et l'intérêt de l'OTAN pour les données commerciales [A2] montrent que la même donnée sert à suivre des militaires, des responsables politiques et des agents. *Synthèse du dossier :* l'OPSEC du personnel sensible doit désormais inclure son téléphone personnel, ses applications et celles de ses proches.

**L'anonymisation n'est pas une solution, l'agrégation forte en est une.** Les études citées par [A1] et les cas récents convergent : une trajectoire pseudonyme reste une personne. Seules les statistiques agrégées, avec des seuils et du bruit, protègent réellement ; elles conviennent à la planification des transports ou à l'épidémiologie, pas au ciblage publicitaire, ce qui explique la résistance du marché.

**Le traitement local progresse, la collecte réseau reste hors de portée de l'utilisateur.** Les systèmes ont donné à l'utilisateur des outils réels (position approximative, autorisations temporaires, historique sur l'appareil). Mais l'opérateur, le fournisseur d'accès, les capteurs des lieux publics et les enchères publicitaires localisent sans passer par ces interrupteurs. C'est la limite du « droit de ne pas être suivi » proposé par [A1] s'il se réduit à une désactivation par défaut côté appareil.

**L'IA déplace la frontière de la donnée de localisation.** Une photo sans coordonnées devient une position, un texte anodin une adresse. [A1] signale le phénomène ; l'OTAN en fait une fonction attendue [A2] ; l'OSINT en fait un outil de preuve [A3]. Les règles fondées sur les capteurs ou les métadonnées ne suffisent plus.

**La fiabilité devient un enjeu de sécurité.** Brouillage et leurrage massifs, bases Wi-Fi aspirables, données commerciales sans métadonnées de précision : la position est moins sûre qu'on ne le croit, alors qu'elle sert de plus en plus de preuve [A1] [A4].

## Limites et questions ouvertes

1. **Un socle documentaire inégal.** Le mémoire [A1] est solide sur la vie privée mais approximatif sur la technique et ancien dans ses exemples ; le dossier a corrigé les points identifiés, sans prétendre à l'exhaustivité technique d'un ouvrage de géodésie ou de radiocommunication.
2. **Des précisions indicatives.** Les ordres de grandeur dépendent du matériel, de l'environnement et de la méthode ; les objectifs des normes 5G ou Bluetooth ne sont pas des performances mesurées sur le terrain.
3. **Des sources d'enquête partielles.** Les chiffres des Databroker Files, de Gravy Analytics ou de First Wap proviennent d'échantillons obtenus par des journalistes ; ils démontrent la faisabilité et l'ordre de grandeur, pas l'état complet du marché.
4. **Un marché opaque et mouvant.** Les courtiers changent de nom, se rachètent et déplacent leurs activités ; les sanctions américaines n'ont pas d'équivalent public de même ampleur ailleurs, et l'on ignore la part du marché qui passe aujourd'hui par les enchères publicitaires plutôt que par les SDK.
5. **Les usages d'État peu documentés.** Les volumes réels de réquisitions, d'achats de données et d'interceptions par la signalisation téléphonique restent largement inconnus en Europe.
6. **Une question ouverte sur la désactivation par défaut.** Le « droit de ne pas être suivi » de [A1] devrait concilier urgences, antifraude et navigation, et atteindre la collecte réseau ; aucune proposition publique ne règle encore ces points.

## Pour aller plus loin

- [EFF — « On Locational Privacy, and How to Avoid Losing it Forever »](https://www.eff.org/wp/locational-privacy) — le texte fondateur de 2009 sur la vie privée de localisation, cité par [A1].
- [de Montjoye *et al.* — « Unique in the Crowd »](https://www.nature.com/articles/srep01376) — l'étude de référence sur l'unicité des traces de mobilité.
- [Rye et Levin — « Surveilling the Masses with Wi-Fi-Based Positioning Systems »](https://arxiv.org/abs/2405.14975) — la démonstration la plus concrète des risques du positionnement Wi-Fi.
- [Andrés *et al.* — « Geo-Indistinguishability »](https://arxiv.org/abs/1212.1984) — le fondement des techniques de brouillage de position.
- [netzpolitik.org — « Databroker Files »](https://netzpolitik.org/2024/data-broker-files-how-data-brokers-sell-our-location-data-and-jeopardise-national-security/) — l'enquête européenne de référence sur le marché des données de localisation et la sécurité nationale.
- [EASA — GNSS outages and alterations](https://www.easa.europa.eu/en/domains/air-operations/global-navigation-satellite-system-outages-and-alterations) — le suivi officiel du brouillage et du leurrage dans l'aviation.

## Analyses internes utilisées et provenance

- **[A1]** [Être localisé en permanence : techniques, usages et risques de la géolocalisation](../analyses/etre-localise-en-permanence-techniques-usages-et-risques-de-la-geolocalisation.md) — source principale : définitions, typologies, dix technologies, usages de l'annexe, risques, unicité des traces et six familles de solutions techniques. Ses limites (approximations techniques, exemples anciens, exclusion de l'État) sont corrigées ou complétées dans le dossier.
- **[A2]** [OTAN : la future plateforme OSINT, un achat de données et d'anonymat plus qu'un projet d'IA](../analyses/otan-la-future-plateforme-osint-un-achat-de-donnees-et-d-anonymat-plus-qu-un-projet-d-ia.md) — usages de renseignement : données commercialement disponibles, géolocalisation automatisée attendue de l'IA, achats de données par la communauté du renseignement américaine.
- **[A3]** [SOCMINT : ce que l'IA change au renseignement sur les réseaux sociaux](../analyses/introduction-to-social-media-intelligence-socmint.md) — géolocalisation et datation d'images par les enquêteurs en source ouverte comme discipline de preuve.
- **[A4]** [Europol : digital forensics en Europe, les lacunes qui fragilisent la preuve numérique](../analyses/europol-digital-forensic-en-europe-les-lacunes-qui-fragilisent-la-preuve-numerique.md) — difficultés d'acquisition des données de véhicules et besoins de formation sur les horodatages et la géolocalisation.
