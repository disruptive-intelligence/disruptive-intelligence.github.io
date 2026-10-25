---
title: "Bitchat et la CIA : chaîne de financement, métadonnées Bluetooth et ce que les preuves établissent"
date: 2026-10-25
kind: dossier
slug: bitchat-et-la-cia-chaine-de-financement-metadonnees-bluetooth-et-ce-que-les-preuves-etablissent
themes:
  - cyber
  - geo-ie
rubriques:
  - rens-opsec
  - geo-influence
  - geo-souverainete
tags:
  - Bitchat
  - Jack Dorsey
  - Bluetooth Low Energy
  - Nostr
  - métadonnées
  - NED
  - OpenSats
  - manifestations
  - désinformation
---

# Bitchat et la CIA : chaîne de financement, métadonnées Bluetooth et ce que les preuves établissent

Date de rédaction : 2026-10-25

## Sources de synthèse

- **[A1]** [Tor Project : distance avec Mullvad, argent de Washington et procès en double standard](../analyses/tor-project-distance-avec-mullvad-argent-de-washington-et-proces-en-double-standard.md)
- **[A2]** [Analyse — Commission européenne (JRC) et Europol : prospective des technologies de confidentialité](../analyses/commission-europeenne-jrc-et-europol-prospective-des-technologies-de-confidentialite.md)

Sélection de sources externes déterminantes ; l’annexe recense l’ensemble des pièces examinées.

