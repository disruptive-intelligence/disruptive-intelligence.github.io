---
title: PARTIE III — Méthodologie d'enquête et gestion du dossier
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 4
chapters: 15
---

> **Ce que cette partie apprend.** Conduire une enquête OSINT du cadrage initial à la structuration du dossier, en passant par la formulation des questions de renseignement, la logique de pivot par sélecteurs, la tenue du journal d'enquête, la chaîne de conservation numérique, et l'organisation du lab.
>
> **Ce qu'elle ne couvre pas.** Les techniques de collecte par source (Parties IV à VII), l'analyse (Partie XI), la production (Partie XII).
>
> **Ce que vous saurez faire après cette partie.** Cadrer rigoureusement une mission, formuler des questions de renseignement, identifier et exploiter les sélecteurs, pivoter sans dérive, tenir un journal défendable, préserver les preuves selon les standards, structurer un dossier d'enquête, monter votre lab.

-----

### Chapitre 12 — Cadrer une mission OSINT

#### 12.1 La phase la plus négligée et la plus déterminante

Le cadrage est la phase d'orientation du cycle du renseignement (Ch.5) appliquée à une mission concrète. C'est la phase **la plus négligée** par les analystes pressés ou peu structurés, et **la plus déterminante** pour la qualité du livrable final. Une mission mal cadrée produit un rapport vague qui ne sert ni le commanditaire ni l'analyste. Une mission bien cadrée se déroule sans dérive et produit un livrable utile.

Le cadrage répond à sept questions structurantes.

#### 12.2 Qui demande ?

Identifier précisément le **commanditaire réel**. Ce n'est pas toujours évident.

**Cas typiques.**
- Un cabinet d'avocats mandate au nom d'un client final. Qui est le client final ? A-t-on accès à lui ? Y a-t-il des restrictions de communication ?
- Une direction interne d'entreprise mandate. Quelle direction (juridique, sécurité, RH, conformité, audit) ? Avec quelle légitimité interne ?
- Un journaliste sollicite pour une enquête. Quel média ? Quelle rédaction valide la publication ?
- Un particulier sollicite (cas à examiner avec prudence).

Connaître le commanditaire réel permet d'évaluer la légitimité, d'anticiper les enjeux, de calibrer le livrable.

#### 12.3 Pourquoi ?

La **motivation** du commanditaire détermine la finalité de l'enquête.

**Motivations légitimes typiques.**
- Préparation d'un contentieux.
- Due diligence pré-transaction.
- Vérification de partenaire commercial.
- Investigation de fraude interne.
- Protection contre une menace identifiée.
- Vérification de réputation pré-recrutement (cadre encadré).
- Enquête journalistique d'intérêt public.

**Motivations problématiques (signaux d'alerte).**
- « Je veux savoir ce qu'il fait » (vague, possible stalking).
- « Mon ex-conjoint(e) » (très haute probabilité de stalking).
- « Pour faire pression sur lui » (instrumentalisation possible).
- « Pour le faire renoncer » (chantage potentiel).
- « Pour le punir » (vengeance).
- Refus de répondre clairement.

Une motivation problématique = refus du mandat. Pas de « zone grise », pas de « si j'aide cette fois ». Le métier en dépend.

#### 12.4 Sur qui ? (la cible)

La **cible** est définie précisément : personne physique, personne morale, événement, contenu, réseau ?

**Personne physique.** Nom, date de naissance (au moins année), juridiction de résidence, contexte professionnel. Plus la cible est précise, moins on risque l'homonymie (Ch.26).

**Personne morale.** Raison sociale, juridiction, numéro d'enregistrement (SIREN, registration number), forme juridique, activité.

**Événement.** Date, lieu, nature. Une vidéo, une publication, un incident.

**Contenu.** URL, hash, source, contexte de découverte.

**Réseau.** Groupe d'entités liées (réseau d'influence, cluster crypto, écosystème criminel). Plus complexe à cadrer, demande explicitation des limites.

#### 12.5 Pour quoi ? (la décision attendue)

Quelle **décision** le commanditaire prendra-t-il sur la base du livrable ?

- Décider de déposer plainte / saisir une autorité.
- Décider d'entrer en transaction / la suspendre.
- Décider de licencier / d'engager.
- Décider de publier un article / le retenir.
- Décider d'engager une action de protection.
- Décider d'investir / s'abstenir.

Connaître la décision conditionne la **forme** du livrable, son **niveau de preuve requis**, et son **délai**.

#### 12.6 Quel périmètre ?

Le **périmètre** définit ce qui entre et ce qui sort de l'enquête.

**Dimensions du périmètre.**
- **Temporel** : sur quelle période ? Faits depuis 2020 ? Depuis la création de la société ? Depuis un événement déclencheur ?
- **Géographique** : quelle juridiction ? France uniquement ? UE ? International ?
- **Thématique** : volet financier seulement ? Volet personnel ? Volet désinformation ?
- **Profondeur** : analyse de surface ou enquête approfondie ?
- **Exclusions** : qu'est-ce qu'on ne touche **pas** explicitement (vie privée familiale, mineurs, certaines juridictions sensibles) ?

Un périmètre flou = dérive d'enquête garantie. Un périmètre trop large = épuisement budget sans livrable.

#### 12.7 Quelles limites ?

Au-delà du périmètre, des **limites** explicites sont définies.

**Limites typiques.**
- **Légales** : pas d'accès non autorisé, pas d'interaction avec mineurs, pas de juridictions interdites.
- **Éthiques** : pas de doxxing, pas de surveillance famille.
- **Méthodologiques** : pas de bases payantes au-delà d'un seuil, pas d'outils non auditables.
- **Opérationnelles** : aucune interaction avec la cible (cas MIRAGE).
- **Confidentialité** : aucune communication externe avant livraison.

Les limites sont **écrites** dans le mandat. Elles protègent l'analyste autant que le commanditaire.

#### 12.8 Quel livrable, quel délai, quel budget ?

**Livrable.** Note flash 2 pages ? Rapport complet 30 pages ? Rapport judiciaire versable au dossier ? Présentation orale ? Fiches entité ? Graphe ?

**Délai.** Calé sur la décision attendue. Un cadrage précoce permet d'évaluer si le délai est réaliste.

**Budget.** Définit l'envergure : nombre de jours-homme, accès à des outils payants, déplacement éventuel, partenariats nécessaires.

Si le triangle « livrable / délai / budget » est incohérent (livrable ambitieux, délai court, budget faible), c'est dit dès le cadrage. Mieux vaut renégocier que livrer un travail bâclé.

#### 12.9 Document de cadrage : le SOR

Le **SOR** (Statement of Requirements, ou cahier des charges OSINT) formalise le cadrage. C'est un document court (2-3 pages) qui sert de contrat opérationnel entre l'analyste et le commanditaire.

**Sections du SOR.**
1. Contexte de la demande (court).
2. Commanditaire et destinataires.
3. Objectifs de l'enquête (questions de renseignement principales).
4. Cible(s).
5. Périmètre temporel, géographique, thématique.
6. Limites légales, éthiques, opérationnelles.
7. Livrables attendus (type, niveau de preuve).
8. Délai et jalons.
9. Budget et ressources.
10. Confidentialité, classification, diffusion.
11. Validation (signature du commanditaire).

Un SOR signé est la pierre angulaire d'une mission propre.

