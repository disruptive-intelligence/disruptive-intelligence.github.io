---
title: OSINT — cours complet
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
format: cours
revue: '2026-05-16'
---

*Investigation en sources ouvertes : doctrine, méthode, collecte, vérification, IA et production de renseignement*

**Cours maître refondu 2026 — 103 chapitres • 12 parties • 15 annexes**

*Investiguer • Collecter • Vérifier • Analyser • Produire du renseignement*

-----

### Avant-propos

#### Ce qu'est ce cours

**OSINT Mastery 2026** est le cours-mère de la bibliothèque. Il est conçu pour être **autonome** : un lecteur qui le travaille intégralement dispose des bases nécessaires pour conduire une investigation OSINT professionnelle de bout en bout, qu'il soit analyste CTI, investigateur financier, journaliste, magistrat, officier de renseignement, responsable conformité, consultant en due diligence, chercheur en sciences sociales ou citoyen formé.

Le cours adopte une posture **professionnelle, méthodologique et défensive**. Il enseigne comment investiguer rigoureusement à partir de sources ouvertes ; il n'enseigne ni à commettre une infraction, ni à échapper à la traçabilité, ni à contourner des protections légitimes. Cette posture est constante : chaque fois qu'une typologie criminelle ou un usage adverse de l'OSINT est exposé, c'est sous l'angle de la compréhension, de la détection et de la défense.

L'OSINT en 2026 n'est plus la même discipline qu'en 2020. Trois ruptures majeures ont reconfiguré le métier : (1) la **professionnalisation institutionnelle** — l'IC OSINT Strategy 2024-2026 de l'ODNI américaine formalise l'OSINT comme INT à part entière, la France crée le **Bataillon de Réserve en Renseignement Spécialisé (B2RS)** et le **service VIGINUM**, l'OTAN intègre l'OSINT à sa doctrine ; (2) l'**irruption de l'intelligence artificielle** — LLMs comme assistants, agents autonomes, deepfakes industriels, géolocalisation multi-agent ; (3) la **fermeture progressive des plateformes** — X payant, API LinkedIn restreinte, Meta verrouillée, Reddit fermé, Google dégradé. Le cours intègre ces ruptures comme structurantes, pas comme annexes.

#### Public cible et prérequis

Ce cours s'adresse à des adultes professionnels ou en formation professionnalisante. Il suppose une **aisance numérique correcte** (navigation web, utilisation d'un terminal, compréhension générale du fonctionnement d'Internet, gestion de fichiers), mais ne suppose aucun bagage préalable en renseignement, en cybersécurité ou en droit. Les prérequis spécifiques (notions de réseau, bases Python, droit du numérique) sont introduits dans le cours quand nécessaire.

Le cours s'adresse également à des **citoyens formés** qui souhaitent comprendre la discipline pour mieux résister à la désinformation, vérifier l'information qu'ils consomment, ou s'engager dans une démarche d'enquête citoyenne encadrée (à l'image des contributeurs Bellingcat ou des participants Trace Labs).

#### Ce que ce cours fait

- Il enseigne la **doctrine** : qu'est-ce que l'OSINT, comment elle s'inscrit dans le cycle du renseignement, quelles sont ses disciplines connexes, quelle est sa place en 2026.
- Il enseigne le **cadre légal et éthique** : RGPD, AI Act, DSA, CSDDD, sanctions, Failure to Prevent Fraud, jurisprudences, déontologie professionnelle.
- Il enseigne la **méthodologie** : cadrage, plan de collecte, sélecteurs, pivots, journal, chaîne de custody, structuration, vérification, ACH, cotation, formulation.
- Il enseigne la **technique** : moteurs, dorks, SOCMINT par plateforme, IMINT, GEOINT, infrastructure web, breaches, leaks, dark web (en vue maître).
- Il enseigne la **vérification** dans un monde post-deepfakes : C2PA, SynthID, signaux visuels, méthodologie intégrée, admissibilité judiciaire.
- Il enseigne l'**IA et l'automatisation** : LLMs comme assistants, prompting, hallucinations, agents autonomes, knowledge graphs locaux, pipelines Python.
- Il enseigne la **production** : note courte, rapport complet, fiche entité, rapport judiciaire, TLP, diffusion, veille.
- Il fournit un **fil rouge complet** (Opération MIRAGE 2026) traversant tous les chapitres jusqu'au cas de synthèse.
- Il fournit **17 cas pratiques** et un exercice final non guidé avec son corrigé.

#### Ce que ce cours ne fait pas

- Il ne se substitue pas aux cours spécialisés de la bibliothèque pour les domaines suivants :
    - L'enquête crypto on-chain approfondie (clustering, attribution, mixers, bridges, cashout) — renvoi systématique à **OSINT Crypto vFULL**.
    - L'investigation financière approfondie (UBO complexes, schémas de blanchiment, AML/CFT, comptabilité forensique) — renvoi systématique à **FININT Investigation Financière vFULL**.
    - L'enquête dark web approfondie (Tor en profondeur, marketplaces, leak sites, IA criminelle, écosystèmes) — renvoi systématique à **Dark Web vFULL**.
    - La Cyber Threat Intelligence approfondie (acteurs, TTP, intrusion analysis, attribution étatique) — renvoi vers le cours CTI dédié.
- Il ne fournit pas de tutoriel exhaustif pour chaque outil cité : les outils changent tous les six mois, la méthodologie reste. Les outils sont présentés comme exemples opérationnels à date 2026.
- Il n'est pas un précis de droit ni un manuel de procédure pénale : il pose le cadre, il ne tient pas lieu de conseil juridique.
- Il ne forme pas à l'utilisation offensive de l'OSINT, à l'usurpation d'identité agressive, au harcèlement, au doxxing, ou à toute pratique non conforme au droit et à l'éthique professionnelle.

#### Posture éthique constante

