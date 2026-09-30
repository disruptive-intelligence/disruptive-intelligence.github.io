---
title: PARTIE IX — IA, agents et automatisation
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 10
chapters: 15
---

> **Ce que cette partie apprend.** Mobiliser les LLMs comme assistants OSINT, maîtriser le prompting OSINT, opérationnaliser le protocole Retrieve-Store-Cite, gérer les hallucinations, déployer des LLMs locaux pour OPSEC, construire des knowledge graphs locaux, intégrer agents autonomes et workflows multi-agents, automatiser conformément aux contraintes légales et techniques, bâtir des pipelines OSINT reproductibles.
>
> **Ce qu'elle ne couvre pas.** La détection des contenus synthétiques (Partie VIII), les passerelles spécialisées (Partie X), la production (Partie XII).
>
> **Ce que vous saurez faire après cette partie.** Utiliser LLMs et agents pour accélérer l'enquête tout en garantissant la traçabilité et la fiabilité, construire des automatisations reproductibles, garder le contrôle souverain de votre infrastructure.

-----

### Chapitre 60 — IA et OSINT : rupture ou accélérateur ?

#### 60.1 Qu'est-ce que l'IA change vraiment ?

L'irruption des LLMs (ChatGPT novembre 2022, GPT-4 mars 2023, Claude, Gemini, Mistral, Llama, et innombrables succession) a transformé profondément l'OSINT entre 2023 et 2026. Plus qu'une simple amélioration, c'est une **rupture méthodologique**.

Mais il faut distinguer ce qui a changé de ce qui n'a pas changé.

**Ce qui a changé.**
- **Vitesse** : extraction d'entités, résumé, traduction divisés par 10 ou plus.
- **Volume** : capacité à traiter des corpus impossibles humainement.
- **Multilinguisme** : barrières linguistiques effondrées.
- **Multimodalité** : LLMs lisent texte, image, audio (en partie).
- **Automatisation** : agents qui pivotent, monitorent, alertent.

**Ce qui n'a pas changé.**
- La **question** initiale reste posée par un humain.
- La **vérification** reste fondamentale.
- La **cotation** reste un acte humain.
- La **décision éthique** reste humaine.
- La **responsabilité** reste humaine.
- La **rigueur méthodologique** reste centrale.

L'analyste 2026 est un **orchestrateur** : il définit les questions, choisit les outils, supervise les agents, vérifie les sorties, prend les décisions de cotation, formule les conclusions. L'IA exécute.

#### 60.2 Augmentation, pas remplacement

L'expression « augmented analyst » désigne la posture 2026 : analyste **augmenté par l'IA**, pas remplacé. Cette nuance est cruciale.

**L'analyste augmenté.**
- Délègue à l'IA les tâches mécaniques (extraction, résumé, traduction).
- Garde la maîtrise des tâches de jugement (cotation, formulation, décision).
- Vérifie systématiquement les sorties IA.
- Maintient une posture critique.
- Reste **responsable** de ses conclusions.

**L'analyste remplacé** (anti-pattern).
- Délègue le jugement à l'IA.
- Accepte les sorties sans vérification.
- Cite l'IA comme source.
- Perd la posture critique.
- Diffuse des hallucinations comme faits.

#### 60.3 Cas d'usage à fort impact en 2026

**Traduction et transcription.** Multilingue effondré. Une vidéo russe est transcrite et traduite en français en quelques minutes.

**Extraction d'entités** depuis corpus volumineux. 500 pages PDF analysées pour extraire toutes les sociétés mentionnées.

**Résumé de corpus.** Synthèse d'un ensemble de documents.

**Classification.** Tri massif (pertinent / non pertinent, sentiment, langue).

**Génération de dorks** et requêtes structurées.

**Reformulation de questions** et hypothèses.

**Analyse de patterns linguistiques.**

**Code et automatisation** (scripts Python, regex, parsers).

**Géolocalisation assistée** (Ch.51).

**Pré-analyse d'images.**

#### 60.4 Cas d'usage à risque élevé

**Recherche factuelle ouverte sans vérification.** Hallucination quasi-garantie.

**Identification de personnes par IA.** Faux positifs catastrophiques.

**Attribution sans corroboration.** L'IA invente des liens.

**Détection 100 % IA-pilotée.** Pas de jugement humain = pas de cotation fiable.

**Publication directe de sortie IA.** Risque juridique et éditorial.

#### 60.5 Les bonnes questions à poser à l'IA en OSINT

**Tâche bien adaptée à l'IA.**
- Mécanique, répétitive, à grand volume.
- Avec critère de vérification clair.
- Sans enjeu de jugement éthique direct.

**Tâche mal adaptée à l'IA.**
- Décision éthique.
- Cotation finale.
- Formulation à enjeu juridique.
- Identification sans vérification possible.

#### 60.6 Le pacte 2026 entre analyste et IA

**L'IA peut s'occuper de.**
- Volume de traitement.
- Vitesse de pré-analyse.
- Suggestions et hypothèses.
- Reformulation et synthèse.

**L'analyste garde.**
- Définition de la question.
- Choix méthodologiques.
- Vérification des sorties.
- Cotation finale.
- Décision éthique.
- Formulation calibrée.
- Responsabilité.

#### 60.7 Limites structurelles des LLMs en OSINT

**Hallucinations.** Cf. Ch.64.

**Connaissances datées.** Cutoff training. Compensé par tools (RAG, search) mais imparfait.

**Biais d'entraînement.** Données surreprésentent certaines régions, langues, perspectives.

**Pas d'accès direct au monde.** L'IA infère, ne perçoit pas.

**Coût.** Tokens consommés, abonnements.

**OPSEC.** Fuite d'intent via prompts (Ch.10, Ch.65).

#### 60.8 LLMs comparés en 2026

**Claude (Anthropic).** Forces : raisonnement structuré, instructions précises, sécurité.

**ChatGPT / GPT-4 / o-series (OpenAI).** Forces : multimodal mature, écosystème, code.

**Gemini (Google).** Forces : multimodal, intégration Google search, contexte long.

**Mistral.** Forces : européen (souveraineté), open source partial, performance.

