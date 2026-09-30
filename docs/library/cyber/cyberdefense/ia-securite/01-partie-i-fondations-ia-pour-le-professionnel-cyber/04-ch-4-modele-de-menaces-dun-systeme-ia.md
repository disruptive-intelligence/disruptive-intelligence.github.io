---
title: Ch.4 — Modèle de menaces d’un système IA
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
up:
- - IA & sécurité
  - ../index.md
- - Partie I — Fondations IA pour le professionnel cyber
  - index.md
---

## 4.1 Les assets à protéger

Un système IA a des assets spécifiques qui s’ajoutent aux assets classiques d’un système d’information.

**Le modèle lui-même** est un asset critique. Il représente un investissement (entraînement, fine-tuning, prompt engineering) et peut contenir des données sensibles mémorisées. Un modèle volé (model extraction) peut être réutilisé par un concurrent ou analysé pour en extraire des informations. Un modèle corrompu (poisoning) peut produire des résultats erronés ou malveillants.

**Les données d’entraînement et de contexte** incluent les datasets de fine-tuning, les documents de la base RAG, les historiques de conversation. Ces données sont souvent plus sensibles que le modèle lui-même — elles contiennent la propriété intellectuelle, les processus métier, et potentiellement des données personnelles.

**Les données utilisateurs** comprennent les prompts, les réponses, les logs de conversation, les metadata. En RGPD, ces données sont des données personnelles si elles permettent d’identifier l’utilisateur — ce qui est le cas dans la grande majorité des déploiements d’entreprise.

**L’infrastructure** inclut les serveurs d’inférence, les bases vectorielles, les serveurs MCP, les pipelines de données. Elle est exposée aux vulnérabilités classiques d’infrastructure plus des vulnérabilités spécifiques (DoS par compute, exfiltration via les logs).

**L’intégrité des décisions** est l’asset souvent oublié : si l’IA influence des décisions métier (scoring de fraude, recommandations, triage), la manipulation de ces décisions a un impact direct sur l’activité.

**La réputation** est l’asset qui rend les dirigeants attentifs : un chatbot d’entreprise qui divulgue des données clients ou qui produit du contenu inapproprié est un incident de réputation qui peut être plus coûteux que l’incident technique lui-même.

## 4.2 Les acteurs de la menace

Les acteurs qui menacent un système IA sont les mêmes que ceux qui menacent tout SI, mais avec des motivations et des capacités adaptées.

**L’attaquant externe** cible le système IA comme vecteur d’entrée (injection pour accéder au SI), comme source de données (exfiltration via le LLM), ou comme cible de manipulation (corruption des résultats). Ses techniques incluent le prompt injection (direct et indirect), l’exploitation de vulnérabilités dans l’infrastructure de serving, et les attaques de supply chain sur les modèles et dépendances.

**L’interne malveillant** a un accès légitime au système et peut injecter des documents empoisonnés dans la base RAG, exfiltrer des données via des requêtes normales en apparence, ou manipuler les données d’entraînement du modèle de fraude pour rendre certains patterns indétectables.

**L’interne négligent** représente la menace la plus fréquente : le collaborateur qui copie des données sensibles dans ChatGPT en version grand public (shadow AI), qui ne vérifie pas les réponses de l’assistant avant de les utiliser, ou qui contourne les procédures de validation.

**Le fournisseur ou tiers compromis** inclut le prestataire avec accès au SharePoint source du RAG (scénario de l’incident dans le fil rouge de NovaSanté), le fournisseur de modèle qui pousse une mise à jour corrompue, le fournisseur de service MCP dont le serveur est compromis.

## 4.3 Les surfaces d’attaque

La surface d’attaque d’un système IA est significativement plus large que celle d’une application web classique.

**Le prompt** est la surface la plus évidente : tout ce que l’utilisateur envoie au modèle. C’est le vecteur du prompt injection direct (jailbreak, manipulation de rôle, encodage).

**Les données de contexte RAG** sont la surface de l’injection indirecte : tout document indexé dans la base vectorielle peut contenir des instructions cachées que le LLM interprétera comme des commandes.

**Les outils et plugins de l’agent** sont la surface de l’excessive agency : chaque outil accessible à l’agent (API AD, ServiceNow, email) est un vecteur d’action potentiellement malveillante.

**Le modèle lui-même** est une surface : les fichiers de modèle au format pickle peuvent exécuter du code arbitraire au chargement (c’est pourquoi le format SafeTensors est devenu la norme de sécurité). Le modèle peut aussi contenir des backdoors insérées pendant l’entraînement.

**La supply chain** (dépendances Python, images Docker, frameworks d’orchestration) hérite de toutes les vulnérabilités classiques de la supply chain logicielle avec une exposition accrue en raison de l’écosystème ML encore jeune et en évolution rapide.

**L’infrastructure classique** ne disparaît pas : le serveur de serving est une application web exposée, la base vectorielle est une base de données, le pipeline de données a des credentials — les vulnérabilités classiques (SSRF, injection SQL, path traversal, désérialisation, RCE) s’appliquent en intégralité.

## 4.4 Cadre structurant

OWASP Top 10 for LLM × MITRE ATLAS × NIST AI RMF

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
