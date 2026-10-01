---
title: Chapitre 23 — Collecte, conservation et chaîne de preuve crypto
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IV — Outils et workflow
  - index.md
---

L’enquête ne sert à rien si les preuves ne sont pas **conservées** correctement. Pour rapport, contestation, procédure judiciaire — la **chaîne de preuve** détermine la valeur du travail. Ce chapitre couvre la méthode.

## 23.1 Pourquoi la chaîne de preuve

Trois objectifs :

**Reproductibilité**. Un autre analyste, 6 mois ou 5 ans plus tard, doit pouvoir refaire l’analyse à partir des mêmes données.

**Crédibilité**. En cas de contestation (par l’acteur enquêté, par un tribunal, par un journaliste), l’analyste peut prouver que les données utilisées sont authentiques.

**Valeur juridique**. Pour soutenir une plainte, une réquisition, ou une saisie, les preuves doivent répondre à des standards.

## 23.2 Captures d’écran et documents

**Méthode** :

**Screenshots** :

- Capture **complète** de la page (pas seulement zone d’intérêt).
- URL visible.
- Horodatage de capture (date+heure UTC précis).
- Format PNG ou JPG haute qualité.

**HTML / Source** :

- Sauvegarde du **HTML brut** pour archives permanentes.
- Outils : Hunchly, Save Page WE, wget, scripts custom.
- Permet inspection sans dépendance à site externe (qui peut évoluer).

**PDF** :

- Capture en PDF pour annexes de rapport.
- Format portable.

**Hash** :

- SHA-256 de chaque fichier capturé.
- Permet de **prouver** que le fichier n’a pas été modifié.
- Stocker les hashes dans un journal séparé.

## 23.3 Captures de transactions

Pour chaque transaction d’enquête :

**Capture de la page d’explorateur** :

- Mempool.space, Etherscan, Tronscan, etc.
- Fenêtre complète avec URL.
- Onglets pertinents (Logs ERC-20, Internal Transactions, etc.).

**TXID** :

- Noté dans le journal d’enquête.
- La blockchain est immutable — le TXID est une référence permanente.

**Cross-references** :

- Si même transaction visible sur plusieurs explorateurs, capturer plusieurs vues. Validation croisée.

**Outils pro export** :

- Reactor / TRM / Elliptic permettent exports CSV des transactions analysées.
- Capturer aussi la vue graph dans l’outil.

## 23.4 Captures d’adresses

Pour chaque adresse pertinente :

**Page d’explorateur** :

- Solde actuel.
- Historique transactions (paginer si nécessaire).
- Labels visibles.
- Première et dernière transaction.

**Page outil pro** (si applicable) :

- Vue cluster.
- Labels propriétaires.
- Risk score.

**Captures successives** : pour adresse en surveillance active, captures régulières (quotidiennes) pour tracer l’évolution.

## 23.5 Métadonnées du journal d’enquête

Le journal d’enquête (Markdown) inclut, pour chaque entrée :

- **Date et heure UTC**.
- **Action effectuée**.
- **Source consultée** (URL si applicable).
- **Référence à la capture** (nom de fichier + hash SHA-256).
- **Observation et hypothèse**.

Ce journal est lui-même versionné (Git ou équivalent), avec sauvegardes immutables.

## 23.6 Stockage immutable

**Principe** : les preuves ne doivent pas pouvoir être **modifiées rétroactivement** (par négligence ou par malveillance interne).

**Méthodes** :

**WORM storage (Write Once Read Many)** :

- Solutions enterprise (NetApp, Dell, AWS S3 Object Lock).
- Garantie technique d’immutabilité.
- Standard pour environnements judiciaires sérieux.

**Hashing avec timestamping qualifié** :

- Hash SHA-256 des fichiers.
- Timestamping via service qualifié (e.g. eIDAS qualified timestamping en EU).
- Permet de prouver que le fichier existait à une date précise.

**Blockchain anchoring** :

- Hash des fichiers ancrés dans une blockchain (OpenTimestamps via Bitcoin, par exemple).
- Preuve d’existence à une date.
- Coût marginal.

**Bonne pratique combinée** :

