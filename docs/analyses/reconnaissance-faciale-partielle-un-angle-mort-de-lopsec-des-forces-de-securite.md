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
source_file: inbox/renseignement-osint/Cyber_LinkedIn_CentralOSINTAgency_Reconnaissance_Faciale_Partielle.txt
source_url: https://www.linkedin.com/feed/update/urn:li:share:7512131051511709696/
---

# Analyse — Reconnaissance faciale partielle : un angle mort de l’OPSEC des forces de sécurité

## Métadonnées

- **Point de départ :** deux publications LinkedIn du compte « centralosintagency » (3 octobre 2026 et 13 avril 2023), où un praticien de l’OSINT affirme pouvoir identifier des militaires et des policiers au visage partiellement couvert ; l’auteur rattache ces travaux à une présentation faite au FIC 2023 et à une enquête menée avec Alexis Martins.
- **Nature :** témoignages de praticien, sans méthode publiée ; les images jointes n’ont pas pu être consultées (LinkedIn exige un compte).
- **Sources mobilisées :** à la demande de l’utilisateur, l’analyse ne se limite pas aux posts. Elle s’appuie dès le corps du texte sur les évaluations du NIST, la recherche en biométrie périoculaire et en comparaison faciale, les enquêtes d’AlgorithmWatch et de Bellingcat, les décisions de la CNIL et d’autres autorités, le droit français de l’anonymat et les politiques d’armées étrangères. Chaque apport extérieur est lié à sa source et daté ; les affirmations propres à l’auteur des posts sont signalées comme telles.
- **Thème :** identification de personnels de sécurité à partir de visages partiellement masqués, et conséquences pour l’OPSEC.
- **Source conservée :** `inbox/renseignement-osint/Cyber_LinkedIn_CentralOSINTAgency_Reconnaissance_Faciale_Partielle.txt`.

## Repères pour comprendre le document

Le sujet tient en une question : que reste-t-il d’un visage quand on en cache la moitié, et cela suffit-il à identifier quelqu’un ? La réponse dépend de trois choses qu’il faut distinguer. La première est **ce que voit la machine** : les algorithmes récents savent travailler sur la seule région des yeux et du front, avec des performances mesurées. La deuxième est **où elle cherche** : identifier un inconnu suppose qu’il existe ailleurs, en ligne, une photo de lui à visage découvert, et un outil qui l’a indexée. La troisième est **qui confirme** : un logiciel propose des ressemblances, un analyste compétent tranche à l’aide d’autres indices. Une identification réussie est toujours la combinaison des trois ; une protection efficace doit donc en casser au moins une.

- **Reconnaissance faciale partielle (RFP)** — Expression de praticien pour l’identification d’une personne à partir d’une partie seulement de son visage (yeux, front, profil). Ce n’est pas une catégorie technique normalisée.
- **Région périoculaire** — Zone autour des yeux (sourcils, paupières, coins des yeux, haut des pommettes), étudiée comme modalité biométrique à part entière ; c’est ce que laissent visible une cagoule ou un tour de cou.
- **Authentification (1:1) et identification (1:N)** — Selon la CNIL, la première vérifie qu’une personne est celle qu’elle prétend être en comparant deux images ; la seconde retrouve une personne dans une base en retenant les visages au score de similarité le plus élevé.
- **Gabarit biométrique** — Représentation numérique calculée à partir d’un visage, que le système compare à d’autres ; sa création fait du visage une donnée biométrique au sens du RGPD.
- **Faux positif et faux négatif** — Le premier associe à tort deux personnes différentes, le second manque une correspondance réelle. Les masques font surtout monter les faux négatifs ; deux images masquées comparées entre elles font monter les faux positifs.
- **Moteur de recherche de visages** — Service en ligne (PimEyes, FindClone, Clearview…) qui renvoie les photos d’internet ou d’un réseau social ressemblant au visage soumis.
- **Super-reconnaisseur** — Personne aux capacités de reconnaissance des visages nettement supérieures à la moyenne, repérée par des tests ; certaines polices en emploient.
- **Comparaison morphologique** — Méthode des experts en criminalistique qui compare, élément par élément, les composantes d’un visage (forme, proportions relatives, marques) selon une liste normalisée.
- **Corroboration contextuelle** — Confirmation d’une identité par des indices extérieurs au visage : cicatrices, tatouages, disposition de l’équipement, arme, lieu, date.
- **OPSEC (sécurité des opérations)** — Discipline qui consiste à repérer les informations qu’un adversaire peut collecter et à les protéger.
- **Unités à anonymat protégé** — Services dont la loi interdit de révéler l’identité des membres (forces spéciales, renseignement, unités d’intervention), listés par arrêté.

