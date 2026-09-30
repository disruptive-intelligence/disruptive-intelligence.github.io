---
title: Ch.7 — Data poisoning, RAG poisoning, intégrité des données et attaques sur le ML classique
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie II — Menaces spécifiques aux systèmes IA
  - index.md
---

## 7.1 Data poisoning : corrompre l’entraînement

Le data poisoning consiste à injecter des données malveillantes dans le jeu d’entraînement d’un modèle pour altérer son comportement en production. C’est une attaque particulièrement pernicieuse car elle se produit avant le déploiement — le modèle est corrompu dès sa naissance.

Il existe deux formes principales. Le **poisoning de disponibilité** dégrade la performance globale du modèle (il devient inutilisable ou peu fiable sur l’ensemble des requêtes). Le **poisoning ciblé** (targeted poisoning) altère le comportement du modèle uniquement sur des cas spécifiques choisis par l’attaquant, tout en maintenant une performance normale sur le reste — ce qui le rend beaucoup plus difficile à détecter.

Le **backdoor poisoning** est une variante sophistiquée du poisoning ciblé : l’attaquant insère un « déclencheur » (trigger) dans les données d’entraînement. Le modèle se comporte normalement sauf quand le déclencheur est présent dans l’entrée, auquel cas il produit le résultat voulu par l’attaquant. Un classifieur de spam backdooré pourrait, par exemple, laisser passer tout email contenant un mot-clé spécifique dans un champ caché.

Des chercheurs ont démontré qu’un attaquant disposant de ressources modestes peut empoisonner des datasets web à grande échelle en achetant des domaines expirés référencés dans les datasets d’entraînement, avec aussi peu que 0,001 % des données du dataset suffisant pour induire des défaillances ciblées. Une étude conjointe du UK AI Security Institute et du Alan Turing Institute a montré qu’environ 250 documents malveillants suffisent pour empoisonner efficacement un modèle d’IA générative, indépendamment de la taille du dataset global.

## 7.2 RAG poisoning

Le RAG poisoning est plus immédiat et plus facile que le data poisoning classique car il ne nécessite pas d’accès aux données d’entraînement — il suffit d’un accès en écriture à une source documentaire du RAG (wiki interne, SharePoint, Confluence, base de tickets).

Le scénario type : un attaquant (interne ou prestataire avec accès) modifie un document dans le wiki interne de l’entreprise. Le pipeline RAG réindexe le document modifié. L’assistant commence à donner des réponses basées sur le contenu falsifié. Contrairement au data poisoning qui nécessite un ré-entraînement, le RAG poisoning peut être quasi-instantané (dépendant de la fréquence de réindexation).

Les défenses incluent le contrôle d’accès strict en écriture sur les sources du RAG, un workflow de validation avant indexation (les modifications doivent être approuvées avant d’être accessibles au RAG), le monitoring des modifications sur les sources (alertes sur les changements de documents critiques), la traçabilité des sources dans les réponses (chaque réponse cite les documents utilisés — ce qui permet de vérifier la cohérence), et la vérification d’intégrité (hash des documents au moment de l’indexation, re-vérification périodique).

## 7.3 Attaques sur le ML classique

Les attaques spécifiques au ML classique (supervisé, non supervisé) sont trop souvent négligées dans les formations orientées LLM. Elles sont pourtant directement pertinentes pour les déploiements de détection de fraude, de scoring, et de détection d’anomalies.

**Les adversarial examples (attaques par évasion).** L’attaquant modifie subtilement ses données d’entrée pour tromper le classifieur sans changer la sémantique humaine. Dans le cas d’un détecteur de fraude, un fraudeur peut ajuster les paramètres de sa déclaration (montant, timing, formulation) de manière imperceptible pour un humain mais suffisante pour basculer le scoring en dessous du seuil d’alerte. Ces perturbations peuvent être calculées analytiquement (attaques white-box type FGSM, PGD) ou estimées par tâtonnement (attaques black-box). La défense inclut l’adversarial training (entraîner le modèle sur des exemples adversariaux), le randomized smoothing, et surtout la diversification des features — un modèle trop dépendant d’un petit nombre de features est plus vulnérable.

