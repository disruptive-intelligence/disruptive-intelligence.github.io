---
title: 'Chapitre 36 — Cas 1 : victime de pig butchering USDT Tron'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VII — Cas pratiques déroulés
  - index.md
---

**Profil de l’enquête** : enquête typique sur un cas individuel de pig butchering. Volume modeste (~200 000 USD), pattern reconnaissable, méthode standard.

## 36.1 Le contexte

Marie (nom d’emprunt), 52 ans, cadre supérieure dans une PME française, contacte un cabinet d’investigation après réalisation d’une fraude. Elle a été victime d’une opération de pig butchering sur 4 mois (octobre 2025 - février 2026).

**Récit factuel** (synthétisé à partir du briefing client) :

- Octobre 2025 : Marie est contactée sur Instagram par un certain « Daniel Wang », se présentant comme entrepreneur à Singapour. Approche amicale, pas de demande financière initiale.
- Novembre 2025 : la relation devient amicale-puis-sentimentale (à distance). Daniel partage des « histoires » de succès en investissement crypto.
- Décembre 2025 : Daniel introduit Marie à une « plateforme exclusive » d’investissement DeFi, gérée par un « ami fonds ». Premier dépôt suggéré : 3 000 USDT.
- Janvier 2026 : la plateforme montre des « gains » de 30% en deux semaines. Marie augmente : 15 000 USDT, puis 50 000 USDT.
- Février 2026 : Marie liquide une partie de son épargne et investit 130 000 USDT supplémentaires.
- Mi-février : Marie tente un retrait de 50 000 USDT. La plateforme demande une « caution fiscale » de 20 000 USDT pour débloquer. Marie refuse et tente de contacter Daniel. Plus de réponse. Plateforme inaccessible.

**Total perdu** : ~198 000 USDT (~ 198 000 EUR au cours du moment).

Marie a porté plainte (gendarmerie locale + signalement Pharos + cybermalveillance.gouv.fr). Elle mandate un cabinet privé pour cartographier les flux et préparer un dossier solide pour la procédure.

## 36.2 Le cadrage de la mission

**Objectifs** :

1. Confirmer les flux on-chain depuis Marie vers la plateforme frauduleuse.
1. Identifier l’écosystème : autres victimes probables, opérateurs derrière la plateforme, points de cashout.
1. Identifier les **angles d’action** des autorités (exchanges traversés, demandes de gel possibles).
1. Produire un **rapport actionnable** pour soutien à la procédure judiciaire.

**Limites** :

- Pas d’identification civile espérée (compounds Asie du Sud-Est probables).
- Récupération des fonds peu probable (déjà 2 mois après dernier paiement).
- Mission OSINT pure, pas d’engagement direct avec scammer.

**Budget** : 15 jours analyste senior, ~25 000 EUR.

**Cadre légal** : mission privée mandatée, RGPD respecté, livrables transmissibles à autorités.

## 36.3 Phase 1 — Collecte initiale

**Inputs fournis par Marie** :

- 18 transactions USDT-TRON (sur 4 mois).
- TXIDs de chacune.
- Captures de l’app de la plateforme frauduleuse (avec adresses de dépôt).
- Captures des conversations Instagram avec Daniel.
- Photos partagées par Daniel (à analyser pour reverse image search).

**Étape 1 — Vérification on-chain**.

L’analyste ouvre Tronscan et vérifie les 18 transactions. Toutes confirmées. Total : 198 200 USDT. Cohérent avec le récit Marie.

**Étape 2 — Adresses de réception**.

Marie a déposé sur **3 adresses différentes** (la plateforme rotait les adresses) :

- T1 : 7 dépôts cumulés ~45 000 USDT (octobre-novembre).
- T2 : 6 dépôts cumulés ~75 000 USDT (décembre-janvier).
- T3 : 5 dépôts cumulés ~78 000 USDT (janvier-février).

**Étape 3 — Constitution fiches initiales**.

