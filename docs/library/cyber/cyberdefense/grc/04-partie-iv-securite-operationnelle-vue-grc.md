---
title: Partie IV — Sécurité opérationnelle vue GRC
source: Cyber/05_Cyberdefense/GRC.md
note: GRC
up:
- - GRC
  - index.md
---

Elle couvre les dimensions de la sécurité opérationnelle qui relèvent du pilotage, de la gouvernance et de l'arbitrage, pas de l'opérationnel technique.*

---


### Chapitre 16 — Gestion des identités et des accès vue GRC

Les principes de gouvernance IAM : moindre privilège (ne donner que les droits nécessaires à la fonction), séparation des devoirs (l'approbateur n'est pas l'exécutant), besoin d'en connaître (l'accès à une information est conditionné par la nécessité fonctionnelle). Les processus : provisioning (création du compte avec les droits associés au profil de poste — automatisé via l'annuaire RH si possible), deprovisioning (désactivation immédiate au départ — le délai entre le départ d'un employé et la désactivation de ses comptes est un indicateur de maturité), et revue des accès (trimestrielle pour les accès privilégiés, semestrielle pour les accès standards — avec CR signé par le propriétaire des données, pas par l'IT). La gestion des comptes privilégiés (PAM — coffre-fort de mots de passe, enregistrement des sessions admin, rotation automatique des mots de passe de service). La politique de MFA (quels comptes : tous les admins + tous les accès distants + les utilisateurs avec accès aux données sensibles ; quels types : résistant au phishing pour les admins — FIDO2/clés physiques, push/TOTP pour les utilisateurs standard). La politique de mots de passe (longueur > complexité — NIST recommande 12+ caractères sans rotation obligatoire, gestionnaire de mots de passe, interdiction de réutilisation).

---


### Chapitre 17 — Sensibilisation

construire un programme qui change les comportements

La sensibilisation n'est pas « envoyer un PowerPoint une fois par an ». C'est un programme continu qui vise le changement de comportement — le facteur humain est le vecteur d'accès initial n°1 (phishing). Les composantes d'un programme efficace : **formation à l'intégration** (onboarding sécurité — 30 min, obligatoire, signée, focus sur les 5 règles essentielles), **phishing simulé** (campagnes mensuelles, métriques par département, coaching individuel pour les récidivistes — pas de punition, de l'accompagnement, sinon les utilisateurs arrêtent de signaler), **formations thématiques par rôle** (développeurs → AppSec, RH → données personnelles, voyageurs → sécurité des déplacements, direction → ingénierie sociale et fraude au président), **micro-learning** (5 min/mois — vidéos courtes, quiz, rappels — maintenir la sécurité dans le radar), et **communication continue** (affiches, newsletter sécurité, alertes — exemples concrets, pas de jargon).

Les métriques : taux de clic phishing (par département et dans le temps — l'objectif n'est pas 0 % mais une tendance à la baisse), taux de signalement (les utilisateurs qui reportent les emails suspects au SOC — aussi important que le taux de clic, car un utilisateur qui signale permet la détection précoce), complétion des formations, et nombre d'incidents signalés par les utilisateurs. L'objectif : que le taux de clic baisse ET que le taux de signalement augmente.

---


### Chapitre 18 — Pilotage du changement, des vulnérabilités et du patching

*Ce chapitre reste à l'angle pilotage GRC — politique, SLA, arbitrage, exceptions, gouvernance. Les détails techniques (scan de vulnérabilités, outils, requêtes) sont dans les cours SOC (Ch.32 VOC) et CTI (Ch.21 vuln intel).*

