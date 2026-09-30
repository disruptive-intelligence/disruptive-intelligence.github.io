---
title: 'Chapitre 7 — Russie : campagnes de référence et opérations d’influence'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie II — Russie
  - index.md
---

Ce chapitre présente les campagnes russes les plus emblématiques, en complément des descriptions de groupes du Ch.6. Plusieurs de ces campagnes sont traitées de manière approfondie ailleurs dans le cours (SolarWinds au Ch.29, Industroyer au Ch.21). Ce chapitre les resitue dans une perspective d’ensemble et ajoute les opérations d’influence.

## 7.1 SolarWinds / SUNBURST (2020-2021)

**Acteur** : APT29 (SVR). **Paradigme** : supply chain comme vecteur d’espionnage à très grande échelle.

**Synthèse** : compromission du processus de build du logiciel SolarWinds Orion (logiciel de supervision réseau déployé dans des dizaines de milliers d’organisations). Une backdoor (SUNBURST) est injectée dans les builds officiels signés entre février et juin 2020. La mise à jour trojanisée est distribuée à ~18 000 organisations clientes. APT29 sélectionne ~100 cibles de haute valeur (Trésor US, Commerce, DHS, Pentagone partiellement, Microsoft, FireEye, autres) et déploie des outils de seconde étape (TEARDROP, RAINDROP, GoldMax). Mouvement latéral via GoldenSAML pour accéder aux emails et documents Azure AD/O365.

**Découverte** : décembre 2020 par FireEye/Mandiant, qui enquêtait initialement sur le vol de ses propres outils Red Team.

**Impact** : accès multi-mois à des communications gouvernementales stratégiques américaines, impact massif sur la confiance dans la supply chain logicielle, déclenchement de l’Executive Order 14028 (mai 2021) qui a structuré la réponse américaine sur la sécurité logicielle. Détaillé Ch.29.

## 7.2 NotPetya (juin 2017)

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : wiper destructif masqué en ransomware, supply chain comme vecteur de propagation initiale.

**Synthèse** : déploiement initial via une mise à jour compromise du logiciel comptable ukrainien **M.E.Doc** (largement utilisé en Ukraine pour les déclarations fiscales — une forme de supply chain massive). Une fois exécuté, NotPetya se propage latéralement via **EternalBlue** (exploit SMB de la NSA leaké par Shadow Brokers) et via des credentials collectés sur les systèmes initiaux. Il chiffre les fichiers de manière **irréversible** — le mécanisme de rançon est factice, la clé de déchiffrement n’existe pas réellement. C’est un wiper déguisé, pas un ransomware.

**Propagation mondiale** : de l’Ukraine, NotPetya se propage aux multinationales ayant des bureaux en Ukraine, puis à leur réseau global. Victimes notables : **Maersk** (~300 M$ de dommages, opérations maritimes mondiales paralysées), **Merck** (~870 M$), **FedEx/TNT Express** (~400 M$), **Saint-Gobain** (~380 M$), **Mondelez** (~150 M$), et des dizaines d’autres. Dommages mondiaux estimés à **10+ milliards de dollars**.

**Attribution** : CIA (attribution interne juin 2017, publicisée février 2018), UK NCSC et DoD (février 2018), US Treasury (sanctions 2018), Five Eyes. Reconnu formellement comme « la cyberattaque la plus destructrice de l’histoire » par les autorités américaines.

**Leçons** : la supply chain d’un petit éditeur peut produire un impact mondial. Le destructif peut être masqué en criminalité. Les dommages collatéraux d’une opération étatique peuvent dépasser massivement les objectifs initiaux (NotPetya était initialement ciblé sur l’Ukraine, l’ampleur mondiale semble avoir été anticipée mais assumée).

## 7.3 Ukraine 2015-2016 : les premiers blackouts cyber

**Acteur** : Sandworm (GRU Unit 74455). **Paradigme** : cyber OT causant un impact physique direct.

**Ukraine décembre 2015 — BlackEnergy / KillDisk** : trois distributeurs d’électricité ukrainiens compromis. Les opérateurs Sandworm prennent le contrôle à distance des systèmes SCADA et ouvrent manuellement des disjoncteurs, coupant l’alimentation de ~230 000 foyers pendant ~6 heures. KillDisk efface ensuite les systèmes de supervision pour compliquer la récupération. Premier blackout confirmé causé par une cyberattaque.

**Ukraine décembre 2016 — Industroyer / CrashOverride** : cyberattaque plus sophistiquée, automatisée via le malware Industroyer. Industroyer manipule directement les protocoles industriels (IEC 60870-5-104, IEC 61850, OPC DA) pour commander les équipements sans intervention humaine. Ouverture de disjoncteurs à un poste de transformation à Kiev, blackout d’~1 heure. Premier malware conçu spécifiquement pour attaquer les systèmes de contrôle électriques via les protocoles natifs.

**Analyse complète** au Ch.21 (OT/ICS).

