---
title: PARTIE I — COMPRENDRE LE RENSEIGNEMENT FINANCIER
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 2
chapters: 11
---

*Cinq chapitres pour cadrer ce que le FININT est, ce qu’il permet, ce qu’il ne permet pas, et comment il s’articule avec les disciplines voisines. Cette partie est la fondation : sans elle, les techniques des parties suivantes seraient utilisées hors-cadre.*

-----

## Chapitre 1 — Pourquoi le FININT est central aujourd’hui

### Objectif du chapitre

Comprendre pourquoi le renseignement financier — discipline relativement récente dans sa formalisation — est devenu un **levier central** des politiques de sécurité, des stratégies de conformité et de la compréhension de la criminalité organisée moderne. Ce chapitre n’expose pas une nostalgie historique : il pose les enjeux concrets qui justifient le poids actuel du FININT, et qui structurent la demande professionnelle adressée aux analystes.

### Le concept

Le **Financial Intelligence (FININT)** est la discipline qui collecte, analyse et exploite l’information financière — bancaire, comptable, patrimoniale, commerciale, registrale — pour détecter, comprendre, entraver et documenter la criminalité économique et le financement d’activités illicites. Le FININT ne se limite pas à la lecture des relevés bancaires : il englobe toute la chaîne d’information qui permet de **suivre l’argent** dans l’économie réelle, depuis l’origine présumée des fonds jusqu’à leur intégration finale.

Le FININT s’enracine historiquement dans la **lutte contre le blanchiment de capitaux** (LCB), formalisée dans les années 1980-1990 (création du GAFI en 1989, réseau Egmont en 1995), et étendue après le 11 septembre 2001 à la lutte contre le **financement du terrorisme** (CFT). Ce socle initial, devenu LCB-FT, s’est progressivement élargi à la corruption transnationale (suite aux scandales Enron, FCPA, à la Convention de Mérida 2003), à la fraude fiscale internationale (lendemain de la crise 2008, montée en puissance de l’EAR/CRS), aux sanctions économiques (en particulier post-2014 et plus encore post-2022), et à la criminalité organisée transnationale dans son ensemble.

### L’utilité opérationnelle

Plusieurs facteurs expliquent la centralité actuelle du FININT.

**Le suivi de l’argent est l’un des seuls leviers communs à toutes les criminalités.** Que l’on parle de trafic de stupéfiants, de cybercriminalité, de corruption, de fraude fiscale ou de financement du terrorisme, à un moment ou à un autre, l’argent doit circuler, être stocké, ou être intégré dans l’économie légale. C’est ce passage qui laisse des traces — et que le FININT exploite.

**Les sanctions économiques sont devenues un instrument de politique extérieure majeur.** L’OFAC, l’UE et l’ONU produisent et font évoluer en continu des listes de personnes et entités sanctionnées. La détection de contournements (via pays tiers, sociétés écrans, cryptos, intermédiaires complaisants) est devenue une priorité opérationnelle pour les États comme pour les institutions financières.

**La transparence financière s’est imposée comme une norme internationale.** L’EAR/CRS (échange automatique de renseignements fiscaux entre plus de 100 juridictions), les directives DAC successives en UE (DAC6, DAC7, DAC8), les registres des bénéficiaires effectifs, l’évolution post-MiCA pour les VASP, dessinent un environnement où le secret bancaire historique a perdu une grande partie de son efficacité — au moins en théorie. Les analystes savent exploiter ce nouveau paysage.

**La criminalité organisée s’est financiarisée.** Les groupes criminels modernes utilisent des structures sophistiquées : holdings, trusts, fondations, montages multi-juridictionnels, corporate service providers professionnels, réseaux de prête-noms. Les comprendre exige une compétence FININT — pas seulement une compétence judiciaire.

**La cybercriminalité a un débouché financier obligatoire.** Les rançons, les fonds volés via BEC, les revenus de la fraude en ligne, les produits de la traite, doivent tous être convertis et intégrés. Le FININT et la cybercriminalité convergent. Dans un dossier moderne, les analystes financiers et cyber doivent souvent coopérer (chapitre 48).

### Méthode — comment se positionner intellectuellement face à un dossier FININT

