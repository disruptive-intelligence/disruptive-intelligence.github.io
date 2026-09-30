---
title: PARTIE II — SOCIAL ENGINEERING NUMÉRIQUE
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 2
chapters: 7
---

---

## Chapitre 6 — Phishing : méthodologie et sophistication

### 6.1 Anatomie d'un email de phishing

Un email de phishing est un système de composantes interdépendantes, chacune contribuant à la crédibilité globale du leurre. Comprendre ces composantes est essentiel pour le praticien — qu'il construise un test autorisé ou qu'il analyse une attaque en cours.

**L'expéditeur.** C'est le premier élément évalué par le destinataire — souvent le seul, sur mobile. L'attaquant dispose de plusieurs techniques pour simuler un expéditeur légitime. Le spoofing d'adresse exploite l'absence ou la mauvaise configuration de SPF/DKIM/DMARC pour envoyer un email qui affiche une adresse légitime dans le champ « From ». Le typosquatting utilise un domaine visuellement similaire (helios-aero.fr → heIios-aero.fr avec un « I » majuscule à la place du « l », ou helios-aer0.fr avec un zéro). Le display name spoofing modifie le nom affiché sans toucher à l'adresse réelle : « Marc Tessier - DG Helios » <attaquant@domaine-malveillant.com> — sur mobile, seul le display name est visible par défaut. La compromission d'email légitime (reply-chain attack) est la technique la plus difficile à détecter : l'attaquant compromet une boîte mail réelle et s'insère dans un fil de conversation existant.

**L'objet.** L'objet détermine l'ouverture de l'email. Les objets les plus efficaces combinent pertinence contextuelle et urgence modérée : « Mise à jour obligatoire — Portail RH » est plus efficace que « URGENT !!! Votre compte sera supprimé !!! » (trop agressif, signaux d'alerte). Les objets qui exploitent la curiosité (« Résultats évaluation annuelle 2025 ») ou l'intérêt professionnel (« Invitation keynote — Congrès Aéronautique Lyon ») ont des taux d'ouverture supérieurs.

**Le corps.** Le corps doit être cohérent avec l'expéditeur et l'objet, utiliser la terminologie de l'entreprise cible, et inclure un appel à l'action clair mais non agressif. Les erreurs de langue, autrefois marqueur fiable de phishing, sont en voie de disparition grâce aux LLM qui génèrent des textes grammaticalement parfaits et stylistiquement adaptés au contexte culturel.

**Le lien ou la pièce jointe.** C'est le vecteur technique : URL vers une landing page de collecte d'identifiants, document piégé (macro Office, fichier HTA, fichier ISO/IMG contenant un exécutable), QR code redirigeant vers un site malveillant, ou pièce jointe légitime (document PDF inoffensif) dans une reply-chain attack où le vrai piège est l'établissement de la confiance pour une demande ultérieure (BEC).

**La landing page.** Pour le credential harvesting, la landing page reproduit l'interface de connexion de la cible (Microsoft 365, Google Workspace, VPN d'entreprise, portail RH). Les kits de phishing modernes reproduisent ces interfaces pixel par pixel, y compris les certificats TLS (Let's Encrypt fournit des certificats gratuits — le cadenas vert ne garantit plus rien). Les techniques de reverse proxy (Evilginx, Modlishka) capturent non seulement les identifiants mais aussi les tokens de session, contournant ainsi le MFA classique (voir Ch.10 pour le détail).

### 6.2 Niveaux de sophistication

Le phishing n'est pas une technique unique — c'est un spectre de sophistication dont chaque niveau a ses techniques, ses cibles et ses contre-mesures.

**Le phishing de masse (spray & pray).** Campagnes non ciblées envoyées à des dizaines de milliers d'adresses. Faible taux de réussite individuel (1-3 %), mais rentable par le volume. Les leurres sont génériques : notification de livraison, facture impayée, mise à jour de sécurité bancaire. Contre-mesures : filtrage email, sensibilisation de base, DMARC strict.

**Le spear-phishing.** Campagnes ciblées sur un groupe restreint (une entreprise, un service, un groupe de projet). Les leurres sont personnalisés : terminologie interne, noms de projets, références aux supérieurs hiérarchiques. Taux de réussite significativement supérieur (15-40 % selon la qualité de la personnalisation). Contre-mesures : filtrage avancé avec analyse comportementale, sensibilisation ciblée, bannières « email externe », simulation de phishing régulière.

**Le BEC/whaling.** Attaques ciblées de haute valeur (dirigeants, DAF, comptabilité). Pas de malware, pas de lien malveillant — pure manipulation par email. L'attaquant usurpe l'identité d'un dirigeant, d'un avocat ou d'un fournisseur pour obtenir un virement ou une information sensible. Taux de réussite variable mais impact unitaire très élevé (dizaines de milliers à dizaines de millions d'euros par incident). Contre-mesures : processus de double validation pour les virements, callback sur numéro connu, culture de la vérification. Le BEC est traité en détail au Ch.9.

