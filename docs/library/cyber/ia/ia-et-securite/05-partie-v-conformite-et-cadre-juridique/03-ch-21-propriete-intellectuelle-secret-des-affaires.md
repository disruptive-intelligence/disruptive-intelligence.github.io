---
title: Ch.21 — Propriété intellectuelle, secret des affaires, contrats fournisseurs et articulation NIS2/DORA/HDS
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie V — Conformité et cadre juridique
  - index.md
---

## 21.1 Propriété intellectuelle des outputs IA

En droit français, une œuvre est protégée par le droit d’auteur si elle est originale et créée par un humain. Le statut juridique des contenus générés par IA est incertain : un texte, une image, ou un code entièrement généré par une IA sans intervention créative humaine significative n’est probablement pas protégeable. En pratique, cela signifie que les contenus produits par l’IA de l’entreprise ne bénéficient pas nécessairement de la protection du droit d’auteur — un concurrent pourrait les réutiliser.

Les données d’entraînement posent un problème inverse : les modèles sont entraînés sur des œuvres protégées et peuvent en régurgiter des fragments. Les procès en cours (NYT vs OpenAI, Getty vs Stability AI) portent précisément sur cette question. Le risque pour l’entreprise est la contrefaçon involontaire si un modèle produit du contenu substantiellement similaire à une œuvre protégée présente dans ses données d’entraînement.

## 21.2 Secret des affaires

Les données stratégiques (plans commerciaux, algorithmes propriétaires, données de R&D) ne doivent jamais transiter par un LLM cloud sans garanties contractuelles fortes. Le secret des affaires (directive 2016/943 transposée en droit français) protège les informations qui ont une valeur commerciale parce qu’elles sont secrètes et qui font l’objet de mesures de protection raisonnables. L’envoi de ces informations à un LLM cloud peut compromettre le caractère « secret » si les mesures de protection sont jugées insuffisantes.

## 21.3 Clauses essentielles des contrats fournisseurs IA

Lors de la contractualisation avec un fournisseur d’IA (API, modèle, plateforme), les clauses critiques incluent la propriété des outputs (qui possède les contenus générés ?), l’utilisation des inputs pour l’entraînement (les prompts et les données envoyées sont-ils utilisés pour améliorer le modèle ? possibilité d’opt-out ?), la confidentialité (quelles garanties de non-divulgation ? quelle durée de rétention des données ?), la localisation des données (où sont stockées et traitées les données ?), les SLA (disponibilité, latence, limites de débit), la responsabilité (qui est responsable en cas de réponse erronée, de fuite de données, de contenu illicite ?), et l’auditabilité (droit d’audit ou de certification du fournisseur).

## 21.4 Articulation NIS2, DORA et HDS

Pour un organisme comme NovaSanté, plusieurs cadres réglementaires se superposent au RGPD et à l’AI Act.

**NIS2** (Directive (UE) 2022/2555, transposée dans les États membres) étend les obligations de cybersécurité aux entités essentielles et importantes. Si NovaSanté relève de NIS2 (selon sa classification sectorielle — le secteur santé est couvert), elle a des obligations de gestion des risques cyber, de notification d’incidents, de sécurité de la supply chain, et de gouvernance de la cybersécurité qui s’appliquent à ses systèmes IA comme à tout autre système.

**DORA** (Digital Operational Resilience Act, Règlement (UE) 2022/2554) concerne les entités du secteur financier. Si NovaSanté est classifiée comme organisme d’assurance, DORA lui impose des exigences de résilience opérationnelle numérique incluant la gestion des risques TIC (dont les systèmes IA), les tests de résilience, la gestion des incidents TIC, la gestion des risques liés aux tiers TIC (dont les fournisseurs d’IA), et le partage d’informations.

**HDS** (Hébergement de Données de Santé) est la certification française obligatoire pour l’hébergement de données de santé à caractère personnel. L’assistant RAG de NovaSanté traite des données de santé — le serveur d’inférence, la base vectorielle, et le stockage des logs doivent être hébergés chez un hébergeur certifié HDS (ou en interne si l’organisme est lui-même certifié). C’est la raison du déploiement on-premise.

L’articulation de ces cadres n’est pas redondante — chacun adresse une dimension spécifique (données personnelles, sécurité des systèmes IA, résilience opérationnelle, cybersécurité des entités essentielles, hébergement de données de santé). Le RSSI doit construire un tableau de conformité croisé qui identifie les exigences de chaque cadre et les mesures techniques et organisationnelles qui y répondent, en évitant la duplication d’efforts.

-----