Le FININT n’est pas un domaine où l’on accumule des informations « parce que c’est intéressant ». Il est strictement **finalisé** : chaque collecte, chaque analyse, chaque livrable répond à une question — une question de renseignement (QR). Cette discipline finalisée est la première compétence à acquérir.

**Cinq postures professionnelles** structurent l’approche :

1. **Postulat du doute calibré** — toute information non vérifiée est une hypothèse. Toute corrélation n’est pas causalité.
1. **Discipline d’attribution** — chaque élément retenu doit être traçable à sa source. La fiabilité de la conclusion dépend de la fiabilité de la source.
1. **Calibration de la confiance** — chaque conclusion porte un niveau de confiance explicite (chapitre 33).
1. **Distinction faits / inférences / hypothèses** — vocabulaire calibré, formulations prudentes.
1. **Recul méthodologique** — pourquoi cherche-t-on cette information ? que va-t-elle changer dans la note ?

### Mini-walkthrough

Imaginons un mandat simple : *« Une équipe compliance d’une banque mutualiste signale qu’un client professionnel — une SAS de négoce de matériel agricole — reçoit depuis six mois des virements importants de Turquie, sans cohérence apparente avec l’activité déclarée. Que peut faire un analyste FININT ? »*.

Réponse opérationnelle : il **ne s’agit pas** de conclure que la SAS blanchit. Il s’agit de :

- formuler trois ou quatre questions de renseignement précises (QR1 : la SAS a-t-elle une activité réelle de négoce ? QR2 : qui sont les contreparties turques ? QR3 : quel est le profil du dirigeant ? QR4 : y a-t-il déjà des DS antérieures ou des éléments dans des leaks ?) ;
- identifier les sources mobilisables (registre français, registre turc, presse, leaks, OSINT sur la société, données bancaires si en cadre légal CRF) ;
- produire une **mini-note** à 45 minutes (parcours express) qui qualifie le dossier en *probable* / *à investiguer* / *peu d’éléments à ce stade* ;
- recommander si besoin l’approfondissement, ou la transmission à un autre service.

Tout l’art réside dans le passage de l’intuition (« ça sent mauvais ») à un livrable structuré et défendable.

### Erreurs fréquentes

- **Confondre intuition et analyse** : un signal n’est pas une conclusion. Il déclenche une enquête, il ne la termine pas.
- **Croire au mythe de la donnée parfaite** : un analyste FININT travaille toujours avec des données partielles, biaisées, parfois contradictoires. La méthode est ce qui transforme cette imperfection en livrable utile.
- **Sur-promettre** : *« on va trouver toute la vérité »*. Non. On va produire du renseignement actionnable, dans un cadre légal, dans un temps borné, avec des limites explicites.
- **Sous-estimer le judiciaire** : la note FININT n’est pas la fin de l’histoire. Elle est un point de bascule potentiel vers une procédure. La rigueur du livrable conditionne l’exploitabilité ultérieure.

### Limites

Le FININT ne **prouve pas** au sens judiciaire (chapitre 4). Il **oriente**. Il n’a pas accès direct aux moyens d’enquête réservés au judiciaire (perquisition, garde à vue, audition). Il dépend de la qualité des sources mobilisables — qui peuvent être fragmentaires, surtout dans les juridictions opaques (chapitre 10). Et il ne remplace pas l’expertise comptable, juridique, fiscale, sectorielle ; un analyste FININT travaille avec ces expertises, pas à leur place.

### Lien avec le fil rouge

> **CLEARFLOW — Cadrage**
> 
> Lorsque le dossier Haddad arrive sur le bureau de Nassim, il représente déjà 17 DS, une douzaine de sociétés présumées, sept juridictions et environ 22 M€ de flux. Si Nassim cherchait *« la vérité complète »*, il s’enliserait. Il commence donc par poser ses cinq questions de renseignement (QR1 à QR5) et estime un budget temps : 6 à 8 semaines pour produire une première note d’analyse robuste, avec coopérations engagées en parallèle. La discipline de cadrage est ce qui distingue une enquête FININT d’une accumulation de documents.

### Points clés à retenir

- Le FININT est une discipline **finalisée**, structurée par des questions de renseignement.
- Sa centralité actuelle découle de la convergence sanctions / transparence / financiarisation du crime / cyber.
- Le FININT produit du **renseignement orienté action**, pas de la connaissance pour la connaissance.
- Cinq postures professionnelles : doute calibré, attribution, calibration, distinction, recul.
- Les limites du FININT — non-preuve judiciaire, sources partielles, dépendance aux cadres légaux — sont à intégrer dès le cadrage.

