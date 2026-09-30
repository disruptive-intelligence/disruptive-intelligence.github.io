---
title: PARTIE III — SOCIAL ENGINEERING PHYSIQUE
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 3
chapters: 7
---

---

## Chapitre 12 — Reconnaissance physique et planification

### 12.1 La reconnaissance du site

La reconnaissance physique complète la reconnaissance OSINT et fournit les informations nécessaires à la planification de l'intrusion. Elle se conduit en plusieurs passes, idéalement sur plusieurs jours et à différentes heures.

**Le périmètre.** Identifier toutes les entrées (accueil principal, livraisons, parking souterrain, accès technique, sortie de secours), leur niveau de contrôle (gardien, badge, interphone, portique, tourniquet), et les zones de transition (fumoir, parking, accès cantine externe). Les sorties de secours, souvent équipées d'alarme mais pas toujours surveillées, sont des points d'intérêt fréquents pour les red teamers.

**Les systèmes de contrôle d'accès.** Observer le type de lecteur (RFID basse fréquence 125 kHz — HID ProxCard, facile à cloner ; RFID haute fréquence 13.56 MHz — MIFARE, iCLASS, plus résistant ; NFC mobile), la présence de biométrie (empreintes, iris — rare en entreprise standard), les sas anti-piggyback (tourniquets, portiques à verrouillage unitaire). Les caméras : identifier leur emplacement, leur angle de couverture, la présence de zones d'ombre, et déterminer si elles sont en monitoring live (opérateur présent) ou en enregistrement passif (consultation a posteriori uniquement).

**Les horaires et les flux.** Les heures d'arrivée (8h-9h30 — flux maximum, contrôles relâchés) et de départ (17h-18h30), les pauses (12h-14h — mouvements entre bâtiments, accès cantine), les livraisons (généralement matin, accès souvent moins contrôlé). Le créneau idéal pour une intrusion physique est souvent 10h-11h ou 14h-15h : assez de monde dans les locaux pour ne pas être remarqué, mais assez calme pour éviter les flux où un inconnu serait plus visible.

### 12.2 L'observation comportementale

Au-delà de l'infrastructure physique, le red teamer observe les comportements des employés, qui constituent souvent la vulnérabilité principale.

**Le badge.** Les employés portent-ils leur badge de manière visible (autour du cou, au revers) ? Ou le gardent-ils dans leur poche/portefeuille et le présentent uniquement au lecteur ? Un environnement où le badge n'est pas porté visiblement est un environnement où un intrus sans badge ne sera pas immédiatement repéré.

**Le tailgating naturel.** Les employés tiennent-ils la porte aux personnes derrière eux ? Vérifient-ils le badge de la personne qui les suit ? Dans la grande majorité des entreprises, la norme sociale est de tenir la porte — refuser est perçu comme impoli.

**La vérification des visiteurs.** Les visiteurs sont-ils systématiquement accompagnés ? Ou sont-ils libres de se déplacer après le passage à l'accueil ? Les badges visiteurs sont-ils visuellement distincts des badges employés ? Sont-ils récupérés en fin de visite ?

**Les zones informelles.** Le fumoir, le café, la cantine sont des zones de socialisation où les barrières de sécurité sont naturellement abaissées. Ce sont les points de contact idéaux pour l'élicitation (Ch.14).

### 12.3 Le dumpster diving

La fouille des poubelles (dumpster diving) reste une technique de reconnaissance basique mais efficace. Les poubelles extérieures (sur le trottoir ou dans la zone de collecte) ne sont généralement pas protégées juridiquement (la jurisprudence varie selon les pays — en France, la fouille de poubelles sur la voie publique n'est pas constitutive d'une infraction ; en revanche, pénétrer dans une propriété privée pour accéder aux poubelles constitue une violation de domicile).

Les trouvailles typiques incluent : documents imprimés non déchiquetés (organigrammes, listes de diffusion, procès-verbaux de réunion, rapports intermédiaires), badges expirés (qui peuvent servir de modèle pour la fabrication d'un faux badge visuellement crédible), post-its avec des mots de passe ou des codes, matériel informatique mis au rebut (disques durs non effacés, clés USB, téléphones), et emballages de matériel révélant les technologies utilisées (cartons de serveurs, de switches, d'équipements de sécurité).

