---
title: Partie III — Protection du patrimoine
source: Cyber/01_CTI/IE.md
note: Intelligence économique
up:
- - Intelligence économique
  - index.md
---

*Identifier ce qui a de la valeur, comprendre les menaces, et construire le dispositif de protection — le pilier défensif de l'IE.*

---


## Chapitre 10 — Identifier et cartographier le patrimoine informationnel

Le patrimoine informationnel est l'ensemble des informations et des savoirs qui ont une valeur économique pour l'organisation. La première étape de la protection est de savoir ce qu'on protège.

Le **patrimoine immatériel** : brevets, savoir-faire non breveté (procédés, recettes, méthodes), données R&D (résultats d'essais, prototypes, formulations), bases de données commerciales (clients, prix, conditions), logiciels et algorithmes propriétaires, et stratégie de l'entreprise (plans de développement, projets d'acquisition, positionnement prix). Le **patrimoine humain** : les personnes clés dont le départ serait irréparable — les identifier (qui détient un savoir-faire critique, unique, et non documenté ?), les fidéliser (rémunération, intérêt du poste, perspectives), et les protéger (sensibilisation aux approches, clauses contractuelles). Le **patrimoine relationnel** : les partenariats stratégiques, les contacts institutionnels (DGA, SISSE, ministères), les réseaux d'influence (think tanks, comités de normalisation).

La méthode de cartographie : inventaire systématique par département, classification par criticité (vital — perte existentielle / important — perte significative / courant — perte gérable), identification des détenteurs (qui détient quoi, sous quelle forme, dans quel système), et évaluation de l'exposition (qui, en interne ou en externe, y a accès — et cet accès est-il nécessaire ?). L'output est la **carte du patrimoine** — le document de référence qui guide toute la politique de protection.

---


## Chapitre 11 — Menaces et modes opératoires de captation

Les modes opératoires de captation du patrimoine — les comprendre pour les détecter et s'en protéger.

L'**espionnage industriel** : intrusion cyber (APT ciblant les données R&D — renvoi vers les cours CTI et APT ; l'APT40 chinois a ciblé systématiquement l'aérospatiale européenne), espionnage humain (approche d'employés clés par des services de renseignement — programme Mille Talents, « collaborations académiques » instrumentalisées, stagiaires positionnés, « visiteurs » intéressés), et espionnage physique (écoute de réunions, vol de documents, photos d'installations, intrusion dans les locaux).

Le **débauchage ciblé** : recrutement coordonné d'experts clés par un concurrent ou un État. Le débauchage n'est pas illégal en soi (la liberté du travail est un principe fondamental), mais le débauchage systématique visant à capturer un savoir-faire peut être qualifié de concurrence déloyale ou de violation du secret des affaires.

La **captation via les partenariats** : JV qui donne accès au savoir-faire (le partenaire apprend puis reproduit), co-développement qui transfère la PI (les résultats sont partagés, mais l'un des partenaires les exploite plus agressivement), prestataire qui copie (le sous-traitant réutilise le savoir-faire pour un concurrent), et acquisition suivie de transfert technologique (racheter l'entreprise pour accéder à sa technologie).

Le **lawfare** (utilisation du droit comme arme — détaillé au Ch.22). La **guerre informationnelle** (déstabilisation réputationnelle ciblée — détaillée au Ch.21). Et l'**OPA hostile** comme mode de captation (acheter l'entreprise pour contrôler sa technologie — investisseurs étrangers, fonds souverains, fonds écrans).

---


## Chapitre 12 — Construire le dispositif de protection

La **PPI** (Politique de Protection du Patrimoine Informationnel) est le document cadre qui organise la protection. Elle couvre la sécurité de l'information (classification — 3 niveaux : C1 public, C2 interne, C3 confidentiel/stratégique ; marquage visible sur chaque document ; contrôle d'accès — besoin d'en connaître ; DLP — Data Loss Prevention sur les flux email et cloud ; chiffrement des données sensibles ; politique d'impression et de destruction sécurisée), la sécurité des personnes (sensibilisation IE — formations obligatoires pour les profils exposés ; clauses de confidentialité renforcées dans les contrats de travail ; non-concurrence encadrée — durée, périmètre, indemnité ; gestion des départs — entretien structuré, rappel des obligations, révocation des accès, période de restriction ; gestion des arrivées — vérification des antécédents, sensibilisation IE dès l'intégration), la sécurité des déplacements (équipements dédiés — PC vierge, téléphone jetable, pas de données sensibles ; brief avant départ — que dire, ne pas dire, risques spécifiques du pays ; debrief retour — observations, approches, informations partagées ; règles — jamais de WiFi hôtel, jamais de clé USB offerte, matériel jamais sans surveillance, attention aux chambres d'hôtel), et la sécurité des partenariats (NDA avant toute discussion sensible, data room contrôlée avec traçabilité, compartimentation — ne donner accès qu'au nécessaire).

---


## Chapitre 13 — Protection juridique et propriété intellectuelle

Stratégie de brevet : le dilemme fondamental est **breveter** (protection de 20 ans, mais publication qui révèle le savoir-faire) ou **garder le secret** (protection indéfinie, mais vulnérable au reverse engineering et à l'espionnage). Où déposer : INPI (France), OEB (Europe), PCT (international — procédure unique avec désignation des pays cibles). Brevet défensif (empêcher les concurrents de copier) vs offensif (générer des revenus de licences, ou bloquer un concurrent qui empiète). La veille brevets comme outil de détection de captation (un concurrent qui dépose un brevet similaire au vôtre → alerte).

Le secret des affaires : conditions (valeur commerciale, mesures de protection, caractère secret), moyens de preuve (marquage, NDA, registre d'accès, enveloppe e-Soleau). Le contentieux PI (contrefaçon, concurrence déloyale, parasitisme — procédures longues et coûteuses, la prévention est toujours plus rentable).

---


## Chapitre 14 — Supply chain, dépendances stratégiques et souveraineté

La supply chain comme surface d'attaque IE : vecteur de captation (prestataire qui accède aux données), de dépendance stratégique (fournisseur unique dont la perte est critique), et de vulnérabilité juridique (clause léonine, droit applicable étranger qui donne accès aux données). La cartographie des dépendances (technologiques, données, compétences, matières premières, financement — pour chaque dimension : criticité de la dépendance, substituabilité, risque pays, risque juridique). Cloud et souveraineté des données (Cloud Act, FISA 702, Schrems II — les données sur AWS/Azure/Google sont accessibles aux autorités US ; solutions : SecNumCloud, chiffrement côté client, cloud souverain). Stratégies de réduction des dépendances (diversification, internalisation, stockage stratégique, souveraineté contractuelle, screening des investisseurs). Le rôle de l'État (screening IEF/SISSE, CFIUS, règlement UE — l'État peut bloquer une acquisition contraire aux intérêts stratégiques).

---
