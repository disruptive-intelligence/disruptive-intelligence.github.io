---
title: Chapitre 103 — Corrigé détaillé de l'exercice final
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 103.1 Approche du corrigé

Le présent corrigé n'est **pas une solution unique**. Plusieurs cadrages valides sont possibles. Il propose une trame de référence permettant à l'apprenant de comparer ses choix et d'identifier les axes de progression.

## 103.2 Cadrage attendu — IR proposées

**IR1.** Solène Faure bénéficie-t-elle, directement ou indirectement, économiquement de Lumière Stratégie Sàrl (Luxembourg) ?

**IR2.** Les conventions réglementées entre VenturaTech SAS et Lumière Stratégie sont-elles conformes aux processus statutaires (autorisation conseil d'administration, déclaration commissaire aux comptes) ?

**IR3.** Les communiqués positifs récents sur VenturaTech ont-ils été amplifiés artificiellement sur les réseaux sociaux, et si oui, qui est plausiblement à l'origine ?

**IR4.** M. Pierre Vidal a-t-il, dans la période considérée, conduit des opérations boursières publiquement visibles compatibles avec usage d'informations privilégiées concernant la participation de VenturaTech dans une société cotée ?

**IR5.** Y a-t-il d'autres signaux d'alerte (sanctions, PEP, adverse media, contentieux) sur Solène Faure, M. Vidal, ou VenturaTech qui ressortiraient de l'investigation OSINT ?

## 103.3 Bornes et OPSEC

**Bornes.**

- Sources ouvertes exclusivement.
- Pas d'ingénierie sociale active.
- Pas de surveillance physique.
- Pas d'accès aux comptes privés sans nécessité absolue.
- Respect RGPD strict.

**OPSEC.**

- VPN no-log + Tor pour les recherches sensibles.
- Comptes d'investigation matures (LinkedIn, X, Instagram).
- Captures Hunchly systématiques.
- Vault Obsidian local chiffré + knowledge graph local (Neo4j).
- LLMs locaux (Ollama Llama 3.3) pour tâches sensibles.

## 103.4 Plan de collecte sur 3 semaines

**Semaine 1 — Cadrage et fondations.**

- Jours 1-2 : Cartographie sources, configuration outils, OPSEC.
- Jours 3-5 : Identification fiable de Solène Faure (LinkedIn, presse, Pappers).
- Jours 6-7 : Cartographie corporate VenturaTech (Pappers, BODACC, communiqués).

**Semaine 2 — Approfondissement.**

- Jours 8-9 : Investigation Lumière Stratégie Luxembourg (RCS Luxembourg, OpenCorporates, ICIJ leaks).
- Jours 10-11 : Investigation M. Vidal (identité, parcours, publications).
- Jours 12-13 : SOCMINT et analyse cluster communiqués (IR3).
- Jour 14 : Synthèse intermédiaire, ajustement.

**Semaine 3 — Convergence et production.**

- Jours 15-16 : Cross-référencement, ACH sur 5 IR.
- Jours 17-18 : Rédaction fiches entités.
- Jours 19-20 : Rédaction rapport.
- Jour 21 : Validation interne, hash, livraison.

## 103.5 Outils mobilisés par IR

**IR1 — Bénéfice indirect.**

- Pappers / Infogreffe (TechnoVert structure).
- RCS Luxembourg + LBR.lu (Lumière Stratégie).
- ICIJ Offshore Leaks Database.
- OpenCorporates cross-juridictions.
- Recherche presse sur Faure / Lumière.

**IR2 — Conventions réglementées.**

- BODACC (modifications statutaires VenturaTech).
- Procès-verbaux AG si publics.
- Communiqués déclaration conventions.
- Presse spécialisée.

**IR3 — Amplification artificielle.**

- X / LinkedIn analyse réseau.
- Comptes amplificateurs : photos profil (Hive Moderation pour IA).
- Stylométrie comparative LLM-generated.
- Analyse temporelle (cadence, synchronisations).
- Recherche infrastructure (sites tiers amplifiant).

**IR4 — Usage information privilégiée par Vidal.**

- Presse boursière sur société cotée mentionnée.
- AMF déclarations dirigeants si Vidal lié.
- Publication des transactions au-dessus de seuils.
- LinkedIn / réseaux : indices sur intérêt boursier de Vidal.

**IR5 — Signaux d'alerte généraux.**

- OpenSanctions.
- WorldCheck si accessible.
- Adverse media multi-langues.
- Légifrance, Doctrine.fr (contentieux).

## 103.6 Cotations anticipées

**Cotations attendues pour les faits clés.**

| Fait type | Cotation typique |
|---|---|
| Identification corporate via Pappers | A1 |
| Identification UBO Luxembourg via LBR | A1 |
| Présence dans ICIJ leak | B2 |
| Compte X verrouillé / privé | non cotable directement |
| Amplification artificielle détectée par signaux convergents | B2 |
| Communiqué officiel | A1 |
| Article presse établie | B2 |
| Stylométrie comparative LLM | B3 |
| Photo IA détectée Hive Moderation | A1 sur la détection, B2 sur l'attribution opérateur |

## 103.7 ACH sur IR1 et IR3 (illustration)

**ACH IR1 — Bénéfice indirect Faure / Lumière.**

| Évidence | H1 (béné. dir) | H2 (consultante régulière) | H3 (pas de lien éco) |
|---|---|---|---|
| Faure ou famille citée RCS Lumière | (à vérifier) | — | — |
| Conventions réglementées TechnoVert ↔ Lumière | C | C | I |
| ICIJ Pandora mention | (à vérifier) | — | — |
| Taille des flux vs activité réelle | (à vérifier) | (à vérifier) | (à vérifier) |
| Capital symbolique Lumière | C | C | C |
| Pas d'autres clients connus de Lumière | C | I | C |

**ACH IR3 — Amplification artificielle.**

| Évidence | H1 (campagne coordonnée) | H2 (engagement organique) | H3 (mix légèrement amplifié) |
|---|---|---|---|
| Photos IA dans cluster amplificateur | C | I | C |
| Cadence parfois inhumaine | C | I | C |
| Tournures stylométriques répétées | C | I | C |
| Comptes créés en lot | C | I | C |
| Mentions par influenceurs authentiques | N | C | C |

**Lecture.** Sur IR3, H2 réfutée. H1 fortement soutenue. H3 plausible (campagne coordonnée + amplification organique consécutive).

## 103.8 Limites identifiées

**À documenter dans le rapport.**

- Registre UBO Luxembourg accès partiel post-CJUE.
- Conventions réglementées détaillées non publiques (accès actionnaire seul, ou expertise comptable).
- Identification précise de chaque acteur derrière les comptes amplificateurs limitée sans réquisitions plateformes.
- Identification précise du commanditaire derrière la campagne d'amplification limitée.
- Transactions Vidar (si elles existent) non visibles publiquement sans accès aux comptes-titres.
- Cross-recherche crypto limitée (renvoi cours OSINT Crypto vFULL si signaux).

## 103.9 Escalades à recommander

**Vers expertise dédiée.**

- Audit comptable forensique VenturaTech 2020-2025 (sur conventions réglementées et flux Lumière).
- Expertise crypto forensique si signaux apparaissent (renvoi OSINT Crypto vFULL).
- Expertise numérique sur contenus IA et campagne d'amplification.

**Vers procédure.**

- Action sociétaire (cabinet mandataire).
- Saisine PNF si éléments suggèrent fraude fiscale.
- Saisine AMF si Vidar lié à transaction boursière concrète.
- Signalement TRACFIN si élément blanchiment.

## 103.10 Structure du rapport final

**Cohérente avec Ch.88.**

- Page de garde + classification.
- Executive summary 2 pages avec BLUF.
- Cadrage du mandat.
- Méthodologie.
- 5 sections IR avec faits cotés, ACH résumé, conclusion calibrée.
- Synthèse intégrée.
- Recommandations actionnables.
- Limites globales.
- Annexes : fiches entités, matrices ACH, timeline, graphe, catalogue pièces.

## 103.11 Executive summary type

> **BLUF.** L'investigation OSINT conduite sur le périmètre Solène Faure / VenturaTech / Lumière Stratégie / Pierre Vidal identifie : (a) probable lien économique entre Faure et Lumière Stratégie Sàrl (B2, cohérence convergente, démonstration directe demande expertise), (b) conventions réglementées documentées mais opacité sur conditions économiques (B3), (c) campagne d'amplification artificielle des communiqués positifs très probable (B1-A1, signaux techniques convergents), (d) absence d'élément public direct concernant transactions boursières de M. Vidar (D-F selon signaux), (e) absence de sanctions, PEP, adverse media majeur sur les acteurs (A1). **Niveau de confiance global : probable** sur l'architecture des soupçons, **élevé** sur les signaux factuels individuels, **modéré** sur l'attribution finale des campagnes d'amplification.
>
> **Recommandations principales.** (1) Audit comptable forensique VenturaTech 2020-2025 par expert inscrit. (2) Action sociétaire prudente avec demande pièces conventions réglementées. (3) Signalement AMF et expertise complémentaire sur amplification réseaux sociaux. (4) Si éléments fraude fiscale se précisent, dénonciation art. 40 vers PNF.

## 103.12 Pédagogie du corrigé

L'apprenant compare :

- Sa formulation d'IR (cohérence, couverture).
- Son plan de collecte (réalisme).
- Sa mobilisation d'outils (pertinence par IR).
- Sa pratique de cotation (discipline Admiralty + WEP).
- Son anti-biais (ACH, devil's advocate).
- Sa production (BLUF, structure, recommandations).
- Son éthique (bornes, signalements potentiels).

**Indicateurs de qualité dans la réponse.**

- IR fermées et vérifiables.
- OPSEC mentionnée explicitement.
- Cotations utilisées correctement.
- ACH mentionné.
- Limites assumées.
- Escalades vers cours spécialisés identifiées.
- Recommandations actionnables proportionnées.

**Indicateurs de faiblesse.**

- IR ouvertes ou vagues.
- Sur-affirmation (« il est certain que »).
- Pas de cotation.
- Pas de devil's advocate.
- Pas de limites mentionnées.
- Recommandations vagues.

## 103.13 Synthèse du master

L'exercice final, et son corrigé, **achèvent** le master OSINT. L'apprenant a parcouru :

- Doctrine et cadre (Parties I-II).
- Méthodologie (Partie III).
- Sources et techniques (Parties IV-VIII).
- IA et automatisation (Partie IX).
- Passerelles spécialisées (Partie X).
- Analyse structurée (Partie XI).
- Production (Partie XII).

L'analyste OSINT 2026 issu de ce master :

- Maîtrise les sources et outils du domaine.
- Applique une cotation rigoureuse.
- Conduit une analyse anti-biais.
- Produit des livrables professionnels.
- Respecte un cadre déontologique strict.
- Coopère avec les domaines spécialisés.
- Évolue avec l'écosystème.

Le master n'est jamais achevé : la formation continue, la pratique sur cas réels (avec déontologie), la veille permanente sur outils et méthodes sont indispensables.

> **Mot final.** L'OSINT mature en 2026 est une discipline d'**équilibre** : entre rigueur et créativité, entre exhaustivité et économie, entre puissance des outils IA et garde de la responsabilité humaine, entre proximité et distance critique avec les sources. Cet équilibre n'est pas un point d'arrivée ; c'est une posture quotidienne. Le présent cours en donne les fondements ; le métier en révèle la profondeur.

-----