Le **change management** vu GRC : tout changement sur le SI passe par un processus de validation (demande → analyse d'impact sécurité → approbation → implémentation → vérification post-changement). L'arbitrage sécurité : chaque changement est évalué pour son impact sur les risques (« ce changement ouvre-t-il une vulnérabilité ? nécessite-t-il une mise à jour de l'analyse de risques ? affecte-t-il l'homologation ? »). Les changements d'urgence (le patch critique à 2h du matin — procédure accélérée mais documentée a posteriori).

La **politique de patching** : SLA par criticité (critique < 48h, élevé < 15 jours, moyen < 30 jours, faible trimestriel), exceptions documentées (le système legacy qui ne peut pas être patché → compensatoire : segmentation + monitoring), et le suivi (% de conformité au SLA par mois — indicateur du Ch.9). L'articulation avec la CTI et le VOC : les vulnérabilités exploitées in the wild (CISA KEV, EPSS — cf. cours CTI Ch.21 et cours SOC Ch.32) sont prioritaires indépendamment du CVSS.

L'**assurance cyber vue pilotage** : les prérequis des assureurs sont devenus un socle de sécurité de fait (MFA, EDR, sauvegardes immutables, plan IR, segmentation). Le questionnaire assureur est un mini-audit qui révèle les gaps. L'assurance couvre le risque résiduel après réduction — ce n'est pas un substitut aux contrôles.

---
#### **Chapitre 19 — Référentiels vulnérabilités utiles à la gouvernance : CVE, CWE, CVSS, EPSS, KEV**

_Avant de définir une politique de gestion des vulnérabilités, il faut parler le même langage. Ce chapitre pose les référentiels que la gouvernance utilise pour qualifier, prioriser, tracer et justifier les décisions. L’objectif n’est pas d’entrer dans la technique d’exploitation, mais de comprendre ce que chaque indicateur apporte — et ce qu’il n’apporte pas — dans une logique de pilotage, de conformité et d’auditabilité._

---


## **19.1 Pourquoi la gouvernance a besoin de ces référentiels**


### Idée directrice

En GRC, le problème n’est pas seulement de “connaître les sigles”, mais de **disposer d’un vocabulaire commun** entre :

- RSSI,
- vulnerability manager,
- SOC,
- équipes infra / patching,
- auditeurs,
- direction.


### Ce que tu peux développer

- Les dashboards, rapports d’audit, tickets de remédiation, bulletins CTI et scans de vulnérabilités utilisent tous ces référentiels.
- Sans cadre commun, les arbitrages deviennent incohérents :
    - un CVSS élevé est pris comme une urgence absolue sans contexte ;
    - une CVE en KEV n’est pas traitée plus vite qu’une autre ;
    - EPSS est mal compris comme une preuve d’exploitation ;
    - la direction reçoit des chiffres sans lecture décisionnelle.
- La gouvernance a besoin de ces référentiels pour transformer des données techniques en **décisions traçables et défendables**.


### Message clé

**La GRC n’utilise pas ces référentiels pour faire de la technique ; elle les utilise pour encadrer la décision.**

---


## **19.2 CVE — l’identifiant de référence**


### Objectif

Présenter la CVE comme la **clé d’identification et de traçabilité**.


### À couvrir

- Une **CVE** est un identifiant unique associé à une vulnérabilité connue.
- Elle permet de relier :
    - bulletin éditeur,
    - scanner de vulnérabilités,
    - CTI,
    - ticket de remédiation,
    - exception,
    - audit,
    - incident éventuel.


### Angle GRC

- La CVE sert de **référence commune** dans les processus.
- C’est l’identifiant à conserver dans :
    - les rapports de vulnérabilités,
    - les décisions de traitement,
    - les exceptions,
    - les preuves d’audit,
    - les comptes rendus de comité.


### Message clé

**La CVE permet de parler exactement du même sujet dans toute la chaîne de gouvernance.**

---


## **19.3 CWE — la faiblesse sous-jacente et l’intérêt pour l’amélioration structurelle**


### Objectif

Montrer que la CWE est utile en GRC non pour l’investigation fine, mais pour la **lecture structurelle des causes**.


### À couvrir

- Une **CWE** décrit une catégorie de faiblesse :
    - contrôle d’accès insuffisant,
    - injection,
    - mauvaise validation d’entrée,
    - erreurs mémoire,
    - désérialisation, etc.
- Différence avec CVE :
    - **CVE** = vulnérabilité précise ;
    - **CWE** = famille de faiblesse.


### Angle GRC

- Très utile pour détecter des tendances :
    - plusieurs CVE sur une même famille de produits peuvent pointer vers la même faiblesse ;
    - plusieurs audits peuvent révéler un défaut systémique de développement, de configuration ou d’architecture.
- Intérêt pour :
    - plans d’action structurels,
    - secure by design,
    - exigences fournisseurs,
    - politique de développement sécurisé,
    - priorisation des efforts de remédiation à moyen terme.


### Message clé

**La CVE aide à traiter un cas ; la CWE aide à corriger une cause récurrente.**

---


## **19.4 CVSS — mesurer la sévérité technique d’une vulnérabilité**


### Objectif

Introduire CVSS comme **score de sévérité**, pas comme décision finale.


### À couvrir

- Le **CVSS** est le référentiel de sévérité le plus utilisé pour exprimer la criticité technique d’une vulnérabilité.
- Expliquer simplement ce qu’il cherche à mesurer :
    - facilité d’exploitation,
    - conditions d’exploitation,
    - impact potentiel sur confidentialité, intégrité, disponibilité.
- Préciser qu’un score CVSS :
    - aide à comparer,
    - aide à prioriser,
    - mais ne suffit jamais seul.


### Angle GRC

- Le score CVSS est un **point de départ**, utile pour :
    - les dashboards,
    - la priorisation initiale,
    - la communication entre équipes,
    - la définition de seuils de rescoring.
- Mais la gouvernance doit explicitement empêcher une lecture naïve du type :
    - “9.8 = toujours urgence absolue”,
    - “5.5 = toujours secondaire”.

Ton cours actuel dit déjà bien que le **score Base brut** est générique et que la gouvernance doit le transformer en score actionnable. Ce nouveau chapitre vient donc préparer naturellement l’actuel chapitre suivant.


### Message clé

**CVSS donne une sévérité technique de référence ; la gouvernance décide ensuite comment l’utiliser.**

---


## **19.5 EPSS — introduire la probabilité d’exploitation dans la décision**


### Objectif

Faire comprendre pourquoi EPSS complète CVSS dans une logique de pilotage.


### À couvrir

- **EPSS** estime la probabilité qu’une vulnérabilité soit exploitée dans un horizon proche.
- Il ne mesure pas la sévérité technique, mais la **pression d’exploitation probable**.
- Deux CVE proches en CVSS peuvent avoir des profils EPSS très différents.


### Angle GRC

- EPSS est utile pour :
    - enrichir les règles de priorisation,
    - arbitrer entre plusieurs remédiations concurrentes,
    - alimenter les comités de sécurité,
    - justifier une accélération de traitement.
- Important de préciser :
    - EPSS n’est pas une preuve d’exploitation ;
    - c’est un **facteur de priorisation** parmi d’autres.

Ton chapitre 18 mentionne déjà que les vulnérabilités exploitées in the wild et les signaux de menace doivent être prioritaires indépendamment du CVSS ; ce chapitre 19 permet justement d’expliquer pourquoi.


### Message clé

**CVSS dit “c’est grave techniquement”, EPSS aide à dire “ça risque d’être exploité bientôt”.**

---


## **19.6 KEV — quand la menace n’est plus théorique**


### Objectif

Donner à KEV sa place de signal fort de gouvernance.


### À couvrir

- Le **KEV** recense les vulnérabilités connues comme exploitées dans le monde réel.
- Là, on ne parle plus de potentiel, mais d’**exploitation observée**.


### Angle GRC

- La présence en KEV change la posture de gouvernance :
    - raccourcissement des SLA,
    - priorisation au comité,
    - demande de suivi renforcé,
    - revue immédiate des actifs exposés,
    - potentiellement note d’alerte RSSI / DSI / COMEX selon le contexte.
- C’est un marqueur fort de **proportionnalité** et de **diligence** dans un contexte audit/conformité.

Ton cours actuel le mobilise déjà dans la logique de rescoring et d’Exploit Maturity ; ici on le pose explicitement en amont comme brique de gouvernance.


### Message clé

**KEV transforme une vulnérabilité théorique en sujet de gouvernance prioritaire.**

---


## **19.7 Bien distinguer les rôles de chaque référentiel**


### Objectif

Faire une sous-partie de synthèse très claire.


### Tableau conseillé

|Référentiel|Ce qu’il dit|Ce qu’il ne dit pas|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on|Si elle est grave ou exploitée|
|**CWE**|Quelle faiblesse est en cause|Si un système précis est compromis|
|**CVSS**|Quelle est la sévérité technique|Quelle priorité absolue retenir chez nous|
|**EPSS**|Quelle est la probabilité d’exploitation|Si la vulnérabilité est déjà exploitée chez nous|
|**KEV**|Qu’elle est exploitée dans le réel|Quel est le niveau de risque précis dans notre SI|


### Message clé

**Aucun de ces référentiels, pris seul, ne suffit à décider. Leur valeur est dans leur combinaison.**

---


## **19.8 Ce que la gouvernance doit en faire concrètement**


### Objectif

Raccorder immédiatement ce chapitre au suivant.


### À couvrir

La gouvernance doit définir :

- quels référentiels sont retenus officiellement ;
- quelles sources sont considérées comme de référence ;
- qui lit quoi et à quel moment ;
- comment les scores et signaux alimentent :
    - la priorisation,
    - les SLA,
    - les exceptions,
    - la traçabilité,
    - les revues de risque,
    - les audits.


### Pont avec le chapitre suivant

Cette sous-partie doit préparer explicitement le futur **chapitre 20 — Politique de gestion des vulnérabilités : du score brut au score contextualisé**, qui expliquera déjà :

- le problème du score Base brut ;
- CVSS v4 et ses groupes Base / Threat / Environmental / Supplemental ;
- les rôles de requalification ;
- les SLA par score contextualisé ;
- la documentation et l’articulation avec ISO 27001, EBIOS RM et NIS2.


### Message clé

**Ce chapitre pose le vocabulaire ; le suivant posera les règles de décision.**

---


## **19.9 Fil rouge — COMPLIANCE

lecture gouvernance d’une vulnérabilité**

Je te conseille une petite sous-partie narrative, comme dans le reste du cours.


### Format possible

> **📊 COMPLIANCE — Épisode X**  
> Marine reçoit un rapport de scan mentionnant plusieurs CVE “critiques” sur des serveurs exposés et internes. Avant de demander une remédiation générale en urgence, elle fait clarifier les éléments de lecture : quelles CVE sont réellement concernées, quelles faiblesses reviennent de manière récurrente, quelles vulnérabilités sont déjà connues comme exploitées, et lesquelles présentent une forte probabilité d’exploitation. Ce premier cadrage ne décide pas encore du SLA, mais il permet d’éviter deux erreurs classiques : traiter toutes les vulnérabilités comme équivalentes, ou s’appuyer sur le seul score brut sans tenir compte du contexte de menace.


### Intérêt

Ça colle bien au ton de ton fil rouge COMPLIANCE, où Marine structure la gouvernance progressivement dans une organisation immature.

---


## **19.10 Transition vers le chapitre 20**


### Phrase de transition possible

> Connaître les référentiels ne suffit cependant pas à piloter une gestion des vulnérabilités. La question décisive pour la gouvernance n’est pas seulement de savoir ce que signifie une CVE ou un score CVSS, mais de définir comment ces éléments seront utilisés dans l’organisation : qui peut requalifier, selon quelles règles, avec quels SLA, et avec quelle traçabilité. C’est l’objet du chapitre suivant.

---


## Structure finale recommandée

Je te conseille donc ce plan :

- **19.1 Pourquoi la gouvernance a besoin de ces référentiels**
- **19.2 CVE — l’identifiant de référence**
- **19.3 CWE — la faiblesse sous-jacente et l’intérêt pour l’amélioration structurelle**
- **19.4 CVSS — mesurer la sévérité technique d’une vulnérabilité**
- **19.5 EPSS — introduire la probabilité d’exploitation dans la décision**
- **19.6 KEV — quand la menace n’est plus théorique**
- **19.7 Bien distinguer les rôles de chaque référentiel**
- **19.8 Ce que la gouvernance doit en faire concrètement**
- **19.9 Fil rouge — COMPLIANCE : lecture gouvernance d’une vulnérabilité**
- **19.10 Transition vers le chapitre 20**
