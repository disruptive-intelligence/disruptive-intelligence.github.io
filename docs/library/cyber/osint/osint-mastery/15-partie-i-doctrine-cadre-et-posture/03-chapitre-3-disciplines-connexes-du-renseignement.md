---
title: Chapitre 3 — Disciplines connexes du renseignement
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE I — Doctrine, cadre et posture
  - index.md
---

## 3.1 Pourquoi distinguer les INTs

L'OSINT s'inscrit dans un écosystème de disciplines de renseignement, chacune avec ses sources, ses méthodes et ses contraintes légales. Il est utile de les distinguer pour comprendre ce que l'OSINT couvre, ce qu'elle ne couvre pas, et comment elle s'articule avec les autres.

## 3.2 HUMINT — Human Intelligence

Renseignement issu de **sources humaines** : entretiens, informateurs, élicitation, infiltration.

**Cadre légal.** Légal s'il est transparent (un journaliste interviewant une source, un investigateur posant une question dans un cadre professionnel normal). Devient illégal si l'investigateur usurpe une identité, exerce une pression, ou manipule la source pour obtenir l'information.

**Articulation avec l'OSINT.** Le HUMINT n'est pas dans le périmètre de l'OSINT, mais certaines pratiques sont voisines : l'élicitation passive en ligne, l'observation de conversations publiques, l'interaction avec une source via un compte d'investigation déclaré. La frontière entre OSINT défensif et HUMINT actif est fine — quand l'investigateur interagit avec une source plutôt que de l'observer, il bascule en HUMINT et le cadre juridique change.

**Pour le privé.** Les enquêteurs privés agréés peuvent faire du HUMINT déclaré (entretiens, démarches). Les analystes OSINT non agréés doivent se limiter à l'observation et aux interactions transparentes.

## 3.3 SIGINT — Signal Intelligence

**Interception de communications électroniques** (radio, téléphone, mail, données).

**Cadre légal.** Strictement réservé aux services d'État autorisés. En France, encadré par la loi renseignement de 2015 et ses évolutions. Aucun investigateur privé ne peut faire du SIGINT légalement. L'interception non autorisée est lourdement sanctionnée pénalement.

**Articulation avec l'OSINT.** Aucun chevauchement légitime pour le privé. Pour les services d'État, le SIGINT est fusionné avec l'OSINT dans des architectures all-source.

## 3.4 IMINT — Image Intelligence

Renseignement par l'**imagerie**.

**Sous-types.**

- IMINT classifié : imagerie satellite haute résolution militaire (KH-11, Pléiades militaires). Réservé aux services.
- IMINT en sources ouvertes : imagerie satellite Sentinel (Copernicus européen), Google Earth, Maxar (commercial, partiellement public), Planet Labs, photos publiées en ligne. Accessible à l'OSINT.

**Articulation.** L'IMINT en sources ouvertes est une composante de l'OSINT (couverte en Partie VII). Les Bellingcat, GeoConfirmed et autres font massivement de l'IMINT-OSINT.

## 3.5 GEOINT — Geospatial Intelligence

Combine **imagerie, cartographie, et données géolocalisées** pour produire du renseignement spatial.

**Méthodes.** Géolocalisation (où ?), chronolocation (quand ?), analyse temporelle d'imagerie satellite, analyse de signature spatiale. La méthode Bellingcat est un GEOINT en sources ouvertes pur.

**Articulation.** L'un des sous-domaines les plus matures de l'OSINT contemporaine. Couvert en Partie VII (Ch.48-52). L'arrivée des agents IA spécialisés en géolocalisation (GeoSpy, GeoSeer) en 2025-2026 transforme la pratique.

## 3.6 SOCMINT — Social Media Intelligence

Renseignement issu des **réseaux sociaux**.

**Importance.** C'est aujourd'hui l'un des plus gros volumes de l'OSINT, à la fois parce que les personnes publient massivement leur vie en ligne et parce que les réseaux sociaux sont devenus des plateformes opérationnelles pour la criminalité (recrutement de mules, marché de fraude, coordination), l'extrémisme, l'influence et la fraude.