## 7.4 Ingérence électorale 2016 aux États-Unis

**Acteur** : APT28 (GRU Unit 26165) pour les compromissions cyber, Internet Research Agency (IRA, entité séparée) pour l’influence sur les réseaux sociaux. **Paradigme** : hack-and-leak coordonné comme instrument d’influence politique.

**Volet cyber** : APT28 compromet le **Comité National Démocrate** (DNC) et le comité de campagne de Hillary Clinton, exfiltre des milliers d’emails et de documents internes entre l’été 2015 et l’été 2016. Les documents sont ensuite publiés en vagues coordonnées via **DCLeaks** (plateforme créée par APT28), **Guccifer 2.0** (persona fictive présentée comme un hacker roumain indépendant — en réalité GRU), et surtout **WikiLeaks** (qui publie les emails Podesta le 7 octobre 2016, quelques heures après la diffusion d’une vidéo embarrassante pour Trump — le timing coordonné suggère une tentative de détournement de l’attention médiatique).

**Volet influence** : l’Internet Research Agency (IRA, troll farm à Saint-Pétersbourg liée à Prigojine) conduit une campagne massive d’influence sur les réseaux sociaux (Facebook, Instagram, Twitter, YouTube) — création de milliers de faux comptes amplifiant des messages polarisants sur des sujets sociétaux (race, armes, immigration), organisation d’événements physiques via des fausses identités.

**Attribution** : ODNI report (janvier 2017) établit l’attribution à la Russie avec « haute confiance ». Indictment DOJ 2018 inculpe nommément 12 officiers du GRU Unit 26165 et 13 personnes/3 entités de l’IRA. Les sanctions et expulsions diplomatiques qui suivent marquent une rupture.

**Leçons** : le cyber et l’influence sont intégrés, pas séparés. Les attributions publiques rapides (2 mois après l’élection) deviennent un standard.

## 7.5 Bundestag 2015 et campagnes anti-OTAN continues

**Acteur** : APT28. **Paradigme** : espionnage gouvernemental stratégique.

**Bundestag (mai 2015)** : APT28 compromet le réseau IT du parlement allemand. Accès maintenu plusieurs semaines, exfiltration massive de documents parlementaires (dont certains classifiés). La découverte conduit à une reconstruction complète du réseau (des mois de travail, des dizaines de millions d’euros). La chancelière Merkel est elle-même directement visée (son adresse email personnelle parlementaire a été compromise).

**Campagnes continues OTAN** : APT28 et APT29 maintiennent un ciblage permanent des ministères de la défense, des institutions de l’OTAN (Alliance, agences), des fournisseurs de défense majeurs, et des think tanks stratégiques. Ces campagnes sont rarement publicisées en détail (les victimes ne communiquent pas), mais des fragments apparaissent dans les rapports de Mandiant, Microsoft, ANSSI. La règle : tout ce qui touche à la stratégie OTAN est une cible prioritaire des services russes.

## 7.6 Campagne Ukraine 2022-présent

La campagne cyber russe contre l’Ukraine depuis février 2022 est la plus intense de l’histoire. Microsoft Threat Intelligence Center a publié plusieurs rapports annuels qui documentent des dizaines de campagnes distinctes et des centaines de cibles. Synthèse.

**Wipers multiples** : HermeticWiper, IsaacWiper, CaddyWiper, WhisperGate, AcidRain, plusieurs variants non catalogués. Déploiement souvent synchronisé avec des événements militaires ou politiques (invasion initiale, changements stratégiques, anniversaires).

**Attaques OT** : tentative **Industroyer2** en avril 2022 contre un opérateur électrique ukrainien — **déjouée** par le CERT-UA et ESET grâce à une détection et une réponse en quelques heures. Échec notable pour Sandworm. Des tentatives ultérieures ont été déjouées, d’autres partiellement réussies (blackouts ponctuels rapidement restaurés).

**AcidRain / Viasat (24 février 2022)** : le jour de l’invasion, Sandworm déploie AcidRain contre les terminaux satellite du fournisseur Viasat KA-SAT. Impact premier : perturbation des communications militaires ukrainiennes (dépendantes de Viasat pour certaines liaisons). Impact collatéral : **5 800 éoliennes allemandes** utilisant Viasat KA-SAT pour la télésupervision rendues inopérables — exemple frappant d’effet collatéral transfrontalier d’une cyberattaque étatique. Attribution publique par UE, UK, US en mai 2022.

**Ciblage multi-secteurs** : gouvernement ukrainien, médias, télécoms, énergie, transport, secteur financier, organisations humanitaires, infrastructure cloud. Gamaredon en continu sur le volume, Sandworm pour les opérations majeures, APT28 pour l’espionnage militaire, Unit 29155 pour les opérations déstabilisatrices.

**Coopération défensive sans précédent** : Microsoft, Google, ESET, AWS, Cloudflare, Starlink (connectivité résiliente), CERT-UA, USCYBERCOM hunt forward teams, européens (CERT-EU, ANSSI, BSI, NCSC). Cette coopération est détaillée au Ch.19 (Ukraine).

