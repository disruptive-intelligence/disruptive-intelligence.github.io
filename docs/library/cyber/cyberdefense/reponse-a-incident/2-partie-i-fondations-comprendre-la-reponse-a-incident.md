---
title: 'PARTIE I — FONDATIONS : COMPRENDRE LA RÉPONSE À INCIDENT'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 2
chapters: 9
---

*Avant de répondre à un incident : comprendre ce qu'est un incident, ce qui distingue l'IR des disciplines voisines, quand un incident devient une crise, et quels cadres méthodologiques structurent la discipline.*

---

### Chapitre 1 — Qu'est-ce qu'un incident de sécurité

#### 1.1 Définition opérationnelle : événement, alerte, incident, crise

La chaîne conceptuelle qui va du bruit ambiant du système d'information jusqu'à la crise majeure comprend quatre niveaux distincts, et la confusion entre ces niveaux est une source récurrente de dysfonctionnement dans les organisations.

Un **événement** est un fait observable dans le système d'information : une connexion réseau, une authentification, une modification de fichier, un scan de port, un redémarrage de service. Les systèmes d'information modernes génèrent des milliards d'événements par jour. La quasi-totalité sont normaux et attendus.

Une **alerte** est un événement signalé par un système de détection (EDR, SIEM, IDS, antivirus, règle de corrélation) comme potentiellement anormal ou malveillant. Le taux de faux positifs des systèmes de détection varie considérablement (de 10 % dans les environnements bien calibrés à plus de 90 % dans les environnements mal configurés), ce qui signifie que la majorité des alertes ne correspondent pas à des incidents réels. Le travail du SOC est précisément de trier ces alertes pour identifier celles qui nécessitent une investigation.

Un **incident** est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité, ou la disponibilité d'un actif du système d'information. La confirmation transforme la suspicion en certitude : un comportement malveillant est effectivement en cours ou a eu lieu. L'incident déclenche des processus spécifiques (investigation, confinement, notification) et mobilise des acteurs qui ne sont pas impliqués dans le traitement des alertes courantes.

Une **crise cyber** est un incident dont l'impact dépasse la capacité de réponse normale de l'organisation et nécessite l'activation d'une gouvernance exécutive. La crise se caractérise par l'ampleur de l'impact (technique, business, réputationnel, réglementaire), l'incertitude sur l'évolution, la pression temporelle intense, et la nécessité de décisions stratégiques qui dépassent le périmètre de l'équipe technique. La distinction entre incident et crise est traitée en profondeur au Ch.3.

Ces distinctions ne sont pas sémantiques. Elles déterminent le niveau de mobilisation (qui est réveillé à 2h du matin), les processus activés (IRP, cellule de crise, communication), les obligations réglementaires (notification ANSSI, CNIL), et les interlocuteurs impliqués (la direction générale n'est pas mobilisée pour chaque alerte — elle l'est pour une crise).

> **Piège fréquent :** Confondre la gravité technique et la gravité business. Un malware sur un poste isolé sans données sensibles est un incident technique mineur même si le malware est sophistiqué. Un phishing qui compromet le compte email du directeur financier est un incident business potentiellement majeur même si la technique est triviale. La classification doit intégrer les deux dimensions.

#### 1.2 Taxonomie des incidents

Une taxonomie partagée est indispensable pour trois raisons : elle accélère le triage (chaque catégorie active un playbook spécifique — voir Ch.7), elle normalise la communication (tous les acteurs parlent le même langage), et elle structure le reporting (les métriques et les tendances ne sont comparables que si les incidents sont classés de manière cohérente).

La classification par **vecteur d'attaque** identifie comment l'attaquant a pénétré le système : phishing (email, SMS, voix), exploitation de vulnérabilité (0-day, N-day non patchée), compromission supply chain (mise à jour logicielle piégée, prestataire compromis), credential stuffing ou brute force, insider (employé ou ex-employé malveillant), accès physique, ou compromission de tiers de confiance (VPN prestataire, accès partenaire).

La classification par **objectif** identifie ce que l'attaquant cherche à accomplir : ransomware et extorsion (chiffrement + menace de publication), espionnage et exfiltration (vol de propriété intellectuelle, renseignement), sabotage et destruction (wiper, manipulation de systèmes OT), fraude financière (BEC, détournement de virements), hacktivisme (défacement, DDoS idéologique), ou cryptomining (utilisation des ressources de calcul).