-----

## Chapitre 2 — Ce que le FININT permet vraiment

### Objectif du chapitre

Cartographier précisément les **résultats utiles** que le FININT peut produire, pour ajuster les attentes et structurer les livrables. Un analyste qui sait ce que sa discipline permet réellement écrit mieux et déçoit moins.

### Le concept

Le FININT permet de produire **six grandes familles de résultats** opérationnels.

1. **Cartographies de réseaux** — qui détient quoi, qui dirige quoi, qui est lié à qui, par quel mécanisme (capital, mandat, parenté, adresse partagée, lien documentaire).
1. **Reconstitutions de flux** — d’où vient l’argent, par où transite-t-il, où va-t-il, sous quelle forme, à quels intervalles, avec quels libellés et quelles contreparties.
1. **Identifications de bénéficiaires effectifs** — la personne physique qui contrôle ultimement une structure, avec un niveau de confiance qualifié.
1. **Profils patrimoniaux** — comparaison entre actifs visibles, revenus déclarés, signaux de train de vie, et activité connue.
1. **Qualifications typologiques** — schéma X est compatible avec une typologie de blanchiment classique, de TBML, de carrousel TVA, de corruption, etc., avec un niveau de confiance.
1. **Recommandations actionnables** — signalement, gel, dissémination, sollicitations complémentaires, escalade vers le judiciaire.

Chaque résultat est livré avec une **traçabilité des sources** et un **niveau de confiance** : c’est ce qui le rend exploitable par d’autres acteurs (parquet, magistrat, équipe d’audit, comité de risque interne).

### L’utilité opérationnelle

Selon le contexte, ces résultats servent des fonctions différentes :

- **En CRF** : alimenter une transmission au parquet, une dissémination Egmont, un gel TRACFIN, ou enrichir une analyse stratégique sectorielle.
- **En conformité bancaire** : qualifier ou écarter un soupçon avant DS, motiver une rupture de relation d’affaires, alimenter un dossier d’audit interne.
- **En due diligence** : établir un rapport KYC/KYB approfondi avant entrée en relation, lors d’une fusion-acquisition, ou avant un partenariat stratégique.
- **En investigation journalistique** : étayer un article ou une enquête longue.
- **En cabinet d’avocat ou expert** : préparer une procédure civile, fiscale, ou pénale ; soutenir un client victime ; assurer une défense documentée.
- **En recouvrement d’actifs** : localiser des biens dissimulés, soutenir une saisie conservatoire ou une exécution forcée à l’international.

### Méthode — qu’est-ce qu’un livrable « utile »

Un livrable FININT utile vérifie cinq propriétés :

1. **Pertinent par rapport au mandat** — il répond aux questions de renseignement formulées au cadrage.
1. **Calibré en confiance** — chaque conclusion est accompagnée de son niveau de confiance.
1. **Sourcé** — chaque élément factuel est traçable.
1. **Actionnable** — il propose des suites, pas seulement des constats.
1. **Lisible par un non-expert** — un magistrat, un comité de risque ou un journaliste doit pouvoir l’exploiter sans avoir besoin de l’expliquer.

À l’inverse, un livrable FININT **non utile** : long, exhaustif, descriptif, sans conclusion claire, sans niveau de confiance, sans recommandation, illisible hors du cercle des analystes.

### Mini-walkthrough

Une demande typique : *« Voici un dirigeant suspect, dis-moi ce que tu peux dire de son patrimoine ».* Que peut produire le FININT ?

- **Patrimoine immobilier identifié** (au degré accessible aux sources ouvertes ou aux droits de communication) : trois biens en France, un en Espagne, peut-être un à Dubaï via une société écran. Niveau de confiance : *probable* à *quasi-certain* selon les sources.
- **Patrimoine financier visible** : participations dans 5 sociétés (registres), 1 fonds d’investissement (presse), comptes étrangers présumés via EAR/CRS (sources fermées, accessibles en CRF uniquement).
- **Train de vie observable** : véhicule de luxe identifié, voyages réguliers visibles sur réseaux sociaux, école privée pour les enfants.
- **Discordance avec revenus déclarés** : oui, significative — *facteur de soupçon élevé*, mais explicable par des sources non identifiées (héritage non documenté ? activités antérieures ?).