> **MIRAGE — Épisode 0 : Cadrage du mandat**
>
> Vendredi 16 mai 2026, 14h. Réunion dans les bureaux du cabinet Legrand & Associés, 6e arrondissement de Paris. Me Patricia Legrand expose le mandat : son client, actionnaire minoritaire (12 %) de TechnoVert SAS, soupçonne Marc Delaunay, DAF, de cinq agissements (détournement, blanchiment crypto, désinformation contre lanceur d'alerte, faux comptes coordonnés, deepfakes). Le client envisage un dépôt de plainte au PNF.
>
> L'analyste pose les questions de cadrage : qui est le commanditaire réel (Me Legrand, mandatée par l'actionnaire qui ne sera pas directement en contact) ; quelle décision (dépôt de plainte) ; quel périmètre (Delaunay, ses sociétés, ses flux visibles, son écosystème ; pas la famille, pas les mineurs ; France et juridictions où il opère manifestement, soit Malte, Chypre, BVI, Luxembourg, Maroc selon premières indications) ; quel livrable (rapport complet versable au dossier judiciaire, 30-50 pages) ; quel délai (6 semaines) ; quel budget (raisonnable, sans bases premium).
>
> Trois limites explicites sont posées : aucune interaction avec Delaunay (techniquement compétent), aucun accès non autorisé, aucune méthode susceptible de compromettre la procédure pénale ultérieure. Le SOR est signé en début de semaine suivante. L'enquête peut démarrer.

#### 12.10 Réflexes du cadrage

- Toujours reformuler la demande du commanditaire.
- Toujours écrire le SOR.
- Toujours signer le SOR avant collecte.
- Toujours évaluer la triangulation livrable/délai/budget.
- Toujours détecter les signaux d'alerte sur la motivation.
- Toujours documenter les exclusions.
- Toujours prévoir un point de revue à mi-parcours.

-----

### Chapitre 13 — Questions de renseignement et plan de collecte

#### 13.1 Du cadrage aux questions opérationnelles

Le cadrage produit des objectifs généraux. La phase suivante transforme ces objectifs en **questions de renseignement** précises, qui guideront la collecte.

Une question de renseignement (Intelligence Requirement, IR) est :
- **Fermée** : elle admet une réponse délimitée (oui/non, valeur, identifiant, liste).
- **Vérifiable** : on peut tester si la réponse trouvée est correcte.
- **Reformulable en hypothèse** : on peut imaginer une réponse alternative.
- **Pertinente** : sa réponse contribue à la décision attendue.

#### 13.2 IR principales et IR secondaires

On distingue deux niveaux.

**IR principales** (3-5 maximum) : les questions critiques qui structurent l'enquête et conditionnent la décision finale.

**IR secondaires** (5-15 selon enquête) : les sous-questions qui alimentent les IR principales et organisent le travail tactique.

**Exemple sur MIRAGE.**

*IR principales.*
- IR1 : Marc Delaunay détient-il, contrôle-t-il ou bénéficie-t-il de sociétés offshore non déclarées ?
- IR2 : Existe-t-il des flux financiers visibles entre TechnoVert et ces sociétés ?
- IR3 : Delaunay possède-t-il des actifs (immobilier, crypto) incohérents avec ses revenus déclarés ?
- IR4 : Une campagne de désinformation contre Antoine Berthier est-elle organisée, et si oui, peut-elle être attribuée à Delaunay ou à son entourage ?
- IR5 : Des contenus synthétiques (deepfakes, photos IA) ont-ils été produits dans le cadre de cette campagne ?

*IR secondaires (extrait).*
- IR1a : Quelles sociétés offshore identifiables sont liées à Delaunay ?
- IR1b : Quels sont les UBO réels de ces sociétés ?
- IR1c : Y a-t-il des nominees, des prête-noms identifiables ?
- IR2a : Quels prestataires de TechnoVert reçoivent des paiements visibles vers ces sociétés ?
- IR2b : Existe-t-il des contrats publiés (annonces légales) entre TechnoVert et ces entités ?
- IR4a : Quels sont les comptes coordonnés diffusant des contenus diffamatoires ?
- IR4b : Existe-t-il un narratif central et une infrastructure (domaine, hébergement, créateurs) ?
- (etc.)

#### 13.3 Formulation des IR : pièges à éviter

**Question trop large.** « Que peut-on dire sur Delaunay ? » → reformuler en sous-questions précises.

**Question fermée sans réponse possible.** « Delaunay a-t-il volé ? » → c'est une qualification pénale qui ne se prouve pas en OSINT.

**Question chargée.** « Comment Delaunay blanchit-il son argent ? » → présuppose la conclusion.

**Question sans lien à la décision.** « Combien a-t-il d'enfants ? » → si non pertinent pour la décision, à exclure.

**Reformulation correcte.** « Marc Delaunay détient-il, contrôle-t-il, ou bénéficie-t-il de sociétés non déclarées hors de France ? » → fermée, vérifiable, neutre, pertinente.

#### 13.4 Hypothèses initiales

À chaque IR, on associe une ou plusieurs **hypothèses concurrentes** (méthode ACH — Ch.79). Cela structure la collecte autour de la **réfutation** plutôt que de la confirmation.

**Exemple IR1.**
- H1 : Delaunay détient personnellement plusieurs sociétés offshore.
- H2 : Delaunay est administrateur nominee, contrôlé par un tiers (vrai bénéficiaire ailleurs).
- H3 : Delaunay n'a aucun lien avec des sociétés offshore — soupçon infondé.

La collecte va chercher des éléments **pour ET contre** chaque hypothèse. C'est la garantie anti-biais.

#### 13.5 Sources prioritaires par IR

À chaque IR, on associe les **sources prioritaires** où chercher la réponse.

**Tableau type.**

| IR | Hypothèse | Sources prioritaires |
|---|---|---|
| IR1 (offshores) | H1, H2, H3 | OpenCorporates, ICIJ Offshore Leaks, Pappers (volet français), Companies House (UK), Companies Registry (Malte, Chypre), BORIS |
| IR2 (flux) | (idem) | BODACC, annonces légales, presse économique, comptes consolidés AMF, Cyprus Confidential si applicable |
| IR3 (actifs) | (idem) | Cadastre, Pages Jaunes, presse locale, réseaux sociaux, registres maritime/aérien selon indices |
| IR4 (désinfo) | (idem) | X, Telegram, archive.today, WHOIS du domaine `verites-technovert.com`, hostnames cluster, EU DisinfoLab méthodologie |
| IR5 (deepfakes) | (idem) | Hive Moderation, Sensity AI, C2PA inspector, analyses image classiques (FotoForensics, ELA) |

Ce tableau est l'embryon du **plan de collecte**.

#### 13.6 Plan de collecte

Le plan de collecte organise concrètement :
- Quelles IR sont travaillées en parallèle, lesquelles en séquence.
- Quels sélecteurs initiaux ouvrent la collecte (Ch.14).
- Quelle priorité (IR1 critique pour la décision, IR3 secondaire).
- Quels jalons (point à J+15, point à J+30).
- Quels arbitrages si une source-clé est inaccessible.

Pour une enquête de 6 semaines comme MIRAGE, le plan type :
- **Semaine 1** : OPSEC, sock puppets si nécessaire, recherche large sur Delaunay (personne + société), premier graphe.
- **Semaine 2** : Approfondissement corporate (sociétés offshore, UBO), pivot via WHOIS.
- **Semaine 3** : Volet financier visible, flux, ICIJ leaks, registres.
- **Semaine 4** : Volet désinformation (faux comptes, blog, faux médias), volet IA (deepfakes).
- **Semaine 5** : Volet crypto (triage OSINT, renvoi vers spécialiste si nécessaire), patrimoine immobilier.
- **Semaine 6** : Vérification, ACH, rédaction, revue, livraison.

