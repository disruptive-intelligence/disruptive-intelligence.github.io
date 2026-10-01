---
title: Chapitre 1 — Pourquoi l’OSINT crypto est devenu central
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie I — Comprendre l’écosystème crypto sans fantasme
  - index.md
---

Les crypto-actifs ne sont plus une curiosité technique réservée aux passionnés. En 2026, ils sont **infrastructure de transfert de valeur** pour des pans entiers de la cybercriminalité, de la fraude retail, du contournement de sanctions, et plus marginalement de l’économie légitime. L’analyste financier ou cyber qui ne sait pas lire une transaction blockchain est aujourd’hui handicapé sur une part croissante de ses dossiers.

## 1.1 Le crypto comme infrastructure de transfert de valeur

Les blockchains publiques offrent une fonctionnalité que les systèmes bancaires traditionnels n’ont jamais su offrir aussi simplement : **transférer de la valeur de pair à pair, sans intermédiaire de confiance, à travers les frontières, en quelques minutes**. Cette propriété, neutre par construction, sert :

- L’**économie légitime** : remittances internationales (envois d’argent par les diasporas), paiements B2B cross-border, marchés DeFi régulés, achats institutionnels (entreprises listées détenant du Bitcoin en trésorerie).
- L’**économie grise** : contournement de contrôles des changes (Chine, Argentine, Liban, Nigeria), utilisation par des entrepreneurs dans des juridictions à banking dysfonctionnel.
- L’**économie criminelle** : ransomware, fraudes retail (pig butchering, Ponzi crypto), darknet markets, contournement de sanctions internationales (Russie post-2022, Corée du Nord), blanchiment d’argent.

Pour l’analyste, comprendre que le crypto est **infrastructure neutre** — pas intrinsèquement criminelle — est important. La même blockchain qui transporte une rançon ransomware transporte aussi le salaire d’un développeur ukrainien payé par une entreprise européenne. La distinction est dans **l’usage**, pas dans l’outil.

## 1.2 Pourquoi les criminels utilisent le crypto

Plusieurs propriétés rendent les crypto-actifs attractifs pour la criminalité.

**Pseudonymat**. Les adresses ne sont pas directement reliées à l’identité civile. Pour un criminel ne maîtrisant pas l’OPSEC, c’est une protection apparente.

**Globalité**. Une transaction crypto traverse les frontières instantanément, sans contrôle bancaire intermédiaire. Pratique pour les transactions internationales criminelles.

**Irréversibilité**. Une transaction confirmée ne peut pas être annulée par chargeback (contrairement aux cartes bancaires). Pour le ransomware, c’est essentiel — la victime ne peut pas « rappeler » la rançon.

**Liquidité globale**. Les marchés crypto fonctionnent 24/7, dans toutes les juridictions, avec des centaines d’exchanges. La conversion en monnaie utilisable est, en principe, possible partout.

**Absence d’intermédiaire centralisé** (pour les blockchains publiques). Pas de banque à convaincre, pas de régulateur à contourner — du moins en théorie.

**Mais ces avantages criminels sont contrebalancés par une faiblesse structurelle** : la **traçabilité publique**. Sur une blockchain comme Bitcoin ou Ethereum, **toutes les transactions sont visibles à jamais**. C’est une différence fondamentale avec le cash (anonyme et sans trace) ou même le système bancaire (où les transactions sont privées sauf réquisition légale). Le criminel crypto laisse une trace **publique, permanente, analysable**. C’est l’opportunité que l’OSINT crypto exploite.

## 1.3 La transparence partielle des blockchains

Les blockchains publiques sont **transparentes**. Toute transaction est visible :

- Quelle adresse a envoyé combien à quelle adresse.
- Quand (timestamp précis).
- Quel actif (BTC, ETH, USDT, etc.).
- Avec quels frais.

Cette transparence est **publique** : pas besoin d’être bank, pas besoin de réquisition, pas besoin de mandat. N’importe qui avec un explorateur peut lire les transactions de n’importe quelle adresse, à tout moment, depuis le bloc genesis.

