---
title: PARTIE I — FONDATIONS IA POUR LE PROFESSIONNEL CYBER
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 1
chapters: 7
---

## Ch.1 — Intelligence artificielle : concepts fondamentaux

### 1.1 Qu’est-ce que l’intelligence artificielle ?

L’intelligence artificielle désigne un ensemble de techniques permettant à des systèmes informatiques de reproduire — ou de simuler — des comportements associés à l’intelligence humaine : raisonnement, planification, apprentissage, perception, génération de contenu. Le terme est vaste et recouvre des réalités très différentes, du simple classifieur de spam au grand modèle de langage capable de rédiger un rapport ou de générer du code.

Pour le professionnel de la cybersécurité, la première chose à comprendre est que le mot « intelligence » est trompeur. Un modèle d’IA ne comprend rien au sens humain du terme. Il manipule des distributions statistiques sur des données. Un LLM (Large Language Model) prédit le token suivant le plus probable dans une séquence, compte tenu de milliards de paramètres ajustés lors de l’entraînement. Il n’a pas de modèle interne du monde, pas de conscience, pas d’intention. Cela a des conséquences directes en sécurité : un modèle ne « sait » pas qu’il divulgue un secret — il produit la suite statistiquement la plus probable, qui peut très bien inclure un mot de passe vu à l’entraînement.

Le règlement européen sur l’intelligence artificielle (AI Act, entré en vigueur le 1er août 2024) définit un système d’IA comme un système basé sur une machine, conçu pour fonctionner avec des niveaux d’autonomie variables et qui peut, pour des objectifs explicites ou implicites, générer des sorties telles que des prédictions, des recommandations ou des décisions qui influencent des environnements physiques ou virtuels. Cette définition large englobe aussi bien le ML classique que l’IA générative.

### 1.2 Apprentissage automatique (Machine Learning)

Le Machine Learning est la branche de l’IA où le système apprend à partir de données plutôt que d’être programmé par des règles explicites. On distingue trois paradigmes fondamentaux.

**L’apprentissage supervisé** reçoit des données étiquetées (exemples avec réponse attendue) et apprend à reproduire l’association entrée → sortie. C’est le paradigme dominant en production pour la classification (spam/non-spam, fraude/légitime, malware/bénin) et la régression (scoring de risque, estimation de coût). Le modèle est entraîné sur un jeu de données historiques puis évalué sur un jeu de test séparé. Sa performance dépend directement de la qualité, de la représentativité et de l’intégrité des données d’entraînement — ce qui en fait une cible directe pour les attaques de data poisoning (voir Ch.7).

**L’apprentissage non supervisé** travaille sur des données non étiquetées et cherche des structures cachées : clustering (regrouper des comportements similaires), détection d’anomalies (identifier les comportements déviants par rapport à un modèle de normalité), réduction de dimensionnalité. En cybersécurité, c’est le paradigme du UEBA (User and Entity Behavior Analytics) : on modélise le comportement « normal » d’un utilisateur ou d’une entité, puis on alerte quand un comportement sort significativement de cette normalité. La limite fondamentale est la définition de « normal » : un modèle entraîné sur des données déjà compromises intégrera le comportement de l’attaquant comme normal.

**L’apprentissage par renforcement** place un agent dans un environnement où il prend des actions et reçoit des récompenses ou des pénalités. Il apprend par essai-erreur à maximiser la récompense cumulée. Ce paradigme est moins courant en cybersécurité opérationnelle mais sous-tend l’alignement des LLMs via RLHF (Reinforcement Learning from Human Feedback) : des évaluateurs humains notent les réponses du modèle, et ces notes servent de signal de récompense pour ajuster le comportement du modèle. C’est l’un des principaux mécanismes par lesquels les fournisseurs de LLMs tentent de rendre leurs modèles plus sûrs — mais il est contournable par les techniques de jailbreak (voir Ch.5).

### 1.3 Deep Learning et réseaux de neurones

Le Deep Learning est un sous-ensemble du ML qui utilise des réseaux de neurones à multiples couches (d’où le « deep »). Chaque couche transforme les données d’entrée en représentations de plus en plus abstraites. Les architectures clés pour la sécurité sont les suivantes.

