---
title: Chapitre 42 — Colonial Pipeline 2021 — récupération FBI
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie VIII — Cas historiques emblématiques
  - index.md
---

Le cas **Colonial Pipeline** est emblématique pour deux raisons : impact géopolitique majeur (perturbation infrastructure US critique), et **récupération significative** des fonds par le FBI dans des délais courts.

## 42.1 Les faits

**Colonial Pipeline** : opérateur de pipelines de carburant US, fournit ~45% du fuel de la côte Est des États-Unis.

**Mai 2021** :

- 7 mai 2021 : Colonial Pipeline découvre compromission par ransomware.
- Vecteur : compte VPN avec mot de passe fuité (sans MFA).
- Auteur : groupe **DarkSide** (RaaS d’origine russophone).
- Décision : Colonial paie **75 BTC** (~4,4 M USD au cours du moment).
- Paiement effectué le 8 mai 2021.
- Décryption key reçue, mais **lente** — Colonial restaure depuis backups en parallèle.

**Impact** :

- Pipeline arrêté plusieurs jours.
- Pénuries de carburant côte Est.
- Réaction politique : Joe Biden émet executive order sur cybersécurité (12 mai 2021).
- Pression sur DarkSide qui annonce sa dissolution officielle (probable rebranding).

## 42.2 La récupération — juin 2021

**Annonce DOJ — 7 juin 2021** :

- **63,7 BTC saisis** (sur 75 payés).
- Valeur au moment de la saisie : ~2,3 M USD (Bitcoin avait baissé entre mai et juin).
- FBI a obtenu accès à la clé privée du wallet contenant ces fonds.

**Méthode** (selon DOJ press release et analyse publique) :

**Étape 1 — Tracking immédiat post-paiement**. FBI suit les BTC payés via Chainalysis dès la transaction.

**Étape 2 — Identification d’un wallet de réception**. Les fonds atterrissent finalement (via plusieurs hops) sur une adresse spécifique contrôlée par un membre de DarkSide.

**Étape 3 — Obtention de la clé privée**. C’est l’élément le plus opaque publiquement. DOJ indique avoir **obtenu la clé privée**. Modalités jamais entièrement explicitées :

- Hypothèse 1 : cloud storage compromis (similaire à Bitfinex).
- Hypothèse 2 : opération sur infrastructure DarkSide (qui était pressurée par autorités à ce moment).
- Hypothèse 3 : informations d’un insider DarkSide (members défectant).
- Hypothèse 4 : exploitation de vulnérabilités dans wallet ou infrastructure.

**Étape 4 — Saisie**. FBI signe transaction avec la clé obtenue, transférant 63,7 BTC vers wallet US gouvernement.

**Étape 5 — Annonce**. DOJ rend public ~30 jours après le paiement initial.

## 42.3 Pourquoi 63,7 sur 75 ?

Différence de 11,3 BTC (~15%). Explications probables :

- Commission affilié : DarkSide opérait en RaaS (affilié garde ~70-80%, opérateur 20-30%). 11,3 BTC pourrait correspondre à la part affilié déjà extraite vers son propre wallet (qu’autorités n’ont pas pu saisir).
- Frais opérationnels (gas, mixing).
- Conversion partielle déjà effectuée.

## 42.4 Méthodes mobilisées

**Tracking on-chain rapide** :

- Réaction en jours (vs Bitfinex en années).
- Outils : Chainalysis utilisé activement.

**Coopération sectorielle** :

- Colonial coopère pleinement avec FBI dès le départ.
- Information sur transaction de paiement immédiate.

**Coordination LEA** :

- FBI Cyber Division.
- Intelligence agencies multiples.

**Pression sur DarkSide** :

- L’attention politique post-Colonial déstabilise le groupe.
- Possible facilitation du tracking par opportunités opérationnelles.

## 42.5 Leçons

**Pour les victimes** :

- **Coopérer immédiatement** avec FBI / autorités améliore probabilité de récupération partielle.
- Pas garanti, mais sans coopération = aucune chance.

**Pour les enquêteurs** :

- **Réaction rapide** = avantage. Les premiers jours / semaines sont critiques.
- **Pression médiatique / politique** peut faciliter coopération internationale.

**Pour les criminels (perspective des autorités)** :

- **Cibler infrastructure critique** = attention politique disproportionnée. DarkSide a été un moment, jamais retrouvé sa stature.

## 42.6 Suite — DarkSide → BlackMatter → ALPHV

**DarkSide** se dissout officiellement après Colonial Pipeline. Mais **rebranding probable** :

- **BlackMatter** apparaît juillet 2021. Patterns techniques similaires à DarkSide. Saisi novembre 2021.
- **ALPHV / BlackCat** apparaît novembre 2021. Patterns continuant lignée. Démantelé 2024.

Cycle classique du RaaS : démantèlement → rebranding → re-démantèlement. L’écosystème est résilient mais pressurized.

-----
