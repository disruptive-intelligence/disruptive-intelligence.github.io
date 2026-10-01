---
title: Chapitre 16 — L'intelligence artificielle
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

multiplicateur de menace et de défense

## 16.1 — L'IA comme amplificateur offensif

Microsoft documente dans son MDDR 2025 une cartographie complète des utilisations de l'IA pour augmenter les cyberattaques traditionnelles. Les domaines d'augmentation incluent : le spearphishing automatisé et personnalisé, la reconnaissance automatisée, la génération et le débogage de code malveillant, le développement d'exploits, la génération de domaines d'usurpation, l'automatisation de bots, la création d'identités synthétiques, la gestion de C2, l'obfuscation de malware, et la traduction linguistique pour des campagnes internationales.

Le CSE canadien évalue que « les technologies d'IA amplifient les menaces dans le cyberespace » — la première des cinq tendances structurantes identifiées pour 2025-2026. L'IA abaisse les barrières à l'entrée pour des acteurs moins compétents tout en augmentant l'efficacité des acteurs sophistiqués.

Le CERT-EU anticipe pour 2026 que l'IA sera utilisée à grande échelle dans les opérations de social engineering, avec des campagnes multi-canal orchestrées par IA combinant email, voix et SMS de manière cohérente et personnalisée.

## 16.2 — LLMs malveillants

L'écosystème cybercriminel a développé ses propres outils d'IA générative. **WormGPT** est un LLM sans les garde-fous des modèles commerciaux, capable de générer des emails de phishing, du code malveillant et des scripts d'arnaque. **FraudGPT** est spécialisé dans la fraude. **Xanthorox AI** est présenté comme un système autonome avec ses propres modèles de langage. Ces outils vont du simple jailbreak (contournement des filtres de sécurité des modèles commerciaux) à des systèmes dédiés.

L'impact réel de ces outils doit être évalué avec prudence. Beaucoup sont des arnaques (vendus à des prix élevés avec des capacités exagérées) ou des jailbreaks simples rapidement patchés par les fournisseurs de LLM. Cependant, la tendance de fond est claire : la mise à disposition d'outils d'IA générative sans contraintes de sécurité pour les cybercriminels.

## 16.3 — AI deepfakes : fraude et influence

Les deepfakes — contenus audio et visuels générés par IA imitant de manière réaliste des personnes réelles — posent des risques dans deux domaines.

En **fraude**, les deepfakes vocaux et visuels permettent l'usurpation d'identité à une échelle sans précédent. Le cas Hong Kong (25M USD de virement après un appel vidéo avec un deepfake du directeur financier) est l'exemple le plus documenté. Microsoft note que des profils LinkedIn avec des photos de portrait générées par IA sont utilisés pour du scraping de données ou de l'ingénierie sociale.

En **influence**, les deepfakes d'ancres de journaux télévisés (AI twinning) permettent de diffuser des narratifs étatiques avec un vernis de crédibilité. Microsoft documente l'émergence d'**acteurs AI-first** — des opérateurs d'influence qui privilégient le contenu généré par IA comme stratégie principale plutôt que comme outil secondaire.

## 16.4 — L'IA comme lure et comme cible

L'intérêt du public pour l'IA est exploité par les cybercriminels comme **lure** : faux sites imitant DeepSeek, Kling AI, Canva Dream Lab distribuent des malwares (infostealers, trojans) sous couvert d'outils d'IA gratuits. Les utilisateurs qui cherchent à accéder à des outils d'IA populaires téléchargent à la place des malwares.

L'IA est aussi une **surface d'attaque** émergente. Le **slopsquatting** exploite les hallucinations des LLMs : lorsqu'un modèle d'IA recommande un package logiciel qui n'existe pas, un attaquant crée ce package avec du code malveillant. Les **Rules File Backdoors** ciblent les assistants de code IA en injectant des instructions cachées dans les fichiers de configuration. L'**empoisonnement de modèles** consiste à injecter des données biaisées ou malveillantes dans les datasets d'entraînement.

Des vulnérabilités spécifiques ont été documentées dans les plateformes IA elles-mêmes : CVE dans Langflow (outil d'orchestration IA), vulnérabilités dans les plugins et fonctions connectées aux LLMs. Microsoft consacre une analyse aux nouvelles surfaces d'attaque créées par l'IA — prompts, données et sources de contexte, orchestration, plugins et fonctions, modèles eux-mêmes.

## 16.5 — L'IA dans les opérations d'influence étatiques

Microsoft documente une croissance significative des contenus générés par IA attribués à des adversaires étatiques. La Chine, l'Iran et la Russie utilisent tous des outils d'IA dans leurs opérations d'influence. Les techniques incluent l'**AI twinning** (création de répliques numériques de présentateurs TV de confiance), l'**empoisonnement de données d'entraînement** (injection de contenu biaisé dans les datasets qui informent les modèles d'IA), et le **clonage vocal** pour l'usurpation d'identité.

Google et Microsoft ont documenté l'utilisation de Gemini et ChatGPT par des acteurs étatiques (Chine, Iran, RPDC) pour des tâches de recherche, de rédaction et de traduction dans le cadre d'opérations cyber et d'influence.

## 16.6 — L'IA comme outil défensif

L'IA est également un multiplicateur défensif. Le CERT-EU note avoir « significativement étendu son utilisation de l'automatisation et de l'intelligence artificielle dans ses processus de monitoring et d'analyse » en 2025, élargissant sa capacité de détection. Les applications défensives incluent : la détection d'anomalies comportementales, l'automatisation du triage des alertes SOC, l'enrichissement automatisé des indicateurs, l'analyse de logs à grande échelle, et l'aide à la rédaction de rapports CTI.

Les limites doivent être explicitement reconnues. La **surreliance à l'IA** crée de nouveaux risques : les analystes qui font confiance aux résultats de l'IA sans vérification humaine introduisent des erreurs systémiques. Les **fuites d'information via prompts** sont un risque réel lorsque des données sensibles sont soumises à des LLMs commerciaux. L'**intégrité des modèles** ne peut être présumée — les modèles sont soumis aux mêmes risques supply chain que tout autre logiciel.

## 16.7 — 🔴 Fil rouge : IA augmentée dans la production CTI

> **📌 FIL ROUGE — Épisode 16**
>
> Sophie intègre un outil de CTI augmentée par IA dans son workflow de production — un LLM fine-tuné pour l'analyse de rapports de menace, capable de résumer les publications, d'extraire les IOCs et de proposer des corrélations. Le gain d'efficacité est réel : le traitement de 20 rapports quotidiens passe de 3 heures à 45 minutes.
>
> Mais les limites apparaissent rapidement. L'outil halluciné un lien entre un IOC et un groupe APT qui n'existe pas dans les sources. Un analyste junior reprend cette hallucination dans un draft de note CTI sans vérifier. Sophie intercepte l'erreur lors de la revue. Elle établit une règle : « L'IA est un assistant, pas un analyste. Tout output IA doit être vérifié par un humain avant intégration dans un produit CTI. Les corrélations proposées par l'IA sont des hypothèses à vérifier, jamais des conclusions. »

---