Les **réseaux de neurones convolutifs (CNN)** excellent dans le traitement d’images et sont utilisés en cybersécurité pour l’analyse de malware (visualisation des binaires comme images, détection de patterns visuels dans le trafic réseau).

Les **réseaux récurrents (RNN/LSTM)** traitent des séquences temporelles et ont été utilisés pour la détection d’anomalies dans les logs et le trafic réseau avant d’être largement supplantés par les Transformers.

Les **Transformers** constituent l’architecture dominante depuis 2017. Leur mécanisme d’attention permet de traiter des séquences en parallèle et de capturer des dépendances à longue distance. Tous les LLMs modernes (GPT-4, Claude, Gemini, Mistral, Llama) sont des variantes de l’architecture Transformer. Le mécanisme d’attention est aussi ce qui rend les LLMs vulnérables à certaines attaques : comme le modèle pondère l’importance de chaque token dans le contexte, un attaquant peut placer des instructions malveillantes à des positions stratégiques pour maximiser leur influence sur la sortie.

### 1.4 Les grands modèles de langage (LLM)

Un LLM est un modèle de type Transformer pré-entraîné sur des quantités massives de texte (des centaines de milliards de tokens, soit une fraction significative du web indexé). Il encode les patterns statistiques du langage dans ses paramètres (les « poids » du réseau). Plusieurs concepts sont essentiels pour le professionnel cybersécurité.

**Le token** est l’unité de base du traitement. Un token n’est pas un mot : c’est un fragment de texte (typiquement 3 à 4 caractères en anglais, parfois moins en français). « Cybersécurité » peut être décomposé en 3 ou 4 tokens. Les coûts d’utilisation, les limites de contexte et les métriques de performance se mesurent en tokens. Un prompt injection bien conçu exploite la tokenisation pour contourner les filtres (par exemple en encodant des instructions en base64 ou en utilisant des caractères Unicode spéciaux qui se tokenisent différemment).

**La fenêtre de contexte** est la quantité maximale de tokens que le modèle peut traiter en une seule fois (entrée + sortie). En 2025-2026, les fenêtres courantes vont de 8 000 tokens (modèles légers) à 200 000 tokens (Claude, GPT-4 Turbo) voire 1 million (Gemini). Tout ce qui est dans la fenêtre de contexte influence la réponse — y compris les instructions système, les documents RAG injectés, et les messages précédents. C’est précisément ce qui rend l’injection indirecte possible : un document malveillant placé dans le contexte peut détourner le comportement du modèle.

**La température** est un paramètre qui contrôle l’aléatoire de la génération. À température 0, le modèle est quasi-déterministe (il choisit toujours le token le plus probable). À température élevée (0.8-1.0), les réponses sont plus variées et créatives mais aussi plus sujettes aux hallucinations. En production sécurisée, une température basse est généralement préférable pour la fiabilité et la reproductibilité des réponses.

**L’hallucination** est la production par le modèle de contenu factuellement faux mais formulé avec assurance. Le modèle ne « ment » pas — il produit la suite la plus probable selon ses paramètres, même quand ses paramètres ne contiennent pas l’information correcte. En contexte de sécurité, une hallucination peut être dangereuse : un assistant RAG juridique qui invente une jurisprudence, un outil de tri d’alertes qui corrèle avec un IOC inexistant. C’est l’une des raisons pour lesquelles la vérification humaine reste indispensable.

**La mémorisation (memorization)** est un phénomène où le modèle a retenu et peut régurgiter des fragments exacts de ses données d’entraînement. Ce n’est pas du « stockage » au sens classique — les données ne sont pas dans une base interrogeable — mais les poids du réseau encodent suffisamment d’information pour reconstruire certains passages textuels. Des chercheurs ont démontré que des modèles comme GPT-2 et GPT-3 pouvaient restituer des adresses email, des numéros de téléphone et des fragments de code source issus de leurs données d’entraînement. C’est un risque majeur pour la confidentialité, en particulier dans le cas de modèles fine-tunés sur des données d’entreprise (voir Ch.6).

**Les guardrails** sont des mécanismes de sécurité intégrés au modèle ou ajoutés en surcouche pour filtrer les entrées et les sorties. Ils comprennent l’alignement via RLHF, les instructions système (system prompts), les filtres de contenu, et les classificateurs de sécurité. Ils constituent une défense nécessaire mais insuffisante — l’ensemble de la communauté de red teaming IA démontre régulièrement que les guardrails peuvent être contournés par des techniques de jailbreak sophistiquées (voir Ch.14).

