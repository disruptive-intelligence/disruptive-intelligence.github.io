---
title: "Europol : cryptomonnaies face au quantique, signatures exposées et migration à organiser"
date: 2026-10-11
kind: analysis
theme: "tech"
slug: "europol-cryptomonnaies-face-au-quantique-signatures-exposees-et-migration-a-organiser"
organization: "Europol"
document_type: "rapport"
source_file: "inbox/Quantum-computing-cryptocurrencies.pdf"
source_url: "https://doi.org/10.2813/9406240"
rubriques:
  - "tech-quantique"
  - "tech-infrastructures"
  - "cyber-menaces-cti"
tags:
  - "cryptomonnaies"
  - "Bitcoin"
  - "cryptographie post-quantique"
  - "portefeuilles"
  - "signatures numériques"
---

# Europol : cryptomonnaies face au quantique, signatures exposées et migration à organiser

## Métadonnées

- **Titre original :** *Quantum Computing and Cryptocurrencies — Bridging Technical Expertise and Decision-Making* (couverture, p. 1).
- **Éditeur et attribution :** **Europol**, via son Centre européen de lutte contre la cybercriminalité (**EC3**) ; aucun auteur individuel n'est nommé dans le rapport (couverture, p. 3, 22).
- **Publication :** **2026**, Office des publications de l'Union européenne. ISBN `978-92-9414-127-9`, DOI [`10.2813/9406240`](https://doi.org/10.2813/9406240). Le document imprimé ne précise pas un jour de publication (p. 22).
- **Source originale :** `inbox/Quantum-computing-cryptocurrencies.pdf`, **22 pages PDF**. L'adresse DOI est imprimée p. 22.
- **Nature et périmètre :** rapport de prospective technique et de recommandations publiques sur la menace quantique pour les cryptomonnaies, de la sécurité des portefeuilles aux contraintes de migration des protocoles (p. 3-5, 10-21).
- **Statut des preuves :** l'étude synthétise des travaux et scénarios ; elle ne présente ni attaque quantique observée contre Bitcoin ou Ethereum ni date certaine d'apparition d'une machine capable de casser leurs signatures (p. 9-11, 19-20).

## Repères pour comprendre le document

Pour lire ce rapport, il faut séparer **la preuve de propriété d'un actif**, **les règles collectives qui valident les blocs** et **la fonction de hachage qui lie les données**. Une attaque sur une signature peut permettre une dépense non autorisée sans effacer rétroactivement toute la chaîne. Cette distinction est le fil conducteur d'Europol ; elle ne veut pas dire que tous les mécanismes de consensus sont indépendants des signatures (p. 3-5, 12-14).

- **Qubit physique / logique** — unité matérielle bruitée / unité rendue plus fiable en combinant plusieurs qubits et en corrigeant des erreurs ; la seconde est celle dont un calcul cryptographique de grande ampleur aurait besoin (p. 8-9).
- **Algorithme de Shor** — méthode quantique qui, avec une machine suffisante, peut résoudre des problèmes mathématiques soutenant RSA et les signatures à courbe elliptique ; elle menace les clés publiques classiques (p. 10).
- **Algorithme de Grover** — recherche quantique offrant un gain quadratique pour certains problèmes non structurés ; son effet ne se confond pas avec celui de Shor sur les signatures (p. 11).
- **Fonction de hachage** — transforme une donnée en empreinte de taille fixe, utilisée notamment pour identifier et relier transactions et blocs ; ses propriétés de préimage et de collision doivent être distinguées (p. 11-13).
- **Clé publique / privée** — la clé privée autorise une dépense et la clé publique sert à contrôler la signature ; leur lien mathématique est le point de vulnérabilité discuté par Europol (p. 13-14).
- **Portefeuille / adresse** — logiciel ou dispositif qui gère les clés et forme des transactions / destination où des fonds peuvent être reçus ; la visibilité de la clé publique dépend du mécanisme d'adresse et des dépenses déjà faites (p. 13-15, 19).
- **PoW / PoS** — preuve de travail, où le consensus exige une dépense de calcul, et preuve d'enjeu, où la participation dépend notamment d'actifs mis en garantie ; leurs règles et usages de signatures diffèrent (p. 12-14).
- **UTXO** — sortie de transaction non dépensée dans Bitcoin ; déplacer les fonds qu'elle contient exige une nouvelle transaction, ce qui occupe de la place dans les blocs (p. 19).
- **PQC** — cryptographie post-quantique exécutable sur des ordinateurs classiques, destinée à résister aux attaques quantiques connues ; l'établissement de clés et les signatures demandent des algorithmes différents (p. 16-17).
- **Abstraction de compte** — dans l'exemple ERC-4337 d'Ethereum, possibilité de programmer les règles de validation d'un portefeuille plutôt que de dépendre du seul format de compte externe ; la résistance quantique dépend alors de la règle réellement codée (p. 15-16 ; dernière précision : inférence de l'analyse).
- **Attaque quantique « juste à temps »** — tentative d'exploiter la clé publique révélée pendant qu'une transaction attend confirmation, afin de diffuser une dépense concurrente (p. 19).