La classification par **impact** identifie les conséquences : atteinte à la confidentialité (données exposées), atteinte à la disponibilité (systèmes hors service), atteinte à l'intégrité (données modifiées), impact réputationnel (perte de confiance des clients, médiatisation), impact réglementaire (notification obligatoire, sanctions), et impact financier (perte d'exploitation, rançon, frais de remédiation).

La classification par **gravité** va de P4 (incident mineur — malware isolé, phishing sans compromission) à P1 (incident critique — compromission de l'AD, ransomware à grande échelle, exfiltration massive) avec des critères objectifs pour chaque niveau. Le détail de la grille de gravité est en Annexe G.

#### 1.3 L'incident comme révélateur systémique

Un incident de sécurité n'est jamais un événement isolé. Il est le symptôme visible d'une ou plusieurs défaillances systémiques dans les couches de défense de l'organisation. L'investigation IR ne vise pas seulement à résoudre l'incident présent — elle vise à comprendre pourquoi les défenses ont échoué et à corriger les causes racines.

Pourquoi le phishing a-t-il fonctionné ? Parce que le sous-traitant n'avait pas de MFA, parce que l'utilisateur n'était pas formé, parce que le filtre anti-phishing n'a pas détecté la pièce jointe. Pourquoi l'attaquant a-t-il pu progresser pendant 5 semaines ? Parce que l'infostealer a échappé à l'antivirus, parce que les alertes de l'EDR ont été classées en faux positifs, parce que la surveillance des comptes de service était insuffisante. Pourquoi le ransomware a-t-il pu chiffrer les sauvegardes ? Parce qu'elles étaient sur le même réseau, accessibles avec les mêmes credentials.

Chaque « pourquoi » révèle une faille corrigeable. C'est cette logique de Root Cause Analysis qui transforme un incident douloureux en opportunité d'amélioration structurelle. L'IR n'est pas du « pompierisme » — c'est de l'investigation structurée avec un double objectif : résoudre l'incident actuel ET empêcher le suivant.

#### 1.4 Fil rouge — BLACKTIDE : l'alerte initiale

> **🔍 BLACKTIDE — Épisode 1**
>
> Vendredi 14 mars 2026, 22h17. L'EDR CrowdStrike Falcon déployé sur le contrôleur de domaine DC01 d'Arvantis déclenche une alerte de sévérité « haute » : détection de l'exécution de `PsExec.exe` depuis le répertoire `C:\Users\svc_deploy\AppData\Local\Temp\`, couplée à une modification de GPO visant à désactiver Windows Defender (commande PowerShell `Set-MpPreference -DisableRealtimeMonitoring $true` exécutée via GPO).
>
> Karim Belkacem, analyste SOC N2 en astreinte, reçoit l'alerte sur son téléphone. Il se connecte à la console EDR depuis son domicile et vérifie : aucune opération de maintenance planifiée ce soir, le compte `svc_deploy` est un compte de service rarement utilisé, et l'exécution de PsExec depuis un répertoire temporaire est anormale. Il contacte l'administrateur d'astreinte : « Tu as lancé quelque chose sur DC01 ce soir ? » Réponse : « Non, rien du tout. »
>
> Karim qualifie : **incident confirmé**. L'activité n'est pas légitime, elle cible un contrôleur de domaine, et elle implique un outil de mouvement latéral et une tentative de désactivation des défenses. Classification initiale : P2 (incident significatif — compromission de serveur critique), en attente de réévaluation.
>
> Il applique la procédure d'escalade : appel à l'IR lead, Nadia Moreau. Il est 22h45.
>
> Première question que personne ne pose encore : depuis combien de temps l'attaquant est-il dans le réseau ?

---

### Chapitre 2 — L'Incident Response comme discipline d'orchestration

#### 2.1 Ce qui distingue l'IR du SOC

Le SOC (Security Operations Center) est un dispositif permanent de détection et de triage. Les analystes SOC N1 traitent les alertes en masse, filtrent les faux positifs, et escaladent les vrais positifs. Les analystes N2 investiguent les alertes escaladées et confirment ou infirment les incidents. Le SOC est un capteur permanent — il fonctionne 24/7, traite des centaines ou des milliers d'alertes par jour, et son objectif est de détecter et qualifier.

L'IR (Incident Response) prend le relais quand l'alerte est confirmée comme incident. L'IR pilote l'investigation approfondie, coordonne les acteurs techniques et non techniques, prend les décisions de confinement et d'éradication, et conduit l'organisation jusqu'à la résolution complète et le retour d'expérience. L'IR est une capacité activée ponctuellement — elle se déclenche quand un incident est confirmé et se désactive quand l'incident est clos.

La frontière entre SOC et IR n'est pas toujours nette dans les petites organisations (les mêmes personnes peuvent porter les deux casquettes), mais les fonctions sont distinctes : le SOC détecte, l'IR orchestre la réponse.

#### 2.2 Ce qui distingue l'IR du forensic

Le forensic numérique (digital forensics) est une discipline d'analyse technique approfondie : acquisition d'images disque bit-à-bit, analyse de la mémoire vive, analyse d'artefacts système, reverse engineering de malware, reconstitution chronologique granulaire des actions sur un système. Le forensic produit des preuves — au sens technique et parfois judiciaire.

L'IR utilise le forensic comme un outil parmi d'autres. L'investigateur IR fait du forensic « good enough » — orienté décision, pas orienté preuve exhaustive. La question de l'IR n'est pas « quelle est l'empreinte exacte du malware dans le registre à la microseconde près ? » mais « ce serveur est-il compromis ? oui ou non — parce que je dois décider dans 30 minutes si je l'isole ». L'IR cherche la compréhension opérationnelle suffisante pour agir ; le forensic cherche la reconstitution exhaustive.

En pratique, les deux sont souvent menés en parallèle : l'IR guide les actions immédiates (confinement, éradication), pendant qu'un forensicien dédié ou un prestataire PRIS produit les analyses approfondies et les preuves pour la plainte pénale. Le cours SOC de la bibliothèque traite de la détection en détail ; le cours Forensic traite de l'analyse technique en profondeur. Ce cours traite de l'orchestration.

#### 2.3 Ce qui distingue l'IR de la gestion de crise

La gestion de crise est un processus de gouvernance qui mobilise la direction générale, la communication, le juridique, et les métiers. Elle traite les aspects stratégiques, réputationnels, réglementaires et financiers de l'incident. L'IR est la composante technique de la gestion de crise.

Les deux doivent fonctionner en parallèle et se nourrir mutuellement, mais ce ne sont pas les mêmes compétences, les mêmes temporalités, ni les mêmes interlocuteurs. L'analyste forensic qui explique la structure des Event IDs Windows au CEO perd son temps et celui du CEO. Le CEO qui intervient dans les décisions de confinement technique prend des risques qu'il ne mesure pas. L'articulation entre la cellule technique (IR) et la cellule de crise exécutive est un enjeu majeur traité au Ch.3 (seuils de bascule) et en Partie VII (gestion de crise).

#### 2.4 Le rôle d'orchestration de l'IR lead

L'IR lead n'est pas nécessairement le meilleur forensicien de l'équipe, ni le meilleur analyste réseau, ni le meilleur spécialiste AD. Il est celui qui maintient la vision d'ensemble de l'incident, coordonne les experts en leur assignant des questions précises, arbitre les priorités quand les ressources sont limitées (et elles le sont toujours), fait l'interface entre le monde technique et le monde décisionnel (traduire « le krbtgt est compromis » en « l'attaquant contrôle potentiellement l'ensemble de notre infrastructure — c'est un incident majeur »), et documente les décisions et leurs justifications.

C'est un chef d'orchestre, pas un soliste. Sa valeur ne réside pas dans sa capacité à analyser un dump mémoire (il a des analystes pour ça) mais dans sa capacité à poser les bonnes questions, à prioriser les efforts, et à maintenir la cohérence de la réponse quand 15 personnes travaillent en parallèle sur des aspects différents de l'incident.

#### 2.5 La logique fondamentale : temps court, forte incertitude, conséquences élevées

L'IR opère dans un régime de décision radicalement différent de la sécurité « temps de paix ». En temps de paix, une décision de sécurité (déployer un EDR, durcir l'AD, segmenter le réseau) peut être étudiée pendant des semaines, testée en environnement de pré-production, et déployée progressivement. En temps d'incident, les décisions doivent être prises en heures (parfois en minutes), avec des informations partielles et évolutives.

Les conséquences d'une mauvaise décision sont immédiates et parfois irréversibles. Isoler un serveur de production arrête la production. Redémarrer un serveur sans collecte forensic détruit la mémoire vive. Communiquer publiquement trop tôt peut être contredit par les faits. Ne pas contenir assez vite laisse l'attaquant progresser. Chaque décision est un arbitrage entre des risques concurrents, et cet arbitrage se fait sous pression, avec de la fatigue, et souvent au milieu de la nuit.

Cette pression n'est pas un accident — c'est la nature même de l'IR. La capacité à décider sous incertitude, à accepter le risque résiduel de chaque décision, et à documenter le raisonnement qui a conduit à cette décision (pour le retex et pour la protection juridique des décideurs) est la compétence fondamentale de l'IR lead. Le Ch.26 est entièrement dédié à cette dimension.

#### 2.6 Fil rouge — BLACKTIDE : l'organisation de la réponse

> **🔍 BLACKTIDE — Épisode 2**
>
> 22h45. Karim appelle Nadia Moreau, IR lead d'Arvantis. Elle décroche immédiatement — elle était d'astreinte ce week-end.
>
> Nadia pose les questions de cadrage en 5 minutes : « Qu'est-ce qu'on voit ? » (PsExec + GPO Defender sur DC01). « Depuis quand ? » (l'alerte EDR date de 22h17, mais on ne sait pas depuis quand l'attaquant est dans le réseau). « Combien de systèmes ? » (DC01 confirmé, à vérifier sur les autres DC). « L'attaquant est-il toujours actif ? » (probablement — l'exécution est récente). « Est-ce qu'on a touché à quelque chose ? » (non, Karim n'a fait qu'observer).
>
> Nadia active le protocole de réponse :
> - Ouverture du canal Signal « IR-BLACKTIDE » (canal pré-configuré, hors SI d'entreprise — le SI interne n'est plus de confiance).
> - Appel au RSSI, Marc Delaunay (réveillé, répond en 2 sonneries — il était en astreinte).
> - Appel au prestataire PRIS sous contrat, CyberForce (SLA : intervention dans les 12h le week-end — arrivée estimée samedi 8h).
> - Message aux analystes SOC N2 disponibles : « surveillance renforcée immédiate sur tous les DC, recherche de PsExec et de modifications GPO sur le parc. »
>
> Première tension : le responsable astreinte IT, David Lemaire, est réveillé par les alertes et propose de « patcher et redémarrer DC01 pour stopper l'attaque ». Nadia l'arrête fermement : « Pas de redémarrage. Pas de modification. On ne touche à rien tant qu'on n'a pas compris ce qui se passe et collecté les preuves. La mémoire de DC01 contient peut-être les clés de l'investigation. » David accepte, mais avec réticence — il sent que « quelque chose de grave est en train de se passer » et son réflexe d'admin est de « réparer ».