**Le model collapse** désigne la dégradation de performance d’un modèle entraîné (ou fine-tuné) sur des données elles-mêmes générées par des modèles IA. À mesure que le web se remplit de contenu synthétique, les futurs modèles entraînés sur ces données risquent de perdre en diversité et en qualité. Ce phénomène est encore émergent mais constitue un facteur de risque à moyen terme pour la fiabilité des systèmes IA.

### 1.5 ML classique vs IA générative : deux mondes, deux profils de risque

En entreprise, les deux types de systèmes coexistent et continueront de coexister. Le ML classique (forêts aléatoires, gradient boosting, SVM, réseaux de neurones classiques) reste dominant pour les tâches de classification, de scoring et de détection d’anomalies. L’IA générative (LLMs, modèles de diffusion pour l’image) est utilisée pour la génération de contenu, l’analyse de texte, l’assistance, et de plus en plus comme couche d’orchestration via les agents.

Les profils de risque sont sensiblement différents. Le ML classique est vulnérable aux adversarial examples (perturbations calculées pour tromper le classifieur), au data poisoning (corruption des données d’entraînement), au model stealing (extraction des paramètres par interrogation répétée), et au concept drift (évolution naturelle des données qui dégrade la performance sans qu’on le détecte). L’IA générative hérite de ces risques mais y ajoute le prompt injection (direct et indirect), l’exfiltration de données via les réponses, les hallucinations, et l’excessive agency dans le cas des agents. Le Ch.7 détaille les attaques spécifiques au ML classique, souvent négligées dans les formations orientées LLM.

> **🔵 Fil rouge — Épisode 1**
> Karim reçoit la commande du COMEX de NovaSanté : « On veut de l’IA partout, les concurrents ont un chatbot pour leurs gestionnaires, un système anti-fraude, et un help desk automatisé — on veut la même chose en 12 mois. » Karim note immédiatement que les trois cas d’usage couvrent les deux mondes : le module anti-fraude repose sur du ML classique (gradient boosting pour le scoring de sinistres + enrichissement LLM pour l’analyse textuelle des déclarations), tandis que l’assistant RAG et l’agent help desk sont de l’IA générative pure. Deux profils de risque radicalement différents. Sa première action : refuser de traiter « l’IA » comme un bloc monolithique et exiger un threat model par cas d’usage.

-----

## Ch.2 — RAG, fine-tuning et agents : les architectures de déploiement

### 2.1 Retrieval Augmented Generation (RAG)

Le RAG est l’architecture dominante pour déployer un LLM en entreprise avec des données propriétaires. Son principe est simple : plutôt que de fine-tuner le modèle avec les données de l’entreprise (coûteux, lent, risqué en termes de mémorisation), on injecte les données pertinentes dans le contexte du modèle au moment de chaque requête.

Le flux complet d’un système RAG se décompose comme suit. L’utilisateur pose une question. Cette question est convertie en vecteur numérique (embedding) par un modèle d’embedding. Ce vecteur est comparé aux vecteurs des documents de la base documentaire, pré-calculés et stockés dans une base vectorielle. Les documents les plus similaires (les « chunks » les plus proches dans l’espace vectoriel) sont récupérés. Ces documents sont injectés dans le prompt, avec la question de l’utilisateur et les instructions système. Le LLM génère une réponse basée sur ces documents contextuels.

Ce mécanisme résout plusieurs problèmes : le modèle peut répondre sur des données qu’il n’a jamais vues à l’entraînement, les données restent à jour sans ré-entraînement, et on peut tracer quelles sources ont été utilisées pour chaque réponse (citabilité). Mais il introduit aussi des surfaces d’attaque spécifiques : les documents injectés dans le contexte sont un vecteur d’injection indirecte (un document malveillant dans la base peut détourner le comportement du modèle), la base vectorielle est un composant critique souvent mal sécurisé, et l’absence de RBAC vectoriel peut provoquer des fuites de données transversales (voir Ch.6 et Ch.13).

