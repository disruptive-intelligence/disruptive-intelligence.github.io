---
title: PARTIE IX — NAVIGATION PRATIQUE ET COLLECTE DÉFENSIVE ENCADRÉE
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 10
chapters: 10
---

> **Ce que cette partie apprend.** Naviguer concrètement avec Tor sur des ressources **légitimes**. Installation et configuration de Tor Browser, anatomie d'une adresse .onion v3, authentification de miroirs officiels (médias, institutions, lanceurs d'alerte), collecte structurée avec Hunchly, vérification défensive de l'exposition de son organisation dans les bases publiques de fuites de données.
>
> **Ce qu'elle ne couvre pas.** L'accès opérationnel aux forums criminels, marketplaces, leak sites ransomware ou canaux clandestins. Ces espaces ont été étudiés en Parties III et V sous l'angle analytique et CTI, mais leur consultation active relève d'un cadre professionnel autorisé, documenté et juridiquement encadré (Ch.22).
>
> **Ce que vous saurez faire après cette partie.** Installer Tor Browser correctement, accéder à des ressources .onion légitimes en vérifiant systématiquement leur authenticité, conduire une collecte documentée et reproductible, vérifier l'exposition de votre périmètre dans les bases de leaks, et produire une note de synthèse défensive utilisable.
>
> **Avertissement.** Les exemples de cette partie portent exclusivement sur des ressources légitimes, publiques, non criminelles. **Les adresses .onion citées peuvent évoluer** — l'opérateur peut les renouveler, les déplacer, voire fermer le service. Toute adresse mentionnée doit être **revérifiée** depuis le site officiel clearnet de l'organisation au moment de l'usage. Aucune adresse n'est une vérité permanente.
>
> **Cadre légal.** La consultation de ressources .onion légitimes est généralement licite dans les États démocratiques, sous réserve des lois locales applicables et des politiques internes de l'organisation de l'analyste. La simple consultation passive de certains espaces criminels peut ne pas constituer une infraction dans certaines juridictions, mais elle expose à des risques juridiques, techniques et déontologiques importants — elle ne doit être menée que dans un cadre professionnel autorisé, documenté et proportionné (Ch.22).

---

### Chapitre 45 — Premier accès à Tor : installation, sécurité et navigation légitime

Pour beaucoup d'analystes débutants, la première difficulté n'est pas conceptuelle mais **opérationnelle** — comment, concrètement, accéder proprement à une ressource .onion légitime, avec une posture de sécurité minimale. Ce chapitre est le premier TP guidé du cours. Il ne cherche pas à faire « explorer le dark web », mais à faire comprendre l'accès propre à des ressources légitimes.

#### 45.1 Installer Tor Browser depuis la source officielle

**Téléchargement**. **Source unique légitime** : `torproject.org`. Toute autre source (sites tiers, packages communautaires non officiels, miroirs douteux) doit être considérée comme suspecte. Tor Browser est précisément l'outil **le plus ciblé par malware piégé** parce que ses utilisateurs cherchent confidentialité et anonymat — un Tor Browser modifié peut journaliser tout le trafic ou contenir un backdoor sans que l'utilisateur le sache.

**Installation** :
- **Windows / macOS** : exécuter l'installeur, choisir un répertoire dédié.
- **Linux** : extraire l'archive, exécuter `start-tor-browser.desktop` ou le script `start-tor-browser`. Pas besoin de root.

#### 45.2 Vérifier l'authenticité du téléchargement

Le Tor Project signe ses binaires avec une clé GPG. Procédure :

1. Télécharger le binaire (`.exe` Windows, `.dmg` macOS, `.tar.xz` Linux).
2. Télécharger la **signature** correspondante (fichier `.asc` à côté du binaire).
3. Importer la clé publique du Tor Browser Developers : `gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org`.
4. Vérifier la signature : `gpg --verify tor-browser-linux64-XX.x_ALL.tar.xz.asc`.
5. Sortie attendue : `Good signature from "Tor Browser Developers (signing key) <torbrowser@torproject.org>"`.

Cette procédure prend 5 minutes et garantit que le binaire n'a pas été altéré entre le serveur du Tor Project et votre poste. Indispensable en contexte professionnel.

> **À retenir.** Un Tor Browser non vérifié est un risque majeur : l'utilisateur croit protéger son anonymat alors qu'il peut installer un navigateur modifié, journalisé ou malveillant.

#### 45.3 Premier lancement et vérification de connexion

**Premier lancement** :
- Tor Browser propose **« Connect »** ou **« Configure »**. Pour usage standard (hors censure), cliquer **Connect**.
- Connexion au réseau Tor : 5-30 secondes typiquement.
- Page d'accueil DuckDuckGo (par défaut) une fois connecté.

**Vérification de connexion**. Aller sur `https://check.torproject.org` — confirme que le trafic passe bien par le réseau Tor et affiche l'IP de sortie (du nœud exit, pas votre vraie IP). Cette page **ne prouve pas** que l'utilisateur est anonyme au sens absolu — elle confirme seulement que le trafic web passe par Tor.

#### 45.4 Configurer le mode Safest

Par défaut, Tor Browser opère en mode **Standard** — JavaScript activé, fonctionnalités web complètes. Pour l'investigation dark web, **passer en Safest** est essentiel.

**Procédure** :
1. Cliquer sur l'icône bouclier en haut à droite du navigateur.
2. Sélectionner **« Settings »** ou « Change ».
3. Choisir **« Safest »** parmi les trois niveaux :
   - **Standard** : tout activé (par défaut).
   - **Safer** : JavaScript désactivé sur sites HTTP (mais activé sur HTTPS), fonts/icônes affichés autrement.
   - **Safest** : JavaScript désactivé partout, beaucoup de fonctionnalités neutralisées.

**Conséquences du mode Safest** :
- Beaucoup de sites cassent ou affichent contenu réduit.
- Pas de vidéo embarquée (YouTube, Vimeo).
- CAPTCHA basés sur JS ne fonctionnent pas.
- Forums avec login JS difficiles d'accès.

**En investigation, le mode Safest doit être la configuration par défaut**. Les exceptions doivent être temporaires, justifiées et documentées. Le confort de navigation ne prime jamais sur la réduction de surface d'attaque. JavaScript désactivé est la principale protection contre les NIT et les exploits navigateur ciblant les utilisateurs Tor (Ch.30).

#### 45.5 Comprendre une adresse .onion v3

Une adresse .onion v3 a la forme :

`duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`

**Décomposition** :
- **56 caractères** avant `.onion` (toujours).
- Caractères : lettres minuscules `a-z` et chiffres `2-7` (encodage base32).
- L'adresse **est** la clé publique du service Tor + checksum + version.

**Génération**. L'opérateur du service génère une clé privée Ed25519. L'adresse est dérivée mathématiquement de la clé publique correspondante. Personne ne peut « créer » l'adresse `duckduckgogg42xjoc72...` sans posséder la clé privée correspondante — c'est une **garantie cryptographique d'authenticité**.

**Vanity addresses**. Un opérateur peut générer des millions de clés jusqu'à en trouver une dont l'adresse commence par un préfixe choisi (ex : `duckduckgo...`). Pour un préfixe court (4-6 caractères), trivial. Pour un préfixe long, demande des ressources GPU significatives.

**Erreur classique**. Vérifier seulement le **début** d'une adresse .onion est insuffisant. Deux adresses peuvent partager un préfixe crédible tout en pointant vers deux services totalement différents. Une adresse officielle se vérifie **caractère par caractère, en entier**.

**Ancien format v2** (déprécié 2021). Adresses de 16 caractères type `3g2upl4pq6kufc4m.onion`. **Plus supportées par Tor depuis octobre 2021**. Si vous trouvez une adresse v2, elle ne fonctionne plus — chercher la v3 actuelle.

#### 45.6 Premières destinations légitimes

> Les adresses suivantes sont des **exemples pédagogiques**. Avant un usage réel, l'analyste doit les confirmer depuis le site clearnet officiel de l'organisation ou via l'en-tête Onion-Location. Une adresse .onion peut être renouvelée par son opérateur sans préavis ; une adresse retrouvée dans un cours ou une liste statique peut donc être obsolète.

