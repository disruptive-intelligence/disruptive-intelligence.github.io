---
title: PARTIE 5 — Linux en réseau
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 5
chapters: 7
---

Une machine isolée est rare. La plupart du temps, un système Linux communique : il sert des pages web, héberge des fichiers, ou s'administre à distance. Maintenant que tu comprends son fonctionnement interne, on l'ouvre sur le réseau. Tu vas apprendre à voir comment la machine communique, à t'y connecter à distance en sécurité, et à transférer des fichiers entre machines.

---


## Chapitre 17 — Les bases du réseau Linux

### Le minimum à savoir

#### Le strict nécessaire de TCP/IP

Pas besoin d'être expert réseau pour administrer Linux, mais quelques notions sont indispensables :

- **Adresse IP** : l'adresse numérique d'une machine sur un réseau (ex. `192.168.1.10`). C'est son « numéro de téléphone ».
- **Masque de sous-réseau** : il définit quelles machines sont sur le **même** réseau local que toi.
- **Passerelle (gateway)** : la « porte de sortie » du réseau local vers le reste du monde (souvent ta box ou ton routeur).
- **Port** : sur une même machine, chaque service écoute sur un **port** numéroté (ex. 22 pour SSH, 80 pour le web, 443 pour le web sécurisé). Si l'IP est l'adresse de l'immeuble, le port est le numéro de l'appartement.
- **DNS** : le système qui traduit les noms (`exemple.com`) en adresses IP. C'est l'annuaire d'Internet.

#### Voir sa configuration réseau : `ip`

La commande moderne pour tout ce qui touche au réseau est `ip` :

```bash
ip a             # affiche les interfaces et leurs adresses IP (a = address)
ip r             # affiche la table de routage, dont la passerelle (r = route)
```

`ip a` te montre tes **interfaces réseau** (carte filaire, Wi-Fi, interface locale `lo`…) et l'adresse IP de chacune. `ip r` te montre par où sortent tes paquets (notamment la ligne `default via ...` qui désigne ta passerelle).

#### Tester la connectivité : `ping`

`ping` envoie de petits paquets à une machine pour vérifier qu'elle répond et mesurer le temps d'aller-retour :

```bash
ping 8.8.8.8             # teste la connectivité vers une IP (Ctrl + C pour arrêter)
ping exemple.com         # teste aussi la résolution DNS (nom → IP)
```

> **Réflexe de diagnostic :** si `ping 8.8.8.8` (une IP) fonctionne mais que `ping exemple.com` (un nom) échoue, ton problème vient probablement du **DNS**, pas de la connexion elle-même. Ce simple test isole déjà la cause.

### Très utile en pratique

#### Voir les ports ouverts : `ss` (et le vieux `netstat`)

Quels services écoutent sur ta machine, et donc quelles « portes » sont ouvertes ? La réponse vient de `ss` :

```bash
ss -tulpn        # tous les ports en écoute, avec le programme associé
```

Décortiquons ces options très utilisées : `-t` (TCP), `-u` (UDP), `-l` (uniquement ce qui **écoute**, *listening*), `-p` (le **programme** qui écoute — nécessite souvent `sudo`), `-n` (afficher les **numéros** de port plutôt que les noms).

> **`ss` vs `netstat` :** tu croiseras souvent `netstat` dans d'anciens cours, scripts ou tutoriels. **`ss` est l'outil moderne recommandé** ; `netstat` est ancien et considéré comme déprécié, mais encore présent partout, donc utile à savoir lire. Sur les systèmes récents, `netstat` n'est même plus installé par défaut (il fait partie du paquet `net-tools`). Apprends `ss`, reconnais `netstat`.

> **Très utile en sécurité :** `ss -tulpn` révèle la **surface d'attaque locale** de la machine — chaque port en écoute est une porte potentielle. Côté défense, on vérifie que **seuls les services attendus** écoutent, et on ferme ou désactive le reste (lien avec le durcissement, chapitre 25). Un port inattendu en écoute est un signal à investiguer.