**Le model stealing (extraction de modèle) — couvert par OWASP LLM10 Unbounded Consumption.** L’OWASP classe le vol de modèle comme risque LLM10, et il ne concerne pas uniquement le ML classique. Pour les LLMs déployés via API, un attaquant peut interroger le modèle de manière répétée avec des entrées soigneusement choisies et utiliser les réponses pour entraîner un modèle « élève » fonctionnellement équivalent (distillation adversariale). Au-delà de la propriété intellectuelle, le modèle volé peut être analysé offline pour concevoir des attaques optimales (adversarial examples calibrés, techniques de jailbreak spécifiques). Pour les modèles propriétaires exposés via API (cas de NovaSanté avec le modèle de scoring de fraude), le risque est double : perte d’avantage concurrentiel et exposition accrue aux attaques adversariales. La défense inclut le rate limiting strict, la limitation des informations dans les réponses (ne pas retourner les scores de confiance exacts, les logits, ou les probabilités par classe), la détection de patterns d’interrogation suspectes (requêtes structurées de type grid search), le watermarking du modèle (marquage traçable dans les prédictions), et la journalisation exhaustive des appels API pour investigation.

**L’inférence d’appartenance (membership inference).** L’attaquant détermine si un échantillon spécifique faisait partie des données d’entraînement du modèle. C’est une atteinte à la vie privée : prouver qu’un individu était dans le dataset d’entraînement d’un modèle médical révèle qu’il avait la pathologie étudiée. Les shadow models (modèles auxiliaires entraînés par l’attaquant pour calibrer la détection) sont la technique dominante. La défense principale est la differential privacy, qui ajoute du bruit calibré pendant l’entraînement pour limiter l’influence de chaque exemple individuel — au prix d’une perte de précision du modèle.

**L’inversion de modèle (model inversion).** L’attaquant tente de reconstruire les données d’entraînement à partir du modèle et de ses sorties. C’est une attaque de confidentialité : un modèle de reconnaissance faciale inversé peut régénérer des approximations des visages utilisés pour l’entraînement. Plus le modèle est complexe et plus il overfitte, plus l’attaque est efficace.

**Le concept drift et le data drift.** Ce ne sont pas des attaques à proprement parler mais des risques de fiabilité avec des implications de sécurité. Le concept drift est l’évolution de la relation entre les features et la cible (les patterns de fraude changent au fil du temps). Le data drift est l’évolution de la distribution des données d’entrée (la population de clients change). Un modèle de détection de fraude qui n’est pas régulièrement réévalué et réentraîné voit sa performance se dégrader silencieusement — les faux négatifs augmentent sans alerte. Le monitoring de la performance en production avec des métriques de drift (PSI, KL divergence) est essentiel.

**Le feature store poisoning.** Dans les architectures ML modernes, les features sont souvent pré-calculées et stockées dans un feature store centralisé. La corruption de ce feature store affecte tous les modèles qui en dépendent. C’est un point de défaillance unique souvent sous-protégé.

> **🔵 Fil rouge — Épisode 6**
> Le module de détection de fraude de NovaSanté utilise un modèle XGBoost entraîné sur 3 ans d’historique de sinistres. Karim identifie deux risques spécifiques : d’une part, le concept drift — les patterns de fraude évoluent et le modèle doit être réévalué tous les trimestres ; d’autre part, le risque d’adversarial evasion — un fraudeur qui comprend les features du modèle (montant, délai de déclaration, fréquence des sinistres) peut ajuster sa fraude pour rester sous le seuil. Karim exige un monitoring de la distribution des scores et un jeu de test adversarial trimestriel.

-----