**DuckDuckGo** : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`. Moteur de recherche par défaut de Tor Browser. Permet de chercher sur le clearnet sans révéler à DuckDuckGo votre IP via Tor exit node.

**Tor Project** : `2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion`. Site officiel du Tor Project en miroir .onion. Documentation, téléchargements, news.

**BBC News** : `bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion`. Miroir .onion officiel de la BBC, lancé en 2019. Important pour les utilisateurs dans pays où BBC est censurée.

**The New York Times** : `www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion`. Miroir officiel.

**ProPublica** : `p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion`. Premier grand média US à avoir lancé un miroir .onion (2016).

**Deutsche Welle** : `dwnewsgngmhlplxy6o2twtfgjnrnjxbegbwqx6wnotdhkzt562tszfid.onion`. Service public allemand, multiples langues.

**Facebook** : `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion`. Miroir officiel Facebook depuis 2014. Vanity address commençant par `facebook`. Permet utilisation de Facebook en pays bloquants.

**Protonmail** : `protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion`. Messagerie chiffrée.

**Ahmia** (moteur de recherche .onion) : `juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion`. Maintenu par Juha Nurmi (Finlande), filtre anti-CSAM strict, projet open source documenté. Adresse vérifiable sur ahmia.fi (clearnet).

**Cas particuliers à traiter avec prudence** :

- **Wikipedia** ne maintient **pas** de miroir .onion officiel. Les miroirs disponibles communautairement ne sont pas garantis. Pour usage standard, accéder à Wikipedia clearnet via Tor Browser fait le job.
- **Le Monde** et plusieurs autres médias francophones ont eu, à certaines périodes, des miroirs .onion sans les maintenir durablement. La seule référence fiable est la page officielle clearnet de l'organisation à l'instant T.

#### 45.7 Sessions de découverte type — TPs progressifs

Pour un nouvel analyste, séquence d'apprentissage progressive sur ~6-8h cumulées.

**TP 1 — Installation et validation de Tor Browser** (1-2h) :
1. Téléchargement Tor Browser depuis torproject.org.
2. Vérification GPG du binaire.
3. Installation et lancement.
4. Connexion réseau Tor.
5. Navigation sur `check.torproject.org`.
6. Activation mode Safest.
7. Visite DuckDuckGo .onion.
8. Recherche sur DuckDuckGo onion d'un sujet courant.

**TP 2 — Navigation sur miroirs médias officiels** (2h) :
1. Visite BBC News .onion. Comparer avec bbc.com classique.
2. Visite NYT .onion. Lire un article.
3. Visite ProPublica .onion. Section investigations.
4. Notation des différences UX (latence, certains éléments cassés en Safest).

**TP 3 — Comparaison clearnet / onion** (1-2h) :
1. Visite Tor Project .onion (documentation).
2. Comparaison structure et contenu avec torproject.org clearnet.
3. Visite Facebook .onion (sans login si possible — mode Safest peut empêcher login).
4. Visite Protonmail .onion.

**TP 4 — Recherche encadrée via Ahmia et DuckDuckGo** (1-2h) :
- Visite Ahmia .onion. Recherches sur sujets techniques, médias, organisations légitimes.
- Comparaison avec recherches DuckDuckGo onion.
- Évaluation de la qualité des résultats.

**TP 5 — Découverte passive de SecureDrop** (1h) :
- Visite SecureDrop instances de médias **sans soumettre de contenu** :
  - NYT SecureDrop : sur le site NYT classique, lien vers .onion.
  - Guardian SecureDrop.
  - The Intercept.
- Comprendre comment ces services protègent les sources.

**Règle stricte pour ces TPs** : aucun téléchargement, aucune création de compte, aucune soumission de formulaire et aucune interaction avec un service sensible. Navigation et observation passives uniquement.

#### 45.8 Pièges du débutant

**Cliquer sur des liens « hidden wiki » sans vérification**. The Hidden Wiki et ses successeurs sont des listes communautaires d'adresses .onion. **Beaucoup de ces listes contiennent des liens vers du contenu illicite, des arnaques, ou des phishing pages d'apparence légitime**. Le débutant qui suit aveuglément un lien « .onion drogues » ou « .onion porn » s'expose à des risques juridiques et techniques.

**Recommandation** : ne suivre que des adresses .onion **publiquement référencées par leur opérateur officiel**. Si la BBC indique sur son site clearnet « notre adresse .onion est X », c'est fiable. Si une « hidden wiki » liste « BBC : Y », c'est suspect — vérifier d'abord X sur bbc.com.

Le premier réflexe de l'analyste débutant n'est pas « où trouver des liens ? », mais « comment vérifier que le lien que j'ai est authentique ? ».

**Activer JavaScript automatiquement**. Tentation forte quand un site casse en mode Safest. À éviter sauf nécessité absolue identifiée — beaucoup de NIT historiques exploitent JavaScript.

**Télécharger des fichiers**. Tout fichier téléchargé du dark web doit être traité comme **potentiellement malveillant**. Ouvrir uniquement en VM isolée, jamais sur le poste hôte.

**Logger avec ses comptes personnels**. Se connecter à son Gmail, Twitter, ou banque depuis Tor Browser n'est pas illégal mais expose à plusieurs risques (services qui détectent Tor et bloquent ; corrélation possible entre activité Tor et identité personnelle si erreur OPSEC). Pour analyste pro : machine d'investigation jamais utilisée pour comptes personnels.

**Confondre « lent » et « cassé »**. Tor est lent. Une page qui met 10 secondes à charger n'est pas forcément cassée — c'est normal. Patience.

#### 45.9 Vérifier sa propre exposition (premier aperçu)

Exercice utile pour terminer cette première session : vérifier votre propre exposition publique.

**Outils gratuits** :
- **Have I Been Pwned** (haveibeenpwned.com) : entrer son email, voir dans quels breaches publics il apparaît.
- **Firefox Monitor** : alerte continue.
- **DeHashed** (dehashed.com) : version commerciale plus complète.

Cette première vérification personnelle sert de démonstration. Le **Ch.48** formalise la méthode pour un usage défensif individuel ou organisationnel.

---

### Chapitre 46 — Authentifier un miroir officiel .onion

L'usurpation d'adresses .onion (typosquatting) est une menace réelle. Un faux miroir BBC peut imiter parfaitement le vrai, capturer les communications de visiteurs, ou injecter de la désinformation. Ce chapitre apprend une compétence très concrète : **ne jamais faire confiance à une adresse .onion simplement parce qu'elle « ressemble » à une adresse officielle**.

#### 46.1 Le risque du typosquatting .onion

Le typosquatting .onion exploite une faiblesse **humaine**, pas une faiblesse cryptographique : l'adresse est sûre cryptographiquement, mais l'utilisateur peut se tromper d'adresse.

**Le mécanisme**. Comme expliqué Ch.45, on peut générer des adresses commençant par un préfixe choisi via vanity address generation. Un attaquant peut créer une adresse `bbcnewsd73XXX...` (différente de l'adresse officielle BBC) qui présentera le même préfixe.

**Risques pour le visiteur** :
- **Contenu altéré** : faux miroir injecte désinformation, propagande, contenus modifiés.
- **Phishing** : faux miroir avec formulaire de login récupère credentials d'utilisateurs (rare pour médias, plus pertinent pour SecureDrop usurpé qui pourrait piéger des sources).
- **Exploits navigateur** : faux site héberge NIT pour identifier IPs réelles.
- **Tracking** : faux site ajoute beacons pour identifier visiteurs.

**Cas réels documentés** : multiples miroirs imitant SecureDrop, de fausses versions de Tor Project lui-même, des copies cosmétiques de marketplaces (qui scament les acheteurs).

#### 46.2 Identifier les sources d'autorité — par ordre de confiance

1. **Site clearnet officiel de l'organisation**. La méthode la plus fiable : trouver l'adresse .onion sur le site clearnet officiel.
2. **Header Onion-Location**. Les sites compatibles envoient un header HTTP `Onion-Location: <adresse.onion>` quand un visiteur arrive sur leur version clearnet. Tor Browser détecte ce header et propose une bannière « Cette page est disponible sur version .onion ». Garantie d'authenticité (le serveur officiel envoie l'info).
3. **Documentation officielle ou page d'aide** de l'organisation, mentionnant explicitement l'adresse.
4. **Répertoire officiel reconnu** — par exemple, **Freedom of the Press Foundation** (freedom.press) maintient une liste centralisée des SecureDrop déployés.
5. **Annuaire communautaire reconnu** (Tor.taxi, Dark.fail) — uniquement en complément, jamais comme source primaire.
6. **Hidden Wiki et listes anonymes** : non fiables comme source primaire.

**Recoupement multi-sources**. Pour confirmer une adresse .onion, exiger **au moins deux sources indépendantes** qui matchent — typiquement (1) + (2) ou (1) + (3) ou (1) + (4).

#### 46.3 Walkthrough : authentifier le miroir BBC

Exemple complet, étape par étape.

**Étape 1 — clearnet officiel**.
- Naviguer sur bbc.com (depuis Tor Browser ou tout navigateur).
- Chercher « onion » ou « Tor » dans la barre de recherche du site, ou Google « BBC .onion site ».
- Trouver l'article officiel BBC : « The BBC's .onion site explained ».
- Adresse mentionnée : `bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion`.

**Étape 2 — Onion-Location header**.
- Visiter bbc.com depuis Tor Browser.
- Observer la bannière « .onion available ». Cliquer pour redirect.
- Confirmer que l'adresse correspond à celle de l'étape 1.

**Étape 3 — comparaison caractère par caractère**.
- Bien aligner les deux adresses : `bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion`.
- Comparer chaque caractère. Pas seulement le préfixe. La fin (`uqd.onion`) doit aussi matcher.

**Étape 4 — première visite**.
- Coller l'adresse dans Tor Browser.
- Vérifier que la page charge correctement (logo BBC, structure familière).
- Pas d'avertissement de certificat (si HTTPS sur .onion, le certificat doit être valide).
- Naviguer quelques articles, comparer avec bbc.com (les contenus doivent être cohérents).

**Étape 5 — bookmark et documentation**.
- Sauvegarder l'adresse dans Tor Browser bookmarks.
- Documenter dans le carnet d'investigation l'adresse, la date de vérification, et la source d'autorité.

**Livrable attendu** : note courte indiquant adresse officielle trouvée, source clearnet utilisée, date de vérification, méthode de comparaison, conclusion d'authenticité.

#### 46.4 Walkthrough : authentifier un miroir SecureDrop

SecureDrop est plus sensible que BBC — destiné à des sources lanceurs d'alerte qui prennent des risques. L'authentification est cruciale.

**Le mécanisme officiel SecureDrop** :
- Chaque média qui déploie SecureDrop documente son adresse .onion sur **son site clearnet officiel**.
- L'adresse SecureDrop est différente du miroir « news » du média.
- La fondation **Freedom of the Press Foundation** (freedom.press) maintient une liste centralisée.

**Walkthrough — SecureDrop NYT**.
1. Aller sur nytimes.com.
2. Chercher « tips » ou « confidential tips » dans le menu.
3. Trouver la page « How to Tip the NYT » qui détaille les méthodes (post, encrypted email, Signal, SecureDrop).
4. Adresse SecureDrop NYT mentionnée explicitement.
5. Cross-check sur freedom.press/securedrop/directory : la NYT y est listée avec son adresse, qui doit matcher.
6. Si les deux sources concordent : adresse authentique.

**Précaution importante** : une instance SecureDrop ne se « teste pas » en envoyant un message factice. Un tel comportement pollue le canal de réception du média et peut déclencher une analyse inutile côté journalistes. La visite est strictement passive — observer la page d'accueil, capturer pour documentation, ne pas interagir.

#### 46.5 Détecter un faux miroir — trois familles de signaux

Méthodologie pour vérifier si une adresse suspecte est un faux miroir.

**Signaux d'adresse** :
- Adresse trouvée uniquement sur sources tierces (pas sur clearnet officiel).
- Préfixe similaire mais corps différent.
- Adresse trouvée seulement sur annuaire communautaire ou hidden wiki.
- Différence d'un ou deux caractères avec l'adresse officielle (typo intentionnelle).

**Signaux de contenu** :
- Design proche mais contenu daté ou divergent.
- Articles modifiés vs version clearnet.
- Liens externes suspects (boutons « download » qui pointent vers des fichiers .exe).
- Demandes de login inhabituelles pour un site qui n'en exige pas habituellement.
- Formulaires absents de la version clearnet.

**Signaux techniques** :
- Absence d'Onion-Location quand le site officiel en propose un.
- Scripts inhabituels (en mode Safest, JS bloqué donne des indices indirects).
- Redirections vers domaines non cohérents.
- Téléchargements proposés sans justification.
- Latence anormalement faible (peut indiquer hosting non-Tor traditionnel masqué).

**En cas de doute** :
- Ne pas continuer la navigation.
- Documenter l'adresse suspecte (capture, hash de la page).
- Signaler au CSIRT compétent (CERT-FR pour France) pour évaluation.
- Pour les médias : signaler à l'organisation usurpée.

#### 46.6 Le cas des moteurs de recherche .onion

Pour les exercices de cette partie, **seuls DuckDuckGo et Ahmia doivent être utilisés**. Les autres moteurs (Torch, Haystak, Tor66, Excavator) sont mentionnés pour culture générale, mais leur usage peut exposer à des résultats non maîtrisés, y compris illicites ou frauduleux.

- **Ahmia** : projet documenté, filtre CSAM strict, source d'autorité raisonnable. Adresse vérifiable sur ahmia.fi.
- **DuckDuckGo .onion** : indexe le clearnet via Tor exit, pas le contenu .onion. Moteur principal de Tor Browser par défaut.

Pour un analyste pro qui doit explorer du contenu .onion criminel dans le cadre d'une mission, l'élargissement aux autres moteurs est possible — mais relève alors du cadre Partie V, pas des exercices de cette partie.

#### 46.7 Tenir une liste de référence interne

Pour un programme d'investigation durable, **constituer et maintenir une liste interne** de miroirs .onion légitimes vérifiés.

**Format suggéré** :

| Organisation | Type | Adresse .onion (extrait) | Source officielle | Date vérification | Vérificateur | Statut |
|---|---|---|---|---|---|---|
| BBC | Média | bbcnewsd73...uqd.onion | bbc.com (article ref) | YYYY-MM-DD | Analyste | Actif |
| Tor Project | Institution | 2gzyxa5ihm7...wid.onion | torproject.org | YYYY-MM-DD | Analyste | Actif |
| ProPublica | Média | p53lf57qovy...uqd.onion | propublica.org | YYYY-MM-DD | Analyste | Actif |
| SecureDrop NYT | Lanceur d'alerte | (adresse complète) | nytimes.com tips + freedom.press | YYYY-MM-DD | Analyste | Actif |

**Règle** : une adresse non revérifiée depuis plusieurs mois ne doit pas être considérée comme fiable par défaut. Revue trimestrielle minimum.

**Partage** : cette liste peut être partagée avec d'autres équipes internes (formation, communications, juridique). Pour le partage externe (ISAC), nettoyer ce qui est sensible et publier en TLP CLEAR.

---

### Chapitre 47 — Collecter et documenter une source légitime avec Hunchly

Au-delà de la simple navigation, l'analyste documente. **Hunchly** est l'outil de référence pour la capture structurée d'investigation web (clearnet et .onion). Ce chapitre montre concrètement son usage sur une source légitime.

#### 47.1 Pourquoi documenter une session ?

Une page visitée sans capture, sans horodatage et sans hash est une **observation fragile**. L'analyste peut s'en souvenir, mais il ne pourra pas forcément la démontrer, la transmettre, ou la réutiliser dans un rapport.

Sans outil structuré, la capture d'une session de navigation produit :
- Des screenshots éparpillés sans nommage cohérent.
- Pas d'horodatage fiable.
- Pas de hash garantissant l'intégrité.
- Pas de capture de la source HTML.
- Pas de lien entre observations et investigation globale.

#### 47.2 Pourquoi Hunchly

Outil commercial développé par Justin Seitz (auteur de Bellingcat, OSINT). Extension Chrome/Firefox + application desktop. Capture **automatiquement** et **systématiquement** chaque page visitée pendant la session.

**Fonctions clés** :
- Capture HTML + screenshot + metadata pour chaque page visitée.
- Horodatage précis.
- Hashing automatique des contenus capturés.
- Annotations (selectors mode pour highlighter et noter).
- Cases d'investigation avec organisation.
- Export rapport structuré.

**Coût** : ~130 USD/an pour licence individuelle, options enterprise.

**Alternatives gratuites** : OSINT Cloner (open source, moins riche), captures manuelles structurées (chronophage).

#### 47.3 Installation et configuration

**Téléchargement** : hunch.ly. Compte requis pour licence.

**Installation** :
1. Application desktop (Windows, macOS, Linux). Installation classique.
2. Extension navigateur (Chrome, Firefox/Tor Browser). Activer.
3. Authentification de l'extension avec compte Hunchly.

**Configuration pour Tor Browser**.
- Hunchly fonctionne dans Firefox (Tor Browser est basé sur Firefox ESR).
- Installer l'extension Firefox dans Tor Browser.

**Note OPSEC** : installer une extension dans Tor Browser modifie le fingerprint du navigateur. Pour les exercices sur sources légitimes, ce risque est acceptable. Pour une investigation sensible (cible paranoïaque, OPSEC critique), l'architecture de collecte doit être validée par l'équipe, et l'outil de capture ne doit pas être improvisé — éventuellement, scripts custom hors Tor Browser pour ne pas modifier le fingerprint.

**Premier test** :
1. Lancer Hunchly desktop.
2. Créer un nouveau **case** : « Test_Premiere_Session ».
3. Activer la capture (toggle on).
4. Visiter quelques pages clearnet (n'importe quoi : Wikipedia, un blog).
5. Observer : Hunchly capture chaque page automatiquement.
6. Retour à l'application desktop : pages capturées listées avec horodatages, screenshots.

#### 47.4 Walkthrough : documenter SecureDrop NYT

Cas pratique : documenter le déploiement SecureDrop du New York Times pour une investigation sur l'écosystème journalisme protection sources.

**Setup**.
1. Tor Browser ouvert, mode Safest.
2. Hunchly extension activée.
3. Hunchly desktop : nouveau case « SecureDrop_Ecosystem_2026 ».
4. Activer la capture.

**Étape 1 — cadrage clearnet**.
- Visite nytimes.com.
- Navigation vers section « tips ».
- Page « How to Tip the NYT ».
- Hunchly capture chaque page automatiquement.
- Annotation : « Description officielle des canaux confidentiels par le NYT ».

**Étape 2 — vérification de l'adresse SecureDrop**.
- Sur la page tips, identification de l'adresse .onion SecureDrop NYT.
- Cross-check avec freedom.press/securedrop/directory.
- Visite freedom.press, vérification que l'adresse matche.
- Hunchly capture les deux pages.
- Annotation : « Cross-check freedom.press confirme l'adresse SecureDrop NYT ».

**Étape 3 — visite de l'adresse SecureDrop**.
- Coller l'adresse .onion dans Tor Browser.
- Page d'accueil SecureDrop : interface standard avec deux options (« Submit documents and messages » / « Check for replies »).
- Hunchly capture.
- Annotation : « Page d'accueil SecureDrop NYT, interface standard. Pas de soumission test. ».
- **NE PAS CLIQUER sur « Submit » ni interagir au-delà de la consultation passive**.

**Étape 4 — capture de la documentation SecureDrop**.
- Visite securedrop.org (clearnet) — projet officiel.
- Navigation dans documentation, FAQ.
- Hunchly capture.
- Section sur les déploiements actifs : capture de la liste.

**Étape 5 — autres déploiements similaires**.
- Visite Guardian SecureDrop (procédure identique).
- Visite ProPublica, The Intercept.
- Hunchly capture chaque session.

**Étape 6 — finalisation**.
- Désactivation de la capture.
- Dans Hunchly desktop : vérification que toutes les pages attendues sont capturées.
- Annotations finales sur le case.
- Export du case en PDF ou archive ZIP pour archivage long terme.

**Livrable attendu** :
- Page clearnet officielle documentant SecureDrop.
- Page Freedom of the Press Foundation confirmant l'adresse.
- Page .onion SecureDrop capturée.
- Annotations expliquant la méthode.
- Export Hunchly horodaté.
- Conclusion : miroir authentifié / non authentifié.

#### 47.5 Documenter une page institutionnelle

Variante : documenter le site officiel d'une institution avec son miroir .onion.

**Cas — Tor Project** :
- Visite torproject.org (clearnet).
- Visite Tor Project .onion.
- Comparaison des deux versions : contenu identique, structure identique.
- Hunchly capture les deux versions de chaque page.
- Documentation de la cohérence : la version .onion est un miroir authentique, pas une version modifiée.

Cet exercice est particulièrement utile en sensibilisation interne : il montre à des profils non techniques qu'un service .onion peut être institutionnel, légitime et défensif.

#### 47.6 Bonnes pratiques de collecte

**Avant la session** :
- Définir l'**objectif** de la collecte (qu'est-ce qu'on cherche à documenter ?).
- Préparer le **case Hunchly** avec nom explicite.
- S'assurer que la connexion Tor est fonctionnelle.
- Lister les URLs à visiter (planification).
- Vérifier que le mode Safest est actif.
- Validation hiérarchique si exercice non-routinier.

**Pendant la session** :
- **Capture activée** dès le début, désactivée seulement à la fin.
- **Annotations en temps réel** : ne pas attendre la fin pour documenter ses observations.
- Pas de téléchargement.
- Pas de soumission de formulaire.
- Pas d'activation JS sauf justification documentée.
- Pas de manipulation de fichiers téléchargés sans VM isolée séparée.

**Après la session** :
- **Revue des captures** : vérifier qu'aucune page critique n'a été oubliée.
- **Annotations finales** : synthèse, conclusions, hypothèses.
- **Export** : générer rapport ou archive pour conservation long terme.
- **Sauvegarde** : stockage immutable (Ch.28).
- **Mise à jour graphe d'investigation** : ajouter entités observées, relations.
- **Mise à jour de la base interne** (liste de référence Ch.46.7).

#### 47.7 Limites et alternatives

**Limites Hunchly** :
- Coût (130 USD/an).
- Tier modeste — pour entreprises grandes, options plus puissantes (commerciales).
- Ne capture pas les flux dynamiques complexes (vidéos, APIs).
- Ne fonctionne pas en CLI (pour automatisation lourde).

**Alternatives partielles** :
- **OSINT Cloner** : extension navigateur open source, moins riche.
- **Wayback Machine** (archive.org) : pour clearnet uniquement, ne capture pas .onion.
- **archive.today** : alternative avec différentes couvertures.
- **Scripts custom** : Python avec Selenium ou Playwright + capture HTML, screenshots, hashing. Pour automatisation de masse.
- **Capture manuelle** : screenshots OS + sauvegarde HTML « Save Page As » + hash en CLI. Chronophage mais zéro coût.

**Important** : Hunchly ne remplace pas une vraie chaîne de conservation de preuve lorsqu'un dossier doit être exploité judiciairement. Il facilite la documentation, mais le niveau probatoire dépend aussi du contexte, de la procédure interne, du stockage, de la signature et de l'horodatage qualifié (Ch.28).

---

### Chapitre 48 — Vérification défensive de l'exposition dans les bases de leaks publiques

Au-delà du dark web .onion, la **veille des data leaks publiques** est un aspect essentiel de la pratique défensive. Plusieurs services indexent les breaches publics et permettent à une organisation de vérifier son exposition. Ce chapitre couvre les outils, méthodes, et limites — strictement défensifs.

#### 48.1 Comprendre les bases de leaks publiques

**Have I Been Pwned (HIBP)** — haveibeenpwned.com. Maintenu par Troy Hunt depuis 2013. La référence absolue. Indexe les breaches publiquement connus, déduplique, expose via interface web et API. Gratuit pour usage standard, API payante pour usage volumétrique.

Caractéristiques :
- ~13 milliards de comptes indexés (cumul historique).
- ~700+ breaches répertoriés.
- Recherche email simple : entre l'email, voit les breaches où il apparaît.
- Recherche password (« Pwned Passwords ») : vérifier si un mot de passe spécifique apparaît dans un breach.
- **Domain search** : pour propriétaires de domaines vérifiés, voir tous les emails du domaine compromis.

**DeHashed** — dehashed.com. Plateforme commerciale qui va plus loin que HIBP — indexe données complètes (pas seulement emails), permet recherches par username, IP, téléphone, nom, etc. Inclut breaches qu'HIBP ne couvre pas. Coût : ~5-15 USD/mois individuel, plus pour entreprises.

**LeakCheck.io** — leakcheck.io. Concurrent DeHashed, accès commercial.

**Snusbase** — snusbase.com. Autre alternative payante.

**IntelX** — intelx.io. Plateforme plus large : leaks, .onion archives, pastebin, deep web. Tier gratuit limité.

**Limite importante** : ces services ne donnent pas une vision **exhaustive** de l'exposition réelle. Ils donnent une vision partielle, utile pour prioriser des actions défensives, mais ils ne remplacent ni une investigation complète ni un programme CTI structuré. Faux négatifs possibles : votre exposition réelle peut être plus large que ce qui apparaît.

#### 48.2 Limites juridiques et RGPD

Avant les walkthroughs avancés, cadrer le périmètre.

**Principes** :
- **Base légale** : recherche sur sa propre identité ou sur le périmètre de son organisation = base légale solide (intérêt légitime, sécurité). Recherche sur tiers = nécessite mandat client, autorité légale, ou autre base précise.
- **Minimisation** : ne télécharger que ce qui est nécessaire à l'investigation.
- **Durée de conservation** : limitée, suppression après usage.
- **Habilitation** : seul personnel autorisé accède aux données collectées.
- **Journalisation des recherches** : tracer qui cherche quoi pour audit.
- **Non-prolifération** : ne pas rediffuser les données récupérées.
- **Suppression** : politique formalisée post-investigation.

**Cadre juridique français/européen** :
- **RGPD** : traitement de données personnelles encadré, même si données déjà publiquement exposées.
- **Code pénal article 226-18** : traitement de données à caractère personnel par moyens frauduleux.
- **Articles 226-1 et suivants** : atteinte à la vie privée.

Un analyste qui dériverait dans des usages offensifs (recherche sur tiers sans mandat, préparation cred stuffing, doxing) s'expose à sanctions disciplinaires, civiles, et pénales. Le cadre **professionnel défensif** est strict.

#### 48.3 Vérification individuelle

**Vérifier votre propre adresse email** :
1. Aller sur haveibeenpwned.com.
2. Entrer votre email pro et perso.
3. Voir la liste des breaches où l'email apparaît.

**Interprétation** :
- Plusieurs breaches : statistique pour utilisateur internet actif (LinkedIn 2012, Adobe 2013, Collection #1 2019).
- Breaches récents : préoccupant — réinitialiser mot de passe sur services concernés, activer MFA.
- Breach mentionnant « passwords cracked » : votre mot de passe a été exposé en clair → ne plus le réutiliser, MFA prioritaire.

L'objectif n'est pas de paniquer à chaque apparition d'un email dans un breach ancien. L'objectif est de **vérifier les réutilisations de mots de passe**, **activer le MFA** et **comprendre quels comptes restent exposés**.

**Vérifier vos mots de passe**. HIBP « Pwned Passwords » permet de tester un mot de passe (sans l'envoyer en clair grâce à k-anonymity — vous envoyez seulement les 5 premiers caractères du hash SHA-1, le service renvoie tous les hashes commençant par ces 5 caractères, vous comparez localement).

**Activer le monitoring**. HIBP propose des alertes — entrer son email, recevoir un email à chaque nouveau breach contenant cet email. Gratuit. Bonne pratique pour tout utilisateur.

#### 48.4 Vérification organisationnelle avec HIBP Domain Search

Pour les propriétaires de domaines vérifiés, HIBP expose tous les emails compromis du domaine.

**Vérification de propriété** :
1. Aller sur haveibeenpwned.com/DomainSearch.
2. Entrer le domaine (ex : `vectris-aerospace.eu`).
3. HIBP demande de prouver la propriété — plusieurs méthodes :
   - Email à un compte privilégié du domaine (postmaster@, security@, etc.).
   - DNS TXT record.
   - Meta tag sur le site web.
   - Upload d'un fichier sur le site web.
4. Une fois vérifié, accès aux résultats.

**Résultats** : liste de tous les emails du domaine apparaissant dans des breaches, breaches concernés, dates, statistiques.

**Distinction de criticité** :
- **Email exposé dans un breach ancien grand public** : criticité faible à moyenne.
- **Mot de passe en clair ou hash faible associé à email professionnel** : criticité élevée.
- **Log infostealer récent avec cookie ou accès VPN** : criticité critique.
- **Accès corporate vendu par IAB** : urgence sécurité.

**Action défensive** :
- **Reset mots de passe** des emails concernés (en supposant le mot de passe utilisé sur le service breach a été ou pourrait être réutilisé en interne).
- **Vérifier réutilisation** : si l'email pro a été compromis dans LinkedIn 2012 avec un mot de passe, ce mot de passe est-il toujours utilisé en interne ?
- **MFA partout** : breach + réutilisation = compromission ; MFA résistant phishing protège.
- **Sensibilisation** : informer les employés concernés, les inviter à vérifier leurs propres comptes personnels.

#### 48.5 Recherche granulaire avec DeHashed / LeakCheck

Pour aller au-delà de HIBP (qui ne donne que les breaches concernés, pas les données), les plateformes commerciales permettent recherches granulaires.

**DeHashed walkthrough** :
1. Compte créé sur dehashed.com (vérification email).
2. Souscription mensuel ($5-15 selon tier).
3. Interface de recherche : champs email, username, IP, téléphone, nom, hash, password (pour reverse lookup d'un mot de passe vers comptes l'ayant utilisé).

**Recherches utiles pour défense** :
- **Email professionnel** : voir non seulement les breaches mais le contenu (mot de passe en clair, hash, infos additionnelles).
- **Username** : vérifier si un username utilisé en pro apparaît ailleurs (réutilisation = pivot pour attaquants).
- **IP de l'organisation** : breaches de fournisseurs SaaS contenant log entries depuis IPs Vectris peuvent indiquer compromission de partenaire.

Une recherche granulaire sur des personnes identifiables doit être limitée au **périmètre autorisé**. Même si l'outil permet techniquement de chercher n'importe qui, l'analyste ne doit rechercher que les identités, domaines ou actifs couverts par sa mission.

#### 48.6 Veille active vs ponctuelle

**Vérification ponctuelle** : à l'embauche d'un nouveau RSSI, lors d'un audit, après un incident.

**Veille active** : monitoring continu, alerting en temps réel.

**Outils de veille active** :
- **HIBP** alerts automatiques (gratuit, par email).
- **DeHashed** monitoring (commercial).
- **Plateformes CTI** intégrées (SOCRadar, Flare, Recorded Future) — incluent monitoring data leak avec attribution sectorielle.

**Pour une organisation** : combinaison recommandée :
- HIBP Domain Monitoring pour exposition large.
- Une plateforme commerciale (Flare, SOCRadar) pour monitoring multi-source.
- Procédure de réaction documentée à chaque alerte (qui investigue, qui notifie, qui escalade).

#### 48.7 Workflow d'alerte data leak — matrice opérationnelle

Cas pratique : votre plateforme CTI alerte qu'un email cadre Vectris apparaît dans un nouveau breach.

**Étape 1 — qualification (15 min)** :
- Quel est le breach concerné ?
- Date de la compromission, type de données exposées.
- Source du leak (publication publique, vente sur dark web, leak interne).
- Email du cadre concerné, position, criticité du compte.

**Étape 2 — investigation profonde (1-2h)** :
- Recherche complète sur DeHashed/HIBP : autres comptes du cadre exposés ?
- Vérifier sur Russian Market / autres marchés logs : credentials récents disponibles ?
- Vérifier le poste du cadre : signe de compromission via stealer ?
- Vérifier les services associés au compte breach : mot de passe réutilisé en interne ?

**Matrice de criticité et action** :

| Signal détecté | Criticité | Action |
|---|---|---|
| Email pro dans breach ancien sans mot de passe clair | Faible | Information utilisateur, vérification MFA |
| Email pro + mot de passe en clair | Élevée | Reset, révocation sessions, contrôle réutilisation |
| Log infostealer récent | **Critique** | Isolation poste, reset global, révocation tokens, hunting |
| Accès VPN/RDP vendu par IAB | **Critique** | IR immédiat, vérification logs, notification RSSI/autorités |
| Dump entreprise annoncé | **Critique** | Cellule de crise, authentification, juridique, communication |

**Étapes complémentaires** (selon criticité) :
- **Communication** : si impact business significatif → remontée RSSI puis direction. Si données personnelles compromises → évaluation notification CNIL (RGPD art. 33-34). Si OIV → remontée ANSSI selon procédure.
- **Audit** : poste du cadre, autres cadres du même périmètre (effet de cluster).
- **Documentation** : CRM CTI, IoC SIEM si pertinents.

#### 48.8 Valeur des données et priorisation

Pour calibrer la valeur d'un leak observé sur dark web, ordres de grandeur indicatifs (cf Ch.14 pour grille complète).

| Type | Source primaire | Prix dark web (indicatif) | Valeur défensive |
|---|---|---|---|
| Combo lists générales | Breaches mass-cumulés | 5-50 USD pour millions | Vérifier reuse via HIBP |
| Logs infostealer corporate | Russian Market | 50-500 USD/log | **Critique** — accès direct possible |
| Fullz US | BriansClub | 10-70 USD/identité | Prévention fraude |
| Dossier médical US | Marchés santé | 50-250 USD | Compliance HIPAA, fraude assurance |
| Base données enterprise | Forums/IndustrialLeaks | 500-100 000 USD+ | Selon sensibilité |
| Données R&D / IP | Niche | 1 000-100 000 USD+ | Compliance export, IP protection |

Le prix dark web ne mesure pas seulement la gravité pour la victime. Il mesure surtout la **valeur marchande perçue par les criminels**. Une donnée peu chère peut néanmoins être critique pour une organisation donnée — un employé exposé dans un combo list à 5 USD peut être le maillon faible d'une compromission majeure.

#### 48.9 Manipuler des données de fuite sans devenir un facteur de risque

Un analyste qui manipule des leak data — même publiquement disponibles — opère dans un cadre éthique strict.

**Principes opérationnels** :
- **Minimisation** : ne télécharger que ce qui est nécessaire à l'investigation.
- **Sécurisation** : stocker chiffré, accès limité.
- **Limitation temporelle** : suppression après usage.
- **Non-prolifération** : ne pas rediffuser.
- **Respect des victimes** : les données représentent des personnes réelles.
- **Non-exploitation curieuse** : ne pas explorer un dump par curiosité, seulement pour mission.
- **Coopération autorités** : si découverte d'infractions graves, signalement.

**Cas litigieux** :
- Découverte d'un breach non publiquement annoncé : qu'en faire ? Notification responsible disclosure à la victime, signalement éventuel CNIL/ANSSI, pas de publication unilatérale.
- Données contenant CSAM : **arrêt immédiat**, non-conservation, signalement Pharos / autorités compétentes.
- Données politiquement sensibles : neutralité analytique, pas d'exploitation idéologique.

Le cadre professionnel impose une discipline éthique que l'analyste maintient au-delà des règles strictes — c'est ce qui le distingue des acteurs malveillants partageant les mêmes accès techniques.

#### 48.10 Synthèse pour l'analyste

**Outils essentiels gratuits** :
- HIBP : exposition individuelle et organisationnelle.
- HIBP Pwned Passwords : hygiène mots de passe.

**Outils complémentaires commerciaux (selon budget)** :
- DeHashed / LeakCheck : recherches granulaires.
- IntelX : leaks plus larges incluant .onion archives.
- Plateforme CTI complète (Recorded Future, Flare, SOCRadar) : monitoring continu sectoriel.

**Procédures à formaliser** :
- Vérification périodique de l'exposition organisationnelle.
- Réaction structurée aux alertes data leak.
- Communication avec employés concernés.
- Coordination IR + CTI + communication + juridique.

Pour beaucoup d'organisations, **la surveillance des leaks publics et des logs d'infostealers est le premier niveau réaliste de CTI défensive** : peu coûteux, rapidement déployable, et directement relié à des actions de sécurité concrètes. Pour une organisation moyenne, c'est souvent le **premier programme** de veille à mettre en place — bénéfice/coût excellent.

---

### Exercice final de la Partie IX — Mini-investigation défensive légitime

**Objectif**. Réaliser une collecte complète, légitime et documentée sur une ressource .onion officielle. Mobilise les compétences des Ch.45-48 en une démarche cohérente.

**Scénario**. Vous êtes analyste CTI junior. Votre responsable vous demande de documenter l'existence d'un miroir .onion officiel d'un média ou d'une institution, de vérifier son authenticité, puis de produire une note courte expliquant votre méthode.

**Étapes attendues** :

1. **Choisir une ressource légitime** : BBC, ProPublica, Tor Project, Deutsche Welle, ou autre média/institution mentionné en Ch.45.6.
2. **Trouver l'adresse .onion** depuis le site clearnet officiel.
3. **Vérifier si un header Onion-Location** est présent quand vous visitez le site clearnet via Tor Browser.
4. **Comparer l'adresse complète** avec la source officielle (caractère par caractère).
5. **Visiter le miroir .onion** avec Tor Browser en mode Safest.
6. **Capturer la page** avec Hunchly ou, à défaut, capture manuelle + sauvegarde HTML.
7. **Calculer le hash SHA-256** des fichiers collectés.
8. **Rédiger une note courte** (template ci-dessous).

**Livrable attendu** :

```markdown
# Note courte — Authentification d'un miroir .onion légitime

