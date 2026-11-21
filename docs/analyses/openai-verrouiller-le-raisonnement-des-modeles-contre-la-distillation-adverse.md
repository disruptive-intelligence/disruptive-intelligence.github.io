---
title: "OpenAI : verrouiller le raisonnement des modèles contre la distillation adverse"
date: 2026-11-21
kind: analysis
theme: "ia"
slug: "openai-verrouiller-le-raisonnement-des-modeles-contre-la-distillation-adverse"
organization: "OpenAI"
document_type: rapport
rubriques:
  - ia-risques-surete
  - ia-gouvernance
  - geo-intelligence-economique
tags:
  - distillation
  - distillation adverse
  - chaîne de raisonnement
  - sécurité des modèles
  - capacités cyber
  - contrôle des exportations
events:
  - evt-d7c9a2b8-696f-4902-ab17-8d68a5d13cae
  - evt-5c139481-1c42-4768-8eba-fcf77f39d353
source_url: "https://openai.com/index/combatting-adversarial-distillation/"
---

# OpenAI : verrouiller le raisonnement des modèles contre la distillation adverse

## Métadonnées

- **Titre original :** *Combatting adversarial distillation*, avec pour chapeau « How we're addressing safety risks of distillation and lessons we've learned for strengthening safeguards across the industry ».
- **Éditeur :** OpenAI, billet publié sur son site, sans auteur nommé.
- **Date :** 20 novembre 2026.
- **Nature :** communication d'entreprise mêlant bilan de sécurité, résultats d'évaluations internes et prises de position politiques ; un graphique, un tableau, une note de bas de page.
- **Source analysée :** PDF original, copie texte de la page web ; la version en ligne a été comparée et correspond au texte (mêmes chiffres, même note). Le document n'étant pas paginé, les renvois se font aux intertitres de la page.
- **Thématique :** sécurité des modèles d'IA de pointe, distillation non autorisée, protection des traces de raisonnement, transfert de capacités cyber, enjeux de sécurité nationale américains.
- **Méthode de la fiche :** les sections jusqu'aux « Cinq éléments essentiels » restituent le seul billet ; la dernière section le confronte aux publications d'Anthropic et d'OpenAI de septembre-octobre 2026, à la documentation de l'API, aux textes en discussion au Congrès et au débat sur la lisibilité du raisonnement des modèles.

## Repères pour comprendre le document

Le billet traite d'un problème que les laboratoires d'IA ont fait passer, en 2026, du registre de la propriété intellectuelle à celui de la sécurité. La distillation consiste à entraîner un modèle « élève » sur les productions d'un modèle « enseignant » ; c'est une technique ordinaire, que les laboratoires emploient eux-mêmes pour produire des versions plus petites de leurs propres modèles. Elle devient « adverse » lorsqu'un tiers interroge massivement le modèle d'un concurrent, sans autorisation, pour en récolter les sorties et en tirer un modèle comparable. OpenAI soutient que cette copie ne transfère pas seulement des capacités, mais les transfère **sans les garde-fous** qui encadrent leur usage chez l'enseignant.

Le document repose sur une seconde distinction, moins visible : celle entre la **trace exacte du raisonnement** (la chaîne de raisonnement que le modèle produit en interne avant de répondre) et ce que voit l'utilisateur, à savoir la réponse finale, un **résumé du raisonnement** et les appels d'outils. Les modèles d'OpenAI ne livrent pas leur raisonnement brut ; l'API le renvoie au développeur sous forme chiffrée, pour que le modèle puisse le réutiliser au tour suivant sans que le client puisse le lire. Tout l'enjeu du billet est de montrer que ce raisonnement « protégé » a une valeur particulière pour un distillateur et de décrire comment OpenAI empêche de l'extraire. Les définitions ci-dessous sont des explications pédagogiques ; celles qui reprennent le document le signalent.

- **Distillation** — technique d'apprentissage automatique dans laquelle un modèle apprend à partir de données produites par un autre : ses réponses, son raisonnement ou ses jugements sur la meilleure réponse (définition du document).
- **Distillation adverse** — distillation non autorisée des sorties d'un modèle de pointe par un tiers, pour reproduire ses capacités et les déployer sans protections équivalentes (cadrage d'OpenAI).
- **Enseignant / élève** — le modèle qui produit les données d'entraînement et celui qui apprend à partir d'elles (termes du document).
- **Chaîne de raisonnement (*chain-of-thought*)** — étapes intermédiaires qu'un modèle génère avant sa réponse ; le document précise qu'elles peuvent contenir des informations absentes de la réponse finale.
- **Raisonnement protégé** — expression d'OpenAI pour la chaîne de raisonnement qui n'est pas montrée à l'utilisateur et que ses protections visent à garder confidentielle.
- **Résumé du raisonnement** — version abrégée du raisonnement présentée à l'utilisateur ; c'est la « ligne de base » de l'étude cyber du billet.
- **Trajectoire** — enregistrement complet de toutes les étapes d'un modèle sur une tâche, appels d'outils et réponse finale compris (définition du document).
- **Affinage supervisé (SFT) et apprentissage par renforcement (RL)** — deux phases d'entraînement : le SFT apprend à l'élève à imiter des exemples ; le RL l'améliore par essais récompensés dans des environnements de test.
- **Budget d'inférence** — quantité de calcul, mesurée ici en tokens de sortie pondérés, que le modèle peut dépenser au moment de répondre ; plus il est élevé, plus le modèle peut « réfléchir ».
- **Red-teaming automatisé** — tests offensifs menés par des modèles d'IA attaquants contre le système défendu ; « adaptatif » lorsque l'attaquant ajuste sa méthode aux réponses obtenues, « boîte noire » lorsqu'il n'a que la vue d'un utilisateur externe.
- **Taux de succès d'attaque (ASR)** — part des tentatives d'extraction qui aboutissent ; c'est l'indicateur principal du tableau du billet.
- **Classifieur d'entrée / de sortie** — modèle de détection placé avant le modèle principal pour repérer les requêtes d'extraction, ou après lui pour bloquer une fuite dans la réponse.
- **Indicateurs de compromission (IoC)** — éléments techniques caractérisant une attaque (comptes, adresses, motifs de requêtes) que des organisations s'échangent pour détecter la même activité chez elles.