## Résumé exécutif

Les forces spéciales, les unités d’intervention et, plus largement, les forces de sécurité comptent sur la cagoule ou le tour de cou pour protéger l’identité de leurs membres photographiés en mission, en défilé ou par leur propre communication. Un praticien de l’OSINT affirme sur LinkedIn que cette protection est largement illusoire : avec des outils commerciaux accessibles à tous, il dit avoir rattaché à leur visage entier un opérateur du RAID cagoulé, un gendarme vu de profil et une militaire filmée avec un tour de cou. Il demande que la reconnaissance faciale partielle entre dans les réflexes OPSEC dès la prise de vue.

Les sources indépendantes donnent raison au principe. Le NIST a mesuré en 2020 que les meilleurs algorithmes, d’abord mis en échec par les masques, avaient divisé leurs erreurs jusqu’à dix en quelques mois, pour ne plus se tromper que dans 2,4 à 5 % des comparaisons de visages masqués. La recherche en biométrie étudie la région des yeux précisément parce qu’elle reste exploitable à distance et quand le reste du visage est caché. Des moteurs de recherche de visages vendus quelques dizaines d’euros par mois ont déjà servi à identifier des policiers antiémeute russes, des soldats russes en Ukraine et, par croisement avec les réseaux sociaux, des soldats israéliens poursuivis à l’étranger.

Les mêmes sources dessinent aussi les limites. Comparer deux visages masqués multiplie les fausses correspondances par 10 à 100 ; les erreurs publiques d’identification existent ; et l’expertise humaine, que l’auteur place au premier rang, n’améliore les résultats que lorsqu’elle est formée et combinée aux algorithmes. Les parades efficaces sont connues mais rarement appliquées : lunettes en plus du tour de cou, attention à l’équipement personnalisé et surtout politique de prise de vue et de floutage à la source, comme l’a adoptée l’armée israélienne en janvier 2025.

Pour la veille, le sujet est à la croisée de l’OSINT, de la protection des personnels et du droit des données biométriques. Il pose une question de doctrine : la menace ne vient plus seulement des services étatiques, mais de quiconque sait combiner un moteur de recherche de visages et une méthode de vérification.

## Chronologie

L’histoire récente du sujet montre une capacité qui se diffuse plus vite que les protections.

- **2015-2016** — La biométrie périoculaire devient un champ de recherche structuré, avec une première synthèse de référence (Alonso-Fernandez et Bigun).
- **Novembre 2016** — Des chercheurs de Carnegie Mellon montrent que des montures de lunettes imprimées peuvent tromper un système de reconnaissance faciale.
- **2016** — La France crée l’article 413-14 du Code pénal, qui punit la révélation de toute information permettant d’identifier un membre des forces spéciales.
- **Décembre 2017** — La Cour de cassation juge que l’interdiction de révéler l’identité d’agents protégés couvre les photos et indices permettant de les identifier, pas seulement leur nom.
- **2019** — Des militants russes identifient des policiers antiémeute avec FindClone ; Bellingcat publie un guide de ces outils.
- **Juillet et décembre 2020** — Le NIST mesure l’effet des masques sur 89 puis 152 algorithmes.
- **Mars 2022** — L’Ukraine confirme utiliser Clearview AI pour identifier des soldats russes tués.
- **Octobre 2022** — La CNIL inflige 20 millions d’euros d’amende à Clearview AI.
- **Février 2024** — Le NIST cesse d’évaluer séparément les algorithmes sur visages masqués.
- **Septembre 2024** — L’autorité néerlandaise inflige 30,5 millions d’euros d’amende à Clearview AI.
- **Janvier 2025** — L’armée israélienne impose de masquer visage et nom de ses militaires dans les médias.
- **2 février 2025** — Entrée en application des interdictions du règlement européen sur l’IA, dont la constitution de bases faciales par moissonnage non ciblé.
- **Mai 2026** — Nouvelle édition du guide du ministère des Armées sur les médias sociaux.
- **3 octobre 2026** — Le post sur la militaire au tour de cou relance l’alerte.

## Thèse principale

La thèse de départ est une alerte de praticien : couvrir le bas du visage ne suffit plus à protéger l’identité des personnels exposés, et les intéressés le savent mal. Confrontée aux sources indépendantes, elle se précise. Le risque est réel et documenté, mais il ne tient pas à un logiciel miracle : il naît de la **rencontre entre des algorithmes devenus robustes aux masques, des bases d’images publiques immenses et des méthodes de vérification** désormais accessibles à des acteurs non étatiques.