**Défense** : politique de destruction documentaire (déchiqueteuse cross-cut minimum — les déchiqueteuses en bandes sont reconstructibles), bennes fermées et cadenassées, sensibilisation au risque des documents jetés sans précaution.

### 12.4 Le matériel du red teamer

La préparation matérielle est critique pour la crédibilité du pretexte et le succès de l'opération.

**La tenue.** Adaptée au pretexte : costume et cravate pour un « auditeur » ou un « consultant », polo logotypé et jean pour un « technicien IT », bleu de travail et gilet haute visibilité pour un « prestataire de maintenance ». Le gilet haute visibilité est l'un des outils les plus puissants du social engineering physique : il confère une légitimité quasi automatique et réduit les questions.

**Le faux badge.** Les badges d'entreprise sont rarement vérifiés visuellement en détail au-delà de la couleur et de la présence d'un logo. Un badge imprimé sur un support similaire (même taille, même orientation, couleur cohérente, logo de l'entreprise récupéré en OSINT) suffit dans la majorité des cas pour l'examen visuel. Le badge ne passera pas un contrôle RFID si la technologie n'est pas clonée (Ch.27), mais dans les environnements où le badge est présenté visuellement (à un gardien) plutôt qu'électroniquement (sur un lecteur), la version imprimée est suffisante.

**Le clipboard.** Le « bouclier social » par excellence. Une personne qui se déplace dans des locaux avec un clipboard (ou un ordinateur portable et une mine concentrée) n'est presque jamais questionnée. Le clipboard projette l'image de quelqu'un en mission, qui a quelque chose à faire et qui sait où il va.

**Les outils techniques.** Dans le cadre d'un red team autorisé : implants réseau (LAN Turtle, rogue access point WiFi), clé USB malveillante (Rubber Ducky, Bash Bunny), keylogger hardware, lecteur RFID (Proxmark3 pour le clonage — voir Ch.27). Ces outils sont transportés discrètement et déployés une fois l'accès physique obtenu.

### 12.5 Le plan d'intrusion

Le plan d'intrusion est un document opérationnel qui couvre : les objectifs (accès à une zone spécifique, connexion d'un implant réseau, accès à un poste de travail, vol simulé d'un document classifié), le timing (jour, heure, durée maximale de présence), les pretextes (principal + au moins un pretexte de secours en cas d'échec du premier), le matériel nécessaire, le plan d'exfiltration (comment quitter les lieux proprement), et le protocole d'urgence.

Le **protocole d'urgence** est indispensable. Si le red teamer est intercepté, confronté ou arrêté par la sécurité, il doit pouvoir s'identifier immédiatement comme testeur autorisé. Le « safe word » est un mot ou une phrase convenu avec le commanditaire qui, prononcé au téléphone avec le contact de référence, confirme instantanément la légitimité de la mission. Le contact de référence (RSSI, DG, ou personne désignée) doit être joignable 24/7 pendant la durée du test.

---

## Chapitre 13 — Techniques d'intrusion physique

### 13.1 Le tailgating et le piggybacking

Le tailgating (suivre un employé à travers une porte contrôlée) est la technique d'intrusion physique la plus simple et statistiquement la plus efficace. Les gens tiennent la porte par politesse — c'est une norme sociale profondément ancrée que même les programmes de sensibilisation les plus rigoureux peinent à modifier.