**Llama (Meta).** Forces : open source, déployable localement.

**Qwen (Alibaba).** Forces : multilingue chinois fort, open source.

**Choix selon usage.** Pas de modèle universel optimal. Pour OPSEC, LLMs locaux (Ch.65). Pour multimodal complexe, GPT-4V ou Claude. Pour souveraineté EU, Mistral.

#### 60.9 Évolution rapide

L'écosystème LLM évolue mensuellement. Toute affirmation sur les capacités est datée. **Discipline d'analyste 2026** : revue trimestrielle des outils, ré-évaluation, mise à jour des méthodes.

#### 60.10 Synthèse

| Aspect | Avant 2023 | 2026 |
|---|---|---|
| Traduction corpus | Heures-jours | Minutes |
| Extraction entités | Manuel | Semi-auto LLM |
| Volume traité | Limité analyste | Quasi illimité |
| Multilinguisme | Compétences spécifiques | Universel via LLM |
| Vérification | Humain | Humain (inchangé) |
| Cotation | Humain | Humain (inchangé) |
| Responsabilité | Humain | Humain (inchangé) |

L'IA augmente la vitesse et le volume. Elle ne change pas la responsabilité méthodologique.

-----

### Chapitre 61 — LLMs comme assistants OSINT

#### 61.1 Les cas d'usage matures

Les LLMs sont matures pour plusieurs cas d'usage OSINT spécifiques. Ce chapitre les détaille avec méthodologie pratique.

#### 61.2 Extraction d'entités

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

#### 61.3 Résumé de corpus

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

#### 61.4 Traduction et transcription

**Traduction.** LLMs équivalents ou supérieurs à Google Translate / DeepL pour la plupart des langues majeures. Particulièrement bons pour contexte culturel.

**Transcription audio.** OpenAI Whisper (open source) reste référence. Multilingue, précis, gratuit en local.

**Méthode transcription.**
```bash
whisper audio.mp3 --model large --language fr
```

**Vérification.** Échantillonner. Pour pièces critiques, expertise humaine.

#### 61.5 Classification massive

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

#### 61.6 Génération de dorks

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

#### 61.7 Reformulation de questions

**Cas d'usage.** Une intuition vague. L'IA aide à la formuler en questions de renseignement précises.

**Méthode.**
```
Prompt:
J'ai cette intuition vague : « Delaunay pourrait avoir des structures offshore ».
Aide-moi à reformuler cela en 5-10 questions de renseignement opérationnelles, fermées, vérifiables.
```

**Utile.** Mais reste un brouillon à valider.

#### 61.8 Analyse de patterns linguistiques

**Cas d'usage.** Comparer le style de plusieurs textes pour évaluer s'ils ont le même auteur.

**Méthode.**
```
Prompt:
Voici 5 textes. Analyse les patterns stylistiques (vocabulaire, structure, tournures, ponctuation, registre). Identifie s'il y a des similarités suggérant un auteur commun.

Pour chaque paire, donne un score de similarité (0-100) avec justification.
```

**Limite.** L'IA peut hallucinations en stylométrie. Vérification par signaux objectifs (mots récurrents, longueur phrases).

#### 61.9 Aide au code et à l'automatisation

**Cas d'usage.** Script Python pour parser des résultats Sherlock.

**Méthode.** Demander à l'IA un script. **Tester systématiquement**. Le code généré est souvent imparfait, parfois erroné.

#### 61.10 Génération d'hypothèses

**Cas d'usage.** L'IA suggère des hypothèses alternatives à explorer.

**Méthode.**
```
Prompt:
Voici les faits collectés sur l'entité X : [...]
Génère 5-8 hypothèses alternatives expliquant ces faits. Pour chaque hypothèse, indique quels éléments supplémentaires permettraient de la confirmer ou infirmer.
```

**Très utile** pour anti-biais. À traiter comme suggestions à tester (ACH — Ch.79).

#### 61.11 Synthèse — usages matures et risqués

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

### Chapitre 62 — Prompting OSINT et patterns utiles

#### 62.1 Le prompting comme compétence

Bien interroger un LLM est une compétence. Elle se développe. Pour OSINT, certains **patterns de prompts** sont particulièrement utiles.

#### 62.2 Principes de base

**Clarté.** Préciser le rôle, la tâche, le format de sortie, les contraintes.

**Exemples (few-shot).** Montrer 1-2 exemples souvent améliore.

**Contraintes explicites.** « Ne pas inventer », « Si tu ne sais pas, dis-le », « Cite tes sources ».

**Format structuré.** JSON, tableaux, listes. Plus exploitable.

**Décomposition.** Tâches complexes en sous-tâches.

#### 62.3 Pattern : prompt de cadrage

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

#### 62.4 Pattern : prompt de tri

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

#### 62.5 Pattern : prompt d'extraction structurée

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

#### 62.6 Pattern : prompt de vérification

**Objectif.** Tester la cohérence d'une affirmation.

```
Affirmation : [affirmation à vérifier].

1. Quelles évidences sont nécessaires pour confirmer cette affirmation ?
2. Quelles évidences pourraient la réfuter ?
3. Quelles hypothèses alternatives expliqueraient les mêmes faits ?
4. Quelle cotation Admiralty recommanderais-tu pour cette affirmation, et pourquoi ?
```

#### 62.7 Pattern : prompt de rédaction

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

#### 62.8 Pattern : prompt de contre-analyse

**Objectif.** Anti-biais (raisonnement adversaire).

```
Voici les conclusions actuelles d'une enquête OSINT : [...]
Adopte le rôle de devil's advocate.
1. Quelles failles méthodologiques cette enquête présente-t-elle ?
2. Quels biais cognitifs peuvent l'avoir influencée ?
3. Quelles hypothèses alternatives n'ont peut-être pas été suffisamment testées ?
4. Quelles vérifications supplémentaires seraient critiques ?
```

#### 62.9 Pattern : prompt de traduction contextuelle

**Objectif.** Traduction au-delà du littéral.

