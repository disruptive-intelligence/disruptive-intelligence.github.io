---
title: Chapitre 1 — L'OSINT comme discipline de renseignement
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE I — Doctrine, cadre et posture
  - index.md
---

## 1.1 Définition opérationnelle

L'**OSINT** (Open Source Intelligence — en français ROSO, Renseignement d'Origine Sources Ouvertes) est la discipline du renseignement qui collecte, traite, analyse et exploite de l'information accessible publiquement pour produire du renseignement actionnable. Le mot clé est « discipline » — pas une collection d'outils, pas une recherche Google améliorée, pas une accumulation de captures d'écran. C'est un processus structuré, reproductible, documenté, et orienté décision.

L'IC OSINT Strategy 2024-2026 publiée par l'ODNI américaine définit l'OSINT comme « l'intelligence dérivée de l'information accessible publiquement, qui est collectée, exploitée, et disséminée en temps opportun à un public approprié pour traiter une exigence de renseignement spécifique ». Cette définition souligne quatre dimensions cruciales : **accessibilité publique** (pas d'accès illégal), **collecte structurée** (pas de butinage), **temps opportun** (pertinence par rapport à une décision), **exigence de renseignement** (orientation par une question, pas par une curiosité).

## 1.2 Information versus renseignement

La distinction la plus importante du métier est celle entre **information** et **renseignement**.

Une **information** est un fait brut, isolé, non qualifié : « Marc Delaunay est administrateur de Delta Consulting Ltd à Malte ».

Un **renseignement** est une information traitée, contextualisée, corrélée à d'autres sources, évaluée en fiabilité, et présentée avec un niveau de confiance explicite : « Marc Delaunay est administrateur déclaré de Delta Consulting Ltd, société maltaise au capital symbolique, dont le siège est une adresse de domiciliation partagée par 47 autres entités, et dont les flux entrants depuis TechnoVert SAS représentent 89 % du chiffre d'affaires déclaré sur les trois derniers exercices — niveau de confiance élevé, sources A1 et B2 ».

La différence n'est pas cosmétique. C'est ce qui distingue le travail d'un investigateur professionnel d'une recherche amateur, et c'est ce qui rend un livrable défendable devant un client exigeant, un magistrat, ou une contre-expertise.

## 1.3 Trois traits structurants de l'OSINT

L'OSINT se distingue de la simple recherche par trois traits.

**Orientée par un objectif.** « Delaunay contrôle-t-il des sociétés offshore ? » est une question d'investigation. « Que sais-je sur Delaunay ? » n'en est pas une. La question d'investigation est fermée (elle admet une réponse), vérifiable (on peut tester sa véracité), et reformulable en hypothèse (on peut imaginer une réponse alternative). Sans question, il n'y a pas de critère d'arrêt et l'enquête dérive.

**Méthodologie rigoureuse.** Le cycle du renseignement (orientation, collecte, traitement, analyse, diffusion, feedback — Ch.5) appliqué de manière disciplinée. Chaque étape laisse une trace (journal, captures, hashs, cotations). Chaque décision est tracée. L'enquête est reproductible : un confrère, sur les mêmes sélecteurs et la même méthode, doit pouvoir aboutir à des conclusions comparables.

**Livrable avec un niveau de confiance explicite.** Chaque fait porte une cotation de fiabilité (Admiralty A-F/1-6 — Ch.84). Chaque conclusion est qualifiée d'un niveau de confiance (WEP — Ch.85). Chaque limite est documentée. L'analyste qui dit « je suis sûr » sans cotation ni source produit du bruit, pas du renseignement.

## 1.4 Usages contemporains de l'OSINT

L'OSINT est mobilisée dans une variété croissante de métiers et de contextes.

**Renseignement institutionnel.** Services d'État (DGSE, DRM, DGSI, DRSD en France ; CIA, NSA, FBI aux USA ; SIS, GCHQ, MI5 au UK). L'OSINT est devenue une INT à part entière dans la doctrine alliée, fusionnée avec les autres disciplines pour produire de l'all-source intelligence. L'IC OSINT Strategy 2024-2026 reconnaît officiellement ce statut.

