---
title: 'Ch.1 — Intelligence artificielle : concepts fondamentaux'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie I — Fondations IA pour le professionnel cyber
  - index.md
---

## 1.1 Qu’est-ce que l’intelligence artificielle ?

L’intelligence artificielle désigne un ensemble de techniques permettant à des systèmes informatiques de reproduire — ou de simuler — des comportements associés à l’intelligence humaine : raisonnement, planification, apprentissage, perception, génération de contenu. Le terme est vaste et recouvre des réalités très différentes, du simple classifieur de spam au grand modèle de langage capable de rédiger un rapport ou de générer du code.

Pour le professionnel de la cybersécurité, la première chose à comprendre est que le mot « intelligence » est trompeur. Un modèle d’IA ne comprend rien au sens humain du terme. Il manipule des distributions statistiques sur des données. Un LLM (Large Language Model) prédit le token suivant le plus probable dans une séquence, compte tenu de milliards de paramètres ajustés lors de l’entraînement. Il n’a pas de modèle interne du monde, pas de conscience, pas d’intention. Cela a des conséquences directes en sécurité : un modèle ne « sait » pas qu’il divulgue un secret — il produit la suite statistiquement la plus probable, qui peut très bien inclure un mot de passe vu à l’entraînement.

Le règlement européen sur l’intelligence artificielle (AI Act, entré en vigueur le 1er août 2024) définit un système d’IA comme un système basé sur une machine, conçu pour fonctionner avec des niveaux d’autonomie variables et qui peut, pour des objectifs explicites ou implicites, générer des sorties telles que des prédictions, des recommandations ou des décisions qui influencent des environnements physiques ou virtuels. Cette définition large englobe aussi bien le ML classique que l’IA générative.

## 1.2 Apprentissage automatique (Machine Learning)

Le Machine Learning est la branche de l’IA où le système apprend à partir de données plutôt que d’être programmé par des règles explicites. On distingue trois paradigmes fondamentaux.

**L’apprentissage supervisé** reçoit des données étiquetées (exemples avec réponse attendue) et apprend à reproduire l’association entrée → sortie. C’est le paradigme dominant en production pour la classification (spam/non-spam, fraude/légitime, malware/bénin) et la régression (scoring de risque, estimation de coût). Le modèle est entraîné sur un jeu de données historiques puis évalué sur un jeu de test séparé. Sa performance dépend directement de la qualité, de la représentativité et de l’intégrité des données d’entraînement — ce qui en fait une cible directe pour les attaques de data poisoning (voir Ch.7).

**L’apprentissage non supervisé** travaille sur des données non étiquetées et cherche des structures cachées : clustering (regrouper des comportements similaires), détection d’anomalies (identifier les comportements déviants par rapport à un modèle de normalité), réduction de dimensionnalité. En cybersécurité, c’est le paradigme du UEBA (User and Entity Behavior Analytics) : on modélise le comportement « normal » d’un utilisateur ou d’une entité, puis on alerte quand un comportement sort significativement de cette normalité. La limite fondamentale est la définition de « normal » : un modèle entraîné sur des données déjà compromises intégrera le comportement de l’attaquant comme normal.

**L’apprentissage par renforcement** place un agent dans un environnement où il prend des actions et reçoit des récompenses ou des pénalités. Il apprend par essai-erreur à maximiser la récompense cumulée. Ce paradigme est moins courant en cybersécurité opérationnelle mais sous-tend l’alignement des LLMs via RLHF (Reinforcement Learning from Human Feedback) : des évaluateurs humains notent les réponses du modèle, et ces notes servent de signal de récompense pour ajuster le comportement du modèle. C’est l’un des principaux mécanismes par lesquels les fournisseurs de LLMs tentent de rendre leurs modèles plus sûrs — mais il est contournable par les techniques de jailbreak (voir Ch.5).

## 1.3 Deep Learning et réseaux de neurones

Le Deep Learning est un sous-ensemble du ML qui utilise des réseaux de neurones à multiples couches (d’où le « deep »). Chaque couche transforme les données d’entrée en représentations de plus en plus abstraites. Les architectures clés pour la sécurité sont les suivantes.

Les **réseaux de neurones convolutifs (CNN)** excellent dans le traitement d’images et sont utilisés en cybersécurité pour l’analyse de malware (visualisation des binaires comme images, détection de patterns visuels dans le trafic réseau).

Les **réseaux récurrents (RNN/LSTM)** traitent des séquences temporelles et ont été utilisés pour la détection d’anomalies dans les logs et le trafic réseau avant d’être largement supplantés par les Transformers.

Les **Transformers** constituent l’architecture dominante depuis 2017. Leur mécanisme d’attention permet de traiter des séquences en parallèle et de capturer des dépendances à longue distance. Tous les LLMs modernes (GPT-4, Claude, Gemini, Mistral, Llama) sont des variantes de l’architecture Transformer. Le mécanisme d’attention est aussi ce qui rend les LLMs vulnérables à certaines attaques : comme le modèle pondère l’importance de chaque token dans le contexte, un attaquant peut placer des instructions malveillantes à des positions stratégiques pour maximiser leur influence sur la sortie.

## 1.4 Les grands modèles de langage (LLM)

Un LLM est un modèle de type Transformer pré-entraîné sur des quantités massives de texte (des centaines de milliards de tokens, soit une fraction significative du web indexé). Il encode les patterns statistiques du langage dans ses paramètres (les « poids » du réseau). Plusieurs concepts sont essentiels pour le professionnel cybersécurité.