- **[S1]** Christophe Boutry (@Ced_haurus), [fil de vérification sur X](https://x.com/Ced_haurus/status/2114336040567648471), 25 octobre 2026, et la publication accusatrice à laquelle il répond (trois liens : NED, OpenSats ×2).
- **[S2]** Bitchat, [*Protocol Whitepaper* v2.0](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md), 6 juillet 2026 : identité, annonces, relais, limites déclarées.
- **[S3]** Bitchat, [*Peer ID Rotation Specification*](https://github.com/permissionlesstech/bitchat/blob/main/docs/PEER-ID-ROTATION.md) et [*Privacy Assessment*](https://github.com/permissionlesstech/bitchat/blob/main/docs/privacy-assessment.md), juillet-octobre 2026 : ce qu’un observateur radio peut faire aujourd’hui.
- **[S4]** Bitchat Android, [revue de sécurité du 27 juillet 2026](https://github.com/permissionlesstech/bitchat-android/blob/main/docs/security-review-jul-27.md) : 2 failles critiques, 12 élevées, 16 moyennes.
- **[S5]** OpenSats, [états financiers 2022-2024](https://opensats.org/docs/financials/2022-2024.pdf) et [premier semestre 2025](https://opensats.org/docs/financials/2025-Q1-Q2.pdf), avec les annonces des dons de la HRF ([2025](https://opensats.org/blog/additional-ops-budget-from-hrf), [2026](https://opensats.org/blog/opensats-receives-funding-from-the-human-rights-foundation)).
- **[S6]** Trail of Bits, [« Building secure messaging is hard »](https://blog.trailofbits.com/2025/07/18/building-secure-messaging-is-hard-a-nuanced-take-on-the-bitchat-security-debate/), 18 juillet 2025 : lecture des premières failles.
- **[S7]** G. Aceto, V. Persico, A. Pescapè, [*Iran’s January 2026 Internet Shutdown*](https://arxiv.org/abs/2603.28753), arXiv, 30 mars 2026 : Bitchat, sa copie fermée Noghteha et l’Ouganda.
- **[S8]** TechCrunch, [ordre indien contre les dépôts GitHub](https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/) (24 juillet 2026) et [retrait des boutiques en Inde](https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/) (3 octobre 2026).

## Périmètre et méthode

Le point de départ est un échange sur X. Une publication, relayée selon Christophe Boutry par des comptes comme @Hannibal9972485 et @PhilConte007, affirme que « la CIA a financé » Bitchat, la messagerie Bluetooth lancée par Jack Dorsey, en reconstituant la chaîne **NED → Human Rights Foundation → OpenSats → Calle → Bitchat** ; d’autres messages du même courant présentent l’application comme un outil de surveillance des manifestants, évoquent des relais Nostr contrôlés par le renseignement et des nœuds de sortie Tor aux mains des agences américaines. Le 25 octobre 2026, Boutry publie un long fil qui vérifie ces affirmations une à une [S1]. Ce dossier examine **les deux textes** : l’accusation et sa réfutation.

Chaque lien cité a été ouvert. Les affirmations ont été recoupées avec des pièces primaires (comptes annuels d’OpenSats, déclarations fiscales de la HRF, annonces de la NED, code et documentation des deux dépôts Bitchat, notes de version), des analyses de sécurité indépendantes, un article scientifique, la presse internationale (TechCrunch, Bitcoin Magazine, France 24, presse indienne et française) et deux analyses déjà publiées sur ce site [A1, A2]. Le code source n’a pas été audité : il a été interrogé sur des points précis (relais par défaut, annuaire de relais). Quelques pages n’étaient pas accessibles (Reuters, archives du *Washington Post*, CNews) ; elles sont signalées comme telles et ne portent aucune conclusion à elles seules. Recherches arrêtées le **25 octobre 2026**.

La question posée mêle quatre niveaux qu’il faut séparer : **qui finance** (des flux d’argent documentés), **qui commande** (une relation de contrôle sur le logiciel), **ce que le logiciel expose** (des propriétés techniques vérifiables) et **qui peut en tirer parti** (un adversaire, avec des moyens et une position). L’accusation passe du premier au quatrième sans démontrer les deux du milieu.

## Résumé exécutif

1. **Aucune pièce ne relie la CIA à Bitchat.** Les trois liens cités par la publication accusatrice existent, mais ils documentent un partenariat d’événement entre la NED et la HRF (un hackathon de deux jours en septembre 2026), deux dons de la HRF au **budget de fonctionnement** d’OpenSats (250 000 et 116 000 dollars) et le fait que Calle, développeur subventionné par OpenSats, maintient Bitchat Android. Aucune subvention de la NED à la HRF n’a été trouvée ; la HRF ne déclare pas de subventions publiques dans ses comptes 2023 [S5].
2. **L’argent remonte surtout à Jack Dorsey lui-même.** OpenSats a reçu 37,6 millions de dollars de dons de 2022 à 2024 ; son principal financeur connu est #startsmall, la structure philanthropique de Dorsey (10 millions en 2023, et selon la presse 21 millions en 2024). Les 366 000 dollars de la HRF pèsent moins de 1 % des dons d’OpenSats sur la période 2022-mi-2025. La bourse de Calle date de juin 2024, pour Cashu, un an avant Bitchat [S5].
3. **Le soupçon a un terreau historique réel.** La NED reçoit 315 millions de dollars du Congrès pour 2026 ; l’un de ses fondateurs a dit en 1991 qu’elle faisait ouvertement ce que la CIA faisait en secret ; Washington a financé Tor, Signal et Briar au nom de l’« Internet Freedom » [A1] ; et l’USAID a créé en secret, de 2010 à 2012, un « Twitter cubain » (ZunZuneo) qui profilait ses utilisateurs, puis a sollicité Dorsey pour le reprendre. Ce contexte explique la méfiance, il ne prouve rien sur Bitchat.
4. **La faiblesse technique est réelle, et ses développeurs l’écrivent eux-mêmes.** Chaque téléphone diffuse un identifiant de 8 octets qui ne change jamais, son pseudonyme et ses clés publiques en clair, et la liste de dix voisins directs. Un récepteur placé dans une foule peut reconnaître un appareil d’un jour à l’autre et reconstituer qui se tenait près de qui ; la spécification officielle dit que le correctif n’est **pas déployé** [S2, S3]. Jusqu’en août 2026, l’écran de confidentialité iOS promettait pourtant une « identité éphémère », et la politique de confidentialité Android affirme toujours une clé « qui change à chaque session ».
5. **Ce défaut profite d’abord à qui est sur place, pas à une agence lointaine.** L’exposition est radio : elle sert la police ou le service de sécurité présent au cortège, ou tout acteur privé équipé. Les États qui ont agi contre Bitchat (Inde, Chine, Ouganda) lui reprochent l’inverse d’un outil d’espionnage : empêcher « l’interception légale, l’attribution et la traçabilité » [S8].
6. **Le fil de réfutation est solide, avec trois compléments.** Boutry établit correctement la chaîne de financement et les limites du protocole. Il sous-estime l’exposition côté Android (l’identifiant figure dans la réponse au balayage Bluetooth), ne mentionne ni la revue de sécurité Android de juillet 2026 [S4] ni les copies fermées comme Noghteha en Iran [S7], et ne relève pas que la protection Tor de Bitchat n’a pas de ponts : là où Tor est bloqué, elle ne démarre pas.

## Chronologie

| Date | Événement |
|---|---|
| 2010-2012 | L’USAID exploite en secret ZunZuneo, « Twitter cubain » par SMS ; révélé par AP le 3 avril 2014. |
| Mai 2024 | La HRF annonce 250 000 dollars pour OpenSats au Oslo Freedom Forum (publié par OpenSats le 18 février 2025). |
| 21 juin 2024 | OpenSats accorde une bourse de long terme à Calle pour le protocole Cashu. |
| 6 juillet 2025 | Jack Dorsey annonce Bitchat et publie un livre blanc. |
| 7-18 juillet 2025 | Alex Radocea démontre une usurpation d’identité ; Dorsey reconnaît l’absence de revue externe ; analyse de Trail of Bits [S6]. |
| Septembre 2025 | Pics de téléchargements au Népal (près de 50 000 le 8 septembre) et à Madagascar (environ 70 000 en une semaine). |
| 8-10 janvier 2026 | Coupure d’internet en Iran : la copie fermée Noghteha dépasse 72 000 téléchargements ; usage signalé en Ouganda [S7]. |
| 20 janvier 2026 | Deuxième don de la HRF à OpenSats : 116 000 dollars. |
| Avril 2026 | Apple retire Bitchat de l’App Store chinois à la demande de l’administration du cyberespace. |
| 6 juillet 2026 | Livre blanc v2.0, qui écrit que les métadonnées sont « la partie la plus faible de cette conception » [S2]. |
| 23-27 juillet 2026 | Ordre indien contre les dépôts GitHub [S8] ; revue de sécurité Android et correctif de la faille critique C1 [S4]. |
| 30 juillet 2026 | Lettre d’OpenSats : Calle maintient Bitchat Android ; le code est dupliqué hors de GitHub. |
| 10 août 2026 | Le projet iOS retire la mention « identité éphémère », jugée fausse (PR n° 1595). |
| 25 septembre 2026 | La NED annonce les lauréats de l’*AI Hack for Freedom III*, organisé avec la HRF. |
| 3 octobre 2026 | Bitchat retiré des boutiques d’applications en Inde (article 69A de l’IT Act) [S8]. |
| 17-24 octobre 2026 | France : mobilisations des 17 et 24 octobre, panne Orange le 21 ; Bitchat en tête de l’App Store le 22. |
| 22-23 octobre 2026 | Bitchat Android 2.0.3 et iOS 1.8.0. |
| 25 octobre 2026 | Fil de Christophe Boutry [S1]. |

## 1. Pourquoi la rumeur circule maintenant

L’accusation prend en France parce que Bitchat y est devenu, en quelques jours, un outil de masse. Le 22 octobre 2026, l’application est **première de la catégorie réseaux sociaux de l’App Store français**, devant Signal et Telegram, après la manifestation du 17 octobre, une panne du réseau mobile d’Orange le 21 et avant la journée de mobilisation du 24 ([Presse-citron, 23 octobre](https://www.presse-citron.net/manifestations-panne-orange-voici-la-nouvelle-app-que-les-francais-installent-massivement/) ; [Renseignement économique, 25 octobre](https://renseignementeconomique.fr/bitchat-bondit-en-tete-des-telechargements-en-france-l-appli-de-messagerie-sans-internet-au-coeur-des-mobilisations)). Des responsables politiques ont évoqué des coupures ciblées des réseaux sociaux pendant les manifestations ; une messagerie qui fonctionne sans opérateur répond directement à cette crainte.

Le même schéma s’est répété ailleurs. Bitchat a servi au **Népal** et à **Madagascar** en septembre 2025, pendant des mouvements de jeunesse ([France 24](https://www.france24.com/en/live-news/20250912-from-discord-to-bitchat-tech-at-the-heart-of-nepal-protests) ; [Midi Madagasikara](https://midi-madagasikara.mg/gen-z-world-telechargement-de-bitchat-en-hausse-a-madagascar/)), en **Iran** et en **Ouganda** pendant les coupures de janvier 2026 [S7], puis en **Inde** en juillet 2026, où le pays a représenté 85 % des téléchargements mondiaux en une semaine et plus de 330 000 utilisateurs actifs le 23 juillet, pendant les manifestations étudiantes de New Delhi [S8]. Dans chaque cas, l’application devient un enjeu politique : utile aux manifestants, gênante pour les autorités, et donc cible de récits concurrents. La publication accusatrice reprend d’ailleurs cette liste de pays (« Népal en 2025, Iran et Inde en 2026 »), qui est exacte.

## 2. La chaîne de financement, maillon par maillon

La publication accusatrice cite trois sources. Toutes existent et disent ce qu’elle leur fait dire, à la lettre. Le problème est ce qu’elle en déduit.

**NED → HRF : un partenariat d’événement.** La page de la NED annonce les lauréats de l’*AI Hack for Freedom III*, compétition de deux jours tenue les 24 et 25 septembre 2026 à son siège de Washington, « en partenariat avec la Human Rights Foundation ». La page ne dit pas qui a financé les prix et ne mentionne ni Bitchat, ni OpenSats, ni Nostr, ni Calle ([NED, 25 septembre 2026](https://www.ned.org/ned-announces-the-winners-of-ai-hack-for-freedom-iii/)). Aucune subvention de la NED à la HRF n’a été trouvée. Les déclarations fiscales de la HRF montrent des **financeurs privés** : fonds de dons (Vanguard Charitable, DonorsTrust), John Templeton Foundation, Sergey Brin Family Foundation, Sarah Scaife Foundation ; la ligne « subventions publiques » est à zéro pour 2023 ([ProPublica, EIN 20-2669700](https://projects.propublica.org/nonprofits/organizations/202669700) ; [philanthropy.org, exercice 2023](https://philanthropy.org/990/report/202669700/human-rights-foundation-inc/2023)). La HRF, fondée en 2005 par le Vénézuélien Thor Halvorssen, est souvent critiquée pour son orientation libérale et anticommuniste ; elle n’est pas pour autant un relais budgétaire de l’État américain.

**HRF → OpenSats : 366 000 dollars, pour l’administration.** OpenSats a reçu 250 000 dollars de la HRF, annoncés au Oslo Freedom Forum de 2024 et publiés le 18 février 2025, puis 116 000 dollars le 20 janvier 2026, issus du *Bitcoin Development Fund* de la HRF. Les deux annonces précisent que l’argent va au **budget de fonctionnement** (instruction des demandes, vérifications techniques et de sécurité, comptabilité), séparé des fonds qui « reversent 100 % des dons » aux développeurs [S5]. Ce cloisonnement est comptable : un budget de fonctionnement mieux doté libère indirectement d’autres ressources. Mais l’ordre de grandeur règle la question. OpenSats a déclaré **37,6 millions de dollars de dons de 2022 à 2024** et 2,6 millions au premier semestre 2025 [S5] : les dons de la HRF en représentent moins de 1 %.

**Le vrai financeur d’OpenSats : Jack Dorsey.** OpenSats a annoncé le 4 mai 2023 un don de **10 millions de dollars** de #startsmall, la structure philanthropique de Jack Dorsey, dont la moitié pour l’écosystème Nostr ([OpenSats](https://opensats.org/blog/opensats-receives-additional-funding-of-dollar10m-from-startsmall)). Selon [Crypto Briefing](https://cryptobriefing.com/dorsey-start-small-bitcoin-ai-open-source/), #startsmall a ajouté 21 millions en mai 2024 ; ce second chiffre n’a pas été retrouvé sur le site d’OpenSats, mais il est cohérent avec les 24,3 millions de dons déclarés pour 2024. Autrement dit, la chaîne qui doit mener de Washington à Bitchat passe par une organisation financée d’abord par l’homme qui a lancé Bitchat.

**OpenSats → Calle → Bitchat : un lien antérieur au projet.** Calle, créateur du protocole de monnaie électronique Cashu, reçoit une bourse de long terme d’OpenSats depuis le **21 juin 2024**, pour Cashu ([OpenSats](https://opensats.org/blog/cashu-calle-receives-lts-grant)). Bitchat n’existe publiquement que depuis le 6 juillet 2025. La lettre trimestrielle d’OpenSats du 30 juillet 2026 confirme que Calle « construit et maintient Bitchat Android » ([OpenSats, 2026-Q2](https://opensats.org/newsletter/2026-Q2)) ; il en est de loin le premier contributeur (641 contributions). Le dépôt iOS, annoncé par Dorsey et d’abord hébergé sous le compte *jackjackbits*, est porté par ce même compte (688 contributions) ; les liens de financement d’OpenSats ne concernent pas cette version.

| Maillon | Ce qui est établi | Ce qui ne l’est pas |
|---|---|---|
| NED → HRF | Partenariat pour un hackathon de deux jours (septembre 2026). | Un flux financier ; un rôle de la NED dans Bitchat. |
| HRF → OpenSats | 366 000 dollars en deux dons, budget de fonctionnement. | Une affectation à Bitchat ; une origine publique de ces fonds. |
| OpenSats → Calle | Bourse depuis juin 2024 (Cashu) ; Calle maintient Bitchat Android. | Une commande de Bitchat par OpenSats ou ses donateurs. |
| Calle → Bitchat | Maintien de la version Android, code public sous licence libre. | Une fonction cachée ; une collecte de données. |
| CIA | Aucune pièce. | Tout. |

La formule de Boutry résume bien l’écart : « Un partenariat n’est pas un virement. Un virement n’est pas une commande. » [S1] On peut ajouter qu’une commande, si elle existait, laisserait des traces dans le code, qui est public.

## 3. NED, CIA et « Internet Freedom » : un contexte réel, pas une preuve

La méfiance envers la NED n’est pas une invention. La fondation a été créée en 1983 et reste financée par le Congrès : **315 millions de dollars** votés pour l’exercice 2026, malgré une proposition de l’administration Trump de supprimer ce financement et un premier gel contesté en justice par la NED en mars 2025 ([NED, 5 mars 2025](https://www.ned.org/national-endowment-for-democracy-files-lawsuit-seeking-access-to-congressionally-appropriated-funds/) ; [Legis1, 24 février 2026](https://legis1.com/news/ned-hearing-exposes-gop-rift-over-democracy-funding)). En 1991, l’un de ses fondateurs, Allen Weinstein, déclarait au *Washington Post* qu’une grande partie de ce que fait la NED était faite en secret par la CIA vingt-cinq ans plus tôt ([David Ignatius, « Innocence Abroad: The New World of Spyless Coups », 22 septembre 1991](https://www.washingtonpost.com/archive/opinions/1991/09/22/innocence-abroad-the-new-world-of-spyless-coups/92bb989a-de6e-4bb8-99b9-462c76b59a16/) ; texte intégral non accessible ici, citation abondamment reprise). La phrase dit une **continuité d’objectifs** passée du clandestin à l’assumé ; elle ne fait pas de la NED une branche de la CIA en 2026.

Le financement américain des outils de contournement est, lui, une politique publique revendiquée. [L’analyse du site sur Tor et Mullvad](../analyses/tor-project-distance-avec-mullvad-argent-de-washington-et-proces-en-double-standard.md) rappelle que le routage en oignon est né au Naval Research Laboratory, que Tor a dépendu à 85 % de fonds publics américains en 2015 et que le programme « Internet Freedom » a distribué plus de 500 millions de dollars en dix ans, notamment à Signal et Tor [A1]. Briar, messagerie pair-à-pair souvent conseillée aux militants, cite aussi l’Open Technology Fund parmi ses financeurs, à côté de fonds européens ([Briar](https://briarproject.org/about-us/)). L’analyse [A1] en tire une leçon applicable ici : le financeur paie un travail public et vérifiable sans en contrôler le code, et le vrai risque de la dépendance est la **continuité** (les coupes de 2025 l’ont montré), pas l’espionnage.

Il existe pourtant un précédent qui donne du crédit au soupçon et que les publications ne citent pas. De 2010 à 2012, l’USAID a fait fonctionner à Cuba **ZunZuneo**, un réseau de messages courts conçu pour attirer de jeunes utilisateurs avec du sport et de la musique avant de les orienter vers la contestation. Les utilisateurs ignoraient l’origine américaine du service ; ses serveurs analysaient leurs messages et des données démographiques, dont leur « réceptivité » et leurs « tendances politiques » ; et l’USAID a sollicité **Jack Dorsey** pour en reprendre le financement, sans succès connu ([AP, reprise par Inquirer, 3 avril 2014](https://technology.inquirer.net/35229/us-secretly-built-cuban-twitter-to-stir-unrest) ; [TechCrunch, 3 avril 2014](https://techcrunch.com/2014/04/03/u-s-created-cuban-twitter-to-stir-dissent-sought-funding-from-jack-dorsey-ap-reports)). La comparaison éclaire surtout ce qui manque pour Bitchat : ZunZuneo reposait sur des serveurs centraux aux mains de prestataires, une origine dissimulée et une collecte organisée. Bitchat n’a ni compte, ni serveur exploité par le projet, ni code fermé.

## 4. Ce que le protocole expose réellement

Le cœur sérieux du dossier est technique, et la source la plus sévère est la documentation de Bitchat elle-même. Le [livre blanc v2.0](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md) écrit : « les métadonnées sont la partie la plus faible de cette conception » [S2]. La [spécification de rotation des identifiants](https://github.com/permissionlesstech/bitchat/blob/main/docs/PEER-ID-ROTATION.md) détaille ce qu’un auditeur passif, muni d’un simple récepteur Bluetooth et placé dans une foule, peut faire « sans attaque cryptographique » [S3] :

- **Repérer qu’un téléphone utilise Bitchat.** L’identifiant de service Bluetooth est une constante ; au premier plan, il est émis en clair. Le document sur sa [détectabilité](https://github.com/permissionlesstech/bitchat/blob/main/docs/SERVICE-UUID-DETECTABILITY.md) conclut que masquer l’usage de l’application est impossible pour un logiciel libre qui doit permettre à des inconnus de se trouver.
- **Lui attribuer un identifiant permanent.** L’identifiant de 8 octets de chaque paquet est dérivé de la clé Noise du téléphone, créée une fois et jamais renouvelée : « même téléphone, mêmes octets, la semaine suivante, dans une autre ville ». La randomisation de l’adresse Bluetooth par le système n’y change rien.
- **Lire ses clés publiques et son pseudonyme.** Les annonces de présence les transportent en clair, toutes les 4 à 30 secondes.
- **Reconstituer qui se tenait près de qui.** Chaque annonce liste jusqu’à dix voisins directs : un seul récepteur obtient le graphe local, sans triangulation.
- **Remonter à l’auteur d’un message public.** Les paquets partent avec une durée de vie maximale, que chaque relais décrémente : la distance en sauts désigne l’émetteur.

La spécification ajoute deux points que le fil de Boutry ne relève pas. D’abord, les étiquettes des messages confiés à des « coursiers » sont calculées à partir de la clé **publique** du destinataire, diffusée en clair : n’importe quel observateur peut les recalculer, et l’affirmation du livre blanc selon laquelle ces messages ne sont pas reliables d’un jour à l’autre « ne tient pas actuellement » [S3]. Ensuite, la longueur des paquets reste visible pour la plupart des types de trafic, faute de bourrage [S2].

**Les promesses affichées ont devancé la réalité.** Jusqu’au 10 août 2026, l’écran de confidentialité de l’application iOS annonçait une « identité éphémère, nouvel identifiant généré régulièrement » ; le correctif qui l’a retiré (PR n° 1595) reconnaît que l’identifiant est stable jusqu’à l’effacement d’urgence et que la rotation n’existe que sur le papier ([GitHub](https://github.com/permissionlesstech/bitchat/pull/1595)). Côté Android, la [politique de confidentialité](https://github.com/permissionlesstech/bitchat-android/blob/main/PRIVACY_POLICY.md), datée de janvier 2025, affirme toujours que la clé publique visible des voisins « change à chaque session ». La revue de sécurité Android du 27 juillet 2026 constate l’inverse : l’identifiant stable est même placé dans la **réponse au balayage Bluetooth**, ce qui permet de suivre un utilisateur dans le temps et l’espace sans échanger avec l’application (point M3) [S4]. Pour des manifestants qui choisissent un outil sur la foi de ces textes, l’écart est plus grave que la faille elle-même.

**Le correctif est conçu, pas livré.** La spécification décrit des identifiants renouvelés toutes les heures, des clés retirées des annonces et une reconnaissance des contacts par des étiquettes calculables par eux seuls. Elle précise que les dérivations sont « implémentées et testées » mais que « rien n’est branché sur le maillage livré », et que le changement exige l’accord des équipes iOS et Android [S3]. La spécification affirme aussi que la suppression de la liste de voisins a « été intégrée séparément » ; au 25 octobre 2026, la demande correspondante (PR n° 1492, ouverte le 26 juillet) est **toujours ouverte** ([GitHub](https://github.com/permissionlesstech/bitchat/pull/1492)). Les [notes de la version iOS 1.8.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.8.0) du 23 octobre 2026 citent la spécification (« primitives fonctionnelles et spécification pour relecture ») parmi les changements, sans activation ; Boutry le relevait déjà [S1].

**Qui peut exploiter ces faiblesses ?** Toute personne à portée radio, soit quelques dizaines de mètres pour un téléphone, davantage avec une antenne. La recherche académique a montré dès 2019 que des appareils Bluetooth peuvent être suivis malgré la randomisation des adresses ([Becker, Li et Starobinski, PETS 2019](https://petsymposium.org/popets/2019/popets-2019-0036.php)) ; avec Bitchat, l’application fournit elle-même l’identifiant stable. L’exploitation demande d’être **physiquement présent**, ou d’avoir déployé des capteurs aux points de passage. Le bénéficiaire naturel est donc le service de police ou de sécurité de l’État où se tient la manifestation, ou un acteur privé équipé, bien plus qu’une agence étrangère. C’est le point qui retourne l’accusation : si Bitchat expose ses utilisateurs, c’est surtout aux autorités qu’ils contestent. Le rapport JRC-Europol sur les technologies de confidentialité rappelait déjà que le contenu chiffré n’empêche pas de voir « les relations et les déplacements », et que l’analyse des métadonnées est la voie de repli naturelle des enquêteurs [A2].

## 5. Le chemin internet : relais Nostr, géohash et Tor

Quand une connexion existe, Bitchat utilise Nostr, un protocole où des **relais** reçoivent et redistribuent des événements signés. Le code iOS fixe quatre relais par défaut, exploités par des acteurs connus de l’écosystème : `relay.damus.io`, `nos.lol`, `relay.primal.net` et `offchain.pub` (fichier `NostrRelayManager.swift`). Les salons géographiques s’appuient sur un annuaire d’environ 440 relais téléchargé depuis un fichier CSV du dépôt GitHub. La revue Android relève que cet annuaire est mis à jour quotidiennement **sans signature ni épinglage** : quiconque prendrait le contrôle de ce fichier pourrait orienter les utilisateurs vers ses relais (point M9) [S4]. C’est un risque concret, plus vérifiable que l’idée de relais « contrôlés par la CIA », dont aucune preuve n’est apportée.

Pour les messages privés, un relais voit la clé publique Nostr du **destinataire**, l’heure (rendue floue de plus ou moins 15 minutes), la taille et les informations de connexion, mais ni le contenu ni l’identité stable de l’expéditeur. Ce format est propre à Bitchat et n’offre **pas de confidentialité persistante** : la compromission ultérieure de la clé du destinataire expose les messages conservés [S2]. Les salons géohash sont publics par construction ; la revue Android signale des identités par zone qui ne changent jamais, des notes publiées avec une précision d’environ 30 mètres et conservées par les relais, et des accusés de réception automatiques qui permettent de vérifier qu’un appareil est en ligne (points H6 à H8) [S4]. La revue signalait aussi que les signatures des événements géohash entrants n’étaient jamais vérifiées, ce qui permettait à un relais de se faire passer pour n’importe quel participant (H5) ; les [notes de la version 2.0.3](https://github.com/permissionlesstech/bitchat-android/releases/tag/v2.0.3) du 22 octobre 2026 indiquent que ces signatures sont désormais vérifiées avant la détection des doublons.

Le routage **Tor** est activé par défaut sur les deux plateformes, en « échec fermé » : si Tor n’est pas prêt, les requêtes attendent au lieu de partir en clair. La [documentation Tor du projet](https://github.com/permissionlesstech/bitchat/blob/main/docs/TOR-INTEGRATION.md) reconnaît cependant que le client n’a **ni ponts ni transports enfichables** : dans un pays qui bloque Tor, la connexion ne s’établit jamais. C’était le cas de l’Iran avant la coupure de janvier 2026 [S7]. L’utilisateur qui désactive Tor pour retrouver ses messages expose alors son adresse IP à tous les relais, y compris ceux qui portent ses messages privés ; l’application l’en avertit.

## 6. Failles reconnues et réponse des développeurs

Le lancement de juillet 2025 a été mouvementé. Le 7 juillet, Alex Radocea (Supernetworks) a montré qu’un attaquant pouvait se faire passer pour un contact « favori » : la clé d’identité n’authentifiait rien ([Supernetworks](https://www.supernetworks.org/pages/blog/agentic-insecurity-vibes-on-bitchat)). Dorsey a reconnu que le logiciel n’avait fait l’objet d’**aucune revue de sécurité externe** ([TechCrunch, 9 juillet 2025](https://techcrunch.com/2025/07/09/jack-dorsey-says-his-secure-new-bitchat-app-has-not-been-tested-for-security/)). Trail of Bits a jugé ces défauts « fondamentaux », a déconseillé tout usage sensible, mais a aussi relevé la publication du code, la réaction rapide et l’adoption du cadre Noise, tout en reprochant à Dorsey d’avoir encouragé un usage dans des manifestations [S6]. Un signalement communautaire de mars 2026 fait état d’un empoisonnement de cache corrigé rapidement ; sa source n’a pas pu être consultée.

Depuis, le rythme de correction est soutenu et documenté. La version iOS 1.7.1 (31 juillet 2026) lie les sessions chiffrées à l’identité annoncée, chiffre les photos et messages vocaux privés **avant** leur passage sur le maillage (ils circulaient en clair auparavant), épingle les clés de signature et rend les clés d’identité non exportables. La revue de sécurité Android du 27 juillet 2026 recensait des failles graves, dont l’écriture des secrets de session Noise dans le journal système (C1, corrigée le jour même) et des messages privés déchiffrés journalisés (H3) [S4] ; le statut de chacun de ses trente points n’a pas été vérifié un à un. Les deux applications publient désormais des constructions reproductibles : Android affirme que ses binaires non signés ont été reconstruits deux fois à l’identique, iOS publie un manifeste de source à chaque version.

Le bilan est contrasté : une équipe réactive et une documentation d’une franchise rare, mais des propriétés promises en retard sur le code, et un public visé (militants, manifestants) pour qui ce retard compte. La politique de sécurité du projet classe d’ailleurs « hors périmètre » la visibilité des annonces et la détectabilité Bluetooth, présentées comme des propriétés de conception ([SECURITY.md](https://github.com/permissionlesstech/bitchat/blob/main/SECURITY.md)).

## 7. Les risques que la rumeur ignore

**Les copies.** En Iran, l’application la plus utilisée pendant la coupure n’était pas Bitchat mais **Noghteha**, une copie à code fermé adaptée au persan, téléchargée plus de 72 000 fois du 8 au 10 janvier 2026 [S7]. Son auteur, l’activiste Nariman Gharib, justifie la fermeture du code par le risque de copies malveillantes ; Calle a répondu publiquement de ne « jamais » utiliser une messagerie de confidentialité fermée, qui « pourrait vous espionner à votre insu » ([Bitcoin Magazine, 12 janvier 2026](https://bitcoinmagazine.com/news/iranian-protestors-turn-to-censorship-resistant-freedom-tech-during-internet-blackout)). Le chercheur Ziya Sadr y rapporte que le régime diffuse de faux liens de téléchargement. Un outil de surveillance déguisé en Bitchat est un scénario bien plus plausible qu’un Bitchat piégé : il suffit d’un APK modifié.

**Le téléphone saisi.** La [note d’évaluation de confidentialité](https://github.com/permissionlesstech/bitchat/blob/main/docs/privacy-assessment.md) écrit que la compromission réaliste n’est pas l’interception mais « un téléphone pris et, souvent, déverrouillé sous la contrainte ». Il n’existe ni code de détresse ni verrouillage propre à l’application ; l’effacement d’urgence ne couvre pas les copies déjà reçues par d’autres appareils ou conservées par des relais [S3]. Sur Android, la revue de juillet relevait des notifications affichant le texte des messages privés sur l’écran verrouillé (H4) [S4].

**Le blocage par l’État.** L’Inde a ordonné le retrait des dépôts GitHub le 23 juillet 2026, au motif que l’application permet de communiquer pendant les coupures et entrave « l’interception légale, l’attribution et la traçabilité », puis l’a fait retirer des boutiques le 3 octobre [S8]. La Chine l’avait fait retirer de l’App Store en avril 2026. En Ouganda, une cellule informatique a affirmé avoir bloqué les communications Bluetooth, sans détail technique ni validation indépendante [S7]. Le code reste dupliqué sur Codeberg, GitLab, Radicle et d’autres plateformes, et l’application Android peut désormais se transmettre d’un téléphone à l’autre sans internet ([OpenSats, 2026-Q2](https://opensats.org/newsletter/2026-Q2)).

## 8. Bitchat parmi les autres messageries : des modèles de menace différents

Boutry a raison de rappeler que toutes les messageries exposent des métadonnées, et que la question utile est « qui voit quoi, d’où et avec quels moyens » [S1]. Le tableau suivant reprend cette grille avec les sources primaires.

| Service | Qui observe | Ce qui est exposé | Source |
|---|---|---|---|
| Bitchat (Bluetooth) | Toute personne à portée radio | Usage de l’application, identifiant stable, pseudonyme, clés, voisins, taille des paquets, signal | [S2, S3] |
| Bitchat (Nostr) | Opérateurs de relais | Destinataire, heure approximative, taille ; IP si Tor est désactivé ; zone des salons géohash | [S2] |
| Signal | Signal (serveur) | Date de création du compte et dernière connexion selon ses réponses aux réquisitions ; expéditeur masqué par *Sealed Sender* | [Signal](https://signal.org/bigbrother/) |
| Telegram | Telegram (serveur) | IP, appareils, historique des noms d’utilisateur, jusqu’à 12 mois ; contenu des discussions ordinaires non chiffré de bout en bout | [Telegram](https://telegram.org/privacy) |
| WhatsApp | Meta (serveur) | Numéro, informations de connexion, appareil, carnet d’adresses selon les réglages ; contenu chiffré de bout en bout | [WhatsApp](https://www.whatsapp.com/legal/privacy-policy) |

La différence tient en une phrase : les messageries centralisées confient les métadonnées à **un opérateur** que l’on peut contraindre par la loi ; Bitchat en Bluetooth les livre à **quiconque est présent**, sans réquisition. Ni l’un ni l’autre n’est neutre ; ce ne sont pas les mêmes adversaires. Dans une manifestation, l’adversaire le plus probable est justement celui qui est présent.

## 9. Vérification des affirmations

| Affirmation | Verdict | Source |
|---|---|---|
| « La NED est partenaire de la HRF. » (publication accusatrice) | **Exact mais limité** : partenariat pour un hackathon de deux jours ; aucun flux financier NED → HRF trouvé. | [NED](https://www.ned.org/ned-announces-the-winners-of-ai-hack-for-freedom-iii/) ; [ProPublica](https://projects.propublica.org/nonprofits/organizations/202669700) |
| « La HRF a versé 116 000 $ à OpenSats. » | **Exact**, précédé de 250 000 $ ; les deux pour le budget de fonctionnement. | [S5] |
| « OpenSats finance Calle, responsable de Bitchat Android. » | **Exact**, mais la bourse date de juin 2024 et visait Cashu. | [OpenSats](https://opensats.org/blog/cashu-calle-receives-lts-grant) |
| « La CIA a financé cette appli. » | **Non étayé** : aucune pièce ; le financeur principal d’OpenSats est Dorsey. | [S5] |
| « Utilisé au Népal en 2025, en Iran et en Inde en 2026. » | **Exact** ; aussi Madagascar (2025), Ouganda (2026), France (octobre 2026). | [S7, S8] |
| Bitchat serait conçu pour surveiller les manifestants. | **Non démontré comme intention** ; exposition réelle, documentée, exploitable par tout observateur sur place. | [S2, S3] |
| Les relais Nostr seraient contrôlés par le renseignement. | **Non étayé** ; relais par défaut identifiés ; l’annuaire non signé est un vrai point faible. | [S4] |
| Les nœuds de sortie Tor seraient majoritairement contrôlés par les agences américaines. | **Non étayé** ; le record documenté (23,95 % des sorties en mai 2020) revient à un acteur criminel visant les portefeuilles bitcoin. | [Security Affairs](https://securityaffairs.com/125248/hacking/kax17-threat-actor-tor.html) |
| Si Dorsey offre l’application, c’est qu’il vend les données. | **Sans fondement** : ni compte, ni SDK publicitaire ou analytique, ni serveur du projet ; manifestes de confidentialité sans collecte. | [Politique de confidentialité](https://github.com/permissionlesstech/bitchat/blob/main/PRIVACY_POLICY.md) |
| Identifiant stable et non renouvelé, reconnu par la documentation. (Boutry) | **Exact**. | [S2, S3] |
| La nouvelle mécanique d’annonces n’est pas déployée. (Boutry) | **Exact** : « rien n’est branché sur le maillage livré ». | [S3] |
| Toutes les métadonnées ne figurent pas dans les paquets publicitaires. (Boutry) | **À nuancer** : vrai sur iOS ; sur Android l’identifiant stable est dans la réponse au balayage ; l’identifiant de service est émis en clair. | [S4] ; [S3] |
| Tor activé par défaut. (Boutry) | **Exact**, mais sans ponts : inopérant là où Tor est bloqué. | [Doc Tor](https://github.com/permissionlesstech/bitchat/blob/main/docs/TOR-INTEGRATION.md) |
| Citation d’Allen Weinstein en 1991. (Boutry) | **Authentique** selon l’article référencé du *Washington Post* ; texte intégral non consulté ici. | [Washington Post](https://www.washingtonpost.com/archive/opinions/1991/09/22/innocence-abroad-the-new-world-of-spyless-coups/92bb989a-de6e-4bb8-99b9-462c76b59a16/) |

## 10. Ce que cela change pour un utilisateur

Bitchat reste utile dans le cas pour lequel il a été conçu : échanger quand le réseau mobile est saturé, coupé ou en panne. Il ne doit pas être choisi pour **l’anonymat**. À partir de la documentation du projet, quelques règles en découlent.

- **Considérer le téléphone comme repérable.** Toute personne à portée sait que Bitchat est ouvert et peut reconnaître l’appareil d’une fois sur l’autre. Le téléphone reste par ailleurs visible du réseau mobile s’il y est connecté.
- **Changer d’identité avant et après un événement sensible.** L’identifiant ne change qu’avec l’effacement d’urgence (triple appui sur le logo), qui crée une nouvelle identité au prix des favoris [S2]. Choisir un pseudonyme qui n’est utilisé nulle part ailleurs.
- **Laisser Tor activé** et éviter les salons géohash de précision fine ; ce qui y est publié est public et durable.
- **Installer uniquement depuis les boutiques officielles ou les publications signées du dépôt**, jamais un APK transmis par un inconnu ou une copie fermée.
- **Préférer Signal pour les conversations sensibles** lorsque le réseau fonctionne, et vérifier les empreintes de ses contacts en personne, dans l’une comme dans l’autre application.

## Signaux à surveiller

- **L’activation de la rotation des identifiants** : une version qui émet les nouvelles annonces sur iOS et Android, et la fusion de la PR n° 1492 sur la liste de voisins. C’est le seul changement qui réduirait sensiblement l’exposition radio.
- **Un audit externe** : aucun audit indépendant complet n’a été publié à ce jour.
- **La politique de confidentialité Android**, qui contredit le code depuis plus d’un an.
- **Les mesures françaises** : appels à couper les réseaux sociaux pendant les manifestations, ou démarche visant Bitchat comme en Inde.
- **Des copies malveillantes** diffusées en France à la faveur de l’engouement.

## Limites et questions ouvertes

1. **Absence de preuve n’est pas preuve d’absence.** Ce dossier établit qu’aucune pièce publique ne relie la CIA à Bitchat et que la chaîne citée ne le démontre pas ; il ne peut pas exclure une opération qui n’aurait laissé aucune trace publique. Le code ouvert et les constructions reproductibles réduisent toutefois fortement la place d’une fonction cachée dans les versions officielles.
2. **Le code n’a pas été audité ici.** Les constats techniques reposent sur la documentation des développeurs, une revue interne Android et des analyses externes, recoupées par quelques lectures ciblées du code.
3. **Les comptes de la HRF sont partiels.** Les déclarations fiscales consultées couvrent 2021 à 2024 ; les dons qui transitent par des fonds de dons masquent les donateurs finaux.
4. **Le second don de #startsmall (21 millions en 2024)** n’est confirmé que par la presse spécialisée, en cohérence avec les comptes d’OpenSats.
5. **Le statut des trente points de la revue Android** n’a pas été vérifié un à un ; seuls certains correctifs sont confirmés.
6. **La faisabilité opérationnelle du pistage** (densité de capteurs nécessaire, fiabilité dans une foule de milliers de téléphones) n’est démontrée par aucune expérimentation publique propre à Bitchat.
7. **La publication accusatrice** n’a pu être identifiée qu’à travers le fil de Boutry et ses liens ; son auteur exact n’est pas établi ici.

## Conclusion

L’accusation assemble des faits exacts (un partenariat NED-HRF, des dons de la HRF à OpenSats, une bourse d’OpenSats à un développeur de Bitchat) et en tire une conclusion qu’aucun d’eux ne contient. Remonté jusqu’au bout, l’argent mène surtout à Jack Dorsey, pas à Langley. Le soupçon s’appuie sur un passé réel, de la NED « qui fait au grand jour ce que faisait la CIA » au « Twitter cubain » de l’USAID, mais ce passé décrit des opérations centralisées et dissimulées, l’inverse d’un code public sans serveur.

Le vrai problème est ailleurs, et il est sérieux. Bitchat diffuse en clair un identifiant permanent, un pseudonyme et le voisinage de chaque téléphone ; ses développeurs le reconnaissent, ont conçu la correction, mais ne l’ont pas livrée, et l’application a longtemps promis une identité éphémère qu’elle n’offrait pas. Ce défaut profite d’abord à ceux qui sont physiquement présents dans un cortège, c’est-à-dire le plus souvent aux autorités du pays. Pour les manifestants français qui l’ont installé cette semaine, la bonne question n’est pas « qui a payé ? » mais « qui, autour de moi, peut écouter ? ».

## Annexe — pièces examinées

**Les deux publications de départ.**

- **01 — [Fil de Christophe Boutry](https://x.com/Ced_haurus/status/2114336040567648471)**, 25 octobre 2026. Consulté (texte intégral). Vérification rigoureuse ; ses rares imprécisions sont traitées au § 9.
- **02 — Publication accusatrice**, en réponse au fil, auteur non identifié ici ; ses trois liens sont les pièces 03 à 05.

**Les trois liens de la publication accusatrice.**

- **03 — [NED, *AI Hack for Freedom III*](https://www.ned.org/ned-announces-the-winners-of-ai-hack-for-freedom-iii/)**, 25 septembre 2026. Consulté. Partenariat avec la HRF pour un événement ; aucune mention de Bitchat.
- **04 — [OpenSats, don de la HRF](https://opensats.org/blog/opensats-receives-funding-from-the-human-rights-foundation)**, 20 janvier 2026. Consulté. 116 000 dollars, budget de fonctionnement.
- **05 — [OpenSats, lettre 2026-Q2](https://opensats.org/newsletter/2026-Q2)**, 30 juillet 2026. Consultée. Calle maintient Bitchat Android ; demande de retrait indienne et duplication du code.

**Financements et institutions.**

- **06 — [OpenSats, don de 250 000 dollars de la HRF](https://opensats.org/blog/additional-ops-budget-from-hrf)**, 18 février 2025. Consulté.
- **07 — [OpenSats, états financiers 2022-2024](https://opensats.org/docs/financials/2022-2024.pdf) et [2025-S1](https://opensats.org/docs/financials/2025-Q1-Q2.pdf)**. Consultés ; chiffres déclarés par l’organisation, non audités ici.
- **08 — [OpenSats, 10 millions de #startsmall](https://opensats.org/blog/opensats-receives-additional-funding-of-dollar10m-from-startsmall)**, 4 mai 2023. Consulté.
- **09 — [Crypto Briefing, 21 millions de #startsmall](https://cryptobriefing.com/dorsey-start-small-bitcoin-ai-open-source/)**. Source secondaire unique pour ce montant.
- **10 — [OpenSats, bourse de Calle](https://opensats.org/blog/cashu-calle-receives-lts-grant)**, 21 juin 2024. Consulté ; montant non publié.
- **11 — [ProPublica, comptes de la HRF](https://projects.propublica.org/nonprofits/organizations/202669700)** et [philanthropy.org](https://philanthropy.org/990/report/202669700/human-rights-foundation-inc/2023). Consultés ; agrégateurs de déclarations fiscales.
- **12 — [NED, recours de mars 2025](https://www.ned.org/national-endowment-for-democracy-files-lawsuit-seeking-access-to-congressionally-appropriated-funds/)** et [Legis1, audition du 24 février 2026](https://legis1.com/news/ned-hearing-exposes-gop-rift-over-democracy-funding). Consultés.
- **13 — [*Washington Post*, 22 septembre 1991](https://www.washingtonpost.com/archive/opinions/1991/09/22/innocence-abroad-the-new-world-of-spyless-coups/92bb989a-de6e-4bb8-99b9-462c76b59a16/)**. Accès refusé ; archive référencée, citation reprise de sources concordantes.
- **14 — [AP via Inquirer](https://technology.inquirer.net/35229/us-secretly-built-cuban-twitter-to-stir-unrest) et [TechCrunch](https://techcrunch.com/2014/04/03/u-s-created-cuban-twitter-to-stir-dissent-sought-funding-from-jack-dorsey-ap-reports)**, 3 avril 2014. Consultés ; ZunZuneo.
- **15 — [Briar, financeurs](https://briarproject.org/about-us/)**. Consulté.

**Documentation et code de Bitchat.**

- **16 — [Livre blanc v2.0](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)**, 6 juillet 2026. Lu intégralement.
- **17 — [Spécification de rotation des identifiants](https://github.com/permissionlesstech/bitchat/blob/main/docs/PEER-ID-ROTATION.md)**. Lue intégralement ; document de travail.
- **18 — [Évaluation de confidentialité](https://github.com/permissionlesstech/bitchat/blob/main/docs/privacy-assessment.md)**, juillet 2026. Lue.
- **19 — [Détectabilité de l’identifiant de service](https://github.com/permissionlesstech/bitchat/blob/main/docs/SERVICE-UUID-DETECTABILITY.md)** et [intégration de Tor](https://github.com/permissionlesstech/bitchat/blob/main/docs/TOR-INTEGRATION.md). Lues.
- **20 — [Politique de confidentialité iOS](https://github.com/permissionlesstech/bitchat/blob/main/PRIVACY_POLICY.md)**, juillet 2026, et [Android](https://github.com/permissionlesstech/bitchat-android/blob/main/PRIVACY_POLICY.md), janvier 2025. Lues ; la seconde contredit le code.
- **21 — [Politique de sécurité](https://github.com/permissionlesstech/bitchat/blob/main/SECURITY.md)**. Lue.
- **22 — [Revue de sécurité Android du 27 juillet 2026](https://github.com/permissionlesstech/bitchat-android/blob/main/docs/security-review-jul-27.md)**. Lue ; revue statique non indépendante, versée au dépôt avec le correctif C1.
- **23 — [Notes de version iOS](https://github.com/permissionlesstech/bitchat/releases)** (1.7.1, 1.8.0) et [Android](https://github.com/permissionlesstech/bitchat-android/releases) (2.0.1, 2.0.3). Lues.
- **24 — [PR n° 1595](https://github.com/permissionlesstech/bitchat/pull/1595)** (mentions de confidentialité inexactes, fusionnée le 10 août 2026) et **[PR n° 1492](https://github.com/permissionlesstech/bitchat/pull/1492)** (liste de voisins, ouverte). Consultées.
- **25 — Code iOS, `NostrRelayManager.swift` et `GeoRelayDirectory.swift`.** Lecture ciblée : relais par défaut et annuaire.

**Analyses de sécurité et recherche.**

- **26 — [Alex Radocea, Supernetworks](https://www.supernetworks.org/pages/blog/agentic-insecurity-vibes-on-bitchat)**, 7 juillet 2025. Consulté.
- **27 — [TechCrunch, absence de revue](https://techcrunch.com/2025/07/09/jack-dorsey-says-his-secure-new-bitchat-app-has-not-been-tested-for-security/)**, 9 juillet 2025. Référencé, non relu intégralement.
- **28 — [Trail of Bits](https://blog.trailofbits.com/2025/07/18/building-secure-messaging-is-hard-a-nuanced-take-on-the-bitchat-security-debate/)**, 18 juillet 2025. Consulté.
- **29 — [Aceto, Persico et Pescapè, arXiv](https://arxiv.org/abs/2603.28753)**, 30 mars 2026. PDF consulté ; prépublication.
- **30 — [Becker, Li et Starobinski, PETS 2019](https://petsymposium.org/popets/2019/popets-2019-0036.php)**. Résumé consulté.
- **31 — [Security Affairs, KAX17 et relais Tor malveillants](https://securityaffairs.com/125248/hacking/kax17-threat-actor-tor.html)**, décembre 2021. Référencé.

**Contexte d’usage et réactions des États.**

- **32 — [TechCrunch, Inde, 24 juillet](https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/) et [3 octobre 2026](https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/)**. Consultés.
- **33 — [Bitcoin Magazine, Iran et Noghteha](https://bitcoinmagazine.com/news/iranian-protestors-turn-to-censorship-resistant-freedom-tech-during-internet-blackout)**, 12 janvier 2026. Consulté ; média spécialisé bitcoin.
- **34 — [France 24, Népal](https://www.france24.com/en/live-news/20250912-from-discord-to-bitchat-tech-at-the-heart-of-nepal-protests)** et [Midi Madagasikara](https://midi-madagasikara.mg/gen-z-world-telechargement-de-bitchat-en-hausse-a-madagascar/). Référencés via l’article Wikipédia, non relus intégralement.
- **35 — [Presse-citron](https://www.presse-citron.net/manifestations-panne-orange-voici-la-nouvelle-app-que-les-francais-installent-massivement/)** et [Renseignement économique](https://renseignementeconomique.fr/bitchat-bondit-en-tete-des-telechargements-en-france-l-appli-de-messagerie-sans-internet-au-coeur-des-mobilisations), 23 et 25 octobre 2026. Consultés ; classements, pas de chiffres de téléchargement.
- **36 — Pages de confidentialité de [Signal](https://signal.org/bigbrother/), [Telegram](https://telegram.org/privacy) et [WhatsApp](https://www.whatsapp.com/legal/privacy-policy).** Les deux premières consultées ; la troisième référencée.

## Analyses internes utilisées et provenance

- **[A1] [Tor Project : distance avec Mullvad, argent de Washington et procès en double standard](../analyses/tor-project-distance-avec-mullvad-argent-de-washington-et-proces-en-double-standard.md)** — analyse du 18 octobre 2026 d’une publication sur X ; mobilisée pour l’histoire du financement public américain de Tor, l’ordre de grandeur du programme « Internet Freedom » (chiffre du *Guardian*, 19 février 2026) et la distinction entre financer un travail public et contrôler un code. Ses sources externes sont reprises de l’analyse, non revérifiées ici.
- **[A2] [Commission européenne (JRC) et Europol : prospective des technologies de confidentialité](../analyses/commission-europeenne-jrc-et-europol-prospective-des-technologies-de-confidentialite.md)** — analyse du 8 octobre 2026 d’un rapport de prospective ; mobilisée pour le constat que le chiffrement du contenu laisse visibles relations et déplacements, et que l’analyse des métadonnées est la voie de repli des enquêteurs.
