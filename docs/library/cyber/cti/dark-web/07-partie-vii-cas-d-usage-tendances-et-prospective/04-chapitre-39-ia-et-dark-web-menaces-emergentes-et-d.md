---
title: 'Chapitre 39 — IA et dark web : menaces émergentes et défensives'
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VII — Cas d'usage, tendances et prospective
  - index.md
---

L'**intelligence artificielle générative** transforme l'écosystème dark web depuis 2022-2023. Ce chapitre cartographie les usages observés, en menaces et en défenses, et anticipe les évolutions.

## 39.1 L'arrivée des LLM dans le dark web

L'arrivée publique des LLM (ChatGPT novembre 2022, puis cascade — Claude, Gemini, Llama open source, etc.) a immédiatement été détournée. Plusieurs angles.

**Bypass des garde-fous des LLM commerciaux**. Les LLM mainstream (OpenAI, Anthropic, Google) ont des restrictions contre usages malveillants. Techniques de jailbreaking, prompt injection, role-playing — apparaissent rapidement dans la communauté cybercriminelle. Effectivité variable selon les versions, fenêtres exploitées puis fermées.

**Modèles alternatifs sur dark web**. Émergence de LLM spécifiquement marketés pour usage criminel.

- **WormGPT** (apparu 2023) : version sans garde-fous basée sur GPT-J open source, marketée pour BEC fraud, phishing, malware writing. Vendu en abonnement (~100 USD/mois). Modèle initial fermé après publicité, plusieurs successeurs.
- **FraudGPT** (2023) : focus fraude, carding, social engineering.
- **DarkBERT** (académique, pas malveillant) : modèle entraîné sur dark web pour recherche.
- **Multiples successeurs** : WolfGPT, EscapeGPT, EvilGPT, etc. Marketing principalement, sous le capot souvent simples LLM open source avec prompts adaptés.

**Usage des LLM open source**. Les LLM open source (Llama, Mistral, autres) ne posent pas de restriction d'usage par défaut. Les acteurs sophistiqués les déploient localement et les fine-tunent pour cas criminels.

## 39.2 Les usages offensifs

**Génération de phishing**. LLM produisent emails de phishing en multiples langues, avec qualité linguistique excellente — fin du « phishing avec fautes d'orthographe identifiable ». Personnalisation à grande échelle (mention de détails du destinataire scrapés sur LinkedIn).

**Génération de code malveillant**. LLM aident à écrire malware. Compétence variable — pour code simple, efficace ; pour malware sophistiqué (évasion EDR, anti-analyse avancée), encore limité. Mais les progrès sont rapides.

**Génération de contenu pour social engineering**. Pretexts crédibles, scénarios élaborés, faux profils LinkedIn cohérents.

**Deepfakes vocaux**. Voice cloning à partir de quelques secondes d'audio. Usage : fraude au CEO (faux appel téléphonique du CEO demandant transfert urgent). Cas documentés multiples 2023-2025.

**Deepfakes vidéo**. Plus complexes mais accessibles. Usage : usurpation d'identité en visio-conférence (un employé voit son CEO en visio demandant transfert — c'est un deepfake animé). Incident à grande échelle documenté à Hong Kong début 2024 (Arup, ~25 M USD perdus à un deepfake en visio-conférence).

**Vishing automatisé**. Appels téléphoniques automatisés avec voix IA, conversation interactive. Plus convaincant que les robocalls classiques. En émergence.

**Génération de leak sites et phishing kits**. Création accélérée d'infrastructures cosmétiques.

**Reconnaissance et profilage**. LLM aident à analyser des grandes quantités de données OSINT pour profiler des cibles.

**Translation et adaptation linguistique**. Acteurs russophones produisent emails phishing impeccables en français, anglais, allemand.

## 39.3 Les marchés IA criminels

**Marketplaces**. Plusieurs marketplaces dark web et Telegram listent des **services IA criminels** :

- Génération de phishing emails personnalisés.
- Génération de malware sur commande.
- Voice cloning à la demande.
- Deepfake vidéo à la commande (~50-500 USD selon complexité).
- Faux profils LinkedIn générés (avec photo, historique).
- LLMs sans restrictions par abonnement.

**Prix**. Très accessibles. Phishing kit IA-augmenté : 50-500 USD. Voice cloning : 100-1 000 USD selon qualité voulue. Deepfake vidéo simple : 200-2 000 USD.

**Évolution rapide**. La qualité progresse mensuellement. Le marché, encore embryonnaire en 2023, est mature en 2025.

## 39.4 Les usages défensifs

L'IA n'est pas qu'offensive. Côté défensif, applications croissantes.

**Détection d'anomalies**. ML pour détecter comportements anormaux (fraude, intrusion, exfiltration). Plus performants que règles statiques.

**Analyse de logs à grande échelle**. SIEM augmentés par ML, threat hunting assisté par LLM.

**Classification de threat intelligence**. Tri automatique des alertes, scoring de pertinence, regroupement des indicateurs liés.

**Analyse stylométrique automatisée**. Pour pivoting et corrélation pseudonymes (Ch.29).

**Synthèse de rapports**. LLM aident l'analyste à rédiger rapports plus vite, à synthétiser corpus volumineux.

**Détection de deepfakes**. Outils dédiés (Microsoft Video Authenticator, Intel FakeCatcher, Reality Defender, Hive AI). Course offense/défense permanente.

**Détection de phishing IA-généré**. Outils émergents qui identifient signatures linguistiques de génération automatique. Effectivité variable.

**Veille dark web automatisée**. LLM analysent posts forums, traduisent, classifient. Réduit charge humaine.

