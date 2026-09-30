---
title: Partie 2 — Identité, compartimentation et hygiène comportementale
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 3
chapters: 8
---

> **Objectif** : passer de la cartographie à l’action. Avant de durcir des appareils ou de chiffrer des canaux, il faut réduire ce qui fuit déjà, contrôler ce qu’on expose, et architecturer la séparation entre les compartiments de sa vie.

-----

## Chapitre 5 — OSINT défensif : auditer son propre profil

### 5.1 Pourquoi s’OSINTer soi-même est l’étape zéro

Un attaquant qui s’intéresse à toi commence par une recherche ouverte. Tant que tu n’as pas fait cette recherche à sa place, tu défends à l’aveugle. L’OSINT défensif inverse la posture : tu te mets dans la peau de l’adversaire, tu reproduis sa démarche, tu mesures ce qu’il trouvera, puis tu réduis. Ce chapitre est le miroir défensif du cours OSINT Mastery (voir cours dédié pour la méthode offensive complète).

### 5.2 Méthode systématique en six axes

L’OSINT défensif sérieux suit une méthode. Improviser conduit à manquer des angles.

**Axe 1 — Identité civile** : recherche par nom + prénom + ville sur Google, Bing, DuckDuckGo. Pas connecté à un compte. En navigation privée. Avec et sans guillemets. Puis variantes orthographiques. Puis combinaison nom + employeur, nom + ancien lieu d’études.

**Axe 2 — Emails** : tester chaque email connu sur HaveIBeenPwned, Intelligence X, DeHashed (limites légales selon juridictions). Identifier dans quelles fuites tu apparais, quelles données ont été exposées.

**Axe 3 — Pseudonymes** : faire la liste de tous tes pseudonymes (Twitter, Reddit, GitHub, forums, gaming, dating). Pour chacun, recherche directe et username pivot avec des outils comme WhatsMyName ou Sherlock.

**Axe 4 — Numéros de téléphone** : recherche du numéro sur Google, mais aussi sur Truecaller, Sync.me (gardez en tête : ces services sont eux-mêmes intrusifs ; recherchez via un compte temporaire ou via un proche).

**Axe 5 — Photos** : reverse image sur Yandex Images (souvent le plus efficace pour les visages), Google Lens, TinEye, PimEyes (payant, contestable éthiquement), FaceCheck.ID. Tester ses photos professionnelles, ses photos de profil, ses photos publiques.

**Axe 6 — Documents publics** : registres du commerce, archives administratives, listes électorales (selon pays), publications scientifiques, contributions GitHub, mailing-lists archivées.

### 5.3 Outils de référence (2025-2026)

- **HaveIBeenPwned** (gratuit, référence) : fuites de credentials.
- **Intelligence X** (freemium) : recherche dans des dumps, paste sites, Tor.
- **Epieos** (freemium) : recherche par email, téléphone, nom.
- **Hunter.io** : recherche d’emails par domaine (utile pour vérifier ce qu’on expose côté professionnel).
- **Wayback Machine** : archives du web ; vérifier ce qui de toi a été archivé.
- **WhatsMyName, Sherlock** (gratuits) : recherche de pseudonyme sur des centaines de plateformes.
- **PimEyes, FaceCheck.ID** : reverse image faciale (à utiliser avec une photo *non* affiliée à tes comptes principaux pour éviter d’alimenter leurs bases).

**Limite éthique et légale** : certains de ces outils opèrent en zone grise. PimEyes a été condamné en plusieurs juridictions. L’usage à des fins d’audit défensif sur soi-même est généralement légitime ; l’usage sur des tiers sans consentement ne l’est pas. Ce cours ne couvre pas l’usage offensif.

### 5.4 Cartographier les liens entre comptes

Le danger n’est pas chaque compte individuellement, c’est leur connexion. Si l’attaquant prouve que @LeaMartens (Twitter) et lea.martens@gmail.com et leam94 (GitHub) appartiennent à la même personne, il a un graphe complet. La carte que tu produis doit donc inclure ces ponts : reuse d’email entre comptes, photo identique sur deux profils, même biographie, références croisées (« mon GitHub : leam94 » dans le profil Twitter), mêmes contacts mutuels.