Pour chaque adresse :

- Première transaction : voit Marie comme dépositaire principal mais aussi **autres adresses sources**.
- Solde actuel : 0 (consolidé).
- Pattern de réception : multi-source, montants variables.

**Insight initial** : ces adresses ont **chacune reçu de multiples sources** (~30-50 sources par adresse). Marie n’est pas la seule victime.

## 36.4 Phase 2 — Expansion vers le cluster

**Étape 1 — Identifier l’adresse hub**.

T1, T2, T3 ont consolidé leurs fonds vers une **adresse hub commune** : T-HUB. Cette adresse a reçu cumulativement ~3,2 M USDT (donc bien plus que Marie — l’opération a multiple branches).

**Étape 2 — Caractériser T-HUB**.

T-HUB :

- Active depuis ~6 mois.
- Reçoit de ~12 adresses de collecte (T1-T12 dans la fiche).
- Volume total entrée : ~3,2 M USDT.
- Volume sortie : ~3,1 M USDT (consolidation rapide).
- Pas de label public Tronscan.
- Label Chainalysis Reactor : **« High risk - probable scam »** (label propriétaire basé sur patterns).

**Étape 3 — Identifier les sources des autres adresses de collecte**.

Sur Tronscan, l’analyste liste les sources de T1-T12. Total : ~400 adresses sources distinctes. Probables **400 victimes** différentes de la même opération de pig butchering.

**Étape 4 — Suivi post-T-HUB**.

T-HUB envoie ses fonds vers :

- 30% : exchange non-KYC asiatique (label Chainalysis : « Asian exchange, KYC weak »).
- 25% : 4 adresses « hub-niveau-2 » (probable layering supplémentaire).
- 20% : DEX SunSwap (TRON DEX) pour swap USDT → TRX → puis re-swap.
- 15% : adresses inconnues sans label.
- 10% : Garantex (avant sanctions OFAC), sinon successeur identifié.

**Insight** : opération **structurée** avec consolidation, layering, et points de cashout multiples.

## 36.5 Phase 3 — Investigation off-chain

**Étape 1 — Reverse image search sur photos Daniel**.

Les photos partagées par Daniel sont passées à l’analyse. Résultat : **3 photos sont issues d’un compte Instagram d’un homme réel (entrepreneur singapourien légitime)**. Identité volée. Daniel n’existe pas — c’est un alias utilisant les photos d’un tiers innocent.

**Note importante** : l’identité réelle volée n’est **pas mise en cause**. Le rapport mentionne la victime collatérale (l’entrepreneur singapourien), avec recommandation que Marie / autorités le contactent pour signaler abus de son identité.

**Étape 2 — Recherche OSINT sur la « plateforme »**.

Le nom de la plateforme (« CryptoYield Pro » — fictif) est recherché :

- Site web (capture Wayback Machine) : créé 8 mois avant arnaque, design crédible imitant exchange légitime.
- Domaine : enregistré chez registrar opaque, propriétaire masqué.
- Adresses mentionnées sur le site (« contacts ») : adresse à Singapour qui correspond à un coworking commercial — pas de bureau réel.
- Multiple signalements sur Chainabuse, Reddit r/CryptoScams, autres forums anti-scam.
- Plateforme listée comme **scam** sur multiple sites de recensement.

**Étape 3 — Recoupement avec autres victimes**.

L’analyste contacte le forum r/CryptoScams où des victimes ont signalé la même plateforme. **6 autres victimes identifiées** publiquement avec adresses crypto perdues. Les adresses correspondent à T-HUB ou T1-T12. **Confirmation** que c’est la même opération.

**Étape 4 — Tentative attribution opérateur**.

Patterns observables :

- Adresses fraîches utilisées par cycles (T1-T12 alternées sur 6 mois).
- Consolidation rapide post-réception (souvent dans les 24h).
- Cashout via exchanges asiatiques.