Conclusion calibrée : *« Le patrimoine identifié dépasse de plusieurs ordres de grandeur les revenus déclarés sur la période. Les origines des fonds ne sont pas établies par les sources mobilisées. Hypothèses non exclusives : revenus non déclarés, héritage non documenté, prête-nom, financement par tiers. Recommandation : approfondir via […] »*.

### Erreurs fréquentes

- **Promettre l’identification certaine d’un UBO masqué** dans une juridiction opaque sans sources fermées — souvent impossible.
- **Annoncer une « preuve de blanchiment »** : ce vocabulaire appartient au judiciaire, pas au renseignement.
- **Ignorer la dimension temporelle** : une cartographie est valable à une date. Six mois plus tard, l’organisation a peut-être muté.

### Limites

Le FININT **ne dit pas** :

- *« cette personne est coupable »* — c’est le tribunal qui dit cela ;
- *« ce flux prouve le blanchiment »* — il *est compatible avec* un schéma de blanchiment ;
- *« cette société est une société écran »* — sauf à pouvoir le démontrer rigoureusement (chapitre 26) ;
- *« telle juridiction est complaisante »* — c’est un débat politique et diplomatique.

### Lien avec le fil rouge

> **CLEARFLOW — Calibrage des attentes**
> 
> Au cadrage, Nassim explique au coordinateur du dossier ce qu’il pourra et ne pourra pas livrer. Il pourra reconstituer les flux observables, cartographier les sociétés et mandataires, identifier le patrimoine français visible, qualifier les schémas avec un niveau de confiance, et recommander les actions. Il ne pourra pas, sans coopération chypriote et émiratie, identifier de manière certaine les UBO finaux des structures offshore. Ce calibrage initial évite de promettre l’impossible.

### Points clés à retenir

- Six familles de résultats : réseaux, flux, UBO, patrimoine, typologies, recommandations.
- Un livrable utile est pertinent, calibré, sourcé, actionnable, lisible.
- Le FININT répond à un mandat ; il ne produit pas de la connaissance hors mandat.
- Le vocabulaire des conclusions doit être prudent et calibré.

-----

## Chapitre 3 — Ce que le FININT ne permet pas

### Objectif du chapitre

Tracer la **frontière des limites** du FININT. Cette frontière n’est pas un défaut de la discipline — elle est sa marque de sérieux. Connaître ses limites est ce qui permet de produire un livrable défendable et de ne pas conduire un demandeur à des décisions disproportionnées.

### Le concept

Trois grandes catégories de limites se recoupent en pratique.

**Limites épistémiques** — des choses que le FININT ne peut pas savoir, faute de sources accessibles. Exemple : l’UBO d’un trust irrévocable régi par un droit étranger sans registre public.

**Limites légales** — des sources auxquelles l’analyste n’a pas accès en cadre ouvert (relevés bancaires détaillés, données fiscales individuelles, informations couvertes par le secret professionnel). Ces sources sont mobilisables uniquement par des autorités compétentes (CRF avec droits de communication, magistrats, services d’enquête).

**Limites méthodologiques** — un raisonnement par corrélation ne prouve pas la causalité. Un faisceau d’indices, même solide, n’est pas une preuve judiciaire.

### L’utilité opérationnelle

Connaître ces limites évite trois erreurs lourdes :

1. **Promettre ce qu’on ne livrera pas** — sape la crédibilité du service auprès du demandeur.
1. **Conduire à une décision disproportionnée** — un gel, une rupture de relation, une dénonciation publique fondés sur du renseignement présenté comme une preuve peuvent entraîner des contentieux.
1. **Affaiblir l’exploitabilité judiciaire** — un livrable mal calibré, qui mélange faits, inférences et opinions, est difficilement exploitable par un magistrat.

### Méthode — comment formaliser les limites dans un livrable

Toute note FININT comporte une section **« Lacunes »** explicite. Elle liste :

- Les **sources non consultées** (et pourquoi : indisponibilité, hors cadre légal, contrainte de temps).
- Les **juridictions non couvertes** (parce que l’enquête s’est bornée à un périmètre, ou parce qu’aucune coopération n’a été obtenue).
- Les **données manquantes** structurelles (registres opaques, secret bancaire local).
- Les **délais et conditions** sous lesquels certaines lacunes pourraient être levées (réquisition, MLA, dissémination Egmont).