## Résumé exécutif

Europol considère que l'arrivée éventuelle d'un ordinateur quantique suffisamment puissant menacerait d'abord les **signatures classiques qui contrôlent les fonds**. La chaîne de blocs et ses fonctions de hachage présentent un profil différent : le rapport ne voit pas un effondrement inévitable des cryptomonnaies, mais un risque de vol d'actifs, de perturbation des transactions et de perte de confiance si l'écosystème ne migre pas. Aucune machine capable de réaliser aujourd'hui cette attaque n'est documentée ; le calendrier reste incertain (p. 3-5, 9-14, 20).

Le rapport explique que **Shor** pourrait retrouver une clé privée à partir d'une clé publique classique, tandis que **Grover** affecte moins directement les fonctions de hachage et les clés symétriques. Il donne une enquête de **32 experts** dont les réponses sur la rupture de RSA-2048 en 24 heures varient fortement selon l'horizon : le graphique est une agrégation d'opinions, pas une prévision propre à Bitcoin. Europol déplace ainsi l'attention vers les portefeuilles et la durée nécessaire pour remplacer signatures, logiciels, matériels et fonds immobilisés dans les anciennes sorties (p. 8-14, 19).

Trois familles de réponse sont proposées : adaptations transitoires des portefeuilles et des adresses ; adoption de **signatures post-quantiques** et mise à niveau des règles de la chaîne ; exploration de technologies quantiques comme la distribution quantique de clés. Europol juge cette dernière voie trop coûteuse et peu adaptée à un déploiement large à court terme. La difficulté centrale est la **coordination** entre développeurs, opérateurs, mineurs ou validateurs, prestataires de portefeuilles et utilisateurs : même avec un algorithme disponible, une grande partie des fonds doit être déplacée par des transactions réelles (p. 4, 15-20).

Cette fiche retient toutefois plusieurs **réserves techniques importantes**. Le rapport attribue parfois trop simplement la sûreté du consensus aux seuls hachages, présente l'abstraction de compte et les preuves ZK comme des protections quantiques sans préciser la règle de validation, et avance un « consensus de 90 % des mineurs » pour les grands changements Bitcoin sans démontrer qu'il s'agit d'une règle générale. La décision ne peut donc pas être « installer un portefeuille intelligent » en bloc : il faut examiner les signatures, les clés visibles, la capacité du protocole et la gouvernance de **chaque** chaîne (p. 12-19 ; réserves de l'analyse).

## Chronologie

Le problème est surtout une **séquence de migration** : l'exposition d'une clé aujourd'hui, l'apparition incertaine d'une capacité d'attaque, et la place nécessaire pour déplacer les fonds avant ce point.

1. **2024 :** le NIST finalise les premiers standards post-quantiques cités par Europol ; le rapport distingue notamment l'encapsulation de clés Kyber et la signature Dilithium (p. 16).
2. **2025 :** une enquête du Global Risk Institute interroge **32 experts** sur la probabilité de casser RSA-2048 en 24 heures. La figure reproduite par Europol place les réponses interprétées entre **5 et 15 % à cinq ans**, **28 et 49 % à dix ans**, et **81 et 93 % à trente ans** ; ce ne sont ni des observations expérimentales ni une échéance pour les portefeuilles (p. 9, figure 1).
3. **2026 :** Europol publie ce rapport et recommande d'engager l'inventaire, les essais de signatures post-quantiques et la concertation, sans annoncer de rupture quantique actuelle (p. 3-4, 20-22).
4. **Avant une capacité d'attaque suffisante :** les réseaux devraient adopter de nouvelles règles et les détenteurs de fonds déplacer leurs avoirs exposés vers des sorties protégées. La migration consommerait une capacité de blocs finie (p. 15-19).
5. **Pendant une dépense à clé révélée :** une attaque « juste à temps » deviendrait envisageable si un adversaire quantique pouvait calculer et diffuser une transaction concurrente avant la confirmation ; le rapport n'établit pas quand ce scénario serait réalisable (p. 19).

## Thèse principale

Le rapport est une **synthèse de sensibilisation et de politique publique**. Sa thèse la plus solide est que la disponibilité d'algorithmes post-quantiques ne suffit pas : il faut que les protocoles les acceptent, que les portefeuilles les utilisent et que les avoirs quittent les formes vulnérables avant une rupture cryptographique. Le risque est donc davantage une **transition collective lente** qu'une destruction soudaine de toutes les fonctions de la blockchain (p. 3-5, 14-20).

Europol veut que décideurs et acteurs techniques puissent choisir des priorités sans confondre l'attaque de Shor sur les clés publiques avec celle, plus limitée et différente, de Grover sur certains usages des hachages. Ce raisonnement justifie la préparation ; il n'établit ni un calendrier fiable de machine quantique ni l'efficacité automatique des mesures transitoires citées (p. 9-11, 15-21).

## Informations et arguments importants

### Des capacités quantiques encore conditionnelles

Le rapport distingue machines quantiques actuelles, **qubits physiques bruités** et capacité de calcul logique corrigée des erreurs. Il rappelle que les diverses plateformes, de l'ion piégé au circuit supraconducteur, ont des contraintes différentes et que le bruit gêne fortement les calculs prolongés. Les annonces industrielles d'objectifs ne valent donc pas démonstration d'une capacité à casser une clé en situation opérationnelle (p. 6-10).

Sa figure issue du Global Risk Institute offre un signal d'incertitude, pas une date unique. À **dix ans**, elle affiche **28 à 49 %** selon l'interprétation « pessimiste » ou « optimiste » des réponses sur une machine capable de casser **RSA-2048 en 24 heures**. Le transfert direct de ces pourcentages à ECDSA, à un UTXO Bitcoin ou à une fenêtre de confirmation n'est pas donné par la figure (p. 9 ; dernière phrase : inférence de l'analyse).

