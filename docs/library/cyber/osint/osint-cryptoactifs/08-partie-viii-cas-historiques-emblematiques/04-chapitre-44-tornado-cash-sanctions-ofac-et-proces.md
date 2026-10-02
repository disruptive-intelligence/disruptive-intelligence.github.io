---
title: Chapitre 44 — Tornado Cash — sanctions OFAC et procès
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VIII — Cas historiques emblématiques
  - index.md
---

**Tornado Cash** est le cas emblématique de **conflit entre code open source et responsabilité légale**. Sanctions OFAC, démantèlement partiel, procès des développeurs — débat juridique en cours.

## 44.1 Le contexte

**Tornado Cash** : mixer décentralisé sur Ethereum, lancé août 2019 par Roman Semenov, Roman Storm, Alexey Pertsev. Cf Ch.31.

**Adoption** :

- 2019-2022 : usage massif. Multi-milliards USD passés à travers les pools.
- Légitime : utilisateurs privacy-conscious, payments anonymes, donations sensibles.
- Illicite : Lazarus, ransomware, hackers DeFi.

## 44.2 Les sanctions OFAC — août 2022

**8 août 2022** : OFAC sanctionne Tornado Cash.

**Justifications** :

- Plus de **7 Mrd USD** estimés blanchis via Tornado depuis 2019.
- Usage massif par Lazarus (incluant Ronin, Ch.43).
- Usage par autres acteurs ransomware et fraude.

**Sanctions** :

- Adresses smart contracts Tornado Cash placées sur SDN list.
- Toute interaction par US persons interdite.
- Étendu à GitHub : Microsoft désactive le repo Tornado et comptes développeurs (controverse, partiellement réversé après).

**Réactions** :

- Communauté privacy : réaction forte. Paradigme de **« les développeurs ne sont pas responsables des usages »**.
- Civil liberties orgs (EFF, Coin Center) attaquent en justice.
- Multi-application : Coinbase finance partiellement le procès Coin Center vs OFAC.

**Coin Center vs OFAC** :

- Argument : OFAC outrepasse son mandat en sanctionnant un smart contract immutable (vs une personne / entité).
- Procès en cours 2023-2024-2025.
- Premiers verdicts : partiellement favorables aux plaintifs (un juge a noté que les smart contracts immutables ne peuvent pas être « personnes » sanctionnables au sens classique).
- Évolution complexe, à suivre.

## 44.3 Inculpation et procès Pertsev

**Alexey Pertsev** : développeur de Tornado Cash, Russe, résidant Pays-Bas.

**Arrestation — août 2022** : arrêté Pays-Bas suite à enquête FIOD (autorité financière néerlandaise).

**Charges** : blanchiment d’argent (faciliter le blanchiment via le service développé).

**Procès — 2023-2024** :

- Argumentation accusation : Pertsev a sciemment continué à développer un service utilisé massivement pour blanchiment, malgré conscience.
- Argumentation défense : Tornado est code open source, immutable, Pertsev ne contrôlait pas les usages.

**Verdict — 14 mai 2024** : Pertsev **condamné** par tribunal néerlandais à **5 ans et 4 mois de prison** pour blanchiment d’argent.

**Implications** :

- Premier verdict significatif sur responsabilité de développeur de mixer.
- Précédent juridique majeur EU.
- Appel en cours.

## 44.4 Inculpation Storm aux US

**Roman Storm** : co-développeur Tornado, US-resident.

**Inculpation — août 2023** : DOJ inculpe Storm pour conspiracy to commit money laundering, conspiracy to operate unlicensed money transmitter, conspiracy to violate sanctions.

**Arrestation** : Storm arrêté août 2023.

**Procès US — 2024-2025** :

- Procès initialement programmé septembre 2024.
- Reporté à plusieurs reprises.
- Procès tenu finalement 2025 selon évolution.
- **Verdict** : à confirmer selon évolution. Au moment de rédaction (2026), procédures en cours / partiellement résolues.

**Roman Semenov** : autre développeur, sanctionné OFAC août 2023, en fuite (juridiction non révélée publiquement).

## 44.5 Évolutions post-sanctions

**Tornado Cash continue de fonctionner** : code immutable. Smart contracts sur Ethereum, accessibles techniquement. Volume très réduit post-sanctions (~95% drop) mais non-nul.

**Acteurs contournant** :

- Lazarus continue à utiliser Tornado malgré sanctions.
- Autres acteurs criminels conscients du risque.

**Migrations** :

- Vers d’autres mixers (Sinbad sanctionné après).
- Vers privacy coins (Monero).
- Vers techniques mixtes (CoinJoin Bitcoin + bridges).

**Sanctions Sinbad — novembre 2023** : OFAC sanctionne Sinbad.io, mixer ayant pris une partie du volume post-Tornado. Cycle continue.

## 44.6 Leçons

**Pour l’industrie crypto** :

- **Développeurs peuvent être tenus responsables** dans certaines juridictions.
- **Code immutable n’est pas immunité légale**.
- Distinction floue entre « outils neutres » et « facilitations volontaires ».

**Pour les utilisateurs** :

- **Risque de sanctions** d’utiliser un service dont l’opérateur sera sanctionné rétroactivement.
- **Compliance** devient préoccupation majeure.

**Pour les enquêteurs** :

- **Tornado Cash post-sanctions** : moins de volume, mais acteurs criminels qui continuent sont **identifiables comme criminels** (interaction avec sanctions = signal fort).
- **Multiplications de mixers** rend tracking plus complexe mais aussi chaque service plus exposé.

## 44.7 Pour l’analyste

Le cas Tornado Cash illustre l’**évolution réglementaire rapide** de l’écosystème crypto. L’analyste suit :

- Listes OFAC SDN (mises à jour régulières).
- Sanctions UE / autres juridictions.
- Procédures judiciaires marquantes.
- Évolutions du débat « code as speech » vs régulation.

Ces cadres déterminent **ce qui est légitimement enquêtable**, **ce qui peut faire l’objet d’action** (gel, saisie), et **ce qui expose l’utilisateur final** (interaction avec sanctioned).

-----