**Mais transparence ≠ identité**. Voir qu’une adresse a reçu 10 BTC ne dit pas qui contrôle cette adresse. C’est ici qu’intervient le travail d’enquête : relier les adresses observées à des **entités** (services, individus, groupes) via des labels publics, des heuristiques de clustering, et des recoupements OSINT off-chain.

## 1.4 Pseudonymat vs anonymat — la nuance fondamentale

**Pseudonymat** : les transactions sont publiques mais associées à des pseudonymes (adresses) qui ne révèlent pas directement l’identité. Bitcoin et Ethereum sont pseudonymes. Une fois le pseudonyme relié à une identité (KYC d’exchange, publication volontaire, erreur OPSEC), **l’historique entier devient attribuable**.

**Anonymat** : les transactions ne révèlent ni les parties ni les montants. Monero, Zcash (mode shielded). Casser cet anonymat nécessite des moyens cryptographiques avancés ou des erreurs spécifiques de l’utilisateur.

Cette distinction est **structurante** pour l’analyste :

- Sur **Bitcoin / Ethereum / TRON / Solana / la plupart des blockchains** : l’enquête est faisable, parfois fastidieuse mais méthodologiquement claire.
- Sur **Monero** : l’enquête on-chain est largement bloquée. Le travail se déplace vers les **points off-chain** (exchanges, OPSEC errors, infrastructure).

## 1.5 « Tout est public » ne veut pas dire « tout est attribuable »

Erreur répandue, y compris chez certains journalistes : confondre la **lisibilité publique** des transactions avec la **possibilité d’attribuer** chaque adresse à une personne.

La réalité :

- **~10-20%** des adresses Bitcoin actives sont labellisées (services connus, exchanges, mixers, sanctioned entities). Source : observations Chainalysis et autres vendors.
- **~80-90%** restent **unlabelled** — appartenant à des entités non identifiées (utilisateurs particuliers, services obscurs, criminels n’ayant jamais interagi avec un service KYC).
- Les **clusters** regroupent des adresses appartenant probablement à une même entité, mais l’identification de cette entité reste ouverte sans données off-chain.

Pour le criminel sophistiqué qui n’utilise jamais un exchange KYC, dont les wallets sont créés avec OPSEC stricte, et dont les flux passent par mixers et privacy coins, **l’attribution complète peut être impossible** sur les seules données publiques.

## 1.6 Place de l’OSINT crypto dans l’écosystème professionnel

L’OSINT crypto s’intègre dans plusieurs métiers :

**CTI (Cyber Threat Intelligence)**. Suivi de wallets de groupes ransomware, IAB, opérateurs malware. Identification de patterns de paiement. Alimentation de threat intel actionnable.

**SOC et IR**. Validation de paiements de rançon, traçage post-incident, identification de wallets compromis. Coordination avec les enquêteurs financiers.

**Forensique**. Capture et analyse de preuves crypto dans le cadre d’investigations. Documentation pour procédures judiciaires.

**Lutte anti-fraude**. Investigation de scams retail (pig butchering, faux investissements), détection de patterns de blanchiment.

**Conformité (AML/CFT)**. Screening de transactions, surveillance de clientèle, déclarations TRACFIN, application des sanctions OFAC/UE.

**Enquête judiciaire**. Soutien technique aux enquêteurs financiers et magistrats. Production de pièces à conviction. Coopération internationale via réquisitions.

**Enquête patrimoniale**. Identification d’avoirs crypto dans le cadre de successions, divorces, recouvrement de créances.

**Renseignement**. Suivi des flux financiers liés à des acteurs étatiques sanctionnés, organisations terroristes, prolifération.

Pour chacun de ces métiers, l’OSINT crypto est un **outil** parmi d’autres, à intégrer dans une démarche plus large. Rare est le dossier qui se résout uniquement par analyse on-chain — le crypto **complète** l’OSINT classique, le SIGINT, le HUMINT, la coopération institutionnelle.

## 1.7 L’évolution 2020-2026

L’écosystème crypto et son investigation ont profondément évolué.

