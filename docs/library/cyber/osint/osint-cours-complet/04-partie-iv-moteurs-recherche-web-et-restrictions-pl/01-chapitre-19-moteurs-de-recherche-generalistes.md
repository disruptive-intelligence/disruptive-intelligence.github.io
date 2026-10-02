---
title: Chapitre 19 — Moteurs de recherche généralistes
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 19.1 Pourquoi Google ne suffit pas

Google reste le premier réflexe, mais sa dégradation 2024-2026 est documentée : résultats personnalisés (bulle de filtrage), suppression de l'opérateur `+`, dépréciation de `intitle:` et `inurl:` en effet, focus sur la « pertinence commerciale » au détriment de l'exhaustivité, dégradation du cache. L'analyste OSINT qui utilise uniquement Google rate une part significative de l'information accessible.

La règle 2026 : **multi-moteurs systématique**. Toute recherche significative doit être conduite sur au moins 2-3 moteurs complémentaires.

## 19.2 Google : usage raisonné

Malgré sa dégradation, Google reste utile pour :

- Recherches en anglais et langues majeures.
- Indexation rapide de contenus récents.
- Recherche de fichiers (`filetype:`).
- Recherche site-spécifique (`site:`).
- Image search (Google Lens reste compétitif).

**Recommandations.**

- Naviguer **déconnecté** d'un compte Google personnel (profil dédié ou navigation privée).
- Désactiver la personnalisation (paramètres avancés, `&pws=0` dans l'URL).
- Utiliser Google avec VPN pour éviter biais géographique.
- Limiter à `&num=100` pour voir plus de résultats par page.

## 19.3 Bing : alternative crédible

**Bing** (Microsoft) a fortement progressé depuis 2023, notamment via l'intégration GPT (Copilot). Ses opérateurs sont robustes et certains spécifiques (`contains:`, `linkfromdomain:`).

**Avantages OSINT.**

- Indexation parfois différente de Google (sites manqués par Google peuvent apparaître).
- Image search compétitif (Bing Visual Search).
- Reverse image search dédié.
- API plus accessible que Google.

## 19.4 Yandex : irremplaçable

**Yandex** (russe) est l'un des outils les plus précieux de l'OSINT contemporain, **pour deux raisons** distinctes :

**Reverse image search supérieur.** Yandex Images est régulièrement classé comme le meilleur moteur de recherche inversée pour visages, scènes, objets. Il indexe différemment et identifie des sources que Google et TinEye manquent.

**Contenus russophones et CEI.** Pour toute investigation touchant la Russie, l'Ukraine, la Biélorussie, l'Asie centrale, Yandex est incontournable.

**Précaution.** Yandex est un service russe. Vos requêtes sont visibles depuis la Russie. Pour usage OSINT sensible, utiliser via VPN et compte d'investigation séparé.

## 19.5 Baidu : la Chine

**Baidu** est le moteur dominant en Chine. Indispensable pour :

- Recherches sur le web chinois (sites .cn, blogs domestiques).
- Recherche d'entités chinoises (sociétés, personnes, événements).
- Comprendre la version « domestique » d'un sujet international.

**Précautions.**

- Censure massive sur sujets politiques sensibles.
- Vos requêtes peuvent être loguées par les autorités chinoises.
- Interface en mandarin (utiliser DeepL ou Google Translate).
- Préférer accès via VPN japonais/coréen pour cohérence linguistique.

## 19.6 DuckDuckGo, Brave Search, Mojeek, Marginalia

Moteurs alternatifs orientés privacy ou indexation indépendante.

**DuckDuckGo.** Pas de tracking, résultats Bing + sources indépendantes. Utile pour comparer rapidement avec Google sans empreinte.

**Brave Search.** Index indépendant (depuis 2023). Croissance rapide. Discovery panel intéressant.

**Mojeek.** Index totalement indépendant (UK). Petit mais authentique — pas une syndication. Utile pour découvrir des sites non bien indexés par les majors.

**Marginalia.** Moteur expérimental pour le « web non-commercial » (blogs, wikis, sites personnels). Excellent pour échapper au SEO industriel.

## 19.7 Recherche multilingue

Toute investigation internationale doit considérer les langues locales.

**Stratégies.**

- Traduire les requêtes dans la langue de la juridiction (DeepL, Google Translate).
- Utiliser le moteur local (Yandex pour russe, Baidu pour chinois, Naver pour coréen, Yahoo Japan pour japonais).
- Indexation par caractères natifs (penser à utiliser cyrillique, arabe, japonais en script natif quand pertinent).
- Translittération inversée pour noms propres (un même nom russe peut s'écrire de plusieurs manières en latin).

**Outils.**

- **Google Translate** : large couverture, qualité moyenne.
- **DeepL** : qualité supérieure pour langues européennes.
- **OpenAI/Claude/Gemini** : pour traductions contextuelles.
- **ChatGPT/Claude pour translittération** : noms russes, chinois, arabes.

## 19.8 Synthèse — choisir son moteur

| Contexte | Moteur(s) recommandé(s) |
|---|---|
| Recherche générale anglais/français | Google + Bing + DuckDuckGo |
| Reverse image search | Yandex (en premier) + Google Lens + TinEye |
| Contenu russe / CEI | Yandex + recherche cyrillique |
| Contenu chinois | Baidu + traduction |
| Échapper au SEO commercial | Marginalia + Mojeek |
| Privacy-friendly | DuckDuckGo + Brave Search |
| Académique | Google Scholar + Semantic Scholar + Connected Papers |
| Documents PDF | Google `filetype:pdf` + Bing `contains:pdf` |

-----
