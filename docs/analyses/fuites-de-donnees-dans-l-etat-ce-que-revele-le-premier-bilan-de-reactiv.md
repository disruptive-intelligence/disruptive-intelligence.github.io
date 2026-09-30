---
title: "Analyse — Fuites de données dans l’État : ce que révèle le premier bilan de REACTIV"
date: 2026-09-30
kind: analysis
theme: cyber
slug: fuites-de-donnees-dans-l-etat-ce-que-revele-le-premier-bilan-de-reactiv
organization: "Agence nationale de la sécurité des systèmes d’information (ANSSI) — CERT-FR"
tags:
  - REACTIV
  - ANSSI
  - CERT-FR
  - fuite de données
  - Metabase
  - infostealer
  - authentification multifacteur
  - administration publique
source_file: inbox/CERTFR-2026-CTI-006.pdf
source_url: https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/
events:
  - evt-6b42289b-6f48-4cd7-8d3f-0ceedab5f17c
  - evt-c9511822-9545-4867-bcb1-93c579977a9f
  - evt-505123c8-a2a8-464e-91fd-37b311e52f57
---

# Analyse — Fuites de données dans l’État : ce que révèle le premier bilan de REACTIV

## Métadonnées

- **Document :** *REACTIV. Point de situation. Septembre 2026*, 10 pages, dont une couverture, une quatrième de couverture et une page presque vide.
- **Éditeur :** Agence nationale de la sécurité des systèmes d'information (ANSSI), dont le logo figure en couverture avec le bloc « République française » et celui du CERT-FR ; l'adresse de l'ANSSI clôt le document (p. 10). Aucun rédacteur n'est nommé.
- **Date :** « Septembre 2026 », sans jour précis (p. 1). Le CERT-FR l'a mis en ligne le 30 septembre 2026 sous la référence CERTFR-2026-CTI-006, dans sa série de rapports sur la menace et les incidents.
- **Support :** PDF conservé dans `inbox/CERTFR-2026-CTI-006.pdf`.
- **Périmètre :** les violations de données qui ont touché les services de l'État depuis le 1er août 2026, dans le cadre de l'opération REACTIV lancée par le Premier ministre le 1er septembre.
- **Méthode de la fiche :** jusqu'aux « Cinq éléments essentiels », seule la lecture du PDF fonde les constats, avec renvoi aux pages. La dernière section confronte ces constats à des sources extérieures citées et datées.

## Repères pour comprendre le document

Le texte n'est ni un rapport d'enquête ni une étude de la menace : c'est un **point de situation opérationnel**, un état des lieux dressé en cours d'opération, que l'ANSSI présente elle-même comme provisoire et non exhaustif (p. 2). Il se lit en deux temps. Une première partie présente l'opération REACTIV puis synthétise l'ensemble des incidents : volume, vulnérabilités récurrentes, données exposées, rôle de l'ANSSI (p. 2-4). Une seconde partie résume les incidents ministère par ministère, en quelques lignes chacun (p. 5-9). Le lecteur doit garder en tête une distinction que le document installe dès sa page 3 : un « événement de sécurité » peut être un simple signalement ou un incident avéré, et les chiffres globaux mélangent les deux.

- **REACTIV** — « Réponse et action interministérielle face aux violations de données » : opération de cyberdéfense demandée le 1er septembre 2026 par le Premier ministre, qui réoriente les moyens de l'ANSSI vers l'appui aux ministères victimes de fuites de données (p. 2).
- **Violation de données** — Atteinte à la sécurité qui entraîne la perte de confidentialité, d'intégrité ou de disponibilité de données, le plus souvent ici leur vol. *Définition ajoutée :* le document emploie le terme sans le définir.
- **Signalement et incident** — Un signalement porte sur un événement indésirable qui menace un système ; il devient un incident lorsque la compromission est avérée ou l'attaque réussie (p. 3, note 1).
- **Metabase** — Logiciel libre de tableaux de bord et de statistiques, qui se connecte aux bases de données d'une application pour les interroger. *Explication ajoutée :* le document le nomme sans le décrire.
- **Injection SQL** — Technique qui fait exécuter par l'application une requête de base de données fabriquée par l'attaquant ; c'est le mécanisme de la faille Metabase (p. 3-4).
- **IDOR** — Vulnérabilité d'accès direct à un objet (fiche, document, compte) en modifiant son identifiant dans une requête, faute de contrôle des autorisations. Le document la définit comme un accès « sans authentification ou identification préalable » (p. 3, note 4) ; *précision ajoutée :* le terme usuel est *Insecure Direct Object Reference*, et la faille touche souvent des utilisateurs déjà connectés qui accèdent aux objets d'autrui.
- **Infostealer** — Programme malveillant qui vole des informations sensibles, notamment des identifiants de connexion (p. 3, note 2).
- **Second facteur faible** — Code d'authentification envoyé par courriel : il ne protège pas si la messagerie s'ouvre avec le mot de passe déjà volé (p. 3).
- **Compromission par rebond** — Attaque qui atteint une administration à travers un prestataire ou un sous-traitant compromis (p. 3, 6).
- **Latéralisation** — Déplacement d'un attaquant d'un système compromis vers d'autres systèmes reliés (p. 5, 7).
- **Marqueurs de compromission** — Indices techniques d'une attaque (adresses, fichiers, comportements) que l'ANSSI partage pour permettre à d'autres victimes de se reconnaître ; plusieurs détections du document en découlent (p. 4, 6-7).
- **PASSI** — Prestataire d'audit de la sécurité des systèmes d'information qualifié par l'ANSSI, chargé ici d'un premier audit à la DGFiP (p. 6).

