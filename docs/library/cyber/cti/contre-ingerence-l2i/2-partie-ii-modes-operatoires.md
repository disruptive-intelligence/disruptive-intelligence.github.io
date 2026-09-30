---
title: PARTIE II — MODES OPÉRATOIRES
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
chapter: 2
chapters: 7
---

---

## Chapitre 6 — Anatomie d'une opération d'influence : le cycle opérationnel

### 6.1 Le modèle en 5 phases

Une opération d'influence structurée suit un cycle opérationnel qui peut être décomposé en cinq phases, inspiré du modèle kill chain adapté au domaine informationnel.

**Phase 1 — Reconnaissance.** L'opérateur cartographie l'environnement informationnel cible : fractures sociétales exploitables, sujets de polarisation, personnalités influentes, écosystème médiatique, fonctionnement algorithmique des plateformes ciblées, contexte politique (élections, crises, événements). Cette phase est analogue à la reconnaissance en cybersécurité — elle vise à identifier les vulnérabilités de l'espace informationnel. VIGINUM a documenté comment Storm-1516 adapte ses narratifs en fonction des contextes politiques de chaque pays cible, ciblant les thématiques les plus clivantes du moment (immigration en France, corruption présumée aux États-Unis, fractures sociétales en Allemagne).

**Phase 2 — Préparation.** L'infrastructure est mise en place : création de comptes sur les plateformes (avec photos de profil générées, biographies construites, historique factice de publications non politiques pour construire une apparence de légitimité), enregistrement de noms de domaine pour les sites de réinformation, mise en place des canaux d'amplification (Telegram, newsletters), production des contenus (articles, vidéos, deepfakes, memes). La préparation peut s'étaler sur plusieurs mois : le rapport VIGINUM sur Storm-1516 documente que certains comptes utilisés par le MOI ont été créés jusqu'à un an avant leur activation dans une opération.

**Phase 3 — Déploiement (injection).** Les narratifs sont injectés dans l'espace informationnel. Cette phase est critique et souvent le point le plus vulnérable de l'opération — le primo-diffuseur est le plus exposé à la détection. Storm-1516 utilise trois vecteurs de primo-diffusion : des comptes jetables sur X (créés et abandonnés après usage), des tiers rémunérés (influenceurs payés pour partager le contenu), et des publications sur le réseau de faux sites CopyCop. La primo-diffusion est souvent discrète et s'appuie sur un nombre limité de comptes.

**Phase 4 — Amplification.** Le contenu primo-diffusé est massivement amplifié par un réseau coordonné : retweets synchronisés, partages dans des groupes Facebook, republication sur des chaînes Telegram, intégration dans des newsletters. Le blanchiment (*laundering*) est une étape clé : le contenu passe de sources manifestement suspectes à des sources semi-légitimes (médias étrangers rémunérés, blogs d'opinion, comptes d'influenceurs idéologiques) puis potentiellement à des médias mainstream. Storm-1516 illustre cette mécanique : les contenus du MOI sont primo-diffusés par des comptes jetables, blanchis par des médias étrangers rémunérés et des comptes de réseaux sociaux rémunérés, puis amplifiés par des influenceurs liés à la Fondation pour combattre l'injustice (FCI) et l'Association des journalistes des BRICS (BJA), avant d'être repris par des médias d'État russes et des canaux Telegram russophones.

**Phase 5 — Exploitation.** L'opérateur capitalise sur l'impact : le narratif a pénétré le débat public, des médias mainstream en parlent (même pour le contester), des personnalités politiques le relayent ou le commentent, la perception publique est modifiée. Le rapport VIGINUM note que certains narratifs de Storm-1516 ont été repris par des sénateurs et membres de la Chambre des représentants américains, notamment pour justifier des positions sur l'aide à l'Ukraine. L'exploitation peut aussi inclure l'alimentation de la propagande interne — les narratifs anti-occidentaux de Storm-1516 sont systématiquement repris par des canaux Telegram russophones pour alimenter le récit domestique russe.

### 6.2 Le framework DISARM

Le framework DISARM (*Disinformation Analysis and Risk Management*), anciennement AMITT, est le principal cadre de référence pour décrire les opérations d'influence de manière structurée. Créé en 2018, il reprend la logique de la matrice MITRE ATT&CK en cybersécurité : une matrice de tactiques, techniques et procédures (TTPs) adaptée au domaine informationnel.

DISARM structure les opérations en quatre grandes phases — planification, préparation, exécution, évaluation — et décompose chaque phase en tactiques (étapes de haut niveau) et techniques (activités observables). Par exemple, la tactique « Élaborer les récits » (TA14) inclut des techniques comme « Exploiter des récits existants » (T0003), « Développer des récits contradictoires » (T0004), « Exploiter des théories conspirationnistes » (T0022) ou « Intégrer les vulnérabilités des audiences cibles dans les récits » (T0083).

VIGINUM a fait le choix stratégique d'exploiter DISARM pour standardiser ses pratiques et faciliter le partage de la connaissance au sein de la communauté de la lutte contre les manipulations de l'information. Le service a publié en février 2024 une traduction française de la matrice Red Team, déposée sur GitHub. L'EEAS utilise également DISARM dans le cadre STIX (*Structured Threat Information eXpression*) pour encoder les incidents FIMI de manière interopérable.

