---
title: Chapitre 15 — Autres acteurs étatiques, mercenaires cyber et zones grises
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie IV — DPRK, iran ET autres acteurs
  - index.md
---

Ce chapitre couvre les acteurs étatiques non traités en Parties II-III-IV (acteurs régionaux avec capacités cyber croissantes), les mercenaires cyber commerciaux (NSO, Intellexa, Candiru), et les zones grises crime-État.

## 15.1 Acteurs régionaux documentés

**Vietnam — OceanLotus / APT32** (Cobalt Kitty, BISMUTH) : service de renseignement vietnamien (probablement Ministry of Public Security). Mission : espionnage régional (ASEAN, Chine, Cambodge), dissidents vietnamiens et opposants politiques à l’étranger, entreprises étrangères opérant au Vietnam. TTP : sophistication croissante, ciblage macOS et mobile (distinctif pour un acteur régional), malware custom (SOUNDBITE, PHOREAL). Campagnes contre BMW et Hyundai documentées (2019). Ciblage notable des journalistes vietnamiens à l’étranger.

**Pakistan — SideCopy, Transparent Tribe** : services pakistanais. Mission : ciblage quasi exclusif de l’Inde — gouvernement, défense, télécoms. TTP : malware mobile (Crimson RAT, CapraRAT pour Android, CapraSpy pour iOS), sophistication modérée. Campagne continue depuis les années 2010.

**Inde — SideWinder, Patchwork (Dropping Elephant)** : probablement services indiens. Mission : ciblage du Pakistan, de la Chine, et de l’Asie du Sud-Est dans une moindre mesure. SideWinder est particulièrement actif avec des centaines de campagnes documentées. TTP : spear-phishing, malware custom relativement simple.

**Turquie — Sea Turtle / Teal Kurma** : services turcs probablement. Mission : ciblage régional Moyen-Orient/Europe du Sud. **TTP signature : détournement DNS** — Sea Turtle a documenté une technique de compromission de **registrars DNS** pour détourner les résolutions de domaines de ses cibles (Chypre, Grèce, Kurdistan). Technique inhabituelle et sophistiquée. Ciblage des dissidents kurdes.

**Amérique latine** — **Blind Eagle / APT-C-36** : acteur latino-américain (probablement colombien selon certaines analyses). Mission : ciblage régional (Colombie, Équateur, Pérou, Venezuela). Cibles : gouvernements, finance, entreprises. Sophistication modérée.

**Corée du Sud** : services sud-coréens ont des capacités cyber importantes mais très peu documentées publiquement (l’écosystème sud-coréen publie moins sur ses propres capacités offensives). Quelques mentions de ciblage de la DPRK, en contre-intelligence.

Ces acteurs régionaux se caractérisent généralement par une sophistication modérée, un ciblage géographique concentré, et une visibilité moindre que les grandes puissances cyber. Ils sont néanmoins actifs et peuvent créer des incidents significatifs dans leurs zones d’influence.

## 15.2 Mercenaires cyber / PSO (Private Sector Offensive)

Les **PSO** (Private Sector Offensive) sont des entreprises privées qui développent et vendent des capacités cyber offensives à des États (et parfois à d’autres clients). Le marché est dominé par quelques acteurs majeurs.

**NSO Group** (Israël, fondé 2010) — **Pegasus**. Spyware mobile exploitant des **0-day iOS et Android**, permettant une compromission complète du terminal : accès aux messages (y compris messageries chiffrées type Signal et WhatsApp — lecture en post-déchiffrement sur le terminal lui-même), géolocalisation, microphone et caméra à distance, extraction de données.

NSO vend Pegasus exclusivement à des gouvernements (officiellement), avec un discours « lutte antiterroriste et criminalité grave ». La réalité documentée est beaucoup plus large : usage contre des **journalistes** (Jamal Khashoggi et ses proches avant l’assassinat, Cecilio Pineda au Mexique, des dizaines d’autres documentés par le **Pegasus Project** en 2021 — consortium de 17 médias internationaux coordonné par Forbidden Stories), **dissidents** (membres des familles de dissidents saoudiens, marocains, azerbaïdjanais), **chefs d’État et personnalités politiques** (Emmanuel Macron cité parmi les cibles potentielles, plusieurs dirigeants européens), **avocats des droits humains**, **militants**.

Implications : NSO a été ajouté à l’**Entity List** du Commerce US en novembre 2021. Apple et Meta ont porté plainte contre NSO. L’usage de Pegasus par le gouvernement polonais contre l’opposition (confirmé par Citizen Lab) a fait scandale. L’entreprise a subi des difficultés financières importantes et plusieurs changements de direction, mais reste opérationnelle.

**Intellexa** (consortium européen basé à Chypre/Grèce/Irlande/Macédoine du Nord) — **Predator**. Spyware concurrent de Pegasus, capacités similaires. Documenté par Citizen Lab comme ayant des victimes dans plusieurs pays, notamment des politiciens et journalistes (scandale retentissant en Grèce en 2022-2023, avec ciblage d’un député opposant et de journalistes — affaire **Predatorgate**). Sanctionné par les États-Unis en juillet 2023 et mars 2024.

