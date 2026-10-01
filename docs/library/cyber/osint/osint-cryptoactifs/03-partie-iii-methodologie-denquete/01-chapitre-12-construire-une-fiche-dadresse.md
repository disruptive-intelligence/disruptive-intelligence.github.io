---
title: Chapitre 12 — Construire une fiche d’adresse
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

La **fiche d’adresse** est l’unité documentaire de base de l’enquête crypto. Pour chaque adresse pertinente, l’analyste constitue une fiche structurée qui synthétise tout ce qu’il sait. Les fiches s’agrègent en graphe d’enquête. Sans fiche, l’enquête se dilue dans le flou.

## 12.1 Pourquoi la fiche d’adresse

Trois fonctions :

**Mémoire**. L’enquête sur 50 adresses, sur 8 semaines, ne peut pas tenir « dans la tête ». La fiche externalise la mémoire et permet de retrouver instantanément ce qu’on sait sur une adresse spécifique.

**Communication**. Quand Sarah doit briefer la DGSI ou son directeur Athéna sur l’enquête, les fiches d’adresses sont son support. Synthèse précise, vérifiable.

**Calibration**. Tenir une fiche oblige à expliciter ce qu’on sait, ce qu’on suppose, et ce qu’on ne sait pas. Discipline anti-confusion entre observation et inférence.

## 12.2 Le template fiche d’adresse

Modèle complet à adapter selon l’enquête. À retrouver en Annexe B.

```markdown
# Fiche adresse — [Identifiant abrégé]

## Identification
- **Adresse complète** : [adresse exacte 42-56 caractères]
- **Blockchain** : [Bitcoin / Ethereum / TRON / Solana / etc.]
- **Type d'adresse** : [P2PKH / P2SH / SegWit / Taproot / EOA / Contract / autre]
- **Identifiant interne enquête** : [Akira-BTC-007 par exemple]

## Activité observable
- **Première transaction** : [date UTC, TXID]
- **Dernière transaction** : [date UTC, TXID]
- **Nombre total de transactions** : [N]
- **Solde actuel** : [montant et actif]
- **Actifs reçus historiques** : [montants par actif]
- **Actifs envoyés historiques** : [montants par actif]

## Contreparties
- **Adresses contreparties principales** : [top 5-10 par volume]
- **Services labellisés impliqués** : [exchanges, mixers, bridges identifiés]
- **Cluster Chainalysis (ou TRM)** : [ID cluster + nb adresses + label si applicable]

## Labels publics
- **Labels Etherscan / Tronscan / Mempool** : [liste]
- **Labels propriétaires Chainalysis / TRM** : [si accès]
- **Sanctions OFAC** : [oui/non + détail si oui]
- **Mentions OSINT** : [forums, presse, twitter, etc.]

## Hypothèses
- **Hypothèse principale** : [ex : « adresse de réception ransomware Akira »]
- **Niveau de confiance** : [WEP : très probable / probable / possible / spéculatif]
- **Hypothèses alternatives** : [autres explications possibles, à noter]
- **Éléments de preuve** : [observations supportant l'hypothèse principale]
- **Éléments d'incertitude** : [observations qui pourraient contredire ou nuancer]

## Captures et sources
- **Captures de pages d'explorateur** : [liens vers fichiers archivés + hashes]
- **Sources externes** : [URL forums, presse, etc.]
- **Cross-check effectués** : [outils utilisés, dates]

## Statut enquête
- **Date de création de la fiche** : YYYY-MM-DD
- **Dernière mise à jour** : YYYY-MM-DD
- **Statut** : [Active / Surveillance / Clôturée]
- **Investigateur** : [nom]
- **Liens vers fiches connexes** : [autres adresses du graphe]
```


## 12.3 Renseigner la fiche : ordre méthodologique

**Étape 1 — Identification**. Saisie immédiate dès qu’une adresse entre dans le périmètre d’enquête. Vérifier la blockchain (erreur classique : adresse Ethereum rentrée comme adresse Bitcoin).

**Étape 2 — Activité observable**. Lecture sur explorateur principal (Mempool, Etherscan, Tronscan). Captures systématiques. Hash de chaque capture.

**Étape 3 — Contreparties**. Lister les adresses qui ont reçu/envoyé. Pour les top contreparties (par volume), noter et identifier si elles sont dans le périmètre d’enquête ou nouvelles.

**Étape 4 — Labels**. Vérifier sur explorateurs publics. Si accès aux outils pro, croiser. Sanctions OFAC : vérifier sur SDN list.

**Étape 5 — OSINT externe**. Recherche sur l’adresse dans Google, Twitter, forums (parfois des adresses sont publiquement associées à des services ou acteurs). Recherche sur DeHashed/IntelX au cas où l’adresse apparaît dans des leaks. Cf. cours **Dark Web** et **OSINT Mastery** pour méthodes.

**Étape 6 — Hypothèses**. Formuler explicitement. Calibrer la confiance.

**Étape 7 — Documentation**. Toutes les sources, captures, dates.

## 12.4 Le piège de la fiche prématurée

Une fiche peut **figer prématurément** une hypothèse. Tentation : nommer l’adresse « Akira-Hot-Wallet-3 » alors qu’on ne sait pas encore que c’est un hot wallet d’Akira.

**Bonne pratique** :

- Identifiant interne **neutre** au début (« BTC-Investigation-007 ») jusqu’à preuve d’attribution suffisante.
- Hypothèse principale **calibrée** : « possible adresse de blanchiment Akira (confiance 50%) » plutôt que « adresse Akira ».
- **Mises à jour** quand de nouvelles infos arrivent. La fiche évolue.

## 12.5 Maintien de la fiche dans le temps

Une fiche n’est pas un document one-shot. Elle évolue.

**Mises à jour quotidiennes** pour adresses actives en surveillance.

**Vérification hebdomadaire** pour adresses moins actives.

**Reprise complète** lors de tournants d’enquête (nouvel angle, validation/invalidation d’hypothèse).

**Versioning** : noter les versions successives, dater chaque mise à jour. Outils Git ou systèmes de fichiers avec horodatage suffisent.

## 12.6 Fiches et graphe

Les fiches s’articulent en **graphe** :

- Chaque fiche = un **nœud**.
- Les contreparties identifiées = **arêtes** vers d’autres fiches.
- Les patterns (peeling chain, consolidation) sont représentés par séquences d’arêtes.

Outils de visualisation (Ch.21) consomment ce graphe pour produire des vues exploitables.

-----