L'intérêt opérationnel de DISARM est double : il fournit un **langage commun** pour décrire les opérations (essentiel pour la coopération inter-agences et internationale) et il permet l'**analyse comparative** des TTPs entre différents acteurs et opérations, facilitant l'attribution (un acteur a un « style » opérationnel caractéristique). L'annexe B de ce cours présente la matrice de référence avec le mapping vers les chapitres.

### 6.3 Les indicateurs d'opération (IOI)

Par analogie avec les IoC (Indicators of Compromise) en cybersécurité, les IOI (*Indicators of Information Operations*) sont les marqueurs observables d'une opération d'influence. Ils portent sur trois dimensions.

**Indicateurs comportementaux** : création massive de comptes dans une fenêtre temporelle courte, patterns de publication coordonnés (publications à quelques minutes d'intervalle), ratios d'engagement anormaux (un compte avec 50 followers dont les posts obtiennent 5000 retweets), activité à des horaires incompatibles avec le fuseau horaire affiché, utilisation de copy-pasta (messages identiques ou quasi identiques publiés par de nombreux comptes).

**Indicateurs d'infrastructure** : domaines enregistrés récemment chez des registrars anonymes, serveurs hébergés chez des hébergeurs complaisants (*bulletproof hosting*), certificats SSL partagés entre plusieurs sites apparemment sans lien, utilisation de services d'anonymisation (Cloudflare, Njalla), templates WordPress identiques sur des sites différents.

**Indicateurs de contenu** : narratifs apparaissant simultanément sans antécédent organique, contenu traduit avec des erreurs idiomatiques spécifiques, images générées par IA avec des artefacts caractéristiques, documents fuitées dont la provenance ne peut être établie, contenu émotionnellement chargé et polarisant de manière systématique.

La détection repose sur la convergence de ces indicateurs — un indicateur isolé est un signal faible, un faisceau d'indicateurs convergents est un signal exploitable. La qualification comme opération d'influence suppose une analyse approfondie qui distingue la coordination inauthentique d'une mobilisation organique intense (Ch.12).

### 6.4 Le rapport coût/impact

Les opérations d'influence sont probablement l'arme la plus rentable du spectre hybride. Le budget mensuel de l'IRA pour l'opération 2016 était estimé à 1,25 million de dollars — une fraction infinitésimale du budget de défense d'un État, pour un impact politique considérable. Le coût d'une opération de type Storm-1516 est probablement encore plus faible : quelques opérateurs, des outils d'IA générative accessibles, une infrastructure web modeste. Le 4e rapport EEAS utilise d'ailleurs le concept de « FIMI Deterrence Playbook » qui vise précisément à augmenter le coût des opérations pour les acteurs malveillants, en frappant les maillons critiques (intermédiaires, proxies, fournisseurs de services).

L'asymétrie est structurelle : créer et diffuser une fausse information est rapide et peu coûteux. La détecter, la qualifier, l'attribuer et la contrer demande infiniment plus de temps, de compétences et de ressources. C'est le « dilemme du défenseur » informationnel — un concept qui résonne directement avec le même dilemme en cybersécurité.

### 6.5 Cas concret détaillé : reconstruction d'une opération documentée

Pour illustrer le cycle opérationnel, prenons l'exemple reconstitué d'une opération Storm-1516 documentée par VIGINUM. En octobre 2024, le MOI a diffusé un faux témoignage vidéo accusant Timothy Walz, colistier de Kamala Harris, d'avoir agressé sexuellement l'un de ses anciens élèves.

**Préparation.** La vidéo met en scène un individu se présentant comme « Matthew Metro », réel ancien élève du lycée concerné dont les traits ont probablement été usurpés à partir de photos collectées sur ses comptes de réseaux sociaux. Un compte X (@MattMetro) a été créé en octobre 2023, un an avant l'opération — illustrant l'anticipation dans la phase de préparation.

**Déploiement.** La vidéo a été publiée sur le compte @MattMetro et primo-diffusée par des comptes jetables maîtrisés par les opérateurs.

**Amplification.** Le contenu a été repris et amplifié par des influenceurs liés à la FCI et la BJA, relayé par des médias pro-russes, et partagé sur Telegram. En moins de 24 heures, la vidéo a atteint plus de cinq millions de vues sur X.

**Exploitation.** Le narratif visait à décrédibiliser le ticket démocrate à quelques semaines de l'élection présidentielle américaine. Le fait que des médias et fact-checkers aient dû répondre et démonter le faux témoignage a lui-même contribué à amplifier la visibilité du narratif — l'effet Streisand inversé.

---

## Chapitre 7 — Astroturfing et réseaux de comptes inauthentiques

### 7.1 Définition et mécanique

L'astroturfing — du nom du gazon synthétique Astroturf — désigne la création artificielle d'une apparence de mobilisation populaire spontanée. Dans le contexte des opérations d'influence, il s'agit de faire croire qu'un narratif, une pétition, un hashtag ou une cause bénéficie d'un soutien large et organique alors qu'il est porté par un réseau de comptes coordonnés inauthentiques.

Le terme de *Coordinated Inauthentic Behavior* (CIB), popularisé par Meta dans ses rapports de transparence, est devenu la terminologie de référence. Il désigne l'usage coordonné de faux comptes ou de comptes trompeurs pour manipuler le débat public. Le concept met l'accent sur le comportement (inauthenticité, coordination) plutôt que sur le contenu — ce qui permet d'éviter le piège de l'arbitrage de la vérité.

VIGINUM utilise le concept de « mode opératoire informationnel » (MOI), défini comme un ensemble de comportements, d'outils, de tactiques, techniques et procédures et de ressources adverses mis en œuvre par un acteur ou un groupe d'acteurs malveillants dans le cadre d'une ou de plusieurs opérations informationnelles numériques. Ce concept est plus large que le CIB de Meta, car il ne se limite pas aux réseaux sociaux et intègre l'ensemble de la chaîne d'influence (sites web, newsletters, médias, relais physiques).

### 7.2 Techniques de création de comptes

La création de comptes inauthentiques a considérablement évolué. Les « fermes de comptes » rudimentaires (profils avec des photos volées, des noms incohérents et un historique vide) sont de moins en moins efficaces face à la détection automatisée des plateformes. Les opérations contemporaines utilisent des techniques plus sophistiquées.

Les **comptes générés** utilisent des photos de profil créées par des générateurs d'images IA (GAN puis modèles de diffusion), des noms culturellement calibrés pour la zone cible, des biographies construites avec une apparence de crédibilité, et un historique factice de publications non controversées (photos de nourriture, commentaires sportifs, memes) avant l'activation dans une opération. La qualité des photos générées par IA a progressé au point de rendre la détection visuelle difficile — les artefacts caractéristiques des GANs (reflets asymétriques, boucles d'oreilles incohérentes, arrière-plans flous) sont de moins en moins présents dans les modèles de diffusion récents. Cependant, les détecteurs automatiques de photos générées restent des signaux exploratoires, pas des verdicts (voir Ch.15 et le cours OSINT Mastery Ch.14 pour le détail technique).

Les **comptes achetés** sur des marketplaces spécialisées offrent l'avantage d'un historique réel, d'un réseau de followers organique et d'une ancienneté qui résiste aux vérifications de surface. Le marché des comptes de réseaux sociaux anciens est actif et structuré, avec des prix variant selon la plateforme, l'ancienneté, le nombre de followers et le domaine géographique.

Les **comptes dormants réactivés** sont des comptes créés longtemps à l'avance, maintenus avec une activité minimale, puis activés au moment d'une opération. Storm-1516 a utilisé cette technique avec le compte @MattMetro, créé un an avant son utilisation opérationnelle.

### 7.3 Techniques d'amplification

L'amplification est le mécanisme par lequel un contenu initialement diffusé par un nombre limité de comptes atteint une audience massive. Plusieurs techniques sont documentées.

La **coordination temporelle** est le marqueur comportemental le plus caractéristique : les comptes publient ou partagent le même contenu dans des fenêtres temporelles serrées (typiquement 5 à 15 minutes). Cette synchronicité est un indicateur fort d'opération coordonnée, car elle est statistiquement improbable dans une diffusion organique. VIGINUM a documenté cette technique dans les opérations du Baku Initiative Group, où des comptes publiaient des messages avec les mêmes hashtags dans des fenêtres anormalement étroites.

Le **hashtag hijacking** consiste à s'emparer d'un hashtag existant (populaire ou lié à un événement en cours) pour y injecter du contenu manipulé, ou à créer un hashtag dédié et le propulser dans les tendances par la coordination de comptes inauthentiques.

L'**achat d'engagement** (likes, followers, vues, retweets) est un service commercial facilement accessible qui permet de gonfler artificiellement la visibilité et la crédibilité apparente d'un contenu ou d'un compte. Les tarifs sont dérisoires : quelques dizaines d'euros pour des milliers de likes ou de followers.

Les **publicités sponsorisées** ont été détournées pour amplifier des contenus de désinformation — l'opération Doppelgänger/RRN utilisait des publicités ciblées sur Facebook pour diriger les utilisateurs vers des clones de sites médiatiques avec des articles modifiés. Le DSA a renforcé les obligations de transparence sur les publicités politiques, mais les contournements restent possibles.

### 7.4 Plateformes spécifiques

Chaque plateforme a des caractéristiques qui influencent la manière dont les opérations s'y déploient.

**X (ex-Twitter)** reste la plateforme la plus documentée dans les rapports d'analyse, en partie parce que son API a historiquement permis une collecte et une analyse systématique des données. Le 3e rapport EEAS note que X représentait 88 % de l'activité FIMI détectée en 2024. L'évolution de la plateforme post-rachat (réduction de la modération, réintégration de comptes suspendus, modification de l'API) a modifié l'écosystème : davantage de comptes inauthentiques actifs mais aussi des restrictions d'accès aux données qui compliquent la recherche et la détection.

**TikTok** est un terrain d'opération croissant en raison de son algorithme de recommandation particulièrement puissant — un contenu peut devenir viral sans que le compte auteur n'ait de base d'abonnés significative. Cette caractéristique rend TikTok vulnérable à l'amplification organique involontaire de contenus manipulés. En revanche, l'accès aux données pour les chercheurs reste très limité et la modération opaque, ce qui complique l'analyse.

**Telegram** est devenu l'espace central de l'amplification et de la coordination des opérations d'influence. La quasi-absence de modération (avec une inflexion partielle après l'arrestation de Pavel Durov en août 2024), l'absence d'API publique exploitable, et la possibilité de créer des canaux de diffusion unidirectionnels avec un nombre illimité d'abonnés en font un vecteur privilégié. Le rapport VIGINUM sur Storm-1516 documente l'utilisation de chaînes Telegram pour la diffusion des narratifs vers les audiences russophones et internationales.

