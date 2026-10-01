---
title: Chapitre 35 — Faux comptes, bots et comportements coordonnés
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 35.1 L'industrialisation de l'inauthenticité

L'inauthenticité numérique s'est industrialisée. Bots, fermes de comptes, IA-generated content, services de désinformation à louer composent un marché mature. L'analyste OSINT doit savoir détecter ces phénomènes, parce qu'ils :

- Polluent l'enquête (faux signaux).
- Constituent eux-mêmes l'objet d'enquête (campagnes d'influence).
- Manipulent l'écosystème observable.

## 35.2 Typologies d'inauthenticité

**Astroturfing.** Création de l'illusion d'un soutien populaire via faux comptes coordonnés.

**Bots automatiques.** Programmes qui publient/interagissent sans humain.

**Cyborgs.** Humains qui pilotent plusieurs comptes en parallèle, parfois avec assistance bot.

**Trolling coordonné.** Groupes humains qui attaquent une cible.

**Sock puppets.** Comptes opérés par un individu pour plusieurs identités (Ch.11 — cadre légitime ou frauduleux selon usage).

**Fermes de comptes.** Industries (Macédoine, Indonésie, Russie) qui créent et opèrent des milliers de faux comptes.

**Coordinated Inauthentic Behavior (CIB).** Terme Meta. Activités coordonnées simulant des opinions ou réactions organiques. Concept central.

## 35.3 Signaux de bot automatique

- Cadence anormale (poste toutes les 15 secondes).
- Activité 24/7 sans pauses humaines.
- Volume disproportionné (1000 posts/jour).
- Contenus dupliqués ou paraphrasés.
- Pas de variation contextuelle.
- Réponses inappropriées (cohérence syntaxique mais sémantique faible).

## 35.4 Signaux de ferme de comptes

- Comptes créés en lot (timestamps de création groupés).
- Photos de profil :
  - Recyclées (recherche inversée renvoie autres comptes).
  - Volées de banques d'images.
  - **Générées par IA** (signal 2026 majeur).
- Bios génériques ou absentes.
- Followings disproportionnés (50 000 follow, 200 follower).
- Activité corrélée temporellement.

## 35.5 Signaux de Coordinated Inauthentic Behavior (CIB)

Le **CIB** combine plusieurs signaux indiquant qu'une activité apparemment organique est en fait coordonnée.

**Indicateurs.**

- **Coordination temporelle** : posts simultanés ou en cluster temporel.
- **Coordination de contenu** : narratif identique ou paraphrasé.
- **Coordination de hashtags** : usage synchronisé de hashtags spécifiques.
- **Réseau d'amplification** : retweets/likes mutuels formant clusters.
- **Origine technique commune** : VPN, infrastructure partagée.

**Outils.**

- **Hamilton 2.0** (Alliance for Securing Democracy) : monitoring Russie/Chine.
- **Information Laundromat** (Stanford Internet Observatory).
- Graphes Gephi avec algorithmes communautés.

## 35.6 Détection des photos IA (signal 2026 majeur)

Une part croissante des faux comptes utilise des photos générées par IA.

**Détection.**

- **Hive Moderation** : score AI-generated.
- **Optic AI or Not** : interface simple.
- **Sensity AI** : détection deepfakes.
- Inspection visuelle (anomalies mains, dents, asymétries).

**Implication.** Vérifier systématiquement les photos de profil suspects.

## 35.7 Méthodologie de détection de cluster

Pour une enquête sur un cluster de comptes suspects :

1. **Listing initial** : identifier 5-30 comptes suspects (cible affirmée + ramifications via mentions/retweets).
2. **Analyse de profil** : date création, follower count, ratio, photo profil (IA ?), bio.
3. **Analyse temporelle** : timestamps de posts, heatmaps.
4. **Analyse de contenu** : narratifs, mots-clés, hashtags.
5. **Analyse de réseau** : graphe d'interactions, communautés (Gephi).
6. **Signatures techniques** : si accès (peu probable hors LEA) : IPs, user-agents.
7. **Synthèse** : ces comptes sont-ils coordonnés ? Probabilité ? Attribution probable ?

## 35.8 Attribution prudente

L'**attribution** d'une campagne CIB à un acteur est délicate.

**Niveaux d'attribution.**

- **Origine probable** (analyse linguistique, fuseaux horaires, narratifs idéologiques).
- **Infrastructure technique** (IPs, domaines, hostings).
- **Mode opératoire** (TTP comparables à campagnes connues).
- **Aveu** ou **leak** (rare).

L'attribution étatique (« cette campagne est russe / chinoise ») demande des éléments solides. Sans eux, formuler : « narratifs et patterns compatibles avec des opérations d'influence pro-X », pas « campagne menée par les services X ».

## 35.9 Cas de référence

**Internet Research Agency (IRA, Russie).** Ferme de trolls Saint-Pétersbourg. Active 2014-2024. Documentée par Stanford, Mueller Report, Graphika.

**Doppelgänger (Russie).** Campagne de faux médias imitant Le Monde, Bild, etc., diffusée via X et Telegram. Documentée par VIGINUM (rapport 2024).

**Spamouflage (Chine).** Campagnes pro-PRC sur X, YouTube, Facebook. Volume massif. Documentée par Graphika.

**Indian Chronicles (EU DisinfoLab, 2019-2020).** 750+ faux médias en 116 pays orchestrés depuis l'Inde.

## 35.10 Cadre légal et institutionnel France

**VIGINUM** (SGDSN) est l'acteur français de référence sur la détection et caractérisation des « phénomènes inauthentiques ». Le **DSA** européen impose des obligations aux plateformes (rapports, accès chercheurs).

## 35.11 Synthèse — boîte à outils détection CIB

| Outil | Usage |
|---|---|
| Gephi + algorithmes communautés | Analyse de réseau |
| Hamilton 2.0 | Monitoring Russie/Chine |
| Hive Moderation | Détection photos IA |
| Sensity AI | Détection deepfakes |
| Information Laundromat | Cross-référencement narratifs |
| EU DisinfoLab méthodologie | Cas studies de référence |
| Maltego | Pivots multi-plateformes |
| API X/Bluesky/Mastodon | Collection de données |
| LLMs (avec validation) | Analyse de patterns linguistiques |

L'expertise CIB est devenue une spécialité OSINT en soi. Pour les cas avancés (campagnes étatiques massives), partenariat avec acteurs spécialisés (Bellingcat, EU DisinfoLab, Graphika) ou agences (VIGINUM).

-----