Il en découle une conclusion de doctrine plus qu’une conclusion technique : la protection de l’identité doit être pensée au moment de la captation et de la diffusion des images, en tenant compte de tout ce qui reste visible (yeux, front, équipement, contexte), et pas seulement du tissu porté sur le visage.

## Informations et arguments importants

### Ce que voit la machine dans un visage couvert

Le meilleur repère public reste la série d’évaluations du NIST, l’institut américain des normes. En juillet 2020, avec des masques ajoutés numériquement sur environ six millions de photos, les 89 algorithmes commerciaux testés, conçus avant la pandémie, voyaient leurs erreurs exploser : les plus précis passaient d’environ 0,3 % d’échecs sur visage nu à environ 5 % sur visage masqué, et beaucoup échouaient dans 20 à 50 % des cas ([NIST, NISTIR 8311, 27 juillet 2020](https://www.nist.gov/news-events/news/2020/07/nist-launches-studies-masks-effect-face-recognition-software)). Cinq mois plus tard, les algorithmes soumis après le début de la pandémie avaient réduit leurs erreurs jusqu’à un facteur dix ; les meilleurs ne se trompaient plus que dans 2,4 à 5 % des cas, soit le niveau des meilleurs systèmes de 2017 sur visage découvert ([NIST, NISTIR 8331, 1er décembre 2020](https://www.nist.gov/news-events/news/2020/12/face-recognition-software-shows-improvement-recognizing-masked-faces)).

Ces rapports apportent trois enseignements directement utiles au sujet :

1. **Ce qui est caché compte plus que la quantité cachée.** Les erreurs augmentent quand le masque couvre le nez et quand il est large et descend sur les joues ; les masques noirs et rouges dégradent davantage les résultats. Un tour de cou remonté sous les yeux correspond au cas le plus défavorable pour l’algorithme, mais il laisse intacts les yeux, les sourcils, le front et la ligne des cheveux.
2. **Masqué contre découvert n’est pas masqué contre masqué.** Quand les deux images comparées sont masquées, le taux de fausses correspondances est 10 à 100 fois plus élevé que lorsque la photo de référence est découverte. Rapprocher deux photos d’un même opérateur cagoulé est donc plus risqué que retrouver sa photo civile.
3. **Les chiffres portent sur la vérification 1:1.** Le NIST n’a pas mesuré la recherche dans une base, qui est le cas de l’OSINT ; il insiste aussi sur la variabilité d’un algorithme à l’autre et recommande des tests sur de vrais masques.

La recherche en biométrie explique pourquoi l’œil suffit souvent. La région périoculaire est étudiée depuis le milieu des années 2010 parce qu’elle reste exploitable quand le visage est partiellement caché ou capté de loin ; ses chercheurs notent que la pandémie en a fait, même en conditions contrôlées, « la seule zone visible » du visage ([Alonso-Fernandez et Bigun, *A Survey on Periocular Biometrics Research*](https://arxiv.org/abs/1810.03360) ; [*Periocular Biometrics: A Modality for Unconstrained Scenarios*, IEEE Computer, 2023](https://arxiv.org/abs/2212.13792)). Le NIST a d’ailleurs cessé en février 2024 d’évaluer séparément les algorithmes sur visages masqués ([NIST FRTE](https://pages.nist.gov/frvt/html/frvt_facemask.html)) : aucune mesure publique récente ne dit donc où en sont les systèmes aujourd’hui.

### Où la machine cherche : les moteurs de recherche de visages

Identifier un inconnu suppose qu’une photo de lui à visage découvert existe et soit indexée. C’est le rôle des moteurs de recherche de visages, dont l’offre s’est banalisée. AlgorithmWatch en a dressé un panorama en août 2022 ([« Face recognition for everyone », 3 août 2022](https://algorithmwatch.org/en/face-recognition-for-everyone/)) :

- **PimEyes** parcourt le web ouvert (sites, articles de presse, blogs) mais pas les réseaux sociaux, pour environ 30 dollars par mois ; la société revendique près de trois milliards de visages indexés, chiffre non audité.
- **FindClone**, service russe, compare les visages aux profils du réseau social VKontakte pour environ 5 dollars par mois ; Bellingcat le décrivait comme l’un des outils d’OSINT les plus puissants.
- **Search4faces** puise dans VKontakte, TikTok, Instagram et OK.ru.
- **Clearview AI**, réservé en principe aux forces de l’ordre, revendiquait 20 milliards d’images en mars 2022 puis 30 milliards fin 2022, aspirées sur les réseaux sociaux sans consentement.

Deux conséquences en découlent pour les forces de sécurité. D’une part, la menace dépend de l’**empreinte d’images** de chaque personne : une photo de mariage, de club sportif ou d’un ancien profil suffit à servir de référence. D’autre part, les outils les plus efficaces sont souvent hors de l’Union européenne (Russie, Géorgie, États-Unis), donc hors de portée des sanctions européennes.

### Qui confirme : l’analyste et sa méthode

L’auteur des posts insiste sur un point que les débats publics négligent : la RFP n’est pas une opération automatique, mais un travail d’ajustements, de comparaisons et de confirmation. La recherche lui donne raison sur le principe. Une étude du NIST publiée dans *PNAS* en 2018 a montré que les examinateurs spécialisés en comparaison faciale et les super-reconnaisseurs font nettement mieux que des non-spécialistes, avec de fortes différences individuelles, et que le meilleur résultat est obtenu par un examinateur associé au meilleur algorithme, devant deux examinateurs réunis ([NIST, « Face recognition experts perform better with AI as partner », mai 2018](https://www.nist.gov/news-events/news/2018/05/nist-study-shows-face-recognition-experts-perform-better-ai-partner)).

La méthode des experts est elle-même normalisée. La norme ASTM E3149-18, issue des travaux du groupe FISWG, fixe la liste des composantes du visage à examiner, du haut vers le bas, en proportions relatives plutôt qu’en mesures, et déconseille la photoanthropométrie, jugée trop peu fiable ([ASTM E3149-18](https://store.astm.org/e3149-18.html)). Bellingcat, de son côté, applique une règle simple aux résultats des moteurs : **une correspondance est une piste, pas une preuve**. Il faut remonter au profil d’origine, vérifier son contexte (photos de groupe, comptes de proches, ancienneté) et chercher d’autres éléments avant de conclure ; ses propres tests montrent des scores de 0,70 attribués à des sosies ([Bellingcat, guide SearchFace/FindClone, 2019, mis à jour](https://www.bellingcat.com/resources/how-tos/2019/02/19/using-the-new-russian-facial-recognition-site-searchface-ru)).

C’est exactement la démarche que décrit l’auteur pour l’opérateur du RAID : il dit avoir confirmé la correspondance entre deux interventions par des marques visibles sur la peau, la disposition personnelle du gilet, l’arme et le viseur. Cette **corroboration par l’équipement** est un enseignement en soi : masquer le visage ne protège pas si le matériel personnalisé reste reconnaissable d’une image à l’autre.

### Des usages déjà documentés contre militaires et policiers

Les cas cités par l’auteur (un gendarme photographié de profil au Niger, un militaire russe identifié à une trentaine de mètres sur un char, l’opérateur du RAID suivi de l’affaire Merah à l’Hyper Cacher, la militaire du 54e régiment de transmissions filmée avec un tour de cou) ne sont pas vérifiables, faute d’images publiées. Mais des cas comparables sont documentés publiquement :

- **Policiers et manifestants en Russie.** En 2019, des militants ont identifié des policiers antiémeute avec FindClone et la recherche d’images de Yandex ; les policiers ont ensuite masqué leur visage, tandis que la reconnaissance faciale servait à arrêter des militants à domicile (AlgorithmWatch, 2022).
- **Guerre en Ukraine.** En mars 2022, le vice-Premier ministre ukrainien a confirmé l’usage de Clearview AI pour identifier des soldats russes tués et prévenir leurs familles ([CBC/Reuters, mars 2022](https://amp.cbc.ca/news/world/ukraine-clearview-ai-russian-soldiers-identify-war-1.6395446)) ; des chercheurs en sources ouvertes ont utilisé FindClone pour identifier des soldats morts ou capturés, et un média d’investigation pour retrouver un soldat lié aux exécutions de Boutcha (AlgorithmWatch). Une société française de formation a revendiqué l’identification d’un commandant tchétchène à partir d’une vidéo ([Futura, mars 2022](https://www.futura-sciences.com/alternative/amp/actualite/97283)).
- **Soldats israéliens.** La Hind Rajab Foundation a croisé les visages de soldats vus dans des vidéos de Gaza avec leurs profils sur les réseaux sociaux pour déposer des plaintes dans plusieurs pays, dont une a conduit un juge brésilien à ordonner une enquête fin 2024 ([CNN via KVIA, 8 janvier 2025](https://kvia.com/news/us-world/cnn-world/2025/01/08/israel-to-conceal-soldiers-identities-after-brazilian-probe-into-war-crimes-allegations/)).
- **Militaires français.** Mediapart a recensé plus de 1 500 photos et vidéos publiées par des militaires français, surtout de l’opération Barkhane, révélant l’organisation des camps, les forces présentes et leurs mouvements ; le gouvernement a répondu que l’usage des réseaux sociaux est encadré, pas interdit ([question écrite n° 35472, Assemblée nationale](https://questions.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE35472.pdf)).

Ces cas montrent aussi le revers de la méthode. Un journaliste néerlandais a désigné à tort une femme à partir d’une vidéo de l’ambassade russe et un forum russe a utilisé FindClone pour harceler des particuliers (AlgorithmWatch). Une capacité qui protège dans un cas expose des innocents dans un autre.

### Les parades : du tissu à la politique d’image

Les parades se situent à trois niveaux, de la plus simple à la plus structurante.

1. **Couvrir davantage.** L’auteur recommande d’ajouter des lunettes de soleil au tour de cou. Une étude de 2021 confirme que les lunettes dégradent la reconnaissance humaine presque autant qu’un masque, y compris chez les super-reconnaisseurs, qui restent toutefois meilleurs que la moyenne ([Noyes et al., *Royal Society Open Science*, 24 mars 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8074904)). Aucune mesure publique ne porte sur la combinaison tour de cou et lunettes face aux outils commerciaux ; le front, les cheveux, les oreilles et la silhouette restent visibles.
2. **Neutraliser les indices non faciaux.** Équipement personnalisé, arme, insignes, tatouages, cicatrices, lieu et date de la photo servent à confirmer une identité. La parade relève de la discipline individuelle et de la vérification des images avant publication.
3. **Maîtriser la captation et la diffusion.** C’est le niveau décisif, parce que les images exploitées viennent souvent de la presse ou de la communication des institutions. En janvier 2025, l’armée israélienne a imposé de ne plus montrer ni le visage ni le nom de ses militaires dans les médias, de ne publier que des images prises de dos ou floutées et de soumettre à autorisation les images de zones de combat ([Ynet](https://ynetnews.com/article/hkb5xv2uyl)). En France, le guide du ministère des Armées sur les médias sociaux, réédité en mai 2026, alerte sur ce qu’une photo peut révéler et rappelle que les personnels sont des cibles, sans traiter explicitement de la reconnaissance faciale ([ministère des Armées, 27 mai 2026](https://www.defense.gouv.fr/terre/actualites/reseaux-sociaux-guide-2026-adopter-bons-reflexes)).

Les techniques de leurre restent marginales. Des chercheurs de Carnegie Mellon ont montré dès 2016 que des montures de lunettes imprimées pouvaient faire échouer ou tromper un système de reconnaissance faciale ([Sharif et al., « Accessorize to a Crime », ACM CCS 2016](https://doi.org/10.1145/2976749.2978392)), mais ces attaques visent un modèle connu et ne protègent pas contre un examinateur humain.

### Ce que dit le droit

Le droit français protège l’identité de certains personnels, pas le visage masqué en tant que tel, et il l’entend largement.

- **Loi du 29 juillet 1881, article 39 *sexies*.** Elle punit de 15 000 euros d’amende la révélation de l’identité des membres de services désignés par arrêté (arrêté du 7 avril 2011 modifié pour le ministère des Armées). La Cour de cassation a jugé le 12 décembre 2017 (pourvoi n° 17-80821) que l’interdiction couvre toute information permettant l’identification : l’affaire portait sur des photos d’un policier du groupe de sécurité du président publiées avec quelques indications sur son poste ([veille juridique de l’IRSEM, février 2018](https://www.irsem.fr/storage/file_manager_files/2025/03/veille-juridique-fevrier-2018.pdf)).
- **Code pénal, article 413-14.** Créé en 2016, il punit de cinq ans d’emprisonnement et 75 000 euros d’amende la révélation de toute information pouvant conduire, directement ou indirectement, à l’identification d’un membre des forces spéciales ou des unités antiterroristes désignées ([amendement gouvernemental CL107, 2016](https://www.assemblee-nationale.fr/14/amendements/1278/CION_LOIS/CL107.pdf)). Il a déjà servi à convoquer des journalistes ([Next, 2018](https://next.ink/6851/107909-convocation-journalistes-par-dgsi-aux-origines-larticle-413-14-code-penal/)).
- **Code pénal, article 223-1-1.** Depuis 2021, il réprime la diffusion d’informations permettant d’identifier ou de localiser une personne pour l’exposer à un risque, avec une peine aggravée lorsque la victime est dépositaire de l’autorité publique. C’est la protection de droit commun des personnels qui ne figurent pas dans les arrêtés.
- **RGPD, article 9.** Le gabarit d’un visage est une donnée biométrique sensible ([CNIL, « Reconnaissance faciale »](https://www.cnil.fr/fr/reconnaissance-faciale)). Sur ce fondement, la CNIL a infligé 20 millions d’euros d’amende à Clearview AI en octobre 2022, sans obtenir de paiement à mi-2023 ([Siècle Digital, 21 octobre 2022](https://siecledigital.fr/2022/10/21/reconnaissance-faciale-la-cnil-sanctionne-clearview-ai-dune-amende/) ; [11 mai 2023](https://siecledigital.fr/2023/05/11/clearview-ai-recolte-une-nouvelle-amende-pour-ne-pas-avoir-respecte-une-decision-de-la-cnil/)), et l’autorité néerlandaise 30,5 millions d’euros en septembre 2024 ([Jurist](https://www.jurist.org/news/2024/09/netherlands-data-protection-authority-fines-us-ai-company-30-5-million-euros-over-facial-recognition-database)).
- **Règlement européen sur l’IA, article 5.** Depuis le 2 février 2025, il interdit les systèmes qui constituent ou étendent des bases de reconnaissance faciale par moissonnage non ciblé d’images sur internet ou de vidéosurveillance. Il ne vise pas en tant que tel l’usage ponctuel d’un moteur par un analyste.

*Inférence de l’analyse :* deux conséquences pratiques en découlent. Publier sans floutage le résultat d’une RFP visant un membre d’une unité protégée peut tomber sous l’article 413-14 ; le floutage pratiqué par l’auteur des posts est donc aussi une précaution juridique. Et l’illicéité européenne des grandes bases faciales ne protège pas contre des acteurs qui les utilisent depuis l’extérieur de l’Union.

## Points particulièrement intéressants pour la veille

- **L’exposition par la communication institutionnelle.** Les images exploitées proviennent souvent des services de communication eux-mêmes ; le cas de 2026 vient d’une vidéo où une militaire se présente. *Inférence pour la veille :* les campagnes de recrutement et de valorisation, qui multiplient les visages identifiables, deviennent un sujet de sécurité.
- **La diffusion de la capacité.** Des outils à quelques dizaines d’euros par mois suffisent quand ils sont maniés avec méthode. *Inférence pour la veille :* la menace inclut activistes, groupes criminels et services étrangers, et pas seulement les grandes puissances.
- **Les politiques d’image des armées.** Israël a formalisé une règle de dissimulation des visages en janvier 2025 ; la France en reste à la sensibilisation. *Inférence pour la veille :* surveiller les consignes des ministères des Armées et de l’Intérieur sur le floutage et la prise de vue.
- **Le contentieux contre les moteurs de visages.** Les sanctions européennes contre Clearview restent largement impayées et PimEyes opère depuis l’extérieur de l’Union. *Inférence pour la veille :* l’application du règlement sur l’IA à ces services sera un test.
- **L’absence de mesure publique récente.** Le NIST a cessé ses tests dédiés aux masques en 2024. *Inférence pour la veille :* toute nouvelle évaluation publique sur visages partiels ou périoculaires mérite d’être suivie de près.

## Faits, opinions et interprétations

### Faits rapportés par les sources

Les faits les plus solides viennent des évaluations publiques : en 2020, le NIST a mesuré la chute puis le redressement rapide des performances sur visages masqués, avec des erreurs de **2,4 à 5 %** pour les meilleurs algorithmes adaptés, et des fausses correspondances **10 à 100 fois** plus fréquentes entre deux images masquées. L’usage de moteurs de recherche de visages contre des policiers, des soldats et des particuliers est documenté par AlgorithmWatch, Reuters et la presse internationale. Les sanctions de **20 millions** (CNIL, 2022) et **30,5 millions d’euros** (Pays-Bas, 2024) contre Clearview AI et la politique israélienne de janvier 2025 sont établies. En revanche, les identifications revendiquées par l’auteur des posts restent des déclarations : ni images, ni outils, ni taux de réussite ne sont publiés.

### Opinions ou positions

L’auteur des posts juge la sensibilisation des opérateurs insuffisante, estime que les lunettes de soleil compliqueraient fortement l’identification et place l’expertise de l’analyste au premier rang ; son refus de publier ses méthodes est un choix éthique assumé. La CNIL considère les enjeux de la reconnaissance faciale comme « considérables » pour les libertés. Les critiques citées par AlgorithmWatch jugent impossible une identification concluante sur une image basse résolution où la bouche, la mâchoire et les oreilles sont cachées.

### Interprétations et inférences

*Inférence de l’analyse :* le sujet mélange souvent deux risques distincts. Le premier est l’**identification** d’un inconnu masqué par recherche dans une base, qui dépend de l’existence de photos découvertes de la personne en ligne. Le second est le **suivi** d’une même personne d’une image masquée à une autre, qui ne donne pas son identité civile mais permet de reconstituer ses missions. Le premier se combat surtout par la réduction de l’empreinte d’images personnelles ; le second par la maîtrise des images opérationnelles et de l’équipement visible. L’auteur suggère enfin que les grands services de renseignement disposent de capacités bien supérieures ; c’est plausible, mais aucune source publique ne permet de le mesurer.

## Limites et points à vérifier

1. **Des démonstrations invérifiables.** Les identifications revendiquées dans les posts ne sont accompagnées ni d’images consultables, ni d’outils, ni de taux d’échec ; elles ne peuvent servir que d’illustration.
2. **Des mesures publiques datées et partielles.** Les chiffres du NIST datent de 2020, portent sur des masques ajoutés numériquement et sur la vérification 1:1, pas sur la recherche dans une base ni sur le tour de cou réel.
3. **Le risque de faux positif sous-estimé.** La comparaison de deux visages masqués multiplie les erreurs ; une confirmation par l’équipement peut elle-même tromper quand le matériel est réglementaire et identique au sein d’une unité.
4. **Une efficacité des lunettes non mesurée.** Les données sur les lunettes portent sur la reconnaissance humaine ; aucune évaluation ne porte sur la combinaison tour de cou et lunettes face aux outils actuels.
5. **Des chiffres d’entreprises non audités.** Les tailles de base revendiquées par PimEyes ou Clearview sont des déclarations commerciales.
6. **Une doctrine française mal connue.** Les guides publics du ministère des Armées n’abordent pas explicitement la reconnaissance faciale ; d’éventuelles consignes internes ne sont pas publiques.
7. **Une attribution incomplète.** L’auteur des posts n’est identifié que par le nom de son compte ; la vidéo citée n’est désignée que par un lien raccourci.

## Sources et références mentionnées

Les posts eux-mêmes citent peu de références : une vidéo d’un créateur désigné comme « Romain P. » et la collaboration d’Alexis Martins. L’essentiel de l’analyse repose donc sur des sources extérieures de natures différentes : évaluations techniques publiques (NIST), littérature scientifique (biométrie périoculaire, *PNAS*, *Royal Society Open Science*, ACM CCS), normes de criminalistique (ASTM E3149), enquêtes de la société civile (AlgorithmWatch, Bellingcat), décisions d’autorités de protection des données (CNIL, autorité néerlandaise), textes et jurisprudence français, et presse internationale sur l’Ukraine et Israël. Les sources primaires ont été privilégiées ; quelques faits ne sont connus que par la presse (politique israélienne, condamnations impayées).

## Cinq éléments essentiels à retenir

1. Un **visage couvert jusqu’au nez reste exploitable** : les algorithmes adaptés aux masques ne se trompaient plus que dans 2,4 à 5 % des cas dès fin 2020, et la région des yeux est une modalité biométrique à part entière.
2. Les **moteurs de recherche de visages** grand public (PimEyes, FindClone) et Clearview ont déjà servi à identifier des policiers, des soldats et des particuliers.
3. L’identification fiable repose sur la **méthode de l’analyste** et la **corroboration par d’autres indices** ; une correspondance logicielle n’est qu’une piste, et deux visages masqués comparés entre eux produisent beaucoup plus de fausses correspondances.
4. La parade efficace est une **politique de prise de vue et de floutage à la source**, comme celle de l’armée israélienne depuis janvier 2025, complétée par les lunettes et la discrétion sur l’équipement.
5. Le **droit français** protège largement l’identité des unités désignées (articles 39 *sexies* de la loi de 1881 et 413-14 du Code pénal), et le droit européen interdit les grandes bases faciales, sans empêcher leur usage depuis l’étranger.

## État de l’art et regards extérieurs

Recherches effectuées le 2026-10-10. Les sources extérieures étant mobilisées dans tout le corps de l’analyse, cette section se limite à la vérification des affirmations des posts, aux contrepoints et aux ressources.

### Vérification des affirmations de la source

| Affirmation des posts | Verdict | Source de la vérification |
|---|---|---|
| La reconnaissance faciale ne fonctionne pas qu’avec des visages entiers et de face | **Confirmé** | NIST, NISTIR 8311 et 8331 (2020) ; littérature périoculaire |
| Des outils accessibles aux civils permettent d’identifier des militaires | **Confirmé** | AlgorithmWatch (2022) ; usages en Russie et en Ukraine |
| Les outils relient un visage masqué à un visage découvert | **Confirmé** dans le principe | NIST 8331 : algorithmes adaptés aux masques |
| Les identifications obtenues sont fiables une fois confirmées | **Non établi** | Aucun protocole ni taux d’échec publiés ; risque accru de faux positifs entre images masquées (NIST) |
| L’expertise de l’analyste est décisive | **Confirmé** | Phillips et al., *PNAS* (2018) |
| Des lunettes rendent l’identification très difficile, voire impossible | **Nuancé** | Noyes et al. (2021) : forte dégradation chez l’humain ; aucune mesure sur les outils commerciaux |
| La vidéo citée porte sur un hacker contrôlant les réseaux du ministère | **Nuancé** | Seul épisode public correspondant : un faux piratage, jeu de piste de recrutement de l’Armée de Terre récompensé par une visite du 54e RT ([Futura, 30 septembre 2025](https://www.futura-sciences.com/tech/actualites/guerre-futur-armee-terre-t-elle-ete-piratee-ce-week-end-etait-ce-piege-ce-revele-cette-drole-manoeuvre-126021/)) ; rapprochement non confirmé |

### Contrepoints et critiques

- **Le risque d’erreur d’identification.** Un développeur de Bosch cité par AlgorithmWatch juge « complètement impossible » une identification concluante sur une image basse résolution où la bouche, la mâchoire et les oreilles sont cachées. Cette réserve vise les identifications sans confirmation ; elle rappelle qu’une démonstration non documentée peut aussi exposer des innocents.
- **La tension avec la liberté de la presse.** Interdire de photographier les opérateurs, même cagoulés, heurterait la liberté d’informer ; l’usage de l’article 413-14 contre des journalistes a déjà suscité des critiques. Le floutage décidé à la source par l’institution, sur le modèle israélien, est une alternative moins attentatoire.
- **Le double usage de la méthode.** Les mêmes techniques servent à documenter des crimes de guerre et à harceler des particuliers. Publier des méthodes de RFP aiderait les défenseurs autant que les attaquants ; le refus de l’auteur de les divulguer se comprend, mais il empêche aussi l’évaluation indépendante de ses résultats.

### Évolutions depuis la publication

Le post date du 3 octobre 2026 ; aucun fait postérieur notable n’a été trouvé au 10 octobre 2026. Si la vidéo citée est bien celle de la campagne de recrutement cyber de l’Armée de Terre lancée en septembre 2025, l’exposition dénoncée provient d’une opération de communication de l’institution elle-même.

### Pour aller plus loin

- [AlgorithmWatch, « Face recognition for everyone »](https://algorithmwatch.org/en/face-recognition-for-everyone/) — Panorama des outils grand public et de leurs usages, des enquêtes de guerre au harcèlement.
- [Bellingcat, guide SearchFace/FindClone](https://www.bellingcat.com/resources/how-tos/2019/02/19/using-the-new-russian-facial-recognition-site-searchface-ru) — Méthode OSINT publique et ses règles de vérification.
- [NIST, FRTE Face Mask Effects](https://pages.nist.gov/frvt/html/frvt_facemask.html) — Résultats de référence sur la reconnaissance des visages masqués.
- [Noyes et al., *Royal Society Open Science* (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8074904) — Effet des masques et des lunettes de soleil sur la reconnaissance humaine.
- [Ministère des Armées, guide du bon usage des médias sociaux (mai 2026)](https://www.defense.gouv.fr/aides-demarches/guide-du-bon-usage-medias-sociaux) — Règles et réflexes officiels pour les personnels.
- [CNIL, « Reconnaissance faciale »](https://www.cnil.fr/fr/reconnaissance-faciale) — Définitions et position de l’autorité française.