Cette section n’est pas un aveu de faiblesse : c’est un **élément de qualité** qui permet au demandeur de calibrer ses propres décisions et qui rend l’analyste honnête.

### Mini-walkthrough — trois exemples concrets

**Exemple 1 — Identification UBO en juridiction opaque.** Sans coopération internationale ou sans accès à des leaks pertinents, l’identification du bénéficiaire effectif d’une société aux Îles Vierges Britanniques (BVI) est généralement *indéterminable* à partir des seules sources ouvertes. Mention explicite à porter dans le livrable : *« UBO non identifié à partir des sources mobilisées ; identification effective conditionnée à une coopération via Egmont avec la CRF locale »*.

**Exemple 2 — Origine des fonds.** Sans accès aux relevés bancaires en amont (réquisition), il n’est pas possible d’établir avec certitude l’origine d’un dépôt de 500 000 € sur un compte. On peut au mieux émettre des hypothèses calibrées. Mention : *« Les éléments observés sont compatibles avec H1 [revenus professionnels non déclarés], H2 [héritage non documenté], H3 [prête-nom]. La résolution requiert une réquisition judiciaire des relevés du compte source »*.

**Exemple 3 — Intentionnalité.** Le FININT décrit des comportements et leur compatibilité avec des schémas. Il ne décrit pas les intentions internes des personnes. Affirmer *« X savait qu’il blanchissait »* relève du tribunal, sur la base de preuves d’intention (correspondances, témoignages, expertises).

### Erreurs fréquentes

- **Présenter une corrélation comme une preuve** — *« Mr X et Mr Y figurent dans les Panama Papers, donc ils sont complices »*. Non — ils figurent dans une fuite documentaire ; cela alimente une hypothèse, pas une conclusion.
- **Attribuer une intention** sans preuve directe.
- **Considérer le silence comme une preuve** — l’absence de réponse à une sollicitation n’est pas un aveu.
- **Conclure à partir d’une seule source** — toute conclusion forte doit reposer sur **au moins deux sources indépendantes** (chapitre 33).

### Limites — méta

Même les limites évoluent : un registre fermé peut s’ouvrir (pression réglementaire, leak), une source nouvelle peut apparaître (DAC8 pour les transactions crypto, base UBO post-AMLA), une décision de justice peut élargir l’accès. L’analyste maintient une veille permanente sur l’évolution des sources (chapitre 30 — non, en l’occurrence chapitre 50).

### Lien avec le fil rouge

> **CLEARFLOW — Cartographier les zones d’ombre**
> 
> Avant même de commencer son analyse, Nassim dresse une carte des **zones d’ombre prévisibles** dans le dossier Haddad : (a) les UBO finaux des structures chypriote, émiratie et libanaise — accessibles seulement via Egmont ; (b) les flux non bancaires (espèces, hawala suspecté) — non observables directement ; (c) la qualification d’éventuels marchés publics ouest-africains opaques — accessible seulement via coopération locale. Il documente ces zones d’ombre dans son cadrage initial, ce qui permet au coordinateur de prioriser les coopérations à engager.

### Points clés à retenir

- Trois familles de limites : épistémiques, légales, méthodologiques.
- Toute note FININT comporte une section **Lacunes** explicite.
- Une corrélation n’est pas une preuve ; un silence n’est pas un aveu ; une présence dans un leak n’est pas une condamnation.
- Calibrer les limites au cadrage initial protège l’analyste, le service et le demandeur.

-----

## Chapitre 4 — Renseignement, soupçon, preuve et judiciarisation

### Objectif du chapitre

Maîtriser **les quatre étapes** d’une chaîne d’information financière, de la donnée brute à la preuve judiciaire — et savoir où se situe le FININT dans cette chaîne. C’est le socle de la rigueur analytique qui distingue un professionnel d’un commentateur.

### Le concept

Quatre étapes hiérarchisées, chacune avec son **régime juridique** et son **régime de vérité**.

**1. La donnée.** Elle est ce qui est observable, factuel : un virement, une mention sur un registre, une déclaration de soupçon, une publication de presse. La donnée est le matériau brut. Elle peut être fiable ou non, complète ou non, datée ou non.

