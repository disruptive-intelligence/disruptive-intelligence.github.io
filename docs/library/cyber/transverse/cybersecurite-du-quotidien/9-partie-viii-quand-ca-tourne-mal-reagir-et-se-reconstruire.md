---
title: 'PARTIE VIII — QUAND ÇA TOURNE MAL : RÉAGIR ET SE RECONSTRUIRE'
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 9
chapters: 9
---

*Les réflexes ne suffisent pas toujours. Cette partie couvre la réaction quand un incident se produit — vite, méthodiquement, sans panique — et la préparation d'un plan personnel qui inclut aussi la transmission numérique.*

---

<a id="chapitre-41"></a>
### Chapitre 41 — Réagir à une compromission de compte

L'ordre des actions : (1) **changer immédiatement le mot de passe** du compte compromis (si l'accès est encore possible — si l'attaquant a changé le mot de passe, utiliser la procédure de récupération), (2) **changer le mot de passe de l'email maître** (si le même mot de passe était utilisé — si le compte compromis et l'email ont le même mot de passe, l'email est potentiellement compromis aussi, et l'email contrôle la réinitialisation de tous les autres comptes), (3) **activer le MFA** sur le compte compromis et sur l'email maître (si ce n'est pas déjà fait), (4) **révoquer toutes les sessions actives** (la plupart des services permettent de « déconnecter tous les appareils » dans les paramètres de sécurité — l'attaquant qui a volé un cookie de session perd l'accès), (5) **vérifier les paramètres du compte** (l'attaquant peut avoir ajouté une adresse email de récupération, un numéro de téléphone, ou une règle de transfert automatique d'email → les supprimer ; vérifier aussi les filtres email qui pourraient masquer les notifications de sécurité de l'attaquant), (6) **changer le mot de passe sur tous les comptes qui utilisaient le même mot de passe**, (7) **documenter** ce qui s'est passé (captures d'écran, emails reçus, dates, actions effectuées — pour la plainte ou le signalement), et (8) **informer les contacts** si le compte a pu être utilisé pour les contacter (faux messages envoyés au nom de la victime).

Le cas particulier de l'**email maître compromis** : c'est le pire scénario parce que l'email contrôle la réinitialisation de mot de passe de tous les autres comptes. Si l'attaquant a accès à votre Gmail, il peut demander la réinitialisation de votre banque, de votre cloud, de vos réseaux sociaux. Reprendre l'email d'abord, puis tous les comptes liés. Si vous ne pouvez pas reprendre l'email (mot de passe et MFA changés par l'attaquant), passer immédiatement par la procédure de récupération du fournisseur — ces procédures existent et fonctionnent, mais peuvent prendre plusieurs jours.

Les erreurs à ne PAS faire : paniquer et tout changer en même temps sans ordre (→ risque de perdre l'accès à tout, et de se déconnecter du seul appareil qui a encore une session valide), supprimer le compte compromis (→ perte de l'historique et des données, et l'attaquant peut recréer le compte), ou ignorer l'incident en espérant qu'il n'y aura pas de conséquences (→ l'attaquant revient et exploite l'accès).

---

<a id="chapitre-42"></a>
### Chapitre 42 — Téléphone perdu, volé ou compromis

L'ordre de reprise : (1) **bloquer la carte SIM** (appeler l'opérateur — le numéro est sur le contrat ou le site de l'opérateur → noter ce numéro AVANT d'en avoir besoin et le stocker ailleurs que dans le téléphone), (2) **localiser et verrouiller/effacer** le téléphone à distance (Find My iPhone, Find My Device), (3) **changer le mot de passe de l'email maître** (depuis un autre appareil — l'ordinateur, le téléphone d'un proche), (4) **révoquer les sessions actives** sur les comptes critiques (banque, email, messageries), (5) **changer les mots de passe** des comptes sensibles, (6) **prévenir la banque** si l'app bancaire était sur le téléphone, (7) **prévenir l'employeur** si le téléphone avait des usages pro, (8) **déclarer la perte/le vol** au commissariat (récépissé utile pour les démarches d'opposition et d'assurance).

Le cas du **vol ciblé** : le voleur observe le code de déverrouillage (shoulder surfing dans le métro, dans la file d'attente, au café), puis vole le téléphone. Avec le code, il accède à tout — y compris aux apps bancaires, au gestionnaire de mots de passe (si celui-ci se déverrouille avec le code de l'iPhone), et à l'email. Il peut changer le mot de passe du compte Apple/Google et empêcher le propriétaire de localiser ou effacer le téléphone à distance. La prévention : utiliser un code long et non prévisible, privilégier Face ID/Touch ID en lieu public pour ne pas taper le code, et activer la **protection contre le vol** (iOS 17.3+ : Stolen Device Protection — les opérations critiques nécessitent la biométrie même quand le code est connu, avec un délai de sécurité d'une heure pour les changements de paramètres critiques quand on est dans un lieu non familier ; Android : Theft Detection Lock sur Android 15+ qui verrouille automatiquement le téléphone si un mouvement de vol est détecté).

Le cas du **téléphone compromis sans perte physique** (malware, stalkerware) : si le doute existe, la procédure est plus radicale → sauvegarder ce qui peut l'être (photos, contacts) sur un support externe, réinitialiser entièrement le téléphone (réglages d'usine), changer tous les mots de passe critiques depuis un autre appareil, et ne pas restaurer une sauvegarde du téléphone compromis (la sauvegarde peut contenir les éléments qui ont permis la compromission). Pour un cas suspecté de stalkerware, voir Ch.38.

> **🔵 Lina — Épisode 10 :** Lina, après l'épisode du Ch.10, a tout préparé. Son nouveau téléphone est volé lors d'un concert. En 15 minutes depuis le téléphone d'un ami : SIM bloquée, iPhone localisé et verrouillé via Find My, email maître vérifié et mot de passe changé, sessions révoquées sur les comptes critiques, banque prévenue. Impact : zéro. La préparation a transformé un désastre potentiel en simple désagrément logistique. La différence entre l'épisode 4 (téléphone perdu sans préparation : 3 jours, 2 abonnements frauduleux) et l'épisode 10 (téléphone volé avec préparation : 15 minutes, zéro dégât) tient entièrement à ce qui a été fait avant l'incident.

---

<a id="chapitre-43"></a>
### Chapitre 43 — Revente, don et réparation : effacer avant de céder

*Un appareil cédé sans précaution emporte des années de données personnelles. Ce chapitre traite la fin de vie numérique des appareils — un angle mort fréquent.*

#### 43.1 Pourquoi c'est sérieux

Un téléphone, un ordinateur, ou un disque dur revendu sur Leboncoin ou Vinted contient potentiellement : photos, conversations, emails, mots de passe enregistrés, sessions ouvertes vers des comptes bancaires, documents administratifs, contacts. Une réinitialisation rapide ne suffit pas toujours — surtout sur des PC anciens où un « formatage simple » laisse les données récupérables avec des outils gratuits. Plusieurs études ont montré que les disques achetés d'occasion contiennent encore des données personnelles dans 40 à 60 % des cas.

#### 43.2 Téléphone : la procédure correcte

**iPhone** : (1) sauvegarder ce qu'on veut conserver (iCloud ou ordinateur), (2) se déconnecter de l'iCloud — Réglages > [votre nom] > Déconnexion (cette étape désactive Find My et le verrouillage d'activation, sans quoi le nouvel utilisateur ne pourra rien faire de l'appareil), (3) Réglages > Général > Transférer ou réinitialiser l'iPhone > Effacer contenu et réglages, (4) retirer la SIM physique et désactiver l'eSIM si présente.

**Android** : (1) sauvegarder, (2) chiffrer le téléphone si ce n'est pas déjà fait (le chiffrement préalable garantit que les données résiduelles sont illisibles après réinitialisation), (3) déconnecter le compte Google — Paramètres > Comptes > Google > Supprimer le compte (essentiel pour désactiver le verrouillage d'activation FRP — Factory Reset Protection), (4) Paramètres > Système > Réinitialisation > Effacer toutes les données, (5) retirer SIM et eSIM.

#### 43.3 Ordinateur : la procédure correcte