```
Voici un texte en [langue source] : [...]
Traduis en français en :
- Préservant le sens et le ton.
- Ajoutant entre crochets toute information culturelle / contextuelle nécessaire à un lecteur français.
- Notant toute expression difficilement traduisible avec justification.
- Identifiant toute référence implicite (personnages, événements, expressions idiomatiques).
```

#### 62.10 Pattern : prompt comparatif

**Objectif.** Comparer plusieurs sources.

```
Voici N versions d'un même fait, rapportées par sources différentes : [...]
1. Identifie les points convergents.
2. Identifie les contradictions.
3. Pour chaque contradiction, propose une hypothèse explicative.
4. Quelle source semble la plus fiable, et pourquoi ?
5. Quelle synthèse retenir avec quel niveau de confiance ?
```

#### 62.11 Bibliothèque de prompts d'analyste

L'analyste mature constitue sa propre **bibliothèque de prompts** (templates). Versionnable, partageable en équipe, améliorée au fil des usages.

**Format type.** Fichier markdown par catégorie (cadrage, tri, extraction, vérification, rédaction, etc.) avec exemples d'usage et résultats attendus.

#### 62.12 Anti-pattern à éviter

**Question ouverte sans contexte.** « Que penses-tu de Delaunay ? » → hallucination probable.

**Pas de contraintes.** Pas de « ne pas inventer », pas de format → sortie variable.

**Confiance aveugle.** Accepter sortie sans vérification.

**Surcharge.** 50 instructions dans un prompt → l'IA en oublie.

**Pas de validation.** Ne jamais re-tester la même question avec une formulation différente.

-----

### Chapitre 63 — Protocole Retrieve-Store-Cite

#### 63.1 Le protocole opérationnel

Le **protocole Retrieve-Store-Cite** est la formalisation de l'usage rigoureux des LLMs en OSINT. Il garantit que toute information utilisée dans un livrable est traçable à une source primaire vérifiable, et non pas à une hallucination LLM.

**Trois étapes.**

**Retrieve.** Le LLM récupère ou identifie des éléments candidats (faits, sources, hypothèses).

**Store.** L'analyste stocke ces éléments avec leur source originale.

**Cite.** Dans le livrable, la source citée est la **source originale**, jamais le LLM.

#### 63.2 Pourquoi ce protocole

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

#### 63.3 Mise en œuvre pratique

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

#### 63.4 Exemple concret

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

#### 63.5 Tracer le LLM dans la méthodologie

**Bonne pratique.** Mentionner l'usage du LLM dans la **méthodologie** du rapport.

**Exemple.**
> « Méthodologie : la collecte initiale a été assistée par LLMs (Claude, ChatGPT) pour extraction d'entités sur les corpus presse et registres publics. Chaque fait restitué dans ce rapport a fait l'objet d'une vérification directe sur la source primaire (URL, hash, et capture archivée référencés en annexe). Aucune affirmation n'est citée sur la seule base d'une production LLM. »

#### 63.6 Garde-fous techniques

**RAG (Retrieval Augmented Generation).** Architecture qui force le LLM à citer des sources réelles fournies en contexte. Réduit (sans éliminer) les hallucinations.

**Outils RAG OSINT.**
- **Perplexity** : moteur conversationnel avec sources.
- **OpenAI assistants avec retrieval**.
- **Notebook LM** (Google) : on fournit les sources, le LLM répond avec citations.
- **Self-hosted RAG** : LangChain, LlamaIndex avec vector DB locale.

#### 63.7 Limites du protocole

**Ne supprime pas les hallucinations.** Le LLM peut citer la bonne source mais affirmer ce qu'elle ne contient pas. Vérification reste obligatoire.

**Coûteux en temps.** Vérifier chaque sortie LLM prend du temps. Mais c'est le prix de la rigueur.

**Adoption.** Doit devenir un réflexe. La tentation de zapper est forte sous pression de délais.

#### 63.8 Application aux différentes sources

**Sortie de Perplexity, ChatGPT search.** Cliquer chaque source citée. Vérifier que ce que le LLM affirme est dans la source.

**Sortie résumé.** Vérifier les faits clés contre le corpus d'origine.

**Sortie traduction.** Échantillonner. Pour pièces critiques, traducteur humain.

**Sortie identification.** Toujours corroborer par recherche directe.

#### 63.9 Cas particuliers

**LLM admet ne pas savoir.** Bon signal. Continuer à investiguer sans pression.

**LLM hallucine en cas particulier.** Investigation pour comprendre pourquoi. Ne pas reproduire le pattern.

**LLM cohérent et confident, mais hallucine.** Cas le plus dangereux. La rigueur de vérification est seule défense.

#### 63.10 Synthèse — règle d'or

> **Aucune affirmation produite par un LLM n'entre dans un livrable sans avoir été vérifiée contre sa source primaire. Sans exception.**

C'est le **protocole Retrieve-Store-Cite**. C'est ce qui rend l'IA utilisable en OSINT sans compromettre la rigueur.

-----

### Chapitre 64 — Hallucinations, biais et erreurs IA

#### 64.1 Qu'est-ce qu'une hallucination

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

#### 64.2 Pourquoi les LLMs hallucinent

Les LLMs prédisent le mot suivant le plus probable selon leur entraînement. Ils n'ont pas de **modèle de vérité**. Ils produisent ce qui « ressemble à » une réponse plausible.

**Conséquence.** Lorsque l'information demandée est rare, dépassée, ou hors corpus d'entraînement, le LLM **fabule** plutôt que d'admettre l'ignorance. Et cette fabulation est typiquement convaincante.

#### 64.3 Domaines à haut risque d'hallucination

**Personnes peu connues.** Noms hors top 10 000 références. Le LLM va inventer biographies, parcours, événements.

**Événements récents.** Au-delà du cutoff training. Et même avant le cutoff, les événements peu médiatisés sont mal couverts.

**Informations très spécifiques.** Dates précises, chiffres précis, références de documents.

**Citations.** Le LLM peut inventer une « citation » plausible attribuée à une personnalité.

**Sources.** URLs, articles, papers — souvent inventés.

**Langues moins représentées.** Hallucinations plus fréquentes en langues mineures.