**Sandboxing intelligent**. ML pour analyser comportements de fichiers suspects, détecter malware obfusqué.

## 39.5 Les marchés défensifs IA

Côté défense, écosystème commercial structuré.

**Vendors mainstream** intégrant IA : Microsoft Security Copilot, CrowdStrike Charlotte AI, SentinelOne Purple AI, Google Security AI, Palo Alto Cortex avec IA, Recorded Future avec LLM intégré.

**Vendors spécialisés** : entreprises focused sur détection deepfake, sur détection phishing IA, sur threat intelligence avec LLM.

**Open source** : projets variés, performance variable.

**Standards émergents** : initiatives de watermarking (C2PA pour authentification de contenus), provenance des contenus.

## 39.6 Le problème de la prolifération

L'IA criminelle pose un problème structurel : **prolifération vers acteurs moins sophistiqués**.

Avant IA : compromettre une entreprise nécessitait compétences techniques. Phishing efficace requérait talent linguistique. Deepfake nécessitait expertise.

Avec IA : un acteur sans compétences profondes peut produire phishing crédible, malware basique, deepfake convaincant. Le **plancher technique** descend.

**Impact** : explosion potentielle du volume d'attaques. Plus d'attaquants, attaques plus crédibles.

**Mais** : l'IA défensive aussi proliférise. Les organisations sans compétences cyber peuvent maintenant déployer des outils défensifs IA pré-emballés. Course technologique.

**Résultat net** : incertain. Hypothèses possibles : (a) avantage offensif court terme (les défenseurs sont réactifs), puis stabilisation ; (b) avantage défensif long terme (l'IA permet meilleure détection que prévention humaine) ; (c) escalade continue sans déséquilibre net. Les 5 prochaines années répondront.

## 39.7 La menace deepfake spécifique

Les deepfakes méritent un traitement à part car leur impact peut être disproportionné.

**Types** :

- **Fraude financière** : faux CEO en visio demandant transfert. Cas Arup (2024) : ~25 M USD perdus.
- **Désinformation politique** : fausses déclarations de dirigeants pour influencer.
- **Sextorsion** : fausses images/vidéos compromettantes pour chantage. Pratique en croissance contre individus.
- **Diffamation** : faux contenus pour discréditer cibles.
- **Manipulation boursière** : faux contenus déstabilisant titres cotés.

**Défenses** :

- Procédures double-vérification pour transactions critiques (canal indépendant, code secret).
- Sensibilisation employés (recognize that deepfakes happen).
- Outils de détection technique.
- Watermarking des contenus officiels (provenance vérifiable).
- Cadre réglementaire émergent (UE AI Act 2024, obligations de transparence).

**Limites** : la course détection/génération est asymétrique. Les générateurs s'améliorent plus vite que les détecteurs. Approche structurée : ne pas se reposer uniquement sur détection technique, ajouter procédures organisationnelles.

## 39.8 Les hallucinations et leurs implications criminelles

Les LLM **hallucinent** — produisent affirmations confiantes mais incorrectes. Pour un criminel utilisateur, conséquence ambivalente.

**Pour le criminel** : LLM peut produire malware qui ne fonctionne pas, conseils techniques erronés, identifiants fictifs. Réduit la fiabilité de l'IA criminelle pour acteurs peu sophistiqués qui ne peuvent pas vérifier.

**Pour la défense** : signaux d'IA dans phishing détectables si hallucinations. Email de phishing qui mentionne « votre commande N° 47823-XYZ chez Lufthansa » alors que la victime n'a jamais commandé chez Lufthansa = signal IA générique pas finement personnalisé.

**Évolution** : les hallucinations diminuent avec versions. RAG (Retrieval Augmented Generation) atténue. Mais ne disparaîtront pas totalement.

## 39.9 Le cadre réglementaire

**UE AI Act (2024)**. Cadre majeur. Obligations de transparence, classification de risques, interdictions de certains usages (manipulation, social scoring), exigences pour systèmes high-risk. Impact sur produits commerciaux IA, peu d'impact direct sur usage criminel (qui est déjà illégal).

**US Executive Order on AI (octobre 2023)**. Cadre fédéral, focus sur sécurité IA, divulgation des modèles puissants.

**Initiatives sectorielles**. Standards C2PA, watermarking, partenariats public-privé.

**Pour l'analyste** : connaître ces cadres, anticiper les obligations qu'ils créent pour les organisations clients (déploiement IA légal, gestion des risques).

## 39.10 Anticipation 2026-2030

Tendances probables.

**Multi-modalité IA**. Combinaison voix + vidéo + texte cohérent dans deepfakes. Contenus indistinguables du réel pour œil humain non-formé.

**Agents IA autonomes**. L'IA capable d'exécuter chaînes d'actions complexes (recon, exploitation, exfiltration). Émergent en 2024-2025, mature potentiel 2026-2028. Implications offensives : attaques largement automatisées. Implications défensives : agents défensifs équivalents.

**LLMs domain-specific criminels**. Modèles fine-tunés sur larges corpus criminels (malware code, phishing samples, fraud schemes). Performance technique en hausse.

**IA dans investigations défensives**. Analystes augmentés par agents qui automatisent collecte, corrélation, première analyse — humain valide et oriente.

**Régulation accrue**. Watermarking obligatoire pour contenus IA (US, UE en discussion). Obligations de provenance.

**Course armements**. Pas d'équilibre attendu — chaque progrès offensif appelle progrès défensif et vice versa.

Pour l'analyste actuel, **rester à jour** sur l'évolution IA est devenu une compétence centrale. Les outils et menaces de 2025 ne seront pas ceux de 2027.

---