**Windows** : la réinitialisation native de Windows (Paramètres > Système > Récupération > Réinitialiser ce PC) propose une option « Supprimer mes fichiers et nettoyer le lecteur » — choisir cette option, qui écrase les données après suppression et rend la récupération beaucoup plus difficile. Pour un appareil avec données très sensibles : un effacement sécurisé (outil DBAN, ou commande `cipher /w:` sur la partition concernée) est plus rigoureux.

**macOS** : Préférences/Réglages > Effaçeur des contenus et réglages (sur les Mac Apple Silicon et T2 — l'opération est rapide et sécurisée car les données sont chiffrées par défaut, et l'effacement détruit la clé de chiffrement, rendant les données irrécupérables). Sur les Mac Intel sans T2 : Utilitaire de disque depuis le mode récupération + réinstallation de macOS.

**Disques durs externes et SSD** : un disque dur classique (HDD) doit être écrasé en plusieurs passes (DBAN, ou outil natif). Un SSD doit être effacé avec la commande secure erase (souvent disponible dans le BIOS ou via un outil constructeur — Samsung Magician, Crucial Storage Executive, etc.). En cas de doute, ou pour un disque très ancien : la destruction physique (perceuse, marteau sur les plateaux pour un HDD) reste la solution la plus sûre.

#### 43.4 Le cas du SAV et de la réparation

Confier un téléphone, un ordinateur, ou un disque pour réparation = donner accès aux données. Avant de l'envoyer : sauvegarder, et idéalement réinitialiser si le SAV n'a pas besoin d'accéder aux données pour diagnostiquer (souvent le cas pour les pannes physiques — écran, batterie, port). Si le SAV demande le mot de passe pour faire des tests : changer ce mot de passe pour un mot de passe temporaire, et le re-changer au retour. Au retour de SAV : vérifier que rien n'a été ajouté (apps installées, profils MDM, comptes liés), changer le mot de passe principal, et idéalement faire une nouvelle réinitialisation si on a des doutes.

#### 43.5 Cartes SD, clés USB, NAS

**Cartes SD et clés USB** : un formatage rapide n'efface pas les données. Utiliser un outil d'effacement sécurisé (Eraser sur Windows, sdelete, ou la commande `dd if=/dev/zero` sur Linux/macOS) avant de les céder ou de les jeter.

**NAS, anciens disques internes d'ordinateurs** : les retirer physiquement avant de céder un PC (ou les effacer rigoureusement comme indiqué plus haut). Une vente d'occasion d'un ordinateur avec disque non effacé est l'un des cas les plus fréquents de fuite de données personnelles.

**Imprimantes connectées et photocopieurs** : la mémoire interne peut contenir des copies des documents imprimés/scannés. Vérifier dans le manuel s'il existe une procédure de réinitialisation de la mémoire interne avant la cession.

---

<a id="chapitre-44"></a>
### Chapitre 44 — Signaler, documenter, se faire assister

Ce qu'il faut **documenter** (pour la plainte et les démarches) : captures d'écran des messages frauduleux (avec l'URL visible, le numéro de l'expéditeur, la date et l'heure), les IBAN vers lesquels des virements ont été faits, les numéros de téléphone des appels frauduleux, les échanges avec la banque (dates, noms des interlocuteurs, références de dossier), les logs bancaires (la banque peut fournir l'historique des opérations), et les emails/SMS reçus. Conserver les originaux numériques (ne pas se contenter de captures — l'email original contient des en-têtes techniques qui peuvent aider à l'enquête).