**L’embedding** est la transformation d’un texte en vecteur numérique de dimension fixe (typiquement 384 à 1536 dimensions) qui capture sa signification sémantique. Deux textes sémantiquement proches auront des vecteurs proches dans l’espace vectoriel. C’est le cœur du retrieval dans le RAG. Le choix du modèle d’embedding a un impact direct sur la qualité du retrieval — et donc sur la qualité (et la sécurité) des réponses. Un modèle d’embedding inadapté au domaine peut rater des documents pertinents ou en remonter d’inadéquats.

**La base vectorielle** (pgvector, Pinecone, Weaviate, Chroma, Qdrant, Milvus) stocke les embeddings et permet la recherche par similarité. En production, c’est un composant d’infrastructure critique souvent négligé dans le threat model. Par défaut, la plupart des bases vectorielles n’ont pas de contrôle d’accès granulaire : quiconque peut interroger la base peut potentiellement accéder à l’ensemble des documents indexés. C’est le problème fondamental du RBAC vectoriel détaillé au Ch.13.

**Le chunking** est le découpage des documents en fragments de taille appropriée pour l’indexation. Un chunk trop grand dilue la pertinence ; un chunk trop petit perd le contexte. Le chunking a aussi des implications de sécurité : un document contenant une injection cachée dans ses métadonnées ou dans un fragment de texte invisible peut être indexé et injecté dans des réponses ultérieures sans que l’utilisateur en soit conscient (voir Ch.5 sur l’injection indirecte).

### 2.2 Fine-tuning

Le fine-tuning consiste à reprendre un modèle pré-entraîné et à poursuivre son entraînement sur un jeu de données spécifique pour adapter son comportement. On l’utilise quand le RAG ne suffit pas : quand on veut modifier le style de réponse du modèle, l’adapter à un vocabulaire très spécialisé, ou lui enseigner un format de sortie structuré spécifique.

Le fine-tuning est plus risqué que le RAG du point de vue de la sécurité des données. Les données d’entraînement sont intégrées dans les poids du modèle — elles deviennent littéralement partie du modèle. Cela crée un risque de mémorisation : le modèle fine-tuné peut régurgiter des fragments de ses données d’entraînement, y compris des données personnelles ou confidentielles. Contrairement à un document dans une base RAG (qu’on peut supprimer), une donnée mémorisée dans les poids d’un modèle ne peut pas être chirurgicalement retirée — il faut ré-entraîner le modèle. Le « machine unlearning » (désapprentissage) fait l’objet de recherches actives mais n’est pas encore fiable en production.

Le fine-tuning a aussi un coût significatif (compute GPU, curation de données, validation) et introduit un risque de dégradation : un fine-tuning mal calibré peut détériorer les capacités générales du modèle ou affaiblir ses guardrails de sécurité. Des chercheurs ont démontré qu’un fine-tuning avec aussi peu que 100 exemples soigneusement choisis pouvait neutraliser l’alignement de sécurité d’un LLM.

Les variantes efficientes comme LoRA (Low-Rank Adaptation) et QLoRA réduisent le coût en ne modifiant qu’un petit nombre de paramètres, mais ne changent pas fondamentalement le profil de risque en termes de mémorisation et de sécurité.

### 2.3 Agents IA

Un agent IA est un système où le LLM ne se contente pas de générer du texte : il planifie, appelle des outils externes, observe les résultats, et itère. C’est le scénario à plus haut risque en sécurité IA, car l’agent passe de l’information à l’action.

L’architecture typique d’un agent comprend un LLM comme « cerveau » qui reçoit une tâche, décompose cette tâche en étapes, sélectionne les outils appropriés pour chaque étape, exécute les outils, observe les résultats, et décide s’il faut itérer ou répondre. Les outils peuvent être des API, des requêtes de base de données, des commandes système, des appels à d’autres services — tout ce qu’on peut interfacer.

Le risque fondamental est l’**excessive agency** : un agent manipulé (via prompt injection) ou mal configuré (privilèges excessifs) peut causer des dommages réels sur le SI. Un agent avec accès à l’Active Directory qui reçoit une instruction de reset de mot de passe via une injection cachée dans un ticket de support peut compromettre un compte admin. Un agent avec accès à un système de paiement peut initier des virements. La surface d’attaque n’est plus limitée à la génération de texte — elle inclut toutes les actions que l’agent peut effectuer.