**Facebook/Instagram (Meta)** reste important pour le ciblage de communautés via les groupes fermés et la publicité ciblée. Meta publie des rapports CIB réguliers et a développé les capacités de détection les plus avancées parmi les plateformes, mais le volume de contenus rend la modération exhaustive impossible.

### 7.5 Limites et contre-mesures

Les plateformes détectent et suppriment régulièrement des réseaux de CIB — les *takedowns* sont documentés dans les rapports de transparence. Cependant, la reconstitution des réseaux après suppression est rapide et peu coûteuse. Un réseau de comptes supprimé sur X peut être remplacé en quelques jours. Le déplacement vers des plateformes moins modérées (Telegram, Rumble, Odysee, VKontakte) est une réponse classique aux takedowns.

La coopération entre VIGINUM et les plateformes, bien que renforcée en 2024, reste « objectivement en-deçà des attentes légitimes » selon le rapport d'activité de VIGINUM, notamment sur l'accès aux APIs nécessaires à l'identification des ingérences.

> **🔵 BROUILLARD — Épisode 3**
> L'analyse approfondie des 47 comptes initiaux révèle un réseau plus étendu. Parmi les comptes identifiés, 38 ont des photos de profil présentant des caractéristiques compatibles avec une génération par IA — mais l'analyse est nuancée : les détecteurs automatiques (Is It AI, Hive Moderation) donnent des résultats contradictoires sur certains profils. L'analyse manuelle identifie des artefacts subtils (texture de l'arrière-plan, incohérence de la ligne des cheveux) sur la majorité des images. Neuf comptes sont des comptes anciens avec un changement de nom récent — probablement achetés. En élargissant la recherche par analyse de réseau (qui retweet qui, qui partage les mêmes URLs), le réseau s'étend à plus de 200 comptes sur X, 50 comptes Facebook, 12 canaux Telegram, et 3 sites web de réinformation avec une newsletter commune. Élise documente les indicateurs d'opération dans sa fiche d'analyse.