**2. Le soupçon.** Il naît quand la donnée présente des **éléments qualifiés** qui sortent de la normalité attendue. Le soupçon a un seuil légal en LCB-FT : il est l’élément déclencheur de la déclaration de soupçon (DS). Le seuil n’est ni la certitude ni la preuve — c’est un faisceau d’éléments objectifs qui justifie la déclaration. Le soupçon est une **lecture qualifiée** de la donnée.

**3. Le renseignement.** Il est produit par l’analyste à partir de plusieurs données et de plusieurs soupçons (DS convergentes, sources OSINT, sources fermées). Il **structure** une hypothèse, en évalue la confiance, identifie le réseau et les flux, et formule des recommandations. C’est le livrable FININT au sens strict.

**4. La preuve.** Elle est ce qui est **opposable devant un tribunal**. Elle doit avoir été obtenue dans un cadre légal admissible (réquisition judiciaire, audition, expertise judiciaire, perquisition autorisée). Le renseignement FININT n’est généralement pas une preuve directe : il est une **piste** qui oriente l’enquête judiciaire, laquelle, par ses propres actes, transforme certains éléments en preuves admissibles.

### L’utilité opérationnelle

Cette distinction structure tout le travail :

- **Au cadrage** : quelles sources puis-je mobiliser ? Quel est leur régime juridique ?
- **Pendant l’analyse** : ce que je vois, qu’est-ce que c’est — donnée, soupçon, renseignement ?
- **Dans le livrable** : quel vocabulaire, quel niveau d’affirmation ?
- **À la sortie** : à qui je transmets, sous quelles conditions, et que peut-on en faire ?

Mal positionner une information dans la chaîne, c’est **faire un faux pas opérationnel** : présenter une preuve quand on n’a qu’un soupçon (sur-promettre, faire du mal), ou inversement présenter un soupçon quand on a déjà du renseignement structuré (sous-vendre, faire perdre du temps).

### Méthode — la grille de qualification

Face à toute information, l’analyste applique une grille en quatre questions :

1. **Source** — qui est l’émetteur, dans quel cadre ai-je obtenu l’information ?
1. **Régime juridique** — l’information peut-elle être utilisée ouvertement, en interne, judiciairement ?
1. **Niveau de qualification** — donnée brute, soupçon, renseignement, preuve ?
1. **Niveau de confiance** — quasi-certain, probable, possible, indéterminable (chapitre 33) ?

Cette grille peut être tabulée pour chaque pièce du dossier. Elle accompagne ensuite la note d’analyse, comme matrice de sources.

### Mini-walkthrough — la chaîne CLEARFLOW

Reprenons un fragment du dossier Haddad pour illustrer la chaîne complète :

|Étape        |Élément                                                                                                                                                                                                                  |Régime                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|Donnée       |Un virement de 92 000 € de SOCIETE_DUBAI vers NEXUS_FRANCE le 14 mars                                                                                                                                                    |Observation                                                      |
|Soupçon      |Le virement s’inscrit dans une série de 18 virements similaires sur 6 mois, libellés vagues, contrepartie nouvelle, sans cohérence apparente avec l’activité déclarée → DS de la banque                                  |Déclaration LCB-FT                                               |
|Renseignement|Recoupé avec 16 autres DS et OSINT, le schéma est compatible avec une activité de TBML (probable, niveau de confiance modéré)                                                                                            |Note FININT, exploitable par autorités, non opposable au tribunal|
|Preuve       |Le procureur, sur la base du renseignement, ouvre une enquête. La réquisition judiciaire des relevés permet d’obtenir les pièces exploitables au tribunal. L’expertise comptable d’un expert judiciaire qualifie les flux|Pièces du dossier judiciaire                                     |

À chaque étape, ce qui change : la **qualification** (de l’observation à la qualification typologique à la qualification pénale), le **régime** (fait observable, déclaration légale, livrable analytique, pièce judiciaire), et l’**autorité** qui en est responsable (banque → analyste → magistrat).

### Erreurs fréquentes

- **Confondre DS et preuve** : une DS est un signalement légal, pas une affirmation de culpabilité. Le déclarant n’a pas besoin d’être certain — il a besoin d’avoir un soupçon qualifié.
- **Présenter le renseignement comme « la vérité »** : le renseignement est une lecture qualifiée à un instant donné. Il peut être révisé.
- **Ne pas baliser ce qu’on transmet** : transmettre un livrable sans préciser sa nature (« renseignement », « pré-rapport », « note de cadrage ») expose à des malentendus.

