---
title: PARTIE I — FONDATIONS
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 1
chapters: 7
---

---

## Chapitre 1 — Le facteur humain : pourquoi les humains sont le maillon

### 1.1 La vulnérabilité humaine comme constante

Le social engineering ne repose pas sur l'exploitation d'une faiblesse individuelle. Il exploite des réponses cognitives normales, câblées par l'évolution, que chaque être humain partage : la tendance à faire confiance, le désir de coopérer, la sensibilité à l'autorité, l'aversion au conflit. Un employé qui tient la porte à un inconnu portant un gilet haute visibilité ne fait pas preuve de négligence — il fait preuve de civilité. C'est précisément cette normalité qui rend le social engineering si redoutable : il détourne des comportements sociaux sains pour atteindre des objectifs malveillants.

Aucune technologie ne peut éliminer le facteur humain. Les pare-feux bloquent des paquets, les antivirus détectent des signatures, les systèmes de détection d'intrusion analysent du trafic — mais aucun de ces dispositifs ne peut empêcher un ingénieur R&D de répondre à un faux recruteur sur LinkedIn, ni un comptable de valider un virement demandé par une voix qui ressemble à celle du directeur général. La surface d'attaque humaine n'est pas un résidu de mauvaise hygiène informatique : c'est une constante structurelle de toute organisation qui emploie des êtres humains.

Cette constante ne signifie pas que la défense est impossible. Elle signifie que la défense ne peut pas reposer uniquement sur la technologie. La résilience d'une organisation face au social engineering se construit sur trois piliers : la sensibilisation ciblée (comprendre les mécanismes, pas réciter des règles), les processus vérifiés (double validation, callback, séparation des tâches) et la culture de sécurité (un environnement où signaler un doute est valorisé, pas puni). Le présent cours développe ces trois piliers dans leur dimension offensive et défensive.

### 1.2 Le social engineering dans le spectre des menaces

Le social engineering n'est pas synonyme de phishing. Le phishing est un vecteur — le plus visible, le plus documenté, le plus mesuré — mais il ne représente qu'une fraction du spectre. Le social engineering est un corpus structuré de techniques qui couvre l'ensemble des interactions humaines exploitables : communication numérique (email, téléphone, messagerie), interaction physique (intrusion, tailgating, impersonation), relation interpersonnelle (élicitation, cultivation, recrutement).

Les chiffres sont sans ambiguïté. Selon le Verizon Data Breach Investigations Report (DBIR), le facteur humain est impliqué dans environ 68 % des violations de données confirmées. Le rapport Unit 42 2025 de Palo Alto Networks confirme que plus d'un tiers des cas de réponse à incident traités au cours de l'année écoulée ont débuté par une tactique de social engineering — sans zero-day, sans malware sophistiqué, mais par l'exploitation de la confiance. Les pertes financières liées au seul BEC (Business Email Compromise) dépassent les 2,9 milliards de dollars aux États-Unis selon l'IC3/FBI, ce qui en fait la catégorie de cybercriminalité la plus coûteuse, loin devant les ransomwares en termes de pertes directes.

L'évolution de la menace est marquée par deux tendances convergentes. D'une part, l'industrialisation : les campagnes de phishing sont automatisées, les kits de phishing-as-a-service sont accessibles à des acteurs peu qualifiés, les techniques de contournement MFA (Evilginx, reverse proxy) se démocratisent. D'autre part, la sophistication ciblée : les groupes APT investissent des semaines dans la construction de relations de confiance avant l'envoi du premier payload, les deepfakes vocaux permettent des fraudes au président d'un réalisme inédit, et l'IA générative permet de produire des leurres personnalisés à l'échelle.

### 1.3 Le spectre du social engineering : matrice de positionnement

Pour naviguer dans ce cours, il est essentiel de distinguer clairement les différentes dimensions du social engineering et les disciplines connexes. La matrice ci-dessous pose les fondations terminologiques du cours.

| Dimension | Définition | Exemples | Chapitre(s) de référence |
|---|---|---|---|
| **Social engineering numérique** | Obtenir un accès, une action ou une information par manipulation via un canal numérique | Phishing, vishing, smishing, BEC, quishing | Ch.6-11 |
| **Social engineering physique** | Obtenir un accès physique ou une information par manipulation en personne | Tailgating, impersonation, dumpster diving | Ch.12-16 |
| **Élicitation** | Extraction d'information dans une conversation apparemment normale — la cible ne sait pas qu'elle est interrogée | Conversation de salon, faux recruteur, debriefing informel | Ch.14, 22, 28 |
| **HUMINT** | Collecte structurée de renseignement par des sources humaines — relation dans la durée | Repérage, développement, recrutement, exploitation d'une source | Ch.3, 17 |
| **Contre-ingénierie sociale** | Détection, interruption, signalement, protection et résilience face aux tentatives de SE | Contre-élicitation, formation, processus de vérification, culture de signalement | Ch.21-25 |
| **Red team SE** | Simulation autorisée de techniques de SE dans un cadre contractuel et éthique | Test d'intrusion physique, campagne de phishing contrôlée | Ch.19-20 |
| **Attaquant réel** | Exploitation malveillante des mêmes techniques sans cadre ni consentement | APT, BEC criminel, fraude, espionnage | Ch.17-18 |

Cette matrice n'est pas décorative. Elle structure l'ensemble du cours. Chaque technique abordée sera positionnée sur ce spectre, avec les implications éthiques et juridiques correspondantes. La même technique d'élicitation utilisée par un red teamer dans un cadre autorisé et par un agent de renseignement étranger sans consentement de la cible relève de deux réalités juridiques et éthiques totalement différentes, même si le mécanisme psychologique exploité est identique.

### 1.4 Éthique et cadre légal : la ligne entre test autorisé et manipulation