### Signatures, hachages et consensus ne jouent pas le même rôle

Selon Europol, **Shor** menace les schémas classiques à clé publique : un acteur doté des moyens nécessaires pourrait retrouver la clé privée correspondante et **forger une signature de dépense**. **Grover** donne un avantage plus circonscrit dans des recherches sur les hachages ou des secrets symétriques ; le rapport en conclut que l'intégrité des blocs n'a pas le même niveau d'exposition que la propriété des fonds (p. 10-14).

Dans **Bitcoin**, la preuve de travail et les liens entre blocs reposent fortement sur le hachage ; les sorties non dépensées restent contrôlées par des conditions de dépense qui impliquent souvent des signatures classiques. Dans **Ethereum après la fusion**, les validateurs ne minent plus les blocs de la même manière ; le rapport rappelle lui-même qu'une signature peut authentifier leur proposition, tout en affirmant que la sécurité du consensus repose surtout sur les hachages. Cette formulation mérite une analyse par protocole : les signatures ne servent pas uniquement aux portefeuilles (p. 12-14 ; dernière phrase : réserve de l'analyse).

La visibilité d'une **clé publique** n'est pas identique pour toutes les adresses et à toutes les étapes. Europol indique qu'une transaction peut révéler une clé pendant l'attente de confirmation et décrit alors une attaque « juste à temps ». Une clé déjà exposée et associée à des fonds non migrés serait une cible durable. Le rapport invite à classer les UTXO par risque, sans donner dans ses pages une répartition vérifiable de leurs montants par type de sortie (p. 14-15, 19).

### Les remèdes proposés et ce qu'ils supposent

Europol propose d'abord **rotation d'adresses**, **abstraction de compte**, **multisignature** et éventuellement **preuves à divulgation nulle** pour réduire certaines expositions sans attendre une refonte complète. Il reconnaît que ces techniques sont inégales selon les chaînes et que des clés déjà révélées exigent de déplacer les fonds avant l'attaque. Son exemple ERC-4337 concerne l'écosystème Ethereum ; il ne devient pas automatiquement un mécanisme disponible dans Bitcoin (p. 4, 15-16).

La mesure de fond est l'intégration de **signatures post-quantiques** et de règles de validation capables de les accepter. Le rapport cite les standards NIST de 2024, le projet QRL et des obstacles de taille de signatures. Il donne l'ordre de grandeur d'environ **20 Ko** pour certaines signatures à base de hachage contre **72 octets** pour une signature ECDSA, sans pouvoir l'appliquer à tous les algorithmes PQC. Il mentionne aussi **Kyber**, mécanisme d'établissement de secret : son rôle ne se substitue pas à une signature de transaction (p. 16-17).