#### 64.4 Domaines à risque modéré

**Concepts généraux.** Définitions, méthodes établies. Risque modéré (mais non nul).

**Personnalités très médiatiques.** Le LLM a du contenu, risque réduit mais non nul (confusions, attributions erronées).

**Sciences établies.** Faits scientifiques bien documentés. Risque relativement faible.

#### 64.5 Reconnaître une hallucination

**Signaux d'alerte.**
- Précision inhabituelle (date exacte, chiffre précis, URL spécifique) sans source vérifiable.
- Cohérence narrative trop parfaite.
- Sources citées non vérifiables.
- Détails biographiques trop riches pour une personne obscure.
- Contradiction discrète avec faits connus.

**Test.** Re-poser la même question dans une formulation différente, ou à un autre LLM. Si les réponses divergent, méfiance.

#### 64.6 Biais des LLMs

Au-delà des hallucinations, biais structurels :

**Biais linguistique.** Anglais surreprésenté → meilleures performances en anglais.

**Biais culturel.** Perspectives occidentales dominantes.

**Biais temporel.** Cutoff training crée un « horizon ».

**Biais idéologique.** Selon datasets et fine-tuning, certaines perspectives sont sur-représentées.

**Biais de complaisance.** Tendance à dire ce que l'utilisateur veut entendre.

**Implication OSINT.** Toujours valider hypothèses contre sources externes. Ne pas se fier au « consensus IA ».

#### 64.7 Erreurs de raisonnement

Au-delà des hallucinations factuelles, erreurs logiques :

**Sauts de logique.** Conclusion non soutenue par les prémisses.

**Confusion de catégories.** Mélange entre faits et hypothèses.

**Causalité abusive.** Inférer cause à partir de corrélation.

**Vérification.** Re-faire le raisonnement à la main pour décisions critiques.

#### 64.8 Stratégies de mitigation

**1. RAG (Retrieval Augmented Generation).** Fournir sources au LLM, demander des citations. Réduit (sans éliminer).

**2. Cross-validation multi-LLMs.** Poser même question à Claude, GPT, Gemini. Divergences = signal de doute.

**3. Vérification source primaire systématique.** Le protocole Retrieve-Store-Cite (Ch.63).

**4. Demander incertitude.** « Si tu n'es pas sûr, dis-le. » Améliore (sans garantir).

**5. Prompts qui valorisent la prudence.** « Préfère dire 'je ne sais pas' à inventer. »

**6. Structurer la sortie.** JSON, tableaux. Force le LLM à être précis ou à laisser vides.

**7. Re-poser avec formulation différente.** Test de cohérence.

#### 64.9 Cas particulier : sur-confiance

Les LLMs **expriment de la confiance** même quand ils hallucinent. Le ton assertif ne reflète pas la justesse. L'analyste doit dissocier **forme** (autorité du ton) et **fond** (justesse des affirmations).

**Réflexe.** Toujours appliquer la même rigueur de vérification, indépendamment du ton du LLM.

#### 64.10 Sur-confiance de l'analyste

Le piège n'est pas dans le LLM, mais dans la **psychologie de l'analyste**.

**Pattern dangereux.**
- L'analyste utilise le LLM avec succès sur 50 cas faciles.
- L'analyste développe une confiance.
- Sur le 51e cas (difficile, peu de données), le LLM hallucine.
- L'analyste, en confiance, ne vérifie pas.
- Hallucination publiée.

**Défense.** Toujours vérifier, **surtout** quand on est en confiance.

#### 64.11 Documentation des limites IA dans rapport

**Bonne pratique.** Le rapport mentionne explicitement les outils IA utilisés et leurs limites.