Le social engineering opère dans un espace éthique et juridique sous tension permanente. Les mêmes techniques qui permettent à un red teamer de tester les défenses d'une organisation sont celles qu'utilise un attaquant réel pour compromettre cette même organisation. La différence ne réside pas dans la technique, mais dans le cadre.

**Le cadre du test autorisé.** Un test de social engineering légitime repose sur quatre piliers indissociables. Premièrement, une autorisation écrite explicite signée par un représentant habilité de l'organisation (généralement le dirigeant ou le RSSI, avec validation juridique). Cette lettre de mission doit définir le scope (quels sites, quels employés, quels vecteurs sont autorisés), la durée, les objectifs et les limites. Deuxièmement, un scope clairement borné : les techniques autorisées sont listées, les lignes rouges sont explicites. Troisièmement, un protocole d'urgence : un « safe word » ou un contact de référence permettant au red teamer de s'identifier immédiatement s'il est intercepté ou si une situation dégénère. Quatrièmement, une clause de confidentialité des résultats individuels : les résultats du test évaluent les processus et la culture, pas les individus.

**Les limites absolues.** Même dans un cadre autorisé, certaines techniques sont proscrites. Le red teamer ne doit jamais exploiter des vulnérabilités personnelles réelles (problèmes de santé, difficultés financières, addictions, situations familiales). Il ne doit jamais recourir au chantage, à l'intimidation réelle, ni créer de détresse psychologique durable. Il ne doit jamais établir de relation intime ou affective avec une cible dans le cadre d'un test. Ces limites ne sont pas des recommandations : ce sont des lignes rouges non négociables qui distinguent le professionnel éthique du manipulateur.

**Le cadre juridique.** En droit français, le social engineering malveillant relève de plusieurs infractions : escroquerie (art. 313-1 du Code pénal), usurpation d'identité (art. 226-4-1), accès frauduleux à un système de traitement automatisé de données (art. 323-1 et suivants), atteinte au secret des correspondances. Le RGPD encadre strictement le traitement des données personnelles collectées, y compris dans un contexte de test autorisé. Le droit du travail impose des limites sur la surveillance des employés et les sanctions disciplinaires pouvant résulter d'un test (le cadre juridique complet est détaillé au Ch.19 et à l'Annexe F).

### 1.5 Articulation avec la bibliothèque

Ce cours s'inscrit dans un écosystème de cours spécialisés avec lesquels il entretient des renvois croisés explicites, sans créer de dépendance forte. Chaque cours reste exploitable seul.

Le cours *Cybersécurité du quotidien* adopte le prisme de la victime : reconnaître une tentative de phishing, protéger ses comptes, adopter les bons réflexes. Le présent cours explique comment ces attaques sont construites, pourquoi elles fonctionnent et comment les tester et les détecter à l'échelle d'une organisation.

Le cours *Intelligence économique* traite l'HUMINT d'entreprise légal : collecte d'information en salon professionnel, debriefing de collaborateurs, veille concurrentielle. Le présent cours approfondit les techniques d'élicitation, les étend au contexte du renseignement étatique et traite la dimension contre-ingérence.

Le cours *APT* traite le social engineering comme vecteur d'accès initial dans les campagnes de menaces avancées. Le présent cours détaille les techniques elles-mêmes, leur construction et leur défense.

Le cours *OSINT Mastery* fournit les méthodes de reconnaissance en sources ouvertes. Le présent cours montre comment cette reconnaissance alimente directement la crédibilité des pretextes de social engineering (voir Ch.5).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 1**
>
> **Contexte.** Nathan Vilar, 32 ans, consultant en sécurité offensive (red team) au sein du cabinet de conseil en cybersécurité CyberEdge Partners, reçoit un appel de Lucie Ferraro, RSSI d'Helios Aéronautique. Helios est un équipementier aéronautique de 1 200 employés, réparti sur trois sites en France : siège social à Toulouse (direction, commercial, RH, finance), site de production à Bordeaux (atelier, logistique, qualité) et bureau R&D à Paris (ingénierie, prototypage, brevets).
>
> **Le mandat.** Helios vient de remporter un contrat de sous-traitance pour un programme de défense européen. Le comité de direction, alerté par les retours de la DGSI sur les risques d'ingérence économique dans le secteur aéronautique, décide de mandater un test d'intrusion physique et social engineering complet. La lettre de mission est signée par le DG (Marc Tessier) et la RSSI. Le scope couvre les trois sites, tous les employés (y compris le comité de direction), et toutes les techniques de social engineering sauf le chantage et l'exploitation de vulnérabilités personnelles (santé, finance, vie privée). Durée : 6 semaines. Budget : 45 000 € HT.
>
> Nathan constitue son équipe : lui-même (lead, élicitation, intrusion physique), Yasmine Berrada (phishing, vishing, OSINT) et Thomas Schaeffer (infrastructure technique, implants). Première étape : la reconnaissance.

---

## Chapitre 2 — Psychologie de la manipulation : les mécanismes profonds

### 2.1 Les principes de Cialdini approfondis

Robert Cialdini a identifié six principes fondamentaux de l'influence, documentés dans *Influence: The Psychology of Persuasion* (1984) puis enrichis dans *Pre-Suasion* (2016) avec un septième principe (l'unité). Ces principes ne sont pas des « astuces » : ce sont des mécanismes cognitifs profonds, forgés par l'évolution, que tout être humain partage. Comprendre ces mécanismes est la base de toute pratique de social engineering, qu'elle soit offensive (exploitation) ou défensive (détection).

**La réciprocité.** Quand quelqu'un fait quelque chose pour nous, nous ressentons une obligation de rendre la pareille. Ce mécanisme est si puissant qu'il fonctionne même lorsque le « cadeau » initial est non sollicité ou de faible valeur. En social engineering, la réciprocité est exploitée de multiples façons : le faux technicien IT qui « aide » un employé à résoudre un problème (réel ou fabriqué) avant de demander un accès ; le « recruteur » LinkedIn qui partage un article intéressant ou une opportunité professionnelle avant de poser des questions sur les projets internes ; l'attaquant qui fournit un mot de passe « pour vérification » afin d'obtenir le vrai mot de passe en retour (le partage réciproque). La défense repose sur la capacité à reconnaître les obligations artificiellement créées et à les refuser sans culpabilité.