Le plan reste **adaptatif**. Une découverte précoce peut réorienter. Mais avoir un plan évite la dérive.

#### 13.7 Critères d'arrêt

Quand s'arrête-t-on de chercher ?

**Critères positifs.**
- Toutes les IR ont une réponse cotée.
- Le seuil de confiance pour la décision est atteint.
- Le budget est consommé.
- Le délai est consommé.

**Critères négatifs (rebond).**
- Une IR centrale reste sans réponse → escalade ou décision sur la limite à présenter.
- Une découverte ouvre un volet nouveau (élargissement du périmètre à valider avec commanditaire).
- Une source-clé inaccessible compromet la mission (renégociation).

L'analyste qui ne sait pas s'arrêter dérive vers la collecte infinie. La discipline d'arrêt est aussi importante que la discipline de pivot.

> **MIRAGE — Épisode 1 : Questions de renseignement**
>
> Lundi 19 mai 2026. L'analyste tient une séance de cadrage IR avec Me Legrand. Cinq IR principales sont formalisées (supra), avec 18 IR secondaires. Pour chaque IR, deux à trois hypothèses concurrentes sont posées. Le plan de collecte est calé sur 6 semaines avec jalons à J+15 (revue avec Me Legrand) et J+30 (point d'étape).
>
> L'analyste insiste sur un point : la décision est un dépôt de plainte. Le seuil de preuve attendu est donc « faisceau d'indices convergents suffisant pour saisir le PNF », pas une « preuve au sens pénal ». Cette clarification calibre l'effort : on ne cherche pas l'irréfutable, on cherche un dossier soutenable.

-----

### Chapitre 14 — Sélecteurs OSINT et logique de pivot

#### 14.1 Définition du sélecteur

Un **sélecteur** est un élément d'information qui sert de **point d'entrée** ou de **point de pivot** dans une enquête. Le sélecteur permet d'interroger des sources, d'obtenir des résultats, et de découvrir d'autres sélecteurs.

L'enquête OSINT progresse par **pivots successifs** : on part d'un sélecteur initial, on l'interroge dans une source, on obtient un résultat qui contient un nouveau sélecteur, on pivote sur ce nouveau sélecteur dans une autre source, etc. La trajectoire forme un graphe d'exploration.

#### 14.2 Les 14 sélecteurs canoniques

Quatorze sélecteurs sont opérationnels en OSINT moderne. Les six premiers sont les sélecteurs primaires que tout analyste maîtrise. Les huit suivants sont des sélecteurs avancés selon les contextes.

**Sélecteurs primaires.**

1. **Nom complet.** Sélecteur évident, mais imprécis en raison des homonymies. À enrichir systématiquement (date de naissance, lieu, profession).
2. **Email.** Sélecteur puissant : utilisé partout, peu réutilisé, traçable à travers leaks, registres WHOIS, plateformes.
3. **Username (pseudonyme).** Très puissant car les utilisateurs réutilisent souvent le même username sur plusieurs plateformes.
4. **Téléphone.** Sélecteur d'identification fort (lié à SIM, opérateur). Utilisé sur Telegram, WhatsApp, Signal pour le découvrir.
5. **Photo (visage, image).** Recherche inversée (Yandex, Google Lens, TinEye), reconnaissance faciale (PimEyes, FaceCheck).
6. **Adresse postale.** Cadastre, annuaires, registres fonciers, sociétés domiciliées.

**Sélecteurs avancés.**

