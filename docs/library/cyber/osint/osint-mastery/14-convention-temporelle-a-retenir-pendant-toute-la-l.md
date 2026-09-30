---
title: Convention temporelle (à retenir pendant toute la lecture)
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - index.md
---

> **État des connaissances : mai 2026.**
>
> Ce cours décrit l'état de l'écosystème OSINT à mai 2026. Les éléments suivants évoluent rapidement et doivent être **revérifiés contre la documentation officielle** avant tout usage opérationnel :
>
> - **Outils** : disponibilité, accès gratuit / payant, fonctionnalités, intégrations.
> - **APIs plateformes** : conditions d'accès (X, Reddit, Telegram, Meta, TikTok, etc.), tarifs, limitations, suppressions.
> - **Politiques de plateformes** : CGU, modération, fermetures, restrictions de scraping.
> - **Politiques de conservation** : Wayback Machine, archive.today, services tiers.
> - **Modèles IA** : capacités, performances, tarifs, modèles locaux disponibles, modèles déployés en cloud.
> - **Outils de détection** : deepfake, IA-generated content, watermarks (les détecteurs perdent en efficacité face aux nouveaux modèles).
> - **Doctrine et cadres légaux** : AI Act, DSA, CSDDD, AMLD, MiCA, jurisprudence.
> - **Acteurs documentés** : groupes APT, opérations d'influence (Doppelgänger, Spamouflage, Storm-1516, etc.).
> - **Coopération institutionnelle** : Telegram post-Durov, accords inter-services.
> - **Outils dédiés** : Bellingcat tools, plateformes commerciales (Maltego, Sayari, etc.).
>
> **Règle d'or.** Toute mention d'outil ou de politique dans ce cours doit être considérée comme **datée**. Vérifier la documentation officielle au moment de l'usage. Les principes méthodologiques (cycle, cotation, ACH, déontologie) restent valides ; les détails techniques doivent être actualisés.
>
> **Risques typiques d'obsolescence** :
> - **Très élevé** (< 6 mois) : APIs payantes, restrictions plateformes, IOCs CTI.
> - **Élevé** (< 1 an) : outils tiers gratuits, scrapers, agrégateurs.
> - **Modéré** (1-2 ans) : registres officiels, leaks ICIJ, frameworks.
> - **Faible** (long terme) : principes méthodologiques, cadres légaux fondamentaux.
>
> L'analyste mature **assume** ce caractère vivant de la discipline et le **documente** dans ses livrables (« outils utilisés à date X, vérifiés Y »).

-----


## Parcours express — Mener une enquête OSINT en 60 minutes

> **Ce parcours est un compagnon opérationnel.** Il ne se substitue pas au cours, mais il permet à un analyste pressé de structurer une investigation simple en une heure. Imprimez-le, gardez-le à côté de votre clavier.

L'enquête OSINT n'est jamais improvisée. Même quand vous disposez d'une heure, suivez la séquence ci-dessous. Sauter une étape, c'est s'exposer à produire du bruit, à violer un cadre légal, ou à griller une cible.


### Étape 1 — Comprendre la demande (5 minutes)

Qui demande ? Pourquoi ? Quel est l'événement déclencheur ? Quelle est la décision attendue à partir de votre livrable ? Quel est le délai ? Quelles sont les contraintes (budget, OPSEC, légalité, juridiction) ? Si la demande est vague, posez la question : « Que ferez-vous si je vous donne A ? Que ferez-vous si je vous donne B ? » — la réponse révèle le besoin réel.


### Étape 2 — Vérifier le mandat et le périmètre (3 minutes)

Êtes-vous légitime pour conduire cette enquête ? Avez-vous un mandat écrit ou implicite ? Le périmètre est-il clairement défini ? S'agit-il d'une personne physique, d'une société, d'un événement, d'un contenu ? Si vous êtes en cabinet, ce n'est pas optionnel : sans mandat clair, vous ne lancez pas.


