---
title: PARTIE V — DÉFENSE ET CONTRE-INGÉNIERIE SOCIALE
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 5
chapters: 7
---

---

## Chapitre 21 — Sensibilisation : au-delà du e-learning annuel

### 21.1 Pourquoi la sensibilisation classique ne fonctionne pas

Les formations de sensibilisation e-learning annuelles — un module en ligne de 30 minutes suivi d'un quiz à choix multiples — ont un impact démontrablement limité sur le comportement réel des employés. Les études montrent que le taux de clic sur les campagnes de phishing diminue faiblement (5-10 %) après une formation e-learning et que cet effet s'estompe en quelques semaines.

Les raisons de cet échec sont identifiées. Le biais d'optimisme (« je sais maintenant, donc je ne me ferai pas piéger ») est renforcé par la réussite au quiz — l'employé a la preuve qu'il « connaît le phishing ». Le transfert d'apprentissage est faible : reconnaître un phishing dans un contexte d'examen (où on s'attend à un phishing) est radicalement différent de reconnaître un phishing dans le flux quotidien de 200 emails alors qu'on est pressé par un deadline. Et la formation traite le phishing comme un problème de connaissance (« si vous savez, vous ne cliquerez pas ») alors que c'est un problème de comportement en situation de charge cognitive (« même en sachant, vous cliquerez si les conditions sont réunies »).

### 21.2 Les formations qui fonctionnent

