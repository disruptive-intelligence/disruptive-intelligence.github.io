---
title: PARTIE III — SOURCES OSINT FINANCIÈRES
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 4
chapters: 11
---

*Huit chapitres pour la cartographie complète des sources ouvertes financières — registres, comptes annuels, marchés publics, contentieux, presse, leaks, SOCMINT financier. Cette partie est la plus volumineuse de la phase « pré-réquisitions » d’une enquête.*

-----

## Chapitre 11 — Registres d’entreprises : France, UK, US

### Objectif du chapitre

Maîtriser les **trois principaux registres** que tout analyste FININT consulte régulièrement : France (Infogreffe / INPI), Royaume-Uni (Companies House), États-Unis (registres fédéraux et étatiques, principalement Delaware, et SEC EDGAR pour les sociétés cotées).

### Le concept

Un **registre du commerce et des sociétés** est la base officielle qui recense les entités juridiques d’un pays, leurs caractéristiques (forme, capital, dirigeants, siège), et publie certains actes (statuts, modifications, comptes annuels selon les seuils). C’est la source de premier niveau pour identifier une entité et pour ouvrir une enquête.

Tous les registres ne sont pas équivalents en richesse, en accessibilité et en gratuité. Trois pôles dominent les enquêtes occidentales modernes.

### France — INPI / Infogreffe / RCS

Architecture actuelle (2025) :