**Exemple section méthodologique.**
> « Cette enquête a mobilisé des LLMs (Claude 4, GPT-4) pour assistance en extraction d'entités, traduction et reformulation. Tous les faits et conclusions ont fait l'objet d'une vérification directe sur sources primaires. Aucune affirmation n'est issue de la seule production LLM sans corroboration externe. Les limites connues des LLMs (hallucinations, biais d'entraînement, cutoff training) ont été prises en compte dans la cotation des faits. »

#### 64.12 Synthèse

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

### Chapitre 65 — LLMs locaux et OPSEC

#### 65.1 Pourquoi LLMs locaux

Les LLMs commerciaux (ChatGPT, Claude, Gemini) sont puissants mais posent des **risques OPSEC** :

- Prompts conservés par fournisseur.
- Apprentissage possible (variable selon politiques).
- Profilage du compte.
- Réquisitions judiciaires dans pays du fournisseur.
- Fuite d'intent.

**Pour les enquêtes sensibles**, les **LLMs locaux** offrent une alternative : pas de fuite, pas de cloud, données sous contrôle souverain.

#### 65.2 État de l'art LLMs locaux 2026

L'écart entre LLMs commerciaux frontier et LLMs locaux open source s'est **réduit** entre 2023 et 2026. Modèles open source actuels :

- **Llama 3.3 / Llama 4** (Meta) : référence open source.
- **Mistral Large** (Mistral) : européen.
- **Qwen 2.5 / Qwen 3** (Alibaba) : multilingue fort.
- **DeepSeek R1** : raisonnement.
- **Gemma 2 / 3** (Google) : compact, multilingue.
- **Phi-4** (Microsoft) : compact mais performant.

**Performance.** Pour tâches OSINT standard (extraction, résumé, traduction, classification), LLMs locaux performants ~Claude / GPT-4 niveau de 2023. Pour raisonnement complexe, commerciaux restent supérieurs.

**Suffisant** pour la plupart des cas OSINT.

#### 65.3 Outils de déploiement local

**Ollama** (ollama.com). Standard de fait. Installation simple, API locale, multi-modèles.
```bash
# Installation
curl https://ollama.ai/install.sh | sh

# Lancer Llama 3.3
ollama run llama3.3

# Lancer Mistral
ollama run mistral
```

**LM Studio**. Interface graphique. Pour utilisateurs moins techniques.

**vLLM** (auto-hébergé). Pour deployment production.

**Llama.cpp**. Très efficace, low-level.

**GPT4All**. Multi-OS, simple.

#### 65.4 Matériel requis

**Minimum.** PC moderne avec GPU 8-12 Go VRAM. Modèles 7B-13B fonctionnent.

**Confortable.** GPU 24-48 Go VRAM. Modèles 30B-70B en quantization.

**Workstation OSINT type 2026.**
- CPU récent (Intel i7 / Ryzen 7).
- 32-64 Go RAM.
- GPU NVIDIA RTX 4090 (24 Go VRAM) ou équivalent.
- SSD 1 To.
- Coût : 2500-4000 €.

#### 65.5 Modèles recommandés selon usage

**Extraction d'entités, classification, traduction.** Llama 3.3 70B (quantization Q4), ou Mistral Large.

**Multilingue.** Qwen 2.5 (excellence chinois, asiatique).

**Code.** DeepSeek Coder ou Qwen Coder.

**Compact (machine modeste).** Phi-4, Gemma 2 9B.

**Multimodal.** LLaVA, Qwen-VL.

#### 65.6 Workflow local

**Mise en place.**
1. Installation Ollama.
2. Téléchargement des modèles utilisés.
3. Test des performances.
4. Intégration dans pipeline (Jupyter, scripts Python).

**Usage pour enquête sensible.**
1. Toutes les requêtes vont au LLM local.
2. Aucune donnée ne quitte la machine.
3. Logs locaux (Ollama tient un historique consultable).
4. Modèles peuvent être supprimés en fin d'enquête (purge).

#### 65.7 API locale

Ollama expose une API HTTP locale :
```python
import requests

response = requests.post('http://localhost:11434/api/generate', 
    json={
        "model": "llama3.3",
        "prompt": "Extrais les entités de ce texte : ...",
        "stream": False
    })
print(response.json()['response'])
```

Intégration possible avec **LangChain**, **LlamaIndex** pour RAG local.

#### 65.8 Quand basculer commercial vs local

| Cas | Commercial | Local |
|---|---|---|
| Enquête publique non sensible | ✓ | (option) |
| Enquête corporate confidentielle | (option) | **Préférable** |
| Cible avec ressources surveillance | (déconseillé) | **Obligatoire** |
| Cible étatique | (interdit) | **Obligatoire** |
| Cible avec compétences cyber | (déconseillé) | **Préférable** |
| Tâche multimodale complexe | (souvent supérieur) | (option si modèle dispo) |
| Tâche raisonnement complexe | (souvent supérieur) | (limite) |

#### 65.9 Limites LLMs locaux

**Performance.** Sur tâches très complexes, écart avec commerciaux frontier.

**Maintenance.** Mise à jour des modèles, hardware.

**Pas de tools intégrés.** Pas de web search natif (à coupler avec autres outils).

**Coût hardware.** Investissement initial.

#### 65.10 Synthèse

LLMs locaux 2026 sont **prêts pour usage professionnel** sur la plupart des tâches OSINT standard. Pour enquêtes sensibles, c'est le **standard**. Le coût hardware se rentabilise rapidement face aux risques OPSEC des solutions cloud.

> **MIRAGE — Note OPSEC IA.** L'enquête MIRAGE utilise principalement LLMs locaux (Ollama avec Llama 3.3 70B). Tâches sensibles (extraction d'entités sur documents, traduction de mémos chypriotes, analyse de patterns) : tout en local. Tâches non-sensibles (génération de dorks publics, reformulation) : commercial OK. Cette discipline OPSEC protège la confidentialité du dossier face à toute compromission cloud.

-----

### Chapitre 66 — Knowledge graphs locaux

#### 66.1 Pourquoi un knowledge graph

Une enquête OSINT mature génère **des centaines d'entités** (personnes, sociétés, domaines, comptes, contenus, lieux, événements) et **des milliers de relations** (employer, owner, communicates_with, located_at, etc.).

Un **knowledge graph** structure ces données en graphe interrogeable. C'est l'évolution naturelle du vault Obsidian (Ch.17) vers une structure plus formelle.

#### 66.2 Bénéfices d'un knowledge graph local

**Requêtes complexes.** « Toutes les personnes liées à TechnoVert ET à une société offshore » → requête SPARQL en quelques lignes.

**Visualisation.** Graphe explorable, communautés détectées.

**Inférences.** Si A possède B et B possède C, on peut inférer relation transitive A-C.

**Réutilisabilité.** Données d'enquête A peuvent informer enquête B (avec déontologie).

**Souveraineté.** Local, chiffré, sous contrôle.

#### 66.3 Modèle de données : RDF et OWL

**RDF** (Resource Description Framework). Standard W3C pour décrire des triplets (sujet, prédicat, objet) :
```
ex:MarcDelaunay  rdf:type      foaf:Person .
ex:MarcDelaunay  foaf:worksFor ex:TechnoVert .
ex:TechnoVert    rdf:type      ex:Company .
ex:MarcDelaunay  ex:director_of ex:DeltaConsulting .
```

**OWL** (Web Ontology Language). Pour définir des ontologies (taxonomies de classes, propriétés).

Pour OSINT, ontologie type comprend : Person, Company, Domain, Account, Document, Event, Place, Wallet, Phone, Email — plus relations diverses.

#### 66.4 Outils graphes locaux

**Apache Jena** (open source). Stack Java complet pour RDF + SPARQL.

**Eclipse RDF4J** (anciennement OpenRDF Sesame).

**Stardog** (commercial, freemium).

**Blazegraph**.

**Pour graphes property graph (Neo4j-style).**
- **Neo4j Community** (free, local).
- **Memgraph**.
- **TigerGraph Cloud / Local**.

**Pour OSINT simplifié.**
- **Maltego Casefile** (offline).
- **Obsidian** avec plugin graphe.

#### 66.5 SPARQL : langage de requête

**Exemple SPARQL.**
```sparql
PREFIX ex: <http://mirage-investigation.local/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?person ?company
WHERE {
  ?person foaf:worksFor ex:TechnoVert .
  ?person ex:director_of ?offshore_company .
  ?offshore_company ex:juridiction ?juridiction .
  FILTER(?juridiction IN ("Malta", "Cyprus", "BVI"))
}
```