Enfin, Europol examine la **distribution quantique de clés** et des cryptomonnaies fondées sur des états quantiques. Il en souligne le coût, la portée et la difficulté de passage à l'échelle, puis juge les algorithmes post-quantiques exécutables sur des machines classiques beaucoup plus réalistes à court et moyen terme. Cette partie relève de pistes de recherche, sans proposition de déploiement pour une chaîne publique existante (p. 18).

### Le coût de la migration collective

Les mises à niveau des règles communes demandent un accord social et technique, tandis que les utilisateurs doivent parfois changer de logiciel ou de matériel et **déplacer chaque UTXO concerné**. Le rapport cite l'étude de Pont et collègues pour un minimum de **76 jours de capacité continue** si toute la capacité envisagée était consacrée à la migration, ou environ **300 jours** en y réservant **25 %** de chaque bloc. Ce sont des estimations dépendant des hypothèses de l'étude, pas un calendrier officiel adopté par Bitcoin (p. 19).

Le texte affirme par ailleurs qu'un changement important de Bitcoin exigerait **90 % de consensus des mineurs**, et que Taproot représenterait moins de **1 % de la valeur des UTXO** au moment étudié. Il ne précise ni règle de gouvernance générale étayant le premier chiffre, ni date et méthode de mesure du second. Ces points doivent être vérifiés avant d'être utilisés pour planifier. Europol a néanmoins raison de distinguer capacité du réseau, adoption des portefeuilles et sort des fonds anciens comme trois contraintes différentes (p. 19-20 ; dernière phrase : inférence de l'analyse).

### Recommandations aux décideurs

Le rapport termine par **quatre lignes d'action** : actualiser l'information des responsables publics sur l'état du calcul quantique ; ouvrir rapidement les discussions de migration ; constituer un groupe de travail européen réunissant Commission, scientifiques, industrie, États et agences telles qu'Europol, ENISA, CERT-EU et EU-AMLA ; enfin, surveiller la sécurité quantique des futures monnaies numériques de banque centrale avec la BCE. Ces propositions visent la **coordination**, sans créer par elles-mêmes d'obligation juridique nouvelle (p. 21).

## Points particulièrement intéressants pour la veille

Le signal prioritaire est le **temps nécessaire pour rendre une signature post-quantique utilisable partout**, puis pour déplacer les fonds qui restent protégés par les anciennes règles.

- **Inventaire des sorties exposées.** Le rapport place la clé publique visible au centre du risque. *Inférence pour la veille :* suivre par type de script ou d'adresse les avoirs dont la clé est déjà publique, ceux où elle ne se révèle qu'à la dépense, et les avoirs inactifs difficiles à migrer (p. 13-15, 19).
- **Capacité de migration.** Les transactions de transfert occupent les mêmes blocs que l'activité ordinaire. *Inférence pour la veille :* examiner les hypothèses derrière les **76 jours** cités et tester plusieurs parts de capacité disponible, sans transformer l'estimation en date certaine (p. 19).
- **Écart entre nom d'une technique et protection réelle.** ERC-4337, multisignature et ZK-STARK sont mentionnés comme voies intermédiaires. *Inférence pour la veille :* demander quelle signature autorise effectivement la dépense et si le protocole la vérifie avec un schéma post-quantique (p. 15-16).
- **Gouvernance des changements.** Les solutions demandent une décision collective et parfois une bifurcation du protocole. *Inférence pour la veille :* suivre les propositions publiées, tests, mécanismes d'activation et traitements des fonds non migrés, chaîne par chaîne (p. 14, 16, 19-20).
- **Horizon quantique incertain.** L'enquête d'experts cite une gamme plutôt qu'une date. *Inférence pour la veille :* suivre les progrès démontrés en correction d'erreurs et calcul cryptographique, séparément des annonces d'objectifs matériels (p. 8-10).

## Faits, opinions et interprétations

### Faits rapportés par la source

Europol rapporte que le NIST a finalisé en **2024** plusieurs standards de cryptographie post-quantique, qu'un panel de **32 experts** a été interrogé sur RSA-2048, et que Bitcoin et Ethereum reposent sur des mécanismes de consensus et de signatures distincts. Il cite des projets de migration et une étude estimant la charge de transfert des UTXO Bitcoin à **76 jours** de capacité continue selon certains paramètres. Ces faits sont **rapportés par le document** ; la validité des métriques et des généralisations techniques est examinée séparément (p. 9, 12-19).

### Opinions ou positions de l'auteur

Europol juge **plus probable une adaptation graduelle qu'un effondrement** des cryptomonnaies et demande une action préventive. Il présente les portefeuilles comme le principal point de vulnérabilité, la distribution quantique de clés comme marginale à moyen terme, et la coopération publique-privée comme indispensable. Ce sont des appréciations et recommandations de politique technique ; aucune probabilité chiffrée d'effondrement ni date de rupture des signatures n'est établie (p. 3-5, 18-21).

### Interprétations et inférences

L'analyse infère que le danger opérationnel n'est pas uniforme : il dépend de **la clé exposée**, **la règle de dépense**, **la valeur encore détenue**, **la vitesse d'un éventuel adversaire** et **la possibilité collective de migrer à temps**. Elle distingue une signature forgée d'une chaîne « entièrement déchiffrée », expression inadaptée à un registre public. Les passages suggérant que tout portefeuille intelligent ou tout mécanisme ZK neutraliserait le risque doivent être lus comme des options de conception à prouver, pas comme des protections déjà établies (p. 13-19).

## Limites et points à vérifier

1. **Calendrier quantique spéculatif.** La figure de probabilités est une enquête d'opinion sur RSA-2048, non une démonstration de calcul ni une mesure directe de la sécurité des cryptomonnaies. Les seuils matériels pour une attaque pendant une fenêtre de transaction ne sont pas établis (p. 9, 19).
2. **Consensus trop réduit au hachage.** Le rapport affirme que l'intégrité des chaînes PoW et PoS repose principalement sur les hachages, puis reconnaît qu'une signature peut authentifier un validateur. Il faut préciser le rôle de chaque signature et de chaque règle de consensus avant de limiter le risque aux seuls portefeuilles (p. 12-14).
3. **Portefeuille intelligent et preuve ZK insuffisamment spécifiés.** ERC-4337 change la programmabilité de la validation, sans que le rapport montre une règle de dépense post-quantique déployée. La présence d'une preuve ZK ne démontre pas à elle seule que toutes les signatures classiques deviennent inutiles (p. 15-16).
4. **Effet de Grover sur les collisions.** Le texte regroupe préimages et collisions sous un même raccourci de « gain quadratique » et donne un exemple générique à 256 bits. Ces propriétés ne se ramènent pas automatiquement au même coût d'attaque ni à la même fonction de sécurité (p. 11-13).
5. **Chiffres Bitcoin à contextualiser.** Les **90 % de mineurs**, **moins de 1 % de valeur UTXO Taproot** et **76 jours** sont présentés sans même niveau de preuve ni même portée. Il faut retrouver règles d'activation, date des données et paramètres de calcul avant de les réutiliser (p. 19).
6. **Solutions expérimentales mêlées aux standards.** Les signatures NIST, l'abstraction de compte, la QKD et les monnaies quantiques ne se situent pas au même stade de normalisation ou d'adoption. Les mettre dans une même liste de « remèdes » peut surestimer leur disponibilité pour les réseaux dominants (p. 15-18).
7. **Adoption des détenteurs inactifs.** La migration suppose que les propriétaires puissent et veuillent déplacer leurs fonds. Le rapport n'établit pas une solution sociale ou juridique pour les clés perdues, comptes inactifs ou désaccords sur un éventuel gel d'anciennes sorties (p. 14-16, 19-21).

## Sources et références mentionnées

Europol s'appuie sur ses rapports antérieurs concernant le quantique et la finance, sur l'enquête de **32 experts** du Global Risk Institute, sur **Shor**, **Grover** et des travaux académiques sur les attaques quantiques, sur les standards **NIST**, sur les feuilles de route de la Commission et d'agences nationales, ainsi que sur **ERC-4337**, **BIP 341** et l'étude de **Pont et collègues** sur la migration des UTXO. Les références mêlent normes, recherche, documents institutionnels, documentation communautaire et supports commerciaux ; leur présence ne valide pas chaque chiffre ou extrapolation du texte (p. 3, 9-10, 15-19).

## Cinq éléments essentiels à retenir

1. **Le risque principal concerne la signature de dépense**, dont la clé privée pourrait être dérivée d'une clé publique classique par un ordinateur quantique assez puissant (p. 10, 13-14).
2. **Hachages et signatures ont des profils d'exposition différents** ; cela ne rend pas tous les mécanismes de consensus ou tous les portefeuilles quantiquement sûrs (p. 11-14).
3. **Aucune date fiable de rupture n'est donnée** : les pourcentages de la figure sont des opinions d'experts sur RSA-2048 (p. 9).
4. **La migration exige signatures nouvelles, règles de validation, portefeuilles et transferts de fonds**, avec une capacité de blocs et une gouvernance limitées (p. 16-20).
5. **Les remèdes transitoires ne se suffisent pas à eux-mêmes** : leur efficacité dépend des règles cryptographiques effectivement déployées et des détenteurs capables de migrer (p. 15-19).

## État de l'art et regards extérieurs

Recherches effectuées le **11 octobre 2026**. Les éléments ci-dessous confrontent le rapport à des spécifications, normes et travaux distincts ; ils ne changent pas ce qu'Europol écrit dans les sections précédentes. La [notice officielle d'Europol](https://www.europol.europa.eu/publications-events/publications/quantum-computing-and-cryptocurrencies) date la publication du **7 octobre 2026**, précision absente des pages imprimées du PDF.

### Travaux de référence

- **Normes NIST de 2024.** [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) normalise **ML-KEM**, un mécanisme d'encapsulation de clé ; il ne peut pas, à lui seul, autoriser une dépense. [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) normalise **ML-DSA** et [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) **SLH-DSA**, deux familles de signatures. Pour une chaîne, il faut encore définir leur intégration aux conditions de dépense, aux règles de consensus, aux portefeuilles et à la taille admissible des transactions. Les normes apportent des primitives, pas une migration Bitcoin ou Ethereum déjà accomplie.
- **Coût d'une migration Bitcoin.** L'[étude de Pont et collègues](https://arxiv.org/abs/2410.16965), publiée en 2024, qualifie elle-même ses **76,16 jours** de *borne inférieure non serrée* du temps d'arrêt cumulé dans son modèle. Elle rend concret le coût de la capacité de bloc ; son résultat n'est ni une décision de suspendre le réseau ni une durée certaine pour toute architecture de migration.
- **Cryptanalyse des hachages.** Le [travail de Brassard, Høyer et Tapp](https://arxiv.org/abs/quant-ph/9705002) donne pour la recherche de collisions dans son modèle un coût quantique en **O(N^(1/3))**. Cette propriété diffère de la recherche de préimage associée à Grover en **O(√N)**. Réduire indistinctement toutes les propriétés d'un hachage de 256 bits à « 128 bits de sécurité quantique » efface cette différence et les hypothèses de chaque attaque.

### Compléments sur le sujet

Le rapport met justement l'accent sur les avoirs, mais son raisonnement peut être prolongé en examinant **les estimations de ressources publiées depuis 2025**, **les sorties Bitcoin réellement exposées**, **les clés de consensus Ethereum**, **la validation des portefeuilles programmables** et **les propositions de transition encore au stade de projet**.

- **Une attaque « juste à temps » désormais chiffrée.** Europol s'appuie sur un sondage d'experts et n'établit pas quand une attaque pendant l'attente de confirmation deviendrait réalisable (p. 9, 19). Le [livre blanc de Google Quantum AI, daté du 30 mars 2026](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf), cosigné notamment par Craig Gidney, Dan Boneh et Justin Drake de la Fondation Ethereum, comble en partie ce vide. Il estime que l'algorithme de Shor contre la courbe **secp256k1** de Bitcoin tiendrait dans **1 200 qubits logiques et 90 millions de portes Toffoli**, ou **1 450 qubits logiques et 70 millions**, soit **moins de 500 000 qubits physiques** sur une architecture supraconductrice, près de vingt fois moins que l'estimation antérieure. Le calcul durerait **18 à 23 minutes**, et environ **9 minutes** si la machine a précalculé la première moitié de l'algorithme en attendant qu'une clé publique apparaisse : moins que les **10 minutes** moyennes d'un bloc Bitcoin. Les auteurs distinguent ainsi les architectures « rapides » (supraconducteurs, photonique), qui permettraient d'intercepter une transaction dans le mempool, des architectures « lentes » (atomes neutres, ions piégés), limitées aux clés exposées depuis longtemps. Ils chiffrent les avoirs dormants vulnérables à plus de **1,7 million de BTC** dans des sorties P2PK et jusqu'à **2,3 millions** tous types de scripts confondus, et proposent un cadre de « sauvetage numérique » pour ces fonds. Pour ne pas divulguer de mode d'attaque, ils valident leurs chiffres par une preuve à divulgation nulle de connaissance. Ce sont des **estimations pour une machine qui n'existe pas** ; elles ne datent pas son arrivée, mais rendent concret le scénario qu'Europol mentionne sans le quantifier.

- **Bitcoin : une clé peut être visible dès la réception.** La [spécification de Taproot, BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), indique que la clé publique de sortie est directement incluse dans la sortie P2TR. Sa visibilité ne commence donc pas seulement lorsqu'une transaction de dépense entre dans le mempool. Pour des formats qui n'affichent qu'un haché de clé avant la dépense, l'exposition peut suivre une autre chronologie ; la réutilisation d'adresse ou une dépense passée change aussi le risque. Toute cartographie des UTXO doit donc identifier leur type et leur historique, plutôt que supposer une fenêtre unique d'attaque.
- **Ethereum : les validateurs signent également.** La [documentation officielle des clés de preuve d'enjeu](https://ethereum.org/developers/docs/consensus-mechanisms/pos/keys/) décrit des clés de validation **BLS** servant à signer propositions de blocs et attestations ; leur clé publique est publiée lors du dépôt. Une rupture quantique d'une signature classique toucherait donc aussi une partie du mécanisme de consensus, avec des effets à analyser séparément du vol d'un portefeuille. Les fonctions de hachage restent importantes, mais ne suffisent pas à conclure que « le consensus PoS » serait intrinsèquement protégé.
- **ERC-4337 : flexibilité de validation, pas immunité automatique.** Selon l'[ERC-4337](https://eips.ethereum.org/EIPS/eip-4337), le compte intelligent doit vérifier le champ `signature` d'une `UserOperation` dans `validateUserOp`. Le contrat détermine donc la méthode d'autorisation. Un compte qui continue à accepter une signature à courbe elliptique vulnérable ne devient pas sûr parce qu'il utilise l'abstraction de compte ; il faudrait une règle cryptographique appropriée, correctement mise en œuvre et déployée. Une preuve ZK peut jouer un rôle dans une telle conception, sans suffire à garantir la sécurité de toutes les voies de dépense.
- **BIP 360 : un étage de transition encore proposé.** La [BIP 360, *Pay-to-Merkle-Root*](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki), est au statut **Draft** au 11 octobre 2026. Elle propose une sortie sans chemin de dépense par clé Taproot afin de réduire l'exposition longue. Ses auteurs précisent que les attaques durant le court passage dans le mempool pourraient exiger des **signatures post-quantiques supplémentaires**. Le texte illustre une réponse technique au problème, mais ni son activation ni la protection complète des transactions ne sont acquises.

### Vérification des affirmations de la source

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| Shor met en cause les signatures à courbe elliptique contrôlant les fonds. | **Confirmé**, sous condition d'une machine quantique cryptographiquement pertinente ; aucune date démontrée. | [BIP 360, motivation et modèle de menace](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki). |
| Les hachages rendent globalement le consensus PoW/PoS peu vulnérable. | **Nuancé** : Ethereum PoS dépend aussi de signatures de validateurs BLS. | [Documentation Ethereum sur les clés PoS](https://ethereum.org/developers/docs/consensus-mechanisms/pos/keys/). |
| ERC-4337 et les techniques ZK protègent les portefeuilles contre le quantique. | **Non établi** comme affirmation générale : l'algorithme validé par chaque contrat est décisif. | [ERC-4337, `validateUserOp`](https://eips.ethereum.org/EIPS/eip-4337). |
| La description générale d'une clé seulement exposée pendant la dépense s'applique aussi aux sorties Taproot. | **Contredit** pour le chemin de clé P2TR : la clé de sortie figure déjà dans le `scriptPubKey`. Europol reconnaît ailleurs que la visibilité dépend du stockage. | [BIP 341, conception et règles des sorties](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki). |
| La recherche de collisions et de préimages bénéficie uniformément du raccourci de Grover. | **Contredit** dans cette généralité : les problèmes et leurs coûts quantiques diffèrent. | [Brassard, Høyer et Tapp, algorithme de collision](https://arxiv.org/abs/quant-ph/9705002). |
| Tout changement important de Bitcoin exige **90 %** de consensus des mineurs. | **Contredit** comme règle universelle : Taproot avait un seuil d'activation particulier de 90 %, tandis que la [BIP 9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki) spécifie 95 % sur le réseau principal et permet de modifier ce paramètre. Le signal minier ne résume pas l'acceptation du réseau. | [BIP 341, déploiement](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) ; [BIP 9, seuils](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki). |
| Une attaque « juste à temps » pendant l'attente de confirmation est envisageable, sans calendrier établi. | **Nuancé** : une estimation publiée six mois avant le rapport juge qu'un ordinateur quantique supraconducteur pourrait casser une clé secp256k1 en une dizaine de minutes, soit dans le temps moyen d'un bloc Bitcoin ; la date d'une telle machine reste inconnue. | [Google Quantum AI, livre blanc du 30 mars 2026](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf). |
| La migration prendrait au minimum **76,16 jours** d'arrêt cumulé. | **Nuancé** : borne inférieure dépendant du modèle et de l'architecture étudiés, non durée observée ou programme d'arrêt décidé. | [Pont et collègues, résumé de l'étude](https://arxiv.org/abs/2410.16965). |
| Taproot représente moins de **1 % de la valeur des UTXO**. | **Non établi** ici : le rapport ne fournit ni date, ni méthode, ni jeu de données permettant de reproduire ce ratio. | [Rapport Europol, p. 19](https://doi.org/10.2813/9406240) ; la [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) décrit le protocole, pas cette statistique. |

### Contrepoints et critiques

- **Ne pas réduire l'exposition à « portefeuilles contre chaîne ».** Les clés de validateurs Ethereum sont une dépendance du consensus et les clés Taproot peuvent être visibles avant toute dépense. Ces deux spécifications ne renversent pas la priorité donnée par Europol à la propriété des fonds ; elles obligent à étendre l'inventaire des clés et à distinguer les types d'attaque. [Documentation Ethereum](https://ethereum.org/developers/docs/consensus-mechanisms/pos/keys/) ; [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).
- **Ne pas confondre proposition et protection disponible.** La BIP 360 retire une voie d'exposition longue, mais se déclare elle-même incomplète pour l'exposition courte. Inversement, les signatures NIST sont normalisées mais leur présence dans une norme ne garantit pas que les principaux réseaux les valident. Le rapport gagne à être lu comme un appel à préparer des choix techniques, pas comme une liste de remèdes déjà opérationnels. [BIP 360](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki) ; [NIST FIPS 204](https://csrc.nist.gov/pubs/fips/204/final).
- **Ne pas transformer un sondage en échéance.** Le graphique d'experts repris par Europol porte sur une rupture de **RSA-2048 en 24 heures**, selon des horizons temporels proposés aux répondants. Il ne mesure ni une démonstration de matériel disponible, ni directement une attaque contre ECDSA ou BLS. La fenêtre entre révélation d'une clé et confirmation d'une transaction ajoute encore une contrainte opérationnelle distincte (rapport, p. 9, 19).

### Évolutions depuis la publication

Le rapport officiel a été mis en ligne le **7 octobre 2026** et cette vérification intervient seulement **quatre jours plus tard**. Aucun jalon de déploiement Bitcoin ou Ethereum nouveau, postérieur à cette date, n'a été retenu. Les BIP 360 et 361 figurent déjà dans le [dépôt des propositions Bitcoin](https://github.com/bitcoin/bips) comme **Draft** : elles constituent un état de la discussion au 11 octobre, non un changement du protocole depuis la publication d'Europol. La [communication d'Europol du 7 octobre](https://www.europol.europa.eu/media-press/newsroom/news/europol-urges-early-action-to-protect-cryptocurrencies-and-sensitive-data-quantum-threats) insiste elle aussi sur la préparation précoce et l'incertitude du calendrier.

### Cadre juridique et éthique

- **Union européenne.** La [feuille de route coordonnée publiée le 23 juin 2025](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) s'adresse aux États membres et à leurs parties prenantes pour organiser une transition post-quantique. Elle ne constitue pas, par elle-même, une obligation générale immédiatement applicable à tous les détenteurs de cryptomonnaies.
- **Actifs anciens et gouvernance.** Rendre inutilisables des sorties qui ne migrent pas, ou préserver leur dépense classique, créerait des effets opposés pour propriétaires absents, victimes potentielles et sécurité collective. La [BIP 361](https://github.com/bitcoin/bips/blob/master/bip-0361.mediawiki) est un **projet** sur la migration et l'extinction de signatures héritées ; son dépôt n'est ni une décision de consensus ni un règlement. La réponse exige un débat public sur les règles et les preuves de propriété.

### Pour aller plus loin

- [Europol, notice et rapport original, 7 octobre 2026](https://www.europol.europa.eu/publications-events/publications/quantum-computing-and-cryptocurrencies) : point d'entrée institutionnel et fichier PDF.
- [Google Quantum AI, *Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities*, 30 mars 2026](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf) : estimations de ressources contre secp256k1, attaques « au repos » et « à la dépense », sort des avoirs dormants.
- [NIST, FIPS 203, 204 et 205](https://csrc.nist.gov/projects/post-quantum-cryptography) : distinguer mécanisme d'établissement de clé et signatures normalisées.
- [Bitcoin, BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) et [BIP 360](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki) : comparer la sortie Taproot déployée avec une proposition de limitation de l'exposition longue.
- [Ethereum, clés des validateurs PoS](https://ethereum.org/developers/docs/consensus-mechanisms/pos/keys/) et [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) : séparer sécurité du consensus et règles d'autorisation des comptes.
- [Pont et collègues, coût d'une migration Bitcoin](https://arxiv.org/abs/2410.16965) : retrouver les hypothèses de la borne de **76,16 jours**.