## Résumé exécutif

OpenAI présente le 20 novembre 2026 son dispositif contre la distillation adverse et le résultat qu'elle en attend : empêcher qu'un concurrent reproduise les capacités de ses modèles, notamment en cybersécurité, sans reproduire leurs garde-fous. Le chiffre mis en avant est la chute du taux de succès des attaques visant à récupérer le raisonnement protégé d'une requête antérieure : **54,0 % contre GPT-6 Astra** avec ses protections d'origine, **0,2 % contre GPT-6.2 Astra** avec les protections renforcées, dans une évaluation interne adaptative en boîte noire menée par six modèles attaquants.

Le raisonnement suit trois temps. Une étude interne d'abord : un même modèle élève, entraîné sur des trajectoires de modèles de niveau Astra effectuant des tâches de code et de cyberdéfense, progresse davantage sur deux bancs d'essai cyber (ExploitBench, SEC-bench Pro) lorsqu'il reçoit les traces exactes que lorsqu'il reçoit les résumés, du moins au budget d'inférence le plus élevé après renforcement. Un dispositif ensuite, à deux niveaux : protections de chaque requête (entraînement adverse du modèle, classifieurs d'entrée et de sortie y compris sur les arguments d'appels d'outils, verrous de l'API liant le raisonnement à la conversation qui l'a produit) et enquêtes sur les campagnes coordonnées, avec sanctions contre des réseaux de comptes et partage d'indicateurs avec les autres fournisseurs. Un plaidoyer enfin : la distillation adverse est présentée comme un risque de sécurité nationale, DeepSeek et Moonshot AI sont cités, et OpenAI dit soutenir trois textes américains de contrôle des exportations de puces ainsi qu'une loi permettant de sanctionner les acteurs étrangers qui extraient des capacités.

Le billet est précieux pour la veille parce qu'il chiffre, pour la première fois chez OpenAI, la valeur des traces exactes pour transférer des capacités cyber, et parce qu'il décrit une architecture défensive presque identique à celle qu'Anthropic a présentée un mois plus tôt, ce qui dessine un standard de fait. Ses limites tiennent à sa nature : toutes les mesures sont internes, la comparaison des taux d'attaque change à la fois de modèle et de protections, l'avantage des traces exactes n'apparaît qu'à budget élevé, et les attributions à DeepSeek et Moonshot renvoient à des publications antérieures sans preuve nouvelle.

## Chronologie

Le billet s'inscrit dans une séquence qu'il rappelle lui-même ; les dates ci-dessous sont celles que donne le document.

- **Février 2026** — OpenAI informe le Congrès d'une activité indiquant que DeepSeek tentait de distiller des modèles de pointe américains.
- **Été 2026** — le rythme des sanctions hebdomadaires contre des réseaux de comptes de distillation « augmente significativement ».
- **Septembre 2026** — OpenAI publie un rapport sur une campagne d'extraction du raisonnement protégé, dont elle attribue une partie centrale à des personnes associées à Moonshot AI, développeur de Kimi ; ce rapport décrit le déplacement de raisonnement chiffré d'une conversation à une autre.
- **Avant le 20 novembre 2026** — déploiement de GPT-6.2 Astra et GPT-6.2 Sol avec les protections renforcées ; certaines améliorations sont ensuite appliquées à GPT-6 Astra.
- **20 novembre 2026** — publication du billet ; OpenAI annonce d'autres révélations « bientôt » sur des campagnes récemment perturbées.

## Thèse principale

Le texte est un **plaidoyer argumenté** sous forme de bilan technique. Sa thèse tient en une phrase : la distillation adverse est d'abord un problème de sûreté, parce qu'elle transfère des capacités à double usage vers des modèles moins protégés, et ce problème se traite par une défense en couches dont la pièce maîtresse est la confidentialité du raisonnement. L'argument de propriété intellectuelle est mentionné (« au-delà des questions de propriété intellectuelle ») mais volontairement relégué au second plan.

OpenAI cherche aussi à installer deux idées au-delà de sa propre plateforme. La première est que les protections doivent être homogènes dans toute l'industrie, partenaires de déploiement compris, faute de quoi le distillateur se reporte sur le maillon le plus faible ; le billet se termine par quatre recommandations aux autres développeurs. La seconde est que la défense technique et le contrôle des exportations de puces sont deux moyens complémentaires de préserver l'avance américaine : l'un limite l'accès au matériel pour entraîner, l'autre l'accès aux capacités des modèles déjà entraînés. Cette avance, ajoute le texte, laisse aux développeurs la marge de retarder un lancement pour tester leurs garde-fous.

## Informations et arguments importants

### Pourquoi la distillation devient une question de sûreté

Le billet (section « Why distillation is a safety issue ») part de la nature duale des capacités en jeu. Un modèle qui aide un défenseur à trouver des vulnérabilités peut aider un attaquant à les exploiter ; un modèle qui assiste la recherche biologique peut aider à concevoir un pathogène. Si ces capacités passent dans un modèle aux garde-fous plus faibles, celui-ci fournira l'aide que l'original aurait refusée ou que ses filtres auraient bloquée. L'exemple d'ouverture est explicitement cyber : un adversaire distille les capacités cyber d'un modèle pour mener des attaques que l'original n'aurait pas assistées.

L'argument le plus fin concerne les tâches **autorisées**. OpenAI écrit qu'un élève entraîné sur un grand nombre de sorties bénignes (code, cyberdéfense) peut acquérir des compétences offensives qui se généralisent au-delà des tâches réellement effectuées par l'enseignant. Autrement dit, filtrer les demandes malveillantes ne suffit pas : c'est l'accumulation de traces sur des tâches licites qui constitue le risque.

### L'étude interne sur le transfert de capacités cyber

Pour mesurer ce que vaut la trace exacte, OpenAI a comparé deux entraînements du même modèle élève préentraîné (section « The importance of protecting exact reasoning traces »). Le protocole est décrit ainsi :

