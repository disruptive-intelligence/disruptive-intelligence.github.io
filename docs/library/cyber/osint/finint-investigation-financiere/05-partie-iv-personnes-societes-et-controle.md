---
title: PARTIE IV — PERSONNES, SOCIÉTÉS ET CONTRÔLE
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 5
chapters: 11
---

*Huit chapitres pour identifier précisément les acteurs (personnes physiques, sociétés) et comprendre les structures de contrôle (formes juridiques, mandataires, actionnaires, UBO, holdings, trusts, sociétés écrans). C’est la grammaire fine du FININT : sans elle, les flux observés au chapitre suivant restent illisibles.*

-----

## Chapitre 19 — Identifier une personne physique sans se tromper d’homonyme

### Objectif du chapitre

Maîtriser la **discipline d’identification** d’une personne physique. C’est l’erreur la plus courante et la plus dommageable en FININT : attribuer à une cible des éléments qui concernent en réalité un homonyme. Cette erreur peut détruire la crédibilité d’un livrable et causer un préjudice réel à un tiers innocent.

### Le concept

L’**homonymie** est une réalité statistique. Pour des prénoms et noms courants, on compte des centaines, voire des milliers d’homonymes dans un pays. Pour des noms moins courants, ce risque baisse mais n’est jamais nul. L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.

### Les attributs d’identification

L’analyste cherche à stabiliser autant d’attributs que possible parmi :

- **Nom et prénoms** complets, dans l’ordre, avec orthographe précise.
- **Date de naissance** (jour, mois, année).
- **Lieu de naissance** (commune, pays).
- **Nationalité(s)** — peut être multiple.
- **Adresse(s) connue(s)** — actuelle, antérieures.
- **Numéro d’identification fiscale** (numéro fiscal de référence en France, NIF, NIN, etc.) — rarement accessible en OSINT, mais central en sources fermées.
- **Numéro de sécurité sociale** — non accessible en OSINT.
- **Numéro de passeport** — non accessible en OSINT sauf cas particuliers (leaks).
- **Photographie** — recoupement visuel.
- **Profil professionnel public** (LinkedIn, presse) — cohérence biographique.
- **Réseau familial** : conjoint, parents, frères et sœurs, enfants — souvent identifiable via presse ou réseaux sociaux.
- **Réseau professionnel** : associés, employeurs, mandats parallèles.

Plus le nombre d’attributs convergents, plus l’identification est solide. La règle pratique :

- 2 attributs forts (nom complet + date de naissance, ou nom + photo) = identification *possible*.
- 3-4 attributs convergents = identification *probable*.
- 5+ attributs convergents, dont des recoupements indépendants = identification *quasi-certaine*.

### Les pièges classiques

**Translittération** : un même nom peut s’écrire de plusieurs façons selon la langue source. « Mohamed » vs « Mohammad » vs « Muhammad ». « Иванов » → « Ivanov », « Ivanoff », « Iwanow » selon les conventions. L’analyste teste systématiquement les variantes.

**Articles et particules** : « Van der Berg », « De la Cruz », « Al-Hadi » — selon les sources, certaines parties peuvent être omises ou attachées. « Karim Haddad » peut apparaître comme « Haddad, Karim », « Karim El-Haddad », « K. Haddad », etc.

**Initiales** : les comptes annuels et certains documents officiels n’utilisent parfois que l’initiale du prénom. Source d’ambiguïté.

**Diminutifs** : « William » ↔ « Bill », « James » ↔ « Jim », « Catherine » ↔ « Cathy » ou « Kate » — fréquents dans le monde anglophone.

**Changement de nom** : mariage, divorce, naturalisation, raisons personnelles. Une personne née sous un nom peut apparaître sous un autre dans certains documents.

**Confusion père/fils** : Karim Haddad Senior vs Karim Haddad Junior — même nom, attributs différents. Toujours vérifier la date de naissance.

### Méthode — protocole d’identification en 6 étapes

1. **Collecter les attributs disponibles** : nom complet, date de naissance, lieu, nationalité, profession.
1. **Tester les variantes** : translittérations, articles, initiales, ordre.
1. **Croiser avec les sources** : registres (mandats déclarés), presse, leaks, réseaux sociaux.
1. **Identifier les homonymes potentiels** : combien de personnes avec ces attributs ?
1. **Valider par convergence** : la personne identifiée a-t-elle bien tous les attributs attendus ?
1. **Calibrer la confiance** : sur la base du nombre et de la qualité des recoupements.

### Mini-walkthrough

Cible : « Karim Haddad », mentionné dans une DS comme dirigeant suspect.

- Recherche initiale : « Karim Haddad » → des centaines de résultats Google, plusieurs profils LinkedIn, plusieurs entrées registre dans plusieurs pays.
- Attributs initiaux fournis par la DS : âge approximatif (« la cinquantaine »), nationalité (franco-libanais), domaine d’activité (négoce et import-export).
- Recherche affinée : « Karim Haddad » + « négoce » + « Liban » ou « France ».
- 3 candidats émergent :
  - Karim Haddad A, né 1965, ingénieur télécoms à Beyrouth → exclu (profession différente).
  - Karim Haddad B, né 1968, négociant franco-libanais, dirigeant déclaré de plusieurs sociétés en France et au Liban → match probable.
  - Karim Haddad C, né 1981, journaliste basé à Paris → exclu (profession différente).
- Recoupement complémentaire : RBE des SAS françaises identifie un UBO Karim Haddad, né 1968 à Beyrouth, nationalité française. Convergence : nom + date + lieu + nationalité + profession + mandats → identification *quasi-certaine*.

### Erreurs fréquentes

- **Conclure sur 2 attributs faibles** (nom + secteur) — risque homonyme élevé.
- **Ne pas tester les variantes orthographiques** — manque la cible si elle apparaît sous variante.
- **Ignorer les changements de nom** — femme mariée, naturalisation, etc.
- **Confondre père / fils** — toujours vérifier l’année de naissance précise.
- **Attribuer une photo sans recoupement** — un nom commun peut avoir plusieurs photos sur Internet, certaines non attribuables.

### Limites

L’identification peut rester **indéterminable** dans certains cas : très peu d’attributs accessibles (personne discrète, juridiction opaque), risque homonyme élevé (nom très courant), absence de photo ou de date de naissance. L’analyste documente explicitement la limite : *« Identification de M. K. Haddad établie à un niveau de confiance probable. Une confirmation quasi-certaine nécessiterait l’accès au numéro fiscal ou à un document d’identité, hors périmètre des sources ouvertes mobilisées. »*

### Lien avec le fil rouge