**L'engagement et la cohérence.** Une fois qu'un individu s'est engagé dans une direction — même par un acte minime — il tend à rester cohérent avec cet engagement initial. C'est le fondement de la technique du « pied dans la porte » (détaillée au Ch.15) : obtenir un premier « oui » (une petite demande anodine) augmente considérablement la probabilité d'obtenir un « oui » à une demande plus importante. En vishing, l'attaquant commence par des questions de vérification simples (« pouvez-vous confirmer votre nom ? ») avant d'escalader vers des demandes sensibles (« et votre identifiant employé ? »). Chaque réponse renforce l'engagement de la cible dans la conversation et rend le refus psychologiquement plus coûteux.

**La preuve sociale.** En situation d'incertitude, les individus se tournent vers le comportement des autres pour guider le leur. Si « tout le monde le fait », cela doit être correct. L'attaquant exploite ce principe en invoquant des précédents (« vos collègues du 3e étage ont déjà fait la mise à jour »), en simulant une activité normale (se comporter comme si l'on appartenait à l'environnement) ou en créant de faux consensus (« la direction a validé cette procédure »). La preuve sociale est particulièrement efficace dans les grandes organisations où les employés ne connaissent pas personnellement tous leurs collègues et où le comportement des autres sert de boussole sociale.

**L'autorité.** La tendance à obéir aux figures d'autorité est l'un des mécanismes les plus documentés en psychologie sociale, depuis les expériences de Stanley Milgram (1963). En social engineering, l'autorité n'a pas besoin d'être réelle — elle doit être perçue. Un titre (« directeur technique »), un uniforme (gilet haute visibilité, costume), un jargon technique maîtrisé, un ton assuré suffisent à activer le mécanisme de déférence. La fraude au président exploite directement ce principe : l'employé reçoit un ordre de virement d'une personne qu'il perçoit comme son supérieur hiérarchique, et la chaîne de commandement fait le reste.

**La sympathie (liking).** Nous sommes plus enclins à accéder aux demandes de personnes que nous trouvons sympathiques. La sympathie est activée par la similarité perçue (mêmes intérêts, même parcours, même langage), la flatterie, la familiarité et l'attractivité physique. En élicitation, l'attaquant construit un rapport rapide en identifiant des points communs (« vous aussi vous avez fait l'INSA ? »), en validant les opinions de la cible et en adoptant un langage corporel ouvert et accueillant. La sympathie désarme la vigilance parce qu'elle active un mode de traitement cognitif coopératif plutôt que critique.

**La rareté.** Ce qui est rare est perçu comme plus précieux. L'urgence temporelle (« cette offre expire dans 2 heures ») et la disponibilité limitée (« il ne reste que 3 places ») sont les leviers les plus courants. En phishing, l'urgence artificielle est le levier le plus fréquemment utilisé : « votre compte sera désactivé dans 24h », « validation requise avant 17h ». En vishing, le temps réel amplifie l'effet : la cible n'a pas le temps de réfléchir, de vérifier, de consulter un collègue. La rareté fonctionne parce qu'elle active le système de pensée rapide (System 1 de Kahneman) au détriment du système analytique (System 2).

### 2.2 Au-delà de Cialdini : les leviers complémentaires

Les six principes de Cialdini constituent le socle, mais le praticien de social engineering dispose de leviers complémentaires tout aussi opérationnels.

**La curiosité.** L'être humain est câblé pour résoudre les lacunes informationnelles. Un email dont l'objet est « Vos résultats d'évaluation annuelle » ou « Photos de la soirée d'entreprise » exploite la curiosité — le clic n'est pas un acte de négligence, c'est une réponse cognitive automatique. Les clés USB déposées dans un parking (baiting) exploitent le même mécanisme : « qu'y a-t-il dessus ? ».

**La peur.** La peur court-circuite l'analyse rationnelle. Les scareware (« votre ordinateur est infecté ! ») et les emails menaçant une désactivation de compte exploitent la peur de perdre l'accès, de subir une sanction, d'être exposé. La peur est un levier particulièrement efficace lorsqu'elle est combinée avec l'urgence : la cible doit agir vite pour éviter une conséquence négative, ce qui laisse peu de place à la vérification.

**La fatigue décisionnelle.** À mesure que la journée avance et que les décisions s'accumulent, la qualité du jugement se dégrade. Les attaquants le savent : les campagnes de phishing envoyées le lundi matin (accumulation d'emails du week-end) ou le vendredi après-midi (fatigue de fin de semaine, envie de conclure rapidement) ont des taux de réussite significativement supérieurs à celles envoyées à d'autres moments.

**L'ego et la flatterie.** Être reconnu comme expert, comme la personne indispensable, comme le seul à comprendre un système — cette flatterie est un puissant désinhibiteur. En élicitation, affirmer « vous êtes la seule personne qui comprenne vraiment ce système » transforme la cible en source volontaire. La flatterie fonctionne même lorsqu'elle est perçue comme telle, parce que l'ego apprécie la reconnaissance indépendamment de son authenticité.

**Le sentiment d'obligation professionnelle.** Les cultures d'entreprise qui valorisent la réactivité, le service client ou la disponibilité créent un terreau fertile pour le social engineering. Un helpdesk formé à « résoudre le problème du client le plus vite possible » est structurellement vulnérable au pretexting : le technicien qui refuse d'aider un « collègue bloqué » viole la norme professionnelle qu'on lui a inculquée.

### 2.3 Les biais cognitifs en profondeur