### 5.5 Limites de l’auto-OSINT

Tu ne trouveras pas tout ce qu’un attaquant motivé trouvera. Tes angles morts incluent : bases de données vendues qui ne sont pas publiquement indexées, données obtenues par requête judiciaire ou réquisition, données dans des forums fermés, données issues d’OSINT humain (questions posées à ton entourage). L’OSINT défensif est nécessaire mais pas suffisant. Il borne ce que *tout adversaire* trouvera trivialement — pas ce qu’un adversaire ressourcé reconstituera.

### 5.6 *Fil rouge* — Léa fait son OSINT

Léa applique la méthode. Découvertes notables :

- Une vieille photo de classe lycée scannée par une ancienne camarade et postée publiquement sur Facebook, indexée par Google Images, retrouvée par reverse image à partir de sa photo LinkedIn.
- Un mémo professionnel PDF, mis en ligne par un ancien employeur, contenant son nom dans les métadonnées XMP même si retiré du texte visible.
- Un compte de forum nutrition (2014, pseudo lea.m_94) avec son adresse email principale, son alimentation, et ses lieux fréquentés.
- Trois pages d’archives de mailing-lists journalistiques où son adresse pro apparaît en clair.

Elle constate que l’attaquant compétent reconstituerait son identité civile, sa carrière, ses fréquentations professionnelles, et un certain nombre de détails personnels en moins d’une heure. Elle priorise.

-----

## Chapitre 6 — Data brokers, courtiers de données et désinscription effective

### 6.1 Anatomie du marché

Les data brokers compilent, à partir de sources légales (registres publics, programmes de fidélité, applications mobiles vendant leurs données, fuites achetées, données dérivées des plateformes), des profils détaillés revendus à des annonceurs, des assureurs, des banques, et — point critique — à des forces de l’ordre via achat plutôt que mandat judiciaire (cas documenté aux États-Unis : ICE achète à des courtiers ce qu’ils ne pourraient obtenir sans mandat).

Aux États-Unis, l’industrie est florissante (Acxiom, LexisNexis, Spokeo, BeenVerified, Whitepages, Intelius, ID Analytics, etc.). En Europe, le RGPD limite — sans empêcher — la pratique. En France, des courtiers existent (Société.com, Pages Jaunes Pro, Easyfichiers, etc.) sur des bases plus limitées.

### 6.2 Cas français et européens

En France et en Europe, les sources principales de profilage sont :

- Le registre du commerce et des sociétés (gérants, adresses, capitaux).
- Les annuaires (Pages Jaunes, Pages Blanches — désinscription possible).
- Les listes électorales (consultables sous conditions).
- Les annonces légales (publications obligatoires).
- Le BODACC pour les dirigeants.
- Les sites de fuites agrégant des bases européennes.
- Les anciens annuaires d’écoles et d’universités.

Le RGPD permet d’invoquer le droit à l’effacement (article 17) et le droit d’opposition (article 21). Ces droits sont opposables à tout responsable de traitement basé en UE ou ciblant des résidents UE.

### 6.3 Désinscription manuelle vs services payants

Les services type DeleteMe (US), Optery, Incogni, Privacy Bee automatisent la désinscription auprès de centaines de courtiers. Avantages : gain de temps. Limites : couverture incomplète (surtout courtiers européens), efficacité partielle (certains courtiers réinscrivent), modèle économique qui suppose une renouvellement (les courtiers re-collectent en continu), confiance à accorder au service lui-même (qui reçoit en bonus une liste de tes données).

La désinscription manuelle reste l’option maximaliste : long, fastidieux, mais traçable. Pour la France, deux types de courriers utiles :

- Demande de droit à l’effacement (article 17 RGPD) avec justificatif d’identité, à adresser au DPO du courtier.
- Demande d’opposition (article 21) avec motif (généralement : « finalité de prospection commerciale »).

