---
title: PARTIE VII — MAISON CONNECTÉE, FAMILLE ET FRONTIÈRE PRO/PERSO
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 8
chapters: 9
---

*L'environnement domestique et l'entourage forment un périmètre que vous ne contrôlez qu'en partie. Cette partie couvre la maison connectée, la famille, et la zone grise entre vie professionnelle et vie personnelle — y compris le cas particulier mais sérieux de la surveillance par un proche.*

---

<a id="chapitre-35"></a>
## Chapitre 35 — Cloud personnel et partage familial

Les risques du cloud personnel : la **synchronisation automatique** (iCloud, Google Photos, OneDrive — les photos prises sont automatiquement uploadées dans le cloud, y compris les captures d'écran de conversations privées, les photos de documents sensibles, et les photos accidentelles → vérifier régulièrement ce qui est synchronisé et supprimer ce qui ne devrait pas être dans le cloud). Les **liens de partage** (un lien Google Drive « toute personne ayant le lien » n'a aucun contrôle d'accès — si le lien est forwardé, intercepté, ou indexé par un moteur de recherche, le contenu est accessible à tous → pour les documents sensibles : partage nominatif avec authentification, durée limitée, et révocation possible).

La **corbeille** : les fichiers supprimés du cloud vont dans la corbeille pendant 30-60 jours. Ils sont récupérables — pratique en cas de suppression accidentelle, mais aussi accessibles à un attaquant qui a accès au compte. Les **photos « Récemment supprimées »** sur iOS/iCloud restent 30 jours dans un dossier dédié — accessible avec le compte. Pour une suppression réellement immédiate, vider également ce dossier après suppression.

Le **partage familial** : un compte partagé avec le conjoint ou les enfants (Apple Family, Google Family) signifie que les achats, les abonnements, la localisation, et parfois les photos sont visibles par tous les membres. Compartimenter ce qui doit l'être : si la localisation familiale est activée, savoir précisément qui voit quoi. Le partage familial n'est PAS adapté aux relations conflictuelles ou en transition (cf. Ch.38).

L'erreur classique : un Google Drive avec un dossier « Administratif » contenant CNI, passeport, bulletins de salaire, RIB, déclarations d'impôts — le tout accessible via un compte avec un mot de passe faible et sans MFA. Si le compte est compromis (et les comptes Google sont une cible fréquente de credential stuffing), c'est le kit complet d'usurpation d'identité. Le réflexe : ces documents ne doivent pas être stockés en clair dans le cloud principal — soit chiffrés (archive ZIP avec mot de passe fort, ou application de chiffrement type Cryptomator), soit dans un cloud séparé dédié uniquement à ces documents et avec MFA renforcé.

Les **partages anciens** : le lien partagé en 2021 pour un projet ponctuel est probablement encore actif en 2026. La majorité des comptes Google Drive / OneDrive contiennent des dizaines de partages oubliés. À réviser périodiquement — tous les 6 mois, lister les partages actifs et révoquer ce qui n'est plus pertinent.

> **🔵 Lina — Épisode 9 :** Lina partage un dossier Google Drive avec un ami pour un projet associatif. Le lien est en mode « toute personne ayant le lien ». Le dossier contient les documents du projet — mais aussi, dans un sous-dossier qu'elle a oublié, un scan de sa CNI et un RIB qu'elle avait stockés là « temporairement » il y a 6 mois. L'ami forward le lien par email à 5 autres personnes. Le scan de la CNI de Lina est maintenant accessible à des personnes qu'elle ne connaît pas. La leçon : un dossier partagé doit contenir UNIQUEMENT ce qu'on accepte de voir partagé. Les documents personnels n'y ont pas leur place, même temporairement.

---

<a id="chapitre-36"></a>
## Chapitre 36 — Maison connectée et objets du quotidien

### 36.1 La box Internet : la porte d'entrée du foyer

Changer le mot de passe Wi-Fi par défaut (le mot de passe imprimé sur l'étiquette sous la box est accessible à quiconque a eu un accès physique — technicien, voisin, visiteur, ancien locataire), activer le WPA3 si disponible (WPA2 minimum — ne JAMAIS utiliser WEP ou un réseau ouvert), désactiver le WPS (Wi-Fi Protected Setup — vulnérable au brute force), et mettre à jour le firmware de la box (les mises à jour sont souvent automatiques chez les FAI mais pas toujours).

L'**interface d'administration** de la box (généralement accessible via 192.168.1.1 ou freebox.fr / mafreebox.freebox.fr / livebox.fr) a son propre mot de passe, distinct du Wi-Fi. Beaucoup de gens ne l'ont jamais changé. Or, depuis cette interface, on peut modifier le DNS (rediriger tout le trafic du foyer vers des serveurs malveillants), ouvrir des ports vers Internet, et voir les appareils connectés. Mot de passe à changer dès l'installation.

### 36.2 Caméras, babyphones, sonnettes connectées

Si elles sont accessibles depuis Internet, elles doivent avoir un mot de passe fort et unique (PAS le mot de passe par défaut « admin/admin » ou « 123456 »), un firmware à jour, et idéalement un accès restreint (certaines caméras permettent de limiter l'accès à certaines IP ou à un VPN). Les caméras avec mot de passe par défaut sont indexées par des moteurs comme Shodan et accessibles à quiconque — des milliers de babyphones et caméras domestiques sont visibles publiquement.

Les **sonnettes connectées** (Ring, Nest Hello, etc.) enregistrent en continu et stockent dans le cloud. Vérifier qui a accès au flux (le compte principal + les utilisateurs partagés), à la durée de conservation, et à la politique de partage avec les autorités du fournisseur.

### 36.3 Assistants vocaux

Alexa, Google Home, Siri : ils écoutent en permanence pour détecter le mot de déclenchement. Les enregistrements sont stockés dans le cloud du fournisseur. Vérifier les paramètres de confidentialité, supprimer l'historique régulièrement (Amazon : Paramètres Alexa > Confidentialité ; Google : myactivity.google.com), et désactiver le micro physiquement (bouton dédié sur la plupart des appareils) quand l'assistant n'est pas utilisé. Ne pas placer un assistant vocal dans une chambre où sont tenues des conversations sensibles, ni à proximité d'un téléphone qui sonne en permanence.

### 36.4 NAS, imprimantes, et stockage familial

Le **NAS** (Network Attached Storage — Synology, QNAP, etc.) est un mini-serveur de stockage à la maison, souvent utilisé pour centraliser les photos et documents familiaux. Risques : interface d'administration exposée à Internet (si elle l'est, c'est une cible majeure — le NAS doit n'être accessible que depuis le réseau local, ou via un VPN), mot de passe admin par défaut, firmware non mis à jour. Les ransomwares ciblant les NAS particuliers existent (ex. famille Qlocker sur QNAP en 2021) — un NAS compromis = toutes les photos et documents familiaux chiffrés.

L'**imprimante connectée** : elle a souvent une interface d'administration accessible sur le réseau local et parfois exposée à Internet. Mot de passe à changer. La mémoire interne de certaines imprimantes conserve des copies des documents imprimés, scannés, ou faxés — point d'attention en cas de revente de l'imprimante (cf. Ch.43).

Les **clés USB familiales** qui circulent (la clé USB du grand-père, partagée pour transférer des photos, branchée sur l'ordinateur de chacun) sont un vecteur classique de propagation de malwares. Si un appareil de la famille est infecté, la clé qui passe partout propage. Réflexe : ne pas brancher de clé USB inconnue, et idéalement n'avoir qu'une clé dédiée par usage (sauvegarde, transfert, etc.).

### 36.5 La segmentation simple

Mettre les objets connectés sur un réseau Wi-Fi séparé. La plupart des box récentes permettent de créer un réseau invité — les objets connectés (caméras, TV, assistants, imprimantes, NAS exposé en lecture) vont sur le réseau invité, les ordinateurs et téléphones sur le réseau principal. Si un objet connecté est compromis (vulnérabilité du firmware, mot de passe par défaut), il n'a pas accès aux appareils principaux. C'est le geste qui réduit le plus le risque domestique pour un coût d'effort minime.

---

<a id="chapitre-37"></a>
## Chapitre 37 — Enfants, famille et entourage numérique

### 37.1 Tablettes et téléphones d'enfants

Sans contrôle parental, un enfant a accès à tout Internet. Les faux jeux (applications qui imitent des jeux populaires mais contiennent des malwares ou des publicités agressives), les achats intégrés (un enfant qui clique sur « acheter 1 000 pièces d'or pour 9,99 € » dans un jeu — les factures peuvent atteindre des centaines d'euros), et les publicités ciblées dans les apps gratuites. Les réglages : contrôle parental activé (Screen Time sur iOS, Family Link sur Android), restrictions d'achat (validation parentale obligatoire pour tout achat), et sélection des applications installées.

### 37.2 Grooming et prédation en ligne

Un adulte malveillant établit une relation de confiance avec un enfant en ligne — via les chats intégrés aux jeux (Fortnite, Roblox, Minecraft), les réseaux sociaux (TikTok, Snapchat, Instagram), ou les messageries. Le risque est réel et documenté. Les signaux : l'enfant devient secret sur son utilisation du téléphone/tablette, parle d'un « nouvel ami en ligne », reçoit des cadeaux (codes de jeux, cartes cadeaux), ou modifie brusquement ses habitudes. Le réflexe : dialogue ouvert (pas surveillance invasive — un enfant surveillé en permanence apprend à contourner et perd confiance), espace de jeu dans les pièces communes (pas d'écran dans la chambre pour les jeunes enfants), et vérification régulière des contacts et des applications.

### 37.3 Sextorsion adolescente

Cas particulier mais en forte hausse : un adolescent reçoit un message d'un faux profil (souvent féminin séduisant si la cible est masculine, ou inverse), engage une conversation, partage une photo intime → l'attaquant menace immédiatement de la diffuser à la famille et aux amis si une rançon n'est pas payée. La pression psychologique sur un mineur est extrême. Le réflexe : l'adolescent doit savoir que ce scénario existe ET que la réponse n'est PAS de payer (les attaquants demandent toujours plus une fois qu'on a payé) MAIS de tout arrêter, ne pas répondre, conserver les preuves, et en parler à un adulte. Plateforme nationale : **3018** (ligne d'écoute pour mineurs et jeunes adultes victimes de violences numériques — gratuit, anonyme, 7j/7 de 9h à 23h), Pharos pour le signalement, plainte au commissariat. La honte est l'arme principale de l'attaquant — la rompre par le dialogue est ce qui désamorce.

### 37.4 Sharenting

Les parents qui publient les photos de leurs enfants sur les réseaux sociaux (nom, école, activités, localisation, visage) — créant une empreinte numérique de l'enfant avant même qu'il soit en âge de consentir. Les risques : les photos sont exploitables par des prédateurs (localisation de l'école, habitudes), les photos sont récupérables par des services de reconnaissance faciale, et l'enfant pourra reprocher cette exposition à l'âge adulte. Le cadre légal en France : la loi du 19 février 2024 reconnaît le droit à l'image de l'enfant comme un attribut de l'autorité parentale conjointe — un parent qui publie sans accord de l'autre peut être contesté.

### 37.5 Aider les proches âgés

Les arnaques au faux conseiller bancaire, au faux support, et au faux colis ciblent particulièrement les personnes âgées. Le réflexe d'aide : configurer le téléphone d'un parent âgé avec les bons réglages (notifications visibles, contacts de confiance bien identifiés), expliquer une règle simple et reproductible (« si quelqu'un demande un code par téléphone, raccrocher et m'appeler »), être identifié comme contact de récupération sur les comptes critiques (avec son accord), et vérifier régulièrement les opérations bancaires inhabituelles. L'objectif n'est pas de surveiller — c'est d'avoir un filet quand le doute apparaît.

### 37.6 Mauvaises pratiques héritées

Un parent qui n'utilise pas de gestionnaire de mots de passe transmet cette habitude. Un grand-parent qui clique sur chaque lien reçu par SMS est un relais d'arnaques involontaire. L'entourage qui partage des informations ou des photos sans vérifier est une extension de la surface d'attaque. Le cours peut se transmettre — pas comme une leçon, mais comme une conversation lors d'un repas de famille : « tu sais, tu peux installer un truc qui retient tes mots de passe pour toi, je t'aide ? ».

---

<a id="chapitre-38"></a>
## Chapitre 38 — Stalkerware et surveillance par un proche

*Ce chapitre traite un sujet sensible et en croissance : la surveillance numérique exercée par un proche — actuel ou ex-partenaire, parent contrôlant, employeur abusif. Les outils existent, sont accessibles, et la victime ne sait souvent pas qu'elle est suivie. Si vous lisez ce chapitre dans le contexte d'une relation conjugale violente, des ressources spécialisées sont en bas de chapitre — n'agissez pas seule.*

### 38.1 Le contexte

La surveillance numérique d'un proche est différente d'une attaque externe. L'attaquant a un accès physique régulier au téléphone ou à l'ordinateur, connaît les mots de passe ou peut les voir être tapés, partage des comptes (Apple Family, Google Family, Netflix, etc.), et a une connaissance intime de la victime qui rend l'ingénierie sociale très efficace. Le contexte typique : ex-conjoint contrôlant ou violent, séparation conflictuelle, parent intrusif d'un jeune adulte, employeur dépassant le cadre légal de la surveillance. L'objectif de l'attaquant peut être le contrôle, la jalousie, le harcèlement, la collecte d'éléments pour une procédure (divorce, garde d'enfants), ou la coercition.

### 38.2 Les vecteurs concrets

**AirTags et trackers Bluetooth malveillants** : un AirTag glissé dans un sac, une voiture, une poche de manteau permet de suivre les déplacements de la victime. iOS et Android détectent les trackers inconnus qui voyagent avec vous et affichent une alerte (« un AirTag inconnu se déplace avec vous » sur iPhone, équivalent sur Android via l'app Tracker Detect ou les notifications natives Android 14+). Prendre ces alertes très au sérieux. Une alerte qui revient régulièrement n'est pas un faux positif.

**Partage de localisation** : Localiser/Find My, Google Maps « partage de position », Snap Map, partages familiaux. Vérifier qui a accès à votre localisation en permanence. Désactiver les partages anciens. Le partage Find My peut avoir été activé sans que vous le sachiez si quelqu'un a eu votre téléphone déverrouillé quelques minutes.

**Stalkerware** : applications de surveillance installées sur le téléphone de la victime, souvent vendues comme « contrôle parental » ou « contrôle conjugal » mais utilisées comme outils de surveillance. Elles transmettent SMS, appels, photos, localisation, frappes au clavier vers un compte distant. Sur Android, l'installation nécessite généralement un accès physique au téléphone et peut nécessiter de désactiver Play Protect. Sur iOS, c'est plus rare mais existe via la prise en main du compte iCloud (toutes les sauvegardes, photos, messages, localisation deviennent accessibles à qui contrôle le compte iCloud, sans application installée). Signaux possibles : batterie qui se vide anormalement vite, données mobiles consommées rapidement sans raison, téléphone qui chauffe au repos, applications inconnues, ou comportements suspects (le partenaire « sait » des choses qu'il ne devrait pas savoir).

**Comptes partagés** : iCloud familial avec accès aux photos, Apple ID partagé entre partenaires, comptes Google liés, gestionnaire de mots de passe partagé. Tout ce qui est partagé avec une personne dont la confiance est rompue devient un canal de surveillance.

**Caméras et micros de la maison** : les caméras de surveillance domestique installées « pour la sécurité » peuvent être réorientées vers l'intérieur, les babyphones peuvent être utilisés comme micros, les assistants vocaux peuvent enregistrer et l'historique peut être consulté par qui a accès au compte du foyer.

**Accès physique** : le partenaire connaît le code de déverrouillage (vu, deviné, partagé volontairement à un moment de confiance), accède au téléphone la nuit, lit les messages, installe ce qu'il veut.

### 38.3 Le diagnostic : signes d'une surveillance possible

- Le partenaire connaît votre localisation, vos messages, ou vos contenus sans que vous les ayez partagés.
- Le téléphone a un comportement inhabituel : batterie qui se vide vite, chauffe sans raison, notifications étranges, applications inconnues.
- Vous recevez des alertes de tracker inconnu.
- Vos comptes ont des sessions actives sur des appareils que vous ne reconnaissez pas.
- Vous découvrez un partage de localisation que vous n'avez pas activé.
- Vous remarquez un nouveau profil dans les paramètres MDM (Mobile Device Management) du téléphone.

Aucun de ces signes pris isolément ne prouve une surveillance — leur accumulation est ce qui doit alerter.

### 38.4 Que faire — avec précaution

**Le piège** : si vous êtes dans une situation de violence conjugale, la suppression brutale d'un stalkerware peut alerter l'agresseur et déclencher une escalade. Si la situation est dangereuse, ne pas agir seule — contacter le **3919** (violences conjugales, gratuit, anonyme, 24/7) pour être écoutée et orientée, une association spécialisée (Solidarité Femmes, France Victimes), ou un commissariat. **En cas de danger immédiat, le 3919 n'est pas un numéro d'urgence : appeler le 17 (police) ou le 112.** Des protocoles existent pour sécuriser numériquement une victime sans alerter l'agresseur.

**Si la situation n'est pas dangereuse mais que vous voulez reprendre le contrôle** :

1. Vérifier les **partages de localisation** actifs (iCloud > Localiser > Personnes ; Google Maps > Partage de position) et révoquer ceux qui ne devraient pas exister.
2. Vérifier les **sessions actives** sur les comptes principaux (Apple ID, Google, Facebook, Instagram, WhatsApp Web/Desktop) et déconnecter tout ce qui n'est pas à vous.
3. Vérifier les **profils MDM** sur iOS (Réglages > Général > VPN et gestion d'appareils) et Android (Paramètres > Sécurité > Applis d'administration de l'appareil) — supprimer ce qui n'a rien à faire là.
4. Vérifier les **applications installées** et désinstaller celles qui sont inconnues.
5. Changer **tous** les mots de passe critiques (email, banque, cloud, gestionnaire) depuis un appareil dont vous êtes sûre, et activer/changer le MFA.
6. Faire le **tour des trackers Bluetooth** dans le sac, les vêtements, le véhicule (utiliser l'app Tracker Detect d'Apple sur Android, ou la fonctionnalité native iOS qui scanne les trackers à proximité).
7. Sortir des **partages familiaux** (Apple Family, Google Family) si la relation est rompue — le faire au bon moment et dans le bon ordre.

Pour un nettoyage plus profond (ré-initialisation du téléphone, changement de SIM, nouveau compte) : se faire accompagner. La précipitation peut détruire des preuves utiles à une procédure judiciaire.

### 38.5 Reconstruction numérique après séparation

Une séparation est aussi une séparation numérique. Liste à parcourir : changer tous les mots de passe (email, banque, cloud, réseaux sociaux, streaming), retirer l'ex-partenaire du partage familial, retirer les accès aux comptes communs, vérifier les bénéficiaires sur les comptes bancaires et assurance-vie, réviser les sauvegardes automatiques (iCloud commun → désynchroniser), supprimer les appareils en commun des comptes personnels, et faire le tour des partages cloud (Drive, Dropbox, OneDrive). Cette liste prend du temps — la traiter méthodiquement, idéalement avec l'aide d'une personne de confiance.

### 38.6 Ressources

- **3919** — Violences Femmes Info, gratuit, anonyme, 24/7. Numéro d'écoute et d'orientation. **En cas de danger immédiat, appeler le 17 ou le 112.**
- **3018** — violences numériques pour mineurs et jeunes adultes, gratuit, anonyme, 7j/7 de 9h à 23h.
- **France Victimes** (116 006) — assistance aux victimes, écoute, orientation juridique.
- **Cybermalveillance.gouv.fr** — fiche dédiée au cyberharcèlement et à la surveillance par un proche.
- Coalition Against Stalkerware — ressources internationales.

---

<a id="chapitre-39"></a>
## Chapitre 39 — Frontière pro/perso : les risques de la porosité

Le **téléphone perso avec usages pro** (BYOD) : les emails pro sur le téléphone perso = si le téléphone perso est compromis (malware, vol, perte), les données pro le sont aussi. Le **cloud perso pour les documents pro** : envoyer un fichier pro sur Google Drive perso pour « travailler ce weekend » → le document pro est maintenant dans un cloud personnel potentiellement moins sécurisé que le cloud d'entreprise, sans les contrôles de sécurité de l'entreprise (DLP, audit, chiffrement). Les **messageries non prévues** : discuter d'un projet client sur WhatsApp perso, envoyer un devis par iMessage, partager un fichier via un lien Dropbox personnel → les données pro circulent sur des canaux non maîtrisés par l'entreprise, non archivés, non auditables. L'**impression à domicile** : imprimer un document confidentiel chez soi → le document est dans la corbeille à papier, dans la mémoire de l'imprimante, et potentiellement visible par les membres du foyer.

Le **risque dans les deux sens** : le perso contamine le pro (malware sur le téléphone perso → accès aux emails pro) et le pro contamine le perso (l'entreprise a un droit de regard sur le téléphone BYOD en cas d'incident → les données personnelles sont potentiellement accessibles dans le cadre d'une investigation). Le cas des **outils IA** est devenu central : coller un document client dans ChatGPT pour le résumer = exfiltrer ce document hors du périmètre de l'entreprise (cf. Ch.27).

Le réflexe : séparer les mots de passe (ne JAMAIS réutiliser un mot de passe entre un compte pro et un compte perso), ne pas synchroniser les comptes pro et perso sur le même appareil sans mesures de protection (conteneurisation, profil séparé), connaître la politique de l'entreprise (certaines entreprises ont des outils de MDM — Mobile Device Management — qui donnent un accès à distance au téléphone BYOD), et ne pas confondre « plus pratique » avec « autorisé ». Si l'entreprise n'a pas mis en place le bon outil pour un usage légitime, c'est un sujet à remonter à la DSI, pas à contourner par un outil personnel.

---

<a id="chapitre-40"></a>
## Chapitre 40 — Quand l'attaque personnelle devient un problème d'entreprise

Un **compte perso compromis** avec le même mot de passe que le VPN d'entreprise → l'attaquant accède au réseau de l'entreprise. C'est l'un des scénarios d'intrusion les plus courants documentés dans les rapports d'incidents. Une **usurpation d'identité** sur LinkedIn → le faux profil contacte des collègues et des clients pour du social engineering (« bonjour, je suis X, nouveau chez Y, est-ce que tu peux m'envoyer le fichier Z ? »). Un **SMS de phishing** sur le téléphone perso → le malware accède aux emails pro synchronisés sur le même appareil. Un salarié **ciblé via sa vie personnelle** (réseaux sociaux, habitudes, centres d'intérêt — les informations publiées sur Instagram ou Facebook sont utilisées pour crédibiliser un email de spear phishing professionnel : « Bonjour, j'ai vu sur LinkedIn que vous étiez au salon X la semaine dernière... »).

Le cas du **deepfake vocal du dirigeant** : l'attaquant clone la voix du PDG à partir de ses interventions publiques (interviews, podcasts, conférences sur YouTube) et appelle un comptable pour autoriser un virement « urgent et confidentiel ». La fraude au président par deepfake a fait des victimes pour des montants de plusieurs millions d'euros en 2024-2025. La défense : procédure de validation hors canal sur les virements (jamais valider un virement urgent sur un seul appel, toujours rappeler sur le numéro connu), et formation des collaborateurs en contact avec les flux financiers.

Les bons réflexes côté salarié : séparer les mots de passe pro/perso (le gestionnaire gère les deux mais avec des mots de passe différents pour chaque compte), signaler immédiatement à l'employeur tout incident personnel qui pourrait avoir un impact pro (compte compromis, malware, phishing réussi), connaître la procédure de signalement de l'entreprise (un signalement rapide peut limiter les dégâts — un signalement tardif laisse l'attaquant pivoter vers l'entreprise), et ne pas avoir honte de signaler un phishing dans lequel on est tombé (la honte fait taire — le silence est l'allié de l'attaquant).

---

> ### 🟦 Réflexes — Fin de Partie VII
>
> **À configurer** :
> - Box Internet : mot de passe Wi-Fi unique, WPA2/WPA3, WPS désactivé, mot de passe admin changé
> - Réseau invité activé pour les objets connectés (caméras, TV, NAS, imprimantes)
> - Caméras et babyphones avec mot de passe fort (pas le défaut), firmware à jour
> - Contrôle parental sur les appareils d'enfants
> - Mots de passe pro et perso strictement séparés dans le gestionnaire
>
> **À éviter** :
> - Mot de passe Wi-Fi par défaut imprimé sur la box
> - Documents pro dans Google Drive / WhatsApp perso
> - Documents d'identité stockés en clair dans le cloud familial
> - Partage familial actif avec un proche dont la confiance est rompue
> - Utiliser un même mot de passe entre une plateforme perso et le VPN d'entreprise
>
> **À vérifier** :
> - Partages de localisation actifs (Find My, Google Maps, Snap Map)
> - Sessions actives sur les comptes principaux
> - Trackers Bluetooth inconnus signalés par le téléphone
> - Profils MDM ou apps d'administration sur le téléphone
> - Liste des appareils connectés à la box (interface admin)
>
> **Si quelque chose arrive** :
> - Soupçon de surveillance par un proche → ne pas agir seule, contacter 3919 / France Victimes / Cybermalveillance
> - Sextorsion adolescent → 3018, conserver les preuves, pas de paiement, plainte
> - Compte perso compromis avec MdP réutilisé sur un compte pro → signaler à l'employeur immédiatement
> - Alerte de tracker inconnu répétée → ne pas ignorer, vérifier sac/véhicule

---