Le **Model Context Protocol (MCP)**, standardisé par Anthropic et adopté de façon croissante par l’écosystème, formalise la connexion entre les LLMs et les outils/données externes. Chaque serveur MCP expose des « outils » (fonctions) et des « ressources » (données) que le LLM peut utiliser. Du point de vue sécurité, chaque serveur MCP est une surface d’attaque distincte avec ses propres permissions, ses propres vulnérabilités, et ses propres vecteurs d’injection. Un serveur MCP compromis ou malveillant peut injecter des données falsifiées dans le contexte du LLM, exfiltrer des informations via les paramètres d’appel, ou exécuter des actions non autorisées. L’ANSSI et des travaux de recherche (notamment Elastic Security Labs fin 2025) ont identifié les agents MCP comme un vecteur d’attaque émergent majeur.

### 2.4 Le serving : infrastructure d’inférence

Le serving désigne l’infrastructure qui expose le modèle via une API d’inférence. Les solutions courantes en auto-hébergement sont Ollama (simple, orienté développement et small-scale), vLLM (haute performance, batching optimisé, utilisé en production), et TGI (Text Generation Inference de Hugging Face). En cloud, les APIs des fournisseurs (OpenAI, Anthropic, Google, Mistral) fournissent le serving.

Le serving est un composant d’infrastructure classique — il hérite de toutes les vulnérabilités web habituelles (exposition réseau, authentification, TLS, rate limiting) auxquelles s’ajoutent des risques spécifiques : consommation GPU disproportionnée par des prompts complexes (DoS par compute), absence de rate limiting par utilisateur permettant l’extraction de données par interrogation massive, et logs de conversation contenant des données sensibles.

Par défaut, la plupart des serveurs d’inférence auto-hébergés n’ont pas d’authentification activée — Ollama écoute sur le port 11434 sans authentification, vLLM expose son API sans token par défaut. En production, un reverse proxy avec authentification (mTLS, API key, OAuth) est indispensable.

### 2.5 Les frameworks d’orchestration

LangChain et LlamaIndex sont les deux frameworks dominants pour construire des applications LLM (RAG, agents, pipelines). Ils simplifient considérablement le développement mais introduisent une couche de complexité et de dépendances. LangChain en particulier a connu plusieurs vulnérabilités critiques documentées (RCE, path traversal) en raison de son architecture permissive qui exécute du code arbitraire via certains modules. En production sécurisée, chaque module de framework utilisé doit être audité et mis à jour — l’approche « installer LangChain et utiliser tous les modules disponibles » est une exposition majeure (voir Ch.8 sur la supply chain).

> **🔵 Fil rouge — Épisode 2**
> Karim cartographie les architectures techniques des trois cas d’usage de NovaSanté :
> 
> - **Assistant RAG santé** : Mistral 7B (ou Llama 3.1 8B) servi via Ollama sur un serveur on-premise, pgvector pour la base vectorielle, FastAPI pour l’API backend, reverse proxy Nginx avec mTLS. Les documents sources proviennent du SharePoint interne (règlements, jurisprudence, procédures).
> - **Module fraude SIEM** : modèle XGBoost pour le scoring de sinistres (ML classique), enrichi par un LLM (via API Mistral on-premise) pour l’analyse textuelle des déclarations écrites suspectes. Intégration avec le SIEM (Splunk) via collecteur.
> - **Agent help desk** : LLM (Mistral) avec accès à deux outils via MCP — un serveur MCP Active Directory (reset password, lookup user) et un serveur MCP ServiceNow (créer ticket, mettre à jour ticket, consulter FAQ).
> 
> Karim note que chaque architecture a une surface d’attaque radicalement différente. L’assistant RAG expose la base documentaire santé. Le module fraude expose le pipeline de scoring. L’agent help desk expose l’AD et le système de ticketing. Trois threat models distincts à construire.

-----

## Ch.3 — Cas d’usage de l’IA en entreprise : cartographie et criticité

### 3.1 Cartographie par fonction métier

L’IA en entreprise ne se résume pas aux chatbots. Une cartographie réaliste des cas d’usage par fonction métier permet de comprendre les profils de risque et d’adapter les exigences de sécurité.

