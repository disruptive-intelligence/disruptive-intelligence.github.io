---
title: "Analyse — Piratage de la DGFiP : identifiants volés, réseau ouvert, supervision aveugle"
date: 2026-09-29
kind: analysis
theme: cyber
slug: piratage-de-la-dgfip-identifiants-voles-reseau-ouvert-supervision-aveugle
organization: "Agence nationale de la sécurité des systèmes d'information (ANSSI)"
tags:
  - DGFiP
  - ANSSI
  - retour d'expérience
  - infostealer
  - authentification multifacteur
  - fuite de données
  - supervision
source_file: inbox/20260923_NP_TLPCLEAR_ANSSI_Rapport_incident_DGFIP.pdf
source_url: https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/
events:
  - evt-505123c8-a2a8-464e-91fd-37b311e52f57
---

# Analyse — Piratage de la DGFiP : identifiants volés, réseau ouvert, supervision aveugle

## Métadonnées

- **Document :** *Rapport d'incident – Septembre 2026. Actes malveillants observés sur le système d'information de la Direction générale des Finances publiques entre mai 2026 et août 2026*, 20 pages.
- **Éditeur :** Agence nationale de la sécurité des systèmes d'information (ANSSI), dont le logo figure en page de titre avec le bloc « République française » ; référence n° 3033/ANSSI/SDO/NP. Aucun rédacteur n'est nommé.
- **Date :** 23 septembre 2026 (p. 1). Selon la page de publication de l'ANSSI, le rapport a été remis au Premier ministre le 24 septembre et rendu public le 29 septembre 2026.
- **Diffusion :** version publique marquée **TLP:CLEAR**, anonymisée (comptes et adresses IP renommés) et caviardée : plusieurs passages sont masqués par des bandeaux noirs (p. 2, 4-5, 7-8, 17-20).
- **Support :** PDF conservé dans `inbox/20260923_NP_TLPCLEAR_ANSSI_Rapport_incident_DGFIP.pdf`, publié sur cyber.gouv.fr.
- **Périmètre :** deux exfiltrations de données de la DGFiP, l'une depuis l'application E-Contact (revendiquée le 12 août 2026), l'autre depuis le serveur professionnel de données cadastrales (revendiquée le 13 août), et les défaillances qui les ont permises.
- **Méthode de la fiche :** jusqu'aux « Cinq éléments essentiels », seule la lecture du PDF fonde les constats, avec renvoi aux pages. La dernière section confronte ces constats à des sources extérieures citées et datées.

## Repères pour comprendre le document

Le texte est un **retour d'expérience après incident** : l'ANSSI y reconstitue ce qui s'est passé à partir des journaux et documents disponibles, puis en tire des « enseignements » et des « mesures de remédiation ». Son plan le dit (p. 2) : une synthèse, une analyse des défaillances, un plan de remédiation, puis une chronologie détaillée en annexe, qui occupe à elle seule six pages et constitue la matière première du rapport. Pour le lire, il faut se représenter l'architecture en jeu. La DGFiP n'a pas été attaquée par la porte d'entrée d'impots.gouv.fr, mais par des **portails d'accès** destinés à ses agents et à ses partenaires, joignables depuis Internet ou depuis le réseau commun des ministères. L'attaquant n'a exploité aucune faille logicielle : il s'est connecté avec les identifiants de vrais utilisateurs, puis a aspiré des données en simulant des consultations. Tout l'enjeu du rapport est donc de savoir pourquoi des connexions « légitimes » en apparence n'ont alerté personne.

