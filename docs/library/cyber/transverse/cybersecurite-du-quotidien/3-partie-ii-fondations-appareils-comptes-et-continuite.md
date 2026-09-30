---
title: 'PARTIE II — FONDATIONS : APPAREILS, COMPTES ET CONTINUITÉ'
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 3
chapters: 9
---

*Sécuriser les fondations avant tout — un appareil non protégé, un mot de passe réutilisé, ou un plan de récupération inexistant rendent toutes les autres protections inutiles.*

---

<a id="chapitre-5"></a>
## Chapitre 5 — Sécuriser son téléphone : le maillon central

Le téléphone est le point central de la vie numérique. Il contient l'email, la banque, le MFA, les messageries, les photos, la localisation. Le perdre sans préparation est l'un des pires scénarios du quotidien.

Le **verrouillage** : code à 6 chiffres minimum (un code à 4 chiffres a 10 000 combinaisons — observable par shoulder surfing en 2 secondes ; un code à 6 chiffres en a 1 million). La biométrie (Face ID, Touch ID, empreinte digitale) est un complément, pas un remplacement — le code est le vrai verrou car c'est lui qui déchiffre le téléphone au démarrage. Ne jamais utiliser un code trivial (000000, 123456, date de naissance). Le **chiffrement** est activé par défaut sur iOS et Android récent — mais il dépend du code : pas de code = pas de chiffrement effectif. Les **mises à jour** : activer les mises à jour automatiques. Les patchs de sécurité corrigent des vulnérabilités exploitées activement. Un téléphone qui ne reçoit plus de mises à jour de sécurité (Android en fin de support, iPhone trop ancien) est un téléphone à remplacer à moyen terme.

La **localisation et l'effacement à distance** : Find My iPhone (iOS), Find My Device (Android) — à configurer MAINTENANT, pas le jour de la perte. Ces services permettent de localiser le téléphone, de le verrouiller avec un message, et de l'effacer à distance si nécessaire.

Les **permissions des applications** : chaque application demande des permissions (micro, caméra, localisation, contacts, photos, fichiers). Le réflexe : accorder uniquement ce qui est strictement nécessaire à la fonction de l'application. Une application de lampe torche n'a pas besoin d'accéder aux contacts ni au micro. Réviser les permissions régulièrement (Réglages > Confidentialité sur iOS, Paramètres > Applications > Autorisations sur Android). Les **stores officiels** (App Store, Google Play) : ne pas installer d'applications depuis des sources tierces (APK téléchargés depuis un site web, liens reçus par SMS). Les applications malveillantes existent aussi sur les stores officiels, mais elles sont nettement moins fréquentes et sont retirées plus rapidement.

Le root (Android) et le jailbreak (iOS) **désactivent les protections de sécurité** du système d'exploitation. Ne pas le faire sur un appareil du quotidien. L'argument « je veux personnaliser mon téléphone » ne vaut pas la perte de la sandbox de sécurité, des mises à jour automatiques, et de la protection contre les applications malveillantes.

**Ce que votre téléphone sait de vous** — et partage sans que vous le réalisiez : l'**historique de localisation** (Google Timeline sur Android, Lieux importants sur iOS — désactivable dans les réglages de confidentialité ; cet historique montre vos déplacements sur des mois ou des années), les **permissions abusives des apps** (une app de jeu gratuit qui demande l'accès aux contacts et au micro pour « améliorer l'expérience » → elle collecte et revend ces données), le **pistage publicitaire** (IDFA sur iOS, GAID sur Android — un identifiant unique qui permet aux annonceurs de suivre votre activité entre les applications ; réinitialisable dans les réglages — iOS : Réglages > Confidentialité > Suivi, Android : Paramètres > Google > Publicité), les **notifications sur l'écran de verrouillage** (un code MFA, un message WhatsApp, un SMS bancaire — visibles par quiconque regarde l'écran → configurer les notifications en mode « pas de prévisualisation » pour les apps sensibles), et le **clipboard partagé** (un mot de passe copié dans le gestionnaire est accessible pendant quelques secondes à toute app qui lit le clipboard — sur iOS 16+, une notification apparaît quand une app lit le clipboard).

---

<a id="chapitre-6"></a>
## Chapitre 6 — Sécuriser son ordinateur personnel

Le **compte utilisateur** : utiliser un compte standard au quotidien, pas un compte administrateur. Un malware exécuté en admin a le contrôle total de la machine — il peut installer des logiciels, modifier la configuration, accéder à tous les fichiers. En compte standard, ses actions sont limitées. L'administrateur ne sert que pour les installations et les modifications système.

Les **mises à jour** : OS + navigateur + applications. Les mises à jour de l'OS seules ne suffisent pas — le navigateur est l'une des principales surfaces d'attaque (c'est par lui que passent les sites malveillants, les téléchargements, les extensions), et les applications tierces (lecteur PDF, suite bureautique, logiciel de visioconférence) ont aussi des vulnérabilités.

