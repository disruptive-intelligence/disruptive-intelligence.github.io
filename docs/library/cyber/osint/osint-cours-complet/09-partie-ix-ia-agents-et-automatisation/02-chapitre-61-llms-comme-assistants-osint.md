---
title: Chapitre 61 — LLMs comme assistants OSINT
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 61.1 Les cas d'usage matures

Les LLMs sont matures pour plusieurs cas d'usage OSINT spécifiques. Ce chapitre les détaille avec méthodologie pratique.

## 61.2 Extraction d'entités

**Cas d'usage.** Un PDF de 200 pages d'un rapport financier. Extraction de toutes les sociétés, personnes, montants, dates mentionnées.

**Méthode.**

```
Prompt: 
Tu es un analyste OSINT. Voici un document. Extrais en tableau structuré :
- Sociétés mentionnées (nom, juridiction si indiquée)
- Personnes physiques (nom, fonction si indiquée)
- Montants financiers (montant, devise, contexte)
- Dates clés
- Domaines / URL mentionnés

Document : [...]

Sortie en CSV avec colonnes : type, valeur, contexte, occurrence_page.
```


**Vérification.** Toujours **échantillonner** les sorties contre le document source. L'IA peut inventer des entités ou en oublier.

## 61.3 Résumé de corpus

**Cas d'usage.** 30 articles sur une entité. Synthèse en une page.

**Méthode.**

```
Prompt:
Voici 30 articles concernant l'entité X. Produis une synthèse :
- 3-5 phrases résumant l'activité principale
- Faits clés datés
- Acteurs importants mentionnés
- Controverses / risques identifiés
- Contradictions entre sources

Ne pas inventer. Si une affirmation n'est dans aucun article, ne pas la mentionner.

Articles : [...]
```


**Vérification.** Re-lire les passages clés. Vérifier que les dates et faits cités sont dans les articles.

## 61.4 Traduction et transcription

**Traduction.** LLMs équivalents ou supérieurs à Google Translate / DeepL pour la plupart des langues majeures. Particulièrement bons pour contexte culturel.

**Transcription audio.** OpenAI Whisper (open source) reste référence. Multilingue, précis, gratuit en local.

**Méthode transcription.**

```bash
whisper audio.mp3 --model large --language fr
```


**Vérification.** Échantillonner. Pour pièces critiques, expertise humaine.

## 61.5 Classification massive

**Cas d'usage.** Tri de 10 000 tweets pour identifier ceux qui sont pertinents pour une enquête.

**Méthode.**

```
Prompt:
Pour chaque tweet, indique s'il est pertinent ou non pour une enquête sur [sujet].
Critères : [...]

Sortie : tweet_id, pertinent (oui/non), justification courte.

Tweets : [...]
```


**Mise en œuvre.** Via API batch (OpenAI, Anthropic). Coûts maîtrisables.

## 61.6 Génération de dorks

**Cas d'usage.** Générer des requêtes Google complexes pour un sujet.

**Méthode.**

```
Prompt:
Génère 15 dorks Google pour rechercher :
- Mentions d'une personne (Marc Delaunay) liée à TechnoVert
- Documents internes potentiellement exposés
- Communications publiques de la société
- Liens avec d'autres sociétés
- Etc.

Pour chaque dork, indique l'objectif visé.
```


**Vérification.** Tester les dorks générés. Certains seront inopérants ou triviaux.

## 61.7 Reformulation de questions

**Cas d'usage.** Une intuition vague. L'IA aide à la formuler en questions de renseignement précises.

**Méthode.**

```
Prompt:
J'ai cette intuition vague : « Delaunay pourrait avoir des structures offshore ».
Aide-moi à reformuler cela en 5-10 questions de renseignement opérationnelles, fermées, vérifiables.
```


**Utile.** Mais reste un brouillon à valider.

## 61.8 Analyse de patterns linguistiques

**Cas d'usage.** Comparer le style de plusieurs textes pour évaluer s'ils ont le même auteur.

**Méthode.**

```
Prompt:
Voici 5 textes. Analyse les patterns stylistiques (vocabulaire, structure, tournures, ponctuation, registre). Identifie s'il y a des similarités suggérant un auteur commun.

Pour chaque paire, donne un score de similarité (0-100) avec justification.
```


**Limite.** L'IA peut hallucinations en stylométrie. Vérification par signaux objectifs (mots récurrents, longueur phrases).

## 61.9 Aide au code et à l'automatisation

**Cas d'usage.** Script Python pour parser des résultats Sherlock.

**Méthode.** Demander à l'IA un script. **Tester systématiquement**. Le code généré est souvent imparfait, parfois erroné.

## 61.10 Génération d'hypothèses

**Cas d'usage.** L'IA suggère des hypothèses alternatives à explorer.

**Méthode.**

```
Prompt:
Voici les faits collectés sur l'entité X : [...]
Génère 5-8 hypothèses alternatives expliquant ces faits. Pour chaque hypothèse, indique quels éléments supplémentaires permettraient de la confirmer ou infirmer.
```


**Très utile** pour anti-biais. À traiter comme suggestions à tester (ACH — Ch.79).

## 61.11 Synthèse — usages matures et risqués

| Usage | Maturité 2026 | Vigilance |
|---|---|---|
| Extraction entités | Mature | Échantillonner vérification |
| Résumé corpus | Mature | Vérifier faits |
| Traduction | Très mature | OK |
| Transcription audio | Très mature (Whisper) | OK |
| Classification massive | Mature | Validation échantillon |
| Génération dorks | Mature | Tester |
| Reformulation questions | Mature | Validation humaine |
| Analyse stylométrique | Limitée | Combiner avec signaux objectifs |
| Génération hypothèses | Mature | Traiter comme suggestion |
| Code | Mature | Tester systématiquement |
| Recherche factuelle | **À risque** | Vérifier toujours |
| Attribution sans corroboration | **Évité** | Hallucinations dangereuses |

-----
