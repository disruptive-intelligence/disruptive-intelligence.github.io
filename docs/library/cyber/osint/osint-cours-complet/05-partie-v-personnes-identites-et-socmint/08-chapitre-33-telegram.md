---
title: Chapitre 33 — Telegram
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 33.1 L'écosystème Telegram

**Telegram** (créé 2013 par les frères Durov) est devenu en 2024-2026 l'une des plateformes centrales pour OSINT, criminalité organisée, désinformation, et activités politiques.

**Caractéristiques.**

- Application chiffrée (E2EE pour secrets chats, non-E2EE pour conversations normales).
- Channels (broadcast unidirectionnel, jusqu'à millions d'abonnés).
- Groupes (conversations multi-utilisateurs, jusqu'à 200 000 membres).
- Bots (interfaces programmables).
- Stickers, médias.
- Mode anonyme (numéro caché, username affiché).

**Volume.** 900 millions d'utilisateurs en 2024. Géographie : forte présence Russie/CEI, Iran, Inde, Indonésie, Europe de l'Est. Croissance rapide en Occident.

## 33.2 Évolution post-arrestation Durov 2024

L'arrestation de **Pavel Durov en France (août 2024)** par les autorités françaises (mise en examen pour complicité de complicité de crimes graves via la plateforme) a déclenché des évolutions :

- Coopération renforcée avec LEA (notamment françaises).
- Partage d'IP et numéros pour réquisitions pénales graves.
- Modération renforcée (CSAM, terrorisme).
- Mais cœur business (channels, bots, anonymat raisonnable) maintenu.

**Implication.** Telegram en 2026 reste accessible mais avec coopération LEA accrue. Pour OSINT privé, les méthodes restent identiques.

## 33.3 Canaux publics : exploitation

Les **canaux publics** sont consultables sans connexion sur web (`t.me/nom_du_canal`).

**Sources OSINT.**

- **Telegago** (telegago.fr) : moteur de recherche Telegram public.
- **TGStat** (tgstat.com) : statistiques canaux publics.
- **Telemetr.io** : analyse de croissance.
- **Lyzem** : recherche dans messages historiques.
- **Combot** : statistiques de groupes.

**Méthode.**

- Recherche par mot-clé sur Telegago.
- Identification canaux suspects.
- Préservation : captures + export JSON via Telegram Desktop.

## 33.4 Groupes et observation passive

Les **groupes** nécessitent invitation ou lien public.

**Méthode.**

- Compte d'investigation Telegram (numéro dédié).
- Joindre les groupes via lien public.
- Observation passive (pas d'interaction).
- Export régulier des messages (Telegram Desktop → Export chat history → JSON).

**OPSEC.**

- Numéro d'investigation séparé physiquement.
- Mode anonyme activé (username affiché, numéro masqué aux autres).
- Pas de photo profil identifiable.

## 33.5 Bots Telegram

Les **bots** sont des comptes programmables. Pour OSINT :

**Bots utiles.**

- **@quotly_bot** : capture jolie de messages (preuves).
- **@combot** : stats de groupe.
- Bots d'archive : différents selon usage.

**Précaution.** Bots tiers voient ce que vous voyez. OPSEC : compte invest pour interactions bots.

## 33.6 Pivots Telegram → autres plateformes

**Username Telegram** est souvent unique → pivot Sherlock vers autres plateformes.

**Numéro** : si visible (souvent caché), pivot Truecaller, WhatsApp.

**Photo profil** : recherche inversée.

**Liens partagés** : révèlent infrastructure (domaines, autres canaux, sites externes).

**Cross-promotions** : un canal mentionne un autre = lien d'écosystème.

## 33.7 Cas d'usage criminels (compréhension, pas exploitation)

Telegram est utilisé pour :

- Marketplaces criminelles (vente fraudes, drogues, données).
- Recrutement (mules, hackers, terroristes).
- Diffusion de leaks et stealer logs.
- Coordination d'opérations cyber.
- Désinformation et trolling.

**Approche OSINT.**

- **Consultation** des canaux ouverts = légale.
- **Joindre** un groupe = à évaluer selon contenu (CSAM, terrorisme = refus immédiat).
- **Interaction / achat** = sortie du périmètre OSINT pur, réservé LEA.
- **Signalement** à Pharos / autorités si contenu illégal.

## 33.8 Stealer logs sur Telegram

Une part majeure du marché stealer logs (Ch.43) se déploie sur Telegram (canaux de vente, dropbox de logs).

**Approche.**

- Observation possible (cadre légal documenté).
- Pas d'achat (zone pénale).
- Documentation pour orientation enquête.

## 33.9 Méthodologie d'enquête Telegram

1. **Cartographie** : identifier les canaux/groupes pertinents (Telegago, recherche directe).
2. **Joindre** (compte invest) les groupes publics légaux.
3. **Préservation** : exports JSON réguliers.
4. **Analyse** : extraction d'entités, sélecteurs.
5. **Pivots** : usernames, numéros, liens externes.
6. **Documentation** : journal d'enquête détaillé.

## 33.10 Limites

- Channels privés / payants inaccessibles.
- Chiffrement E2EE des secrets chats.
- Bots avec accès limité.
- Évolution rapide post-Durov.

> **MIRAGE — Épisode 7 : Telegram, forums et communautés**
>
> L'analyste explore Telegram pour identifier la coordination du cluster de désinformation.
>
> **Recherche Telegago** sur termes liés à TechnoVert, Berthier, Delaunay : aucun canal public significatif détecté avec ces termes en français.
>
> **Hypothèse étendue** : la coordination peut se faire dans un canal privé ou dans un groupe spécialisé en services de désinformation à louer.
>
> **Recherche par sujets connexes** : canaux d'achat-vente de comptes X / bot networks. Identification de 12 canaux/groupes Telegram proposant ce type de service en français. Observation passive via compte d'investigation Telegram (numéro dédié, mode anonyme).
>
> **Découverte significative** : un canal `@socialmedia_boost_fr` (15 000 abonnés) propose explicitement « campagnes coordonnées 8-20 comptes, narratif fourni, plateforme X et Telegram, livré sous 72h ». Tarif affiché : 1500-3500 € par campagne selon volume.
>
> **Vérification** : ce canal est-il actif sur la période suspecte (octobre 2025 à mai 2026) ? Examen des messages publics : oui, plusieurs « livraisons » mentionnées sur la période, avec captures de comptes X qui ont depuis été suspendus. Aucune mention explicite de TechnoVert ou Berthier (les clients sont anonymisés dans les communications publiques).
>
> **Note** : ce canal est une piste forte pour l'attribution de la campagne. Cotation B2. Approfondissement à venir (cross-référencement avec les comptes coordonnés effectifs, pivot infrastructure).
>
> **Sur le volet stealer logs** : recherche dans les canaux Telegram de vente de stealer logs (8 canaux principaux identifiés). Filtre par domaine `@gmail.com` avec `delaunay76` : un hit dans un dump de janvier 2026 publié sur canal `@cloudsec_dumps`. Capture (en mode lecture seule, sans téléchargement) : 47 credentials associés à l'email `marc.delaunay76@gmail.com`, dont des entrées Binance, ProtonMail, plusieurs sites e-commerce. **Pivot crypto majeur** : compte Binance identifié → renvoi à MIRAGE 14.

-----
