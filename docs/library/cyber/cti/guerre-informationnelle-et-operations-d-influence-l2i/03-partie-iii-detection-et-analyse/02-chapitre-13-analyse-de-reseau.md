---
title: Chapitre 13 — Analyse de réseau
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence (L2I).md
note: Guerre informationnelle et opérations d'influence (L2I)
up:
- - Guerre informationnelle et opérations d'influence (L2I)
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

cartographier les opérations coordonnées

## 13.1 Social Network Analysis appliquée aux opérations d'influence

L'analyse de réseau social (SNA — *Social Network Analysis*) est la méthode clé pour cartographier les opérations coordonnées. Elle consiste à construire un graphe d'interactions (qui retweet qui, qui partage les mêmes URLs, qui mentionne qui, qui suit qui) et à analyser sa structure pour identifier des clusters de coordination.

Les métriques classiques de la SNA sont directement exploitables : la **centralité** (quels comptes sont au centre du réseau de diffusion — les amplificateurs clés), la **densité** (un réseau inauthentique est typiquement plus dense qu'un réseau organique — les faux comptes interagissent davantage entre eux), les **communautés** (identification de clusters de comptes qui interagissent préférentiellement entre eux — technique de Louvain, Leiden), et les **bridges** (comptes qui relient le réseau inauthentique à des communautés authentiques — les points de passage du fringe au mainstream).

Dans le cadre d'une opération d'influence, l'analyse de réseau vise à répondre à trois questions : le réseau présente-t-il des caractéristiques de coordination inauthentique (synchronicité, densité, homogénéité) ? Quel est le noyau central (les comptes « amplificateurs » qui structurent la diffusion) ? Quels sont les points de contact avec les communautés organiques (les « bridges » par lesquels le narratif pénètre le débat authentique) ?

## 13.2 Analyse temporelle

L'analyse temporelle est souvent le marqueur le plus discriminant. La détection de synchronicité — publications à quelques minutes d'intervalle dans des fenêtres anormalement serrées — est un indicateur fort de coordination. L'analyse des horaires d'activité peut révéler des incohérences avec le fuseau horaire affiché (un réseau de comptes prétendument français publiant aux horaires de bureau de Moscou). Les pics de volume coordonnés, superposés à la timeline des événements, permettent de reconstituer le cycle opérationnel de l'opération.

## 13.3 Analyse d'infrastructure

L'analyse technique des URLs partagées et des domaines associés mobilise les mêmes techniques que l'OSINT technique classique. L'analyse Whois (historique et actuelle), le reverse IP, les certificats SSL, l'analyse de l'hébergeur, les records DNS, et l'analyse des patterns d'enregistrement (même registrar, mêmes données de contact, même serveur) permettent d'identifier l'infrastructure sous-jacente.

Le rapport VIGINUM sur Storm-1516 illustre cette approche : les opérateurs de CopyCop utilisent des services d'anonymisation de Cloudflare, des hébergeurs peu discriminants, et des templates WordPress quasi systématiquement différents pour gêner la détection. Malgré ces précautions, l'analyse d'infrastructure a permis d'identifier des liens entre les différents sites du réseau.

La doctrine OpenCTI de VIGINUM documente l'utilisation d'observables spécifiques (adresses email, adresses IP, médias, URLs, noms de domaine) pour tracer l'infrastructure des opérations informationnelles et les relier à des acteurs identifiés.

## 13.4 Outils

Le paysage d'outils pour l'analyse de réseau a significativement évolué entre 2023 et 2026, principalement du fait des restrictions d'accès aux données des plateformes.

**Gephi** reste la référence open source pour la visualisation et l'analyse de graphes — gratuit, puissant, mais avec une courbe d'apprentissage significative et des limites de performance sur les très grands graphes. **NodeXL** (Microsoft Excel plugin) est adapté pour des analyses de taille modérée avec une interface plus accessible. **Graphistry** offre des capacités de visualisation GPU-accelerée pour les graphes massifs. **Maltego** est utilisé pour l'enrichissement et la visualisation des données d'investigation.

**CrowdTangle**, l'outil de Meta pour le suivi de la diffusion sur Facebook et Instagram, a été fermé en août 2024 et remplacé par la **Meta Content Library** — dont l'accès est restreint aux chercheurs qualifiés et dont les fonctionnalités sont plus limitées. Cette fermeture a significativement dégradé les capacités de monitoring pour l'ensemble de la communauté.

**Botometer** (Indiana University) évalue la probabilité qu'un compte Twitter/X soit un bot — mais ses performances sont connues pour être limitées (taux de faux positifs et faux négatifs significatifs) et il ne doit jamais être utilisé comme verdict autonome.

Les **APIs des plateformes** sont de plus en plus restreintes. L'API de X (ex-Twitter) est devenue payante et coûteuse depuis 2023, ce qui a sévèrement limité les capacités de recherche académique et opérationnelle. Le DSA impose un accès aux données pour les chercheurs agréés, mais la mise en œuvre effective reste lente et difficile.

## 13.5 Visualisation et restitution

La présentation des résultats d'analyse de réseau à un décideur non technique est un enjeu opérationnel majeur. Un graphe de réseau brut est incompréhensible pour un non-spécialiste. La restitution doit inclure : un graphe simplifié et annoté (avec les clusters identifiés, les nœuds centraux étiquetés, les connexions clés mises en évidence), une description narrative du réseau (taille, structure, comportements caractéristiques), les indicateurs quantitatifs clés (nombre de comptes, volume de publications, engagement total, fenêtres temporelles), et les conclusions avec niveaux de confiance.

> **🔵 BROUILLARD — Épisode 5**
> La cartographie du réseau est complète. Élise et son équipe ont reconstitué un graphe de relations impliquant plus de 200 comptes X, 50 comptes Facebook, 12 canaux Telegram, 3 sites web de réinformation et une newsletter. L'analyse de réseau identifie un cluster central de 30 comptes « amplificateurs » qui structurent la diffusion — ces comptes sont les premiers à partager les contenus publiés sur les sites de réinformation et les canaux Telegram, et les autres comptes du réseau les retweet dans des fenêtres de 5 à 15 minutes. L'analyse temporelle confirme la coordination : les pics d'activité sont systématiquement synchronisés, avec des horaires d'activité concentrés entre 8h et 17h UTC+3 (Moscou). L'infrastructure des trois sites web est tracée via Whois et reverse IP. Le rapport visuel — graphe annoté, timeline, tableau d'indicateurs — est préparé pour le briefing hebdomadaire.

---