---

### Chapitre 3 — Incident technique, incident majeur, crise cyber : les seuils de bascule

#### 3.1 Pourquoi cette distinction est critique

En pratique, la confusion entre « incident gérable par l'équipe technique » et « crise nécessitant une gouvernance exécutive » est une source majeure de dysfonctionnement. Deux erreurs symétriques menacent.

La **sous-escalade** : traiter une crise comme un incident technique ordinaire. L'équipe IT essaie de « gérer en interne » un ransomware qui a chiffré 200 serveurs, sans informer la direction, sans mobiliser le juridique, sans notifier l'ANSSI. Les conséquences : perte de temps critique, non-respect des obligations légales, décisions techniques prises sans validation stratégique, et découverte tardive de l'ampleur réelle — souvent quand l'attaquant publie les données sur son leak site et que la presse appelle.

La **sur-escalade** : déclencher la cellule de crise pour un incident mineur. Un phishing bloqué par le filtre email, un malware isolé sur un poste sans données sensibles, une tentative de brute force bloquée par le WAF. La sur-escalade crée de la panique inutile, use la crédibilité de l'équipe sécurité auprès de la direction (« ils crient au loup tout le temps »), et gaspille des ressources qui seraient mieux employées ailleurs.

La capacité à calibrer correctement l'escalade — ni trop, ni trop peu — est une compétence clé de l'IR lead. Elle repose sur des critères objectifs, pas sur l'intuition.