- **INPI (Registre national des entreprises — RNE)** : depuis 2023, l’INPI centralise le RNE, qui regroupe les informations historiquement réparties entre RCS (commerçants) et autres registres (artisans, agricoles, libéraux). Accès gratuit et public à beaucoup de données via [data.inpi.fr](https://data.inpi.fr/) et le portail RNE.
- **Infogreffe** : portail des greffes de tribunaux de commerce. Accès payant pour certains actes, gratuit pour la fiche identité. Toujours utilisé en pratique pour les **actes** (statuts, comptes annuels, K-bis officiel).
- **Pappers** : agrégateur tiers gratuit, très ergonomique, qui republie une grande partie des données ouvertes (siret, dirigeants, comptes annuels jusqu’aux seuils, liens entre sociétés). Devenu un réflexe d’analyste.
- **Société.com, Verif.com, Manageo, Score3** : agrégateurs concurrents avec degrés de gratuité variables.
- **BODACC** (Bulletin officiel des annonces civiles et commerciales) : publications officielles (créations, radiations, procédures collectives). Accès gratuit en ligne.

**Ce que l’analyste obtient gratuitement :**

- Identification : SIREN/SIRET, dénomination, forme juridique, capital social, date de création, NAF/APE.
- Adresse du siège, et historique des sièges.
- Dirigeants : président, gérant, DG, directeurs, administrateurs (avec dates de nomination et de fin).
- Liste des établissements secondaires.
- Procédures collectives : sauvegarde, redressement, liquidation.
- Modifications du registre (changements de dénomination, de capital, de dirigeants, transferts de siège).
- **Comptes annuels** publiés (sociétés au-delà des seuils, dans la limite du droit à confidentialité demandé par certaines petites sociétés depuis 2014).

**Pour aller plus loin (réquisition / accès professionnel) :** liste des associés (rarement publique), informations bancaires.

### Royaume-Uni — Companies House

[Companies House](https://www.gov.uk/government/organisations/companies-house) — registre officiel UK. C’est l’un des registres **les plus ouverts au monde**. Accès gratuit et complet à :

- Identification de la société (Company Number, denomination, forme, statut).
- Officers (directors, secretaries) — actuels et historiques, avec dates et adresses.
- **Persons with Significant Control (PSC)** — depuis 2016, le UK rend public le registre des personnes exerçant un contrôle significatif (équivalent UBO). Seuils : 25 % de capital ou de droits de vote, ou contrôle effectif. Accessible en ligne, gratuit, par société.
- Comptes annuels (filings) publiés pour la quasi-totalité des sociétés actives.
- Confirmations annuelles (Annual Confirmation Statement).
- Mortgages and charges (sûretés inscrites).

Cas particuliers : LLP (Limited Liability Partnership), Scottish Limited Partnership (SLP — historiquement utilisées pour le blanchiment, soumises au PSC depuis 2017).

**Limites du PSC** : déclaratif. Les fraudeurs déclarent parfois faux. Les sanctions pour fausse déclaration existent mais sont peu appliquées en pratique pour les petites entités. Reste, pour l’analyste FININT, l’une des sources les plus utiles au monde.

### États-Unis — Delaware, SEC EDGAR, registres étatiques

Les US n’ont pas de registre fédéral des sociétés. Chaque État a son propre registre. Les principaux :

- **Delaware Division of Corporations** — siège juridique d’environ 60 % des sociétés cotées américaines et de la majorité des LLC US. La consultation publique est très limitée : nom, statut, type, et c’est à peu près tout. Pas de dirigeants publics. Pas d’UBO public (en attente de la mise en œuvre du **Corporate Transparency Act** — voir infra).
- **California Secretary of State, New York Department of State, Texas, Florida, Wyoming, Nevada** — chacun a son portail.
- **OpenCorporates** — agrégateur qui aspire les registres étatiques et offre une recherche unifiée. Très utile pour l’analyste FININT.

**SEC EDGAR** : pour les **sociétés cotées** ou émettrices de titres aux US, la SEC (Securities and Exchange Commission) publie via [EDGAR](https://www.sec.gov/edgar) les déclarations détaillées (10-K, 10-Q, 8-K, S-1, proxy statements, etc.). Source d’or pour les grandes entreprises et leurs filiales.

**Corporate Transparency Act (CTA)** : loi US de 2021 ayant obligé les LLC et corporations à déclarer leurs UBO à FinCEN. Trajectoire très instable en 2024-2025 (contestations judiciaires, décisions successives). **Depuis l’interim final rule FinCEN de mars 2025**, les sociétés domestiques américaines (« domestic reporting companies ») **ne sont plus tenues** de déclarer leurs bénéficiaires effectifs à FinCEN ; l’obligation subsiste principalement pour **certaines entités étrangères enregistrées pour faire des affaires aux États-Unis**. La situation reste sujette à évolution (textes, décisions, contentieux) — un analyste consulte la mise à jour la plus récente sur le site FinCEN avant toute conclusion.

**FinCEN files** : le leak FinCEN 2020 (BuzzFeed/ICIJ) a révélé que les SAR américains contenaient des éléments sur la criminalité financière mondiale. Pas une source courante mais à connaître (Chapitre 18).

### L’utilité opérationnelle

Pour la majorité des dossiers FININT impliquant des entités françaises, britanniques ou américaines (cotées), ces trois registres couvrent l’essentiel du travail d’identification et de cartographie de premier niveau. La gratuité française et britannique permet un travail systématique sans budget. La gratuité partielle américaine est compensée par les agrégateurs (OpenCorporates) et SEC EDGAR pour les cotées.

### Méthode — workflow d’identification

1. **France** : Pappers (vue rapide) + INPI/RNE (validation officielle) + Infogreffe (acte officiel si besoin) + BODACC (procédures).
1. **UK** : Companies House (everything) + recherche par directeur/PSC pour identifier les autres sociétés liées.
1. **US** : OpenCorporates (vue agrégée) + registre étatique pertinent (validation) + SEC EDGAR si coté + FinCEN si CTA en vigueur.

Toujours **archiver** les pages consultées (capture d’écran horodatée, hash si possible — chapitre 53).

### Mini-walkthrough

Cible : *« NEXUS TRADING SAS, suspectée d’être une société écran française liée à un réseau franco-libanais. »*

- Pappers : SIREN, dénomination, capital 10 000 €, créée il y a 14 mois, dirigeant unique « Monsieur X », adresse à un cabinet de domiciliation, NAF 4690Z (commerce de gros non spécialisé). Comptes non publiés (1er exercice non clos).
- INPI : confirme + accès aux statuts initiaux.
- BODACC : aucune procédure.
- Recherche par dirigeant : Monsieur X est gérant de 7 autres SAS, toutes domiciliées à la même adresse, toutes créées entre 2023 et 2024, toutes en commerce de gros. **Pattern clair de gestionnaire multi-sociétés**.

Conclusion : à ce stade, NEXUS est **possible-à-probable** une société de façade ou un véhicule à usage spécifique. Le statut de « société écran » exige des éléments complémentaires (chapitre 26).

### Erreurs fréquentes

- **Se fier uniquement à Pappers** sans aller voir les actes officiels (Pappers est utile mais peut être en retard sur certaines mises à jour).
- **Ignorer le BODACC** (les procédures collectives sont parfois la clé d’un dossier).
- **Oublier les agrégateurs internationaux** (OpenCorporates) quand l’enquête sort de France.
- **Ne pas archiver** : un registre peut être modifié ou une fiche supprimée. La capture horodatée fait foi.

### Limites

Les registres sont **déclaratifs**. Les fraudeurs peuvent fausser les déclarations. Les modifications sont parfois en retard. L’UBO déclaré peut être un prête-nom. Croiser systématiquement avec d’autres sources.

### Lien avec le fil rouge

> **CLEARFLOW — Cartographie initiale via registres**
> 
> Sur les 14 sociétés présumées liées à Haddad, Nassim identifie 4 SAS françaises via Pappers/INPI, 2 Limited UK via Companies House (avec PSC pointant deux personnes physiques distinctes — possible alignement de prête-noms), et 1 LLC Delaware via OpenCorporates (pas d’UBO accessible — limite documentée). Le travail registre prend environ 6 heures pour cette première vague et produit un premier graphe de liens (chapitre 31).

### Points clés à retenir

- France : INPI/RNE + Pappers + Infogreffe + BODACC. Largement gratuit.
- UK : Companies House. Gratuit, riche, avec PSC.
- US : OpenCorporates + registres étatiques + SEC EDGAR. CTA à suivre.
- Toujours archiver. Toujours croiser.

-----

## Chapitre 12 — Registres d’entreprises : reste de l’Europe et du monde

### Objectif du chapitre

Étendre la couverture aux **autres juridictions clés** : reste de l’UE, Suisse, juridictions offshore, pays émergents. La logique reste la même qu’au chapitre 11 ; les outils et les degrés d’ouverture varient.

### Le concept

Hors France/UK/US, l’analyste mobilise plusieurs niveaux de sources :

1. **Registres nationaux directs** quand ils sont accessibles en ligne et en langue exploitable.
1. **Portails européens consolidés** (e-Justice, BRIS).
1. **Agrégateurs tiers** (OpenCorporates, Sayari, Orbis, Dun & Bradstreet — chapitres 50-51).
1. **Bases UBO européennes** (chapitre 13).

### Méthode — registres clés par juridiction

**Allemagne — Handelsregister**. [handelsregister.de](https://www.handelsregister.de/) ou portail unifié. Accès payant à de nombreux actes mais informations de base souvent gratuites. La structure (GmbH, AG, KG, OHG) doit être maîtrisée (chapitre 21). Bundesanzeiger pour les comptes annuels publiés.

**Italie — Registro Imprese**. [registroimprese.it](https://www.registroimprese.it/) — via les chambres de commerce. Payant. La société italienne est riche en formes (S.p.A., S.r.l., S.a.s., S.n.c., cooperativa).

**Espagne — Registro Mercantil Central** (RMC). Accès en ligne payant ; agrégateurs (Axesor, Einforma) fournissent des données plus accessibles.

**Belgique — Banque-Carrefour des Entreprises (BCE / KBO)**. [kbopub.economie.fgov.be](https://kbopub.economie.fgov.be/). Recherche par numéro d’entreprise, accès gratuit aux infos publiques (statut, dirigeants visibles via les publications du Moniteur belge — annexes au Moniteur).

**Pays-Bas — KvK (Kamer van Koophandel)**. Registre des chambres de commerce néerlandaises. Très utilisé dans les schémas internationaux (les Pays-Bas sont une juridiction de holding très active).

**Luxembourg — Registre de Commerce et des Sociétés (RCS)**. [lbr.lu](https://www.lbr.lu/) — informations de base gratuites. Densité de SOPARFI et SCSp (sociétés de gestion d’actifs).

**Suisse — Zefix**. [zefix.ch](https://www.zefix.ch/) — registre fédéral. Accès gratuit aux infos de base (forme, siège, dirigeants, état). Accès aux actes par les registres cantonaux (Genève, Zurich, etc., souvent payant).

**Pologne — KRS (Krajowy Rejestr Sądowy)**. Accès en ligne, en polonais, gratuit. Important pour les schémas Europe centrale.

**Roumanie — ONRC (Oficiul Național al Registrului Comerțului)**. Accès en ligne, payant.

**Estonie, Lettonie, Lituanie**. Registres nationaux accessibles en ligne, en partie en anglais. Les baltes hébergent une part importante des structures Europe de l’Est.

**Russie — EGRUL**. Registre russe accessible en ligne. Depuis 2022, l’accès depuis l’UE est techniquement entravé pour des raisons de sanctions et politiques. Des copies / agrégateurs existent (par exemple via OpenCorporates pour les données antérieures).

**Ukraine — YouControl, Opendatabot**. Bases agrégées qui exploitent les registres ouverts ukrainiens (très ouverts depuis les réformes 2014+).

**Israël — Registrar of Companies**. Accès payant, en hébreu.

**Chine — National Enterprise Credit Information Publicity System** (NECIPS) ; **Qichacha**, **Tianyancha** (agrégateurs commerciaux populaires). Données souvent en chinois.

**Hong Kong — Companies Registry / ICRIS**. Accès en ligne, payant pour les actes. Une des juridictions à transparence relative en Asie.

**Singapour — ACRA (BizFile+)**. Accès en ligne, payant pour les rapports détaillés.

**Inde — Ministry of Corporate Affairs (MCA)**. Accès en ligne, partiellement gratuit.

**Émirats arabes unis — registres par émirat et par free zone** (DED Dubaï, ADGM, DIFC, DMCC, RAK ICC, JAFZA). Hétérogène. Le DIFC et l’ADGM sont les juridictions de droit anglais des Émirats, avec leurs propres registres.

**Liban, Iran, Soudan, Venezuela** etc. — registres souvent inaccessibles en ligne ou peu fiables. Coopération internationale et sources secondaires (presse, leaks) deviennent prépondérantes.

**Caraïbes (BVI, Cayman, Bahamas, Bermudes)** — registres avec accès très limité au public. UBO accessible aux autorités sous conditions (BOSS pour BVI). Le travail repose largement sur les leaks (Panama Papers, Pandora Papers) et la coopération internationale.

### Portails européens consolidés

**BRIS (Business Registers Interconnection System)** — portail européen e-Justice qui interconnecte les registres nationaux des États membres. [e-justice.europa.eu](https://e-justice.europa.eu/). Recherche cross-border simplifiée.

**EBOCS (European Business Ownership and Control Service)** — agrégation des registres UE pour les analystes professionnels.

### L’utilité opérationnelle

Pour un dossier multi-juridictionnel, la séquence type :

- **OpenCorporates** pour la vue agrégée initiale.
- **Registres nationaux directs** pour la validation et les actes.
- **BRIS** pour les recherches transfrontalières en UE.
- **Sayari, Orbis** (chapitres 50-51) si abonnement disponible — couverture internationale plus large et plus complète.

### Mini-walkthrough

Cible : OMEGA HOLDINGS LTD, Chypre, identifiée dans une DS comme contrepartie d’un flux de 850 K€.

- OpenCorporates : trouvée — Cyprus, registered 2019, status active.
- Registre chypriote (Department of Registrar of Companies and Intellectual Property) : accès en ligne, partiellement gratuit. Identification confirmée. Directors visibles ; UBO **non public** (accès limité depuis l’arrêt CJUE 2022 — chapitre 13).
- Recherche complémentaire via leaks : présence d’OMEGA HOLDINGS dans Pandora Papers ? (chapitre 18).
- Sayari (si disponible) : recoupement avec dossiers similaires.

### Erreurs fréquentes

- **Se contenter d’OpenCorporates.** Utile pour la vue agrégée mais souvent en retard sur les modifications récentes.
- **Ne pas tester plusieurs orthographes** dans les langues étrangères (translittérations, accents, articles initiaux).
- **Sous-estimer les agrégateurs locaux** (Qichacha en Chine, YouControl en Ukraine).

### Limites

Beaucoup de registres asiatiques, africains, ou caribéens sont peu accessibles ou peu fiables. La coopération internationale (Egmont) et les leaks deviennent alors les principaux leviers.

### Lien avec le fil rouge

> **CLEARFLOW — Multi-juridictions**
> 
> Nassim mobilise BRIS pour les sociétés européennes du dossier Haddad (CY, FR, DE, NL), OpenCorporates pour la vue agrégée, Sayari (licence du service) pour la validation et l’extension du graphe, registres locaux émiratis pour les sociétés Free Zone identifiées, et coopération via Egmont pour les juridictions inaccessibles (Liban). Le travail prend 4 à 5 jours pour la cartographie complète.

### Points clés à retenir

- Hors France/UK/US, mobilisation d’un mix : registres nationaux + portails consolidés + agrégateurs.
- BRIS est le portail UE de référence pour la recherche multi-juridictions.
- Les juridictions caribéennes et certaines asiatiques exigent leaks + coopération.

-----

## Chapitre 13 — Identifier les bénéficiaires effectifs

### Objectif du chapitre

Comprendre la notion de **bénéficiaire effectif (UBO)**, savoir mobiliser les registres UBO disponibles, anticiper leurs limites, et croiser pour identifier le ou les UBO réels d’une structure. C’est un objectif central du FININT, et l’un des plus difficiles dans les juridictions opaques.

### Le concept

Le **bénéficiaire effectif** (UBO — Ultimate Beneficial Owner) d’une entité est, en droit européen :

- toute personne physique qui détient ou contrôle, directement ou indirectement, plus de **25 %** du capital ou des droits de vote ;
- ou exerce un contrôle par d’autres moyens (contrat, convention de vote, droit de nomination) ;
- ou, à défaut, occupe la fonction de dirigeant principal (UBO « de dernier recours », en France parfois appelé UBO « par défaut »).

Pour les **trusts et fondations**, l’UBO inclut : le constituant (settlor), le ou les trustee(s), le ou les protecteur(s), le ou les bénéficiaire(s) (ou catégorie de bénéficiaires), et toute autre personne contrôlant le trust.

### Les registres UBO

Depuis la 4ème puis la 5ème directive AML, l’UE a imposé aux États membres de tenir des **registres des bénéficiaires effectifs**. Organisation et accès varient.

**France — Registre des bénéficiaires effectifs (RBE)** tenu par l’INPI. Toutes les entités juridiques françaises doivent déclarer leurs UBO. Accès au RBE :

- pour les autorités compétentes : sans restriction.
- pour les assujettis (banques, etc.) : dans le cadre de leurs obligations LCB-FT.
- pour le public : a été ouvert puis restreint suite à l’**arrêt CJUE du 22 novembre 2022** qui a invalidé l’accès public généralisé au motif de protection de la vie privée. La situation actuelle (2025) : accès maintenu pour les autorités, les assujettis, et certaines catégories spécifiquement justifiées (presse d’investigation sous conditions, certains professionnels). L’accès « grand public » direct est restreint. À vérifier auprès de la dernière communication de l’INPI au moment de l’enquête.

**UK — PSC (Persons with Significant Control)**. Public et gratuit via Companies House. Resté ouvert (UK hors UE depuis Brexit, donc non concerné par l’arrêt CJUE).

**Allemagne — Transparenzregister**. Accès très restreint au public depuis l’arrêt CJUE.

**Pays-Bas — UBO-register**. Idem, restreint.

**Luxembourg — Registre des bénéficiaires effectifs (RBE)**. Restreint depuis CJUE.

**Italie, Espagne, autres EU**. Situations variables, mais tendance générale au resserrement post-CJUE.

**En pratique, l’accès varie désormais fortement** selon les États membres, les catégories d’acteurs (autorités, assujettis LCB-FT, presse, chercheurs, professionnels avec intérêt légitime) et la justification d’un **intérêt légitime** à connaître l’UBO. L’analyste vérifie systématiquement l’état du droit dans chaque juridiction concernée par le dossier au moment de l’enquête.

**Pays tiers** (BVI, Cayman, Émirats, etc.) — registres existent mais accès quasi-systématiquement réservé aux autorités locales.

**AMLA et nouveau paquet AML européen (2024-2026)** : prévoit une **interconnexion européenne** des registres UBO et un encadrement plus précis de l’accès. Mise en œuvre progressive.

### L’utilité opérationnelle

L’UBO est la **clé** d’une cartographie : sans UBO, on a une coquille juridique sans sa réalité humaine.

L’analyste cherche à :

- identifier l’UBO « déclaré » officiellement dans le registre ;
- vérifier sa **plausibilité** (cet UBO a-t-il les caractéristiques pour être réellement le contrôleur — capacité financière, expérience, lien avec l’activité ?) ;
- identifier d’éventuels signes de **prête-nom** (chapitre 25) ;
- recouper avec d’autres sources (leaks, presse, registres connexes) pour confirmer ou infirmer.

### Méthode — démarche en 4 étapes

1. **Récupérer la déclaration UBO officielle** quand accessible (RBE France pour les autorités/assujettis, PSC UK public, etc.).
1. **Vérifier la cohérence** : profil, nationalité, adresse, antécédents. Un UBO de 22 ans déclaré contrôleur d’un groupe à 50 M€ de CA est invraisemblable.
1. **Croiser** avec : autres mandats déclarés, presse, leaks, réseaux sociaux, registres connexes.
1. **Calibrer la confiance** : UBO déclaré = *possible* ; UBO confirmé par recoupement = *probable* ; UBO confirmé par documents indépendants (réquisitions, EAR) = *quasi-certain*.

### Mini-walkthrough

Cible : OMEGA HOLDINGS LTD (Chypre).

- Recherche RBE chypriote : restreint depuis CJUE.
- Companies House équivalent chypriote : directors visibles, UBO non.
- Sayari (licence) : indique un UBO possible, M. Y, basé à Beyrouth, avec un lien sur trois autres sociétés méditerranéennes.
- Recherche dans Pandora Papers (Aleph ICIJ) : OMEGA HOLDINGS apparaît, avec un settlor d’un trust chypriote. Le settlor est *distinct* de M. Y. **Hypothèse : M. Y est le directeur déclaré, mais le settlor du trust contrôle in fine** — UBO probable = settlor.
- Vérification du settlor : presse libanaise antérieure, fonctions dans des sociétés liées au commerce régional. Profil cohérent.
- Calibration : UBO probable = settlor (Karim Haddad ou personne associée), niveau de confiance *probable* sur la base du recoupement Pandora.
- Lacune : la liste exacte des bénéficiaires du trust est inaccessible — il faudrait Egmont avec Mokas ou MROS selon l’évolution.

### Erreurs fréquentes

- **Croire l’UBO déclaré sans vérification.** Beaucoup d’UBO déclarés sont des prête-noms.
- **Conclure à un prête-nom sans preuve.** Inversement, ce n’est pas parce que l’UBO déclaré paraît modeste qu’il est nécessairement un prête-nom.
- **Ignorer le contrôle indirect.** Un UBO peut contrôler par convention, par usufruit, par contrat de gestion — pas seulement par % de capital.
- **Mélanger l’UBO d’une société et l’UBO d’un compte bancaire.** Ce ne sont pas toujours les mêmes (un compte peut être au nom d’une personne mandataire de la société, ou d’un fiduciaire).

### Limites

L’identification de l’UBO réel d’une structure complexe **multi-juridictionnelle** opaque exige souvent : des leaks, des coopérations internationales, des réquisitions auprès de banques, et parfois reste **indéterminable** par le seul OSINT.

### Lien avec le fil rouge

> **CLEARFLOW — Identification UBO progressive**
> 
> Pour les 4 SAS françaises : UBO déclarés au RBE = personnes physiques résidant en France. Pour 2 d’entre elles, l’UBO déclaré est un retraité français de 78 ans avec un patrimoine modeste — **alarme prête-nom probable**. Pour les Limited UK : PSC = M. Y (libanais, basé à Dubaï). Pour OMEGA Chypre : UBO déclaré = trustee professionnel (couverture). Pour la LLC Delaware : aucun UBO accessible (depuis l’interim final rule FinCEN de mars 2025, les LLC domestiques US sont exemptées de déclaration BOI à FinCEN). Conclusion : *probable* que Karim Haddad est l’UBO réel d’une partie significative du réseau, sous prête-noms et trustees, mais l’identification *quasi-certaine* exigerait coopération internationale et réquisitions.

### Points clés à retenir

- UBO = personne physique qui détient/contrôle ultimement, seuils 25 % en UE (capital ou droits de vote).
- Registres UBO : accès restreint en UE depuis CJUE 2022. UK PSC reste public.
- Croiser systématiquement déclaration / cohérence / recoupements / leaks.
- L’UBO réel d’une structure complexe peut être *indéterminable* sans coopération.

-----

## Chapitre 14 — Comptes annuels, bilans et documents financiers

### Objectif du chapitre

Savoir trouver et **lire les documents financiers publiés** par les entreprises pour en extraire des indicateurs de cohérence économique, des signaux d’anomalie, et étayer les hypothèses d’enquête. Le détail technique de l’analyse comptable sera couvert au chapitre 36 ; ici, on se concentre sur l’accès et la lecture rapide.

### Le concept

Selon les juridictions et la taille des entreprises, les **comptes annuels** publiés varient en richesse :

- **Bilan** — photo du patrimoine à une date (actif / passif).
- **Compte de résultat** — flux d’activité sur une période (produits / charges / résultat).
- **Annexe** — explications, méthodes, tableaux complémentaires.
- **Tableau des flux de trésorerie** — variations de cash sur la période (très utile, mais pas obligatoire pour les petites sociétés).
- **Rapport de gestion** — narratif des dirigeants.
- **Rapport des commissaires aux comptes** (CAC) — quand la société y est tenue.

En France : seuils de publication. Au-delà des seuils (à la fois en CA, total bilan, effectif), publication obligatoire au greffe. Possibilité depuis 2014 pour les très petites sociétés de demander la **confidentialité** des comptes (publication avec accès restreint aux assujettis et autorités, pas au public). Chez Pappers et autres agrégateurs, on voit fréquemment la mention « comptes confidentiels ».

Au UK : la quasi-totalité des sociétés publient. Format selon la taille (statutory accounts, abridged, micro-entity).

Aux US : les sociétés non cotées ne publient pas en règle générale ; les sociétés cotées publient via SEC EDGAR (très riches : 10-K, 10-Q, 8-K).

En Allemagne, les sociétés publient au Bundesanzeiger ; en Belgique, au Moniteur belge ; en Italie, à la Camera di Commercio ; au Luxembourg, au RCS (avec certaines obligations spécifiques).

### L’utilité opérationnelle

Lecture FININT d’un bilan / compte de résultat (pour le détail technique : chapitre 36) :

- **Cohérence sectorielle** : la marge brute est-elle cohérente avec le secteur ? Le ratio CA / effectif est-il vraisemblable ?
- **Évolution dans le temps** : les chiffres explosent-ils sans justification ? Sont-ils stables tandis que l’apparence opérationnelle change ?
- **Postes anormaux** : créances clients gigantesques (fictives ?), prêts intragroupe sans contrepartie, immobilisations incorporelles surévaluées, charges de « conseil » dominantes, charges de sous-traitance massives sans personnel propre ?
- **Engagements hors bilan** : garanties, cautions données — souvent dans l’annexe.
- **Écart résultat / trésorerie** : un beau résultat sans cash correspondant est suspect.

### Méthode — récupération et lecture rapide

Pour une société française :

- Pappers : aperçu des comptes publiés.
- Infogreffe : téléchargement de l’acte officiel (PDF) — gratuit ou modique selon les actes.
- INPI/RNE : équivalent.

Pour une société UK : Companies House — téléchargement gratuit.

Pour une société US cotée : SEC EDGAR — téléchargement gratuit.

Pour une société non publique US ou hors UE : selon le pays. Souvent, comptes inaccessibles (juridiction opaque ou exemption). Mention explicite dans le livrable.

**Lecture rapide en 5 ratios clés** :

1. **Marge brute** = (CA - achats consommés) / CA. À comparer avec le secteur.
1. **Marge d’exploitation** = résultat d’exploitation / CA.
1. **Charges de personnel / CA** — donne l’intensité main-d’œuvre.
1. **Stock / CA** — rotation des stocks, anomalie si très élevé.
1. **Créances clients / CA** — délai de paiement clients, anomalie si très élevé (ventes fictives ou clients fragiles).

À comparer avec les ratios moyens du secteur (sources : INSEE, statistiques sectorielles, base de données des cabinets comptables).

### Mini-walkthrough

NEXUS TRADING SAS (France), 1er exercice clos. Comptes publiés (non confidentiels).

- CA : 12,4 M€ — élevé pour un 1er exercice avec dirigeant unique.
- Achats consommés : 11,9 M€. Marge brute : 4 % — très faible pour le négoce de gros (5-10 % attendu).
- Charges de personnel : 32 K€ (un dirigeant, sans salariés). Cohérent avec un dirigeant unique et activité de pure intermédiation.
- Stock : 0 €. Cohérent avec une activité d’intermédiation sans détention.
- Créances clients : 280 K€ (≈ 8 % du CA, soit ~30 jours de délai — normal).
- Résultat d’exploitation : 80 K€. Faible mais positif.
- Trésorerie en fin d’exercice : 35 K€.

Lecture FININT : profil compatible avec une activité de **pure intermédiation commerciale** (pas de stock, pas de salariés autres que le dirigeant) sur un volume élevé pour un 1er exercice. Marge faible mais cohérente avec une intermédiation. Attention : un tel profil est aussi compatible avec une **société de transit** dans un schéma TBML (passage de fonds avec apparence commerciale). Ne tranche pas — élément de soupçon **possible**, à recouper avec la cohérence des contreparties et des marchandises.

### Erreurs fréquentes

- **Lire les chiffres sans les comparer.** Un CA de 12 M€ ne dit rien sans le secteur, la taille, l’historique.
- **Ignorer l’annexe.** Beaucoup d’informations utiles y figurent (engagements, méthodes comptables, événements postérieurs).
- **Surinterpréter une faible marge.** Faible marge ≠ blanchiment automatique. Elle est cohérente avec le négoce de gros, l’intermédiation, certains modèles online.
- **Considérer la « confidentialité » comme un signal en soi.** Beaucoup de TPE françaises légitimes optent pour la confidentialité pour des raisons concurrentielles.

### Limites

Les comptes annuels sont **historiques** (publiés généralement 6 à 12 mois après la clôture). Ils peuvent être **falsifiés** (sans CAC, le contrôle externe est minimal). L’analyste ne peut pas conclure sur les seuls comptes — il les croise.

### Lien avec le fil rouge

> **CLEARFLOW — Lecture des comptes**
> 
> Sur les 4 SAS françaises du réseau Haddad, 2 ont publié des comptes (les 2 plus anciennes), 2 sont en 1er exercice. Sur celles qui ont publié : marges brutes faibles (3-5 %), charges de conseil à des sociétés liées chypriotes (cumulé 280 K€/an), prêts intragroupe sans intérêts apparents. Profil compatible avec un schéma de **transit avec rétention de marge minimale** et **transferts intragroupe possiblement de complaisance**. Soupçons : *probable* à *quasi-certain* sur le schéma de transit, *possible* sur la qualification fraude. Approfondissements requis.

### Points clés à retenir

- Comptes annuels = source publique précieuse, surtout en France et UK.
- Lecture rapide en 5 ratios + comparaison sectorielle.
- Pas de conclusion sur les seuls comptes — toujours croiser.
- L’absence de comptes (confidentialité ou non publication) est documentée mais n’est pas un soupçon en soi.

-----

## Chapitre 15 — Marchés publics, subventions et appels d’offres

### Objectif du chapitre

Connaître les **bases publiques de marchés publics, subventions et appels d’offres** comme source d’enquête, notamment pour les schémas de corruption (chapitre 42), de favoritisme et d’attribution douteuse.

### Le concept

Les **marchés publics** (commande publique) sont, dans de nombreuses juridictions, soumis à des obligations de **publication** : annonces préalables, attributions, contrats. Ces données ouvertes sont une mine d’information pour l’analyste FININT enquêtant sur la corruption ou les schémas adressés à l’État ou à des collectivités.

### Méthode — bases utiles par pays

**France** :

- **BOAMP** (Bulletin officiel des annonces de marchés publics) — publications obligatoires des marchés au-delà des seuils. Accès en ligne, gratuit.
- **JOUE / TED (Tenders Electronic Daily)** — équivalent UE.
- **data.gouv.fr** : datasets ouverts sur la commande publique (DECP — Données essentielles de la commande publique).
- **HATVP** (Haute Autorité pour la transparence de la vie publique) — déclarations de patrimoine et d’intérêts des responsables publics. Accès en ligne, partiellement public. **Périmètre à connaître** : toutes les fonctions publiques ne sont pas couvertes de la même manière. Le périmètre des assujettis HATVP est défini par fonctions et seuils (parlementaires, membres du gouvernement, élus locaux à partir de certains seuils, dirigeants d’organismes publics, etc.). Un élu local d’une petite commune n’est pas nécessairement couvert ; un parlementaire l’est. Vérifier la liste à jour des assujettis sur le site de la HATVP.
- **AIFE — Chorus Pro** (factures de l’État).

**UE** :

- **TED (Tenders Electronic Daily)** — toutes les annonces UE au-delà des seuils.
- **eForms** — format unifié à partir de 2024.
- **EU Funding & Tenders Portal** pour les financements européens (Horizon, FEDER, FSE, etc.).

**UK** :

- **Contracts Finder**, **Find a Tender Service**.

**US** :

- **SAM.gov** (System for Award Management) — base fédérale.
- **USAspending.gov** — dépenses fédérales.
- **State and local procurement portals**.

**Subventions** :

- France : data.gouv.fr (subventions associatives, aides aux entreprises).
- UE : Cohesion Open Data Platform.

### L’utilité opérationnelle

L’analyste cherche à identifier :

- **Marchés attribués à des sociétés du réseau** sous enquête (lien direct avec le secteur public).
- **Schémas d’attribution suspects** : faible nombre de soumissionnaires, dérogations à appel d’offres, marchés découpés sous les seuils, marchés négociés sans publicité.
- **Liens entre attributaires et décideurs** (HATVP en France pour les conflits d’intérêts).
- **Sous-traitants en cascade** dont une partie peut être des sociétés écrans.

### Mini-walkthrough

Une SARL de BTP en région française, dans un dossier de soupçon de corruption locale.

- BOAMP : la SARL a remporté 7 marchés sur 3 ans, dans 3 communes, pour un montant cumulé de 4,2 M€.
- DECP : on identifie les acheteurs publics (3 communes), les types de marchés (voirie, bâtiments scolaires).
- HATVP : le maire de la commune principale a déclaré un intérêt (ami / parent travaillant dans une société liée).
- Recoupement : on cherche dans les conseils municipaux, presse locale, des éléments confirmant ou infirmant.

Conclusion : signal de **conflit d’intérêts probable** à approfondir. Pas de qualification de corruption à ce stade — exige des éléments d’intentionnalité et de contrepartie.

### Erreurs fréquentes

- **Lire un marché public comme une preuve.** Beaucoup de marchés sont gagnés légitimement par des entreprises locales — la concentration n’est pas la preuve.
- **Ignorer les seuils.** Les marchés sous certains seuils ne sont pas publiés — l’analyse est partielle.
- **Sous-utiliser HATVP** en France — c’est une source précieuse pour les liens entre décideurs et entreprises.

### Limites

Les bases publiques ne couvrent pas tous les marchés (seuils). Elles ne disent rien des **marchés privés** (B2B), qui peuvent aussi être l’objet de corruption. La corruption se prouve par d’autres moyens (preuves d’intention, paiements traçables, témoignages).

### Lien avec le fil rouge

> **CLEARFLOW — Marché ivoirien**
> 
> Une des sociétés du réseau Haddad, NEXUS NEGOCE (Côte d’Ivoire), a remporté un marché public ivoirien de fourniture de matériel agricole en 2023 pour 3,2 M€. Source : presse économique régionale + rapport de la Chambre des comptes ivoirienne. Profil du marché : faible nombre de soumissionnaires, attributaire créé moins d’un an avant l’attribution, lien possible avec un haut fonctionnaire ivoirien (presse). Le volet ivoirien sera renvoyé en coopération internationale (Egmont avec la CRF ivoirienne) — impossible à approfondir depuis la France sans ce levier.

### Points clés à retenir

- BOAMP, TED, SAM.gov, Contracts Finder : bases ouvertes principales.
- HATVP : essentielle pour les liens décideurs / entreprises en France.
- Marchés publics ne prouvent pas la corruption : ils alimentent l’hypothèse.
- Les marchés privés et les marchés sous seuils sont des angles morts.

-----

## Chapitre 16 — Contentieux, procédures collectives et sanctions administratives

### Objectif du chapitre

Mobiliser les **données de contentieux et de procédures** comme indicateurs de risque, de tension, ou d’historique d’anomalies. Une société ou une personne avec un passif contentieux significatif n’est pas nécessairement coupable — mais elle a un historique à intégrer.

### Le concept

Plusieurs catégories de données :

**Procédures collectives** (sauvegarde, redressement judiciaire, liquidation judiciaire). En France : BODACC, Infogreffe. Au UK : The Gazette. Dans la majorité des juridictions, ces procédures sont publiques.

**Décisions de justice publiées** : selon les juridictions, certaines décisions sont publiées (avec ou sans anonymisation). En France : Légifrance, Doctrine, Dalloz, Lexbase. Plateformes payantes pour certains accès. Open data judiciaire en cours (depuis le décret « open data des décisions »).

**Sanctions administratives** :

- **AMF** (Autorité des marchés financiers) — sanctions sur les acteurs des marchés financiers en France.
- **ACPR** (Autorité de contrôle prudentiel et de résolution) — sanctions sur les banques, assurances, PSP, EME.
- **Commission des sanctions de l’AMF**, idem ACPR : décisions publiées.
- **CNIL** : sanctions RGPD.
- **Autorité de la concurrence**.
- Équivalents européens : ESMA, EBA, EIOPA.
- **OFAC**, **OFSI**, **DG Trésor — pôle sanctions financières internationales** : sanctions liées aux sanctions économiques.
- **SEC**, **DOJ**, **CFTC** aux US.

**Cybercrime / fraude** : décisions condamnatoires, signalements ANSSI, etc. (croisement CTI / FININT).

**Contentieux fiscaux** : majorations, redressements publiés, contentieux administratif.

### L’utilité opérationnelle

Pour l’analyste :

- Une **procédure collective récente** sur une contrepartie est un signal de risque ;
- Un **passif contentieux** chargé sur un dirigeant ou une société est un facteur de réputation ;
- Une **sanction AMF/ACPR** sur un acteur financier renseigne sur ses pratiques antérieures ;
- Une **condamnation pénale** publique antérieure (selon les juridictions) est un facteur clé.

L’analyste construit ainsi une **fiche réputationnelle** pour chaque acteur clé.

### Méthode — workflow rapide

1. **France** :
- BODACC pour les procédures collectives.
- Légifrance / Doctrine pour les décisions publiées.
- Site AMF (commission des sanctions) et site ACPR.
- Site Direction Générale du Trésor pour les sanctions économiques.
- Presse et adverse media (chapitre 17) pour les affaires non encore jugées ou anonymisées.
1. **UK** :
- The Gazette pour insolvency.
- BAILII et Caselaw.uk pour décisions.
- FCA register pour sanctions.
1. **US** :
- PACER (federal court records, payant).
- SEC press releases.
- DOJ press releases.
- CFTC.
- State courts.
1. **International** : ICIJ Aleph, OCCRP archives (chapitre 18).

### Mini-walkthrough

Sur le dirigeant Monsieur X (gestionnaire des SAS françaises liées à Haddad) :

- BODACC : 2 procédures collectives sur des sociétés antérieurement dirigées par M. X (liquidations 2018 et 2020).
- Légifrance : pas de décision publique le concernant directement.
- AMF/ACPR : non.
- Presse : un article de 2019 mentionne sa mise en cause dans une affaire de carrousel TVA (instruction en cours, présomption d’innocence).

Conclusion : profil avec **historique contentieux significatif**, à mentionner dans la fiche personne (chapitre 27) avec niveau de confiance approprié et précautions sur la présomption d’innocence.

### Erreurs fréquentes

- **Confondre instruction et condamnation.** La présomption d’innocence est un principe — l’analyste ne diabolise pas un mis en examen.
- **Ignorer les anonymisations.** Beaucoup de décisions modernes sont anonymisées (initials des parties) — l’identification exige souvent croisement.
- **Surinterpréter une procédure collective.** Beaucoup d’entreprises échouent sans fraude.

### Limites

Beaucoup de contentieux ne sont pas publics, notamment dans les juridictions opaques. Les contentieux fiscaux sont rarement publics dans le détail. La donnée est donc **indicative**, pas exhaustive.

### Lien avec le fil rouge

> **CLEARFLOW — Historique contentieux**
> 
> Le profil contentieux du réseau Haddad : 2 procédures collectives passées sur des sociétés du même gestionnaire (Monsieur X), une enquête fiscale française antérieure sur Haddad lui-même (réglée par transaction fiscale, presse 2018), aucune sanction AMF/ACPR. Le profil n’est pas immaculé. Cela alimente la fiche personne et oriente la priorisation du dossier.

### Points clés à retenir

- BODACC, Légifrance, AMF, ACPR, presse — sources clés en France.
- Présomption d’innocence à respecter dans tout livrable.
- Historique contentieux = facteur réputationnel, pas une preuve.
- Beaucoup d’angles morts (anonymisation, confidentialité, juridictions opaques).

-----

## Chapitre 17 — Presse, adverse media et SOCMINT financier

### Objectif du chapitre

Maîtriser l’**OSINT non-structuré** appliqué à la finance : presse économique, presse d’investigation, adverse media en bases agrégées, et **SOCMINT financier** (signaux issus des réseaux sociaux et de la présence en ligne des dirigeants et entités).

### Le concept

**Presse économique généraliste** : Le Monde, Les Échos, La Tribune, FT, WSJ, Reuters, Bloomberg, Handelsblatt, Frankfurter Allgemeine, Financial Times Italia, El País Negocios, etc. Sources de fond, articles fouillés, dossiers thématiques, archives accessibles via abonnement institutionnel.

**Presse d’investigation** : Mediapart, Investigate Europe, Disclose, Le Canard Enchaîné, OpenDemocracy, OCCRP, ICIJ, ProPublica, The Guardian Investigations, Süddeutsche Zeitung Investigations, Reflets.info. Volume plus restreint mais profondeur d’enquête souvent supérieure.

**Bases d’agrégation professionnelles** : Factiva (Dow Jones), LexisNexis, Nexis Newsdesk, Dow Jones Risk & Compliance, Factiva Risk & Compliance — chapitre 51. Couvrent des milliers de titres mondiaux avec recherche en texte intégral.

**Bases adverse media gratuites ou freemium** : OpenSanctions (qui agrège PEP, sanctions, et adverse media), Aleph (ICIJ), ICIJ databases.

**Annuaires officiels et registres complémentaires** : registre des armes, registre des bateaux, registres aéronautiques (FAA, EASA), pour les actifs très visibles.

**SOCMINT financier** :

- **LinkedIn** : signal de carrière, parcours professionnel, trajectoire, fonctions actuelles et passées, employeurs, réseau visible. Utile pour profiler un dirigeant, identifier des liens entre personnes, repérer des changements d’employeur (passage à une société sous enquête).
- **Réseaux sociaux personnels** (Instagram, Facebook, X/Twitter, TikTok) : signaux de train de vie (voyages, biens, événements), réseau d’amis et de relations, géolocalisation visible (chapitre 39).
- **Blogs et sites professionnels personnels** : occasionnellement, des dirigeants laissent transparaître leurs activités, leurs projets, leurs partenaires.
- **Sites des sociétés cibles** : organisation, équipes, filiales, actualités, partenaires commerciaux affichés — souvent une source plus riche qu’attendue.
- **Annonces publicitaires et événements professionnels** : participations à salons, conférences, prises de parole.
- **Photographies d’événements publics** : croisements visuels (qui est avec qui, où, quand).

### L’utilité opérationnelle

Trois usages majeurs dans une enquête FININT :

1. **Adverse media** : qualification du risque réputationnel d’une personne ou d’une entité — affaires antérieures, associations problématiques, mises en cause publiques.
1. **Profilage humain** (SOCMINT) : qui est cette personne au-delà de sa fiche registre — formation, parcours, réseau, train de vie, signaux de cohérence ou d’incohérence.
1. **Recoupement OSINT général** : croisement avec d’autres sources (presse d’un côté, marchés publics de l’autre, leak d’une troisième) pour bâtir un faisceau d’éléments solide.

### Méthode — workflow presse + SOCMINT

**Presse / adverse media** :

1. **Recherche par nom** dans les agrégateurs. Tester orthographes, translittérations, variantes.
1. **Recherche par société** — actualités, contentieux, opérations corporate.
1. **Recherche thématique** — secteur d’activité + termes typologiques (« blanchiment », « fraude », « conflit d’intérêts », « offshore », etc.).
1. **Tri qualitatif** : presse de référence vs presse moins fiable. Agrégation des dates, recoupement entre titres.
1. **Archivage** des articles consultés (capture, hash si critique).

**SOCMINT financier (LinkedIn et réseaux pro)** :

1. **Identification précise** de la personne (cf. chapitre 19 — homonymie). Profil LinkedIn = un parcours complet possible.
1. **Cartographie des employeurs** : trajectoire historique, durée de chaque fonction, employeur actuel.
1. **Réseau visible** : connexions notables, recommandations.
1. **Cohérence / incohérence** : un dirigeant déclaré d’un groupe à 50 M€ qui sur LinkedIn affiche 4 ans d’expérience junior dans une PME locale = signal de prête-nom probable.
1. **Pour chaque profil consulté** : capture horodatée, archivage. Les profils LinkedIn changent fréquemment.

**SOCMINT financier (réseaux personnels)** :

1. **Présence proportionnée** : un dirigeant officiel discret qui affiche un train de vie démonstratif sur Instagram = source de signaux patrimoniaux.
1. **Géolocalisations** : voyages, présence dans certaines villes, séjours à l’étranger — recoupement avec mouvements financiers.
1. **Réseau visible** : qui aime, commente, est tagué — cartographie des relations personnelles.
1. **Limites RGPD et déontologie** : la consultation est légitime quand l’objet est public ; pas de phishing, pas de faux profils, pas d’intrusion.

### Mini-walkthrough — adverse media sur Karim Haddad

- Factiva (sources françaises et internationales) : 14 articles depuis 2018. Mention dans une transaction fiscale française (2018, sans poursuite pénale), présence dans un dossier d’export contesté en 2021 (article Le Monde), contributions à une fondation philanthropique libanaise (presse libanaise, 2022-2023).
- Mediapart : un article de 2023 sur des allégations de favoritisme pour des marchés en Côte d’Ivoire (sans nommer Haddad explicitement, mais avec des détails recoupés par OSINT).
- OCCRP : pas d’article direct, mais mention d’une société liée dans un dossier régional.
- LinkedIn : profil officiel Haddad, parcours déclaré 1995-aujourd’hui dans le négoce, actuellement « Chairman » de plusieurs entités. Cohérence avec l’image publique.
- Instagram : présence modérée, voyages réguliers (Beyrouth, Dubaï, Genève, Paris), événements professionnels visibles.
- Recoupement : profil global cohérent avec un homme d’affaires international actif. Aucune affaire judiciaire majeure publiquement connue. Adverse media présent mais à distance des qualifications fortes (présomption d’innocence pour les volets en cours).

### Mini-walkthrough — SOCMINT sur Monsieur X (gérant SAS françaises)

- LinkedIn : profil minimal, mention d’une « activité de conseil aux entreprises ». Pas d’expérience préalable affichée en cohérence avec la gestion de 8 SAS commerciales actives.
- Recherche image : photo de profil utilisée également sur un site de cabinet de domiciliation (corrélation forte).
- Conclusion : profil compatible avec un **professionnel multi-mandats** au service d’un cabinet de domiciliation. Pas une preuve, mais un facteur ajouté à l’hypothèse de prête-nom (chapitre 25).

### Erreurs fréquentes

- **Considérer la presse comme preuve.** La presse est une source d’information ; certains articles peuvent être imprécis, partiels ou orientés.
- **Surinterpréter un voyage.** Les voyages sur Instagram peuvent être un facteur d’analyse mais pas une qualification.
- **Ne pas archiver.** Les profils LinkedIn et les réseaux personnels changent — capture horodatée systématique.
- **Croiser des homonymes** (chapitre 19) : un Monsieur X présent sur LinkedIn n’est pas nécessairement le Monsieur X gestionnaire de la SAS. Vérifier date de naissance, parcours, photo.
- **Risquer le phishing OSINT** : créer un faux profil pour entrer en contact avec la cible viole les règles déontologiques et peut violer le droit (en France, manœuvres frauduleuses pour obtenir des données).

### Limites

La presse couvre principalement les acteurs visibles (grandes affaires, personnages publics). Les acteurs « moyens » d’un dossier complexe ne sont souvent pas couverts. Le SOCMINT est limité aux personnes qui ont une présence en ligne ; un homme d’affaires de l’ancienne génération ou opérant dans une culture peu numérique peut être quasi-invisible.

Le RGPD limite, en pratique, certaines exploitations en France et en UE — la donnée doit être collectée pour une finalité légitime, et le traitement doit être conforme. En CRF, le cadre légal autorise un traitement étendu ; en cabinet privé, les limites sont plus strictes (chapitre 68).

### Lien avec le fil rouge

> **CLEARFLOW — Le SOCMINT élargit le réseau**
> 
> Sur LinkedIn, Nassim identifie 5 collaborateurs proches déclarés de Haddad (employés ou anciens employés des sociétés du réseau). Sur Instagram, plusieurs photos de Haddad lors d’événements caritatifs au Liban montrent des personnalités politiques et économiques régionales. Une photo prise en 2023 lors d’un dîner à Genève montre Haddad avec un ancien dirigeant d’une banque privée suisse — la même banque dans laquelle un compte personnel apparaît dans les DS. Ce recoupement, *quasi-certain* à la confirmation visuelle (recherche image inverse + métadonnées), nourrit l’hypothèse d’un canal financier privilégié. Ce n’est pas une preuve, mais un faisceau qui oriente la coopération suisse.

### Points clés à retenir

- Presse économique + presse d’investigation + bases d’agrégation = adverse media solide.
- SOCMINT financier : LinkedIn pour le pro, réseaux perso pour le train de vie et le réseau humain.
- Croiser systématiquement plusieurs sources avant qualification.
- Présomption d’innocence et cadre RGPD à respecter.
- Toujours archiver — les profils en ligne changent vite.

-----

## Chapitre 18 — Leaks financiers : ICIJ, OCCRP, Aleph, Panama/Pandora

### Objectif du chapitre

Maîtriser l’usage des **leaks financiers majeurs** comme source d’enquête FININT. Les leaks ne sont pas la totalité du métier, mais ils sont devenus une source de référence pour les structures opaques offshores et certaines révélations sectorielles.

### Le concept

Un **leak** est une fuite documentaire massive d’informations financières, généralement :

- issue d’un cabinet juridique, fiduciaire ou d’une institution financière ;
- obtenue par un lanceur d’alerte ou un hack ;
- transmise à un consortium de journalistes (ICIJ ou OCCRP étant les plus connus) qui en mène l’analyse coordonnée et la publication.

Ces leaks ont **changé** le paysage du FININT en rendant accessible (avec des limites — voir infra) une partie des structures historiquement opaques (BVI, Panama, Bahamas, etc.).

### Les principaux leaks et bases

**Panama Papers (2016)** — fuite de 11,5 millions de documents du cabinet Mossack Fonseca (Panama). Origine : un lanceur d’alerte anonyme (« John Doe ») au journaliste allemand Bastian Obermayer (Süddeutsche Zeitung), partagé avec ICIJ. Conséquence : révélation massive de structures offshores liées à des PEP, des hommes d’affaires, des criminels organisés. La base [Offshore Leaks](https://offshoreleaks.icij.org/) de l’ICIJ regroupe les structures identifiées et est consultable publiquement par nom.

**Paradise Papers (2017)** — fuite du cabinet Appleby (Bermudes) et de divers fournisseurs. ICIJ. Inclus dans la base Offshore Leaks.

**Pandora Papers (2021)** — fuite combinée de 14 prestataires offshore. ICIJ. Près de 12 millions de documents. Particulièrement riche sur les UBO et les bénéficiaires de trusts. Inclus dans la base Offshore Leaks.

**FinCEN Files (2020)** — fuite de SAR (Suspicious Activity Reports) américains. Différent des autres leaks : il s’agit de signalements internes de banques au régulateur US. Coordonné par BuzzFeed et ICIJ. Couvre 2 trillions USD de transactions suspectes.

**Suisse Secrets (2022)** — fuite de comptes Credit Suisse, coordonnée par OCCRP et plusieurs journaux européens.

**Cyprus Confidential (2023)** — fuite portant sur des prestataires de services chypriotes, ICIJ.

**Russian Asset Tracker (2022+)** — base OCCRP sur les actifs des oligarques russes sous sanctions.

**OCCRP Aleph** — plateforme **agrégée** de l’OCCRP qui regroupe des leaks, registres ouverts, sanctions, et bases de données journalistiques. Devenue une référence pour les analystes, accessible via partenariat avec OCCRP. Recherche unifiée, très utile.

**Aleph (instance ICIJ)** — moteur de recherche sur l’écosystème ICIJ. Accès journalistique principalement.

**Smaller leaks** : Bahamas Leaks (2016), Lux Leaks (2014), Swiss Leaks (HSBC, 2015), Malta Files, Glencore Leak, etc.

### L’utilité opérationnelle

Pour un analyste FININT, les leaks permettent :

1. **Identification de structures cachées** : une société BVI dont l’UBO n’est pas accessible en registre peut figurer dans Panama/Pandora avec ses bénéficiaires.
1. **Recoupement de réseaux** : les liens entre personnes via des trusts ou des fondations sont souvent visibles dans les documents leakés.
1. **Profilage de prestataires** : certains cabinets de domiciliation ou trust companies apparaissent récurremment dans des dossiers à risque.
1. **Documentation historique** : les leaks couvrent souvent des périodes anciennes — utile pour reconstituer l’historique d’un montage.

### Méthode — workflow leaks

1. **Recherche par nom de personne** dans Offshore Leaks (ICIJ) — gratuit, public.
1. **Recherche par nom de société** dans Offshore Leaks.
1. **Recherche dans Aleph (OCCRP)** si accès — agrège plus largement.
1. **Recherche dans les archives journalistiques** publiées (les articles ICIJ/OCCRP sont publics avec une partie des sources).
1. **Vérification croisée** : un nom dans un leak n’est pas un fait avéré — c’est un document supposé authentique. La présence ne vaut pas culpabilité (la détention d’une société offshore peut être parfaitement légale).
1. **Documentation** : capture, référence à l’article ou à la base, date de consultation.

### Mini-walkthrough — Pandora dans CLEARFLOW

- Recherche dans Offshore Leaks par « Karim Haddad » : 1 résultat — un trust chypriote enregistré en 2019, dont le settlor est nommé Karim Haddad, et dont les bénéficiaires incluent une SAS française et une LLC Delaware (toutes deux du réseau du dossier).
- Recherche par « OMEGA HOLDINGS » : 2 résultats — la société chypriote elle-même + une mention dans une entité liée à Beyrouth.
- Aleph (OCCRP) : recoupement avec un article OCCRP de 2023 sur les flux entre Liban et Afrique de l’Ouest, mentionnant un homme d’affaires correspondant à Haddad sans le nommer.
- Calibration : la présence dans Pandora est *quasi-certaine* (document authentique, attribution claire). L’usage du trust pour des fins illicites n’est pas démontré par le seul leak — il est *compatible* avec, et nécessite recoupement des flux et de l’activité.

### Erreurs fréquentes

- **Présence dans un leak = culpabilité.** Non. La détention d’une structure offshore peut être parfaitement légale (planification successorale, protection patrimoniale légitime, résidence à l’étranger).
- **Leak = source primaire complète.** Les leaks sont des extraits limités à ce qu’a obtenu le lanceur d’alerte. Ils peuvent omettre des éléments cruciaux.
- **Leak = preuve admissible.** En cadre judiciaire, l’admissibilité dépend du droit national et de l’origine. Certaines décisions (CEDH, en particulier) admettent les preuves issues de leaks sous conditions, d’autres non.
- **Surinterpréter une similitude de nom.** Un Karim Haddad dans un leak peut être un homonyme — vérifier les autres champs (date de naissance, adresse, autres mandats).

### Limites

Les leaks sont **datés** : ils reflètent un instant. Une société leakée en 2016 peut avoir été liquidée en 2018, ou son UBO peut avoir changé. Les leaks couvrent les juridictions dont les prestataires ont été leakés — d’autres juridictions restent dans l’ombre. L’accès complet aux bases (au-delà des recherches publiques) est généralement réservé à la presse partenaire.

### Lien avec le fil rouge

> **CLEARFLOW — Le leak comme accélérateur**
> 
> Sans le hit Pandora, l’identification de Haddad comme settlor du trust chypriote aurait demandé une coopération via Egmont avec Mokas — délai de plusieurs semaines, sans garantie. Le leak fournit *gratuitement* en quelques minutes une information dont la valeur opérationnelle est élevée. Nassim documente le hit et le qualifie *probable* à *quasi-certain* selon les recoupements. Cette information sera l’un des **piliers** de l’hypothèse centrale du dossier (chapitre 64).

### Points clés à retenir

- Panama, Paradise, Pandora, FinCEN Files, Suisse Secrets : leaks majeurs.
- Offshore Leaks (ICIJ) et Aleph (OCCRP) : bases consultables.
- Présence dans un leak ≠ culpabilité ; mais signal de structure offshore avérée.
- Les leaks accélèrent considérablement les enquêtes sur les juridictions opaques.
- Vérification croisée et calibration de la confiance impératives.

-----