**Candiru** (Israël, fondée 2014) — spyware ciblant les desktops (Windows principalement) via des 0-day navigateur. Documenté par Citizen Lab et Microsoft (qui a identifié la vulnérabilité CVE-2021-33771 exploitée par Candiru). Sanctionné par les États-Unis en novembre 2021 (Entity List).

**Autres acteurs** : Paragon Solutions (Israël), TrueDialog, et divers acteurs moins documentés. Le marché est en évolution — certains se professionnalisent, d’autres ferment sous la pression réglementaire.

**Pourquoi la CTI documente les mercenaires** : leurs outils apparaissent dans les campagnes d’espionnage étatique. Un analyste qui identifie un spyware Pegasus chez une victime sait que le commanditaire est probablement un **client étatique de NSO**, pas un cybercriminel autonome. La liste des clients NSO/Intellexa/Candiru est partiellement publique (via les révélations Citizen Lab, les enquêtes journalistiques, les sanctions) et inclut de nombreux régimes autoritaires ou illibéraux.

## 15.3 Régulations émergentes sur les PSO

Le marché PSO fait l’objet d’efforts réglementaires croissants.

**Pall Mall Process** : initiative conjointe franco-britannique lancée en février 2024 à Londres. Objectif : établir un cadre international pour la régulation du marché des capacités cyber commerciales. Signataires : une quarantaine d’États, entreprises, et organisations de la société civile (dont les « Big Tech » et des ONG). Le processus est itératif — les discussions se poursuivent dans plusieurs rounds.

**Restrictions d’exportation** : plusieurs pays ont durci les règles d’exportation des technologies de surveillance cyber. L’**Arrangement de Wassenaar** (export control multilatéral) inclut les « intrusion software » depuis 2013. L’UE a un règlement dual-use qui encadre les exportations. Les États-Unis utilisent l’Entity List comme levier.

**Sanctions ciblées** : les Entity List américaines, les sanctions OFAC, et les sanctions UE ont visé NSO, Intellexa, Candiru, et plusieurs individus associés. Ces sanctions ont un effet réel sur la capacité opérationnelle de ces entreprises.

**EU ban on spyware for political surveillance** : des propositions européennes visent à interdire l’usage de spywares commerciaux contre les journalistes, opposants politiques, et défenseurs des droits humains. État législatif en évolution.

**Limitations** : malgré ces efforts, le marché reste actif. De nouveaux acteurs émergent pour remplacer ceux qui sont sanctionnés. La demande étatique (États autoritaires, certaines démocraties aussi) reste forte. L’efficacité des régulations dépendra de leur universalité — les États qui refusent de coopérer peuvent continuer à s’approvisionner.

## 15.4 Zones grises crime-État

Les **zones grises crime-État** sont l’un des phénomènes les plus importants à comprendre dans le paysage cyber contemporain. Elles recouvrent plusieurs configurations.

**APT41 — la double casquette assumée** : déjà traité au Ch.9. Le cas illustre la tolérance étatique (probablement MSS) pour les activités cybercriminelles personnelles des opérateurs, tant que les priorités étatiques sont respectées.

**Ransomware russophone — la tolérance tacite** : déjà traité au Ch.5. Les groupes LockBit, Conti, BlackBasta, ALPHV, Black Suit, Play opèrent sous la tolérance tacite russe. Certains ont des liens documentés avec les services (Conti Leaks 2022 ont révélé des échanges évoquant le FSB). La frontière entre tolérance et connivence est variable selon les groupes.

**DPRK — la méthode criminelle, la finalité étatique** : déjà traité aux Ch.11-12. Lazarus vole des crypto-actifs par des méthodes cybercriminelles, mais la finalité et le commanditaire sont étatiques.

**Hacktivisme instrumentalisé** : déjà traité au Ch.5 (KillNet, NoName057(16), IT Army of Ukraine). Mouvements présentés comme indépendants mais avec un alignement opérationnel systématique sur les priorités d’un État.

**Initial Access Brokers (IAB) — la chaîne fragmentée** : les IAB sont des acteurs cybercriminels qui compromettent des organisations et **vendent l’accès** sur des forums dark web à d’autres acteurs (typiquement des opérateurs ransomware). L’écosystème IAB est massivement russophone. Un accès vendu peut être acheté par un opérateur ransomware classique (finalité criminelle) ou par un acteur étatique qui l’utilise pour un ciblage plus stratégique. La chaîne « IAB → acheteur → usage » brouille l’attribution de l’origine (la compromission initiale) par rapport à l’usage (l’action finale contre la victime).

**Implications pour l’analyse** : face à un incident :

- Ne pas assumer que l’opérateur visible (ransomware, hacktiviste) est l’acteur stratégique réel.
- Identifier si l’accès initial vient d’un IAB — ce qui ajoute une couche analytique.
- Évaluer si le ciblage est cohérent avec une motivation purement financière ou si des signaux étatiques sont présents (choix de cible stratégique, timing politique, absence de monétisation rigoureuse).
- Documenter les incertitudes — dans les zones grises, l’attribution définitive (étatique ou criminel) est souvent impossible sans accès au renseignement non-public.

Le Ch.25 approfondit l’écosystème cyber offensif mondial et ses évolutions.

-----