#### 3.2 Critères de bascule en incident majeur

Un incident technique standard bascule en **incident majeur** quand au moins un des critères suivants est vérifié : compromission de l'Active Directory (contrôleur de domaine, compte krbtgt, Golden Ticket — la perte de contrôle de l'AD signifie la perte de contrôle de l'ensemble du SI Windows), chiffrement ou destruction de données à grande échelle (le ransomware a touché plus de quelques postes isolés), exfiltration de données sensibles confirmée (propriété intellectuelle, données personnelles, secrets industriels), impact sur un site OIV ou une infrastructure critique (obligations légales spécifiques), atteinte au réseau OT/ICS (risque physique potentiel), compromission du système de sauvegarde (la dernière ligne de défense est tombée), ou indisponibilité d'un service critique métier (production, facturation, logistique).

L'incident majeur déclenche une mobilisation renforcée : le prestataire PRIS est appelé si pas encore mobilisé, le RSSI prend le relais de la coordination, et un point de situation régulier est établi avec la direction technique.

#### 3.3 Critères de bascule en crise cyber

Un incident majeur bascule en **crise cyber** quand l'impact dépasse la sphère technique et touche le fonctionnement de l'organisation dans ses dimensions business, réputationnelle, réglementaire ou stratégique.

Les critères de bascule incluent un impact business significatif (production arrêtée, perte de chiffre d'affaires mesurable, clients impactés), une exposition médiatique (revendication sur un leak site, article de presse, tendance sur les réseaux sociaux), un impact réglementaire (notification CNIL obligatoire, notification ANSSI en tant qu'OIV/OSE, enquête réglementaire potentielle), une demande d'extorsion (la rançon est un élément de crise par nature — elle implique des décisions stratégiques, juridiques et éthiques), une atteinte à la sécurité physique (compromission de systèmes OT/SCADA dans un environnement industriel à risque), ou un dépassement de la capacité de réponse technique (l'équipe IR est submergée, l'incident évolue plus vite que la capacité d'analyse).