Au-delà des principes d'influence, plusieurs biais cognitifs rendent les individus particulièrement vulnérables au social engineering.

**Le biais d'optimisme** (« ça n'arrive qu'aux autres ») est le plus destructeur en matière de sensibilisation. Les employés qui ont suivi une formation reconnaissent le phishing en théorie, mais croient sincèrement qu'ils ne se feront pas piéger en pratique. Ce biais explique pourquoi les campagnes de sensibilisation par quiz ont un impact limité : réussir un quiz ne modifie pas la perception du risque personnel.

**Le biais de confirmation** amène les individus à interpréter les informations de manière cohérente avec leurs croyances préexistantes. Si un employé s'attend à recevoir un email de la RH sur les congés, il sera moins vigilant face à un phishing qui utilise ce prétexte. L'attaquant ne crée pas la crédibilité ex nihilo — il s'appuie sur les attentes existantes de la cible.

**L'effet de halo** fait qu'une impression positive sur un attribut (apparence soignée, titre prestigieux, langage professionnel) se généralise à l'ensemble de la personne. Le red teamer en costume qui arrive avec un clipboard et un badge d'entreprise bénéficie de l'effet de halo : son apparence professionnelle le rend crédible avant même qu'il n'ouvre la bouche.

**Le biais de normalité** (« ce comportement est normal dans notre entreprise ») explique pourquoi le tailgating fonctionne si bien. Dans une entreprise où « on tient la porte » est la norme sociale, refuser de tenir la porte à un inconnu est un acte de déviance sociale. L'attaquant ne pirate pas un système — il s'insère dans un système de normes sociales existant.

### 2.4 La charge cognitive comme vulnérabilité

La vigilance n'est pas un état permanent. C'est une ressource limitée qui se dégrade sous l'effet du stress, de la fatigue, du multitâche et de la surcharge informationnelle. Un employé qui gère simultanément une deadline projet, 200 emails non lus et un appel téléphonique inattendu n'a tout simplement pas les ressources cognitives nécessaires pour analyser critiquement une demande suspecte.

Les attaquants créent artificiellement la surcharge cognitive. Le visher qui appelle avec une urgence fabriquée (« votre compte a été compromis, il faut agir maintenant ») ne transmet pas seulement une fausse information — il active le mode de traitement d'urgence du cerveau, qui privilégie la rapidité d'action au détriment de l'analyse. L'email de phishing qui arrive pendant une réunion importante sera traité en mode « multi-tâche » avec une attention réduite. Le pretexte qui combine autorité et urgence (« le DG a besoin de ce virement avant 17h ») crée une double pression qui réduit drastiquement la capacité de jugement.

Cette réalité a une implication directe pour la défense : les processus de sécurité qui reposent sur la vigilance individuelle sont structurellement fragiles. Un processus robuste est un processus qui fonctionne même quand l'individu est fatigué, stressé ou distrait — c'est-à-dire un processus qui impose des vérifications automatiques (callback, double validation) plutôt que de compter sur l'analyse critique de chaque demande.

### 2.5 Persuasion et manipulation : le continuum éthique

La distinction entre persuasion et manipulation n'est pas binaire — c'est un continuum. À une extrémité, la persuasion légitime : un commercial qui argumente sur les mérites de son produit, un manager qui motive son équipe, un médecin qui convainc un patient de suivre un traitement. À l'autre extrémité, la coercition : menaces, chantage, violence. Entre les deux, un spectre de pratiques dont la légitimité dépend du contexte, de l'intention et du consentement.

L'influence se situe au milieu de ce spectre : elle oriente le comportement de l'autre en utilisant des leviers psychologiques, sans que l'autre soit nécessairement conscient de ces leviers. La manipulation va plus loin : elle oriente le comportement de l'autre contre ses propres intérêts, en exploitant des vulnérabilités cognitives ou émotionnelles, souvent avec un élément de tromperie.

Pour le praticien de social engineering, cette distinction a des implications concrètes. Le red teamer utilise la manipulation dans un cadre autorisé et borné : les mêmes techniques, utilisées par un attaquant réel, constituent des délits. Le formateur en sensibilisation utilise la compréhension de la manipulation pour enseigner la détection. L'analyste en contre-ingénierie sociale utilise la connaissance des leviers pour identifier les tentatives en cours. Dans tous les cas, la compréhension profonde des mécanismes est un prérequis — mais la façon dont cette compréhension est utilisée détermine si le praticien est du côté de la défense ou de l'attaque.

---

## Chapitre 3 — Le HUMINT dans le monde du renseignement

### 3.1 Définition et cadre

HUMINT (Human Intelligence) désigne la collecte de renseignement par l'intermédiaire de sources humaines. C'est le plus ancien des « INTs » — bien avant l'existence de SIGINT (interception de communications), IMINT (imagerie satellite) ou OSINT (sources ouvertes), les espions recueillaient de l'information par la conversation, l'observation et la relation interpersonnelle. Le HUMINT reste, en 2025, irremplaçable pour certains types d'information : les intentions d'un décideur, les projets non encore documentés, les arbitrages internes d'une organisation, les vulnérabilités d'un processus qui n'apparaissent dans aucun système.

Le HUMINT ne se confond pas avec le social engineering, même si les deux disciplines partagent des techniques communes (élicitation, pretexting, rapport building). Le social engineering vise généralement un objectif tactique précis (obtenir un mot de passe, un accès, une action) dans un temps court. Le HUMINT s'inscrit dans une logique stratégique, souvent sur des mois ou des années, avec un objectif de collecte continue. Le social engineering peut être le premier acte d'une opération HUMINT, mais le HUMINT est un processus structuré qui va bien au-delà.

### 3.2 Le cycle HUMINT

Le cycle HUMINT suit une progression méthodique en cinq phases. Chaque phase a ses techniques, ses risques et ses contre-mesures.

