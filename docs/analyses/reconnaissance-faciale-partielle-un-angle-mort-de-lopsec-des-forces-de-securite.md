---
title: "Analyse — Reconnaissance faciale partielle : un angle mort de l’OPSEC des forces de sécurité"
date: 2026-10-10
kind: analysis
document_type: essai
theme: cyber
slug: reconnaissance-faciale-partielle-un-angle-mort-de-lopsec-des-forces-de-securite
author: "Central OSINT Agency (LinkedIn)"
tags:
  - reconnaissance faciale
  - OSINT
  - OPSEC
  - biométrie
  - forces spéciales
  - vie privée
source_file: inbox/Cyber_LinkedIn_CentralOSINTAgency_Reconnaissance_Faciale_Partielle.txt
source_url: https://www.linkedin.com/feed/update/urn:li:share:7512131051511709696/
---

# Analyse — Reconnaissance faciale partielle : un angle mort de l’OPSEC des forces de sécurité

## Métadonnées

- **Documents :** deux publications LinkedIn d’un même compte, la seconde renvoyant explicitement à la première : un post du **3 octobre 2026** sur un visage partiellement couvert par un tour de cou, et un post du **13 avril 2023** qui prolonge une présentation faite au Forum international de la cybersécurité (FIC) 2023.
- **Auteur :** compte LinkedIn « centralosintagency », d’après les adresses transmises par l’utilisateur. Le texte ne donne ni le nom de la personne ni sa fonction ; l’auteur s’y présente comme praticien de l’OSINT et cite une collaboration avec Alexis Martins pour l’enquête de 2026.
- **Dates :** déduites des identifiants des publications, le contenu étant inaccessible sans compte LinkedIn.
- **Support :** billets d’opinion et de démonstration, sans méthode publiée ; les images jointes (visages floutés, comparaisons) n’ont pas pu être consultées. Source conservée dans `inbox/Cyber_LinkedIn_CentralOSINTAgency_Reconnaissance_Faciale_Partielle.txt`.
- **Périmètre :** identification de membres des forces spéciales, de la police et de la gendarmerie à partir de visages partiellement masqués (cagoule, tour de cou, profil), et réflexes d’OPSEC qui en découlent.
- **Méthode de la fiche :** jusqu’aux « Cinq éléments essentiels », seule la lecture des deux posts fonde les constats ; la dernière section les confronte à des sources extérieures citées et datées.

## Repères pour comprendre le document

Les deux posts reposent sur une idée simple : un visage n’a pas besoin d’être entier pour être reconnu. L’auteur ne parle pas de vidéosurveillance d’État, mais d’**outils commerciaux** accessibles à des particuliers, combinés par un analyste expérimenté, et appliqués à des images publiées par la presse ou par les services de communication des institutions elles-mêmes. Pour le lire, il faut séparer deux opérations que le texte enchaîne : la **suggestion** (un logiciel propose des visages ressemblants) et la **confirmation** (un humain vérifie, avec d’autres indices, qu’il s’agit bien de la même personne). La force de la démonstration dépend surtout de la seconde, que le texte affirme sans la détailler.

- **Reconnaissance faciale partielle (RFP)** — Expression employée par l’auteur pour désigner l’identification d’une personne à partir d’une partie seulement de son visage (yeux, front, profil). Le terme n’est pas une catégorie technique normalisée.
- **Région périoculaire** — Zone autour des yeux : sourcils, paupières, coins des yeux, haut des pommettes. C’est la partie que laissent visible une cagoule ou un tour de cou, et un champ de recherche biométrique à part entière (explication ajoutée).
- **Comparaison 1:1 et recherche 1:N** — La première vérifie si deux images montrent la même personne ; la seconde cherche dans une base les visages les plus proches d’une image. Les moteurs de recherche de visages font de la recherche 1:N (explication ajoutée).
- **Faux positif et faux négatif** — Un faux positif associe à tort deux personnes différentes ; un faux négatif manque une correspondance réelle. Avec un visage masqué, le risque principal change selon l’usage (explication ajoutée).
- **Moteur de recherche de visages** — Service en ligne qui retrouve sur le web ou sur des réseaux sociaux des photos d’une personne à partir d’un visage soumis ; le texte vise ces outils sans les nommer.
- **Correspondance positive (*positive match*)** — Formule de l’auteur pour un rapprochement jugé certain entre une partie de visage et un visage entier non masqué.
- **Pivot masque-visage** — Pour l’auteur, la capacité des outils à relier un visage masqué à une photo à visage découvert, et inversement, ce qui permet de suivre une personne d’une mission à sa vie publique.
- **Corroboration contextuelle** — Confirmation par des indices extérieurs au visage : cicatrices, disposition de l’équipement, arme, viseur. L’auteur s’en sert pour confirmer l’identité de l’opérateur du RAID.
- **OPSEC (sécurité des opérations)** — Discipline qui consiste à repérer les informations qu’un adversaire peut collecter et à les protéger ; l’auteur demande d’y intégrer la RFP.
- **Tour de cou (TDC)** — Tissu tubulaire couvrant le cou et le bas du visage, porté par les forces armées et de sécurité ; selon l’auteur, il donne un faux sentiment d’anonymat.
- **Unités à anonymat protégé** — Services dont la loi interdit de révéler l’identité des membres (forces spéciales, renseignement, unités d’intervention) ; le texte n’en parle pas, mais c’est le cadre qui donne sa portée au sujet (explication ajoutée).