### 6.3 Construction d'un lure crédible

La crédibilité d'un lure de phishing repose sur quatre piliers : le contexte, le timing, la personnalisation et l'urgence calibrée.

**Le contexte.** Le meilleur lure s'inscrit dans un contexte que la cible attend ou connaît. Si l'entreprise est en pleine migration vers Microsoft 365, un email sur la mise à jour des identifiants sera perçu comme normal. Si une conférence sectorielle approche, une invitation de dernière minute sera crédible. La reconnaissance OSINT (Ch.5) fournit ces contextes.

**Le timing.** Le lundi matin (accumulation d'emails du week-end, traitement rapide), le vendredi après-midi (fatigue, volonté de conclure la semaine), la veille de vacances (stress de dernière minute, départs précipités), la période de clôture comptable (pression, urgence des validations) sont des fenêtres de vulnérabilité documentées.

**La personnalisation.** L'utilisation du nom du destinataire, de son service, de son manager, d'un projet sur lequel il travaille, d'un événement récent (formation, séminaire, réorganisation) augmente la crédibilité de manière exponentielle. Un email qui mentionne « suite à votre réunion avec Frédéric Morin hier » est perçu comme interne avant même d'être analysé.

**L'urgence calibrée.** L'urgence doit être suffisante pour déclencher une action rapide mais insuffisante pour paraître suspecte. « Veuillez valider avant fin de journée » est plus efficace que « URGENT — action immédiate requise !!!». L'urgence fonctionne en réduisant le temps disponible pour la réflexion et la vérification.

### 6.4 L'infrastructure de phishing

La construction d'une infrastructure de phishing crédible est un savoir-faire technique qui évolue rapidement.

**Domaines lookalike et typosquatting.** L'enregistrement de domaines similaires à celui de la cible (heIios-aero.fr, helios-aero.com, helios-aeronautique.fr) permet de créer des adresses email et des URLs visuellement proches de l'original. Les domaines internationalisés (IDN — utilisant des caractères Unicode visuellement identiques aux caractères ASCII) ajoutent une couche de sophistication. Contre-mesure : surveillance proactive des enregistrements de domaines similaires, DMARC en mode « reject ».

**Compromission d'email légitime (reply-chain attack).** L'attaquant compromet une boîte mail réelle (par phishing préalable, credential stuffing ou achat sur le darkweb) et s'insère dans un fil de conversation existant. Cette technique est extrêmement difficile à détecter car l'email provient d'une adresse légitime, dans un fil de conversation légitime, avec un historique de conversation réel.

**Contournement de SPF/DKIM/DMARC.** SPF vérifie que le serveur d'envoi est autorisé par le domaine. DKIM signe cryptographiquement l'email. DMARC combine les deux et définit une politique de rejet. En configuration stricte (DMARC p=reject), ces protocoles bloquent le spoofing direct du domaine. Mais ils ne protègent pas contre le typosquatting, les domaines lookalike, le compromission d'email légitime ou le display name spoofing. La protection email est une défense en profondeur, pas une solution unique.

### 6.5 Red team phishing vs attaquant réel

Le red teamer et l'attaquant réel utilisent les mêmes techniques — mais dans un cadre radicalement différent. Le red teamer documente chaque étape (emails envoyés, taux de clic, identifiants collectés, temps avant signalement), ne compromet pas réellement les systèmes (les identifiants collectés sont stockés de manière sécurisée et jamais exploités), produit un rapport factuel et constructif, et forme les employés sur les mécanismes exploités. L'attaquant réel exploite immédiatement les identifiants collectés, latéralise dans le réseau, exfiltre des données et peut persister pendant des mois. Cette différence de finalité est fondamentale, mais les techniques sont identiques — ce qui permet au red team d'évaluer la vulnérabilité réelle de l'organisation.

---

## Chapitre 7 — Vishing : l'arme de la voix

### 7.1 Pourquoi le vishing est plus dangereux que le phishing

Le vishing (voice phishing) est, de l'avis consensuel des praticiens de red team, le vecteur de social engineering le plus efficace. Plusieurs facteurs expliquent cette efficacité supérieure au phishing par email.

La voix crée un lien personnel et immédiat. Un email est un objet passif que le destinataire peut analyser à son rythme, comparer avec des exemples connus, transférer à un collègue pour avis. Un appel téléphonique est une interaction en temps réel qui engage émotionnellement le destinataire et ne lui laisse pas le temps de la réflexion distanciée.

La pression est exercée en temps réel. L'attaquant ajuste son discours en fonction des réponses de la cible : s'il perçoit une hésitation, il renforce l'urgence ; s'il perçoit de la méfiance, il change d'angle ; s'il perçoit de la coopération, il escalade. Cette adaptabilité en temps réel est impossible par email.

L'autorité vocale est puissante. Un ton assuré, un vocabulaire technique maîtrisé, un rythme de parole contrôlé projettent une autorité que le texte écrit reproduit difficilement. L'expérience de Milgram a démontré que la présence physique (ou vocale) de la figure d'autorité augmente significativement la compliance.

La documentation est plus difficile. Un email suspect peut être transféré au SOC pour analyse (headers, URLs, pièces jointes). Un appel téléphonique ne laisse pas de trace exploitable (sauf enregistrement — qui pose des questions légales dans de nombreuses juridictions). Le signalement d'un appel suspect repose sur la mémoire et le récit de l'employé.

### 7.2 Les pretextes classiques du vishing

Les pretextes de vishing les plus efficaces exploitent des situations où un appel téléphonique est attendu ou normal.

**Le support IT.** « Bonjour, je suis Paul de l'équipe support informatique. Nous avons détecté une activité suspecte sur votre compte — je dois vérifier quelques informations avec vous pour sécuriser votre accès. » Ce pretexte est redoutablement efficace parce qu'il combine autorité (IT), urgence (activité suspecte) et bienveillance (sécuriser votre compte). Le rapport Unit 42 2025 documente de nombreux cas où ce pretexte a permis le reset de credentials MFA via le helpdesk.

**Le prestataire ou fournisseur.** Après avoir identifié le prestataire IT par OSINT, l'attaquant se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. La crédibilité est renforcée par la connaissance du nom du prestataire, du contrat en cours, des interlocuteurs habituels.

**La direction.** « Bonjour, je suis l'assistante de Marc Tessier. Il est en déplacement et il a besoin que vous fassiez un virement urgent — je vous envoie les coordonnées par email. » La combinaison appel + email (social engineering multi-canal, détaillé au Ch.8) renforce la crédibilité.

**Le recruteur.** Approche LinkedIn suivie d'un appel : « Suite à votre profil que j'ai trouvé très intéressant, j'ai une opportunité confidentielle à vous présenter. » Ce pretexte est le vecteur préféré des groupes APT comme Lazarus (opération « Dream Job ») et des services de renseignement pour l'élicitation (voir Ch.3 et Ch.17).

### 7.3 Techniques vocales

La voix est un outil qui se travaille. Les red teamers expérimentés maîtrisent plusieurs techniques vocales qui augmentent l'efficacité du vishing.

**Le matching de ton.** Adapter son registre au profil de la cible : formel et technique avec un ingénieur, chaleureux et empathique avec une réceptionniste, directif et pressé avec un cadre. Le ton doit être cohérent avec le pretexte — un technicien IT qui parle comme un commercial ou un DG qui parle comme un stagiaire crée une dissonance cognitive qui active la vigilance.

**Le name-dropping.** Mentionner des noms de personnes réelles de l'organisation (collectés par OSINT) est l'un des marqueurs de crédibilité les plus puissants. « Frédéric Morin m'a demandé de vous appeler » ou « j'ai vu avec Lucie Ferraro hier » crée un lien implicite avec l'organisation qui désarme la méfiance.

**Le « oui building ».** Commencer par des questions auxquelles la réponse est évidemment « oui » (« c'est bien le poste de [nom] ? », « vous êtes bien dans le service [service] ? ») avant d'escalader vers la demande réelle. Chaque « oui » renforce l'engagement de la cible dans la conversation (principe d'engagement et de cohérence, Ch.2).

**Le silence stratégique.** Après avoir posé une question sensible, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le silence dans une conversation téléphonique et le comblent en parlant — souvent en fournissant plus d'information que ce qui leur était demandé. Le silence est l'une des techniques d'élicitation les plus sous-estimées.

### 7.4 Caller ID spoofing

Le caller ID spoofing permet à l'attaquant d'afficher un numéro de téléphone arbitraire sur l'écran de la cible. Des services en ligne (SpoofCard, SpoofTel — attention, l'usage est réglementé dans de nombreuses juridictions et interdit pour fraude) et des services VoIP configurables permettent de simuler le numéro du standard de l'entreprise, du prestataire IT ou même du supérieur hiérarchique.