---

## Chapitre 8 — Contenu manipulé et IA générative

### 8.1 Taxonomie du contenu manipulé

Le contenu manipulé recouvre trois catégories distinctes qui ne posent pas les mêmes problèmes de détection.

Le **contenu fabriqué** est créé de toutes pièces : articles inventés présentés comme des reportages, faux documents officiels, deepfakes vidéo ou audio, sites web entiers imitant des médias existants. L'opération Doppelgänger/RRN illustre cette catégorie à grande échelle — des centaines de clones de sites médiatiques (Le Monde, Der Spiegel, The Guardian) avec des articles fabriqués qui modifient subtilement le contenu original pour y injecter des narratifs pro-russes.

Le **contenu manipulé** est un contenu réel qui a été modifié : images retouchées, vidéos montées pour modifier le sens, citations tronquées ou sorties de leur contexte, données statistiques présentées avec des échelles trompeuses. Cette catégorie est plus difficile à détecter car elle s'appuie sur un substrat réel — la modification est souvent subtile et nécessite une comparaison avec l'original.

Le **contenu détourné** est un contenu authentique, non modifié, mais placé dans un contexte faux. Une photographie réelle d'un événement ancien présentée comme illustrant un événement récent, un document officiel réel cité dans un contexte qui en altère le sens, une statistique réelle interprétée de manière trompeuse. C'est la forme la plus difficile à qualifier car le contenu lui-même n'est pas faux — c'est l'usage qui est manipulateur.

### 8.2 Deepfakes vidéo : état de l'art 2025-2026

La technologie de deepfake vidéo a franchi plusieurs seuils de qualité depuis 2022. Les modèles actuels produisent des vidéos suffisamment réalistes pour être crédibles en première analyse, particulièrement en basse résolution et dans des conditions de visionnage rapide (format court, écran de smartphone). La démocratisation des outils — Stable Video Diffusion, DeepFaceLab, outils commerciaux comme Synthesia — rend la technologie accessible à des acteurs disposant de moyens modestes.