## Résumé exécutif

Dans un post du 3 octobre 2026, le compte « centralosintagency » rappelle une alerte qu’il avait lancée en 2023 : les membres des forces spéciales et des unités d’intervention, même cagoulés, peuvent être identifiés par **reconnaissance faciale partielle**. Il s’appuie cette fois sur une vidéo où une militaire du 54e régiment de transmissions apparaît avec un tour de cou qui ne cache que le bas du visage. Avec un collaborateur, l’auteur dit avoir retrouvé son visage entier sans grande difficulté, et le publie flouté. Il en conclut que le tour de cou ne protège pas l’identité, que des lunettes de soleil compliqueraient fortement l’identification par les outils grand public, et que la RFP devrait entrer dans les réflexes OPSEC des institutions.

Le post de 2023 donne l’arrière-plan. Après une présentation au FIC, l’auteur affirme avoir démontré que la reconnaissance faciale fonctionne sans photo de face, sans visage entier et sans image de haute qualité : il cite l’identification d’un gendarme photographié de profil au Niger, d’un militaire russe assis sur un char à une trentaine de mètres, et d’un opérateur du RAID retrouvé, cagoulé, sur deux opérations différentes (l’affaire Merah en 2012, l’Hyper Cacher en 2015). Il insiste sur la confirmation par des indices non faciaux (marques sur la peau, gilet, arme, viseur) et refuse de publier ses méthodes et ses outils.

La thèse est crédible dans son principe : les données publiques confirment que les algorithmes se sont adaptés aux visages masqués depuis 2020, et que des outils de recherche de visages accessibles au public ont déjà servi à identifier soldats, policiers et manifestants. Sa limite est probatoire : les posts ne donnent ni outils, ni taux de réussite, ni nombre d’échecs, ni démarche de confirmation reproductible. Leur valeur pour la veille tient surtout à l’angle choisi, **la communication des institutions elles-mêmes comme source d’exposition**, et à l’appel à une protection pensée dès la prise de vue.

## Chronologie

L’alerte de l’auteur s’inscrit dans une séquence où les outils, les usages et le droit ont évolué en parallèle.

- **Mars 2012 et janvier 2015** — Interventions du RAID dans l’affaire Merah à Toulouse, puis à l’Hyper Cacher de Porte de Vincennes ; l’auteur dit avoir rapproché un même opérateur cagoulé sur les deux (post de 2023).
- **2016** — Le Code pénal crée une infraction spécifique de révélation de l’identité des membres des forces spéciales et des unités antiterroristes (article 413-14).
- **2019-2022** — Des moteurs de recherche de visages (FindClone, PimEyes) servent à identifier des policiers russes, des manifestants et, après février 2022, des soldats russes en Ukraine.
- **Juillet et novembre 2020** — Le NIST mesure l’effet des masques sur 89 puis 152 algorithmes de reconnaissance faciale.
- **Octobre 2022** — La CNIL inflige 20 millions d’euros d’amende à Clearview AI.
- **Avril 2023** — Présentation de l’auteur au FIC de Lille, puis post du 13 avril.
- **Janvier 2025** — L’armée israélienne impose de masquer visage et nom de ses militaires dans les médias.
- **2 février 2025** — Entrée en application des interdictions du règlement européen sur l’IA, dont la constitution de bases faciales par moissonnage non ciblé.
- **Septembre 2025** — L’Armée de Terre simule le piratage de ses comptes de recrutement dans un jeu de piste dont le lot est une visite du 54e régiment de transmissions.
- **3 octobre 2026** — Post de l’auteur sur la militaire au tour de cou.

