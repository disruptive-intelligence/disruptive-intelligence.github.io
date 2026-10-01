---
title: Chapitre 8 — Contenu manipulé et IA générative
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence.md
note: Guerre informationnelle et opérations d'influence
up:
- - Guerre informationnelle et opérations d'influence
  - ../index.md
- - Partie II — Modes opératoires
  - index.md
---

## 8.1 Taxonomie du contenu manipulé

Le contenu manipulé recouvre trois catégories distinctes qui ne posent pas les mêmes problèmes de détection.

Le **contenu fabriqué** est créé de toutes pièces : articles inventés présentés comme des reportages, faux documents officiels, deepfakes vidéo ou audio, sites web entiers imitant des médias existants. L'opération Doppelgänger/RRN illustre cette catégorie à grande échelle — des centaines de clones de sites médiatiques (Le Monde, Der Spiegel, The Guardian) avec des articles fabriqués qui modifient subtilement le contenu original pour y injecter des narratifs pro-russes.

Le **contenu manipulé** est un contenu réel qui a été modifié : images retouchées, vidéos montées pour modifier le sens, citations tronquées ou sorties de leur contexte, données statistiques présentées avec des échelles trompeuses. Cette catégorie est plus difficile à détecter car elle s'appuie sur un substrat réel — la modification est souvent subtile et nécessite une comparaison avec l'original.

Le **contenu détourné** est un contenu authentique, non modifié, mais placé dans un contexte faux. Une photographie réelle d'un événement ancien présentée comme illustrant un événement récent, un document officiel réel cité dans un contexte qui en altère le sens, une statistique réelle interprétée de manière trompeuse. C'est la forme la plus difficile à qualifier car le contenu lui-même n'est pas faux — c'est l'usage qui est manipulateur.

## 8.2 Deepfakes vidéo : état de l'art 2025-2026

La technologie de deepfake vidéo a franchi plusieurs seuils de qualité depuis 2022. Les modèles actuels produisent des vidéos suffisamment réalistes pour être crédibles en première analyse, particulièrement en basse résolution et dans des conditions de visionnage rapide (format court, écran de smartphone). La démocratisation des outils — Stable Video Diffusion, DeepFaceLab, outils commerciaux comme Synthesia — rend la technologie accessible à des acteurs disposant de moyens modestes.

Dans le domaine des opérations d'influence, l'usage documenté des deepfakes vidéo reste à ce stade relativement limité en nombre mais significatif en impact. Le deepfake de Volodymyr Zelensky appelant les soldats ukrainiens à déposer les armes (mars 2022) a été un moment de cristallisation — techniquement grossier mais démontrant le potentiel de déstabilisation. Storm-1516 utilise des deepfakes vidéo pour crédibiliser de faux témoignages, comme le cas Matthew Metro/Walz décrit au Ch.6.

La recherche de VIGINUM souligne une nuance importante : des contenus manipulés de faible sophistication (*cheapfakes* — montages simples, décontextualisation, légendes trompeuses) peuvent être aussi nuisibles que des deepfakes sophistiqués. Le coût de production d'un cheapfake est quasi nul, sa diffusion est identique, et son impact émotionnel peut être supérieur car il repose sur des images réelles (et donc plus crédibles) décontextualisées.

## 8.3 Deepfakes audio et voice cloning

Le clonage vocal est probablement la menace technique la plus sous-estimée. La qualité des synthèses vocales actuelles est remarquable — quelques secondes d'échantillon audio suffisent pour produire une voix synthétique difficile à distinguer de l'originale. L'usage dans le domaine politique est documenté : Storm-1516 a diffusé en août 2024 un enregistrement audio présenté comme un appel entre Barack Obama et David Axelrod, incluant trois fichiers audio probablement générés artificiellement.

L'analyse spectrale permet de détecter certains artefacts de synthèse vocale, mais les détecteurs automatiques restent incertains — le rapport VIGINUM sur Storm-1516 illustre cette difficulté avec un cas où l'analyse humaine experte a identifié des artefacts spectraux confirmant la synthèse, mais le détecteur automatique donnait un résultat « incertain ».