### Limites

Cette taxonomie est claire en théorie ; en pratique, certains éléments sont **ambigus** : une expertise privée commandée par une partie a-t-elle valeur de preuve ? Un rapport d’audit forensique peut-il être versé au dossier ? Un relevé obtenu en EAR/CRS est-il directement opposable ? Les réponses dépendent du droit national applicable et de l’usage qui en est fait. L’analyste consulte le juriste de son service en cas de doute.

### Lien avec le fil rouge

> **CLEARFLOW — Posture de Nassim**
> 
> Sa note finale (chapitre 64) commencera par cette phrase : *« La présente note constitue un livrable de renseignement financier au sens de l’article L.561-29 CMF [équivalent fictif]. Elle vise à orienter l’enquête. Elle n’est pas opposable en l’état comme pièce judiciaire. Les éléments qu’elle expose sont calibrés en confiance ; les pièces sous-jacentes sont conservées dans le dossier de référence et peuvent être communiquées au magistrat sur demande, dans le cadre approprié. »* Cette phrase n’est pas une formalité : elle protège l’analyste, le service, et l’exploitabilité ultérieure.

### Points clés à retenir

- Quatre étapes : donnée → soupçon → renseignement → preuve.
- Chaque étape a son régime juridique et son régime de vérité.
- Le FININT produit du renseignement ; il ne produit pas de preuve directe.
- La grille de qualification (source / régime / qualification / confiance) accompagne tout livrable sérieux.

-----

## Chapitre 5 — FININT, OSINT financier, AML, CTI et OSINT Crypto

### Objectif du chapitre

Positionner le FININT par rapport aux disciplines voisines, pour éviter les confusions et exploiter au mieux les complémentarités. Beaucoup de dossiers modernes mobilisent plusieurs disciplines simultanément ; un analyste qui ne sait pas où il se situe ne sait pas non plus à qui s’adresser pour ce qu’il ne fait pas lui-même.

### Le concept

Plusieurs disciplines coexistent et se recoupent :

- **AML / LCB-FT** (Anti-Money Laundering / Lutte contre le blanchiment et le financement du terrorisme) — discipline réglementaire centrée sur la **conformité** : KYC, KYB, monitoring, déclaration de soupçon, screening sanctions, gel. Elle est portée par les **assujettis** (banques, PSP, etc.) avec des obligations légales précises.
- **FININT** — discipline analytique et de **renseignement** centrée sur l’exploitation de l’information financière pour comprendre, détecter, qualifier et orienter l’action contre la criminalité économique. Pratiquée en CRF, en services d’enquête, en cabinets d’investigation, en compliance avancée.
- **OSINT financier** — sous-ensemble de l’OSINT spécialisé sur les **sources ouvertes financières et économiques** : registres, comptes annuels, presse, leaks, marchés publics, SOCMINT financier. C’est une **boîte à outils** mobilisée par le FININT.
- **CTI** (Cyber Threat Intelligence) — discipline de renseignement sur la **menace cyber** : acteurs, TTP, infrastructures, indicateurs. Lorsqu’une criminalité est cyber-financière (ransomware, BEC, hacks DeFi), CTI et FININT convergent.
- **OSINT Crypto** — discipline d’enquête **on-chain** : blockchains, transactions, wallets, mixers, bridges, DEX, privacy coins, cashout. C’est le complément naturel du FININT pour le volet crypto-actifs.

### L’utilité opérationnelle

Concrètement, dans un dossier moderne :

- **AML** détecte et signale (banque émet une DS).
- **FININT** reçoit, recoupe, analyse, qualifie et oriente (CRF produit une note).
- **OSINT financier** alimente le FININT en sources ouvertes (registres, presse, leaks).
- **CTI** alimente quand le dossier comporte un volet cyber (acteur ransomware identifié, TTP connue).
- **OSINT Crypto** alimente quand le dossier comporte une branche on-chain.

Aucune de ces disciplines n’est « supérieure » aux autres. Elles **se complètent**. Un bon analyste FININT sait *quand* solliciter une autre discipline, et *comment* exploiter ce qu’elle lui rend.