En cas de refus ou de non-réponse sous un mois : réclamation à la CNIL.

### 6.4 Le piège : la désinscription qui re-confirme

Certains courtiers exigent, pour te désinscrire, que tu confirmes ton identité et tes données déjà détenues. Cela peut paradoxalement *enrichir* leur base si tu fournis des données qu’ils n’avaient pas. Règle : fournis le strict minimum exigé légalement, et conserve une copie de tes envois.

Autre piège : la désinscription via un courtier *re-confirme* qu’un humain réel se cache derrière ce profil. Pour certains courtiers, c’est plus précieux que la donnée brute.

### 6.5 Maintenance : le ré-empilage et la routine semestrielle

Les courtiers ré-acquièrent constamment de nouvelles données (achats de bases, agrégation depuis applications). Une désinscription n’est pas définitive. Il faut prévoir un cycle semestriel ou annuel :

1. Recherche de soi sur les principaux courtiers.
1. Identification des nouveaux apparitions.
1. Réémission des demandes RGPD.
1. Suivi des réponses.

C’est un travail à organiser, à dater, à documenter. Sans cette routine, tout reflue en six mois.

### 6.6 Limite réelle

Tu ne nettoieras jamais à 100 %. Certaines bases ne sont pas indexables, certaines fuites sont irrécupérables (une fois sur Telegram, une donnée y reste), certaines juridictions n’appliquent pas le RGPD. La désinscription est *complémentaire* à la compartimentation, pas un substitut. Pour les nouveaux comptes, tu créeras une nouvelle empreinte ; à toi de l’architecturer mieux.

-----

## Chapitre 7 — Doxxing : mécanique, prévention et réponse

### 7.1 Définition et formes

Le **doxxing** (parfois orthographié *doxing*) consiste à révéler publiquement des informations personnelles identifiantes (nom réel, adresse, employeur, contacts familiaux, photos privées) sur une cible, dans une intention nuisible : harcèlement, intimidation, atteinte professionnelle, violences physiques par procuration.

Formes principales :

- **Doxxing classique** : publication d’une fiche identifiante.
- **Swatting** : appel des forces d’intervention à l’adresse de la cible sous prétexte fallacieux. Documenté avec des morts aux États-Unis. Risque croissant en Europe.
- **Harcèlement coordonné** : campagne organisée (raid sur un compte, signalements coordonnés, messages massifs).
- **Doxxing par deepfake** : association de la cible à des contenus fabriqués (cf. Ch 34).
- **Doxxing patrimonial** : révélation d’informations sur la famille, les enfants, l’école, le lieu de travail.

### 7.2 Anatomie d’une opération de doxxing

Une opération typique suit cinq phases :

1. **Trigger** : action de la cible (publication, prise de position, conflit en ligne) qui motive l’attaque.
1. **Reconnaissance** : OSINT sur la cible (cf. Ch 5 inversé).
1. **Compilation** : assemblage d’une fiche avec les informations agrégées.
1. **Publication** : sur un forum hostile, un site dédié, ou via des canaux de chat.
1. **Amplification** : appel à harcèlement de masse.

La défense efficace agit aux phases 2 et 3 : réduire ce qui est trouvable, casser les corrélations qui permettent l’assemblage.

### 7.3 Profils particulièrement ciblés

Les données disponibles (rapports PEN America, Online Harassment Field Manual, Coalition Against Online Violence) identifient comme cibles surreprésentées : femmes journalistes, journalistes traitant de l’extrême-droite ou des questions de genre, activistes LGBTQ+, chercheurs sur les mouvements extrémistes, victimes de gamergates et de raids ciblés, témoins dans des affaires sensibles.

### 7.4 Prévention structurelle

Sept axes prioritaires :

