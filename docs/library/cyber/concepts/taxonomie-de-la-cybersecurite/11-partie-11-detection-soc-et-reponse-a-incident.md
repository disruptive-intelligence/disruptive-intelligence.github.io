---
title: Partie 11 — Détection, SOC et réponse à incident
source: Cyber/11 Concepts/Cartes & familles/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

> Le SOC (Security Operations Center) et la réponse à incident incarnent la posture *assume breach* : puisque la prévention échouera un jour, il faut *voir* (détection) et *agir* (réponse). On suit ici le cycle de vie d'un incident, du signal brut au retour d'expérience. Cadre de référence : NIST CSF *Detect / Respond / Recover*, et le cycle de réponse à incident (préparation, détection/analyse, confinement/éradication/rétablissement, post-incident).


## Chapitre 245 — Événement, alerte, incident

**Définition.** Trois niveaux d'objets du SOC, à ne pas confondre.

- **Événement** : tout fait journalisé (une connexion, une requête). Neutre, massif.
- **Alerte** : un événement (ou une corrélation) jugé *suspect* par une règle/un modèle, qui mérite examen.
- **Incident** : une alerte *confirmée* comme atteinte (ou menace) réelle à la sécurité, qui déclenche la réponse.

**Principe.** Le SOC filtre un déluge d'événements → quelques alertes → encore moins d'incidents réels. La qualité du filtrage (réduire le bruit sans rater le signal) est l'enjeu central.

🧭 **Taxonomie** — Pipeline : événements (logs) → alertes (détection) → incidents (qualification) → réponse.

🎯 **À retenir** — Tout incident est un événement, mais l'immense majorité des événements ne sont pas des incidents. Le travail du SOC est ce tri.


## Chapitre 246 — Faux positif, vrai positif, faux négatif

**Définition.** Vocabulaire de la qualité de détection.

- **Vrai positif** : une alerte correspondant à une vraie menace (bonne détection).
- **Faux positif** : une alerte déclenchée à tort (bruit) — coûte du temps d'analyse.
- **Faux négatif** : une menace réelle *non* détectée (le plus dangereux) — angle mort.
- **Vrai négatif** : absence d'alerte sur une activité légitime (normal).

**Principe.** Il y a un arbitrage : durcir la détection réduit les faux négatifs mais augmente les faux positifs (et la fatigue d'alerte), et inversement. L'objectif est de maximiser les vrais positifs tout en maîtrisant le bruit.

⚠️ **Erreur fréquente** — Trop d'alertes (faux positifs) noient les analystes et masquent les vraies menaces (fatigue d'alerte). Le réglage fin (tuning) est continu.

🎯 **À retenir** — Le faux négatif est le plus dangereux (menace ratée) ; le faux positif use les équipes. Le réglage des détections arbitre constamment entre les deux.


## Chapitre 247 — IOC, IOA, TTP

**Définition.** Trois niveaux d'indicateurs de menace, par ordre de valeur croissante.