**Maturation des outils**. Chainalysis (fondé 2014), TRM Labs (2018), Elliptic (2013) ont structuré une industrie de la blockchain intelligence. Capacités de clustering, labellisation, scoring de risque, intégration AML — tout cela était embryonnaire en 2017, mature en 2026.

**Saisies massives**. La saisie Bitfinex (3,6 Mrd USD en 2022, Ch.41), Colonial Pipeline (2,3 M USD récupérés, Ch.42), opérations contre mixers (Helix, Bitcoin Fog, Chipmixer, Tornado Cash, Samourai) montrent que **le traçage fonctionne** — quand les ressources et la coopération internationale s’alignent.

**Diversification des typologies**. Le ransomware reste dominant en volume médiatique, mais le **pig butchering** est devenu un fléau retail en explosion (estimations Chainalysis 2024-2025 : plusieurs milliards USD/an), les **hacks DeFi** alimentent des vols récurrents, les **acteurs étatiques** (Lazarus en tête) mobilisent des techniques de plus en plus sophistiquées.

**Essor des stablecoins**. USDT et USDC sont devenus la **monnaie de transaction** de pans entiers de l’écosystème, légitime comme illicite. Le FATF souligne en 2024-2025 que les stablecoins représentent une part majeure des volumes on-chain et une fraction significative des flux illicites observables. TRON est devenu la blockchain dominante pour les flux USDT illicites en volume.

**Pression réglementaire**. MiCA en UE (entrée en vigueur 2024), Travel Rule étendue, sanctions OFAC ciblant des entités crypto (Tornado Cash août 2022, Garantex, Suex, Bitzlato), durcissement KYC sur les exchanges centralisés. L’écosystème devient progressivement **moins anonyme** par couche réglementaire.

**Intégration IA**. Les outils de blockchain intelligence intègrent du ML pour détection de patterns, automatisation d’attribution, scoring de risque. Côté criminel, l’IA assiste la création de faux profils (pig butchering automatisé), le contournement de KYC.

## 1.8 Fil rouge — MIXSHADOW : la sollicitation

> **🔗 MIXSHADOW — Épisode 1 : le mandat**
> 
> Lundi 16 mars 2026. Sarah Marin reçoit le brief de mission. Réunion de cadrage en visio avec :
> 
> - Le **RSSI d’Aurélien Médical**, qui a piloté la cellule de crise depuis le 8 mars (date de chiffrement).
> - Deux **interlocuteurs DGSI** (officier traitant + spécialiste cyber).
> - Un **représentant TRACFIN** (cellule cyber).
> - Le **directeur d’Athéna Group**.
> 
> Le RSSI présente les faits. Compromission Akira datée du 8 mars vers 03h47 (chiffrement effectif). Vecteur d’entrée : compromission d’un compte VPN administrateur via stealer log acquis sur Russian Market (forensics Mandiant). Demande de rançon initiale : 80 BTC (~4,5 M EUR). Négociation via portail Tor descend à 35 BTC (~2 M EUR). Paiement effectué le 14 mars à 09h12. Décryption key reçue à 15h28 le même jour. Reprise opérationnelle progressive sur 3 semaines.
> 
> La DGSI précise le cadre : Athéna travaille sous mandat client (Aurélien Médical) avec **coopération étroite** mais non exclusive avec la DGSI. Remontée bi-hebdomadaire. Pas d’engagement public, TLP RED jusqu’à autorisation contraire. Coordination prévue avec Europol EC3 (le groupe Akira étant suivi par plusieurs services européens). FBI Cyber Division en partenaire potentiel via la DGSI (les US ont également des victimes Akira documentées).
> 
> Le mandat Athéna : tracer, cartographier, identifier les off-ramps, contribuer à l’attribution, coopérer.
> 
> Sarah note : objectif réaliste. Pas de promesse de récupération. La mission est de **maximiser la valeur de renseignement** extraite des 35 BTC payés, et d’alimenter des dossiers en cours qui dépassent largement le cas Aurélien Médical isolé.
> 
> Première action : préparer son environnement d’investigation et démarrer le traçage. Ch.5 détaillera l’OPSEC ; Ch.6 l’environnement ; Ch.13 le démarrage formel.

-----
