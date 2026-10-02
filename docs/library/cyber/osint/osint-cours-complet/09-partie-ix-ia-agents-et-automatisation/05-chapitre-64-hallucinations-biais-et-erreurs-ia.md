---
title: Chapitre 64 — Hallucinations, biais et erreurs IA
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 64.1 Qu'est-ce qu'une hallucination

Une **hallucination** est une affirmation produite par un LLM qui est fausse mais formulée avec autorité comme si elle était vraie. C'est le risque numéro un de l'IA en OSINT.

**Types d'hallucinations.**

- Fait inventé.
- Date erronée.
- Citation d'une source qui n'existe pas.
- URL plausible mais inexistante.
- Attribution incorrecte.
- Chiffre précis fantaisiste.
- Personne fictive présentée comme réelle.
- Événement inventé.

## 64.2 Pourquoi les LLMs hallucinent

Les LLMs prédisent le mot suivant le plus probable selon leur entraînement. Ils n'ont pas de **modèle de vérité**. Ils produisent ce qui « ressemble à » une réponse plausible.

**Conséquence.** Lorsque l'information demandée est rare, dépassée, ou hors corpus d'entraînement, le LLM **fabule** plutôt que d'admettre l'ignorance. Et cette fabulation est typiquement convaincante.

## 64.3 Domaines à haut risque d'hallucination

**Personnes peu connues.** Noms hors top 10 000 références. Le LLM va inventer biographies, parcours, événements.

**Événements récents.** Au-delà du cutoff training. Et même avant le cutoff, les événements peu médiatisés sont mal couverts.

**Informations très spécifiques.** Dates précises, chiffres précis, références de documents.

**Citations.** Le LLM peut inventer une « citation » plausible attribuée à une personnalité.

**Sources.** URLs, articles, papers — souvent inventés.

**Langues moins représentées.** Hallucinations plus fréquentes en langues mineures.

## 64.4 Domaines à risque modéré

**Concepts généraux.** Définitions, méthodes établies. Risque modéré (mais non nul).

**Personnalités très médiatiques.** Le LLM a du contenu, risque réduit mais non nul (confusions, attributions erronées).

**Sciences établies.** Faits scientifiques bien documentés. Risque relativement faible.

## 64.5 Reconnaître une hallucination

**Signaux d'alerte.**

- Précision inhabituelle (date exacte, chiffre précis, URL spécifique) sans source vérifiable.
- Cohérence narrative trop parfaite.
- Sources citées non vérifiables.
- Détails biographiques trop riches pour une personne obscure.
- Contradiction discrète avec faits connus.

**Test.** Re-poser la même question dans une formulation différente, ou à un autre LLM. Si les réponses divergent, méfiance.

## 64.6 Biais des LLMs

Au-delà des hallucinations, biais structurels :

**Biais linguistique.** Anglais surreprésenté → meilleures performances en anglais.

**Biais culturel.** Perspectives occidentales dominantes.

**Biais temporel.** Cutoff training crée un « horizon ».

**Biais idéologique.** Selon datasets et fine-tuning, certaines perspectives sont sur-représentées.

**Biais de complaisance.** Tendance à dire ce que l'utilisateur veut entendre.

**Implication OSINT.** Toujours valider hypothèses contre sources externes. Ne pas se fier au « consensus IA ».

## 64.7 Erreurs de raisonnement

Au-delà des hallucinations factuelles, erreurs logiques :

**Sauts de logique.** Conclusion non soutenue par les prémisses.

**Confusion de catégories.** Mélange entre faits et hypothèses.

**Causalité abusive.** Inférer cause à partir de corrélation.

**Vérification.** Re-faire le raisonnement à la main pour décisions critiques.

## 64.8 Stratégies de mitigation

**1. RAG (Retrieval Augmented Generation).** Fournir sources au LLM, demander des citations. Réduit (sans éliminer).

**2. Cross-validation multi-LLMs.** Poser même question à Claude, GPT, Gemini. Divergences = signal de doute.

**3. Vérification source primaire systématique.** Le protocole Retrieve-Store-Cite (Ch.63).

**4. Demander incertitude.** « Si tu n'es pas sûr, dis-le. » Améliore (sans garantir).

**5. Prompts qui valorisent la prudence.** « Préfère dire 'je ne sais pas' à inventer. »

**6. Structurer la sortie.** JSON, tableaux. Force le LLM à être précis ou à laisser vides.

**7. Re-poser avec formulation différente.** Test de cohérence.

## 64.9 Cas particulier : sur-confiance

Les LLMs **expriment de la confiance** même quand ils hallucinent. Le ton assertif ne reflète pas la justesse. L'analyste doit dissocier **forme** (autorité du ton) et **fond** (justesse des affirmations).

**Réflexe.** Toujours appliquer la même rigueur de vérification, indépendamment du ton du LLM.

## 64.10 Sur-confiance de l'analyste

Le piège n'est pas dans le LLM, mais dans la **psychologie de l'analyste**.

**Pattern dangereux.**

- L'analyste utilise le LLM avec succès sur 50 cas faciles.
- L'analyste développe une confiance.
- Sur le 51e cas (difficile, peu de données), le LLM hallucine.
- L'analyste, en confiance, ne vérifie pas.
- Hallucination publiée.

**Défense.** Toujours vérifier, **surtout** quand on est en confiance.

## 64.11 Documentation des limites IA dans rapport

**Bonne pratique.** Le rapport mentionne explicitement les outils IA utilisés et leurs limites.

**Exemple section méthodologique.**

> « Cette enquête a mobilisé des LLMs (Claude 4, GPT-4) pour assistance en extraction d'entités, traduction et reformulation. Tous les faits et conclusions ont fait l'objet d'une vérification directe sur sources primaires. Aucune affirmation n'est issue de la seule production LLM sans corroboration externe. Les limites connues des LLMs (hallucinations, biais d'entraînement, cutoff training) ont été prises en compte dans la cotation des faits. »

## 64.12 Synthèse

| Risque IA | Mitigation |
|---|---|
| Hallucination factuelle | Vérification source primaire |
| Hallucination URL/citation | Cliquer / consulter |
| Biais linguistique | Multi-LLMs, sources directes |
| Sur-confiance ton | Dissocier forme et fond |
| Erreur de raisonnement | Re-faire à la main |
| Sur-confiance analyste | Vigilance permanente |

> **Principe.** L'IA est un outil. Comme tout outil, elle a des défauts. La rigueur de l'analyste est la **seule** garantie de qualité du livrable. Aucun outil ne se substitue à cette rigueur.

-----