Cette requête retourne toutes les personnes qui travaillent à TechnoVert ET dirigent une société offshore.

#### 66.6 Architecture type pour enquête

**Vault Obsidian** comme couche éditoriale (rédaction, notes).

**Graphe local (Neo4j ou Jena)** comme couche structurée.

**Synchronisation** : scripts qui extraient entités/relations depuis Obsidian vers le graphe, et réciproquement.

**Visualisation** : Neo4j Bloom, Gephi (depuis export).

#### 66.7 Knowledge graphs et LLMs

**Pattern émergent 2025-2026.** Combiner LLM + knowledge graph.

**Use case.**
- LLM extrait entités d'un document.
- Entités sont ajoutées au graphe.
- LLM peut interroger le graphe pour répondre à questions complexes.
- Permet « questions naturelles » répondues sur données structurées.

**Outils.**
- **LangChain** avec graph stores.
- **LlamaIndex** avec knowledge graph index.
- **GraphRAG** (Microsoft).

#### 66.8 OPSEC du knowledge graph

**Localisation.** Stockage local. Chiffrement disque.

**Accès.** Limité à analystes autorisés.

**Sauvegarde.** Chiffrée, 3-2-1.

**Destruction.** Purge sécurisée en fin d'enquête (RGPD).

#### 66.9 Pièges classiques

**Sur-modélisation.** Créer 50 types de relations alors que 10 suffisent. Complication inutile.

**Sous-cotation.** Oublier de coter les faits ajoutés au graphe.

**Pas de provenance.** Chaque triplet doit pointer vers une source (named graph).

**Bruit.** Ajouter tout au graphe → graphe ingérable.

#### 66.10 Cas d'usage MIRAGE

Pour MIRAGE, knowledge graph résumant :
- 4 sociétés (TechnoVert, Delta Consulting, Verde Holdings, SCI La Provence Familiale).
- ~50 personnes (employés, dirigeants, contacts, journalistes mentionnés, etc.).
- ~30 domaines et comptes.
- ~100 événements datés.
- Relations : employer, director, owner, located_at, communicates_with, mentions, etc.

Requête type : « Quels sont les chemins de relations entre Delaunay et le cluster X de désinformation ? » → graphe répond en quelques lignes SPARQL.

#### 66.11 Synthèse

| Bénéfice | Coût |
|---|---|
| Requêtes complexes | Apprentissage (RDF/Neo4j/SPARQL) |
| Visualisation | Maintenance technique |
| Inférence | Modélisation initiale |
| Souveraineté | Investissement temps |
| Réutilisabilité | Discipline (provenance, cotation) |

Pour enquêtes complexes (>200 entités), le knowledge graph devient un investissement rentable.

-----

### Chapitre 67 — Agents autonomes et workflows multi-agents

#### 67.1 Agentic AI : la rupture 2024-2026

Les **agents autonomes** sont des LLMs équipés d'**outils** (web search, calculatrice, code execution, bases de données, autres LLMs). Ils peuvent **planifier**, **exécuter**, **boucler** sur des tâches complexes.

Entre 2023 et 2026, l'agentic AI est passée du prototype à la maturité opérationnelle. Pour l'OSINT, c'est une révolution silencieuse.

#### 67.2 Architecture agent

**Composantes.**
- **LLM core** : raisonne, planifie.
- **Tools** : capacités externes (web search, scraping, APIs, code).
- **Memory** : court terme (contexte conversation) et long terme (persistant).
- **Planner** : décompose les objectifs en sous-tâches.
- **Executor** : exécute les sous-tâches.
- **Validator** : vérifie les sorties.

**Frameworks.**
- **LangChain Agents** : standard.
- **AutoGPT, BabyAGI** : pionniers.
- **OpenAI Assistants API**.
- **Anthropic Claude tool use**.
- **CrewAI** : multi-agents orchestrés.
- **AutoGen** (Microsoft) : multi-agents conversationnels.

#### 67.3 Cas d'usage OSINT

**Monitoring continu.** Agent surveille les mentions d'une entité sur réseaux sociaux et alertes en cas de pic.

**Profilage automatique de social graphs.** Agent identifie les comptes liés, extrait métadonnées, génère rapport.

**Géolocalisation multi-hypothèses.** Plusieurs agents proposent hypothèses, validateur cross-check, synthèse.

**Investigation préliminaire.** Agent reçoit nom d'une entité, conduit première investigation autonome, livre fiche entité de base.

**Veille concurrence / risque.** Agent monitore X entités, détecte changements significatifs, alerte.

#### 67.4 Outils commerciaux 2026

**Bitsight, RiskIQ, SecurityScorecard.** ASM (Attack Surface Management) avec composantes agentiques.

**Fivecast** (Australie) : suite OSINT institutionnelle avec ONYX/LUNEX/MATRIX, agentic.

**Babel Street** : multi-source intelligence, AI-driven.

**ShadowDragon** : OSINT enterprise.

**Brandwatch, Talkwalker, Meltwater** : SOCMINT agentic.

Ces outils sont **chers** (10-200 k€/an) mais structurent l'OSINT institutionnelle.

#### 67.5 Construire un agent OSINT

**Exemple simple : agent enrichissement entité.**

```python
from langchain_anthropic import ChatAnthropic
from langchain.agents import Tool, initialize_agent

llm = ChatAnthropic(model="claude-opus-4-7")

tools = [
    Tool(name="web_search", func=lambda q: search_web(q), description="..."),
    Tool(name="whois_lookup", func=lambda d: whois(d), description="..."),
    Tool(name="email_check", func=lambda e: holehe(e), description="..."),
    Tool(name="username_search", func=lambda u: sherlock(u), description="..."),
]

agent = initialize_agent(tools, llm, agent_type="react")
agent.run("Enrichir l'entité Marc Delaunay, DAF TechnoVert SAS.")
```

L'agent va décider quels outils utiliser dans quel ordre, exécuter, synthétiser.

#### 67.6 Multi-agents orchestrés

Pour tâches complexes, plusieurs agents collaborent.