- **RIE (Réseau interministériel de l'État)** — Réseau qui interconnecte les ministères. Un poste compromis dans un ministère peut, faute de cloisonnement, atteindre des applications d'un autre (p. 8, 14).
- **PIGP (Portail internet de la gestion publique)** — Portail de la DGFiP ouvert aux ordonnateurs et comptables des collectivités et établissements publics ; il donnait aussi aux agents l'accès à leur messagerie en ligne et à des services RH (p. 14).
- **ADER** — Portail d'accès à certaines applications de la DGFiP à travers le RIE ; c'est par lui que l'attaquant a atteint E-Contact (p. 13).
- **E-Contact** — Application de messagerie qui sert aux échanges entre la DGFiP et les usagers ; ses données sont celles de la première fuite (p. 13).
- **APEX** — Portail réservé aux partenaires externes, notamment notaires et géomètres-experts, protégé par un mot de passe et un code à usage unique envoyé par courriel (p. 13).
- **SPDC (Serveur professionnel de données cadastrales)** — Service qui donne aux professionnels autorisés l'accès aux données du cadastre ; source de la seconde fuite (p. 14, 20).
- **Infostealer** — Logiciel malveillant qui aspire discrètement les identifiants et données d'un appareil infecté ; ces identifiants sont ensuite revendus (p. 13).
- **Authentification multifacteur et OTP par courriel** — Exiger, en plus du mot de passe, un second élément ; le rapport souligne qu'un code envoyé par courriel ne protège rien si la messagerie elle-même s'ouvre avec le même mot de passe ou depuis le même poste compromis (p. 7, 11).
- **Scraping** — Extraction automatique de données d'une application web par un programme qui enchaîne les requêtes, une page consultée par requête (p. 7, 14).
- **SOC, SIEM et CSIRT** — Le SOC surveille et répond aux incidents ; le SIEM centralise et corrèle les journaux de sécurité ; le CSIRT est l'équipe de réponse aux incidents, ici déclinée par ministère (p. 13-14).
- **Latéralisation** — Déplacement d'un attaquant d'un système compromis vers d'autres systèmes reliés au premier ; ici, du ministère de l'Éducation nationale vers la DGFiP (p. 5, 9).
- **TLP:CLEAR** — Marquage du *Traffic Light Protocol* qui autorise la diffusion publique sans restriction. *Explication ajoutée :* le rapport ne définit pas ce marquage.

## Résumé exécutif

Le rapport retrace deux fuites de données de la DGFiP révélées en août 2026 par un acteur nommé Zerobytes. La première, revendiquée le 12 août, porte sur des données issues de l'outil de relation avec les usagers E-Contact et concerne, selon la synthèse, près de **353 000 particuliers et 252 000 professionnels** ; la seconde, revendiquée le 13 août, porte sur des données cadastrales exfiltrées entre le 27 juillet et le 8 août par le compte d'un géomètre-expert (p. 4). Son apport principal tient en une phrase de l'ANSSI : la compromission « n'est pas la conséquence d'une attaque sophistiquée », mais de faiblesses dans trois domaines, **l'identité, l'architecture et la détection** (p. 4-5).

Le déroulé est celui d'une longue préparation restée invisible. Pendant trois mois, l'attaquant accumule plusieurs dizaines d'identifiants d'agents, probablement volés par des infostealers sur des ordinateurs que la DGFiP n'administre pas. Il les teste sur le PIGP, puis passe par le RIE, auquel il accède grâce à la compromission du ministère de l'Éducation nationale, pour atteindre le portail ADER et l'application E-Contact. Il développe un outil de scraping, exfiltre 11 Go de données du 24 au 25 juin, puis 3 Go les 22 et 23 juillet (p. 7, 17-19). Des alertes se déclenchent à plusieurs reprises, mais elles portent sur le PIGP et se soldent par des réinitialisations de mots de passe qui n'interrompent ni les sessions en cours ni l'accès par ADER, que le SOC ne supervise pas (p. 5, 18). La découverte vient de la revendication de l'attaquant, sept semaines après la première exfiltration (p. 4).

Le plan de remédiation découle de ce diagnostic : cloisonner les applications selon leur usage interne, partenaire ou public, mettre toutes les applications sous supervision avec des quotas de consultation, interdire les appareils personnels, généraliser une authentification multifacteur résistante au vol du mot de passe, et accompagner toute réinitialisation d'une analyse d'activité et d'une révocation des sessions (p. 10-12). Les mesures d'endiguement, qui ont coupé les accès des agents aux portails ADER et PIGP et verrouillé APEX, ont eu « des impacts significatifs » sur les services (p. 4, 20).

Pour la veille, c'est un document rare : un **retour d'expérience public et daté à la minute** sur la compromission d'une grande administration, qui montre comment une chaîne d'attaque triviale traverse des défenses en place. Sa valeur est limitée par les caviardages, par des écarts de chiffres non expliqués et par un regard très bref de l'ANSSI sur ses propres manques.

## Chronologie

La chronologie de l'annexe (p. 15-20) est la partie la plus riche du document. Les jalons ci-dessous en retiennent l'essentiel ; les heures sont en UTC+2.

- **2-8 mai 2026 :** connexions au PIGP avec un même compte d'agent depuis trois lieux, à partir d'adresses IP malveillantes situées en France et en Inde ; le 7 mai, ce compte accède aussi à E-Contact par ADER. Son mot de passe est réinitialisé le jour même, pour un autre incident.
- **13-17 mai :** trois nouveaux comptes compromis ; du 22 mai au 3 juin, tentatives de connexion au PIGP sans alerte. L'un des trois comptes n'est jamais signalé par le prestataire de veille, un autre n'est réinitialisé que neuf jours après son signalement.
- **7 juin :** un compte se connecte au PIGP puis, quelques minutes plus tard, à ADER depuis deux adresses du RIE. Une alerte sur des recherches suspectes entraîne la réinitialisation du compte, mais le passage vers ADER n'est pas vu.
- **9 et 11 juin :** le centre opérationnel du ministère de l'Éducation nationale (COSSIM) signale un incident à tous les CSIRT ministériels et partage 17 marqueurs, dont l'une des adresses du RIE utilisées par l'attaquant, puis un marqueur supplémentaire.
- **15 juin :** un partenaire informe l'ANSSI de la compromission de deux comptes de la DGFiP ; la DGFiP ne répond pas et l'ANSSI ne la relance pas (les comptes avaient déjà été réinitialisés).
- **21-23 juin :** reconnaissance technique sur ADER, téléchargement d'une documentation applicative, puis concentration sur E-Contact et développement itératif d'un outil de scraping. Le 23 juin à 20 h 50, une alerte crée automatiquement un ticket au SOC.
- **24 juin 4 h 26 – 25 juin 2 h 31 :** première exfiltration automatisée. Le ticket est traité le 24 juin à 10 h 40 par une réinitialisation de mot de passe, qui n'interrompt pas la session.
- **Fin juin – début juillet :** tentatives de connexion en échec sur une quinzaine de comptes ; nouveaux signalements de comptes compromis et vendus ; le 4 juillet, nouveau lot de marqueurs du COSSIM ; les 6 et 7 juillet, un compte déjà réinitialisé en juin est réutilisé sur ADER.
- **18-24 juillet :** deux nouveaux comptes compromis ; le 21, l'attaquant vérifie cinq couples identifiant/mot de passe ; le 22, seconde exfiltration automatisée (7 h 28 – 11 h 33, puis 16 h 20 – 17 h 16). Le SOC détecte des recherches suspectes le 23 et réinitialise le compte le 24, en bloquant une adresse IP.
- **27 juillet – 8 août :** exfiltration des données cadastrales par le portail APEX, avec le compte d'un géomètre-expert (p. 4).
- **6 août :** l'ANSSI, en recherchant des antécédents sur ses sondes, signale à la DGFiP deux adresses IP malveillantes ; la DGFiP répond le 11 août avoir réinitialisé cinq comptes et bloqué ces adresses.
- **12 août :** à 13 h 50, Zerobytes revendique le vol de données d'impots.gouv.fr ; l'ANSSI prévient la DGFiP à 16 h 32.
- **13-18 août :** revendication sur le cadastre (13 août, 18 h 44) ; coupure d'ADER pour les agents (13 août), identification du compte du géomètre et verrouillage d'APEX (14 août), coupure du PIGP pour les agents et désactivation des comptes du cabinet de géomètres (18 août).
- **23 septembre 2026 :** date du rapport.

## Thèse principale

L'ANSSI soutient qu'une attaque à la portée d'un acteur peu sophistiqué a réussi parce que **trois lignes de défense ont cédé en même temps** : l'identité (des identifiants qui fuient depuis des appareils personnels et suffisent seuls à entrer), l'architecture (des applications sensibles ouvertes sans cloisonnement à Internet et au RIE) et la détection (une supervision qui ne couvrait pas le portail utilisé et ne corrélait pas des signaux pourtant classiques) (p. 4-5). Aucune de ces défaillances n'aurait suffi seule ; leur conjonction a offert à l'attaquant « une chaîne d'exploitation triviale » (p. 4).

Le texte est à la fois un **constat technique** et un **plaidoyer pour la défense en profondeur**. Il ne cherche ni à attribuer l'attaque ni à établir des responsabilités individuelles ; il veut montrer que la veille sur les comptes compromis, sur laquelle la DGFiP comptait, n'est qu'une « boucle de rattrapage » et ne peut remplacer ni l'authentification forte ni le cloisonnement (p. 4, 6).

## Informations et arguments importants

### Une attaque en trois temps : accumuler, tester, aspirer

Le rapport décrit une progression méthodique, que la chronologie rend lisible. L'attaquant commence par **accumuler des identifiants** : sur trois mois, il dispose de plusieurs dizaines de couples identifiant/mot de passe d'agents internes et de personnels externes ayant accès aux applications de la DGFiP. Aucune attaque par force brute ni par *credential stuffing* n'est observée ; il possédait donc déjà les mots de passe, valides ou expirés (p. 6). Il **teste** ensuite ces comptes sur le PIGP, souvent plusieurs comptes depuis une même adresse IP, et change d'adresse d'un jour à l'autre (p. 16). Enfin, dès qu'un compte fonctionne, il **pivote** du PIGP, joignable depuis Internet, vers le portail ADER, qu'il atteint depuis le RIE à travers l'infrastructure compromise du ministère de l'Éducation nationale (p. 8, 16-17).

La phase d'exfiltration montre un attaquant qui apprend. Le 22 juin, il télécharge une documentation applicative ; le 23, il fait une capture d'écran d'E-Contact et commence à écrire son outil de scraping ; le 24, l'outil tourne pendant près de 22 heures (p. 17-18). En juillet, il vérifie d'abord ses accès en téléchargeant manuellement deux fiches, puis relance l'extraction automatique (p. 19).

### Ce qui a été volé

Les deux fuites relèvent de périmètres distincts.

- **E-Contact :** selon la synthèse, près de 353 000 particuliers et 252 000 professionnels (p. 4). L'annexe rapporte la revendication de l'attaquant, qui annonce 678 437 enregistrements, dont 392 867 particuliers et 285 570 professionnels, et l'associe à la session du 24 juin (p. 19). Le rapport ne réconcilie pas ces deux séries de chiffres.
- **Cadastre (SPDC) :** l'attaquant revendique 2 millions de Français concernés et des données comprenant noms, dates de naissance, identifiants fonciers, parcelles et biens détenus (p. 20). Le rapport ne donne pas de volume établi par les investigations.
- **Volumes de trafic :** 11 Go échangés entre le 22 et le 25 juin, 3 Go entre le 21 et le 23 juillet, observés a posteriori dans les journaux du ministère de l'Éducation nationale (p. 7, 18-19).

### L'identité : des mots de passe qui suffisent

L'ANSSI situe la cause première dans l'usage d'**appareils non administrés** par la DGFiP : ordinateurs personnels d'agents pour ADER, postes d'organismes tiers pour APEX (p. 6). Elle le présente comme une supposition (« il est supposé »), mais elle en tire la conséquence essentielle : réinitialiser un mot de passe ne sert à rien si l'appareil infecté n'est pas nettoyé, ce qui ne peut être garanti chez des tiers (p. 6-7). Deux autres faiblesses aggravent la situation. Le PIGP et ADER n'exigeaient **aucun second facteur**, ce qui permettait la réutilisation immédiate des identifiants volés ; APEX en exigeait un, mais sous forme de code envoyé par courriel, que la compromission du poste du géomètre a permis de contourner (p. 7, 20).

La DGFiP n'était pas démunie : depuis plusieurs années, elle recevait de prestataires (Recorded Future, Orange Cyberdéfense) les signalements de comptes compromis ou mis en vente, et son SOC réinitialisait alors le mot de passe, recherchait des actions concomitantes et sensibilisait l'agent (p. 15). Le rapport reconnaît l'intérêt de ce dispositif tout en montrant ses trois limites : il ne couvre pas toutes les plateformes de revente, il laisse une fenêtre incompressible entre la compromission et la réinitialisation, et l'analyse de l'activité passée de chaque compte est trop lourde pour être exhaustive (p. 6).

### La détection : des signaux présents, jamais corrélés

L'ANSSI énumère les indicateurs qui auraient dû attirer l'attention et qu'aucun mécanisme n'a exploités (p. 7) :

1. **Le volume échangé** : 11 Go puis 3 Go sans alerte.
2. **Le nombre de requêtes par utilisateur** : le scraping impose une requête par fiche ; aucun mécanisme de limitation de débit (*rate-limiting*) n'était appliqué.
3. **La réputation et l'origine des adresses IP** : connexions depuis des VPN, depuis l'Inde, depuis des adresses classées malveillantes, et réutilisation d'une même adresse pour des comptes déjà connus comme compromis.
4. **Les horaires** : connexions nocturnes non interprétées.

L'agence concède que chacun de ces signaux, pris isolément, produit beaucoup de faux positifs, mais que leur **corrélation** aurait permis d'alerter (p. 7). Encore fallait-il voir l'activité : le SOC ne supervisait pas ADER, ce qui l'empêchait de relier les alertes du PIGP à ce qui se passait sur E-Contact (p. 5, 8). Le rapport relève enfin, sans l'avoir étudié, que des comptes non privilégiés avaient accès à un volume important de données, point renvoyé à un audit organisationnel de « phase 2 » (p. 8).

### L'architecture et la coordination interministérielle

Plusieurs accès illégitimes proviennent du RIE, depuis des localisations sans besoin apparent d'accéder à la DGFiP : la segmentation réseau est jugée « trop permissive » (p. 8). Le point le plus sensible concerne la coordination entre ministères. Quand la première exfiltration a lieu, le ministère de l'Éducation nationale gère déjà, avec l'ANSSI, un incident sur son périmètre, et des tentatives de latéralisation vers d'autres organisations raccordées au RIE ont été repérées (p. 8-9). Le COSSIM a diffusé ses marqueurs le 9 juin, dont une adresse qu'utilisait l'attaquant (p. 16). Le rapport, prudent, estime seulement qu'il « est raisonnable de préciser » que l'analyse et le partage de ces marqueurs auraient dû être plus rapides, et que des blocages de flux au niveau du RIE supposeraient d'abord une cartographie fine des flux légitimes (p. 9).

### L'aveu sur la supervision de l'ANSSI

L'ANSSI consacre quelques lignes à ses propres manques : elle ne disposait pas de supervision applicative sur ce périmètre, et sa supervision réseau ne pouvait distinguer des connexions faites avec des comptes légitimes (p. 8). Elle ajoute que le volume de requêtes « aurait dû déclencher des alertes ». Une partie du paragraphe est caviardée. La chronologie montre par ailleurs que l'agence n'a pas relancé la DGFiP après un signalement resté sans réponse le 15 juin, et qu'elle a trouvé des traces sur ses sondes le 6 août, six jours avant la revendication (p. 17, 20).

### Le plan de remédiation

Les mesures sont organisées en trois familles (p. 10-12).

- **Restreindre l'accès aux applications métier** selon leur usage. Les applications internes ne doivent être accessibles que depuis des postes administrés, et depuis Internet uniquement par un VPN dédié. Les applications destinées à des partenaires ne doivent être joignables que par VPN ou, à défaut, par une liste d'adresses autorisées, compensée par une authentification multifacteur et des limitations métier. Les applications publiques doivent au moins filtrer ou signaler les connexions selon la géolocalisation et la réputation des adresses. Toutes doivent être supervisées dans un SIEM, avec des quotas de consultation, de requêtes et de volume, une protection contre les injections et un blocage par géolocalisation et réputation IP.
- **Protéger contre le vol d'identifiants.** Proscrire les appareils personnels, durcir les postes professionnels (mises à jour, EDR, VPN permanent), déployer l'authentification multifacteur sur toutes les applications avec un second facteur résistant à la compromission du premier (clés physiques ou applications d'authentification plutôt qu'un code par courriel, idéalement sur un autre appareil), gérer finement les droits et plafonner les consultations.
- **Revoir le processus de réinitialisation.** Accompagner chaque réinitialisation d'une analyse de l'activité du compte depuis la date présumée de compromission, révoquer toutes les sessions actives, rechercher la cause racine en cas de compromission répétée et étudier le blocage automatique des comptes après des recherches suspectes.

La synthèse ajoute que ces chantiers exigent l'appui de toute la chaîne métier, de la hiérarchie ministérielle et de l'interministériel, et qu'ils peuvent alimenter la feuille de route de sécurité numérique de l'État (p. 5).

## Points particulièrement intéressants pour la veille

- **La réinitialisation n'est pas une remédiation.** Le 24 juin, le mot de passe est changé à 10 h 40, mais l'exfiltration continue jusqu'au lendemain parce que la session reste ouverte (p. 18). *Inférence pour la veille :* toute procédure de réponse à une compromission de compte qui ne révoque pas les sessions et ne regarde pas en arrière est une procédure de façade ; c'est un point de contrôle simple à vérifier dans n'importe quelle organisation.
- **Le poste personnel comme porte d'entrée de l'État.** Le rapport attribue la fuite en série d'identifiants à des appareils non administrés (p. 6). *Inférence pour la veille :* la frontière entre sécurité personnelle et professionnelle a disparu ; un agent qui consulte sa messagerie professionnelle depuis un ordinateur familial infecté expose toute son administration.
- **L'interconnexion comme vecteur.** L'attaquant est entré à la DGFiP par le réseau d'un autre ministère (p. 8). *Inférence pour la veille :* la sécurité d'une administration raccordée au RIE dépend du plus faible de ses voisins, ce qui fait de la vitesse de partage des marqueurs entre ministères un enjeu de défense collective.
- **Le code par courriel ne suffit plus.** Le cas du géomètre montre qu'un second facteur livré sur le poste compromis ne protège rien (p. 7, 11, 20). *Inférence pour la veille :* les portails ouverts aux professions réglementées (notaires, géomètres, experts-comptables) sont un maillon faible, puisque l'administration n'en maîtrise pas les postes.
- **La revendication comme alarme.** Les deux fuites ont été découvertes par l'annonce de l'attaquant, pas par la défense (p. 4, 20). *Inférence pour la veille :* la surveillance des forums de revendication et des sites d'alerte sur les fuites reste, en pratique, un détecteur de dernier recours pour les administrations elles-mêmes.

## Faits, opinions et interprétations

### Faits rapportés par la source

Le rapport établit, à partir des journaux de la DGFiP et du ministère de l'Éducation nationale, des signalements de Recorded Future et de l'analyse de l'ANSSI, une chronologie datée de mai à août 2026 (p. 15). Il rapporte l'usage de plusieurs dizaines de comptes, deux sessions d'exfiltration principales sur E-Contact (**11 Go** fin juin, **3 Go** fin juillet), l'accès par le RIE depuis l'infrastructure du ministère de l'Éducation nationale, l'absence d'authentification multifacteur sur le PIGP et ADER, l'absence de supervision d'ADER par le SOC et l'absence de détection des exfiltrations par la DGFiP comme par l'ANSSI (p. 4-8). Il donne deux séries de chiffres sur les victimes d'E-Contact : **353 000 particuliers et 252 000 professionnels** dans la synthèse, **678 437 enregistrements** revendiqués par l'attaquant dans l'annexe (p. 4, 19). Ces éléments proviennent pour une large part de la DGFiP elle-même, et le rapport prévient que des écarts de temps peuvent exister entre les sources (p. 15).

### Opinions ou positions de l'auteur

L'ANSSI juge que l'attaque n'était pas sophistiquée et que la chaîne d'exploitation était « triviale » (p. 4). Elle qualifie la veille sur les comptes compromis de « boucle de rattrapage pertinente » mais insuffisante, et l'accès à des données sensibles par un simple vol d'identifiants de « contraire aux principes de résilience et de défense en profondeur » (p. 6). Elle estime que la corrélation des signaux « aurait pu permettre » d'alerter et que le volume de requêtes « aurait dû déclencher des alertes » (p. 7-8). Ses recommandations sont formulées sur le mode de l'obligation (« doit être proscrit », « doit être déployée ») pour l'essentiel, et du conditionnel pour le blocage automatique des comptes (p. 11-12).

### Interprétations et inférences

L'origine des identifiants volés est une interprétation de l'ANSSI : ils ont été « probablement » compromis par des infostealers sur des appareils non administrés (p. 4, 6). Pour la présente analyse, le rapport se lit aussi comme un document de **gouvernance** : en rappelant que les chantiers exigent l'appui de la hiérarchie ministérielle et de l'interministériel (p. 5), l'ANSSI signale que les obstacles ne sont pas seulement techniques. La réutilisation en juillet d'un compte déjà réinitialisé en juin (p. 16, 18) suggère que l'attaquant a obtenu le nouveau mot de passe, ce qui plaide pour la persistance d'une infection sur l'appareil de l'agent ; le rapport ne tire pas explicitement cette conclusion, mais elle rejoint son propos sur le nettoyage des appareils.

## Limites et points à vérifier

1. **Des chiffres de victimes non réconciliés.** La synthèse avance 353 000 particuliers et 252 000 professionnels, l'annexe rapporte une revendication de 678 437 enregistrements rattachée à la seule session du 24 juin (p. 4, 19). Le rapport ne dit pas si l'écart tient à des doublons, à la seconde exfiltration ou à l'exagération de l'attaquant, alors que c'est la donnée qui intéresse le plus le public.
2. **Une seconde fuite à peine documentée.** L'incident du cadastre tient en une demi-page : aucun volume établi, une période d'exfiltration (27 juillet – 8 août) qui ne coïncide pas avec la date revendiquée (29 juillet), aucune précision sur la manière dont le second facteur a été contourné (p. 4, 20).
3. **« Aucune détection » à nuancer.** La synthèse affirme qu'aucune exfiltration n'a été détectée (p. 4), mais la chronologie montre des alertes réelles les 7 juin, 23 juin, 6 juillet et 23 juillet, suivies de réinitialisations (p. 16-19). Le problème décrit est moins l'absence d'alerte que leur traitement étroit, compte par compte, sans vision d'ensemble ; la formule de la synthèse le masque.
4. **Des caviardages qui retirent l'essentiel de certaines sections.** La partie sur la supervision de l'ANSSI, le détail du filtrage réseau, un indicateur de détection et la nature des données extraites sont masqués (p. 5, 7-8, 17-19). Le lecteur ne peut juger ni de l'ampleur exacte des données volées ni de la capacité de supervision de l'État.
5. **Une coordination interministérielle décrite sans responsabilités.** On sait que les marqueurs du 9 juin contenaient une adresse de l'attaquant, mais pas qui les a reçus, quand ils ont été intégrés, ni pourquoi l'accès par ADER a pu se poursuivre jusqu'en juillet (p. 9, 16). L'incident du ministère de l'Éducation nationale lui-même n'est pas décrit.
6. **Un auditeur qui s'examine lui-même.** L'ANSSI est à la fois l'enquêteur et l'un des acteurs dont la supervision a échoué ; elle ne relance pas un signalement resté sans réponse le 15 juin (p. 17). Ses propres manques occupent quelques lignes, en partie caviardées (p. 8), sans recommandation qui la concerne.
7. **Des causes supposées plutôt qu'établies.** L'origine des identifiants (infostealers sur appareils personnels) est présentée comme probable, sans analyse d'un appareil infecté ni indication de la famille de logiciel malveillant (p. 4, 6). La gestion des droits, qui a permis à des comptes non privilégiés d'accéder à des centaines de milliers de fiches, n'a pas été étudiée (p. 8).
8. **Une chronologie à lire avec prudence.** Le rapport prévient lui-même des écarts entre sources (p. 15), et quelques incohérences le confirment : une date de réinitialisation qui varie d'un jour selon le passage (24 ou 25 mai, p. 16), une connexion à ADER datée avant la vérification des comptes qui la précède logiquement (21 juillet, p. 19), une période « du 21 au 27 juillet » pour des sessions observées les 21 et 22 (p. 19).

## Sources et références mentionnées

Le rapport ne comporte pas de bibliographie : c'est un document d'enquête fondé sur des **sources primaires internes**, énumérées en tête de l'annexe (p. 15). Il s'agit des documents d'analyse de la DGFiP (main courante et chronologie), de ses journaux d'événements, des notifications de Recorded Future, son prestataire de veille sur la menace, des journaux de flux réseau ADER/Odin transmis par le ministère de l'Éducation nationale, et des publications de FrenchBreaches et de Zerobytes relevées en source ouverte. Orange Cyberdéfense apparaît comme seconde source de signalement de comptes compromis. Les seules références externes au sens propre sont les « exigences fournies par l'ANSSI » sur l'authentification forte, citées sans titre (p. 11), et la feuille de route de sécurité numérique de l'État (p. 5). L'équilibre des sources penche nettement vers la DGFiP, qui est à la fois la victime et le principal fournisseur des faits.

## Cinq éléments essentiels à retenir

1. Deux fuites de la DGFiP, sur **E-Contact** (environ 600 000 usagers selon la synthèse) et sur le **cadastre**, ont été découvertes par la revendication de l'attaquant, pas par la défense.
2. L'attaque n'avait **rien de sophistiqué** : des dizaines d'identifiants d'agents probablement volés par infostealers sur des appareils personnels, réutilisés faute d'authentification multifacteur.
3. L'attaquant a atteint E-Contact par le **réseau interministériel**, depuis l'infrastructure compromise du ministère de l'Éducation nationale, à travers un portail que le SOC ne supervisait pas.
4. Des alertes ont bien sonné, mais leur traitement s'est limité à des **réinitialisations de mots de passe** qui n'ont coupé ni les sessions ni l'autre chemin d'accès.
5. Le remède proposé est classique et exigeant : **cloisonnement** selon l'usage, **authentification forte** résistante au vol du poste, **supervision** de toutes les applications avec quotas, et réinitialisations accompagnées d'une enquête.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-09-29. Les constats suivants complètent ou corrigent la lecture du PDF ; ils ne modifient pas les sections précédentes, fondées sur la seule source.

### Travaux de référence

- **La doctrine de l'ANSSI sur l'authentification.** Le guide [ANSSI — « Recommandations relatives à l'authentification multifacteur et aux mots de passe »](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe) (8 octobre 2021) est vraisemblablement le texte que le rapport désigne comme « exigences fournies par l'ANSSI » (p. 11). Il recommande de privilégier l'authentification multifacteur et, parmi les facteurs, ceux qui reposent sur la possession d'un objet. L'incident montre qu'en 2026, cinq ans après sa publication, deux portails d'une administration centrale n'en appliquaient pas le principe de base.
- **Le précédent Snowflake, même mécanique à l'échelle mondiale.** Le rapport de [Mandiant (Google Cloud) — « UNC5537 Targets Snowflake Customer Instances for Data Theft and Extortion »](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion) (10 juin 2024) décrit une campagne contre environ 165 organisations, menée uniquement avec des identifiants volés par infostealers, sur des comptes sans authentification multifacteur ni liste d'adresses autorisées. 79,7 % des comptes utilisés avaient déjà été exposés, certains depuis novembre 2020, et des postes de sous-traitants servant aussi à des usages personnels ont ouvert l'accès à plusieurs clients à la fois. C'est, deux ans plus tôt, le scénario de la DGFiP, et la preuve que la leçon était connue.
- **Le précédent France Travail et sa sanction.** La [CNIL — « Violation de données : sanction de 5 millions d'euros à l'encontre de France Travail »](https://cnil.fr/fr/violation-de-donnees-sanction-5millions-france-travail) (22 janvier 2026) sanctionne une fuite de 2024 obtenue en usurpant des comptes de conseillers Cap emploi, partenaires extérieurs de l'opérateur. Les trois manquements retenus, authentification insuffisante des partenaires, journalisation incapable de détecter les comportements anormaux et habilitations trop larges, sont exactement ceux que l'ANSSI relève à la DGFiP.

### Compléments sur le sujet

Le rapport se concentre sur la mécanique technique d'un incident. Il laisse de côté quatre dimensions qui en changent la portée : l'économie des infostealers qui alimente ce type d'attaque, le profil réel des attaquants, la série d'incidents dont la DGFiP n'est qu'un épisode, et la réponse politique qu'il a déclenchée.

- **Les infostealers, fournisseurs industriels d'accès.** Le scénario que l'ANSSI suppose, des identifiants professionnels volés sur des appareils personnels, est désormais la norme statistique. Le [Verizon — « 2025 Data Breach Investigations Report »](https://www.verizon.com/business/resources/reports/2025-dbir-data-breach-investigations-report.pdf) (avril 2025) a relevé que 46 % des systèmes dont les journaux d'infostealer contenaient des identifiants d'entreprise étaient des appareils non administrés, qui mêlaient identifiants personnels et professionnels. Le cas Snowflake a montré que ces identifiants restent exploitables pendant des années si rien ne les invalide. La veille sur la revente de comptes que pratiquait la DGFiP, et dont le rapport montre les trous, se heurte donc à un stock énorme et ancien, que seule une authentification forte rend inutilisable.
- **Des attaquants très jeunes et déjà connus.** Le rapport ne dit rien des auteurs. Selon [Next — « Piratage de la DGFiP : deux suspects interpellés, l'enquête se poursuit »](https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/) (4 septembre 2026), un jeune homme de 18 ans de la région parisienne, interpellé le 18 août, a été mis en examen le 20 août et placé en détention provisoire, et un mineur de 16 ans, interpellé le 26 août, a été relâché après audition. Le premier avait déjà été mis en examen en juin 2024 et en janvier 2025 pour d'autres cyberattaques, sous contrôle judiciaire. Le groupe Zerobytes est aussi soupçonné d'attaques contre le ministère de l'Éducation nationale, France Travail et SFR. [Silicon — « Piratage de la DGFiP : ce que l'on sait vraiment »](https://www.silicon.fr/cybersecurite-1371/piratage-de-la-dgfip-ce-que-lon-sait-vraiment-228727) (18 août 2026) rapporte que le groupe se présentait lui-même comme un « binôme français ». Le jugement de l'ANSSI sur une attaque « non sophistiquée » s'en trouve pleinement confirmé.
- **Un été de fuites dans l'État, et trois incidents à la DGFiP.** Le rapport traite deux fuites ; la DGFiP en a connu une troisième. La note de la commission des finances du Sénat, présentée par Claude Raynal et Jean-François Husson, en décrit trois vecteurs : les identifiants d'agents via le RIE pour E-Contact, le compte du géomètre-expert pour des données cadastrales concernant **434 564 foyers**, et une vulnérabilité technique d'un outil de traitement statistique pour les successions vacantes, détectée mi-août ([INCYBER News — « Piratage DGFiP : le Sénat pointe des failles »](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/), 9 septembre 2026). Selon la même source et [Banque des Territoires](https://www.banquedesterritoires.fr/cyberattaque-de-la-dgfip-lanssi-lance-reactiv-le-senat-pointe-les-limites-des-acces-partages) (8 septembre 2026), les sénateurs insistent sur la multiplication des accès tiers, et la DGFiP comptait 7 810 cyberattaques détectées à fin août 2026, contre 2 579 en 2023. Next recense la même année l'Agence nationale des titres sécurisés en avril, puis le ministère de l'Éducation nationale, le ministère de l'Intérieur, le cadastre et les successions vacantes ([Next — « Cybersécurité : l'ANSSI lance son mécanisme REACTIV dédié aux services de l'État »](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/), 8 septembre 2026). L'incident DGFiP est donc le symptôme d'une vulnérabilité générale de l'État.
- **La réponse politique déborde le rapport.** Le Premier ministre Sébastien Lecornu a réuni une cellule interministérielle de crise mi-août et commandé à l'ANSSI l'audit dont le rapport est issu ([Silicon](https://www.silicon.fr/cybersecurite-1371/piratage-de-la-dgfip-ce-que-lon-sait-vraiment-228727), 18 août 2026 ; [ANSSI](https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/), 29 septembre 2026). Côté Bercy, le ministre David Amiel a annoncé dans une lettre aux responsables de la commission des finances du Sénat le rattachement du responsable de la sécurité des systèmes d'information directement au directeur général, 10 millions d'euros supplémentaires en 2026 portant le budget cyber à 28 millions, des clés USB sécurisées pour l'authentification des agents d'ici fin 2026, des quotas de connexion sur les applications sensibles et une formation obligatoire ([Acteurs publics — « Cyberattaque du fisc : l'administration prend acte et repense sa gouvernance cyber »](https://acteurspublics.fr/articles/cyberattaque-du-fisc-ladministration-prend-acte-et-repense-sa-gouvernance-cyber/), septembre 2026). Plusieurs de ces mesures reprennent mot pour mot les recommandations du rapport.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
|---|---|---|
| Près de 353 000 particuliers et 252 000 professionnels concernés par la fuite E-Contact (p. 4) | **Nuancé.** La note du Sénat retient le même ordre de grandeur (350 000 et 250 000), mais la DGFiP a annoncé le 14 août « environ 678 000 comptes », soit le chiffre revendiqué ; les deux comptages coexistent sans explication publique | [INCYBER News](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/) (9 septembre 2026) ; [Silicon](https://www.silicon.fr/cybersecurite-1371/piratage-de-la-dgfip-ce-que-lon-sait-vraiment-228727) (18 août 2026) |
| Revendication de 2 millions de Français concernés par la fuite du cadastre (p. 20) | **Non établi.** La note du Sénat parle de 434 564 foyers ; le rapport ne donne aucun chiffre vérifié | [INCYBER News](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/) (9 septembre 2026) |
| Attaque « non sophistiquée » fondée sur des identifiants volés (p. 4) | **Confirmé.** Deux suspects de 18 et 16 ans interpellés, dont un déjà mis en examen pour des faits similaires | [Next](https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/) (4 septembre 2026) |
| Accès au RIE rendu possible par la compromission d'infrastructures du ministère de l'Éducation nationale (p. 8) | **Nuancé.** La note du Sénat évoque plus précisément la compromission du compte d'un agent de ce ministère ; les deux descriptions sont compatibles mais la seconde est plus précise | [INCYBER News](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/) (9 septembre 2026) |
| Aucune exfiltration détectée par la supervision (p. 4) | **Confirmé.** Les sénateurs relèvent que des comptes ont été désactivés mais que les volumes anormaux d'extraction n'ont pas été identifiés | [INCYBER News](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/) (9 septembre 2026) |
| Les identifiants volés et l'absence de MFA suffisent à compromettre une grande organisation (p. 4, 6-7) | **Confirmé.** Même scénario documenté pour 165 organisations clientes de Snowflake | [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion) (10 juin 2024) |
| L'ANSSI a « mis en place un plan d'action » avec la DGFiP (p. 5) | **Confirmé.** Bercy annonce clés d'authentification, quotas, budget et nouvelle gouvernance | [Acteurs publics](https://acteurspublics.fr/articles/cyberattaque-du-fisc-ladministration-prend-acte-et-repense-sa-gouvernance-cyber/) (septembre 2026) |

### Contrepoints et critiques

- **Le rapport met en avant les usages des agents plus que l'exposition des applications.** La cause première désignée est l'appareil personnel. Les sénateurs, eux, insistent sur la multiplication des accès tiers et sur l'ouverture des applications ([Banque des Territoires](https://www.banquedesterritoires.fr/cyberattaque-de-la-dgfip-lanssi-lance-reactiv-le-senat-pointe-les-limites-des-acces-partages), 8 septembre 2026). Le cas Snowflake montre qu'une simple liste d'adresses autorisées aurait neutralisé des identifiants volés : c'est un choix d'architecture de l'organisation, pas une faute de l'utilisateur. Le rapport le recommande, mais sa synthèse place l'identité en tête.
- **Une sanction impossible contre l'État.** La présidente de la CNIL, Marie-Laure Denis, a annoncé le 10 septembre un contrôle de la DGFiP et de l'Agence nationale des titres sécurisés, en rappelant que l'autorité ne peut infliger d'amende à l'État et que l'issue sera une mise en demeure ou une sanction non pécuniaire ([Le Monde — « Piratage du site des impôts : la CNIL va contrôler le fisc »](https://www.lemonde.fr/pixels/article/2026/09/11/piratage-du-site-des-impots-la-cnil-va-controler-le-fisc-apres-le-vol-de-donnees-massif-survenu-durant-l-ete_6770181_4408996.html), 11 septembre 2026). France Travail, pour les mêmes manquements, a payé 5 millions d'euros. Cette asymétrie affaiblit l'incitation à corriger que le rapport cherche à créer.
- **Un effort de l'ANSSI prélevé sur d'autres missions.** Le directeur de l'ANSSI, Vincent Strubel, a précisé que le dispositif REACTIV né de cette crise est « temporaire » et se fait « au détriment d'autres pans de la menace » ([Next](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/), 8 septembre 2026). Le rapport ne dit rien des moyens de supervision applicative dont l'agence aurait besoin pour ne plus être aveugle, alors qu'il reconnaît cette lacune (p. 8).

### Évolutions depuis la publication

Le rapport date du 23 septembre 2026 ; les faits postérieurs à sa rédaction sont encore peu nombreux, mais plusieurs décisions prises pendant sa préparation en modifient la lecture.

- **Une nouvelle capacité d'injonction pour l'ANSSI.** Annoncé le 7 septembre, REACTIV (« Réponse et action interministérielle face aux violations de données ») permet à l'ANSSI d'imposer aux ministères des mesures de protection dans des délais contraints et de centraliser la communication technique de crise ; il complète la feuille de route de sécurité numérique de l'État 2026-2027, dont le Premier ministre a demandé l'accélération ([ANSSI — « Cyberattaques : l'ANSSI met en place une capacité renforcée de réaction dédiée aux services de l'État »](https://cyber.gouv.fr/actualites/cyberattaques-lanssi-met-en-place-une-capacite-renforcee-de-reaction-dediee-aux-services-de-letat/), 7 septembre 2026). C'est la réponse institutionnelle au défaut de coordination que décrit le rapport (p. 8-9).
- **Publication et remise au Premier ministre.** Le rapport a été remis le 24 septembre et publié le 29 septembre 2026 ([ANSSI](https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/)).
- **Contrôle de la CNIL en cours.** Annoncé le 10 septembre, il pourrait déboucher sur une mise en demeure d'ici la fin de l'année ([Le Monde](https://www.lemonde.fr/pixels/article/2026/09/11/piratage-du-site-des-impots-la-cnil-va-controler-le-fisc-apres-le-vol-de-donnees-massif-survenu-durant-l-ete_6770181_4408996.html), 11 septembre 2026).
- **Enquête judiciaire en cours.** Menée par l'Office anticybercriminalité sous l'autorité du parquet de Paris, elle cherche à identifier d'autres participants ([Next](https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/), 4 septembre 2026).

### Cadre juridique et éthique

- **RGPD — sécurité et notification des violations.** Le responsable de traitement doit assurer une sécurité adaptée, notifier la violation à la CNIL et informer les personnes en cas de risque élevé. La DGFiP a notifié la CNIL et informé individuellement les usagers concernés par courriel ([Silicon](https://www.silicon.fr/cybersecurite-1371/piratage-de-la-dgfip-ce-que-lon-sait-vraiment-228727), 18 août 2026). Pour France Travail, la CNIL a jugé que l'authentification des partenaires, la journalisation et les habilitations relevaient de cette obligation de sécurité ([CNIL](https://cnil.fr/fr/violation-de-donnees-sanction-5millions-france-travail), 22 janvier 2026).
- **Pouvoirs de la CNIL envers l'État.** L'autorité peut contrôler, mettre en demeure et sanctionner, mais ne peut pas infliger d'amende à l'État ([Le Monde](https://www.lemonde.fr/pixels/article/2026/09/11/piratage-du-site-des-impots-la-cnil-va-controler-le-fisc-apres-le-vol-de-donnees-massif-survenu-durant-l-ete_6770181_4408996.html), 11 septembre 2026).
- **Droit pénal — atteintes aux systèmes de traitement automatisé de données.** Le parquet de Paris poursuit notamment pour accès et maintien frauduleux dans un système de données à caractère personnel en bande organisée, et pour association de malfaiteurs ([Next](https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/), 4 septembre 2026) ; les peines encourues vont jusqu'à sept ans d'emprisonnement ([Silicon](https://www.silicon.fr/cybersecurite-1371/piratage-de-la-dgfip-ce-que-lon-sait-vraiment-228727), 18 août 2026).
- **Doctrine de l'État.** La feuille de route de sécurité numérique de l'État 2026-2027, citée par le rapport (p. 5), et REACTIV fixent le cadre d'action interministériel ; ce ne sont pas des textes législatifs, mais des engagements du gouvernement dont REACTIV renforce le caractère contraignant pour les ministères.

### Pour aller plus loin

- [ANSSI — page de publication du rapport](https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/) (29 septembre 2026) : la présentation officielle et le lien vers le PDF.
- [ANSSI — « Recommandations relatives à l'authentification multifacteur et aux mots de passe »](https://messervices.cyber.gouv.fr/guides/recommandations-relatives-lauthentification-multifacteur-et-aux-mots-de-passe) (2021) : le guide de référence pour choisir un second facteur qui résiste au vol du premier.
- [Mandiant — campagne UNC5537 contre les clients de Snowflake](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion) (2024) : le cas d'école des identifiants volés par infostealers, avec guide de recherche de menaces.
- [CNIL — sanction de France Travail](https://cnil.fr/fr/violation-de-donnees-sanction-5millions-france-travail) (2026) : ce que le régulateur attend en matière d'accès des partenaires et de journalisation.
- [Next — REACTIV](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/) (2026) : la réponse de l'ANSSI replacée dans la série d'incidents de l'État en 2026.
