---
title: PARTIE II — LES ENTITÉS DE L'ÉCOSYSTÈME
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
chapter: 2
chapters: 8
---

*Apprendre à identifier et qualifier chaque type d'entité qu'on retrouve dans un écosystème clandestin. Progression : du plus humain au plus systémique — qui → avec qui → où → via quoi → comment l'argent circule.*

---

## Chapitre 6 — Personnes, alias et identités fragmentées

### 6.1 L'identité clandestine comme objet composite

Dans le monde clandestin, un acteur n'a pas « un nom » — il a un faisceau d'identifiants fragmentés, distribués sur plusieurs plateformes, parfois contradictoires, parfois intentionnellement trompeurs. L'identité clandestine est un objet composite qui comprend un ou plusieurs pseudonymes (le handle utilisé sur les forums et canaux), des adresses email (souvent multiples, certaines jetables, d'autres réutilisées par erreur), des clés PGP ou de chiffrement (utilisées pour la communication sécurisée et parfois comme identifiant stable), des avatars et photos de profil (parfois réutilisés d'une plateforme à l'autre), des numéros de téléphone (pour les comptes Telegram, souvent des numéros VoIP), des wallets crypto (qui peuvent servir d'identifiant stable si réutilisés), et un profil comportemental (horaires d'activité, style d'écriture, sujets d'intérêt, langues parlées).

La distinction fondamentale est celle entre l'individu réel (la personne physique derrière le clavier) et la persona (l'identité construite pour opérer dans l'espace clandestin). Un individu peut contrôler plusieurs personas distinctes pour compartimenter ses activités. Inversement, une persona peut être partagée entre plusieurs individus (un compte de forum peut changer de main, un pseudo peut être « vendu » avec son historique de réputation).

Pour l'analyste, l'objectif n'est pas d'identifier « qui est kr0n0s_ops dans la vraie vie » (c'est le travail des forces de l'ordre avec des moyens d'investigation judiciaire), mais de déterminer quels comptes, quelles activités, et quels rôles dans l'écosystème sont contrôlés par la même entité — qu'elle soit identifiée nominativement ou non.

### 6.2 Réutilisation d'identité et cloisonnement OPSEC

La sécurité opérationnelle (OPSEC) des acteurs clandestins varie considérablement, et c'est cette variation qui crée les opportunités d'investigation.

Les acteurs sophistiqués compartimentent rigoureusement : un pseudo par activité, des emails jetables créés pour chaque opération, des wallets à usage unique, des systèmes opérationnels différents pour chaque rôle, une discipline stricte sur les horaires de connexion (pour masquer le fuseau horaire réel), et l'utilisation systématique de VPN, Tor, et machines virtuelles. Face à un acteur parfaitement compartimenté, la cartographie identitaire est extrêmement difficile.

Les acteurs moins disciplinés — et c'est la majorité — réutilisent des identifiants d'une plateforme à l'autre. Le même pseudo sur un forum de carding et sur un profil GitHub personnel. Le même email ProtonMail pour enregistrer un domaine C2 et pour s'inscrire sur un site de jeu en ligne. Le même mot de passe (révélé dans une breach) sur un compte criminel et sur un compte personnel. C'est cette réutilisation qui crée les pivots permettant de relier les activités et, potentiellement, de remonter vers l'identité réelle.

L'erreur OPSEC la plus fréquente est temporelle : un acteur qui commence ses activités avec une mauvaise OPSEC (utilisant des identifiants personnels, se connectant sans VPN) puis améliore sa sécurité au fil du temps. Les traces anciennes restent dans les bases de données historiques (WHOIS historique, breaches anciennes, caches de moteurs de recherche, archives web) et constituent des « fossiles numériques » exploitables par l'analyste.

### 6.3 Analyse linguistique et comportementale

Au-delà des identifiants techniques, le profil linguistique et comportemental d'un acteur constitue un sélecteur d'identification souvent sous-exploité.

Le **style d'écriture** — vocabulaire, syntaxe, tics de langage, erreurs grammaticales récurrentes, utilisation de l'argot, mix de langues — peut servir à relier des comptes sur différentes plateformes. Un acteur qui utilise systématiquement « ngl » (not gonna lie), des doubles points de suspension, et un mélange d'anglais et de russe translittéré a une empreinte linguistique distinctive. L'analyse stylométrique (computational stylometry) est une discipline formalisée qui peut quantifier la similarité entre des textes attribués à différents auteurs, bien qu'elle ne soit pas une preuve à elle seule.

Le **fuseau horaire d'activité** est un indicateur géographique souvent fiable. En analysant les timestamps des messages sur un forum ou un canal Telegram (en supposant que l'acteur a un rythme de vie normal avec des heures de sommeil), on peut estimer le fuseau horaire probable. Un acteur qui publie régulièrement entre 09h et 02h UTC+3 vit probablement en Europe de l'Est ou au Moyen-Orient. Cette estimation est un indice, pas une preuve — un acteur peut intentionnellement décaler ses heures d'activité.