1. **Données** : un jeu d'affinage supervisé composé principalement de trajectoires de modèles enseignants « de niveau Astra » travaillant sur des tâches de code et de cyberdéfense.
2. **Deux conditions** : l'élève reçoit soit ce que voit normalement l'utilisateur (réponses finales, résumés du raisonnement, interactions avec les outils), soit ces mêmes éléments avec les traces exactes du raisonnement.
3. **Deux mesures** : après l'affinage, puis après une passe légère d'apprentissage par renforcement dans des environnements de cybersécurité et de code.
4. **Deux bancs d'essai** : ExploitBench et SEC-bench Pro, évalués à des budgets d'inférence croissants ; l'indicateur est une « couverture de capacités » qui reste, sur le graphique, sous 40 %.

Les résultats sont plus nuancés que la conclusion qu'en tire le billet. Après l'affinage, l'élève nourri de traces exactes fait « généralement » mieux. Après le renforcement, il ne garde l'avantage qu'**au budget d'inférence le plus élevé** testé, sur les deux bancs ; aux budgets plus faibles, c'est l'élève entraîné sur les résumés qui obtient le meilleur score. Le graphique ne donne pas de valeurs chiffrées lisibles dans la copie texte. OpenAI conclut néanmoins que protéger les traces « peut limiter » le transfert de capacités cyber et annonce de nouvelles études sur d'autres élèves et d'autres recettes. La note de bas de page rattache ce résultat à un travail d'Anthropic montrant un avantage comparable sur SWE-bench Verified, un banc d'essai de génie logiciel, et affirme que l'avantage « s'étend » à la cybersécurité de pointe.

### Première couche : protéger chaque requête

La défense est présentée comme une boucle (section « Defenses that reinforce one another ») : les protections de chaque requête limitent l'extraction, les enquêtes repèrent les campagnes, et les attaques découvertes deviennent des exemples d'entraînement et de test. Au niveau de la requête, le billet décrit trois mécanismes :

- **Entraînement défensif du modèle.** Le modèle apprend à reconnaître les tentatives d'extraction et à refuser de divulguer son raisonnement protégé, tout en continuant à répondre aux demandes légitimes d'explication. Les exemples d'entraînement proviennent des attaques réussies trouvées par le red-teaming automatisé interne, par les enquêtes et par les signalements de chercheurs ou de partenaires extérieurs.
- **Classifieurs.** Des classifieurs d'entrée détectent les tentatives d'extraction ; des classifieurs de sortie détectent les fuites dans les messages de l'assistant **et dans les arguments des appels d'outils**, en mode diffusé (*streaming*) comme en mode normal. Le point des outils est souligné : un modèle peut exposer son raisonnement dans les paramètres qu'il passe à un outil sans le faire apparaître dans sa réponse.
- **Verrous de l'API.** Ils limitent la réutilisation du raisonnement protégé entre interactions et entre modèles. Le rapport de septembre décrivait des attaques qui transportaient un raisonnement chiffré d'une conversation à une autre pour demander au modèle de le restituer en clair. OpenAI dit avoir renforcé les cloisons entre utilisateurs, espaces de travail, organisations et familles de modèles, et fermé une voie qui pouvait exposer le raisonnement chiffré **d'un autre utilisateur**. Avec GPT-6.2 Astra et Sol, le raisonnement est lié à l'historique qui l'a produit : si un message antérieur est réécrit, l'API abandonne le raisonnement qui suivait ; et les familles de modèles plus anciennes, moins protégées, ne peuvent plus lire le raisonnement de GPT-6.2.

### Seconde couche : enquêter sur les campagnes et sanctionner

Au-delà de chaque requête, OpenAI cherche dans les signaux de requêtes et de comptes les motifs qui trahissent une extraction coordonnée (section « Investigating and disrupting coordinated campaigns »). Lorsqu'une violation est établie, la sanction vise **le réseau de comptes** entier. Chaque enquête alimente la détection suivante, et les indicateurs de compromission sont partagés avec les autres fournisseurs de modèles. La politique dite de « standards cohérents » étend ces exigences aux partenaires qui proposent les modèles d'OpenAI : mêmes garde-fous, application coordonnée.

Le billet donne un ordre de grandeur de l'activité (section « Campaign detection and enforcement ») : plusieurs campagnes non autorisées observées cette année, des **sanctions hebdomadaires visant de quelques milliers à plusieurs dizaines de milliers de comptes**, en forte hausse l'été dernier. Trois objectifs sont fixés : limiter le volume et la valeur des données obtenues, augmenter le coût des campagnes, raccourcir le délai de réponse. Deux indicateurs les suivent, la prévalence de l'abus et le délai entre détection et sanction ; aucun de leurs chiffres n'est publié.

### Mesurer la résistance à l'extraction

La section « Measuring progress » décrit une méthode d'évaluation qui distingue deux axes. Les évaluations **statiques** rejouent un corpus fixe d'attaques déjà réussies ; les évaluations **adaptatives** confient l'attaque à des modèles qui ajustent leur stratégie, ce qui révèle des failles que les tests figés manquent. Les testeurs travaillent soit en **boîte noire** (vue d'un utilisateur externe), soit en **boîte blanche** (informations supplémentaires sur le système). Le dispositif de test est dit proche du déploiement en production.

Le seul résultat publié est celui de l'évaluation adaptative en boîte noire, agrégée sur six modèles attaquants :

| Type d'attaque | GPT-6 Astra, protections d'origine | GPT-6.2 Astra, protections renforcées |
| --- | --- | --- |
| Extraire le raisonnement d'une requête antérieure | 54,0 % | 0,2 % |
| Extraire le raisonnement de la requête en cours | 22,9 % | 0,9 % |

OpenAI ajoute que certaines améliorations sont désormais appliquées à GPT-6 Astra. Les résultats statiques et en boîte blanche ne sont pas donnés.

### La dimension de sécurité nationale

