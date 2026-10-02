---
title: Chapitre 6 — Cadre juridique français de l'investigation OSINT
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 6.1 Le RGPD comme cadre central

Le **Règlement Général sur la Protection des Données** (RGPD, règlement UE 2016/679, entré en application le 25 mai 2018) est le cadre principal pour toute investigation OSINT en France et dans l'UE. Il s'applique dès qu'une donnée à caractère personnel est traitée, ce qui couvre quasiment toute investigation OSINT sur des personnes physiques.

**Définition d'une donnée personnelle.** Toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement. Un nom, une adresse, un email, un téléphone, une photo, un identifiant en ligne sont des données personnelles. Une adresse IP peut l'être (CNIL et CJUE l'ont confirmé).

**Principes RGPD applicables à l'OSINT.**

- **Licéité du traitement** (art. 6). Une base légale est requise : intérêt légitime de l'investigateur, exécution d'un contrat, mission d'intérêt public, etc. Pour un investigateur privé, l'intérêt légitime est la base la plus fréquente.
- **Finalité déterminée, explicite et légitime**. L'investigateur doit savoir pourquoi il collecte. Une collecte « au cas où » est non conforme.
- **Minimisation des données**. Ne collecter que ce qui est nécessaire à la finalité. Un excès de collecte est une violation.
- **Exactitude**. Les données collectées doivent être exactes et tenues à jour si elles sont conservées.
- **Limitation de la durée de conservation**. Les données ne doivent pas être conservées indéfiniment.
- **Sécurité et confidentialité**. Stockage chiffré, accès restreint, traçabilité.
- **Responsabilité (accountability)**. Capacité à démontrer la conformité.

**Droit des personnes concernées.** Droit d'accès, de rectification, d'effacement, d'opposition. Ces droits peuvent être opposés à l'investigateur dans certains cas, avec des exceptions (intérêt légitime supérieur, mission d'intérêt public, droit à l'information).

**Régimes spécifiques.** Les données sensibles (santé, opinions politiques, religion, orientation sexuelle, biométrie) bénéficient d'une protection renforcée (art. 9). Leur collecte est en principe interdite, sauf exceptions strictes.

## 6.2 Code pénal : les infractions à connaître

Plusieurs articles du Code pénal français encadrent l'investigation et fixent les limites pénales.

**Article 226-1 — Atteinte à la vie privée.** Punit l'enregistrement ou la transmission de paroles ou d'images d'une personne dans un lieu privé, sans son consentement. Périmètre principalement physique mais peut s'appliquer à certaines captures intrusives en ligne. **1 an d'emprisonnement et 45 000 € d'amende.**

**Article 226-18 — Collecte déloyale.** Punit la collecte de données à caractère personnel par moyen frauduleux, déloyal ou illicite. C'est l'un des articles centraux pour l'OSINT : une collecte qui contourne des protections techniques, qui ruse délibérément, ou qui usurpe une qualité peut tomber sous ce coup. **5 ans d'emprisonnement et 300 000 € d'amende.**

**Article 226-19 — Conservation illicite de données sensibles.** Punit la conservation illégale de certaines catégories de données (origine raciale, opinions politiques, syndicales, religieuses, mœurs, santé). **5 ans et 300 000 €.**

**Article 226-22 — Détournement de finalité.** Punit le détournement de la finalité d'un traitement. Un investigateur qui utilise des données collectées pour une autre fin que celle annoncée tombe sous ce coup. **5 ans et 300 000 €.**

**Article 323-1 — Accès frauduleux à un STAD (Système de Traitement Automatisé de Données).** Punit l'accès ou le maintien frauduleux dans un système informatique. **3 ans et 100 000 €**, 5 ans et 150 000 € si suppression ou modification de données.

**Article 323-3-1 — Mise à disposition de programmes ou données pour accès frauduleux.** **5 ans et 150 000 €.**

**Article 433-19 — Usurpation d'identité.** **1 an et 15 000 €.**

**Articles 226-15 et suivants — Atteinte au secret des correspondances**. L'interception non autorisée de communications privées tombe ici. Risque pénal majeur en cas de tentation d'accéder à un compte.

## 6.3 La jurisprudence Bluetouff — le cas fondateur

L'**arrêt Bluetouff** (Cour de cassation, chambre criminelle, 20 mai 2015) est l'arrêt fondamental pour comprendre la limite OSINT en France.

**Faits.** Olivier Laurelli (alias Bluetouff), journaliste et blogueur, a accédé à environ 8 Go de données internes de l'ANSES (Agence nationale de sécurité sanitaire) via une simple recherche Google. Les données étaient accessibles publiquement via une URL non protégée, mais leur accès reposait sur une défaillance de configuration. Bluetouff a téléchargé ces données.

**Décision.** La Cour de cassation a confirmé la condamnation pour **maintien frauduleux dans un système de traitement automatisé de données** (art. 323-1). Argument central : même si l'accès initial était techniquement possible sans contournement, le maintien dans le système après avoir compris qu'il s'agissait de données internes constituait un maintien frauduleux. Bluetouff a été condamné à 3 000 € d'amende.

**Conséquences pour l'OSINT.** Cet arrêt établit le principe que **« accessible n'équivaut pas à exploitable sans limite »**. Une donnée techniquement accessible peut être pénalement protégée si l'analyste comprend (ou aurait dû comprendre) qu'il s'agissait d'une donnée non destinée à la diffusion publique.

**Implication pratique.**

- Un bucket S3 mal configuré n'est pas une source OSINT légitime.
- Une page interne accessible via une URL devinée n'est pas exploitable sans précaution.
- Un dump de données apparu en ligne peut être pénalement risqué à consulter et exploiter.
- En cas de doute, **on ne consulte pas, on documente, et on signale**.

## 6.4 Le principe « accessible ≠ public »

C'est le **corollaire pratique** de la jurisprudence Bluetouff.

Une donnée est **publique** quand :

- Elle est volontairement diffusée par son auteur (post sur un réseau social ouvert, communiqué de presse, registre légal).
- Elle est sur un site dont la diffusion est l'objet (presse, blog, page institutionnelle).
- Elle est indexée par les moteurs et reste accessible sans contournement.

Une donnée est **techniquement accessible mais non publique** quand :

- Elle a été exposée par erreur (bucket mal configuré, URL prédictible non protégée).
- Elle a été extraite d'un système compromis (leak provenant d'un piratage).
- Elle suppose un contournement technique pour y accéder (même mineur).