### Étape 3 — Formuler les questions de renseignement (5 minutes)

Une question OSINT est **fermée, vérifiable, et reformulable en hypothèse**. « Que sais-tu sur Delaunay ? » n'est pas une question OSINT. « Delaunay contrôle-t-il une société à Malte ? » en est une. « Quelle est l'adresse personnelle de Delaunay ? » en est une autre. Listez 3 à 5 questions principales et 5 à 10 questions secondaires.


### Étape 4 — Identifier les sélecteurs initiaux (2 minutes)

Quels sont les **points d'entrée** dans l'enquête ? Nom complet, date de naissance, email, téléphone, photo, adresse, username, domaine, IP, wallet ? Listez ce que vous avez. C'est sur ces sélecteurs que vous allez pivoter.


### Étape 5 — Évaluer les risques juridiques et éthiques (3 minutes)

L'enquête touche-t-elle à des données personnelles sensibles (santé, opinions politiques, religion, orientation sexuelle) ? À des mineurs ? À une juridiction restrictive (UE et RGPD, USA et CCPA, Allemagne) ? Y a-t-il un risque de doxxing involontaire ? Y a-t-il un risque de violation du secret professionnel ? Si oui, formalisez et tracez votre décision avant de lancer.


### Étape 6 — Préparer l'OPSEC minimale (5 minutes)

Pour une enquête simple, vous avez besoin a minima de : un navigateur en profil dédié (ou navigation privée), un VPN si la cible est susceptible de consulter ses logs, un compte d'investigation (pas votre compte personnel) pour toute interaction avec une plateforme. Pour des enquêtes plus sensibles, voir Ch.9-11.


### Étape 7 — Lancer les recherches prioritaires (15 minutes)

Commencez par les sources gratuites, rapides, et indexées : Google, Yandex (irremplaçable pour reverse image et contenus russophones), Bing, registres officiels, archive.org. Posez les bonnes requêtes (dorks ciblés, pas de fouille au hasard). Documentez chaque action dans votre journal.


### Étape 8 — Pivoter sans se disperser (10 minutes)

À chaque résultat, demandez-vous : **ceci m'apporte-t-il un nouveau sélecteur exploitable ?** Si oui, ajoutez-le à votre liste et continuez. Si non, ne vous laissez pas distraire. La discipline du pivot est ce qui distingue un investigateur expérimenté d'un curieux qui surfe.


### Étape 9 — Capturer, horodater, hasher (en continu)

Chaque page visitée d'intérêt est capturée (Hunchly idéalement, SingleFile sinon), horodatée, et hashée si elle est destinée à un usage judiciaire. Une URL est un mauvais témoin : elle peut changer ou disparaître. Une capture horodatée et hashée est une preuve.


### Étape 10 — Vérifier et corroborer (5 minutes)

Pour chaque fait majeur : **deux sources indépendantes minimum**. Une source unique = une piste à confirmer, pas un fait établi. Une rumeur reprise par 50 sites n'est pas 50 sources : c'est une seule source mal recyclée.


### Étape 11 — Construire une mini-timeline (3 minutes)

Reportez les événements datés sur une ligne temporelle. Les incohérences chronologiques sont l'un des révélateurs les plus puissants : une déclaration impossible à la date alléguée, un poste occupé avant la fondation de l'entreprise, une photo prise après l'événement supposé.


### Étape 12 — Distinguer piste, indice, fait, hypothèse et preuve (en continu)

C'est la discipline du chapitre 4. Une **piste** est une direction à explorer. Un **indice** est un élément factuel qui oriente une hypothèse. Un **fait** est un indice établi par au moins deux sources indépendantes et cotées. Une **hypothèse** est une explication candidate des faits. Une **preuve** est un fait qui établit la véracité d'une hypothèse au-delà du raisonnable. Confondre ces niveaux est l'erreur la plus fréquente de l'analyste débutant.


