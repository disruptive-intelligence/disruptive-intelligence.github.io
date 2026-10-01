---
title: Chapitre 17 — Presse, adverse media et SOCMINT financier
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Maîtriser l’**OSINT non-structuré** appliqué à la finance : presse économique, presse d’investigation, adverse media en bases agrégées, et **SOCMINT financier** (signaux issus des réseaux sociaux et de la présence en ligne des dirigeants et entités).

## Le concept

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

## L’utilité opérationnelle

Trois usages majeurs dans une enquête FININT :

1. **Adverse media** : qualification du risque réputationnel d’une personne ou d’une entité — affaires antérieures, associations problématiques, mises en cause publiques.
1. **Profilage humain** (SOCMINT) : qui est cette personne au-delà de sa fiche registre — formation, parcours, réseau, train de vie, signaux de cohérence ou d’incohérence.
1. **Recoupement OSINT général** : croisement avec d’autres sources (presse d’un côté, marchés publics de l’autre, leak d’une troisième) pour bâtir un faisceau d’éléments solide.

## Méthode — workflow presse + SOCMINT

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

## Mini-walkthrough — adverse media sur Karim Haddad

- Factiva (sources françaises et internationales) : 14 articles depuis 2018. Mention dans une transaction fiscale française (2018, sans poursuite pénale), présence dans un dossier d’export contesté en 2021 (article Le Monde), contributions à une fondation philanthropique libanaise (presse libanaise, 2022-2023).
- Mediapart : un article de 2023 sur des allégations de favoritisme pour des marchés en Côte d’Ivoire (sans nommer Haddad explicitement, mais avec des détails recoupés par OSINT).
- OCCRP : pas d’article direct, mais mention d’une société liée dans un dossier régional.
- LinkedIn : profil officiel Haddad, parcours déclaré 1995-aujourd’hui dans le négoce, actuellement « Chairman » de plusieurs entités. Cohérence avec l’image publique.
- Instagram : présence modérée, voyages réguliers (Beyrouth, Dubaï, Genève, Paris), événements professionnels visibles.
- Recoupement : profil global cohérent avec un homme d’affaires international actif. Aucune affaire judiciaire majeure publiquement connue. Adverse media présent mais à distance des qualifications fortes (présomption d’innocence pour les volets en cours).

## Mini-walkthrough — SOCMINT sur Monsieur X (gérant SAS françaises)

- LinkedIn : profil minimal, mention d’une « activité de conseil aux entreprises ». Pas d’expérience préalable affichée en cohérence avec la gestion de 8 SAS commerciales actives.
- Recherche image : photo de profil utilisée également sur un site de cabinet de domiciliation (corrélation forte).
- Conclusion : profil compatible avec un **professionnel multi-mandats** au service d’un cabinet de domiciliation. Pas une preuve, mais un facteur ajouté à l’hypothèse de prête-nom (chapitre 25).

## Erreurs fréquentes

- **Considérer la presse comme preuve.** La presse est une source d’information ; certains articles peuvent être imprécis, partiels ou orientés.
- **Surinterpréter un voyage.** Les voyages sur Instagram peuvent être un facteur d’analyse mais pas une qualification.
- **Ne pas archiver.** Les profils LinkedIn et les réseaux personnels changent — capture horodatée systématique.
- **Croiser des homonymes** (chapitre 19) : un Monsieur X présent sur LinkedIn n’est pas nécessairement le Monsieur X gestionnaire de la SAS. Vérifier date de naissance, parcours, photo.
- **Risquer le phishing OSINT** : créer un faux profil pour entrer en contact avec la cible viole les règles déontologiques et peut violer le droit (en France, manœuvres frauduleuses pour obtenir des données).

## Limites

La presse couvre principalement les acteurs visibles (grandes affaires, personnages publics). Les acteurs « moyens » d’un dossier complexe ne sont souvent pas couverts. Le SOCMINT est limité aux personnes qui ont une présence en ligne ; un homme d’affaires de l’ancienne génération ou opérant dans une culture peu numérique peut être quasi-invisible.

Le RGPD limite, en pratique, certaines exploitations en France et en UE — la donnée doit être collectée pour une finalité légitime, et le traitement doit être conforme. En CRF, le cadre légal autorise un traitement étendu ; en cabinet privé, les limites sont plus strictes (chapitre 68).

## Lien avec le fil rouge

> **CLEARFLOW — Le SOCMINT élargit le réseau**
> 
> Sur LinkedIn, Nassim identifie 5 collaborateurs proches déclarés de Haddad (employés ou anciens employés des sociétés du réseau). Sur Instagram, plusieurs photos de Haddad lors d’événements caritatifs au Liban montrent des personnalités politiques et économiques régionales. Une photo prise en 2023 lors d’un dîner à Genève montre Haddad avec un ancien dirigeant d’une banque privée suisse — la même banque dans laquelle un compte personnel apparaît dans les DS. Ce recoupement, *quasi-certain* à la confirmation visuelle (recherche image inverse + métadonnées), nourrit l’hypothèse d’un canal financier privilégié. Ce n’est pas une preuve, mais un faisceau qui oriente la coopération suisse.

## Points clés à retenir

- Presse économique + presse d’investigation + bases d’agrégation = adverse media solide.
- SOCMINT financier : LinkedIn pour le pro, réseaux perso pour le train de vie et le réseau humain.
- Croiser systématiquement plusieurs sources avant qualification.
- Présomption d’innocence et cadre RGPD à respecter.
- Toujours archiver — les profils en ligne changent vite.

-----