## Résumé exécutif

Le document dresse le premier bilan public de l'opération REACTIV, lancée par le Premier ministre le 1er septembre 2026 face à « l'intensification des attaques cybercriminelles » visant les données de l'État (p. 2). Son chiffre central est net : depuis le 1er août 2026, **99 violations de données** ont été portées à la connaissance de l'ANSSI, dont **67 confirmées** (p. 3). Il en tire six causes récurrentes et décrit une vingtaine d'incidents dans sept ensembles ministériels, de l'Éducation nationale aux services du Premier ministre (p. 3, 5-9).

Le diagnostic tient en deux familles de failles. D'un côté, des **accès volés** : identifiants dérobés par infostealers sur des postes personnels ou récupérés dans d'anciennes fuites, qui ouvrent des services exposés sans double authentification ou protégés par un simple code envoyé par courriel. De l'autre, des **applications vulnérables** : une faille d'injection SQL dans Metabase, exploitée massivement depuis début août et qui a compromis neuf instances ministérielles, des failles IDOR qui ont permis l'exfiltration massive de documents, et des défauts courants de développement et de configuration (p. 3-4). S'y ajoute un cas de compromission par un sous-traitant (p. 3, 6).

Les incidents couvrent des données très diverses : fiscales et cadastrales à la DGFiP, dossiers d'enseignants et d'élèves à l'Éducation nationale, conversations Tchap, boîtes de messagerie d'un bureau numérique interministériel, fichiers de propriétaires de logements vacants, comptes du Service national universel. Le cas le plus massif, la plateforme Zéro Logement Vacant, concernerait **48 millions de propriétaires** (p. 7). L'ANSSI décrit son propre rôle comme un appui : coordination technique, partage de marqueurs, aide à l'analyse forensique et à la remédiation, alertes sur Metabase et durcissement des authentifications (p. 4). Plusieurs détections ont d'ailleurs été déclenchées par ces marqueurs partagés (p. 6-7).

Pour la veille, c'est le **premier panorama officiel** de la vague de fuites de l'été 2026 dans l'État, et un document d'une franchise rare : l'ANSSI y inscrit la compromission de son propre laboratoire d'innovation (p. 8). Sa valeur reste limitée par son caractère provisoire, par des chiffres parfois contradictoires d'une page à l'autre et par l'absence de toute information sur les attaquants.

## Chronologie

Le document ne présente pas de chronologie ; les jalons ci-dessous sont reconstitués à partir des incidents qu'il décrit.

- **Fin juin – mi-juillet 2026 :** exfiltration de données chez le sous-traitant d'assistance du portail de télédéclaration de TRACFIN (p. 6).
- **Juillet – fin juillet :** incidents dans plus d'une dizaine d'académies ; intrusion détectée sur le système GAIA de l'Éducation nationale (p. 5).
- **1er août :** début de la période couverte par le décompte de l'ANSSI (p. 3).
- **Début août :** début de l'exploitation massive de la faille Metabase ; le correctif est disponible le **6 août** (p. 3).
- **7 août :** fuite de numéros de téléphone depuis un compte professionnel de Bloctel ; **8 août :** compromission de France VAE par la faille Metabase ; **11 août :** fermeture définitive de Bloctel (p. 6, 8).
- **12 août :** violation de données à l'Agence pour l'enseignement français à l'étranger (AEFE) ; **12-13 août :** détection des incidents de la DGFiP (p. 5-6).
- **17 août :** revendication d'une fuite concernant enseignants et élèves, révélant l'exfiltration de la base élèves SIECLE de l'académie de Créteil (p. 5).
- **19 août :** la DINUM détecte la compromission d'un compte Tchap d'un agent de l'Éducation nationale ; **21 août :** les douanes relient trois comptes de messagerie compromis à un serveur d'échange grâce aux marqueurs de l'ANSSI (p. 5-6).
- **25 août :** détection de plus de 300 comptes compromis sur le Bureau numérique du ministère de la Transition écologique ; revendication de l'exfiltration de Docurba (p. 7-8).
- **28 août :** l'ANSSI est informée de la revendication visant Zéro Logement Vacant (p. 7).
- **1er septembre :** le Premier ministre demande à l'ANSSI de lancer REACTIV (p. 2).
- **Début septembre :** revendication visant Préférence Formation ; **7 septembre :** revendication d'une fuite sur un portail du Service national universel (p. 5, 9).

## Thèse principale

Le document soutient implicitement que la vague de fuites qui frappe l'État ne tient pas à une attaque d'exception, mais à l'**accumulation de faiblesses élémentaires** exploitées à grande échelle : identifiants volés, absence de second facteur robuste, applications non mises à jour ou mal développées, prestataires mal maîtrisés (p. 3-4). Face à ce constat, il présente REACTIV comme une réponse d'autorité autant que de moyens : l'ANSSI peut désormais « faire prendre aux ministères, dans des délais contraints, les mesures d'urgence » et centralise la communication technique de crise (p. 2).