#### 3.4 Gouvernance technique vs gouvernance exécutive

L'activation de la crise crée deux niveaux de gouvernance qui doivent fonctionner en parallèle sans se mélanger.

La **cellule technique** est pilotée par l'IR lead. Elle comprend les analystes forensic, les analystes logs/réseau, l'analyste CTI, les administrateurs systèmes et réseaux, et le prestataire PRIS. Elle gère l'investigation technique, les actions de confinement et d'éradication, la collecte de preuves, et la production des IoC. Elle travaille en heures et en minutes.

La **cellule de crise exécutive** est pilotée par le DG ou son représentant mandaté. Elle comprend le RSSI (interface entre les deux cellules), le directeur juridique, le directeur de la communication, le DRH, le DPO, le directeur des opérations/métiers, et le DSI. Elle gère les décisions stratégiques (couper ou ne pas couper la production, payer ou ne pas payer la rançon), la communication (interne et externe), le juridique (notifications réglementaires, dépôt de plainte), et l'allocation de ressources.

Les deux cellules communiquent via des SitRep (Situation Reports) réguliers — toutes les 4 à 6 heures en phase aiguë, 1 à 2 fois par jour en phase de stabilisation. Le RSSI est la charnière entre les deux : il traduit la situation technique en termes compréhensibles par la direction, et il répercute les décisions stratégiques vers la cellule technique. Quand cette articulation fonctionne, la réponse est fluide. Quand elle dysfonctionne (le DG veut comprendre les Event IDs, l'analyste forensic conteste la décision de communication), la réponse patine.

#### 3.5 Temporalités divergentes et objectifs parfois contradictoires

La cellule technique et la cellule exécutive ne travaillent pas dans le même temps, et leurs objectifs peuvent temporairement diverger.

La technique veut **comprendre avant d'agir**. L'idéal technique serait de cartographier complètement la compromission, d'identifier tous les mécanismes de persistance, et de planifier une éradication chirurgicale — ce qui peut prendre des jours. Observer l'attaquant sans l'alerter (pour comprendre l'étendue complète) est parfois plus productif que le confiner immédiatement.

Le business veut **agir avant de comprendre**. La direction veut redémarrer la production, rassurer les clients, communiquer que « tout est sous contrôle ». Chaque jour d'arrêt coûte des centaines de milliers d'euros, les clients menacent de partir, et le conseil d'administration demande des comptes.

