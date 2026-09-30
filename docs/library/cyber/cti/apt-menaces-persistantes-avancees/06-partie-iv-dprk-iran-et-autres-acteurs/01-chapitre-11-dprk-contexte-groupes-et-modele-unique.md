---
title: 'Chapitre 11 — DPRK : contexte, groupes et modèle unique'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie IV — DPRK, iran ET autres acteurs
  - index.md
---

## 11.1 Le cyber comme instrument économique du régime

La République Populaire Démocratique de Corée (DPRK) présente un cas **unique au monde** : c’est le seul État qui utilise le cyber **principalement comme source de revenus** pour contourner les sanctions internationales et financer le régime et son programme d’armement nucléaire et balistique.

Cette particularité découle de la configuration stratégique nord-coréenne. Sous sanctions internationales sévères depuis les années 2000 (renforcées par les résolutions ONU 2006, 2009, 2013, 2016, 2017), coupée des circuits financiers légaux, la DPRK doit financer son régime et surtout son programme nucléaire/balistique par des canaux alternatifs : commerce illégal (charbon, pêche), trafic d’êtres humains, contrefaçon de devises, et depuis les années 2010, **cybervol**.

Les estimations de revenus générés par le cyber nord-coréen varient selon les sources mais s’accordent sur des ordres de grandeur massifs :

- **Rapport ONU** (Panel of Experts) : plusieurs milliards de dollars cumulés depuis 2017.
- **Chainalysis** (rapport annuel) : en 2022, la DPRK a volé environ 1,7 milliard de dollars en crypto-actifs. En 2023, ~1 milliard. En 2024, les volumes sont repartis à la hausse. Le vol Bybit de février 2025 (~1,5 milliard de dollars) est à lui seul le plus gros vol crypto de l’histoire.
- **US Treasury / UN** : cumulé entre 3 et 6+ milliards de dollars sur la décennie 2014-2024.

Pour contextualiser : le PIB total de la DPRK est estimé à environ 30 milliards de dollars par an (difficile à mesurer précisément). Le cybervol annuel représente donc plusieurs pourcents du PIB — équivalent, en proportion, à ce qu’un État comme la France générerait s’il dégageait 80-100 milliards d’euros par an de cybervol. L’ordre de grandeur est macroéconomique.

## 11.2 Le RGB : Reconnaissance General Bureau

Le **RGB** (정찰총국 — Reconnaissance General Bureau) est le service de renseignement militaire nord-coréen. Il supervise l’ensemble des opérations cyber offensives de la DPRK. Les opérateurs cyber sont formés dans des programmes militaires dédiés (Kim Il-sung Military University, autres institutions spécialisées) et intègrent ensuite les bureaux opérationnels du RGB.

Le RGB est structuré en plusieurs bureaux, dont les principaux pour le cyber sont :

- **Bureau 121** : cyberopérations.
- **Lab 110** : développement de malware (certaines sources indiquent une structure fluctuante).

Une caractéristique opérationnelle unique : les **opérateurs cyber nord-coréens sont souvent stationnés à l’étranger**. Principalement en Chine (Shenyang, Dandong — proches de la frontière DPRK), mais aussi en Russie, Malaisie, Singapour, et dans plusieurs pays d’Asie du Sud-Est. Raisons : meilleure connectivité Internet (la Corée du Nord a une bande passante limitée et surveillée), OPSEC (rendre le ciblage plus difficile), et évite la détection automatique par origine IP coréenne du Nord.

Cette configuration produit des artefacts d’attribution parfois trompeurs : certaines opérations Lazarus apparaissent initialement comme provenant de Chine ou de Russie, avant que l’analyse approfondie (comportement, TTP, liens avec d’autres opérations DPRK) ne confirme l’origine nord-coréenne.

## 11.3 Lazarus Group / Diamond Sleet — vue d’ensemble

**Lazarus Group** est le nom générique sous lequel l’écosystème cyber nord-coréen est souvent regroupé. En réalité, **Lazarus est un ensemble de sous-groupes** avec des missions distinctes, tous rattachés au RGB mais avec des spécialisations fonctionnelles.