C'est un texte d'**information institutionnelle**, à mi-chemin entre le bilan opérationnel et la démonstration d'action publique. Il n'argumente pas : il recense, et laisse le lecteur conclure de la répétition des mêmes causes d'un ministère à l'autre.

## Informations et arguments importants

### L'opération REACTIV : une bascule plus qu'une structure

REACTIV n'est pas présenté comme un nouveau service, mais comme un « basculement immédiat des efforts opérationnels » de l'ANSSI vers deux tâches, le traitement des comptes utilisateurs compromis et l'analyse des violations de données (p. 2). Le dispositif complète la feuille de route de sécurité numérique de l'État 2026-2027, dont le Premier ministre a demandé l'accélération. Deux pouvoirs nouveaux le distinguent du rôle habituel de conseil de l'agence :

- **Un pouvoir d'injonction :** l'ANSSI peut faire prendre aux ministères, dans des délais contraints, les mesures d'urgence nécessaires pour protéger les données des citoyens.
- **Une communication centralisée :** l'ANSSI pilote la communication technique de crise lorsqu'une attaque de ce type touche des services de l'État.

### Le volume : 99 violations en deux mois

Depuis le 1er août 2026, 99 violations de données ont été portées à la connaissance de l'ANSSI ; 67 sont confirmées, dont 32 en cours de traitement par l'agence (p. 3). La note qui accompagne ces chiffres précise qu'ils agrègent signalements et incidents, et un encadré prévient qu'ils sont « susceptibles d'évoluer » (p. 2-3). Le document n'en donne ni la répartition par ministère ni la répartition par vecteur d'attaque.

### Six causes récurrentes

L'ANSSI regroupe les causes observées en six familles, de la plus spécifique à la plus diffuse (p. 3-4).

1. **La faille Metabase (CVE-2026-72898).** Une injection SQL permet à un utilisateur non authentifié d'accéder à la base de données de l'application et d'obtenir les droits d'administrateur. Exploitée massivement depuis début août, elle a compromis neuf instances ministérielles ; le correctif existe depuis le 6 août, et l'ANSSI a demandé à tous les ministères d'inventorier et de mettre à jour leurs instances.
2. **Les comptes volés par infostealers.** Des identifiants dérobés sur des postes personnels utilisés à titre professionnel, ou issus de fuites antérieures, ouvrent des services exposés sans double authentification ; c'est « un vecteur initial marquant ».
3. **Les failles IDOR.** Plusieurs ont été exploitées dans le périmètre ministériel, parfois combinées à d'autres faiblesses, et ont permis l'exfiltration massive de documents.
4. **L'absence de double authentification ou un second facteur faible.** C'est le « facteur clé de nombreux incidents » : sans second facteur, ou avec un code par courriel, un mot de passe faible ou divulgué suffit à entrer.
5. **La sous-traitance.** Un incident illustre la compromission par rebond : le vol de données du ministère s'est produit dans l'infrastructure du prestataire.
6. **Les défauts de développement et de configuration.** Rarement vecteur d'intrusion, mais souvent présents : absence de contrôle des autorisations, injections SQL, fichiers exposés.

### Ce qui a été exposé

Le document classe les données exposées en cinq catégories (p. 4). Les données **fiscales et patrimoniales** concernent près de 353 000 particuliers, 252 000 professionnels et 434 000 propriétaires dans le cadre du serveur cadastral. Les données **d'identification et de contact** touchent plus de 30 000 utilisateurs de l'AEFE, 275 000 utilisateurs du Service national universel, 3 millions de numéros de téléphone pour Bloctel et 5 265 personnes pour Préférence Formation. S'y ajoutent des données **professionnelles** (identifiants fiscaux, numéros SIREN et SIRET, certifications, données d'enseignants et de contrôleurs techniques), **techniques** (journaux de connexion, comptes techniques, mots de passe hachés) et des **conversations** (Tchap, courriels, échanges avec le support). Les personnes concernées ont été informées « lorsque la nature des données le justifiait ».

### Les incidents, ministère par ministère

La seconde partie décrit les incidents en quelques lignes chacun (p. 5-9). Ils se regroupent en trois types selon leur mode opératoire.

#### Les comptes compromis

C'est le cas le plus fréquent. À l'**AEFE**, un compte compromis a permis d'accéder à l'annuaire interne et d'en extraire des informations sur plus de 300 000 personnes selon la page 5 (p. 5). À **Bloctel**, un compte professionnel d'entreprise a servi à télécharger les listes de numéros soumises et traitées, d'où l'identification par différence d'environ 600 000 inscrits ; le service a été fermé le 11 août (p. 6). Sur **Tchap**, le compte d'un agent de l'Éducation nationale a donné accès à des salons, dont certains de la DGFiP et du cadastre, dont les conversations ont été exfiltrées (p. 5). À la **DGFiP**, un compte de géomètre-expert a permis d'extraire environ 2 millions de données cadastrales concernant 434 000 usagers, et des identifiants volés par infostealers ont été essayés sur le PIGP (p. 6). Aux **douanes**, trois comptes de messagerie compromis menaient à un serveur d'échange avec des prestataires (p. 6). Au **Bureau numérique** de la Transition écologique, plus de 300 comptes compromis ont ouvert une messagerie mutualisée entre ministères et des espaces de fichiers, intégralement exfiltrés ; l'activation de la double authentification a ensuite empêché certains utilisateurs de se connecter (p. 7). Sur le portail **OISO**, le compte d'un organisme privé a permis d'énumérer les données de 22 000 agents et organismes agréés (p. 7).

