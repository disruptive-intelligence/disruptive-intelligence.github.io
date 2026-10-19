---
title: "ISO/IEC 27090 : sécuriser l’IA, ce que la norme apporte et ce qu’elle laisse de côté"
date: 2026-10-19
kind: dossier
slug: iso-iec-27090-securiser-l-ia-ce-que-la-norme-apporte-et-ce-qu-elle-laisse-de-cote
themes:
  - ia
  - cyber
rubriques:
  - ia-risques-surete
  - ia-gouvernance
  - ia-agents
tags:
  - ISO/IEC 27090
  - normalisation
  - sécurité de l’IA
  - injection de prompt
  - empoisonnement des données
  - AI Act
---

# ISO/IEC 27090 : sécuriser l’IA, ce que la norme apporte et ce qu’elle laisse de côté

Date de rédaction : 2026-10-19

## Sources de synthèse

- **[A1]** `analyses/recommandations-de-securite-pour-un-systeme-dia-generative.md`

Sélection des sources externes déterminantes ; la liste complète, avec ce que chaque source permet d’établir, figure en fin de dossier.

- **[S1]** InnovaSafe Consulting, Christophe Godefroid, [« ISO/IEC 27090 : la sécurité de l’IA »](https://www.innovasafe.be/article-iso-27090-securite-ia.html), article de départ, 18 octobre 2026.
- **[S2]** ISO, [fiche officielle d’ISO/IEC 27090:2026](https://www.iso.org/standard/27090), édition 1, octobre 2026.
- **[S3]** iTeh Standards, [notice et extrait officiel de la norme](https://standards.iteh.ai/catalog/standards/iso/0b64ee20-3192-4976-a90f-9e16225dcab0/iso-iec-fdis-27090) : sommaire complet, introduction, clauses 1 à 5.3.
- **[S4]** ISO, [« ISO/IEC 27090 explained »](https://www.iso.org/home/insights-news/resources/ISO-27090-explained.html), guide de présentation rédigé d’après le projet final.
- **[S5]** iso27001security.com, [fiche commentée d’ISO/IEC 27090](https://www.iso27001security.com/html/27090), mise à jour le 19 octobre 2026 : structure et critiques.
- **[S6]** L. Nannini, A. L. Smith et al., [*AI Agents Under EU Law*](https://arxiv.org/abs/2604.04604), arXiv, avril 2026 : statut juridique de la norme et lacunes sur les agents.
- **[S7]** NCSC (Royaume-Uni), [« Prompt injection is not SQL injection (it may be worse) »](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection), 8 décembre 2025.
- **[S8]** AI Standardisation Watch, [édition 16, septembre 2026](https://krogrules.com/news/edition-16-september-2026) : état des normes harmonisées européennes, dont prEN 18282.

## Périmètre et méthode

Ce dossier part de l’[article d’InnovaSafe du 18 octobre 2026](https://www.innovasafe.be/article-iso-27090-securite-ia.html) [S1], publié quatre jours après la parution de la norme. Le texte intégral d’ISO/IEC 27090 est payant (56 pages, 204 francs suisses selon le [catalogue du bureau serbe de normalisation](https://iss.rs/en/project/show/iso:proj:56581)) et n’a pas été acheté. En revanche, l’**extrait officiel** diffusé par iTeh [S3] a été lu : page de titre, sommaire détaillé, avant-propos, introduction, domaine d’application, références normatives, les trente définitions et la clause 5 jusqu’à 5.3. Pour les clauses 6 et 7, le dossier s’appuie sur le sommaire, le guide de l’ISO [S4], la notice d’iTeh et des commentaires spécialisés ; ces passages sont signalés comme tels. L’arrêt de la recherche est fixé au **19 octobre 2026**.

Les sources externes ont été choisies pour couvrir quatre questions : **ce que dit la norme** (ISO, extrait officiel, commentateur de référence des normes 27000) ; **ce qu’elle vaut juridiquement** (AI Act, Cyber Resilience Act, normes harmonisées européennes) ; **ce que montre la menace réelle** (incidents, travaux de recherche, retours d’agences) ; **ce qu’en disent les autres référentiels** (ETSI, NIST, OWASP, ANSSI, NCSC). Les articles de cabinets de conseil ou d’éditeurs, y compris l’article de départ, sont traités comme des lectures secondaires : leurs avis sont rapportés comme avis.

L’analyse interne [A1] sert de point de comparaison : le guide de l’ANSSI de 2024 sur l’IA générative couvre une partie du même terrain avec une approche plus prescriptive, et permet de mesurer ce que la norme internationale ajoute ou n’ajoute pas.

## Résumé exécutif

1. **Une norme publiée, de recommandations, non certifiable.** ISO/IEC 27090:2026, *Cybersecurity — Artificial intelligence (AI) — Addressing security threats and compromises to AI systems*, est parue le **14 octobre 2026** sous l’égide du sous-comité JTC 1/SC 27 [S2][S3]. C’est un document de recommandations : il ne peut pas faire l’objet d’une certification et ne crée aucune présomption de conformité au droit européen [S6]. Il vise toutes les organisations qui développent **ou utilisent** de l’IA, pas seulement les fournisseurs de modèles.
2. **Le socle reste la sécurité classique.** La clause 5 pose que les mesures d’ISO/IEC 27002 s’appliquent d’abord, et qu’il est souvent plus efficace de durcir l’infrastructure qui héberge un modèle que d’empiler des protections propres à l’IA [S3]. Gouvernance de l’IA avec inventaire, zéro confiance (y compris pour les agents), pratiques de développement sécurisé, chaîne d’approvisionnement, modélisation des menaces et red teaming complètent ce socle.
3. **Le cœur est un catalogue de douze compromissions.** La norme définit douze types de compromission, dont neuf font l’objet d’une sous-clause détaillée (description, défaillances, détection, atténuation) : empoisonnement des données, évasion, inférence d’appartenance, exfiltration de modèle, inversion de modèle, empoisonnement direct du modèle, sortie sensible, injection de prompt et sortie porteuse d’injection [S3]. Les « neuf menaces » de l’article de départ correspondent à ces neuf sous-clauses.
4. **Son idée la plus originale porte sur les mesures elles-mêmes.** La clause 7 traite les protections comme un système : elles peuvent entrer en conflit, se dégrader avec le temps et doivent rester cohérentes sur tout le cycle de vie [S3][S4]. C’est une différence nette avec les listes de contrôles, qui juxtaposent les mesures sans examiner leurs effets croisés.
5. **Elle arrive tard sur deux terrains devenus centraux.** Lancé vers 2022 [S5], le projet a été écrit pour l’essentiel avant l’essor des agents. Les agents sont mentionnés, mais aucune catégorie ne couvre en propre l’abus d’outils, l’empoisonnement de mémoire ou les chaînes multi-agents, que l’[OWASP](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications/) et MITRE ATLAS documentent depuis 2025. Et la norme traite l’injection de prompt comme une menace à détecter et atténuer, alors que le [NCSC](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) [S7] et [Meta](https://ai.meta.com/blog/practical-ai-agent-security/) jugent qu’elle ne peut qu’être contenue par conception.
6. **Sa valeur réelle tient au vide qu’elle comble.** La norme européenne harmonisée sur la cybersécurité de l’IA (prEN 18282) a été rejetée à l’enquête publique de juillet 2026 [S8], et les obligations « haut risque » de l’AI Act ont été repoussées à décembre 2027. D’ici là, ISO/IEC 27090 est la référence internationale publiée la plus complète pour démontrer qu’une organisation a traité les menaces propres à l’IA « selon l’état de l’art », ce qu’exigent aussi bien l’article 15 de l’AI Act que NIS2.

## Chronologie

- **Mars 2023** — L’ENISA recense, dans son rapport [*Cybersecurity of AI and Standardisation*](https://www.enisa.europa.eu/sites/default/files/publications/Cybersecurity%20of%20AI%20and%20Standardisation.pdf), les normes en préparation et pointe le besoin de guides appliquant la cybersécurité à l’IA.
- **2022–2024** — Projet ISO/IEC 27090 au sein du groupe de travail SC 27/WG 4, d’abord intitulé *Guidance for addressing security threats to artificial intelligence systems* [S5].
- **31 janvier 2025** — Le Royaume-Uni publie son [*Code of Practice for the Cyber Security of AI*](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice), transmis à l’ETSI pour en faire une norme.
- **Mars 2025** — Le NIST publie [NIST AI 100-2 E2025](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf), taxonomie de référence des attaques contre l’apprentissage automatique.
- **Avril 2025** — Projet de norme internationale (DIS) de 46 pages, [référencé par DIN Media](https://www.dinmedia.de/en/draft-standard/iso-iec-dis-27090/391729195).
- **Juin 2025** — Divulgation d’[EchoLeak (CVE-2025-32711)](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html), injection de prompt sans clic dans Microsoft 365 Copilot.
- **Juillet 2025** — Fin du vote sur le DIS [S6].
- **Octobre–décembre 2025** — [Étude Anthropic–AISI–Turing](https://www.anthropic.com/research/small-samples-poison) sur l’empoisonnement par 250 documents (9 octobre) ; règle des deux de Meta (31 octobre) ; NCSC sur l’injection de prompt (8 décembre) ; Top 10 OWASP des applications agentiques (9 décembre) ; projet préliminaire du [profil Cyber AI du NIST](https://csrc.nist.gov/News/2025/nist-releases-prelim-draft-cyber-ai-profile) (16 décembre).
- **15 janvier 2026** — L’ETSI publie [EN 304 223](https://www.telecomtv.com/content/etsi/etsi-releases-world-leading-standard-for-securing-ai-54664/), première norme européenne de sécurité de base pour l’IA ; ISO/IEC 27090 la citera.
- **11 mars 2026** — Enregistrement comme projet final (FDIS) [S6] ; version FDIS datée de juin 2026.
- **27 juillet 2026** — Entrée en vigueur de l’[omnibus numérique sur l’IA (règlement (UE) 2026/1744)](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/) : obligations « haut risque » de l’annexe III reportées au 2 décembre 2027.
- **30 juillet 2026** — Clôture de l’enquête publique sur prEN 18282, rejeté par une majorité d’organismes nationaux [S8].
- **14 octobre 2026** — Publication d’ISO/IEC 27090:2026, 56 pages, en anglais [S2][S3].
- **18 octobre 2026** — Premiers commentaires de praticiens, dont l’article de départ [S1].

## 1. Ce qu’est la norme, et ce qu’elle n’est pas

ISO/IEC 27090 appartient à la famille 27000, celle de la sécurité de l’information, et non à la famille 42000 consacrée au management de l’IA. Ce rattachement dit l’essentiel : la norme regarde l’IA **comme un actif à protéger**, avec le vocabulaire et les réflexes de la sécurité de l’information (confidentialité, intégrité, disponibilité, menace, vulnérabilité). Le guide de l’ISO le formule nettement : il s’agit de protéger les systèmes d’IA contre les menaces, et non d’utiliser l’IA pour défendre d’autres systèmes [S4]. Son titre français, donné en page de titre, parle de « traitement des menaces et des situations susceptibles de compromettre les systèmes d’IA » [S3].

Trois caractéristiques en découlent.

- **Un document de recommandations.** La norme ne fixe pas d’exigences de système de management et ne se prête pas à un audit de certification. Le texte emploie bien « shall » dans la clause 5 (appliquer les mesures d’ISO/IEC 27002 selon les risques ; prendre en compte les compromissions du tableau 1 sur tout le cycle de vie) [S3], mais ces formulations renvoient à l’analyse de risques de chaque organisation et ne donnent rien de vérifiable par un auditeur. Les offres « certifiez-vous ISO 27090 » qui commencent à circuler, jusque dans les encarts publicitaires des catalogues de normes, relèvent du contresens.
- **Un public large.** La norme vise les organisations de toute taille, publiques ou privées, qui développent **ou utilisent** des systèmes d’IA [S2]. Elle ne se limite pas à l’IA générative : son tableau 2 indique, pour chaque compromission, si elle concerne l’IA générative, l’IA prédictive ou les deux, et si elle suppose un attaquant [S3].
- **Un texte d’assemblage.** Ses références normatives (ISO/IEC 22989 pour le vocabulaire, ISO/IEC 23053 pour le cadre de l’apprentissage automatique) et sa bibliographie croisent les normes ISO (27001, 27002, 23894, 42001, 5338, 38507, 5259-1), l’ETSI (EN 304 223, TR 104 128) et le NIST (SSDF, SP 800-218) [S3]. L’OWASP AI Exchange, projet ouvert sous licence CC0, indique avoir apporté **70 pages** de contenu au projet [S16] ; la part effectivement retenue dans le texte final n’est pas connue.

*Inférence pour la veille :* le choix du SC 27 plutôt que du SC 42 explique la tonalité du texte. La norme parle aux RSSI et aux équipes sécurité dans leur langue, ce qui facilite son intégration dans un SMSI ISO 27001 existant, mais elle hérite aussi des angles morts de cette culture : elle pense en actifs et en attaquants, beaucoup moins en comportements émergents ou en autonomie des systèmes.

## 2. Architecture du document

Le sommaire officiel [S3] montre un texte court et très concentré : sur 56 pages, la clause 6, consacrée aux compromissions, en occupe une vingtaine.

| Partie | Contenu | Pages |
|---|---|---|
| Introduction | Pourquoi l’IA ajoute des vulnérabilités : dépendance aux données, opacité du fonctionnement, attaques passant par des requêtes légitimes | vi–vii |
| 1 à 4 | Domaine d’application, références, **30 définitions** (dont les douze compromissions), abréviations | 1–5 |
| 5. Application de la sécurité de l’information | Généralités, programme de gouvernance de l’IA, principes de zéro confiance, génie logiciel, chaîne d’approvisionnement (cinq sous-parties), modélisation des menaces, red teaming | 5–10 |
| 6. Types de compromission | Tableaux 1 et 2, neuf sous-clauses détaillées (6.2 à 6.10), puis 6.11 « Considérations pour les systèmes d’IA » | 10–32 |
| 7. Mesures et interactions | Conflits entre mesures, continuité sur le cycle de vie, dégradation dans le temps, journalisation, protection de l’environnement de développement, filtrage des entrées, limitation d’usage, taille du modèle | 33–36 |
| Annexe A | Correspondance attaques / étapes du cycle de vie / actifs | 37–43 |
| Annexe B | Versions propres à l’IA d’attaques classiques : déni de service, chaîne d’approvisionnement, portes dérobées | 44–48 |
| Annexe C | Apprentissage fédéré | 49–50 |

La présence d’une annexe entière sur l’apprentissage fédéré, quand les agents n’ont pas de sous-clause, est un indice de l’époque où le texte a été conçu : la recherche en sécurité de l’apprentissage automatique d’avant 2023 s’intéressait beaucoup à ce mode d’entraînement réparti.

## 3. Le socle : la sécurité classique d’abord

La clause 5 est la plus utile pour une organisation qui découvre le sujet, parce qu’elle dit **par où commencer**. Son raisonnement tient en trois temps [S3].

D’abord, un système d’IA est un logiciel intégré dans un autre système, pas un modèle isolé. Tout ce qui protège les logiciels, les réseaux et les accès s’applique donc à lui, à toutes les étapes du cycle de vie. La norme en tire une recommandation de priorité qui mérite d’être retenue : si l’on craint le vol d’un modèle, mieux vaut d’abord durcir la pile qui l’héberge contre le **vol direct** des paramètres que de déployer des mesures coûteuses contre l’extraction par requêtes. L’article de départ résume justement cette idée [S1].

Ensuite, cinq pratiques organisationnelles encadrent l’IA :

- **Un programme de gouvernance de l’IA** (5.2), qui commence par un inventaire des systèmes d’IA et de leurs usages, puis une analyse et un traitement des risques ; la mise en œuvre renvoie à ISO/IEC 42001 et ISO/IEC 38507.
- **Les principes de zéro confiance** (5.3) : présumer la compromission, ne jamais faire confiance par défaut, chiffrer de bout en bout, vérifier chaque requête comme si elle venait de l’extérieur, appliquer le moindre privilège **y compris pour l’accès au modèle**, authentifier et autoriser chaque demandeur. La norme les décline pour les données d’entraînement (présumées pouvoir contenir des données empoisonnées), pour l’accès au modèle par API, intégration applicative ou RAG, et pour le fonctionnement des agents.
- **Les bonnes pratiques de génie logiciel** (5.4), complétées par des pratiques propres à l’IA : provenance et lignage des données, traçabilité des modèles, validation continue, tests d’obsolescence et de dérive.
- **La chaîne d’approvisionnement** (5.5), avec des sous-parties sur les menaces propres à l’IA, les chaînes complexes, les vecteurs d’attaque et les stratégies d’atténuation ; la norme renvoie aux mesures A.6.2.3 et A.6.2.6 d’ISO/IEC 42001 et au cadre SSDF du NIST.
- **La modélisation des menaces et le red teaming** (5.6 et 5.7), le second présenté comme le moyen d’éprouver le système avec les scénarios de la clause 6.

Enfin, la norme assume une approche par les risques : ses exemples ne sont « pas exhaustifs » et chaque organisation choisit les menaces pertinentes pour son système [S3].

*Inférence pour la veille :* cette clause rejoint presque mot pour mot la position de l’ANSSI en 2024 [A1] — sécuriser un système d’IA comme un système d’information complet, avec cloisonnement, moindre privilège et traçabilité — et celle de son document de février 2025 cosigné par une vingtaine d’agences, [*Développer la confiance dans l’IA par une approche par les risques cyber*](https://cyber.gouv.fr/sites/default/files/document/Document_Analyse_de_risques_FR.pdf). La convergence entre une norme internationale et les agences nationales est en soi une information : sur le socle, le consensus est acquis.

## 4. Les douze compromissions

La clause 6 range les compromissions selon l’actif touché et la propriété de sécurité compromise (tableau 1), puis selon qu’elles exigent un attaquant et concernent l’IA générative, prédictive ou les deux (tableau 2) [S3]. Les définitions de la clause 3 permettent de reconstituer la liste exacte. Neuf compromissions ont une sous-clause propre, construite chaque fois en quatre temps : description, défaillances qui en résultent, détection, atténuation. Les trois autres, qui relèvent de la sécurité classique (vol, fuite), sont définies mais sans sous-clause dédiée.

| Compromission (sous-clause) | Ce que fait l’attaquant, selon la définition de la norme | Propriété touchée | Ce que montre l’état de l’art |
|---|---|---|---|
| Empoisonnement des données (6.2) | Manipule des données pour modifier le comportement du système | Intégrité | 250 documents suffisent à implanter une porte dérobée dans des modèles de 600 millions à 13 milliards de paramètres, soit 0,00016 % des jetons d’entraînement ([Anthropic, AISI, Turing, oct. 2025](https://www.anthropic.com/research/small-samples-poison)) |
| Évasion (6.3) | Modifie les entrées, parfois de façon imperceptible, pour provoquer une erreur | Intégrité | Famille la mieux étudiée de la recherche ; défenses sans garantie robuste selon le [NIST](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf) |
| Inférence d’appartenance (6.4) | Détermine si une donnée a servi à l’entraînement | Confidentialité | Enjeu de protection des données personnelles, traité aussi par le futur ISO/IEC 27091 |
| Exfiltration de modèle (6.5) | Recrée un modèle équivalent par des requêtes répétées | Confidentialité | Campagnes de distillation à grande échelle attribuées en 2026 par Anthropic, OpenAI et Google (voir le [dossier sur la distillation](distillation-des-modeles-d-ia-methodes-accusations-preuves-et-enjeux-juridiques.md)) |
| Inversion de modèle (6.6) | Reconstitue tout ou partie des données d’entraînement à partir des sorties | Confidentialité | Risque accru pour les modèles affinés sur des données sensibles |
| Empoisonnement direct du modèle (6.7) | Manipule le modèle pendant le développement ou l’exploitation | Intégrité | Modèles piégés publiés sur des plateformes de partage ; porte dérobée dans la passerelle LiteLLM en mars 2026 ([Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)) |
| Sortie sensible (6.8) | Obtient par les sorties des éléments d’entrées passées : données d’entraînement, prompts d’autres utilisateurs | Confidentialité | Fuites de prompts système et de contextes RAG |
| Injection de prompt (6.9) | Introduit un contenu qui devient une instruction et déclenche un comportement non voulu | Intégrité, puis confidentialité | [EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html) (CVSS 9,3) ; hausse relative de 32 % des pages web piégées entre novembre 2025 et février 2026 ([Google](https://blog.google/security/prompt-injections-web/)) |
| Sortie porteuse d’injection (6.10) | Fait produire au modèle du code ou des commandes qui attaquent les systèmes en aval | Intégrité | Vecteur GrafanaGhost (rendu Markdown d’images) en avril 2026 ([CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/)) |
| Vol direct du modèle (déf. 3.19) | Obtient les paramètres confidentiels | Confidentialité | Relève de la sécurité classique de l’hébergement |
| Fuite directe des données d’entraînement (déf. 3.20) | Compromet la confidentialité du jeu d’entraînement | Confidentialité | Idem : contrôle d’accès et chiffrement des stockages |
| Fuite des entrées du modèle (déf. 3.21) | Compromet la confidentialité des données soumises en exploitation | Confidentialité | Enjeu central pour les usages d’outils du marché (données collées dans un assistant) |

Deux choix de conception méritent d’être soulignés. Le premier est le **niveau de connaissance de l’attaquant** : la norme définit des attaques sans connaissance, avec connaissance partielle ou totale du système, en précisant que ces deux dernières ne supposent pas de détenir des identifiants [S3]. Cette gradation, classique en recherche, aide à calibrer une analyse de risques : un modèle ouvert est par construction exposé aux attaques à connaissance totale. Le second est l’insistance de l’introduction sur la **requête légitime** : l’exfiltration de modèle passe par des interrogations qui ressemblent à un usage normal, de sorte que le contrôle d’accès ne suffit pas sans détection des usages suspects [S3][S4].

La sous-clause 6.11, « Considérations pour les systèmes d’IA », mérite une attention particulière, car c’est là que la norme sort de la logique attaque par attaque. Elle traite de la **limitation des données** pour réduire l’impact, de la **maîtrise des effets d’un comportement indésirable du modèle** en exploitation (supervision, moindre privilège du modèle, transparence, validation continue, explicabilité, tests de biais) et de la **provenance** des systèmes et des données [S3]. Ce sont, sous une autre forme, les principes que les praticiens des agents appliquent aujourd’hui.

## 5. Les mesures comme système : l’apport le plus original

La clause 7 part d’un constat simple qu’on trouve rarement dans les référentiels : une mesure de sécurité ne s’évalue pas seule [S4]. Elle peut en affaiblir une autre, réduire la performance du modèle, ou perdre son efficacité à mesure que le modèle, les données et les attaques évoluent. Les sous-clauses 7.2 à 7.4 traitent exactement ces trois points : conflits entre mesures, continuité sur le cycle de vie, dégradation du modèle et des protections dans le temps [S3].

Quelques exemples suffisent à montrer l’enjeu. L’entraînement adversarial, qui durcit un modèle contre l’évasion, peut le rendre plus vulnérable à l’inférence d’appartenance. La confidentialité différentielle, qui protège contre l’inversion et l’inférence, dégrade la précision. Masquer les scores de confiance gêne l’extraction mais prive les utilisateurs d’une information utile. Un filtre d’entrées réglé trop finement multiplie les faux positifs. Le commentaire de PlayCISO en tire une règle pratique : mesurer l’effet combiné des protections sur la précision avant de les empiler ([PlayCISO, 18 octobre 2026](https://playciso.com/blog/iso-iec-27090-ai-security-standard-what-ciso-should-do)).

Les mesures concrètes de la clause 7 sont ensuite assez classiques : journalisation et surveillance de l’usage du modèle, protection de l’environnement de développement, détection des entrées hors distribution et des entrées adverses, limitation du débit de requêtes, et optimisation de la taille du modèle [S3]. La dernière est la plus inattendue : un modèle plus petit que nécessaire offre moins de capacité à mémoriser, donc moins de prise à l’inversion et à l’inférence d’appartenance.

L’ensemble repose sur une logique de **défense en profondeur**, en reconnaissant explicitement que certaines menaces restent difficiles à détecter [S4].

*Inférence pour la veille :* c’est sur ce point que la norme apporte le plus aux organisations déjà équipées d’un SMSI. Un auditeur ISO 27001 vérifie qu’une mesure existe ; la clause 7 invite à vérifier qu’elle ne contredit pas les autres et qu’elle fonctionne encore six mois après le déploiement. Pour un système d’IA dont le modèle est mis à jour par un fournisseur sans préavis, cette question est permanente.

## 6. La place de la norme dans l’écosystème des référentiels

ISO/IEC 27090 n’arrive pas sur un terrain vide. En 2026, une organisation dispose d’une demi-douzaine de référentiels sérieux sur la sécurité de l’IA, de nature très différente. Le tableau suivant les situe par rapport à elle.

| Référentiel | Nature | Rapport avec ISO/IEC 27090 |
|---|---|---|
| **ISO/IEC 27001 / 27002** | Système de management de la sécurité, certifiable ; catalogue de mesures | Socle explicite : la norme s’y insère et les complète pour l’IA |
| **ISO/IEC 42001:2023** | Système de management de l’IA, certifiable ; certificateurs accrédités selon ISO/IEC 42006:2025 | Gouvernance d’ensemble de l’IA ; ISO/IEC 27090 en détaille le volet sécurité et renvoie à ses mesures A.6.2.3 et A.6.2.6 |
| **ISO/IEC 23894:2023** | Management du risque lié à l’IA | Cadre d’analyse de risques dans lequel insérer les menaces de la clause 6 |
| **ISO/IEC 27091** | Protection de la vie privée dans l’IA, au stade de projet final | Norme sœur du même sous-comité, pour les risques de vie privée |
| **ETSI EN 304 223** (janvier 2026) | Norme européenne de sécurité de base, 13 principes sur 5 phases du cycle de vie | Citée par ISO/IEC 27090 ; plus prescriptive, elle peut servir de liste de contrôle là où 27090 sert de catalogue de menaces |
| **prEN 18282** (CEN-CENELEC) | Future norme harmonisée pour l’article 15 de l’AI Act | Seule voie vers une présomption de conformité ; rejetée à l’enquête en juillet 2026 [S8] |
| **NIST AI 100-2 E2025** | Taxonomie des attaques adverses | Vocabulaire et classification plus détaillés, régulièrement mis à jour |
| **NIST IR 8596 et COSAiS** | Profil CSF 2.0 pour l’IA ; surcouches SP 800-53 (en préparation) | Équivalent américain orienté résultats, avec des déclinaisons prévues pour les agents |
| **OWASP Top 10 LLM et agentique** | Listes de risques d’application, gratuites, révisées tous les ans | Plus à jour sur l’injection de prompt et les agents ; l’OWASP AI Exchange a contribué au texte |
| **MITRE ATLAS** | Base de tactiques, techniques et cas réels d’attaques contre l’IA | Matériau pour la modélisation des menaces et le red teaming de la clause 5 |
| **ANSSI** (2024 et 2025) | Guide de 35 recommandations sur l’IA générative ; approche par les risques | Positions convergentes, plus prescriptives sur l’hébergement et le cloisonnement [A1] |

La lecture de ce tableau conduit à une répartition des rôles assez nette. **ISO/IEC 42001** dit comment gouverner l’IA, **ISO/IEC 27090** dit contre quoi la protéger et avec quelles familles de mesures, l’**ETSI** fixe un socle vérifiable, l’**OWASP** et **MITRE ATLAS** suivent la menace au rythme des incidents, et **prEN 18282** dira, le jour où il sera cité au Journal officiel, ce qui suffit juridiquement en Europe. Adam Leon Smith, spécialiste de la normalisation de l’IA, recommandait dès décembre 2025 de ne pas choisir entre ces textes mais de les empiler selon le besoin ([Substack, 11 décembre 2025](https://adamleonsmith.substack.com/p/which-standard-to-use-for-the-cybersecurity)).

## 7. Ce que la norme vaut en droit européen

La question juridique est celle où les commentaires sont les plus approximatifs. Trois textes sont en jeu.

### L’AI Act

L’article 15 impose aux systèmes d’IA à haut risque un niveau approprié d’exactitude, de robustesse et de cybersécurité sur tout leur cycle de vie. Son paragraphe 5 énumère les vulnérabilités propres à l’IA que les solutions techniques doivent permettre de prévenir, détecter, traiter et maîtriser : empoisonnement des données, empoisonnement de modèle par des composants pré-entraînés, exemples adverses ou évasion, attaques contre la confidentialité et défauts du modèle ([texte de l’article 15](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15)). La correspondance avec la clause 6 d’ISO/IEC 27090 est presque terme à terme, ce qui fait de la norme un bon outil de lecture de cet article.

Mais elle **ne confère aucune présomption de conformité** : seules les normes harmonisées citées au Journal officiel en confèrent, et ISO/IEC 27090 n’en est pas une [S6]. Or la norme harmonisée prévue, prEN 18282, a été rejetée à l’enquête publique close le 30 juillet 2026 ; un vote sur un périmètre révisé, plus proche du texte de l’AI Act, s’est clos le 16 septembre [S8]. L’objectif du CEN-CENELEC d’une disponibilité au quatrième trimestre 2026 paraît hors d’atteinte, et le mandat de normalisation expire le 28 février 2027 [S8].

Le calendrier a lui-même bougé. L’[omnibus numérique sur l’IA](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/), règlement (UE) 2026/1744 entré en vigueur le 27 juillet 2026, reporte au **2 décembre 2027** les obligations des systèmes à haut risque de l’annexe III et au **2 août 2028** celles des systèmes intégrés à des produits réglementés (annexe I).

### Le Cyber Resilience Act

L’article 12 du [règlement (UE) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) offre une autre voie : un produit comportant des éléments numériques qui est aussi un système d’IA à haut risque, et qui satisfait aux exigences essentielles de cybersécurité du CRA, est réputé satisfaire aux exigences de cybersécurité de l’article 15 de l’AI Act, à condition que la déclaration UE de conformité le démontre. L’exactitude et la robustesse restent régies par l’AI Act. Les obligations principales du CRA s’appliqueront à partir du 11 décembre 2027.

### NIS2

Pour les entités essentielles et importantes, NIS2 impose des mesures de gestion des risques « tenant compte de l’état des connaissances ». L’article de départ signale qu’un courrier d’août 2026 du Centre pour la cybersécurité Belgique aux entités essentielles invoque les menaces liées à l’IA de pointe pour justifier la priorité donnée aux mesures fondamentales [S1] ; ce courrier n’a pas pu être consulté directement.

*Inférence pour la veille :* le vide normatif européen donne à ISO/IEC 27090 un rôle plus important que son statut ne le laisse penser. Sans présomption de conformité, une organisation doit **démontrer** qu’elle a traité les risques selon l’état de l’art. Une norme internationale publiée, consensuelle et datée, à laquelle on peut rattacher une analyse de risques menace par menace, est le meilleur appui disponible pour cette démonstration devant une autorité de contrôle, un client ou un assureur, jusqu’à ce que prEN 18282 aboutisse. L’article 15 et la clause 6 parlant presque la même langue, le travail fait aujourd’hui avec ISO/IEC 27090 devrait se réutiliser largement le jour où la norme harmonisée sera citée — sans garantie, puisque son périmètre est en cours de révision.

## 8. Angles morts et critiques

Les critiques publiées sont encore rares, la norme ayant cinq jours. Elles viennent surtout du commentateur de référence des normes 27000 [S5], des travaux sur les agents [S6] et, indirectement, des agences qui ont publié entre-temps sur l’injection de prompt. Six limites ressortent.

1. **Les agents ne sont qu’effleurés.** La norme mentionne le fonctionnement des agents dans ses principes de zéro confiance [S3], mais aucune sous-clause ne traite l’abus d’outils, l’usurpation d’identité d’agent, l’empoisonnement de la mémoire, les communications entre agents ou les défaillances en cascade, qui forment l’essentiel du [Top 10 OWASP des applications agentiques](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications/) publié en décembre 2025. Or c’est là que se concentrent les incidents : le rapport OWASP de 2026 suit 53 projets d’agents, dont 28 agents de code, et l’injection de prompt figure dans six des dix catégories agentiques ([Help Net Security, 11 juin 2026](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)). Les travaux sur le droit européen relèvent d’ailleurs qu’aucune définition internationale de l’agent n’est encore stabilisée [S6].
2. **L’injection de prompt est traitée comme une menace parmi d’autres.** La sous-clause 6.9 tient en un peu plus d’une page et suit le schéma détection-atténuation. Le NCSC soutient au contraire que les modèles de langage ne séparent pas instructions et données, que l’injection ne peut donc pas être corrigée comme une injection SQL, et qu’il faut concevoir le système en supposant le modèle manipulable [S7]. Meta en a tiré sa règle des deux : un agent ne doit pas réunir sans supervision humaine entrées non fiables, accès à des données sensibles et capacité d’agir ou de communiquer vers l’extérieur. Les mesures de 6.11 (limitation des données, moindre privilège du modèle, supervision) vont dans ce sens, mais la norme ne hiérarchise pas : elle ne dit pas que le confinement par conception prime sur le filtrage.
3. **La menace considérée est étroite.** La norme se concentre sur des attaques délibérées menées par des adversaires compétents et laisse largement de côté les menaces accidentelles (défauts de conception, bogues) et les menaces internes [S5]. Pour un système d’IA, l’erreur de configuration d’un connecteur ou un agent trop permissif causent pourtant autant d’incidents que les attaques sophistiquées : la suppression d’une base de production par un assistant de code chez Replit, en 2025, n’impliquait aucun attaquant.
4. **L’IA comme arme est hors champ.** Le texte traite les attaques **contre** l’IA, pas les attaques **menées avec** l’IA [S4][S5]. Le choix est cohérent, mais le paysage a basculé : en septembre 2025, un acteur étatique a confié à Claude Code l’essentiel d’une campagne d’espionnage contre une trentaine d’organisations ([MITRE ATT&CK, C0062](https://attack.mitre.org/campaigns/C0062/)), et en mars 2026 un robot d’attaque autonome a compromis la chaîne de publication de LiteLLM. Le même agent peut être cible et outil ; une organisation devra chercher ailleurs comment traiter le second cas.
5. **L’orientation vers la détection.** L’introduction affirme qu’il ne sert à rien de développer des mesures sans détection efficace des menaces [S3]. Le commentateur de iso27001security juge cette position discutable : des mesures passives et générales, comme le cloisonnement ou le moindre privilège, protègent aussi contre des attaques qu’on ne détecte pas [S5]. La remarque compte d’autant plus que les menaces les plus graves pour les agents sont précisément celles qu’on détecte mal.
6. **Le temps normatif contre le temps de la menace.** Quatre ans séparent le lancement du projet de sa publication ; le projet soumis au vote date d’avril 2025, avant la plupart des incidents agentiques documentés. Le NIST reconnaît de son côté que les défenses disponibles n’offrent pas de garantie robuste [S13]. Une norme ISO est révisée tous les cinq ans environ ; la base MITRE ATLAS et les listes OWASP le sont plusieurs fois par an.

À ces limites de fond s’ajoute une limite d’accès : la norme coûte 204 francs suisses, n’existe qu’en anglais, et la licence ISO interdit de la diffuser en interne au-delà des usages autorisés [S3]. Les ressources gratuites qui couvrent le même terrain, comme l’OWASP AI Exchange sous licence CC0 [S16] ou les guides de l’ANSSI et du NCSC, resteront le premier contact des PME avec le sujet.

## 9. Ce que cela implique pour une organisation

L’article de départ propose de lire la norme comme un **catalogue** où puiser selon son profil, et non comme une liste à cocher intégralement [S1]. Cette lecture est la bonne, et la norme elle-même la justifie par son approche par les risques. Les trois profils proposés par InnovaSafe se prêtent bien à une correspondance avec les clauses.

| Profil | Exposition principale | Clauses prioritaires | Premières mesures |
|---|---|---|---|
| **Utilisateur d’outils du marché** (assistants, copilotes) | Fuite des entrées, sortie sensible, dépendance au fournisseur | 5.2, 5.5, 6.8, définition 3.21 | Inventaire des usages, y compris non déclarés ; règles sur les données partagées ; engagements contractuels des fournisseurs sur la conservation, l’entraînement et la notification d’incidents |
| **IA connectée aux données ou aux outils** (RAG, agents, automatisations) | Injection de prompt directe et indirecte, sortie porteuse d’injection, privilèges excessifs | 5.3, 6.9, 6.10, 6.11, 7.5, 7.8 | Moindre privilège par agent et par outil ; validation humaine des actions irréversibles ; journalisation des appels d’outils ; aucune combinaison non supervisée d’entrées non fiables, de données sensibles et de capacité d’action |
| **Entraînement ou adaptation de modèles** | Toute la clause 6, plus la chaîne d’approvisionnement | 5.4 à 5.7, 6.2 à 6.7, 7.2 à 7.4, 7.6 | Provenance et intégrité des jeux de données ; vérification des modèles tiers ; red teaming avant mise en production ; suivi de la dérive et réévaluation des protections après chaque mise à jour |

Le deuxième profil est jugé le plus exposé par l’article de départ [S1] ; les données d’incidents de 2026 lui donnent raison. Unit 42 en mars 2026, puis Forcepoint en avril, ont recensé des pages web contenant des instructions cachées destinées aux agents : virement PayPal de 5 000 dollars, suppression de sauvegardes, exfiltration de clés d’API [S22]. Le rapport OWASP de 2026 souligne qu’un seul des huit incidents majeurs du premier trimestre a reçu un identifiant CVE : les scanners de vulnérabilités classiques ne voient pas ces failles [S22].

Quatre conseils de méthode complètent ce tableau.

- **Ne pas créer de silo.** Les menaces de la clause 6 s’intègrent dans l’analyse de risques existante, qu’elle suive ISO/IEC 27005 ou EBIOS Risk Manager, et dans le SMSI déjà en place. C’est la recommandation de l’article de départ [S1] comme de la norme.
- **Séparer fournisseur et déployeur.** Une grande partie des menaces de la clause 6 (empoisonnement, inversion, exfiltration) se traite chez le fournisseur du modèle ; l’organisation qui déploie répond surtout de l’intégration, des accès, des données exposées et de la surveillance. Les questionnaires fournisseurs doivent le refléter : provenance du modèle, résultats de red teaming, politique de divulgation des failles d’agents.
- **Tenir un inventaire des composants d’IA.** Modèles, jeux de données, bibliothèques, serveurs MCP et connecteurs : l’incident LiteLLM et le premier serveur MCP malveillant observé en 2026 montrent que la chaîne d’approvisionnement de l’IA est déjà une cible.
- **Réévaluer après chaque changement de modèle.** La clause 7.4 s’applique à la lettre aux organisations dont le fournisseur change de version de modèle : les protections validées sur l’ancienne version doivent être retestées.

## Vérification des affirmations de l’article de départ

| Affirmation de l’article [S1] | Verdict | Source de la vérification |
|---|---|---|
| Norme publiée en octobre 2026 | **Confirmé** | Publication le 14 octobre 2026 [S2][S3] |
| Disponible uniquement en anglais | **Confirmé** | Seule une version anglaise de 56 pages est en vente ; le titre français figure en page de titre [S3] |
| Guide de recommandations, non certifiable | **Confirmé** | ISO [S4] ; aucune présomption de conformité [S6] |
| Une norme « pour la première fois » consacrée aux menaces sur l’IA | **Nuancé** | Première norme internationale ISO/IEC sur ce sujet ; l’ETSI EN 304 223 (janvier 2026) et le rapport technique ISO/IEC TR 24028 (2020) l’ont précédée |
| Neuf menaces propres à l’IA | **Nuancé** | Neuf sous-clauses détaillées, mais douze compromissions définies [S3] |
| Pour chaque menace : attaque, conséquences, détection, traitement | **Confirmé** | Structure description / défaillances / détection / atténuation de 6.2 à 6.10 [S3] |
| Sécuriser l’infrastructure est souvent plus rentable que des protections propres à l’IA | **Confirmé** | Clause 5.1, exemple du vol direct de modèle [S3] |
| Moindre privilège pour les agents d’IA | **Confirmé** | 5.3 (moindre privilège y compris pour l’accès au modèle, agents cités) et 6.11 [S3] |
| Les mesures peuvent se dégrader ou entrer en conflit | **Confirmé** | Clauses 7.2 et 7.4 [S3][S4] |
| ISO/IEC 42001 = gouvernance, ISO/IEC 27090 = volet sécurité | **Confirmé** | Distinction posée par l’ISO [S4] ; renvois à 42001 dans la clause 5 [S3] |
| L’article 15 de l’AI Act exige la robustesse face à l’empoisonnement ; la norme propose des pistes | **Nuancé** | Exact sur le fond, mais sans présomption de conformité, et obligations reportées à décembre 2027 et août 2028 par l’omnibus |
| Courrier du CCB d’août 2026 invoquant l’IA de pointe | **Non établi** | Courrier signalé par des sources secondaires (11 août 2026) ; document non consulté |

## Contrepoints

- **Une norme utile malgré son retard.** Le reproche d’arriver tard vaut pour toute norme consensuelle. L’ISO revendique d’ailleurs un rôle de socle : le texte complète les pratiques existantes et ne garantit pas l’immunité [S4]. Les listes OWASP et la base ATLAS, plus réactives, n’offrent pas la même légitimité devant un régulateur ou un auditeur ; les deux types de ressources se complètent plus qu’ils ne s’opposent.
- **La lecture « catalogue » a un revers.** Laisser chaque organisation choisir ses menaces suppose une analyse de risques compétente. Les organisations qui en ont le plus besoin, celles qui découvrent l’IA, sont aussi celles qui risquent d’écarter trop vite l’injection indirecte ou la chaîne d’approvisionnement. Un socle prescriptif comme l’ETSI EN 304 223 protège mieux contre cet écueil.
- **Les commentaires de praticiens sont des textes commerciaux.** L’article de départ comme celui de PlayCISO se terminent par une offre de service. Leurs synthèses sont fidèles sur les points vérifiés ici, mais leur insistance sur l’urgence relève aussi de la prospection.

## Limites et questions ouvertes

Ce dossier repose sur l’extrait officiel de la norme jusqu’à la clause 5.3 et sur des présentations fiables du reste ; les détails des sous-clauses 6.2 à 7.9 (mesures précises recommandées pour chaque menace, contenu des tableaux 1 et 2, annexe A) n’ont pas été lus dans le texte. Plusieurs faits récents reposent sur des sources secondaires : rejet de prEN 18282 (une seule lettre d’information spécialisée), courrier du CCB, chiffres du rapport OWASP de 2026. Ils sont signalés comme tels.

Trois questions restent ouvertes. **La norme sera-t-elle reprise en norme européenne ?** Une adoption par le CEN-CENELEC la rendrait plus visible en Europe, sans lui donner de présomption de conformité. **Que deviendra prEN 18282 ?** Son périmètre révisé dira si le travail fait avec ISO/IEC 27090 se réutilise tel quel. **Le SC 27 ouvrira-t-il un chantier sur les agents ?** Aucun projet de norme ISO/IEC consacré à la sécurité des agents n’a été repéré ; l’UIT en a fait un sujet prioritaire en juin 2026, et le NIST prépare des surcouches pour les systèmes mono- et multi-agents.

## Conclusion

ISO/IEC 27090 est une norme de bon sens plus qu’une norme de rupture. Elle dit d’abord que l’IA se protège comme le reste du système d’information, puis fournit un vocabulaire commun et un catalogue de douze compromissions que l’on peut verser dans une analyse de risques. Son apport le plus neuf est ailleurs : traiter les protections comme un système qui se contredit et s’use, ce qui correspond exactement à la vie d’un système d’IA dont le modèle change sous les pieds de ceux qui l’exploitent.

Ses faiblesses tiennent à son calendrier. Pensée avant l’essor des agents, elle les mentionne sans les traiter, et elle range l’injection de prompt parmi les menaces à détecter alors que les agences de sécurité la tiennent désormais pour un risque résiduel à confiner par conception. Une organisation qui l’adopterait seule serait bien armée contre l’empoisonnement ou l’extraction de modèle, moins contre l’agent trop permissif qui lit une page web piégée.

Sa valeur pratique, enfin, dépend du droit européen plus que d’elle-même. Tant que prEN 18282 n’est pas cité au Journal officiel, ISO/IEC 27090 est la meilleure référence publiée pour démontrer un traitement des menaces propres à l’IA conforme à l’état de l’art. Trois signaux diront si cette position dure : le sort de prEN 18282 au premier semestre 2027, une éventuelle adoption européenne de la norme, et l’ouverture d’un chantier international sur la sécurité des agents.

## Pour aller plus loin

- **[Extrait officiel de la norme sur iTeh](https://standards.iteh.ai/catalog/standards/iso/0b64ee20-3192-4976-a90f-9e16225dcab0/iso-iec-fdis-27090)** — sommaire, introduction et définitions : de quoi juger avant d’acheter.
- **[OWASP AI Exchange](https://owaspai.org/go/toc)** — ressource gratuite sous licence CC0, contributrice du texte, la plus proche de son contenu.
- **[NCSC, « Prompt injection is not SQL injection »](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)** — l’argument le plus clair pour concevoir les agents en supposant le modèle manipulable.
- **[NIST AI 100-2 E2025](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf)** — la taxonomie de référence des attaques adverses, plus détaillée que la clause 6.
- **[ANSSI, approche par les risques cyber (février 2025)](https://cyber.gouv.fr/sites/default/files/document/Document_Analyse_de_risques_FR.pdf)** — la version française et institutionnelle de la même démarche.
- **[Dossier : autonomie des systèmes d’IA](autonomie-des-systemes-dia-risques-et-mecanismes-de-controle.md)** — pour le versant agents et mécanismes de contrôle que la norme laisse ouvert.

## Sources

**Norme et normalisation**

- **[S2]** ISO, [fiche d’ISO/IEC 27090:2026](https://www.iso.org/standard/27090). Statut, édition, date. Consultée.
- **[S3]** iTeh Standards, [notice et extrait officiel](https://standards.iteh.ai/catalog/standards/iso/0b64ee20-3192-4976-a90f-9e16225dcab0/iso-iec-fdis-27090). Sommaire complet, introduction, clauses 1 à 5.3 lus ; la notice résumant les clauses 6 et 7 est une présentation commerciale, utilisée avec prudence.
- **[S4]** ISO, [« ISO/IEC 27090 explained »](https://www.iso.org/home/insights-news/resources/ISO-27090-explained.html). Guide rédigé d’après le projet final ; positionnement par rapport à 27001 et 42001.
- **[S5]** iso27001security.com, [fiche ISO/IEC 27090](https://www.iso27001security.com/html/27090). Structure et critiques (menace étroite, orientation vers la détection, IA comme arme hors champ).
- [DIN Media, projet DIS d’avril 2025](https://www.dinmedia.de/en/draft-standard/iso-iec-dis-27090/391729195) et [catalogue de l’ISS](https://iss.rs/en/project/show/iso:proj:56581). Pagination, prix, dates.
- **[S8]** AI Standardisation Watch, [édition 16](https://krogrules.com/news/edition-16-september-2026). État de prEN 18282 et des normes de JTC 21 ; source unique pour le rejet à l’enquête.
- [Adam Leon Smith, « Which standard to use for the cybersecurity of AI systems? »](https://adamleonsmith.substack.com/p/which-standard-to-use-for-the-cybersecurity), 11 décembre 2025. Comparaison 27090 / prEN 18282 / ETSI.
- [ETSI EN 304 223](https://www.telecomtv.com/content/etsi/etsi-releases-world-leading-standard-for-securing-ai-54664/), communiqué du 15 janvier 2026.
- [ENISA, *Cybersecurity of AI and Standardisation*](https://www.enisa.europa.eu/sites/default/files/publications/Cybersecurity%20of%20AI%20and%20Standardisation.pdf), mars 2023.

**Droit**

- **[S6]** Nannini, Smith et al., [*AI Agents Under EU Law*](https://arxiv.org/abs/2604.04604), avril 2026. Statut de la norme (pas de présomption de conformité), dates du DIS et du FDIS, lacunes sur les agents.
- [AI Act, article 15](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15), service d’assistance de la Commission.
- [Cyber Resilience Act, règlement (UE) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj), article 12.
- [ActuIA, omnibus 2026/1744](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/). Calendrier reporté ; source secondaire concordante avec plusieurs autres.

**Menace réelle et autres référentiels**

- **[S7]** NCSC, [« Prompt injection is not SQL injection »](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection), 8 décembre 2025.
- [Meta, « Agents Rule of Two »](https://ai.meta.com/blog/practical-ai-agent-security/), 31 octobre 2025.
- [Anthropic, AISI et Alan Turing Institute, empoisonnement par petits échantillons](https://www.anthropic.com/research/small-samples-poison), 9 octobre 2025. Résultat limité à une porte dérobée simple et à des modèles de 13 milliards de paramètres au plus.
- **[S13]** NIST, [AI 100-2 E2025](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf), mars 2025 ; [profil Cyber AI, projet préliminaire](https://csrc.nist.gov/News/2025/nist-releases-prelim-draft-cyber-ai-profile), 16 décembre 2025.
- [OWASP, Top 10 des applications agentiques](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications/), 9 décembre 2025.
- **[S16]** [OWASP AI Exchange](https://owaspai.org/go/toc). Licence CC0, 70 pages déclarées comme apportées au texte.
- [The Hacker News, EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html), juin 2025.
- [Google, injections de prompt sur le web](https://blog.google/security/prompt-injections-web/), avril 2026. Hausse relative ; sophistication jugée faible par Google.
- **[S22]** [Cloud Security Alliance, injection indirecte en conditions réelles](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/), 26 avril 2026. Synthèse de Unit 42, Google, Forcepoint et OWASP.
- [Help Net Security, rapport OWASP sur la sécurité agentique](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/), 11 juin 2026. LiteLLM, serveur MCP malveillant, CVE d’agents.
- [MITRE ATT&CK, campagne C0062](https://attack.mitre.org/campaigns/C0062/). Campagne orchestrée par IA, septembre 2025.
- [CISA, NSA et FBI, *AI Data Security*](https://www.cisa.gov/news-events/alerts/2025/05/22/new-best-practices-guide-securing-ai-data-released), 22 mai 2025.
- [Gouvernement britannique, Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice), 31 janvier 2025.
- [ANSSI, *Développer la confiance dans l’IA par une approche par les risques cyber*](https://cyber.gouv.fr/sites/default/files/document/Document_Analyse_de_risques_FR.pdf), février 2025.

**Commentaires de praticiens**

- **[S1]** [InnovaSafe, article de départ](https://www.innovasafe.be/article-iso-27090-securite-ia.html), 18 octobre 2026. Synthèse fidèle sur les points vérifiés ; article de cabinet de conseil.
- [PlayCISO](https://playciso.com/blog/iso-iec-27090-ai-security-standard-what-ciso-should-do), 18 octobre 2026. Lecture fournisseur / déployeur, arbitrages entre mesures ; texte promotionnel.

## Analyses internes utilisées et provenance

- **[A1] [ANSSI : *Recommandations de sécurité pour un système d’IA générative*](../analyses/recommandations-de-securite-pour-un-systeme-dia-generative.md)** — analyse du guide ANSSI-PA-102 d’avril 2024 ; mobilisée comme point de comparaison sur le socle de sécurité (cloisonnement, moindre privilège, maîtrise humaine des actions critiques). Les positions de l’ANSSI y sont rapportées comme positions, non comme exigences normatives.