**Le repérage (spotting).** C'est l'identification de cibles potentielles — des individus qui ont accès à l'information recherchée et qui présentent des facteurs de vulnérabilité exploitables. Le repérage repose massivement sur l'OSINT : profils LinkedIn, publications professionnelles, présence en conférence, réseau social. Un ingénieur R&D qui publie régulièrement sur ses projets, participe à des conférences internationales et affiche un réseau LinkedIn ouvert est une cible de repérage évidente. Le repérage évalue aussi les facteurs de motivation : insatisfaction professionnelle, ambition bloquée, difficultés financières, ego surdimensionné.

**Le développement (development).** C'est l'établissement du contact et la construction progressive de la relation. Le « developmental contact » est conçu pour paraître naturel : rencontre en conférence, connexion LinkedIn via un intérêt commun, invitation à un séminaire, proposition de collaboration académique. L'objectif n'est pas d'obtenir de l'information immédiatement — c'est de créer un lien de confiance qui sera exploité ultérieurement. La patience est l'arme fondamentale du HUMINT : des semaines ou des mois de contacts apparemment anodins avant la première demande significative.

**Le recrutement (recruitment).** C'est la transformation du contact en source active. Le recrutement peut être explicite (la source sait qu'elle collabore avec un service de renseignement) ou implicite (la source livre de l'information sans réaliser la nature réelle de son interlocuteur). Le recrutement exploite les leviers classiques du modèle MICE : Money (rémunération), Ideology (adhésion à une cause), Coercion (chantage, compromission), Ego (reconnaissance, flatterie). Dans la pratique contemporaine, le recrutement par l'ego et la rémunération est bien plus courant que le recrutement par la coercition — cette dernière étant plus risquée et moins stable.

**L'exploitation.** C'est la phase de collecte structurée. La source fournit de l'information selon un cadre défini par le traitant : questions ciblées, documents, accès à des réunions, identification d'autres cibles potentielles. L'exploitation est gérée avec soin pour ne pas « brûler » la source (ne pas la mettre en danger en demandant trop ou trop vite).

**La gestion (handling).** C'est la maintenance de la relation et de la sécurité opérationnelle : canaux de communication sécurisés, rendez-vous discrets, rémunération, soutien psychologique, gestion des crises (si la source est soupçonnée). La gestion est souvent la phase la plus longue et la plus délicate du cycle HUMINT.

### 3.3 Les services de renseignement et l'élicitation d'entreprise

Les services de renseignement étrangers ciblent activement les employés des entreprises stratégiques et des administrations. Ce n'est pas une menace théorique : la DGSI publie régulièrement des alertes sur les tentatives d'ingérence économique visant les entreprises françaises dans les secteurs de la défense, de l'aéronautique, de l'énergie, des télécommunications et de la recherche.

Les vecteurs de contact les plus fréquents sont les salons professionnels internationaux (où les cibles sont accessibles, ouvertes au networking et éloignées de leur cadre de sécurité habituel), les plateformes professionnelles en ligne (LinkedIn est devenu le terrain de chasse principal pour le repérage et le contact initial), les invitations à des séminaires académiques ou professionnels dans certains pays, et les approches par des « journalistes », « consultants » ou « recruteurs » dont l'identité est difficile à vérifier.

Les signaux d'alerte d'une tentative d'élicitation par un service de renseignement incluent : des questions inhabituellement spécifiques sur des projets ou des technologies internes, une insistance à déplacer la conversation vers un canal privé (WhatsApp, Signal), une progression relationnelle rapide (invitation à dîner dès le premier contact), des propositions de rémunération pour des « consultations » ou des « expertises » vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et un profil difficile à vérifier (entreprise opaque, parcours incohérent, photos de profil douteuses). Les techniques de contre-élicitation sont détaillées au Ch.22.

### 3.4 HUMINT d'entreprise vs HUMINT de renseignement

L'HUMINT d'entreprise — collecte d'information concurrentielle par des moyens humains légaux — partage des techniques avec l'HUMINT de renseignement (élicitation, observation, debriefing) mais opère dans un cadre juridique et éthique radicalement différent.

L'HUMINT d'entreprise légal se limite à la collecte d'informations disponibles ou accessibles par des moyens licites : conversations en salon professionnel (sans faux pretexte), debriefing de collaborateurs après un événement, analyse des déclarations publiques de concurrents, observation du marché. Il ne recourt ni à la tromperie, ni à l'usurpation d'identité, ni au recrutement de sources internes chez un concurrent. Le cadre est celui de la veille concurrentielle et de l'intelligence économique (renvoi vers le cours IE, Ch.8).

La ligne de démarcation est claire dans le principe, mais parfois floue dans la pratique. Une conversation spontanée en conférence où un concurrent partage volontairement des informations est de l'intelligence économique légitime. La même conversation, si elle est orchestrée sous un faux pretexte (se faire passer pour un journaliste ou un universitaire pour obtenir des informations concurrentielles), bascule dans l'illégalité.

### 3.5 Le rôle de l'OSINT dans le HUMINT

La reconnaissance en sources ouvertes est la phase préparatoire obligatoire de toute opération HUMINT. Aucun professionnel sérieux — qu'il soit red teamer, analyste en contre-ingérence ou agent de renseignement — n'aborde une cible sans avoir préalablement collecté et analysé toute l'information disponible en source ouverte.

L'OSINT alimente le HUMINT à chaque étape du cycle. En phase de repérage, elle identifie les cibles potentielles et évalue leur accessibilité (profil LinkedIn ouvert vs fermé, présence en conférence, publications). En phase de développement, elle fournit les éléments de personnalisation du contact (intérêts communs, parcours partagé, sujets de conversation). En phase d'exploitation, elle permet de formuler des questions d'élicitation pertinentes et de valider les réponses obtenues.

La qualité de la reconnaissance OSINT détermine directement la crédibilité du pretexte et donc le taux de succès de l'opération de social engineering. Un phishing générique envoyé à 10 000 adresses aura un taux de clic de 2 à 5 %. Un spear-phishing construit à partir d'une reconnaissance OSINT approfondie (terminologie interne, noms de projets, prestataires identifiés) aura un taux de clic de 20 à 40 %. La reconnaissance est le multiplicateur de force du social engineering. Les méthodes de reconnaissance OSINT sont détaillées au Ch.5 (renvoi vers le cours OSINT Mastery pour la profondeur méthodologique).

---

## Chapitre 4 — Les profils vulnérables et les facteurs de risque

### 4.1 Qui est vulnérable ? Tout le monde

Le mythe de la victime naïve est l'un des plus dangereux en social engineering. Il crée un faux sentiment de sécurité chez les individus qui se considèrent trop informés, trop intelligents ou trop expérimentés pour être piégés. La réalité est exactement inverse : les experts se font piéger aussi souvent que les novices — simplement par des techniques adaptées à leur profil.

Un RSSI qui détectera un phishing grossier peut se laisser piéger par un spear-phishing hautement personnalisé qui exploite son ego professionnel (« votre expertise est reconnue dans le secteur, nous aimerions vous inviter comme keynote speaker »). Un ingénieur R&D qui ignore les emails suspects peut succomber à une élicitation de face-à-face menée par un faux chercheur universitaire qui parle son langage technique. Un dirigeant qui se méfie des appels inconnus peut être vulnérable à une fraude au président menée par deepfake vocal lors d'une visioconférence apparemment légitime.

La vulnérabilité n'est pas une caractéristique personnelle — c'est une situation. Le même individu peut être vigilant dans un contexte et vulnérable dans un autre. Comprendre les facteurs de risque contextuels est bien plus utile que de profiler des « victimes types ».

### 4.2 Les facteurs de risque contextuels

Certaines situations augmentent significativement la vulnérabilité au social engineering, indépendamment de la compétence ou de l'intelligence de l'individu.

**Le nouveau poste.** Un employé récemment arrivé ne connaît pas encore les procédures, les visages, les habitudes de l'organisation. Il est en mode d'adaptation et d'apprentissage, ce qui le rend réceptif aux demandes de personnes qui semblent connaître l'entreprise mieux que lui. Le pretexting classique « je suis de l'IT, je dois configurer votre poste » est particulièrement efficace sur les nouveaux arrivants.

**Le voyage professionnel.** L'isolement géographique, la désorientation culturelle, le décalage horaire et l'absence du cadre de sécurité habituel (collègues de confiance, procédures connues) créent une fenêtre de vulnérabilité. Les services de renseignement exploitent systématiquement les voyages professionnels dans certains pays : chambre d'hôtel surveillée, contacts « spontanés » dans les bars d'hôtel, invitations à des événements sociaux (voir Ch.22 pour les contre-mesures).

**Le salon professionnel.** L'ouverture sociale est la norme : échanger des cartes de visite, discuter de ses projets, nouer des contacts est le but même de la participation. Cette ouverture crée un environnement idéal pour l'élicitation : les barrières sociales habituelles sont abaissées, la curiosité intellectuelle est stimulée, et le contexte professionnel légitime les questions sur l'activité de l'entreprise.

**La période de stress ou de conflit professionnel.** Un employé en conflit avec sa hiérarchie, menacé de licenciement, sous-estimé ou frustré dans ses ambitions est plus réceptif aux approches extérieures — qu'il s'agisse d'un faux recruteur qui propose une « opportunité de carrière » ou d'un interlocuteur qui offre reconnaissance et écoute. Ce facteur est l'un des leviers classiques du recrutement de sources par les services de renseignement.

**La transition de carrière.** Un employé en fin de contrat, en pré-retraite ou en recherche active d'emploi est structurellement réceptif aux propositions professionnelles — et donc aux approches de faux recruteurs.

### 4.3 Le modèle MICE et ses extensions

Le modèle MICE (Money, Ideology, Coercion, Ego) est le cadre classique du renseignement pour analyser les motivations d'un individu à collaborer comme source. Il reste pertinent en 2025, mais il a été étendu pour mieux refléter la diversité des leviers.

**Money.** La motivation financière reste un levier puissant, particulièrement pour les individus qui perçoivent un décalage entre leur contribution et leur rémunération, ou qui traversent des difficultés financières. Les « consultations rémunérées » proposées par de faux cabinets de conseil sont un vecteur classique.

**Ideology.** L'adhésion à une cause — politique, environnementale, religieuse, nationaliste — peut motiver la divulgation d'informations. Ce levier est moins fréquent en contexte d'entreprise qu'en contexte étatique, mais il existe (lanceurs d'alerte convaincus de servir l'intérêt public, employés politisés ciblés par des acteurs étrangers partageant apparemment les mêmes convictions).

**Coercion.** Le chantage, la compromission (kompromat) et les menaces constituent le levier le plus risqué et le moins stable — une source recrutée par la coercition est une source hostile qui cherchera à se libérer. En contexte de red team, ce levier est formellement interdit.

**Ego.** La flatterie, la reconnaissance, le sentiment d'être un interlocuteur privilégié sont des leviers extrêmement efficaces, en particulier auprès d'experts techniques qui manquent de reconnaissance dans leur organisation. Le modèle RASCLS (Reciprocity, Authority, Scarcity, Commitment, Liking, Social proof) étend l'analyse des leviers aux principes d'influence de Cialdini, offrant une grille d'analyse plus fine.

**Revenge.** La vengeance est un levier ajouté par les praticiens contemporains : un employé qui se sent trahi par son employeur (licenciement perçu comme injuste, promotion ratée, conflit avec la hiérarchie) peut être motivé par le désir de « punir » l'organisation.

### 4.4 Les insiders involontaires

La distinction entre insider malveillant et insider involontaire est fondamentale. L'insider malveillant agit délibérément contre les intérêts de son organisation (vol de données, sabotage). L'insider involontaire est un employé légitime, loyal et bien intentionné, qui divulgue des informations ou accorde des accès sans réaliser qu'il est manipulé.

L'insider involontaire est la cible privilégiée du social engineering et de l'élicitation. Il ne sait pas qu'il participe à une opération hostile. Le « recruteur » LinkedIn avec qui il échange depuis trois mois lui semble être un contact professionnel légitime. Le « technicien de maintenance » à qui il a tenu la porte dans le couloir avait un badge qui ressemblait au bon. L'email qui lui demandait de « mettre à jour ses identifiants » venait d'une adresse qui ressemblait à celle de la DSI.

La détection des insiders involontaires passe par la formation (reconnaître les signaux d'élicitation), les processus (vérification des demandes sensibles) et la surveillance comportementale (détection d'accès anormaux), mais aussi par une culture où le signalement d'un doute est encouragé sans conséquence négative pour celui qui signale.

### 4.5 Le profilage éthique en contexte red team

Dans un test de social engineering autorisé, le red teamer évalue la vulnérabilité des individus pour déterminer les cibles les plus probables et les pretextes les plus efficaces. Ce profilage est nécessaire — mais il doit respecter des limites strictes.

**Ce qu'on observe et exploite** : le rôle dans l'organisation (accès, responsabilités), le comportement professionnel observable (présence en conférence, publications, activité LinkedIn), les habitudes de travail visibles (horaires, déplacements, habitudes de pause), le niveau de familiarité avec les procédures de sécurité.

**Ce qu'on n'observe pas et n'exploite jamais** : les problèmes personnels (santé, finances, vie sentimentale, addictions), les situations de vulnérabilité individuelle (deuil, divorce, problèmes familiaux), les opinions politiques ou religieuses, les données sensibles au sens du RGPD.

La ligne est claire dans le principe, mais elle peut être floue en pratique. Un red teamer qui découvre, au cours de sa reconnaissance OSINT, qu'un employé traverse un divorce difficile (information visible sur les réseaux sociaux) ne doit pas utiliser cette information pour personnaliser son approche, même si un attaquant réel le ferait. Le red teamer teste les défenses de l'organisation, pas les faiblesses personnelles des individus.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 2**
>
> **Phase de reconnaissance.** Nathan et Yasmine lancent la reconnaissance OSINT sur Helios Aéronautique. En trois jours, ils collectent un volume d'information considérable.
>
> **LinkedIn** : 350 profils identifiés, dont 42 cadres et 28 ingénieurs R&D. L'organigramme est reconstitué à 80 %. Le DSI s'appelle Frédéric Morin. Le responsable de la production à Bordeaux est Jean-Marc Duval. Trois ingénieurs R&D publient régulièrement sur des conférences techniques. Le prestataire de maintenance informatique est identifié grâce à un post LinkedIn d'un de ses techniciens mentionnant une intervention chez Helios.
>
> **Offres d'emploi** : 12 annonces en cours révèlent la stack technique (Microsoft 365, Azure AD, SAP, SolidWorks, un ERP maison) et les compétences recherchées (ingénieur simulation, technicien qualité, développeur .NET).
>
> **Réseaux sociaux personnels** : photos de la soirée d'entreprise sur Instagram → badges visibles sur 4 photos (format, couleur, logo, puce RFID apparente). Post Facebook d'un employé : « Super formation incendie ce matin, on a tous évacué par la sortie Est ». Géolocalisation de posts TikTok par deux jeunes employés → identification de l'entrée fumoir côté parking.
>
> **Site web et presse** : communiqué de presse sur le contrat de sous-traitance défense (confirme l'enjeu stratégique), photos du siège (architecture, entrées, parking), rapport RSE mentionnant le prestataire de ménage et le traiteur de la cantine.
>
> Nathan rédige le dossier de reconnaissance et commence à construire les pretextes.

---

## Chapitre 5 — Reconnaissance et OSINT préparatoire

### 5.1 L'OSINT comme préalable obligatoire

Toute opération de social engineering commence par la reconnaissance. C'est un axiome, pas une recommandation. La qualité de l'information collectée en phase de reconnaissance détermine directement la crédibilité du pretexte, le choix de la cible et le taux de succès de l'opération. Un pretexte construit sans reconnaissance est un pretexte générique — et un pretexte générique échoue face à un employé moyennement vigilant.

L'OSINT (Open Source Intelligence) fournit au social engineer trois types d'information critiques : l'information organisationnelle (structure, processus, culture d'entreprise), l'information individuelle (profils, intérêts, vulnérabilités professionnelles des cibles potentielles) et l'information technique (systèmes utilisés, configurations de sécurité, vecteurs d'attaque potentiels). Le cours OSINT Mastery de la bibliothèque couvre en profondeur les méthodologies de collecte — le présent chapitre se concentre sur l'application spécifique de l'OSINT au social engineering.

### 5.2 Reconnaissance organisationnelle

La reconnaissance organisationnelle vise à comprendre l'entreprise cible comme un système : sa structure, ses processus, sa culture, ses partenaires et ses vulnérabilités structurelles.

**L'organigramme.** LinkedIn est la source principale. En croisant les profils des employés, le red teamer reconstitue l'organigramme fonctionnel : qui dirige quoi, qui reporte à qui, quels sont les liens hiérarchiques et fonctionnels. Les signatures d'emails (collectées via des interactions légitimes ou des fuites) complètent le tableau. L'organigramme identifie les cibles à haute valeur (accès à des informations sensibles, pouvoir de décision sur les virements) et les cibles à basse résistance (nouveaux arrivants, postes à fort turnover, prestataires).

**La terminologie interne.** Chaque organisation a son jargon : noms de projets, acronymes internes, noms de systèmes, appellations de services. Maîtriser cette terminologie est un marqueur de crédibilité majeur. Un phishing qui mentionne « le projet Vega » ou « la migration vers SAP S/4HANA » sera infiniment plus crédible qu'un email générique. Les sources de terminologie incluent les offres d'emploi (qui décrivent les outils et les projets), les publications des employés (articles LinkedIn, présentations en conférence), les documents publics (rapports annuels, communiqués de presse) et les fuites involontaires (photos de tableaux blancs sur les réseaux sociaux).

**Les prestataires et fournisseurs.** Les prestataires sont des vecteurs d'intrusion majeurs — ils ont souvent un accès physique ou logique aux locaux et aux systèmes sans être soumis aux mêmes contrôles que les employés internes. Identifier les prestataires (IT, ménage, maintenance, restauration, sécurité) permet de construire des pretextes d'impersonation crédibles. Les sources incluent LinkedIn (employés des prestataires mentionnant leurs clients), les réseaux sociaux (photos de véhicules de prestataires sur le parking), les offres d'emploi des prestataires eux-mêmes et les documents publics (appels d'offres, marchés publics pour les entreprises du secteur public).

**Le calendrier.** Les périodes de vulnérabilité sont prévisibles : fin de trimestre (pression sur les résultats), période de vacances (effectifs réduits, intérimaires moins formés), événements d'entreprise (soirées, séminaires — ouverture sociale accrue), audits prévus (les employés s'attendent à des demandes inhabituelles).