Les **habitudes comportementales** — types de sujets abordés, réactivité aux messages, fréquence de connexion, jours d'activité (la plupart des acteurs réduisent leur activité le week-end, ce qui confirme paradoxalement une routine « professionnelle ») — complètent le profil.

> **Piège fréquent :** L'analyse linguistique peut produire des faux positifs significatifs. Deux acteurs issus de la même communauté culturelle utiliseront un vocabulaire et un style similaires sans être la même personne. L'analyse linguistique est un indice convergent, jamais une preuve isolée. Voir Ch.12 sur la convergence d'indices.

### 6.4 Homonymie, usurpation et identité reconstruite

Les faux positifs identitaires sont parmi les pièges les plus dangereux de la cartographie d'écosystèmes.

L'**homonymie** est fréquente : un pseudo courant (« darkmaster », « h4ck3r », « admin ») peut être utilisé par des dizaines de personnes différentes sur des plateformes distinctes. Établir que le « darkmaster » du forum A est le même que le « darkmaster » du forum B exige des indices corroborants indépendants du pseudo lui-même (même email, même clé PGP, même style d'écriture, même fuseau horaire).

L'**usurpation** est un risque actif : un acteur peut délibérément utiliser le pseudo d'un autre pour le discréditer, lui attribuer des activités, ou créer de la confusion. Dans les conflits entre groupes cybercriminels, l'usurpation d'identité est une tactique courante (voir Ch.34 sur la déception).

L'**identité reconstruite** désigne un acteur qui abandonne un pseudo compromis et en crée un nouveau, parfois en achetant un compte ancien sur le marché noir (avec son historique de réputation intact). Cette pratique complique le suivi longitudinal des acteurs.

La règle fondamentale est que l'identification ne s'affirme jamais — elle se qualifie par convergence d'indices indépendants. Deux indices convergents (même pseudo + même email) suggèrent. Trois indices indépendants (même pseudo + même email + même clé PGP) commencent à démontrer. La convergence est détaillée au Ch.12.

### 6.5 Fil rouge — NEXUS : la piste identitaire

