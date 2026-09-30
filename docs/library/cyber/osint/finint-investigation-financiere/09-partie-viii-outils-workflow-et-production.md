---
title: PARTIE VIII — OUTILS, WORKFLOW ET PRODUCTION
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 9
chapters: 11
---

*Six chapitres pour structurer la pratique : workflow d’enquête complet, outils gratuits, outils professionnels, visualisation, chaîne de preuve, livrables et diffusion. Cette partie transforme la méthode en pratique organisée.*

-----

## Chapitre 49 — Workflow complet d’une enquête FININT

### Objectif du chapitre

Décrire un **workflow complet** d’enquête FININT, du signalement initial au livrable final. Ce workflow est une trame, pas un dogme : il s’adapte à chaque dossier mais en respecte la logique.

### Le workflow en 9 phases

**Phase 1 — Réception et triage.** Le signalement arrive (DS, sollicitation, plainte, demande externe). Triage : urgence, ressources, périmètre approximatif, doublon avec dossier existant.

**Phase 2 — Cadrage initial.** L’analyste pose les questions de renseignement (QR), estime le budget temps, identifie les ressources nécessaires, identifie les coopérations à activer, documente les zones d’ombre prévisibles.

**Phase 3 — Stabilisation des identités.** Identification rigoureuse des entités et personnes (chapitres 19-20). Pas d’enquête de fond sans cette étape.

**Phase 4 — Collecte OSINT.** Registres, comptes annuels, marchés publics, presse, leaks, SOCMINT — tous les sources accessibles selon le périmètre (Partie III).

**Phase 5 — Mobilisation des sources fermées.** En CRF : droits de communication, EAR/CRS, FICOBA, coopérations Egmont. En cabinet : limites strictes.

**Phase 6 — Analyse.** Construction des fiches (personne, société, flux, actif). Graphes relationnels. Analyse de flux et comptabilité (Partie VI). Qualification typologique (Partie VII).

**Phase 7 — Calibration.** Application de l’échelle WEP. Distinction faits / inférences / hypothèses. Documentation des lacunes.

**Phase 8 — Rédaction.** Note FININT structurée (chapitre 54). Modèle K en annexe.

**Phase 9 — Diffusion et suivi.** Transmission aux autorités compétentes. Suivi des coopérations engagées. Mise à jour du dossier au fil des retours.

### Durée typique

Pour un dossier de complexité moyenne (réseau de 10-15 entités, 3-5 juridictions, plusieurs DS convergentes) : 4 à 12 semaines de travail effectif, avec phases de relance lors des coopérations internationales (2 à 8 semaines additionnelles).

### L’utilité opérationnelle

Le workflow structure :

- **Le temps de l’analyste** : pas de dispersion.
- **La qualité du livrable** : chaque phase a son output.
- **La coopération** : chaque acteur sait où on en est.
- **La répétabilité** : un même protocole pour différents dossiers permet apprentissage et amélioration.

### Erreurs fréquentes

- **Sauter le cadrage initial** : on commence à collecter avant de savoir ce qu’on cherche.
- **Ne pas documenter les zones d’ombre** : le rapport devient lisse et trompeur.
- **Sous-estimer les coopérations internationales** : les délais sont structurellement longs.

### Limites

Le workflow doit être adapté. Un dossier d’urgence (BEC en cours, asset recovery rapide) compresse les phases. Un dossier d’investigation profonde les étend.

### Lien avec le fil rouge

> **CLEARFLOW — Workflow Nassim**
> 
> Nassim suit ce workflow strict : phases 1-2 en 3 jours (triage + cadrage), phase 3 en 2 jours (stabilisation), phase 4 sur 2-3 semaines (collecte OSINT), phase 5 en parallèle (coopérations), phase 6 sur 2-3 semaines (analyse), phase 7-8 sur 1 semaine (calibration et rédaction), phase 9 ouverte (suivi long). Le dossier est consolidé en environ 8 semaines.

### Points clés à retenir

- 9 phases : réception, cadrage, stabilisation, collecte OSINT, sources fermées, analyse, calibration, rédaction, diffusion.
- Workflow = trame, à adapter.
- Documentation et traçabilité à chaque phase.

-----

## Chapitre 50 — Outils gratuits : registres, sanctions, presse, leaks

### Objectif du chapitre

Recenser les **outils gratuits ou freemium** utilisables en FININT pour un travail solide sans budget.

### Catalogue raisonné

**Registres d’entreprises (chapitres 11-12)** :

