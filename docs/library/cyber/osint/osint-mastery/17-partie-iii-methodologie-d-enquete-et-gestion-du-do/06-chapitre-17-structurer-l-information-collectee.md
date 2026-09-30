---
title: Chapitre 17 — Structurer l'information collectée
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 17.1 Pourquoi structurer

Une enquête OSINT génère vite **trop d'informations**. Pour une enquête comme MIRAGE, à mi-parcours, l'analyste accumule typiquement plusieurs centaines de captures, deux à trois cents entités identifiées (personnes, sociétés, domaines, comptes, lieux), des dizaines d'événements datés.

Sans structuration, cette masse devient inutilisable. La structuration transforme la collecte en matériau analysable.

## 17.2 Les six structures principales

Six structures complémentaires organisent le dossier.

**1. Fiches entités.** Une fiche par entité d'intérêt (personne, société, compte, domaine, lieu, contenu, wallet, source). Champs standardisés. Mises à jour au fil de la collecte.

**2. Tableau de sélecteurs.** Liste maître des sélecteurs identifiés, avec leur entité associée, leur source de découverte, leur statut (vérifié, à confirmer).

**3. Timeline.** Ligne temporelle des événements datés. Permet d'identifier incohérences, séquences causales, simultanéités suspectes.

**4. Graphe relationnel.** Représentation visuelle des liens entre entités. Met en évidence les clusters, les pivots, les nœuds critiques.

**5. Matrice source / information.** Tableau qui croise les informations clés avec leurs sources. Permet d'identifier les faits corroborés (plusieurs sources) versus les pistes uniques.

**6. Matrice hypothèses / éléments.** Tableau qui croise les hypothèses concurrentes (ACH — Ch.79) avec les éléments collectés (pour / contre). Cœur de l'analyse.

## 17.3 Fiche entité : structure type

**Fiche personne physique.**

```
ENTITÉ : Marc Delaunay
Type : Personne physique
Statut : Cible principale

== Identité ==
Nom complet : Marc Henri Delaunay
Date de naissance : 17 octobre 1976 (présumé, à confirmer)
Lieu de naissance : Nantes (à confirmer)
Nationalité : Française (présumée)
Résidence : Paris 16e (présumée)

== Profession ==
Poste actuel : DAF, TechnoVert SAS (depuis 2019)
Parcours :
- 2015-2019 : Directeur financier, Solucia Industries
- 2010-2015 : Senior Manager, KPMG
- 2002-2010 : Auditeur senior, Deloitte
- 1999-2002 : Junior associate, BDO
Formation : X-Ponts, promo 1999

== Identifiants numériques ==
Email pro : m.delaunay@technovert.fr [confirmé, A1]
Email perso suspecté : marc.delaunay76@gmail.com [hypothèse, à confirmer]
LinkedIn : /in/marc-delaunay-08394 [confirmé, A1]
Twitter : @mdelaunay76 [hypothèse forte, B2]
Instagram : mdelaunay76 [hypothèse forte, B2]

== Liens entités ==
- Société TechnoVert SAS [employeur]
- Société Delta Consulting Ltd (Malte) [administrateur déclaré]
- Société Verde Holdings (Chypre) [à confirmer]
- SCI La Provence Familiale [administrateur via épouse]

== Indicateurs financiers visibles ==
- Salaire estimé TechnoVert : 180-250 k€/an
- Patrimoine SCI : ~1.8 M€
- Villa Marrakech : valeur estimée 800 k€

== Cotations préliminaires ==
Source A : confirmé (TechnoVert communiqués)
Source B : très probable (recoupements)
Source C : possible (à approfondir)

== Notes ==
- Aucune présence Telegram/Signal détectable via sélecteurs connus
- Possible username perso "mdelaunay76" récurrent
- Cluster Delta-Verde à creuser

== Historique de mise à jour ==
2026-05-19 : création
2026-05-22 : ajout LinkedIn et parcours
2026-05-25 : hypothèse Delta Consulting confirmée
```


**Fiche société.** Structure similaire adaptée : raison sociale, juridiction, numéro, capital, administrateurs, UBO, activité, siège, dates.

**Fiche compte social.** Plateforme, handle, date de création, photo, bio, abonnés, abonnements, activité type, signaux d'authenticité.

**Fiche domaine.** Domaine, registrar, WHOIS, DNS, certificats, hébergement, technologies, contenu, dates.