Le deepfake audio est particulièrement dangereux dans les opérations d'influence car : la vérification est plus difficile qu'en vidéo (pas de repères visuels), la diffusion via des plateformes audio (podcasts, messages vocaux WhatsApp) est difficile à tracer, et l'impact émotionnel d'une « voix réelle » est supérieur à celui d'un texte.

## 8.4 Textes AI-generated : production de masse

L'utilisation de LLM pour la production de masse de contenus textuels est documentée dans plusieurs opérations. Le réseau CopyCop, opéré par John Mark Dougan dans le cadre de Storm-1516, utilise des outils d'IA générative pour reformuler automatiquement des articles et les publier sur un réseau de faux sites d'information. VIGINUM a noté une « montée en compétences des opérateurs » et une amélioration de leurs procédures de sécurité opérationnelle, potentiellement avec l'appui technique du Centre d'expertise géopolitique et du GRU.

L'IA permet trois usages distincts en production textuelle : la **génération** de contenus originaux à partir de consignes (articles, commentaires, posts), la **traduction** idiomatique permettant de cibler des audiences multilingues avec un coût marginal quasi nul, et la **reformulation** permettant de produire des milliers de variantes d'un même message pour contourner la détection de duplications. Le rapport VIGINUM sur l'IA et la menace informationnelle souligne que ces capacités pourraient rendre obsolètes des techniques de détection comme la détection de copy-pasta, en les remplaçant par des reformulations plus complexes à identifier.

## 8.5 Images AI-generated

Les générateurs d'images IA sont utilisés à deux niveaux dans les opérations d'influence : la création de photos de profil pour les faux comptes (usage massif, documenté dans pratiquement toutes les opérations récentes) et la création de fausses scènes ou de faux documents (usage plus ciblé mais en croissance).

La transition des GANs vers les modèles de diffusion (Midjourney, DALL-E, Stable Diffusion) a amélioré la qualité des images générées et réduit les artefacts caractéristiques qui facilitaient la détection. VIGINUM a développé en interne des capacités de détection d'images « probablement artificielles » mais insiste sur le fait que cette détection produit des signaux, pas des certitudes.

## 8.6 Détection : état des lieux et principes

La détection de contenu synthétique en 2025-2026 repose sur un paysage d'outils en évolution rapide mais aux performances variables.

**Détecteurs de texte AI-generated** (GPTZero, Originality.ai, Binocular et al.) ont des performances médiocres sur les textes courts, une forte sensibilité aux paraphrases, des taux de faux positifs significatifs, et ne constituent en aucun cas un verdict autonome. Le rapport VIGINUM souligne que la méthode Binocular, qui mesure la probabilité qu'un texte ait été écrit par un humain, s'appuie elle-même sur des LLM.

**Détecteurs d'images et de vidéo** utilisent des approches variées : analyse de métadonnées, Error Level Analysis (ELA), détection d'artefacts statistiques, classificateurs entraînés. Leur fiabilité varie considérablement selon le modèle générateur et la post-production appliquée au contenu.

**Provenance et watermarking.** Le standard C2PA (*Content Credentials*), porté par Microsoft, Adobe et la BBC, vise à intégrer des métadonnées de provenance vérifiables dans les contenus numériques. Le concept est prometteur mais son adoption reste limitée et il ne résout pas le problème des contenus existants ou produits hors écosystème C2PA. L'AI Act européen prévoit des obligations de marquage des contenus générés par IA, mais la mise en œuvre effective est encore à venir.

**Principe fondamental.** La détection automatique est un signal exploratoire, jamais une preuve. La corroboration multi-méthode est obligatoire : un détecteur automatique produit une hypothèse qui doit être corroborée par l'analyse manuelle, la vérification contextuelle, l'analyse de la chaîne de diffusion et d'autres éléments convergents. Ce principe est un fil conducteur de l'ensemble du cours (voir aussi Ch.15 et le cours OSINT Mastery Ch.14).

---
