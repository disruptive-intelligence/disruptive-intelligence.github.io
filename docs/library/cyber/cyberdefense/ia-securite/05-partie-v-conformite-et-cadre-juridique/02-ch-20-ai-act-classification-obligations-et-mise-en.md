---
title: 'Ch.20 — AI Act : classification, obligations et mise en conformité'
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA & sécurité
up:
- - IA & sécurité
  - ../index.md
- - Partie V — Conformité et cadre juridique
  - index.md
---

## 20.1 Les quatre niveaux de risque

L’AI Act (Règlement UE 2024/1689) classe les systèmes d’IA en quatre niveaux de risque.

**Risque inacceptable** → interdit. La liste inclut la notation sociale (social scoring), la manipulation subliminale, l’exploitation de vulnérabilités de groupes spécifiques, la reconnaissance faciale en temps réel dans l’espace public par les forces de l’ordre (sauf exceptions), et l’inférence d’émotions sur le lieu de travail ou dans l’éducation (sauf raisons médicales ou de sécurité).

**Risque élevé** → conformité stricte. Les systèmes listés à l’Annexe III incluent : biométrie, infrastructures critiques, éducation et formation professionnelle, emploi et gestion du personnel, accès aux services essentiels (banque, assurance), forces de l’ordre, migration et contrôle aux frontières, administration de la justice. Pour NovaSanté, le module de scoring de fraude (qui influence des décisions sur des prestations d’assurance) pourrait relever du « risque élevé » selon l’interprétation de l’accès aux services essentiels.

**Risque limité** → obligations de transparence. Les systèmes qui interagissent avec des personnes (chatbots) doivent informer l’utilisateur qu’il interagit avec une IA. Les contenus générés par IA (texte, image, audio, vidéo) doivent être marqués comme tels.

**Risque minimal** → pas d’obligations spécifiques. La grande majorité des systèmes IA en entreprise relèvent de cette catégorie.

## 20.2 Calendrier d’application (à date)

Le calendrier de référence, tel qu’indiqué par la Commission européenne, prévoit l’entrée en vigueur le 1er août 2024, les pratiques interdites et les obligations d’AI literacy applicables depuis le 2 février 2025, les obligations GPAI (General Purpose AI) applicables depuis le 2 août 2025, l’application générale (dont les obligations pour les systèmes haut risque) au 2 août 2026, et certaines règles haut risque embarquées dans des produits réglementés jusqu’au 2 août 2027.

> **⚠️ Point de vigilance**
> Des propositions d’ajustement de l’implémentation et des standards techniques ont été discutées fin 2025 et début 2026. La Commission européenne a notamment proposé un paquet de simplification pouvant décaler le calendrier des règles applicables aux systèmes haut risque jusqu’à 16 mois supplémentaires. Le calendrier ci-dessus est le calendrier de référence à date mais reste susceptible d’ajustements d’implémentation. Le praticien doit suivre les publications de l’AI Office et des autorités nationales (en France, la CNIL se positionne pour assumer le rôle d’autorité de contrôle pour l’AI Act).

## 20.3 Obligations pour les systèmes haut risque

Les systèmes haut risque doivent respecter des exigences strictes : système de gestion des risques, gouvernance des données, documentation technique détaillée, journalisation (logging), transparence et information des déployeurs, supervision humaine, exactitude, robustesse et cybersécurité, et évaluation de conformité (auto-évaluation ou par un organisme notifié selon les cas). Le marquage CE est requis avant la mise sur le marché. Les sanctions peuvent atteindre 35 M€ ou 7 % du CA mondial.

## 20.4 Obligations GPAI

Les fournisseurs de modèles GPAI (General Purpose AI — les modèles de fondation comme GPT-4, Claude, Gemini, Mistral Large) ont des obligations spécifiques de documentation technique, de respect du droit d’auteur, de publication d’un résumé du contenu d’entraînement, et de coopération avec les autorités. Les modèles GPAI à risque systémique (dépassant un seuil de compute d’entraînement) ont des obligations renforcées d’évaluation et de reporting.

-----