L'arbitrage entre ces temporalités n'est pas technique — il est stratégique. Il appartient à la direction, informée par l'équipe technique. Le rôle de l'IR lead est de formuler des options claires avec leurs risques respectifs (voir Ch.26 — Décider sous incertitude), pas de prendre seul la décision.

> **Bonne pratique :** Quand les objectifs divergent, la question arbitrale est : « Quelle décision serions-nous le plus en difficulté de défendre a posteriori si elle s'avérait mauvaise ? » Redémarrer trop vite et être réinfecté est plus difficile à défendre que mettre 2 jours de plus à reprendre la production. Cette asymétrie des regrets guide la prise de décision.

#### 3.6 Fil rouge — BLACKTIDE : la bascule en crise

> **🔍 BLACKTIDE — Épisode 3**
>
> Samedi 15 mars, 02h00. L'investigation initiale progresse. En 3 heures, l'équipe a établi :
> - DC01, DC02 et DC03 montrent des traces de PsExec et de modification GPO.
> - Le ransomware PhantomCrypt est en cours de déploiement via GPO — les serveurs de fichiers de 3 sites commencent à chiffrer.
> - Le trafic sortant vers le domaine C2 `update-srv-infra[.]xyz` est identifié (corrélation avec le cours Cartographie des Écosystèmes — c'est le même domaine).
> - Le volume d'exfiltration est inconnu mais des flux suspects vers AWS S3 sont repérés dans les logs proxy.
>
> Nadia évalue : ce n'est plus un incident P2. C'est un incident P1 avec probable bascule en crise. Elle appelle Marc (RSSI) à 02h15 :
>
> « Marc, on a une compromission des 3 DC, un ransomware en cours de déploiement sur les serveurs de fichiers de Fos, Lyon et Cologne, et une exfiltration probable vers un serveur externe. Le site OIV est touché. Je recommande la bascule en crise. »
>
> Marc active la cellule de crise exécutive pour 06h00 le samedi matin. Les deux gouvernances — technique et exécutive — sont désormais actives en parallèle.
>
> À 02h30, Nadia produit le premier SitRep :
>
> **SITREP #1 — BLACKTIDE — 15/03/2026 02h30**
> - **Ce qu'on sait :** 3 DC compromis, ransomware en cours de déploiement (3 sites touchés dont OIV Fos), trafic C2 identifié.
> - **Ce qu'on ne sait pas :** Étendue complète de la compromission. Volume de données exfiltrées. Identité de l'attaquant. Durée de présence dans le réseau.
> - **Ce qu'on fait :** Investigation en cours. Surveillance renforcée. Préparation des options de confinement.
> - **Ce qu'on envisage :** Confinement réseau des 3 sites impactés. Mobilisation PRIS. Notification ANSSI.
> - **Ce dont on a besoin :** Décision de confinement (impact production). Autorisation de notification ANSSI. Confirmation de la mobilisation du prestataire PRIS.

---

### Chapitre 4 — Référentiels, modèles et cadres méthodologiques

#### 4.1 NIST SP 800-61 — le cadre de référence international

Le NIST Special Publication 800-61 (Computer Security Incident Handling Guide), publié par le National Institute of Standards and Technology américain, est le cadre de référence le plus largement adopté pour structurer la réponse à incident. Sa dernière révision majeure (Rev. 2) organise l'IR en quatre phases.

La **phase 1 — Preparation** couvre tout ce qui doit être en place avant l'incident : équipe, outils, processus, formation, exercices. Le NIST insiste sur le fait que la qualité de la réponse est directement proportionnelle à la qualité de la préparation — un constat que la Partie II de ce cours développe en 6 chapitres.

La **phase 2 — Detection & Analysis** couvre la détection de l'incident, sa confirmation, sa classification, sa notification aux parties prenantes, et l'analyse initiale. Le NIST distingue les vecteurs d'attaque (email, web, media amovible, attrition, etc.) et fournit des indicateurs de classification.

La **phase 3 — Containment, Eradication & Recovery** regroupe trois activités que d'autres cadres séparent. Le confinement stoppe la progression de l'attaquant. L'éradication supprime les mécanismes de compromission. La récupération restaure les systèmes à un état sûr. Le NIST reconnaît que ces trois activités sont souvent itératives et parallèles.

La **phase 4 — Post-Incident Activity** couvre le retour d'expérience, la capitalisation, et l'amélioration continue.

**Forces du NIST 800-61 :** structurant, adopté mondialement, applicable à toutes tailles d'organisation, régulièrement mis à jour. **Limites :** très conceptuel (peu de détails techniques opérationnels), centré contexte américain (les obligations réglementaires européennes ne sont pas couvertes), et pas de traitement explicite de la dimension « crise » (la gouvernance exécutive, la communication de crise, et la pression médiatique ne sont pas dans le périmètre du document).

#### 4.2 SANS PICERL — les 6 phases

Le modèle SANS (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned) est plus granulaire que le NIST sur la distinction entre Containment, Eradication et Recovery — trois phases que le NIST regroupe. Cette granularité est utile pédagogiquement et opérationnellement : les trois phases mobilisent des compétences, des outils, et des temporalités différentes.

Le modèle SANS est la base des formations SANS les plus reconnues en IR : FOR508 (Advanced Incident Response, Threat Hunting, and Digital Forensics), FOR500 (Windows Forensic Analysis), et FOR578 (Cyber Threat Intelligence). Il est profondément ancré dans la communauté des praticiens.

**Limite principale :** la linéarité implicite du modèle (P→I→C→E→R→L) ne reflète pas la réalité itérative de l'IR. En pratique, on revient constamment en arrière : on identifie de nouveaux systèmes compromis pendant l'éradication (retour à l'identification), on découvre de nouvelles persistances pendant la recovery (retour à l'éradication), et les lessons learned commencent dès les premières heures de l'incident (pas seulement après la clôture).

#### 4.3 ISO 27035 — le cadre normatif

La norme ISO 27035 (Information Security Incident Management), en trois parties, fournit un cadre formel pour la gestion des incidents dans un contexte de système de management de la sécurité de l'information (SMSI) conforme à ISO 27001. Elle est plus structurée sur la gouvernance et la documentation que les cadres NIST/SANS, mais moins technique.

ISO 27035 est pertinente pour les organisations certifiées ISO 27001 qui doivent intégrer la gestion des incidents dans leur SMSI, et pour les organisations qui ont besoin d'un cadre normatif reconnu pour justifier leur approche auprès d'auditeurs ou de régulateurs.

#### 4.4 Cadre ANSSI, CERT-FR et PRIS

Le cadre français de la réponse à incident s'articule autour de plusieurs composantes.

L'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information) est l'autorité nationale en matière de cybersécurité. Elle opère le **CERT-FR**, qui fournit un service de réponse aux incidents pour les administrations et les OIV, publie des avis de sécurité et des alertes, et coordonne la réponse aux incidents d'ampleur nationale. Le CERT-FR peut déployer des équipes spécialisées (notamment en environnement OT/SCADA) en appui des organisations victimes.

Le référentiel **PRIS** (Prestataires de Réponse aux Incidents de Sécurité) définit les exigences de qualification pour les prestataires d'IR. La version 3.2, publiée en octobre 2025, couvre désormais cinq activités qualifiables : recherche d'indicateurs de compromission, investigation numérique (forensic), analyse de codes malveillants, pilotage et coordination des investigations, et — nouveauté de la v3.2 — gestion de crise d'origine cyber. Cette dernière activité, ajoutée après un appel à commentaires terminé en mai 2025, permet à l'ANSSI de délivrer des qualifications attestant la capacité d'un prestataire à gérer la dimension crise (pas seulement la dimension technique) d'un incident cyber.

Les **obligations de notification** dans le cadre français sont multiples. Les OIV (Opérateurs d'Importance Vitale) doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels. La directive NIS 2, en cours de transposition en France via la « Loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité » (dite « Loi Résilience ») — adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, promulgation attendue début 2026 —, imposera des obligations de notification aux entités essentielles (notification initiale sous 24h, notification complète sous 72h) et aux entités importantes. Le périmètre est considérablement élargi par rapport à NIS 1 : environ 15 000 entités seront concernées en France, contre quelques centaines sous le régime actuel.

L'articulation avec les **forces de l'ordre** passe par le dépôt de plainte auprès du procureur de la République, qui peut être traité par l'OCLCTIC (Office Central de Lutte contre la Criminalité liée aux Technologies de l'Information et de la Communication), le C3N (Centre de lutte Contre les Criminalités Numériques, Gendarmerie), la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris), ou la JUNALCO (Juridiction Nationale de Lutte contre la Criminalité Organisée, parquet de Paris — section J3 cybercriminalité).