1. **Adresse postale alternative** : boîte postale, domiciliation commerciale (légale, ~15-30€/mois), ou adresse d’un proche consentant. À utiliser pour tout enregistrement public, livraisons sensibles.
1. **Téléphone séparé** : un numéro pro distinct du numéro principal — eSIM, MVNO, ou service comme MySudo (US), JMP.chat. Ce numéro filtre les contacts professionnels.
1. **Hygiène photo** : éviter les arrière-plans identifiants, les marquages industriels (entreprises locales), les vues par fenêtre permettant la géolocalisation visuelle (cf. Ch 35).
1. **Audit de l’entourage** : tes proches publient-ils ton nom, ton adresse, tes photos ? Conversation diplomatique recommandée.
1. **Compartimentation des plateformes** : ton compte professionnel n’a pas besoin de mentionner ton compte personnel, et inversement.
1. **Filtrage des questions de récupération** : pas de question dont la réponse est dans tes posts publics (« nom de ton chien »).
1. **Surveillance proactive** : Google Alerts sur ton nom, monitoring HaveIBeenPwned (notifications automatiques de nouvelles fuites).

### 7.5 Réponse à doxxing en cours

Si tu es la cible d’un doxxing actif :

1. **Documenter** : captures d’écran, URLs, horodatages. Préserver les preuves avant suppression éventuelle.
1. **Signaler aux plateformes** : la plupart ont des procédures spécifiques anti-doxxing (X, Reddit, GitHub, Discord, etc.).
1. **Contacter les hébergeurs** (si nécessaire) : un site dédié peut être signalé à son hébergeur, à son registrar, et à son CDN.
1. **Évaluer la menace physique** : si l’adresse est publiée et qu’il y a menace crédible, prévenir les autorités, envisager un changement temporaire de logement.
1. **Soutien psychologique et juridique** : pas un détail. Le doxxing est traumatisant. PEN America, GIJN, RSF, La Quadrature, Reporters Sans Frontières proposent des aides selon les profils.
1. **Plainte** : en France, le doxxing peut tomber sous plusieurs qualifications (atteinte à la vie privée, violation du secret des correspondances, mise en danger délibérée, harcèlement). PHAROS pour le signalement.

### 7.6 *Fil rouge* — Léa découvre son adresse sur un forum

Trois semaines après une publication intermédiaire sur son enquête, Léa reçoit une capture d’écran d’un canal Telegram : son adresse postale, son numéro de téléphone, et le nom de son père y sont publiés, avec « cette journaliste mérite une visite ». Application immédiate de la procédure ci-dessus. Mise en alerte de son entourage proche. Dépôt de plainte. Et surtout, leçon : son adresse était dans le registre du commerce belge (entreprise individuelle) — elle bascule en SCI avec domiciliation commerciale dans la semaine.

-----

## Chapitre 8 — Réseaux sociaux et exposition publique

### 8.1 Le modèle économique = surveillance

Les paramètres « privacy » des plateformes ne neutralisent pas le modèle : la plateforme te surveille toujours en interne (clics, durée de visualisation, position du pouce, contacts, photos, métadonnées). Ce qu’ils contrôlent, c’est ce que d’autres utilisateurs voient de toi. Ne pas confondre les deux.

### 8.2 Audit de présence

Avant de durcir, mesure. Pour chaque plateforme où tu as un compte :

- Date de création, fréquence d’usage.
- Quelles informations sont publiques sur ton profil (nom, date de naissance, employeur, ville, école, téléphone).
- Quelles photos sont publiques et taguées.
- Quelles relations sont publiques (followers, amis, contacts).
- Quel historique de publication est public et combien remonte.
- Quels paramètres de confidentialité par défaut sont actifs.

Pour Facebook spécifiquement, utiliser l’outil intégré « Apparaître en tant que » pour voir ton profil comme un inconnu le voit. Découverte fréquente : ce que tu croyais privé est public.

### 8.3 Paramétrage défensif par plateforme

**Facebook / Meta** : profil verrouillé (public uniquement nom et photo), audience par défaut « Amis », désactivation de la reconnaissance faciale, désactivation du tagging automatique, restriction des recherches par email/téléphone, vérification de l’historique de publications.