- France : Pappers, INPI/data.inpi.fr, Infogreffe (partiellement gratuit), BODACC.
- UK : Companies House.
- US : OpenCorporates, SEC EDGAR, registres étatiques.
- UE : BRIS via e-justice.europa.eu.
- Multi-pays : OpenCorporates (agrégateur, freemium).

**UBO et bénéficiaires effectifs (chapitre 13)** :

- France RBE : accès restreint depuis CJUE.
- UK PSC : Companies House.
- Pandora / Panama / Paradise / Pandora Papers : Offshore Leaks ICIJ.

**Sanctions et PEP** :

- OpenSanctions.org : base agrégée gratuite (sanctions OFAC, UE, ONU, OFSI, et plus).
- Site OFAC, UE consolidated list, ONU, OFSI.
- Sanctions.io : lecture libre partielle.

**Adverse media et presse** :

- Google News (avec limites).
- Médias référents accessibles en consultation gratuite.
- ICIJ Aleph (accès journalistique principalement).
- OCCRP Aleph (selon partenariats).

**Comptes annuels** :

- France : Pappers, Infogreffe.
- UK : Companies House.
- Allemagne : Bundesanzeiger.
- Belgique : Moniteur belge.

**Marchés publics** :

- BOAMP, data.gouv.fr (DECP), TED, SAM.gov, USAspending.gov.

**Patrimoine** :

- DVF (Demandes de valeurs foncières) data.gouv.fr.
- Patrim (accès via espace personnel impots.gouv.fr — limité aux usages personnels).
- Cadastre.gouv.fr.
- Bases yachts/maritime : MarineTraffic (free tier).
- Bases aéronefs : FlightAware, ADS-B Exchange.

**Visualisation gratuite** :

- Maltego (free tier, transforms limitées).
- Gephi (open source).
- Cytoscape.
- Excel/LibreOffice (graphes simples).

**Recherche d’images inverse** :

- Google Images.
- TinEye.
- Yandex.

**Archives web** :

- Web Archive (Wayback Machine).
- archive.today.

**OSINT général utile en FININT** :

- IntelTechniques (outils OSINT).
- OSINT Framework.
- Bellingcat investigations toolkit.

### Méthode — workflow gratuit type

Pour un dossier sans budget, l’enchaînement standard :

1. Pappers + INPI + Companies House + OpenCorporates → identification + cartographie initiale.
1. ICIJ Offshore Leaks → recoupement leaks.
1. OpenSanctions → screening sanctions/PEP.
1. Google + agrégateurs gratuits → adverse media.
1. DVF + cadastre + MarineTraffic → patrimoine français visible.
1. Gephi → visualisation finale.

Couvre 70-80 % d’une enquête de complexité moyenne avec un budget de 0 €.

### Erreurs fréquentes

- **Sous-estimer ce qu’on peut faire gratuitement.** Beaucoup d’analystes débutent en pensant que l’OSINT financier est inaccessible — c’est faux.
- **Surestimer la profondeur des outils gratuits.** Pour les juridictions opaques, le multi-juridictionnel intensif, l’agrégation à grande échelle, des outils professionnels sont nécessaires.

### Limites

Les outils gratuits ont des **plafonds** (nombre de requêtes, profondeur de couverture, fréquence de mise à jour). Pour des dossiers complexes ou volumineux, les outils professionnels apportent une vraie valeur ajoutée.

### Lien avec le fil rouge

> **CLEARFLOW — Phase OSINT gratuite**
> 
> Nassim utilise gratuitement Pappers, Companies House, OpenCorporates, OpenSanctions, Offshore Leaks pour le travail de cartographie initial. L’investissement dans Sayari (chapitre 51) intervient pour étendre la couverture sur les juridictions à risque où les outils gratuits sont insuffisants.

### Points clés à retenir

- Beaucoup d’OSINT financier est accessible gratuitement.
- Catalogue raisonné par usage.
- Plafond des gratuits → bascule vers professionnels selon complexité.

-----

## Chapitre 51 — Outils professionnels : Sayari, Orbis, World-Check, Dow Jones, LexisNexis

### Objectif du chapitre

Présenter les **principaux outils professionnels** utilisés en FININT, leurs forces, leurs usages, leur coût.

### Catalogue raisonné

**Sayari** : référence moderne pour l’OSINT financier multi-juridictionnel. Agrège registres mondiaux, sanctions, leaks, contentieux. Particulièrement fort sur la cartographie de réseaux et l’identification d’UBO indirects. Tarif annuel : selon licence, allant de plusieurs milliers à plusieurs dizaines de milliers d’euros.