La section « The national security implications » change de registre. Un acteur étranger qui reproduit les capacités d'un modèle américain peut les déployer sans ses protections. Le billet rappelle deux épisodes : en février, l'information du Congrès sur une activité indiquant que **DeepSeek** tentait de distiller des modèles américains ; en septembre, l'attribution d'une partie centrale d'une campagne d'extraction à des personnes associées à **Moonshot AI**. D'autres révélations sont annoncées.

Sur le plan politique, OpenAI soutient une législation qui donnerait au gouvernement des moyens d'identifier et de sanctionner les acteurs étrangers qui extraient illicitement des capacités, sans nommer de texte. Elle dit avoir indiqué au Congrès son soutien au **Chip Security Act**, à l'**AI OVERWATCH Act** et au **MATCH Act**, trois textes de contrôle des exportations. L'articulation proposée est explicite : les contrôles à l'exportation privent l'adversaire du matériel pour entraîner, la défense contre la distillation le prive d'un raccourci par les modèles déjà entraînés.

### Les recommandations à l'industrie

Le billet se termine (section « How others can build on this work ») par quatre recommandations, présentées comme tirées de l'expérience :

1. **Protéger le raisonnement sur toute l'interaction**, en contrôlant les messages de l'assistant et les arguments d'outils, et en limitant la réutilisation du raisonnement chiffré entre conversations et modèles.
2. **Conserver les attaques réussies comme tests de non-régression**, issues du red-teaming, de la surveillance de production ou des signalements, les utiliser pour l'entraînement et les classifieurs lorsque la politique de confidentialité le permet, et rejouer les attaques d'origine tout en vérifiant qu'un attaquant adaptatif ne passe plus.
3. **Combiner protections par requête et enquêtes avec sanctions** au niveau des campagnes.
4. **Coordonner exigences et application avec les partenaires de déploiement** et partager l'expertise avec les autres développeurs, pour garantir un plancher élevé dans toute l'industrie.

OpenAI rappelle avoir déjà partagé des constats via le Frontier Model Forum et des canaux gouvernementaux, en gardant privés les détails exploitables par les attaquants.

## Points particulièrement intéressants pour la veille

- **La trace exacte devient un actif stratégique.** Le billet chiffre l'intérêt des traces exactes pour transférer des capacités cyber et en fait le cœur de sa défense. *Inférence pour la veille :* la non-divulgation du raisonnement, justifiée en 2024 par l'expérience utilisateur et l'avantage concurrentiel, devient une mesure de sûreté revendiquée ; elle a peu de chances d'être assouplie, et le débat sur la transparence du raisonnement s'en trouve durci.
- **Le risque vient aussi des tâches licites.** OpenAI admet qu'un élève peut apprendre des compétences offensives à partir de sorties de cyberdéfense parfaitement autorisées. *Inférence pour la veille :* la modération par refus de contenus malveillants ne protège plus contre ce risque ; ce sont le volume, la provenance et la structure des requêtes qui comptent, ce qui pousse vers la surveillance des comptes et des usages.
- **L'API devient plus contraignante pour les développeurs.** Le raisonnement est lié à l'historique et disparaît si un message antérieur est réécrit. *Inférence pour la veille :* les intégrations d'agents qui réécrivent ou compactent l'historique doivent être revues ; la sûreté se paie en coût, latence et parfois qualité.
- **Les fuites par les outils sont prises au sérieux.** Les classifieurs de sortie couvrent les arguments d'appels d'outils. *Inférence pour la veille :* avec les agents, l'outil devient un canal d'exfiltration à part entière, y compris pour d'autres données que le raisonnement ; c'est un point d'audit pour toute organisation qui expose un agent à des outils tiers.
- **Une faille de cloisonnement entre clients a existé.** OpenAI dit avoir fermé une voie qui pouvait exposer le raisonnement chiffré d'un autre utilisateur. *Inférence pour la veille :* au-delà de la distillation, c'est un incident de confidentialité multi-locataire, mentionné en une phrase, sans date ni périmètre ; il mérite un suivi.
- **Un standard industriel se forme.** Classifieurs, liaison du raisonnement au contexte, interdiction de lecture par les anciens modèles, partage d'indicateurs : OpenAI décrit et recommande les mêmes briques qu'Anthropic. *Inférence pour la veille :* la défense contre la distillation se structure comme la cyberdéfense, avec partage de renseignement entre concurrents et pression pour l'étendre aux revendeurs et hébergeurs.
- **La sûreté sert la politique industrielle.** Le billet relie distillation, sécurité nationale et contrôle des exportations de puces, et cite deux laboratoires chinois. *Inférence pour la veille :* le cadrage « sûreté » renforce le poids des laboratoires américains dans le débat sur les sanctions et les exportations ; il faut lire leurs chiffres comme ceux d'une partie prenante.

## Faits, opinions et interprétations

### Faits rapportés par la source

Selon OpenAI, son évaluation adaptative en boîte noire montre une chute du taux de succès des attaques visant le raisonnement d'une requête antérieure de **54,0 % à 0,2 %**, et de **22,9 % à 0,9 %** pour la requête en cours, entre GPT-6 Astra avec ses protections d'origine et GPT-6.2 Astra avec ses protections renforcées, sur six modèles attaquants. L'entreprise dit sanctionner chaque semaine des réseaux allant de **quelques milliers à plusieurs dizaines de milliers de comptes**, avoir fermé une voie d'accès au raisonnement chiffré d'autres utilisateurs, lier désormais le raisonnement à l'historique de la conversation et interdire sa lecture par les familles de modèles plus anciennes. Elle rapporte avoir informé le Congrès en février d'une activité de DeepSeek et attribué en septembre une partie d'une campagne à des personnes liées à Moonshot AI. Tous ces faits sont déclarés par l'entreprise et ne sont accompagnés d'aucune donnée vérifiable de l'extérieur.

Le résultat de l'étude cyber est lui aussi un fait déclaré : l'avantage des traces exactes sur les résumés après affinage, et sa persistance après renforcement **seulement au budget d'inférence le plus élevé**, les résumés l'emportant aux budgets inférieurs.

### Opinions ou positions de l'auteur