**Renseignement militaire et théâtre.** Suivi des conflits (Ukraine depuis 2022 a été un cas d'école), targeting, évaluation des dommages, identification de violations du droit international. Le **B2RS** (Bataillon de Réserve en Renseignement Spécialisé) créé en France illustre l'institutionnalisation de l'OSINT militaire chez les réservistes.

**Investigation judiciaire et police.** OSINT mobilisée par les services d'enquête (Section de Recherches gendarmerie, OCLCTIC, JIRS, C3N en France ; FBI Cyber, NCA en UK) pour l'investigation pénale ; par les magistrats instructeurs comme source d'orientation ; par les douanes (DNRED en France) pour les enquêtes fiscales et de trafic.

**Conformité, AML/CFT, KYC.** Banques, sociétés de gestion, assurances, courtiers, mobilisent l'OSINT pour le KYC (Know Your Customer), le KYB (Know Your Business), la due diligence renforcée sur les PEP, l'adverse media screening. Renforcement réglementaire avec **MiCA**, **AMLD**, **Travel Rule**.

**Cyber Threat Intelligence.** Identification d'infrastructures adverses, attribution prudente, monitoring de leak sites et forums, surveillance de la surface d'attaque. L'OSINT est l'une des sources majeures de la CTI, aux côtés de l'analyse interne et des feeds commerciaux.

**Due diligence et intelligence économique.** Vérification de partenaires commerciaux, M&A, supply chain (la **CSDDD** européenne 2024 impose un devoir de vigilance qui mobilise massivement l'OSINT), investigation de fraude interne, lutte contre la contrefaçon.

**Journalisme d'investigation.** Bellingcat est devenue la référence mondiale. ICIJ et OCCRP mobilisent l'OSINT pour leurs enquêtes (Panama, Pandora, FinCEN, Cyprus Confidential). Le journalisme d'investigation contemporain est profondément OSINT-augmenté.

**Recherche académique et droits humains.** Documentation de crimes de guerre, identification de victimes de pédocriminalité (programmes Europol *Stop Child Abuse — Trace an Object*), monitoring de violations des droits humains, recherche en sciences sociales.

**Executive protection.** Identification des menaces sur dirigeants, vérification d'environnement avant un déplacement, monitoring des fuites d'informations personnelles, gestion de réputation.

**Recherche citoyenne encadrée.** Trace Labs (CTF humanitaires de recherche de personnes disparues), Bellingcat Discord, projets de recherche participative. L'OSINT citoyenne est devenue une force réelle.

## 1.5 L'OSINT comme discipline professionnelle

L'OSINT est devenue **un métier**. En 2026, il existe des intitulés de postes dédiés (analyste OSINT, investigateur OSINT, OSINT specialist), des certifications reconnues (GIAC GOSI, TCM PORP, IntelTechniques OSIP), des cursus universitaires, des associations professionnelles (OSMOSIS, AFCOSINT en France). Les rémunérations et les responsabilités se sont structurées.

Cette professionnalisation s'accompagne d'une **exigence déontologique croissante**. L'analyste OSINT n'est plus un curieux solitaire derrière son écran : il est un professionnel responsable, tenu à des standards de méthode, de traçabilité, de proportionnalité, de respect des personnes. Le cours forme à cette posture professionnelle, pas à une virtuosité technique sans cadre.

## 1.6 OSINT et cycle du renseignement : aperçu

Le cycle du renseignement (Ch.5 pour le détail) structure toute investigation. Six phases : **orientation** (formuler la question), **collecte** (mobiliser les sources), **traitement** (nettoyer, organiser), **analyse** (corréler, tester les hypothèses, coter), **diffusion** (produire le livrable), **feedback** (le commanditaire réagit, on rebondit). Ce cycle n'est pas strictement séquentiel : les phases se chevauchent, on revient en arrière, on itère. Mais la discipline du cycle prévient les deux pièges classiques : la collecte qui ne mène à rien (pas d'orientation claire) et le rapport bâclé (pas d'analyse structurée).

## 1.7 Ce que l'OSINT n'est pas

L'OSINT n'est pas du **HUMINT déguisé**. L'investigateur ne se fait pas passer pour qui il n'est pas auprès de sources humaines (sauf cadre LEA précis). Le sock puppet sert à observer, pas à manipuler activement.

L'OSINT n'est pas du **SIGINT**. L'investigateur n'intercepte aucune communication. Toute interception est réservée aux services autorisés.

L'OSINT n'est pas du **hacking**. Toute exploitation d'accès non autorisé sort du cadre OSINT et bascule dans l'illégal (Code pénal art. 323-1).

L'OSINT n'est pas une **garantie de vérité**. C'est une production de renseignement coté sous incertitude, à partir de sources accessibles mais potentiellement biaisées, manipulées ou incomplètes. La rigueur méthodologique est ce qui distingue le renseignement du bruit, pas une magie qui ferait surgir la vérité.

-----