La **protection locale** : Windows Defender (intégré à Windows) est suffisant pour un usage personnel — pas besoin d'acheter une suite de sécurité payante. Sur macOS, Gatekeeper (vérifie la signature des applications) et XProtect (antimalware intégré) couvrent les bases. L'antivirus est un filet de sécurité, pas une protection absolue — il ne bloque pas tout et ne remplace pas les bons réflexes.

Le **chiffrement du disque** : BitLocker sur Windows Pro, FileVault sur macOS. Si l'ordinateur est volé, les données sont illisibles sans le mot de passe de session. Sans chiffrement, un attaquant peut accéder à tous les fichiers en démarrant depuis une clé USB. Le **verrouillage de session** : Win+L sur Windows, Ctrl+Cmd+Q sur macOS — le verrouiller à CHAQUE départ, même pour 2 minutes. Une session ouverte dans un café, une bibliothèque, ou un bureau partagé est une session compromise.

Les **téléchargements** : ne télécharger que depuis les sources officielles ou les stores. Les cracks, les logiciels piratés, et les « versions gratuites » de logiciels payants restent un vecteur majeur d'infection sur PC — le logiciel fonctionne, mais il contient parfois un malware en bonus (keylogger, stealer, ransomware). Les **macros Office** : ne JAMAIS « activer le contenu » dans un document reçu par email, sauf si l'on sait exactement pourquoi et que l'on fait confiance à l'expéditeur. Les macros malveillantes dans les documents Office sont un vecteur d'attaque classique. Les **extensions de navigateur** : chaque extension a accès à tout ce que le navigateur voit — y compris les pages bancaires. Installer le minimum strict, vérifier les permissions, et supprimer celles qu'on n'utilise plus.

---

<a id="chapitre-7"></a>
## Chapitre 7 — Mots de passe, gestionnaire, passkeys, MFA et SIM swap

### 7.1 Le vrai problème : la réutilisation