## Thèse principale

L’auteur défend une thèse d’alerte : couvrir le bas du visage ne suffit plus à protéger l’identité des personnels exposés, parce que des outils commerciaux, maniés par un analyste compétent, savent relier une partie de visage à une photo complète publiée ailleurs. Le danger n’est donc pas seulement technologique ; il tient au **décalage entre la croyance des opérateurs**, convaincus d’être protégés par leur cagoule ou leur tour de cou, et la réalité des capacités d’identification.

Le texte est un plaidoyer appuyé sur des démonstrations, pas une étude. Il appelle à intégrer la RFP dans l’OPSEC dès la captation et la diffusion des images, et à ajouter des lunettes de soleil au tour de cou, tout en soulignant que la qualité du résultat dépend d’abord de l’expertise de l’analyste.

## Informations et arguments importants

### Ce que l’auteur dit avoir démontré

Les deux posts présentent une série de cas, tous décrits sans les images ni les outils qui permettraient de les vérifier. Ils couvrent des situations de difficulté croissante, de la vue de profil au visage presque entièrement couvert.

1. **Le gendarme au Niger** (2023) : photographié de profil, donc avec une moitié de visage visible, il aurait fait l’objet d’une identification positive.
2. **Le militaire russe sur un char** (2023) : identifié à une trentaine de mètres, ce qui contredit selon l’auteur l’idée qu’il faut être proche du sujet.
3. **L’opérateur du RAID** (2023) : photographié cagoulé lors de deux opérations distinctes, il serait reconnaissable de l’une à l’autre ; la confirmation s’appuie sur des marques visibles du visage, la disposition de son gilet, son arme et son viseur.
4. **La militaire du 54e RT** (2026) : apparaissant à 6 min 12 s d’une vidéo, présentée par son grade et son prénom, le bas du visage couvert par un tour de cou, elle aurait été rattachée à son visage entier « sans grandes difficultés ».

L’auteur en tire une conclusion générale : les croyances selon lesquelles la reconnaissance exige une photo de face, un visage entier, une bonne résolution et une faible distance sont « toutes fausses ».

### Le pivot entre visage masqué et visage découvert

L’argument technique central est la capacité des outils à **pivoter** d’un visage masqué vers un visage découvert, et inversement. Un opérateur photographié en mission par la presse ou par son service de communication peut ainsi être relié à des photos de sa vie privée ou de démonstrations publiques. L’auteur ajoute un élément que l’on oublie souvent : les outils qu’il emploie sont payants mais accessibles à des civils, et donc « bas de gamme » au regard des capacités étatiques ; il s’interroge sur ce dont disposent les grands services de renseignement.

### L’analyste plus que l’outil

Le post de 2026 insiste sur une idée souvent absente des débats : la RFP n’est pas une opération automatique. Elle suppose une combinaison d’outils, des ajustements, des comparaisons et une confirmation, et dépend de l’expertise de l’analyste en morphologie des visages. L’auteur en fait le facteur principal, avant la qualité et l’angle des images. Il garde volontairement ses méthodes secrètes pour ne pas faciliter le travail d’éventuels adversaires.

### Les parades proposées

Les réponses suggérées restent générales. L’auteur recommande de penser la protection **dès la captation et la diffusion** des images, en se demandant quels visages restent reconnaissables et quelles informations les accompagnent. Il propose un ajout simple au tour de cou, les lunettes de soleil, qui rendraient selon lui l’identification beaucoup plus difficile, voire impossible, pour les outils commerciaux. En 2023, il posait aussi la question d’une interdiction faite à la presse de photographier ou filmer les opérateurs spéciaux, même cagoulés, sans y répondre.

## Points particulièrement intéressants pour la veille