Le protocole STIR/SHAKEN (Secure Telephony Identity Revisited / Signature-based Handling of Asserted information using toKENs), déployé aux États-Unis depuis 2021 et en cours de déploiement en Europe, vise à authentifier l'identité de l'appelant au niveau du réseau téléphonique. En 2025, son déploiement reste inégal et contournable dans certains contextes (appels internationaux, réseaux VoIP non conformes). La contre-mesure la plus fiable reste le callback de vérification : ne jamais agir sur la base d'un appel entrant sans rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel).

### 7.5 Le vishing AI-enabled : deepfake vocal

Le clonage vocal par IA représente la menace émergente la plus sérieuse en matière de vishing. En 2025, plusieurs plateformes permettent de cloner une voix à partir d'échantillons de quelques secondes à quelques minutes (ElevenLabs, Respeecher, technologies open source). La qualité est suffisante pour tromper un interlocuteur non prévenu dans un appel téléphonique standard.

Les cas documentés se multiplient. En 2024, une entreprise de Hong Kong a perdu 25 millions de dollars dans une fraude utilisant un deepfake vidéo et vocal du CFO en visioconférence (plusieurs « participants » étaient des deepfakes en temps réel). Des cas de vishing par deepfake vocal ciblant des DAF pour des virements urgents ont été rapportés par plusieurs cabinets d'incident response.