#### La faille Metabase

Six services, soit sept instances, en relèvent de façon avérée ou suspectée ; le document n’identifie donc pas les neuf instances ministérielles annoncées page 3 (p. 7-8) :

- **Zéro Logement Vacant**, plateforme des collectivités pour repérer les logements durablement vacants : point d'entrée présumé par une instance Metabase, service coupé, violation qui concernerait 48 millions de propriétaires.
- **Qualicharge**, gestion des bornes de recharge : 102 000 sessions de recharge et une centaine de comptes techniques exfiltrés.
- **Docurba**, plateforme de la DGALN pour les documents d'urbanisme : compromission revendiquée le 25 août, datant probablement de plusieurs mois.
- **Laboratoire d'innovation de l'ANSSI** : 118 comptes Metabase compromis, dont une trentaine d'utilisateurs externes.
- **DINUM** : deux instances (ProConnect et Nuage-Public) compromises, pour des données déjà publiques selon le document.
- **France VAE** : accès privilégié obtenu le 8 août et exfiltration de l'intégralité des données utilisateurs.

#### Les failles applicatives et la sous-traitance

Le portail du **Service national universel** aurait été exploité par une faille IDOR, exposant 275 000 utilisateurs (p. 5). Chez **TRACFIN**, c'est le sous-traitant de l'opérateur du support aux déclarants qui a été compromis, exposant 136 assujettis et le contenu de 213 demandes d'assistance, sans donnée relative aux déclarations de soupçon ; l'administration a rompu avec le prestataire (p. 6). À l'**Éducation nationale**, l'attaquant a pu se latéraliser vers plusieurs services nationaux : le système GAIA aurait livré les données de 4,35 millions d'enseignants, et la base élèves SIECLE de l'académie de Créteil celles d'un million d'élèves, de leurs responsables légaux et d'enseignants (p. 5). Deux incidents de la Transition écologique, Signal Logement et le Bureau des courriers parlementaires, sont encore « en cours de qualification » (p. 7).

### Les remédiations observées