L'OSINT touche à la vie privée, à la réputation, à la liberté de circulation, parfois à la liberté physique de personnes — y compris de personnes innocentes ou non concernées. Une note d'analyse mal calibrée, un soupçon pris pour une preuve, une diffusion non maîtrisée, une confusion entre renseignement et accusation peuvent causer des dommages réels. La rigueur méthodologique n'est pas un luxe académique : elle est la condition même de la légitimité de la discipline. Tout au long du cours, cette rigueur est présentée comme un réflexe quotidien, pas comme un appendice de fin de chapitre.

#### Place de l'IA dans l'OSINT moderne

L'IA est un **accélérateur, pas un substitut**. Elle excelle là où l'humain est inefficace (volume, traduction, extraction d'entités, monitoring continu, première classification) ; elle reste défaillante là où l'humain est irremplaçable (jugement contextuel, vérification, formulation calibrée, décision éthique). Le cours adopte une position **augmentée mais souveraine** : l'IA assiste l'analyste, l'analyste reste responsable. Le protocole **Retrieve-Store-Cite** (Ch.63) opérationnalise ce principe : aucune affirmation produite par IA n'entre dans un livrable sans source vérifiable et tracée.

#### Articulation avec la bibliothèque

Le tableau suivant cartographie les renvois entre OSINT Mastery et les cours spécialisés.

| Domaine | Couverture dans OSINT Mastery | Cours spécialisé pour approfondir |
|---|---|---|
| Crypto / blockchain | Vue maître (Ch.72) | OSINT Crypto vFULL |
| Investigation financière | Vue maître (Ch.70-71, 77) | FININT Investigation Financière vFULL |
| Dark web / DARKINT | Vue opérationnelle (Ch.44) | Dark Web vFULL |
| Cyber Threat Intelligence | Chapitre dédié (Ch.74-75) | Cours CTI dédié |
| Intelligence économique / due diligence | Chapitres dédiés (Ch.36-38, 77) | Cours IE / Due Diligence |
| Forensic numérique | Méthodologie + chaîne de custody (Ch.15-16) | Cours Forensic dédié |

L'annexe O fournit la cartographie complète.

#### Importance de la preuve, de la traçabilité et de l'incertitude

Trois principes traversent tout le cours.

**La preuve OSINT est toujours faillible.** Une capture peut être falsifiée, un registre peut être erroné, un compte peut être usurpé, un contenu peut être généré par IA. L'analyste OSINT ne produit pas de preuve absolue : il produit du renseignement coté, avec un niveau de confiance explicite et des limites documentées. Le vocabulaire calibré (Ch.86) protège contre la tentation du verdict.

**La traçabilité conditionne la valeur du renseignement.** Une affirmation sans source citée est du bruit. Une source non horodatée et non préservée est une affirmation faible. Le journal d'enquête (Ch.15) et la chaîne de conservation numérique (Ch.16) ne sont pas des formalités : ils sont la colonne vertébrale du métier.

**L'incertitude est constitutive du métier, pas un échec.** Le travail de l'analyste n'est pas de produire des certitudes, mais d'éclairer une décision sous incertitude. La cotation (Ch.84-85), l'ACH (Ch.79), la formulation analytique (Ch.86) sont les outils qui permettent de dire ce qu'on sait, ce qu'on ne sait pas, et ce qu'on suppose, sans confondre les trois.

-----

### Mode d'emploi du cours

#### Comment lire ce cours

Le cours est **dense**. Il peut se lire de plusieurs manières.

**Lecture linéaire intégrale.** C'est le parcours recommandé pour une formation initiale ou une montée en compétence complète. Comptez entre 80 et 120 heures de lecture active selon votre rythme et votre niveau d'entrée. Le fil rouge MIRAGE est conçu pour être suivi dans cet ordre.

**Lecture par parcours thématique.** Si vous avez un objectif spécialisé (CTI, due diligence, GEOINT, IA, rapport judiciaire), suivez l'un des sept parcours proposés ci-dessous. Chaque parcours est conçu pour être autosuffisant sur son périmètre.

**Lecture par référence.** Chaque chapitre est conçu pour être autonome dans la mesure du possible. La table des matières et le glossaire (Annexe A) permettent un usage à la demande.

**Préparation d'enquête.** Avant de lancer une investigation réelle, le Parcours express (60 minutes) et les annexes opérationnelles (D, E, F, G, H, J, K, L) sont des compagnons de bureau.

#### Parcours de lecture recommandés

Sept parcours sont proposés. Ils ne sont pas exclusifs : un parcours « analyste OSINT complet » devrait à terme couvrir l'intégralité du cours.

**Parcours 1 — Débutant OSINT (formation initiale, 20-30 heures)**

Pour un lecteur sans expérience préalable qui souhaite acquérir les bases solides.

- Avant-propos, mode d'emploi, parcours express.
- Partie I complète (Ch.1-5).
- Partie II : Ch.6, 8, 9, 11.
- Partie III : Ch.12, 14, 15, 18.
- Partie IV : Ch.19, 20, 23.
- Partie V : Ch.26, 27, 31, 32.
- Partie VII : Ch.45, 46, 48.
- Partie VIII : Ch.53, 57.
- Partie XI : Ch.78, 84, 85.
- Partie XII : Ch.87, 93.
- Annexes A, D, F, K.

**Parcours 2 — Analyste OSINT complet (formation cœur, 80-120 heures)**

L'intégralité du cours, dans l'ordre. C'est le parcours par défaut.

**Parcours 3 — SOC / CTI (40-60 heures)**

Pour un analyste SOC, CTI ou ingénieur sécurité.

- Parties I et II intégrales.
- Partie IV intégrale.
- Partie VI : Ch.36, 39, 40, 41, 42, 43, 44.
- Partie VIII : Ch.55, 57, 59.
- Partie IX intégrale.
- Partie X : Ch.74, 75, 76.
- Parties XI et XII (sélection : Ch.78, 79, 84, 85, 87, 88, 100).
- Annexes A, B, C, D, E, F, K, N, O.

**Parcours 4 — Investigation financière / due diligence (40-60 heures)**

Pour un analyste FININT, KYC/KYB, due diligence M&A.

- Parties I, II, III intégrales.
- Partie V : Ch.26, 27, 28, 29, 31.
- Partie VI intégrale.
- Partie VIII : Ch.53, 55, 57.
- Partie X : Ch.70, 71, 72, 73, 77.
- Partie XI intégrale.
- Partie XII : Ch.87, 88, 89, 90, 91, 97, 101.
- Annexes A, C, D, E, H, J, L, O.
- **Renvoi systématique vers FININT vFULL et OSINT Crypto vFULL.**

**Parcours 5 — GEOINT / vérification visuelle (30-40 heures)**

Pour un journaliste d'investigation, un analyste de conflit, un humanitaire.

- Parties I, II intégrales.
- Partie III : Ch.12, 14, 15, 16.
- Partie VII intégrale.
- Partie VIII intégrale.
- Partie XI : Ch.79, 80, 84, 85, 86.
- Partie XII : Ch.87, 94.
- Annexes A, D, F, J, K.

**Parcours 6 — IA / automatisation (30-40 heures)**

Pour un analyste qui souhaite industrialiser ses workflows.

- Parties I, II intégrales (focus Ch.7, 10).
- Partie III : Ch.16, 17.
- Partie IV : Ch.22, 24, 25.
- Partie VIII : Ch.55, 56.
- Partie IX intégrale.
- Partie XI : Ch.82, 83, 84, 85.
- Annexes A, E, K, N.

**Parcours 7 — Juridique / rapport (25-35 heures)**

Pour un magistrat, un avocat, un officier de police judiciaire, un commanditaire.

- Parties I, II intégrales.
- Partie III intégrale.
- Partie VIII : Ch.55, 57, 58, 59.
- Partie XI intégrale.
- Partie XII : Ch.87, 88, 89, 90, 91, 92, 93.
- Annexes A, G, H, I, J, L, O.

#### Conventions de notation

Le cours utilise les conventions suivantes.

- **Termes techniques** en gras à leur première occurrence.
- *Encadrés MIRAGE* pour les épisodes du fil rouge.
- > **Encadrés méthodologiques** pour les principes clés à mémoriser.
- Tableaux pour les comparaisons d'outils, de sources, de cadres.
- Code monospaced pour les dorks, requêtes, commandes : `site:example.com filetype:pdf`.
- Renvois explicites : *(voir Ch.X)* pour les renvois internes, *(renvoi → cours Y vFULL)* pour les renvois externes.

#### Mise à jour du cours

L'écosystème OSINT évolue mensuellement. Les outils nommés sont des exemples opérationnels à date avril-mai 2026. Une révision annuelle est recommandée. Les principes méthodologiques (Parties I-III, XI) ont une durée de vie longue ; les chapitres techniques (Parties IV, V, VI, IX) doivent être révisés régulièrement.

#### Convention temporelle (à retenir pendant toute la lecture)

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

### Parcours express — Mener une enquête OSINT en 60 minutes

> **Ce parcours est un compagnon opérationnel.** Il ne se substitue pas au cours, mais il permet à un analyste pressé de structurer une investigation simple en une heure. Imprimez-le, gardez-le à côté de votre clavier.

L'enquête OSINT n'est jamais improvisée. Même quand vous disposez d'une heure, suivez la séquence ci-dessous. Sauter une étape, c'est s'exposer à produire du bruit, à violer un cadre légal, ou à griller une cible.

#### Étape 1 — Comprendre la demande (5 minutes)

Qui demande ? Pourquoi ? Quel est l'événement déclencheur ? Quelle est la décision attendue à partir de votre livrable ? Quel est le délai ? Quelles sont les contraintes (budget, OPSEC, légalité, juridiction) ? Si la demande est vague, posez la question : « Que ferez-vous si je vous donne A ? Que ferez-vous si je vous donne B ? » — la réponse révèle le besoin réel.

#### Étape 2 — Vérifier le mandat et le périmètre (3 minutes)

Êtes-vous légitime pour conduire cette enquête ? Avez-vous un mandat écrit ou implicite ? Le périmètre est-il clairement défini ? S'agit-il d'une personne physique, d'une société, d'un événement, d'un contenu ? Si vous êtes en cabinet, ce n'est pas optionnel : sans mandat clair, vous ne lancez pas.

#### Étape 3 — Formuler les questions de renseignement (5 minutes)

Une question OSINT est **fermée, vérifiable, et reformulable en hypothèse**. « Que sais-tu sur Delaunay ? » n'est pas une question OSINT. « Delaunay contrôle-t-il une société à Malte ? » en est une. « Quelle est l'adresse personnelle de Delaunay ? » en est une autre. Listez 3 à 5 questions principales et 5 à 10 questions secondaires.

#### Étape 4 — Identifier les sélecteurs initiaux (2 minutes)

Quels sont les **points d'entrée** dans l'enquête ? Nom complet, date de naissance, email, téléphone, photo, adresse, username, domaine, IP, wallet ? Listez ce que vous avez. C'est sur ces sélecteurs que vous allez pivoter.

#### Étape 5 — Évaluer les risques juridiques et éthiques (3 minutes)

L'enquête touche-t-elle à des données personnelles sensibles (santé, opinions politiques, religion, orientation sexuelle) ? À des mineurs ? À une juridiction restrictive (UE et RGPD, USA et CCPA, Allemagne) ? Y a-t-il un risque de doxxing involontaire ? Y a-t-il un risque de violation du secret professionnel ? Si oui, formalisez et tracez votre décision avant de lancer.

#### Étape 6 — Préparer l'OPSEC minimale (5 minutes)

Pour une enquête simple, vous avez besoin a minima de : un navigateur en profil dédié (ou navigation privée), un VPN si la cible est susceptible de consulter ses logs, un compte d'investigation (pas votre compte personnel) pour toute interaction avec une plateforme. Pour des enquêtes plus sensibles, voir Ch.9-11.

#### Étape 7 — Lancer les recherches prioritaires (15 minutes)

Commencez par les sources gratuites, rapides, et indexées : Google, Yandex (irremplaçable pour reverse image et contenus russophones), Bing, registres officiels, archive.org. Posez les bonnes requêtes (dorks ciblés, pas de fouille au hasard). Documentez chaque action dans votre journal.

#### Étape 8 — Pivoter sans se disperser (10 minutes)

À chaque résultat, demandez-vous : **ceci m'apporte-t-il un nouveau sélecteur exploitable ?** Si oui, ajoutez-le à votre liste et continuez. Si non, ne vous laissez pas distraire. La discipline du pivot est ce qui distingue un investigateur expérimenté d'un curieux qui surfe.

#### Étape 9 — Capturer, horodater, hasher (en continu)

Chaque page visitée d'intérêt est capturée (Hunchly idéalement, SingleFile sinon), horodatée, et hashée si elle est destinée à un usage judiciaire. Une URL est un mauvais témoin : elle peut changer ou disparaître. Une capture horodatée et hashée est une preuve.

#### Étape 10 — Vérifier et corroborer (5 minutes)

Pour chaque fait majeur : **deux sources indépendantes minimum**. Une source unique = une piste à confirmer, pas un fait établi. Une rumeur reprise par 50 sites n'est pas 50 sources : c'est une seule source mal recyclée.

#### Étape 11 — Construire une mini-timeline (3 minutes)

Reportez les événements datés sur une ligne temporelle. Les incohérences chronologiques sont l'un des révélateurs les plus puissants : une déclaration impossible à la date alléguée, un poste occupé avant la fondation de l'entreprise, une photo prise après l'événement supposé.

#### Étape 12 — Distinguer piste, indice, fait, hypothèse et preuve (en continu)

C'est la discipline du chapitre 4. Une **piste** est une direction à explorer. Un **indice** est un élément factuel qui oriente une hypothèse. Un **fait** est un indice établi par au moins deux sources indépendantes et cotées. Une **hypothèse** est une explication candidate des faits. Une **preuve** est un fait qui établit la véracité d'une hypothèse au-delà du raisonnable. Confondre ces niveaux est l'erreur la plus fréquente de l'analyste débutant.

#### Étape 13 — Utiliser l'IA uniquement comme assistant vérifiable (en continu)

Un LLM peut traduire, résumer, extraire des entités, générer des dorks. Il ne peut **pas** être cité comme source. Tout ce qui sort d'un LLM est à vérifier. Protocole **Retrieve-Store-Cite** : si vous citez un fait, vous citez sa source primaire, pas le LLM qui l'a produit.

#### Étape 14 — Produire une mini-note (3 minutes)

Une mini-note OSINT tient en une page. **BLUF** (Bottom Line Up Front) : la conclusion en deux phrases, avec son niveau de confiance. Puis : trois à cinq faits clés cotés, une timeline, les sources, les limites. Pas de verdict, vocabulaire calibré.

#### Étape 15 — Identifier les limites et les suites possibles (1 minute)

Quelles questions restent ouvertes ? Quelles sources n'avez-vous pas pu consulter ? Quelles vérifications complémentaires seraient utiles ? Quelles spécialisations devraient prendre le relais (crypto, FININT, dark web) ? Ces limites font partie du livrable, pas en marge de lui.

-----

### Fil rouge — Opération MIRAGE 2026

> **Le fil rouge MIRAGE traverse l'ensemble du cours.** Il sert deux fonctions : illustrer concrètement les concepts au fil des chapitres, et fournir un cas de synthèse complet (Ch.93). Vous le retrouverez sous forme d'encadrés *« MIRAGE — Épisode N »* tout au long du cours.

#### Contexte du mandat

Un cabinet d'avocats parisien, **Legrand & Associés**, mandate une investigation OSINT sur **Marc Delaunay**, 48 ans, directeur administratif et financier de **TechnoVert SAS** — ETI française spécialisée dans les technologies de recyclage industriel, 450 collaborateurs, CA 85 M€, deux sites de production (Lyon, Lille). Le cabinet représente un actionnaire minoritaire (12 % du capital) qui formule cinq soupçons :

1. **Détournement de fonds** vers des structures offshore via des contrats de « consulting » fictifs ou surfacturés.
2. **Blanchiment partiel** de ces fonds en crypto-actifs.
3. **Campagne de désinformation** orchestrée contre un lanceur d'alerte interne — un ancien contrôleur de gestion remercié 8 mois plus tôt après avoir alerté sur des écritures comptables suspectes.
4. **Cluster de faux comptes coordonnés** sur X et Telegram amplifiant la diffamation, possiblement opérés par un service criminel rémunéré.
5. **Production et diffusion de contenus générés par IA** — courte vidéo deepfake du lanceur d'alerte, fausses photos d'alibi, faux média en ligne créé pour amplifier le narratif diffamatoire.

#### Sélecteurs initiaux fournis par le client

- Nom complet : Marc Delaunay.
- Date de naissance approximative : 1976-1977.
- Poste : DAF TechnoVert SAS.
- Email professionnel : `m.delaunay@technovert.fr`.
- Lanceur d'alerte concerné par la campagne diffamatoire : Antoine Berthier, contrôleur de gestion remercié en septembre 2025.

#### Mandat

Produire un rapport OSINT complet, exploitable judiciairement, identifiant :

- les structures offshore éventuelles et leur articulation avec Delaunay ;
- les flux financiers visibles en source ouverte (sans accès aux comptes bancaires) ;
- les actifs détenus directement ou indirectement ;
- la campagne de désinformation : architecture, faux comptes, faux média, contenus IA, attribution probable ;
- les éléments crypto traçables en source ouverte.

Le cabinet envisage un dépôt de plainte au **Parquet National Financier** et une saisine du **C3N** (Centre de lutte contre les criminalités numériques) pour le volet désinformation et deepfake.

#### Contraintes

- **Délai** : 6 semaines.
- **Budget** : raisonnable (cabinet d'avocats privé), sans accès à des bases payantes lourdes — pas de Chainalysis, pas de WorldCheck Pro, pas de Maltego Pro.
- **Aucune interaction** avec la cible Delaunay (techniquement compétent, susceptible de détecter une approche).
- **Aucun accès illégal** sous aucun prétexte. Pas d'accès à des données protégées, pas d'usurpation d'identité agressive, pas de phishing.
- **OPSEC stricte** : Delaunay et ses éventuels prestataires de désinformation sont susceptibles d'observer la surface d'investigation.
- **Rapport versable au dossier judiciaire** : chaîne de custody, capture horodatée et hashée, vocabulaire calibré, cotation explicite, limites documentées.

#### Trajectoire narrative

Au fil des 103 chapitres, l'investigateur va passer du nom de Delaunay à un schéma articulé :

- Un réseau de **quatre sociétés écrans** (Malte, Chypre, BVI, Luxembourg) reliées par adresse de domiciliation, nominees et flux croisés.
- Des **flux bancaires opaques** convertis partiellement en Bitcoin via un compte particulier sur Binance, avec cashout via P2P et stablecoins USDT-TRC20 *(le détail blockchain est renvoyé au cours OSINT Crypto vFULL)*.
- Un **patrimoine immobilier** en SCI familiale incohérent avec les revenus déclarés (un mas en Provence à 1,8 M€, une villa à Marrakech, deux appartements parisiens dans une SCI nominee).
- Une **campagne de désinformation** orchestrée via un blog `verites-technovert.com`, huit faux comptes coordonnés sur X (et neuf sur Telegram), un faux média `info-finance-eu.com` publiant articles diffamatoires, une **courte vidéo deepfake** d'Antoine Berthier tenant des propos compromettants fictifs, et trois fausses photographies de soirées professionnelles destinées à fabriquer un narratif d'inconduite.
- Une **trace dans des stealer logs** : les identifiants Gmail personnels de Delaunay apparaissent dans un dump récent vendu sur un canal Telegram, fournissant un point de pivot inattendu.

#### Les 21 épisodes du fil rouge

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

## Sommaire

- [PARTIE I — Doctrine, cadre et posture](01-partie-i-doctrine-cadre-et-posture/index.md)
    - [Chapitre 1 — L'OSINT comme discipline de renseignement](01-partie-i-doctrine-cadre-et-posture/01-chapitre-1-l-osint-comme-discipline-de-renseigneme.md)
    - [Chapitre 2 — Histoire et doctrine OSINT 2024-2026](01-partie-i-doctrine-cadre-et-posture/02-chapitre-2-histoire-et-doctrine-osint-2024-2026.md)
    - [Chapitre 3 — Disciplines connexes du renseignement](01-partie-i-doctrine-cadre-et-posture/03-chapitre-3-disciplines-connexes-du-renseignement.md)
    - [Chapitre 4 — Donnée, information, indice, fait, preuve, hypothèse, renseignement](01-partie-i-doctrine-cadre-et-posture/04-chapitre-4-donnee-information-indice-fait-preuve-h.md)
    - [Chapitre 5 — Cycle du renseignement appliqué à l'OSINT](01-partie-i-doctrine-cadre-et-posture/05-chapitre-5-cycle-du-renseignement-applique-a-l-osi.md)
- [PARTIE II — Cadre juridique, éthique et OPSEC](02-partie-ii-cadre-juridique-ethique-et-opsec/index.md)
    - [Chapitre 6 — Cadre juridique français de l'investigation OSINT](02-partie-ii-cadre-juridique-ethique-et-opsec/01-chapitre-6-cadre-juridique-francais-de-l-investiga.md)
    - [Chapitre 7 — Cadre européen et international 2024-2026](02-partie-ii-cadre-juridique-ethique-et-opsec/02-chapitre-7-cadre-europeen-et-international-2024-20.md)
    - [Chapitre 8 — Éthique, déontologie et responsabilité de l'analyste](02-partie-ii-cadre-juridique-ethique-et-opsec/03-chapitre-8-ethique-deontologie-et-responsabilite-d.md)
    - [Chapitre 9 — OPSEC de l'investigateur OSINT](02-partie-ii-cadre-juridique-ethique-et-opsec/04-chapitre-9-opsec-de-l-investigateur-osint.md)
    - [Chapitre 10 — OPSEC face aux plateformes et à l'IA](02-partie-ii-cadre-juridique-ethique-et-opsec/05-chapitre-10-opsec-face-aux-plateformes-et-a-l-ia.md)
    - [Chapitre 11 — Sock puppets, avatars et identités d'enquête](02-partie-ii-cadre-juridique-ethique-et-opsec/06-chapitre-11-sock-puppets-avatars-et-identites-d-en.md)
- [PARTIE III — Méthodologie d'enquête et gestion du dossier](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/index.md)
    - [Chapitre 12 — Cadrer une mission OSINT](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/01-chapitre-12-cadrer-une-mission-osint.md)
    - [Chapitre 13 — Questions de renseignement et plan de collecte](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/02-chapitre-13-questions-de-renseignement-et-plan-de.md)
    - [Chapitre 14 — Sélecteurs OSINT et logique de pivot](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/03-chapitre-14-selecteurs-osint-et-logique-de-pivot.md)
    - [Chapitre 15 — Journal d'enquête, preuve et traçabilité](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/04-chapitre-15-journal-d-enquete-preuve-et-tracabilit.md)
    - [Chapitre 16 — Chaîne de conservation numérique](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/05-chapitre-16-chaine-de-conservation-numerique.md)
    - [Chapitre 17 — Structurer l'information collectée](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/06-chapitre-17-structurer-l-information-collectee.md)
    - [Chapitre 18 — Lab de l'investigateur](03-partie-iii-methodologie-d-enquete-et-gestion-du-do/07-chapitre-18-lab-de-l-investigateur.md)
- [PARTIE IV — Moteurs, recherche web et restrictions plateformes](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/index.md)
    - [Chapitre 19 — Moteurs de recherche généralistes](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/01-chapitre-19-moteurs-de-recherche-generalistes.md)
    - [Chapitre 20 — Google dorking et opérateurs avancés](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/02-chapitre-20-google-dorking-et-operateurs-avances.md)
    - [Chapitre 21 — Moteurs spécialisés OSINT](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/03-chapitre-21-moteurs-specialises-osint.md)
    - [Chapitre 22 — IA-search et moteurs conversationnels](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/04-chapitre-22-ia-search-et-moteurs-conversationnels.md)
    - [Chapitre 23 — Archivage et préservation web](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/05-chapitre-23-archivage-et-preservation-web.md)
    - [Chapitre 24 — Restrictions plateformes 2024-2026](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/06-chapitre-24-restrictions-plateformes-2024-2026.md)
    - [Chapitre 25 — Adaptation méthodologique aux restrictions](04-partie-iv-moteurs-recherche-web-et-restrictions-pl/07-chapitre-25-adaptation-methodologique-aux-restrict.md)
- [PARTIE V — Personnes, identités et SOCMINT](05-partie-v-personnes-identites-et-socmint/index.md)
    - [Chapitre 26 — Identification de personne physique](05-partie-v-personnes-identites-et-socmint/01-chapitre-26-identification-de-personne-physique.md)
    - [Chapitre 27 — Pivots email, téléphone, username, photo](05-partie-v-personnes-identites-et-socmint/02-chapitre-27-pivots-email-telephone-username-photo.md)
    - [Chapitre 28 — Identité numérique et pseudonymes](05-partie-v-personnes-identites-et-socmint/03-chapitre-28-identite-numerique-et-pseudonymes.md)
    - [Chapitre 29 — Documents, métadonnées et traces indirectes](05-partie-v-personnes-identites-et-socmint/04-chapitre-29-documents-metadonnees-et-traces-indire.md)
    - [Chapitre 30 — Reconnaissance faciale et image-to-person](05-partie-v-personnes-identites-et-socmint/05-chapitre-30-reconnaissance-faciale-et-image-to-per.md)
    - [Chapitre 31 — SOCMINT : méthodologie générale](05-partie-v-personnes-identites-et-socmint/06-chapitre-31-socmint-methodologie-generale.md)
    - [Chapitre 32 — Plateformes sociales occidentales](05-partie-v-personnes-identites-et-socmint/07-chapitre-32-plateformes-sociales-occidentales.md)
    - [Chapitre 33 — Telegram](05-partie-v-personnes-identites-et-socmint/08-chapitre-33-telegram.md)
    - [Chapitre 34 — Discord, forums et plateformes alternatives](05-partie-v-personnes-identites-et-socmint/09-chapitre-34-discord-forums-et-plateformes-alternat.md)
    - [Chapitre 35 — Faux comptes, bots et comportements coordonnés](05-partie-v-personnes-identites-et-socmint/10-chapitre-35-faux-comptes-bots-et-comportements-coo.md)
- [PARTIE VI — Corporate, infrastructure et données exposées](06-partie-vi-corporate-infrastructure-et-donnees-expo/index.md)
    - [Chapitre 36 — Investigation corporate généraliste](06-partie-vi-corporate-infrastructure-et-donnees-expo/01-chapitre-36-investigation-corporate-generaliste.md)
    - [Chapitre 37 — Registres corporate et sources internationales](06-partie-vi-corporate-infrastructure-et-donnees-expo/02-chapitre-37-registres-corporate-et-sources-interna.md)
    - [Chapitre 38 — Due diligence, sanctions, PEP et adverse media](06-partie-vi-corporate-infrastructure-et-donnees-expo/03-chapitre-38-due-diligence-sanctions-pep-et-adverse.md)
    - [Chapitre 39 — Domaines, DNS, WHOIS/RDAP et certificats](06-partie-vi-corporate-infrastructure-et-donnees-expo/04-chapitre-39-domaines-dns-whois-rdap-et-certificats.md)
    - [Chapitre 40 — Sous-domaines, IP, ASN, BGP et exposition technique](06-partie-vi-corporate-infrastructure-et-donnees-expo/05-chapitre-40-sous-domaines-ip-asn-bgp-et-exposition.md)
    - [Chapitre 41 — Surface d'attaque moderne](06-partie-vi-corporate-infrastructure-et-donnees-expo/06-chapitre-41-surface-d-attaque-moderne.md)
    - [Chapitre 42 — Breaches, leaks et pastebins](06-partie-vi-corporate-infrastructure-et-donnees-expo/07-chapitre-42-breaches-leaks-et-pastebins.md)
    - [Chapitre 43 — Infostealers et stealer logs](06-partie-vi-corporate-infrastructure-et-donnees-expo/08-chapitre-43-infostealers-et-stealer-logs.md)
    - [Chapitre 44 — Dark Web et DARKINT : panorama opérationnel](06-partie-vi-corporate-infrastructure-et-donnees-expo/09-chapitre-44-dark-web-et-darkint-panorama-operation.md)
- [PARTIE VII — IMINT, GEOINT et transport](07-partie-vii-imint-geoint-et-transport/index.md)
    - [Chapitre 45 — IMINT : analyse d'image](07-partie-vii-imint-geoint-et-transport/01-chapitre-45-imint-analyse-d-image.md)
    - [Chapitre 46 — Recherche inversée et indexation visuelle](07-partie-vii-imint-geoint-et-transport/02-chapitre-46-recherche-inversee-et-indexation-visue.md)
    - [Chapitre 47 — Analyse technique d'image](07-partie-vii-imint-geoint-et-transport/03-chapitre-47-analyse-technique-d-image.md)
    - [Chapitre 48 — GEOINT : géolocaliser un contenu](07-partie-vii-imint-geoint-et-transport/04-chapitre-48-geoint-geolocaliser-un-contenu.md)
    - [Chapitre 49 — Chronolocation](07-partie-vii-imint-geoint-et-transport/05-chapitre-49-chronolocation.md)
    - [Chapitre 50 — OSINT spatial et imagerie satellite](07-partie-vii-imint-geoint-et-transport/06-chapitre-50-osint-spatial-et-imagerie-satellite.md)
    - [Chapitre 51 — GEOINT assisté par IA](07-partie-vii-imint-geoint-et-transport/07-chapitre-51-geoint-assiste-par-ia.md)
    - [Chapitre 52 — OSINT maritime, aérien et transport](07-partie-vii-imint-geoint-et-transport/08-chapitre-52-osint-maritime-aerien-et-transport.md)
- [PARTIE VIII — Vérification, deepfakes et provenance](08-partie-viii-verification-deepfakes-et-provenance/index.md)
    - [Chapitre 53 — Contenus synthétiques : image, vidéo, audio, texte](08-partie-viii-verification-deepfakes-et-provenance/01-chapitre-53-contenus-synthetiques-image-video-audi.md)
    - [Chapitre 54 — Signaux faibles de manipulation](08-partie-viii-verification-deepfakes-et-provenance/02-chapitre-54-signaux-faibles-de-manipulation.md)
    - [Chapitre 55 — C2PA, Content Credentials et provenance](08-partie-viii-verification-deepfakes-et-provenance/03-chapitre-55-c2pa-content-credentials-et-provenance.md)
    - [Chapitre 56 — Watermarking, SynthID et détection IA](08-partie-viii-verification-deepfakes-et-provenance/04-chapitre-56-watermarking-synthid-et-detection-ia.md)
    - [Chapitre 57 — Méthodologie de vérification intégrée](08-partie-viii-verification-deepfakes-et-provenance/05-chapitre-57-methodologie-de-verification-integree.md)
    - [Chapitre 58 — Fact-checking et OSINT](08-partie-viii-verification-deepfakes-et-provenance/06-chapitre-58-fact-checking-et-osint.md)
    - [Chapitre 59 — Preuve OSINT dans un monde post-deepfake](08-partie-viii-verification-deepfakes-et-provenance/07-chapitre-59-preuve-osint-dans-un-monde-post-deepfa.md)
- [PARTIE IX — IA, agents et automatisation](09-partie-ix-ia-agents-et-automatisation/index.md)
    - [Chapitre 60 — IA et OSINT : rupture ou accélérateur ?](09-partie-ix-ia-agents-et-automatisation/01-chapitre-60-ia-et-osint-rupture-ou-accelerateur.md)
    - [Chapitre 61 — LLMs comme assistants OSINT](09-partie-ix-ia-agents-et-automatisation/02-chapitre-61-llms-comme-assistants-osint.md)
    - [Chapitre 62 — Prompting OSINT et patterns utiles](09-partie-ix-ia-agents-et-automatisation/03-chapitre-62-prompting-osint-et-patterns-utiles.md)
    - [Chapitre 63 — Protocole Retrieve-Store-Cite](09-partie-ix-ia-agents-et-automatisation/04-chapitre-63-protocole-retrieve-store-cite.md)
    - [Chapitre 64 — Hallucinations, biais et erreurs IA](09-partie-ix-ia-agents-et-automatisation/05-chapitre-64-hallucinations-biais-et-erreurs-ia.md)
    - [Chapitre 65 — LLMs locaux et OPSEC](09-partie-ix-ia-agents-et-automatisation/06-chapitre-65-llms-locaux-et-opsec.md)
    - [Chapitre 66 — Knowledge graphs locaux](09-partie-ix-ia-agents-et-automatisation/07-chapitre-66-knowledge-graphs-locaux.md)
    - [Chapitre 67 — Agents autonomes et workflows multi-agents](09-partie-ix-ia-agents-et-automatisation/08-chapitre-67-agents-autonomes-et-workflows-multi-ag.md)
    - [Chapitre 68 — Automatisation conforme](09-partie-ix-ia-agents-et-automatisation/09-chapitre-68-automatisation-conforme.md)
    - [Chapitre 69 — Pipelines OSINT reproductibles](09-partie-ix-ia-agents-et-automatisation/10-chapitre-69-pipelines-osint-reproductibles.md)
- [PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence](10-partie-x-passerelles-specialisees-finint-crypto-ct/index.md)
    - [Chapitre 70 — OSINT financier et patrimonial](10-partie-x-passerelles-specialisees-finint-crypto-ct/01-chapitre-70-osint-financier-et-patrimonial.md)
    - [Chapitre 71 — Sanctions, PEP, KYC/KYB et adverse media](10-partie-x-passerelles-specialisees-finint-crypto-ct/02-chapitre-71-sanctions-pep-kyc-kyb-et-adverse-media.md)
    - [Chapitre 72 — Crypto-actifs et blockchain : panorama OSINT](10-partie-x-passerelles-specialisees-finint-crypto-ct/03-chapitre-72-crypto-actifs-et-blockchain-panorama-o.md)
    - [Chapitre 73 — Workflow intégré personne / société / finance / crypto](10-partie-x-passerelles-specialisees-finint-crypto-ct/04-chapitre-73-workflow-integre-personne-societe-fina.md)
    - [Chapitre 74 — OSINT pour Cyber Threat Intelligence](10-partie-x-passerelles-specialisees-finint-crypto-ct/05-chapitre-74-osint-pour-cyber-threat-intelligence.md)
    - [Chapitre 75 — Surface d'attaque et exposition cyber](10-partie-x-passerelles-specialisees-finint-crypto-ct/06-chapitre-75-surface-d-attaque-et-exposition-cyber.md)
    - [Chapitre 76 — Désinformation, influence et guerre cognitive](10-partie-x-passerelles-specialisees-finint-crypto-ct/07-chapitre-76-desinformation-influence-et-guerre-cog.md)
    - [Chapitre 77 — Renseignement économique et due diligence](10-partie-x-passerelles-specialisees-finint-crypto-ct/08-chapitre-77-renseignement-economique-et-due-dilige.md)
- [PARTIE XI — Analyse structurée, cotation et raisonnement](11-partie-xi-analyse-structuree-cotation-et-raisonnem/index.md)
    - [Chapitre 78 — Transformer la collecte en renseignement](11-partie-xi-analyse-structuree-cotation-et-raisonnem/01-chapitre-78-transformer-la-collecte-en-renseigneme.md)
    - [Chapitre 79 — ACH : Analysis of Competing Hypotheses](11-partie-xi-analyse-structuree-cotation-et-raisonnem/02-chapitre-79-ach-analysis-of-competing-hypotheses.md)
    - [Chapitre 80 — Biais cognitifs](11-partie-xi-analyse-structuree-cotation-et-raisonnem/03-chapitre-80-biais-cognitifs.md)
    - [Chapitre 81 — Raisonnement adversaire](11-partie-xi-analyse-structuree-cotation-et-raisonnem/04-chapitre-81-raisonnement-adversaire.md)
    - [Chapitre 82 — Entity resolution](11-partie-xi-analyse-structuree-cotation-et-raisonnem/05-chapitre-82-entity-resolution.md)
    - [Chapitre 83 — Timeline et graphe d'enquête](11-partie-xi-analyse-structuree-cotation-et-raisonnem/06-chapitre-83-timeline-et-graphe-d-enquete.md)
    - [Chapitre 84 — Cotation source / information (Admiralty)](11-partie-xi-analyse-structuree-cotation-et-raisonnem/07-chapitre-84-cotation-source-information-admiralty.md)
    - [Chapitre 85 — Niveaux de confiance WEP](11-partie-xi-analyse-structuree-cotation-et-raisonnem/08-chapitre-85-niveaux-de-confiance-wep.md)
    - [Chapitre 86 — Formulation analytique](11-partie-xi-analyse-structuree-cotation-et-raisonnem/09-chapitre-86-formulation-analytique.md)
- [PARTIE XII — Production, transmission et cas pratiques](12-partie-xii-production-transmission-et-cas-pratique/index.md)
    - [Chapitre 87 — Note courte OSINT](12-partie-xii-production-transmission-et-cas-pratique/01-chapitre-87-note-courte-osint.md)
    - [Chapitre 88 — Rapport OSINT complet](12-partie-xii-production-transmission-et-cas-pratique/02-chapitre-88-rapport-osint-complet.md)
    - [Chapitre 89 — Fiches opérationnelles](12-partie-xii-production-transmission-et-cas-pratique/03-chapitre-89-fiches-operationnelles.md)
    - [Chapitre 90 — Rapport judiciaire et précontentieux](12-partie-xii-production-transmission-et-cas-pratique/04-chapitre-90-rapport-judiciaire-et-precontentieux.md)
    - [Chapitre 91 — Diffusion, confidentialité et TLP](12-partie-xii-production-transmission-et-cas-pratique/05-chapitre-91-diffusion-confidentialite-et-tlp.md)
    - [Chapitre 92 — Veille post-rapport et capitalisation](12-partie-xii-production-transmission-et-cas-pratique/06-chapitre-92-veille-post-rapport-et-capitalisation.md)
    - [Chapitre 93 — Cas complet : synthèse MIRAGE](12-partie-xii-production-transmission-et-cas-pratique/07-chapitre-93-cas-complet-synthese-mirage.md)
    - [Chapitre 94 — Cas pratique : GEOINT sur vidéo virale](12-partie-xii-production-transmission-et-cas-pratique/08-chapitre-94-cas-pratique-geoint-sur-video-virale.md)
    - [Chapitre 95 — Cas pratique : dé-anonymisation d'un pseudonyme](12-partie-xii-production-transmission-et-cas-pratique/09-chapitre-95-cas-pratique-de-anonymisation-d-un-pse.md)
    - [Chapitre 96 — Cas pratique : désinformation et faux comptes IA](12-partie-xii-production-transmission-et-cas-pratique/10-chapitre-96-cas-pratique-desinformation-et-faux-co.md)
    - [Chapitre 97 — Cas pratique : société opaque](12-partie-xii-production-transmission-et-cas-pratique/11-chapitre-97-cas-pratique-societe-opaque.md)
    - [Chapitre 98 — Cas pratique : fuite de données](12-partie-xii-production-transmission-et-cas-pratique/12-chapitre-98-cas-pratique-fuite-de-donnees.md)
    - [Chapitre 99 — Cas pratique : OPSEC défensive sur Telegram](12-partie-xii-production-transmission-et-cas-pratique/13-chapitre-99-cas-pratique-opsec-defensive-sur-teleg.md)
    - [Chapitre 100 — Cas pratique : CTI infrastructure suspecte](12-partie-xii-production-transmission-et-cas-pratique/14-chapitre-100-cas-pratique-cti-infrastructure-suspe.md)
    - [Chapitre 101 — Cas pratique : triage financier / crypto](12-partie-xii-production-transmission-et-cas-pratique/15-chapitre-101-cas-pratique-triage-financier-crypto.md)
    - [Chapitre 102 — Exercice final non guidé](12-partie-xii-production-transmission-et-cas-pratique/16-chapitre-102-exercice-final-non-guide.md)
    - [Chapitre 103 — Corrigé détaillé de l'exercice final](12-partie-xii-production-transmission-et-cas-pratique/17-chapitre-103-corrige-detaille-de-l-exercice-final.md)
- [Annexes](13-annexes/index.md)
    - [ANNEXE A — Glossaire OSINT 2026](13-annexes/01-annexe-a-glossaire-osint-2026.md)
    - [ANNEXE B — Dorks et opérateurs multi-moteurs](13-annexes/02-annexe-b-dorks-et-operateurs-multi-moteurs.md)
    - [B.1 — Dorks Google](13-annexes/03-b-1-dorks-google.md)
    - [ANNEXE C — Atlas plateformes, registres et sources par pays](13-annexes/04-annexe-c-atlas-plateformes-registres-et-sources-pa.md)
    - [C.1 — France](13-annexes/05-c-1-france.md)
    - [C.4 — Union Européenne (États membres principaux)](13-annexes/06-c-4-union-europeenne-etats-membres-principaux.md)
    - [ANNEXE E — Catalogue d'outils OSINT par usage](13-annexes/07-annexe-e-catalogue-d-outils-osint-par-usage.md)
    - [E.8 — IMINT et GEOINT](13-annexes/08-e-8-imint-et-geoint.md)
    - [E.14 — Outils à risque obsolescence Très Élevé (vigilance)](13-annexes/09-e-14-outils-a-risque-obsolescence-tres-eleve-vigil.md)
    - [G.3 — Exemple d'entrée de journal MIRAGE](13-annexes/10-g-3-exemple-d-entree-de-journal-mirage.md)
    - [H.1 — Template fiche personne physique](13-annexes/11-h-1-template-fiche-personne-physique.md)
    - [H.2 — Template fiche société](13-annexes/12-h-2-template-fiche-societe.md)