Dans le domaine des opérations d'influence, l'usage documenté des deepfakes vidéo reste à ce stade relativement limité en nombre mais significatif en impact. Le deepfake de Volodymyr Zelensky appelant les soldats ukrainiens à déposer les armes (mars 2022) a été un moment de cristallisation — techniquement grossier mais démontrant le potentiel de déstabilisation. Storm-1516 utilise des deepfakes vidéo pour crédibiliser de faux témoignages, comme le cas Matthew Metro/Walz décrit au Ch.6.

La recherche de VIGINUM souligne une nuance importante : des contenus manipulés de faible sophistication (*cheapfakes* — montages simples, décontextualisation, légendes trompeuses) peuvent être aussi nuisibles que des deepfakes sophistiqués. Le coût de production d'un cheapfake est quasi nul, sa diffusion est identique, et son impact émotionnel peut être supérieur car il repose sur des images réelles (et donc plus crédibles) décontextualisées.

### 8.3 Deepfakes audio et voice cloning

Le clonage vocal est probablement la menace technique la plus sous-estimée. La qualité des synthèses vocales actuelles est remarquable — quelques secondes d'échantillon audio suffisent pour produire une voix synthétique difficile à distinguer de l'originale. L'usage dans le domaine politique est documenté : Storm-1516 a diffusé en août 2024 un enregistrement audio présenté comme un appel entre Barack Obama et David Axelrod, incluant trois fichiers audio probablement générés artificiellement.

L'analyse spectrale permet de détecter certains artefacts de synthèse vocale, mais les détecteurs automatiques restent incertains — le rapport VIGINUM sur Storm-1516 illustre cette difficulté avec un cas où l'analyse humaine experte a identifié des artefacts spectraux confirmant la synthèse, mais le détecteur automatique donnait un résultat « incertain ».

Le deepfake audio est particulièrement dangereux dans les opérations d'influence car : la vérification est plus difficile qu'en vidéo (pas de repères visuels), la diffusion via des plateformes audio (podcasts, messages vocaux WhatsApp) est difficile à tracer, et l'impact émotionnel d'une « voix réelle » est supérieur à celui d'un texte.

### 8.4 Textes AI-generated : production de masse

L'utilisation de LLM pour la production de masse de contenus textuels est documentée dans plusieurs opérations. Le réseau CopyCop, opéré par John Mark Dougan dans le cadre de Storm-1516, utilise des outils d'IA générative pour reformuler automatiquement des articles et les publier sur un réseau de faux sites d'information. VIGINUM a noté une « montée en compétences des opérateurs » et une amélioration de leurs procédures de sécurité opérationnelle, potentiellement avec l'appui technique du Centre d'expertise géopolitique et du GRU.

L'IA permet trois usages distincts en production textuelle : la **génération** de contenus originaux à partir de consignes (articles, commentaires, posts), la **traduction** idiomatique permettant de cibler des audiences multilingues avec un coût marginal quasi nul, et la **reformulation** permettant de produire des milliers de variantes d'un même message pour contourner la détection de duplications. Le rapport VIGINUM sur l'IA et la menace informationnelle souligne que ces capacités pourraient rendre obsolètes des techniques de détection comme la détection de copy-pasta, en les remplaçant par des reformulations plus complexes à identifier.

### 8.5 Images AI-generated

Les générateurs d'images IA sont utilisés à deux niveaux dans les opérations d'influence : la création de photos de profil pour les faux comptes (usage massif, documenté dans pratiquement toutes les opérations récentes) et la création de fausses scènes ou de faux documents (usage plus ciblé mais en croissance).

La transition des GANs vers les modèles de diffusion (Midjourney, DALL-E, Stable Diffusion) a amélioré la qualité des images générées et réduit les artefacts caractéristiques qui facilitaient la détection. VIGINUM a développé en interne des capacités de détection d'images « probablement artificielles » mais insiste sur le fait que cette détection produit des signaux, pas des certitudes.

### 8.6 Détection : état des lieux et principes

La détection de contenu synthétique en 2025-2026 repose sur un paysage d'outils en évolution rapide mais aux performances variables.

**Détecteurs de texte AI-generated** (GPTZero, Originality.ai, Binocular et al.) ont des performances médiocres sur les textes courts, une forte sensibilité aux paraphrases, des taux de faux positifs significatifs, et ne constituent en aucun cas un verdict autonome. Le rapport VIGINUM souligne que la méthode Binocular, qui mesure la probabilité qu'un texte ait été écrit par un humain, s'appuie elle-même sur des LLM.

**Détecteurs d'images et de vidéo** utilisent des approches variées : analyse de métadonnées, Error Level Analysis (ELA), détection d'artefacts statistiques, classificateurs entraînés. Leur fiabilité varie considérablement selon le modèle générateur et la post-production appliquée au contenu.

**Provenance et watermarking.** Le standard C2PA (*Content Credentials*), porté par Microsoft, Adobe et la BBC, vise à intégrer des métadonnées de provenance vérifiables dans les contenus numériques. Le concept est prometteur mais son adoption reste limitée et il ne résout pas le problème des contenus existants ou produits hors écosystème C2PA. L'AI Act européen prévoit des obligations de marquage des contenus générés par IA, mais la mise en œuvre effective est encore à venir.

