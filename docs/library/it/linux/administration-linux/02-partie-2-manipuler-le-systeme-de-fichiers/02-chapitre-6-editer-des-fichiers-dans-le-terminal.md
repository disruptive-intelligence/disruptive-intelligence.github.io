---
title: Chapitre 6 — Éditer des fichiers dans le terminal
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 2 — Manipuler le système de fichiers
  - index.md
---

## Le minimum à savoir

### Pourquoi éditer sans interface graphique ?

Quand tu administres un serveur, tu n'as **pas de souris ni de fenêtres** : tu es connecté en ligne de commande (on verra le SSH en Partie 5). Pour modifier un fichier de configuration, il te faut donc un éditeur qui fonctionne **dans le terminal**. C'est une compétence incontournable : la quasi-totalité du réglage d'un système Linux passe par l'édition de fichiers texte dans `/etc`.

### `nano` : l'éditeur pour débuter

`nano` est simple, lisible, et c'est celui qu'on recommande pour commencer :

```bash
nano notes.txt           # ouvre (ou crée) le fichier dans l'éditeur
```


Une fois dans `nano`, tu tapes ton texte normalement. En bas de l'écran, une **barre d'aide** rappelle les raccourcis. Le symbole `^` y signifie la touche **`Ctrl`**. Les deux à connaître absolument :

- **`Ctrl + O`** → *enregistrer* (puis Entrée pour confirmer le nom)
- **`Ctrl + X`** → *quitter*

> **Le minimum vital dans nano :** écrire, puis `Ctrl + O` pour sauvegarder, puis `Ctrl + X` pour sortir. Avec juste ça, tu peux déjà modifier n'importe quelle configuration.

### `vim` : survivre, au minimum

`vim` (et son ancêtre `vi`) est extrêmement puissant, mais **déroutant** au premier contact. Tu finiras peut-être par l'adorer, mais pour l'instant l'objectif est simple : **savoir en sortir sans paniquer**, car tu tomberas dessus par surprise un jour (certains systèmes l'ouvrent par défaut).

La clé : `vim` a des **modes**. Au démarrage, tu es en mode « commande » (taper du texte ne marche pas comme prévu). Le strict minimum :

- Appuie sur **`i`** → passe en mode *insertion* (là, tu peux taper du texte)
- Appuie sur **`Échap`** → reviens en mode commande
- Tape **`:wq`** puis Entrée → *write & quit* (enregistrer et quitter)
- Tape **`:q!`** puis Entrée → quitter **sans** enregistrer (la sortie de secours)

> **Si tu es coincé dans vim** et que tu veux juste partir sans rien casser : appuie sur `Échap`, puis tape `:q!` et Entrée. Retiens ce `:q!` — c'est ta porte de sortie garantie.

### Écrire sans éditeur : `echo` et les redirections

Pour des modifications très rapides, on peut écrire dans un fichier directement depuis la ligne de commande :

```bash
echo "première ligne" > notes.txt     # > ÉCRASE le fichier avec ce texte
echo "ligne ajoutée" >> notes.txt     # >> AJOUTE à la fin sans rien effacer
```