- **L’exposition par la communication institutionnelle.** L’auteur souligne que les images exploitées viennent de la presse, mais aussi des services de communication des forces elles-mêmes ; le cas de 2026 provient d’une vidéo mettant en scène une militaire. *Inférence pour la veille :* les campagnes de recrutement et de valorisation, qui multiplient les visages identifiables, deviennent un sujet de sécurité à part entière.
- **La banalisation des outils.** Les moyens décrits sont accessibles à des particuliers pour quelques dizaines d’euros par mois. *Inférence pour la veille :* la menace ne se limite pas aux services étatiques ; elle inclut activistes, groupes criminels et militants capables de cibler des personnels.
- **Le facteur humain de l’identification.** L’auteur fait de l’expertise de l’analyste la variable décisive. *Inférence pour la veille :* la montée en compétence en comparaison faciale (OSINT, criminalistique) compte autant que l’évolution des logiciels, dans un sens comme dans l’autre.
- **La corroboration par l’équipement.** Gilet, arme et viseur servent à confirmer l’identité de l’opérateur du RAID. *Inférence pour la veille :* masquer le visage ne protège pas si l’équipement personnalisé reste visible d’une image à l’autre.
- **Une question de doctrine encore ouverte.** L’auteur demande une place pour la RFP dans les réflexes OPSEC. *Inférence pour la veille :* surveiller les éventuelles consignes des ministères des Armées et de l’Intérieur sur la prise de vue et le floutage.

## Faits, opinions et interprétations

### Faits rapportés par la source

Les faits avancés par l’auteur sont des **résultats d’identification qu’il déclare avoir obtenus** : un gendarme de profil au Niger, un militaire russe à une trentaine de mètres, un opérateur du RAID retrouvé sur deux opérations, et une militaire du 54e RT retrouvée à partir d’un visage couvert par un tour de cou. Le texte ajoute un élément vérifiable en principe, la présence de cette militaire à 6 min 12 s d’une vidéo, et une collaboration avec Alexis Martins pour l’enquête de 2026. Aucun de ces résultats n’est accompagné d’images consultables, de noms d’outils ou de taux de réussite ; ils restent invérifiables à partir des posts seuls.

### Opinions ou positions de l’auteur

L’auteur juge que la sensibilisation des opérateurs est insuffisante et que leur confiance dans le tour de cou est mal fondée. Il estime que les lunettes de soleil compliqueraient fortement l’identification, que l’expertise de l’analyste compte plus que l’outil, et que la RFP doit entrer dans la doctrine OPSEC. Son choix de ne pas publier ses méthodes relève d’une position éthique assumée : protéger les opérateurs plutôt que prouver.

### Interprétations et inférences

L’auteur interprète la facilité de ses identifications comme un indice des capacités supérieures des grands services de renseignement ; c’est une extrapolation plausible, mais non démontrée. *Inférence de la présente analyse :* le texte mélange deux risques distincts. Le premier est l’identification d’un inconnu masqué par recherche dans une base (1:N), qui dépend de l’existence de photos découvertes de la personne en ligne. Le second est le rapprochement de deux images masquées d’une même personne, comme pour l’opérateur du RAID, qui ne donne pas son identité civile mais permet de suivre son parcours. Ces deux risques n’appellent pas les mêmes parades.

## Limites et points à vérifier

1. **Une démonstration sans protocole.** Ni les outils, ni les réglages, ni les étapes de confirmation ne sont décrits ; le choix de ne pas les publier est défendable, mais il empêche toute vérification et toute mesure de la fiabilité.
2. **Aucun taux d’échec.** Les posts présentent des réussites ; ils ne disent pas combien de tentatives ont échoué ni combien de candidats erronés les outils ont proposés avant la bonne correspondance. Sans ce dénominateur, la généralisation « toutes ces croyances sont fausses » n’est pas établie.
3. **Le risque de faux positif est absent du texte.** Rapprocher deux visages masqués augmente fortement le risque d’associer deux personnes différentes ; la confirmation par l’équipement compense en partie ce risque, mais un gilet ou une arme réglementaires peuvent être identiques au sein d’une même unité.
4. **Des cas difficiles à dater et à situer.** Le gendarme au Niger, le militaire russe et la vidéo de 2026 ne sont ni datés ni sourcés ; la vidéo citée n’est désignée que par un lien raccourci.
5. **Une conclusion sur les lunettes de soleil non étayée.** L’affirmation que des lunettes rendraient l’identification impossible pour les outils commerciaux n’est appuyée par aucun test ; elle laisse aussi de côté les indices non faciaux que l’auteur utilise lui-même.
6. **Un cadre juridique ignoré.** Le texte ne mentionne ni les règles qui protègent l’anonymat de certaines unités, ni la licéité des outils de recherche faciale en Europe, alors que ces deux points conditionnent à la fois le risque et la pratique de l’OSINT.
7. **Une attribution incomplète.** L’auteur n’est identifié que par le nom de son compte ; son expertise ne peut être appréciée qu’à travers ses propres affirmations.

