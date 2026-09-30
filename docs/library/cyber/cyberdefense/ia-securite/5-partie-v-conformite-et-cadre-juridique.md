---
title: PARTIE V — CONFORMITÉ ET CADRE JURIDIQUE
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
chapter: 5
chapters: 7
---

## Ch.19 — RGPD et traitements IA

### 19.1 Base légale par traitement IA

Tout traitement de données personnelles dans un système IA doit reposer sur une base légale (article 6 du RGPD). Les bases légales mobilisables varient selon le cas d’usage.

**L’intérêt légitime** est la base la plus fréquemment invoquée pour les traitements IA en entreprise (détection de fraude, amélioration de service, optimisation de processus). Il suppose un intérêt réel et légitime de l’entreprise, la nécessité du traitement IA (pas de moyen moins intrusif pour atteindre le même résultat), et la mise en balance avec les droits des personnes (le traitement ne porte pas une atteinte disproportionnée). La CNIL a précisé en 2025 qu’un intérêt commercial constitue un intérêt légitime, à condition que le traitement soit nécessaire et proportionné. À l’inverse, le développement de systèmes catégoriquement interdits par d’autres réglementations (comme l’AI Act) ne peut pas reposer sur l’intérêt légitime.

**Le consentement** est requis dans certains cas spécifiques (profilage à des fins marketing, traitement de données sensibles sauf exceptions). Il doit être libre, spécifique, éclairé et univoque. Dans un contexte employeur-employé, le caractère « libre » du consentement est souvent contesté.

**L’exécution d’un contrat** peut fonder un traitement IA directement lié à l’exécution du service contractuel (un assistant pour les gestionnaires de sinistres qui traite les données des sinistres dans le cadre du contrat d’assurance).

### 19.2 Minimisation et DPIA

Le principe de minimisation (article 5.1.c) exige de ne traiter que les données adéquates, pertinentes et limitées à ce qui est nécessaire. En IA, cela signifie ne pas indexer toute la base RH dans le RAG si seules les fiches de poste sont nécessaires, ne pas conserver les historiques de conversation au-delà de la durée nécessaire, et ne pas utiliser de données personnelles réelles quand des données synthétiques ou anonymisées suffisent.

La DPIA (Data Protection Impact Assessment / AIPD en français) est obligatoire pour les traitements susceptibles d’engendrer un risque élevé pour les droits et libertés des personnes. La CNIL considère que la réalisation d’une AIPD est présumée nécessaire pour le déploiement de tout système d’IA à haut risque au sens de l’AI Act dès lors qu’il implique des données personnelles, et que le développement de modèles de fondation ou de systèmes d’IA à usage général nécessite dans la majorité des cas une AIPD.

L’AIPD peut s’articuler avec la documentation exigée par l’AI Act : la CNIL encourage la réutilisation d’éléments entre les deux cadres pour éviter la redondance.

### 19.3 Sous-traitance et transferts

L’utilisation d’une API LLM cloud constitue un traitement de sous-traitance au sens du RGPD. Un DPA (Data Processing Agreement, article 28) est obligatoire entre le responsable de traitement (l’entreprise) et le sous-traitant (le fournisseur de l’API). Le DPA doit couvrir la finalité et la durée du traitement, les catégories de données traitées, les obligations du sous-traitant (sécurité, confidentialité, notification de violation), les droits d’audit, et les conditions de sous-sous-traitance.

Si le fournisseur est américain (OpenAI, Anthropic, Google), le traitement implique un transfert hors UE. Depuis l’invalidation du Privacy Shield (arrêt Schrems II, 2020) et l’adoption du EU-US Data Privacy Framework (DPF, 2023), les transferts vers les US reposent sur le DPF pour les entreprises certifiées, ou sur des SCC (Standard Contractual Clauses) avec évaluation d’impact du transfert. Le DPF fait l’objet de contestations juridiques et sa pérennité n’est pas garantie — un « Schrems III » est possible.

Pour les données de santé (HDS), les contraintes sont renforcées : l’hébergeur doit être certifié HDS, ce qui exclut de fait la plupart des fournisseurs de LLM cloud pour un traitement on-premise obligatoire (c’est le cas de l’assistant RAG de NovaSanté).

### 19.4 Droits des personnes et décisions automatisées

L’article 22 du RGPD donne aux personnes le droit de ne pas faire l’objet d’une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou des effets significatifs similaires. Le module de détection de fraude de NovaSanté est directement concerné : un scoring qui déclenche le rejet automatique d’un sinistre est une décision automatisée au sens de l’article 22.

Les obligations incluent le droit d’obtenir une explication de la décision (ce qui suppose une forme d’explicabilité du modèle), le droit de contester la décision et d’obtenir une intervention humaine, et la nécessité d’une base légale spécifique (consentement explicite ou nécessité pour l’exécution du contrat).