### Étape 13 — Utiliser l'IA uniquement comme assistant vérifiable (en continu)

Un LLM peut traduire, résumer, extraire des entités, générer des dorks. Il ne peut **pas** être cité comme source. Tout ce qui sort d'un LLM est à vérifier. Protocole **Retrieve-Store-Cite** : si vous citez un fait, vous citez sa source primaire, pas le LLM qui l'a produit.


### Étape 14 — Produire une mini-note (3 minutes)

Une mini-note OSINT tient en une page. **BLUF** (Bottom Line Up Front) : la conclusion en deux phrases, avec son niveau de confiance. Puis : trois à cinq faits clés cotés, une timeline, les sources, les limites. Pas de verdict, vocabulaire calibré.


### Étape 15 — Identifier les limites et les suites possibles (1 minute)

Quelles questions restent ouvertes ? Quelles sources n'avez-vous pas pu consulter ? Quelles vérifications complémentaires seraient utiles ? Quelles spécialisations devraient prendre le relais (crypto, FININT, dark web) ? Ces limites font partie du livrable, pas en marge de lui.

-----


## Fil rouge — Opération MIRAGE 2026

> **Le fil rouge MIRAGE traverse l'ensemble du cours.** Il sert deux fonctions : illustrer concrètement les concepts au fil des chapitres, et fournir un cas de synthèse complet (Ch.93). Vous le retrouverez sous forme d'encadrés *« MIRAGE — Épisode N »* tout au long du cours.


### Contexte du mandat

Un cabinet d'avocats parisien, **Legrand & Associés**, mandate une investigation OSINT sur **Marc Delaunay**, 48 ans, directeur administratif et financier de **TechnoVert SAS** — ETI française spécialisée dans les technologies de recyclage industriel, 450 collaborateurs, CA 85 M€, deux sites de production (Lyon, Lille). Le cabinet représente un actionnaire minoritaire (12 % du capital) qui formule cinq soupçons :

1. **Détournement de fonds** vers des structures offshore via des contrats de « consulting » fictifs ou surfacturés.
2. **Blanchiment partiel** de ces fonds en crypto-actifs.
3. **Campagne de désinformation** orchestrée contre un lanceur d'alerte interne — un ancien contrôleur de gestion remercié 8 mois plus tôt après avoir alerté sur des écritures comptables suspectes.
4. **Cluster de faux comptes coordonnés** sur X et Telegram amplifiant la diffamation, possiblement opérés par un service criminel rémunéré.
5. **Production et diffusion de contenus générés par IA** — courte vidéo deepfake du lanceur d'alerte, fausses photos d'alibi, faux média en ligne créé pour amplifier le narratif diffamatoire.


### Sélecteurs initiaux fournis par le client

- Nom complet : Marc Delaunay.
- Date de naissance approximative : 1976-1977.
- Poste : DAF TechnoVert SAS.
- Email professionnel : `m.delaunay@technovert.fr`.
- Lanceur d'alerte concerné par la campagne diffamatoire : Antoine Berthier, contrôleur de gestion remercié en septembre 2025.


### Mandat

Produire un rapport OSINT complet, exploitable judiciairement, identifiant :

- les structures offshore éventuelles et leur articulation avec Delaunay ;
- les flux financiers visibles en source ouverte (sans accès aux comptes bancaires) ;
- les actifs détenus directement ou indirectement ;
- la campagne de désinformation : architecture, faux comptes, faux média, contenus IA, attribution probable ;
- les éléments crypto traçables en source ouverte.

Le cabinet envisage un dépôt de plainte au **Parquet National Financier** et une saisine du **C3N** (Centre de lutte contre les criminalités numériques) pour le volet désinformation et deepfake.


### Contraintes

