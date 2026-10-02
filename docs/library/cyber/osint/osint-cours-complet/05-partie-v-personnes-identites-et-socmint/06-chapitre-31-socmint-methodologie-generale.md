---
title: 'Chapitre 31 — SOCMINT : méthodologie générale'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 31.1 Le SOCMINT comme volume principal

Le **SOCMINT** (Social Media Intelligence) est devenu, en volume, l'une des composantes principales de l'OSINT contemporaine. Les personnes publient massivement leur vie en ligne ; les organisations criminelles utilisent les réseaux comme plateformes opérationnelles ; les opérations d'influence s'y déploient ; la fraude s'y prépare.

Mais le SOCMINT est aussi le domaine où les **restrictions 2024-2026** frappent le plus durement (Ch.24). L'analyste doit conjuguer méthodologie rigoureuse et adaptation aux contraintes.

## 31.2 Cycle SOCMINT

Le cycle SOCMINT spécifique :

1. **Cadrage** : quel objectif sur quelle cible ?
2. **Identification de comptes** : quels comptes appartiennent à la cible ?
3. **Maturation OPSEC** : avatars matures, archivage anticipé.
4. **Collecte** : captures, exports API, scraping résilient.
5. **Analyse de réseau** : qui suit qui, qui parle à qui, clusters.
6. **Analyse temporelle** : cadence, événements, corrélations.
7. **Analyse de contenu** : sujets, narratifs, signaux.
8. **Vérification** : authenticité, attribution.
9. **Cotation et formulation.**

## 31.3 Identification de comptes

L'identification des comptes appartenant à une cible mobilise :

- Username search (Sherlock, WhatsMyName) — Ch.27.
- Email pivot (Holehe, Epieos) — Ch.27.
- Téléphone pivot (Telegram, WhatsApp).
- Photo pivot (recherche inversée) — Ch.30.
- Recherche presse (mentions de comptes).
- Cross-promotion (un compte mentionne l'autre).
- Mentions par tiers connus.

## 31.4 Analyse de réseau social

Une fois les comptes identifiés, l'analyse de réseau révèle structures et dynamiques.

**Notions.**

- **Nœud** : compte / personne.
- **Arête** : lien (follow, mention, reply, retweet, like).
- **Degree centrality** : nombre de connexions.
- **Betweenness centrality** : à quel point un nœud relie des sous-graphes.
- **Communautés** : groupes densément connectés (algorithmes Louvain, modularité).
- **Influencers** : nœuds à forte centralité.

**Outils.**

- **Gephi** (open source). Standard académique.
- **Maltego** (commercial). Standard professionnel.
- **NetworkX** (Python). Pour pipelines reproductibles.
- **Cytoscape**.

**Cas d'usage MIRAGE.** Le cluster de 8 faux comptes X coordonnés amplifiant la diffamation contre Berthier sera analysé en graphe : qui retweete qui, quelles sont les communautés, qui est le nœud central.

## 31.5 Analyse temporelle

**Indicateurs temporels.**

- Cadence de publication (postes / jour, / heure).
- Heures et jours actifs (heatmap).
- Délai de réponse / retweet.
- Synchronisations suspectes (plusieurs comptes publient simultanément).
- Périodes d'inactivité corrélées.

**Outil simple.** Pandas + matplotlib pour visualiser timestamps.

## 31.6 Analyse de contenu

**Dimensions.**

- **Topics** : sujets récurrents (TF-IDF, topic modeling).
- **Sentiment** : tonalité (positif, négatif, agressif).
- **Langue** : maîtrise et niveau.
- **Style** : voir Ch.28 (stylométrie).
- **Visuels** : images partagées, leur origine, leur authenticité.

**Outils.**

- LLMs (Claude, GPT) pour analyse rapide de corpus (avec vérification).
- **VADER**, **TextBlob** pour analyse de sentiment.
- **BERTopic** pour topic modeling.

## 31.7 Behavioral fingerprinting

Le **behavioral fingerprinting** combine plusieurs signaux pour caractériser le « comportement » d'un compte.

**Signaux.**

- Cadence (Ch.28).
- Heures d'activité.
- Lexique.
- Émojis.
- Types de contenu (photos perso, retweets, articles).
- Cercle social.
- Sujets.

**Cas d'usage.**

- Distinguer compte humain vs bot.
- Identifier un opérateur unique derrière plusieurs comptes.
- Détecter un changement d'opérateur (compte revendu, compromis).

## 31.8 Influence et amplification

L'**analyse d'influence** mesure :

- **Reach** : combien de personnes voient les contenus.
- **Engagement** : ratio interactions / followers.
- **Amplification** : qui retweete / partage.
- **Pivots de viralité** : nœuds qui propulsent un contenu.

**Outils.**

- **Brandwatch**, **Talkwalker**, **Meltwater** (commerciaux haut de gamme).
- **NodeXL** (Excel, gratuit).
- Calculs manuels via API ou scraping.

## 31.9 Détection d'inauthenticité

Le SOCMINT mature consacre une attention spécifique à la **détection des faux comptes et comportements coordonnés** (CIB — Coordinated Inauthentic Behavior). Voir Ch.35.

## 31.10 Limites du SOCMINT

- **Bulle observable.** On ne voit que ce qui est public. Tout ce qui est privé échappe.
- **Réseaux fragmentés.** Pas une plateforme = une vue complète.
- **Manipulation.** Les comptes peuvent être faux, manipulés, vendus.
- **Inauthenticité industrielle.** Bots, fermes de comptes, IA-generated.
- **Restrictions API.** Volume limité (Ch.24).

> **Principe.** Le SOCMINT révèle une **représentation publique** de la cible, pas sa réalité complète. La cotation doit en tenir compte.

-----
