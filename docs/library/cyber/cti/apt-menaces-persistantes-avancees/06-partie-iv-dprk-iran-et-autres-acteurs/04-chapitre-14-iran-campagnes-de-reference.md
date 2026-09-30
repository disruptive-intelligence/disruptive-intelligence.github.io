---
title: 'Chapitre 14 — Iran : campagnes de référence'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie IV — DPRK, iran ET autres acteurs
  - index.md
---

Ce chapitre présente les campagnes iraniennes emblématiques, organisées chronologiquement et thématiquement.

## 14.1 Stuxnet (2010) — le catalyseur

**Acteurs** : co-attribution **États-Unis et Israël** (publiquement documentée par plusieurs sources journalistiques dont le livre *Confront and Conceal* de David Sanger, 2012). **Paradigme** : première arme cyber OT, catalyseur des capacités cyber iraniennes.

**Cible** : le **programme d’enrichissement d’uranium iranien**, spécifiquement les centrifugeuses IR-1 à Natanz.

**Mécanisme** : Stuxnet est un malware d’une complexité sans précédent à son époque. Il combinait :

- **Quatre vulnérabilités 0-day Windows** (usage exceptionnel — un seul 0-day suffit généralement à compromettre une cible).
- **Ciblage extrêmement précis** : Stuxnet ne s’activait que sur des systèmes très spécifiques — machines Windows configurées avec WinCC/STEP7 de Siemens, contrôlant des automates S7-315 spécifiques, eux-mêmes contrôlant des centrifugeuses tournant à certaines vitesses.
- **Manipulation physique** : une fois sur le système de contrôle, Stuxnet modifiait les commandes envoyées aux centrifugeuses pour provoquer leur destruction (variations de vitesse anormales causant des contraintes mécaniques), **tout en affichant des valeurs normales aux opérateurs**. Cette double manipulation (destruction réelle + masquage) est la signature du malware.

**Impact** : environ **1 000 centrifugeuses détruites**, programme iranien retardé de 2-3 ans selon les estimations. Stuxnet a démontré que le cyber pouvait causer des dommages physiques significatifs à un programme militaro-industriel majeur.

**Propagation non intentionnelle** : Stuxnet s’est propagé au-delà des systèmes ciblés (machines Windows génériques, réseaux industriels non ciblés) via USB, ce qui a conduit à sa découverte en 2010 par des chercheurs en sécurité biélorusses puis internationaux.

**Catalyseur iranien** : Stuxnet a eu un **effet boomerang** majeur. L’Iran, conscient de la capacité cyber offensive déployée contre lui, a investi massivement dans son propre programme cyber offensif. Shamoon, développé environ 2 ans après Stuxnet, est la réponse iranienne — un wiper déployé contre Saudi Aramco (allié américain régional) en 2012. L’Iran est depuis devenu un acteur cyber significatif, étape structurée par Stuxnet.

**Autres traitements** : Stuxnet est abordé au Ch.18 (Israël), au Ch.21 (OT/ICS), et au Ch.25 (prolifération cyber — le code Stuxnet a fuité et a été étudié par tous les acteurs étatiques).

## 14.2 Shamoon v1/v2/v3 (2012-2018)

**Acteur** : attribué à l’Iran, avec liens APT33 pour certaines itérations. **Paradigme** : wiper destructif à grande échelle comme représailles stratégiques.

**Shamoon v1 (août 2012)** : déployé contre **Saudi Aramco**, compagnie pétrolière nationale saoudienne. Le wiper a effacé les disques durs de **30 000 postes de travail** (soit environ 75% du parc de la compagnie). Les systèmes de production pétrolière n’ont pas été touchés, mais les opérations administratives ont été paralysées pendant des semaines. Parallèlement, un wiper similaire a frappé RasGas (Qatar) avec un impact plus limité.

**Message politique** : Shamoon v1 a été interprété comme une **représailles iranienne** pour Stuxnet, dirigée contre un allié majeur des États-Unis dans la région. Le message : « si vous nous attaquez, nous pouvons frapper votre industrie pétrolière ».

**Shamoon v2 (novembre 2016 - janvier 2017)** : réapparition du wiper contre des cibles saoudiennes, dans un contexte de tensions régionales renouvelées.

**Shamoon v3 (décembre 2018)** : nouvelle version, ciblage Saipem (entreprise pétrolière italienne) et autres.

**Analyse** : Shamoon est devenu un outil récurrent iranien signalant les moments de tensions régionales. Son déploiement est souvent associé à des événements politiques (sommet de l’OPEP, sanctions, incidents régionaux).

## 14.3 Campagne contre l’Albanie (juillet 2022)

**Acteur** : Iran (MOIS, attribution publique par les États-Unis en septembre 2022 via sanctions OFAC et par l’Albanie). **Paradigme** : wiper + ransomware déployés pour représailles politiques.