**Articulation.** Sous-domaine majeur de l'OSINT, couvert en Partie V (Ch.31-35). Souvent fusionné avec l'IMINT (photos publiées) et l'OSINT classique (pivots vers domaines, emails).

## 3.7 FININT — Financial Intelligence

**Renseignement financier**.

**Sous-types.**

- FININT institutionnel : déclarations de soupçon, accès aux flux bancaires, levée du secret bancaire. Réservé aux Cellules de Renseignement Financier (TRACFIN en France, FinCEN aux USA).
- FININT en sources ouvertes : registres d'entreprises, comptes publiés, listes de sanctions, Pandora Papers, presse financière. Accessible à l'OSINT.

**Articulation.** L'OSINT financier est couvert en vue maître dans le présent cours (Ch.70-71, 77). Pour la profondeur métier (UBO complexes, schémas de blanchiment, comptabilité forensique, AML/CFT), **renvoi vers FININT vFULL**.

## 3.8 DARKINT — Dark Web Intelligence

Renseignement issu du **dark web** — forums clandestins, marketplaces, leak sites.

**Cadre.** La consultation est légale (à condition de ne pas accéder à des contenus pénalement répréhensibles : CSAM, terrorisme). L'interaction est réservée à un cadre professionnel strict ou aux LEA. Aucun analyste OSINT privé ne devrait acheter sur une marketplace dark web.

**Articulation.** Vue opérationnelle dans le présent cours (Ch.44). Pour la profondeur (écosystèmes, IA criminelle, opérations LEA), **renvoi vers Dark Web vFULL**.

## 3.9 CYBINT — Cyber Intelligence (et CTI)

Renseignement sur les **menaces et acteurs cyber**.

**Articulation.** CTI (Cyber Threat Intelligence) est un sous-domaine professionnalisé. L'OSINT est l'une de ses sources majeures (forums, leak sites, infrastructure adverse). Couvert dans le présent cours en Ch.74-75. Pour la profondeur, **renvoi vers cours CTI dédié**.

## 3.10 MASINT, TECHINT, OSINT corporate

**MASINT** (Measurement and Signature Intelligence). Renseignement par signatures techniques (acoustique, radar, infrarouge). Très spécialisé, principalement militaire. Hors périmètre OSINT.

**TECHINT** (Technical Intelligence). Renseignement technique sur les capacités adverses (matériel, équipement, technologie). Une partie en sources ouvertes (manuels, brochures, salons, dépôts de brevets) est accessible à l'OSINT.

**OSINT corporate / Business Intelligence.** Sous-domaine de l'OSINT appliqué à la due diligence, l'intelligence économique, le M&A. Couvert dans le présent cours en Partie VI et Ch.77.

## 3.11 Récapitulatif et frontières

| Discipline | Source | Cadre légal privé | Couverture OSINT Mastery |
|---|---|---|---|
| **HUMINT** | Sources humaines | Limité (transparence) | Hors périmètre |
| **SIGINT** | Communications interceptées | Interdit | Hors périmètre |
| **IMINT** | Imagerie | Sources ouvertes seules | Partie VII |
| **GEOINT** | Géospatial | Sources ouvertes | Partie VII |
| **SOCMINT** | Réseaux sociaux | Conditionné | Partie V |
| **FININT** | Financier | Sources ouvertes seules | Ch.70-71, 77 + FININT vFULL |
| **DARKINT** | Dark web | Consultation OK, interaction limitée | Ch.44 + Dark Web vFULL |
| **CYBINT / CTI** | Cyber | Sources ouvertes + feeds | Ch.74-75 + CTI vFULL |
| **MASINT** | Signatures techniques | Inaccessible privé | Hors périmètre |

L'OSINT englobe ou recoupe l'IMINT en sources ouvertes, le GEOINT, le SOCMINT, la part ouverte du FININT, le DARKINT en consultation, le CYBINT en sources publiques. Une investigation OSINT typique combine plusieurs de ces sous-disciplines. Le cours les enseigne de manière intégrée.

-----