> **CLEARFLOW — Stabiliser Karim Haddad**
> 
> Avant toute autre analyse, Nassim consacre 2 heures à stabiliser l’identification : nom complet (Karim Élie Haddad), date de naissance (1968), lieux (Beyrouth puis Paris), nationalités (libanaise et française), parcours professionnel (négoce et import-export depuis 1995). Photo officielle récupérée via LinkedIn et site d’une chambre de commerce franco-libanaise. Cette stabilisation initiale conditionne tout le reste : sans elle, les attributions ultérieures seraient suspectes.

### Points clés à retenir

- L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.
- Pièges : translittération, particules, initiales, diminutifs, changements de nom, père/fils.
- 5+ attributs convergents = quasi-certain ; 2 attributs faibles = à approfondir.
- Documenter explicitement les limites quand l’identification reste incomplète.

-----

## Chapitre 20 — Identifier une société et ses variantes internationales

### Objectif du chapitre

Maîtriser l’identification d’une **personne morale** : variantes orthographiques, sociétés de même nom dans plusieurs juridictions, sociétés homonymes, identifiants officiels permettant de stabiliser la référence.

### Le concept

L’identification d’une société repose essentiellement sur son **identifiant officiel** dans la juridiction de son siège :

- **France** : SIREN (9 chiffres) ou SIRET (14 chiffres = SIREN + identifiant établissement).
- **UE** : EUID (European Unique Identifier) émergent ; chaque pays a son identifiant national (Numéro KvK aux Pays-Bas, Numéro d’entreprise belge, etc.).
- **UK** : Company Number (8 caractères : 2 lettres + 6 chiffres pour Scottish, sinon 8 chiffres).
- **US** : EIN (Employer Identification Number) au niveau fédéral, mais pas universel. Plus utile : numéro d’enregistrement de l’État (Delaware, etc.).
- **LEI** (Legal Entity Identifier) : code ISO 17442 à 20 caractères, attribué aux entités opérant sur les marchés financiers. Base mondiale [GLEIF](https://www.gleif.org/). Particulièrement utile pour les institutions financières et les contreparties cotées.
- **DUNS Number** : identifiant Dun & Bradstreet, utilisé largement dans la commande publique et l’évaluation de risque.
- **VAT Number** : numéro de TVA intracommunautaire (UE), vérifiable via VIES.

L’identifiant officiel est **clé** : il lève l’ambiguïté entre sociétés de même nom dans plusieurs juridictions.

### Les pièges classiques

**Sociétés homonymes inter-juridictions** : « NEXUS TRADING » peut exister en France, en UK, à Chypre et à Dubaï — entités juridiques distinctes, parfois liées, parfois non. Toujours préciser la juridiction et l’identifiant.

**Variantes orthographiques** : « NEXUS TRADING SAS » vs « Nexus Trading » vs « N. Trading SAS » — le registre officiel a une dénomination exacte qui prévaut.

**Sociétés rebaptisées** : une société peut changer de dénomination plusieurs fois. L’identifiant SIREN/Company Number reste, mais la recherche par nom historique peut manquer la cible.

**Sociétés fusionnées / absorbées** : une société absorbée disparaît juridiquement ; son identifiant aussi. Continuité économique parfois trompeuse.

**Groupes vs filiales** : « TOTAL » peut désigner TotalEnergies SE, TotalEnergies Marketing France SAS, TotalEnergies E&P, etc. Préciser l’entité concernée.

**Marques vs sociétés** : une marque commerciale (« Apple ») peut correspondre à plusieurs sociétés juridiques (Apple Inc., Apple Operations International, Apple Sales International, etc.).

### Méthode — protocole d’identification

1. **Recueillir tous les attributs** : dénomination, juridiction (pays + ville si possible), secteur d’activité, dirigeants connus, adresse.
1. **Recherche dans le registre national** (chapitres 11-12).
1. **Vérifier l’identifiant officiel** : SIREN / Company Number / autre.
1. **Vérifier l’historique** : changements de dénomination, fusions, transferts de siège.
1. **Identifier les entités liées** : filiales, sociétés sœurs, holding mère.
1. **Documenter** : fiche identification précise (annexe D).

### Mini-walkthrough

Cible : « NEXUS HOLDINGS », mentionnée dans une DS comme contrepartie d’un flux de 1,2 M€ provenant de Chypre.

- Recherche initiale : Pappers, Companies House, OpenCorporates → 14 résultats sociétés contenant « Nexus » dans le nom, dans 9 juridictions.
- Affinage avec le contexte (Chypre + 2019 + dirigeant connu) : 2 candidats.
  - NEXUS HOLDINGS LTD (Chypre, registered 2019, directeur M. Y) → match probable.
  - NEXUS HOLDINGS LIMITED (BVI, registered 2010, directeurs trustees professionnels) → exclu (différents directeurs et antériorité).
- Identifiant officiel : Cyprus Company Registration Number HE-XXXXXX.
- Historique : pas de changement de dénomination depuis création.
- Entités liées : la société est associée majoritaire d’une SAS française et d’une LLC US — graphe à étendre.

### Erreurs fréquentes

- **Confondre des sociétés de même nom dans des juridictions différentes** — c’est l’erreur n°1 dans les enquêtes multi-juridictionnelles.
- **Oublier de tester les translittérations** — « Sergei » vs « Sergey », « Loutchnikov » vs « Luchnikov ».
- **Confondre groupe et filiale** — un dossier sur « TOTAL » sans préciser l’entité juridique est ininterprétable.
- **Confondre dénomination commerciale et dénomination sociale** — la marque ne suffit pas.

### Limites

Dans les juridictions opaques (BVI, Cayman, Panama, etc.), les recherches par nom peuvent ne pas être publiques. L’analyste s’appuie alors sur leaks (chapitre 18), agrégateurs et coopération internationale.

### Lien avec le fil rouge

> **CLEARFLOW — Stabiliser les 14 entités**
> 
> Sur les 14 sociétés du réseau Haddad mentionnées dans les DS, Nassim stabilise chaque identification par juridiction et identifiant officiel. Une particularité émerge : 3 sociétés portent un nom proche (« Nexus Trading », « Nexus Holdings », « Nexus International ») mais sont dans 3 juridictions différentes (France, Chypre, Émirats). L’analyse confirme qu’elles sont liées (sociétés affiliées contrôlées par le même réseau), mais ce sont des entités juridiques distinctes — distinction à maintenir dans tout livrable pour éviter les amalgames.

### Points clés à retenir

- L’identifiant officiel (SIREN, Company Number, LEI) prime sur le nom.
- Tester systématiquement les variantes orthographiques et les translittérations.
- Distinguer sociétés homonymes, groupes, filiales et marques.
- Documenter l’historique (changements de dénomination, fusions).

-----

## Chapitre 21 — Formes juridiques comparées

### Objectif du chapitre

Connaître les **formes juridiques principales** rencontrées en FININT, leurs caractéristiques (responsabilité, transparence, capital, gouvernance), et leur signification dans une cartographie. La forme juridique d’une entité informe sur sa flexibilité, son opacité potentielle et ses obligations.

### Le concept

Les formes juridiques varient considérablement par juridiction. Quelques familles structurantes.

**Sociétés de capitaux** : responsabilité limitée au capital. La grande majorité des entreprises modernes.

- **SAS / SASU** (France) — société par actions simplifiée (unipersonnelle si un seul associé). Flexible, gouvernance librement définie dans les statuts. Présidence par personne physique ou morale.
- **SARL / EURL** (France) — société à responsabilité limitée. Plus encadrée que la SAS. Gérée par un ou plusieurs gérants.
- **SA** (France) — société anonyme. Plus lourde (CAC obligatoire, conseil d’administration ou directoire + conseil de surveillance), capital minimum 37 000 €. Pour les grandes entreprises ou les sociétés cotées.
- **SCA** (France) — société en commandite par actions. Rare mais utilisée dans certains schémas familiaux ou patrimoniaux.
- **GmbH** (Allemagne) — équivalent SARL allemand. Très commune.
- **AG** (Allemagne) — équivalent SA. Pour les grandes entreprises et les cotées.
- **S.r.l.** (Italie) — équivalent SARL.
- **S.p.A.** (Italie) — équivalent SA.
- **S.L.** (Espagne) — équivalent SARL.
- **S.A.** (Espagne) — équivalent SA.
- **B.V.** (Pays-Bas) — Besloten Vennootschap, équivalent SARL. Très utilisée dans les holdings internationaux.
- **N.V.** (Pays-Bas, Belgique) — Naamloze Vennootschap, équivalent SA.
- **Ltd / Limited** (UK, Irlande) — équivalent SARL ; obligation de publier comptes et PSC.
- **PLC** (UK) — Public Limited Company, équivalent SA cotée.
- **LLC** (US, plusieurs États) — Limited Liability Company. Hybride entre société et partnership ; flexibilité fiscale ; très utilisée dans les structures opaques (Delaware, Wyoming, Nevada).
- **Inc. / Corporation** (US) — équivalent SA.
- **AG** (Suisse) — équivalent SA.
- **GmbH** (Suisse) — équivalent SARL.

**Sociétés de personnes** : responsabilité illimitée (généralement).

- **SNC** (France) — société en nom collectif. Associés indéfiniment et solidairement responsables.
- **Société civile** (France) — civile par défaut, fréquente pour gestion patrimoniale (SCI immobilière).
- **Partnership** (UK, US) — équivalent SNC.
- **LLP** (UK, US) — Limited Liability Partnership, hybride. UK : doit publier comme une Limited.

**Structures de holding et particulières** :

- **Soparfi** (Luxembourg) — Société de Participation Financière. Régime fiscal favorable pour les holdings.
- **SCSp** (Luxembourg) — Société en Commandite Spéciale, structure flexible pour les fonds.
- **IBC** (International Business Company) — typique des juridictions offshore caribéennes.
- **LP / Limited Partnership** (Scottish LP, Delaware LP, etc.) — historiquement opaque, désormais sous PSC au UK.

**Trusts et fondations** (chapitre 25, en détail) :

- **Trust** (Common law : UK, US, BVI, Cayman, Bahamas, etc.) — relation juridique entre settlor, trustee, bénéficiaires.
- **Fondation** (droit continental : Liechtenstein Stiftung, Panamanian Foundation, etc.) — entité juridique distincte du fondateur.

**Associations et structures sans but lucratif** :

- **Association loi 1901** (France).
- **Charity** (UK).
- **501(c)(3)** (US).

### L’utilité opérationnelle

Pour l’analyste :

- **La forme oriente sur la transparence attendue.** Une SAS française publie ses comptes (au-delà des seuils) ; une LLC Delaware ne publie rien. Un trust BVI n’est pas une entité juridique publique.
- **La forme oriente sur la gouvernance.** Une SA a un conseil d’administration ou directoire + conseil de surveillance ; une SAS peut être pilotée par un président unique.
- **La forme oriente sur les obligations LCB-FT.** Certaines formes sont des assujettis (notaires, avocats sous certaines conditions, agents immobiliers), d’autres non.
- **La forme oriente sur les schémas typiques.** SCI pour la détention immobilière. SOPARFI pour les holdings. LLC Delaware pour les structures opaques. Trust pour la séparation patrimoniale.

Une cartographie de réseau qui ne distingue pas les formes juridiques est lacunaire.

### Méthode — lecture d’une cartographie par forme

Sur un graphe avec 12 entités, l’analyste annote chaque nœud :

```
ENTITY 1 — SAS française, capital 10 K€, dirigeant unique
ENTITY 2 — Ltd UK, PSC déclaré, comptes publiés (micro)
ENTITY 3 — LLC Delaware, opacité maximale
ENTITY 4 — IBC BVI, UBO accessible aux autorités locales
ENTITY 5 — SOPARFI Luxembourg, holding intermédiaire
ENTITY 6 — Trust BVI, settlor identifié dans Pandora
ENTITY 7 — Stiftung Liechtenstein, fondateur dans Pandora
ENTITY 8 — Société libanaise, opaque
```

Cette annotation simple oriente immédiatement la stratégie d’investigation : où sont les zones d’opacité, où sont les leviers (PSC UK), où la coopération internationale est requise.

### Mini-walkthrough — formes du réseau Haddad

- 4 SAS françaises : comptes publics, dirigeants visibles, UBO RBE (accès assujettis et autorités).
- 2 Limited UK : PSC public, comptes publics.
- 1 LLC Delaware : opacité forte, UBO inaccessible (CTA contesté).
- 1 SOPARFI Luxembourg : comptes publiés au RCS, mais structure de holding intermédiaire.
- 1 Ltd Chypre : registres limités, UBO non-public (post-CJUE).
- 1 IBC BVI : pas de comptes publics, UBO accessible aux autorités locales.
- 1 trust chypriote (identifié via Pandora) : structure non publique, settlor connu via leak.
- 2 sociétés émiraties (free zone) : registres limités.
- 1 société libanaise : informations limitées.

Une lecture : le réseau combine des **entités visibles** (UK et France, pour l’opérationnel et l’apparence légitime), des **véhicules opaques** (LLC US, IBC BVI, trust CY), et des **holdings intermédiaires** (SOPARFI Luxembourg) qui structurent le contrôle. Schéma classique d’**ingénierie offshore** sans préjuger de sa légalité.

### Erreurs fréquentes

- **Considérer toutes les formes comme équivalentes.** Une LLC Delaware ≠ une SAS française ≠ un trust BVI. Les régimes et les transparences diffèrent radicalement.
- **Confondre forme et fonction.** Une « société de holding » peut être SARL, SA, SAS, SOPARFI, LLC, BV, etc. La forme dit la structure, pas la fonction.
- **Ignorer les particularités locales** : LP écossais, SCSp luxembourgeoise, fondation panaméenne — chacune a des spécificités à connaître pour comprendre la logique du montage.

### Limites

La connaissance fine des formes juridiques de toutes les juridictions du monde dépasse les capacités d’un analyste. L’objectif est de connaître les formes courantes et d’identifier les formes spécifiques quand elles apparaissent (recherche à la demande). Les juristes spécialisés sont consultés quand un montage particulier exige une analyse poussée.

### Lien avec le fil rouge

> **CLEARFLOW — Lecture juridique du réseau**
> 
> Nassim produit une fiche par entité avec sa forme juridique et ses implications. Cette annotation lui permet, en consolidation, d’expliquer dans la note finale : *« Le réseau s’appuie sur 4 SAS françaises (front opérationnel apparent), 2 Limited UK (présence visible mais activité réelle douteuse), 1 LLC Delaware (opacité), 1 SOPARFI luxembourgeoise (holding intermédiaire), 1 société chypriote contrôlée par un trust (structure de contrôle ultime probable). Le montage est typique d’une architecture multi-juridictionnelle combinant légitimité de façade et opacité de contrôle. »*

### Points clés à retenir

- Formes courantes UE : SAS, SARL, SA, GmbH, BV, Ltd, SOPARFI.
- Formes opaques notables : LLC Delaware, IBC BVI/Cayman, fondations Liechtenstein, trusts.
- La forme oriente la transparence, la gouvernance, les obligations.
- Un graphe de réseau bien annoté en formes informe immédiatement la stratégie d’investigation.

-----

## Chapitre 22 — Dirigeants, mandataires et administrateurs

### Objectif du chapitre

Cartographier les **personnes physiques exerçant des fonctions officielles** dans une entité : présidents, gérants, directeurs généraux, administrateurs, membres du conseil de surveillance, secrétaires (UK), commissaires aux comptes, fondés de pouvoir. Identifier les profils anormaux et les patterns suspects.

### Le concept

Toute entité juridique a au moins une **personne physique** investie d’un mandat officiel — c’est le minimum pour qu’elle puisse être représentée. Ces mandats sont déclarés au registre et accessibles publiquement dans la plupart des juridictions.

**Mandats principaux selon les formes** :

- SAS française : président (et éventuellement DG, directeurs adjoints).
- SARL française : gérant(s).
- SA française : conseil d’administration (membres + président) et directeur général, OU directoire + conseil de surveillance.
- Limited UK : directors et secretary.
- GmbH allemande : Geschäftsführer.
- AG allemande : Vorstand (directoire) et Aufsichtsrat (conseil de surveillance).
- LLC américaine : member(s) ou manager(s).
- Trust : trustee(s), settlor, protecteur(s).

**Mandataires accessoires** : commissaires aux comptes (sociétés au-delà des seuils), fondés de pouvoir (pour certaines opérations), liquidateurs (en cas de procédure).

### L’utilité opérationnelle

L’analyse des mandataires permet :

1. **Identifier les acteurs déclarés** — qui répond officiellement de l’entité.
1. **Détecter les profils anormaux** — multi-mandats, retraités âgés, jeunes sans expérience.
1. **Cartographier les liens entre entités** — un même dirigeant pour plusieurs entités = lien fort de contrôle ou de coordination.
1. **Identifier les corporate service providers** — cabinets qui fournissent des mandataires professionnels (« nominee directors ») dans le cadre d’une opacification.

### Méthode — analyse des mandataires

1. **Récupérer la liste des mandataires actuels et passés** (registre).
1. **Profiler chacun** : date d’entrée en fonction, durée, autres mandats déclarés (recherche par nom), profession, profil LinkedIn.
1. **Repérer les patterns** :
- Mandataire avec 20+ mandats actifs dans des sociétés non liées sectoriellement.
- Mandataire âgé sans expérience apparente du secteur.
- Mandataire à l’adresse identique à la société.
- Mandataire d’une société de domiciliation connue.
- Rotation rapide des mandataires (changements multiples en peu de temps).
1. **Croiser avec sanctions, PEP, adverse media** (chapitre 17).

### Mini-walkthrough — analyse des mandataires CLEARFLOW

**Sur les 4 SAS françaises** :

- 2 SAS : Monsieur X comme président, en fonction depuis la création (14 à 22 mois).
- 1 SAS : Mme Z comme présidente, en fonction depuis 11 mois.
- 1 SAS : société de domiciliation comme directeur (rare en France — admis pour certaines formes).

Profilage de Monsieur X :

- LinkedIn minimal, « activité de conseil aux entreprises ».
- 8 mandats actifs identifiés dans Pappers (croisement par nom + date de naissance).
- Tous les mandats dans des SAS de commerce de gros, créées 2022-2024.
- Toutes domiciliées à la même adresse (cabinet de domiciliation).
- Aucune expérience préalable visible dans le négoce.
- 2 procédures collectives sur des sociétés antérieurement gérées (chapitre 16).

→ Profil compatible avec un **gestionnaire multi-mandats au service d’un cabinet de domiciliation**. Niveau de confiance *probable* sur la qualification prête-nom.

Profilage de Mme Z :

- LinkedIn présent, parcours d’agente commerciale dans un autre secteur (parfumerie).
- 1 seul mandat actuel.
- Adresse personnelle distincte de la société.

→ Profil moins suspect, mais à recouper avec relation potentielle à Haddad (réseau personnel).

**Sur les 2 Limited UK** :

- Director déclaré : un Libanais résidant à Dubaï, M. Y.
- PSC : même M. Y (déclaré comme exerçant contrôle significatif via droits de vote).
- Profilage : LinkedIn affichant un parcours dans le négoce libanais, lien visible avec Haddad (employé de longue date selon presse).

→ Profil compatible avec un **collaborateur de confiance** plutôt qu’un prête-nom anonyme. La qualification UBO reste à confirmer (un collaborateur peut être lui-même un prête-nom).

### Erreurs fréquentes

- **Conclure « prête-nom » sans recoupement.** Un mandataire avec plusieurs mandats peut être un gestionnaire légitime (cabinet d’expertise comptable, par exemple).
- **Ignorer les commissaires aux comptes.** Le choix d’un CAC reconnu vs un CAC inconnu peut être un signal.
- **Ne pas chercher les mandats antérieurs.** Les anciennes fonctions racontent l’histoire de la personne.

### Limites

Les registres sont déclaratifs. Un mandataire peut être nominalement en fonction sans exercer réellement le contrôle. Inversement, le contrôle réel peut être exercé par une personne sans mandat déclaré (chapitre 23 sur le contrôle indirect).

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des mandataires**
> 
> Nassim produit un tableau croisé : 12 personnes physiques exercent des mandats dans les 14 entités du réseau. 5 de ces personnes ont 3+ mandats, dont Monsieur X (gestionnaire français multi-mandats, profil prête-nom probable) et M. Y (libanais à Dubaï, collaborateur de confiance probable). Aucune n’est Karim Haddad lui-même : il **n’apparaît dans aucun mandat officiel** des entités françaises et UK du dossier. Ce constat est important — cela conforte l’hypothèse d’un contrôle indirect (chapitre 23) plutôt que d’une gestion directe.

### Points clés à retenir

- Tous les mandataires des entités cibles sont à profiler.
- Patterns suspects : multi-mandats, profils inadaptés, adresses partagées, rotation rapide.
- Mandataire déclaré ≠ contrôle réel — vérifier par croisement avec UBO.
- Une cartographie « mandataires × entités » est l’un des livrables les plus utiles d’une enquête FININT.

-----

## Chapitre 23 — Actionnaires, UBO et contrôle indirect

### Objectif du chapitre

Comprendre la **chaîne du contrôle** : actionnaires immédiats, sociétés interposées, UBO de dernier niveau, mécanismes de contrôle indirect au-delà du capital (conventions, usufruit, options, conventions de vote).

### Le concept

Trois niveaux à distinguer :

1. **Actionnariat / association** : qui détient les titres ou les parts au capital de l’entité — souvent une autre société, parfois une personne physique directement.
1. **UBO** : qui contrôle ultimement (personne physique). Peut être direct (actionnaire personne physique) ou indirect (via chaîne de sociétés, trusts, conventions).
1. **Contrôle effectif** : qui décide réellement — peut être différent de l’UBO de droit. Par exemple, un actionnaire majoritaire qui a délégué le contrôle par convention à un tiers.

**Mécanismes de contrôle indirect** :

- **Chaîne de holdings** : société A détenue par société B, elle-même détenue par société C, elle-même détenue par M. X. Le contrôle est traçable mais demande à remonter la chaîne.
- **Trusts** : la société est détenue par un trust. Le settlor a apporté les actifs ; le trustee les gère ; les bénéficiaires en jouissent. Le contrôle peut être chez le settlor (trust révocable), chez le trustee (trust irrévocable), ou ailleurs (protecteur).
- **Fondations** : entité juridique qui détient les titres. Le fondateur a apporté ; le conseil de fondation gère ; les bénéficiaires en jouissent.
- **Nominees** : prête-noms officiels (déclarés comme tels en common law).
- **Conventions de vote** : un actionnaire minoritaire peut contrôler par convention si la majorité accepte de voter selon ses instructions.
- **Usufruit** : démembrement de propriété. Le nu-propriétaire détient le capital ; l’usufruitier exerce les droits.
- **Options et promesses de vente** : un investisseur peut avoir une option d’achat lui permettant de prendre le contrôle à tout moment.
- **Pactes d’actionnaires** : conventions privées qui modulent les droits formels.
- **Démembrement entre associés** : un dirigeant détient peu mais a une convention lui donnant un pouvoir étendu.

### L’utilité opérationnelle

L’analyste cherche à répondre à : **qui contrôle réellement cette entité, et avec quel niveau de confiance ?**

Cela conditionne :

- L’identification du véritable décideur ;
- La compréhension de la stratégie économique ;
- L’attribution des responsabilités ;
- Le ciblage des coopérations et réquisitions.

### Méthode — remonter la chaîne

1. **Identifier les associés immédiats** (registre, statuts).
1. **Pour chaque associé personne morale, remonter** : qui sont ses associés ? (récursion).
1. **Arriver à une personne physique** OU **arriver à une structure opaque** (trust, IBC offshore sans accès).
1. **Mobiliser les leaks** (chapitre 18) si arrêt sur structure opaque.
1. **Mobiliser la coopération internationale** si toujours bloqué.
1. **Calibrer la confiance** : UBO de droit identifié ≠ UBO réel automatique. Le contrôle effectif peut résider ailleurs (conventions, options, pacte).

### Mini-walkthrough — chaîne CLEARFLOW (partielle)

Sur une des SAS françaises, NEXUS TRADING SAS :

- Associé unique au capital : NEXUS HOLDINGS LTD (Chypre).
- NEXUS HOLDINGS LTD : actionnaire majoritaire = OMEGA HOLDINGS TRUST (trust chypriote).
- OMEGA HOLDINGS TRUST : settlor = Karim Élie Haddad (identifié via Pandora Papers, chapitre 18). Trustee : cabinet professionnel chypriote (corporate service provider). Bénéficiaires : « la famille Haddad » (formulation typique d’un trust patrimonial — flou volontaire).

Chaîne : NEXUS FR ← NEXUS CY ← OMEGA TRUST ← Karim Haddad (settlor + bénéficiaire probable).

Niveau de confiance :

- Sur la chaîne juridique : *quasi-certain* (registres + leak).
- Sur l’identification de Haddad comme UBO réel : *probable* à *quasi-certain* selon recoupements ultérieurs (analyse de flux, contrôle effectif observable).

Lacunes : la formulation « famille Haddad » dans les bénéficiaires masque le pourcentage et la nature exacte du contrôle. Une coopération avec Mokas (CRF chypriote) serait nécessaire pour clarifier.

### Erreurs fréquentes

- **S’arrêter au premier niveau.** Identifier un associé personne morale sans remonter = travail incomplet.
- **Confondre actionnaire principal et UBO.** Un actionnaire détenant 24,9 % peut ne pas être UBO au sens UE (seuil 25 %), mais peut être UBO de fait par convention.
- **Ignorer le contrôle effectif.** Les statuts juridiques ne disent pas toujours qui dirige réellement.

### Limites

Lorsque la chaîne aboutit à une **structure opaque** (trust offshore, IBC sans accès), l’identification de l’UBO réel reste *probable* au mieux sur la base d’OSINT seul. La coopération internationale est nécessaire pour passer à *quasi-certain*.

### Lien avec le fil rouge

> **CLEARFLOW — Mapping du contrôle**
> 
> En remontant systématiquement chaque chaîne, Nassim aboutit à 4 « racines » principales du réseau : Karim Haddad (settlor du trust chypriote, UBO probable de plusieurs entités), un proche collaborateur basé à Dubaï (M. Y, PSC de plusieurs Limited UK), une fondation libanaise (rôle réel non clarifié), et un cabinet de trustees professionnel (mandant véritable inconnu — possible interposition supplémentaire). Cette carte du contrôle est l’un des livrables les plus stratégiques de la note.

### Points clés à retenir

- Distinguer associés / UBO / contrôle effectif.
- Remonter systématiquement la chaîne jusqu’à une personne physique ou une structure opaque.
- Mécanismes de contrôle indirect : trusts, fondations, nominees, conventions, options, usufruit.
- Niveau de confiance à calibrer à chaque étape de la chaîne.

-----

## Chapitre 24 — Holdings, filiales et montages en cascade

### Objectif du chapitre

Comprendre la **logique économique** des montages en cascade (holding mère, filiales, sous-filiales), distinguer les montages légitimes des montages à finalité d’opacification ou d’optimisation discutable.

### Le concept

Un **groupe** est un ensemble d’entités juridiques distinctes liées par des liens de capital ou de contrôle. La structuration typique :

- **Holding ultime** (parfois nommée « top holding ») — détient les autres entités.
- **Sous-holdings intermédiaires** — fonctions spécifiques (financement, gestion d’actifs, opérations dans une juridiction).
- **Filiales opérationnelles** — entités qui réalisent l’activité économique réelle.

**Pourquoi des holdings ?** Plusieurs raisons, légitimes et moins légitimes :

- **Optimisation fiscale légale** : régimes mère-filles, exonération des dividendes intra-groupe, traités fiscaux.
- **Séparation juridique des risques** : une activité risquée dans une filiale dédiée, protégée des autres.
- **Gouvernance** : structuration par métier, par géographie.
- **Pré-IPO ou opérations corporate** : préparer une cession ou une introduction en bourse.
- **Opacification** : ajouter des couches pour rendre le contrôle moins lisible.
- **Évitement fiscal agressif** : combinaisons exploitant les failles de traités (treaty shopping).
- **Blanchiment** : couches successives complexifiant le suivi des fonds (layering).

### L’utilité opérationnelle

L’analyste cherche à comprendre :

- **La logique économique** du montage. Est-ce cohérent avec l’activité (groupe international légitime avec présence dans plusieurs pays) ou disproportionné (3 holdings pour une activité de PME locale) ?
- **Les juridictions choisies** et leur sens (chapitre 10) : Luxembourg pour holding (régime mère-filles favorable), Pays-Bas pour la même raison, Suisse pour la banque privée, BVI pour l’opacité, etc.
- **Les flux intra-groupe** : management fees, redevances de marque, prêts intragroupe, dividendes — autant de canaux pour faire circuler la valeur de manière préférentielle.
- **Les filiales dormantes** : présentes mais sans activité — coquilles à recycler ou réserves stratégiques.

### Méthode — analyse d’un montage en cascade

1. **Construire le graphe** : qui détient qui, à quel pourcentage, dans quelle juridiction.
1. **Annoter chaque entité** : forme juridique, juridiction, activité déclarée, CA, effectif si connu.
1. **Identifier les flux intra-groupe** dans les comptes consolidés ou par les conventions visibles (notes annexes).
1. **Détecter les anomalies** : couches sans justification économique, juridictions opaques sans rationale, holdings sans substance économique.
1. **Calibrer** : montage cohérent avec activité internationale légitime ? Disproportionné ? Compatible avec optimisation fiscale agressive ? Avec opacification ?

### Mini-walkthrough — montage Haddad

Cartographie progressive :

```
Karim Haddad (UBO probable)
  └─ OMEGA HOLDINGS TRUST (Chypre)
        └─ NEXUS HOLDINGS LTD (Chypre)
              ├─ NEXUS TRADING SAS (France) — opérations
              ├─ NEXUS INTERNATIONAL FZ (Émirats, free zone) — siège commercial
              ├─ NEXUS LOGISTICS LTD (UK) — logistique apparente
              ├─ NEXUS DELAWARE LLC (US, Delaware) — opacité
              └─ SOPARFI LUX SARL (Luxembourg) — holding intermédiaire
                    ├─ NEXUS NEGOCE SARL (Côte d'Ivoire) — opérations Afrique
                    └─ NEXUS LIBAN SAL (Liban) — racine régionale
```

Lecture FININT :

- **Top holding** : trust chypriote (opacification + planification patrimoniale plausible).
- **Sous-holding chypriote** : NEXUS HOLDINGS LTD — intermédiaire commercial typique.
- **Filiales opérationnelles** : SAS France, FZ Émirats, Limited UK — couvrent les zones d’activité commerciale.
- **Coquille opaque** : LLC Delaware — pas d’activité visible, fonction inconnue (à investiguer).
- **Sous-holding luxembourgeois** : SOPARFI — point intermédiaire pour les filiales africaines.
- **Filiales africaines et libanaise** : opérations locales.

Lacunes : substance économique réelle des holdings non-opérationnels (NEXUS HOLDINGS CY, SOPARFI LUX, LLC Delaware) ? Présence de personnel ? Locaux ? Cette substance distingue un montage légitime (présence économique réelle dans chaque juridiction) d’un montage de pure interposition.

Hypothèses :

- **H1 — Montage de structuration légitime** : groupe familial international avec présence multi-juridictionnelle légitime, optimisation fiscale aux limites du légal. *Possible.*
- **H2 — Montage d’opacification et d’optimisation agressive** : couches sans substance économique réelle, ingénierie pour brouiller le contrôle et minimiser la fiscalité. *Probable.*
- **H3 — Montage incluant des éléments de blanchiment** : certaines entités servent au transit de fonds illicites. *Possible, à confirmer par l’analyse de flux.*

### Erreurs fréquentes

- **Confondre montage complexe et illégalité.** Beaucoup de groupes internationaux légitimes ont des montages très complexes.
- **Surinterpréter une juridiction.** Le Luxembourg est une juridiction européenne respectée ; sa présence n’est pas un signal d’illégalité en soi.
- **Ne pas chercher la substance économique** : la présence/absence de personnel, locaux, activité opérationnelle réelle distingue le légitime du fictif.

### Limites

La substance économique des holdings offshore est souvent **invisible à l’OSINT seul**. La coopération internationale (CRF locales) ou les rapports sectoriels publiés sont nécessaires.

### Lien avec le fil rouge

> **CLEARFLOW — Architecture du groupe**
> 
> Nassim conclut, après cartographie complète : le montage Haddad est **disproportionné** par rapport à l’activité commerciale visible (négoce de matériel agricole et services). Plusieurs entités sont des coquilles probables. La présence du trust chypriote au sommet et de la LLC Delaware en branche latérale sont des signaux d’opacification. Le SOPARFI luxembourgeois pourrait être légitime (régime mère-filles) ou pourrait être une couche additionnelle d’optimisation agressive. La qualification globale du montage : *probable* opacification, *possible* implication dans des schémas illicites — à confirmer par l’analyse de flux (Partie VI).

### Points clés à retenir

- Les montages en cascade ont des justifications légitimes et illégitimes.
- Analyser : juridictions, substance économique, flux intra-groupe.
- Distinguer optimisation légale, optimisation agressive, opacification, blanchiment.
- La substance économique est souvent la clé.

-----

## Chapitre 25 — Trusts, fondations, nominees et prête-noms

### Objectif du chapitre

Maîtriser les **structures de détention indirecte** : trusts, fondations privées, nominees, prête-noms — leurs mécanismes, leurs usages légitimes, leur exploitation dans l’opacification, et leur lecture en enquête FININT.

### Le concept

**Trust** (common law). Une relation juridique tripartite :

- **Settlor** (constituant) : la personne qui apporte les actifs au trust.
- **Trustee** : la personne (physique ou morale, souvent un trust company) qui détient et gère légalement les actifs au profit des bénéficiaires.
- **Bénéficiaires** : personnes (nommées ou non) qui jouissent des actifs (revenus ou capital, selon les termes).
- **Protecteur** (parfois) : tiers chargé de surveiller le trustee et/ou de modifier le trust.

**Types de trusts** :

- **Trust révocable** : le settlor peut révoquer et récupérer les actifs. Faible opacification ; les actifs restent attribuables.
- **Trust irrévocable** : le settlor ne peut plus récupérer. Opacification renforcée ; mais le settlor est généralement listé.
- **Trust discrétionnaire** : le trustee a un pouvoir discrétionnaire sur la distribution. Souvent utilisé pour des montages opaques (qui sont les bénéficiaires effectifs ? le trustee décide).
- **Trust avec lettre de souhait** : le settlor laisse une « letter of wishes » non contraignante au trustee — outil d’opacification fréquent.

**Juridictions de trust** : UK, US, BVI, Cayman, Bahamas, Jersey, Guernsey, Île de Man, Singapour, Hong Kong, Suisse (admis depuis 2007 sous certaines conditions), New Zealand.

**Fondation privée** (droit continental). Entité juridique distincte. Mécanisme similaire au trust mais juridiquement différent :

- **Fondateur** : apporte les actifs.
- **Conseil de fondation** : gère.
- **Bénéficiaires** : reçoivent.

**Juridictions de fondations privées** : Liechtenstein (Stiftung), Panama, Pays-Bas (Stichting), Autriche, Suisse, certaines juridictions caribéennes.

**Nominee**. Prête-nom **officiel**, déclaré comme tel. Mécanisme courant en common law (nominee director, nominee shareholder). Le nominee détient au nom d’un bénéficiaire qu’il représente. La relation est formalisée par un contrat (declaration of trust, nominee agreement).

**Prête-nom (en droit continental)**. Personne qui apparaît officiellement comme dirigeant ou associé sans l’être réellement. À la différence du nominee, la relation est **dissimulée** dans la plupart des juridictions de droit continental. En France, le prête-nom est illicite quand il vise à frauder.

### L’utilité opérationnelle

L’analyste doit savoir :

- **Identifier la présence** d’une telle structure dans une chaîne de contrôle (chapitre 23).
- **Comprendre les rôles** : qui est settlor / fondateur / trustee / bénéficiaire.
- **Identifier les UBO réels** : selon les directives AML, ce sont (pour les trusts) le settlor, les trustees, les protecteurs, les bénéficiaires identifiés ou la classe, et toute personne contrôlant.
- **Détecter les prête-noms** : signaux d’incohérence entre profil et fonction.

### Méthode — analyser une structure de détention indirecte

1. **Récupérer les actes** quand accessibles (trust deed, statuts de fondation) — souvent indisponibles en sources ouvertes, possibles en leaks (Pandora particulièrement riche).
1. **Identifier les acteurs déclarés** : settlor, trustee, bénéficiaires, protecteurs.
1. **Profiler chacun** : le trustee est-il un cabinet professionnel ? Quels autres trusts gère-t-il ? Le settlor est-il visible publiquement ?
1. **Croiser avec leaks et presse** : Pandora et Paradise Papers contiennent souvent les éléments de trusts non publics.
1. **Identifier les bénéficiaires** : nommés ou catégorie ? Si « famille X », identifier les membres.
1. **Calibrer** : qui contrôle réellement ? Réversibilité ? Liens visibles entre settlor et bénéficiaires ?

**Détecter un prête-nom (signaux probabilistes)** :

- **Profil incohérent** : retraité de 80 ans dirigeant 7 SAS de négoce.
- **Absence d’expérience visible** dans le secteur.
- **Réseau personnel pauvre** sur LinkedIn et réseaux sociaux par rapport aux mandats officiels.
- **Domiciliation à l’adresse de la société** ou d’un cabinet de domiciliation.
- **Multi-mandats** dans des secteurs sans cohérence.
- **Rotation rapide** des mandats (entrées et sorties multiples).
- **Lien capillaire avec un autre acteur** identifié comme contrôleur réel possible.

Aucun de ces signaux ne suffit. **Plusieurs convergents** justifient le qualificatif *probable* prête-nom — jamais *quasi-certain* sans éléments documentaires (témoignages, actes contestés, aveux).

### Mini-walkthrough — OMEGA HOLDINGS TRUST

- Identification dans Pandora Papers (chapitre 18) : trust chypriote constitué en 2019.
- **Settlor** : Karim Élie Haddad, identifié.
- **Trustee** : Cabinet Pancyprian Trustees Ltd (Chypre) — cabinet professionnel, identifié comme administrateur de plusieurs centaines de trusts dans Pandora.
- **Bénéficiaires** : « the family of the settlor » — formulation vague, à étendre.
- **Protecteur** : non identifié dans les documents disponibles.
- Type : trust irrévocable, mais avec letter of wishes mentionnée dans le trust deed (les souhaits du settlor sont à respecter par le trustee).

Lecture FININT : structure typique d’un trust patrimonial à finalité d’opacification du contrôle. Le settlor est identifié *quasi-certain* (leak Pandora). Le contrôle effectif est *probable* chez le settlor (letter of wishes), avec autonomie nominale du trustee. Les bénéficiaires (famille Haddad) restent à identifier précisément — recherche presse et OSINT sur l’entourage familial.

### Erreurs fréquentes

- **Considérer tout trust comme illégal.** Les trusts sont des outils juridiques largement utilisés et légitimes, notamment en droit anglo-saxon (planification successorale, protection des incapables, donations conditionnelles, etc.).
- **Considérer tout prête-nom comme volontaire.** Certaines personnes peuvent être *abusées* (mules, identités usurpées).
- **Confondre nominee et prête-nom illicite.** Le nominee anglo-saxon est légal s’il est correctement déclaré.

### Limites

La structure interne d’un trust ou d’une fondation est généralement **non publique** en l’absence de leak. La coopération internationale est nécessaire pour obtenir le trust deed, la liste des bénéficiaires, les distributions effectuées.

### Lien avec le fil rouge

> **CLEARFLOW — Trust et prête-noms**
> 
> Nassim consolide : OMEGA TRUST = structure de contrôle ultime du réseau Haddad, settlor identifié, contrôle effectif probable. En parallèle, Monsieur X et 3 autres mandataires français sont *probables* prête-noms (profils convergents avec multi-mandats, cabinet de domiciliation, absence d’expérience sectorielle). Mme Z, présidente d’une SAS, n’est pas *probable* prête-nom — son profil est différent et un recoupement avec le réseau personnel de Haddad (presse libanaise antérieure) montre un lien amical. Hypothèse Mme Z : présidente nominale avec lien personnel à Haddad, sans qualification certaine de prête-nom. Calibration *possible*.

### Points clés à retenir

- Trust : settlor + trustee + bénéficiaires + (protecteur). Fondation : fondateur + conseil + bénéficiaires.
- Tous les rôles sont, selon la 4e/5e directive AML, à considérer comme UBO.
- Prête-noms : détecter par convergence de signaux faibles, jamais sur un seul indice.
- Sources : leaks (Pandora particulièrement), coopération internationale.

-----

## Chapitre 26 — Sociétés écrans et sociétés dormantes

### Objectif du chapitre

Comprendre la notion de **société écran**, distinguer les **sociétés dormantes**, et caractériser quand une structure est probablement écran sur la base d’un faisceau d’indices.

### Le concept

**Société écran** (shell company). Notion ambiguë. En sens strict : entité juridique sans activité économique réelle, sans personnel, sans actifs autres que les titres de la société, créée pour porter une finalité spécifique sans substance opérationnelle propre.

**Société de façade**. Entité avec une activité économique de façade (apparente) mais dont la véritable fonction est tout autre (canal de blanchiment, fraude, etc.).

**Société dormante**. Entité existante mais qui n’exerce plus d’activité, ni de manière à façade. Distinct de la société écran : dormante = inactive, écran = active mais sans substance économique propre.

**Société boîte aux lettres** (mailbox company, letterbox company). Entité avec une simple adresse de domiciliation, sans présence opérationnelle. Souvent synonyme de société écran selon les contextes.

**Important** : toutes les sociétés écrans **ne sont pas illégales**. Beaucoup ont des usages légitimes :

- Holding de gestion patrimoniale.
- Véhicule de financement (SPV — Special Purpose Vehicle).
- Société de portage temporaire (M&A).
- Société pré-IPO.
- Société pour acquisition immobilière (SCI, REIT, etc.).

**Société écran à finalité illicite** : créée pour dissimuler des transactions, opacifier une chaîne, fictivement justifier des flux, ou frauder.

### L’utilité opérationnelle

L’analyste cherche à qualifier : cette entité est-elle une société écran ? Si oui, à quelle finalité (légitime ou illicite) ?

**Indices d’écran à finalité illicite** :

1. **Absence de substance économique** : pas de personnel, pas de locaux propres, pas d’activité visible.
1. **Adresse de domiciliation** partagée avec de nombreuses autres entités.
1. **Dirigeant unique** avec multi-mandats (signal prête-nom probable).
1. **Création récente** (souvent juste avant la transaction d’intérêt).
1. **Capital social minimal** (1 €, 100 €, 10 000 €).
1. **Comptes non publiés** ou publiés en retard, ou « confidentiels » dès l’origine.
1. **Activité déclarée** (NAF/SIC code) très large et vague (« commerce de gros non spécialisé », « activités de holding »).
1. **Pas de présence web** ou site web vide / générique.
1. **Pas de comptes bancaires identifiables** dans la juridiction du siège, ou banque exotique disproportionnée.
1. **Transactions disproportionnées** avec la taille apparente (CA en M€ avec 1 employé et 1 € de capital).
1. **Liens avec d’autres entités du même profil** (cluster de coquilles).
1. **Présence dans des leaks** (Panama, Pandora) ou dans des bases adverse media.

Aucun indice n’est suffisant ; **plusieurs convergents** qualifient *probable* écran ; **beaucoup convergents + recoupements** approchent du *quasi-certain*.

### Méthode — qualification d’une société écran

1. **Profil de base** : registre, comptes, dirigeants, UBO.
1. **Substance économique** : personnel ? locaux ? site web ? clientèle ? fournisseurs ?
1. **Cohérence sectorielle** : flux compatibles avec activité déclarée ?
1. **Liens à d’autres entités** : appartenance à un cluster ?
1. **Adresse de domiciliation** : combien d’autres sociétés à la même adresse ?
1. **Cumul d’indices** : 5+ indices convergents = *probable* écran.
1. **Calibrer la finalité** : écran légitime (holding patrimonial, SPV) ou écran suspect (canal de blanchiment, fraude, transit fictif) ?

### Mini-walkthrough — NEXUS DELAWARE LLC

- Registre : LLC enregistrée à Delaware en 2022. UBO non accessible (CTA contesté).
- Substance économique : pas de personnel public, pas de site web, pas de présence physique identifiable.
- Adresse de domiciliation : un service de registered agent partagé avec des milliers d’autres LLC Delaware (standard, sans valeur diagnostique en soi).
- Activité : non identifiable.
- Comptes : non publiés (Delaware LLC, exemption).
- Flux observables (via DS) : 850 K€ reçus depuis Chypre, 800 K€ transférés vers un compte personnel suisse. Quelques jours d’écart.
- Lien à d’autres entités : appartient à la chaîne NEXUS du réseau Haddad.

Cumul d’indices : opacité, absence de substance visible, activité non identifiable, flux disproportionnés, cluster d’entités liées. *Probable* société écran à finalité de transit. La finalité (blanchiment ? optimisation ? simple holding ?) reste à confirmer par l’analyse globale des flux et la coopération.

### Erreurs fréquentes

- **Qualifier « société écran » trop facilement.** Beaucoup de PME légitimes ont peu de personnel, un site web minimaliste, une faible présence en ligne.
- **Ignorer les usages légitimes** : SPV, holdings patrimoniaux, sociétés en cours de création.
- **Confondre dormante et écran.** Une société dormante peut être un actif stratégique non frauduleux.
- **Conclure sans cumul d’indices.** Un seul indice ne suffit jamais.

### Limites

La qualification *quasi-certaine* d’écran à finalité illicite exige presque toujours des éléments judiciaires (réquisition des relevés bancaires montrant absence d’activité réelle, audition du dirigeant). L’analyste OSINT s’arrête à *probable*.

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des écrans probables**
> 
> Sur les 14 entités du réseau Haddad, Nassim qualifie : 4 SAS françaises = *possible* écran (substance économique faible, mais activité commerciale apparente — nécessite confirmation par analyse de flux), NEXUS DELAWARE LLC = *probable* écran de transit, 2 Limited UK = *possible* écran (activité commerciale apparente mais déconnectée du réel à confirmer), entités libanaise et émiraties = données insuffisantes (*indéterminable*). Conclusion : présence d’écrans probables à des fins minimum d’opacification ; finalité illicite *possible* à *probable* selon la confirmation par les flux.

### Points clés à retenir

- Société écran ≠ illégale par nature. Beaucoup d’usages légitimes.
- Société dormante ≠ écran.
- Qualification par **cumul d’indices** : substance économique, personnel, locaux, activité, cohérence, cluster.
- L’analyste OSINT atteint *probable*, rarement *quasi-certain* sans éléments judiciaires.

-----