- Hash SHA-256 de chaque preuve.
- Stockage en WORM (ou équivalent).
- Hashes archivés dans un journal cumulatif lui-même WORM.
- Pour cas judiciaires importants : timestamping qualifié.

## 23.7 Chain of custody

Pour preuves potentiellement judiciaires, tenue d’une **chain of custody** explicite.

**Format type** :

```
Pièce de preuve : Capture transaction TXID e3a5...
Date de collecte : 2026-03-14 09:30 UTC
Collecté par : Sarah Marin, Athéna Group
Source : mempool.space
Hash SHA-256 : abc123...
Format : HTML + PNG screenshot
Stockage : Athéna secure storage, path /MIXSHADOW/evidence/tx_e3a5...
Accès : Sarah Marin, directeur Athéna, autorités sur réquisition
Modifications : Aucune (immutable)
Transmission : Transmise à DGSI le 2026-03-15 (capture intégrale + hash)
```


Chaque pièce a sa fiche. Ensemble forme la chain of custody.

## 23.8 Limites des captures

**Captures pas suffisantes pour preuve judiciaire absolue**. Une capture peut être falsifiée. Pour preuves lourdes :

- Hashing + timestamping qualifié.
- Cross-references multiples.
- Données de la blockchain elle-même (TXID, qui est immutable).

**Données dynamiques**. Soldes peuvent évoluer entre capture et utilisation. Toujours noter le timestamp.

**Variations explorateurs**. Les explorateurs peuvent évoluer (UI changes, données enrichies). Capture à un moment T peut différer de capture à T+6 mois.

**Solution robuste** : référer aux **données blockchain elles-mêmes** (TXID, block height) — immutables — plutôt qu’aux représentations dans les explorateurs.

## 23.9 Pour les rapports formels

**Citations de transactions** :

- Format normalisé : « TXID [hash], block [N], date [UTC] ».
- Capture en annexe avec hash.
- Lien stable vers explorateur (si possible).

**Citations d’adresses** :

- Adresse complète.
- Blockchain explicite.
- Capture de page d’explorateur en annexe.

**Citations d’analyses outils pro** :

- « Cluster Reactor ID […] avec [N] adresses, label ‘Akira’ attribué avec confiance high par Chainalysis le [date] ».
- Captures Reactor en annexe.

## 23.10 Fil rouge — MIXSHADOW : chain of custody

> **🔗 MIXSHADOW — Épisode 15 : preuve solide**
> 
> Pour MIXSHADOW, Sarah maintient une chain of custody rigoureuse.
> 
> **Pour chaque transaction Akira** capturée :
> 
> - Capture HTML de la page Mempool.space (ou Etherscan / Tronscan selon chaîne).
> - Screenshot PNG.
> - Capture de la vue Reactor correspondante.
> - Hash SHA-256 de chaque fichier.
> - Entrée dans le journal Markdown daté.
> 
> **Pour chaque rapport hebdomadaire** envoyé à la DGSI :
> 
> - PDF du rapport.
> - Hash SHA-256 du PDF.
> - Annexes incluses (captures principales).
> - Email avec accusé de réception.
> 
> **Stockage** :
> 
> - Tous les fichiers MIXSHADOW dans un répertoire chiffré.
> - Sauvegarde quotidienne sur stockage WORM Athéna.
> - Hashes cumulés dans un fichier `MIXSHADOW_hashes.csv` lui-même hashé.
> - Tâche cron qui ancre le hash global hebdomadaire dans Bitcoin via OpenTimestamps (preuve d’existence à date).
> 
> **Pour le rapport final** (semaine 8) :
> 
> - Toutes les preuves référées sont accompagnées de leur hash dans l’annexe.
> - Méthodologie de collecte décrite (« captures via Hunchly, hashing SHA-256, stockage WORM, anchoring OpenTimestamps »).
> - Permet à la DGSI ou autorité ultérieure (procureur, juge) de vérifier l’intégrité.
> 
> Le coût en temps : ~10% du temps total d’enquête. Cher mais indispensable. Sans cette discipline, le rapport est lu mais non utilisable formellement. Avec, il est exploitable judiciairement.

-----