**Mission globale** : espionnage, cybervol (crypto et traditionnel), opérations ciblées politiques, et depuis 2017 opérations de dégâts collatéraux massifs (WannaCry).

**Particularités opérationnelles** :

- **Multi-plateforme** : Lazarus développe des implants Windows, macOS, Linux — l’un des rares écosystèmes APT à couvrir les trois systèmes avec la même profondeur.
- **Sophistication variable selon les opérations** : des opérations ultra-sophistiquées (3CX supply chain) côtoient des opérations plus standards.
- **Réutilisation d’infrastructure et de code** : les liens entre opérations Lazarus sont souvent détectables par des réutilisations d’outils, ce qui a facilité la consolidation du cluster.

Les principales sous-structures dans l’écosystème Lazarus :

## 11.4 APT38 / BlueNoroff / Sapphire Sleet

**Spécialisation** : cyber-braquages financiers. Ciblage : banques, institutions financières, exchanges de crypto, plateformes DeFi.

**Campagnes historiques** :

- **Bangladesh Bank (février 2016)** : compromission du terminal SWIFT de la banque centrale du Bangladesh, transfert de 81 millions de dollars vers des comptes aux Philippines. Un 951 millions de dollars supplémentaires ont été bloqués grâce à une faute de frappe dans un ordre de virement (« fandation » au lieu de « foundation » ayant déclenché un examen manuel). **Premier cyber-braquage bancaire majeur par un acteur étatique**.
- **Ciblage continu SWIFT** : tentatives multiples contre d’autres banques (Vietnam TPBank, Équateur, plusieurs en Asie) avec des succès variables.

**Pivot crypto (2018+)** : BlueNoroff/APT38 a ensuite tourné massivement son attention vers les crypto-actifs, plus faciles à monétiser que les virements bancaires traditionnels. Ciblage d’exchanges, de services DeFi, de bridges cross-chain. Les campagnes emblématiques sont détaillées au Ch.12.

**TTP signature** :

- **Social engineering ciblé** sur employés d’institutions financières et d’exchanges crypto.
- **Malware custom multi-plateforme** : FALLCHILL, BADCALL, HOPLIGHT, DTrack, AppleJeus (macOS, ciblage spécifique crypto).
- **Supply chain** pour atteindre les clients finaux (3CX 2023 notamment, géré en cas au Ch.30).

## 11.5 Kimsuky / Emerald Sleet

**Spécialisation** : espionnage diplomatique et nucléaire. Ciblage : chercheurs spécialisés sur la péninsule coréenne, diplomates, ministères des affaires étrangères, think tanks d’études coréennes, universités, décideurs impliqués dans les négociations sur le programme nucléaire nord-coréen.

**TTP signature** :

- **Spear-phishing extrêmement ciblé** : emails personnalisés adressés à des chercheurs et fonctionnaires nommés, avec contexte précis (invitations à des conférences, demandes d’entretien, thèmes de recherche).
- **Credential harvesting** : fausses pages de login (Gmail, ProtonMail, services académiques coréens, services gouvernementaux sud-coréens).
- **Malware** : **BabyShark** (backdoor légère), **AppleSeed**, **FlowerPower**, plusieurs RAT custom.
- **Ciblage géographique** : Corée du Sud massivement, US (think tanks et universités travaillant sur la DPRK), Europe (centres de recherche sur la non-prolifération), Japon.

**Activité continue** : Kimsuky est l’un des groupes les plus actifs en volume dans l’écosystème DPRK. Volumes élevés de phishing, campagnes quasi permanentes. Sophistication modérée mais efficacité par persistance.

## 11.6 APT43 / Velvet Chollima / Kimsuky-adjacent

**Distinction avec Kimsuky** : les profils se recoupent et certains analystes les considèrent comme très proches ou partiellement fusionnés. Mandiant promeut APT43 comme cluster distinct depuis 2023.

**Spécialisation** : ciblage **académique, think tanks, médias, ONG** travaillant sur la DPRK. Collecte de renseignement sur les positions externes et les narratifs médiatiques.