> **Distinction capitale** (qu'on approfondira au chapitre 7) : `>` **écrase** tout le contenu existant, `>>` **ajoute** à la fin. Confondre les deux sur un fichier important est une erreur classique aux conséquences sérieuses.

## Très utile en pratique

### Le réflexe sauvegarde-avant-modification

C'est la **troisième règle d'or** de la Partie 0, et c'est ici qu'elle prend tout son sens. **Avant de modifier un fichier de configuration, on en fait toujours une copie de sauvegarde.** Si la modification casse quelque chose, on restaure la copie et tout repart.

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. copie de sécurité (.bak)
sudo nano /etc/ssh/sshd_config                           # 2. on modifie
```


L'extension `.bak` est une convention (pour « backup ») : elle n'a rien de magique, mais elle signale clairement « ceci est une sauvegarde ». Si la modification tourne mal :

```bash
sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config    # on restaure, et on est sauvé
```


### `sudoedit` : la bonne façon d'éditer un fichier système

Pour modifier un fichier qui appartient au système (dans `/etc`, par exemple), il faut des droits d'administrateur. On pourrait écrire `sudo nano fichier`, mais il existe **mieux** : `sudoedit`.

```bash
sudoedit /etc/ssh/sshd_config       # (équivalent : sudo -e ...)
```


`sudoedit` t'ouvre le fichier dans une **copie temporaire** avec **ton** éditeur habituel et **tes** réglages, puis réécrit le fichier original à ta place une fois que tu as fini. C'est plus propre et plus sûr que `sudo nano` : ton éditeur ne tourne pas avec les pleins pouvoirs, ce qui limite les dégâts en cas de mauvaise manipulation.

> **Bonne pratique professionnelle :** pour éditer un fichier système, préfère `sudoedit fichier` plutôt que `sudo nano fichier`. *(Pour choisir quel éditeur `sudoedit` lance, on règle la variable d'environnement `EDITOR` — un sujet du chapitre 8.)*

### Comparer deux versions : `diff`

Après une modification, comment savoir **exactement** ce qui a changé ? `diff` compare deux fichiers et n'affiche que les **différences** :

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```


Le workflow complet, propre et professionnel, devient donc :

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak    # 1. sauvegarde
sudoedit /etc/ssh/sshd_config                            # 2. édition sécurisée
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config       # 3. vérification du changement
```


> **Très utile en sécurité :** garder un `.bak` et un `diff` permet de **prouver** ce qui a été modifié dans une configuration, et de revenir à l'état initial en cas de problème. C'est une trace précieuse lors d'un incident.

## ❌ Erreur classique

```bash
# Confondre > et >> et écraser un fichier
echo "nouvelle conf" > /etc/important.conf    # ❌ tout l'ancien contenu est PERDU
echo "ligne en plus" >> /etc/important.conf   # ✅ ajoute sans détruire

# Modifier une config système SANS sauvegarde
sudo nano /etc/ssh/sshd_config                # ❌ et si ça casse ?
sudo cp .../sshd_config .../sshd_config.bak   # ✅ toujours un .bak d'abord

# Rester bloqué dans vim et fermer brutalement le terminal
# ✅ Échap puis :q! suffit pour sortir proprement

# Croire que sudo nano = sudoedit
sudo nano /etc/fichier        # fonctionne, mais l'éditeur tourne en root
sudoedit /etc/fichier         # ✅ plus sûr : édition dans une copie temporaire

# Éditer un fichier système sans les droits
nano /etc/hosts               # ❌ "Permission denied" ou impossible d'enregistrer
sudoedit /etc/hosts           # ✅
```


## Exercices

**Guidé :** Avec `nano`, crée un fichier `~/notes-cours.txt`, écris-y trois lignes décrivant ce que tu as appris jusqu'ici, enregistre avec `Ctrl + O` et quitte avec `Ctrl + X`. Vérifie le contenu avec `cat ~/notes-cours.txt`.

**Autonome :** Crée un fichier `config-test.txt` avec quelques lignes. Fais-en une copie `.bak`. Modifie ensuite l'original (change une ligne, ajoutes-en une) avec l'éditeur de ton choix. Enfin, lance `diff config-test.txt.bak config-test.txt` et lis attentivement ce que `diff` te montre : reconnais-tu tes modifications ?

**Défi :** Ouvre volontairement un fichier avec `vim` (`vim test-vim.txt`). Passe en mode insertion avec `i`, écris une phrase, reviens en mode commande avec `Échap`, puis quitte **sans enregistrer** avec `:q!`. Recommence, mais cette fois enregistre avec `:wq`. Vérifie avec `cat` quel essai a bien été sauvegardé.

## ✅ Tu sais maintenant…

- Pourquoi l'édition en terminal est indispensable en administration
- Éditer simplement avec `nano` (sauver `Ctrl + O`, quitter `Ctrl + X`)
- **Survivre dans `vim`** : `i` pour écrire, `Échap`, puis `:wq` (enregistrer) ou `:q!` (sortie de secours)
- Écrire vite avec `echo >` (écrase) et `echo >>` (ajoute)
- Le **réflexe `.bak`** avant toute modification de configuration
- Éditer proprement un fichier système avec `sudoedit` (mieux que `sudo nano`)
- Vérifier précisément un changement avec `diff`

---
