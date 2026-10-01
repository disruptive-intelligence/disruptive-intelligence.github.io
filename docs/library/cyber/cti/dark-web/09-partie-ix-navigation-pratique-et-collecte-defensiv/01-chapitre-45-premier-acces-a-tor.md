---
title: Chapitre 45 — Premier accès à Tor
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IX — Navigation pratique et collecte défensive encadrée
  - index.md
---

installation, sécurité et navigation légitime

Pour beaucoup d'analystes débutants, la première difficulté n'est pas conceptuelle mais **opérationnelle** — comment, concrètement, accéder proprement à une ressource .onion légitime, avec une posture de sécurité minimale. Ce chapitre est le premier TP guidé du cours. Il ne cherche pas à faire « explorer le dark web », mais à faire comprendre l'accès propre à des ressources légitimes.

## 45.1 Installer Tor Browser depuis la source officielle

**Téléchargement**. **Source unique légitime** : `torproject.org`. Toute autre source (sites tiers, packages communautaires non officiels, miroirs douteux) doit être considérée comme suspecte. Tor Browser est précisément l'outil **le plus ciblé par malware piégé** parce que ses utilisateurs cherchent confidentialité et anonymat — un Tor Browser modifié peut journaliser tout le trafic ou contenir un backdoor sans que l'utilisateur le sache.

**Installation** :

- **Windows / macOS** : exécuter l'installeur, choisir un répertoire dédié.
- **Linux** : extraire l'archive, exécuter `start-tor-browser.desktop` ou le script `start-tor-browser`. Pas besoin de root.

## 45.2 Vérifier l'authenticité du téléchargement

Le Tor Project signe ses binaires avec une clé GPG. Procédure :

1. Télécharger le binaire (`.exe` Windows, `.dmg` macOS, `.tar.xz` Linux).
2. Télécharger la **signature** correspondante (fichier `.asc` à côté du binaire).
3. Importer la clé publique du Tor Browser Developers : `gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org`.
4. Vérifier la signature : `gpg --verify tor-browser-linux64-XX.x_ALL.tar.xz.asc`.
5. Sortie attendue : `Good signature from "Tor Browser Developers (signing key) <torbrowser@torproject.org>"`.

Cette procédure prend 5 minutes et garantit que le binaire n'a pas été altéré entre le serveur du Tor Project et votre poste. Indispensable en contexte professionnel.

> **À retenir.** Un Tor Browser non vérifié est un risque majeur : l'utilisateur croit protéger son anonymat alors qu'il peut installer un navigateur modifié, journalisé ou malveillant.

## 45.3 Premier lancement et vérification de connexion

**Premier lancement** :

- Tor Browser propose **« Connect »** ou **« Configure »**. Pour usage standard (hors censure), cliquer **Connect**.
- Connexion au réseau Tor : 5-30 secondes typiquement.
- Page d'accueil DuckDuckGo (par défaut) une fois connecté.

**Vérification de connexion**. Aller sur `https://check.torproject.org` — confirme que le trafic passe bien par le réseau Tor et affiche l'IP de sortie (du nœud exit, pas votre vraie IP). Cette page **ne prouve pas** que l'utilisateur est anonyme au sens absolu — elle confirme seulement que le trafic web passe par Tor.

## 45.4 Configurer le mode Safest

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

## 45.5 Comprendre une adresse .onion v3

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

## 45.6 Premières destinations légitimes

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

## 45.7 Sessions de découverte type — TPs progressifs

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

## 45.8 Pièges du débutant

**Cliquer sur des liens « hidden wiki » sans vérification**. The Hidden Wiki et ses successeurs sont des listes communautaires d'adresses .onion. **Beaucoup de ces listes contiennent des liens vers du contenu illicite, des arnaques, ou des phishing pages d'apparence légitime**. Le débutant qui suit aveuglément un lien « .onion drogues » ou « .onion porn » s'expose à des risques juridiques et techniques.

**Recommandation** : ne suivre que des adresses .onion **publiquement référencées par leur opérateur officiel**. Si la BBC indique sur son site clearnet « notre adresse .onion est X », c'est fiable. Si une « hidden wiki » liste « BBC : Y », c'est suspect — vérifier d'abord X sur bbc.com.

Le premier réflexe de l'analyste débutant n'est pas « où trouver des liens ? », mais « comment vérifier que le lien que j'ai est authentique ? ».

**Activer JavaScript automatiquement**. Tentation forte quand un site casse en mode Safest. À éviter sauf nécessité absolue identifiée — beaucoup de NIT historiques exploitent JavaScript.

**Télécharger des fichiers**. Tout fichier téléchargé du dark web doit être traité comme **potentiellement malveillant**. Ouvrir uniquement en VM isolée, jamais sur le poste hôte.

**Logger avec ses comptes personnels**. Se connecter à son Gmail, Twitter, ou banque depuis Tor Browser n'est pas illégal mais expose à plusieurs risques (services qui détectent Tor et bloquent ; corrélation possible entre activité Tor et identité personnelle si erreur OPSEC). Pour analyste pro : machine d'investigation jamais utilisée pour comptes personnels.

**Confondre « lent » et « cassé »**. Tor est lent. Une page qui met 10 secondes à charger n'est pas forcément cassée — c'est normal. Patience.

## 45.9 Vérifier sa propre exposition (premier aperçu)

Exercice utile pour terminer cette première session : vérifier votre propre exposition publique.

**Outils gratuits** :

- **Have I Been Pwned** (haveibeenpwned.com) : entrer son email, voir dans quels breaches publics il apparaît.
- **Firefox Monitor** : alerte continue.
- **DeHashed** (dehashed.com) : version commerciale plus complète.

Cette première vérification personnelle sert de démonstration. Le **Ch.48** formalise la méthode pour un usage défensif individuel ou organisationnel.

---
