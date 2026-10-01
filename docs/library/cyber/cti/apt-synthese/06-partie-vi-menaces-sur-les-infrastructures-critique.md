---
title: Partie VI — Menaces sur les infrastructures critiques et l'OT
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

*Le ciblage des systèmes industriels est le scénario le plus critique — celui qui peut causer des dommages physiques. Il mérite un traitement dédié.*

---


## Chapitre 20 — APT et OT/ICS : pourquoi c'est différent

L'environnement OT (Operational Technology) a des spécificités qui changent radicalement la donne de la cybersécurité. Les **protocoles industriels** (IEC 104, IEC 61850, Modbus, DNP3, OPC) n'ont pas d'authentification native — si un attaquant atteint le réseau OT, il peut envoyer des commandes aux automates sans credential. La **convergence IT/OT** croissante (les postes d'ingénierie OT sont connectés au réseau IT pour la maintenance, la supervision, et les mises à jour) crée un chemin d'attaque du réseau bureautique vers les systèmes de contrôle. Les **systèmes hérités** (automates et systèmes de supervision avec 15-20 ans d'âge) ne sont souvent pas patchables et ne supportent pas les agents EDR. Et l'**impact physique** est le différenciateur fondamental : une attaque OT réussie peut provoquer des blackouts, des explosions, des contaminations, ou des accidents industriels.

Le modèle d'attaque OT typique : accès initial via IT (phishing, exploitation de VPN) → mouvement latéral dans le réseau IT → pivot vers OT via un poste d'ingénierie à double connexion (le « jump host ») → reconnaissance du réseau OT (identification des automates, des protocoles, de la topologie) → manipulation des automates (envoi de commandes via les protocoles industriels). L'ensemble prend des semaines à des mois — l'attaquant doit comprendre le processus industriel avant de pouvoir le manipuler.

---


## Chapitre 21 — Campagnes OT/ICS de référence

**Stuxnet (2010)** : la première arme cyber conçue pour causer des dommages physiques. Co-attribution US/Israël. Ciblage des centrifugeuses d'enrichissement d'uranium à Natanz (Iran). Le malware manipulait les automates Siemens S7-300 pour modifier la vitesse de rotation des centrifugeuses, causant leur destruction, tout en affichant des valeurs normales aux opérateurs (manipulation de l'affichage). ~1 000 centrifugeuses détruites, programme retardé de 2-3 ans. Stuxnet a démontré que le cyber peut causer des dommages physiques — il a ouvert l'ère des armes cyber OT.

**BlackEnergy / KillDisk — Ukraine 2015** : Sandworm a compromis 3 distributeurs d'électricité ukrainiens, coupant l'alimentation de ~230 000 foyers pendant 6 heures. Premier blackout confirmé causé par une cyberattaque. L'attaque a été conduite manuellement par des opérateurs qui prenaient le contrôle à distance des systèmes SCADA.

**Industroyer / CrashOverride — Ukraine 2016** : Sandworm a déployé un malware qui manipulait directement les protocoles industriels (IEC 104, IEC 61850, OPC DA) pour ouvrir des disjoncteurs dans un poste de transformation électrique à Kiev, causant un blackout d'~1 heure. C'est le premier malware conçu spécifiquement pour attaquer les systèmes de contrôle du réseau électrique via les protocoles natifs.

**Triton / TRISIS — Arabie Saoudite 2017** : le scénario le plus dangereux. Un attaquant (attribué à la Russie, via le Central Scientific Research Institute of Chemistry and Mechanics — TsNIIKhM) a ciblé les systèmes de sécurité SIS (Safety Instrumented Systems) d'une usine pétrochimique saoudienne — les systèmes dont la seule fonction est d'empêcher les accidents en arrêtant le processus en cas de paramètres dangereux. Désactiver les SIS AVANT de provoquer une condition dangereuse = un potentiel de dommages physiques catastrophiques (explosion, fuite toxique). L'attaque a échoué car le malware a provoqué un arrêt de sécurité non anticipé, révélant l'intrusion.

**Industroyer2 — Ukraine 2022** : tentative de blackout pendant l'invasion russe, déjouée par le CERT-UA et ESET grâce à une détection en quelques heures et une réponse coordonnée. Preuve que les capacités OT continuent d'être développées et déployées.

**Colonial Pipeline (2021)** : ransomware DarkSide sur le réseau IT de l'opérateur d'oléoduc. L'OT n'a pas été directement touché, mais l'opérateur a coupé l'OT par précaution — illustrant que la convergence IT/OT signifie qu'un incident IT peut paralyser l'OT même sans compromission directe.

---


## Chapitre 22 — Le pré-positionnement : la menace silencieuse

Le pré-positionnement est le maintien d'un accès dormant dans des infrastructures critiques, sans action immédiate, pour une utilisation future en cas de conflit. C'est le scénario le plus inquiétant pour les États car il transforme le cyberespace en un terrain de pré-conflit permanent.

**Volt Typhoon** est le cas d'école : depuis 2021 au moins (probablement plus tôt), des opérateurs liés à la Chine ont maintenu des accès dans des infrastructures critiques américaines (télécoms, énergie, eau, transport) en utilisant un LotL quasi exclusif (LOLBins, credentials légitimes, pas de malware custom). Aucune exfiltration, aucun sabotage — juste un accès maintenu pendant des mois/années. La signification stratégique est celle d'une **capacité de dissuasion/représailles** : « si vous intervenez militairement à Taïwan, nous pouvons frapper vos infrastructures critiques ».

La difficulté de détection est maximale : pas d'IoC (pas de malware custom à hasher), pas de traffic anormal (les communications utilisent les outils légitimes), et pas de comportement distinctif (les actions ressemblent à de l'administration normale). La détection repose entièrement sur les anomalies comportementales (un compte admin qui se connecte à un serveur inhabituel, un LOLBin exécuté dans un contexte anormal) et la corrélation multi-sources.

Les implications pour l'Europe : les opérateurs d'énergie, de télécom, et de transport européens sont des cibles potentielles de pré-positionnement — pas seulement par la Chine, mais aussi par la Russie (Sandworm a ciblé les infras critiques européennes dans le contexte du conflit ukrainien). La préparation passe par la visibilité (EDR sur les postes OT, monitoring réseau OT, segmentation IT/OT physique), la détection comportementale (pas de signatures), et la coordination avec les agences nationales (ANSSI, BSI, NCSC).

> **⚡ BLACKOUT — Épisode 5**
>
> BLACKOUT est un scénario de pré-positionnement classique : l'attaquant s'est positionné dans le réseau OT sans agir. Si c'est Sandworm, l'objectif est probablement le sabotage en cas d'escalade du conflit ukrainien. Si c'est Volt Typhoon ou un acteur similaire, l'objectif est la capacité de frappe en cas de conflit Indo-Pacifique. Si c'est un nouveau cluster, l'objectif est indéterminé. La réponse doit être immédiate (éradication + sécurisation OT) mais la compréhension de l'acteur oriente la priorisation et le signalement (ANSSI, OTAN, ISAC énergie).

---
