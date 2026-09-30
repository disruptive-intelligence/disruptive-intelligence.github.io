---
title: 'Chapitre 13 — Iran : contexte, doctrine et groupes APT'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie IV — DPRK, iran ET autres acteurs
  - index.md
---

## 13.1 Priorités iraniennes et doctrine cyber

Les cyberopérations iraniennes s’inscrivent dans une configuration stratégique définie par plusieurs axes.

**Rivalité régionale** : tensions permanentes avec Israël (rivalité existentielle), Arabie saoudite et monarchies du Golfe (rivalité sunnite/chiite + géopolitique). Le cyber est un levier asymétrique pour un pays qui n’égale pas les capacités militaires de ses rivaux.

**Surveillance interne et diaspora** : répression politique contre la dissidence interne et surveillance des opposants à l’étranger (notamment post-Mahsa Amini 2022 et la vague de protestations « Femme Vie Liberté »).

**Sabotage ponctuel** : l’Iran est l’un des rares États à utiliser occasionnellement le **cyber destructif ouvert** (wipers), en réponse à des événements perçus comme des agressions (Stuxnet 2010 a catalysé cette trajectoire).

**Opérations d’influence** : promotion du récit iranien dans les conflits régionaux (Yémen, Liban, Syrie, Irak), influence sur les communautés chiites internationales.

**Contournement de sanctions** : l’Iran subit des sanctions sévères depuis 1979 (renforcées à plusieurs reprises). Le cyber peut servir à contourner certaines sanctions (vol financier, exfiltration de technologies).

**Doctrine** : le cyber iranien est un **levier asymétrique**. Moins sophistiqué que les acteurs de pointe (US, Israël, Russie, Chine), il compense par une grande activité, une acceptation du destructif, et une capacité à causer des dommages à des cibles plus puissantes.

## 13.2 Structure : MOIS vs IRGC

L’appareil cyber iranien est structuré autour de deux pôles institutionnels distincts qui ont des cultures et des missions différentes.

**MOIS / VAJA** (Ministry of Intelligence and Security — وزارت اطلاعات) est le renseignement civil. Institution relativement classique (comparable à un ministère de l’intérieur étendu), conduit l’espionnage extérieur et le contre-espionnage intérieur. Les groupes APT associés au MOIS tendent à être plus orientés **espionnage classique** (collecte de renseignement, ciblage diplomatique).

**IRGC / Sepah** (Islamic Revolutionary Guard Corps — سپاه پاسداران انقلاب اسلامی) est le corps des Gardiens de la Révolution. Force militaire parallèle à l’armée régulière, avec des missions idéologiques et révolutionnaires. Conduit les opérations à l’étranger (Quds Force), gère une partie de l’économie iranienne, et a des branches cyber importantes. Les groupes APT associés à l’IRGC tendent à être plus **agressifs**, **idéologiques**, avec une forte composante de surveillance des opposants et des personnalités cibles.

La distinction MOIS/IRGC est importante pour l’analyse : une opération IRGC peut refléter une initiative révolutionnaire/militaire (ciblage d’un dissident, représailles), une opération MOIS reflète plus probablement un besoin de renseignement classique.

**L’IRGC a une branche cyber structurée** : IRGC Intelligence Organization (IRGC-IO), qui supervise APT42 notamment. L’IRGC a également des capacités cyber dans d’autres structures (IRGC Electronic Warfare and Cyber Defense Command).

## 13.3 APT33 / Peach Sandstorm (IRGC)

**Mission** : espionnage industriel sur l’énergie, l’aérospatial, la pétrochimie. Cibles privilégiées : entreprises énergétiques du Golfe, sous-traitants aérospatiaux américains et européens, industries pétrochimiques saoudiennes (en cohérence avec la rivalité régionale).

**TTP signature** :

- **Password spraying massif** : APT33 est l’un des acteurs les plus connus pour le password spraying à grande échelle sur Azure AD/M365. Volumes gigantesques, faible taux de succès par tentative mais volume global efficace.
- **Malware custom** : backdoors comme **DropShot** (dropper), **StoneDrill** (wiper apparenté à Shamoon), **TurnedUp** (backdoor).
- **Spear-phishing** sur employés cibles.

**Campagnes** :

- Ciblage de l’industrie aérospatiale US (Boeing, sous-traitants) — documenté par FireEye en 2017.
- Ciblage énergie Golfe (Saudi Aramco, autres) — continu.
- Campagnes 2023-2024 documentées par Microsoft (Peach Sandstorm).

**Lien suspecté avec Shamoon** (Ch.14) : certains analystes ont établi des liens entre APT33 et les opérations Shamoon — ce qui placerait APT33 au croisement de l’espionnage et du destructif. Attribution pas pleinement consolidée.

## 13.4 APT34 / OilRig / Hazel Sandstorm (MOIS)

**Mission** : espionnage régional au service du MOIS. Cibles : gouvernements du Moyen-Orient (Golfe, Liban, Israël), finance régionale, énergie, télécommunications.

**TTP signature** :

- **DNS tunneling** : APT34 a historiquement été l’un des groupes qui ont le plus massivement utilisé le DNS tunneling comme canal C2.
- **Webshells** : déploiement massif sur serveurs web compromis.
- **Credential harvesting** : fausses pages de login, spearphishing avec emails contextualisés.
- **Malware** : **QUADAGENT**, **OopsIE**, **Helminth**, **ISMAgent**.

