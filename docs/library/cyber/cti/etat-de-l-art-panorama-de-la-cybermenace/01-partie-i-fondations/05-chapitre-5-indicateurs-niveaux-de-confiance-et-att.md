---
title: Chapitre 5 — Indicateurs, niveaux de confiance et attribution
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE I — Fondations
  - index.md
---

## 5.1 — Types d'indicateurs : IoC, IoA et signaux faibles

Les indicateurs sont les données élémentaires sur lesquelles repose l'analyse CTI. Ils se déclinent en plusieurs catégories de valeur et de durée de vie différentes.

Les **Indicators of Compromise (IoC)** sont des artefacts techniques qui signalent une compromission : hashes de fichiers malveillants, adresses IP de serveurs C2, domaines malveillants, URLs de phishing, signatures de malware. Les IoC sont faciles à opérationnaliser (ils peuvent être chargés dans les systèmes de détection) mais ont une durée de vie courte : les attaquants changent régulièrement leur infrastructure et leurs outils. Un hash de malware est utile pendant quelques semaines ; une adresse IP de C2 peut être abandonnée en quelques jours.

Les **Indicators of Attack (IoA)** sont des patterns comportementaux qui signalent une attaque en cours ou imminente : séquences d'actions sur un système (exécution de PowerShell après ouverture d'un document Office), patterns de communication (beaconing régulier vers un domaine externe), ou anomalies de comportement utilisateur (accès inhabituels à des partages réseau). Les IoA sont plus durables que les IoC (les comportements changent moins vite que les outils) mais plus difficiles à opérationnaliser (ils nécessitent une analyse comportementale, pas un simple matching de signatures).

Les **TTPs** (Tactics, Techniques and Procedures), structurés selon MITRE ATT&CK, sont les indicateurs les plus durables et les plus stratégiques. Un acteur peut changer ses outils et son infrastructure quotidiennement, mais ses TTPs évoluent beaucoup plus lentement — parce qu'ils reflètent son expertise, son entraînement et ses objectifs. Identifier les TTPs d'un acteur permet de le reconnaître même lorsqu'il change tous ses indicateurs techniques.

Les **signaux faibles** sont des indicateurs partiels, ambigus ou non confirmés qui, pris isolément, ne permettent pas de conclure mais qui, combinés avec d'autres, peuvent révéler une menace émergente. Un scan inhabituel sur un port spécifique, une requête DNS vers un domaine récemment enregistré, un changement de comportement d'un compte utilisateur — chacun de ces éléments est anodin isolément mais peut être significatif en contexte.

## 5.2 — Évaluer la confiance : le code Admiralty et la matrice CERT-EU

Le code Admiralty (ou NATO system) est le standard utilisé par l'ENISA et le CERT-EU pour évaluer la confiance dans les informations collectées. Il repose sur deux dimensions indépendantes.

La **fiabilité de la source** évalue le track record du producteur d'information : A (complètement fiable — source avec un historique long et vérifié), B (habituellement fiable), C (relativement fiable), D (habituellement peu fiable), E (peu fiable), F (fiabilité impossible à juger). Un CERT national avec lequel on collabore depuis des années sera typiquement noté A ou B. Un post anonyme sur un forum underground sera noté E ou F.

La **crédibilité de l'information** évalue la plausibilité et la corroboration de l'information elle-même : 1 (confirmée par d'autres sources), 2 (probablement vraie), 3 (possiblement vraie), 4 (douteuse), 5 (improbable), 6 (crédibilité impossible à juger). La crédibilité est indépendante de la source : une source fiable peut transmettre une information non confirmée (B3), et une source non testée peut transmettre une information corroborée (F1).

Le CERT-EU applique un **seuil d'acceptation strict** : seules les combinaisons A1, A2, B1 et B2 sont autorisées dans ses produits CTI. Toutes les autres combinaisons sont exclues. Ce seuil garantit que les produits sont basés sur des sources ayant un track record démontré (A ou B) et une corroboration ou plausibilité suffisante (1 ou 2). C'est un choix qui privilégie la fiabilité sur la couverture — un CTL qui ne rapporte que des informations de haute confiance sera plus fiable mais potentiellement moins complet qu'un CTL avec un seuil plus bas.

## 5.3 — Communiquer l'incertitude : LCA, WEP et standards FIRST

Le CERT-EU implémente les guidelines FIRST pour la communication de l'incertitude dans les produits CTI, utilisant deux systèmes complémentaires.

Les **Levels of Confidence in Assessment (LCA)** expriment le degré de confiance dans un jugement analytique : low confidence (peu de données, analyse faible), moderate confidence (données partielles, analyse plausible), high confidence (données solides, analyse robuste). Le LCA reflète la qualité et la quantité des preuves ainsi que la solidité du raisonnement analytique.

Les **Words of Estimative Probability (WEP)** expriment la probabilité d'un événement futur ou l'exactitude d'une évaluation : « almost certainly » (>95%), « very likely » (80-95%), « likely » (55-80%), « roughly even chance » (45-55%), « unlikely » (20-45%), « very unlikely » (5-20%), « almost certainly not » (<5%). Ces mots sont calibrés — chaque terme correspond à une fourchette de probabilité définie — ce qui évite l'ambiguïté du langage courant.

L'utilisation cohérente de ces systèmes est une discipline analytique exigeante. L'erreur la plus fréquente est l'overconfidence — présenter un assessment comme « high confidence » alors que les données ne le justifient pas. L'erreur inverse — l'excès de prudence — produit des CTL tellement hédgés qu'ils perdent leur valeur décisionnelle. Le bon calibrage vient avec l'expérience et la rigueur.

## 5.4 — Scoring et priorisation des menaces

Le scoring transforme l'analyse qualitative en évaluation quantifiable, nécessaire pour la priorisation. Le framework CERT-EU combine plusieurs dimensions dans son scoring : la sophistication de l'acteur, l'impact potentiel sur les constituants, la probabilité de matérialisation, et la capacité de détection et de réponse.

En pratique, le scoring doit être pragmatique. Un système trop complexe (20 critères pondérés) ne sera pas maintenu. Un système trop simple (haut/moyen/bas) ne différencie pas suffisamment. Le bon compromis dépend de la maturité de l'organisation et de la taille de l'équipe CTI.

## 5.5 — Le problème de l'attribution

L'attribution — déterminer qui est responsable d'une cyberattaque — est l'un des problèmes les plus complexes de la CTI. Elle repose sur la convergence d'indicateurs techniques, comportementaux et contextuels, et reste intrinsèquement probabiliste.

Les **indicateurs techniques** incluent les malwares utilisés (certaines familles sont associées à des acteurs spécifiques), l'infrastructure C2 (certains acteurs réutilisent des blocs d'adresses IP ou des registrars), et les artefacts de développement (langues, fuseaux horaires, conventions de nommage dans le code). Chacun de ces indicateurs est manipulable : un acteur peut délibérément utiliser le malware d'un autre, enregistrer son infrastructure via des services associés à un tiers, ou insérer de faux artefacts.