**Orbis** (Moody’s / Bureau van Dijk) : base massive de sociétés mondiales avec données financières, dirigeants, actionnariat, indicateurs de risque. Standard historique du due diligence. Tarif élevé.

**Dun & Bradstreet** : équivalent fonctionnel à Orbis, plus orienté évaluation de risque commercial.

**World-Check (Refinitiv / LSEG)** : base PEP, sanctions, adverse media. Standard de l’industrie financière pour le screening KYC.

**Dow Jones Risk & Compliance** : équivalent de World-Check, agrégateur de risque.

**LexisNexis Diligence** : équivalent, avec couverture juridique et adverse media plus large.

**Factiva (Dow Jones)** : base presse internationale, indispensable pour l’adverse media approfondi.

**Nexis Newsdesk** : équivalent presse.

**Refinitiv Eikon** : données marchés financiers, indispensable pour les analyses sur sociétés cotées.

**S&P Capital IQ** : équivalent.

**Bloomberg Terminal** : référence absolue (et chère) pour les marchés financiers.

**ICIJ Aleph** : accès professionnel (journalisme).

**OCCRP Aleph** : accès professionnel.

**Outils crypto pro** : Chainalysis Reactor, TRM Labs, Elliptic (renvoi OSINT Crypto).

### L’utilité opérationnelle

Les outils professionnels apportent :

- **Couverture** plus large (juridictions, périodes, types de données).
- **Agrégation** : recherche unifiée sur des sources hétérogènes.
- **Détection d’UBO indirects** : algorithmes propriétaires de remontée de chaîne.
- **Mise à jour** : fréquence supérieure aux outils gratuits.
- **Garanties qualité** : sources vérifiées, méthodologies documentées.

### Méthode — choix d’outil par usage

- **Cartographie de réseau multi-juridictionnel** : Sayari > Orbis.
- **Due diligence due process** : Orbis + Dun & Bradstreet + World-Check + Factiva.
- **Screening PEP/sanctions à grande échelle** : World-Check ou Dow Jones R&C.
- **Adverse media profond** : Factiva + LexisNexis.
- **Cotées et marchés** : Refinitiv Eikon, S&P, Bloomberg.
- **Crypto** : renvoi OSINT Crypto.

### Erreurs fréquentes

- **Croire que l’outil remplace l’analyse.** Un graphe Sayari ne fait pas l’analyse à votre place.
- **Surinterpréter les scores de risque** propriétaires : ils sont des indicateurs, pas des conclusions.
- **Négliger les sources gratuites** une fois équipé professionnel : la complémentarité reste utile.

### Limites

Tarifs élevés (10K à 100K+ EUR par an selon licence). Couverture inégale selon juridictions et secteurs. Confiance variable selon la maturité de l’outil sur un domaine particulier.

### Lien avec le fil rouge

> **CLEARFLOW — Sayari pour les juridictions à risque**
> 
> Nassim mobilise Sayari pour étendre la cartographie sur Chypre, Émirats, Liban — là où les outils gratuits étaient insuffisants. Le retour est élevé : identification de plusieurs entités liées non repérées en OSINT gratuit, recoupements UBO précieux.

### Points clés à retenir

- Sayari, Orbis, World-Check, Dow Jones R&C, LexisNexis, Factiva : outils professionnels de référence.
- Tarifs élevés, couverture supérieure.
- Choix par usage opérationnel.
- L’outil ne remplace pas l’analyste.

-----

## Chapitre 52 — Visualisation : Maltego, i2, Linkurious, Gephi, Graphistry

### Objectif du chapitre

Maîtriser les **outils de visualisation** pour construire des graphes relationnels FININT exploitables.

### Catalogue raisonné

**Maltego** : standard OSINT depuis 15+ ans. Forces : transforms multiples (intégrations natives avec dizaines de sources), modélisation de graphes, exploration interactive. Versions : Community (gratuite, limitée), Pro, Enterprise.

**i2 Analyst’s Notebook (IBM)** : standard du renseignement institutionnel et police. Forces : analyse de cas complexes, modèles temporels, intégration avec bases policières. Lourd à prendre en main mais très puissant. Coût élevé.

**Linkurious Enterprise** : plateforme web-based, backend Neo4j. Forces : exploration interactive grands graphes, collaboration multi-utilisateurs, audit. Adopté par certaines CRF et banques.

**Gephi** : open source, orienté analyse de données (centralités, communautés, layout). Excellent pour les graphes statiques de présentation.

**Graphistry** : web-based, accélération GPU pour très grands graphes. Forces : performance, exploration interactive, intégration analytique.

**Cytoscape** : open source, à l’origine biologique, utilisable pour réseaux financiers.