#### 4.5 Kill Chain, Diamond Model et ATT&CK comme outils d'investigation

Ces cadres ne sont pas des « modèles IR » au sens de NIST ou SANS — ce sont des outils que l'investigateur utilise pendant la réponse pour structurer ses observations et ses hypothèses.

La **Cyber Kill Chain** (Lockheed Martin) structure le raisonnement sur la progression de l'attaque en 7 étapes (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives). Elle est utile pour situer l'attaque dans son cycle de vie : si l'attaquant en est à « Actions on Objectives » (exfiltration, chiffrement), c'est qu'il a traversé toutes les étapes précédentes — et l'investigation doit les reconstituer.

Le **Diamond Model** (adversary, capability, infrastructure, victim) structure le raisonnement sur l'attribution et le contexte. Pour chaque événement de l'intrusion, l'analyste identifie l'adversaire (qui ?), la capacité utilisée (quel outil, quelle technique ?), l'infrastructure employée (quel C2, quel hébergement ?), et la victime ciblée (quel système, quelle donnée ?).

La **matrice MITRE ATT&CK** fournit un vocabulaire commun pour décrire les TTP (Tactics, Techniques, and Procedures) observées pendant l'investigation. Chaque étape du chemin d'attaque est mappée sur les tactiques ATT&CK (Initial Access, Execution, Persistence, etc.), ce qui normalise le rapport, facilite le partage avec la communauté, et oriente la remédiation (pour chaque technique utilisée : quelle détection ou quelle mesure préventive aurait pu la contrer ?).

