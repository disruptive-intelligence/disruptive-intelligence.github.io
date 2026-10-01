---
title: Ch.6 — Fuite de données et exfiltration via l’IA
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie II — Menaces spécifiques aux systèmes IA
  - index.md
---

## 6.1 Les cinq vecteurs de fuite

La fuite de données via un système IA peut emprunter cinq chemins distincts, chacun avec ses propres mécanismes et ses propres défenses.

**Via les prompts (données envoyées au modèle).** C’est le vecteur du shadow AI : un collaborateur copie un contrat client, un rapport financier, ou des données de santé dans ChatGPT en version grand public pour obtenir un résumé ou une analyse. Les données sont envoyées au fournisseur du LLM, potentiellement stockées dans ses logs, potentiellement utilisées pour l’entraînement (selon les conditions d’utilisation), et transférées hors UE si le fournisseur est américain. C’est le scénario le plus fréquent et le plus documenté — Samsung a fait les gros titres en 2023 quand des ingénieurs ont collé du code source propriétaire dans ChatGPT.

**Via les réponses (données exposées par le RAG).** Quand le RAG n’a pas de RBAC vectoriel, un utilisateur peut obtenir via l’assistant des données auxquelles il n’a pas accès dans le système source. Le modèle ne vérifie pas les droits — il répond avec les documents les plus pertinents de la base vectorielle, quel que soit leur niveau de confidentialité. C’est un problème d’architecture, pas un problème de modèle.

**Via les logs.** Les conversations entre utilisateurs et LLM sont typiquement loguées pour le debugging, le monitoring, et l’amélioration continue. Ces logs contiennent en clair les prompts et les réponses — donc potentiellement des données sensibles, des données personnelles, des secrets métier. Si les logs ne sont pas traités comme des données sensibles (chiffrement, contrôle d’accès, durée de conservation), ils constituent une fuite passive permanente.

**Via le modèle (mémorisation).** Un modèle fine-tuné sur des données d’entreprise peut régurgiter des fragments de ces données en réponse à des prompts spécifiques. Des techniques d’extraction ciblée permettent d’augmenter la probabilité de récupérer des données mémorisées. Ce risque est particulièrement élevé pour les modèles entraînés sur de petits datasets (la probabilité de mémorisation augmente quand le ratio données/paramètres diminue) et pour les données répétées dans le dataset d’entraînement.

**Via les outils de l’agent.** Un agent manipulé par une injection peut exfiltrer des données via les outils auxquels il a accès. Un agent email manipulé peut transférer le contenu de la conversation à une adresse externe. Un agent avec accès à une API de recherche peut encoder des données sensibles dans les paramètres de requête vers un serveur contrôlé par l’attaquant.

## 6.2 Le RBAC vectoriel

Le RBAC vectoriel (Role-Based Access Control appliqué à la base vectorielle) est le contrôle le plus critique pour la sécurité d’un RAG. Son principe : chaque document indexé est tagué avec les permissions d’accès du système source (groupe AD, rôle métier, niveau de classification). Lors du retrieval, le système filtre les résultats par droits de l’utilisateur courant AVANT de chercher les documents pertinents, pas après.

L’implémentation technique varie selon les bases vectorielles. pgvector permet d’ajouter des colonnes de filtrage dans la table et de les inclure dans la clause WHERE de la requête de similarité. Pinecone, Weaviate et Qdrant supportent les filtres de métadonnées natifs. Le point critique est que le filtrage doit être fait au niveau du retriever (avant la recherche vectorielle ou en conjonction), pas au niveau du LLM (après la recherche) — le LLM ne doit jamais voir les documents auxquels l’utilisateur n’a pas accès.

L’absence de RBAC vectoriel est l’une des failles les plus fréquentes et les plus graves des déploiements RAG. Elle est d’autant plus insidieuse qu’en phase de POC (où les tests sont souvent faits par l’équipe projet avec des droits larges), le problème ne se manifeste pas.

## 6.3 DLP adapté à l’IA

Le DLP (Data Loss Prevention) traditionnel surveille les canaux de sortie classiques (email, web, USB). Pour l’IA, il doit s’adapter sur deux axes.

En entrée (prompt DLP) : intercepter les requêtes envoyées au LLM et détecter les données sensibles avant qu’elles ne quittent le SI. Cela suppose un proxy applicatif entre l’utilisateur et le modèle (ou entre le SI et l’API cloud du fournisseur). Les éléments à détecter incluent les PII (noms, adresses, numéros de sécurité sociale), les secrets techniques (API keys, tokens, mots de passe), les données classifiées (mentions de niveau de classification), et les données métier sensibles (montants, numéros de contrat, diagnostics médicaux).

En sortie (response DLP) : scanner les réponses du modèle avant de les afficher à l’utilisateur pour détecter les fuites de données (le RAG a exposé un document confidentiel) ou les marqueurs de données sensibles.

> **🔵 Fil rouge — Épisode 5**
> Lors d’un test utilisateur pré-production, un gestionnaire de sinistres demande à l’assistant RAG de NovaSanté : « Quels sont les sinistres récents de Mme Dupont ? ». L’assistant renvoie les sinistres de TOUTES les Mme Dupont de la base — y compris celles gérées par d’autres gestionnaires dans d’autres agences, et une Mme Dupont dont le dossier est en contentieux avec accès restreint au service juridique. Le RBAC vectoriel n’a pas été implémenté : la base vectorielle contient l’intégralité des fiches sinistre sans filtrage par permissions.
> 
> Karim stoppe immédiatement le pilote. L’implémentation du RBAC vectoriel devient un prérequis bloquant pour le go-live : chaque fiche sinistre doit être taggée avec l’agence, le gestionnaire attitré, et le niveau de confidentialité du dossier. Le retriever pgvector est modifié pour filtrer systématiquement par `gestionnaire_id = $current_user OR agence = $current_user_agence` avec exclusion des dossiers à accès restreint.

-----