Les défenses sont encore immatures. Les détecteurs de deepfake vocal existent mais sont peu fiables en conditions réelles (environnement bruité, compression téléphonique, variété des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible (virement, reset de credentials, communication d'informations confidentielles), imposer une vérification out-of-band (callback sur numéro connu, confirmation par un second canal, validation hiérarchique). La technologie seule ne suffit pas — le processus est la dernière ligne de défense.

---

## Chapitre 8 — Smishing, messageries, collaboration et vecteurs alternatifs

### 8.1 SMS et smishing

Le smishing (SMS phishing) exploite les spécificités du canal SMS : messages courts, contexte limité, URLs raccourcies qui masquent la destination réelle, et confiance instinctive dans les SMS (perçus comme plus personnels et plus fiables que les emails). Le spoofing d'expéditeur SMS (sender ID spoofing) permet d'afficher un nom d'entreprise (« Helios-RH », « IT-Support ») au lieu d'un numéro, ce qui renforce la crédibilité.

Les pretextes classiques incluent : notification de livraison avec lien de suivi, alerte bancaire avec demande de vérification, message RH sur les congés ou la paie, et alerte de sécurité (« accès suspect à votre compte »). Les taux de clic sur SMS sont généralement supérieurs à ceux sur email, parce que les utilisateurs mobiles sont moins entraînés à la vigilance sur ce canal et que les indicateurs de fraude (URL complète, en-têtes, adresse d'expéditeur) sont moins visibles sur un écran de smartphone.

### 8.2 Messageries chiffrées et réseaux sociaux

WhatsApp, Signal, Telegram et les messageries intégrées des réseaux sociaux sont devenus des vecteurs de social engineering à part entière. Leur utilisation par les attaquants s'explique par plusieurs facteurs : le chiffrement de bout en bout complique la surveillance et l'analyse par les équipes de sécurité, le sentiment de confidentialité encourage le partage d'informations sensibles, et les fonctionnalités de messages éphémères réduisent les traces.

**LinkedIn InMail** est le vecteur de choix pour le ciblage professionnel. Les faux recruteurs (vecteur utilisé par le groupe APT Lazarus dans l'opération « Dream Job » et par des services de renseignement pour l'élicitation) exploitent la norme de la plateforme : recevoir un InMail d'un recruteur est un événement normal et positif sur LinkedIn. La transition vers WhatsApp ou Signal (« pour discuter plus librement ») isole la cible du contexte professionnel et élimine les contrôles de la plateforme.

**Les groupes** sur Telegram, Discord et WhatsApp sont exploités pour le social engineering de masse ciblé : infiltrer un groupe professionnel ou communautaire permet de gagner de la crédibilité par la présence dans un espace de confiance, de collecter de l'information en écoutant les conversations, et d'approcher des cibles individuelles avec un pretexte renforcé (« on est dans le même groupe sur le forum X »).

### 8.3 Suites collaboratives : Teams, Slack, Google Workspace

Les plateformes de collaboration d'entreprise sont devenues des vecteurs de social engineering majeurs depuis la généralisation du travail hybride. Le rapport Unit 42 2025 documente plusieurs cas d'intrusions initiées via ces plateformes.

**Microsoft Teams.** L'ouverture des communications externes (External Access) permet à un attaquant d'envoyer des messages à des employés depuis un tenant Microsoft 365 externe. L'interface Teams affiche un avertissement « externe » souvent ignoré. Les pretextes incluent : partage de document « urgent » (lien vers une landing page de phishing), invitation à une réunion (lien Zoom/Meet malveillant), et prise de contact par un faux collègue d'un autre site ou d'un partenaire.

**Faux partages de documents.** Les notifications OneDrive/SharePoint/Google Drive « [Nom] a partagé un document avec vous » sont exploitées pour le phishing. L'attaquant crée un document sur sa propre instance et le partage avec la cible. Le lien pointe vers une page de connexion légitime (Microsoft ou Google) qui capture les identifiants ou les tokens de session. La difficulté est que le mécanisme de partage est identique au mécanisme légitime — seule l'analyse de l'expéditeur et du contexte permet de distinguer un partage légitime d'un phishing.

**OAuth consent phishing (consent grant attack).** L'attaquant crée une application OAuth malveillante qui demande des permissions d'accès au compte de la cible (lecture des emails, accès aux fichiers, accès au calendrier). La cible est redirigée vers une page de consentement légitime (Microsoft ou Google) et autorise l'accès — l'attaquant obtient alors un token d'accès persistant qui survit au changement de mot de passe et au MFA. Cette technique est particulièrement insidieuse parce que la page de consentement est une page légitime de Microsoft ou Google, pas une page de phishing. La défense repose sur la restriction des applications tierces autorisées (Azure AD : désactiver le consentement utilisateur, imposer l'approbation admin) et la surveillance des grants OAuth.

**Faux bots et automatisations.** Les plateformes comme Slack et Teams permettent l'intégration de bots et de workflows automatisés. Un attaquant qui compromet un workspace ou obtient un accès admin peut créer un faux bot (« Security-Bot », « HR-Assistant ») qui collecte des informations auprès des employés sous un pretexte automatisé.

### 8.4 QR codes malveillants (quishing)

Le quishing exploite les QR codes comme vecteur de redirection. L'utilisation massive des QR codes depuis 2020 (menus de restaurant, documents administratifs, affiches événementielles) a normalisé le scan de QR codes inconnus — ce qui constitue un vecteur d'attaque sous-estimé.

Les vecteurs de distribution incluent : QR codes physiques collés sur des panneaux légitimes (parking d'entreprise, accueil, salles de réunion), QR codes inclus dans des emails de phishing (contournant les filtres URL qui ne scannent pas les images), QR codes dans des documents imprimés (faux courriers RH, fausses affiches d'événement). La redirection pointe vers une landing page de credential harvesting ou un téléchargement de malware mobile.

La défense passe par la sensibilisation (ne pas scanner de QR code sans vérifier l'URL de destination — les smartphones modernes affichent l'URL avant la navigation), l'utilisation de QR codes sécurisés pour les communications légitimes de l'entreprise, et l'inspection physique régulière des QR codes affichés dans les locaux.

### 8.5 Social engineering multi-canal

La combinaison de plusieurs vecteurs dans une même opération augmente considérablement la crédibilité et le taux de succès. Le schéma typique est : email préparatoire → appel téléphonique → SMS de confirmation, ou approche LinkedIn → transition WhatsApp → appel téléphonique → demande par email.

Chaque canal renforce la crédibilité du précédent. Un email seul peut être analysé froidement. Mais un email suivi d'un appel téléphonique (« je vous appelle suite à l'email que je vous ai envoyé ce matin ») crée un effet de convergence qui désarme la vigilance — la cible perçoit une cohérence entre deux canaux distincts, ce qui renforce la perception de légitimité. Le rapport Unit 42 2025 documente cette hybridation croissante des tactiques où les techniques conventionnelles de social engineering sont de plus en plus complétées par des composantes multi-canaux.

---

## Chapitre 9 — BEC (Business Email Compromise) et fraude au président

### 9.1 Le BEC comme menace n°1 en pertes financières

Le Business Email Compromise est la forme de cybercriminalité la plus coûteuse au monde en termes de pertes financières directes. Les données de l'IC3 (Internet Crime Complaint Center) du FBI indiquent des pertes cumulées de plusieurs milliards de dollars par an aux États-Unis seuls. En France, les pertes liées à la fraude au président et aux arnaques au fournisseur se chiffrent en centaines de millions d'euros annuellement.

Le BEC est redoutable parce qu'il ne repose sur aucun composant technique sophistiqué : pas de malware, pas de vulnérabilité logicielle, pas de zero-day. C'est une attaque de pure manipulation humaine — un email suffisamment crédible pour déclencher un virement vers un compte contrôlé par l'attaquant. La détection technique est donc intrinsèquement limitée : l'email ne contient ni lien malveillant ni pièce jointe piégée — seulement du texte convaincant.

### 9.2 Les variantes du BEC

**La fraude au président (CEO fraud).** L'attaquant usurpe l'identité du dirigeant de l'entreprise et ordonne un virement urgent et confidentiel au responsable financier ou au comptable. Les éléments clés sont : l'urgence (« c'est pour une acquisition confidentielle, il faut agir avant 17h »), la confidentialité (« n'en parlez à personne d'autre — c'est stratégique et sensible »), l'autorité (le DG qui s'adresse directement à un subordonné en court-circuitant la hiérarchie normale) et la pression émotionnelle (« je compte sur vous personnellement »).