## Sources et références mentionnées

Les références sont minces et internes à la démarche de l’auteur : sa présentation au FIC 2023 et son post de 2023, une vidéo d’un créateur désigné comme « Romain P. » sur un prétendu piratage des réseaux du ministère de la Défense, et la collaboration d’Alexis Martins. Les opérations citées (Merah, Hyper Cacher, Niger) sont connues du public, mais aucun document technique, aucune étude et aucun outil ne sont cités. Les posts relèvent du témoignage de praticien.

## Cinq éléments essentiels à retenir

1. L’auteur affirme qu’un **visage partiellement couvert** (cagoule, tour de cou, profil) peut être relié à une photo à visage découvert avec des outils commerciaux accessibles au public.
2. Il cite quatre cas, dont un **opérateur du RAID** retrouvé cagoulé sur deux opérations et une **militaire du 54e RT** filmée avec un tour de cou.
3. Il fait de l’**expertise de l’analyste** et de la **confirmation par des indices non faciaux** (équipement, arme, marques) la clé de l’identification.
4. Il recommande d’intégrer la RFP dans l’**OPSEC dès la prise de vue** et d’ajouter des **lunettes de soleil** au tour de cou.
5. Ses démonstrations ne sont **pas vérifiables** : ni outils, ni images, ni taux d’échec ne sont publiés.

## État de l’art et regards extérieurs

Recherches effectuées le 2026-10-10. Ces constats complètent les sections précédentes sans les modifier ; les posts LinkedIn et la vidéo citée n’ont pas pu être consultés directement, LinkedIn exigeant un compte.

### Travaux de référence