Où **signaler** : la **banque** (opposition immédiate sur la carte ou le virement, contestation des opérations frauduleuses — la loi protège le consommateur pour les opérations non autorisées : article L133-18 du Code monétaire et financier), la **plainte** (selon le type d'infraction, **THESEE** permet un dépôt de plainte en ligne pour les e-escroqueries et certaines usurpations en ligne — pour les particuliers majeurs ; pour les autres situations, ou si THESEE ne couvre pas le cas, se rendre en commissariat ou en gendarmerie, ou utiliser la pré-plainte en ligne), le **signalement** (**Pharos** pour les contenus illicites en ligne, **Signal Spam** pour le phishing email, **33700** pour le smishing SMS), **17Cyber** (guichet d'assistance en ligne lancé fin 2024, disponible 24h/24 et 7j/7, qui oriente les victimes selon leur situation), **Cybermalveillance.gouv.fr** (plateforme nationale d'assistance — fiches pratiques, prestataires labellisés, accompagnement), et l'**employeur** (si l'incident a un impact professionnel — le signalement rapide peut limiter les dégâts).

Le délai compte : pour une **fraude bancaire**, la contestation doit être faite dans les 13 mois suivant l'opération (70 jours pour les opérations hors EEE). Pour une **usurpation d'identité**, plus la plainte est déposée tôt, plus les chances de limiter les dégâts sont élevées. Le numéro **Info Escroqueries** (0 805 805 817 — gratuit) fournit des conseils et oriente les victimes.

La **négligence grave** est la notion juridique qui peut bloquer un remboursement bancaire. La banque peut refuser le remboursement si elle prouve que la victime a été gravement négligente (avoir donné soi-même un code SMS à un faux conseiller, par exemple). La jurisprudence évolue — plusieurs décisions récentes ont reconnu que face à une arnaque sophistiquée (numéro spoofé, conseiller qui connaît des informations personnelles), la victime n'est pas en négligence grave. En cas de refus de remboursement, ne pas s'arrêter à la première réponse — saisir le médiateur bancaire de l'établissement, puis si nécessaire la justice. Des associations (UFC-Que Choisir, CLCV) accompagnent les victimes.

#### 44.bis — La seconde arnaque : recovery scam après une première fraude

Une fois victime d'une arnaque, vous devenez une cible plus probable, pas moins. Les coordonnées des victimes sont revendues entre arnaqueurs, et de nouveaux groupes recontactent en se présentant comme « cabinet de récupération de fonds », « avocat spécialisé en cybercrime », « enquêteur privé », ou même « policier en charge de votre dossier ». Le scénario : on vous promet de récupérer l'argent perdu, en échange d'un acompte, de « frais de procédure », de « taxes de déblocage », ou d'une « commission au succès payable d'avance ». L'arnaque à la récupération est désormais aussi fréquente que l'arnaque initiale qui l'a précédée.

Le réflexe absolu après une première fraude : **aucun cabinet sérieux ne demande de paiement préalable** pour récupérer des fonds. Les vraies procédures passent par votre banque, par la justice (plainte, juge des référés), et par votre assurance le cas échéant — et elles ne se rémunèrent pas avant résultat (ou alors sont gratuites pour la victime, comme les associations d'aide). Toute personne qui vous appelle après une arnaque pour vous proposer de l'aide payante est presque certainement un second arnaqueur. Ne pas reverser un euro. Signaler le second contact à 17Cyber et à la même plainte que la première arnaque (pour faire ajouter le second épisode).

Le **soutien psychologique** : être victime d'une arnaque, d'une usurpation, ou d'un harcèlement numérique génère honte, sentiment de stupidité, anxiété — alors même que l'arnaque a fonctionné précisément parce qu'elle était bien faite. France Victimes (116 006) propose un accompagnement psychologique gratuit. La parole et l'accompagnement sont aussi importants que les démarches techniques.

---

<a id="chapitre-45"></a>
### Chapitre 45 — Construire son plan personnel et préparer l'héritage numérique

*Le dernier chapitre transforme tout ce qui a été appris en un plan d'action concret et personnalisé — y compris la question rarement traitée mais essentielle de la transmission numérique.*

#### 45.1 L'inventaire personnel

L'**inventaire des comptes critiques** : les 5-10 comptes dont la compromission serait la plus grave — email maître, banque, gestionnaire de mots de passe, cloud principal, messagerie principale, et les fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste, France Identité). Ce sont ceux qui doivent avoir les mots de passe les plus forts et le MFA le plus robuste.

L'**inventaire des appareils** : téléphone principal, ordinateur, éventuel second appareil — chacun doit être verrouillé, chiffré, à jour, avec la localisation à distance activée.

Le **plan de sauvegarde** : quelles données, sur quels supports, à quelle fréquence → les photos sur iCloud/Google Photos + un disque externe tous les 3 mois, les codes de récupération MFA imprimés dans un lieu sûr, la sauvegarde du gestionnaire de mots de passe.

Le **plan de réaction** : que faire si le téléphone disparaît ? (bloquer SIM → localiser/effacer → email maître → sessions → banque), si un compte est compromis ? (mot de passe → email maître → MFA → sessions → paramètres → comptes liés), si un prélèvement frauduleux apparaît ? (opposition → plainte → contestation bancaire → documentation).

#### 45.2 Les 10 habitudes qui couvrent 80 % du risque

(1) gestionnaire de mots de passe avec un mot de passe unique par compte, (2) authentification forte sur les comptes critiques — application TOTP ou clé physique pour l'email, le cloud, le gestionnaire, et les fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste) ; pour la banque, utiliser le moyen d'authentification forte proposé par l'établissement (application bancaire, Secure Key, validation biométrique) plutôt que le SMS quand une alternative existe, (3) mises à jour automatiques sur tous les appareils, (4) verrouillage systématique (téléphone code 6+, ordinateur), (5) sauvegardes régulières (cloud + disque externe tous les 3 mois), (6) vérifier avant de cliquer (lien, QR code, appel — 10 secondes de vérification suffisent), (7) localisation à distance configurée (Find My / Find My Device), (8) nettoyer les images avant partage (flouter, recadrer, supprimer les EXIF), (9) raccrocher et rappeler pour tout appel suspect, (10) codes de récupération MFA stockés hors du téléphone.

Le **mot de sécurité familial** : convenir avec ses proches (parents, conjoint, enfants) d'un mot ou d'une phrase à demander dans toute situation d'urgence où l'identité doit être confirmée — protection contre le deepfake vocal. Ce mot ne doit jamais figurer en ligne, dans un message, ou dans une publication — il vit uniquement dans la mémoire des membres de la famille.

#### 45.3 Préparer l'héritage numérique

*La question rarement abordée : que devient votre vie numérique si vous ne pouvez plus y accéder — accident, maladie, décès ?*

Sans préparation : les proches se retrouvent à devoir prouver leur lien à des fournisseurs étrangers, parfois sans succès. Les photos de famille restent verrouillées dans iCloud, les comptes en ligne continuent d'exister sans personne pour les fermer, les abonnements continuent de prélever, et les messages sur les réseaux sociaux restent en suspens.

**Les outils des plateformes** : la plupart des géants du numérique ont mis en place des mécanismes — encore mal connus — pour préparer la transmission.

- **Apple** : « Contact légataire » (Réglages > [votre nom] > Connexion et sécurité > Contact légataire) — désigne une personne qui pourra accéder à vos données iCloud après votre décès en présentant un certificat de décès.
- **Google** : « Gestionnaire de compte inactif » (myaccount.google.com/inactive) — définit ce qui doit se passer si le compte n'est pas utilisé pendant X mois (transmission de certaines données à des contacts désignés, suppression).
- **Facebook/Meta** : « Contact légataire » qui peut transformer le profil en compte de commémoration ou demander la suppression.
- **Microsoft** : pas d'équivalent direct, mais procédure de demande pour les ayants droit.

**Le coffre papier minimal** : un document — chez un notaire, dans un coffre, ou chez un proche de confiance — contenant le strict nécessaire pour qu'une personne de confiance puisse intervenir en cas d'incapacité ou de décès. Quoi y mettre : la liste des comptes essentiels (email, banque, gestionnaire de mots de passe — pas les mots de passe en clair, juste l'inventaire), les contacts utiles (employeur, banque, mutuelle, opérateurs), et le mot de passe maître du gestionnaire — soit dans le même document, soit dans une enveloppe scellée à part. Cette information doit être traitée avec autant de soin qu'un testament — c'est de fait un testament numérique.

**Le testament numérique** : la loi française reconnaît le droit de définir des directives concernant la conservation, l'effacement, et la communication des données après le décès (article 85 de la loi Informatique et Libertés modifiée). Ces directives peuvent être inscrites auprès d'un tiers de confiance certifié, ou plus simplement dans un testament classique chez un notaire.

**Le geste minimum**, même sans formaliser : informer une personne de confiance qu'il existe un gestionnaire de mots de passe, où les codes de récupération sont stockés, et qui contacter en cas d'urgence. Cette conversation de 5 minutes peut épargner des semaines de difficultés à vos proches.

#### 45.4 Maintenir : la cybersécurité comme habitude, pas comme projet

La sécurité n'est pas un projet qui se termine. Les comptes évoluent, les outils changent, les menaces se transforment. Le réflexe d'entretien : une **revue annuelle** (15 minutes en début d'année — état des comptes critiques, mises à jour, sauvegarde fonctionne, codes de récupération à jour, contacts de récupération encore valides), et une **revue trimestrielle légère** (sessions actives sur les comptes principaux, partages cloud, abonnements actifs).

Le piège inverse : la sur-paranoïa qui paralyse. Si la cybersécurité personnelle devient une charge mentale qui empêche d'utiliser le numérique sereinement, c'est qu'elle est mal calibrée. Le but : un cadre qui rend le numérique plus serein, pas plus stressant.

> **🔵 Lina — Épilogue :** 6 mois après le début du cours. Gestionnaire de mots de passe (Bitwarden), authentification forte sur les 8 comptes critiques (TOTP pour email/cloud/gestionnaire/FranceConnect/Ameli/impôts/messagerie ; validation par l'app bancaire pour la banque), iPhone et MacBook chiffrés et à jour, Find My activé, codes de récupération imprimés chez ses parents, sauvegarde trimestrielle sur disque externe, profil Instagram en privé, partages Google Drive nominatifs, mot de sécurité familial convenu avec sa mère, et contact légataire Apple désigné. Elle n'est pas devenue paranoïaque — elle a construit des habitudes. Le jour où elle reçoit un faux appel de sa banque, elle raccroche, rappelle le vrai numéro, et signale la tentative. 30 secondes. Zéro dégât. La méthode a remplacé la vigilance vague — et c'est ce qui change tout.

---

> ### 🟦 Réflexes — Fin de Partie VIII
>
> **À configurer** :
> - Plan de réaction écrit : numéros opposition SIM/banque, ordre des actions
> - Contact légataire Apple / Gestionnaire de compte inactif Google
> - Coffre papier minimal chez un proche de confiance ou notaire
> - Revue annuelle planifiée (date dans l'agenda)
>
> **À éviter** :
> - Réinitialisation de téléphone/PC sans déconnecter d'abord les comptes Apple/Google
> - Vente d'appareil avec un formatage rapide (pas suffisant)
> - SAV qui demande votre mot de passe sans changement temporaire
> - Réinstallation depuis une sauvegarde d'un appareil qu'on suspecte compromis
>
> **À vérifier** :
> - Find My / Find My Device toujours actif et fonctionnel
> - Sessions actives sur les comptes critiques (trimestriel)
> - Partages cloud actifs (semestriel)
> - Vous savez où sont vos codes de récupération MFA
> - Une personne de confiance sait où trouver l'essentiel en cas d'urgence
>
> **Si quelque chose arrive** :
> - Compte compromis → MdP du compte → email maître → MFA → sessions → comptes liés
> - Téléphone perdu/volé → SIM → Find My → email → sessions → banque → plainte
> - Fraude bancaire → opposition immédiate → contestation 13 mois max → THESEE → médiateur si refus
> - Doute sur compromission → 17Cyber + Cybermalveillance.gouv.fr

---



## ANNEXES

---

<a id="annexe-a"></a>
### Annexe A — Glossaire

| Terme | Définition |
|-------|-----------|
| **Phishing** | Email frauduleux imitant un service légitime pour voler des identifiants |
| **Smishing** | Phishing par SMS |
| **Vishing** | Phishing par appel vocal |
| **Quishing** | Phishing par QR code |
| **Credential stuffing** | Test automatisé de mots de passe volés sur d'autres services |
| **SIM swap** | Transfert frauduleux du numéro de téléphone vers une nouvelle SIM |
| **MFA fatigue** | Envoi massif de notifications MFA pour pousser la victime à accepter |
| **Evil Twin** | Faux point d'accès Wi-Fi imitant un réseau légitime |
| **Juice jacking** | Vol de données ou installation de malware via un port USB public |
| **Shoulder surfing** | Observation du code/mot de passe par-dessus l'épaule |
| **Passkey** | Authentification sans mot de passe par clé cryptographique |
| **TOTP** | Time-based One-Time Password — code temporaire de MFA généré par une application |
| **Dark pattern** | Design d'interface conçu pour tromper l'utilisateur |
| **Deepfake** | Contenu audio/vidéo synthétique généré par IA |
| **BYOD** | Bring Your Own Device — utilisation d'un appareil personnel au travail |
| **EXIF** | Métadonnées intégrées dans les photos (GPS, appareil, date) |
| **PNR** | Passenger Name Record — référence de réservation aérienne |
| **Spoofing** | Falsification de l'identité de l'expéditeur (email, téléphone) |
| **Stalkerware** | Logiciel de surveillance installé à l'insu de la victime, souvent par un proche |
| **FRP** | Factory Reset Protection — protection Android empêchant l'usage après réinitialisation sans le compte Google d'origine |
| **Verrouillage d'activation** | Équivalent Apple du FRP (lié au compte iCloud) |
| **Sextorsion** | Chantage à la diffusion de contenu intime |
| **Sharenting** | Partage par les parents de contenus concernant leurs enfants sur les réseaux sociaux |
| **Romance scam** | Arnaque sentimentale en ligne aboutissant à une demande d'argent |
| **Spear phishing** | Phishing ciblé sur une personne précise avec des informations personnalisées |
| **Fraude au président** | Arnaque ciblant une entreprise en se faisant passer pour le dirigeant |
| **DLP** | Data Loss Prevention — outils de prévention de fuite de données en entreprise |
| **MDM** | Mobile Device Management — gestion à distance d'appareils mobiles |
| **HTTPS** | Protocole web chiffré (cadenas dans la barre d'adresse) |
| **3D Secure** | Authentification forte pour les paiements en ligne |
| **Mule (financière)** | Personne utilisée à son insu pour transiter des fonds frauduleux |
| **Caviardage** | Masquage d'informations sensibles dans un document |
| **CSPN** | Certification de Sécurité de Premier Niveau délivrée par l'ANSSI à un produit, sur une version et un périmètre précis |
| **Qualification ANSSI** | Évaluation plus poussée que la CSPN, à trois niveaux (Élémentaire, Standard, Renforcée) ; concerne aussi le service (SecNumCloud pour les hébergeurs) |
| **SecNumCloud** | Référentiel ANSSI qualifiant des prestataires cloud sur des exigences de sécurité et de souveraineté |
| **Conteneur chiffré** | Fichier qui rassemble et chiffre d'autres fichiers, ouvert par mot de passe ou clé (ex. Zed!, VeraCrypt) — protège le contenu indépendamment du canal de transport |

---

<a id="annexe-b"></a>
### Annexe B — Checklists pratiques

#### Checklist téléphone
Code 6+ chiffres ; biométrie activée ; mises à jour automatiques actives ; Find My / Find My Device activé et testé ; permissions des apps révisées ; notifications sans prévisualisation sur écran de verrouillage pour les apps sensibles ; chiffrement actif ; store officiel uniquement ; Stolen Device Protection (iOS 17.3+) / Theft Detection Lock (Android 15+) activée ; numéro d'opposition SIM noté hors du téléphone.

#### Checklist ordinateur
Compte standard (pas admin) au quotidien ; mises à jour OS + navigateur + apps automatiques ; chiffrement disque (BitLocker / FileVault) ; verrouillage de session automatique (5 minutes) ; antimalware actif (Defender / XProtect suffit) ; pas de cracks ni logiciels piratés ; macros Office désactivées par défaut ; extensions navigateur minimales et révisées.

#### Checklist mots de passe et MFA
Gestionnaire de mots de passe installé et alimenté ; mot de passe maître long, mémorisé, unique ; un mot de passe unique par compte ; authentification forte sur les comptes critiques (application TOTP ou clé physique pour email/cloud/gestionnaire/fournisseurs d'identité utilisés via FranceConnect, application bancaire ou validation biométrique pour la banque) ; SMS évité dès qu'une alternative existe ; codes de récupération imprimés et stockés hors du téléphone ; passkeys activées sur les services qui les supportent ; mots de passe pro et perso strictement séparés.

#### Checklist Wi-Fi public
Préférer le partage de connexion mobile pour les opérations sensibles ; vérifier la présence du HTTPS ; oublier le réseau après usage ; pas de banque, email maître, ni paiement sur Wi-Fi public sans VPN payant fiable ; portail captif → ne jamais saisir email + mot de passe d'un compte existant.

#### Checklist voyage
Sauvegarder avant de partir ; noter les numéros de blocage SIM et opposition bancaire sur un support hors du téléphone ; activer Find My ; filtre de confidentialité sur le laptop ; pas de recharge USB publique (chargeur secteur ou data-blocker) ; vérifier les QR codes (autocollant ?) ; se déconnecter des smart TV et appareils d'hôtel au checkout.

#### Checklist achat en ligne
Vérifier l'URL exacte (domaine officiel ?) ; HTTPS présent ; mentions légales et SIRET vérifiables ; prix cohérents avec le marché ; moyen de paiement sécurisé (CB avec 3DS, PayPal — pas de virement à un particulier) ; ne pas suivre un lien envoyé par message — taper l'URL directement.

#### Checklist partage de document sensible
Lien nominatif (pas « toute personne ayant le lien ») ; durée limitée ; filigrane contextuel (« remis à X le Y pour Z ») ; métadonnées supprimées ; canal sécurisé (Signal, partage authentifié) ; principe du minimum nécessaire (masquer ce qui n'est pas pertinent).

#### Checklist compte compromis
Changer mot de passe du compte → email maître si même MdP → activer MFA → révoquer toutes les sessions → vérifier paramètres (email de récup, transfert, filtres) → changer comptes avec même MdP → documenter → informer contacts si messages envoyés en votre nom.

#### Checklist téléphone perdu ou volé
Bloquer SIM (numéro opérateur) → localiser/verrouiller/effacer (Find My) → email maître changé → révoquer sessions des comptes critiques → mots de passe sensibles changés → banque prévenue → employeur prévenu si pro → plainte au commissariat (récépissé pour assurance).

#### Checklist revente / don / SAV
Sauvegarder ce qu'on veut garder → déconnecter iCloud / compte Google AVANT réinitialisation → effacer (option « nettoyer le lecteur » sur Windows, Effaçeur sur macOS, Effacer toutes les données sur Android) → retirer SIM physique et désactiver eSIM → pour SAV : changer MdP temporairement et revérifier au retour.

#### Checklist parent attentif
Contrôle parental activé (Screen Time / Family Link) ; restrictions d'achat ; écrans dans pièces communes pour jeunes enfants ; dialogue ouvert sur ce que l'enfant fait en ligne ; numéro 3018 connu par l'adolescent ; pas de photo de l'enfant publique avec école/lieu identifiable.

#### Checklist relation potentiellement à risque
Mots de passe critiques personnels (pas partagés) ; partage de localisation révisé ; comptes familiaux inventoriés ; trackers Bluetooth vérifiés ; sessions actives revues ; profils MDM contrôlés ; en cas de crainte de violence : 3919 avant tout geste numérique.

---

<a id="annexe-c"></a>
### Annexe C — Tableau des signaux d'arnaque

| Signe observé | Risque probable | Action recommandée |
|--------------|----------------|-------------------|
| SMS « votre colis est en attente » + lien | Smishing — phishing colis | Ne pas cliquer → vérifier sur le site du transporteur |
| Appel « service fraude de votre banque » | Vishing — faux conseiller | Raccrocher → rappeler le numéro officiel |
| Pop-up « VOTRE PC EST INFECTÉ » | Faux support technique | Fermer le navigateur (Alt+F4) → ne pas appeler |
| Email « votre compte sera fermé » + lien | Phishing classique | Ne pas cliquer → aller directement sur le site officiel |
| QR code collé sur une borne/affiche | Quishing — faux QR code | Vérifier l'URL avant d'ouvrir → pas de données bancaires |
| Offre d'emploi trop belle sans entretien | Faux recrutement / mule | Ne pas envoyer pièce d'identité ni RIB |
| Demande d'argent urgente d'un « proche » | Deepfake vocal / usurpation | Raccrocher → rappeler sur le vrai numéro → mot de sécurité |
| Vendeur marketplace qui veut payer hors plateforme | Arnaque marketplace | Rester sur la plateforme → ne pas suivre les liens externes |
| Code SMS demandé par un interlocuteur | Validation d'une opération frauduleuse | Ne JAMAIS donner un code SMS reçu → raccrocher |
| Notification MFA non sollicitée | MFA fatigue ou compromission | Ne JAMAIS accepter → changer le mot de passe |
| Email « impôts/Ameli/CAF » avec lien de connexion | Phishing administratif | Ne pas cliquer → aller sur impots.gouv.fr / ameli.fr |
| Investissement « rendement garanti » par DM | Pig butchering / faux trading | Ne pas verser → vérifier listes noires AMF + agrément REGAFI |
| Faux profil séduisant qui partage du contenu intime | Sextorsion | Ne pas répondre → conserver preuves → 3018 / Pharos |
| Logement à louer trop beau, paiement avant visite | Arnaque au logement | Visite physique obligatoire → pas de paiement avant signature |
| « J'ai vu votre profil sur LinkedIn », demande pro inhabituelle | Spear phishing | Vérifier hors canal (rappel sur numéro connu) |
| Téléphone qui chauffe, batterie qui tombe vite, app inconnue | Stalkerware potentiel | Ne pas agir seule si contexte sensible → 3919 / Cybermalveillance |
| Alerte « tracker inconnu se déplace avec vous » | AirTag malveillant | Vérifier sac/véhicule → suivre les instructions du téléphone |

---

<a id="annexe-d"></a>
### Annexe D — Configuration minimale recommandée

**iPhone** : code 6 chiffres + Face ID/Touch ID ; mises à jour auto ; Find My activé ; notifications sans prévisualisation pour banque, MFA, messageries ; AirDrop « Contacts uniquement » ; Stolen Device Protection activée ; révision des permissions apps ; contact légataire désigné.

**Android** : code 6 chiffres + biométrie ; mises à jour auto (système + apps) ; Find My Device activé ; Google Play Protect activé ; notifications sans contenu sur verrouillage ; Quick Share « Contacts uniquement » ; Theft Detection Lock activé (Android 15+).

**Windows** : compte standard ; Windows Update auto ; BitLocker activé (Pro) ; Windows Defender actif ; verrouillage auto 5 min ; pas de macros auto dans Office ; extensions navigateur minimales.

**macOS** : FileVault activé ; mises à jour auto ; Gatekeeper activé ; verrouillage auto 5 min ; pare-feu activé ; XProtect actif (par défaut).

**Navigateur** : mises à jour auto ; extensions minimales ; auto-remplissage désactivé (utiliser le gestionnaire de MdP) ; notifications push refusées par défaut ; HTTPS-Only mode activé si disponible ; profil dédié pour les usages sensibles.

**Box Internet** : mot de passe Wi-Fi changé (pas celui par défaut) ; WPA2/WPA3 ; WPS désactivé ; mot de passe admin de la box changé ; firmware à jour ; réseau invité activé pour les objets connectés.

**Cloud personnel** : MFA TOTP activé ; partages révisés (semestriel) ; pas de documents d'identité en clair ; corbeille vidée régulièrement ; album « masqué » / dossier verrouillé pour les contenus sensibles.

**Comptes administratifs** : fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste, France Identité) avec mot de passe unique et authentification renforcée disponible activée ; France Identité activée si CNI électronique ; alertes Ameli activées ; vérification trimestrielle des connexions sur l'espace FranceConnect.

---

<a id="annexe-e"></a>
### Annexe E — Modèle de plan personnel de cybersécurité

```
MES COMPTES CRITIQUES (par ordre de priorité)
1. Email maître : _______ (MFA : oui/non, type : _______)
2. Banque : _______ (MFA : oui/non, type : _______)
3. Gestionnaire de MdP : _______ (MdP maître mémorisé : oui/non)
4. Cloud principal : _______ (MFA : oui/non)
5. Messagerie principale : _______
6. Fournisseur(s) d'identité FranceConnect (Ameli, impots, La Poste, France Identité) : _______ (auth. forte : oui/non)
7. Réseau social principal : _______ (MFA : oui/non)

MES APPAREILS
- Téléphone : _______ (Find My : oui/non, chiffré : oui/non)
- Ordinateur : _______ (chiffrement disque : oui/non)
- Appareil de secours : oui/non

MA SAUVEGARDE
- Cloud : _______ (fréquence : _______)
- Disque externe : oui/non (fréquence : _______)
- Codes de récupération MFA : imprimés et stockés à _______

MA RÉACTION EN CAS D'INCIDENT
- N° blocage SIM : _______
- N° opposition bancaire : _______
- Email de récupération secondaire : _______
- Mot de sécurité familial : convenu avec _______

MA TRANSMISSION NUMÉRIQUE
- Contact légataire Apple : _______
- Gestionnaire de compte inactif Google configuré : oui/non
- Coffre papier minimal stocké chez : _______
- Personne de confiance informée : _______

MES 5 ACTIONS PRIORITAIRES (à compléter)
1. _______
2. _______
3. _______
4. _______
5. _______

PROCHAINE REVUE : _______ (date dans l'agenda)
```

---

<a id="annexe-f"></a>
### Annexe F — Cartographie des arnaques fréquentes

| Arnaque | Mécanisme | Signaux | Réflexe |
|---------|-----------|---------|---------|
| **Faux colis** | SMS avec lien vers faux site de livraison | Lien court, urgence, demande de paiement | Ne pas cliquer → vérifier sur le site transporteur |
| **Faux support** | Pop-up ou appel prétendant virus | Alarmisme, prise en main à distance | Fermer → ne pas appeler → ne pas donner accès |
| **Faux banquier** | Appel spoofé, connaissance partielle infos | Demande de code SMS, urgence | Raccrocher → rappeler le vrai numéro |
| **Faux QR code** | QR autocollant collé sur le vrai | Autocollant visible, URL suspecte | Vérifier l'URL avant d'ouvrir |
| **Faux recrutement** | Offre trop belle, demande de docs | Pas d'entretien, salaire irréaliste | Ne pas envoyer ID ni RIB |
| **Marketplace** | Paiement hors plateforme, faux lien | Lien externe, urgence vendeur/acheteur | Rester sur la plateforme |
| **Romance scam** | Relation en ligne + demande d'argent | « Proche » jamais vu, urgence financière | Ne jamais envoyer d'argent |
| **Pig butchering** | Relation + investissement « sûr » | Plateforme inconnue, gains progressifs, retraits bloqués | Ne pas verser, ne pas investir, signaler AMF |
| **Deepfake vocal** | Clone de voix d'un proche | Urgence, demande d'argent, appel inattendu | Rappeler le vrai numéro, mot de sécurité |
| **Arnaque CPF** | Appel/SMS « votre CPF expire » | Le CPF n'expire jamais | Ne pas répondre → signaler 33700 |
| **Faux paiement** | Lien de paiement frauduleux | URL non officielle, contexte marketplace | Ne payer que via plateforme officielle |
| **Sextorsion** | Faux profil + chantage diffusion contenu intime | Demande de rançon, menaces | Ne pas payer, conserver preuves, 3018/Pharos |
| **Faux logement** | Annonce alléchante, paiement avant visite | Pas de visite physique possible | Visite obligatoire, jamais de virement avant signature |
| **Faux Ameli/impôts** | Email/SMS de phishing administratif | Lien de « connexion » ou « remboursement » | Aller directement sur le site officiel |
| **Fraude au président** | Deepfake vocal du dirigeant + virement urgent | Confidentialité demandée, urgence | Validation hors canal obligatoire |
| **SIM swap** | Détournement du numéro vers nouvelle SIM | Plus de réseau soudain, SMS d'opérateur étranges | Contacter opérateur immédiatement, opposition compte |

---

<a id="annexe-g"></a>
### Annexe G — Ressources utiles

| Ressource | Usage | Accès |
|-----------|-------|-------|
| **Cybermalveillance.gouv.fr** | Assistance aux victimes, fiches pratiques | cybermalveillance.gouv.fr |
| **17Cyber** | Assistance en ligne, diagnostic, orientation | 17cyber.gouv.fr |
| **THESEE** | Plainte en ligne pour e-escroqueries et certaines usurpations (particuliers majeurs) | service-public.fr/cmi |
| **Pharos** | Signalement de contenus illicites en ligne | internet-signalement.gouv.fr |
| **Signal Spam** | Signalement de phishing email | signal-spam.fr |
| **33700** | Signalement de SMS frauduleux | Envoyer le SMS au 33700 |
| **Info Escroqueries** | Conseil et orientation victimes | 0 805 805 817 (gratuit) |
| **3919** | Violences Femmes Info — écoute, orientation (pas un numéro d'urgence : danger immédiat → 17 ou 112) | 3919 (gratuit, anonyme, 24/7) |
| **3018** | Violences numériques pour mineurs et jeunes adultes | 3018 (gratuit, anonyme, 7j/7 9h-23h) |
| **France Victimes** | Accompagnement aux victimes | 116 006 |
| **ANSSI** | Guide d'hygiène numérique | ssi.gouv.fr |
| **CNIL** | Droits, réclamations, vie privée | cnil.fr |
| **Have I Been Pwned** | Vérifier si un email est dans une fuite | haveibeenpwned.com |
| **Listes noires AMF** | Identifier les sites/intermédiaires signalés comme frauduleux ou non autorisés (finance) | listes-noires.amf-france.org |
| **REGAFI** | Registre des agents financiers — vérifier l'agrément d'une entité offrant des services financiers en France | regafi.fr |
| **ORIAS** | Vérifier intermédiaires assurance/finance enregistrés | orias.fr |
| **Opposition bancaire** | Blocage carte / contestation | Numéro au dos de la carte |
| **SignalConso** | Signaler démarchage abusif, pratiques commerciales déloyales | signal.conso.gouv.fr |
| **France Rénov'** | Espace conseil officiel rénovation énergétique | france-renov.gouv.fr |
| **Olvid** | Messagerie sécurisée française (CSPN ANSSI sur versions/périmètres précis) | olvid.io |
| **Tchap** | Messagerie souveraine du secteur public français | tchap.beta.gouv.fr |
| **Tixeo** | Visioconférence française certifiée CSPN par l'ANSSI ; offres TixeoPrivateCloud sur hébergement qualifié SecNumCloud (selon versions/périmètres précis) | tixeo.com |
| **France Transfert** | Transfert de fichiers volumineux pour agents de l'État | francetransfert.numerique.gouv.fr |
| **Zed! (PRIM'X)** | Conteneurs chiffrés pour envoi de fichiers sensibles (certifications ANSSI sur versions/périmètres précis) | primx.eu |
| **Cryptomator** | Coffre chiffré open source pour cloud personnel | cryptomator.org |
| **VeraCrypt** | Conteneurs chiffrés avancés open source | veracrypt.fr |
| **La Suite numérique (DINUM)** | Outils numériques souverains pour les agents publics | suite.numerique.gouv.fr |
| **Albert (Etalab)** | Assistant IA d'État pour les agents publics | albert.api.etalab.gouv.fr |
| **ANSSI — Catalogue de produits qualifiés** | Liste officielle des produits évalués/qualifiés par l'ANSSI | cyber.gouv.fr (rubrique « Visa de sécurité ») |

---

<a id="annexe-h"></a>
### Annexe H — Matrice de priorité

Pour aider à trier les actions par urgence et impact réel, voici une matrice à trois niveaux. Le **vital** doit être en place avant tout. L'**important** vient ensuite et limite les dégâts. L'**utile** renforce la posture mais n'est pas un préalable.

| Priorité | À faire | Pourquoi |
|----------|---------|----------|
| **Vital** | Email maître sécurisé (mot de passe unique + MFA app TOTP ou clé physique) ; gestionnaire de mots de passe ; téléphone verrouillé code 6+ ; Find My / Find My Device activé ; sauvegarde des photos et documents critiques | Protège l'identité numérique. Sans ça, tout le reste s'effondre en cas d'incident. |
| **Important** | Cloud principal sécurisé ; fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste) avec mot de passe unique et authentification renforcée ; banque avec authentification forte de l'app bancaire ; mises à jour automatiques ; codes de récupération MFA imprimés hors du téléphone ; vérification des sessions actives ; séparation pro/perso des mots de passe ; choix conscient des outils selon la sensibilité des données (Partie V) | Limite les dégâts en cas de compromission d'un compte secondaire, et évite les fuites involontaires liées au choix d'outil. |
| **Utile** | Profils navigateur séparés ; segmentation IoT (réseau invité) ; suppression des métadonnées avant partage ; revue annuelle des partages cloud ; carte virtuelle pour les essais gratuits ; mot de sécurité familial ; contact légataire désigné ; clé physique de secours pour comptes critiques ; chiffrement local avec **Cryptomator** ou **Zed!** selon usage (cloud personnel vs envoi à un destinataire identifié) ; pour agents publics ou contextes sensibles : **Tchap**, **Olvid**, **France Transfert**, **Visio de l'État**, **Tixeo** selon validation organisationnelle | Renforce la posture, prévient des fuites involontaires, prépare la transmission. |

**Lecture suggérée** : si vous lisez ce cours pour la première fois, traitez le « vital » dans l'heure (Parcours Express en tête), puis l'« important » sur quelques semaines, puis l'« utile » à votre rythme. Tenter le tout en une fois fatigue plus qu'il ne protège.

---

<a id="annexe-i"></a>
### Annexe I — Que faire si... (situations courantes)

*Format ultra court : situation → gravité → actions immédiates. À consulter en cas d'incident, sans relire tout le cours.*

#### J'ai cliqué sur un lien suspect mais je n'ai rien saisi
**Gravité : faible.** Un simple clic sur un lien malveillant est rarement suffisant pour compromettre un appareil moderne à jour. **Actions** : fermer l'onglet, ne pas saisir d'identifiant, ne pas télécharger ce qui est proposé. Vérifier l'URL exacte (capture d'écran si signalement). Lancer une analyse antimalware par sécurité. Si vous étiez sur un site bancaire, vérifier les sessions actives et changer le mot de passe par précaution.

#### J'ai saisi mon mot de passe sur un site suspect
**Gravité : élevée.** Le mot de passe est probablement compromis. **Actions immédiates** : (1) changer ce mot de passe sur le vrai site, (2) si ce mot de passe était réutilisé ailleurs, le changer partout, (3) activer le MFA si pas déjà fait, (4) vérifier les sessions actives et déconnecter tout, (5) vérifier les paramètres du compte (email de récupération, transferts, filtres ajoutés). Surveiller les jours suivants.

#### J'ai donné un code SMS à quelqu'un qui m'appelait
**Gravité : critique.** L'attaquant a très probablement validé une opération frauduleuse à votre place. **Actions immédiates** : (1) appeler la banque sur le vrai numéro pour faire opposition et bloquer toute opération en cours, (2) faire opposition sur la carte, (3) consulter l'historique des opérations et lister les anomalies, (4) déposer plainte (THESEE ou commissariat), (5) contester par écrit auprès de la banque dans les 13 mois (article L133-18 CMF). Conserver tous les éléments.

#### J'ai envoyé une photo de ma CNI / passeport
**Gravité : élevée à critique** selon le destinataire. **Actions** : (1) si le destinataire est suspect, déposer plainte pour usurpation d'identité potentielle (THESEE), (2) demander une nouvelle CNI (le numéro change), (3) interroger la Banque de France pour vérifier qu'aucun crédit n'a été souscrit (FICP), (4) surveiller les courriers reçus dans les semaines suivantes (notifications de comptes inconnus, relances), (5) garder une copie de la plainte — elle sera demandée par chaque organisme victime d'usurpation.

#### J'ai perdu mon téléphone
**Gravité : élevée si non préparé, faible si préparé.** **Actions immédiates** : (1) bloquer la SIM (numéro opérateur, à noter à l'avance hors du téléphone), (2) localiser et verrouiller/effacer via Find My / Find My Device depuis un autre appareil, (3) changer le mot de passe de l'email maître, (4) révoquer les sessions actives sur les comptes critiques, (5) prévenir la banque, (6) déposer plainte (récépissé pour assurance). Voir Ch.42.

#### Je reçois une menace de sextorsion
**Gravité : élevée psychologiquement, faible si on ne paie pas.** **Actions** : (1) ne pas répondre, ne pas payer (les arnaqueurs disparaissent quand ils n'obtiennent rien — payer entraîne plus de demandes), (2) bloquer le contact, (3) conserver toutes les preuves (captures avec URL/identifiant), (4) signaler sur Pharos, (5) plainte au commissariat ou via THESEE, (6) si mineur ou jeune adulte : 3018 (gratuit, anonyme, 7j/7 9h-23h). Si la menace concerne une diffusion, un signalement aux plateformes peut être appuyé par les autorités.

#### Une opération bancaire inconnue apparaît sur mon compte
**Gravité : élevée.** **Actions immédiates** : (1) faire opposition sur la carte si carte concernée (numéro au dos de la carte ou app bancaire), (2) contester l'opération par écrit auprès de la banque (délai 13 mois, 70 jours hors EEE), (3) demander un remboursement (article L133-18 CMF), (4) déposer plainte (THESEE), (5) si la banque refuse au motif de « négligence grave », saisir le médiateur bancaire, puis association de consommateurs (UFC-Que Choisir, CLCV).

#### Je pense être surveillé(e) par un proche
**Gravité : variable, parfois critique.** **NE PAS AGIR SEULE** si le contexte est violent ou conflictuel — une suppression brutale d'un stalkerware peut déclencher une escalade. **Actions** : (1) si situation de violence : 3919 (Violences Femmes Info, gratuit, anonyme, 24/7 — écoute et orientation, **pas un numéro d'urgence : danger immédiat → 17 ou 112**) ou France Victimes (116 006) pour un protocole de mise en sécurité, (2) sinon, suivre les étapes du Ch.38 (vérifier partages de localisation, sessions actives, profils MDM, trackers Bluetooth), (3) ne pas confronter directement avant d'avoir mis l'essentiel en sécurité.

#### J'ai mis un fichier pro / sensible dans une IA publique (ChatGPT, Gemini, etc.)
**Gravité : variable.** Le contenu est potentiellement sorti du périmètre maîtrisé. **Actions** : (1) supprimer la conversation dans l'historique de l'outil (cela ne garantit pas la suppression complète mais limite la visibilité), (2) si l'option « ne pas utiliser pour entraîner les modèles » existe, l'activer pour le compte, (3) signaler à la DSI / RSSI si pertinent (obligation potentielle si données client, données de santé, données régulées), (4) évaluer la nature du contenu — si données très sensibles, considérer l'incident comme une fuite et appliquer la procédure de l'organisation. Voir Ch.27.

#### J'ai reçu une notification MFA que je n'ai pas déclenchée
**Gravité : critique.** Quelqu'un essaie d'accéder à votre compte. **Actions immédiates** : (1) **refuser** la notification, (2) changer immédiatement le mot de passe du compte concerné, (3) vérifier les sessions actives, (4) vérifier que le MFA est bien actif, (5) chercher d'où vient la fuite (mot de passe réutilisé compromis ? — vérifier sur Have I Been Pwned).

#### Mon SIM ne capte plus subitement et je reçois des SMS de mon opérateur
**Gravité : critique** — possible SIM swap en cours. **Actions immédiates** : (1) appeler l'opérateur depuis un autre téléphone pour bloquer la SIM frauduleuse, (2) prévenir la banque (les comptes liés au numéro sont en danger immédiat), (3) changer les mots de passe critiques depuis un appareil sûr, (4) déposer plainte. Le SIM swap permet à l'attaquant de recevoir vos SMS, donc vos codes MFA SMS — ne plus se reposer dessus.

---

<a id="annexe-j"></a>
### Annexe J — Fiche d'urgence à imprimer

*Imprimer cette fiche en une page, la stocker en lieu sûr (chez soi, chez un proche de confiance, dans un coffre). Elle contient ce qu'il faut sous la main quand le téléphone n'est pas accessible. Ne pas y inscrire de mots de passe en clair — uniquement des références.*

```
┌───────────────────────────────────────────────────────────────┐
│            FICHE D'URGENCE NUMÉRIQUE — À IMPRIMER             │
│                                                               │
│  Nom : _______________________  Date de mise à jour : ____    │
│                                                               │
│  ━━━━━━━━━━━━━━━━ NUMÉROS À APPELER ━━━━━━━━━━━━━━━━           │
│                                                               │
│  Opposition carte bancaire : _____________________________    │
│  Banque (numéro général) :   _____________________________    │
│  Opérateur mobile (blocage SIM) : _______________________     │
│  Box Internet / FAI :        _____________________________    │
│  Assurance habitation :      _____________________________    │
│  Mutuelle santé :            _____________________________    │
│                                                               │
│  ━━━━━━━━━━━━━━━━ EMAILS DE RÉCUPÉRATION ━━━━━━━━━━━━━━━━     │
│                                                               │
│  Email maître :              _____________________________    │
│  Email de récupération 2 :   _____________________________    │
│  (sur fournisseur différent)                                  │
│                                                               │
│  ━━━━━━━━━━━━━━━━ MOT DE SÉCURITÉ FAMILIAL ━━━━━━━━━━━━━━     │
│                                                               │
│  Convenu avec : _________________________________________     │
│  (le mot lui-même reste en mémoire — ne pas l'écrire ici)     │
│                                                               │
│  ━━━━━━━━━━━━━━━ PERSONNE DE CONFIANCE ━━━━━━━━━━━━━━━━━      │
│                                                               │
│  Nom :       _____________________________                    │
│  Téléphone : _____________________________                    │
│  Sait où trouver : codes de récupération, gestionnaire        │
│                                                               │
│  ━━━━━━━━━━━━━━━━ AIDE D'URGENCE ━━━━━━━━━━━━━━━━━━━━━━       │
│                                                               │
│  17Cyber                  17cyber.gouv.fr (24/7)              │
│  Cybermalveillance        cybermalveillance.gouv.fr           │
│  Info Escroqueries        0 805 805 817 (gratuit)             │
│  THESEE (plainte)         service-public.fr/cmi               │
│  Pharos (signalement)     internet-signalement.gouv.fr        │
│  Signal Spam              signal-spam.fr                      │
│  SMS frauduleux           Renvoyer au 33700                   │
│  Violences Femmes Info    3919 (écoute, 24/7) — urgence : 17 │
│  Violences numériques     3018 (gratuit, 7j/7 9h-23h)         │
│  France Victimes          116 006                             │
│                                                               │
│  ━━━━━━━━━━━━ PLAN TÉLÉPHONE PERDU/VOLÉ ━━━━━━━━━━━━━         │
│                                                               │
│  1. Bloquer la SIM (opérateur)                                │
│  2. Localiser/verrouiller/effacer (Find My)                   │
│  3. Changer mot de passe email maître                         │
│  4. Révoquer sessions sur comptes critiques                   │
│  5. Prévenir la banque                                        │
│  6. Plainte au commissariat (récépissé assurance)             │
│                                                               │
│  ━━━━━━━━━━━━━━━ CODES DE RÉCUPÉRATION ━━━━━━━━━━━━━━━        │
│                                                               │
│  Stockés à : _____________________________                    │
│  (NE PAS les recopier ici — juste indiquer où ils sont)       │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

<a id="annexe-k"></a>
### Annexe K — Sources et ressources officielles

*Le cours s'appuie sur des références publiques. Les principales sont listées ici pour permettre au lecteur d'aller à la source en cas de doute ou d'évolution.*

| Domaine | Source officielle | URL |
|---------|------------------|-----|
| Assistance victimes (général) | Cybermalveillance.gouv.fr | cybermalveillance.gouv.fr |
| Assistance en ligne | 17Cyber | 17cyber.gouv.fr |
| Hygiène numérique (référence) | ANSSI | ssi.gouv.fr |
| Catalogue produits qualifiés ANSSI (Visa de sécurité) | ANSSI | cyber.gouv.fr |
| Outils souverains pour agents publics | La Suite numérique (DINUM) | suite.numerique.gouv.fr |
| Messagerie publique souveraine | Tchap | tchap.beta.gouv.fr |
| Transfert de fichiers (État) | France Transfert | francetransfert.numerique.gouv.fr |
| Assistant IA d'État | Albert (Etalab) | albert.api.etalab.gouv.fr |
| Démarches publiques (annuaire) | Service-public.fr | service-public.fr |
| Identité numérique fédérée | FranceConnect | franceconnect.gouv.fr |
| Identité numérique régalienne | France Identité | france-identite.gouv.fr |
| Données personnelles, droits | CNIL | cnil.fr |
| Marchés financiers, listes noires | AMF | amf-france.org |
| Banque, contrôle prudentiel | ACPR | acpr.banque-france.fr |
| Intermédiaires finance/assurance | ORIAS | orias.fr |
| Registre agents financiers | REGAFI | regafi.fr |
| Vérification fuite de données | Have I Been Pwned | haveibeenpwned.com |
| Plainte en ligne (e-escroqueries) | THESEE | service-public.fr/cmi |
| Signalement contenus illicites | Pharos | internet-signalement.gouv.fr |
| Signalement phishing email | Signal Spam | signal-spam.fr |
| Signalement SMS frauduleux | 33700 | renvoi du SMS au 33700 |
| Signalement consommation | SignalConso | signal.conso.gouv.fr |
| Rénovation énergétique | France Rénov' | france-renov.gouv.fr |
| CPF / formation | Mon Compte Formation | moncompteformation.gouv.fr |
| Violences femmes | 3919 | 3919.fr (numéro 3919) |
| Violences numériques (mineurs/jeunes) | e-Enfance / 3018 | e-enfance.org |
| Aide aux victimes | France Victimes | france-victimes.fr |
| Stalkerware (international) | Coalition Against Stalkerware | stopstalkerware.org |

---

<a id="annexe-l"></a>
### Annexe L — Avertissement éditorial et juridique

Ce cours a été rédigé pour fournir une vision générale, pratique et accessible des risques cybernétiques du quotidien et des gestes pour s'en prémunir. Il ne constitue ni un avis juridique, ni un conseil financier, ni une consultation médicale, ni une recommandation personnalisée.

**Indications juridiques** : les références aux articles de loi, aux délais de prescription, aux procédures de plainte, aux droits des consommateurs, aux droits à l'image, aux questions d'usurpation d'identité ou de violences numériques, sont **générales et informatives**. Elles peuvent évoluer (lois nouvelles, décrets, jurisprudence) et doivent être vérifiées au cas par cas. En cas de préjudice sérieux ou de situation complexe, il est recommandé de consulter un professionnel du droit (avocat, juriste), une association d'aide aux victimes (France Victimes, UFC-Que Choisir, CLCV), ou les autorités compétentes (police, gendarmerie, médiateur bancaire, CNIL, ARCEP, AMF selon le sujet).

**Indications financières** : les références aux placements, rendements, et types d'arnaques d'investissement n'ont pas vocation à se substituer à un conseil financier personnalisé. Avant tout investissement, vérifier l'agrément des intermédiaires (AMF, ACPR, ORIAS) et consulter un conseiller en investissement financier (CIF) enregistré.

**Indications médicales** : les références aux données de santé, à Mon espace santé, aux applications santé n'entendent pas se substituer à un avis médical. Pour toute question de santé, s'adresser à un professionnel de santé.

**Évolutions** : les outils, services, plateformes, listes de fournisseurs (FranceConnect notamment), numéros d'assistance, et procédures évoluent. Au moindre doute, vérifier sur le site officiel concerné — les URL des sources sont listées en Annexe K.

**Choix éditoriaux** : ce cours privilégie la clarté pratique sur l'exhaustivité technique. Certaines simplifications sont assumées pour ne pas perdre le lecteur non-expert. Le cours ne couvre pas les sujets techniques avancés (administration réseau, sécurité d'entreprise, menaces étatiques, cryptographie appliquée), qui font l'objet d'autres ressources spécialisées.

---

<a id="annexe-m"></a>
### Annexe M — Les 12 règles à retenir

*Si vous ne deviez retenir qu'une page de tout ce cours, c'est celle-ci. Une règle par geste essentiel. À relire de temps en temps. À transmettre à un proche.*

**1. Un mot de passe unique par compte.**
La réutilisation est le risque numéro un. Un gestionnaire de mots de passe rend cette règle tenable. Sans gestionnaire, on triche — avec gestionnaire, on tient.

**2. Email maître protégé en priorité.**
L'email principal contrôle la réinitialisation de tous les autres comptes. C'est le maillon central. Mot de passe unique le plus fort, MFA application TOTP ou clé physique, email de récupération secondaire chez un autre fournisseur.

**3. MFA sur les comptes critiques.**
Email, cloud, gestionnaire, fournisseurs d'identité utilisés via FranceConnect, et l'authentification forte de l'application bancaire pour la banque. Application TOTP ou clé physique préférables au SMS quand une alternative existe.

**4. Codes de récupération hors du téléphone.**
Imprimés ou notés à la main, stockés en lieu sûr (chez soi, chez un proche, dans un coffre). Pas dans le téléphone qu'on perd, pas uniquement dans le cloud.

**5. Raccrocher et rappeler.**
Pour tout appel inattendu sur un sujet sensible (banque, support, administration, proche en urgence). Ce seul réflexe désamorce la majorité des arnaques téléphoniques et des deepfakes vocaux.

**6. Ne jamais donner un code SMS.**
Aucun conseiller, aucun service, aucune autorité légitime ne demande un code SMS reçu sur votre téléphone. Quel que soit le prétexte, c'est une arnaque.

**7. Ne pas déposer un document sensible dans un outil non validé.**
Si vous n'auriez pas le droit d'envoyer ce document à une personne extérieure, ne le déposez pas dans une IA grand public, un convertisseur PDF gratuit, un OCR en ligne, ou un cloud personnel non sécurisé.

**8. Pas de lien public permanent pour les documents sensibles.**
« Toute personne ayant le lien » n'est pas un partage privé. Préférer le partage nominatif, avec mot de passe, durée d'expiration, et révocation possible. Pour les documents très sensibles, **chiffrer avant d'envoyer** (conteneur Zed! ou Cryptomator selon le contexte) — *le canal transporte, le conteneur protège*.

**9. Sauvegarder, dont une copie hors ligne.**
Photos irremplaçables, documents administratifs, codes de récupération : règle 3-2-1 (3 copies, 2 supports, 1 hors ligne). Le ransomware, la perte, et l'erreur humaine n'attendent pas.

**10. Vérifier avant de cliquer.**
Lien dans un SMS, QR code dans un lieu public, pièce jointe inattendue, page de connexion atterrie depuis un message : 10 secondes de vérification (URL, contexte, expéditeur réel) évitent des heures de galère.

**11. Préparer le plan « téléphone perdu ».**
Numéro d'opposition SIM, numéro d'opposition bancaire, email de récupération secondaire, codes de récupération, second appareil avec MFA configuré. La préparation transforme le désastre en désagrément.

**12. Demander de l'aide rapidement en cas d'incident.**
17Cyber, Cybermalveillance.gouv.fr, Info Escroqueries (0 805 805 817), 3919 / 3018 selon le contexte, France Victimes (116 006). La honte fait taire les victimes — le silence est l'allié de l'attaquant. Parler tôt limite les dégâts.

---

> **Note de clôture**
>
> Ce cours a été conçu pour enseigner la cybersécurité du quotidien comme une discipline de vigilance pratique — pas une collection d'astuces, pas un catalogue de menaces, pas un cours technique déguisé en sensibilisation.
>
> Lina illustre une transformation que chacun peut réaliser : en quelques heures d'apprentissage et quelques dizaines de minutes de mise en place, on passe de « je fais attention » (vague, insuffisant, et souvent faux) à « j'ai des habitudes, des outils, et un plan » (concret, mesurable, et efficace contre la grande majorité des risques).
>
> Le cours assume trois convictions. **Première** : la plupart des incidents commencent par un geste banal, pas par un exploit sophistiqué — la fatigue, l'urgence, la confiance, l'habitude et le confort sont les vrais vecteurs. **Deuxième** : 5 à 10 actions simples réduisent 80 % du risque — le gestionnaire de mots de passe, le MFA, les sauvegardes, les mises à jour, la vérification avant clic, et le « raccrocher et rappeler ». **Troisième** : la préparation transforme le désastre en désagrément — le même incident (téléphone volé, compte compromis, arnaque réussie) a des conséquences radicalement différentes selon qu'on a préparé la réaction ou non.
>
> Le cours assume aussi qu'on n'est jamais seul face à un incident. Les ressources existent — Cybermalveillance, 17Cyber, THESEE, 3919, 3018, France Victimes — et la honte qui fait taire les victimes est précisément ce sur quoi misent les attaquants. Parler, signaler, documenter, se faire aider : ces gestes ne sont pas des aveux d'échec, ce sont les premiers gestes de la reprise.
>
> *Comprendre les risques • Reconnaître les signaux • Adopter les réflexes • Savoir réagir • Préparer la transmission — parce que la cybersécurité du quotidien n'est pas une option, c'est une compétence de vie.*