### 5.3 Reconnaissance individuelle

La reconnaissance individuelle cible les personnes spécifiques qui seront approchées pendant l'opération.

**LinkedIn.** C'est la mine d'or du social engineer. Un profil LinkedIn complet fournit : le poste exact et les responsabilités, le parcours professionnel (ancienneté dans l'entreprise, postes précédents), les compétences techniques (outils maîtrisés, certifications), le réseau professionnel (collègues, anciens collègues, contacts communs exploitables pour le name-dropping), les publications et partages (intérêts professionnels, opinions, expertise revendiquée), les recommandations (relations de confiance identifiées) et la photo (reconnaissance visuelle pour l'intrusion physique). La restriction de visibilité d'un profil LinkedIn n'est que partiellement efficace : les noms, les titres et les entreprises restent souvent visibles même pour les profils restreints.

**Réseaux sociaux personnels.** Facebook, Instagram, Twitter/X, TikTok fournissent des informations complémentaires sur les centres d'intérêt (sport, voyage, cuisine — autant de sujets pour construire un rapport), les habitudes (horaires, lieux fréquentés), l'environnement personnel (famille, animaux) et les opinions. Ces informations permettent de personnaliser l'approche et de créer une connexion rapide. Un red teamer qui découvre que sa cible est passionnée de course à pied peut se présenter comme coureur pour établir un lien. L'exploitation de ces informations est légitime en red team (information publique) mais doit rester dans les limites éthiques (ne pas exploiter de données sensibles).