Le droit d’effacement dans un modèle fine-tuné est une question juridique ouverte : si des données personnelles sont mémorisées dans les poids du modèle, le droit d’effacement (article 17) implique-t-il un ré-entraînement du modèle ? La CNIL a indiqué en 2025 que selon les cas, elle pourrait exiger le ré-entraînement ou la suppression du modèle en cas de violation de données avérée.

### 19.5 Statut RGPD du modèle et vraisemblance de réidentification

La CNIL a publié en juillet 2025 une méthodologie spécifique pour évaluer si un modèle d’IA entre dans le champ du RGPD. Le principe : un modèle entraîné sur des données personnelles peut être considéré comme anonyme (hors RGPD) uniquement si la vraisemblance de réidentification de personnes physiques à partir du modèle est insignifiante. Si cette vraisemblance est non négligeable — ce qui est le cas dès que des techniques d’extraction, d’inférence d’appartenance ou d’inversion du modèle peuvent révéler des données personnelles avec des moyens raisonnables — le RGPD s’applique pleinement au modèle lui-même.

Cette logique a des conséquences directes pour le praticien. Tout modèle fine-tuné sur des données personnelles doit faire l’objet d’une évaluation documentée de la vraisemblance de réidentification. Cette évaluation doit être régulièrement réévaluée, car l’état de l’art en matière de techniques d’extraction évolue — une extraction jugée improbable aujourd’hui peut devenir réalisable demain. Le fournisseur doit prévoir des modalités de remontée d’information par les utilisateurs en cas d’incident (extraction inattendue de données personnelles) et gérer l’incident comme une violation de données potentielle (documentation, notification CNIL dans les 72 heures si risque pour les personnes, information des personnes si risque élevé).

Cette approche est directement cohérente avec les attaques de membership inference, model inversion et extraction de données détaillées au Ch.7. Le threat model d’un système IA doit inclure explicitement la vraisemblance de réidentification comme risque à évaluer et à surveiller dans le temps (voir aussi l’Annexe C — checklist d’exploitation).

-----

## Ch.20 — AI Act : classification, obligations et mise en conformité

### 20.1 Les quatre niveaux de risque

L’AI Act (Règlement UE 2024/1689) classe les systèmes d’IA en quatre niveaux de risque.

**Risque inacceptable** → interdit. La liste inclut la notation sociale (social scoring), la manipulation subliminale, l’exploitation de vulnérabilités de groupes spécifiques, la reconnaissance faciale en temps réel dans l’espace public par les forces de l’ordre (sauf exceptions), et l’inférence d’émotions sur le lieu de travail ou dans l’éducation (sauf raisons médicales ou de sécurité).

**Risque élevé** → conformité stricte. Les systèmes listés à l’Annexe III incluent : biométrie, infrastructures critiques, éducation et formation professionnelle, emploi et gestion du personnel, accès aux services essentiels (banque, assurance), forces de l’ordre, migration et contrôle aux frontières, administration de la justice. Pour NovaSanté, le module de scoring de fraude (qui influence des décisions sur des prestations d’assurance) pourrait relever du « risque élevé » selon l’interprétation de l’accès aux services essentiels.

**Risque limité** → obligations de transparence. Les systèmes qui interagissent avec des personnes (chatbots) doivent informer l’utilisateur qu’il interagit avec une IA. Les contenus générés par IA (texte, image, audio, vidéo) doivent être marqués comme tels.

**Risque minimal** → pas d’obligations spécifiques. La grande majorité des systèmes IA en entreprise relèvent de cette catégorie.

### 20.2 Calendrier d’application (à date)

Le calendrier de référence, tel qu’indiqué par la Commission européenne, prévoit l’entrée en vigueur le 1er août 2024, les pratiques interdites et les obligations d’AI literacy applicables depuis le 2 février 2025, les obligations GPAI (General Purpose AI) applicables depuis le 2 août 2025, l’application générale (dont les obligations pour les systèmes haut risque) au 2 août 2026, et certaines règles haut risque embarquées dans des produits réglementés jusqu’au 2 août 2027.

> **⚠️ Point de vigilance**
> Des propositions d’ajustement de l’implémentation et des standards techniques ont été discutées fin 2025 et début 2026. La Commission européenne a notamment proposé un paquet de simplification pouvant décaler le calendrier des règles applicables aux systèmes haut risque jusqu’à 16 mois supplémentaires. Le calendrier ci-dessus est le calendrier de référence à date mais reste susceptible d’ajustements d’implémentation. Le praticien doit suivre les publications de l’AI Office et des autorités nationales (en France, la CNIL se positionne pour assumer le rôle d’autorité de contrôle pour l’AI Act).

### 20.3 Obligations pour les systèmes haut risque

Les systèmes haut risque doivent respecter des exigences strictes : système de gestion des risques, gouvernance des données, documentation technique détaillée, journalisation (logging), transparence et information des déployeurs, supervision humaine, exactitude, robustesse et cybersécurité, et évaluation de conformité (auto-évaluation ou par un organisme notifié selon les cas). Le marquage CE est requis avant la mise sur le marché. Les sanctions peuvent atteindre 35 M€ ou 7 % du CA mondial.