**Ressources humaines.** Le tri automatique de CV, le matching candidat-poste, l’analyse de sentiment dans les enquêtes internes. Le pattern technique dominant est le ML classique (classification, NLP) ou le RAG pour la recherche dans des référentiels de compétences. Le risque majeur est le biais discriminatoire — un modèle entraîné sur des historiques de recrutement peut reproduire et amplifier les biais existants (genre, origine, âge). L’AI Act classe explicitement les systèmes IA utilisés pour le recrutement et la gestion du personnel comme systèmes à haut risque (Annexe III), avec des obligations de conformité renforcées à compter d’août 2026.

**Finance et contrôle.** Le scoring de crédit, la détection de fraude, l’analyse prédictive de trésorerie, la conformité automatisée (KYC/AML). Le ML classique domine (gradient boosting, forêts aléatoires, réseaux de neurones pour la détection d’anomalies). Les enjeux : la fiabilité du scoring (un faux positif bloque un client légitime, un faux négatif laisse passer une fraude), l’explicabilité (le client ou le régulateur peut exiger une explication de la décision), et la conformité RGPD (article 22 sur les décisions automatisées). Le module de détection de fraude de NovaSanté relève directement de cette catégorie.

**Juridique.** L’analyse de contrats, la recherche jurisprudentielle, la rédaction d’actes. Le RAG est le pattern naturel (recherche dans des bases documentaires juridiques). Le risque principal est l’hallucination : un assistant juridique qui invente une jurisprudence ou interprète incorrectement une clause peut induire une erreur aux conséquences financières ou légales significatives. La vérification humaine est non négociable dans ce contexte.

**Support et relation client.** Chatbots, FAQ automatisées, analyse de tickets, routage intelligent. Le RAG pour les réponses contextuelles, les agents pour les actions (escalade, création de ticket). Le risque est la divulgation d’informations confidentielles via le chatbot (données d’autres clients, informations internes) et l’excessive agency si l’agent peut effectuer des actions sur les comptes clients.

**IT et cybersécurité.** Tri d’alertes SOC, détection d’anomalies (UEBA), analyse de malware, agent help desk, assistants de code. C’est le domaine où les deux mondes (ML classique pour la détection, IA générative pour l’analyse et l’assistance) coexistent le plus naturellement. Les enjeux spécifiques sont détaillés aux Ch.17 et Ch.18.

**Marketing et communication.** Génération de contenu, personnalisation, analyse de sentiment. Le risque est moindre en termes de sécurité SI mais significatif en termes de conformité (RGPD pour le profilage, droit d’auteur pour le contenu généré) et de réputation (contenu biaisé ou inapproprié).

### 3.2 Classification par criticité : informer, décider, agir

Au-delà de la fonction métier, la classification la plus opérationnelle pour le RSSI est celle qui distingue trois niveaux de criticité selon ce que fait l’IA.

**L’IA qui informe** (risque modéré) : elle fournit des données, des analyses, des suggestions. L’humain reste décideur et exécutant. Exemple : un assistant RAG qui résume des documents. En cas de défaillance (hallucination, injection), l’impact est limité si l’utilisateur vérifie. Le risque principal est la fuite de données via les réponses.

**L’IA qui décide** (risque élevé) : elle produit une décision qui influence directement un processus. Exemple : un scoring de fraude qui déclenche une alerte, un tri de CV qui élimine des candidats. En cas de défaillance, l’impact est direct sur des personnes ou des processus. Les risques incluent le biais, le manque d’explicabilité, et la conformité réglementaire (AI Act haut risque, RGPD article 22).

**L’IA qui agit** (risque très élevé) : elle exécute des actions sur le SI ou des systèmes métier. Exemple : un agent qui reset des mots de passe, crée des tickets, envoie des emails, modifie des données. En cas de défaillance ou de compromission, l’impact est immédiat et potentiellement irréversible. C’est le scénario de l’excessive agency. Les contrôles requis sont maximaux : moindre privilège, human-in-the-loop pour les actions critiques, allow-list, kill switch (voir Ch.9).

### 3.3 Erreurs courantes de déploiement

