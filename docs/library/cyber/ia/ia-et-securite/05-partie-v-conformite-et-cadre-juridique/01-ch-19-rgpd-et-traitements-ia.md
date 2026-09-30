---
title: Ch.19 — RGPD et traitements IA
source: Cyber/05_Cyberdefense/IA_Secu.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie V — Conformité et cadre juridique
  - index.md
---

## 19.1 Base légale par traitement IA

Tout traitement de données personnelles dans un système IA doit reposer sur une base légale (article 6 du RGPD). Les bases légales mobilisables varient selon le cas d’usage.

**L’intérêt légitime** est la base la plus fréquemment invoquée pour les traitements IA en entreprise (détection de fraude, amélioration de service, optimisation de processus). Il suppose un intérêt réel et légitime de l’entreprise, la nécessité du traitement IA (pas de moyen moins intrusif pour atteindre le même résultat), et la mise en balance avec les droits des personnes (le traitement ne porte pas une atteinte disproportionnée). La CNIL a précisé en 2025 qu’un intérêt commercial constitue un intérêt légitime, à condition que le traitement soit nécessaire et proportionné. À l’inverse, le développement de systèmes catégoriquement interdits par d’autres réglementations (comme l’AI Act) ne peut pas reposer sur l’intérêt légitime.

**Le consentement** est requis dans certains cas spécifiques (profilage à des fins marketing, traitement de données sensibles sauf exceptions). Il doit être libre, spécifique, éclairé et univoque. Dans un contexte employeur-employé, le caractère « libre » du consentement est souvent contesté.

**L’exécution d’un contrat** peut fonder un traitement IA directement lié à l’exécution du service contractuel (un assistant pour les gestionnaires de sinistres qui traite les données des sinistres dans le cadre du contrat d’assurance).

## 19.2 Minimisation et DPIA

Le principe de minimisation (article 5.1.c) exige de ne traiter que les données adéquates, pertinentes et limitées à ce qui est nécessaire. En IA, cela signifie ne pas indexer toute la base RH dans le RAG si seules les fiches de poste sont nécessaires, ne pas conserver les historiques de conversation au-delà de la durée nécessaire, et ne pas utiliser de données personnelles réelles quand des données synthétiques ou anonymisées suffisent.

La DPIA (Data Protection Impact Assessment / AIPD en français) est obligatoire pour les traitements susceptibles d’engendrer un risque élevé pour les droits et libertés des personnes. La CNIL considère que la réalisation d’une AIPD est présumée nécessaire pour le déploiement de tout système d’IA à haut risque au sens de l’AI Act dès lors qu’il implique des données personnelles, et que le développement de modèles de fondation ou de systèmes d’IA à usage général nécessite dans la majorité des cas une AIPD.

L’AIPD peut s’articuler avec la documentation exigée par l’AI Act : la CNIL encourage la réutilisation d’éléments entre les deux cadres pour éviter la redondance.

## 19.3 Sous-traitance et transferts

L’utilisation d’une API LLM cloud constitue un traitement de sous-traitance au sens du RGPD. Un DPA (Data Processing Agreement, article 28) est obligatoire entre le responsable de traitement (l’entreprise) et le sous-traitant (le fournisseur de l’API). Le DPA doit couvrir la finalité et la durée du traitement, les catégories de données traitées, les obligations du sous-traitant (sécurité, confidentialité, notification de violation), les droits d’audit, et les conditions de sous-sous-traitance.

Si le fournisseur est américain (OpenAI, Anthropic, Google), le traitement implique un transfert hors UE. Depuis l’invalidation du Privacy Shield (arrêt Schrems II, 2020) et l’adoption du EU-US Data Privacy Framework (DPF, 2023), les transferts vers les US reposent sur le DPF pour les entreprises certifiées, ou sur des SCC (Standard Contractual Clauses) avec évaluation d’impact du transfert. Le DPF fait l’objet de contestations juridiques et sa pérennité n’est pas garantie — un « Schrems III » est possible.

Pour les données de santé (HDS), les contraintes sont renforcées : l’hébergeur doit être certifié HDS, ce qui exclut de fait la plupart des fournisseurs de LLM cloud pour un traitement on-premise obligatoire (c’est le cas de l’assistant RAG de NovaSanté).

## 19.4 Droits des personnes et décisions automatisées

L’article 22 du RGPD donne aux personnes le droit de ne pas faire l’objet d’une décision fondée exclusivement sur un traitement automatisé produisant des effets juridiques ou des effets significatifs similaires. Le module de détection de fraude de NovaSanté est directement concerné : un scoring qui déclenche le rejet automatique d’un sinistre est une décision automatisée au sens de l’article 22.

Les obligations incluent le droit d’obtenir une explication de la décision (ce qui suppose une forme d’explicabilité du modèle), le droit de contester la décision et d’obtenir une intervention humaine, et la nécessité d’une base légale spécifique (consentement explicite ou nécessité pour l’exécution du contrat).

Le droit d’effacement dans un modèle fine-tuné est une question juridique ouverte : si des données personnelles sont mémorisées dans les poids du modèle, le droit d’effacement (article 17) implique-t-il un ré-entraînement du modèle ? La CNIL a indiqué en 2025 que selon les cas, elle pourrait exiger le ré-entraînement ou la suppression du modèle en cas de violation de données avérée.

## 19.5 Statut RGPD du modèle et vraisemblance de réidentification

La CNIL a publié en juillet 2025 une méthodologie spécifique pour évaluer si un modèle d’IA entre dans le champ du RGPD. Le principe : un modèle entraîné sur des données personnelles peut être considéré comme anonyme (hors RGPD) uniquement si la vraisemblance de réidentification de personnes physiques à partir du modèle est insignifiante. Si cette vraisemblance est non négligeable — ce qui est le cas dès que des techniques d’extraction, d’inférence d’appartenance ou d’inversion du modèle peuvent révéler des données personnelles avec des moyens raisonnables — le RGPD s’applique pleinement au modèle lui-même.

Cette logique a des conséquences directes pour le praticien. Tout modèle fine-tuné sur des données personnelles doit faire l’objet d’une évaluation documentée de la vraisemblance de réidentification. Cette évaluation doit être régulièrement réévaluée, car l’état de l’art en matière de techniques d’extraction évolue — une extraction jugée improbable aujourd’hui peut devenir réalisable demain. Le fournisseur doit prévoir des modalités de remontée d’information par les utilisateurs en cas d’incident (extraction inattendue de données personnelles) et gérer l’incident comme une violation de données potentielle (documentation, notification CNIL dans les 72 heures si risque pour les personnes, information des personnes si risque élevé).

Cette approche est directement cohérente avec les attaques de membership inference, model inversion et extraction de données détaillées au Ch.7. Le threat model d’un système IA doit inclure explicitement la vraisemblance de réidentification comme risque à évaluer et à surveiller dans le temps (voir aussi l’Annexe C — checklist d’exploitation).

-----
