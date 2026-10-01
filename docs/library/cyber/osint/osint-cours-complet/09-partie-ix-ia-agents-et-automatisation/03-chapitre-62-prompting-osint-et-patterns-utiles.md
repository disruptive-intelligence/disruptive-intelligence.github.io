---
title: Chapitre 62 — Prompting OSINT et patterns utiles
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 62.1 Le prompting comme compétence

Bien interroger un LLM est une compétence. Elle se développe. Pour OSINT, certains **patterns de prompts** sont particulièrement utiles.

## 62.2 Principes de base

**Clarté.** Préciser le rôle, la tâche, le format de sortie, les contraintes.

**Exemples (few-shot).** Montrer 1-2 exemples souvent améliore.

**Contraintes explicites.** « Ne pas inventer », « Si tu ne sais pas, dis-le », « Cite tes sources ».

**Format structuré.** JSON, tableaux, listes. Plus exploitable.

**Décomposition.** Tâches complexes en sous-tâches.

## 62.3 Pattern : prompt de cadrage

**Objectif.** Formuler une mission.

```
Tu es un analyste OSINT senior. Voici un mandat reçu : [description].
Aide-moi à :
1. Reformuler en 3-5 questions de renseignement (fermées, vérifiables).
2. Identifier les sélecteurs initiaux disponibles.
3. Lister 5-8 sources prioritaires à explorer.
4. Identifier les risques juridiques / éthiques.
5. Proposer un plan de collecte sur 2 semaines.

Format : tableau structuré.
```


## 62.4 Pattern : prompt de tri

**Objectif.** Filtrer un corpus.

```
Pour chacun des 200 résultats suivants, indique :
- Pertinent (oui/non) pour la question : [question]
- Catégorie (presse / réseau social / blog / officiel / autre)
- Cotation préliminaire Admiralty (A-F / 1-6)
- Justification (1 phrase)

Résultats : [...]

Sortie : CSV.
```


## 62.5 Pattern : prompt d'extraction structurée

**Objectif.** Extraire entités d'un texte.

```
Voici un document. Extrais en JSON :
{
  "personnes": [
    {"nom": "...", "fonction": "...", "occurrence_page": ...}
  ],
  "sociétés": [
    {"raison_sociale": "...", "juridiction": "...", "rôle": "..."}
  ],
  "montants": [
    {"valeur": "...", "devise": "...", "contexte": "..."}
  ],
  "dates": [
    {"date": "YYYY-MM-DD", "événement": "..."}
  ],
  "domaines": [...],
  "emails": [...]
}

Si une information n'est pas dans le texte, ne pas l'inventer. Mettre liste vide.

Document : [...]
```


## 62.6 Pattern : prompt de vérification

**Objectif.** Tester la cohérence d'une affirmation.

```
Affirmation : [affirmation à vérifier].

1. Quelles évidences sont nécessaires pour confirmer cette affirmation ?
2. Quelles évidences pourraient la réfuter ?
3. Quelles hypothèses alternatives expliqueraient les mêmes faits ?
4. Quelle cotation Admiralty recommanderais-tu pour cette affirmation, et pourquoi ?
```


## 62.7 Pattern : prompt de rédaction

**Objectif.** Aide à la rédaction d'un livrable.

```
Tu es un analyste senior rédigeant un rapport OSINT.
Style : sobre, calibré, sans verdict, vocabulaire WEP.
Voici les faits cotés à intégrer : [...]
Voici les hypothèses retenues : [...]
Voici les limites identifiées : [...]

Produis :
- Executive summary (3 paragraphes, BLUF).
- Section faits clés (5-7 faits avec cotation).
- Section hypothèses et niveau de confiance.
- Section limites de l'enquête.

Ne pas exprimer de certitude au-delà de ce que les sources soutiennent.
```


## 62.8 Pattern : prompt de contre-analyse

**Objectif.** Anti-biais (raisonnement adversaire).

```
Voici les conclusions actuelles d'une enquête OSINT : [...]
Adopte le rôle de devil's advocate.
1. Quelles failles méthodologiques cette enquête présente-t-elle ?
2. Quels biais cognitifs peuvent l'avoir influencée ?
3. Quelles hypothèses alternatives n'ont peut-être pas été suffisamment testées ?
4. Quelles vérifications supplémentaires seraient critiques ?
```


## 62.9 Pattern : prompt de traduction contextuelle

**Objectif.** Traduction au-delà du littéral.

```
Voici un texte en [langue source] : [...]
Traduis en français en :
- Préservant le sens et le ton.
- Ajoutant entre crochets toute information culturelle / contextuelle nécessaire à un lecteur français.
- Notant toute expression difficilement traduisible avec justification.
- Identifiant toute référence implicite (personnages, événements, expressions idiomatiques).
```


## 62.10 Pattern : prompt comparatif

**Objectif.** Comparer plusieurs sources.

```
Voici N versions d'un même fait, rapportées par sources différentes : [...]
1. Identifie les points convergents.
2. Identifie les contradictions.
3. Pour chaque contradiction, propose une hypothèse explicative.
4. Quelle source semble la plus fiable, et pourquoi ?
5. Quelle synthèse retenir avec quel niveau de confiance ?
```


## 62.11 Bibliothèque de prompts d'analyste

L'analyste mature constitue sa propre **bibliothèque de prompts** (templates). Versionnable, partageable en équipe, améliorée au fil des usages.

**Format type.** Fichier markdown par catégorie (cadrage, tri, extraction, vérification, rédaction, etc.) avec exemples d'usage et résultats attendus.

## 62.12 Anti-pattern à éviter

**Question ouverte sans contexte.** « Que penses-tu de Delaunay ? » → hallucination probable.

**Pas de contraintes.** Pas de « ne pas inventer », pas de format → sortie variable.

**Confiance aveugle.** Accepter sortie sans vérification.

**Surcharge.** 50 instructions dans un prompt → l'IA en oublie.

**Pas de validation.** Ne jamais re-tester la même question avec une formulation différente.

-----