Le document montre des réponses assez homogènes : réinitialisation des mots de passe, révocation des sessions, mise à jour des instances vulnérables, isolement des services du réseau interministériel, coupure de services entiers (Zéro Logement Vacant, OISO, solution d'échange des douanes), retrait de l'accès à la messagerie depuis Internet et activation généralisée de la double authentification (p. 5-8). À la DGFiP, l'ANSSI conduit une revue des investigations et pilote un premier audit confié à un PASSI (p. 6).

## Points particulièrement intéressants pour la veille

- **Un outil de statistiques devenu porte d'entrée.** Metabase, logiciel annexe de tableaux de bord, a servi de point d'entrée vers des bases de production dans au moins six services (p. 7-8). *Inférence pour la veille :* les outils d'analyse et de visualisation, souvent déployés vite et exposés pour faciliter le partage, détiennent des accès directs aux données ; ils méritent le même suivi de vulnérabilités que les applications métier.
- **La vitesse d'exploitation dépasse celle des correctifs.** Le correctif Metabase date du 6 août ; France VAE est compromis le 8 (p. 3, 8). *Inférence pour la veille :* pour une faille critique exploitable sans authentification, la fenêtre de mise à jour se compte en heures, ce qui justifie de suivre les alertes du CERT-FR en temps réel.
- **Le partage de marqueurs fonctionne.** Les douanes et la Transition écologique ont détecté leurs compromissions grâce aux marqueurs diffusés par l'ANSSI (p. 6-7). *Inférence pour la veille :* c'est la réponse directe au défaut de coordination relevé dans le rapport sur la DGFiP, où des marqueurs partagés en juin n'avaient pas été exploités à temps.
- **Des messageries internes comme cibles.** Tchap, le Bureau numérique et les messageries des douanes ont été vidés de leur contenu (p. 5-7). *Inférence pour la veille :* au-delà des fichiers d'usagers, les conversations entre agents deviennent une matière exploitable pour l'hameçonnage ciblé et la connaissance interne de l'État.
- **La double authentification a un coût d'usage.** Son activation au Bureau numérique a bloqué des utilisateurs (p. 7). *Inférence pour la veille :* la généralisation annoncée du second facteur dans l'État se heurtera à des difficultés de déploiement qu'il faudra suivre.

## Faits, opinions et interprétations

### Faits rapportés par la source

Le document établit un décompte, **99 violations** signalées depuis le 1er août, dont **67 confirmées**, et décrit une vingtaine d'incidents avec leurs dates, leurs vecteurs et leurs volumes (p. 3, 5-9). Il rapporte la compromission de **neuf instances Metabase** ministérielles par la CVE-2026-72898, corrigée le 6 août (p. 3), et donne les volumes principaux : 353 000 particuliers et 252 000 professionnels à la DGFiP, 434 000 propriétaires au cadastre, 275 000 utilisateurs au SNU, 4,35 millions d'enseignants et un million d'élèves à l'Éducation nationale, 48 millions de propriétaires pour Zéro Logement Vacant (p. 4-7). Plusieurs de ces chiffres sont toutefois présentés au conditionnel ou comme revendiqués (« aurait exposé », « concernerait », « porterait »), et le document prévient qu'ils peuvent évoluer (p. 2, 5, 7, 9).

### Opinions ou positions de l'auteur

L'ANSSI qualifie l'absence de double authentification de « facteur clé de nombreux incidents » et les infostealers de « vecteur initial marquant » (p. 3). Elle juge les défauts de développement « plus marginalement utilisés comme vecteur d'intrusion » mais « présents couramment » (p. 3-4). Ces appréciations ne sont pas chiffrées. Le ton est celui de la mobilisation : le ministère de l'Éducation nationale « s'est rapidement mobilisé », les renforcements des douanes ont été « rapidement mis en œuvre » (p. 5-6).

### Interprétations et inférences

Le document suggère, sans l'affirmer, un lien entre plusieurs incidents : le compte Tchap de l'Éducation nationale donnait accès à des salons de la DGFiP et du cadastre (p. 5), la revendication du 17 août reprenait en partie les données de GAIA (p. 5), et les mêmes marqueurs ont révélé des compromissions dans plusieurs ministères (p. 6-7). Pour la présente analyse, le recensement dessine un **écosystème d'attaquants opportunistes** qui exploitent en série les mêmes faiblesses plutôt qu'une campagne unique ; le document ne dit rien de leur identité ni de leur nombre, ce qui rend cette lecture non vérifiable à partir de la seule source.

## Limites et points à vérifier

1. **Des chiffres contradictoires d'une page à l'autre.** L'AEFE compte « plus de 30 000 utilisateurs » page 4 et « plus de 300 000 personnes » page 5 ; Bloctel « 3 millions de numéros » page 4 et « environ 600 000 numéros inscrits » page 6. De plus, les données attribuées à l'AEFE page 5 (certifications, évaluations, financement de la validation des acquis de l'expérience) sont celles que le document décrit pour France VAE page 8, ce qui laisse soupçonner une erreur de rédaction.
2. **Un décompte sans ventilation.** Les 99 violations mélangent signalements et incidents, et ni leur répartition par ministère ni leur répartition par vecteur ne sont données (p. 3). Des jugements comme « facteur clé de nombreux incidents » ne peuvent donc pas être mesurés.
3. **Une synthèse des impacts sélective.** La page 4 omet les deux fuites les plus massives décrites plus loin, Zéro Logement Vacant (48 millions de propriétaires) et l'Éducation nationale (4,35 millions d'enseignants, un million d'élèves) (p. 5, 7). Le lecteur pressé qui s'arrête à la synthèse sous-estime l'ampleur de la situation.
4. **Des volumes revendiqués présentés comme des bilans.** Plusieurs chiffres viennent des attaquants et n'ont pas été vérifiés, ce que le conditionnel signale parfois mais pas toujours ; « 4,35 millions d'enseignants » et « 48 millions de propriétaires » sont donnés sans dire comment ils ont été comptés (p. 5, 7).
5. **Aucune information sur les attaquants.** Le document ne nomme aucun acteur, ne dit pas si les incidents sont liés entre eux et ne mentionne pas les procédures judiciaires. C'est un choix compréhensible pour un document opérationnel, mais il empêche d'évaluer l'hypothèse d'une campagne coordonnée.
6. **Des définitions techniques imprécises.** La note 3, appelée sur le mot « identifiants », définit en réalité l'injection SQL, et la note 4 développe IDOR en *Indirect Object Reference* au lieu d'*Insecure Direct Object Reference*, en réduisant la faille à un accès sans authentification (p. 3). Ces erreurs comptent parce que le document se veut pédagogique pour les ministères.
7. **Une causalité implicite discutable.** Bloctel est dit « définitivement fermé le 11 août » juste après le récit de la fuite (p. 6), ce qui laisse croire à une fermeture due à l'incident ; le document ne donne pas la cause de cette fermeture.
8. **Un état figé d'une situation mouvante.** Plusieurs incidents sont « en cours de qualification » ou d'investigation (p. 5, 7, 9), et le document ne comporte pas de date précise. Il faudra le relire à la lumière des points de situation suivants.

## Sources et références mentionnées

Le document ne comporte pas de bibliographie : il repose sur les **informations opérationnelles de l'ANSSI** et des ministères concernés, sans citer de source extérieure. Il renvoie par des liens à deux documents publics : la feuille de route des efforts prioritaires en matière de sécurité numérique de l'État 2026-2027 (p. 2) et le bulletin d'alerte du CERT-FR sur la vulnérabilité Metabase (p. 3). Il mentionne des acteurs institutionnels (Premier ministre, DINUM, CSIRT de la DGDDI, DGALN) et des revendications publiques d'attaquants, sans jamais citer ces derniers. Cette construction en fait une source primaire sur la réponse de l'État, mais une source de seconde main, non vérifiée, sur plusieurs volumes de données revendiqués.

## Cinq éléments essentiels à retenir

1. Depuis le 1er août 2026, **99 violations de données** ont été signalées à l'ANSSI dans les services de l'État, dont **67 confirmées** ; REACTIV réoriente les moyens de l'agence et lui donne un pouvoir d'injonction envers les ministères.
2. Les causes sont **élémentaires et répétées** : identifiants volés par infostealers, absence de double authentification ou code par courriel, applications vulnérables ou mal configurées, prestataires compromis.
3. La faille **Metabase CVE-2026-72898**, exploitable sans authentification et corrigée le 6 août, a compromis neuf instances ministérielles, jusqu'au laboratoire d'innovation de l'ANSSI.
4. Les fuites touchent des **données fiscales, cadastrales, scolaires, professionnelles et des conversations internes** ; la plus massive, Zéro Logement Vacant, concernerait 48 millions de propriétaires.
5. Le document est **provisoire et parfois incohérent** dans ses chiffres (AEFE, Bloctel) et muet sur les attaquants : il faut en recouper les volumes avant de les reprendre.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-09-30. Les constats suivants complètent ou corrigent la lecture du PDF ; ils ne modifient pas les sections précédentes, fondées sur la seule source.

### Travaux de référence

- **L'alerte du CERT-FR sur Metabase.** Le bulletin [CERT-FR — « Vulnérabilité dans Metabase » (CERTFR-2026-ALE-010)](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-010/) (10 septembre 2026) est le document auquel renvoie le point de situation. Il confirme une exploitation étendue et donne aux administrateurs une méthode de détection : repérer dans les journaux une requête `POST /api/session/reset_password` en échec suivie d'un `GET /api/user/current` réussi. Il recommande, au-delà de la mise à jour, de révoquer les sessions, de contrôler les clés d'API et les comptes administrateurs et de changer les identifiants des bases connectées, ce qui rappelle qu'un correctif appliqué après compromission ne suffit pas.
- **L'avis de l'éditeur.** L'avis [Metabase — GHSA-vwf4-m7j8-wcjf](https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf) (6 août 2026) décrit une injection SQL par la route non authentifiée de réinitialisation de mot de passe, cotée **10 sur 10**, et confirme une exploitation active dès sa publication. L'analyse de [Bishop Fox — « Critical SQL Injection in Metabase via Password Reset »](https://bishopfox.com/blog/critical-sql-injection-in-metabase-via-password-reset-cve-2026-72898) (11 août 2026) en détaille le mécanisme : des champs non prévus dans la requête de réinitialisation atteignent la base comme expressions SQL.
- **Le rapport d'incident de la DGFiP.** Publié la veille par l'ANSSI, il détaille l'un des incidents que le point de situation résume en un paragraphe ; il est analysé sur ce site : [Piratage de la DGFiP : identifiants volés, réseau ouvert, supervision aveugle](https://disruptive-intelligence.github.io/analyses/piratage-de-la-dgfip-identifiants-voles-reseau-ouvert-supervision-aveugle/) (29 septembre 2026).

### Compléments sur le sujet

Le point de situation recense les incidents sans en raconter la dynamique. Quatre dimensions extérieures l'éclairent : la mécanique concrète de la faille Metabase dans l'écosystème numérique de l'État, l'écart entre lignes revendiquées et personnes réellement touchées, le profil des attaquants, et la réponse politique qui a précédé REACTIV.

- **Metabase, ou le prix des outils déployés vite.** Le cas de Zéro Logement Vacant montre comment un outil annexe devient la clé d'une base de production. Selon le récit de l'attaquant relayé par [Clubic — « Zéro Logement Vacant piraté : 148,9 millions de lignes de données revendiquées par ZeroBytes »](https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html) (29 août 2026), une instance Metabase exposée sous le domaine `beta.gouv.fr` donnait accès à une session de super-utilisateur, où figuraient en clair les identifiants de la base PostgreSQL de production. La fuite comprendrait environ 82 millions d'enregistrements issus des fichiers fonciers et fiscaux et quelque 3 500 comptes d'agents et de collectivités. Le mécanisme dépasse la seule faille logicielle : un outil de statistiques branché en direct sur les données sensibles, joignable depuis Internet et conservant des secrets en clair, combine trois erreurs de conception que le correctif ne corrige pas.
- **Des lignes aux personnes : lire les volumes.** Les chiffres qui circulent mesurent souvent des enregistrements, pas des individus. Pour Zéro Logement Vacant, les 148,9 millions de lignes revendiquées correspondent à environ 48 millions de personnes après dédoublonnage, un même propriétaire apparaissant pour chaque bien et chaque année ([Clubic](https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html), 29 août 2026). Pour l'Éducation nationale, les 4,35 millions « d'enseignants » sont des identifiants de personnels qui incluent anciens agents, retraités et personnels administratifs accumulés depuis des années ([FrenchBreaches — « Piratage massif de l'Éducation nationale »](https://frenchbreaches.com/blog/piratage-massif-de-leducation-nationale-des-millions-deleves-et-de-personnels-exposes), août 2026). Pour Bloctel, 3 millions de numéros figuraient dans les fichiers volés, dont 600 000 inscrits ([DGCCRF](https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/), août 2026). À l'inverse, le point de situation clarifie un chiffre du cadastre resté flou dans le rapport sur la DGFiP : « 2 millions » désigne des données cadastrales, et 434 000 le nombre d'usagers.
- **Des attaquants jeunes, opportunistes et prolifiques.** Le document ne nomme personne. Les revendications publiques désignent surtout ZeroBytes pour la DGFiP, l'Éducation nationale et Zéro Logement Vacant, et un acteur nommé LunarisSec pour le Service national universel, où une faille IDOR a été combinée à la création frauduleuse de comptes de responsables de structure ([FrenchBreaches — « Nouvelle fuite de données au Service national universel »](https://frenchbreaches.com/blog/nouvelle-fuite-de-donnees-au-service-national-universel-275-000-comptes-auraient-ete-compromis), septembre 2026). Deux suspects liés à ZeroBytes, âgés de 18 et 16 ans, ont été interpellés en août ; le premier avait déjà été mis en examen en 2024 et 2025 pour d'autres cyberattaques ([Next — « Piratage de la DGFiP : deux suspects interpellés, l'enquête se poursuit »](https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/), 4 septembre 2026). Le secteur public n'est pas seul visé : INCYBER recensait fin août une cinquantaine de fuites confirmées en France sur le mois, tous secteurs confondus ([INCYBER News — « France : les fuites de données d'août 2026 à retenir »](https://incyber.org/article/france-fuites-de-donnees-aout-2026-retenir/), 24 août 2026). Ce paysage confirme la lecture d'une vague opportuniste, où quelques acteurs exploitent en série des failles connues.
- **La réponse politique avant REACTIV.** Le 31 août, le Premier ministre Sébastien Lecornu a annoncé une unité d'intervention cyber composée d'agents de l'ANSSI, la double authentification pour les agents de la DGFiP d'ici fin 2026, des quotas d'accès aux données, un audit de l'ANSSI, le recours à l'IA pour la prévention et un programme de primes à la découverte de failles (*bug bounty*) pour les sites de l'État, avec 200 millions d'euros supplémentaires pour la cybersécurité des administrations ([Banque des Territoires — « Après la révélation de trois fuites de données fiscales, le gouvernement crée une unité cyber spécialisée »](https://www.banquedesterritoires.fr/apres-la-revelation-de-trois-fuites-de-donnees-fiscales-le-gouvernement-cree-une-unite-cyber), 31 août 2026). REACTIV est la mise en forme opérationnelle de cette « unité », annoncée publiquement le 7 septembre ([ANSSI](https://cyber.gouv.fr/actualites/cyberattaques-lanssi-met-en-place-une-capacite-renforcee-de-reaction-dediee-aux-services-de-letat/), 7 septembre 2026).

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
|---|---|---|
| Faille Metabase de type injection SQL, exploitable sans authentification, corrigée le 6 août (p. 3) | **Confirmé.** Avis de l'éditeur du 6 août, sévérité 10/10, exploitation active confirmée | [Metabase — GHSA-vwf4-m7j8-wcjf](https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf) (6 août 2026) ; [CERT-FR — ALE-010](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-010/) |
| AEFE : informations sur « plus de 300 000 personnes » (p. 5) | **Contredit.** L'AEFE et les relevés publics parlent d'environ 30 000 entrées d'annuaire (nom, fonction, courriel professionnel, ville, pays, photo), conformément à la page 4 du document | [AEFE — « Incident de cybersécurité »](https://aefe.gouv.fr/fr/actualites/incident-de-cybersecurite) (août 2026) ; [INCYBER News](https://incyber.org/article/france-fuites-de-donnees-aout-2026-retenir/) (24 août 2026) |
| Bloctel : 3 millions de numéros (p. 4), 600 000 inscrits identifiables (p. 6), fermeture le 11 août | **Nuancé.** Les deux chiffres sont exacts mais mesurent des choses différentes ; la fermeture découle de la loi du 30 juin 2025 instaurant le consentement préalable au démarchage, non de la fuite | [DGCCRF](https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/) (août 2026) |
| Zéro Logement Vacant : 48 millions de propriétaires concernés (p. 7) | **Nuancé.** Chiffre issu de la revendication (148,9 millions de lignes), ramené à environ 48 millions de personnes après dédoublonnage | [Clubic](https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html) (29 août 2026) |
| GAIA : données de 4,35 millions d'enseignants (p. 5) | **Nuancé.** Il s'agit d'identifiants de personnels incluant anciens agents et retraités, pas de 4,35 millions d'enseignants en poste | [FrenchBreaches](https://frenchbreaches.com/blog/piratage-massif-de-leducation-nationale-des-millions-deleves-et-de-personnels-exposes) (août 2026) |
| SNU : 275 000 utilisateurs exposés par une faille IDOR (p. 5) | **Nuancé.** Volume revendiqué ; le ministère évoque la création frauduleuse de comptes de responsables, combinée à la faille, et les comptes concernent surtout des structures partenaires | [FrenchBreaches](https://frenchbreaches.com/blog/nouvelle-fuite-de-donnees-au-service-national-universel-275-000-comptes-auraient-ete-compromis) (septembre 2026) |
| Cadastre : environ 434 000 usagers (p. 4, 6) | **Confirmé.** La note du Sénat retient 434 564 foyers | [INCYBER News — « Piratage DGFiP : le Sénat pointe des failles »](https://incyber.org/article/piratage-dgfip-senat-pointe-failles/) (9 septembre 2026) |

### Contrepoints et critiques

- **Une transparence réelle mais tardive et partielle.** Publier un bilan qui inclut la compromission de son propre laboratoire est inhabituel pour une agence de sécurité. Mais le document arrive après une série de révélations par les attaquants eux-mêmes et par la presse spécialisée : pour Zéro Logement Vacant, le SNU ou l'Éducation nationale, le public a appris l'essentiel par les revendications, relayées par des sites comme FrenchBreaches, bien avant ce point de situation.
- **Un effort prélevé sur d'autres missions.** Le directeur de l'ANSSI, Vincent Strubel, a présenté REACTIV comme un effort « temporaire », mené « au détriment d'autres pans de la menace » ([Next — « Cybersécurité : l'ANSSI lance son mécanisme REACTIV dédié aux services de l'État »](https://next.ink/brief-article/cybersecurite-lanssi-lance-son-mecanisme-reactiv-dedie-aux-services-de-letat/), 8 septembre 2026). Le point de situation ne dit rien des moyens mobilisés ni de ce qui est mis de côté pendant l'opération.
- **Une réponse d'urgence face à une dette structurelle.** Les causes recensées (applications non mises à jour, outils exposés, absence de second facteur) relèvent d'années de développement rapide et de faible maîtrise des applications de l'État. Une opération temporaire peut contenir les fuites en cours, mais pas corriger seule cette dette ; le plan gouvernemental du 31 août mise d'ailleurs sur des mesures de fond, double authentification et audits, dont les échéances courent jusqu'à fin 2026 ([Banque des Territoires](https://www.banquedesterritoires.fr/apres-la-revelation-de-trois-fuites-de-donnees-fiscales-le-gouvernement-cree-une-unite-cyber), 31 août 2026).

### Évolutions depuis la publication

Le document a été mis en ligne le 30 septembre 2026, jour de cette analyse ; aucun fait postérieur n'est encore connu. Deux publications de la même semaine en prolongent la lecture : le rapport d'incident de l'ANSSI sur la DGFiP, rendu public le 29 septembre ([ANSSI](https://cyber.gouv.fr/actualites/lanssi-publie-le-rapport-dincident-sur-les-cyberattaques-ayant-touche-la-dgfip/)), et le contrôle de la DGFiP annoncé par la CNIL le 10 septembre, qui pourrait déboucher sur une mise en demeure d'ici la fin de l'année ([Le Monde — « Piratage du site des impôts : la CNIL va contrôler le fisc »](https://www.lemonde.fr/pixels/article/2026/09/11/piratage-du-site-des-impots-la-cnil-va-controler-le-fisc-apres-le-vol-de-donnees-massif-survenu-durant-l-ete_6770181_4408996.html), 11 septembre 2026). Les prochains points de situation REACTIV permettront de vérifier si le rythme des violations ralentit.

### Cadre juridique et éthique

- **RGPD — notification des violations.** Les articles 33 et 34 imposent de notifier la CNIL dans les meilleurs délais, si possible sous 72 heures, et d'informer les personnes lorsque la violation présente un risque élevé pour elles ([CNIL — « Notifier une violation de données personnelles »](https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles)). C'est le critère que traduit la formule du document : informer « lorsque la nature des données le justifiait » (p. 4).
- **Pouvoirs de la CNIL envers l'État.** L'autorité peut contrôler et mettre en demeure les administrations, mais ne peut pas leur infliger d'amende ([Le Monde](https://www.lemonde.fr/pixels/article/2026/09/11/piratage-du-site-des-impots-la-cnil-va-controler-le-fisc-apres-le-vol-de-donnees-massif-survenu-durant-l-ete_6770181_4408996.html), 11 septembre 2026).
- **Démarchage téléphonique.** La loi du 30 juin 2025 a remplacé l'inscription sur liste d'opposition par le consentement préalable, d'où la fin de Bloctel le 11 août 2026 ([DGCCRF](https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/), août 2026).
- **Doctrine de l'État.** REACTIV et la feuille de route de sécurité numérique de l'État 2026-2027 sont des décisions gouvernementales, non des textes législatifs ; le pouvoir d'injonction de l'ANSSI envers les ministères découle de la demande du Premier ministre (p. 2).

### Pour aller plus loin

- [CERT-FR — page du point de situation REACTIV](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/) (30 septembre 2026) : le document et les autres rapports de la série CTI.
- [CERT-FR — alerte Metabase CERTFR-2026-ALE-010](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-010/) (2026) : versions touchées, marqueurs de détection et mesures après compromission.
- [Bishop Fox — analyse de CVE-2026-72898](https://bishopfox.com/blog/critical-sql-injection-in-metabase-via-password-reset-cve-2026-72898) (2026) : le fonctionnement technique de la faille.
- [Analyse du rapport d'incident de la DGFiP](https://disruptive-intelligence.github.io/analyses/piratage-de-la-dgfip-identifiants-voles-reseau-ouvert-supervision-aveugle/) (2026) : l'incident le mieux documenté de la série, vu de près.
- [INCYBER News — les fuites de données d'août 2026](https://incyber.org/article/france-fuites-de-donnees-aout-2026-retenir/) (2026) : le contexte des fuites hors de l'État sur la même période.