Patterns cohérents avec **compound asiatique** (Cambodge, Myanmar, Laos selon distribution typologique 2024-2026 documentée par TRM Labs et Elliptic). Pas d’attribution individuelle.

## 36.6 Phase 4 — Analyse et synthèse

**Calibration** :

|Élément                                                 |Niveau       |Confiance|
|--------------------------------------------------------|-------------|---------|
|Marie a déposé 198 200 USDT vers T1, T2, T3             |Fait         |Certain  |
|T1, T2, T3 sont liés à l’opération « CryptoYield Pro »  |Très probable|90%      |
|T-HUB est la consolidation centrale de l’opération      |Probable     |80%      |
|Au moins 400 victimes affectées par l’opération         |Probable     |75%      |
|L’opération est gérée depuis un compound Asie du Sud-Est|Possible     |50%      |
|L’identité « Daniel Wang » est usurpée                  |Très probable|90%      |
|Récupération des fonds Marie possible                   |Peu probable |15%      |

**Volume de l’opération** :

- ~3,2 M USDT cumulé sur 6 mois identifiés (probablement plus avant et après).
- Marie représente ~6% du volume total observé.

**Points de cashout identifiés** :

- Exchange asiatique (KYC faible).
- Garantex (sanctionné).
- DEX TRON.
- Adresses inconnues (probables OTC/P2P).

## 36.7 Phase 5 — Rapport et recommandations

**Rapport de 22 pages** structuré (Annexe H) :

- Executive summary.
- Méthodologie.
- Faits Marie (timeline, transactions).
- Cartographie de l’opération (graphes).
- Volume estimé et nombre de victimes.
- Points de cashout et angles d’action.
- Limites et incertitudes.
- Recommandations.

**Recommandations** :

1. **Pour Marie** :
- Transmettre le rapport au procureur en charge de la plainte.
- Signaler l’identité usurpée à l’entrepreneur singapourien (action de courtoisie).
- Documenter ses pertes pour fiscalité (déduction de pertes en investissement frauduleux selon législation).
- Soutien psychologique recommandé.
1. **Pour les autorités** (si transmettent) :
- Coordination internationale via Europol / Interpol.
- Contact avec autorités cambodgiennes / myanmarcaises / laotiennes (limite : coopération variable).
- Demande de gel à exchange asiatique identifié (faible probabilité de succès).
- Surveillance des adresses identifiées (futures activités).
1. **Pour la communauté** :
- Signalement à Chainabuse pour enrichissement base communautaire.
- Partage anonymisé avec ISAC financier.

## 36.8 Restitution

Restitution à Marie : 1 heure. Marie est soulagée d’avoir une compréhension claire et un dossier solide, même si récupération improbable. Marie remercie pour la calibration honnête (pas de fausse promesse de récupération).

Le rapport est transmis par Marie au procureur en charge. Devenir ultérieur : fonction de la procédure judiciaire, hors mission cabinet.

## 36.9 Bilan honnête

✅ **Réussites** :

- Cartographie complète de l’opération.
- Identification de 400+ co-victimes potentielles.
- Volume total documenté.
- Rapport actionnable pour autorités.

⚠️ **Limites** :

- Pas de récupération des fonds Marie (probabilité faible reconnue dès le départ).
- Pas d’identification civile des opérateurs (probable compound asiatique, hors d’atteinte OSINT).
- Cashout via exchange non-KYC = peu d’angles directs.

📊 **Métriques** :

- Durée : 12 jours analyste senior.
- Coût : 22 000 EUR.
- Couverture : 100% des flux Marie tracés. ~75% des flux opération globale identifiés.
- Calibration : tous les éléments avec WEP explicite.

**Apprentissage clé** : pour pig butchering, l’enquête **fonctionne** (cartographie, identification écosystème, alimente justice) mais ne **récupère** pas les fonds dans la grande majorité des cas. Honnêteté du mandat dès le départ = relation client saine.

-----