**Instagram** : compte privé si possible, désactivation du suggéré, désactivation de la synchronisation des contacts (Instagram aspire ton carnet d’adresses si activé), audit des photos taguées.

**X (Twitter)** : protéger les tweets si pertinent, désactiver la découverte par email/téléphone, désactiver les DM ouverts si pas indispensable.

**LinkedIn** : limitation de la visibilité du profil aux moteurs (paramètre dédié), choix de ce qui apparaît au public vs aux connexions, suppression des notifications publiques de changements (« John updated his profile »), désactivation du « people you may know ».

**TikTok** : compte privé, désactivation du téléchargement de tes vidéos par d’autres, restriction des duets/stitch.

**Bluesky, Mastodon** : décentralisé, mais ton serveur (instance) voit tout. Choisir une instance de confiance. Comportement à publication reste sous ton contrôle.

### 8.4 Photos et tagging

Les photos sont le vecteur sous-estimé. Quatre risques :

1. **Géolocalisation** : EXIF + arrière-plan + indices visuels.
1. **Identification croisée** : la même photo sur deux comptes les corrèle.
1. **Reconnaissance faciale** : PimEyes et FaceCheck.ID indexent en continu.
1. **Tagging par des tiers** : tu n’as pas le contrôle de ce que tes proches publient avec toi.

Mesures : photos de profil dédiées (jamais utilisées ailleurs), demande explicite à tes proches de ne pas te taguer, désactivation des suggestions de tag automatique, audit régulier des photos publiées par d’autres.

### 8.5 Métadonnées invisibles côté plateforme

Même quand une plateforme retire les EXIF côté serveur (la plupart le font), elle conserve en interne : horodatage exact, géolocalisation au moment de l’upload, modèle d’appareil. Ces données ne sont pas publiques mais sont accessibles à la plateforme et, sur réquisition, aux autorités.

### 8.6 Silence stratégique

Ce que tu **ne publies pas** compte autant que ce que tu publies :

- Pas de photos de vacances en temps réel (signale ta maison vide).
- Pas de check-in dans des lieux récurrents (signale tes habitudes).
- Pas d’humeur en temps réel sur tes opinions politiques clivantes si tu vis dans un contexte risqué.
- Pas de mention de tes proches sans leur consentement.
- Pas d’achat coûteux affiché (signale la valeur de ton logement).

### 8.7 Suppression vs désactivation vs anonymisation

**Désactivation** : compte invisible mais récupérable. Tes données restent chez la plateforme.

**Suppression** : effacement (en théorie) après un délai de grâce (30 jours typiquement). En pratique, les sauvegardes plateformes peuvent conserver certaines données plus longtemps. Les archives publiques (Wayback, ArchiveTeam) conservent ce qu’elles ont aspiré.

**Anonymisation progressive** : changer nom, photo, biographie, mais garder le compte. Permet de conserver l’historique de relations sans afficher l’identité. Utile sur les comptes anciens.

### 8.8 Alternatives décentralisées

Mastodon et Bluesky proposent un modèle fédéré qui change la juridiction (instance choisie) et le modèle économique (souvent associatif). Mais :

- Tes posts sont publics par design.
- Ton instance voit tout (administrateur compris).
- La fédération expose certaines données à d’autres instances.

Ce ne sont pas des refuges privacy, ce sont des alternatives au modèle économique. Pas la même chose.

-----

## Chapitre 9 — Compartimentation et hygiène comportementale

### 9.1 Principe directeur

La compartimentation consiste à structurer ta vie numérique en compartiments étanches, tels que la compromission de l’un n’expose pas les autres. C’est l’architecture défensive la plus puissante disponible à un individu, et celle qui demande le plus de discipline.

Règle : *deux choses qui ne doivent pas être reliées ne doivent jamais l’être par un identifiant commun*. Email, téléphone, photo, appareil, IP, mot de passe, style d’écriture, horaire — chacun peut être un pont.

### 9.2 Niveaux d’identité

Cinq niveaux typiques à distinguer :