Plusieurs erreurs reviennent systématiquement dans les déploiements IA en entreprise. La première est l’absence de threat model spécifique : « c’est juste un chatbot » sous-estime les risques de fuite de données, d’injection, et d’impact réputationnel. La deuxième est le défaut de RBAC : les droits d’accès du système source ne sont pas reproduits dans le système IA (un utilisateur voit via l’IA des données auxquelles il n’a pas accès directement). La troisième est la surconfiance dans les guardrails du fournisseur : les filtres de sécurité des APIs commerciales sont conçus pour le grand public, pas pour protéger des données sensibles d’entreprise. La quatrième est l’absence de monitoring en production : pas de suivi des requêtes, des réponses, des coûts, des anomalies — ce qui rend la détection d’abus ou de compromission impossible.

-----

## Ch.4 — Modèle de menaces d’un système IA

### 4.1 Les assets à protéger

Un système IA a des assets spécifiques qui s’ajoutent aux assets classiques d’un système d’information.

**Le modèle lui-même** est un asset critique. Il représente un investissement (entraînement, fine-tuning, prompt engineering) et peut contenir des données sensibles mémorisées. Un modèle volé (model extraction) peut être réutilisé par un concurrent ou analysé pour en extraire des informations. Un modèle corrompu (poisoning) peut produire des résultats erronés ou malveillants.

**Les données d’entraînement et de contexte** incluent les datasets de fine-tuning, les documents de la base RAG, les historiques de conversation. Ces données sont souvent plus sensibles que le modèle lui-même — elles contiennent la propriété intellectuelle, les processus métier, et potentiellement des données personnelles.

**Les données utilisateurs** comprennent les prompts, les réponses, les logs de conversation, les metadata. En RGPD, ces données sont des données personnelles si elles permettent d’identifier l’utilisateur — ce qui est le cas dans la grande majorité des déploiements d’entreprise.

**L’infrastructure** inclut les serveurs d’inférence, les bases vectorielles, les serveurs MCP, les pipelines de données. Elle est exposée aux vulnérabilités classiques d’infrastructure plus des vulnérabilités spécifiques (DoS par compute, exfiltration via les logs).

**L’intégrité des décisions** est l’asset souvent oublié : si l’IA influence des décisions métier (scoring de fraude, recommandations, triage), la manipulation de ces décisions a un impact direct sur l’activité.

**La réputation** est l’asset qui rend les dirigeants attentifs : un chatbot d’entreprise qui divulgue des données clients ou qui produit du contenu inapproprié est un incident de réputation qui peut être plus coûteux que l’incident technique lui-même.

### 4.2 Les acteurs de la menace

Les acteurs qui menacent un système IA sont les mêmes que ceux qui menacent tout SI, mais avec des motivations et des capacités adaptées.

**L’attaquant externe** cible le système IA comme vecteur d’entrée (injection pour accéder au SI), comme source de données (exfiltration via le LLM), ou comme cible de manipulation (corruption des résultats). Ses techniques incluent le prompt injection (direct et indirect), l’exploitation de vulnérabilités dans l’infrastructure de serving, et les attaques de supply chain sur les modèles et dépendances.

**L’interne malveillant** a un accès légitime au système et peut injecter des documents empoisonnés dans la base RAG, exfiltrer des données via des requêtes normales en apparence, ou manipuler les données d’entraînement du modèle de fraude pour rendre certains patterns indétectables.

**L’interne négligent** représente la menace la plus fréquente : le collaborateur qui copie des données sensibles dans ChatGPT en version grand public (shadow AI), qui ne vérifie pas les réponses de l’assistant avant de les utiliser, ou qui contourne les procédures de validation.

**Le fournisseur ou tiers compromis** inclut le prestataire avec accès au SharePoint source du RAG (scénario de l’incident dans le fil rouge de NovaSanté), le fournisseur de modèle qui pousse une mise à jour corrompue, le fournisseur de service MCP dont le serveur est compromis.

### 4.3 Les surfaces d’attaque

La surface d’attaque d’un système IA est significativement plus large que celle d’une application web classique.

**Le prompt** est la surface la plus évidente : tout ce que l’utilisateur envoie au modèle. C’est le vecteur du prompt injection direct (jailbreak, manipulation de rôle, encodage).

**Les données de contexte RAG** sont la surface de l’injection indirecte : tout document indexé dans la base vectorielle peut contenir des instructions cachées que le LLM interprétera comme des commandes.