- **Délai** : 6 semaines.
- **Budget** : raisonnable (cabinet d'avocats privé), sans accès à des bases payantes lourdes — pas de Chainalysis, pas de WorldCheck Pro, pas de Maltego Pro.
- **Aucune interaction** avec la cible Delaunay (techniquement compétent, susceptible de détecter une approche).
- **Aucun accès illégal** sous aucun prétexte. Pas d'accès à des données protégées, pas d'usurpation d'identité agressive, pas de phishing.
- **OPSEC stricte** : Delaunay et ses éventuels prestataires de désinformation sont susceptibles d'observer la surface d'investigation.
- **Rapport versable au dossier judiciaire** : chaîne de custody, capture horodatée et hashée, vocabulaire calibré, cotation explicite, limites documentées.


### Trajectoire narrative

Au fil des 103 chapitres, l'investigateur va passer du nom de Delaunay à un schéma articulé :

- Un réseau de **quatre sociétés écrans** (Malte, Chypre, BVI, Luxembourg) reliées par adresse de domiciliation, nominees et flux croisés.
- Des **flux bancaires opaques** convertis partiellement en Bitcoin via un compte particulier sur Binance, avec cashout via P2P et stablecoins USDT-TRC20 *(le détail blockchain est renvoyé au cours OSINT Crypto vFULL)*.
- Un **patrimoine immobilier** en SCI familiale incohérent avec les revenus déclarés (un mas en Provence à 1,8 M€, une villa à Marrakech, deux appartements parisiens dans une SCI nominee).
- Une **campagne de désinformation** orchestrée via un blog `verites-technovert.com`, huit faux comptes coordonnés sur X (et neuf sur Telegram), un faux média `info-finance-eu.com` publiant articles diffamatoires, une **courte vidéo deepfake** d'Antoine Berthier tenant des propos compromettants fictifs, et trois fausses photographies de soirées professionnelles destinées à fabriquer un narratif d'inconduite.
- Une **trace dans des stealer logs** : les identifiants Gmail personnels de Delaunay apparaissent dans un dump récent vendu sur un canal Telegram, fournissant un point de pivot inattendu.


### Les 21 épisodes du fil rouge

Le fil rouge se déploie en 21 épisodes répartis le long du cours. Chaque épisode est court (un encadré de 200 à 400 mots) et illustre une notion du chapitre où il apparaît.

| Épisode | Titre | Chapitre |
|---|---|---|
| MIRAGE 0 | Cadrage du mandat | Ch.12 |
| MIRAGE 1 | Questions de renseignement | Ch.13 |
| MIRAGE 2 | Sélecteurs initiaux | Ch.14 |
| MIRAGE 3 | OPSEC et plan de collecte | Ch.18 |
| MIRAGE 4 | Personne physique et homonymie | Ch.26 |
| MIRAGE 5 | Identité numérique et pseudonymes | Ch.28 |
| MIRAGE 6 | SOCMINT multi-plateformes | Ch.32 |
| MIRAGE 7 | Telegram, forums et communautés | Ch.33 |
| MIRAGE 8 | Sociétés, dirigeants et UBO | Ch.37 |
| MIRAGE 9 | Infrastructure web et domaines | Ch.39 |
| MIRAGE 10 | Breaches, leaks et stealer logs | Ch.43 |
| MIRAGE 11 | Image suspecte et vérification | Ch.47 |
| MIRAGE 12 | GEOINT et chronolocation | Ch.49 |
| MIRAGE 13 | Signaux financiers ouverts | Ch.70 |
| MIRAGE 14 | Piste crypto, renvoi OSINT Crypto | Ch.72 |
| MIRAGE 15 | Piste dark web, renvoi Dark Web | Ch.44 |
| MIRAGE 16 | Deepfake et contenu synthétique | Ch.53 |
| MIRAGE 17 | Campagne d'influence coordonnée | Ch.76 |
| MIRAGE 18 | Graphe d'entités et timeline | Ch.83 |
| MIRAGE 19 | Hypothèses concurrentes | Ch.79 |
| MIRAGE 20 | Rapport final, limites et suites possibles | Ch.93 |

-----