> **🔍 NEXUS — Épisode 6**
>
> L'email `kr0n0s-ops@proton.me` trouvé dans le WHOIS historique a été corrélé au pseudo `kr0n0s_ops` sur le forum XSS via une breach de 2023. Samira pousse l'investigation identitaire.
>
> **Sherlock (outil OSINT de recherche de pseudo) :** Le pseudo `kr0n0s_ops` apparaît sur GitHub (3 repositories publics contenant des scripts d'exploitation de vulnérabilités réseau, dernière activité il y a 5 mois), et sur un canal Telegram public lié à la revente d'accès réseau.
>
> **Analyse linguistique :** Sur le forum XSS, kr0n0s_ops écrit en anglais avec des fautes caractéristiques d'un locuteur russophone (confusion des articles, calques syntaxiques). Il utilise systématiquement l'expression « ez pz » et des emojis spécifiques. Le fuseau horaire d'activité (analyse des timestamps sur 6 mois) indique une plage UTC+3 à UTC+4 — compatible avec Moscou, mais aussi Istanbul ou Dubaï.
>
> **DeHashed (recherche étendue) :** L'email ProtonMail apparaît dans une seconde breach (base de données d'un service VPN en 2022). Le mot de passe hashé est différent de celui du forum, mais l'IP de création du compte VPN pointe vers un réseau résidentiel en Russie (ISP : Rostelecom). C'est un indice géographique, pas une preuve (l'IP peut être un proxy).
>
> **Bilan identitaire provisoire :** Les indices convergent vers un acteur unique (même email sur WHOIS et breaches, même pseudo sur forum/GitHub/Telegram, profil linguistique russophone cohérent, fuseau horaire cohérent, IP résidentielle russe sur une donnée ancienne). Niveau de confiance que les comptes sont liés : élevé (B2). Niveau de confiance sur la localisation géographique : modéré (C3). Identité réelle : inconnue.

---

## Chapitre 7 — Entités organisationnelles

### 7.1 Groupes cybercriminels et marques

L'un des pièges conceptuels les plus fréquents est de confondre le « groupe » avec la « marque ». Dans l'écosystème ransomware, la marque (LockBit, BlackCat, Conti, PhantomCrypt dans notre fil rouge) est un nom commercial — l'équivalent d'une franchise. Derrière la marque, il faut distinguer quatre niveaux d'acteurs.

L'**opérateur** (ou core team) est le noyau qui contrôle le code source du ransomware, maintient l'infrastructure (builder, panel, leak site, serveurs de négociation), fixe les règles du programme d'affiliation, et capte une commission sur chaque rançon payée (typiquement 20 à 30 %). L'opérateur est souvent un petit groupe de 5 à 15 personnes — développeurs, administrateurs système, et gestionnaires. C'est l'entité la plus critique de l'écosystème : si l'opérateur est compromis, tout le réseau d'affiliés est impacté.

Les **affiliés** sont les utilisateurs du service. Ils reçoivent le builder (l'outil qui génère des variants personnalisées du ransomware), accèdent au panel (l'interface de contrôle des victimes), et mènent les opérations d'attaque de manière autonome. Un opérateur RaaS peut avoir des dizaines d'affiliés actifs simultanément. Chaque affilié gère ses propres cibles, ses propres méthodes de compromission, et ses propres négociations. Cette autonomie signifie que deux attaques sous la même marque peuvent avoir des profils très différents.

Les **prestataires** sont les acteurs externes qui fournissent des services à l'écosystème sans en être formellement membres : les IAB qui vendent les accès initiaux, les fournisseurs de crypters qui rendent le malware indétectable, les hébergeurs bulletproof, les services de mixing, et les négociateurs spécialisés. Ces prestataires servent souvent plusieurs marques simultanément.

Les **anciens affiliés et successeurs** constituent la mémoire et la continuité. Quand une marque est disrupted (comme Conti après les leaks de 2022, ou ALPHV/BlackCat après l'action du FBI en décembre 2023), les affiliés ne disparaissent pas — ils migrent vers d'autres plateformes. Les développeurs et opérateurs peuvent rebrandir sous un nouveau nom. La communauté CTI suit ces migrations en analysant les TTP, le code, et les infrastructure partagées.

### 7.2 Sociétés écrans et structures de façade

De nombreux écosystèmes cybercriminels utilisent des structures juridiques légales comme couverture. Ces sociétés écrans peuvent servir à enregistrer des domaines et louer de l'hébergement sans attirer l'attention, à ouvrir des comptes bancaires pour le blanchiment, à fournir une couverture d'emploi pour les participants (le développeur d'un ransomware peut être officiellement « consultant IT » dans une société écran), et à faciliter les transactions financières internationales.

L'identification des sociétés écrans passe par la consultation des registres d'entreprises (en France : Infogreffe, Societe.com, Pappers ; à l'international : OpenCorporates, CompanyHouse UK, registres locaux), le cross-référencement des dirigeants (un même individu qui apparaît comme directeur de 15 sociétés dans 5 juridictions est suspect), l'analyse des flux financiers (des sociétés sans activité économique visible mais avec des flux bancaires importants), et la vérification de la substance (la société a-t-elle des employés, des locaux, une activité réelle ?).

Les juridictions privilégiées pour les sociétés écrans liées au cybercrime incluent les Émirats Arabes Unis (Dubaï en particulier, avec des sociétés en free zone), les îles Vierges Britanniques, les Seychelles, la Géorgie, et certains pays baltes. Le choix de la juridiction dépend du service recherché : Dubaï pour le cash-out crypto et l'immobilier, les BVI pour l'opacité juridique, les pays baltes pour les licences de services financiers.

### 7.3 Communautés et collectifs

Tous les regroupements d'acteurs ne sont pas des organisations formelles. De nombreux écosystèmes gravitent autour de communautés informelles — forums spécialisés, canaux Telegram, serveurs Discord — qui fonctionnent comme des écosystèmes sociaux sans hiérarchie formelle.

Ces communautés se caractérisent par une hiérarchie informelle (les membres les plus anciens, les plus actifs, ou les plus compétents ont plus d'influence sans titre officiel), des codes d'entrée (certains canaux Telegram exigent un vouching, un paiement, ou une preuve de compétence technique), des normes comportementales (les forums russophones ont des règles non écrites strictes : ne pas cibler la Russie, ne pas arnaquer les autres membres, ne pas coopérer avec les forces de l'ordre), et des mécanismes de sanction informels (bannissement, exposition publique, blacklisting).

L'analyste doit éviter de traiter une communauté comme une organisation. Tous les membres d'un forum ne coopèrent pas entre eux. Deux personnes actives sur le même canal Telegram ne sont pas nécessairement complices. La communauté est un espace social dans lequel des transactions et des coopérations se forment, mais le fait d'y participer ne constitue pas en soi un lien opérationnel.

### 7.4 Franchises et affiliations — le modèle RaaS comme archétype

Le Ransomware-as-a-Service est le modèle organisationnel le plus important de la cybercriminalité contemporaine, et il se réplique dans d'autres domaines.

Le mécanisme est le suivant : un opérateur central développe le ransomware, fournit le builder (outil de génération de variants), met en place un panel de contrôle (interface web sécurisée pour gérer les victimes, suivre les paiements, accéder aux outils de négociation), opère un leak site (pour la double extorsion), et recrute des affiliés. Les affiliés paient un dépôt initial (typiquement quelques centaines de dollars pour les plateformes entrantes, plus pour les plateformes premium — LockBit 5.0 demande environ 500$ en Bitcoin) et s'engagent à verser un pourcentage de chaque rançon payée (typiquement 20 à 30 % pour l'opérateur). L'affilié gère autonomement la compromission, le déploiement, et la négociation.

Ce modèle se réplique dans le Phishing-as-a-Service (kits de phishing pré-construits avec panels de récupération de credentials, vendus par abonnement mensuel), le Malware-as-a-Service (infostealers comme Lumma, vendus entre 250 et 20 000$ selon le tier — voir Ch.16), le DDoS-for-hire (plateformes de stress testing/booter qui sont en réalité des services de DDoS à la demande), et les botnets en location.

### 7.5 Fil rouge — NEXUS : l'écosystème organisationnel se dessine

> **🔍 NEXUS — Épisode 7**
>
> Sur le canal Telegram identifié, kr0n0s_ops interagit avec deux autres pseudos de manière régulière.
>
> Le premier, `ghost_access`, publie des annonces de vente d'accès réseau : « FR energy company, domain admin, $12,000 ». Le format est standardisé : pays, secteur, niveau d'accès, prix. C'est un IAB (Initial Access Broker).
>
> Le second, `nego_phantom`, gère les négociations avec les victimes pour le compte de la plateforme PhantomCrypt. Il partage des captures d'écran de « chats clients » montrant des échanges avec des victimes paniquées. C'est un service de négociation externalisé.
>
> Samira met à jour le graphe : trois entités organisationnelles distinctes apparaissent — l'affilié (kr0n0s_ops), l'IAB (ghost_access), et le service de négociation (nego_phantom), tous gravitant autour de la plateforme PhantomCrypt (l'opérateur RaaS). Le modèle franchisé se confirme.

---

## Chapitre 8 — Espaces relationnels et médiatiques

### 8.1 Forums underground comme institutions sociales

Les forums underground ne sont pas de simples « marchés noirs en ligne ». Ce sont des institutions sociales complexes qui remplissent simultanément plusieurs fonctions essentielles au fonctionnement de l'écosystème.

**Fonction de marché.** Les forums abritent des sections dédiées à la vente de services (accès, malware, hébergement, carding, blanchiment), avec des annonces structurées, des prix, et des conditions de vente. Les transactions se font généralement en Bitcoin ou Monero, souvent via un système d'escrow intégré au forum (voir Ch.19).

**Fonction de réputation.** Chaque utilisateur accumule un historique visible : nombre de transactions, ratings des acheteurs et vendeurs, ancienneté du compte, contributions à la communauté (tutoriels, outils partagés). Ce capital réputationnel est le bien le plus précieux d'un acteur sur le forum — il est le garant de la confiance dans un environnement sans recours légal.

**Fonction de recrutement.** Les acteurs compétents se font remarquer par la qualité de leurs contributions et sont approchés directement (via messages privés ou via des canaux de communication off-forum comme Tox, Jabber/XMPP, ou Telegram) pour des opérations spécifiques.

**Fonction de gouvernance.** Les admins et modérateurs du forum fixent et appliquent les règles : interdiction de certaines activités (la plupart des forums russophones interdisent la vente de données de victimes russes), résolution des litiges commerciaux (l'admin ou un arbitre désigné tranche les conflits entre vendeur et acheteur), et sanctions (bannissement, exposition publique du scammer).

Les forums les plus significatifs historiquement et actuellement pour l'écosystème cybercriminel incluent XSS et Exploit (forums russophones majeurs, accès sur vouching ou paiement), RAMP (forum russophone plus récent, notable pour avoir hébergé des discussions RaaS après le bannissement de LockBit d'XSS et Exploit), BreachForums (forum anglophone centré sur les données, successeur de RaidForums après sa saisie en 2022, lui-même ayant connu des turbulences avec l'arrestation de son admin « Baphomet » en 2024 et des relances successives), et Cracked/Nulled (forums anglophone de niveau inférieur, plus accessibles mais moins réputés). Le paysage des forums évolue constamment — les saisies, les exit scams des administrateurs, et les migrations sont fréquentes.

### 8.2 Canaux Telegram et Discord

Telegram est devenu le moyen de communication privilégié des écosystèmes cybercriminels, supplantant largement les messageries plus anciennes comme Jabber/XMPP et Tox pour les communications semi-publiques.

**Canaux publics** : ils servent de vitrine — un IAB y publie ses nouvelles offres, un opérateur RaaS y annonce ses mises à jour, un vendeur de logs y partage des échantillons gratuits pour attirer des clients. Ces canaux sont facilement observables par les analystes CTI.

**Groupes privés** : accessibles sur invitation ou après vérification, ils servent d'espace opérationnel — coordination entre affiliés, partage d'outils, discussion technique, échange d'intelligence sur les cibles. L'accès à ces groupes est beaucoup plus difficile pour l'analyste sans franchir les limites légales (pas d'interaction active ni de fausse identité).

L'identification des administrateurs de canaux Telegram est une technique OSINT essentielle. Les outils automatisés (comme TGStat pour les statistiques de canaux, ou l'API Telegram elle-même pour les metadata publiques) peuvent révéler des informations sur la création du canal, les patterns de publication, et parfois les liens entre différents canaux administrés par la même personne. La prudence s'impose toutefois : Telegram a durci ses politiques de coopération avec les forces de l'ordre en 2024-2025 suite à l'arrestation de son fondateur Pavel Durov en France en août 2024, mais les métadonnées publiques restent accessibles.

Discord est moins utilisé que Telegram pour la cybercriminalité « sérieuse » mais reste un espace actif pour les communautés de script kiddies, les marchés de carding de bas niveau, et les discussions techniques informelles.

### 8.3 Leak sites et sites de revendication

Les leak sites sont les plateformes sur lesquelles les opérateurs de ransomware publient les données des victimes qui refusent de payer la rançon. Ces sites, généralement hébergés sur le réseau Tor, remplissent une double fonction de pression directe sur la victime actuelle et de démonstration de capacité pour les victimes futures.

L'analyse des leak sites est une source d'intelligence précieuse. Elle révèle les cibles d'un opérateur (secteurs, pays, tailles d'entreprise), la fréquence des attaques (indicateur de l'activité et du nombre d'affiliés), le volume de données exfiltrées (indicateur de la sophistication de l'opération), les délais entre compromission et publication (indicateur du processus de négociation), et les patterns saisonniers ou géographiques.

Les leak sites sont aussi des espaces de communication stratégique. Les opérateurs y publient des « communiqués de presse » sur leurs nouvelles versions, des réfutations quand les forces de l'ordre annoncent des disruptions, et parfois des messages menaçants envers les chercheurs en sécurité qui les analysent.

### 8.4 Médias de façade et relais d'influence

Certains écosystèmes — notamment les écosystèmes para-étatiques — utilisent des médias de façade pour amplifier leurs opérations. Un blog « journalistique » qui publie un « article d'investigation » sur une entreprise victime de ransomware, en réalité rédigé par les attaquants eux-mêmes ou leurs relais, sert à maximiser la pression médiatique et réputationnelle.

Ces médias de façade sont identifiables par des indicateurs OSINT classiques : domaine récent, pas d'historique de publication avant l'événement, pas d'identité vérifiable des « journalistes », hébergement sur des infrastructures liées à l'écosystème criminel, et contenu aligné exclusivement avec les intérêts de l'attaquant.

La convergence entre cyber-attaque et opération d'influence est une tendance majeure de 2024-2026. Les groupes para-étatiques (et certains groupes purement criminels qui ont compris l'intérêt de la pression médiatique) orchestrent leurs attaques en combinant l'intrusion technique, l'exfiltration de données, la publication sur le leak site, et l'amplification via des canaux Telegram et des médias de façade — dans une séquence coordonnée qui maximise l'impact.

### 8.5 Fil rouge — NEXUS : la dimension informationnelle

> **🔍 NEXUS — Épisode 8**
>
> Le leak site de PhantomCrypt publie une revendication 72 heures après la détection du sample. Le site liste Énergis comme victime avec un compte à rebours de 10 jours et un extrait de données volées (des schémas d'architecture réseau et des documents internes marqués « Confidentiel Entreprise »). Cela signifie que le chiffrement a été bloqué par l'EDR, mais l'exfiltration a peut-être partiellement réussi avant la détection.
>
> Simultanément, le canal Telegram de PhantomCrypt relaie la publication avec un commentaire : « French energy giant — critical infrastructure — premium data. » Le message est repris par 3 autres canaux d'agrégation de leaks en 24 heures.
>
> Plus troublant : le blog `phantom-news[.]press` (identifié sur la même IP que le C2) publie un article en anglais, présenté comme du « journalisme d'investigation », titré « Major French Energy Provider Fails to Protect Critical Infrastructure ». L'article cite des « sources anonymes » et mentionne des détails techniques que seuls les attaquants peuvent connaître. L'article est partagé sur X/Twitter par des comptes qui semblent automatisés.
>
> Samira note : l'écosystème a une dimension informationnelle coordonnée. Le leak site, le canal Telegram, et le blog de façade fonctionnent en séquence pour maximiser la pression. C'est inhabituel pour un affilié RaaS purement opportuniste — les affiliés classiques se contentent du leak site et de la négociation directe. La coordination médiatique suggère soit un affilié sophistiqué, soit une dimension para-étatique.

---

## Chapitre 9 — Objets techniques

### 9.1 Infrastructures réseau

Les objets techniques constituent l'ossature matérielle d'un écosystème cybercriminel. Chaque objet technique — domaine, IP, serveur, certificat, malware — est un nœud potentiel dans le graphe et un point de pivot pour l'investigation.

Les **domaines** sont les identifiants les plus visibles de l'infrastructure. Un domaine C2 est utilisé pour la communication entre le malware et l'opérateur. Un domaine de phishing imite un site légitime pour capturer des credentials. Un domaine de leak site héberge les données des victimes. Les registrars utilisés (certains sont plus complaisants que d'autres), les TLD choisis (les extensions exotiques comme .xyz, .top, .click sont surreprésentées dans l'infrastructure malveillante mais aussi légitimement utilisées, attention aux biais), et les patterns de nommage (génération automatique vs noms plausibles) sont des indicateurs analytiques.

Les **adresses IP et ASN** (Autonomous System Number) permettent d'identifier l'hébergeur et le réseau. Le reverse IP (quels autres domaines partagent cette IP) est l'une des techniques de pivot les plus productives. L'ASN révèle le fournisseur d'hébergement et sa réputation. Certains ASN concentrent une proportion anormalement élevée de contenu malveillant, ce qui en fait des marqueurs d'hébergement bulletproof.

Les **certificats SSL/TLS**, enregistrés publiquement via Certificate Transparency, peuvent révéler des relations entre domaines (certificats wildcard partagés, certificats multi-domaines), des sous-domaines cachés, et des patterns d'infrastructure.

### 9.2 Hébergement bulletproof

L'hébergement bulletproof désigne des fournisseurs d'hébergement qui ignorent délibérément les plaintes d'abus (abuse reports), les requêtes des forces de l'ordre, et les demandes de retrait de contenu malveillant. Ces hébergeurs sont un facilitateur critique de l'écosystème cybercriminel.

Le mécanisme économique est simple : l'hébergeur facture un premium significatif par rapport à un hébergeur classique (5 à 50 fois plus cher pour des services équivalents) en échange de la garantie d'impunité. Les clients paient pour l'assurance que leur infrastructure ne sera pas coupée suite à une plainte.

L'identification d'un hébergeur bulletproof repose sur la concentration de contenu malveillant sur ses IP et ASN (les bases de données de réputation comme AbuseIPDB, Spamhaus, et les rapports CTI le signalent), l'absence de réponse aux abuse reports (un test basique : envoyer un abuse report et observer la réponse), la localisation dans des juridictions à faible coopération judiciaire internationale, et les témoignages et discussions sur les forums underground (les acteurs recommandent et notent les hébergeurs bulletproof).

### 9.3 Malware, builders, crypters et infrastructures C2

L'écosystème technique d'une attaque implique généralement plusieurs couches de logiciels malveillants et d'outils.

Le **malware principal** (ransomware, RAT, infostealer) est le payload final. Son analyse (reverse engineering) révèle la famille, le variant, le builder utilisé, les fonctionnalités, et parfois des artefacts de développement (chemins de fichiers, variables de débogage, commentaires en langue originale) qui peuvent fournir des indices d'attribution.

Le **builder** est l'outil qui permet de générer des variants personnalisées du malware. Dans un modèle RaaS, l'opérateur fournit le builder aux affiliés, qui génèrent leurs propres variants avec des paramètres spécifiques (adresse C2, extension des fichiers chiffrés, contenu de la note de rançon). L'identification du builder confirme le lien avec la plateforme RaaS.

Le **crypter** est un service d'obfuscation qui rend le malware indétectable par les antivirus et les EDR. Les crypters sont vendus comme des services spécialisés (Fully UnDetectable, ou FUD) avec des tarifs variant de 20 à 500 dollars par obfuscation, ou sous forme d'abonnements mensuels. Un même crypter peut être utilisé par des acteurs sans aucun lien entre eux — c'est un piège analytique majeur (voir section suivante).

Le **loader** est un malware de première étape, souvent distribué par email (pièce jointe ou lien), qui télécharge et exécute le payload principal une fois la machine compromise. Les loaders (comme IcedID, QakBot avant sa disruption, ou les successeurs apparus depuis) sont souvent des services indépendants du payload final.

L'**infrastructure C2** (Command and Control) est le réseau de serveurs que le malware utilise pour recevoir des instructions et exfiltrer des données. Les panels C2 — interfaces web accessibles aux opérateurs pour contrôler les machines compromises — sont parfois détectables via des scans réseau (Shodan, Censys) quand ils sont mal sécurisés.

### 9.4 Mutualisation de services techniques — le piège des faux liens

C'est un point critique pour la rigueur analytique : de nombreux services techniques sont mutualisés entre des acteurs qui n'ont aucun lien opérationnel entre eux.

Un même hébergeur bulletproof sert des dizaines de groupes différents. Un même crypter est utilisé par des opérations sans aucune connexion. Un même loader distribue des payloads de familles de malware distinctes. Un même registrar est utilisé pour enregistrer des milliers de domaines malveillants sans lien entre eux.

La conséquence analytique est que la **co-localisation technique n'est pas un lien opérationnel**. Deux domaines sur la même IP ne sont pas nécessairement gérés par le même acteur — ils peuvent simplement être hébergés chez le même prestataire. Deux malwares utilisant le même crypter ne sont pas nécessairement développés par le même groupe — ils utilisent le même service commercial.

Pour qu'un lien technique soit significatif, il faut des indicateurs supplémentaires de co-gestion : même certificat wildcard (qui implique un contrôle commun), même Google Analytics ou pixel de suivi, même code personnalisé dans les pages web, ou des configurations techniques identiques au-delà de ce que le prestataire fournit par défaut. Le détail de la qualification des liens est traité au Ch.11.

### 9.5 Fil rouge — NEXUS : l'infrastructure révèle ses liens

> **🔍 NEXUS — Épisode 9**
>
> L'analyse du malware par le CERT révèle que le sample est un variant de PhantomCrypt généré par le builder v3.2 de la plateforme. L'ID d'affilié est intégré dans le binaire (pratique courante pour le suivi des commissions) : `AFF-0x7A3`. Cet ID confirme le lien avec le programme RaaS PhantomCrypt.
>
> L'infrastructure C2 est explorée plus en profondeur. Le panel de contrôle `phcrypt-panel[.]xyz` est accessible via le port 8443 avec une interface de login. Shodan révèle que ce panel utilise un framework personnalisé avec un header HTTP distinctif (`X-Panel-Version: PC-3.2-aff`). Ce même header est trouvé sur deux autres IP dans des rapports CTI — il s'agit de l'infrastructure centralisée de PhantomCrypt, pas d'un déploiement spécifique à kr0n0s_ops.
>
> Le blog `phantom-news[.]press`, en revanche, partage avec le domaine C2 non seulement la même IP mais aussi le même Google Analytics ID et le même certificat wildcard. Ces indicateurs de co-gestion vont au-delà de la simple co-localisation. Samira qualifie le lien C2-blog comme « fort — co-gestion probable, pas simple mutualisation d'hébergement ».

---

## Chapitre 10 — Objets financiers

### 10.1 Wallets et clusters d'adresses

Une adresse Bitcoin (ou Ethereum, ou toute autre cryptomonnaie) n'est pas une identité — c'est un nœud financier dans un réseau de flux. Un même acteur peut contrôler des centaines d'adresses, et une même adresse peut être utilisée successivement par plusieurs acteurs (dans le cas de wallets de services comme les exchanges ou les mixers).

Le **clustering** est la technique fondamentale de l'analyse blockchain. L'heuristique la plus courante pour Bitcoin est le Common Input Ownership (CIO) : si deux adresses sont utilisées comme inputs dans une même transaction, elles sont probablement contrôlées par la même entité (parce qu'il faut détenir les clés privées de toutes les inputs pour signer la transaction). Cette heuristique permet de regrouper des dizaines ou des centaines d'adresses en « clusters » représentant une seule entité.

Les limites du clustering sont réelles. L'heuristique CIO échoue quand les transactions utilisent des techniques de privacy (CoinJoin, PayJoin) qui mélangent les inputs de plusieurs utilisateurs. Elle peut aussi produire des faux positifs quand un service (exchange, mixer) utilise des inputs de plusieurs clients dans une même transaction. Les clusters ne sont pas des certitudes — ils sont des estimations probabilistes.

Les plateformes comme Chainalysis Reactor enrichissent le clustering brut avec des données d'attribution : elles associent des clusters à des entités connues (exchanges identifiés, services de mixing, portefeuilles de ransomware, adresses de darknet markets) grâce à une combinaison de heuristiques, de données de coopération avec les exchanges, et de monitoring OSINT. La base d'attribution de Chainalysis couvre plus de 5 milliards de clusters (mars 2026).

### 10.2 Flux entrants et sortants comme révélateurs de pouvoir

La cartographie des flux financiers d'un écosystème révèle les relations de pouvoir et de dépendance entre acteurs. Qui paie qui, dans quel sens, à quel volume, et à quelle fréquence — ces informations structurent l'analyse économique.

Les **flux entrants** d'un wallet révèlent ses sources de revenus : paiements de victimes (rançons), revenus de ventes (accès, données, services), transferts d'autres acteurs de l'écosystème. Les **flux sortants** révèlent ses dépenses et ses relations : paiement de l'opérateur (commission RaaS), paiement du IAB (achat d'accès), achat de services (hébergement, crypter), et blanchiment (transfert vers mixers, exchanges, ou wallets intermédiaires).

Un acteur qui reçoit beaucoup et distribue peu est un accumulateur (typiquement un opérateur ou un investisseur). Un acteur qui reçoit peu et redistribue immédiatement est un intermédiaire de transit (typiquement un service de mixing ou une mule). Un acteur qui reçoit de sources multiples et diversifiées est un hub financier (typiquement un exchange ou un service de blanchiment).

### 10.3 Passerelles, mixers, bridges et exchanges

Les points de conversion et d'obfuscation sont les nœuds critiques de l'analyse financière.

Les **exchanges KYC** (qui appliquent les procédures de vérification d'identité) sont les points de dé-anonymisation potentielle. Si un wallet criminel envoie des fonds vers un exchange régulé, les forces de l'ordre peuvent théoriquement obtenir l'identité du titulaire du compte par réquisition judiciaire. C'est pourquoi les acteurs sophistiqués évitent les grands exchanges et passent par des OTC desks (transactions de gré à gré, souvent dans des juridictions peu coopératives) ou des exchanges non régulés.

Les **mixers et tumblers** sont des services qui mélangent les fonds de plusieurs utilisateurs pour rompre le lien entre l'adresse d'origine et l'adresse de destination. Les mixers centralisés (comme Chipmixer, saisi par les autorités en 2023, ou Sinbad, saisi en novembre 2023) sont vulnérables aux saisies. La tendance est aux protocoles décentralisés et aux techniques de mixing intégrées aux wallets (comme le protocole Wasabi, bien que celui-ci ait fermé son service de coordination en 2024, et ses successeurs comme JoinMarket).

Les **bridges cross-chain** permettent de transférer de la valeur d'une blockchain à une autre (de Bitcoin vers Ethereum, par exemple), ce qui complique le traçage. Les **DEX** (exchanges décentralisés) permettent d'échanger des tokens sans intermédiaire centralisé, rendant le traçage plus difficile mais pas impossible pour les plateformes d'analyse avancées.

### 10.4 Wallets dormants, jetables et de transit

Un wallet peut jouer différents rôles selon son pattern d'utilisation.

Un **wallet dormant** reçoit des fonds et ne les déplace pas pendant une longue période. Il peut s'agir d'un stockage long terme (l'acteur attend que l'attention se dissipe avant de blanchir) ou d'un wallet abandonné. Un **wallet jetable** est utilisé une seule fois : il reçoit des fonds, les transfère immédiatement vers une autre adresse, et n'est plus jamais utilisé. Les chaînes de wallets jetables (peeling chains) sont une technique de blanchiment courante. Un **wallet de transit** est un nœud intermédiaire qui ne « possède » pas les fonds mais les relaye — typiquement un wallet d'un service de mixing ou d'un exchange.

La distinction entre ces rôles est critique pour éviter les erreurs d'attribution. Attribuer un wallet de transit à un acteur parce que « des fonds de la rançon y sont passés » est une erreur fréquente : le wallet peut appartenir au service de mixing, pas à l'acteur criminel.

### 10.5 Fil rouge — NEXUS : la piste financière

> **🔍 NEXUS — Épisode 10**
>
> Bien qu'Énergis n'ait pas payé la rançon (l'EDR a bloqué le chiffrement), Samira peut tracer les wallets associés à l'écosystème PhantomCrypt grâce aux rançons payées par d'autres victimes.
>
> Le leak site de PhantomCrypt liste 23 victimes sur les 6 derniers mois. L'analyste identifie les adresses Bitcoin de paiement à partir des notes de rançon partagées dans des rapports CTI communautaires. OXT.me permet de tracer les flux à partir de ces adresses.
>
> Le pattern est récurrent : les paiements arrivent sur des wallets dédiés par victime (une adresse unique par rançon — bonne OPSEC), puis sont transférés vers un wallet de consolidation (cluster de 47 adresses), puis fragmentés vers un service de mixing identifié par Chainalysis comme « Mixer X » (service sanctionné par l'OFAC en 2024). Après le mixing, les fonds réapparaissent sous forme de multiples petites transactions convergent vers deux destinations principales.
>
> La première : un cluster associé à un exchange basé à Dubaï, connu pour ses contrôles KYC laxistes. C'est le cash-out probable.
>
> La seconde : un wallet identifié dans un rapport de Chainalysis de 2025 comme « possiblement lié à des activités de collecte de fonds para-étatiques » — sans attribution définitive, avec un niveau de confiance modéré.
>
> La piste financière rejoint la piste géopolitique. Samira documente le lien avec un niveau de confiance C3 (source : rapport commercial d'éditeur CTI, fiabilité modérée ; information : lien indirect via chaîne de mixing, fiabilité modérée).

---