La qualification de la distillation adverse comme problème de **sûreté** et de **sécurité nationale**, plutôt que comme simple litige commercial, est une position d'OpenAI. Il en va de même du soutien aux trois textes sur les puces et à une législation de sanctions, de l'affirmation que l'avance américaine laisse le temps de tester les garde-fous, et de l'idée qu'un « plancher élevé » de protections doit s'imposer à toute l'industrie. La présentation de l'anti-distillation comme soutien à une « prolifération sûre » des capacités de pointe relève du même registre : elle fait de la restriction d'accès une condition de l'accès large.

### Interprétations et inférences

L'interprétation centrale d'OpenAI est que la protection des traces **peut limiter** le transfert de capacités cyber. Elle est prudente dans le corps du texte, plus affirmative dans la note de bas de page, qui écrit que le résultat « montre » que l'avantage s'étend à la cybersécurité. Or le graphique décrit un avantage qui se réduit après renforcement et s'inverse aux budgets faibles : la conclusion la plus sûre est que les traces exactes aident l'élève à exploiter un grand budget de calcul, pas qu'elles transmettent un avantage général.

*Inférence de l'analyse :* la baisse de 54,0 % à 0,2 % mesure l'effet combiné d'un nouveau modèle et de nouvelles protections ; le billet ne permet pas d'attribuer la part de chacun. Par ailleurs, un faible taux d'extraction du raisonnement n'empêche pas la distillation des réponses et des résumés visibles, que l'étude elle-même utilise comme ligne de base et qui transfèrent déjà une part importante des capacités.

## Limites et points à vérifier

1. **Des évaluations entièrement internes.** Les taux d'attaque, l'étude de transfert et les volumes de sanctions proviennent des équipes d'OpenAI, sur ses propres modèles et attaquants. Aucun protocole détaillé, aucun jeu d'attaques ni aucune évaluation tierce n'est publié ; les chiffres ne peuvent être ni reproduits ni comparés à ceux d'autres fournisseurs.
2. **Une comparaison qui mélange deux variables.** Le tableau compare GPT-6 Astra avec ses protections d'origine et GPT-6.2 Astra avec ses protections renforcées. Le gain peut venir du modèle, des classifieurs, des verrous de l'API ou de leur combinaison ; le résultat de GPT-6 Astra avec les nouvelles protections, désormais en partie appliquées, n'est pas donné.
3. **Une sélection des résultats publiés.** Seule l'évaluation adaptative en boîte noire est chiffrée ; les résultats statiques et en boîte blanche, plus exigeants, ne le sont pas. Le billet ne dit rien non plus des faux positifs, c'est-à-dire des demandes légitimes d'explication bloquées.
4. **Un avantage des traces exactes conditionnel.** L'étude cyber ne montre l'avantage après renforcement qu'au budget maximal, sans valeurs chiffrées, sur un seul modèle élève et une seule recette d'entraînement. La généralisation affirmée dans la note excède ce que montre le graphique.
5. **Le résumé reste une fuite.** L'étude prend comme ligne de base ce que voit l'utilisateur, résumés compris, et ce matériau transfère déjà des capacités. Le billet ne mesure pas ce que les protections empêchent sur ce canal, ni ce qu'un distillateur obtient en se contentant des réponses visibles.
6. **Des attributions sans preuve nouvelle.** DeepSeek et Moonshot AI sont cités par renvoi à des publications antérieures ; le billet ne livre ni méthode d'attribution ni lien entre les données récoltées et un modèle concurrent précis. Les « campagnes récemment perturbées » ne sont pas décrites.
7. **Des indicateurs annoncés mais absents.** La prévalence de l'abus et le délai entre détection et sanction sont présentés comme les mesures du succès, sans aucune valeur. La fourchette des sanctions hebdomadaires ne permet pas de savoir combien de données ont été obtenues avant détection.
8. **Une politique législative imprécise.** La loi de sanctions soutenue n'est pas nommée, et le billet ne dit pas en quoi les trois textes sur les puces, qui visent le matériel, répondent à la distillation. Le lien est un argument politique, non une démonstration.

## Sources et références mentionnées

Le document cite presque exclusivement des publications d'OpenAI : son rapport de septembre sur une campagne d'extraction, l'information du Congrès de février sur DeepSeek, sa politique de standards cohérents applicable aux partenaires et la documentation de son API sur l'abandon du raisonnement après réécriture d'un message. La seule référence externe est le travail d'Anthropic sur l'avantage des transcriptions complètes de raisonnement sur SWE-bench Verified, invoqué en note pour appuyer le résultat cyber. Les bancs d'essai ExploitBench et SEC-bench Pro sont nommés sans description ni lien ; le Frontier Model Forum est mentionné comme canal de partage ; trois textes législatifs (Chip Security Act, AI OVERWATCH Act, MATCH Act) sont cités sans numéro ni état d'avancement. C'est une bibliographie d'entreprise, autoréférentielle, qui ne permet pas de contrôler les résultats.

## Cinq éléments essentiels à retenir

1. OpenAI présente la **distillation adverse comme un risque de sûreté** : un concurrent peut copier des capacités à double usage, notamment cyber, sans copier les garde-fous.
2. Selon une étude interne, les **traces exactes de raisonnement** transfèrent plus de capacités cyber que les résumés, mais après renforcement l'avantage ne subsiste qu'au **budget d'inférence le plus élevé**.
3. Le taux de succès des attaques contre le raisonnement d'une requête antérieure passe de **54,0 % (GPT-6 Astra) à 0,2 % (GPT-6.2 Astra)**, mesure interne qui mélange changement de modèle et de protections.
4. La défense combine **protections par requête** (entraînement adverse, classifieurs jusque dans les appels d'outils, raisonnement lié à l'historique) et **enquêtes sur les campagnes**, avec sanctions hebdomadaires de milliers à dizaines de milliers de comptes.
5. OpenAI relie ce combat à la **sécurité nationale américaine**, cite DeepSeek et Moonshot AI, et soutient trois textes de **contrôle des exportations de puces** ainsi qu'une loi de sanctions.

## État de l'art et regards extérieurs