#### 4.6 Intérêt et limites des modèles

Aucun modèle ne reflète fidèlement la réalité d'un incident majeur. Les phases ne sont pas séquentielles mais itératives et parallèles : on contient pendant qu'on investigue, on investigue pendant qu'on éradique, on découvre de nouveaux problèmes pendant la reconstruction. L'incident avance sur plusieurs fronts simultanément, et les « phases » des modèles sont des repères intellectuels pour structurer la pensée, pas des check-lists rigides à suivre dans l'ordre.

Le danger des modèles est de créer une illusion de contrôle linéaire. L'analyste qui pense « je suis en phase de Containment, donc je ne fais pas d'Eradication » se trompe — si une opportunité d'éradiquer se présente pendant le confinement (par exemple, un mécanisme de persistance trivial à supprimer), il serait absurde de ne pas la saisir sous prétexte que « ce n'est pas la bonne phase ».

Les modèles doivent être connus, intériorisés, puis adaptés au contexte. Ils sont des garde-fous contre l'oubli (« avons-nous pensé aux lessons learned ? ») et des outils de communication (« nous sommes en phase de Containment, voici ce que cela signifie »), pas des carcans.

#### 4.7 Fil rouge — BLACKTIDE : le cadre opérationnel

> **🔍 BLACKTIDE — Épisode 4**
>
> L'équipe IR d'Arvantis utilise le NIST 800-61 comme référence procédurale. L'IRP interne reprend les 4 phases NIST et les décline en actions concrètes. Le mapping ATT&CK est utilisé comme grille de lecture des TTP observées au fil de l'investigation — chaque technique identifiée est documentée avec son ID ATT&CK dans le journal d'incident.
>
> Le prestataire PRIS sous contrat, CyberForce, utilise son propre cadre méthodologique (basé sur SANS PICERL), compatible avec le cadre interne d'Arvantis. L'articulation a été définie contractuellement : CyberForce apporte l'expertise forensic et l'expérience d'incidents similaires, l'équipe interne apporte la connaissance du SI et du contexte métier. L'IR lead reste Nadia (interne) — le consultant senior de CyberForce est en support, pas en pilotage.
>
> L'ANSSI est notifiée à 08h00 (obligation OIV — site de Fos-sur-Mer). Le CERT-FR accuse réception et propose un appui : déploiement d'une équipe spécialisée OT pour auditer le réseau SCADA de Fos, prévu pour lundi.

---