Les **indicateurs comportementaux** incluent les TTPs (la manière dont l'attaque est conduite), la victimologie (le choix des cibles), le timing (heures de travail, jours de la semaine) et la persistance (durée et intensité de la campagne). Ces indicateurs sont plus difficiles à falsifier parce qu'ils reflètent les capacités et les objectifs réels de l'acteur.

Les **indicateurs contextuels** incluent le contexte géopolitique (qui a intérêt à attaquer cette cible à ce moment ?), les capacités connues (quels acteurs ont la capacité technique de mener cette attaque ?) et les précédents (cette attaque ressemble-t-elle à des attaques précédemment attribuées ?).

L'attribution publique — lorsqu'un gouvernement attribue officiellement une cyberattaque à un État — est un acte politique autant que technique. Elle implique des conséquences diplomatiques et doit être distinguée de l'attribution technique (qui est un assessment analytique) et de l'attribution judiciaire (qui répond à des standards de preuve beaucoup plus élevés).

## 5.6 — Distinguer fait, hypothèse et piste exploratoire

La rigueur analytique exige une distinction permanente entre trois niveaux d'assertion.

Un **fait vérifié** est un élément objectivement constaté et confirmé : « Le malware X a été observé sur le réseau Y le 15 mars 2025 ». Un fait ne nécessite pas de qualificatif de probabilité.

Une **hypothèse probable** est une conclusion analytique fondée sur des preuves : « L'intrusion est attribuée avec une confiance modérée à un ensemble d'intrusion China-nexus, sur la base des TTPs observés et de la victimologie ». Une hypothèse doit toujours être accompagnée de son niveau de confiance et de ses éléments de soutien.

Une **piste exploratoire** est une possibilité non confirmée qui mérite investigation : « Les horaires de connexion pourraient indiquer un acteur opérant depuis le fuseau horaire UTC+8, ce qui est cohérent avec une origine chinoise mais aussi avec d'autres hypothèses ». Une piste exploratoire doit être explicitement identifiée comme telle.

Mélanger ces niveaux — présenter une hypothèse comme un fait, ou une piste comme une hypothèse — est l'erreur analytique la plus grave et la plus fréquente. Elle détruit la crédibilité du CTL et peut conduire à des décisions mal fondées.

## 5.7 — 🔴 Fil rouge : signaux faibles sur un serveur exposé

> **📌 FIL ROUGE — Épisode 5**
>
> En février 2025, le SOC d'EuroDefense remonte à Sophie un pattern inhabituel : un serveur Exchange exposé à Internet génère un trafic sortant régulier (beaconing) vers un domaine enregistré il y a trois semaines, hébergé chez un fournisseur cloud légitime. Le volume est faible — quelques Ko toutes les 4 heures. Le domaine ne figure dans aucun feed CTI connu.
>
> Sophie applique sa grille d'analyse :
> — **Fait vérifié** : le beaconing existe, le domaine est récent, le pattern est régulier.
> — **Hypothèse** : le serveur est possiblement compromis. Le pattern de beaconing est cohérent avec un implant C2 de type Cobalt Strike ou ShadowPad (confiance : basse — les données sont insuffisantes pour discriminer).
> — **Piste exploratoire** : le ciblage d'un serveur Exchange exposé est cohérent avec les TTPs de plusieurs groupes — APT28, APT29, et des acteurs cybercriminels. L'attribution est impossible à ce stade.
>
> Sophie rédige une note de renseignement à confiance basse (B4 dans le code Admiralty — source habituellement fiable mais information douteuse) et recommande une investigation approfondie sans alerter le COMEX à ce stade. Elle applique le principe : « escalader quand le niveau de confiance justifie l'action, pas quand il justifie l'inquiétude ».

> **🎯 CAPSTONE Partie I** : À partir d'un briefing fictif décrivant le contexte d'une organisation industrielle européenne classée NIS2, définir : le périmètre du CTL (géographique, sectoriel, technique), les 4 PIR prioritaires, le framework d'analyse retenu (taxonomie, scoring, format), la grille de confiance, et les 5 principales sources à exploiter en justifiant leur sélection.

---