### Méthode — comment articuler les disciplines

Trois principes :

1. **Spécifier les questions adressées à chaque discipline.** Demander à un analyste OSINT Crypto *« est-ce qu’il blanchit ? »* est inopérant. Demander *« peux-tu tracer les fonds depuis cette adresse de dépôt sur l’exchange jusqu’aux destinations finales et identifier les off-ramps ? »* l’est. Le FININT pose des questions techniquement précises.
1. **Recevoir et intégrer les livrables.** Un rapport CTI, un rapport OSINT Crypto, un rapport AML interne d’une banque ne sont pas du renseignement FININT directement utilisable — ils sont des **intrants**. Le FININT les recoupe, en évalue la fiabilité, et les intègre dans une note unifiée.
1. **Documenter la chaîne d’attribution.** Quand le livrable FININT mobilise du renseignement crypto produit par un cabinet externe, le cours OSINT Crypto recommande explicitement (Chapitre 47) une calibration des sources — l’analyste FININT applique le même standard pour citer ces apports : *« L’analyse on-chain conduite par Athéna Group (rapport référencé X) conclut, avec un niveau de confiance “probable”, que les fonds atteignent un exchange non-KYC … »*.

### Mini-walkthrough — qui fait quoi dans CLEARFLOW

|Question                                                   |Discipline              |Acteur                      |
|-----------------------------------------------------------|------------------------|----------------------------|
|Les DS de banques détectent-elles la structuration ?       |AML                     |Compliance des banques      |
|Quelle est la cartographie des sociétés liées à Haddad ?   |FININT + OSINT financier|Nassim                      |
|Y a-t-il des éléments dans les Panama/Pandora Papers ?     |OSINT financier (leaks) |Nassim, ICIJ Aleph          |
|Quelle est la trajectoire des USDT envoyés sur l’exchange ?|OSINT Crypto            |Sarah Marin (Athéna)        |
|Y a-t-il un exploit cyber dans le BEC suspecté ?           |CTI                     |Service partenaire ou Athéna|
|Quel rapport final pour le PNF ?                           |FININT (intégrateur)    |Nassim                      |

C’est le FININT qui **intègre** toutes les contributions et produit le livrable final unifié. Sans intégration, on a une collection de rapports déconnectés.

### Erreurs fréquentes

- **Demander à une discipline ce qu’elle ne fait pas** — par exemple demander à un analyste OSINT Crypto une analyse des comptes annuels d’une SAS française.
- **Faire double emploi** — refaire dans le rapport FININT le détail blockchain qu’a déjà produit l’analyste crypto. Le rapport FININT renvoie, il ne refait pas.
- **Sous-utiliser l’OSINT financier** — beaucoup d’analystes FININT en CRF passent peu de temps sur les registres internationaux ou les leaks alors que les retours opérationnels y sont élevés.

### Limites

La frontière entre disciplines n’est pas toujours nette. Un analyste FININT senior maîtrise une partie de l’OSINT financier classique. Un analyste OSINT Crypto avec passé TRACFIN maîtrise une partie du FININT classique (cas Sarah Marin). C’est plus souvent une **question de profil** que de discipline pure. L’organisation prime : qui livre quoi, à qui, sous quelle responsabilité.

### Lien avec le fil rouge

> **CLEARFLOW — Architecture des coopérations**
> 
> Nassim dessine, dès le cadrage, l’architecture des coopérations : OSINT financier en interne (registres, leaks, presse), branche crypto sous-traitée à Athéna Group / Sarah Marin avec un mandat précis (« tracer USDT depuis l’exchange jusqu’aux off-ramps », pas « est-ce que c’est du blanchiment ? »), branche cyber éventuelle sous-traitée à un service partenaire si BEC se confirme, AML restant chez les banques déclarantes (Nassim ne refait pas leur monitoring). Cette architecture évite les redondances et les angles morts.

### Points clés à retenir

- AML, FININT, OSINT financier, CTI, OSINT Crypto sont **complémentaires**, pas concurrents.
- Le FININT est la discipline **intégratrice** quand un dossier mobilise plusieurs angles.
- Les questions adressées aux disciplines voisines doivent être **techniquement précises**.
- Le livrable FININT renvoie, il ne refait pas — particulièrement pour la branche crypto (renvoi systématique au cours OSINT Crypto).

-----
