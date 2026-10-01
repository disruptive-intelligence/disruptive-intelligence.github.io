---
title: 'Chapitre 58 — Cas 4 : Contournement de sanctions via pays tiers'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IX — Cas pratiques déroulés
  - index.md
---

## Contexte

Une banque française, **BANQUE-X**, identifie via son monitoring un client commercial atypique : une SAS française récemment créée, **EUROFLUX SARL**, qui présente une explosion d’activité avec une contrepartie turque. Les flux sont importants (~3 M€ sur 2 mois) et la nature des opérations (négoce de matériel industriel sensible) attire l’attention.

La compliance déclenche une analyse FININT interne et sollicite TRACFIN via DS.

**Demande (interne CRF)** : qualifier le profil de risque, vérifier la possibilité d’un contournement de sanctions, recommander des suites.

## Indices initiaux

- EUROFLUX SARL : créée 5 mois avant les premiers flux. Capital 5 K€. Dirigeant : un Français, 30 ans, parcours professionnel principalement dans la logistique générale.
- Contrepartie turque : ATLAS TECHNICAL TRADING (société turque créée 7 mois plus tôt).
- Flux observés : 3 M€ entrants depuis ATLAS, libellés « industrial equipment » et « technical components ».
- Sorties : achats auprès de fournisseurs européens (Allemagne, Italie, Pays-Bas) de matériel électronique sensible (CNC, composants industriels avancés).
- Destinations finales déclarées : exports vers Turquie (déclarations douanières).

## Cadrage

**Questions de renseignement** :

- QR1 — Quel est le profil réel d’EUROFLUX et d’ATLAS ?
- QR2 — Les biens commercialisés sont-ils dual-use ?
- QR3 — Y a-t-il un soupçon de réexportation vers une juridiction sanctionnée ?
- QR4 — Quels UBO et liens entre EUROFLUX, ATLAS, et éventuelles entités sanctionnées ?

## Collecte

**OSINT** :

- Pappers : EUROFLUX dirigée par M. T, sans expérience visible dans le secteur. UBO RBE : M. T lui-même.
- Recherche M. T : LinkedIn minimal, pas de réseau apparent dans la tech industrielle.
- Adresse EUROFLUX : cabinet de domiciliation parisien, 21 autres entités.
- Recherche ATLAS Technical Trading (Turquie) : registre turc accessible — UBO turc, M. Ö, 45 ans, parcours dans le négoce général à Istanbul.
- Recherche presse : ATLAS est mentionnée dans un article OCCRP de 2024 sur des sociétés turques utilisées pour acheminement de biens vers la Russie (sanctions UE et US).

**Sanctions et listes** :

- M. Ö (UBO d’ATLAS) : pas sur les listes OFAC, UE, OFSI.
- ATLAS : pas sur les listes.
- Sociétés liées (recherche par M. Ö) : plusieurs sociétés dirigées par M. Ö, dont une avait des liens commerciaux antérieurs avec une entreprise russe **désormais sanctionnée** depuis 2022.

**Nature des biens** :

- Liste détaillée des achats EUROFLUX auprès des fournisseurs européens : composants CNC, contrôleurs PLC, certains équipements de capteurs.
- Vérification dual-use : plusieurs des composants sont sur la **liste UE dual-use** (règlement 2021/821), exigeant licence d’exportation pour certaines destinations.

**Vérification douanière** :

- Déclarations douanières françaises : exports vers Turquie déclarés.
- Pas de vérification immédiate de la destination réelle après Turquie.

## Analyse

**Profil EUROFLUX** : société créée récemment, dirigeant inexpérimenté, domiciliation, faible substance économique propre. *Probable* société écran ou opérationnelle pour un schéma spécifique.

**Profil ATLAS** : société turque créée récemment, mais avec un UBO qui a des liens antérieurs (sociétés liées) avec une entreprise russe désormais sanctionnée.

**Schéma probable** : EUROFLUX achète en Europe des biens dual-use, vend à ATLAS en Turquie. ATLAS réexporte (potentiellement) vers une destination sanctionnée (probablement Russie). Le schéma est typique d’un **contournement de sanctions UE/US** via pays tiers.

**Éléments confortants** :

- Nature des biens (dual-use).
- Lien historique UBO ATLAS / entité russe sanctionnée.
- Volume soudain (3 M€ en 2 mois pour une société de 5 K€ de capital).
- Pas d’activité économique antérieure d’EUROFLUX cohérente avec le secteur.

## Hypothèses calibrées

- **H1 — Contournement de sanctions UE/US via pays tiers (Turquie)** : probable.
- **H2 — Schéma de commerce parallèle légal mais douteux** : possible.
- **H3 — Pure activité commerciale Europe-Turquie** : peu probable au vu de la nature des biens et du profil ATLAS.

## Limites

- Sans vérification de la destination réelle après Turquie, le contournement reste *probable*, pas *quasi-certain*.
- Coopération douanière France-Turquie est complexe (Turquie n’est pas dans l’UE).
- Le volet renseignement avec services spécialisés (DG Trésor pôle sanctions, DGDDI, équivalent dans services de défense) est central.

## Livrable

Note FININT interne CRF + signalement :

- Profil de risque *probable* de contournement de sanctions, biens dual-use.
- Recommandations :
  - DS validée et enrichie, transmission au PNF (équivalent fiction).
  - Saisine immédiate de la DG Trésor (pôle sanctions financières) (Direction Générale du Trésor — sanctions) et des services douaniers (DGDDI).
  - Coopération Egmont avec la CRF turque pour qualifier ATLAS et son réseau.
  - Possibilité de gel administratif si éléments suffisants confirment l’attribution sanctionnée.

## Bilan honnête

Le contournement de sanctions est une typologie particulièrement sensible. La qualification définitive est souvent **politique** autant que judiciaire. Le rôle de la CRF est de produire un dossier solide et de saisir les autorités spécialisées. Les sanctions secondaires OFAC (impact sur les opérateurs européens) ajoutent une dimension géopolitique. Le dossier peut conduire à des suites variées : enquête judiciaire en France, sanctions sur les acteurs (gel), pression diplomatique sur la Turquie pour coopération.

## Leçons FININT

- **Pays tiers** (Turquie, Émirats, Géorgie, Arménie, Asie centrale) sont des canaux d’attention prioritaire depuis 2022.
- **Biens dual-use** : connaître la liste UE, qui est mise à jour régulièrement.
- **UBO et liens passés** : un UBO non sanctionné mais lié historiquement à une entité sanctionnée = signal majeur.
- **Coordination inter-services** : sanctions ≠ FININT seul. DG Trésor (pôle sanctions financières internationales), DGDDI, MAE, parfois services de défense interviennent.

-----