#### Interroger le DNS : `dig` et `nslookup`

Pour traduire un nom en adresse IP (ou enquêter sur la configuration DNS d'un domaine) :

```bash
dig exemple.com          # interrogation DNS détaillée (paquet dnsutils)
nslookup exemple.com     # alternative plus simple à lire
```

`dig` n'est pas toujours installé : `sudo apt install dnsutils` (réflexe de la Partie 0).

#### Télécharger et tester des services web : `curl` et `wget`

Deux outils pour parler à des serveurs web depuis le terminal :

```bash
curl https://exemple.com           # récupère et affiche le contenu d'une URL
curl -I https://exemple.com        # -I : seulement les en-têtes (code de réponse, serveur…)
wget https://exemple.com/fichier   # télécharge un fichier et l'enregistre sur le disque
```

> **À retenir :** `curl` sert surtout à **interroger/tester** un service (et afficher la réponse) ; `wget` sert surtout à **télécharger** un fichier. `curl -I` est un réflexe pratique pour vérifier rapidement qu'un site répond et avec quel code (200 = OK, 404 = absent, 500 = erreur serveur…).

#### Suivre le chemin réseau : `traceroute` (notion)

`traceroute exemple.com` montre les étapes (les routeurs) par lesquelles passent tes paquets pour atteindre une destination. Utile pour localiser **où** une connexion se bloque. Outil à installer au besoin (`sudo apt install traceroute`), bon à connaître de nom.

### ❌ Erreur classique

```bash
# Utiliser ifconfig/netstat par habitude alors qu'ils ne sont plus là
ifconfig                 # ❌ souvent absent sur les systèmes récents
ip a                     # ✅ l'équivalent moderne
netstat -tulpn           # ❌ déprécié / absent par défaut
ss -tulpn                # ✅ l'équivalent moderne

# Oublier sudo pour voir le programme derrière un port
ss -tulpn                # le champ "programme" peut rester vide
sudo ss -tulpn           # ✅ pour voir quel processus écoute

# Conclure trop vite à une panne réseau
ping exemple.com         # échoue...
ping 8.8.8.8             # ✅ teste d'abord par IP : si ça marche, c'est le DNS

# Confondre curl et wget
wget https://api...      # télécharge un fichier au lieu d'afficher la réponse
curl https://api...      # ✅ affiche la réponse dans le terminal
```

### Exercices

**Guidé :** Affiche tes interfaces réseau avec `ip a` et repère ton adresse IP locale (souvent en `192.168.x.x` ou `10.x.x.x`). Affiche ensuite ta passerelle avec `ip r` (la ligne `default via ...`). Enfin, vérifie ta connectivité avec `ping -c 4 8.8.8.8` (le `-c 4` limite à 4 paquets).

**Autonome :** Liste les ports en écoute sur ta machine avec `sudo ss -tulpn`. Pour chaque ligne, identifie le port et, si possible, le programme. Le port 22 (SSH) est-il ouvert ? Reconnais-tu tous les services qui écoutent, ou certains te surprennent-ils ?

**Défi (orientation sécurité) :** Dresse l'inventaire réseau de ta machine comme le ferait un analyste. Enregistre dans un fichier (avec `tee`, chapitre 7) la sortie de `sudo ss -tulpn`. Pour chaque port en écoute, demande-toi : ce service doit-il **vraiment** tourner ? Doit-il être accessible depuis l'extérieur, ou seulement en local ? Cette réflexion est exactement celle du durcissement : **fermer ce qui n'a pas besoin d'être ouvert**.

### ✅ Tu sais maintenant…

- Les notions clés : **IP, masque, passerelle, port, DNS**
- Voir ta config réseau avec `ip a` (adresses) et `ip r` (routage/passerelle)
- Tester la connectivité avec `ping`, et isoler un problème **DNS** vs **réseau**
- Lister les ports en écoute avec **`ss -tulpn`** (la surface d'attaque locale)
- Que `ss` est l'outil **moderne** et `netstat` l'ancien **déprécié** (mais à savoir lire)
- Interroger le DNS (`dig`, `nslookup`) et tester un service web (`curl`, `curl -I`, `wget`)
- Que `traceroute` montre le chemin réseau vers une destination

---


## Chapitre 18 — SSH : se connecter à distance

### Le minimum à savoir

#### Le principe : un terminal sur une machine distante

**SSH** (*Secure Shell*) est le protocole qui permet d'ouvrir un terminal sur une machine **distante**, à travers le réseau, de façon **chiffrée** (personne ne peut espionner la session). C'est l'outil fondamental de l'administration : la quasi-totalité des serveurs dans le monde se gèrent en SSH. Tout ce que tu as appris depuis le chapitre 1 s'applique à l'identique sur la machine distante — c'est juste le terminal qui est « ailleurs ».

Il y a deux côtés :

- Le **client SSH** (`ssh`) : sur ta machine, tu t'en sers pour te connecter.
- Le **serveur SSH** (`sshd`, le démon du chapitre 14) : sur la machine distante, il attend et accepte les connexions, sur le **port 22** par défaut.

#### Se connecter : `ssh`

```bash
ssh alice@192.168.1.50       # se connecte en tant qu'alice sur la machine 192.168.1.50
ssh alice@serveur.exemple.com  # avec un nom de domaine
ssh -p 2222 alice@serveur    # -p pour préciser un port différent du 22
```

À la **première** connexion, SSH affiche l'**empreinte** (*fingerprint*) de la machine distante et te demande de confirmer. C'est une sécurité : tu vérifies que tu te connectes à la bonne machine, et non à un imposteur. Une fois acceptée, l'empreinte est mémorisée ; un changement futur déclenchera un avertissement.

Pour terminer une session distante, on tape simplement `exit` (ou `Ctrl + D`).

### Très utile en pratique

#### L'authentification par clé : plus sûre que le mot de passe

Se connecter par mot de passe fonctionne, mais reste vulnérable (on peut le deviner, le forcer). La méthode professionnelle est l'**authentification par clé**, fondée sur une paire :

- une **clé privée**, qui reste **secrète** sur ta machine (à ne **jamais** partager) ;
- une **clé publique**, qu'on dépose sur les serveurs où l'on veut se connecter.

Le serveur vérifie que tu possèdes la clé privée correspondant à la clé publique qu'il connaît, sans qu'aucun secret ne circule. On génère sa paire de clés une fois :

```bash
ssh-keygen -t ed25519        # crée une paire de clés (algorithme moderne et sûr)
```

Cela crée deux fichiers dans `~/.ssh/` : `id_ed25519` (privée, à protéger) et `id_ed25519.pub` (publique, à diffuser). On copie ensuite la clé **publique** sur le serveur :

```bash
ssh-copy-id alice@serveur    # installe ta clé publique sur le serveur distant
```

Désormais, `ssh alice@serveur` te connecte **sans mot de passe**, de façon plus sûre.

> **Règle d'or des clés :** la clé **privée** ne quitte **jamais** ta machine et ne se partage **jamais**. Si quelqu'un l'obtient, il peut se faire passer pour toi. La clé **publique**, elle, peut être diffusée sans risque. Protège ta clé privée comme le mot de passe le plus important.

#### Simplifier avec `~/.ssh/config`

Si tu te connectes souvent aux mêmes machines, tu peux leur donner des surnoms dans un fichier de configuration personnel :

```bash
# Dans ~/.ssh/config
Host monserveur
    HostName 192.168.1.50
    User alice
    Port 22
```

Tu n'as plus qu'à taper `ssh monserveur`. C'est plus court, moins source d'erreurs, et ça centralise tes accès.

#### Durcir le serveur SSH (côté défense)

Le serveur SSH étant la porte d'entrée d'une machine, c'est une **cible privilégiée** des attaques (notamment les attaques par force brute du chapitre 4). Quelques réglages, dans `/etc/ssh/sshd_config`, réduisent fortement le risque. On les modifie **avec le réflexe du chapitre 6** (`.bak`, `sudoedit`, `diff`) :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
```

Les durcissements les plus courants :

- **`PermitRootLogin no`** : interdire la connexion directe en root (on se connecte en utilisateur normal, puis `sudo`). C'est l'un des réglages les plus importants.
- **`PasswordAuthentication no`** : n'autoriser que les clés, une fois celles-ci en place (supprime tout risque de force brute sur mot de passe).
- Éventuellement, changer le port par défaut pour réduire le bruit automatisé.

Après modification, on **recharge** le service (chapitre 14) pour appliquer :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérifier le changement
sudo systemctl restart ssh                               # 4. appliquer
```

> **⚠️ Prudence vitale en SSH distant :** ne désactive **jamais** ta seule méthode d'accès sans en avoir une autre qui fonctionne. Avant de couper l'authentification par mot de passe, **vérifie que ta clé fonctionne**. Avant de redémarrer `sshd` à distance, garde une session ouverte de secours. Une mauvaise manipulation peut te verrouiller dehors de ta propre machine.

> **Orientation cyber / SOC :** le durcissement SSH (pas de root, clés uniquement) est l'un des gestes défensifs les plus rentables. Et côté surveillance, suivre les tentatives de connexion (`journalctl -u ssh -f`, chapitre 15) permet de détecter une attaque en cours.

### ❌ Erreur classique

```bash
# Partager ou copier la mauvaise clé
cat ~/.ssh/id_ed25519        # ❌ JAMAIS : c'est la clé PRIVÉE, elle reste secrète
cat ~/.ssh/id_ed25519.pub    # ✅ la clé PUBLIQUE, celle qu'on diffuse

# Mauvaises permissions sur ~/.ssh (SSH refuse de fonctionner)
chmod 777 ~/.ssh             # ❌ SSH refusera d'utiliser des clés trop ouvertes
chmod 700 ~/.ssh             # ✅ dossier privé
chmod 600 ~/.ssh/id_ed25519  # ✅ clé privée lisible par toi seul

# Désactiver le mot de passe AVANT de tester la clé
# ❌ risque de se verrouiller dehors
# ✅ teste d'abord ssh par clé, PUIS désactive le mot de passe

# Redémarrer sshd à distance sans filet
sudo systemctl restart ssh   # ⚠️ garde une 2e session ouverte au cas où

# Ignorer un changement d'empreinte
# Un avertissement de changement de fingerprint peut signaler un vrai problème : ne pas l'ignorer aveuglément
```

### Exercices

**Guidé :** Génère ta paire de clés SSH avec `ssh-keygen -t ed25519` (accepte l'emplacement par défaut, choisis ou non une passphrase). Vérifie que deux fichiers ont été créés dans `~/.ssh/` avec `ls -l ~/.ssh/`. Identifie lequel est la clé privée et lequel est la publique. Quelles sont leurs permissions ?

**Autonome (si tu disposes d'une seconde machine ou d'une VM) :** Connecte-toi en SSH d'une machine à l'autre par mot de passe. Observe la demande de confirmation d'empreinte à la première connexion. Une fois connecté, lance `hostname` et `whoami` pour confirmer que tu es bien sur la machine distante. Termine avec `exit`.

**Défi (orientation sécurité, en lab) :** Sur une machine de test où tu as déjà un accès de secours, mets en place l'authentification par clé (`ssh-copy-id`), vérifie qu'elle fonctionne, puis prépare (sans forcément appliquer) les durcissements de `sshd_config` : `PermitRootLogin no` et `PasswordAuthentication no`. Avant tout `restart`, relis la règle d'or : as-tu un accès garanti si quelque chose tourne mal ? Décris la procédure prudente que tu suivrais.

### ✅ Tu sais maintenant…

- Que **SSH** ouvre un terminal **chiffré** sur une machine distante (port 22, démon `sshd`)
- Te connecter avec `ssh user@machine` (et `-p` pour un autre port), et l'importance de l'**empreinte**
- Mettre en place l'**authentification par clé** (`ssh-keygen`, `ssh-copy-id`), plus sûre que le mot de passe
- Que la clé **privée** ne se partage **jamais**, contrairement à la publique
- Simplifier tes accès avec `~/.ssh/config`
- **Durcir** le serveur SSH (`PermitRootLogin no`, `PasswordAuthentication no`) avec le réflexe `.bak`/`sudoedit`/`diff`
- La prudence vitale pour ne pas se verrouiller dehors lors d'un changement à distance

---


## Chapitre 19 — Transférer des fichiers

### Le minimum à savoir

#### Déplacer des fichiers entre machines, en sécurité

Une fois connecté à distance, tu auras souvent besoin de **transférer des fichiers** : envoyer une configuration vers un serveur, récupérer des logs pour les analyser, déployer un script. Bonne nouvelle : ces transferts s'appuient sur SSH, donc ils sont **chiffrés** par défaut, et réutilisent les accès (clés, config) que tu viens de mettre en place.

#### Copier un fichier : `scp`

`scp` (*secure copy*) copie un fichier vers ou depuis une machine distante, avec une syntaxe proche de `cp` :

```bash
scp fichier.txt alice@serveur:/home/alice/      # ENVOIE le fichier vers le serveur
scp alice@serveur:/var/log/app.log .            # RÉCUPÈRE un fichier distant ICI (.)
scp -r dossier/ alice@serveur:/home/alice/      # -r pour un dossier entier (comme cp)
```

La logique : `scp <source> <destination>`, où une machine distante s'écrit `user@machine:/chemin`. Le `:` sépare la machine du chemin. C'est l'outil le plus simple pour un transfert ponctuel.

> **Note de culture :** sur les versions récentes d'OpenSSH, `scp` s'appuie en interne sur SFTP — pour toi, la syntaxe ne change pas. Retiens simplement le partage des rôles : **`scp` pour une copie ponctuelle**, **`rsync` pour les sauvegardes et synchronisations** (vu juste après).

### Très utile en pratique

#### Synchroniser intelligemment : `rsync`

Pour des transferts plus sérieux (gros dossiers, sauvegardes, synchronisations répétées), `rsync` est bien plus efficace que `scp` : il ne transfère que ce qui a **changé**, peut reprendre un transfert interrompu, et préserve les attributs des fichiers.

```bash
rsync -av dossier/ alice@serveur:/sauvegarde/    # synchronise dossier/ vers le serveur
rsync -av alice@serveur:/data/ ./data/           # synchronise depuis le serveur vers ici
```

Les options de base : `-a` (*archive* : préserve permissions, dates, liens…) et `-v` (*verbose* : affiche ce qui se passe). Une option de sécurité précieuse pour s'entraîner :

```bash
rsync -av --dry-run dossier/ alice@serveur:/sauvegarde/   # SIMULE sans rien transférer
```

> **Très utile en pratique :** `--dry-run` te montre **exactement ce qui serait transféré** sans rien faire. C'est le pendant réseau de la prudence des chapitres précédents : on vérifie avant d'agir. À utiliser systématiquement avant un gros `rsync`.

> **Attention au slash final dans `rsync` :** `rsync dossier/` (avec `/`) copie le **contenu** du dossier ; `rsync dossier` (sans `/`) copie le **dossier lui-même** dans la destination. Cette subtilité change le résultat — d'où l'intérêt du `--dry-run` pour vérifier.

#### Une session interactive : `sftp`

`sftp` ouvre une session interactive de transfert (à la manière d'un FTP, mais sécurisé), où l'on navigue et transfère avec des commandes dédiées (`put` pour envoyer, `get` pour récupérer) :

```bash
sftp alice@serveur       # ouvre une session ; puis: put fichier, get fichier, ls, cd, bye
```

Pratique quand on veut explorer l'arborescence distante avant de choisir quoi transférer. Pour débuter, `scp` (ponctuel) et `rsync` (synchronisation) couvrent l'essentiel des besoins.

### ❌ Erreur classique

```bash
# Oublier le : qui sépare machine et chemin
scp fichier.txt alice@serveur/home/alice    # ❌ sans :, scp ne comprend pas
scp fichier.txt alice@serveur:/home/alice   # ✅ le : est obligatoire

# Oublier -r pour un dossier
scp dossier/ alice@serveur:/tmp/            # ❌ refusé (c'est un dossier)
scp -r dossier/ alice@serveur:/tmp/         # ✅

# Lancer un gros rsync sans simulation
rsync -av gros-dossier/ serveur:/dest/      # ❌ et si la cible/le slash est faux ?
rsync -av --dry-run gros-dossier/ serveur:/dest/   # ✅ simule d'abord

# Se tromper de sens (source/destination inversées)
scp serveur:/data/important .               # récupère DEPUIS le serveur
scp important serveur:/data/                # envoie VERS le serveur — vérifie le sens !
```

### Exercices

**Guidé :** Crée un fichier de test localement. Si tu disposes d'un accès SSH à une autre machine, envoie-le avec `scp fichier.txt user@machine:/tmp/`, puis connecte-toi en SSH et vérifie qu'il est bien arrivé dans `/tmp/`. Sinon, entraîne-toi à la **syntaxe** : écris (sans l'exécuter) la commande qui récupérerait `/var/log/syslog` d'un serveur vers ton dossier courant.

**Autonome :** Crée un dossier avec quelques fichiers. Utilise `rsync -av --dry-run` vers une destination (locale ou distante) et lis attentivement ce que la simulation annonce. Puis, si tu veux, lance le vrai transfert sans `--dry-run` et compare.

**Défi (orientation SOC) :** Imagine que tu doives **récupérer les logs** d'un serveur compromis pour les analyser sur ta machine, sans rien modifier sur le serveur. Quelle commande utiliserais-tu, et pourquoi privilégier `rsync` (préservation des dates et attributs, qui sont des preuves) plutôt qu'une simple copie manuelle ? Écris la commande complète.

### ✅ Tu sais maintenant…

- Que les transferts de fichiers s'appuient sur SSH et sont donc **chiffrés**
- Copier ponctuellement avec `scp` (et `-r` pour les dossiers), syntaxe `user@machine:/chemin`
- **Synchroniser** efficacement avec `rsync -av` (ne transfère que les changements)
- Utiliser `rsync --dry-run` pour **simuler** avant d'agir, et l'importance du slash final
- Explorer et transférer en interactif avec `sftp` (`put`, `get`)
- Faire attention au **sens** source → destination

---

> **🏁 CHECKPOINT 5 — Fin de la Partie 5**
>
> Ta machine n'est plus isolée : tu sais inspecter sa configuration réseau, voir ce qui écoute, t'y connecter à distance en sécurité et y transférer des fichiers. Tu peux désormais administrer une machine **que tu n'as pas physiquement devant toi** — la réalité de la quasi-totalité des serveurs.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - afficher ton adresse IP, ta passerelle, et tester ta connectivité ?
> - lister les ports en écoute et expliquer pourquoi c'est un enjeu de sécurité ?
> - te connecter en SSH et mettre en place une authentification par clé ?
> - citer deux durcissements importants du serveur SSH ?
> - transférer un dossier avec `rsync` en simulant d'abord ?
>
> Si oui, tu maîtrises Linux en réseau. Passons à l'**entretien du système sur la durée** : place à la **Partie 6 — Entretenir le système**.

---

---
---