**Fiche image / contenu.** URL, source, hash, métadonnées, analyses (recherche inversée, ELA, détection IA), liens vers autres entités.

**Fiche wallet.** Adresse, blockchain, premier txn, dernière activité, clusters identifiés *(détail dans OSINT Crypto vFULL)*.

**Fiche source.** Domaine ou plateforme, type (presse, registre, blog, réseau social), cotation Admiralty, fiabilité historique.

## 17.4 Tableau de sélecteurs

Tableau maître à maintenir en continu.

| Sélecteur | Type | Valeur | Entité | Source découverte | Date | Statut |
|---|---|---|---|---|---|---|
| Email | Pro | m.delaunay@technovert.fr | Delaunay | TechnoVert site web | 2026-05-19 | Confirmé |
| Email | Perso suspecté | marc.delaunay76@gmail.com | Delaunay | Pivot username | 2026-05-22 | Hypothèse |
| Username | mdelaunay76 | mdelaunay76 | Delaunay | Sherlock | 2026-05-22 | Confirmé multi-plateformes |
| Téléphone | Pro | +33 1 XX XX XX XX | Delaunay | TechnoVert standard | 2026-05-20 | Confirmé |
| Domaine | Suspect | verites-technovert.com | Désinfo | Pivot recherche | 2026-05-28 | Confirmé hostile |
| Domaine | Suspect | info-finance-eu.com | Désinfo | Pivot blog | 2026-05-29 | Confirmé hostile |
| Société | Cible | Delta Consulting Ltd | Offshore | Companies Registry Malte | 2026-05-25 | Confirmé |
| (...) | (...) | (...) | (...) | (...) | (...) | (...) |

## 17.5 Timeline

La timeline est **chronologique**. Elle peut être tenue en :

- Tableau (date / événement / source / cotation).
- Outil dédié : **Timeline Explorer** (gratuit Eric Zimmerman), **Aeon Timeline** (payant, puissant), **Timegraphics**.
- Graphe temporel (avec Maltego, Linkurious).

**Exemple MIRAGE — timeline partielle.**

| Date | Événement | Source | Cot. |
|---|---|---|---|
| 2002 | Diplôme X-Ponts | LinkedIn | A1 |
| 2019-06 | Embauche TechnoVert comme DAF | Communiqué TechnoVert | A1 |
| 2020-03 | Création Delta Consulting Ltd (Malte) | Companies Registry MT | A1 |
| 2021-09 | Premier contrat consulting TechnoVert→Delta | BODACC indirect | C3 |
| 2022-01 | Création Verde Holdings (Chypre) | Companies Registry CY | A1 |
| 2025-04 | Audit interne TechnoVert signal écritures | Antoine Berthier interview | B2 |
| 2025-09-15 | Licenciement Antoine Berthier | Source RH (presse) | B2 |
| 2025-10 | Création domaine verites-technovert.com | WHOIS historique | A1 |
| 2025-11 | Premier post diffamatoire blog | Capture wayback | A2 |
| 2026-01 | Cluster X de 8 comptes amplifie | Archive.today | A2 |
| 2026-03 | Apparition vidéo deepfake Berthier | YouTube (supprimé) + cache | B2 |
| 2026-05-16 | Mandat Legrand & Associés | Mandat | A1 |
| (...) | (...) | (...) | (...) |

Les **incohérences chronologiques** sont l'un des révélateurs les plus puissants. Une publication antérieure à un événement qu'elle décrit. Un poste pris avant la fondation de la société. Une activité supposée pendant des congés documentés ailleurs.

## 17.6 Graphe relationnel

Le graphe représente visuellement les **entités** (nœuds) et les **relations** (arêtes).

**Outils.**

- **Maltego** : standard professionnel. Version Community gratuite limitée, version commerciale puissante.
- **Gephi** : open source, puissant pour analyses statistiques de réseau.
- **Neo4j** + interface (Bloom) : pour analystes techniques, base graph robuste.
- **draw.io / yEd / Lucidchart** : pour graphes manuels, simples.
- **Maltego Casefile** : version offline, pas de transforms automatiques mais OK pour usage souverain.

**Niveaux de graphe.**

**Graphe simple.** Personne → liens directs (sociétés contrôlées, sociétés employeuses, comptes sociaux).

**Graphe relationnel structuré.** Avec types d'arêtes (employer, owner, friend, register, hosting, etc.), métadonnées sur les arêtes (date, source, force du lien).