**Règle pratique.** En cas de doute, traiter comme non public. Ne pas consulter, ne pas exploiter, documenter et signaler le cas échéant à la CNIL ou à l'ANSSI.

## 6.5 Mandat, finalité et proportionnalité

Trois principes opérationnels structurent l'enquête OSINT en droit français.

**Le mandat.** L'investigateur agit sur mandat (contrat avec un client, mission interne, mandat judiciaire). Le mandat encadre ce qui peut et ce qui ne peut pas être fait. Une investigation sans mandat clair est juridiquement exposée. Pour un consultant : contrat écrit, périmètre défini, finalité documentée.

**La finalité.** Toute collecte a une finalité. L'utilisation des données pour une finalité autre que celle annoncée tombe sous l'art. 226-22 (détournement de finalité). Si la finalité initiale était la due diligence M&A, on ne peut pas réutiliser les données pour une investigation pénale sans une nouvelle base légale.

**La proportionnalité.** La collecte doit être proportionnée à la finalité. Si l'objectif est de vérifier l'existence d'une société écran, on ne collecte pas l'intégralité du profil familial du dirigeant. La sur-collecte est une violation RGPD.

## 6.6 OSINT pour les LEA versus le secteur privé

Les **services d'État et autorités judiciaires** ont des pouvoirs que le secteur privé n'a pas :

- Réquisitions judiciaires (accès aux données opérateurs, plateformes).
- Interceptions légales (cadre loi renseignement, art. 100 et suivants CPP).
- Perquisitions et saisies.
- Accès à des bases protégées (FOVeS, FIJAIT, etc.).

Les **investigateurs privés** doivent rester strictement dans le périmètre OSINT (accessible publiquement, sans contournement). La tentation d'utiliser des moyens « gris » (bases de données illégalement constituées, paiement de tipsters internes, accès via leaks) expose à des sanctions pénales.

## 6.7 Cas particulier : les leaks

Le statut juridique des **données fuitées** (leaks, dumps) est complexe.

**Pour les LEA.** Peuvent généralement utiliser les leaks comme sources d'orientation. Cadre judiciaire balise l'usage.

**Pour les journalistes.** Liberté de presse et intérêt public sont des protections fortes. Les ICIJ, OCCRP, médias d'investigation utilisent massivement les leaks (Panama, Pandora, Cyprus Confidential). Risque pénal limité dans un cadre journalistique sérieux.

**Pour les analystes privés non-journalistes.** Zone grise. Consulter un leak public reste généralement toléré. **Exploiter** un leak (intégrer ses données dans un rapport, le commercialiser) est juridiquement plus risqué — particulièrement si les données proviennent d'un piratage avéré.

**Règle pratique.** En l'absence de mandat judiciaire ou de qualité journalistique reconnue, prudence maximale sur l'exploitation des leaks. Documenter l'origine, ne pas reproduire les données, citer les analyses publiées par les sources autorisées (ICIJ notamment) plutôt que d'accéder aux dumps bruts.

## 6.8 Recours en cas d'incident

Si l'investigateur est sollicité par la personne ciblée (droit d'accès, droit d'effacement, plainte) :

- Répondre dans les délais RGPD (1 mois en général).
- Documenter la base légale du traitement.
- Évaluer si l'opposition de la personne doit être suivie ou si l'intérêt légitime prévaut (notamment dans le cadre d'investigations en cours).
- En cas de doute, consulter un avocat spécialisé.

## 6.9 La CNIL comme acteur

La **CNIL** (Commission nationale de l'informatique et des libertés) est l'autorité de contrôle française. Elle peut :

- Contrôler les pratiques (sur plainte ou d'office).
- Sanctionner (jusqu'à 4 % du chiffre d'affaires mondial pour les violations RGPD majeures).
- Publier des recommandations et guidelines (à suivre).

Pour les professionnels de l'OSINT, la CNIL n'a pas publié de doctrine sectorielle complète, mais ses recommandations générales sur le RGPD s'appliquent. En cas de doute, consulter le **registre des activités de traitement** de l'organisation et désigner un DPO si l'activité OSINT est significative.

## 6.10 Synthèse — les 10 réflexes juridiques

1. Vérifier la base légale RGPD du traitement.
2. Documenter la finalité de la collecte.
3. Minimiser la collecte aux données nécessaires.
4. Respecter le principe « accessible ≠ public ».
5. Refuser tout contournement technique (pas de Bluetouff 2).
6. Documenter le mandat (client + finalité + périmètre).
7. Protéger les données collectées (chiffrement, accès restreint).
8. Encadrer la durée de conservation.
9. Préparer les réponses aux droits des personnes concernées.
10. Consulter un avocat en cas de doute, ne pas improviser.

-----