7. **Domaine et sous-domaine.** WHOIS, DNS, certificats, hébergement.
8. **Adresse IP.** Géolocalisation, ASN, services exposés, historique.
9. **Wallet crypto (adresse blockchain).** Explorateurs, clustering, attributions partielles *(renvoi → OSINT Crypto vFULL)*.
10. **Document (PDF, image avec métadonnées).** EXIF, propriétés Office, traces de création.
11. **Organisation (raison sociale, numéro d'enregistrement).** Registres corporate.
12. **Événement (date, lieu, type).** Sources presse, archives, médias sociaux.
13. **Véhicule (immatriculation, VIN).** Limité légalement, certains pays autorisent ; aérien et maritime (registres ADS-B, AIS) sont plus accessibles.
14. **Lieu (coordonnées GPS, point d'intérêt).** Cartographie, imagerie, données géolocalisées.

#### 14.3 Sélecteurs forts versus sélecteurs faibles

Tous les sélecteurs n'ont pas la même puissance discriminante.

**Sélecteurs forts.** Identification quasi-unique. Email (sauf en cas de partage rare), téléphone, IP avec timestamp précis, wallet crypto.

**Sélecteurs faibles.** Polysémie possible. Nom commun (Jean Dupont), photo de visage standard (jumeau), prénom seul.

**Implication.** Un pivot sur sélecteur fort = grande confiance. Un pivot sur sélecteur faible = à corroborer immédiatement.

#### 14.4 Logique de pivot : la mécanique

Le pivot est l'opération centrale de l'OSINT.

**Schéma.**
1. Sélecteur initial S1 (ex : email `m.delaunay@technovert.fr`).
2. Interrogation source X1 (ex : WHOIS lookups).
3. Résultat contenant nouveau sélecteur S2 (ex : domaine `delta-consulting.eu` enregistré avec cet email).
4. Interrogation source X2 sur S2 (ex : registre maltais).
5. Résultat → S3 (ex : nom de société Delta Consulting Ltd, numéro d'enregistrement, administrateur).
6. Interrogation source X3 sur S3 (ex : OpenCorporates pour réseau d'administrations connexes).
7. Etc.

Chaque pivot est **documenté** dans le journal d'enquête (Ch.15). La traçabilité du pivot est ce qui rend l'enquête défendable.

#### 14.5 Pivots fréquents

Quelques pivots emblématiques.

- **Email → WHOIS** : un domaine peut être enregistré avec un email personnel.
- **Email → leaks (HIBP, DeHashed)** : exposition dans des fuites.
- **Email → Hunter / Epieos** : confirmation d'existence, plateformes liées.
- **Username → Sherlock / WhatsMyName / Maigret** : présence cross-plateforme.
- **Photo → Yandex Images / PimEyes** : autres apparitions en ligne.
- **Photo → métadonnées EXIF** : géolocalisation GPS, appareil utilisé.
- **Domaine → DNS / passive DNS / sous-domaines** : infrastructure complète.
- **Domaine → certificats (crt.sh)** : autres domaines liés via certificat.
- **Société → bénéficiaires (OpenCorporates, Pappers, RBE)** : structure d'UBO.
- **Société → adresse de domiciliation → autres sociétés domiciliées** : cluster d'entités.

#### 14.6 Discipline du pivot

L'erreur classique du débutant : pivoter au hasard, explorer toutes les directions, dériver sans direction.

**Réflexes.**
- Avant chaque pivot, se demander : **ceci m'apporte-t-il un nouveau sélecteur pertinent pour mes IR ?**
- Hiérarchiser les pivots par valeur attendue.
- Documenter chaque pivot dans le journal.
- Ne pas s'enfoncer dans des branches stériles plus de 30-60 minutes sans bilan.
- Faire un point de bilan tous les 2-3 heures pour évaluer la trajectoire.

> **MIRAGE — Épisode 2 : Sélecteurs initiaux**
>
> L'analyste recense les sélecteurs disponibles au démarrage : nom Marc Delaunay (sélecteur faible — au moins 23 homonymes identifiables en France), date de naissance approximative (1976-1977), poste (DAF TechnoVert SAS), email professionnel (`m.delaunay@technovert.fr`, sélecteur fort). C'est mince.
>
> Premier pivot : recherche Google sur `"Marc Delaunay" "TechnoVert"`. Résultat : trois communiqués de presse mentionnant le poste, un profil LinkedIn ouvert (Sales Navigator inutile, profil partiel), une interview vidéo sur YouTube datée de 2023. Pivot vers LinkedIn : confirmation du parcours (X-Ponts 1999, parcours en cabinet d'audit puis ETI), photo de profil, 4 abonnements à des comptes professionnels.
>
> Pivot sur l'email : Hunter.io confirme existence et déliverabilité. Pivot Holehe : présence détectée sur LinkedIn, WordPress, Adobe, Spotify, Apple. Pas de présence Telegram/Signal détectable depuis l'email pro (qui ne signifie pas absence — usage probable d'email perso pour ces plateformes).
>
> Recherche WHOIS large : l'email pro n'apparaît dans aucun WHOIS public en lookup direct (les registrars masquent par défaut). Bascule vers l'hypothèse : Delaunay utilise un email personnel pour ses opérations offshore, non encore identifié. Première recherche : username dérivé du nom (`mdelaunay`, `m.delaunay`, `marcdelaunay`, `delaunaymarc`) testé sur Sherlock. Hit sur Twitter sous `@mdelaunay76` (compte verrouillé), Instagram `mdelaunay76` (compte privé), GitHub `mdelaunay` (compte sans activité 2017-2019).
>
> Le 76 dans le username (peut-être lié à 1976, année de naissance) devient un sélecteur secondaire. Hypothèse : Delaunay utilise un username personnel récurrent. L'arbre de pivots commence à prendre forme. Trois pistes à explorer en parallèle dans les jours suivants : approfondissement username, recherche email personnel, exploration corporate à partir du parcours.

-----

### Chapitre 15 — Journal d'enquête, preuve et traçabilité

#### 15.1 Pourquoi tenir un journal

Le journal d'enquête est la **mémoire structurée** de l'investigation. Il n'est pas un journal au sens littéraire : c'est un registre opérationnel.

**Fonctions du journal.**
- **Reproductibilité** : un confrère doit pouvoir refaire votre cheminement.
- **Défense** : capacité à justifier chaque conclusion par les actions menées.
- **Auditabilité** : un magistrat, un contre-expert, un commanditaire peut vérifier la rigueur.
- **Mémoire personnelle** : 4 semaines après une enquête, vous ne vous souvenez plus du détail. Le journal sauve.
- **Cotation** : la cotation finale d'un fait dépend de la fiabilité de la source ET de la rigueur de la collecte. Le journal documente la seconde.

#### 15.2 Champs minimaux d'une entrée de journal

Chaque action significative produit une entrée de journal avec :

- **Date et heure** précises (timezone explicite).
- **Action menée** (description courte mais claire).
- **Source consultée** (URL ou nom de plateforme, version, paramètres de requête).
- **Sélecteur utilisé**.
- **Résultat** (texte court, ou référence à capture).
- **Capture / hash si applicable** (chemin de fichier dans le dossier d'enquête).
- **Pertinence** (haute / moyenne / faible / aucune).
- **Hypothèse(s) éclairée(s)** (référence à l'IR / l'hypothèse concernée).
- **Cotation préliminaire de la source** (Admiralty A-F).
- **Actions suivantes envisagées** (prochain pivot).

#### 15.3 Format pratique

Plusieurs formats sont possibles. Le choix dépend du volume et de la complexité.

**Format A — Markdown structuré (Obsidian).** Un fichier `journal.md` ou un fichier par jour. Tags Obsidian pour entités, IRs, hypothèses. Lié au vault d'enquête.

**Format B — Tableau (Google Sheets chiffré, ou Excel local).** Colonnes structurées. Idéal pour grosses enquêtes avec beaucoup d'actions. Filtrable.

**Format C — Outil dédié (Hunchly).** Hunchly capture automatiquement la navigation web avec horodatage et hash. Génère un rapport. Largement utilisé en OSINT professionnel.

**Format D — Notion (avec prudence OPSEC).** Pour les équipes. Attention au cloud — préférer self-hosted ou outil local pour les sujets sensibles.

#### 15.4 Hunchly comme standard

**Hunchly** est devenu le standard de fait pour le journal d'enquête OSINT.

**Fonctionnalités.**
- Capture automatique de chaque page consultée (timestamped + hashed).
- Surlignage de sélecteurs (notations).
- Export en rapport PDF avec captures, hashes, métadonnées.
- Annotations personnelles.
- Compatible Chrome/Firefox via extension.
- Local-first (les données restent chez vous).

**Coût.** Abonnement payant, mais investissement rentable pour usage professionnel.

**Alternatives gratuites.** SingleFile (extension navigateur, capture HTML complet), Wayback Machine pour les pages publiques, captures manuelles + script de hashing.

#### 15.5 Captures et préservation

Pour chaque page ou ressource d'intérêt :

**Capture.** PDF complet (Hunchly, ou impression PDF), HTML brut (SingleFile), capture image (Greenshot, ShareX, ou outils OS natifs). Le HTML brut permet une analyse ultérieure du code source ; le PDF est lisible directement.

**Horodatage.** Date et heure précises, en UTC ou avec timezone explicite.

**Hash.** SHA-256 du fichier de capture. Un hash garantit que le fichier n'a pas été modifié après collecte.

**Métadonnées contextuelles.** URL exacte, statut HTTP, redirections éventuelles, version du navigateur.

```bash
# Calcul SHA-256 sous Linux/Mac
sha256sum capture_001.pdf

# Sous Windows
certutil -hashfile capture_001.pdf SHA256
```

#### 15.6 Versioning du dossier

Le dossier d'enquête évolue. Le **versioning** permet de tracer l'historique.

**Solutions.**
- **Git** : avec un repo local chiffré. Idéal pour markdown / fichiers texte.
- **Snapshots VeraCrypt** : un conteneur chiffré snapshotté à dates clés.
- **Hunchly export** : génère un rapport horodaté à chaque export.

#### 15.7 Reproductibilité

L'enquête est **reproductible** quand un confrère, avec le même journal et les mêmes accès, aboutit aux mêmes conclusions.

**Conditions.**
- Sources documentées avec URL exacte.
- Requêtes documentées (mots-clés, opérateurs).
- Outils documentés avec version.
- Paramètres de configuration documentés.
- Cheminement de pivot reconstructible.

La reproductibilité est l'idéal. La réalité de l'OSINT en 2026 (plateformes qui ferment, archives qui disparaissent) la rend partiellement impossible. L'archivage anticipé (Ch.23) compense.

#### 15.8 Pièges classiques du journal

- **Tenue rétroactive** : « je remplis le journal le soir ». Fragmentation, oublis, ré-écritures partielles.
- **Imprécision** : « j'ai cherché sur Google ». Quels mots-clés ? Quelle date ?
- **Pas d'horodatage** : journal sans timestamp est inutilisable.
- **Pas de capture** : URL seule = preuve fragile si la page disparaît.
- **Mélange enquête et notes perso** : journal d'enquête est strictement professionnel.
- **Stockage non chiffré** : journal contient des données sensibles, doit être chiffré.
- **Pas de cotation** : sources non cotées = analyse plus tard impossible.

#### 15.9 Synthèse — le journal en cinq règles

1. **Toujours** tenir le journal en temps réel, pas rétroactivement.
2. **Toujours** horodater chaque entrée (avec timezone).
3. **Toujours** capturer (Hunchly, SingleFile, PDF) ce qui compte.
4. **Toujours** hasher les captures (SHA-256).
5. **Toujours** chiffrer le journal (VeraCrypt, LUKS, FileVault).

Un journal négligé est une enquête fragile. Un journal rigoureux est une enquête défendable.

-----

### Chapitre 16 — Chaîne de conservation numérique

#### 16.1 Du journal à la chain of custody

Le journal d'enquête trace les actions de l'analyste. La **chaîne de conservation** (chain of custody) trace les **éléments de preuve eux-mêmes** : leur origine, leur traitement, leur conservation, leur transmission. C'est un concept emprunté à la criminalistique judiciaire, adapté aux preuves numériques.

L'objectif : garantir qu'**un élément présenté en preuve est bien celui qui a été collecté à l'origine**, sans altération, sans substitution, sans contamination. Cette garantie est ce qui rend l'élément opposable.

#### 16.2 Quatre piliers de la chaîne de conservation

**Intégrité.** L'élément n'a pas été modifié depuis sa collecte. Garantie par le hash cryptographique.

**Origine.** L'élément vient d'une source identifiée, traçable. Garantie par la documentation de la collecte (URL, date, méthode).

**Conservation.** L'élément est stocké de manière sécurisée, sans risque d'altération accidentelle ou malveillante. Garantie par chiffrement, sauvegarde, accès restreint.

**Transmission.** Si l'élément est transmis (à un client, un avocat, un magistrat), la transmission est tracée et l'intégrité préservée. Garantie par canal sécurisé et vérification du hash à réception.

#### 16.3 Hash SHA-256 : la signature de l'intégrité

Le **hash cryptographique** est la signature mathématique d'un fichier. Un changement d'un seul bit produit un hash totalement différent. SHA-256 est le standard contemporain (SHA-1 et MD5 sont obsolètes pour usage forensique).

**Pratique.**

```bash
# Hash d'un fichier
sha256sum capture_delaunay_linkedin_20260520.pdf
# Sortie : a3f5b...e9c (64 caractères hex)

# Hash récursif d'un dossier (Linux)
find dossier_enquete/ -type f -exec sha256sum {} \; > hashes.txt

# Vérification ultérieure
sha256sum -c hashes.txt
```

Chaque capture importante a son hash, consigné dans le journal. Le hash est conservé séparément du fichier (idéalement signé numériquement ou conservé sur un media différent).

#### 16.4 Horodatage et timestamp

L'horodatage prouve **quand** l'élément a été collecté.

**Niveaux d'horodatage.**

**Horodatage simple.** Date et heure consignées dans le journal. Suffisant pour l'enquête interne, mais auto-déclaratif (l'analyste peut, théoriquement, ré-écrire son journal).

**Horodatage matériel** (timestamping qualifié). Un tiers de confiance horodate la donnée. Services européens conformes eIDAS : Universign, DocuSign, certaines API gratuites. Le hash + horodatage est signé par le tiers de confiance et opposable.

**Horodatage blockchain.** Certaines solutions ancrent le hash dans une blockchain publique (OpenTimestamps via Bitcoin), créant un timestamp impossible à falsifier rétroactivement. Pour les enquêtes à fort enjeu judiciaire.

**Pour le journalisme et l'enquête privée.** Horodatage simple en général suffit. Pour les éléments destinés au judiciaire, **horodatage qualifié** recommandé.

#### 16.5 Préservation au-delà du fichier

Une capture isolée préserve la donnée. La **chaîne de conservation complète** préserve aussi le contexte.

**Éléments contextuels à préserver.**
- URL exacte (avec paramètres).
- Date/heure UTC de la consultation.
- Statut HTTP (200, 301, etc.).
- Redirections (si A redirige vers B, garder trace).
- Headers HTTP pertinents.
- IP du serveur résolu.
- Capture en plusieurs formats (PDF, HTML brut, parfois screenshots).
- Version du navigateur (Hunchly le fait automatiquement).

Pour les contenus dynamiques (vidéos, lives, contenus JavaScript-rendered), capturer le rendu **et** le source si possible.

#### 16.6 Cas particulier : les vidéos et streams

Les vidéos sont des éléments fragiles (peuvent être retirées rapidement).

**Outils.**
- **yt-dlp** (successeur de youtube-dl) : capture multi-plateformes (YouTube, X, Twitch, Telegram, TikTok).
- **OBS** pour enregistrement écran live.
- **Hunchly** capture les pages contenant la vidéo, mais pas toujours la vidéo elle-même.

**Pratique.**
- Télécharger la vidéo en format original (mp4 en général).
- Hash SHA-256 du fichier.
- Capture de la page contenant la vidéo.
- Pour les lives : enregistrement OBS du flux en temps réel.

#### 16.7 Conservation et stockage

Le stockage de la chaîne de conservation respecte plusieurs principes.

**Sécurité.**
- Conteneur chiffré (VeraCrypt, LUKS).
- Accès restreint (mot de passe robuste, 2FA si solution le permet).
- Pas de stockage sur cloud grand public (Dropbox, Google Drive personnel).
- Cloud spécialisé chiffré côté client (Tresorit, Proton Drive, ou self-hosted Nextcloud) acceptable.

**Redondance.**
- Sauvegarde sur media physique séparé (disque chiffré offline).
- Géographiquement séparée si enjeu fort.
- Stratégie 3-2-1 : 3 copies, 2 supports différents, 1 hors site.

**Cycle de vie.**
- Durée de conservation alignée sur la finalité (RGPD).
- Destruction sécurisée à expiration (shred, wipe).
- Documentation de la destruction.

#### 16.8 Transmission sécurisée

Quand un élément est transmis (au client, à un avocat, à un magistrat) :

**Canal.**
- Email chiffré PGP, ou ProtonMail.
- Service de transfert chiffré (Tresorit Send, Proton Drive partage avec lien).
- Remise physique sur support chiffré pour très sensible.
- **Pas** de WeTransfer / Google Drive partage public.

**Vérification.**
- Le hash est communiqué séparément (autre canal, ou en main propre).
- Le destinataire vérifie le hash à réception.
- Accusé de réception tracé.

#### 16.9 Limites OSINT versus forensique judiciaire

La chaîne de conservation OSINT **n'équivaut pas** à la chaîne forensique judiciaire stricte (saisie pénale, scellés, hash devant huissier).

**OSINT.**
- Auto-collectée par l'analyste.
- Hash auto-déclaré (sauf horodatage qualifié).
- Intégrité technique, mais pas d'autorité judiciaire de saisie.
- **Valeur indicative et orientante**, pas évidence pénale autosuffisante.

**Forensique judiciaire.**
- Saisie sous procédure (perquisition, réquisition).
- Scellés, horodatage huissier, contre-signature.
- Hash certifié par expert judiciaire.
- **Valeur probante directe**.

**Implication.** L'OSINT produit du renseignement orienteur, qui peut justifier une enquête judiciaire. Lors de cette enquête, les éléments seront **re-collectés** sous procédure pour acquérir valeur probante. La chaîne de conservation OSINT facilite cette re-collecte (les magistrats savent où chercher), mais ne la remplace pas.

#### 16.10 Admissibilité 2026 dans un monde post-deepfakes

L'arrivée des contenus synthétiques sophistiqués (Ch.53-59) complique l'admissibilité judiciaire des preuves numériques. Une vidéo, une photo, un audio peuvent désormais être falsifiés à un niveau qui résiste à l'œil nu.

**Tendance 2026.**
- Provenance chain (C2PA) émerge comme standard de preuve d'authenticité.
- Watermarking (SynthID) commence à se déployer.
- Les magistrats demandent de plus en plus une **expertise d'authenticité** pour les éléments numériques.

**Pour l'analyste OSINT.**
- Documenter la **provenance** de chaque élément (où, quand, comment collecté).
- Conserver les **métadonnées C2PA** si présentes.
- Capturer les éléments dès leur publication originale (pas après recopies multiples).
- Si la pièce est centrale, recommander expertise technique complémentaire.

#### 16.11 Synthèse

| Élément | Action |
|---|---|
| Capture | PDF + HTML brut + screenshot, via Hunchly idéalement |
| Hash | SHA-256, consigné séparément |
| Horodatage | Journal + horodatage qualifié si judiciaire |
| Contexte | URL, statut HTTP, redirections, navigateur |
| Stockage | Conteneur chiffré, 3-2-1 backup |
| Transmission | PGP / Proton / Tresorit Send + hash sur autre canal |
| Cycle de vie | Durée alignée finalité, destruction sécurisée tracée |
| Limites | Renseignement orienteur, pas preuve pénale autonome |

La chaîne de conservation n'est pas un luxe — c'est ce qui transforme votre travail en livrable opposable. Sans elle, vous produisez du commentaire.

-----

### Chapitre 17 — Structurer l'information collectée

#### 17.1 Pourquoi structurer

Une enquête OSINT génère vite **trop d'informations**. Pour une enquête comme MIRAGE, à mi-parcours, l'analyste accumule typiquement plusieurs centaines de captures, deux à trois cents entités identifiées (personnes, sociétés, domaines, comptes, lieux), des dizaines d'événements datés.

Sans structuration, cette masse devient inutilisable. La structuration transforme la collecte en matériau analysable.

#### 17.2 Les six structures principales

Six structures complémentaires organisent le dossier.

**1. Fiches entités.** Une fiche par entité d'intérêt (personne, société, compte, domaine, lieu, contenu, wallet, source). Champs standardisés. Mises à jour au fil de la collecte.

**2. Tableau de sélecteurs.** Liste maître des sélecteurs identifiés, avec leur entité associée, leur source de découverte, leur statut (vérifié, à confirmer).

**3. Timeline.** Ligne temporelle des événements datés. Permet d'identifier incohérences, séquences causales, simultanéités suspectes.

**4. Graphe relationnel.** Représentation visuelle des liens entre entités. Met en évidence les clusters, les pivots, les nœuds critiques.

**5. Matrice source / information.** Tableau qui croise les informations clés avec leurs sources. Permet d'identifier les faits corroborés (plusieurs sources) versus les pistes uniques.

**6. Matrice hypothèses / éléments.** Tableau qui croise les hypothèses concurrentes (ACH — Ch.79) avec les éléments collectés (pour / contre). Cœur de l'analyse.

#### 17.3 Fiche entité : structure type

**Fiche personne physique.**

```
ENTITÉ : Marc Delaunay
Type : Personne physique
Statut : Cible principale

== Identité ==
Nom complet : Marc Henri Delaunay
Date de naissance : 17 octobre 1976 (présumé, à confirmer)
Lieu de naissance : Nantes (à confirmer)
Nationalité : Française (présumée)
Résidence : Paris 16e (présumée)

== Profession ==
Poste actuel : DAF, TechnoVert SAS (depuis 2019)
Parcours :
- 2015-2019 : Directeur financier, Solucia Industries
- 2010-2015 : Senior Manager, KPMG
- 2002-2010 : Auditeur senior, Deloitte
- 1999-2002 : Junior associate, BDO
Formation : X-Ponts, promo 1999

== Identifiants numériques ==
Email pro : m.delaunay@technovert.fr [confirmé, A1]
Email perso suspecté : marc.delaunay76@gmail.com [hypothèse, à confirmer]
LinkedIn : /in/marc-delaunay-08394 [confirmé, A1]
Twitter : @mdelaunay76 [hypothèse forte, B2]
Instagram : mdelaunay76 [hypothèse forte, B2]

== Liens entités ==
- Société TechnoVert SAS [employeur]
- Société Delta Consulting Ltd (Malte) [administrateur déclaré]
- Société Verde Holdings (Chypre) [à confirmer]
- SCI La Provence Familiale [administrateur via épouse]

== Indicateurs financiers visibles ==
- Salaire estimé TechnoVert : 180-250 k€/an
- Patrimoine SCI : ~1.8 M€
- Villa Marrakech : valeur estimée 800 k€

== Cotations préliminaires ==
Source A : confirmé (TechnoVert communiqués)
Source B : très probable (recoupements)
Source C : possible (à approfondir)

== Notes ==
- Aucune présence Telegram/Signal détectable via sélecteurs connus
- Possible username perso "mdelaunay76" récurrent
- Cluster Delta-Verde à creuser

== Historique de mise à jour ==
2026-05-19 : création
2026-05-22 : ajout LinkedIn et parcours
2026-05-25 : hypothèse Delta Consulting confirmée
```

**Fiche société.** Structure similaire adaptée : raison sociale, juridiction, numéro, capital, administrateurs, UBO, activité, siège, dates.

**Fiche compte social.** Plateforme, handle, date de création, photo, bio, abonnés, abonnements, activité type, signaux d'authenticité.

**Fiche domaine.** Domaine, registrar, WHOIS, DNS, certificats, hébergement, technologies, contenu, dates.

**Fiche image / contenu.** URL, source, hash, métadonnées, analyses (recherche inversée, ELA, détection IA), liens vers autres entités.

**Fiche wallet.** Adresse, blockchain, premier txn, dernière activité, clusters identifiés *(détail dans OSINT Crypto vFULL)*.

**Fiche source.** Domaine ou plateforme, type (presse, registre, blog, réseau social), cotation Admiralty, fiabilité historique.

#### 17.4 Tableau de sélecteurs

Tableau maître à maintenir en continu.

| Sélecteur | Type | Valeur | Entité | Source découverte | Date | Statut |
|---|---|---|---|---|---|---|
| Email | Pro | m.delaunay@technovert.fr | Delaunay | TechnoVert site web | 2026-05-19 | Confirmé |
| Email | Perso suspecté | marc.delaunay76@gmail.com | Delaunay | Pivot username | 2026-05-22 | Hypothèse |
| Username | mdelaunay76 | mdelaunay76 | Delaunay | Sherlock | 2026-05-22 | Confirmé multi-plateformes |
| Téléphone | Pro | +33 1 XX XX XX XX | Delaunay | TechnoVert standard | 2026-05-20 | Confirmé |
| Domaine | Suspect | verites-technovert.com | Désinfo | Pivot recherche | 2026-05-28 | Confirmé hostile |
| Domaine | Suspect | info-finance-eu.com | Désinfo | Pivot blog | 2026-05-29 | Confirmé hostile |
| Société | Cible | Delta Consulting Ltd | Offshore | Companies Registry Malte | 2026-05-25 | Confirmé |
| (...) | (...) | (...) | (...) | (...) | (...) | (...) |

#### 17.5 Timeline

La timeline est **chronologique**. Elle peut être tenue en :
- Tableau (date / événement / source / cotation).
- Outil dédié : **Timeline Explorer** (gratuit Eric Zimmerman), **Aeon Timeline** (payant, puissant), **Timegraphics**.
- Graphe temporel (avec Maltego, Linkurious).

**Exemple MIRAGE — timeline partielle.**

| Date | Événement | Source | Cot. |
|---|---|---|---|
| 2002 | Diplôme X-Ponts | LinkedIn | A1 |
| 2019-06 | Embauche TechnoVert comme DAF | Communiqué TechnoVert | A1 |
| 2020-03 | Création Delta Consulting Ltd (Malte) | Companies Registry MT | A1 |
| 2021-09 | Premier contrat consulting TechnoVert→Delta | BODACC indirect | C3 |
| 2022-01 | Création Verde Holdings (Chypre) | Companies Registry CY | A1 |
| 2025-04 | Audit interne TechnoVert signal écritures | Antoine Berthier interview | B2 |
| 2025-09-15 | Licenciement Antoine Berthier | Source RH (presse) | B2 |
| 2025-10 | Création domaine verites-technovert.com | WHOIS historique | A1 |
| 2025-11 | Premier post diffamatoire blog | Capture wayback | A2 |
| 2026-01 | Cluster X de 8 comptes amplifie | Archive.today | A2 |
| 2026-03 | Apparition vidéo deepfake Berthier | YouTube (supprimé) + cache | B2 |
| 2026-05-16 | Mandat Legrand & Associés | Mandat | A1 |
| (...) | (...) | (...) | (...) |

Les **incohérences chronologiques** sont l'un des révélateurs les plus puissants. Une publication antérieure à un événement qu'elle décrit. Un poste pris avant la fondation de la société. Une activité supposée pendant des congés documentés ailleurs.

#### 17.6 Graphe relationnel

Le graphe représente visuellement les **entités** (nœuds) et les **relations** (arêtes).

**Outils.**
- **Maltego** : standard professionnel. Version Community gratuite limitée, version commerciale puissante.
- **Gephi** : open source, puissant pour analyses statistiques de réseau.
- **Neo4j** + interface (Bloom) : pour analystes techniques, base graph robuste.
- **draw.io / yEd / Lucidchart** : pour graphes manuels, simples.
- **Maltego Casefile** : version offline, pas de transforms automatiques mais OK pour usage souverain.

**Niveaux de graphe.**

**Graphe simple.** Personne → liens directs (sociétés contrôlées, sociétés employeuses, comptes sociaux).

**Graphe relationnel structuré.** Avec types d'arêtes (employer, owner, friend, register, hosting, etc.), métadonnées sur les arêtes (date, source, force du lien).

**Graphe d'enquête complet.** Plusieurs centaines de nœuds. Clusters identifiables. Algorithmes de détection de communautés (Louvain, modularité). Nœuds centraux (degree centrality, betweenness centrality).

#### 17.7 Matrice source / information

Tableau qui croise une **liste de faits** avec une **liste de sources**, pour identifier les corroborations.

**Exemple simplifié.**

| Fait | Source A (TechnoVert) | Source B (LinkedIn) | Source C (Pappers) | Source D (ICIJ) |
|---|---|---|---|---|
| Delaunay DAF TechnoVert | ✓ | ✓ | ✓ |   |
| Delaunay admin Delta Consulting |   |   |   | ✓ |
| Delta Consulting adresse Malte |   |   |   | ✓ |
| Capital Delta Consulting 1200 € |   |   |   | ✓ |

Une ligne avec une seule croix = piste à corroborer. Une ligne avec plusieurs croix = fait établi à coter.

#### 17.8 Matrice hypothèses / éléments (ACH)

Cœur de la méthode ACH (Ch.79). Tableau qui croise **hypothèses concurrentes** (colonnes) avec **éléments collectés** (lignes), en notant pour chaque élément s'il est **compatible** (C), **incompatible** (I), ou **neutre** (N) avec chaque hypothèse.

**Exemple sur MIRAGE IR1 (Delaunay détient-il des sociétés offshore non déclarées ?).**

| Élément | H1 : Detient personnellement | H2 : Nominee contrôlé par tiers | H3 : Aucun lien |
|---|---|---|---|
| Admin déclaré Delta Consulting | C | C | I |
| Email pro dans WHOIS verites-technovert.com | C | I | I |
| Pas de mention Delta dans déclaration fiscale FR | C (non-déclaration) | C (s'il est nominee, peut ne pas déclarer) | C (rien à déclarer) |
| Flux TechnoVert → Delta Consulting | C | C | I |
| Délivrance pouvoir signature Verde Holdings | C | C | I |

L'hypothèse **la moins infirmée** est retenue. H3 (« aucun lien ») est multiplement incompatible → réfutée. H1 et H2 restent ouvertes. La distinction H1 vs H2 demande approfondissement (Delaunay est-il bénéficiaire effectif réel, ou intermédiaire ?).

#### 17.9 Vault Obsidian comme intégrateur

**Obsidian** est l'outil le plus populaire en 2026 pour intégrer ces six structures dans un vault unique.

**Architecture type d'un vault d'enquête.**

```
/MIRAGE/
├── 00_Cadrage/
│   ├── SOR_signé.md
│   └── Plan_de_collecte.md
├── 01_Journal/
│   ├── 2026-05-19.md
│   ├── 2026-05-20.md
│   └── (...)
├── 02_Entités/
│   ├── Personnes/
│   │   ├── Marc_Delaunay.md
│   │   ├── Antoine_Berthier.md
│   │   └── (...)
│   ├── Sociétés/
│   │   ├── TechnoVert_SAS.md
│   │   ├── Delta_Consulting_Ltd.md
│   │   └── (...)
│   ├── Domaines/
│   ├── Comptes/
│   ├── Contenus/
│   └── Wallets/
├── 03_Sélecteurs/
│   └── Table_sélecteurs.md
├── 04_Timeline/
│   └── Timeline_globale.md
├── 05_Graphes/
│   └── (exports Maltego)
├── 06_Analyse/
│   ├── ACH_IR1_offshores.md
│   ├── ACH_IR4_désinfo.md
│   └── (...)
├── 07_Captures/
│   └── (captures Hunchly, hashes.txt)
├── 08_Rapports/
│   ├── Note_etape_J15.md
│   ├── Rapport_final.md
│   └── (...)
└── 09_Sources/
    └── Bibliographie.md
```

Les liens internes Obsidian (`[[Marc_Delaunay]]`) créent automatiquement un graphe que vous pouvez visualiser avec le plugin Graph View. Les tags (`#hypothèse-IR1`, `#cotation-A1`) permettent les filtres rapides.

#### 17.10 Discipline de structuration

La structuration n'est pas un luxe **après** la collecte — c'est **pendant** la collecte. Chaque entité découverte est ajoutée à sa fiche dans la journée. Chaque pivot est tracé. Chaque hypothèse est testée. La structuration **en continu** prévient le mur des dernières 48h où l'analyste se noie dans 400 captures non triées.

-----

### Chapitre 18 — Lab de l'investigateur

#### 18.1 Le lab comme actif professionnel

Le **lab** désigne l'environnement matériel, logiciel et organisationnel de l'investigateur. C'est un actif professionnel structuré, comparable à l'atelier d'un artisan. Sa qualité conditionne directement la productivité et la sécurité du travail.

Trois niveaux : **lab minimal** (analyste débutant, missions ponctuelles), **lab professionnel** (analyste indépendant, missions régulières), **lab d'équipe** (cabinet, cellule interne).

#### 18.2 Matériel

**Poste principal.** Laptop professionnel récent (CPU correct, 16+ Go RAM, SSD 512+ Go). Système d'exploitation : Linux (Ubuntu 24.04, Pop!_OS, Fedora) ou Windows 11 Pro (avec BitLocker activé), ou macOS récent (FileVault activé). Linux est préféré pour des raisons de souveraineté et de transparence.

**Second poste** (recommandé). Pour cloisonner enquêtes sensibles. Peut être un mini-PC dédié, un laptop d'investigation séparé.

**Téléphone d'investigation.** Séparé physiquement, SIM dédiée. Voir Ch.9.

**Clés YubiKey** (ou équivalent). 2FA matériel pour comptes critiques. Au moins deux clés (principale + backup).

**Disques externes chiffrés.** Pour sauvegardes 3-2-1.

**Imprimante sécurisée locale.** Pas de cloud printing. Pour livrables papier confidentiels.

#### 18.3 Logiciels système et OPSEC

- **Système chiffré** (LUKS, BitLocker, FileVault).
- **Conteneurs VeraCrypt** par enquête.
- **VirtualBox** ou **VMware Workstation** pour VM dédiées.
- **VPN** : Mullvad, IVPN, ProtonVPN. Pas de VPN gratuit.
- **Gestionnaire mots de passe** : KeePassXC (local), Bitwarden self-hosted (équipe).
- **Tails** sur clé USB pour missions ponctuelles sensibles.
- **Whonix** VM pour Tor durable.
- **Signal Desktop** pour communication confidentielle.

#### 18.4 Suite navigateur et OSINT web

- **Firefox** profil dédié : extensions uBlock Origin, NoScript (avec parcimonie), Cookie AutoDelete, Privacy Badger, CanvasBlocker, **Wayback Machine extension**, **OneTab** (gestion onglets), **Hunchly** (capture).
- **Chromium / Brave** profil secondaire pour compatibilité.
- **Tor Browser** pour missions Tor.

#### 18.5 Suite OSINT logicielle

**Note & vault.**
- **Obsidian** (gratuit, vault local, plugins riches). Standard 2026.
- Alternatives : Logseq, Joplin (open source).

**Capture et journal.**
- **Hunchly** (payant, standard professionnel).
- **SingleFile** (extension, gratuit).
- **yt-dlp** (téléchargement vidéo multi-plateformes).

**Graphes.**
- **Maltego CE** (Community Edition, gratuit) + **Casefile** (offline).
- **Maltego Pro** (payant) pour transforms automatiques.
- **Gephi** (open source, analyses statistiques).
- **Neo4j Community** (graph DB locale).

**Timeline.**
- **Timeline Explorer** (Zimmerman, gratuit).
- **Aeon Timeline** (payant).

**Réseaux et infrastructure.**
- **Amass** (sous-domaines), **subfinder**, **dnsx**.
- **WHOIS clients** (terminal).
- **nmap**, **masscan** (avec prudence légale).

**Image & GEOINT.**
- **ExifTool** (métadonnées).
- **QGIS** (cartographie).
- **Google Earth Pro** (gratuit, riche).
- **FotoForensics**, **Forensically** (analyses).

**Crypto / blockchain.** *(renvoi → OSINT Crypto vFULL)*

**Code & automatisation.**
- **Python** (3.11+) + venv ou pyenv.
- **Jupyter Lab** pour notebooks reproductibles.
- **Git** local (chiffré) pour versioning.
- **Playwright** ou Selenium pour scraping résilient.

**IA locale.**
- **Ollama** (LLMs locaux). Llama 3, Mistral, Qwen.
- **LM Studio** (interface graphique).
- **GPT4All**.

#### 18.6 Outils SaaS et abonnements

Selon budget et menace acceptable :

- **Hunter.io** (email lookup).
- **DeHashed** (breaches).
- **Intelligence X** (deep search, leaks).
- **Shodan** (infrastructure Internet).
- **Censys** (idem, complémentaire).
- **PimEyes** (recherche faciale, attention légale).
- **OpenSanctions** (gratuit, sanctions).
- **Pappers** (gratuit/payant, registres français).
- **OpenCorporates** (registres internationaux).
- **Hive Moderation** / **Sensity** (détection IA).

Choisir selon enquêtes types. Renouveler annuellement, vérifier la pertinence.

#### 18.7 Arborescence type d'un dossier d'enquête

Présentée au Ch.17 (vault Obsidian). Le principe :
- Un dossier racine par enquête (code projet, pas le nom de la cible).
- Sous-dossiers standardisés.
- Versioning Git.
- Conteneur VeraCrypt englobant le tout.

#### 18.8 Routines opérationnelles

**Au démarrage de chaque enquête.**
- Création conteneur VeraCrypt dédié.
- Création vault Obsidian.
- Snapshot VM d'investigation.
- Génération sous-domaines hashes initiaux.
- Activation VPN si non permanent.

**En cours.**
- Backup quotidien du dossier d'enquête.
- Hash vérification hebdomadaire.
- Point de revue toutes les 48-72h.

**À la fin de l'enquête.**
- Export final.
- Backup chiffré sur support séparé.
- Destruction sécurisée des éléments non conservés (selon SOR).
- Capitalisation : leçons apprises documentées.

#### 18.9 Lab d'équipe : spécificités

- **Outil collaboratif** : Element/Matrix self-hosted ou Slack chiffré.
- **Stockage partagé** : Nextcloud self-hosted ou équivalent.
- **Wiki interne** : pour SOPs, modèles, leçons.
- **CI/CD pour scripts internes** : Gitea ou GitLab self-hosted.
- **Briefing OPSEC mensuel** : revues d'incidents, mises à jour outils.

#### 18.10 Veille outils

L'écosystème OSINT évolue mensuellement. Une **veille outils** est nécessaire.

- **OSINT Framework** (osintframework.com) — catalogue maintenu.
- **OSINT-FR ressources**.
- **Bellingcat Online Investigation Toolkit**.
- **IntelTechniques** (Michael Bazzell).
- **OSINT Curious** podcast et blog.
- Newsletters spécialisées : ConductORE, OSINT Daily, Bellingcat newsletter.

**Discipline.** Garder une liste maître à jour. Tester les nouveaux outils dans un environnement isolé avant adoption. Documenter dans le wiki interne.

> **MIRAGE — Épisode 3 : OPSEC et plan de collecte**
>
> Mardi 20 mai 2026. L'analyste finalise son environnement d'enquête.
>
> Création d'un conteneur VeraCrypt 50 Go nommé `MIRAGE_2026`. Création d'un vault Obsidian dedans, avec l'arborescence type. Création d'une VM Ubuntu dédiée, snapshot initial. Activation Mullvad VPN avec port forwarding sur un nœud français (cohérence géographique avec l'enquête sur cible française).
>
> Évaluation du threat model : Delaunay est techniquement compétent (DAF expérimenté), sa structure offshore suppose des partenaires (cabinet d'avocats spécialisé, fiduciaire), la branche désinformation suggère un prestataire criminel actif. Threat model : entre « sensible » et « criminelle ». Pas d'enjeu étatique identifié à ce stade.
>
> Conséquence OPSEC :
> - VM dédiée, jamais de connexion personnelle dessus.
> - Profil Firefox dédié, Hunchly activé en permanence.
> - Trois avatars LinkedIn matures déjà disponibles dans le parc du cabinet, l'un d'eux (« Camille Roux », créé en 2024, profil RH) sera utilisé pour observation LinkedIn de Delaunay.
> - Téléphone d'investigation séparé, SIM prépayée déclarée.
> - Pas de connexion depuis le wifi domicile, uniquement depuis le bureau (réseau dédié) ou hotspot téléphone investigation.
>
> Plan de collecte détaillé sur 6 semaines validé avec Me Legrand. Premier jalon à J+15 (29 mai). Critères d'arrêt précisés : faisceau d'indices convergents suffisant pour saisine PNF sur IR1, IR2, IR4, IR5 ; IR3 (patrimoine) à profondeur d'orientation.
>
> L'enquête peut désormais entrer dans sa phase de collecte active. Le Chapitre 19 ouvre la Partie IV — Moteurs, recherche web et restrictions plateformes.

-----