## 7.7 Microsoft breach 2023-2024

**Acteur** : APT29. **Paradigme** : compromission cloud identity contre le plus grand fournisseur cloud du monde.

**Synthèse** : en novembre 2023, APT29 conduit un password spray contre un tenant Azure AD test non-production de Microsoft. Un compte avec des permissions héritées sur un environnement de test est compromis. L’attaquant pivote via une application OAuth legacy aux permissions Graph API excessives, qui permet l’accès aux emails de dirigeants Microsoft. Persistence établie via création d’applications OAuth supplémentaires.

**Détection** : Microsoft détecte l’intrusion en janvier 2024 (dwell time : ~2 mois). Divulgation publique le 19 janvier 2024.

**Cibles additionnelles** : Hewlett Packard Enterprise révèle une compromission liée en janvier 2024. D’autres organisations (non nommées publiquement) ont été affectées via des patterns similaires.

**Leçons** : même les fournisseurs cloud les plus matures sont vulnérables via des configurations héritées et des environnements de test. Les abus d’applications OAuth avec permissions excessives sont un vecteur APT29 récurrent. La visibilité sur les consentements OAuth et les permissions Graph API est devenue une priorité de sécurité cloud.

## 7.8 Opérations d’influence

Les opérations d’influence russes méritent un traitement dédié car elles sont intégrées aux opérations cyber dans la doctrine hybride.

**Internet Research Agency (IRA)** : troll farm basée à Saint-Pétersbourg, liée à Evgueni Prigojine (fondateur du groupe Wagner, tué dans un accident d’avion en août 2023 après la mutinerie contre Poutine). L’IRA a conduit depuis les années 2010 des opérations massives d’influence sur les réseaux sociaux occidentaux (US, Europe). Post-Prigojine, l’organisation a connu une période d’incertitude puis a apparemment été reprise sous contrôle étatique direct.

**Doppelganger** : opération d’influence identifiée publiquement à partir de 2022. Création de faux sites web imitant l’apparence de médias occidentaux légitimes (Le Parisien, Der Spiegel, The Guardian), publication d’articles orientés, diffusion via réseaux sociaux. Démantèlements partiels par Meta, Google, et les autorités françaises. Attribution : proxies russes, avec liens suspectés aux services.

**RRN (Reliable Recent News) / Recent Reliable News** : opération similaire à Doppelganger, ciblage européen et français.

**Storm-1516** (nomenclature Microsoft, 2024) : opération de désinformation liée à la Russie, ciblant des événements politiques européens.

**Techniques** : création de volumes massifs de faux comptes (avec usage croissant d’IA générative pour les profils et le contenu), exploitation de faux sites médias, amplification via influenceurs complaisants, exploitation d’événements réels pour injecter des narratifs orientés.

**Lecture opérationnelle** : une opération d’influence russe typique coordonne plusieurs leviers (hack-and-leak si pertinent, sites médias fabriqués, comptes réseaux sociaux, amplification sur Telegram et plateformes alternatives). Les cyberopérations alimentent l’influence (vol de documents ensuite publiés), l’influence justifie les cyberopérations (campagne de préparation d’opinion avant une action cyber).

## 7.9 Leçons : l’intégration espionnage / destruction / influence

La synthèse de l’expérience russe en cyberopérations révèle un modèle intégré unique.

**Continuum d’opérations** : espionnage, influence, sabotage et pré-positionnement ne sont pas des catégories séparées. Un même service peut conduire plusieurs types simultanément ; les TTP se recouvrent ; le renseignement collecté à un stade nourrit les opérations du stade suivant.

**Tolérance au bruit variable selon le service** : SVR (APT29) maximise la furtivité ; GRU (APT28, Sandworm, Unit 29155) accepte le bruit pour l’efficacité opérationnelle ; FSB varie (Turla ultra-furtif, Gamaredon volumineux et peu furtif).

**Utilisation du cybercrime et de l’hacktivisme comme leviers** : la tolérance tacite de l’écosystème cybercriminel russophone et l’instrumentalisation d’hacktivistes (KillNet, NoName057(16)) permettent d’augmenter la surface opérationnelle sans attribution étatique directe.

**Exposition relativement élevée** : comparé à la Chine (furtive), la Russie assume une visibilité d’opérations supérieure — les attributions publiques sont fréquentes, les indictments nombreux, les sanctions accumulées. L’appareil russe semble juger que l’impact opérationnel dépasse le coût diplomatique.

Pour l’analyste face à une intrusion compatible avec un acteur russe : la clé est de déterminer **quel service** est probablement en jeu, car cela conditionne les attentes (espionnage furtif long terme si SVR, destructif à venir si GRU, opération déstabilisatrice si Unit 29155). Cette discrimination est souvent plus importante, opérationnellement, que l’attribution à « la Russie » en général.

-----