**Leak 2019** : en mars-avril 2019, un leak anonyme sur Telegram (canal « Lab Dookhtegan » — « labo cousu ») a publié des **outils APT34, des données de victimes, et des noms d’opérateurs**. Le leak a exposé l’infrastructure du groupe et plusieurs de ses techniques. L’origine du leak reste débattue (dissident interne, opération Mossad, opération de services tiers).

**Détournement par Turla** : comme mentionné au Ch.6, Turla a été documenté pour avoir utilisé l’infrastructure APT34 pour ses propres opérations — démonstration de l’instabilité relative de l’OPSEC APT34.

## 13.5 APT35 / Charming Kitten / Mint Sandstorm (IRGC)

**Mission** : **social engineering ultra-ciblé**. Cibles : chercheurs spécialisés sur l’Iran et le Moyen-Orient, dissidents politiques iraniens à l’étranger, journalistes, universitaires, cadres d’ONG, parfois femmes politiques (ciblages personnels de campagnes présidentielles US documentés).

**TTP signature — le social engineering d’APT35 est considéré comme le plus sophistiqué au monde dans sa catégorie** :

- **Faux profils LinkedIn** complets de « collègues » ou « recruteurs » avec des mois d’activité pour construire la crédibilité.
- **Impersonation de journalistes** : création de faux profils imitant des journalistes réels de médias respectés, pour approcher des cibles (« je voudrais vous interviewer pour mon article »).
- **Impersonation d’universitaires** : faux chercheurs invitant la cible à une conférence, un panel, ou une publication.
- **Malware léger** : backdoors minimales, souvent déployés via documents Office après établissement de confiance.
- **Phishing OAuth** : fausses applications OAuth imitant Google, Microsoft pour obtenir des accès persistants.

**Particularité** : APT35 investit massivement dans la **construction relationnelle** avant l’attaque. Certaines campagnes impliquent des **mois de conversation légitime** avec la cible avant le moindre élément malveillant. Cette patience et cette sophistication psychologique distinguent APT35.

**Campagnes documentées** :

- **Ciblage de journalistes et universitaires spécialisés sur l’Iran** : continu depuis 2015+.
- **Ciblage de campagnes présidentielles US 2020** : tentatives documentées de ciblage de la campagne Trump.
- **Opérations post-Mahsa Amini (2022-2023)** : ciblage intensif de dissidents à l’étranger, de journalistes couvrant les protestations.

## 13.6 APT42 / Calanque (IRGC-IO)

**Mission** : surveillance ciblée au service de l’IRGC Intelligence Organization. Cibles : opposants politiques iraniens, membres de la diaspora iranienne, personnalités considérées comme menaces par l’IRGC.

**TTP signature** : similaire à APT35 (social engineering, credential harvesting) avec une orientation plus spécifiquement sécuritaire. Surveillance mobile (Android), capture de communications.

**Distinction avec APT35** : les frontières sont parfois floues. Certains analystes considèrent APT42 comme un sous-groupe d’APT35. Microsoft les distingue comme Calanque (APT42) vs Mint Sandstorm (APT35).

## 13.7 MuddyWater / Mango Sandstorm (MOIS)

**Mission** : ciblage régional et international — gouvernements, télécoms, énergie. MuddyWater est l’un des groupes iraniens les plus actifs en volume.

**TTP signature** :

- **PowerShell obfusqué massivement** : MuddyWater a fait du PowerShell obfusqué sa marque de fabrique — scripts lourdement encodés, plusieurs couches d’évasion.
- **Outils open source** : utilisation massive d’outils accessibles publiquement (Koadic, Metasploit, PSEmpire) — moins de malware custom que d’autres groupes, plus d’adaptation d’outils existants.
- **Spear-phishing** avec documents Office contenant des macros.

**Cibles** : Moyen-Orient, Asie centrale, Asie du Sud, Europe dans une moindre mesure.

## 13.8 Scarred Manticore (MOIS, Check Point 2023)

**Attribution** : MOIS, identifié publiquement par Check Point en 2023.

**Mission** : espionnage gouvernemental de haut niveau au Moyen-Orient.

**TTP signature** : outillage **plus sophistiqué** que MuddyWater ou OilRig — rootkits custom, persistence avancée, OPSEC élevée. Scarred Manticore représente potentiellement une montée en gamme du MOIS cyber.

**Campagne récente** : compromission de longue durée (18+ mois) d’organisations gouvernementales au Moyen-Orient.

## 13.9 Agrius — wipers sous fausse bannière hacktiviste

**Attribution** : acteur lié à l’Iran, probablement IRGC.

**Particularité** : Agrius déploie des **wipers** (**Apostle**, **DEADWOOD**, **Moneybird**) généralement **masqués en ransomware**. Les victimes reçoivent une demande de rançon, mais il n’y a pas de mécanisme de déchiffrement réel — c’est un destructif pur. Des **fausses bannières hacktivistes** sont souvent utilisées (« Black Shadow », « Moses Staff ») pour brouiller l’attribution publique et créer un narratif de « hacktivisme antisioniste ».

**Cibles** : Israël principalement, avec quelques extensions régionales.

**Implication** : Agrius illustre une caractéristique de l’écosystème iranien — l’acceptation des opérations destructives et l’utilisation de fausses bannières pour maintenir un déni plausible, tout en signalant aux audiences cibles (en Iran, dans l’« axe de la résistance ») la capacité de frapper.

-----
