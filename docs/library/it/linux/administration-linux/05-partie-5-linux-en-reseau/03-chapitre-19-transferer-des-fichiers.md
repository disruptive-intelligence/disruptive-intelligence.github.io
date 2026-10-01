---
title: Chapitre 19 — Transférer des fichiers
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 5 — Linux en réseau
  - index.md
---

## Le minimum à savoir

### Déplacer des fichiers entre machines, en sécurité

Une fois connecté à distance, tu auras souvent besoin de **transférer des fichiers** : envoyer une configuration vers un serveur, récupérer des logs pour les analyser, déployer un script. Bonne nouvelle : ces transferts s'appuient sur SSH, donc ils sont **chiffrés** par défaut, et réutilisent les accès (clés, config) que tu viens de mettre en place.

### Copier un fichier : `scp`

`scp` (*secure copy*) copie un fichier vers ou depuis une machine distante, avec une syntaxe proche de `cp` :

```bash
scp fichier.txt alice@serveur:/home/alice/      # ENVOIE le fichier vers le serveur
scp alice@serveur:/var/log/app.log .            # RÉCUPÈRE un fichier distant ICI (.)
scp -r dossier/ alice@serveur:/home/alice/      # -r pour un dossier entier (comme cp)
```


La logique : `scp <source> <destination>`, où une machine distante s'écrit `user@machine:/chemin`. Le `:` sépare la machine du chemin. C'est l'outil le plus simple pour un transfert ponctuel.

> **Note de culture :** sur les versions récentes d'OpenSSH, `scp` s'appuie en interne sur SFTP — pour toi, la syntaxe ne change pas. Retiens simplement le partage des rôles : **`scp` pour une copie ponctuelle**, **`rsync` pour les sauvegardes et synchronisations** (vu juste après).

## Très utile en pratique

### Synchroniser intelligemment : `rsync`

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

### Une session interactive : `sftp`

`sftp` ouvre une session interactive de transfert (à la manière d'un FTP, mais sécurisé), où l'on navigue et transfère avec des commandes dédiées (`put` pour envoyer, `get` pour récupérer) :

```bash
sftp alice@serveur       # ouvre une session ; puis: put fichier, get fichier, ls, cd, bye
```


Pratique quand on veut explorer l'arborescence distante avant de choisir quoi transférer. Pour débuter, `scp` (ponctuel) et `rsync` (synchronisation) couvrent l'essentiel des besoins.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Crée un fichier de test localement. Si tu disposes d'un accès SSH à une autre machine, envoie-le avec `scp fichier.txt user@machine:/tmp/`, puis connecte-toi en SSH et vérifie qu'il est bien arrivé dans `/tmp/`. Sinon, entraîne-toi à la **syntaxe** : écris (sans l'exécuter) la commande qui récupérerait `/var/log/syslog` d'un serveur vers ton dossier courant.

**Autonome :** Crée un dossier avec quelques fichiers. Utilise `rsync -av --dry-run` vers une destination (locale ou distante) et lis attentivement ce que la simulation annonce. Puis, si tu veux, lance le vrai transfert sans `--dry-run` et compare.

**Défi (orientation SOC) :** Imagine que tu doives **récupérer les logs** d'un serveur compromis pour les analyser sur ta machine, sans rien modifier sur le serveur. Quelle commande utiliserais-tu, et pourquoi privilégier `rsync` (préservation des dates et attributs, qui sont des preuves) plutôt qu'une simple copie manuelle ? Écris la commande complète.

## ✅ Tu sais maintenant…

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
