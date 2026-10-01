---
title: Chapitre 28 — Élicitation, investigation et contre-ingérence
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie VI — Dimensions avancées
  - index.md
---

usages encadrés et expertise

## 28.1 L'élicitation comme outil d'investigation

Les techniques d'élicitation ne sont pas réservées aux attaquants et aux services de renseignement. Elles sont utilisées légalement dans de nombreux contextes professionnels.

**Les enquêteurs privés** utilisent l'élicitation dans le cadre d'investigations autorisées (fraude interne, compliance, due diligence). Le cadre juridique est strict : l'enquêteur ne peut pas usurper une identité officielle (force de l'ordre, administration), ne peut pas recourir à la contrainte, et doit respecter la vie privée. Les techniques d'élicitation conversationnelle (questions ouvertes, partage réciproque, silence stratégique) sont permises tant qu'elles ne constituent pas un stratagème déloyal au sens de la jurisprudence.

**Les journalistes d'investigation** utilisent des techniques proches de l'élicitation pour obtenir des informations de sources. Le droit français protège le secret des sources journalistiques, ce qui crée un cadre juridique spécifique.

**Les compliance officers** utilisent l'entretien structuré (distinct de l'élicitation — l'entretien est consenti et identifié) dans le cadre d'enquêtes internes sur des suspicions de fraude, de corruption ou de violation de conformité.

## 28.2 Le pretexting dans les enquêtes : cadre légal

Le pretexting — l'utilisation d'un faux pretexte pour obtenir des informations — est juridiquement encadré de manière stricte.

En France, la fabrication et l'utilisation de faux documents sont des infractions pénales (art. 441-1 et suivants du Code pénal). L'usurpation d'identité est un délit (art. 226-4-1). L'enregistrement d'une conversation sans le consentement des participants est interdit (art. 226-1). Ces restrictions limitent significativement les techniques disponibles pour les enquêteurs privés et les compliance officers par rapport aux pratiques anglo-saxonnes (aux États-Unis, le pretexting est plus largement toléré dans certains contextes d'investigation).

Le red team autorisé par lettre de mission constitue une exception encadrée : le pretexting est autorisé dans le cadre et les limites définis par la lettre de mission, qui vaut consentement de l'employeur. Mais cette autorisation ne couvre que les interactions avec les employés de l'organisation mandataire, pas avec des tiers (prestataires, visiteurs, voisins).

## 28.3 Investigation sur les arnaques de social engineering

L'investigation post-incident sur une arnaque de social engineering combine analyse technique et analyse relationnelle.

**Analyse technique.** Forensique email (headers, infrastructure de phishing — domaines, hébergement, certificats), analyse de la landing page (code source, exfiltration des données), traçage des flux financiers (pour le BEC — les fonds transitent typiquement par plusieurs comptes avant d'être convertis en crypto-monnaie ou retirés en liquide).

**Analyse OSINT.** Investigation sur les éléments identifiants de l'attaquant : numéros de téléphone (opérateur, géolocalisation), domaines (Whois, historique DNS, hébergement), profils en ligne (analyse de la fabrication des faux profils, recherche d'image inversée), et croisement avec les bases de données d'incidents connus.

**Coopération.** Avec les plateformes (signalement des faux profils, demande de désactivation), avec les banques (gel de fonds, traçage des virements), avec les forces de l'ordre (dépôt de plainte, transmission des éléments techniques), et avec les agences de renseignement si l'incident relève de l'ingérence étrangère (DGSI en France).

## 28.4 L'entretien et l'interrogatoire

Les techniques d'entretien professionnel (modèle PEACE — Preparation and Planning, Engage and Explain, Account, Closure, Evaluate) et l'entretien cognitif sont des outils d'investigation légaux distincts de l'élicitation.

La différence fondamentale : l'entretien est consenti et identifié (la personne sait qu'elle est interrogée et accepte de répondre), l'élicitation est clandestine (la personne ne sait pas qu'elle est interrogée). Cette distinction a des implications juridiques et éthiques majeures.

Le modèle PEACE, développé au Royaume-Uni, privilégie la collecte d'un récit libre (laisser le sujet raconter sa version sans interruption), la recherche de précisions par des questions non suggestives, et l'identification des incohérences par recoupement — plutôt que la confrontation directe ou les techniques d'interrogatoire agressives (qui produisent des faux aveux et des informations peu fiables).

## 28.5 Le témoignage de l'expert

L'expert en social engineering peut être amené à intervenir dans un cadre judiciaire : rapport d'expertise (analyse technique d'une arnaque, évaluation de la sophistication de l'attaque, évaluation de la responsabilité de la victime), expertise judiciaire (désigné par un tribunal pour éclairer une décision de justice), et contre-expertise (analyse critique d'un rapport d'expertise adverse).

L'expert doit être capable d'expliquer des concepts techniques complexes (phishing, deepfake, élicitation) à un public non technique (magistrats, jurés) de manière claire, rigoureuse et neutre. La crédibilité de l'expert repose sur ses qualifications, son expérience, la rigueur de sa méthodologie et sa capacité à distinguer fait établi, hypothèse probable et piste exploratoire.

---