**Les simulations réalistes.** Les campagnes de phishing simulé (envoyées sans avertissement préalable, avec des leurres crédibles personnalisés) sont significativement plus efficaces que les formations théoriques. Le retour individualisé après le clic (« vous avez cliqué parce que l'email exploitait le mécanisme X — voici comment le détecter ») est l'élément pédagogique clé. Important : le retour doit être explicatif et bienveillant, jamais punitif.

**Les exercices de vishing.** Les simulations d'appels téléphoniques de social engineering (par le red team interne ou un prestataire) testent la résistance des employés au pretexting vocal — une compétence que les formations e-learning ne développent pas du tout.

**Les micro-formations ciblées.** Sessions courtes (15-20 min) sur un sujet spécifique, adaptées au profil de risque : BEC pour les DAF et la comptabilité, pretexting helpdesk pour l'IT support, tailgating pour la réception et la sécurité, élicitation pour les ingénieurs R&D et les dirigeants. La pertinence thématique augmente l'engagement et le transfert.

**Les exercices tabletop.** Scénarios d'incident de social engineering discutés en groupe (comité de direction, équipe de sécurité, service concerné) : « un employé reçoit cet appel — que fait-il ? que fait son manager ? que fait le SOC ? ». Les exercices tabletop développent les réflexes collectifs et identifient les failles de processus.

### 21.3 La formation par profil de risque

Tout le monde n'a pas besoin de la même formation. Les profils à risque doivent recevoir une formation spécifique adaptée aux menaces qui les ciblent.

| Profil | Menace principale | Formation prioritaire |
|---|---|---|
| DAF / Comptabilité | BEC, fraude au fournisseur | Processus de vérification, callback, double validation |
| Assistants de direction | Fraude au président, impersonation du dirigeant | Vérification des demandes urgentes, procédure de validation |
| Helpdesk / IT Support | Pretexting, reset de credentials, MFA manipulation | Procédures de vérification d'identité renforcées |
| Ingénieurs R&D | Élicitation, faux recruteurs, ingérence étrangère | Contre-élicitation, signaux d'alerte HUMINT, protection en conférence |
| Réception / Sécurité | Tailgating, impersonation, intrusion physique | Procédures de vérification des visiteurs, refus poli |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing VIP | Surface d'exposition personnelle, sécurité des communications |

### 21.4 Mesurer l'efficacité

Les métriques classiques (taux de clic sur le phishing simulé) sont nécessaires mais insuffisantes. Un programme de mesure complet inclut : le taux de clic (en baisse au fil des campagnes ?), le taux de signalement (en hausse ? — plus important que le taux de clic, car il mesure la culture de sécurité), le temps de signalement (les employés signalent-ils dans les minutes ou les heures ?), le taux de récidive (les employés qui ont cliqué une fois cliquent-ils encore ?), et les résultats qualitatifs des exercices de vishing et d'intrusion physique.

**Limite importante** : les métriques de phishing ne mesurent pas la résistance au vishing, à l'élicitation ou à l'intrusion physique. Un employé qui ne clique jamais sur les phishings simulés peut se faire piéger par un appel téléphonique convaincant ou une élicitation de face-à-face. La mesure doit être multi-vecteurs.

### 21.5 La culture de sécurité

La culture de sécurité est l'objectif final — au-delà de la formation et des processus, c'est l'environnement humain qui détermine la résilience d'une organisation face au social engineering.

Une culture de sécurité efficace se caractérise par : le signalement encouragé (signaler un email, un appel ou un comportement suspect est perçu comme un acte positif, jamais comme une perte de temps ou une preuve de paranoïa), la vérification normalisée (vérifier l'identité d'un interlocuteur, même s'il se présente comme un supérieur hiérarchique, est un acte professionnel, pas un acte de défiance), la transparence (les résultats des tests de social engineering sont partagés avec les employés — sans nommer les individus — pour démontrer la réalité de la menace), et le renforcement positif (les employés qui signalent sont remerciés publiquement, pas les employés qui « ne se font jamais piéger » — car ceux qui ne signalent jamais ne sont pas nécessairement plus vigilants, ils sont peut-être simplement moins exposés).

---

## Chapitre 22 — Contre-élicitation et protection des informations

### 22.1 Reconnaître une tentative d'élicitation

La détection d'une élicitation en cours est difficile précisément parce que l'élicitation est conçue pour ressembler à une conversation normale. Les signaux d'alerte sont subtils et contextuels.

**Questions inhabituellement spécifiques.** Une conversation de salon professionnel qui passe de « dans quel secteur travaillez-vous ? » à « quels algorithmes utilisez-vous pour la compensation inertielle ? » en quelques minutes présente une escalade de spécificité anormale.

**Flatterie excessive.** « Vous êtes vraiment la personne la plus compétente que j'ai rencontrée sur ce sujet » — en provenance d'un inconnu rencontré il y a 10 minutes — doit activer un signal d'alerte.

**Réciprocité forcée.** L'interlocuteur partage ostensiblement des informations (réelles ou fabriquées) sur son propre travail et attend visiblement un échange réciproque.

**Demande de confidentialité.** « Je préférerais qu'on continue cette discussion en dehors du cadre officiel » ou « pourrait-on en discuter par WhatsApp plutôt que par email professionnel ? » — la transition vers un canal non contrôlé est un signal fort.

**Intérêt disproportionné pour le réseau.** « Est-ce que vous connaissez le responsable du programme X ? » ou « pourriez-vous me mettre en contact avec votre collègue qui travaille sur Y ? » — l'utilisation de la cible comme vecteur vers d'autres cibles.

### 22.2 Les techniques de contre-élicitation

**Le pont.** Répondre à une question par une question. « Et vous, dans quel domaine travaillez-vous exactement ? » Le pont renverse la dynamique de l'élicitation et permet d'évaluer l'interlocuteur.

**La déviation.** Changer de sujet naturellement. « C'est intéressant. Au fait, vous avez vu la keynote de ce matin ? » La déviation n'éveille pas de soupçon si elle est exécutée avec fluidité.

**La réponse vague.** Donner l'impression de répondre sans rien dire d'exploitable. « On travaille sur des sujets similaires à ce qui se fait dans le secteur, avec les contraintes que vous pouvez imaginer. » La cible a l'impression d'avoir répondu, l'éliciteur n'a rien obtenu de spécifique.

**Le signalement discret.** Si l'interlocuteur est identifié comme une menace potentielle (signaux forts d'élicitation, profil incohérent, insistance), le signalement doit être fait au retour : briefing au RSSI ou au responsable sécurité, avec autant de détails que possible (nom, entreprise, carte de visite, sujets abordés, questions posées).

### 22.3 Protection en salon et en conférence

La protection des informations en contexte de salon professionnel repose sur un dispositif en trois temps : brief avant départ (quelles informations sont communicables, quelles informations sont interdites, quels sont les pays et les interlocuteurs à risque), comportement sur place (messages autorisés, gestion des sollicitations, utilisation des dispositifs numériques), et debriefing au retour (avec qui avez-vous échangé ? quelles questions vous ont été posées ? avez-vous observé quelque chose d'inhabituel ?). Ce dispositif est détaillé dans le cours Intelligence Économique (Ch.8) — il est repris ici dans sa dimension spécifique à la contre-ingénierie sociale.

### 22.4 Protection en voyage professionnel

Certains pays présentent des risques d'ingérence particulièrement élevés. Sans nommer de pays spécifiques (les listes évoluent et sont publiées par les services compétents — DGSI, ANSSI, services homologues), les risques incluent : la surveillance des communications (chambres d'hôtel, réseaux WiFi), les approches physiques (contacts « spontanés » dans les hôtels, les bars, les événements), et le ciblage des dispositifs numériques (inspection aux frontières, clonage de téléphone). Les règles de protection incluent : ne jamais laisser de dispositifs sans surveillance, utiliser un téléphone dédié (sans données sensibles), chiffrer les communications, ne pas discuter de sujets sensibles en public, et signaler toute approche suspecte au retour.

### 22.5 Protection des VIP et des cibles à haute valeur

Les dirigeants, les responsables R&D, les cadres travaillant sur des programmes sensibles, et les personnels ayant des habilitations de sécurité nécessitent un dispositif de protection adapté sans être transformés en paranoïaques. Le dispositif inclut : une évaluation de la surface d'exposition personnelle (OSINT sur eux-mêmes — que trouverait un attaquant ?), des recommandations de sécurité des réseaux sociaux (paramètres de confidentialité, gestion du contenu professionnel et personnel), un protocole de communication sécurisé pour les sujets sensibles, et une sensibilisation spécifique aux techniques d'élicitation et de ciblage qui visent leur profil.

---

## Chapitre 23 — Défense technique contre le social engineering

### 23.1 Défense email

**DMARC en mode « reject ».** La configuration DMARC p=reject empêche l'usurpation directe du domaine de l'entreprise (un attaquant ne peut pas envoyer un email qui semble venir de @helios-aero.fr depuis un serveur non autorisé). C'est une mesure P0 — mais elle ne protège pas contre le typosquatting, les domaines lookalike ou la compromission d'email légitime.

**Bannières « email externe ».** L'ajout d'une bannière visible sur tous les emails provenant de l'extérieur de l'organisation (« ATTENTION : cet email provient d'un expéditeur externe ») est une mesure simple mais efficace qui réduit significativement le taux de réussite des phishings par display name spoofing.

**Passerelles anti-phishing.** Les solutions de sécurité email modernes (Proofpoint, Mimecast, Microsoft Defender for Office 365) analysent les URLs, les pièces jointes (sandboxing), le comportement de l'expéditeur et le contenu pour détecter les phishings. Leur efficacité est réelle mais non absolue — les emails de BEC (texte seul, pas de lien ni de pièce jointe) passent souvent les filtres.

**Simulation de phishing continue.** Les campagnes de phishing simulé régulières (mensuelles ou bimestrielles) avec retour individualisé constituent une couche de défense active qui maintient la vigilance.

### 23.2 Défense téléphonique

**Callback verification.** Pour toute demande sensible reçue par téléphone, rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel) — jamais sur le numéro affiché (qui peut être spoofé) ni sur un numéro fourni par l'appelant.

**Procédures de helpdesk renforcées.** Les demandes de reset de credentials par téléphone doivent être soumises à une vérification d'identité robuste : callback sur le numéro enregistré, validation par le manager, code de vérification préétabli, ou vérification en personne pour les comptes à privilèges.

**STIR/SHAKEN.** Le protocole d'authentification de l'identité de l'appelant est en cours de déploiement mais reste incomplet en 2025. Il réduit le spoofing sur les réseaux conformes mais ne l'élimine pas.

### 23.3 Défense d'accès physique

**Contrôle d'accès multi-couches.** Badge seul pour les zones communes, badge + code pour les zones intermédiaires, badge + biométrie pour les zones sensibles (salle serveur, R&D, direction). La biométrie (empreintes, reconnaissance faciale) est résistante au clonage mais pose des questions RGPD (les données biométriques sont des données sensibles au sens du RGPD — leur traitement nécessite une base légale spécifique).

**Anti-tailgating.** Tourniquets unitaires, sas à passage unique, portiques à détection de double passage. Ces dispositifs sont efficaces mais nécessitent un investissement significatif et modifient les flux de circulation (impact sur l'ergonomie et l'acceptabilité par les employés).

**Politique visiteurs.** Accompagnement systématique des visiteurs par un employé de l'arrivée au départ, badge visiteur visuellement distinct (couleur, format), registre des visites, récupération du badge en fin de visite.

### 23.4 Gestion des identités et des accès

**MFA résistant au phishing.** Le déploiement de FIDO2/WebAuthn (clés de sécurité physiques ou passkeys) élimine les risques de phishing en temps réel (Evilginx) parce que l'authentification est liée au domaine — la clé ne s'active que sur le domaine légitime. C'est la mesure technique la plus efficace contre le credential harvesting par phishing. En 2025, le déploiement de FIDO2 est en forte accélération mais reste minoritaire dans les entreprises.

**Principe du moindre privilège.** Chaque utilisateur ne dispose que des accès nécessaires à ses fonctions. Cela limite l'impact d'une compromission : un identifiant d'employé standard compromis par phishing donne accès aux ressources de l'employé, pas aux ressources de l'ensemble de l'organisation.

**Surveillance des accès anormaux.** UEBA (User and Entity Behavior Analytics) et ITDR (Identity Threat Detection and Response) détectent les comportements anormaux après compromission : connexion depuis une géolocalisation inhabituelle, accès à des ressources hors du périmètre habituel, escalade de privilèges.

### 23.5 Les processus métier

**Validation multi-niveaux pour les virements.** Tout virement supérieur à un seuil défini nécessite la validation de deux personnes distinctes, dont au moins une vérification par callback. Les changements de coordonnées bancaires sont soumis à la même procédure.

**Séparation des tâches.** La personne qui initie un virement ne peut pas être la même personne qui le valide. La séparation des tâches élimine le scénario du BEC où un seul employé suffit pour déclencher un virement frauduleux.

---

## Chapitre 24 — Réponse à un incident de social engineering

### 24.1 Détection

La détection d'un incident de social engineering repose sur trois sources : le signalement par l'employé (scénario optimal — c'est pourquoi la culture de signalement est la première défense), la détection technique (connexion anormale, alertes EDR, détection de credentials compromis, analyse de sessions) et la notification externe (un partenaire alerte, un service de renseignement notifie, un chercheur en sécurité signale).

Le temps de détection est critique, en particulier pour le BEC (un virement frauduleux peut être irrécupérable en quelques heures) et pour les intrusions utilisant des credentials compromis (l'attaquant latéralise et exfiltre rapidement).

### 24.2 Qualification

La qualification de l'incident détermine la réponse. Les scénarios principaux sont : phishing réussi simple (credentials compromis — impact limité si le compte n'a pas de privilèges élevés), BEC en cours (virement initié — nécessite une action bancaire urgente pour bloquer le transfert), intrusion physique (implant posé — nécessite une recherche physique et réseau), élicitation de renseignement (fuite d'information — difficile à quantifier, nécessite une évaluation de l'impact).

### 24.3 Containment

Le containment dépend du type d'incident : reset des credentials compromis (tous les comptes affectés), révocation des sessions actives, blocage des accès à risque, recherche de persistence (l'attaquant a-t-il installé des backdoors ou créé des comptes additionnels ?), isolement du segment réseau si un implant physique est suspecté, et pour le BEC, gel du virement via la banque (la rapidité est déterminante — les fonds transférés à l'étranger sont souvent irrécupérables après 24-48h).

### 24.4 Investigation

L'investigation d'un incident de social engineering combine forensique technique et analyse humaine. Forensique email (headers complets, analyse de la landing page, identification de l'infrastructure de phishing), identification de l'acteur (phishing de masse vs spear-phishing ciblé vs APT — la sophistication et la personnalisation sont des indicateurs), évaluation de l'impact (quels accès ont été compromis, quelles données ont potentiellement été exfiltrées, quelle est la persistance de l'attaquant), et analyse de la chaîne de compromission (comment l'attaquant est passé de l'accès initial à ses objectifs finaux).

### 24.5 Retex et amélioration

Le retex (retour d'expérience) post-incident est une obligation, pas une option. Il doit suivre le modèle « no blame post-mortem » : l'objectif est d'identifier les défenses qui ont échoué et de les améliorer, pas de blâmer l'employé qui a cliqué.

Le retex couvre : la chronologie de l'incident (de la première action de l'attaquant à la détection et au containment), les défenses qui ont fonctionné (qu'est-ce qui a alerté ou ralenti l'attaquant ?), les défenses qui ont échoué (pourquoi le phishing n'a pas été filtré ? pourquoi le helpdesk a procédé au reset sans vérification suffisante ?), les recommandations d'amélioration (classées P0/P1/P2), et le plan d'action avec responsable et échéance pour chaque recommandation.

---

## Chapitre 25 — Capstone Partie V : incident de social engineering — de la détection au retex

**Scénario.** Un employé du service comptabilité signale un appel téléphonique suspect au SOC : un interlocuteur se présentant comme le prestataire comptable a demandé l'envoi d'un fichier de paie « pour vérification ». L'employé a d'abord envoyé le fichier, puis a eu un doute et a signalé.

**Livrables attendus :**
1. Fiche de qualification de l'incident (type, gravité, impact potentiel)
2. Plan de containment immédiat
3. Protocole d'investigation (forensique email, analyse de l'appel, évaluation de l'impact)
4. Rapport d'incident (chronologie, analyse, impact, recommandations P0/P1/P2)
5. Plan de retex (format no-blame, actions correctives, responsables, échéances)

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 6**
>
> **Convergence.** L'enquête sur « David Chen » confirme le diagnostic de Nathan. La vérification du profil LinkedIn révèle : photo générée par IA (confirmé par analyse des artefacts — pas de résultat en recherche d'image inversée, symétrie anormale des oreilles), entreprise « Meridian Consulting Asia » sans enregistrement commercial vérifiable dans les registres consultés, numéro WhatsApp enregistré dans un pays tiers, et parcours professionnel avec des incohérences (dates, entreprises non vérifiables).
>
> L'analyse des échanges WhatsApp montre un schéma d'élicitation structuré : 3 premières semaines de conversation générale (flattery, intérêt professionnel, réciprocité), semaine 4-6 escalade vers des questions techniques spécifiques, semaine 7-8 proposition de consulting rémunéré et de rencontre physique. Alexandre Petit a divulgué, sans s'en rendre compte, des informations sur les orientations technologiques de son programme, les noms de ses collègues et les partenaires du consortium.
>
> La DGSI est alertée et prend le relais de l'investigation (ingérence économique étrangère). Alexandre est débriefé sans sanction — il est informé des mécanismes exploités et reçoit une formation de contre-élicitation. Nathan intègre ce cas réel dans son rapport de red team comme illustration de la menace de niveau étatique qui pèse sur Helios.


---
