---
title: Chapitre 26 — Identification de personne physique
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 26.1 Identifier : un acte plus complexe qu'il n'y paraît

**Identifier** une personne en OSINT ne se réduit pas à trouver son nom. C'est confirmer, avec un faisceau d'éléments convergents, que la personne dont on parle est bien **celle qu'on croit** et **personne d'autre**. Les homonymes, les usurpations, les coïncidences sont des pièges récurrents.

Une identification mature s'appuie sur **plusieurs dimensions** (nom + date de naissance + lieu + parcours + photo + sélecteurs uniques) jusqu'à atteindre un niveau de confiance proportionné à l'enjeu.

## 26.2 Désambiguïsation : le premier réflexe

**Avant** toute investigation approfondie sur une personne, vérifier qu'il n'y a pas confusion.

**Cas typique du piège.** Dans une enquête sur « Pierre Martin, DAF de société X », l'analyste trouve sur LinkedIn six profils nommés Pierre Martin. Investiguer le mauvais détruit l'enquête.

**Méthode.**

- Combiner nom + employeur actuel + secteur.
- Cross-vérifier date d'arrivée à l'employeur (presse, communiqué).
- Photo (LinkedIn, presse).
- Parcours antérieur (cohérence).

## 26.3 Sources de désambiguïsation principales

**Presse.** Communiqués de l'employeur, articles avec photo, mentions sectorielles.

**LinkedIn.** Profil professionnel, parcours, connections.

**Pappers / Companies House.** Dirigeants déclarés officiellement.

**Wikipédia / Wikidata.** Pour personnalités publiques. Wikidata fournit identifiants structurés.

**HATVP.** Pour PEP français (déclarations d'intérêt).

## 26.4 Sélecteurs identifiants

Un **sélecteur identifiant** est une information qui distingue **uniquement** une personne.

**Sélecteurs très forts.**

- Numéro SIREN comme dirigeant.
- Email professionnel confirmé.
- Numéro de téléphone.
- Identifiant officiel (CNI, passeport, fiscal) — rarement publics.

**Sélecteurs forts.**

- Username unique cross-plateformes.
- Photo identifiable.
- Date et lieu de naissance précis.
- Adresse résidentielle exclusive.

**Sélecteurs faibles.**

- Nom seul.
- Année de naissance seule.
- Profession générale (« DAF »).
- Ville seule.

## 26.5 Identité civile vs identité publique

**Identité civile.** Nom à l'état civil, adresse, date et lieu de naissance.

**Identité publique.** Ce que la personne expose sur les sources ouvertes.

Les deux ne coïncident pas toujours :

- Pseudonymes professionnels (artistes, journalistes).
- Changement de nom (mariage, naturalisation).
- Identités antérieures (ex-conjoint, naissance dans autre pays).

L'investigation doit parfois remonter à l'identité antérieure.

## 26.6 People search engines américains (limites RGPD)

**TruePeopleSearch, FastPeopleSearch, Whitepages, BeenVerified.** Bases de données américaines de people search.

**Capacités.**

- Adresses passées et actuelles.
- Numéros de téléphone connus.
- Membres de famille.
- Voisins.

**Limites RGPD.** Ces services traitent données personnelles. Leur usage par analyste en UE doit reposer sur base légale (intérêt légitime documenté), et reste juridiquement délicat.

**Pour cibles US.** Restent référence. Pour cibles UE, à utiliser avec parcimonie et documentation rigoureuse.

## 26.7 Outils français de people search

**Pages Jaunes, Annuaire.** Limités mais utiles pour adresses anciennes.

**Verif.com, Societe.com.** Croisement avec sociétés.

**Avis de naissance / mariage / décès.** Presse régionale (archives partiellement payantes).

**Geneanet, FamilySearch.** Généalogie. Utile pour cartographie familiale et héritages.

## 26.8 Cohérence des éléments

Une identification mature **fait converger** plusieurs dimensions.

**Convergence forte (identification quasi-certaine).**

- Nom + photo + employeur + parcours cohérent + date naissance + adresse.
- Sources multiples indépendantes confirmant.

**Convergence moyenne.**

- Nom + photo + parcours probable.
- Source unique ou faisceau partiel.

**Convergence faible.**

- Nom + ville.
- Suggère une piste, pas une identification.

## 26.9 Pièges classiques d'identification

**Homonymie.** Deux personnes du même nom dans le même secteur. Désambiguïsation par sélecteurs forts.

**Usurpation.** Un faux profil au nom de la cible. Cohérence interne du faux suffit parfois à tromper si on n'est pas vigilant.

**Vieillissement.** Photo récente vs photo d'archives. Détection des évolutions plausibles.

**Erreur d'attribution.** Confondre la personne réelle avec un mystificateur sur réseaux sociaux.

**Faux profils IA.** Photo générée par IA (Ch.30 et Ch.35).

## 26.10 Cotation finale d'identification

Pour chaque identification, **cotation Admiralty** explicite.

**A1.** Identification multi-corroborée par sources officielles + cohérence parcours + photos + multiples sélecteurs.

**B2.** Identification probable, faisceau d'indices convergents, mais source unique ou corroboration partielle.

**C3.** Identification possible, signaux convergents mais pas suffisamment.

**D4-F6.** Identification douteuse ou non évaluable. Ne pas conclure.

> **MIRAGE — Épisode 4 : Identification de personne**
>
> L'analyste vérifie l'identification de Marc Delaunay, DAF de TechnoVert SAS, sujet central du mandat.
>
> **Sources convergentes.**
> - **Pappers TechnoVert** : « Marc Delaunay, Directeur Administratif et Financier, nommé le 15 juin 2019 » (A1).
> - **Communiqué TechnoVert** du 12 juin 2019 : annonce de nomination, photo officielle (A1).
> - **LinkedIn Marc Delaunay** : profil correspondant, photo identique au communiqué, parcours cohérent (X-Ponts, audit Big 4, DAF industrie depuis 2014, DAF TechnoVert depuis juin 2019) (A1 pour parcours déclaré).
> - **Interview vidéo professionnelle 2023** (chaîne YouTube secteur) : voix, image, prénom et nom mentionnés (A1).
> - **Mentions presse économique régionale** : 4 articles entre 2020 et 2024 mentionnant « Marc Delaunay, DAF de TechnoVert » (B1).
>
> **Désambiguïsation.** Plusieurs profils LinkedIn portent ce nom. Le profil cible est isolé par : photo correspondant communiqué + parcours déclaré cohérent avec presse + employeur actuel.
>
> **Sélecteurs forts retenus.**
> - Email professionnel : marc.delaunay@technovert.fr (déduit format standard TechnoVert ; à confirmer via Hunter.io).
> - SIREN TechnoVert : Delaunay listé comme représentant.
> - Photo : capturée et hashée.
> - Année de naissance estimée : 1976 (déduit X-Ponts promo 2002, généralement 23-26 ans à la sortie).
>
> **Cotation identification globale.** A1. Identification multi-corroborée, plusieurs sources indépendantes, photo confirmée, parcours cohérent.
>
> **Sélecteurs disponibles pour pivots ultérieurs.**
> - Nom complet : Marc Delaunay.
> - Email pro : marc.delaunay@technovert.fr (à valider).
> - Email perso : à rechercher.
> - Téléphone perso : à rechercher.
> - Username cross-plateformes : à investiguer (pseudonymes possibles).
> - Adresse résidentielle : à rechercher.
> - Famille proche : à investiguer avec déontologie.
>
> Ces sélecteurs seront mobilisés au fil des épisodes suivants.

-----