- **IOC (Indicator of Compromise)** : trace technique d'une compromission (adresse, condensat de fichier, domaine malveillant). Concret mais *éphémère* (l'attaquant change facilement).
- **IOA (Indicator of Attack)** : signe d'un *comportement* d'attaque en cours (séquence d'actions), indépendant des artefacts précis.
- **TTP (Tactics, Techniques, Procedures)** : les *méthodes* de l'attaquant (le « comment » durable), formalisées par MITRE ATT&CK. Le plus stable et le plus précieux.

**Principe : la « pyramide de la douleur ».** Bloquer un IOC gêne peu l'attaquant (il le change) ; détecter ses TTP l'oblige à changer ses méthodes — bien plus coûteux pour lui.

🧭 **Taxonomie** — IOC (artefact) < IOA (comportement) < TTP (méthode). La détection mûre vise les TTP (ATT&CK).

🎯 **À retenir** — Détecter au niveau TTP (comportements/méthodes) fait bien plus mal à l'attaquant que bloquer des IOC volatils.


## Chapitre 248 — Log source

**Définition.** Toute origine de journaux alimentant la détection (postes, serveurs, réseau, applications, cloud, identité, EDR).

**Principe.** La détection ne vaut que par ses *sources* : sans les bons journaux (authentification, processus, réseau, cloud), des pans entiers d'attaque restent invisibles. Le choix et la couverture des sources déterminent ce que le SOC peut voir. Notions : complétude, fiabilité, horodatage synchronisé, centralisation.

🧭 **Taxonomie** — Matière première de la Partie 11 ; relie journalisation (chapitre 26) et logging insuffisant (chapitre 78).

🎯 **À retenir** — Pas de bonne source, pas de détection : la couverture des log sources est le socle du SOC.


## Chapitre 249 — SIEM

**Définition.** *Security Information and Event Management* : plateforme centralisant les journaux, les corrélant et générant des alertes.

**Principe.** Le SIEM agrège les sources, normalise, corrèle (relier des événements épars en un scénario), applique des règles de détection, et sert de base à l'investigation et au reporting. C'est le « cerveau » de corrélation du SOC.

🧭 **Taxonomie** — Cœur de la détection centralisée ; consomme les log sources, alimente le triage et l'investigation.

⚠️ **Erreur fréquente** — Déployer un SIEM sans sources pertinentes ni règles ajustées : un coûteux entrepôt de logs qui ne détecte rien.

🎯 **À retenir** — Le SIEM corrèle les sources pour transformer des événements épars en alertes exploitables — à condition d'être bien alimenté et réglé.


## Chapitre 250 — EDR

**Définition.** *Endpoint Detection and Response* : agent sur les postes/serveurs qui détecte les comportements malveillants et permet d'y répondre (isolation, investigation).

**Principe.** Au-delà de l'antivirus (signatures), l'EDR observe le *comportement* (processus, mémoire, actions) — clé contre le fileless, les LOLBins et les TTP. Il permet aussi des actions de réponse (isoler une machine, tuer un processus) et fournit la télémétrie pour l'investigation.

🧭 **Taxonomie** — Détection/réponse au niveau hôte ; complément du SIEM (vue centrale) et du NDR (vue réseau). Brique du XDR (corrélation multi-domaines).

🎯 **À retenir** — L'EDR voit le comportement sur l'hôte (pas seulement les fichiers) : indispensable contre les attaques furtives modernes.


## Chapitre 251 — NDR

**Définition.** *Network Detection and Response* : détection des menaces par l'analyse du *trafic réseau*.

**Principe.** Le NDR observe les flux (y compris est-ouest, internes) pour repérer scans, mouvement latéral, C2, exfiltration, tunneling — souvent invisibles côté hôte. Il complète l'EDR (qui peut être absent de certains équipements : IoT, OT).

🧭 **Taxonomie** — Détection au niveau réseau ; complément de l'EDR (hôte) et du SIEM (central). Particulièrement utile contre la Partie 7.

🎯 **À retenir** — Le NDR voit ce qui circule, y compris là où il n'y a pas d'agent (IoT/OT) : essentiel pour repérer mouvement latéral et exfiltration.


## Chapitre 252 — SOAR

**Définition.** *Security Orchestration, Automation and Response* : plateforme automatisant et orchestrant les tâches de réponse (playbooks).

**Principe.** Le SOAR enchaîne automatiquement des actions répétitives (enrichir une alerte, isoler une machine, bloquer un indicateur) selon des playbooks, réduisant le temps de réponse et la charge des analystes. Il orchestre les outils entre eux.

🧭 **Taxonomie** — Couche d'automatisation au-dessus du SIEM/EDR/NDR ; accélère le cycle détection→réponse.

⚠️ **Erreur fréquente** — Automatiser des réponses agressives sans garde-fous (risque d'auto-déni de service).

🎯 **À retenir** — Le SOAR automatise et orchestre la réponse : il démultiplie les analystes, à condition de playbooks sûrs et testés.


## Chapitre 253 — Cas d'usage SOC

**Définition.** Un *use case* est un scénario de menace concret que le SOC s'organise pour détecter (par ex. « tentative de password spraying », « exfiltration via DNS »).

**Principe.** On ne détecte pas « tout » : on définit des cas d'usage prioritaires (selon les menaces et les actifs), pour lesquels on identifie les sources, écrit les règles, et prépare la réponse. Les cas d'usage relient menace → détection → réaction. On les cartographie souvent sur ATT&CK pour mesurer la couverture.

🧭 **Taxonomie** — Unité de pilotage de la détection ; relie CTI (menaces), log sources, règles et playbooks.

🎯 **À retenir** — Le cas d'usage structure la détection autour de menaces concrètes : il évite le « tout détecter » illusoire et mesure la couverture.


## Chapitre 254 — Règle de détection

**Définition.** Logique (signature, corrélation, modèle) qui transforme des événements en alerte lorsqu'un schéma suspect apparaît.

**Principe.** Les règles vont de la signature simple (un indicateur connu) à la corrélation comportementale (séquence d'actions) et à l'analyse statistique/ML (anomalies). Elles doivent être *ajustées* (réduire faux positifs/négatifs) et *maintenues* (les menaces évoluent). Des formats partagés (par ex. règles ouvertes type Sigma/Yara) facilitent la mutualisation.

🧭 **Taxonomie** — Brique opérationnelle du cas d'usage ; vise idéalement le niveau TTP (chapitre 247).

🎯 **À retenir** — Une bonne règle détecte le comportement, pas seulement l'artefact, et se règle/maintient en continu.


## Chapitre 255 — Triage

**Définition.** Première étape de traitement d'une alerte : évaluer rapidement sa gravité et sa probabilité pour décider de la suite.

**Principe.** Face au volume d'alertes, le triage priorise : écarter le bruit évident, escalader le sérieux, enrichir (contexte, IOC, actif concerné). C'est le filtre d'entrée du processus de réponse.

🧭 **Taxonomie** — Première étape du cycle de réponse ; précède la qualification (chapitre 256).

🎯 **À retenir** — Le triage trie vite pour concentrer l'effort sur ce qui compte : il protège les analystes de la noyade.


## Chapitre 256 — Qualification

**Définition.** Analyse approfondie d'une alerte triée pour confirmer (ou infirmer) qu'il s'agit d'un incident, et en déterminer la nature/portée.

**Principe.** On rassemble le contexte (sources, télémétrie, IOC/IOA), on reconstitue ce qui se passe, et on décide : faux positif (clôture) ou incident (escalade et réponse). La qualification détermine la gravité et le périmètre initial.

🧭 **Taxonomie** — Transforme une alerte en incident qualifié ; précède l'escalade et le confinement.

🎯 **À retenir** — La qualification confirme la réalité et la portée de la menace : c'est la bascule alerte → incident.


## Chapitre 257 — Escalade

**Définition.** Transmission d'un incident qualifié au niveau/équipe approprié (analystes seniors, réponse à incident, gestion de crise) selon sa gravité.

**Principe.** Tout incident n'exige pas la même réponse ; l'escalade aiguille vers les bonnes compétences et déclenche, si besoin, la cellule de crise (chapitre 39). Des critères clairs (gravité, périmètre, impact) évitent les hésitations sous pression.

🧭 **Taxonomie** — Charnière entre détection (niveaux SOC) et réponse/gestion de crise.

🎯 **À retenir** — L'escalade met le bon niveau d'expertise sur le bon incident, au bon moment : des critères définis à froid l'objectivent.


## Chapitre 258 — Investigation

**Définition.** Analyse détaillée d'un incident pour comprendre *ce qui s'est passé* : vecteur d'entrée, actions, portée, persistance, données touchées.

**Principe.** L'investigation reconstitue le scénario d'attaque (souvent via ATT&CK), identifie tous les systèmes/compte touchés et les mécanismes de persistance — préalable indispensable à un confinement et une éradication *complets*. Elle s'appuie sur la télémétrie (EDR/NDR/SIEM) et le forensic (chapitre 263).

⚠️ **Erreur fréquente** — Réagir avant d'avoir compris la portée : on confine un symptôme en laissant des accès cachés.

🧭 **Taxonomie** — Sous-tend confinement, éradication et rétablissement ; alimente le post-mortem.

🎯 **À retenir** — Comprendre toute la portée *avant* d'agir évite une éradication incomplète et un retour de l'attaquant.


## Chapitre 259 — Containment (confinement)

**Définition.** Mesures pour *limiter la propagation* et l'impact d'un incident, sans nécessairement tout éradiquer immédiatement.

**Principe.** On isole les systèmes/comptes compromis (déconnexion réseau, désactivation de comptes, blocage de flux) pour stopper l'hémorragie. Confinement *court terme* (urgence) puis *long terme* (stabilisation). À équilibrer avec la préservation des preuves (forensic) et la continuité d'activité.

⚠️ **Erreur fréquente** — Confiner brutalement en détruisant les preuves, ou alerter l'attaquant trop tôt (qui accélère/détruit).

🧭 **Taxonomie** — Étape *Respond* ; précède l'éradication.

🎯 **À retenir** — Le confinement arrête la propagation ; il s'équilibre avec la préservation des preuves et la continuité.


## Chapitre 260 — Eradication

**Définition.** Suppression *complète* de la présence de l'attaquant : malwares, comptes/portes dérobées, mécanismes de persistance.

**Principe.** Sur la base d'une investigation complète, on élimine *tout* (pas seulement la charge visible) : backdoors, comptes créés, tâches, implants, secrets compromis (rotation, dont krbtgt si AD). Une éradication partielle = retour de l'attaquant.

⚠️ **Erreur fréquente** — Nettoyer le malware visible en laissant des accès de persistance (backdoor, shadow credentials, golden ticket).

🧭 **Taxonomie** — Étape *Respond* ; suit le confinement, précède le rétablissement.

🎯 **À retenir** — L'éradication doit être *exhaustive* (toute la persistance) sous peine de réinfection : d'où l'importance de l'investigation préalable.


## Chapitre 261 — Recovery (rétablissement)

**Définition.** Remise en service sécurisée des systèmes et données après éradication.

**Principe.** On restaure (sauvegardes saines), on durcit (corriger ce qui a permis l'intrusion), on surveille étroitement (l'attaquant peut tenter de revenir), et on rétablit progressivement l'activité. La restauration s'appuie sur des sauvegardes *vérifiées* (chapitre 28).

⚠️ **Erreur fréquente** — Restaurer à partir d'une sauvegarde elle-même compromise, ou rétablir sans corriger la faille initiale (réintrusion immédiate).

🧭 **Taxonomie** — Étape *Recover* ; relie sauvegarde/PRA (chapitres 28, 267).

🎯 **À retenir** — Le rétablissement remet en service *sainement* : sauvegardes vérifiées, correction de la cause, surveillance renforcée.


## Chapitre 262 — Lessons learned

**Définition.** Analyse rétrospective d'un incident pour en tirer des améliorations durables (techniques, processus, organisation).

**Principe.** Sans retour d'expérience, les mêmes incidents se répètent. On documente ce qui s'est passé, ce qui a bien/mal fonctionné, et on en tire des actions concrètes (nouvelles détections, correctifs, procédures, formation). C'est le moteur d'amélioration continue du SOC.

🧭 **Taxonomie** — Étape post-incident ; relie au post-mortem (chapitre 269) et boucle vers la préparation.

🎯 **À retenir** — Un incident non analysé est un incident à moitié subi : les lessons learned transforment la douleur en progrès.


## Chapitre 263 — Forensic

**Définition.** *Investigation numérique légale* : collecte, préservation et analyse rigoureuses de preuves numériques, exploitables y compris en justice.

**Principe.** Le forensic reconstitue les faits à partir d'artefacts (disques, mémoire, journaux) en garantissant l'*intégrité* et la *traçabilité* des preuves (chaîne de conservation — chapitre 265). Il sert l'investigation, l'attribution, et d'éventuelles suites légales/réglementaires.

🧭 **Taxonomie** — Appui de l'investigation (chapitre 258) ; exige rigueur de preuve (chapitres 264–265).

🎯 **À retenir** — Le forensic produit des preuves fiables et défendables : il impose rigueur et préservation de l'intégrité.


## Chapitre 264 — Timeline

**Définition.** Reconstitution chronologique des événements d'un incident (qui, quoi, quand, dans quel ordre).

**Principe.** La timeline relie les artefacts épars en un *récit* cohérent de l'attaque, du point d'entrée à l'impact. Elle exige des horodatages fiables et synchronisés (sinon les corrélations sont fausses). C'est l'épine dorsale de l'investigation et du forensic.

⚠️ **Erreur fréquente** — Horloges non synchronisées entre sources, rendant la chronologie incohérente.

🧭 **Taxonomie** — Outil central de l'investigation/forensic ; dépend de la qualité des log sources (horodatage).

🎯 **À retenir** — La timeline raconte l'attaque dans l'ordre : sans horodatage fiable et synchronisé, elle s'effondre.


## Chapitre 265 — Chaîne de conservation (chain of custody)

**Définition.** Traçabilité documentée de chaque preuve numérique : qui l'a collectée, manipulée, transférée, quand et comment.

**Principe.** Pour qu'une preuve soit recevable et crédible, on doit prouver qu'elle n'a pas été altérée depuis sa collecte. La chaîne de conservation documente chaque manipulation et garantit l'intégrité (empreintes, copies de travail, originaux préservés).

🧭 **Taxonomie** — Exigence du forensic (chapitre 263) ; condition de la valeur probante.

🎯 **À retenir** — Sans chaîne de conservation, une preuve perd sa valeur : documenter chaque manipulation est impératif.


## Chapitre 266 — Gestion de crise

**Définition.** Pilotage organisationnel d'un incident majeur (rappel du chapitre 39, côté opérationnel du SOC/IR).

**Principe.** Quand l'incident dépasse le SOC, la cellule de crise coordonne décisions, communication, continuité et aspects juridiques/réglementaires, sous pression. Elle s'appuie sur des rôles, des procédures et des canaux *préparés à froid* (et hors du SI potentiellement compromis).

🧭 **Taxonomie** — Niveau de pilotage au-dessus de la réponse technique ; relie PRA/PCA (chapitre 267) et communication (chapitre 268).

🎯 **À retenir** — La gestion de crise coordonne au-delà de la technique : préparée à l'avance, elle évite l'improvisation sous pression.


## Chapitre 267 — PRA / PCA

**Définition.**

- **PCA (Plan de Continuité d'Activité)** : maintenir les activités essentielles *pendant* la crise (avec des moyens dégradés/alternatifs).
- **PRA (Plan de Reprise d'Activité)** : *rétablir* les systèmes après le sinistre, dans des délais et avec des pertes de données maîtrisés.

**Notions clés.** **RTO** (durée de reprise visée) et **RPO** (perte de données acceptable) dimensionnent le dispositif. Le PRA repose sur des sauvegardes vérifiées (chapitre 28) et doit être *testé* régulièrement.

⚠️ **Erreur fréquente** — PRA jamais testé, RTO/RPO théoriques irréalistes le jour J.

🧭 **Taxonomie** — Résilience (chapitre 28) au niveau organisationnel ; pilier de la fonction *Recover*.

🎯 **À retenir** — PCA = tenir pendant ; PRA = se relever après. Tous deux doivent être chiffrés (RTO/RPO) et *testés*.


## Chapitre 268 — Communication de crise

**Définition.** Gestion des messages (internes, clients, partenaires, autorités, public) pendant et après un incident majeur.

**Principe.** Une mauvaise communication aggrave une crise (panique, perte de confiance, sanctions). Il faut des messages préparés, des porte-parole désignés, le respect des obligations de notification (réglementaires : violations de données, etc.), et une coordination avec le juridique. La transparence maîtrisée préserve la confiance.

⚠️ **Erreur fréquente** — Communiquer trop tôt/faux, ou via des canaux compromis ; ignorer les obligations légales de notification.

🧭 **Taxonomie** — Volet de la gestion de crise (chapitres 39, 266) ; à préparer à froid.

🎯 **À retenir** — La communication de crise se prépare à l'avance : messages, porte-parole, obligations de notification et canaux sûrs.


## Chapitre 269 — REX et amélioration continue

**Définition.** Le *retour d'expérience* (REX) et le post-mortem institutionnalisent l'apprentissage tiré des incidents (et des exercices).

**Principe.** Au-delà des « lessons learned » d'un incident, le REX nourrit un cycle d'amélioration continue : mise à jour des détections, des procédures, de l'architecture, de la formation. Idéalement *sans blâme* (blameless), pour favoriser l'honnêteté et l'apprentissage réel.

🧭 **Taxonomie** — Boucle de rétroaction reliant *Respond/Recover* à la préparation (*Govern/Identify/Protect/Detect*).

🎯 **À retenir** — La sécurité progresse par boucles d'apprentissage : un REX sans blâme transforme chaque incident en amélioration durable.

---