**TTP signature** : similaire à Kimsuky (spear-phishing, credential harvesting, RAT légers). APT43 est également documenté pour utiliser des **crypto-vols ponctuels** comme source de financement opérationnel — ce qui en fait un croisement entre les missions d’espionnage (Kimsuky) et financières (APT38).

## 11.7 Andariel / Onyx Sleet

**Spécialisation** : mix ransomware / cyber-espionnage. Moins connu que Lazarus ou APT38, mais significatif.

**Particularité** : Andariel a déployé des opérations de **ransomware ciblé** dans le passé (notamment contre des institutions de santé américaines), en plus de ses missions d’espionnage. Cette mixité rend son classement difficile.

**Cibles** : secteur de la santé (ciblage ransomware Maui), défense sud-coréenne, ATM et banques (braquages divers).

## 11.8 Les opérateurs IT DPRK : phénomène unique

Un phénomène entièrement distinct des APT traditionnelles mérite une section dédiée : les **opérateurs IT DPRK**.

**Modus operandi** : des **milliers de ressortissants nord-coréens**, envoyés à l’étranger par le régime, travaillent sous **de fausses identités** comme développeurs freelance ou salariés à distance dans des entreprises occidentales. Ils génèrent un revenu en dollars qui est en grande partie reversé au régime.

**Revenu estimé** : le gouvernement américain estime à **300 millions de dollars par an et plus** les revenus générés par ce programme. L’ordre de grandeur, tout comme les vols crypto, est macroéconomique pour la DPRK.

**Techniques d’infiltration** :

- **Fausses identités** : achat de documents d’identité volés (américains, sud-coréens, autres), construction de profils LinkedIn complets avec CV, recommandations, photos (parfois générées par IA ou volées).
- **VPN et proxies** : connexions via IP occidentales (US, Europe) pour masquer l’origine coréenne.
- **Intermédiaires (facilitators)** : complices locaux qui prêtent leur identité, leur adresse, leurs comptes bancaires. Plusieurs facilitators ont été arrêtés aux US (notamment « l’opération laptop farm » — l’affaire Christina Chapman en 2024 qui hébergeait 90 ordinateurs connectés via VPN pour permettre à des travailleurs DPRK d’apparaître comme basés aux US).
- **Entretiens via vidéoconférence** : les opérateurs DPRK passent les entretiens en se faisant passer pour des asiatiques basés aux US, parfois avec modifications vidéo ou voice transformation.

**Détection** : indices comportementaux (réticence à allumer la caméra, horaires décalés, anomalies linguistiques, accès depuis IP incompatibles avec la localisation déclarée), vérification approfondie d’identité, background checks renforcés. Le FBI a émis des advisories détaillés en 2023-2024 pour aider les employeurs à détecter ces infiltrations.

**Risques au-delà du financement** : une fois à l’intérieur d’une entreprise, un opérateur IT DPRK peut potentiellement introduire du code malveillant, exfiltrer de la propriété intellectuelle, ou préparer des accès pour d’autres opérations APT nord-coréennes. Plusieurs cas documentés de tentatives d’exfiltration.

## 11.9 Formation, stationnement à l’étranger, OPSEC

La formation des opérateurs cyber DPRK combine formation militaire (discipline, hiérarchie, sécurité opérationnelle) et formation technique (informatique, langues étrangères, compréhension des plateformes occidentales). Les opérateurs les plus doués sont identifiés très tôt et formés dans des programmes d’élite.

**Stationnement à l’étranger** : comme mentionné (11.2), une grande partie des opérations cyber DPRK est conduite depuis l’étranger — Chine principalement, mais aussi Russie, Asie du Sud-Est. Les opérateurs vivent dans des communautés fermées sous surveillance, avec des contrôles stricts (familles restées en DPRK comme « assurance » contre la défection, rotation régulière des postes).

**OPSEC** : globalement moyenne. Les opérateurs DPRK sont formés à l’OPSEC mais l’ampleur du volume d’opérations et les pressions de résultats (le régime attend des revenus) produisent des erreurs régulières qui ont facilité plusieurs attributions. Parmi les artefacts récurrents : réutilisation d’infrastructure, overlaps de TTP entre opérations différentes, quelques cas d’opérateurs identifiés nominativement par les indictments DOJ.

-----