La technique est élémentaire : attendre qu'un employé badge et ouvre une porte, puis le suivre en maintenant un flux naturel. Le succès dépend du timing (arriver juste derrière, pas trop loin pour ne pas être remarqué), du comportement (confiant, pressé, naturel — ne pas hésiter, ne pas regarder autour de soi de manière suspecte), et de l'apparence (tenue cohérente avec l'environnement).

Le piggybacking est une variante où le red teamer engage activement la conversation avec l'employé pendant l'approche de la porte, créant un lien social qui rend le refus d'accès encore plus improbable (« après vous — vous avez vu, ils ont encore changé le code du parking ! »).

**Contre-mesures** : tourniquets unitaires (sas qui ne laissent passer qu'une personne par badge), portiques de sécurité avec détection anti-passback, sensibilisation ciblée du personnel (autorisation de refuser poliment — « désolé, c'est la procédure, chacun doit badger »), culture où la vérification n'est pas perçue comme impolie.

### 13.2 L'impersonation

L'impersonation — se faire passer pour quelqu'un d'autre — est le cœur du social engineering physique. La crédibilité du pretexte est tout. Les pretextes les plus efficaces exploitent des rôles qui ont un accès légitime aux locaux et qui ne sont pas questionnés.

**Le prestataire IT.** Après identification du prestataire par OSINT, le red teamer se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. Crédibilité renforcée par : un polo ou un gilet aux couleurs du prestataire (imprimé pour l'occasion), un faux bon d'intervention, le name-dropping du responsable IT interne et du responsable de compte chez le prestataire.

**L'inspecteur.** Inspecteur incendie, inspecteur sanitaire, auditeur qualité, contrôleur réglementaire — ces rôles confèrent une autorité qui réduit les questions. L'inspecteur est attendu, ou il arrive par surprise — dans les deux cas, il est rarement refusé.

**L'employé d'un autre site.** Dans les organisations multi-sites, les employés ne connaissent pas personnellement les collègues des autres sites. « Je suis Thomas du bureau de Paris, je suis venu pour la réunion avec Jean-Marc Duval — je ne retrouve pas la salle de réunion 3B » est un pretexte simple et efficace.

**Le visiteur.** Un faux rendez-vous avec un responsable identifié par OSINT, annoncé la veille par un appel de « l'assistante » (complice) au standard. Si le rendez-vous est enregistré dans le système de gestion des visiteurs, le red teamer reçoit un badge visiteur légitime.

### 13.3 La manipulation des gardiens et réceptionnistes

Les gardiens et réceptionnistes sont la première ligne de défense physique — et souvent la plus vulnérable. Ils sont formés à l'accueil et à la courtoisie, rarement au contre-social engineering.

Les techniques de manipulation incluent : le **name-dropping** (« je viens voir Frédéric Morin, on a un rendez-vous à 14h »), la **création d'urgence** (« mon technicien est déjà à l'intérieur, il m'attend dans le local serveur — c'est urgent, on a une panne de production »), l'**appel de confirmation** (un complice appelle le standard pendant que le red teamer est à l'accueil et confirme sa venue : « oui, c'est le technicien qu'on attend, faites-le monter »), et la **sympathie** (« je suis vraiment désolé de vous embêter, j'ai un problème de badge, ça fait 20 minutes que je suis bloqué dehors — vous pouvez m'ouvrir le temps que l'IT me refasse un badge ? »).

### 13.4 L'exploitation des badges

Le clonage de badges RFID est une technique de red team courante dont la faisabilité dépend fortement de la technologie utilisée.

**RFID basse fréquence (125 kHz)** — HID ProxCard, EM4100 : facilement clonable avec un Proxmark3, un Flipper Zero ou même des lecteurs/graveurs basiques disponibles en ligne. La lecture peut se faire à distance de quelques centimètres (suffisant pour lire un badge dans la poche d'un employé qui passe près de vous) et la copie sur un badge vierge prend quelques secondes.

**RFID haute fréquence (13.56 MHz)** — MIFARE Classic, MIFARE DESFire, iCLASS : plus résistant au clonage. MIFARE Classic a des faiblesses cryptographiques connues qui permettent le clonage avec un Proxmark3, mais les versions plus récentes (DESFire EV2/EV3) utilisent un chiffrement robuste. iCLASS Standard est également vulnérable, mais iCLASS SE est significativement plus résistant.

**NFC mobile et badges virtuels** — Apple Wallet, Google Wallet : difficiles à cloner car protégés par la cryptographie du smartphone. C'est l'une des raisons de la migration progressive vers les badges mobiles dans les entreprises à sécurité renforcée.

La défense contre le clonage passe par la migration vers des technologies résistantes (DESFire EV2+, badges mobiles), la combinaison badge + biométrie pour les zones sensibles, la détection des anomalies d'accès (même badge utilisé à deux endroits simultanément, accès à des heures inhabituelles) et l'audit régulier du parc de badges.

### 13.5 Le non-verbal et la crédibilité comportementale

En social engineering physique, le corps et le comportement comptent autant que le scénario. Un pretexte parfait sera ruiné par un comportement hésitant, un regard fuyant ou une posture qui trahit le stress.

**La proxémie.** La gestion de la distance interpersonnelle est culturellement déterminée, mais en contexte professionnel français, une distance de 80 cm à 1,2 m est la norme pour une interaction professionnelle. Trop proche : inconfort et suspicion. Trop loin : désengagement et manque de crédibilité.

**La posture.** Dos droit, épaules ouvertes, démarche assurée, regard droit. Le red teamer qui se déplace comme s'il connaissait les lieux ne sera pas questionné. Celui qui hésite à un croisement, regarde les plaques de porte, ou consulte son téléphone avec l'air perdu sera immédiatement repéré par un gardien attentif.

**Le tempo.** La vitesse de déplacement doit être cohérente avec le pretexte. Un « technicien en intervention urgente » se déplace vite et avec détermination. Un « auditeur en visite » se déplace calmement et observe. Un « employé qui va au café » est décontracté.

**La gestion du regard.** Contact visuel bref et naturel avec les personnes croisées (ni évitement ni insistance). Un hochement de tête accompagné d'un « bonjour » suffit à créer un micro-rapport qui désarme la suspicion.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 4**
>
> **Intrusion physique — Site de Bordeaux.** Nathan se présente à l'entrée du site de production de Bordeaux le mardi à 10h30. Tenue : polo gris avec logo brodé de « NetServ Solutions » (le prestataire de maintenance informatique identifié par OSINT — le polo a été imprimé la veille). Badge visiteur visuellement crédible (format Helios, photo de Nathan, nom « T. Beaumont — NetServ Solutions »). Clipboard avec un faux bon d'intervention mentionnant « vérification connectique baie serveur B2 — ref. ticket #NS-2025-0847 ».
>
> Le gardien, Jean-Pierre, vérifie la liste des interventions planifiées. Nathan n'y figure pas. « C'est bizarre, j'ai le ticket ici, c'est Jean-Marc Duval qui l'a ouvert vendredi. Il y a un switch qui pose problème dans la baie B2 depuis la semaine dernière. » Jean-Pierre hésite. Nathan sort son téléphone : « Attendez, je vais appeler mon responsable de compte. » Il appelle Thomas (son complice), qui répond : « Oui, c'est l'intervention NT-0847 pour Helios Bordeaux, technicien Beaumont. C'est bien planifié chez nous, peut-être un oubli de validation côté client. » Jean-Pierre consulte son écran une dernière fois, puis : « Allez-y, vous connaissez le chemin vers le local serveur ? — Oui, bâtiment B, au fond à droite. Merci Jean-Pierre. »
>
> En 45 minutes, Nathan connecte un implant réseau (Raspberry Pi configuré comme rogue access point) dans la baie serveur, prend des photos de trois salles de réunion (post-its sur les écrans avec mots de passe WiFi et codes de salle visioconférence), et photographie le tableau d'affichage du couloir RH (planning des absences, organigramme du site, numéros de téléphone internes).

---

## Chapitre 14 — Élicitation en face-à-face

### 14.1 Définition et fondements

L'élicitation est l'extraction d'information dans le cadre d'une conversation apparemment normale et non menaçante. La cible ne sait pas qu'elle est interrogée — elle pense participer à une conversation ordinaire. C'est précisément ce qui rend l'élicitation si efficace et si difficile à détecter : il n'y a ni demande explicite suspecte, ni canal d'attaque technique, ni pièce jointe à analyser — seulement une conversation.

L'agence américaine NSA définit l'élicitation comme « l'extraction subtile d'information au cours d'une conversation apparemment normale et innocente ». Cette définition est opérationnellement exacte : le succès de l'élicitation repose sur le fait que la cible perçoit l'échange comme naturel, réciproque et bienveillant.

L'élicitation fonctionne pour des raisons psychologiques documentées : la plupart des gens souhaitent être perçus comme compétents et bien informés (ego), désirent aider un interlocuteur sympathique (réciprocité, politesse), sont mal à l'aise avec le silence et le comblent en parlant (anxiété sociale), et ne mentent pas spontanément quand la conversation semble anodine (honnêteté par défaut).

### 14.2 Les techniques d'élicitation

**La question ouverte.** « Comment se passe le projet de migration ? » La question ouverte invite un développement libre — la cible choisit les détails qu'elle partage, ce qui donne l'impression de contrôle alors que l'éliciteur oriente la conversation vers les sujets d'intérêt.

**La provocation (deliberate false statement).** Affirmer volontairement quelque chose de faux pour provoquer une correction. « J'ai entendu dire que vous migriez vers SAP S/4HANA ? » Si la réponse est « Non, on est sur Oracle depuis janvier, c'est tout nouveau », l'éliciteur a obtenu une information technique spécifique sans l'avoir demandée — la cible l'a « corrigé » spontanément. Cette technique exploite le besoin de précision et la difficulté à laisser une erreur non corrigée.

**La flatterie ciblée.** « Vous êtes probablement la personne la mieux placée pour comprendre ce sujet dans l'entreprise. » La flatterie active le mécanisme de réciprocité (la cible se sent valorisée et veut « mériter » le compliment en démontrant sa compétence) et l'ego (plaisir de la reconnaissance).

**Le partage réciproque.** Offrir une information (réelle ou fabriquée) pour créer une obligation de réciprocité. « Chez nous, on a eu un mal fou avec la certification DO-178C — et vous ? » L'éliciteur qui partage d'abord crée un précédent d'ouverture et une attente de réciprocité.

**Le silence stratégique.** Après avoir posé une question, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le vide conversationnel et le comblent en développant — souvent au-delà de ce qu'ils avaient initialement prévu de partager. Le silence stratégique est l'un des outils les plus puissants et les plus sous-utilisés de l'élicitation.

**L'expression de l'ignorance.** « Je ne comprends pas du tout comment fonctionne votre système de badgeage — ça a l'air complexe. » L'ignorance affichée active le besoin d'expliquer et de démontrer sa compétence.

### 14.3 La gestion de la conversation

L'élicitation réussie suit une progression contrôlée : création du rapport → conversation anodine → transition naturelle vers les sujets d'intérêt → extraction d'information → désengagement propre.

**Créer le rapport.** Le rapport (relation de confiance conversationnelle) se construit par le mirroring (reproduire subtilement la posture, le rythme de parole, le vocabulaire de la cible), l'écoute active (reformulation, signaux d'attention — hochements de tête, « je vois », « intéressant »), l'identification de points communs (parcours, intérêts, expériences partagées) et le respect du tempo de la cible (ne pas presser, laisser la conversation se développer naturellement).

**Orienter sans diriger.** L'éliciteur guide la conversation par des questions de relance (« et comment ça se passe concrètement ? »), des ponts thématiques (« en parlant de sécurité, d'ailleurs... ») et des manifestations d'intérêt sélectif (approfondir les sujets utiles, survoler les autres). La cible ne doit jamais avoir l'impression d'être interrogée.

