---
title: Chapitre 63 — Protocole Retrieve-Store-Cite
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 63.1 Le protocole opérationnel

Le **protocole Retrieve-Store-Cite** est la formalisation de l'usage rigoureux des LLMs en OSINT. Il garantit que toute information utilisée dans un livrable est traçable à une source primaire vérifiable, et non pas à une hallucination LLM.

**Trois étapes.**

**Retrieve.** Le LLM récupère ou identifie des éléments candidats (faits, sources, hypothèses).

**Store.** L'analyste stocke ces éléments avec leur source originale.

**Cite.** Dans le livrable, la source citée est la **source originale**, jamais le LLM.

## 63.2 Pourquoi ce protocole

**Risque sans protocole.**

- LLM affirme « X selon source Y ».
- Source Y n'existe pas (hallucination).
- Analyste cite « X » dans le rapport.
- Rapport contient une fausse affirmation invérifiable.
- Carrière compromise, dossier invalidé.

**Protection avec protocole.**

- LLM affirme « X selon source Y ».
- Analyste va vérifier source Y.
- Si source Y existe et contient X : Store, Cite source Y.
- Si source Y n'existe pas : ne pas utiliser.
- Toute citation est traçable à une source vérifiée.

## 63.3 Mise en œuvre pratique

**Étape Retrieve.**

- Utilisation du LLM (Claude, GPT, Gemini, Perplexity) pour extraire / suggérer.
- Sortie : éléments avec source supposée.

**Étape Store.**

- Pour chaque élément retenu :
  - Vérifier la source en cliquant / consultant directement.
  - Capturer la source (Hunchly, SingleFile).
  - Enregistrer dans le journal d'enquête (Ch.15).
  - Coter Admiralty (Ch.84).

**Étape Cite.**

- Dans le rapport, citer la source originale.
- **Jamais** « selon ChatGPT », « d'après Claude ».
- Référence à la capture archivée.

## 63.4 Exemple concret

**Sans protocole (dangereux).**

- Analyste demande à Claude : « Marc Delaunay est-il administrateur de sociétés à l'étranger ? »
- Claude répond : « Selon le Companies Registry de Malte, Marc Delaunay est administrateur de Delta Consulting Ltd depuis mars 2020. »
- Analyste cite dans le rapport : « Marc Delaunay est administrateur de Delta Consulting Ltd à Malte (Source : Companies Registry Malte). »

**Risque.** Claude a peut-être halluciné. Le Companies Registry Malte n'enregistre peut-être pas Delaunay.

**Avec protocole.**

- Analyste demande à Claude (Retrieve).
- Claude suggère l'information avec source.
- **Analyste va directement** sur le Companies Registry de Malte.
- Recherche « Delaunay » ou « Delta Consulting ».
- **Si trouvé** : capture la page, hash, journal. Cotation A1. (Store)
- **Cite** dans le rapport la page Companies Registry directement, avec capture archivée. (Cite)
- **Si non trouvé** : ne pas utiliser. Investiguer pourquoi Claude a affirmé.

## 63.5 Tracer le LLM dans la méthodologie

**Bonne pratique.** Mentionner l'usage du LLM dans la **méthodologie** du rapport.

**Exemple.**

> « Méthodologie : la collecte initiale a été assistée par LLMs (Claude, ChatGPT) pour extraction d'entités sur les corpus presse et registres publics. Chaque fait restitué dans ce rapport a fait l'objet d'une vérification directe sur la source primaire (URL, hash, et capture archivée référencés en annexe). Aucune affirmation n'est citée sur la seule base d'une production LLM. »

## 63.6 Garde-fous techniques

**RAG (Retrieval Augmented Generation).** Architecture qui force le LLM à citer des sources réelles fournies en contexte. Réduit (sans éliminer) les hallucinations.

**Outils RAG OSINT.**

- **Perplexity** : moteur conversationnel avec sources.
- **OpenAI assistants avec retrieval**.
- **Notebook LM** (Google) : on fournit les sources, le LLM répond avec citations.
- **Self-hosted RAG** : LangChain, LlamaIndex avec vector DB locale.

## 63.7 Limites du protocole

**Ne supprime pas les hallucinations.** Le LLM peut citer la bonne source mais affirmer ce qu'elle ne contient pas. Vérification reste obligatoire.

**Coûteux en temps.** Vérifier chaque sortie LLM prend du temps. Mais c'est le prix de la rigueur.

**Adoption.** Doit devenir un réflexe. La tentation de zapper est forte sous pression de délais.

## 63.8 Application aux différentes sources

**Sortie de Perplexity, ChatGPT search.** Cliquer chaque source citée. Vérifier que ce que le LLM affirme est dans la source.

**Sortie résumé.** Vérifier les faits clés contre le corpus d'origine.

**Sortie traduction.** Échantillonner. Pour pièces critiques, traducteur humain.

**Sortie identification.** Toujours corroborer par recherche directe.

## 63.9 Cas particuliers

**LLM admet ne pas savoir.** Bon signal. Continuer à investiguer sans pression.

**LLM hallucine en cas particulier.** Investigation pour comprendre pourquoi. Ne pas reproduire le pattern.

**LLM cohérent et confident, mais hallucine.** Cas le plus dangereux. La rigueur de vérification est seule défense.

## 63.10 Synthèse — règle d'or

> **Aucune affirmation produite par un LLM n'entre dans un livrable sans avoir été vérifiée contre sa source primaire. Sans exception.**

C'est le **protocole Retrieve-Store-Cite**. C'est ce qui rend l'IA utilisable en OSINT sans compromettre la rigueur.

-----