### 20.4 Obligations GPAI

Les fournisseurs de modèles GPAI (General Purpose AI — les modèles de fondation comme GPT-4, Claude, Gemini, Mistral Large) ont des obligations spécifiques de documentation technique, de respect du droit d’auteur, de publication d’un résumé du contenu d’entraînement, et de coopération avec les autorités. Les modèles GPAI à risque systémique (dépassant un seuil de compute d’entraînement) ont des obligations renforcées d’évaluation et de reporting.

-----

## Ch.21 — Propriété intellectuelle, secret des affaires, contrats fournisseurs et articulation NIS2/DORA/HDS

### 21.1 Propriété intellectuelle des outputs IA

En droit français, une œuvre est protégée par le droit d’auteur si elle est originale et créée par un humain. Le statut juridique des contenus générés par IA est incertain : un texte, une image, ou un code entièrement généré par une IA sans intervention créative humaine significative n’est probablement pas protégeable. En pratique, cela signifie que les contenus produits par l’IA de l’entreprise ne bénéficient pas nécessairement de la protection du droit d’auteur — un concurrent pourrait les réutiliser.

Les données d’entraînement posent un problème inverse : les modèles sont entraînés sur des œuvres protégées et peuvent en régurgiter des fragments. Les procès en cours (NYT vs OpenAI, Getty vs Stability AI) portent précisément sur cette question. Le risque pour l’entreprise est la contrefaçon involontaire si un modèle produit du contenu substantiellement similaire à une œuvre protégée présente dans ses données d’entraînement.

### 21.2 Secret des affaires

Les données stratégiques (plans commerciaux, algorithmes propriétaires, données de R&D) ne doivent jamais transiter par un LLM cloud sans garanties contractuelles fortes. Le secret des affaires (directive 2016/943 transposée en droit français) protège les informations qui ont une valeur commerciale parce qu’elles sont secrètes et qui font l’objet de mesures de protection raisonnables. L’envoi de ces informations à un LLM cloud peut compromettre le caractère « secret » si les mesures de protection sont jugées insuffisantes.

### 21.3 Clauses essentielles des contrats fournisseurs IA

Lors de la contractualisation avec un fournisseur d’IA (API, modèle, plateforme), les clauses critiques incluent la propriété des outputs (qui possède les contenus générés ?), l’utilisation des inputs pour l’entraînement (les prompts et les données envoyées sont-ils utilisés pour améliorer le modèle ? possibilité d’opt-out ?), la confidentialité (quelles garanties de non-divulgation ? quelle durée de rétention des données ?), la localisation des données (où sont stockées et traitées les données ?), les SLA (disponibilité, latence, limites de débit), la responsabilité (qui est responsable en cas de réponse erronée, de fuite de données, de contenu illicite ?), et l’auditabilité (droit d’audit ou de certification du fournisseur).

### 21.4 Articulation NIS2, DORA et HDS

Pour un organisme comme NovaSanté, plusieurs cadres réglementaires se superposent au RGPD et à l’AI Act.

**NIS2** (Directive (UE) 2022/2555, transposée dans les États membres) étend les obligations de cybersécurité aux entités essentielles et importantes. Si NovaSanté relève de NIS2 (selon sa classification sectorielle — le secteur santé est couvert), elle a des obligations de gestion des risques cyber, de notification d’incidents, de sécurité de la supply chain, et de gouvernance de la cybersécurité qui s’appliquent à ses systèmes IA comme à tout autre système.

**DORA** (Digital Operational Resilience Act, Règlement (UE) 2022/2554) concerne les entités du secteur financier. Si NovaSanté est classifiée comme organisme d’assurance, DORA lui impose des exigences de résilience opérationnelle numérique incluant la gestion des risques TIC (dont les systèmes IA), les tests de résilience, la gestion des incidents TIC, la gestion des risques liés aux tiers TIC (dont les fournisseurs d’IA), et le partage d’informations.

**HDS** (Hébergement de Données de Santé) est la certification française obligatoire pour l’hébergement de données de santé à caractère personnel. L’assistant RAG de NovaSanté traite des données de santé — le serveur d’inférence, la base vectorielle, et le stockage des logs doivent être hébergés chez un hébergeur certifié HDS (ou en interne si l’organisme est lui-même certifié). C’est la raison du déploiement on-premise.

L’articulation de ces cadres n’est pas redondante — chacun adresse une dimension spécifique (données personnelles, sécurité des systèmes IA, résilience opérationnelle, cybersécurité des entités essentielles, hébergement de données de santé). Le RSSI doit construire un tableau de conformité croisé qui identifie les exigences de chaque cadre et les mesures techniques et organisationnelles qui y répondent, en évitant la duplication d’efforts.

-----