**Neo4j** : base de données graphe utilisée comme backend de plusieurs outils. Requêtes Cypher pour l’analyse.

**Excel / Power BI** : pour les analyses simples ou les présentations exécutives. Sous-estimé par les analystes techniques.

### Méthode — choix d’outil par contexte

- **Exploration interactive, peu de nœuds (< 100)** : Maltego.
- **Cas complexe institutionnel, intégration policière** : i2.
- **Très grand graphe (1000+)** : Linkurious ou Graphistry.
- **Présentation finale propre** : Gephi (export image), Linkurious.
- **Analyse de centralités, communautés** : Gephi.
- **Public exécutif, simple** : Excel / PowerBI.

### L’utilité opérationnelle

Le bon outil :

- **Accélère** la construction du graphe.
- **Permet la calculation** des métriques (centralité, communautés).
- **Communique** efficacement le résultat.

Le mauvais outil :

- **Ralentit** le travail (limites de performance).
- **Cache** la complexité (graphe illisible).
- **Trompe** par mauvais layout.

### Erreurs fréquentes

- **Penser que la visualisation prouve quelque chose.** Elle illustre.
- **Surcharger** le graphe : 200 nœuds visibles = illisible.
- **Ne pas annoter** les arcs et les nœuds : ambiguïté.

### Limites

Aucun outil ne fait l’analyse — l’analyste pose les bonnes questions et interprète.

### Lien avec le fil rouge

> **CLEARFLOW — Linkurious pour le dossier**
> 
> Le dossier Haddad, avec ~40 nœuds principaux, est construit dans Linkurious (licence du service). Maltego sert pour l’exploration initiale, Gephi pour le graphe final présentable. Le travail visualisation prend environ 1 jour cumulé.

### Points clés à retenir

- Maltego (OSINT standard), i2 (institutionnel), Linkurious (web grand graphe), Gephi (analyse + présentation), Graphistry (GPU).
- Choix par contexte.
- La visualisation illustre, ne prouve pas.

-----

## Chapitre 53 — Chaîne de preuve, captures, horodatage, hash

### Objectif du chapitre

Maîtriser la **discipline de chaîne de preuve** : capture des sources, horodatage, hashing, archivage — pour que les éléments collectés restent exploitables et défendables.

### Le concept

La **chaîne de preuve** (chain of custody) est la traçabilité des éléments d’enquête : qui a collecté, quand, où, comment, avec quelle modification, qui les a transmis, à qui. Une chaîne de preuve solide est nécessaire pour :

- Garantir l’**intégrité** des éléments.
- Permettre la **reproduction** par un tiers (juge, magistrat, expert).
- Éviter les contestations d’authenticité.

### Bonnes pratiques

**Capture** : pour chaque élément OSINT collecté :

- Capture d’écran (PNG, PDF) ou enregistrement HTML brut.
- URL exacte de la source.
- Date et heure de capture (avec fuseau horaire).
- Identifiant de l’analyste.

**Horodatage** : utilisation de services d’horodatage tiers pour les éléments critiques (Tiers de confiance, service notarisation horaire). Pour la grande majorité des cas, l’horodatage interne (système de fichiers + journal de l’analyste) suffit.

**Hash** : pour les fichiers téléchargés (rapports, documents PDF, archives), calculer un hash SHA-256 (ou SHA-512) au moment du téléchargement. Le hash garantit l’intégrité.

**Archivage** : stockage dans un système de gestion de dossiers (DMS) avec contrôle d’accès, journalisation, sauvegarde. En CRF : système agréé. En cabinet : à minima répertoire sécurisé avec contrôle d’accès.

**Annotation** : chaque élément annoté de son contexte (pourquoi collecté, qu’apporte-t-il).

**Transmission** : transmission par canaux sécurisés (chiffrement bout en bout, courriers chiffrés, plateformes professionnelles).

### Méthode — workflow type

À chaque collecte :

```
[date/heure] [analyste] capture [URL]
- Capture : nom_fichier.png (hash SHA-256)
- Archive HTML : nom_fichier.html
- PDF source : nom_fichier.pdf (hash)
- Note : pourquoi collecté, qu'apporte-t-il
- Tags : entité concernée, type de source
```

Outils utiles : extensions navigateur de capture (Singlefile pour HTML complet, Hunchly pour OSINT), gestionnaires de notes (Obsidian, Notion, Joplin), DMS internes.

### Erreurs fréquentes