**Pattern type pour OSINT.**

- **Agent Collecteur** : exécute requêtes, captures.
- **Agent Vérificateur** : valide source, authenticité.
- **Agent Analyste** : corrèle, formule hypothèses.
- **Agent Rédacteur** : produit fiche, rapport.
- **Agent Superviseur** : orchestre, valide.

**Bénéfice.** Spécialisation, parallélisation, vérification croisée.

#### 67.7 Knowledge graphs comme mémoire d'agent

Couplage **agent + knowledge graph local** = mémoire structurée persistante.

L'agent enrichit le graphe à chaque investigation. Le graphe devient une **mémoire institutionnelle** (avec déontologie : pas de mélange entre enquêtes selon mandats).

#### 67.8 Validation layer

**Tout agent doit avoir un validation layer.**

**Validations typiques.**
- Sortie respecte format attendu (schéma JSON).
- Sources citées sont vérifiables.
- Cotation Admiralty cohérente.
- Pas d'hallucination détectable (cross-check).
- Pas de violation OPSEC / déontologique.

**Pour l'analyste.** Always-on validation by humain pour décisions critiques.

#### 67.9 Auditabilité et accountability

Un agent qui agit en autonomie pose des questions d'**auditabilité** : qui est responsable des actions ? Comment retracer ?