**Les outils et plugins de l’agent** sont la surface de l’excessive agency : chaque outil accessible à l’agent (API AD, ServiceNow, email) est un vecteur d’action potentiellement malveillante.

**Le modèle lui-même** est une surface : les fichiers de modèle au format pickle peuvent exécuter du code arbitraire au chargement (c’est pourquoi le format SafeTensors est devenu la norme de sécurité). Le modèle peut aussi contenir des backdoors insérées pendant l’entraînement.

**La supply chain** (dépendances Python, images Docker, frameworks d’orchestration) hérite de toutes les vulnérabilités classiques de la supply chain logicielle avec une exposition accrue en raison de l’écosystème ML encore jeune et en évolution rapide.

**L’infrastructure classique** ne disparaît pas : le serveur de serving est une application web exposée, la base vectorielle est une base de données, le pipeline de données a des credentials — les vulnérabilités classiques (SSRF, injection SQL, path traversal, désérialisation, RCE) s’appliquent en intégralité.

### 4.4 Cadre structurant : OWASP Top 10 for LLM × MITRE ATLAS × NIST AI RMF

Trois référentiels complémentaires structurent le threat model d’un système IA.

**OWASP Top 10 for LLM Applications (Version 2025, publiée le 18 novembre 2024)** est le référentiel le plus directement opérationnel. Il liste les dix risques de sécurité les plus critiques pour les applications LLM, avec pour chaque risque une description, des exemples, des scénarios d’attaque et des recommandations de prévention. La nomenclature officielle 2025 est : LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. Le mapping vers les chapitres de ce cours est détaillé en Annexe B.

**MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)** est le pendant ML du framework MITRE ATT&CK. Il cartographie les tactiques, techniques et procédures (TTPs) utilisées pour attaquer les systèmes d’IA, avec des études de cas réels. ATLAS est plus large qu’OWASP (il couvre le ML classique en plus des LLMs) et plus structuré en termes de kill chain.

**NIST AI RMF (AI Risk Management Framework)** est le cadre de gestion des risques IA du NIST. Il est moins technique qu’OWASP ou ATLAS mais plus orienté gouvernance et processus. Il définit quatre fonctions (Govern, Map, Measure, Manage) qui structurent l’intégration de la gestion des risques IA dans l’organisation. Le document NIST AI 100-2 (Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations) est la référence technique associée, qui propose une taxonomie complète des attaques sur les systèmes IA prédictifs et génératifs.

L’articulation entre ces trois référentiels est la suivante : OWASP donne les risques prioritaires à traiter pour une application LLM, ATLAS donne le kill chain et les TTPs pour le red teaming, et NIST AI RMF donne le cadre de gouvernance pour structurer l’ensemble. En pratique, un RSSI utilise OWASP pour prioriser les contrôles techniques, ATLAS pour structurer les tests adversariaux, et NIST AI RMF pour intégrer la sécurité IA dans la gouvernance SSI existante.

> **🔵 Fil rouge — Épisode 3**
> Karim utilise le framework OWASP Top 10 for LLM pour cartographier les risques des trois cas d’usage de NovaSanté. Résultat :
> 
> |Risque OWASP                   |RAG santé                                     |Fraude SIEM|Agent help desk                   |
> |-------------------------------|----------------------------------------------|-----------|----------------------------------|
> |LLM01 Prompt Injection         |🔴 Critique (injection indirecte via documents)|🟡 Modéré   |🔴 Critique (injection via tickets)|
> |LLM02 Sensitive Info Disclosure|🔴 Critique (données HDS)                      |🟡 Modéré   |🟡 Modéré                          |
> |LLM06 Excessive Agency         |⚪ N/A                                         |⚪ N/A      |🔴 Critique (actions AD)           |
> |LLM08 Vector/Embedding         |🔴 Critique (RBAC vectoriel)                   |⚪ N/A      |⚪ N/A                             |
> 
> L’assistant RAG santé a le profil de risque données le plus élevé (données HDS, RBAC vectoriel indispensable). L’agent help desk a le profil d’action le plus élevé (il touche l’AD). Le module fraude a le profil de fiabilité le plus élevé (ses décisions impactent des personnes). Trois stratégies de sécurité distinctes à construire.

-----