**La fraude au fournisseur (vendor email compromise).** L'attaquant se fait passer pour un fournisseur existant et envoie une facture avec des coordonnées bancaires modifiées. La technique est souvent précédée par la compromission de la boîte mail du fournisseur réel (reply-chain) ou par l'enregistrement d'un domaine lookalike. La détection est rendue difficile par le fait que la relation commerciale est réelle — seul l'IBAN a changé.

**La compromission de boîte mail (reply-chain BEC).** L'attaquant compromet une boîte mail interne ou celle d'un partenaire et s'insère dans des fils de conversation existants pour demander des virements ou des modifications de coordonnées bancaires. Cette variante est la plus difficile à détecter parce que l'email provient d'une adresse légitime avec un historique de conversation réel.

**Le faux avocat.** L'attaquant se présente comme un avocat ou un conseiller juridique intervenant dans le cadre d'une transaction confidentielle (acquisition, règlement de litige). La confidentialité est utilisée comme arme : « en raison de la sensibilité juridique de cette opération, je vous demande de ne pas en discuter avec vos collègues ». Cette tactique isole la cible et neutralise le réflexe de vérification.

### 9.3 La construction de l'arnaque

Le BEC réussi repose sur une reconnaissance approfondie. L'attaquant identifie : l'organigramme (qui a le pouvoir de valider un virement, qui est le supérieur hiérarchique direct), les processus de validation financière (seuils, doubles signatures, circuits de validation), les habitudes de communication du dirigeant usurpé (ton, style, formules de politesse, horaires d'envoi), et les fenêtres d'opportunité (déplacement du DG — vérifiable par LinkedIn, agenda public, conférences ; absence du DAF ; périodes de clôture comptable).

Le timing est critique. Le vendredi après-midi (les virements envoyés le vendredi ne sont pas vérifiés avant lundi), la veille de vacances, les périodes de déplacement du dirigeant (impossible de vérifier en personne) sont les fenêtres les plus exploitées.

### 9.4 Deepfake et BEC

L'utilisation de deepfakes vidéo et vocaux dans les BEC représente une évolution qualitative de la menace. Le cas de Hong Kong de début 2024, où une entreprise a perdu l'équivalent de 25 millions de dollars suite à une visioconférence entièrement composée de deepfakes en temps réel, illustre le potentiel destructeur de cette convergence. L'employé ciblé a participé à un appel vidéo où plusieurs participants — dont le CFO — étaient des deepfakes générés en temps réel. La qualité était suffisante pour ne pas éveiller de soupçon pendant toute la durée de l'appel.

Cette évolution remet en question les défenses traditionnelles du BEC. Le callback vocal était considéré comme une contre-mesure fiable — mais si la voix de l'interlocuteur peut être clonée, le callback perd son pouvoir de vérification. La réponse passe par des vérifications multi-facteurs non reproductibles par l'IA : question de sécurité personnelle, vérification physique en présentiel, code de confirmation envoyé par un canal distinct et préétabli.

### 9.5 Défense contre le BEC

La défense contre le BEC est fondamentalement procédurale, pas technologique. Les solutions techniques (détection d'anomalies dans les emails, alerte sur les changements de comportement d'expéditeur) sont utiles mais insuffisantes face à des attaques qui n'utilisent aucun indicateur technique malveillant.

**P0 — Processus de double validation pour tout virement inhabituel.** Aucun virement supérieur à un seuil défini ne peut être exécuté sans validation par deux personnes distinctes, dont au moins une par callback sur un numéro de référence connu (annuaire interne, pas le numéro indiqué dans l'email).

**P0 — Procédure de vérification des changements de coordonnées bancaires.** Tout changement d'IBAN (fournisseur, prestataire, client) fait l'objet d'un callback au fournisseur sur un numéro de référence connu, indépendamment du canal par lequel le changement a été demandé.

**P1 — Formation ciblée.** Les profils à risque (DAF, comptabilité, assistantes de direction, service achats) reçoivent une formation spécifique sur les scénarios de BEC avec des simulations réalistes.

**P1 — Alertes techniques.** Règles email signalant les emails d'expéditeurs externes utilisant des display names identiques à ceux de dirigeants internes, bannières « email externe » clairement visibles, alertes sur les domaines lookalike.

**P2 — Culture de la vérification.** Créer un environnement où vérifier une demande — même du DG — est perçu comme professionnel, pas comme de l'insubordination.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 3**
>
> **Campagne de phishing.** Yasmine lance la campagne de phishing ciblé depuis l'infrastructure de test (domaine enregistré : heIios-rh.fr — « I » majuscule au lieu de « l »). Deux pretextes sont utilisés :
>
> **Pretexte 1** — « Mise à jour obligatoire du portail RH — Entretien annuel 2025 ». Email reproduisant le template visuel d'Helios (couleurs et logo récupérés sur le site web), renvoyant vers une page de connexion Microsoft 365 factice. Envoyé à 80 employés du siège et de Bordeaux le lundi matin à 8h15.
>
> **Pretexte 2** — « Invitation conférence Aéronautique & Défense — Lyon, juin 2025 ». Email ciblé sur 40 ingénieurs R&D et cadres, exploitant l'intérêt professionnel et la curiosité.
>
> **Résultats après 72h** : sur 120 emails envoyés, 34 clics (28,3 %), 18 identifiants collectés (15 %), dont 2 comptes avec des privilèges administrateurs IT (un admin Exchange et un admin Azure AD). Taux de signalement au SOC : 3 emails signalés (2,5 %) — tous dans les 4 premières heures, puis plus rien.
>
> Lucie Ferraro, la RSSI, est surprise par les résultats : « On fait des campagnes de sensibilisation e-learning chaque trimestre depuis deux ans. Les scores au quiz sont bons. » Nathan explique : « Le quiz mesure la reconnaissance théorique des signaux de phishing dans un contexte d'examen. Notre campagne mesure le comportement réel face à un leurre crédible, en conditions de stress et de multitâche. Ce sont deux choses différentes. »

---

## Chapitre 10 — Intrusion numérique par social engineering : identité, SSO, MFA et workflows

### 10.1 Social engineering du helpdesk

Le helpdesk est la surface d'attaque la plus sous-estimée en matière de social engineering numérique. Les techniciens de support sont formés à résoudre les problèmes rapidement et avec courtoisie — deux objectifs qui entrent en conflit direct avec la sécurité lorsqu'un attaquant appelle en se faisant passer pour un employé bloqué.

Le scénario classique est le reset de credentials. L'attaquant appelle le helpdesk en se faisant passer pour un employé dont il a collecté les informations par OSINT (nom, poste, manager, identifiant employé si disponible) et demande un reset de mot de passe ou un reset de MFA. Si les procédures de vérification d'identité du helpdesk sont faibles (questions auxquelles les réponses sont trouvables en OSINT — date de naissance, nom du manager, identifiant employé), l'attaquant obtient un accès légitime au compte de l'employé.

Le rapport Unit 42 2025 documente plusieurs cas graves. Dans un cas, un attaquant a contacté le helpdesk à plusieurs reprises, chaque appel affinant le pretexte avec les informations glanées lors des appels précédents. Après avoir passé les vérifications d'identité, il a obtenu un reset MFA qui lui a donné accès aux systèmes internes. L'ensemble des actions post-compromission mimait un comportement utilisateur légitime, évitant de déclencher les alertes EDR.

**Défense P0** : les procédures de helpdesk pour les resets de credentials doivent inclure des vérifications que l'attaquant ne peut pas contourner par OSINT. Exemples : callback sur le numéro de téléphone enregistré dans l'annuaire (pas celui fourni par l'appelant), vérification en personne pour les comptes à privilèges, validation par le manager direct, utilisation de codes de vérification préétablis.

### 10.2 Le détournement de MFA

Le MFA (Multi-Factor Authentication) est une défense essentielle, mais il n'est pas infaillible face au social engineering.

**Le phishing en temps réel (reverse proxy).** Des outils comme Evilginx2, Modlishka et Muraena permettent de créer des proxies qui s'interposent entre la cible et le service légitime (Microsoft 365, Google Workspace). La cible saisit ses identifiants et son code MFA sur ce qui semble être la page de connexion légitime — mais le proxy capture le token de session authentifié. L'attaquant peut alors utiliser ce token pour accéder au compte sans avoir besoin de re-passer le MFA. Cette technique contourne toutes les formes de MFA basées sur des codes (OTP, push notification) — seul le MFA résistant au phishing (FIDO2/WebAuthn, qui vérifie l'origine du domaine) est immunisé.

**La push fatigue (MFA bombing).** L'attaquant, qui possède déjà les identifiants de la cible (obtenus par phishing, credential stuffing ou achat sur le darkweb), déclenche des demandes de validation MFA push en série. Submergé par les notifications, l'employé finit par approuver une demande — soit par lassitude, soit par erreur, soit pour « faire cesser les notifications ». Certains systèmes modernes (Microsoft Authenticator, Duo) ont implémenté des contre-mesures : number matching (l'utilisateur doit saisir un code affiché à l'écran, pas simplement approuver) et limitation du nombre de notifications.

**Le device code phishing.** Cette technique exploite le flux d'authentification « device code flow » de OAuth2, conçu pour les appareils sans navigateur (TV connectées, IoT). L'attaquant génère un code de device et envoie un lien à la cible (par phishing, vishing ou messagerie) en lui demandant de s'authentifier avec ce code. La cible se connecte sur une page Microsoft ou Google légitime et saisit le code — l'attaquant obtient un token d'accès. Cette technique est particulièrement insidieuse parce que la page d'authentification est 100 % légitime.

### 10.3 Exploitation des processus d'onboarding et d'offboarding

Les processus d'arrivée (onboarding) et de départ (offboarding) sont des fenêtres de vulnérabilité structurelles.

En phase d'onboarding, un attaquant peut se présenter comme un nouvel employé ou un nouveau prestataire pour obtenir des identifiants, un badge d'accès ou un poste de travail. Si le processus d'onboarding ne comporte pas de vérification robuste de l'identité (photo sur le contrat, validation par le manager, vérification d'identité officielle), l'usurpation est possible. Les cas de DPRK IT workers (travailleurs nord-coréens utilisant des identités fictives pour se faire embaucher comme freelances dans des entreprises technologiques) illustrent cette menace à un niveau de sophistication extrême.

En phase d'offboarding, les comptes non désactivés, les accès VPN non révoqués, les sessions OAuth non terminées constituent des portes d'entrée pour un attaquant qui a obtenu les identifiants d'un ancien employé (par social engineering de l'ancien employé lui-même, ou par achat de credentials).

### 10.4 La compromission de la supply chain humaine

La supply chain humaine — l'ensemble des prestataires, fournisseurs et sous-traitants qui ont un accès physique ou logique aux systèmes de l'organisation — est une surface d'attaque souvent négligée.

Le nettoyage de nuit a accès à tous les bureaux. La maintenance informatique a accès aux locaux serveurs. Le traiteur a accès à la cuisine et souvent aux couloirs. Le prestataire de reprographie a accès à des documents confidentiels. Cibler ces prestataires (par social engineering direct ou par compromission de leurs systèmes) permet un accès indirect à l'organisation cible avec un niveau de contrôle souvent inférieur à celui appliqué aux employés internes.

### 10.5 Red team scenarios et résultats typiques

Les résultats des tests de social engineering numérique sont systématiquement supérieurs aux attentes des commanditaires. Les taux de clic sur les campagnes de spear-phishing bien construites se situent typiquement entre 15 % et 40 %. Les taux de soumission d'identifiants (credential harvesting) entre 8 % et 25 %. Les tentatives de reset de credentials via le helpdesk réussissent dans 30 % à 60 % des cas si les procédures ne sont pas renforcées. Ces chiffres ne reflètent pas l'incompétence des employés — ils reflètent la qualité de la personnalisation et la puissance des leviers psychologiques exploités.

---

## Chapitre 11 — Capstone Partie II : campagne de social engineering numérique complète

**Exercice intégrateur.** L'étudiant doit planifier et documenter une campagne de social engineering numérique multi-vecteurs contre une organisation fictive (entreprise de services financiers, 500 employés, 2 sites).

**Livrables attendus :**
1. Dossier de reconnaissance OSINT (sources exploitées, informations collectées, organigramme reconstitué, terminologie interne identifiée)
2. Construction de 3 pretextes (1 phishing, 1 vishing, 1 smishing) avec justification du choix de chaque pretexte et analyse des leviers psychologiques exploités
3. Infrastructure technique (domaines, landing pages, caller ID — description, pas déploiement)
4. Scénario d'exécution (chronologie, séquence multi-canal, points de décision)
5. Estimation des résultats attendus (taux de clic, taux de compromission) avec justification
6. Rapport type red team (résultats, impact potentiel si exploitation réelle, recommandations P0/P1/P2)

**Erreur fréquente** : produire un plan trop ambitieux (trop de vecteurs, trop de cibles) sans profondeur sur chaque composante. Un bon plan de campagne est focalisé et réaliste, pas exhaustif.


---