1. **Identité légale** : nom civil, état civil, documents administratifs. Pour les démarches officielles, le travail, les contrats, les comptes bancaires.
1. **Identité professionnelle** : nom (peut différer si pseudonyme journalistique), email pro, présence professionnelle. Compartiment majeur pour beaucoup de profils.
1. **Pseudonyme stable** : présence en ligne sous nom de plume, militante, communautaire. Pas anonyme (long terme), mais distinct de l’identité civile.
1. **Pseudonyme jetable** : compte créé pour un usage ponctuel, abandonné après.
1. **Identité anonyme** : pour des actions où l’attribution doit être impossible (sources sensibles, lanceurs d’alerte avant divulgation).

Tous les niveaux n’ont pas le même besoin de défense. Mais ceux qui doivent rester séparés doivent l’être *complètement*.

### 9.3 Compartimenter par dimension

Cinq dimensions de compartimentation :

|Dimension          |Compartimentation faible            |Compartimentation forte                           |
|-------------------|------------------------------------|--------------------------------------------------|
|**Appareil**       |Profils OS séparés                  |Appareils physiquement distincts                  |
|**Compte**         |Comptes séparés sur même fournisseur|Fournisseurs différents par usage                 |
|**Numéro**         |Cartes SIM différentes              |Réseaux différents (eSIM + physique + service IP) |
|**Paiement**       |Cartes virtuelles différentes       |Cartes physiques + cash + dénoués géographiquement|
|**Lieu et horaire**|Distinction maison/bureau           |Lieux totalement disjoints, horaires distincts    |

Le niveau adéquat dépend du threat model. Un journaliste enquêtant sur la criminalité organisée a besoin d’une compartimentation forte de la dimension *appareil* et *numéro* au minimum.

### 9.4 Réutilisation : les corrélateurs silencieux

Les corrélations les plus efficaces ne demandent aucune compétence technique. La réutilisation d’un même identifiant entre deux compartiments les corrèle automatiquement :

- Même email : trivial à corréler.
- Même mot de passe entre comptes : la fuite de l’un dévoile l’autre.
- Même pseudo : `whatsmyname.app` te trouve sur 300 services en quelques secondes.
- Même numéro de téléphone : agrégateurs (Truecaller, Sync.me) corrèlent à grande échelle.
- Même photo de profil : reverse image trouve en quelques minutes.
- Même biographie textuelle : recherche exacte sur Google.

### 9.5 Corrélation par style, contacts, métadonnées

Au-delà des identifiants explicites, des corrélations probabilistes :

- **Style d’écriture** (stylométrie, Ch 35) : longueur de phrases, virgules, expressions, fautes typiques.
- **Horaires de connexion** : ton compte « anonyme » se connecte aux mêmes heures que ton compte nominal.
- **Contacts communs** : deux comptes qui suivent les mêmes 50 personnes sont probablement la même.
- **Appareil/navigateur** : même fingerprint navigateur (cf. Ch 23) = même session probable.
- **IP** : connexion depuis le même réseau domestique sur deux comptes les corrèle (à moins de VPN).
- **Métadonnées de fichiers** : un document publié sous pseudonyme avec l’auteur metadata DOCX = nom civil dans le PDF.

### 9.6 L’erreur ponctuelle qui suffit

La compartimentation rigoureuse, c’est une discipline continue. **Une seule erreur peut la détruire**. Trois exemples historiques :

- Ross Ulbricht (Silk Road) : pseudonyme « altoid » sur un forum cryptographique posté avec son email gmail au format `rossulbricht@gmail.com`. Cf. Annexe 8.
- Hector Monsegur (Sabu, LulzSec) : connexion une seule fois à IRC sans Tor depuis son IP domestique. Cf. Annexe 8.
- Cas Reality Winner : impression d’un document classifié sur l’imprimante de son employeur. Les yellow dots (Ch 31) identifiaient l’imprimante, la date, l’heure. Cf. Annexe 8.