**Graphe d'enquête complet.** Plusieurs centaines de nœuds. Clusters identifiables. Algorithmes de détection de communautés (Louvain, modularité). Nœuds centraux (degree centrality, betweenness centrality).

## 17.7 Matrice source / information

Tableau qui croise une **liste de faits** avec une **liste de sources**, pour identifier les corroborations.

**Exemple simplifié.**

| Fait | Source A (TechnoVert) | Source B (LinkedIn) | Source C (Pappers) | Source D (ICIJ) |
|---|---|---|---|---|
| Delaunay DAF TechnoVert | ✓ | ✓ | ✓ |   |
| Delaunay admin Delta Consulting |   |   |   | ✓ |
| Delta Consulting adresse Malte |   |   |   | ✓ |
| Capital Delta Consulting 1200 € |   |   |   | ✓ |

Une ligne avec une seule croix = piste à corroborer. Une ligne avec plusieurs croix = fait établi à coter.

## 17.8 Matrice hypothèses / éléments (ACH)

Cœur de la méthode ACH (Ch.79). Tableau qui croise **hypothèses concurrentes** (colonnes) avec **éléments collectés** (lignes), en notant pour chaque élément s'il est **compatible** (C), **incompatible** (I), ou **neutre** (N) avec chaque hypothèse.

**Exemple sur MIRAGE IR1 (Delaunay détient-il des sociétés offshore non déclarées ?).**

| Élément | H1 : Detient personnellement | H2 : Nominee contrôlé par tiers | H3 : Aucun lien |
|---|---|---|---|
| Admin déclaré Delta Consulting | C | C | I |
| Email pro dans WHOIS verites-technovert.com | C | I | I |
| Pas de mention Delta dans déclaration fiscale FR | C (non-déclaration) | C (s'il est nominee, peut ne pas déclarer) | C (rien à déclarer) |
| Flux TechnoVert → Delta Consulting | C | C | I |
| Délivrance pouvoir signature Verde Holdings | C | C | I |

L'hypothèse **la moins infirmée** est retenue. H3 (« aucun lien ») est multiplement incompatible → réfutée. H1 et H2 restent ouvertes. La distinction H1 vs H2 demande approfondissement (Delaunay est-il bénéficiaire effectif réel, ou intermédiaire ?).

## 17.9 Vault Obsidian comme intégrateur

**Obsidian** est l'outil le plus populaire en 2026 pour intégrer ces six structures dans un vault unique.

**Architecture type d'un vault d'enquête.**

```
/MIRAGE/
├── 00_Cadrage/
│   ├── SOR_signé.md
│   └── Plan_de_collecte.md
├── 01_Journal/
│   ├── 2026-05-19.md
│   ├── 2026-05-20.md
│   └── (...)
├── 02_Entités/
│   ├── Personnes/
│   │   ├── Marc_Delaunay.md
│   │   ├── Antoine_Berthier.md
│   │   └── (...)
│   ├── Sociétés/
│   │   ├── TechnoVert_SAS.md
│   │   ├── Delta_Consulting_Ltd.md
│   │   └── (...)
│   ├── Domaines/
│   ├── Comptes/
│   ├── Contenus/
│   └── Wallets/
├── 03_Sélecteurs/
│   └── Table_sélecteurs.md
├── 04_Timeline/
│   └── Timeline_globale.md
├── 05_Graphes/
│   └── (exports Maltego)
├── 06_Analyse/
│   ├── ACH_IR1_offshores.md
│   ├── ACH_IR4_désinfo.md
│   └── (...)
├── 07_Captures/
│   └── (captures Hunchly, hashes.txt)
├── 08_Rapports/
│   ├── Note_etape_J15.md
│   ├── Rapport_final.md
│   └── (...)
└── 09_Sources/
    └── Bibliographie.md
```


Les liens internes Obsidian (`[[Marc_Delaunay]]`) créent automatiquement un graphe que vous pouvez visualiser avec le plugin Graph View. Les tags (`#hypothèse-IR1`, `#cotation-A1`) permettent les filtres rapides.

## 17.10 Discipline de structuration

La structuration n'est pas un luxe **après** la collecte — c'est **pendant** la collecte. Chaque entité découverte est ajoutée à sa fiche dans la journée. Chaque pivot est tracé. Chaque hypothèse est testée. La structuration **en continu** prévient le mur des dernières 48h où l'analyste se noie dans 400 captures non triées.

-----