**Escalader progressivement.** Commencer par des sujets anodins (l'entreprise en général, le secteur, l'actualité professionnelle), puis avancer vers des sujets plus spécifiques (le projet en cours, les outils utilisés, les défis techniques) et enfin vers les sujets sensibles (les failles de sécurité, les informations confidentielles, les projets non annoncés). Chaque palier valide que la cible est à l'aise avant de monter au suivant.

**Désengager proprement.** La fin de la conversation doit être naturelle et ne pas éveiller de soupçons. Prétexte de départ (« je dois aller à ma prochaine réunion »), remerciement chaleureux, échange de coordonnées (renforce la perception de normalité de l'échange). La cible doit quitter la conversation en se sentant bien — pas en se demandant pourquoi on lui a posé autant de questions.

### 14.4 Les contextes d'élicitation

**Salon professionnel et conférence.** L'environnement idéal pour l'élicitation : la norme sociale est au networking, les barrières sont abaissées, les participants sont en mode « ouverture » et « échange ». Les pauses café, les cocktails et les dîners de gala sont les moments les plus propices. Le bar d'hôtel après une journée de conférence est le terrain de chasse classique de l'élicitation — fatigue, alcool et décompression réduisent la vigilance.

**Voyage professionnel.** Avion, train, salle d'attente d'aéroport — les voyages créent des opportunités de conversation prolongée avec une cible isolée de son contexte habituel. Les vols long-courriers offrent plusieurs heures de conversation potentielle.

**Événement d'entreprise.** Soirée de Noël, séminaire d'équipe, pot de départ — les événements internes mélangent registres professionnel et social, ce qui facilite l'élicitation (la conversation est à la fois professionnelle et personnelle, ce qui rend les questions sur le travail naturelles).

### 14.5 L'élicitation par les services de renseignement étrangers : signaux et continuum

Les services de renseignement utilisent l'élicitation comme technique de base pour évaluer les cibles potentielles et collecter de l'information avant une éventuelle tentative de recrutement. Le processus suit un continuum identifiable : spotting (identification de la cible), assessment (évaluation de l'accès et de la vulnérabilité), developmental contact (établissement d'un lien), cultivation (renforcement progressif de la relation), elicitation ladder (montée en sensibilité des sujets abordés), et potentiellement tentative de recrutement.

Les signaux d'alerte incluent : un interlocuteur dont le profil ou l'entreprise est difficile à vérifier, des questions qui semblent anodines mais qui portent systématiquement sur des sujets sensibles (projets R&D, contrats, technologies), une transition rapide vers un canal de communication privé (WhatsApp, Signal), des propositions de « consulting » ou de « collaboration académique » rémunérées mais vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et une relation qui progresse anormalement vite (invitation à dîner dès la première rencontre).

Les techniques de contre-élicitation sont détaillées au Ch.22. Les cas d'ingérence documentés par la DGSI sont un excellent support de formation.

---

## Chapitre 15 — Manipulation psychologique avancée : de la théorie à l'opérationnel

Ce chapitre est le pendant opérationnel du Ch.2. Là où le Ch.2 explique *pourquoi* les leviers psychologiques fonctionnent (cognition, biais, mécanismes), le présent chapitre explique *comment* le praticien les met en œuvre concrètement en situation.

### 15.1 Le pied dans la porte et la porte au nez

**Le pied dans la porte.** Commencer par une petite demande à laquelle la cible accède facilement, puis escalader vers la demande réelle. La première compliance crée un engagement psychologique qui rend le refus de la demande suivante plus coûteux. En red team : « Est-ce que vous pouvez me montrer où sont les toilettes ? » (petite demande, accès au couloir) → « Au fait, vous savez où est la salle serveur ? Mon collègue m'attend là-bas pour l'intervention » (demande réelle).

**La porte au nez.** Commencer par une demande excessive que la cible refusera, puis proposer une demande modérée (la vraie demande) qui sera perçue comme un compromis raisonnable. « Je dois vérifier tous les postes de travail de l'étage — ça va prendre la journée. » Refus. « Bon, au minimum je dois vérifier le poste du responsable, ça prendra 5 minutes. » Acceptation. La concession de l'éliciteur crée une obligation de concession réciproque.

### 15.2 La création de rapport rapide

Le rapport — cette connexion interpersonnelle qui crée un sentiment de confiance et de sympathie — peut être construit en quelques minutes avec des techniques documentées.

**Le mirroring.** Reproduire subtilement les gestes, la posture, le rythme de parole et le vocabulaire de l'interlocuteur. Le mirroring active les neurones miroirs et crée un sentiment de similarité inconscient. Il doit être subtil — un mirroring trop évident est perçu comme moquerie et détruit le rapport.

**Le pacing-leading.** S'aligner d'abord sur l'état émotionnel et le rythme de la cible (pacing), puis progressivement l'amener vers l'état souhaité (leading). Si la cible est stressée, commencer par un tempo rapide et une énergie élevée (pacing), puis ralentir progressivement (leading) pour créer un état de calme et d'ouverture.

**Les limites éthiques.** Le rapport est un outil, pas une fin en soi. Le red teamer ne crée pas de relation affective réelle — il simule une connexion pour atteindre un objectif opérationnel. La distinction est fondamentale : le rapport de red team est une technique temporaire et bornée. Un red teamer qui développe une relation personnelle authentique avec une cible franchit une ligne éthique.

### 15.3 Le pretexting avancé et la résistance au questionnement

Un pretexte avancé n'est pas une simple identité fictive — c'est un personnage complet avec une histoire, des mannerisms, des réponses aux questions imprévues, et une cohérence interne suffisante pour résister à un interrogatoire léger.

La construction d'un pretexte robuste inclut : une identité complète (nom, entreprise, poste, ancienneté, parcours), une backstory cohérente (comment et pourquoi cette personne est là aujourd'hui), des détails sensoriels (vêtements, accessoires, matériel — cohérents avec le rôle), une préparation aux questions (« qui vous a envoyé ? », « quel est votre numéro de ticket ? », « comment s'appelle votre responsable ? »), et un plan de sortie si le pretexte est mis en doute.

La durée d'un pretexte varie de quelques minutes (interaction avec un gardien) à plusieurs semaines (opération d'élicitation prolongée, faux profil LinkedIn maintenu sur des mois). Plus la durée augmente, plus le risque de démasquage est élevé et plus la maintenance du pretexte consomme de ressources.