**Publications professionnelles.** Articles de blog, interventions en conférence, brevets, publications académiques révèlent l'expertise de la cible et fournissent un vocabulaire technique précis pour l'élicitation. Un faux chercheur universitaire qui cite les travaux publiés de sa cible gagne immédiatement en crédibilité.

### 5.4 Reconnaissance technique

La reconnaissance technique alimente les vecteurs d'attaque numériques et physiques.

**Domaines et email.** L'identification du format d'adresse email (prenom.nom@helios-aero.fr vs p.nom@helios-aero.fr) est critique pour le spear-phishing. Les outils de collecte d'emails (Hunter.io, Snov.io — attention aux limites de quotas et aux conditions d'utilisation) et les fuites de données (Have I Been Pwned, Dehashed) permettent de confirmer les formats et d'identifier des comptes potentiellement compromis.

**Technologies.** Les offres d'emploi sont la source la plus riche : une annonce pour un « Administrateur Microsoft 365 / Azure AD » révèle la stack d'identité. Les en-têtes d'email (SPF, DKIM, DMARC — ou leur absence) indiquent le niveau de protection email. Les sous-domaines (vpn.helios-aero.fr, owa.helios-aero.fr) révèlent les services exposés.

**Contrôle d'accès physique.** Les photos sur les réseaux sociaux sont une source sous-estimée. Une photo de badge visible sur une selfie d'employé peut révéler le format du badge (taille, couleur, logo, position de la puce), le type de technologie (RFID, NFC — la présence d'une antenne circulaire visible indique du HF 13,56 MHz ; une puce simple du LF 125 kHz), le niveau de personnalisation (photo, nom, service) et le système de contrôle d'accès (les lecteurs visibles sur les photos d'entrée identifient souvent le fabricant).

### 5.5 Les limites de la reconnaissance

La reconnaissance en sources ouvertes opère dans un cadre éthique et juridique qui diffère selon le contexte.

En **contexte red team**, l'OSINT est réalisée dans le cadre de la lettre de mission. Toute information publiquement accessible est exploitable, mais l'exploitation doit rester dans le scope autorisé (par exemple, la reconnaissance sur les réseaux sociaux personnels des employés peut être autorisée pour construire des pretextes, mais l'exploitation de données sensibles — santé, opinions politiques, vie sexuelle — est exclue même si ces informations sont publiques).

En **contexte attaquant réel**, aucune limite n'est respectée. L'attaquant exploitera toute information disponible, y compris les données personnelles les plus intimes. Cette asymétrie est l'une des difficultés fondamentales de la défense : le red teamer opère avec des contraintes éthiques que l'attaquant n'a pas. Le test autorisé sous-estime donc systématiquement la surface d'attaque réelle.

En **contexte défensif** (contre-ingérence, évaluation de la surface d'exposition), la reconnaissance est réalisée sur sa propre organisation pour identifier les informations exposées et réduire la surface d'attaque. C'est l'une des actions les plus rentables en matière de défense contre le social engineering : savoir ce que l'attaquant sait de vous avant qu'il ne s'en serve.


---
