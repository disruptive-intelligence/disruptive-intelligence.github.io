---
title: Chapitre 22 — IA-search et moteurs conversationnels
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 22.1 L'irruption des IA-search

Entre 2023 et 2026, une nouvelle génération de « moteurs conversationnels » a émergé : **Perplexity**, **Phind**, **You.com**, **Brave AI summaries**, et les fonctions search intégrées dans **ChatGPT**, **Claude**, **Gemini**. Ces outils combinent recherche web et synthèse LLM.

Pour l'analyste OSINT, ils sont à la fois utiles et dangereux. Utiles parce qu'ils permettent de naviguer rapidement dans un domaine inconnu, d'obtenir une synthèse, de formuler des questions complexes. Dangereux parce qu'ils hallucinent, citent mal, et créent une fausse impression de complétude.

## 22.2 Perplexity

**Perplexity** (perplexity.ai) est le leader actuel des moteurs conversationnels.

**Avantages.**

- Synthèses avec citations sources (cliquables).
- Mode « Focus » (académique, Reddit, YouTube).
- Mode « Pro Search » plus profond.
- Suit l'actualité en continu.

**Limites.**

- Hallucinations résiduelles (citation correcte d'une affirmation incorrecte).
- Sources parfois faibles (Reddit, blogs SEO).
- Profondeur variable.
- Pas un substitut à la recherche directe.

## 22.3 Phind

**Phind** (phind.com) est orienté développeurs (code, doc technique) mais utile pour OSINT technique.

**Cas d'usage OSINT.**

- Comprendre une technologie inconnue.
- Trouver de la documentation sur un outil.
- Synthèse d'articles techniques.

## 22.4 You.com et Brave AI

**You.com** propose plusieurs modes (default, smart, research). Intégration multimodale (image, code).

**Brave AI Summaries** intègre des résumés AI dans les résultats Brave Search.

## 22.5 ChatGPT, Claude, Gemini en mode search

Les grands LLMs proposent désormais des modes search intégrés.

**ChatGPT (OpenAI).** Browse with Bing intégré, mode search dédié.

**Claude (Anthropic).** Web search intégré dans claude.ai (selon plan).

**Gemini (Google).** Intégration Google Search native.

**Pour OSINT.**

- Utiles pour reformulation, synthèse, hypothèses de travail.
- **Jamais** comme source primaire.
- Vérifier chaque affirmation contre la source originale.

## 22.6 Risque d'hallucination en contexte OSINT

L'hallucination est le risque central. Un LLM peut **inventer** :

- Une affirmation qu'aucune source ne soutient.
- Une citation d'une source qui n'existe pas.
- Une URL plausible mais inexistante.
- Un fait correctement attribué mais en réalité faux.
- Des chiffres précis mais fantaisistes.

**Pour un analyste OSINT, l'hallucination est catastrophique** : elle peut entraîner un rapport erroné, une action injuste, une compromission de crédibilité.

## 22.7 Vérification systématique

Toute affirmation produite par un moteur conversationnel doit être **vérifiée contre la source primaire**.

**Protocole.**

1. Le moteur affirme « X selon source Y ».
2. Aller vérifier directement source Y.
3. La source Y contient-elle l'affirmation X ?
4. Si oui, la source Y est-elle fiable (cotation Admiralty) ?
5. Si non (= hallucination), discarder.
6. Si pas de source Y citée, discarder par défaut.

C'est lent. C'est la condition pour utiliser ces outils.

## 22.8 Ne jamais citer un LLM comme source

**Règle absolue.** Un livrable OSINT **ne cite jamais** « selon ChatGPT », « d'après Perplexity ». La source citée est toujours la **source primaire** que le LLM a (peut-être) trouvée.

Cette règle évite les ridicules judiciaires et professionnels. Un rapport qui cite un LLM comme source est invalidé d'office.

## 22.9 Usages légitimes de l'IA-search en OSINT

Malgré ces réserves, les IA-search ont des **usages utiles**.

**Reformulation.** Vous avez une intuition vague, l'IA aide à la formuler en questions précises.

**Cartographie d'un domaine inconnu.** Avant d'investiguer une industrie ou un sujet technique inconnu, l'IA fournit une vue d'ensemble (à vérifier mais utile pour s'orienter).

**Identification de sources.** L'IA suggère des sources que vous ne connaissiez pas. Vous allez ensuite directement à ces sources.

**Synthèse de corpus déjà connus.** Vous donnez à l'IA un corpus que vous avez vérifié, elle produit une synthèse (encore à relire).

**Traduction et transposition culturelle.** Comprendre des sources en langue ou contexte culturel inconnu.

## 22.10 Protocole Retrieve-Store-Cite (anticipation Ch.63)

Le protocole **Retrieve-Store-Cite** (Ch.63 développe) opérationnalise l'usage de l'IA en OSINT.

1. **Retrieve.** L'IA récupère des éléments candidats.
2. **Store.** Vous stockez ces éléments avec leur source originale.
3. **Cite.** Dans le livrable, vous citez **la source originale**, pas l'IA.

Cette discipline rend l'IA utilisable sans compromettre la rigueur.

## 22.11 Synthèse — usage 2026 des IA-search

| Usage | Recommandation |
|---|---|
| Question rapide hors enquête | OK |
| Cartographie domaine inconnu | OK, à vérifier |
| Reformulation de questions | OK |
| Suggestion de sources à consulter | OK, vérification ensuite |
| Source primaire dans un livrable | **JAMAIS** |
| Synthèse de corpus déjà vérifié | OK, relire |
| Action sur la base d'affirmation IA non vérifiée | **JAMAIS** |
| Vérification rapide d'un fait | À vérifier en source primaire |

> **Principe directeur.** L'IA-search est un raccourci, pas un oracle. Elle accélère votre recherche, elle ne se substitue pas à votre rigueur.

-----
