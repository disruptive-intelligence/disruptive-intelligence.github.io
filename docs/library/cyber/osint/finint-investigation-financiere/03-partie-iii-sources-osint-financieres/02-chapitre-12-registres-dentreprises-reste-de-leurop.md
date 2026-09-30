---
title: 'Chapitre 12 — Registres d’entreprises : reste de l’Europe et du monde'
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Étendre la couverture aux **autres juridictions clés** : reste de l’UE, Suisse, juridictions offshore, pays émergents. La logique reste la même qu’au chapitre 11 ; les outils et les degrés d’ouverture varient.

## Le concept

Hors France/UK/US, l’analyste mobilise plusieurs niveaux de sources :

1. **Registres nationaux directs** quand ils sont accessibles en ligne et en langue exploitable.
1. **Portails européens consolidés** (e-Justice, BRIS).
1. **Agrégateurs tiers** (OpenCorporates, Sayari, Orbis, Dun & Bradstreet — chapitres 50-51).
1. **Bases UBO européennes** (chapitre 13).

## Méthode — registres clés par juridiction

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

## Portails européens consolidés

**BRIS (Business Registers Interconnection System)** — portail européen e-Justice qui interconnecte les registres nationaux des États membres. [e-justice.europa.eu](https://e-justice.europa.eu/). Recherche cross-border simplifiée.

**EBOCS (European Business Ownership and Control Service)** — agrégation des registres UE pour les analystes professionnels.

## L’utilité opérationnelle

Pour un dossier multi-juridictionnel, la séquence type :

- **OpenCorporates** pour la vue agrégée initiale.
- **Registres nationaux directs** pour la validation et les actes.
- **BRIS** pour les recherches transfrontalières en UE.
- **Sayari, Orbis** (chapitres 50-51) si abonnement disponible — couverture internationale plus large et plus complète.

## Mini-walkthrough

Cible : OMEGA HOLDINGS LTD, Chypre, identifiée dans une DS comme contrepartie d’un flux de 850 K€.

- OpenCorporates : trouvée — Cyprus, registered 2019, status active.
- Registre chypriote (Department of Registrar of Companies and Intellectual Property) : accès en ligne, partiellement gratuit. Identification confirmée. Directors visibles ; UBO **non public** (accès limité depuis l’arrêt CJUE 2022 — chapitre 13).
- Recherche complémentaire via leaks : présence d’OMEGA HOLDINGS dans Pandora Papers ? (chapitre 18).
- Sayari (si disponible) : recoupement avec dossiers similaires.

## Erreurs fréquentes

- **Se contenter d’OpenCorporates.** Utile pour la vue agrégée mais souvent en retard sur les modifications récentes.
- **Ne pas tester plusieurs orthographes** dans les langues étrangères (translittérations, accents, articles initiaux).
- **Sous-estimer les agrégateurs locaux** (Qichacha en Chine, YouControl en Ukraine).

## Limites

Beaucoup de registres asiatiques, africains, ou caribéens sont peu accessibles ou peu fiables. La coopération internationale (Egmont) et les leaks deviennent alors les principaux leviers.

## Lien avec le fil rouge

> **CLEARFLOW — Multi-juridictions**
> 
> Nassim mobilise BRIS pour les sociétés européennes du dossier Haddad (CY, FR, DE, NL), OpenCorporates pour la vue agrégée, Sayari (licence du service) pour la validation et l’extension du graphe, registres locaux émiratis pour les sociétés Free Zone identifiées, et coopération via Egmont pour les juridictions inaccessibles (Liban). Le travail prend 4 à 5 jours pour la cartographie complète.

## Points clés à retenir

- Hors France/UK/US, mobilisation d’un mix : registres nationaux + portails consolidés + agrégateurs.
- BRIS est le portail UE de référence pour la recherche multi-juridictions.
- Les juridictions caribéennes et certaines asiatiques exigent leaks + coopération.

-----
