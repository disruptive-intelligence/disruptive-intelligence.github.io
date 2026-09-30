---
title: 'Ch.8 — Supply chain IA : modèles, dépendances et datasets'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie II — Menaces spécifiques aux systèmes IA
  - index.md
---

## 8.1 Les vecteurs spécifiques à l’IA

La supply chain IA hérite de tous les risques de la supply chain logicielle classique (dépendances vulnérables, images Docker compromises, registres non vérifiés) mais y ajoute des vecteurs propres.

**Les modèles téléchargés.** Hugging Face est le GitHub des modèles ML — des dizaines de milliers de modèles disponibles en téléchargement. Le risque principal est le format de sérialisation : le format pickle (par défaut pour PyTorch) permet l’exécution de code arbitraire au chargement du modèle. Un modèle malveillant au format pickle peut installer une backdoor, exfiltrer des données, ou compromettre le serveur au moment même où il est chargé en mémoire. Le format SafeTensors, développé par Hugging Face, stocke uniquement les tenseurs (poids numériques) sans aucune capacité d’exécution de code — c’est le format obligatoire en production sécurisée. En 2024, des chercheurs de JFrog ont identifié des modèles malveillants sur Hugging Face contenant des backdoors silencieuses ciblant les data scientists.

**Les dépendances Python ML.** L’écosystème ML Python est vaste et en évolution rapide — PyTorch, TensorFlow, LangChain, LlamaIndex, transformers, sentence-transformers, et des centaines de bibliothèques auxiliaires. Les CVE sont fréquentes. LangChain en particulier a connu plusieurs vulnérabilités critiques (RCE via l’exécution de code arbitraire dans certains modules, path traversal). La vitesse de publication des correctifs varie considérablement d’un projet à l’autre.

**Les datasets publics.** Les datasets d’entraînement téléchargés depuis des sources publiques (Hugging Face Datasets, Kaggle, archives universitaires) peuvent contenir des données empoisonnées, biaisées, ou non conformes (données personnelles collectées sans consentement). La provenance et l’intégrité des datasets sont rarement vérifiées.

**Les plugins et connecteurs.** Chaque plugin LangChain, chaque serveur MCP, chaque connecteur d’agent est une dépendance avec ses propres permissions et vulnérabilités. Un plugin mal codé peut ouvrir une SSRF, une RCE, ou une exfiltration de données.

**Les images Docker de serving.** Les images Docker pour Ollama, vLLM, TGI sont souvent utilisées telles quelles sans vérification. Elles peuvent contenir des vulnérabilités dans les dépendances système, des configurations par défaut non sécurisées, ou des composants obsolètes.

**Le slopsquatting.** C’est un vecteur émergent identifié en 2025 : quand un LLM génère du code qui importe un package inexistant (hallucination de nom de package), un attaquant peut créer un package malveillant portant ce nom sur PyPI ou npm. Les développeurs qui exécutent le code généré installent alors le package malveillant. Ce risque est directement lié au Ch.18 sur le code AI-generated.

## 8.2 Défenses supply chain

Les défenses s’organisent en plusieurs niveaux. SafeTensors uniquement en production (rejeter tout modèle au format pickle, ggml non vérifié, ou format propriétaire non audité). SCA (Software Composition Analysis) sur les dépendances Python — Snyk, Dependabot, pip-audit — avec alertes sur les CVE critiques. Checksums et signatures des modèles au téléchargement. Model registry interne (un registre privé de modèles validés, versionné, avec contrôle d’accès). Audit des plugins et connecteurs avant déploiement. Scan des images Docker (Trivy, Grype). SBOM (Software Bill of Materials) incluant les composants IA (modèles, datasets, frameworks). Et veille active sur les vulnérabilités des composants ML — les flux de CVE classiques ne couvrent pas toujours les bibliothèques ML.

-----