## Ressource étudiée
[Nom de l'organisation]

## Adresse clearnet officielle
[URL]

## Adresse .onion vérifiée
[Adresse complète, 56 caractères + .onion]

## Méthode de vérification
- Source officielle consultée :
- Header Onion-Location observé : oui/non
- Recoupement secondaire :
- Date et heure de vérification :

## Collecte
- Outil utilisé :
- Captures réalisées :
- Hash SHA-256 :

## Conclusion
[Adresse authentifiée / non authentifiée / incertaine]

## Limites
[Éléments non vérifiés, incertitudes, date de validité de la vérification]
```

**Critères d'évaluation** :
- Méthode reproductible par un autre analyste sans contact avec vous.
- Adresse vérifiée sur **au moins deux sources d'autorité indépendantes**.
- Captures horodatées et hashées.
- Note synthétique, factuelle, calibrée.
- Limites explicitement documentées.

Cet exercice transforme les chapitres 45-48 en **compétence mesurable**. Il sert aussi de référence interne — l'analyste qui le réussit produit son premier livrable structuré, réutilisable comme template pour ses missions futures.

## ANNEXES

---

### Annexe A — Glossaire

| Terme | Définition |
|---|---|
| **0-day (zero-day)** | Vulnérabilité non publiquement connue et non patchée par l'éditeur |
| **AiTM** | Adversary-in-the-Middle — phishing interceptant credentials et cookies de session |
| **APT** | Advanced Persistent Threat — acteur étatique sophistiqué et persistant |
| **BEC** | Business Email Compromise — fraude par compromission d'email professionnel |
| **Bulletproof hosting** | Hébergement résilient aux saisies, dans juridictions peu coopératives |
| **CaaS** | Crime-as-a-Service — services criminels en abonnement |
| **CSAM** | Child Sexual Abuse Material — contenu d'abus sexuel d'enfants |
| **Carding** | Fraude à la carte bancaire |
| **Chain of custody** | Traçabilité d'une preuve depuis collecte jusqu'à exploitation |
| **Clearnet** | Internet de surface accessible via navigateurs classiques |
| **CTI** | Cyber Threat Intelligence — renseignement sur les cybermenaces |
| **DDoS** | Distributed Denial of Service — attaque par déni de service distribué |
| **Deep web** | Contenu web non indexé par moteurs de recherche généralistes |
| **Dark web** | Sous-ensemble du deep web accessible via darknets (Tor, I2P, etc.) |
| **Darknet** | Réseau overlay conçu pour l'anonymat (Tor, I2P, Freenet) |
| **DLT** | Distributed Ledger Technology — technologies de registre distribué (incluant blockchains) |
| **Doxing** | Publication d'informations personnelles d'une cible |
| **DPI** | Deep Packet Inspection — inspection en profondeur du trafic réseau |
| **Dwell time** | Temps entre compromission initiale et détection |
| **EDR** | Endpoint Detection and Response — outil de détection sur poste de travail |
| **Eepsite** | Site hébergé sur le réseau I2P (.i2p) |
| **Escrow** | Tiers de confiance détenant fonds entre acheteur et vendeur |
| **Exit node** | Dernier nœud d'un circuit Tor, qui parle au site de destination |
| **Exit scam** | Disparition des opérateurs avec les fonds en escrow |
| **Fullz** | Identité complète volée (nom, SSN, adresse, etc.) |
| **FUD** | Fully Undetected — malware indétectable par antivirus |
| **Garlic routing** | Routage anonyme utilisé par I2P (variante de l'onion routing) |
| **Guard relay** | Premier nœud d'un circuit Tor (côté client) |
| **Hidden service** | Service .onion, accessible uniquement via Tor |
| **Hacktivisme** | Activisme cyber motivé idéologiquement |
| **IAB** | Initial Access Broker — courtier vendant des accès compromis |
| **IoC** | Indicator of Compromise — artefact technique d'une compromission |
| **ISAC** | Information Sharing and Analysis Center — centre de partage sectoriel |
| **JID** | Jabber ID — identifiant utilisateur sur réseau XMPP |
| **KYC** | Know Your Customer — vérification d'identité client |
| **Leak site** | Vitrine publique d'un groupe ransomware (revendications, échantillons) |
| **LotL** | Living off the Land — usage d'outils légitimes pour furtivité |
| **MaaS** | Malware-as-a-Service — location de malware |
| **MFA** | Multi-Factor Authentication |
| **NIT** | Network Investigative Technique — technique policière d'identification |
| **NIS 2** | Directive UE 2022/2555 sur la cybersécurité |
| **OIV** | Opérateur d'Importance Vitale (France) |
| **OFAC** | Office of Foreign Assets Control (US) — sanctions économiques |
| **Onion routing** | Protocole de routage anonyme par chiffrement en couches (utilisé par Tor) |
| **OPSEC** | Operations Security — sécurité opérationnelle |
| **OSINT** | Open Source Intelligence — renseignement de source ouverte |
| **PASSI** | Prestataire d'Audit SSI qualifié ANSSI |
| **PDIS** | Prestataire de Détection d'Incidents de Sécurité ANSSI |
| **PRIS** | Prestataire de Réponse aux Incidents de Sécurité ANSSI |
| **PGP** | Pretty Good Privacy — standard de chiffrement et signature |
| **PhaaS** | Phishing-as-a-Service |
| **PSO** | Private Sector Offensive — fournisseur commercial d'outils offensifs (NSO, etc.) |
| **RaaS** | Ransomware-as-a-Service |
| **RAT** | Remote Access Trojan — cheval de Troie d'accès à distance |
| **RGPD** | Règlement Général sur la Protection des Données (UE) |
| **SCAM** | Arnaque |
| **Stealer (infostealer)** | Malware spécialisé dans le vol de données de session |
| **Stealer log** | Output d'un infostealer — données extraites d'une victime |
| **STIX/TAXII** | Standards d'échange de threat intelligence |
| **Sock puppet** | Faux compte créé pour simuler activité ou influence |
| **SSO** | Single Sign-On — authentification unifiée |
| **TLP** | Traffic Light Protocol — classification de partage (RED/AMBER/GREEN/CLEAR) |
| **TOX** | Protocole de messagerie peer-to-peer chiffré |
| **TTP** | Tactics, Techniques, and Procedures |
| **VM** | Virtual Machine — machine virtuelle |
| **Vouching** | Parrainage d'un nouveau membre par un membre établi |
| **WEP** | Words of Estimative Probability — vocabulaire calibré de probabilité |
| **XMPP / Jabber** | Protocole de messagerie ouvert et chiffrable |

---

### Annexe B — Typologie des espaces dark web

#### B.1 Forums

| Type | Exemples | Caractéristiques principales |
|---|---|---|
| Généralistes cybercrime russophone | XSS Forum, Exploit.in | Vouching strict, vétérans, tout type d'activité |
| Généralistes cybercrime anglophone | BreachForums (multiple instances) | Plus accessible, vente de données dominante |
| Spécialisés carding | BriansClub, WWH Club | Fraude bancaire, dumps |
| Spécialisés données | IndustrialLeaks (fictif), BreachForums (data leaks section) | Vente de breaches, accès |
| Hacktivisme | Variés selon causes | Coordination idéologique, revendications |
| Géographiques | Forums chinois, persophones, arabophones | Barrière linguistique, communautés régionales |

#### B.2 Marchés

| Type | Exemples actuels (2025-2026) | Spécialités |
|---|---|---|
| Généralistes | Abacus, TorZon, MGM Grand | Drogues + digital goods |
| Russophones post-Hydra | BlackSprut, OMG!OMG!, Mega, Kraken | Drogues, dead drops, bloc russophone |
| Logs | Russian Market | Stealer logs avec recherche par domaine |
| Fraude | BriansClub, WWH Club | Cartes, comptes bancaires |
| Spécialisés malware | Variés sur forums | Crypters, loaders, RAT |

#### B.3 Leak sites ransomware

| Famille | Statut 2025-2026 |
|---|---|
| LockBit | Affecté Cronos février 2024, relaunch fragile |
| ALPHV / BlackCat | Disparu mars 2024 (exit scam suspecté post-Change Healthcare) |
| Black Basta | Actif, ciblage enterprise large |
| Cl0p | Actif, exploitation edge devices (MOVEit, Oracle EBS) |
| Play / PlayCrypt | Actif depuis 2022 |
| Akira | Émergent fin 2023, croissance rapide |
| RansomHub | Émergent mi-2024, croissance forte |
| Qilin | Actif, Synnovis/NHS notamment |
| BianLian | Extorsion sans chiffrement depuis 2023 |
| Medusa, 8Base, Hunters Intl, Inc Ransom, Dragonforce, Rhysida, Brain Cipher | Actifs, à surveiller |

#### B.4 Messageries

| Plateforme | Usage typique |
|---|---|
| Telegram | Coordination, canaux publics, leaks. Durci post-Durov 2024 |
| XMPP / Jabber | Russophone classique, OTR/OMEMO, persistance |
| TOX | Peer-to-peer, communications très sensibles |
| Matrix / Element | Fédéré, en croissance post-Durov |
| Session | Sur Lokinet, anonymat strong, croissance |
| Signal | Activistes, journalistes ; moins cybercrime sophistiqué |

#### B.5 Sites légitimes en .onion

| Catégorie | Exemples |
|---|---|
| Médias | BBC, NYT, ProPublica, Le Monde, WaPo, Der Spiegel |
| Recherche | DuckDuckGo, Wikipedia (miroir) |
| ONG | Amnesty International, Reporters Sans Frontières |
| Plateformes | Facebook, Twitter (historique), Protonmail |
| Lanceurs d'alerte | SecureDrop instances (NYT, Guardian, etc.), GlobaLeaks |
| Communauté | Tor Project miroirs, Ahmia, archives forum |

---

### Annexe C — OPSEC analyste : checklists

#### C.1 Préparation environnement (avant première session)

- [ ] **Machine dédiée** : ordinateur séparé de l'usage personnel et professionnel courant.
- [ ] **OS dédié** : Whonix (Gateway + Workstation), Tails, ou Qubes OS. Pas Windows / macOS personnel.
- [ ] **Réseau isolé** : connexion Internet séparée si possible (clé 4G dédiée, ou réseau invité, pas réseau corporate principal).
- [ ] **Tor Browser configuré** : mode Safest activé par défaut, vérification version à jour.
- [ ] **VM de manipulation** : VM jetable pour ouvrir échantillons (Windows 10 sandbox, ou Linux jetable).
- [ ] **Outils installés** : Hunchly ou équivalent capture, exiftool, hash utilities, scripts custom.
- [ ] **Pas de comptes personnels** sur la machine (mail perso, RS, banque — interdit).

#### C.2 Préparation persona

- [ ] **Pseudonyme unique** non lié à l'analyste ou ses identités antérieures.
- [ ] **Histoire crédible** : background fictif documenté (origine, métier, intérêts).
- [ ] **Style linguistique cohérent** avec l'origine prétendue.
- [ ] **Email jetable** sur service approprié (protonmail, autre).
- [ ] **Compte sur forum cible** : créé avec délai progressif d'activité, pas immédiat.
- [ ] **PGP key dédiée** à la persona, pas réutilisée d'ailleurs.
- [ ] **JID XMPP** dédié sur serveur approprié.
- [ ] **Maintenance** : posts occasionnels même hors investigation pour crédibilité.

#### C.3 Pendant chaque session

- [ ] **Vérification Tor Browser à jour** avant lancement.
- [ ] **Mode Safest confirmé** (icône bouclier).
- [ ] **Capture systématique** activée (Hunchly).
- [ ] **Notes en temps réel** : URL visitées, observations, hypothèses.
- [ ] **Pas de comptes personnels** ouverts en parallèle.
- [ ] **Aucun téléchargement direct** sur OS hôte — toujours en VM isolée.
- [ ] **Vérification adresse .onion** sur 2 sources avant accès à un service inconnu.
- [ ] **Pas de JS activé sauf nécessité absolue** identifiée.
- [ ] **Logs OTR/OMEMO** des sessions XMPP archivés.

#### C.4 Post-session

- [ ] **Capture finale** complète (Hunchly export, ou archives manuelles).
- [ ] **Hashing** des fichiers téléchargés (SHA-256 minimum).
- [ ] **Documentation chronologique** dans le journal d'investigation.
- [ ] **Pas de copie hors environnement sécurisé** des données collectées.
- [ ] **Snapshot VM** restauré si modifications.
- [ ] **Mise à jour du graphe d'investigation** (entités, relations).

#### C.5 Communication équipe

- [ ] **Validation hiérarchie** pour actions sensibles (contact vendeur, paiement, téléchargement).
- [ ] **Briefing pair** sur évolutions importantes.
- [ ] **Coordination autorités** maintenue selon mandat.
- [ ] **Confidentialité** stricte — pas de partage avec tiers non habilités.
- [ ] **Debriefing psychologique** disponible si exposition à contenus difficiles.

#### C.6 Signaux d'alerte (compromission persona)

- [ ] **Pseudo identifié** par cibles (contre-investigation, mention « cet acteur est suspect »).
- [ ] **Comportements de contact étranges** (over-cooperation soudaine, demandes inhabituelles).
- [ ] **Tentatives techniques** (envoi de fichiers piégés évidents, liens suspects).
- [ ] **Mentions du nom réel** ou organisation dans communications.
- [ ] **Patterns de surveillance** observés.

→ En cas de signal, **abandonner la persona immédiatement**, ne pas chercher à la « sauver », escalade hiérarchique, debriefing.

---

### Annexe D — Outils d'investigation dark web

#### D.1 Environnements et navigateurs

| Outil | Usage | Coût |
|---|---|---|
| **Tor Browser** | Navigation .onion (référence) | Gratuit, open source |
| **Tails** | Distribution Linux live (USB) | Gratuit, open source |
| **Whonix** | Architecture VM Gateway+Workstation | Gratuit, open source |
| **Qubes OS** | OS isolation par VM | Gratuit, open source |
| **VirtualBox / VMware** | Hyperviseur pour VM jetables | Gratuit / payant |

#### D.2 Capture et documentation

| Outil | Usage | Coût |
|---|---|---|
| **Hunchly** | Capture structurée d'investigation, horodatage | Commercial (~130 USD/an) |
| **OSINT Cloner** | Alternative open source | Gratuit |
| **wget / curl + torify** | Récupération CLI via Tor | Gratuit |
| **Aquatone** | Capture screenshot en masse | Gratuit, open source |
| **Eyewitness** | Reconnaissance web automatique | Gratuit, open source |
| **OnionScan** | Audit OPSEC de services .onion | Gratuit, open source |

#### D.3 Plateformes commerciales CTI

| Plateforme | Force principale | Ordre de prix |
|---|---|---|
| **Recorded Future** | Vision globale, intégration extensive | 100k - 500k+ USD/an |
| **Flashpoint** | Russophone, Telegram | 100k - 300k USD/an |
| **Intel471** | Acteurs, cybercrime profondeur | 100k - 300k USD/an |
| **SOCRadar** | Rapport qualité/prix, PME-friendly | 30k - 100k USD/an |
| **Flare** | Niche dark web et data leaks | 30k - 100k USD/an |
| **DarkOwl** | Crawling .onion étendu | 50k - 200k USD/an |
| **Cybersixgill** (Zenity) | Profilage, attribution | 100k - 300k USD/an |
| **Hudson Rock** | Stealer logs spécialisé | 30k - 100k USD/an |
| **KELA** | Russophone fort | 100k - 300k USD/an |
| **Group-IB** | Vision Europe/Asie | 100k - 300k USD/an |

#### D.4 OSINT et pivoting

| Outil | Usage |
|---|---|
| **Maltego** | Graphing relations entités |
| **SpiderFoot** | Reconnaissance automatisée |
| **Have I Been Pwned** | Vérification breaches publics |
| **DeHashed** | Recherche dans dumps publics |
| **LeakCheck, Snusbase** | Bases de breach |
| **IntelX** | Archives leaks et .onion |
| **GitHub dorking** | Secrets dans repos publics |
| **Reverse image search** | Google Images, TinEye, Yandex |
| **DomainTools, SecurityTrails, ViewDNS** | WHOIS, DNS history |
| **Shodan, Censys** | Recherche infrastructure exposée |

#### D.5 Analyse blockchain

| Outil | Force |
|---|---|
| **Chainalysis** (Reactor, KYT) | Standard industrie, labellisation massive |
| **TRM Labs** (Forensics) | Compliance et investigation |
| **Elliptic** (Navigator) | Graphing et labellisation |
| **CipherTrace** | Mastercard subsidiary |
| **Crystal** | Bitfury subsidiary |
| **Breadcrumbs.app** | Open access partiel |
| **OXT.me** | Open Bitcoin analysis |
| **WalletExplorer** | Clustering basique |
| **Blockstream.info, Mempool.space** | Bitcoin explorers |
| **Etherscan, Tronscan** | Ethereum, TRON explorers |

#### D.6 Threat intelligence platforms

| Plateforme | Usage |
|---|---|
| **MISP** | Plateforme open source de partage d'IoC |
| **OpenCTI** | Plateforme open source TI |
| **Anomali ThreatStream, ThreatConnect, EclecticIQ** | Commerciales |
| **Recorded Future, Flashpoint, etc.** | Plateformes commerciales (incluent TIP) |

#### D.7 Surveillance leak sites

| Outil | Usage |
|---|---|
| **Ransomwatch** | Archive open source des leak sites |
| **Ransomfeed.it** | Agrégateur public |
| **SOCRadar Threat Hunting** | Commercial |
| **DarkOwl Vision** | Commercial |
| **Plateformes générales CTI** | Recorded Future, Flare, etc. |

#### D.8 Outils analyse fichiers

| Outil | Usage |
|---|---|
| **exiftool** | Extraction métadonnées |
| **VirusTotal** | Scan multi-AV |
| **Hybrid Analysis, Joe Sandbox** | Sandboxing |
| **ANY.RUN** | Sandboxing interactif |
| **CyberChef** | Conversions, decoding |
| **Wireshark** | Analyse réseau |
| **Volatility** | Analyse mémoire |

#### D.9 Communication chiffrée

| Outil | Usage |
|---|---|
| **GPG / GnuPG** | Signature et chiffrement PGP |
| **Pidgin + OTR** | XMPP avec chiffrement |
| **Signal, Wire** | Messagerie chiffrée pour équipe |
| **Element / Matrix** | Communication chiffrée fédérée |
| **OnionShare** | Partage de fichiers via Tor |

---

### Annexe E — Grille d'évaluation de crédibilité

Outil pour évaluer rapidement la crédibilité d'une annonce de breach, vente de données, ou autre contenu dark web.

#### E.1 Grille produit / annonce

| Critère | Indicateurs positifs (crédibilité ↑) | Indicateurs négatifs (crédibilité ↓) |
|---|---|---|
| **Vendeur — ancienneté** | Compte 12+ mois, posts réguliers | Compte récent (<3 mois), peu d'activité |
| **Vendeur — réputation** | 100+ transactions, feedback 95%+ | Pas de transactions visibles, pas de vouching |
| **Vendeur — signature** | PGP stable, signée systématiquement | Pas de PGP, ou clé récente/changée |
| **Forum** | Forum sérieux à vouching (XSS, Exploit) | Forum public ou low-end |
| **Description** | Spécifique, technique, cohérente | Générique, vague, exagérée |
| **Volumétrie** | Cohérente avec ce qui est plausible | Disproportionnée (« 100 To en exclusivité ») |
| **Échantillons** | Disponibles, vérifiables | Refusés, vagues, ou demandant paiement |
| **Prix** | Cohérent avec marché (voir Ch.14) | Anormalement bas (scam) ou absurde |
| **Méthode contact** | Standard (XMPP, forum) | Telegram nouveau, email gratuit douteux |
| **Métadonnées échantillons** | Cohérentes avec organisation présumée | Vagues, génériques, ou contradictoires |
| **Timing** | Cohérent avec compromission documentable | Timing improbable (avant événement déclencheur) |
| **Markers internes** | Présents (noms internes, codes spécifiques) | Absents ou contredits |
| **Cohérence cross-source** | Corroboration sur autres canaux | Source unique, non-corroboré |

#### E.2 Scoring rapide

Scoring informel : pour chaque critère, +1 (positif), 0 (neutre/incertain), -1 (négatif). Sommer.

- **+8 et plus** : très probablement authentique. Investigation approfondie justifiée.
- **+3 à +7** : probablement authentique avec réserves. Investigation prudente.
- **0 à +2** : ambigu. Recherche supplémentaire avant conclusion.
- **-3 à -1** : probablement scam ou recyclage. Faible priorité.
- **-4 et moins** : très probablement fake/scam. Classer.

Le scoring est un **outil d'orientation**, pas une vérité. Une investigation peut justifier d'un cas avec score modeste si certains critères sont déterminants (par exemple : marker interne unique = suffit à confirmer authenticité même si autres critères neutres).

#### E.3 Grille acteur (pseudonyme)

Pour évaluer la crédibilité d'un acteur observé (vendeur, IAB, opérateur).

| Critère | Évaluation |
|---|---|
| Ancienneté du compte | Mois / années |
| Volume de posts | Nombre, fréquence |
| Activité par catégorie | Quels types de produits/services |
| Transactions confirmées | Nombre, montants, types |
| Feedback / ratings | Distribution positive/négative |
| Vouching | Qui vouche, quels niveaux |
| Présence multi-forum | Quels forums, cohérence |
| PGP | Stable ? Reconnue cross-platform ? |
| Style linguistique | Cohérence, langue maternelle apparente |
| Wallet crypto | Activité, cluster, exchanges |
| Disputes | Litiges historiques, résolutions |

Sortie : profil structuré du vendeur en 1-2 pages, base de tout dossier d'investigation sur cet acteur.

#### E.4 Pièges classiques à vérifier

- **Recyclage** : la donnée vient-elle d'un breach antérieur connu ? Vérifier HIBP, DeHashed.
- **Composition factice** : assemblage de plusieurs breaches anciens présenté comme nouveau ?
- **Watermark / honeypot** : la donnée contient-elle des markers qui pourraient identifier les acheteurs ou les diffuseurs ?
- **False flag** : le profil de l'acteur est-il cohérent ou semble-t-il « designed » pour pointer vers une autre attribution ?
- **Pression temporelle artificielle** : le vendeur impose-t-il « offre 24h » pour empêcher due diligence ?
- **Prix incohérent** : trop bas (scam) ou trop élevé sans justification ?

---

### Annexe F — Templates de livrables

#### F.1 Template flash alert (1-2 pages)

```markdown
# FLASH ALERT — [Titre court]

**Référence** : FA-YYYYMMDD-NNN
**Date** : YYYY-MM-DD HH:MM (UTC+2)
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Synthèse (3-5 lignes)
[Que se passe-t-il ? Pourquoi maintenant ? Quel niveau de confiance ?]

## Observation
[Faits factuels, sources, timestamps]

## Implication immédiate
[Pourquoi ça concerne le destinataire]

## Action recommandée
- [Action 1, immédiat]
- [Action 2, dans la journée]
- [Action 3, dans la semaine]

## Limites
[Incertitudes, ce qu'on ne sait pas]

## Source(s)
[URL, plateforme, capture en annexe]

## Annexes
- A : Capture(s) horodatée(s) et hachée(s)
- B : Hashes (SHA-256)
```

#### F.2 Template intel note (3-8 pages)

```markdown
# INTEL NOTE — [Titre]

**Référence** : IN-YYYYMMDD-NNN
**Date de rédaction** : YYYY-MM-DD
**Version** : 1.0
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Executive Summary (½ page max)
[Réponses aux questions : que s'est-il passé ? Pourquoi est-ce important ? Que faut-il faire ? Quel niveau de confiance ?]

## Contexte
[Pourquoi cette note ? Quel événement déclencheur ? Quelles observations antérieures pertinentes ?]

## Observations
### Observation 1 : [Titre]
- Source, date, capture
- Description factuelle

### Observation 2 : [Titre]
[...]

## Analyse
[Interprétation, attribution, hypothèses testées, conclusions calibrées]

## Implications
[Risques pour le destinataire, impacts potentiels]

## Recommandations
1. **Immédiat (24-48h)** : [Action]
2. **Court terme (7 jours)** : [Action]
3. **Moyen terme (30 jours)** : [Action]
4. **Long terme (90 jours)** : [Action]

## Limites et incertitudes
[Ce qui n'est pas connu, ce qui pourrait changer l'analyse]

## Indicators (IoC)
[Adresses, domaines, hashes, pseudonymes — selon TLP]

## Annexes
A. Captures horodatées
B. Communications archivées
C. Analyses techniques
D. Chain of custody
```

#### F.3 Template bulletin sectoriel mensuel

```markdown
# BULLETIN MENSUEL — Menaces dark web — [Secteur] — [Mois Année]

**Auteur** : [Nom]
**Période** : [Mois] YYYY
**Classification** : TLP:[]
**Destinataires** : []

## Synthèse exécutive (1 page)
[Tendances majeures du mois, événements significatifs, recommandations stratégiques]

## Statistiques du mois
[Nombre revendications ransomware, top 5 acteurs, volumes leak detected, etc.]

## Événements significatifs
[Top 5-10 événements affectant le secteur ce mois]

## Acteurs en évolution
[Nouveaux groupes, disparitions, restructurations]

## Tendances observées
[Patterns émergents, vecteurs montants, géographies]

## Cas remarquables
[1-3 cas illustratifs avec leçons]

## Recommandations actionnables
[Priorisées par horizon temporel]

## Veille à venir
[Quoi surveiller le mois prochain]

## Annexes
[Détails par catégorie, IoC consolidés, statistiques détaillées]
```

#### F.4 Template rapport d'investigation (cas type DARKSTREAM)

```markdown
# RAPPORT D'INVESTIGATION — [Nom de l'opération]

**Référence** : INV-YYYYMMDD-NNN
**Date** : YYYY-MM-DD
**Version** : [N.N]
**Auteur principal** : [Nom]
**Investigateurs associés** : [Noms]
**Classification** : TLP:[]
**Destinataires** : [Liste]

## Executive Summary
[½ - 1 page max — tout ce qui compte si rien d'autre n'est lu]

## Mandat et cadre
- Donneur d'ordre, objectifs, contraintes
- Cadre légal, autorités impliquées
- Périmètre d'investigation

## Méthodologie
- Outils, sources, période d'investigation
- Personas utilisées
- Limites méthodologiques connues

## Phase 1 — Reconnaissance
[Description détaillée, captures pertinentes]

## Phase 2 — Authentification
[Méthodes, résultats, niveau de confiance]

## Phase 3 — Pivoting et corrélation
[Pivots effectués, résultats, graphes]

## Phase 4 — Analyse et attribution
[Hypothèses testées, conclusion calibrée]

## Phase 5 — Vérifications anti-désinformation
[False flags écartés, biais identifiés]

## Conclusions
[Synthèse des constatations]

## Implications pour le client
[Risques, impacts, échéances]

## Recommandations
[Priorisées, avec délais et destinataires]

## Limites et incertitudes
[Ce qui ne peut être conclu avec les moyens employés]

## Annexes
A. Captures forum (avec hashes)
B. Communications archivées
C. Échantillons et analyses
D. Analyse blockchain
E. IoC structurés (MISP/STIX)
F. Chain of custody
G. Note méthodologique
H. Bibliographie / sources externes
```

#### F.5 Template fiche IoC

```markdown
# FICHE IoC — [Identifiant ou pseudonyme]

**Type** : [Pseudonyme / Adresse crypto / Domaine / IP / Hash / etc.]
**Valeur** : [Indicator]
**Classification** : TLP:[]
**Date première observation** : YYYY-MM-DD
**Date dernière observation** : YYYY-MM-DD
**Confiance** : [WEP : très probable / probable / possible]

## Description
[Contexte, lien avec quel acteur/groupe/campagne]

## Sources de l'observation
[Forum/marché, URL, post ID, captures]

## Liens connus
[Autres IoC liés : autres pseudonymes, wallets, domaines]

## Recommandation
[Bloquer / Surveiller / Enquêter]

## Source originale
[Référence du rapport / investigation]
```

#### F.6 Template note IAB (pour suivi)

```markdown
# FICHE IAB — [Pseudonyme]

**Pseudonymes connus** : [Liste cross-forum]
**Forums présents** : [XSS, Exploit, BreachForums, etc.]
**Première observation** : YYYY-MM-DD
**Dernière observation** : YYYY-MM-DD

## Profil
- Ancienneté
- Style et qualité des posts
- Réputation observée
- Langues utilisées
- Fuseau horaire estimé

## Spécialisation
- Types d'accès vendus (VPN/RDP/Citrix/AD)
- Secteurs ciblés
- Géographies
- Niveau de privilèges typique

## Tarification observée
- Prix moyens demandés
- Évolutions

## Wallet crypto
- Adresses observées
- Cluster (lien Chainalysis/TRM si applicable)
- Exchanges traversés

## Réseau
- Voucheurs
- Acheteurs identifiés
- Partenaires fréquents

## Risque pour client
[Évaluation actualisée]

## Recommandations
[Surveillance, détection préventive, etc.]
```

---

### Annexe G — Ressources et veille

#### G.1 Rapports annuels et périodiques de référence

**Sur les ransomware et leak sites** :
- Coveware (rapports trimestriels) — taux de paiement, montants, secteurs.
- Chainalysis Crypto Crime Report (annuel) — flux financiers ransomware, mixers, sanctions.
- Mandiant M-Trends (annuel) — incidents IR, tendances.
- Sophos State of Ransomware (annuel) — impacts, paiements, défense.
- Recorded Future Annual Threat Report.
- ENISA Threat Landscape (annuel).

**Sur le dark web et cybercrime généraliste** :
- SOCRadar Annual Dark Web Report.
- Flashpoint Cyber Threat Intelligence Report.
- Group-IB Hi-Tech Crime Trends.
- Kela State of Initial Access Brokers.
- Hudson Rock Stealer Report.
- Cyberint Annual Cybercrime Report.

**Sectoriels** :
- FS-ISAC reports (finance).
- H-ISAC reports (santé).
- Verizon DBIR (Data Breach Investigations Report).
- IBM Cost of a Data Breach Report.

**Académiques et recherche** :
- Journal of Cybersecurity, ACM digital library.
- Citizen Lab (University of Toronto) — surveillance, dissidents.
- VirusBulletin Conference papers.
- Black Hat / DEF CON briefings.

#### G.2 Vendors et plateformes commerciales — sites de référence

| Vendor | Site | Spécificité |
|---|---|---|
| Recorded Future | recordedfuture.com | Vision globale CTI |
| Flashpoint | flashpoint.io | Russophone, Telegram |
| Intel471 | intel471.com | Cybercrime profondeur |
| SOCRadar | socradar.io | Rapport qualité-prix |
| Flare | flare.io | Dark web specialist |
| Mandiant (Google) | mandiant.com | IR + threat intel |
| CrowdStrike | crowdstrike.com | EDR + intel |
| Microsoft Threat Intelligence | microsoft.com/security | Vision Microsoft |
| Sekoia | sekoia.io | CTI européen |
| Group-IB | group-ib.com | Vision Asie/Russie |
| KELA | kela.com | Russophone fort |
| Cybersixgill (Zenity) | cybersixgill.com | Profilage |
| Hudson Rock | hudsonrock.com | Stealer logs |
| DarkOwl | darkowl.com | Crawling .onion |

#### G.3 Sources gouvernementales et institutionnelles

**France** :
- ANSSI : ssi.gouv.fr — Bulletins, alertes, rapports.
- CERT-FR : cert.ssi.gouv.fr — Avis, alertes opérationnelles.
- DGSI : dgsi.interieur.gouv.fr — Cadre contre-ingérence.
- Cybermalveillance : cybermalveillance.gouv.fr — Grand public et PME.

**Europe** :
- ENISA : enisa.europa.eu — Reports, threat landscape.
- CERT-EU : cert.europa.eu.
- Europol EC3 : europol.europa.eu.
- Pall Mall Process : initiative régulation PSO.

**International** :
- CISA : cisa.gov (US) — Alerts, advisories, campaigns.
- NCSC : ncsc.gov.uk (UK) — Alerts, guidance.
- BSI : bsi.bund.de (Allemagne).
- ACSC : cyber.gov.au (Australie).
- CCCS : cyber.gc.ca (Canada).
- Interpol : interpol.int.

#### G.4 Communautés et forums professionnels

- **FIRST** (Forum of Incident Response and Security Teams) : first.org — communauté CSIRT internationale.
- **CSIRT national** (France) : Renater pour académique, par secteur ailleurs.
- **ISAC sectoriels** : FS-ISAC (finance), H-ISAC (santé), E-ISAC (énergie), R-CISC (retail), Aviation-ISAC, ASD-EUROSPACE/AIAC (aerospace).
- **MISP communauté** : misp-project.org — partage IoC.
- **CIRCL Luxembourg** : circl.lu — CSIRT et MISP.
- **OSINT communities** : Bellingcat, Citizen Lab, OSINT Curious.

#### G.5 Conférences et événements

**Internationaux** :
- Black Hat USA, DEF CON, Black Hat Europe — Las Vegas, Londres.
- RSA Conference — San Francisco.
- FIRST Annual Conference.
- Virus Bulletin (VB).
- Botconf — recherche botnets.

**Européens / francophones** :
- SSTIC (Rennes, juin) — francophone référence.
- FIC (Lille puis Marseille, janvier) — institutionnel français.
- Hack.lu (Luxembourg).
- Troopers (Heidelberg).
- NDSS, USENIX Security — académiques.

**OSINT spécifiques** :
- OSINT Symposium.
- OSMOSIS Conference.
- Trace Labs CTF events.

#### G.6 Newsletters et veille

- **Risky.Biz** (Patrick Gray) — podcast et newsletter, référence.
- **The CyberWire** — newsletter quotidienne.
- **Krebs on Security** — Brian Krebs blog.
- **The Record** (Recorded Future) — actualité CTI.
- **Bleeping Computer** — actualité accessible.
- **CyberScoop, ArsTechnica Security**.

**Comptes Twitter/X / Mastodon à suivre** (sélection, non exhaustive) :
- @briankrebs, @lorenzofb, @vxunderground, @malwrhunterteam, @MalwareTechBlog, @cyb3rops (Florian Roth), @JohnHultquist, @riskybusiness, @CrowdStrike, @Mandiant, @Flashpoint, @ESETresearch, @Kaspersky, @ANSSI_FR, @CERT_FR, @CISAgov, @NCSC, @citizenlab, @recorded_future.

#### G.7 Livres de référence

**Sur le dark web et cybercrime** :
- *DarkMarket* — Misha Glenny (cybercrime au tournant 2010).
- *American Kingpin* — Nick Bilton (Silk Road, Ross Ulbricht).
- *Sandworm* — Andy Greenberg (APT russe — focus APT mais contexte).
- *Tracers in the Dark* — Andy Greenberg (traçage crypto).
- *The Lazarus Heist* — Geoff White (DPRK cybercrime).
- *Cult of the Dead Cow* — Joseph Menn (histoire hacktivisme).

**Sur l'investigation** :
- *Open Source Intelligence Techniques* — Michael Bazzell (référence OSINT).
- *Hiding in Plain Sight* — Eric Cole (OSINT défensif).
- *Practical Threat Intelligence* — Valentina Costa-Gazcón.
- *The Threat Intelligence Handbook* — Recorded Future (gratuit).

**Sur la méthode analytique** :
- *Psychology of Intelligence Analysis* — Richards Heuer (CIA, classique).
- *Structured Analytic Techniques for Intelligence Analysis* — Heuer & Pherson.

**Sur la crypto** :
- *Mastering Bitcoin* — Andreas Antonopoulos.
- *Tracers in the Dark* (déjà cité).

**Ouvrages français** :
- *Cyberattaque et cyberdéfense* — Daniel Ventre.
- *La cyberdéfense* — Stéphane Taillat et al.
- Publications IRSEM, INHESJ.

#### G.8 Formations

**Certifications** :
- **SANS FOR578 — Cyber Threat Intelligence** (certification GCTI) — référence.
- **SANS FOR589 — Cybercrime Intelligence**.
- **SANS SEC487 — OSINT Foundations**.
- **SEC587 — Advanced OSINT**.
- **CompTIA CySA+** (analyse).
- **EC-Council CTIA** (Certified Threat Intelligence Analyst).

**Formations académiques** :
- Master cyber, master renseignement, master géopolitique en France.
- Programs spécialisés à l'EPITA, EPITECH, INSA, Télécom Paris, etc.

**Formations courtes** :
- Bellingcat (en ligne, OSINT).
- IntelTechniques (Bazzell, OSINT).
- Webinars vendors (Recorded Future, Flare, etc.).

**Communautés d'apprentissage** :
- Trace Labs (CTF OSINT for missing persons).
- Open Source Intelligence Curious (groupe communautaire).

---


## CLÔTURE DU COURS

### Ce que ce cours a cherché à apprendre

Ce cours **LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER** s'est donné pour mission de transmettre une vision **professionnelle, calibrée, opérationnelle** du dark web. Au-delà des clichés médiatiques, le dark web est un écosystème connaissable, traçable dans ses dynamiques, et investiguable par méthodes rigoureuses dans le cadre légal et éthique.

Le cours a posé les fondations (Partie I), expliqué les infrastructures (Partie II), cartographié les écosystèmes (Partie III), articulé l'économie clandestine (Partie IV), formalisé l'investigation (Partie V), structuré l'analyse et le renseignement (Partie VI), exploré les usages contemporains et tendances (Partie VII), synthétisé sur des cas complets (Partie VIII), et ancré la pratique dans des exercices concrets de navigation et de collecte défensive (Partie IX).

Les annexes (A à G) fournissent les outils opérationnels — glossaire, typologie, checklists OPSEC, outils, grilles de crédibilité, templates, ressources de veille. L'analyste qui les utilise quotidiennement gagne en rigueur et en réactivité.

### Les quatre idées centrales

Quatre idées traversent le cours et méritent d'être retenues.

**Première idée — le dark web est un écosystème, pas un mythe**. Connaissable, mesurable, investiguable. Pas un océan infini hors d'atteinte, mais un ensemble structuré d'espaces, d'acteurs, et de dynamiques. Quelques semaines de travail méthodique permettent de cartographier les acteurs majeurs d'un secteur. La connaissance est accessible — il faut juste la rigueur de la construire.

**Deuxième idée — l'investigation est une discipline, pas une intuition**. OPSEC stricte, méthode formalisée, vocabulaire calibré, anti-biais systématique, documentation rigoureuse. L'investigation amateur produit du bruit ; l'investigation disciplinée produit du renseignement. La différence est dans la méthode, pas dans le talent intuitif.

**Troisième idée — la coopération est multiplicateur de capacité**. Avec les autorités (DGSI, ANSSI, FdO), avec les pairs sectoriels (ISAC), avec les vendors CTI, avec la communauté internationale. L'analyste isolé voit peu ; l'analyste connecté voit beaucoup. Les opérations efficaces (Cronos, Endgame, Cookie Monster) sont coopératives, pas solitaires.

**Quatrième idée — l'éthique encadre la pratique**. Légalité scrupuleuse, minimisation, non-prolifération, respect des victimes, neutralité analytique. Ces principes ne sont pas des contraintes — ils sont la condition de la durabilité. Un analyste qui dérive perd sa crédibilité, son organisation, et parfois sa liberté. Un analyste qui maintient l'éthique construit une carrière durable et une contribution réelle.

### Pour aller plus loin

La bibliothèque dont ce cours fait partie articule plusieurs dimensions complémentaires :

- **OSINT Mastery** : techniques OSINT générales, transposables au dark web pour pivoting.
- **AU CŒUR DES APT** : acteurs étatiques qui utilisent le dark web pour opérations. Compréhension géopolitique cyber.
- **Cartographie des écosystèmes cybercriminels** : contexte structurel large.
- **OSINT Crypto** : traçage blockchain en profondeur.
- **FININT — Investigation financière** : analyse financière au-delà du crypto.
- **Cours SOC, IR, Forensics** : aspects techniques défensifs complémentaires.
- **CTI** : structuration de programme de threat intelligence.
- **GRC** : intégration dans gouvernance d'entreprise.

Au-delà de la bibliothèque, l'apprentissage du dark web est **un métier de veille permanente**. Les acteurs évoluent, les marchés changent, les outils se renouvellent. Maintenir la compétence exige lecture continue, exercice régulier, échanges avec la communauté.

### Le mot de la fin

Le dark web restera un espace utilisé pour le crime, le journalisme, le militantisme, la dissidence. Sa neutralité technique en fait un instrument moralement ambigu — protecteur des dissidents, refuge des criminels, canal de la presse libre. Cette ambiguïté n'est pas un défaut à corriger ; c'est une caractéristique structurelle de l'anonymat.

Pour l'analyste, le dark web est un **terrain de travail**. Pas un mythe à démythifier, pas une zone à fuir, pas un sujet à éviter — mais un espace à comprendre méthodiquement, à investiguer rigoureusement, à exploiter défensivement.

Au fil des années, l'analyste mûri par cette pratique développe une **intuition formée** — il reconnaît rapidement un vendeur sérieux d'un scammer, un groupe en croissance d'un groupe en décadence, un signal authentique d'un faux drapeau. Cette intuition n'est pas magique — elle est le fruit accumulé des heures, des semaines, des années passées à observer, analyser, tirer des leçons.

Ce cours a tenté d'accélérer ce mûrissement — en proposant cadre, méthodes, exemples, références. Mais le métier s'apprend in fine **sur le terrain**, avec la patience, la curiosité, l'éthique, et la rigueur que l'analyste apporte chaque jour à son travail.

Bonne route à l'analyste qui s'y engage.