**Contexte** : l’Albanie hébergeait un important camp de l’organisation d’opposition iranienne **MEK** (Mujahideen-e-Khalq — Organisation des Moudjahidin du peuple), à la suite d’un accord avec les États-Unis dans les années 2010 pour leur accueil depuis l’Irak. L’Iran considère le MEK comme un groupe terroriste et a exigé son expulsion.

**Attaque (juillet 2022)** : wipers et ransomware déployés contre les **systèmes gouvernementaux albanais** — services de police, administration, parlement. Disruption significative des services publics. L’attaque a coïncidé avec un congrès prévu du MEK.

**Réponse albanaise (septembre 2022)** : l’Albanie a **rompu les relations diplomatiques** avec l’Iran et expulsé le personnel diplomatique iranien. **Premier cas d’une rupture diplomatique pour cause de cyberattaque** dans l’histoire.

**Attribution et sanctions** : les États-Unis ont attribué publiquement à l’Iran, imposé des sanctions OFAC contre le MOIS et des opérateurs, et soutenu l’Albanie techniquement (FBI a envoyé des équipes).

**Signification** : l’attaque albanaise illustre la volonté iranienne de conduire des opérations destructives à l’étranger pour des motifs politiques, et la capacité occidentale à y répondre par l’attribution et le soutien diplomatique. C’est aussi un précédent juridique intéressant (rupture diplomatique = signal que le cyber peut déclencher des réponses diplomatiques majeures).

## 14.4 Cyberattaques contre Israël 2023-2025

Le conflit Israël-Hamas déclenché en octobre 2023 a amplifié les cyberopérations iraniennes contre Israël et ses intérêts.

**Campagnes documentées** :

- **Opérations Agrius** : wipers continus contre cibles israéliennes, sous fausses bannières hacktivistes (« Cyber Av3ngers » notamment).
- **Ciblage d’infrastructures civiles** : systèmes de santé israéliens, systèmes municipaux, parfois systèmes d’alerte publique.
- **Opérations contre les sous-traitants de défense israéliens et américains** : espionnage classique.
- **Opérations d’influence** : amplification de narratifs pro-palestiniens sur les réseaux sociaux, deepfakes ponctuels, manipulation de contenus.

**Ciblage US post-octobre 2023** : les opérations iraniennes contre des cibles américaines ont également augmenté, notamment contre des infrastructures eau (« Cyber Av3ngers » a revendiqué plusieurs attaques contre des systèmes d’eau municipaux US via exploitation de PLC Unitronics exposés — démonstration plus symbolique qu’impactante mais message clair).

## 14.5 Surveillance des dissidents et diaspora

Les cyberopérations iraniennes contre les dissidents et la diaspora sont un volet continu et sous-documenté publiquement. Quelques éléments publics :

- **Campagnes APT35/APT42** continues contre les dissidents iraniens à l’étranger.
- Post-Mahsa Amini (septembre 2022, mort en détention de la « police des mœurs » iranienne, déclenchement des protestations « Femme Vie Liberté ») : intensification massive du ciblage des militants féministes iraniens à l’étranger, des journalistes couvrant les protestations, des relais de la diaspora.
- **Harcèlement** : au-delà de la surveillance, certaines cibles reçoivent des harcèlements directs (deepfakes humiliants, campagnes de dénigrement, pressions via les familles en Iran).
- **Opérations physiques** : le cyber est parfois coordonné avec des tentatives d’enlèvement ou d’intimidation physique (plusieurs cas documentés aux US et en Europe).

## 14.6 Analyse : la spécificité iranienne

La synthèse des campagnes iraniennes révèle un profil distinct dans l’écosystème APT.

**Le destructif ponctuel comme substitut/complément conventionnel** : l’Iran est l’un des rares États à utiliser régulièrement le cyber destructif ouvertement. Shamoon et Agrius sont des wipers déployés à des moments de tensions régionales — le cyber remplit un rôle que l’action conventionnelle (frappes militaires) remplirait dans d’autres configurations. Cette caractéristique distingue l’Iran des autres acteurs (la Russie fait du destructif aussi mais majoritairement en contexte de guerre déclarée avec l’Ukraine ; la Chine presque pas ; les US/Israël très rarement et ciblé).

**Social engineering extrêmement sophistiqué** : APT35 représente probablement l’état de l’art mondial en social engineering ciblé. Cette compétence compense une sophistication technique de malware moindre que celle des APT russes ou chinoises.

**Utilisation de fausses bannières hacktivistes** : pratique récurrente (Cyber Av3ngers, Moses Staff, autres). Permet à l’Iran de signaler des capacités à son audience domestique et régionale tout en maintenant un déni plausible.

**Montée en sophistication** : Scarred Manticore (2023) suggère que le MOIS investit dans des capacités plus sophistiquées. La trajectoire est à la hausse, même si l’Iran reste un cran en-dessous des acteurs de pointe.

**Pour l’analyste** : face à une intrusion attribuée à l’Iran, les questions discriminantes sont : MOIS ou IRGC ? Opération de renseignement classique ou opération destructive/représailles ? Lien avec un événement politique/régional récent ? Utilisation d’une fausse bannière hacktiviste ?

-----
