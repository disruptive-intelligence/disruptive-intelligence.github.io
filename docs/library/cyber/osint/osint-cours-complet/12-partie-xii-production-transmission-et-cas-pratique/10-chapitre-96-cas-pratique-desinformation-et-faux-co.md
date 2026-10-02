---
title: 'Chapitre 96 — Cas pratique : désinformation et faux comptes IA'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 96.1 Présentation du cas

Un acteur économique majeur subit une vague d'allégations soudaines sur les réseaux sociaux, accusant l'entreprise de pratiques environnementales nocives. Les allégations apparaissent simultanément sur X, LinkedIn, Telegram, en plusieurs langues. L'analyste OSINT est mandaté pour :

- Caractériser le phénomène : organique ou coordonné ?
- Identifier les acteurs derrière.
- Évaluer la sophistication.
- Documenter pour action ultérieure.

## 96.2 Étape 1 — Cartographie initiale

**Collecte.**

- 47 comptes X identifiés relayant les allégations (recherche par mots-clés et hashtags).
- 23 profils LinkedIn équivalents (mais difficile : LinkedIn restreint).
- 12 canaux Telegram amplifiant.
- 3 blogs dédiés (« exposing-X.com », « X-truth.eu », « la-verite-X.fr »).

## 96.3 Étape 2 — Analyse temporelle

**Heatmap d'activité.** Les 47 comptes X publient leur premier message dans une fenêtre de 8 heures, sur 3 jours consécutifs.

**Pattern remarquable.** Création de 23 comptes parmi les 47 dans la même semaine (4-10 mai 2026), tous il y a 6-8 mois avant le pic d'activité.

**Conclusion.** Coordination temporelle très forte. Probabilité d'organique : quasi-nulle.

## 96.4 Étape 3 — Analyse de profils

**Photos profil.** Pour les 47 comptes :

- 38 photos identifiées comme **IA-generated** (Hive Moderation > 70 %).
- 6 photos volées de banques d'images.
- 3 photos non analysables (résolution basse).

**Bios.**

- Tons similaires : « citoyen engagé », « éco-citoyen », « activiste environnemental ».
- Tournures parfois identiques mot pour mot (avec variations mineures).
- Pas de cohérence biographique vérifiable.

**Conclusion.** Faux comptes industriels.

## 96.5 Étape 4 — Analyse de contenu

**Narratifs.**

- 3-4 messages principaux récurrents.
- Variations linguistiques mais cohérence sémantique.
- Vocabulaire technique étonnamment proche entre comptes différents.

**Stylométrie comparative.** Plusieurs comptes partagent des tournures spécifiques suggérant rédaction commune ou LLM.

**Test LLM-generated.** GPTZero sur 30 posts longs : 24/30 « likely AI-generated ». Originality : équivalent.

**Conclusion.** Contenu probablement généré par LLM, distribué entre comptes.

## 96.6 Étape 5 — Analyse de réseau

**Construction graphe.** Maltego + Gephi sur :

- Followings / followers entre les 47 comptes.
- Retweets / replies / mentions.

**Communautés détectées.** Algorithme Louvain identifie :

- Communauté 1 : 18 comptes « activistes francophones ».
- Communauté 2 : 14 comptes « eco-conscious anglophones ».
- Communauté 3 : 11 comptes hispanophones.
- 4 comptes pivots reliant les communautés.

**Centralité.** 4 comptes pivots ont degree centrality très élevée. Hypothèse : amplificateurs principaux.

## 96.7 Étape 6 — Infrastructure technique

**Domaines.** WHOIS sur les 3 blogs :

- `exposing-X.com` : créé 8 février 2026, registrar Namecheap, masqué RGPD.
- `X-truth.eu` : créé 11 février 2026, registrar OVH, contact email Proton.
- `la-verite-X.fr` : créé 14 février 2026, registrar Gandi, masqué.

**Cohérence temporelle.** Créations sur 6 jours.

**Hébergement.** Tous derrière Cloudflare.

**Trackers.** Recherche Google Analytics commun entre les 3 sites : oui, GA Property partagé. Pivot critique.

**Recherche DNSlytics.** GA Property identifié sur un quatrième site, non encore dans le périmètre : `eco-watcher.net`. Cluster élargi.

## 96.8 Étape 7 — Attribution

**Hypothèses concurrentes ACH.**

| H | Description | Soutien |
|---|---|---|
| H1 | Concurrent commanditant campagne | Cohérent intérêt commercial |
| H2 | Activisme authentique avec amplification artificielle | Inco. avec IA-generated content |
| H3 | Acteur étatique étranger | Cohérence avec patterns Doppelgänger |
| H4 | Officine privée (mercenaires désinformation) | Compatible |

**Indicateurs supplémentaires.**

- Aucun élément linguistique typique d'opération étatique (pas de signature russe/chinoise typique).
- Cohérence avec opération orientée business (concurrent ou officine).

**Conclusion ACH.** **Probable** : opération coordonnée par acteur commercial ou officine de désinformation à louer (H1 ou H4). H3 résiduellement possible mais moins soutenue. H2 réfutée.

## 96.9 Étape 8 — Production

**Note courte au mandataire (Ch.87).**

> **BLUF.** L'examen des 47 comptes X, 12 canaux Telegram, 3 blogs et 4e site identifié confirme l'existence d'une **opération de désinformation coordonnée** ciblant l'entreprise. Caractéristiques : faux comptes industriels (photos IA), contenu généré par LLM, infrastructure technique mutualisée (GA partagé), coordination temporelle stricte. Attribution probable : acteur commercial ou officine de désinformation à louer. Niveau de confiance : probable. **Recommandation : signalement aux plateformes pour suppression, documentation pour action judiciaire, réponse communicationnelle calibrée.**

## 96.10 Étape 9 — Suite

**Actions immédiates.**

- Signalement aux plateformes (X, Telegram, blogs).
- Préservation des pièces.
- Veille active.

**Actions moyen terme.**

- Si campagne persiste : action judiciaire (atteinte à l'honneur, diffamation, parfois denigrement commercial).
- Plainte VIGINUM si caractère étatique étranger se confirmait.
- Communication ciblée pour démentir les allégations spécifiques.

## 96.11 Pédagogie

Ce cas illustre :

- Détection rapide d'inauthenticité industrielle.
- Identification du pattern par croisement multi-dimensions (temporel, profil, contenu, infrastructure).
- Outils complémentaires : photo IA detection + LLM detection + graphe + reverse trackers.
- Attribution prudente avec ACH.
- Recommandations actionnables en plusieurs niveaux.

-----