**Principe fondamental.** La détection automatique est un signal exploratoire, jamais une preuve. La corroboration multi-méthode est obligatoire : un détecteur automatique produit une hypothèse qui doit être corroborée par l'analyse manuelle, la vérification contextuelle, l'analyse de la chaîne de diffusion et d'autres éléments convergents. Ce principe est un fil conducteur de l'ensemble du cours (voir aussi Ch.15 et le cours OSINT Mastery Ch.14).

---

## Chapitre 9 — Hack-and-leak et manipulation par les fuites

### 9.1 Le modèle hack-and-leak

Le hack-and-leak combine une opération cyber (compromission d'un système d'information, exfiltration de données) et une opération d'influence (publication stratégique des données pour maximiser l'impact informationnel). Il se situe à l'intersection de la cybersécurité et de la guerre informationnelle, ce qui explique qu'il mobilise des compétences hybrides — techniques (forensic, CTI) et analytiques (narrative, géopolitique).

Le modèle opérationnel comprend quatre étapes : la compromission initiale (phishing, exploitation de vulnérabilité, ingénierie sociale), l'exfiltration des données, la préparation de la publication (sélection, mise en scène, injection éventuelle de faux documents), et la diffusion stratégique via des canaux permettant de maximiser l'impact tout en obscurcissant l'origine. La chaîne de dissémination est critique : publier des documents volés sur un forum anonyme n'a pas le même impact que les faire parvenir à un média mainstream.

### 9.2 Cas fondateurs

L'opération **DNC/Podesta 2016** (GRU → DCLeaks → Guccifer 2.0 → WikiLeaks) est le cas de référence. Le GRU (via APT28/Fancy Bear) a compromis le Comité national démocrate et le directeur de campagne de Hillary Clinton, exfiltré des dizaines de milliers d'emails, puis organisé leur publication via des personnages et plateformes écrans (Guccifer 2.0, DCLeaks) et le relais de WikiLeaks. L'analyse détaillée de cette opération est présentée au Ch.23.

Les **Macron Leaks** (mai 2017) ont testé la transposition du modèle en Europe — avec un résultat plus limité, la période de réserve électorale française ayant freiné l'amplification médiatique. Fait notable : des documents falsifiés avaient été mélangés aux documents authentiques — une technique de « poison pill » visant à décrédibiliser l'ensemble du corpus et à rendre sa vérification plus difficile pour les journalistes et les équipes de campagne.

### 9.3 Le timing de publication comme arme

Le choix du moment de publication est un paramètre opérationnel déterminant. Le schéma idéal pour l'attaquant est la publication dans une fenêtre où le temps de vérification est compressé : avant un scrutin, pendant un débat, au moment d'une décision critique. Les Macron Leaks publiées 48 heures avant le second tour, les emails du DNC publiés pendant la convention démocrate — le timing est toujours calculé.

La défense face au timing exploite la même logique inversée : anticiper le risque, préparer les contre-narratifs, réduire le temps de réaction. Le fait que l'équipe Macron avait anticipé et préparé sa communication pré-positionnée explique en partie le moindre impact de l'opération.

### 9.4 Manipulation des documents fuités : le poison pill

La technique du *poison pill* consiste à injecter des documents falsifiés dans un corpus de vrais documents exfiltrés. L'objectif est multiple : ajouter du contenu incriminant fabriqué, rendre la vérification de l'ensemble du corpus plus difficile (chaque document doit être vérifié individuellement), et, paradoxalement, permettre à la cible de contester l'authenticité de l'ensemble en s'appuyant sur les faux documents identifiés.

Pour le praticien, cela implique une analyse forensique systématique de tout corpus fuité : vérification des métadonnées, comparaison avec des documents de référence, analyse de la typographie, des horodatages et des formats de fichier, identification des incohérences internes. Un document fuité n'est ni automatiquement authentique ni automatiquement faux — chaque pièce du corpus doit être évaluée individuellement.

### 9.5 La chaîne de laundering : du fringe au mainstream

Un hack-and-leak ne produit d'effet que si les documents atteignent une audience large. La chaîne de blanchiment informationnel (*narrative laundering*) est le mécanisme par lequel un contenu d'origine clandestine acquiert progressivement une légitimité perçue.

Le processus typique suit une progression par couches. L'**injection initiale** se fait dans un espace peu contrôlé : forum anonyme (4chan, 8kun), canal Telegram, site marginal. Des **relais idéologiques** — influenceurs, blogs d'opinion, médias alternatifs — reprennent le contenu, lui apportant une première couche de crédibilité perçue. Des **influenceurs semi-authentiques** — personnalités publiques qui ne sont pas nécessairement complices mais qui trouvent le contenu utile à leur cause — l'amplifient vers des audiences plus larges. Des **médias alternatifs ou pseudo-médias** le publient sous une forme journalistique. Enfin, des **médias mainstream** couvrent l'histoire — ne serait-ce que pour la contester — ce qui achève de l'inscrire dans le débat public.

