---
title: Chapitre 4 — Donnée, information, indice, fait, preuve, hypothèse, renseignement
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE I — Doctrine, cadre et posture
  - index.md
---

## 4.1 Pourquoi ce chapitre est central

C'est le **chapitre pivot** du cours. La distinction rigoureuse entre donnée brute, information contextualisée, indice, faisceau d'indices, hypothèse, fait établi, preuve, et renseignement actionnable est ce qui sépare un analyste professionnel d'un curieux. Confondre ces niveaux est l'erreur la plus fréquente — et la plus coûteuse — de l'analyste débutant.

Un investigateur qui présente une hypothèse comme un fait commet une faute professionnelle. Un investigateur qui prend un indice unique pour une preuve produit du bruit. Un investigateur qui présente une donnée brute non contextualisée comme du renseignement actionnable trompe son commanditaire. Maîtriser ces distinctions est la condition de la crédibilité du métier.

## 4.2 Donnée brute

Une **donnée brute** est un élément informationnel non contextualisé, isolé, sans qualification ni interprétation.

**Exemples.**

- `192.168.1.42` est une adresse IP. C'est une donnée brute.
- `m.delaunay@technovert.fr` est une adresse email. C'est une donnée brute.
- Une photographie de profil sur LinkedIn. C'est une donnée brute.
- Un timestamp `2025-09-12T14:32:00Z`. C'est une donnée brute.

Une donnée brute en elle-même **ne dit rien**. Elle n'a pas de valeur opérationnelle sans contextualisation. Le travail de l'analyste commence quand la donnée brute devient information.

## 4.3 Information

Une **information** est une donnée brute **contextualisée** : on sait d'où elle vient, à quoi elle se rapporte, dans quel contexte elle a été produite.

**Exemples.**

- « L'adresse email `m.delaunay@technovert.fr` figure dans le pied de page d'un communiqué de presse TechnoVert du 12 mars 2024, attribuée à Marc Delaunay, DAF. » C'est une information.
- « La photographie X publiée sur le profil LinkedIn de Marc Delaunay le 8 janvier 2025 montre une silhouette en costume sombre devant un fond uni. » C'est une information.
- « Le timestamp 2025-09-12T14:32:00Z apparaît dans les métadonnées EXIF d'une photo téléversée sur Facebook par le compte M.Delaunay. » C'est une information.

Une information **dit quelque chose** mais ne suffit pas à conclure. Elle peut être vraie, fausse, partielle, manipulée. Elle attend d'être qualifiée.

## 4.4 Indice

Un **indice** est une information qui **oriente une hypothèse**.

**Exemples.**

- « L'email `m.delaunay@technovert.fr` apparaît également dans le WHOIS du domaine `delta-consulting.eu`. » C'est un indice : il oriente l'hypothèse que Delaunay est lié à Delta Consulting.
- « La photographie de profil LinkedIn de Marc Delaunay a un score Hive Moderation de 78 % "likely AI-generated". » C'est un indice : il oriente l'hypothèse que la photo est synthétique.

Un indice **n'établit pas un fait**. Il oriente, il suggère, il appelle vérification. Un indice isolé ne suffit pas. Un faisceau d'indices convergents peut établir un fait.

## 4.5 Faisceau d'indices

Un **faisceau d'indices** est un ensemble d'indices convergents pointant vers la même conclusion.

**Exemple.**

- Indice 1 : email `m.delaunay@technovert.fr` dans WHOIS de `delta-consulting.eu`.
- Indice 2 : Marc Delaunay enregistré comme director unique de Delta Consulting Ltd auprès du Companies Registry maltais.
- Indice 3 : adresse de domiciliation Delta Consulting partagée avec 46 autres entités identifiées par un même registered agent.
- Indice 4 : flux entrant de TechnoVert SAS vers Delta Consulting documenté dans une fuite de comptes maltais (Cyprus Confidential).

Le faisceau **converge** vers la conclusion : Delaunay contrôle Delta Consulting et a organisé des flux entre TechnoVert et cette société. Aucun indice isolé ne le prouverait. Ensemble, ils établissent un fait avec un niveau de confiance élevé.

## 4.6 Fait établi

Un **fait** est un élément établi par au moins deux sources indépendantes, cotées, et corroborantes.

**Critères.**

- Deux sources minimum.
- Sources **indépendantes** (un article qui en cite un autre n'est pas une seconde source — c'est la même source recyclée).
- Sources **cotées** (fiabilité connue, traçabilité documentée).
- **Corroboration** : les sources disent la même chose sur le même objet.