Conséquence opérationnelle : **les routines tuent les erreurs**. Si un comportement sensible est automatique (par exemple : impossibilité physique de se connecter au compte sensible depuis le téléphone quotidien parce qu’aucune appli n’est installée), l’erreur est structurellement empêchée.

### 9.7 Fatigue OPSEC, impulsivité, urgence

La compartimentation est attaquée de l’intérieur par trois ennemis humains :

- **Fatigue** : maintenir deux téléphones, plusieurs comptes, plusieurs gestionnaires de mots de passe, c’est lourd. Au bout de six mois, on relâche.
- **Impulsivité** : « juste cette fois, je me connecte vite à mon compte X depuis ce téléphone ». Une fois suffit pour casser la séparation.
- **Urgence** : un événement (deadline, alerte familiale, opportunité professionnelle) pousse à enfreindre les règles « pour cette fois ».

Défenses : (a) automatiser et désautoriser ; (b) accepter que la friction est le prix de la sécurité ; (c) prévoir des protocoles d’urgence qui ne nécessitent pas d’enfreindre la compartimentation.

### 9.8 Routines pour limiter les erreurs

- Démarrer chaque session sensible par une checklist physique (carte plastifiée, post-it).
- Avoir un appareil dédié physiquement distinct, jamais le « téléphone du moment ».
- Établir des règles non négociables : « jamais cet email sur cet appareil », « jamais ce compte sans VPN ».
- Audit trimestriel des dérives.

### 9.9 Cadrage éthique

La compartimentation et le pseudonymat sont des outils défensifs *légitimes*. Un journaliste qui utilise un pseudonyme pour ses enquêtes, un lanceur d’alerte qui sépare ses canaux, une victime de violences conjugales qui restructure ses comptes pour échapper à un ex-partenaire abusif : tous exercent des droits.

Ce n’est pas le sujet de ce cours d’aborder l’usurpation d’identité, la création de faux profils trompeurs, ou la fraude à pseudonymes. Ces pratiques sont pénalement répréhensibles dans la plupart des juridictions et ne relèvent pas de la sécurité défensive.

-----

> 🟦 **Capstone 1 — Construire son architecture de compartimentation**
> 
> **Objectif** : produire pour soi une matrice de compartimentation opérationnelle, applicable dans les 7 jours.
> 
> **Livrable** : un tableau cinq colonnes (Identité / Appareils / Comptes / Paiements / Canaux) pour chacun de tes compartiments principaux. Pour chaque ligne, identifier les ponts existants (ce qui *relie* deux compartiments) et les éliminer un à un.
> 
> **Exemple — Léa, fin de capstone** :
> 
> |Compartiment         |Identité                            |Appareils                      |Comptes                                |Paiements              |Canaux                                   |
> |---------------------|------------------------------------|-------------------------------|---------------------------------------|-----------------------|-----------------------------------------|
> |Vie civile et famille|Léa Martens (nom civil)             |iPhone perso, MacBook Air perso|iCloud personnel, Gmail perso          |CB BNP perso           |iMessage, WhatsApp avec proches          |
> |Vie pro publique     |Léa Martens journaliste             |MacBook Pro pro                |Proton Mail pro, comptes sociaux pro   |CB pro                 |Email, Signal pro                        |
> |Enquête sensible     |Pseudo non utilisé (compte distinct)|Pixel 8a + GrapheneOS dédié    |Compte SimpleX dédié, Proton avec alias|Cash + cartes prépayées|SimpleX, OnionShare, Signal compartimenté|
> 
> **Ponts à éliminer identifiés par Léa** :
> 
> - Carnet d’adresses iCloud personnel contient des numéros de sources potentielles → migration vers carnet pro.
> - Synchronisation iCloud des photos perso pourrait remonter à des photos pro accidentelles → désactivation de la sync auto, tri manuel.
> - Même MacBook Air pour usage perso et certains comptes pro → bascule vers MacBook Pro pour tout pro.
> - Compte Twitter perso suit le pseudo qui sera utilisé pour publication d’enquête → désabonnement préalable.