**Pratiques.**
- Logs détaillés (chaque appel d'outil, chaque sortie LLM).
- Versioning des agents.
- Validation humaine pour actions à enjeu.
- Audit régulier des sorties.
- Documentation dans rapports : « l'investigation a mobilisé un agent autonome X.Y, configuré comme suit... ».

#### 67.10 Limites et risques

**Boucles infinies.** L'agent boucle sur une tâche sans progresser.

**Coût d'exécution.** Agents agressifs consomment beaucoup de tokens / API calls.

**Hallucinations en chaîne.** Une hallucination précoce contamine toute la chaîne.

**Détection adverse.** Une cible peut détecter le pattern d'agent et réagir (counter-OSINT).

**Fuite d'intent.** Logs cloud, prompts révélateurs.

**Auditabilité limitée.** Plus l'agent est complexe, moins on suit son raisonnement.

#### 67.11 Synthèse 2026

Les agents autonomes sont devenus **outils standards** de l'OSINT 2026 institutionnel. Pour l'analyste indépendant ou en cabinet moyen :
- **Outils commerciaux** (Bitsight, Fivecast) si budget.
- **Agents custom** (LangChain, CrewAI) si compétences techniques.
- **Workflows manuels assistés** sinon (LLM en complément, sans full autonomy).

**Discipline 2026.** L'agent doit servir l'enquête, pas la remplacer. La validation humaine reste centrale.

-----

### Chapitre 68 — Automatisation conforme

#### 68.1 L'automatisation comme nécessité

L'OSINT 2026 traite des **volumes** que l'humain seul ne peut gérer. Automatiser certaines tâches devient une nécessité opérationnelle.

Mais l'automatisation soulève des **questions** :
- Conformité aux CGU plateformes.
- Respect des limites légales (scraping, anti-bot).
- Charge serveur (DoS involontaire).
- Reproductibilité et auditabilité.

#### 68.2 Python comme langage OSINT

**Python** est le langage standard de l'automatisation OSINT pour :
- Lisibilité.
- Écosystème de librairies massives.
- Communauté.
- Multi-OS.

**Stack OSINT type.**
- `requests`, `httpx` : requêtes HTTP.
- `BeautifulSoup`, `lxml` : parsing HTML.
- `pandas` : data manipulation.
- `networkx` : graphes.
- `rapidfuzz` : matching de strings.
- `Playwright`, `Selenium` : scraping navigateur.
- `Scrapy` : framework scraping.
- `Telethon`, `Pyrogram` : Telegram API.
- `praw` : Reddit API.
- `tweepy` : Twitter API.

#### 68.3 API officielles

**Toujours privilégier API officielles** quand disponibles.

**APIs OSINT principales.**
- **Shodan** : infrastructure.
- **HIBP** : breaches.
- **VirusTotal** : malware, IOCs.
- **GitHub** : code search.
- **Twitter (X) v2** : payante.
- **Reddit** : payante.
- **Telegram (Telethon)** : conditions strictes.
- **OpenSanctions** : gratuit.

**Authentification** : tokens API personnels, jamais hardcoded dans code.

#### 68.4 Scraping résilient

Quand pas d'API, **scraping** mais avec rigueur.

**Outils.**
- **Playwright** (Microsoft) : moderne, multi-navigateurs.
- **Selenium** : classique.
- **Scrapy** : framework structuré.
- **httpx + BeautifulSoup** : simple.

**Bonnes pratiques.**
- **Respect robots.txt**.
- **Rate limiting** auto-imposé (1 requête / 3-10 sec).
- **User-Agent** identifiable et honnête.
- **Pas de charge sur serveur** (modération du parallélisme).
- **Conservation traçabilité** (logs des requêtes).

#### 68.5 Anti-anti-scraping

Plateformes déploient des anti-bot. Contournements technologiques :

**Rotation User-Agents.** Sélection aléatoire dans liste réaliste.

**Proxies résidentiels.** BrightData, Smartproxy. Coûteux mais efficaces.

**CAPTCHA solvers.** 2Captcha, anti-captcha (déontologie variable).

**Cloudflare bypass.** FlareSolverr, Cloudscraper (durée de vie limitée).

**Behavioral fingerprinting.** Émuler comportement humain (pauses aléatoires, scroll, mouse).

**Précautions juridiques.** Tous ces contournements peuvent enfreindre CGU. Selon juridiction, frottements pénaux potentiels. À documenter et limiter.

#### 68.6 Conformité légale

**Robots.txt** : respecter par défaut.

**CGU** : lire, respecter dans la mesure du raisonnable.

**Charge** : ne pas DoS un site.

**Données personnelles** : RGPD compliance, finalité, minimisation.

**Juridiction** : législations variables. Allemagne plus stricte, US plus permissif (hiQ v. LinkedIn 2022 SCOTUS).

#### 68.7 Reproductibilité

**Scripts versionnés.** Git local.

**Documentation.** Comment lancer, paramètres, attendus.

**Logs.** Chaque exécution traçable.

**Test.** Unit tests pour fonctions critiques.

#### 68.8 Workflows reproductibles

**Notebook Jupyter.** Pour investigation interactive avec traçabilité.

**Scripts orchestrés** (`make`, `snakemake`, `Airflow`). Pour pipelines complexes.

**Dockerized.** Image Docker reproductible avec dépendances figées.

#### 68.9 Stockage des données automatisées

**Formats structurés.** JSON, CSV, Parquet.

**Bases locales.** SQLite (simple), PostgreSQL (volume).

**Pas de cloud non chiffré.** Toujours chiffrement côté client.

#### 68.10 Synthèse — règles d'or automation

1. **API officielle** > scraping.
2. **Respect des CGU et robots.txt** par défaut.
3. **Rate limiting** auto-imposé.
4. **Logs** traçables.
5. **Versioning** Git.
6. **Reproductibilité** documentée.
7. **OPSEC** maintenue (pas de fuite d'intent).
8. **Conformité RGPD** par design.

-----

### Chapitre 69 — Pipelines OSINT reproductibles

#### 69.1 Du script ad hoc au pipeline

L'analyste débutant écrit des scripts ad hoc. L'analyste mature construit des **pipelines reproductibles** : workflows structurés, versionnés, documentés, ré-exécutables.

Bénéfices :
- Reproductibilité (un confrère ré-exécute).
- Capitalisation (modèles réutilisables).
- Auditabilité.
- Qualité (tests, validation).

#### 69.2 Architecture pipeline type

**Étapes typiques pour pipeline OSINT.**

1. **Collecte** : APIs, scraping, captures.
2. **Stockage brut** : données collectées préservées.
3. **Nettoyage / structuration** : déduplication, formatting.
4. **Enrichissement** : croisements, pivots.
5. **Analyse** : agrégations, statistiques, patterns.
6. **Visualisation** : graphes, dashboards.
7. **Production** : génération de rapports.

Chaque étape : input, traitement, output, log.

#### 69.3 Outils

**Scrapy.** Framework Python pour scraping structuré. Production-ready.

**Apache Airflow.** Orchestration de workflows. Standard data engineering.

**dbt** (Data Build Tool). Transformations SQL versionnées.

**Snakemake.** Workflow management bioinformatique-style.

**Jupyter Notebook.** Pour investigation interactive avec narrative.

**Pandas.** Standard data manipulation.

**Polars** : alternative pandas moderne, plus rapide.

**NetworkX.** Graphes.

**RapidFuzz.** Entity resolution / fuzzy matching.

#### 69.4 Entity resolution

Le **entity resolution** (résolution d'entités) consiste à fusionner les références à la même entité dans différents documents.

**Cas.**
- « Marc Delaunay » et « M. Delaunay » et « Mr. Marc H. Delaunay » → même entité.
- « TechnoVert SAS » et « Technovert » et « TechnoVert France » → même entité.

**Outils.**
- **RapidFuzz** : fuzzy matching strings.
- **dedupe.io** (Python library) : entity resolution structurée.
- **Splink** : pour grands volumes.

#### 69.5 Pipeline exemple : monitoring de domaines

**Objectif.** Monitorer 50 domaines suspects pour changements.

**Pipeline.**

```
Étape 1 — Collecte (quotidienne)
  - Pour chaque domaine : WHOIS, DNS records, certificats, contenu page.
  - Stockage : SQLite local + captures Hunchly.

Étape 2 — Comparaison
  - Diff avec snapshot précédent.
  - Détection des changements.

Étape 3 — Alerte
  - Si changement significatif : email/Signal/Slack à analyste.

Étape 4 — Rapport hebdomadaire
  - Synthèse des changements de la semaine.
  - Visualisations.
```

**Implémentation.** Python + cron + SQLite + Hunchly.

#### 69.6 Versioning et Git

**Tout pipeline est versionné en Git local.**

**Discipline.**
- Commits réguliers.
- Messages explicites.
- Branches par fonctionnalité.
- Tags par versions stables.
- Backup chiffré du repo.

#### 69.7 Tests et qualité

**Unit tests** sur fonctions critiques.

**Integration tests** sur pipelines end-to-end (avec données test).

**Validation continue** : pipeline qui échoue silencieusement = pipeline dangereux.

#### 69.8 Documentation

**README** par projet.

**Notebooks documentés** (Markdown intercalé avec code).

**Modèles de prompts** versionnés.

#### 69.9 Pipeline MIRAGE type

Pour MIRAGE, plusieurs pipelines :

**Pipeline 1 : Enrichissement entités.**
- Input : liste d'entités identifiées.
- Pour chaque entité : recherches automatisées (WHOIS, Sherlock, Hunter, Pappers).
- Output : fiches entités structurées.

**Pipeline 2 : Monitoring cluster désinformation.**
- Input : liste de comptes coordonnés identifiés.
- Quotidien : capture nouveaux posts, archivage, alerte si activité.

**Pipeline 3 : Synthèse rapport.**
- Input : graphe entités + journal d'enquête.
- Output : draft rapport markdown.

#### 69.10 Synthèse — maturation de l'analyste

| Niveau analyste | Approche |
|---|---|
| Débutant | Outils manuels |
| Intermédiaire | Scripts ad hoc |
| Avancé | Pipelines reproductibles versionnés |
| Expert | Agents + knowledge graphs + automation structurée |

L'objectif n'est pas d'automatiser pour automatiser, mais de **scaler** la rigueur méthodologique. Une enquête bien automatisée est plus rigoureuse, plus rapide, plus défendable qu'une enquête manuelle.

> **Principe Partie IX.** L'IA et l'automatisation transforment **comment** on conduit l'OSINT, pas **ce qu'est** l'OSINT. La discipline méthodologique, la cotation, la formulation calibrée, la responsabilité humaine restent les piliers. L'IA accélère et augmente — mais elle s'inscrit dans le même cadre éthique et professionnel.

-----