### 15.4 Gestion de la résistance et de la confrontation

Quand la cible dit non, hésite ou exprime de la suspicion, le praticien dispose de plusieurs options.

**Le pivoting.** Changer d'angle d'approche sans changer de pretexte. Si la demande directe échoue, reformuler indirectement. « Je ne peux pas vous donner accès au réseau » → « Pas de problème, je comprends — je peux juste utiliser le WiFi visiteur pour envoyer un email à mon responsable ? » (le WiFi visiteur peut révéler des informations sur l'infrastructure réseau).

**Le recadrage.** Réinterpréter le refus dans un cadre favorable. « Non, je ne suis pas autorisé à donner cette information » → « Bien sûr, je comprends parfaitement — votre politique de sécurité est impressionnante. Justement, c'est ce que je veux documenter dans mon rapport d'audit. »

**L'abandon gracieux.** Quand la résistance est trop forte ou la suspicion trop élevée, se retirer proprement sans éveiller davantage de soupçons. « Pas de souci, je vais rappeler mon responsable pour clarifier. Merci de votre temps. » Un abandon gracieux préserve la possibilité d'une seconde tentative par un autre vecteur.

**La lecture des signaux de gêne.** Reconnaître quand la cible passe de la coopération à l'inconfort : changement de posture (bras croisés, recul), regard fuyant, réponses plus courtes, changement de sujet, vérification du badge. Ces signaux indiquent que la vigilance de la cible est activée et que l'escalade risque la confrontation.

### 15.5 Les limites absolues du red team

Certaines techniques sont absolument proscrites en red team, même si un attaquant réel les utiliserait. L'exploitation de vulnérabilités personnelles (addiction, maladie, problèmes financiers, détresse émotionnelle), les menaces, le chantage, l'intimidation réelle, l'établissement d'une relation intime ou sentimentale avec une cible, et toute action susceptible de causer une détresse psychologique durable sont des lignes rouges non négociables. Un red teamer qui franchit ces lignes cause un préjudice réel à des individus réels — ce qui est contraire à l'objectif même du test, qui est d'améliorer la sécurité, pas de traumatiser des employés.

---

## Chapitre 16 — Capstone Partie III : test d'intrusion physique et élicitation

**Exercice intégrateur.** L'étudiant planifie un test d'intrusion physique complet sur un site industriel fictif (usine de production pharmaceutique, 400 employés, 1 site).

**Livrables attendus :**
1. Reconnaissance physique documentée (plan du site, accès identifiés, systèmes de contrôle d'accès, flux, horaires, comportements observés)
2. Construction de 2 pretextes d'intrusion physique (pretexte principal + pretexte de secours) avec justification
3. Liste du matériel nécessaire
4. Plan d'action (chronologie minute par minute, points de décision, objectifs intermédiaires)
5. Protocole d'urgence (safe word, contact de référence, procédure si confrontation)
6. Script d'élicitation : simulation d'une conversation d'élicitation en contexte salon professionnel (dialogue complet + analyse des techniques utilisées à chaque étape)
7. Grille d'évaluation de la sécurité physique observée (avec recommandations P0/P1/P2)

**Erreur fréquente** : négliger le protocole d'urgence. Un plan d'intrusion sans protocole d'extraction n'est pas un plan professionnel — c'est une improvisation dangereuse.


---
