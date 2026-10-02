---
title: Chapitre 21 — Formes juridiques comparées
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Connaître les **formes juridiques principales** rencontrées en FININT, leurs caractéristiques (responsabilité, transparence, capital, gouvernance), et leur signification dans une cartographie. La forme juridique d’une entité informe sur sa flexibilité, son opacité potentielle et ses obligations.

## Le concept

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

## L’utilité opérationnelle

Pour l’analyste :

- **La forme oriente sur la transparence attendue.** Une SAS française publie ses comptes (au-delà des seuils) ; une LLC Delaware ne publie rien. Un trust BVI n’est pas une entité juridique publique.
- **La forme oriente sur la gouvernance.** Une SA a un conseil d’administration ou directoire + conseil de surveillance ; une SAS peut être pilotée par un président unique.
- **La forme oriente sur les obligations LCB-FT.** Certaines formes sont des assujettis (notaires, avocats sous certaines conditions, agents immobiliers), d’autres non.
- **La forme oriente sur les schémas typiques.** SCI pour la détention immobilière. SOPARFI pour les holdings. LLC Delaware pour les structures opaques. Trust pour la séparation patrimoniale.

Une cartographie de réseau qui ne distingue pas les formes juridiques est lacunaire.

## Méthode — lecture d’une cartographie par forme

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

## Mini-walkthrough — formes du réseau Haddad

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

## Erreurs fréquentes

- **Considérer toutes les formes comme équivalentes.** Une LLC Delaware ≠ une SAS française ≠ un trust BVI. Les régimes et les transparences diffèrent radicalement.
- **Confondre forme et fonction.** Une « société de holding » peut être SARL, SA, SAS, SOPARFI, LLC, BV, etc. La forme dit la structure, pas la fonction.
- **Ignorer les particularités locales** : LP écossais, SCSp luxembourgeoise, fondation panaméenne — chacune a des spécificités à connaître pour comprendre la logique du montage.

## Limites

La connaissance fine des formes juridiques de toutes les juridictions du monde dépasse les capacités d’un analyste. L’objectif est de connaître les formes courantes et d’identifier les formes spécifiques quand elles apparaissent (recherche à la demande). Les juristes spécialisés sont consultés quand un montage particulier exige une analyse poussée.

## Lien avec le fil rouge

> **CLEARFLOW — Lecture juridique du réseau**
> 
> Nassim produit une fiche par entité avec sa forme juridique et ses implications. Cette annotation lui permet, en consolidation, d’expliquer dans la note finale : *« Le réseau s’appuie sur 4 SAS françaises (front opérationnel apparent), 2 Limited UK (présence visible mais activité réelle douteuse), 1 LLC Delaware (opacité), 1 SOPARFI luxembourgeoise (holding intermédiaire), 1 société chypriote contrôlée par un trust (structure de contrôle ultime probable). Le montage est typique d’une architecture multi-juridictionnelle combinant légitimité de façade et opacité de contrôle. »*

## Points clés à retenir

- Formes courantes UE : SAS, SARL, SA, GmbH, BV, Ltd, SOPARFI.
- Formes opaques notables : LLC Delaware, IBC BVI/Cayman, fondations Liechtenstein, trusts.
- La forme oriente la transparence, la gouvernance, les obligations.
- Un graphe de réseau bien annoté en formes informe immédiatement la stratégie d’investigation.

-----