**Exemple.**

- Fait : « Delaunay est administrateur de Delta Consulting Ltd à Malte. »
- Sources : Companies Registry maltais (A1) + acte notarié reproduit dans Cyprus Confidential (B2).
- Conclusion : fait établi avec niveau de confiance élevé.

Un fait est **opposable**. Il peut être versé dans un rapport, défendu en audition, contre-expertisé. Il porte sa cotation.

## 4.7 Hypothèse

Une **hypothèse** est une explication candidate des faits.

**Exemples (hypothèses concurrentes sur Delaunay).**

- H1 : Delaunay détourne sciemment des fonds de TechnoVert vers Delta Consulting pour son enrichissement personnel.
- H2 : Delaunay opère une optimisation fiscale agressive mais légale, pour compte de TechnoVert.
- H3 : Delaunay est administrateur nominee, contrôlé par un tiers, et n'a pas de bénéfice direct.

Une hypothèse n'est ni vraie ni fausse a priori. Elle est **testée** contre les faits (méthode ACH — Ch.79). La meilleure hypothèse n'est pas celle qui confirme nos préjugés, c'est celle qui résiste à la réfutation.

## 4.8 Preuve

Une **preuve** est un fait qui établit la véracité d'une hypothèse au-delà du raisonnable.

L'OSINT produit **rarement des preuves au sens judiciaire**. Elle produit du renseignement coté qui oriente l'enquête judiciaire ou la décision opérationnelle. La preuve, au sens pénal, suppose une procédure (perquisition, audition, expertise judiciaire) que l'analyste OSINT ne maîtrise pas.

Cette limite est centrale. L'analyste OSINT qui présente ses conclusions comme des « preuves » trompe son commanditaire et expose le dossier. La formulation correcte est : « éléments compatibles avec », « faisceau d'indices convergents vers », « niveau de confiance élevé que… » — pas « preuve de ».

## 4.9 Renseignement actionnable

Le **renseignement** est un fait ou un ensemble de faits contextualisés, analysés, cotés, et présentés avec un niveau de confiance explicite à un commanditaire en vue d'une **décision**.

**Caractéristiques.**

- **Pertinent** par rapport à la question du commanditaire.
- **Coté** (fiabilité, niveau de confiance).
- **Tracé** (sources documentées).
- **Honnête** sur ses limites.
- **Actionnable** : il oriente une décision.

C'est le **livrable final** du métier. Un renseignement de qualité peut tenir en une page (note flash) ou s'étendre sur 80 pages (rapport complet) — l'important est qu'il respecte les critères ci-dessus.

## 4.10 Risque de surinterprétation

L'erreur classique : passer trop vite d'un indice à un fait, d'un fait à une preuve, d'une preuve à un verdict. Cette surinterprétation est le piège constant.

**Réflexes pour s'en protéger.**

- Demander systématiquement : ai-je le niveau d'évidence suffisant pour cette affirmation ?
- Formuler en niveau intermédiaire si nécessaire : « plusieurs éléments suggèrent que… », plutôt que « il est établi que… ».
- Appliquer l'ACH (Ch.79) : ai-je testé les hypothèses alternatives ?
- Cotation systématique (Ch.84) : chaque fait porte sa fiabilité.
- Revue par pair : un confrère relit avec un œil frais.
- Délai de réflexion : laisser dormir le rapport 24-48h avant de l'envoyer.

## 4.11 Synthèse opérationnelle

| Niveau | Caractéristique | Exemple |
|---|---|---|
| Donnée brute | Élément isolé non contextualisé | `m.delaunay@technovert.fr` |
| Information | Donnée contextualisée | Email cité dans communiqué TechnoVert |
| Indice | Information orientant une hypothèse | Email apparaît aussi dans WHOIS Delta Consulting |
| Faisceau d'indices | Plusieurs indices convergents | Email + registre + nominee + fuite |
| Fait | Établi par 2+ sources indépendantes cotées | Delaunay administrateur Delta (A1+B2) |
| Hypothèse | Explication candidate testable | Delaunay détourne des fonds |
| Preuve | Fait établissant véracité d'hypothèse | Rare en OSINT pur |
| Renseignement | Faits analysés, cotés, livrés pour décision | Rapport complet ou note flash |

> **Principe directeur.** Quand vous écrivez un rapport, demandez-vous pour chaque affirmation : à quel niveau suis-je ? Suis-je au niveau d'évidence requis pour ce que j'affirme ? Si non, reformulez en niveau inférieur. La discipline du niveau est la première protection contre la surinterprétation.

-----