**Le token** est l’unité de base du traitement. Un token n’est pas un mot : c’est un fragment de texte (typiquement 3 à 4 caractères en anglais, parfois moins en français). « Cybersécurité » peut être décomposé en 3 ou 4 tokens. Les coûts d’utilisation, les limites de contexte et les métriques de performance se mesurent en tokens. Un prompt injection bien conçu exploite la tokenisation pour contourner les filtres (par exemple en encodant des instructions en base64 ou en utilisant des caractères Unicode spéciaux qui se tokenisent différemment).

**La fenêtre de contexte** est la quantité maximale de tokens que le modèle peut traiter en une seule fois (entrée + sortie). En 2025-2026, les fenêtres courantes vont de 8 000 tokens (modèles légers) à 200 000 tokens (Claude, GPT-4 Turbo) voire 1 million (Gemini). Tout ce qui est dans la fenêtre de contexte influence la réponse — y compris les instructions système, les documents RAG injectés, et les messages précédents. C’est précisément ce qui rend l’injection indirecte possible : un document malveillant placé dans le contexte peut détourner le comportement du modèle.

**La température** est un paramètre qui contrôle l’aléatoire de la génération. À température 0, le modèle est quasi-déterministe (il choisit toujours le token le plus probable). À température élevée (0.8-1.0), les réponses sont plus variées et créatives mais aussi plus sujettes aux hallucinations. En production sécurisée, une température basse est généralement préférable pour la fiabilité et la reproductibilité des réponses.

**L’hallucination** est la production par le modèle de contenu factuellement faux mais formulé avec assurance. Le modèle ne « ment » pas — il produit la suite la plus probable selon ses paramètres, même quand ses paramètres ne contiennent pas l’information correcte. En contexte de sécurité, une hallucination peut être dangereuse : un assistant RAG juridique qui invente une jurisprudence, un outil de tri d’alertes qui corrèle avec un IOC inexistant. C’est l’une des raisons pour lesquelles la vérification humaine reste indispensable.

**La mémorisation (memorization)** est un phénomène où le modèle a retenu et peut régurgiter des fragments exacts de ses données d’entraînement. Ce n’est pas du « stockage » au sens classique — les données ne sont pas dans une base interrogeable — mais les poids du réseau encodent suffisamment d’information pour reconstruire certains passages textuels. Des chercheurs ont démontré que des modèles comme GPT-2 et GPT-3 pouvaient restituer des adresses email, des numéros de téléphone et des fragments de code source issus de leurs données d’entraînement. C’est un risque majeur pour la confidentialité, en particulier dans le cas de modèles fine-tunés sur des données d’entreprise (voir Ch.6).

**Les guardrails** sont des mécanismes de sécurité intégrés au modèle ou ajoutés en surcouche pour filtrer les entrées et les sorties. Ils comprennent l’alignement via RLHF, les instructions système (system prompts), les filtres de contenu, et les classificateurs de sécurité. Ils constituent une défense nécessaire mais insuffisante — l’ensemble de la communauté de red teaming IA démontre régulièrement que les guardrails peuvent être contournés par des techniques de jailbreak sophistiquées (voir Ch.14).

**Le model collapse** désigne la dégradation de performance d’un modèle entraîné (ou fine-tuné) sur des données elles-mêmes générées par des modèles IA. À mesure que le web se remplit de contenu synthétique, les futurs modèles entraînés sur ces données risquent de perdre en diversité et en qualité. Ce phénomène est encore émergent mais constitue un facteur de risque à moyen terme pour la fiabilité des systèmes IA.

## 1.5 ML classique vs IA générative

deux mondes, deux profils de risque

En entreprise, les deux types de systèmes coexistent et continueront de coexister. Le ML classique (forêts aléatoires, gradient boosting, SVM, réseaux de neurones classiques) reste dominant pour les tâches de classification, de scoring et de détection d’anomalies. L’IA générative (LLMs, modèles de diffusion pour l’image) est utilisée pour la génération de contenu, l’analyse de texte, l’assistance, et de plus en plus comme couche d’orchestration via les agents.

Les profils de risque sont sensiblement différents. Le ML classique est vulnérable aux adversarial examples (perturbations calculées pour tromper le classifieur), au data poisoning (corruption des données d’entraînement), au model stealing (extraction des paramètres par interrogation répétée), et au concept drift (évolution naturelle des données qui dégrade la performance sans qu’on le détecte). L’IA générative hérite de ces risques mais y ajoute le prompt injection (direct et indirect), l’exfiltration de données via les réponses, les hallucinations, et l’excessive agency dans le cas des agents. Le Ch.7 détaille les attaques spécifiques au ML classique, souvent négligées dans les formations orientées LLM.

> **🔵 Fil rouge — Épisode 1**
> Karim reçoit la commande du COMEX de NovaSanté : « On veut de l’IA partout, les concurrents ont un chatbot pour leurs gestionnaires, un système anti-fraude, et un help desk automatisé — on veut la même chose en 12 mois. » Karim note immédiatement que les trois cas d’usage couvrent les deux mondes : le module anti-fraude repose sur du ML classique (gradient boosting pour le scoring de sinistres + enrichissement LLM pour l’analyse textuelle des déclarations), tandis que l’assistant RAG et l’agent help desk sont de l’IA générative pure. Deux profils de risque radicalement différents. Sa première action : refuser de traiter « l’IA » comme un bloc monolithique et exiger un threat model par cas d’usage.

-----