Le risque le plus structurant n'est pas le mot de passe faible — c'est le mot de passe réutilisé. Quand un service est piraté (LinkedIn 2021, Deezer 2022, et des centaines d'autres chaque année), les mots de passe volés sont testés automatiquement sur des dizaines d'autres services — c'est le credential stuffing. Si le même mot de passe est utilisé sur Netflix ET sur la banque, la compromission de Netflix = la compromission de la banque. La vérification : Have I Been Pwned (haveibeenpwned.com) permet de vérifier gratuitement si un email ou un mot de passe a été exposé dans une fuite de données.

### 7.2 Le gestionnaire de mots de passe

La seule solution réaliste pour avoir des mots de passe uniques partout : un gestionnaire de mots de passe (Bitwarden — gratuit et open source, 1Password — payant et très ergonomique, KeePass — local et gratuit). Le gestionnaire génère un mot de passe unique et aléatoire pour chaque compte, le stocke de manière chiffrée, et le remplit automatiquement. L'utilisateur ne retient qu'un seul mot de passe : le mot de passe maître. Ce mot de passe maître doit être long, mémorisable, et UNIQUE — ne jamais l'utiliser ailleurs. Une phrase de passe de 4-5 mots est idéale : « café.vélo.montagne.Jupiter.2024 ». La migration vers le gestionnaire prend une heure ou deux — c'est l'investissement le plus rentable de toute la cybersécurité personnelle.

### 7.3 Le MFA (authentification multi-facteurs)

Le MFA ajoute un second facteur après le mot de passe : quelque chose que l'on possède (un téléphone, une clé physique) en plus de quelque chose que l'on connaît (le mot de passe). Les options : un **code TOTP** généré par une application (Aegis ou 2FAS pour leur orientation open source et confidentialité, Ente Auth pour la sauvegarde chiffrée de bout en bout, Proton Authenticator pour un usage multiplateforme, Authy pour la commodité ; Google Authenticator reste utilisable mais propose moins de garanties différenciantes), une **notification push** (app bancaire), ou une **clé physique** (YubiKey — la plus sécurisée, résistante au phishing).

**TOTP dans une app dédiée vs dans le gestionnaire** : la plupart des gestionnaires modernes (Bitwarden, 1Password, Proton Pass) intègrent un générateur TOTP. C'est pratique — tout est au même endroit, le remplissage est automatique. Le compromis : si le gestionnaire lui-même est compromis, l'attaquant a à la fois le mot de passe ET le second facteur. La règle de bon sens : pour les comptes vraiment critiques (email maître, banque quand TOTP applicable, gestionnaire lui-même), privilégier une application TOTP séparée ou une clé physique. Pour les comptes secondaires (réseaux sociaux, services en ligne courants), TOTP dans le gestionnaire est acceptable et souvent préférable au SMS. Pour la **banque** en France, l'authentification forte passe en pratique par l'application bancaire, Secure Key, ou la validation biométrique — le TOTP n'est généralement pas l'option proposée ; utiliser le moyen le plus robuste mis à disposition par l'établissement.

Les **passkeys** sont la direction de l'industrie en 2025-2026 — authentification sans mot de passe par clé cryptographique liée au device, résistante au phishing et au credential stuffing. Apple, Google et Microsoft les supportent largement, et la majorité des services majeurs (banques, email, réseaux sociaux) les proposent en option. Quand le service propose les passkeys, les activer.

Les **codes de récupération** : à chaque activation de MFA, le service fournit des codes de secours. Ces codes doivent être imprimés ou stockés dans un lieu sûr — PAS dans le téléphone (c'est le téléphone qu'on perd). Sans ces codes, la perte du téléphone = la perte de l'accès aux comptes. La **fatigue MFA** : les attaquants envoient des dizaines de notifications push MFA jusqu'à ce que la victime accepte par épuisement → ne JAMAIS accepter une notification MFA qu'on n'a pas déclenchée soi-même.

### 7.4 Le SMS comme second facteur, et l'attaque SIM swap

Le **MFA par SMS** est mieux que rien mais il a une vulnérabilité majeure : le **SIM swap** (ou « port-out fraud »). Le mécanisme :

1. L'attaquant rassemble des informations personnelles sur la victime (fuites de données, réseaux sociaux, ingénierie sociale).
2. Il contacte l'opérateur de la victime en se faisant passer pour elle (« j'ai perdu ma carte SIM, j'aimerais la transférer sur une nouvelle SIM ») ou demande une portabilité du numéro vers un autre opérateur.
3. Avec les informations rassemblées (nom, date de naissance, adresse, parfois numéro de pièce d'identité ou d'abonné), il convainc le service client de l'opérateur de procéder au transfert.
4. Une fois le transfert effectué, le téléphone de la victime perd son réseau (plus de signal, plus de SMS, plus d'appels). L'attaquant reçoit désormais TOUS les SMS — y compris les codes MFA bancaires.
5. L'attaquant utilise les codes MFA pour accéder aux comptes de la victime, vider les comptes bancaires, ou changer les mots de passe.

Le SIM swap est devenu suffisamment **documenté et industrialisé** pour devoir être intégré aux réflexes de sécurité des comptes critiques. Des cas documentés font état de pertes de plusieurs dizaines de milliers d'euros par victime. Les opérateurs ont renforcé leurs procédures, mais le risque reste réel.

Les **signaux d'alerte d'un SIM swap en cours** : perte soudaine et inexpliquée du réseau mobile (« pas de service », « SOS uniquement »), notifications de connexion sur des comptes que vous n'avez pas déclenchées, impossibilité de recevoir des SMS, opérations bancaires que vous n'avez pas faites.

La **réaction immédiate en cas de suspicion de SIM swap** : appeler l'opérateur DEPUIS UN AUTRE TÉLÉPHONE (le vôtre n'a plus de réseau) pour bloquer immédiatement la SIM frauduleuse, contacter votre banque pour bloquer les comptes et vérifier les opérations récentes, changer les mots de passe des comptes critiques (depuis un autre appareil), et déposer plainte.

La **prévention** :
- **Préférer les apps TOTP ou les passkeys au SMS** pour le MFA des comptes critiques (banque, email, gestionnaire de mots de passe). Le code TOTP est généré localement sur le téléphone, il ne dépend pas du réseau opérateur.
- **Activer le verrouillage de portabilité** chez votre opérateur (option « blocage de la portabilité » ou « sécurité du numéro » selon les opérateurs — gratuit, à activer en quelques clics dans l'espace client). Cette option ajoute une vérification supplémentaire avant tout transfert.
- **Mettre un code PIN** sur la carte SIM elle-même (Réglages > Mobile sur iOS, Paramètres > Sécurité > Configurer le verrouillage de la carte SIM sur Android). Ce code est demandé au démarrage du téléphone et après tout retrait/insertion de la SIM.
- **Limiter l'exposition publique du numéro de téléphone** sur les réseaux sociaux et les sites web — un numéro associé à un nom et une date de naissance trouvable en ligne facilite le SIM swap.

L'**eSIM** : la carte SIM virtuelle (eSIM) a un profil similaire au SIM swap traditionnel — un eSIM swap consiste à transférer le profil eSIM vers un nouveau téléphone. Les opérateurs ont mis en place des procédures spécifiques (vérification d'identité renforcée), mais le risque existe.

Le **numéro de téléphone n'est plus une preuve d'identité fiable**. C'est une réalité de 2025-2026 que beaucoup de services n'ont pas encore intégrée. Quand vous avez le choix, préférez une méthode d'authentification qui ne dépend PAS du numéro de téléphone.

---

<a id="chapitre-8"></a>
## Chapitre 8 — Navigateur, sessions et hygiène web

Les **sessions actives** : chaque onglet de connexion est une session ouverte. Si quelqu'un accède au navigateur, il accède à tous les comptes connectés. Le réflexe : se déconnecter des comptes sensibles après utilisation (banque, email), surtout sur un ordinateur partagé. Les **cookies** de session maintiennent la connexion — le vol de cookie (par un malware ou une extension malveillante) permet à un attaquant d'accéder au compte sans connaître le mot de passe.

L'**auto-remplissage** : le navigateur propose de sauvegarder les mots de passe. C'est mieux que rien, mais moins sécurisé qu'un gestionnaire dédié — les mots de passe du navigateur sont accessibles à quiconque a accès à la session OS. Les **extensions** : chaque extension a accès à TOUT ce que le navigateur voit — les pages bancaires, les emails, les formulaires de connexion. Installer le minimum strict. Vérifier les permissions (une extension qui demande « lire et modifier toutes les données sur tous les sites » a un accès total). Supprimer les extensions inutilisées.

Les **notifications push** abusives : les sites qui demandent « Autoriser les notifications ? » — refuser systématiquement sauf pour les services essentiels. Les notifications push sont utilisées par des sites malveillants pour afficher du spam et du phishing directement sur le bureau ou l'écran du téléphone. Les **faux onglets de connexion** : un site malveillant affiche un faux formulaire de connexion Google/Microsoft/Facebook dans un popup qui imite parfaitement la page d'authentification légitime. Le réflexe : toujours vérifier l'URL dans la barre d'adresse — un vrai login Google est sur accounts.google.com, pas sur google-login-secure.com.

L'**hygiène par séparation** : utiliser un navigateur ou un profil pour les usages sensibles (banque, email principal, gestionnaire de mots de passe) et un autre pour la navigation courante (recherches, articles, réseaux sociaux). Les sessions, les cookies, et les extensions sont séparés — une compromission de la navigation courante n'affecte pas les sessions sensibles.

---

<a id="chapitre-9"></a>
## Chapitre 9 — Sauvegardes, récupération et comptes de secours

La **règle 3-2-1 adaptée** au grand public : 3 copies des données critiques, sur 2 supports différents (cloud + disque externe), dont 1 hors ligne (un disque externe débranché de l'ordinateur et du réseau). Les données critiques du particulier : photos irremplaçables (les photos de famille ne se recréent pas), documents d'identité numérisés (CNI, passeport — pour faciliter les démarches en cas de perte ou de vol des originaux), documents administratifs et fiscaux (avis d'imposition, contrats, bulletins de salaire), et la sauvegarde du gestionnaire de mots de passe et des codes de récupération MFA.

Les **codes de récupération** : à chaque activation de MFA, les imprimer ou les noter sur papier, et les stocker dans un lieu sûr (un tiroir à la maison, un coffre, chez un proche de confiance). Ne PAS les stocker uniquement dans le téléphone — c'est le téléphone qu'on perd. Ne PAS les stocker uniquement dans le cloud — c'est le cloud qui est inaccessible si le MFA bloque.

L'**email maître** : l'email principal est le compte le plus critique — c'est lui qui reçoit les réinitialisations de mot de passe de tous les autres comptes. Il doit avoir le mot de passe le plus fort (unique, long, stocké dans le gestionnaire), le MFA le plus robuste (application TOTP ou clé physique, PAS SMS), et un email de récupération secondaire qui n'est PAS le même email (un second email sur un fournisseur différent — si Gmail est compromis, l'email de récupération chez ProtonMail ou Outlook permet de reprendre le contrôle).

L'**appareil de secours** : avoir un second appareil (un vieux téléphone, une tablette) avec l'app du gestionnaire de mots de passe et les apps d'authentification MFA configurées. En cas de perte du téléphone principal, la reprise est immédiate — pas besoin d'attendre une nouvelle SIM ou de retrouver des codes de récupération.

---

<a id="chapitre-10"></a>
## Chapitre 10 — Construire sa continuité numérique personnelle

*Que se passe-t-il si votre téléphone disparaît demain matin ? Si vous ne pouvez pas répondre à cette question en 30 secondes, ce chapitre est pour vous.*

L'**effet domino** : perdre le téléphone = perdre l'accès au MFA = perdre l'accès à l'email = perdre l'accès à tous les comptes liés = perdre l'accès à la banque, au cloud, aux messageries, aux réseaux sociaux. Chaque compte dépend d'un autre. Si le premier maillon tombe, tout tombe. La continuité numérique consiste à casser cette chaîne de dépendance pour que la perte d'un maillon ne fasse PAS tout tomber.

L'**ordre de reprise** en cas de perte/vol du téléphone : (1) bloquer la carte SIM (appeler l'opérateur — noter le numéro de blocage SIM AVANT d'en avoir besoin), (2) localiser et verrouiller/effacer le téléphone à distance (Find My), (3) changer le mot de passe de l'email maître (depuis un autre appareil), (4) révoquer les sessions actives sur les comptes critiques, (5) changer les mots de passe des comptes sensibles, (6) prévenir la banque si l'app bancaire était sur le téléphone, (7) prévenir l'employeur si le téléphone avait des usages pro.

Les **comptes critiques** à prioriser : email maître, banque, gestionnaire de mots de passe, cloud (photos, documents), messageries principales. Les comptes secondaires (Netflix, Spotify, Vinted) peuvent attendre.

Le **kit de survie numérique** — à préparer maintenant, pas le jour du sinistre : les codes de récupération MFA imprimés dans un lieu sûr, le mot de passe du gestionnaire mémorisé (pas stocké uniquement dans le téléphone), un second appareil avec les apps critiques, le numéro de blocage de la SIM, les numéros d'opposition bancaire, et un email de récupération secondaire configuré.

> **🔵 Lina — Épisode 4 :** Lina perd son téléphone dans le métro à Lyon. Elle n'a pas configuré Find My iPhone. Elle n'a pas ses codes de récupération MFA. Son email principal a le MFA par SMS — et la SIM est dans le téléphone perdu. Résultat : 3 jours pour reprendre le contrôle de ses comptes, un stress considérable, et 2 abonnements frauduleux souscrits entre-temps avec son compte compromis. Le chapitre montre ce qu'elle aurait dû préparer — et ce qu'elle met en place après l'incident pour que ça ne se reproduise plus.

---

> ### 🟦 Réflexes — Fin de Partie II
>
> **À configurer une fois pour toutes** :
> - Code 6+ chiffres + biométrie sur le téléphone
> - Mises à jour automatiques sur tous les appareils
> - Find My / Find My Device activé
> - Chiffrement disque sur l'ordinateur (BitLocker / FileVault)
> - Gestionnaire de mots de passe avec mot de passe maître unique et mémorisé
> - MFA application TOTP (pas SMS) sur les 5 comptes critiques
> - Email de récupération secondaire chez un autre fournisseur
> - Verrouillage de portabilité activé chez l'opérateur (anti-SIM swap)
> - Code PIN sur la carte SIM
>
> **À éviter absolument** :
> - Le même mot de passe sur deux comptes
> - MFA par SMS pour la banque ou l'email maître
> - Codes de récupération stockés uniquement dans le téléphone
> - Cracks et logiciels piratés
> - Macros Office « activées » sans raison
>
> **À vérifier tous les 6 mois** :
> - Sessions actives sur les comptes critiques
> - Permissions des applications mobiles
> - Extensions de navigateur (supprimer celles inutilisées)
> - Have I Been Pwned (votre email apparaît-il dans une nouvelle fuite ?)
>
> **Si quelque chose arrive** :
> - Signaux SIM swap : perte soudaine de réseau → appeler l'opérateur depuis un autre téléphone
> - Notification MFA non sollicitée → REFUSER, changer le mot de passe immédiatement
> - Compte compromis : voir Ch.41

---