La distinction entre reprise opportuniste, reprise sincère mais manipulée, et amplification coordonnée est souvent difficile à établir. Le rapport VIGINUM sur Storm-1516 note que les reprises par les médias et acteurs occidentaux pro-russes sont « majoritairement opportunistes (voire inconscientes et involontaires) » mais qu'il « demeure plausible que certains des acteurs, organisations ou MOI mentionnés soient directement activés par les opérateurs ». Cette ambiguïté est structurelle et doit être documentée dans l'analyse — pas résolue par une attribution prématurée.

Le rôle des **influenceurs semi-authentiques** est particulièrement important et souvent sous-estimé. Un compte militant qui partage un narratif injecté par une opération d'influence n'est pas nécessairement un compte opéré par l'opération — il peut être un acteur sincère qui trouve le narratif utile à sa cause. La frontière entre « relais manipulé » et « acteur autonome convergeant » est analytiquement fondamentale et souvent impossible à trancher sans renseignement complémentaire (voir Ch.16 sur les limites de l'attribution).

### 9.6 Défense

La défense contre le hack-and-leak repose sur trois piliers : la **prévention** (cybersécurité des systèmes d'information, sensibilisation au phishing, segmentation des accès), la **préparation** (identification préalable des contenus les plus sensibles, préparation de réponses calibrées, communication de crise pré-positionnée) et la **réponse** (détection précoce via monitoring du dark web et de Telegram, communication proactive plutôt que « pas de commentaire », coordination avec les plateformes). Le cadre juridique est celui de l'atteinte aux systèmes de traitement automatisé de données (STAD), du vol de données, et potentiellement de l'ingérence étrangère.

---

## Chapitre 10 — Ciblage, micro-targeting et arme des données personnelles

### 10.1 Le ciblage d'audience dans les opérations d'influence

Les opérations d'influence ne visent pas une population dans son ensemble — elles segmentent et ciblent des audiences spécifiques en fonction de leur vulnérabilité à un narratif donné. Le ciblage peut être démographique (tranche d'âge, genre, catégorie socioprofessionnelle), géographique (région, ville, quartier), politique (sympathisants d'un parti, abstentionnistes), émotionnel (personnes anxieuses, en colère, méfiantes) ou communautaire (diaspora, minorité linguistique, communauté religieuse).

L'IRA a démontré en 2016 un ciblage extrêmement granulaire des fractures sociales américaines — des comptes spécifiquement conçus pour cibler les communautés afro-américaines, les communautés hispaniques, les chrétiens évangéliques, les vétérans militaires, chacun avec des narratifs adaptés. Ce n'est pas un ciblage algorithmique sophistiqué mais une segmentation manuelle par des opérateurs ayant une bonne compréhension des dynamiques sociales du pays cible.

### 10.2 L'exploitation des données personnelles

Le modèle Cambridge Analytica — collecte de données personnelles via une application tierce, profilage psychographique, ciblage publicitaire individualisé — a sensibilisé l'opinion au risque d'exploitation des données pour l'influence. Depuis 2018, les plateformes ont restreint l'accès aux données (fermeture de l'API Graph de Facebook, restriction des APIs Twitter/X), mais les data brokers continuent de commercialiser des profils comportementaux à grande échelle. Les fuites de données massives (des milliards de records exposés chaque année) constituent une autre source de données exploitables.

En pratique, les opérations documentées en 2024-2026 s'appuient moins sur des données personnelles individualisées que sur un ciblage communautaire et thématique — exploiter les fractures existantes plutôt que cibler des individus spécifiques. Les publicités ciblées de Facebook/Instagram restent un vecteur (documenté dans Doppelgänger/RRN), mais les contrôles renforcés du DSA et des plateformes elles-mêmes ont réduit ce risque.

### 10.3 Le ciblage des diasporas

Le ciblage des diasporas est un mode opératoire spécifique qui exploite les communautés linguistiques et culturelles vivant hors de leur pays d'origine. Les exemples documentés incluent le ciblage de la diaspora russophone en Baltique par des médias russophones pro-Kremlin (amplifiant les narratifs de discrimination des russophones dans les États baltes), le ciblage de la diaspora chinoise par les opérations de type Spamouflage (visant à maintenir une adhésion au récit officiel de Pékin et à réprimer la dissidence transnationale), et le ciblage de la diaspora turque en Europe par des campagnes pro-Ankara.

Le rapport VIGINUM sur l'IA et la menace informationnelle souligne que l'IA permet des « expérimentations de micro ciblage ayant recours à des présentateurs générés par l'IA, utilisant différents accents et tonalités de couleur de peau pour attirer des audiences locales », une capacité particulièrement préoccupante pour le ciblage des diasporas.

### 10.4 Telegram et les espaces non modérés

Le déplacement progressif des opérations d'influence vers des espaces moins modérés — Telegram en premier lieu, mais aussi Discord, WhatsApp, groupes Facebook privés — représente un défi majeur pour la détection. Telegram fonctionne comme un espace de transit et d'amplification central : les canaux de diffusion permettent de toucher des dizaines de milliers d'abonnés, les groupes permettent la coordination, et les bots facilitent l'automatisation. Le rapport VIGINUM sur Storm-1516 identifie Telegram comme le vecteur de diffusion final vers les audiences russophones, avec des chaînes comme @golosmordora comme primo-diffuseurs systématiques.

---

## Chapitre 11 — Influence et conflits armés : fonctions opérationnelles du champ informationnel

Ce chapitre est recentré sur les fonctions opérationnelles de l'information en contexte de conflit armé, plutôt que sur la description des conflits eux-mêmes (les études de cas sont traitées en Partie V).

### 11.1 Les fonctions opérationnelles de l'information en guerre

En contexte de conflit armé, l'information remplit six fonctions opérationnelles distinctes, souvent poursuivies simultanément.

La **démoralisation** vise à briser la volonté de résistance de l'adversaire et de sa population. Le deepfake de Zelensky appelant à la reddition (2022) est une tentative directe de démoralisation — grossière mais illustrative. La désinformation massive sur les pertes ukrainiennes, amplifiée par les médias d'État russes, vise le même objectif sur le long terme.

Le **brouillage** informationnel consiste à saturer l'espace informationnel de versions contradictoires pour empêcher la formation d'un consensus factuel. La stratégie du « firehose of falsehood » attribuée à la Russie — produire un volume massif de narratifs contradictoires (« l'avion a été abattu par l'Ukraine / par les séparatistes / n'a pas été abattu / a été détourné ») — vise à créer la confusion plutôt qu'à imposer une version unique.

La **légitimation** vise à justifier ses propres actions auprès des audiences domestiques, alliées et neutres. L'effort informationnel russe pour présenter l'invasion de l'Ukraine comme une « opération militaire spéciale » de dénazification relève de cette fonction.

La **désorientation** vise à perturber la compréhension de la situation par l'adversaire — analogue à la déception militaire traditionnelle mais appliquée au domaine informationnel.

La **mobilisation** vise à galvaniser le soutien de sa propre population et de ses alliés. La communication de guerre de Zelensky — vidéos quotidiennes en tenue militaire depuis Kiev dès les premiers jours de l'invasion — est un cas d'école de mobilisation informationnelle réussie.

La **perception internationale** vise à influencer l'opinion des pays tiers et des organisations internationales. L'effort d'influence russe en Afrique (African Initiative, Corps africain) vise explicitement à construire un soutien international pour les positions russes dans les enceintes multilatérales.

### 11.2 L'OSINT citoyenne et le brouillard de guerre informationnel

Le conflit russo-ukrainien a vu l'émergence d'une OSINT citoyenne de masse — des analystes indépendants, des journalistes et des citoyens utilisant l'imagerie satellite, les réseaux sociaux, les données de géolocalisation et les sources ouvertes pour suivre les mouvements de troupes, documenter les atteintes aux droits humains, et vérifier les allégations des parties en conflit. Bellingcat, le Centre for Information Resilience, et de nombreux comptes OSINT individuels ont joué un rôle de fact-checking géopolitique en temps réel.

Les **limites** de cette OSINT citoyenne sont cependant significatives : biais des sources (accès asymétrique aux données selon le camp), risque d'instrumentalisation (un belligérant peut « nourrir » les analystes OSINT avec des informations calibrées), risque de sur-attribution (chaque événement est analysé mais pas nécessairement dans son contexte opérationnel complet), et pression émotionnelle (les analystes OSINT exposés en continu à des images de conflit sont sujets au burnout et à la radicalisation des positions).

### 11.3 Droit international et information en conflit

Le droit international humanitaire (DIH) encadre partiellement l'usage de l'information en conflit armé. Les Conventions de Genève interdisent le fait de perfidement utiliser les emblèmes de la Croix-Rouge ou des Nations unies. Le principe de distinction interdit de cibler les civils, y compris par des opérations psychologiques qui causeraient des terreurs dans la population civile. Cependant, la propagande de guerre n'est pas en tant que telle interdite par le DIH, et les zones grises sont nombreuses.

Le cadre juridique international est insuffisant pour couvrir les formes contemporaines de guerre informationnelle — deepfakes de dirigeants, fausses alertes de capitulation, manipulation des perceptions civiles à grande échelle. C'est un chantier ouvert pour le droit international.

> **🔵 BROUILLARD — Épisode 4**
> Un deepfake audio du candidat X circule sur Telegram, repris par des comptes du réseau identifié. L'enregistrement le fait entendre dans une conversation privée avec un interlocuteur non identifié, tenant des propos contradictoires avec ses positions publiques sur la politique étrangère européenne. Élise doit qualifier : fabrication complète ou montage de vrais extraits ? L'analyse forensique audio est confiée à un expert externe. Les détecteurs automatiques de synthèse vocale donnent des résultats contradictoires — un détecteur identifie des artefacts spectraux compatibles avec une synthèse, un autre classe l'audio comme « probablement authentique ». L'expert humain identifie des transitions anormales entre certains segments du fichier audio, compatibles avec un montage. Conclusion provisoire : « probable synthèse, confiance modérée ». Le résultat des détecteurs automatiques est documenté comme signal exploratoire, pas comme verdict.


---