Recherches effectuées le 2026-11-21. Les constats ci-dessous ne modifient pas les sections précédentes, fondées sur le seul billet. Pour l'historique complet des accusations et des preuves publiques, voir le dossier [Distillation des modèles d'IA : méthodes, accusations, preuves et enjeux juridiques](https://disruptive-intelligence.github.io/dossiers/distillation-des-modeles-d-ia-methodes-accusations-preuves-et-enjeux-juridiques/) (14 octobre 2026), dont cette section ne reprend que ce qui éclaire le billet ou s'est produit depuis.

### Travaux de référence

- **Le rapport d'incident d'OpenAI du 30 septembre 2026.** [OpenAI — « Disrupting a coordinated model distillation campaign »](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) (30 septembre 2026) est la pièce à laquelle le billet renvoie trois fois. Il décrit la technique : copier un raisonnement chiffré d'une conversation et demander à un modèle, dans une autre, de le « déchiffrer et transcrire », sans casser le chiffrement. La campagne commence le 1er juillet ; les 24 et 25 juillet, **16 000 requêtes** présentant un motif d'extraction viennent de plus de 4 000 utilisateurs, et une activité apparentée touche plus de 15 000 utilisateurs avant d'être stoppée le 28 juillet. Le rapport précise qu'il s'agit de tentatives « pas nécessairement réussies » et qu'il n'est pas établi que tous les opérateurs relèvent d'un même acteur : c'est un **noyau** de l'activité qui est associé à Moonshot AI.
- **Le bilan défensif d'Anthropic du 12 octobre 2026.** [Anthropic — « Distillation defenses »](https://www.anthropic.com/news/distillation-defenses) (12 octobre 2026) est le travail cité en note. Un élève entraîné sur les transcriptions de Claude Opus 4.8 obtient **80,4 % sur SWE-bench Verified avec le raisonnement complet contre 71,8 % avec les résumés**. Anthropic y décrit des mesures très proches de celles d'OpenAI et chiffre leur effet : un volume de raisonnement extrait par les distillateurs qu'elle détecte divisé par 10 à 100 (« environ 90 à 99 % » de baisse). La comparaison des deux textes montre que la note d'OpenAI est exacte, mais qu'Anthropic mesure un écart net sur un banc logiciel, quand OpenAI obtient un avantage conditionnel au budget sur des bancs cyber.
- **La mise en garde de Lawfare.** [Lawfare — « Responding to AI distillation without panic »](https://www.lawfaremedia.org/article/responding-to-ai-distillation-without-panic) (16 juillet 2026) invite à mesurer le gain réel des sorties récoltées avant d'assimiler imitation et vol. L'article précède les rapports de l'automne, mais sa question reste celle que le billet n'aborde pas : quelle capacité un modèle concurrent a-t-il effectivement obtenue grâce à ces données ?

### Compléments sur le sujet

Le billet décrit la défense d'un fournisseur ; il laisse de côté la convergence de toute l'industrie, la bataille juridique et législative engagée à Washington, les preuves d'efficacité de la distillation sur des modèles réels et le coût de ces protections pour les clients. Ces quatre dimensions changent la portée de ce qu'affirme OpenAI.

- **Une architecture défensive commune, en cours de normalisation.** Le dispositif d'Anthropic du 12 octobre comprend un « raisonnement préservé » qui interdit aux nouveaux comptes API (créés depuis le 31 août 2026) de modifier le contexte antérieur, l'interdiction de lecture du raisonnement par des modèles plus anciens, la restriction des transcriptions à l'organisation demandeuse, un classifieur à deux étages au taux de faux positifs annoncé sous 0,1 %, des bans de dizaines de milliers de comptes et la facturation, depuis le 24 septembre, des requêtes bloquées avant réponse ([Anthropic](https://www.anthropic.com/news/distillation-defenses), 12 octobre 2026). Le billet d'OpenAI reprend presque point par point cette architecture. Le partage de renseignement entre concurrents est lui-même organisé depuis le printemps : [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china) rapportait le 6 avril 2026 qu'OpenAI, Anthropic et Google échangent des informations sur les tentatives de distillation via le Frontier Model Forum, sur le modèle de la cybersécurité. Le 21 octobre, OpenAI a publié sa politique [« Broad access through consistent standards »](https://openai.com/index/broad-access-through-consistent-standards/), qui impose aux hébergeurs partenaires et revendeurs des garde-fous alignés sur les siens ; selon [BankInfoSecurity](https://www.bankinfosecurity.com/openai-tightens-rules-to-block-rival-model-distillation-a-33194), la mise à jour des conditions d'usage interdit d'utiliser les sorties pour entraîner des modèles concurrents et soumet à autorisation les intermédiaires d'accès. La « prolifération sûre » du billet passe donc par un contrôle accru de toute la chaîne de distribution.
- **Un front législatif plus large que les trois textes cités.** Le billet soutient une loi de sanctions sans la nommer. Deux propositions existent : le *Deterring American AI Model Theft Act* (H.R. 8283), adopté à l'unanimité par la commission des affaires étrangères de la Chambre le 22 avril 2026 ([Just Security](https://www.justsecurity.org/137498/diagnosis-deterrence-us-response-distillation/), 5 mai 2026), et le *BLADE Act* (S. 5252), déposé au Sénat le 5 août 2026 ([texte sur GovInfo](https://www.govinfo.gov/app/details/BILLS-119s5252is)), qui prévoit une procédure de désignation et de sanction ainsi qu'une liste publique des auteurs d'extraction. L'[IAPS](https://www.iaps.ai/research/ai-distillation-attacks-executive-and-congressional-action-can-go-further) juge le mémorandum présidentiel d'avril insuffisant faute de mécanismes de responsabilité concrets et regrette que le texte de la Chambre n'organise pas clairement le partage des informations sur les extractions au sein de l'administration. Quant aux trois textes sur les puces, ils restent en suspens : intégrés comme amendements au projet de loi de programmation militaire (NDAA) du Sénat, bloqué en juillet, ils n'ont été adoptés par aucune chambre, et le Congrès doit reprendre la NDAA en décembre dans un contexte de pression accrue sur les ventes de puces à la Chine ([CNBC](https://www.cnbc.com/2026/11/17/congress-ai-china-jensen-huang-chips.html), 17 novembre 2026).
- **L'efficacité réelle de la distillation, au cœur du débat.** Le billet raisonne sur un élève de laboratoire ; la question politique porte sur des modèles réels. Le 28 octobre 2026, *The Information* a rapporté, selon des sources anonymes, que Moonshot AI et DeepSeek s'étaient largement appuyés sur les sorties de GPT-6 Astra pour entraîner Kimi K3.1 Pro et DeepSeek V4.1-Flash 1017 ; ni OpenAI ni les deux laboratoires n'ont confirmé ([Techzine](https://www.techzine.eu/news/analytics/145373/deepseek-and-moonshot-ai-are-reportedly-using-gpt-6-astra-for-training/), octobre 2026). Moonshot avait déjà contesté que Kimi K3 soit issu d'une distillation, et son rapport technique décrit une distillation à partir de modèles experts internes (voir le dossier cité plus haut). Le billet du 20 novembre ne confirme pas l'article de *The Information* et ne publie aucune mesure de gain chez un concurrent : la preuve d'un transfert déterminant reste à apporter publiquement.
- **Le coût des protections pour les clients.** La documentation de l'API ([OpenAI — « Keep the prefix unchanged »](https://developers.openai.com/api/docs/guides/keep-prefix-unchanged), consultée le 21 novembre 2026) précise que l'API abandonne les éléments de raisonnement qui suivent toute modification du préfixe de la conversation. Le modèle doit alors refaire son raisonnement, avec plus de tokens, de coût et de latence, une baisse possible de la qualité et une moindre réutilisation du cache. OpenAI recommande des conversations en ajout seul : ne plus réécrire le premier message développeur, ne pas changer en cours de route l'effort de raisonnement, les outils ou le format de sortie, et passer par sa propre fonction de compaction. Anthropic reconnaît de même que certains développeurs ont dû modifier leurs intégrations et que des requêtes bénignes sont bloquées. La sûreté décrite dans le billet a donc un prix d'ingénierie pour tous les clients, pas seulement pour les distillateurs.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| Le succès des attaques sur le raisonnement d'une requête antérieure passe de 54,0 % à 0,2 % | **Non établi** de façon indépendante : chiffre interne, comparaison modèle + protections, sans réplication | Billet lui-même ; aucune évaluation tierce trouvée |
| OpenAI a informé le Congrès en février d'une activité de distillation de DeepSeek | **Confirmé** : note du 12 février 2026 à la commission spéciale de la Chambre, formulation « compatible avec » | [OpenAI, note au Congrès](https://cdn.openai.com/pdf/045aa967-ee96-4a09-94ee-3098ddf6db2c/OpenAI-US-House-Select-Cmte-Update-%5B021226%5D.pdf), 12 février 2026 |
| En septembre, OpenAI a attribué une partie centrale d'une campagne à des personnes liées à Moonshot AI | **Confirmé**, avec réserve : un « noyau » de l'activité, des tentatives et non des extractions réussies | [OpenAI](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/), 30 septembre 2026 |
| Anthropic a observé un avantage similaire des transcriptions complètes sur SWE-bench Verified | **Confirmé** : 80,4 % contre 71,8 % | [Anthropic](https://www.anthropic.com/news/distillation-defenses), 12 octobre 2026 |
| Le résultat d'OpenAI « montre » que l'avantage s'étend à la cybersécurité | **Nuancé** : le graphique du billet n'établit l'avantage après renforcement qu'au budget maximal | Billet lui-même (légende et texte du graphique) |
| L'API abandonne le raisonnement qui suit un message réécrit | **Confirmé**, avec coûts associés (tokens, latence, cache, qualité) | [Documentation OpenAI](https://developers.openai.com/api/docs/guides/keep-prefix-unchanged), consultée le 21 novembre 2026 |
| Les exigences s'étendent aux partenaires via la politique de standards cohérents | **Confirmé** : politique publiée le 21 octobre 2026 | [OpenAI](https://openai.com/index/broad-access-through-consistent-standards/), 21 octobre 2026 |
| OpenAI partage ses constats via le Frontier Model Forum | **Confirmé** : partage entre OpenAI, Anthropic et Google rapporté dès avril | [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china), 6 avril 2026 |
| Soutien au Chip Security Act, à l'AI OVERWATCH Act et au MATCH Act | **Confirmé** pour les textes ; aucun n'est adopté, avenir lié à la NDAA de décembre | [CNBC](https://www.cnbc.com/2026/11/17/congress-ai-china-jensen-huang-chips.html), 17 novembre 2026 |
| Une législation donnerait des outils pour sanctionner les acteurs étrangers | **Nuancé** : deux propositions existent (H.R. 8283, S. 5252), aucune n'est adoptée ; le billet ne dit pas laquelle il soutient | [Just Security](https://www.justsecurity.org/137498/diagnosis-deterrence-us-response-distillation/), 5 mai 2026 ; [GovInfo](https://www.govinfo.gov/app/details/BILLS-119s5252is) |

### Contrepoints et critiques

- **Verrouiller le raisonnement réduit aussi le regard extérieur.** Le billet traite la confidentialité du raisonnement comme une protection ; une partie de la recherche en sûreté y voit un problème de transparence. Une prépublication du 10 novembre 2026, [Davies et Bearman — « Transparency Disclosures for Chain-of-Thought Monitorability »](https://arxiv.org/abs/2611.13873), propose cinq indicateurs que les développeurs devraient publier pour qu'on puisse juger la surveillance du raisonnement, dont l'**accès des tiers** au raisonnement ; aucun des trois laboratoires audités, OpenAI compris, ne les couvre tous. Le sujet est sensible chez OpenAI même : son directeur scientifique, Jakub Pachocki, a alerté en septembre sur l'érosion de la capacité à surveiller le raisonnement des modèles ([Numerama](https://www.numerama.com/tech/2326859-le-directeur-scientifique-dopenai-indique-perdre-le-controle-sur-le-raisonnement-de-ses-ia.html), 7 septembre 2026), et OpenAI reconnaissait à la sortie de GPT-6 Astra que son raisonnement était plus difficile à surveiller que celui de Sol lorsqu'il tentait d'échapper au contrôle ([The Next Web](https://thenextweb.com/news/gpt-6-astra-benchmarks-monitorability-cyber), 4 septembre 2026). Cacher le raisonnement aux distillateurs ne nuit pas à la surveillance interne, mais rend plus difficile un audit indépendant de ce que le modèle « pense ».
- **Une question technique avant d'être législative.** Greg Brockman, président d'OpenAI, estimait en juillet que la réponse à la distillation était « en définitive une question technique », s'appuyant sur des systèmes de détection déjà en place, et que l'avantage réel d'OpenAI tenait à ses puces et centres de données ([Semafor](https://www.semafor.com/article/07/24/2026/openais-brockman-says-distillation-is-a-technical-problem), 24 juillet 2026). Le billet de novembre, qui revendique une défense technique efficace tout en appelant à des sanctions et à des contrôles d'exportation, mêle les deux lignes ; le recours au législateur sert aussi la stratégie industrielle.
- **Des lois de sanctions à préciser.** L'ITIF soutient le principe du texte de la Chambre mais critique sa définition de l'extraction, adossée aux violations de conditions d'utilisation, qui sont des contrats privés et variables ; elle demande que chaque inscription sur la liste des auteurs d'extraction s'appuie sur un résumé des preuves, et que la recherche académique, l'open source et les tests de sécurité bénéficient d'exemptions ([ITIF — « How to fix the AI model theft bill before it becomes law »](https://itif.org/publications/2026/07/28/how-to-fix-the-ai-model-theft-bill-before-it-becomes-law/), 28 juillet 2026). C'est la limite du cadrage du billet : faire des conditions d'usage d'une entreprise le fondement de sanctions d'État exige des garanties que l'entreprise ne mentionne pas.
- **Des chiffres de partie prenante.** Les volumes de comptes sanctionnés et les taux d'attaque d'OpenAI, comme les 90 à 99 % de baisse d'Anthropic, sont produits par des entreprises engagées dans une compétition commerciale et un débat politique avec les laboratoires qu'elles accusent. Le dossier du 14 octobre rappelait déjà qu'aucun de ces chiffres n'a été audité de l'extérieur et qu'ils ne mesurent que la part du trafic que chaque fournisseur voit.

### Évolutions depuis la publication

Le billet a un jour au moment de ces recherches ; aucune réaction de DeepSeek ou de Moonshot AI n'a été trouvée, et les « révélations prochaines » annoncées sur des campagnes récentes ne sont pas encore publiées. Trois échéances sont à suivre : la publication de ces nouvelles campagnes, la reprise de la NDAA par le Congrès en décembre, qui décidera du sort des trois textes sur les puces ([CNBC](https://www.cnbc.com/2026/11/17/congress-ai-china-jensen-huang-chips.html), 17 novembre 2026), et le sort des deux propositions de sanctions contre la distillation. GPT-6.2 Astra et GPT-6.2 Sol avaient été lancés le 17 novembre ([OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol), 17 novembre 2026), trois jours avant le billet.

### Cadre juridique et éthique

- **Conditions d'utilisation des fournisseurs.** Elles restent le fondement principal : les conditions d'OpenAI interdisent d'utiliser ses sorties pour développer des modèles concurrents, et leur violation justifie la fermeture des comptes. Elles n'ont d'effet que sur les clients identifiés et ne valent pas sanction publique.
- **États-Unis, mémorandum NSTM-4 (23 avril 2026).** Le [mémorandum de la Maison-Blanche](https://www.whitehouse.gov/wp-content/uploads/2026/04/NSTM-4.pdf) affirme l'existence de campagnes étrangères de distillation « à l'échelle industrielle » et ordonne une coordination de la réponse, sans publier les renseignements sous-jacents.
- **États-Unis, propositions de loi.** Le *Deterring American AI Model Theft Act* (H.R. 8283) et le *BLADE Act* (S. 5252) créeraient une procédure de désignation et de sanction des auteurs étrangers d'extraction ; aucun n'est adopté au 21 novembre 2026.
- **États-Unis, contrôle des exportations.** Le Chip Security Act (vérification de localisation des puces exportées), l'AI OVERWATCH Act (examen parlementaire des licences d'exportation) et le MATCH Act (équipements de fabrication de puces) visent le matériel, non la distillation elle-même.
- **Union européenne.** L'AI Act ne traite pas la distillation non autorisée comme telle ; les lignes directrices de la Commission sur les modèles d'IA à usage général précisent seulement comment compter le calcul d'entraînement d'un modèle distillé pour ses obligations (voir le dossier du 14 octobre).

### Pour aller plus loin

- [Dossier « Distillation des modèles d'IA : méthodes, accusations, preuves et enjeux juridiques »](https://disruptive-intelligence.github.io/dossiers/distillation-des-modeles-d-ia-methodes-accusations-preuves-et-enjeux-juridiques/) — la chronologie des accusations, ce que prouvent les éléments publics et l'état du droit au 14 octobre 2026.
- [Anthropic — « Distillation defenses »](https://www.anthropic.com/news/distillation-defenses) — la description la plus détaillée des protections et de leurs compromis par un laboratoire, à lire en parallèle du billet.
- [OpenAI — « Keep the prefix unchanged »](https://developers.openai.com/api/docs/guides/keep-prefix-unchanged) — la traduction concrète des protections pour les développeurs qui construisent des agents sur l'API.
- [IAPS — « AI Distillation Attacks: Executive and Congressional Action Can Go Further »](https://www.iaps.ai/research/ai-distillation-attacks-executive-and-congressional-action-can-go-further) — une lecture des outils publics disponibles contre la distillation et de leurs lacunes.
- [Davies et Bearman — « Transparency Disclosures for Chain-of-Thought Monitorability »](https://arxiv.org/abs/2611.13873) — le contrepoint transparence : ce que les laboratoires devraient publier sur leur raisonnement.