- **Pas de capture** : on s’appuie sur une URL qui change ou disparaît.
- **Pas d’horodatage** : on perd la séquence des collectes.
- **Pas de hash** : on ne peut pas prouver l’intégrité.
- **Stockage non sécurisé** : risque de fuite ou de perte.

### Limites

La chaîne de preuve OSINT n’a pas la même valeur judiciaire qu’une saisie sous procédure. Mais une chaîne propre rend le livrable beaucoup plus crédible.

### Lien avec le fil rouge

> **CLEARFLOW — Chain of custody Nassim**
> 
> Sur 8 semaines de travail, Nassim accumule environ 1 200 captures (HTML, PNG, PDF). Toutes archivées dans le DMS interne de la CRF, hashées, horodatées, tagées par entité. Cette discipline rend la note finale **reproductible** : un tiers peut suivre chaque chaîne.

### Points clés à retenir

- Chaîne de preuve = intégrité + reproductibilité + non-contestation.
- Pratiques : capture, horodatage, hash, archivage, annotation, transmission sécurisée.
- Outils : Singlefile, Hunchly, Obsidian, DMS interne.

-----

## Chapitre 54 — Note FININT, rapport et diffusion

### Objectif du chapitre

Maîtriser la **rédaction et la diffusion** d’une note FININT — livrable final du travail. Modèle complet en annexe K.

### Structure type d’une note FININT

1. **En-tête** : référence, date, version, classification (TLP), auteur, destinataires.
1. **Résumé exécutif** : 10-15 lignes maximum, conclusions calibrées, recommandations.
1. **Mandat et questions de renseignement** : ce qu’on a cherché à établir.
1. **Méthodologie** : sources mobilisées, limites du périmètre.
1. **Analyse** : organisée par thèmes (entités, personnes, flux, typologie).
1. **Hypothèses calibrées** : explicitement formulées, avec niveau WEP.
1. **Lacunes** : ce qui n’a pas pu être établi, pourquoi, comment.
1. **Recommandations** : actions concrètes (signalement, gel, coopération, approfondissement).
1. **Annexes** : fiches personne, société, flux, actif ; graphes ; sources détaillées.

### Style de rédaction

- **Phrases courtes**, claires.
- **Vocabulaire prudent** : « les éléments observés sont compatibles avec », « l’hypothèse la plus robuste est », « niveau de confiance probable ».
- **Pas de jargon non défini**.
- **Faits / inférences / hypothèses** distincts.
- **Sources** systématiquement référencées (par numéro, avec liste en annexe).

### Classification TLP

Standard utilisé en renseignement :

- **TLP:WHITE** ou **TLP:CLEAR** — diffusion libre.
- **TLP:GREEN** — diffusion à la communauté (peers).
- **TLP:AMBER** — diffusion restreinte aux destinataires et à leur organisation.
- **TLP:AMBER+STRICT** — destinataires uniquement.
- **TLP:RED** — destinataires nominatifs uniquement.

La note FININT typique : TLP:AMBER.

### Diffusion

- **Autorités judiciaires** : transmission via canal officiel (réquisitions, articles 40 CPP en France, équivalents internationaux).
- **CRF étrangères** : via FIU.NET (UE) ou Egmont Secure Web (mondial).
- **Services partenaires nationaux** : canaux établis (DGSI, DGDDI, DGFiP, etc.).
- **Communication interne** : selon le format et la classification.

### L’utilité opérationnelle

La note FININT est le **point culminant** du travail. Sa qualité détermine son exploitation :

- Une note claire et calibrée est utilisée par les magistrats.
- Une note confuse ou non calibrée est mise de côté.

### Erreurs fréquentes

- **Note trop longue** : un magistrat lit le résumé exécutif. S’il est obscur, le reste est ignoré.
- **Vocabulaire affirmatif sans calibration** : risque de contestation et de perte de crédibilité.
- **Pas de recommandations** : la note décrit mais ne propose pas.
- **Pas de lacunes** : sape la confiance.

### Limites

La note est un livrable, pas une fin. Le suivi (coopérations, retours, mises à jour) continue après.

### Lien avec le fil rouge

> **CLEARFLOW — Note finale**
> 
> Au terme des 8 semaines, Nassim produit une note de 24 pages (corps + 7 fiches personne, 14 fiches société, 22 fiches flux, 11 fiches actif, 1 graphe principal). Résumé exécutif d’1 page. Recommandations claires. Transmission au PNF, TRACFIN coordinateur, et coopérations internationales engagées en parallèle.

### Points clés à retenir

- Note FININT = livrable structuré, calibré, sourcé, actionnable.
- Résumé exécutif essentiel.
- Classification TLP.
- Diffusion par canaux officiels.

-----
