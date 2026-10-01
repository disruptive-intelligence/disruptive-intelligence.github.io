---
title: Chapitre 8 — Iran, Corée du Nord et acteurs émergents
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE II — Les acteurs étatiques
  - index.md
---

## 8.1 — L'Iran : APT42, MuddyWater, Cyber Av3ngers

Le programme cyber iranien est plus ciblé et moins scalable que les programmes chinois et russe, mais il possède des capacités significatives, particulièrement en matière de surveillance d'individus et d'opérations de rétorsion.

**APT42** est le groupe d'espionnage le plus actif, ciblant les think tanks, les organismes de recherche, les universités et les individus perçus comme des menaces pour le régime iranien — chercheurs, journalistes, dissidents, membres de la diaspora iranienne. L'ANSSI note que depuis fin 2023, les opérations d'APT42 contre les ONG, centres de recherche et universités semblent représenter une part croissante de ses activités. Microsoft a observé cette activité ciblant des entités en Belgique, France, à Gaza, en Israël, au Royaume-Uni et aux États-Unis.

**MuddyWater** cible des secteurs plus diversifiés, incluant le secteur financier mondial. Le CERT-EU documente une campagne de MuddyWater ciblant des cadres financiers, y compris en Europe.

**Cyber Av3ngers**, affiliés aux Gardiens de la révolution, ont ciblé des systèmes OT dans le secteur de l'eau, exploitant des contrôleurs Unitronics PLC pour accéder à des systèmes de traitement d'eau et d'eaux usées. Ce ciblage OT par un acteur étatique iranien représente une escalade significative par rapport aux opérations d'espionnage traditionnelles.

Le conflit Israël-Hamas a intensifié l'activité cyber iranienne, avec un triplement des cyberattaques attribuées à l'Iran et au Hezbollah selon les autorités israéliennes. L'Iran utilise le cyber comme outil de rétorsion asymétrique — frapper des cibles civiles et économiques en réponse à des actions militaires conventionnelles.

## 8.2 — La Corée du Nord : financement du régime par la cybercriminalité

La RPDC est unique dans le paysage étatique parce que la cybercriminalité est un **outil central de financement du régime**, pas un effet secondaire. Sous sanctions internationales, la RPDC utilise le vol de cryptomonnaies, le ransomware et la fraude pour générer des revenus estimés à plusieurs milliards de dollars.

**Lazarus** (et ses sous-groupes) est l'acteur le plus documenté. Ses opérations incluent le vol massif de cryptomonnaies (les vols attribués à Lazarus représentent certaines des plus grosses pertes individuelles de l'histoire de la crypto), le ransomware ciblant les hôpitaux et les fournisseurs de soins de santé, et les campagnes d'espionnage technologique visant le secteur de la défense.

Le CERT-EU documente en octobre 2025 une campagne de Lazarus utilisant des lures d'offres d'emploi pour cibler des entreprises européennes de défense privées et publiques, en particulier les entités impliquées dans les véhicules aériens sans pilote (UAV). Ce type de ciblage combine l'ingénierie sociale (offres d'emploi attractives) avec l'espionnage technologique (vol de données sur les systèmes d'armement).

## 8.3 — Le phénomène des faux employés IT nord-coréens

Une technique distinctive de la RPDC, documentée par Microsoft et le FBI, est l'infiltration d'entreprises technologiques occidentales par de faux employés IT utilisant des identités synthétiques. Ces opérateurs nord-coréens postulent à des postes de développeurs en télétravail, utilisent des identités volées ou fabriquées, et une fois embauchés, génèrent des revenus pour le régime tout en ayant potentiellement accès à des systèmes sensibles.

La sophistication de ces opérations est croissante : les faux employés utilisent des deepfakes en temps réel pour les entretiens vidéo, des documents d'identité générés par IA (le service OnlyFake permet de créer des faux documents d'identité réalistes), et des réseaux de facilitateurs dans les pays occidentaux qui reçoivent le matériel informatique et fournissent les adresses locales.