- **NIST, [*FRVT Part 6A*](https://www.nist.gov/news-events/news/2020/07/nist-launches-studies-masks-effect-face-recognition-software) (NISTIR 8311, 27 juillet 2020) et [*Part 6B*](https://www.nist.gov/news-events/news/2020/12/face-recognition-software-shows-improvement-recognizing-masked-faces) (NISTIR 8331, 1er décembre 2020).** Avant la pandémie, même les meilleurs des 89 algorithmes testés passaient d’environ 0,3 % d’erreur sur visage nu à environ 5 % sur visage masqué, et beaucoup échouaient dans 20 à 50 % des cas. Quatre mois plus tard, les algorithmes adaptés avaient réduit leurs erreurs jusqu’à un facteur dix, les meilleurs se trompant dans 2,4 à 5 % des cas. Ces tests portent sur des masques numériques et sur la comparaison 1:1, pas sur la recherche dans une base ; ils confirment néanmoins le diagnostic de l’auteur sur l’adaptation rapide des outils.
- **Alonso-Fernandez et Bigun, [« A Survey on Periocular Biometrics Research »](https://arxiv.org/abs/1810.03360), *Pattern Recognition Letters* (2015-2016).** La région périoculaire, celle que laisse visible un tour de cou, est étudiée comme modalité biométrique à part entière, précisément parce qu’elle reste exploitable à distance ou quand le reste du visage est caché. Les mêmes auteurs ont actualisé cette synthèse en intégrant les visages masqués ([arXiv:2212.13792](https://arxiv.org/abs/2212.13792), 2022).
- **Phillips et al., [« Face recognition accuracy of forensic examiners, superrecognizers, and face recognition algorithms »](https://www.nist.gov/news-events/news/2018/05/nist-study-shows-face-recognition-experts-perform-better-ai-partner), *PNAS*, mai 2018.** Les examinateurs spécialisés et les « super-reconnaisseurs » font mieux que des non-spécialistes, et le meilleur résultat vient d’un examinateur associé au meilleur algorithme. C’est l’appui scientifique le plus net de l’idée de l’auteur selon laquelle l’expertise de l’analyste, combinée aux outils, fait la différence.

### Compléments sur le sujet

Les posts restent centrés sur la démonstration technique. Quatre dimensions éclairent pourtant leur portée : l’usage réel de ces outils dans les conflits et contre les forces de l’ordre, la réponse d’autres armées, le droit français de l’anonymat des unités, et le statut juridique des moteurs de recherche de visages en Europe.

**Des outils déjà employés contre des militaires et des policiers.** AlgorithmWatch a documenté en août 2022 la banalisation de services comme FindClone, PimEyes ou Search4faces, pour quelques dollars par mois ([« Face recognition for everyone »](https://algorithmwatch.org/en/face-recognition-for-everyone/), 3 août 2022). Des militants russes ont identifié en 2019 des policiers antiémeute avec FindClone ; des chercheurs en sources ouvertes l’ont utilisé pour identifier des soldats russes morts ou capturés, et un média d’investigation pour retrouver un soldat lié aux exécutions de Boutcha. Le même article montre le revers de la médaille : un journaliste néerlandais a désigné à tort une femme à partir d’une vidéo, et un forum russe a utilisé ces outils pour harceler des particuliers. L’Ukraine a confirmé en mars 2022 utiliser Clearview AI pour identifier des soldats russes tués et prévenir leurs familles ([CBC/Reuters, mars 2022](https://amp.cbc.ca/news/world/ukraine-clearview-ai-russian-soldiers-identify-war-1.6395446)), et une société française de formation a revendiqué l’identification d’un commandant tchétchène à partir d’une vidéo ([Futura, mars 2022](https://www.futura-sciences.com/alternative/amp/actualite/97283)). Ces cas confirment que le risque décrit par l’auteur est réel et déjà exploité, des deux côtés d’un conflit.

**L’armée israélienne a fait de la protection des visages une règle.** En janvier 2025, après des plaintes déposées à l’étranger par la Hind Rajab Foundation, qui croisait les visages de soldats vus à Gaza avec leurs profils sur les réseaux sociaux, l’armée israélienne a imposé de ne plus montrer le visage ni le nom de ses militaires dans les médias, de ne publier que des photos prises de dos ou floutées, et de soumettre à autorisation les images de zones de combat ([CNN via KVIA, 8 janvier 2025](https://kvia.com/news/us-world/cnn-world/2025/01/08/israel-to-conceal-soldiers-identities-after-brazilian-probe-into-war-crimes-allegations/) ; [Ynet](https://ynetnews.com/article/hkb5xv2uyl)). Les seuils de grade varient selon les comptes rendus, et la mesure n’est pas rétroactive. C’est l’exemple le plus abouti de la réponse que l’auteur appelle de ses vœux : une politique de prise de vue, pas seulement de port de cagoule.

**Le droit français protège l’identité, pas le visage masqué en tant que tel.** L’article 39 *sexies* de la loi du 29 juillet 1881 punit de 15 000 euros la révélation de l’identité des membres de services désignés par arrêté, et l’article 413-14 du Code pénal, créé en 2016, punit de cinq ans d’emprisonnement et 75 000 euros la révélation de toute information pouvant conduire, directement ou indirectement, à l’identification d’un membre des forces spéciales ou des unités spécialisées antiterroristes désignées par arrêté ([amendement gouvernemental CL107, Assemblée nationale, 2016](https://www.assemblee-nationale.fr/14/amendements/1278/CION_LOIS/CL107.pdf)). Les arrêtés du 7 avril 2011 et du 20 octobre 2016 listent les unités concernées du ministère des Armées. La chambre criminelle de la Cour de cassation a jugé le 12 décembre 2017 (pourvoi n° 17-80821) que l’interdiction couvre toute information permettant l’identification, pas seulement le nom : l’affaire portait sur des photographies d’un policier du Groupe de sécurité de la présidence de la République publiées avec quelques indications sur son poste ([veille juridique de l’IRSEM, février 2018](https://www.irsem.fr/storage/file_manager_files/2025/03/veille-juridique-fevrier-2018.pdf)). *Inférence de l’analyse :* un rapprochement par RFP publié sans floutage pourrait tomber sous ces textes ; le floutage pratiqué par l’auteur et son refus de publier ses méthodes sont donc aussi une précaution juridique. Ces règles ne s’appliquent toutefois pas à tous les personnels : un régiment qui ne figure pas dans les arrêtés n’est couvert que par le droit commun, notamment l’article 223-1-1 du Code pénal, créé en 2021, qui réprime la diffusion d’informations permettant d’identifier ou de localiser une personne pour l’exposer à un danger.

**Les moteurs de recherche de visages sont largement illicites en Europe, mais restent accessibles.** La CNIL a infligé 20 millions d’euros d’amende à Clearview AI en octobre 2022 et lui a ordonné de supprimer les données des personnes situées en France, sans obtenir le paiement à mi-2023 ([Siècle Digital, 21 octobre 2022](https://siecledigital.fr/2022/10/21/reconnaissance-faciale-la-cnil-sanctionne-clearview-ai-dune-amende/) ; [11 mai 2023](https://siecledigital.fr/2023/05/11/clearview-ai-recolte-une-nouvelle-amende-pour-ne-pas-avoir-respecte-une-decision-de-la-cnil/)). L’autorité néerlandaise a suivi avec 30,5 millions d’euros en septembre 2024 ([Jurist, septembre 2024](https://www.jurist.org/news/2024/09/netherlands-data-protection-authority-fines-us-ai-company-30-5-million-euros-over-facial-recognition-database)). Ces sanctions n’ont pas fait disparaître l’offre : Privacy International a relevé en juillet 2024 plus de 2 300 accès à PimEyes depuis les ordinateurs de la police de Londres en trois mois ([Freevacy, juillet 2024](https://www.freevacy.com/news/privacy-international/pi-sends-open-letter-to-ico-and-mps-commissioner-of-pimeyes-use/5544)). *Inférence de l’analyse :* l’illicéité européenne ne réduit pas la menace venant d’acteurs hors de l’Union, et elle place les praticiens européens de l’OSINT dans une zone juridique délicate.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
|---|---|---|
| La reconnaissance faciale ne fonctionne pas qu’avec des visages entiers | **Confirmé** | NIST, NISTIR 8311 et 8331 (2020) ; littérature périoculaire |
| Des outils accessibles aux civils permettent d’identifier des militaires | **Confirmé** | AlgorithmWatch (2022) : FindClone, PimEyes ; usage contre soldats et policiers |
| Il est possible de relier un visage masqué à un visage découvert | **Confirmé** dans le principe | NIST 8331 : algorithmes adaptés aux masques, erreurs de 2,4 à 5 % pour les meilleurs en 1:1 |
| Les résultats sont fiables une fois confirmés par l’analyste | **Non établi** | Aucun protocole ni taux d’échec publiés ; NIST note des faux positifs 10 à 100 fois plus fréquents quand les deux images sont masquées |
| L’expertise de l’analyste est décisive | **Confirmé** | Phillips et al., *PNAS* (2018) : examinateur + algorithme > examinateurs seuls |
| Des lunettes de soleil rendent l’identification très difficile, voire impossible | **Nuancé** | Noyes et al. (2021) : lunettes et masques dégradent autant la reconnaissance humaine, mais les super-reconnaisseurs restent meilleurs ; aucune mesure publiée sur masque + lunettes avec outils commerciaux |
| La vidéo citée montre un « hacker qui contrôlait les réseaux » du ministère | **Nuancé** | Le seul épisode public correspondant est un faux piratage, jeu de piste de recrutement de l’Armée de Terre (septembre 2025) récompensé par une visite du 54e RT ([Futura, 30 septembre 2025](https://www.futura-sciences.com/tech/actualites/guerre-futur-armee-terre-t-elle-ete-piratee-ce-week-end-etait-ce-piege-ce-revele-cette-drole-manoeuvre-126021/)) ; rapprochement non confirmé |

### Contrepoints et critiques

- **Le risque d’erreur d’identification.** AlgorithmWatch rapporte qu’un développeur de Bosch jugeait « complètement impossible » une identification concluante quand la bouche, la mâchoire et les oreilles sont cachées sur une image en basse résolution, et cite des erreurs publiques de journalistes. Cette réserve ne contredit pas l’auteur, qui insiste sur la confirmation, mais elle rappelle qu’une démonstration sans taux d’erreur peut aussi exposer des innocents.
- **L’efficacité des lunettes de soleil.** L’étude de Noyes, Davis, Petrov, Gray et Ritchie ([*Royal Society Open Science*, 24 mars 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8074904)) montre que les lunettes de soleil dégradent la reconnaissance humaine presque autant qu’un masque, ce qui va dans le sens de l’auteur. Mais elle porte sur des observateurs humains, pas sur des logiciels, et l’auteur reconnaît lui-même que l’équipement, l’arme ou les cicatrices suffisent parfois ; la parade qu’il propose est donc utile mais partielle.
- **La tension avec la liberté de la presse.** La question d’une interdiction de photographier les opérateurs, posée en 2023, heurte la liberté d’informer ; l’article 413-14 a déjà servi de fondement à la convocation de journalistes par la DGSI ([Next, 2018](https://next.ink/6851/107909-convocation-journalistes-par-dgsi-aux-origines-larticle-413-14-code-penal/)). L’exemple israélien montre qu’une politique de floutage à la source, décidée par l’institution, est une alternative à l’interdiction.

### Évolutions depuis la publication

Le post de 2023 a été suivi d’évolutions qui confirment sa pertinence. Le NIST a cessé en février 2024 d’évaluer séparément les algorithmes 1:1 sur visages masqués ([NIST FRTE Face Mask Effects](https://pages.nist.gov/frvt/html/frvt_facemask.html)) ; aucune évaluation publique récente ne mesure donc les progrès réalisés depuis sur les visages couverts. Le règlement européen sur l’IA interdit depuis le 2 février 2025 la constitution ou l’extension de bases de reconnaissance faciale par moissonnage non ciblé d’images sur internet ou de vidéosurveillance (article 5, paragraphe 1, point e). L’armée israélienne a adopté sa politique de dissimulation des visages en janvier 2025. En septembre 2025, l’Armée de Terre a lancé une campagne de recrutement cyber fondée sur un faux piratage de ses comptes ; si c’est bien la vidéo citée par l’auteur, l’exposition qu’il dénonce provient d’une opération de communication de l’institution.

### Cadre juridique et éthique

- **France, loi du 29 juillet 1881, article 39 *sexies*.** Amende de 15 000 euros pour la révélation de l’identité des personnels de services désignés par arrêté (arrêté du 7 avril 2011 modifié pour le ministère des Armées).
- **France, Code pénal, article 413-14.** Cinq ans d’emprisonnement et 75 000 euros pour toute révélation d’informations pouvant conduire à l’identification d’un membre des forces spéciales ou des unités antiterroristes désignées (arrêté du 20 octobre 2016 pour les forces spéciales).
- **France, Code pénal, article 223-1-1.** Réprime depuis 2021 la diffusion d’informations permettant d’identifier ou de localiser une personne afin de l’exposer à un risque, avec une peine aggravée pour les dépositaires de l’autorité publique.
- **Union européenne, RGPD, article 9.** Les données biométriques traitées pour identifier une personne sont des données sensibles ; c’est le fondement des sanctions contre Clearview AI.
- **Union européenne, règlement sur l’IA, article 5.** Interdit depuis février 2025 les systèmes qui constituent des bases faciales par moissonnage non ciblé ; il ne vise pas en tant que tel l’usage ponctuel d’un moteur de recherche par un analyste.

### Pour aller plus loin

- [AlgorithmWatch, « Face recognition for everyone »](https://algorithmwatch.org/en/face-recognition-for-everyone/) — Panorama des outils grand public et de leurs usages, des enquêtes de guerre au harcèlement.
- [Bellingcat, guide SearchFace/FindClone](https://www.bellingcat.com/resources/how-tos/2019/02/19/using-the-new-russian-facial-recognition-site-searchface-ru) — Exemple de méthodologie OSINT publique et de ses précautions de vérification.
- [NIST, FRTE Face Mask Effects](https://pages.nist.gov/frvt/html/frvt_facemask.html) — Résultats de référence sur la reconnaissance des visages masqués.
- [Noyes et al., *Royal Society Open Science* (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8074904) — Effet des masques et des lunettes de soleil sur la reconnaissance humaine, y compris chez les super-reconnaisseurs.
- [CNIL, « Reconnaissance faciale »](https://www.cnil.fr/fr/reconnaissance-faciale) — Positions et décisions de l’autorité française.