## 8.4 — Acteurs émergents : Inde et mercenaires cyber

L'ENISA ETL 2025 documente une observation notable : l'émergence d'activités d'intrusion attribuées à des ensembles d'intrusion **India-nexus** (4% des activités étatiques contre l'UE). Les groupes Sidewinder et DoNot ont été observés ciblant des entités diplomatiques d'Europe du Sud. Bien que représentant une part faible du total, cette émergence est significative parce qu'elle diversifie le paysage d'acteurs étatiques au-delà du quadrilatère traditionnel (Chine, Russie, Iran, RPDC).

Les **mercenaires cyber** (PSOA) constituent une catégorie transversale. Le marché du spyware commercial est dominé par quelques acteurs — NSO Group (Pegasus), Candiru, Paragon — qui vendent des capacités d'intrusion sophistiquées (exploitation de zero-day, compromission de smartphones) à des clients gouvernementaux. Google TAG documente l'existence d'un marché plus large incluant des entreprises moins connues. Ce marché pose des risques spécifiques pour les institutions européennes, les journalistes, les défenseurs des droits humains et les opposants politiques.

## 8.5 — La menace insider à l'ère de la compétition géopolitique

Microsoft consacre dans son MDDR 2025 une analyse substantielle aux menaces internes dans le contexte de la compétition géopolitique. Les États-nations « ont accru leur utilisation d'insiders pour accéder au renseignement », souvent via des opérations à long terme utilisant des affiliations académiques ou professionnelles comme couverture.

Les secteurs les plus exposés — IA, technologies quantiques, biotechnologie, défense — ont à la fois une valeur économique et militaire. L'espionnage par insider peut causer des pertes financières immédiates et un préjudice compétitif à long terme, « effaçant des années d'innovation et d'avantage marché par le vol de R&D ».

Le délai moyen de confinement d'un incident insider est de **81 jours** (données Ponemon/DTEX) — un dwell time considérable qui donne aux acteurs étatiques un point d'appui persistant pour étendre leur accès, couvrir leurs traces et établir des backdoors pour un usage futur.

Les cadres de sécurité traditionnels n'ont pas été conçus pour la menace insider. Les outils de DLP détectent les transferts massifs de fichiers mais manquent l'exfiltration lente et furtive d'un insider espion. L'architecture zero trust ajoute de la protection mais nécessite une opérationnalisation cohérente pour prévenir l'utilisation non autorisée de comptes légitimes. Les licenciements et restructurations exacerbent le risque en créant des employés mécontents et en affaiblissant la supervision.

## 8.6 — 🔴 Fil rouge : alerte Lazarus sur les ingénieurs UAV

> **📌 FIL ROUGE — Épisode 8**
>
> En mai 2025, le CERT-EU diffuse une alerte TLP:AMBER signalant une campagne de Lazarus ciblant les entreprises européennes de défense via de fausses offres d'emploi sur LinkedIn, avec un focus sur les ingénieurs UAV. La branche spatial/drones d'EuroDefense emploie exactement ce profil.
>
> Sophie active immédiatement le protocole insider. Elle demande à l'équipe RH de vérifier les candidatures récentes pour les postes d'ingénieurs UAV et de drones. Parallèlement, elle sensibilise les managers de la branche spatial aux techniques de social engineering via offres d'emploi. Elle fait ajouter des indicateurs techniques (domaines, hashes) issus de l'alerte CERT-EU aux règles de détection du SOC.
>
> Un cas remonte rapidement : un ingénieur a reçu une offre LinkedIn apparemment légitime d'un recruteur d'une entreprise aérospatiale asiatique. Le profil LinkedIn du recruteur a été créé il y a trois mois, a peu de connexions, et la description de l'offre contient un lien vers un « test technique » à télécharger. L'ingénieur n'a pas cliqué, mais Sophie note que la campagne est active et que la branche spatial d'EuroDefense est bien dans le scope.

---
