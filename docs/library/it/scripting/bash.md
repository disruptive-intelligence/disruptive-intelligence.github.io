---
title: Bash
source: IT/05_Scripting_Langage-Prog/Bash.md
---

### De zéro à l'automatisation — Guide pour débutant absolu

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c'est un ordinateur avec Linux (ou un terminal Bash sur Mac/Windows via WSL).

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Terminal** | La fenêtre noire où tu tapes des commandes texte |
| **Shell** | Le programme qui lit et exécute tes commandes (Bash est un shell) |
| **Script** | Un fichier texte contenant une liste de commandes à exécuter |
| **Variable** | Un conteneur avec un nom qui stocke une valeur |
| **Argument** | Une info que tu donnes à un script quand tu le lances |
| **Commande** | Une instruction que le shell sait exécuter (`echo`, `ls`, `cd`...) |
| **Sortie standard (stdout)** | Là où une commande affiche son résultat (l'écran par défaut) |
| **Sortie d'erreur (stderr)** | Là où une commande affiche ses erreurs (l'écran aussi par défaut) |
| **Code de retour** | Un nombre (0 = succès, autre = erreur) que chaque commande renvoie |
| **Boucle** | Un mécanisme qui répète des commandes plusieurs fois |
| **Fonction** | Un bloc de code réutilisable auquel on donne un nom |
| **Pipe** | Un "tuyau" (`\|`) qui envoie la sortie d'une commande vers une autre |

---

### Comment penser un script

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

Concrètement, il n'y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier...)
2. **Stocker** des informations dans des variables
3. **Tester** si quelque chose est vrai ou faux (conditions)
4. **Répéter** une action plusieurs fois (boucles)
5. **Afficher ou enregistrer** un résultat (sortie)

Tous les scripts, même les plus complexes, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

---

### Table des matières

1. [Découverte de Bash et premier script](#chapitre-1-decouverte-de-bash-et-premier-script)
2. [Variables, affichage et saisie utilisateur](#chapitre-2-variables-affichage-et-saisie-utilisateur)
3. [Arguments et variables spéciales](#chapitre-3-arguments-et-variables-speciales)
4. [Redirections, erreurs et pipes](#chapitre-4-redirections-erreurs-et-pipes)
5. [Opérateurs, calculs et logique](#chapitre-5-operateurs-calculs-et-logique)
6. [Conditions, comparaisons et tests](#chapitre-6-conditions-comparaisons-et-tests)
7. [Boucles](#chapitre-7-boucles)
8. [Fonctions et case](#chapitre-8-fonctions-et-case)
9. [Chaînes de caractères](#chapitre-9-chaines-de-caracteres)
10. [Tableaux](#chapitre-10-tableaux)
11. [Déboguer et écrire des scripts propres](#chapitre-11-deboguer-et-ecrire-des-scripts-propres)
12. [Cas pratiques et automatisation](#chapitre-12-cas-pratiques-et-automatisation)

---

## Chapitre 1 — Découverte de Bash et premier script

### Le minimum à savoir

#### Le terminal et le shell

Le **terminal**, c'est une fenêtre où tu tapes des commandes en texte au lieu de cliquer sur des icônes. Le **shell**, c'est le programme à l'intérieur du terminal qui comprend et exécute ces commandes. Le shell le plus répandu s'appelle **Bash**.

Pour ouvrir un terminal :

- **Linux** : `Ctrl + Alt + T` ou cherche "Terminal" dans tes applications
- **Mac** : cherche "Terminal" dans Spotlight
- **Windows** : installe WSL (Windows Subsystem for Linux)

Vérifie que tu utilises bien Bash :

```bash
echo $SHELL
```

Tu devrais voir `/bin/bash`.

#### Quelques commandes pour se familiariser

Tape ces commandes dans ton terminal pour te familiariser :

```bash
echo "Bonjour !"       # Afficher du texte
pwd                     # Où suis-je ? (quel dossier)
ls                      # Qu'est-ce qu'il y a ici ? (liste des fichiers)
date                    # Quelle date et heure ?
whoami                  # Qui suis-je ? (nom d'utilisateur)
```

> **À retenir :** le symbole `#` marque un **commentaire**. Bash ignore tout ce qui suit un `#`. Les commentaires servent à expliquer ton code.

#### Ton premier script en 5 étapes

Un script, c'est simplement **plusieurs commandes rangées dans un fichier**. Au lieu de les taper une par une, tu les écris une fois et tu les lances quand tu veux.

**Étape 1 — Crée un dossier de travail :**

```bash
mkdir -p ~/mes_scripts
cd ~/mes_scripts
```

**Étape 2 — Crée le fichier :**

```bash
nano hello.sh
```

> **Bonne pratique :** l'extension `.sh` indique que c'est un script Bash. Ce n'est pas obligatoire, mais c'est une convention utile.

**Étape 3 — Écris le script :**

```bash
#!/bin/bash
# Mon tout premier script
echo "Hello, World !"
echo "Je suis un script Bash !"
```

Sauvegarde (`Ctrl + O` puis Entrée dans nano) et quitte (`Ctrl + X`).

**Étape 4 — Rends-le exécutable :**

```bash
chmod +x hello.sh
```

**Étape 5 — Lance-le :**

```bash
./hello.sh
```

Résultat :

```
Hello, World !
Je suis un script Bash !
```

Félicitations, tu viens d'écrire et d'exécuter ton premier script !

#### Le shebang : `#!/bin/bash`

La première ligne `#!/bin/bash` s'appelle le **shebang**. Elle dit au système : "ce fichier doit être lu par Bash".

Sans shebang, le système ne sait pas quel langage utiliser. Avec le shebang, tu peux lancer ton script avec `./script.sh` directement.

> **À retenir :** mets TOUJOURS `#!/bin/bash` en première ligne de tes scripts.

#### Pourquoi `./` devant le script ?

Quand tu tapes `ls` ou `date`, le système sait où trouver ces commandes grâce à une variable appelée `PATH`. Ton dossier personnel n'est pas dans le `PATH`, donc il faut préciser "cherche dans le dossier actuel" avec `./`.

#### La commande `exit`

`exit` permet de terminer un script avec un **code de sortie** :

```bash
#!/bin/bash
echo "Ce message s'affiche"
exit 0
echo "Ceci ne s'affichera JAMAIS"
```

Les codes essentiels :

| Code | Signification |
|------|--------------|
| **`0`** | **Succès** (tout s'est bien passé) |
| **`1`** | **Erreur générale** |
| **`127`** | **Commande introuvable** |

> **À retenir :** en Bash, `0` = succès, tout autre nombre = erreur. C'est l'inverse de ce qu'on pourrait penser !

> Pour info, d'autres codes existent (`2` = mauvaise utilisation, `130` = Ctrl+C, `126` = pas le droit d'exécuter), mais tu n'as pas besoin de les mémoriser maintenant.

### ❌ Erreur classique

```bash
# Oublier le shebang → le script peut ne pas fonctionner avec ./script.sh
# Oublier chmod +x → "Permission denied" quand tu lances le script
# Oublier le ./ → "command not found"
```

### Exercices

**Guidé :** Crée un script `salut.sh` qui affiche deux lignes : "Bonjour !" puis "Bienvenue dans le monde du scripting."

**Autonome :** Crée un script `info.sh` qui affiche ton nom d'utilisateur (`whoami`), la date (`date`), et le dossier actuel (`pwd`) sur des lignes séparées.

### ✅ Tu sais maintenant...

- Ce qu'est un terminal, un shell et un script
- Créer un fichier script avec le shebang `#!/bin/bash`
- Rendre un script exécutable avec `chmod +x`
- Lancer un script avec `./mon_script.sh`
- Ce que signifie un code de sortie

---

## Chapitre 2 — Variables, affichage et saisie utilisateur

### Le minimum à savoir

#### Qu'est-ce qu'une variable ?

Une variable, c'est un **conteneur avec une étiquette**. L'étiquette c'est le nom, et à l'intérieur il y a une valeur.

```
┌─────────────────┐
│  prenom = Alice  │   ← "prenom" est le nom, "Alice" est la valeur
└─────────────────┘
```

#### Créer et afficher une variable

```bash
#!/bin/bash

prenom="Alice"
echo "Bonjour, $prenom !"
```

Résultat : `Bonjour, Alice !`

**Règle critique : PAS d'espace autour du `=`**

```bash
# ✅ CORRECT
prenom="Alice"

# ❌ FAUX — Bash croit que "prenom" est une commande
prenom = "Alice"
```

Pour accéder au contenu d'une variable, on met `$` devant son nom. Sans le `$`, Bash affiche le texte brut :

```bash
echo "Bonjour, $prenom"     # → Bonjour, Alice
echo "Bonjour, prenom"      # → Bonjour, prenom
```

> **Bonne pratique :** écris `"$prenom"` (avec guillemets) plutôt que `$prenom` nu. Ça évite des problèmes si la valeur contient des espaces. Prends ce réflexe dès maintenant.

#### La forme avec accolades `${variable}`

Les accolades servent à éviter les ambiguïtés :

```bash
animal="chat"
echo "J'ai 3 ${animal}s"    # → J'ai 3 chats
echo "J'ai 3 $animals"      # → J'ai 3  (Bash cherche la variable "animals" qui n'existe pas)
```

#### Modifier une variable

Tu peux changer la valeur à tout moment :

```bash
#!/bin/bash
humeur="content"
echo "Je suis $humeur"

humeur="fatigué"
echo "Maintenant je suis $humeur"
```

#### Guillemets simples vs doubles

```bash
prenom="Alice"

echo "Bonjour, $prenom"    # Guillemets doubles → Bash remplace la variable
# → Bonjour, Alice

echo 'Bonjour, $prenom'    # Guillemets simples → tout est affiché tel quel
# → Bonjour, $prenom
```

> **À retenir :**
> - **Guillemets doubles `" "`** → Bash interprète les variables
> - **Guillemets simples `' '`** → tout est littéral, aucune interprétation

#### Lire une saisie utilisateur avec `read`

La commande `read` demande à l'utilisateur de taper quelque chose :

```bash
#!/bin/bash

read -p "Ton prénom : " prenom
read -p "Ton âge : " age
echo "Tu es $prenom et tu as $age ans."
```

Exécution :

```
Ton prénom : Alice
Ton âge : 25
Tu es Alice et tu as 25 ans.
```

`-p` permet de mettre le message et la saisie sur la même ligne. C'est la forme la plus pratique.

### Très utile en pratique

#### La substitution de commande

Tu peux **stocker le résultat d'une commande** dans une variable avec `$(commande)` :

```bash
#!/bin/bash

aujourdhui=$(date)
echo "Nous sommes le : $aujourdhui"

utilisateur=$(whoami)
echo "Connecté en tant que : $utilisateur"

nb_fichiers=$(ls | wc -l)
echo "Il y a $nb_fichiers éléments dans ce dossier"
```

> **À retenir :** `$(commande)` exécute la commande et renvoie son résultat. C'est l'une des fonctionnalités les plus puissantes de Bash.

#### Les variables d'environnement

Ton système contient des variables déjà définies :

```bash
echo "Utilisateur : $USER"
echo "Dossier personnel : $HOME"
echo "Shell actuel : $SHELL"
echo "Dossier actuel : $PWD"
```

#### Variables en lecture seule

Pour qu'une variable ne puisse jamais être modifiée :

```bash
readonly PI=3.14159
PI=3.0    # → Erreur ! bash: PI: readonly variable
```

### Bonus

#### Note sur les "types" en Bash

En Bash, une variable contient surtout du texte. Même les nombres sont manipulés comme du texte, sauf quand tu fais du calcul (chapitre 5). Il n'y a pas de système de types strict comme dans d'autres langages. Ne te préoccupe pas de ça pour l'instant.

#### Autres options de `read`

```bash
read -p "Mot de passe : " -s motdepasse    # -s : saisie invisible
read -p "Choix rapide : " -t 5 choix        # -t 5 : timeout de 5 secondes
```

### ❌ Erreur classique

```bash
prenom = "Alice"     # ❌ Espaces autour du = → Bash croit que "prenom" est une commande
prenom="Alice"       # ✅ Correct

echo $prenom         # ⚠️ Fonctionne, mais risqué si la valeur contient des espaces
echo "$prenom"       # ✅ Toujours préférer cette forme
```

### Exercices

**Guidé :** Crée un script `presentation.sh` qui demande le prénom et l'âge avec `read -p`, puis affiche "Tu es [prénom] et tu as [âge] ans."

**Autonome :** Crée un script `machine.sh` qui affiche le nom de l'utilisateur, la date et le nom de la machine (`hostname`) en utilisant la substitution de commande `$(...)`.

### 🧩 Mini-projet (chapitres 1-2)

Crée un script `bienvenue.sh` qui :
1. Affiche "Bienvenue sur cette machine !"
2. Affiche la date du jour (avec substitution de commande)
3. Demande le prénom de l'utilisateur
4. Affiche "Bonjour [prénom], connecté en tant que [whoami]"

### ✅ Tu sais maintenant...

- Créer une variable et l'afficher avec `$`
- La différence entre guillemets simples et doubles
- Lire une saisie utilisateur avec `read -p`
- Stocker le résultat d'une commande avec `$(commande)`

---

## Chapitre 3 — Arguments et variables spéciales

### Le minimum à savoir

#### C'est quoi un argument ?

Au lieu que le script pose des questions (avec `read`), tu peux lui **donner des infos directement** quand tu le lances :

```bash
./saluer.sh Alice
#                 ↑ c'est un argument
```

#### Les paramètres positionnels

Chaque argument est stocké dans une variable numérotée :

```
./mon_script.sh  pomme   banane  cerise
       $0          $1      $2      $3
```

- `$0` → le nom du script
- `$1` → le premier argument
- `$2` → le deuxième
- `$3` → le troisième...

Exemple :

```bash
#!/bin/bash
echo "Bonjour, $1 !"
```

```bash
./saluer.sh Alice     # → Bonjour, Alice !
./saluer.sh Bob       # → Bonjour, Bob !
```

#### Les variables spéciales essentielles

| Variable      | Contenu                                       |
| ------------- | --------------------------------------------- |
| `$0`          | Le nom du script                              |
| `$1`, `$2`... | Les arguments par position                    |
| `$#`          | Le **nombre** d'arguments                     |
| `$@`          | **Tous** les arguments (séparément)           |
| `$?`          | Le **code de sortie** de la dernière commande |

Exemple :

```bash
#!/bin/bash

echo "Nom du script : $0"
echo "Nombre d'arguments : $#"
echo "Tous les arguments : $@"
echo "Premier : $1"
echo "Deuxième : $2"
```

```bash
./infos.sh pomme banane cerise
```

```
Nom du script : ./infos.sh
Nombre d'arguments : 3
Tous les arguments : pomme banane cerise
Premier : pomme
Deuxième : banane
```

#### Vérifier qu'un argument est fourni

Un script qui attend un argument devrait **toujours vérifier** qu'il a été donné :

```bash
#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Erreur : donne un prénom en argument !"
    echo "Utilisation : $0 <prénom>"
    exit 1
fi

echo "Bonjour, $1 !"
```

> **Explication :** `-z` teste si la chaîne est vide. Si `$1` est vide (= pas d'argument), on affiche un message d'erreur et on quitte. On verra les conditions en détail au chapitre 6.

#### La variable `$?`

Chaque commande renvoie un code de sortie. `$?` contient le code de la **dernière commande** :

```bash
ls /tmp
echo $?           # → 0 (succès, le dossier existe)

ls /dossier_inexistant
echo $?           # → 2 (erreur, le dossier n'existe pas)
```

### Très utile en pratique

#### Utiliser plusieurs arguments

```bash
#!/bin/bash
echo "Comparaison de $1 et $2"
echo "Taille de $1 :"
wc -c < "$1"
echo "Taille de $2 :"
wc -c < "$2"
```

> **Bonne pratique :** mets toujours `"$1"` entre guillemets (pas `$1` nu). Ça évite les problèmes si le nom de fichier contient des espaces.

#### Différence entre `$@` et `$*`

```bash
./test.sh "Jean Pierre" Marie
```

- `"$@"` → préserve chaque argument : `"Jean Pierre"` et `"Marie"` (2 éléments)
- `"$*"` → fusionne tout : `"Jean Pierre Marie"` (1 seul bloc)

**Utilise `"$@"` dans la grande majorité des cas.**

### Bonus

#### La variable `$$`

`$$` contient le numéro de processus (PID) du script. Utile pour créer des fichiers temporaires uniques :

```bash
fichier_temp="/tmp/script_$$.tmp"
```

#### La commande `shift`

`shift` décale tous les arguments d'une position : `$2` devient `$1`, `$3` devient `$2`, etc. On l'utilisera au chapitre 8 pour parser des options avancées.

### ❌ Erreur classique

```bash
# Oublier de vérifier si l'argument existe
echo "Bonjour, $1"    # Si lancé sans argument → "Bonjour, " (chaîne vide, pas d'erreur)

# Ne pas mettre de guillemets
cat $1                 # ❌ Plante si le fichier s'appelle "mon document.txt"
cat "$1"               # ✅ Correct
```

### Exercices

**Guidé :** Crée un script `bonjour_arg.sh` qui prend un prénom en argument, vérifie qu'il est fourni, et affiche "Bonjour, [prénom] !"

**Autonome :** Crée un script `chercher.sh` qui prend un nom de fichier en argument et le cherche sur le système : `find / -iname "$1" 2>/dev/null`

### ✅ Tu sais maintenant...

- Passer des arguments à un script (`$1`, `$2`...)
- Connaître le nombre d'arguments avec `$#`
- Récupérer tous les arguments avec `$@`
- Vérifier le code de retour avec `$?`
- Vérifier qu'un argument existe avant de l'utiliser

---

## Chapitre 4 — Redirections, erreurs et pipes

### Le minimum à savoir

#### Les 3 flux de données

Chaque commande travaille avec trois flux :

```
                  ┌──────────────┐
  Entrée ───────▶ │   Commande   │ ──▶ 1 = Sortie normale (stdout)
  (clavier)       │              │ ──▶ 2 = Erreurs (stderr)
                  └──────────────┘
```

| Numéro | Nom                         | Par défaut  |
| ------ | --------------------------- | ----------- |
| 0      | stdin (entrée)              | Le clavier  |
| **1**  | **stdout (sortie normale)** | **L'écran** |
| **2**  | **stderr (erreurs)**        | **L'écran** |

Les redirections permettent de **changer la destination** de ces flux.

#### Rediriger la sortie vers un fichier

**Écraser avec `>` :**

```bash
echo "Bonjour" > message.txt   # Crée le fichier (ou l'écrase !)
ls /etc > liste.txt            # La liste va dans le fichier
```

**Ajouter avec `>>` :**

```bash
echo "Ligne 1" > journal.txt       # Crée le fichier
echo "Ligne 2" >> journal.txt      # Ajoute à la suite
echo "Ligne 3" >> journal.txt      # Ajoute encore
```

> **À retenir :** `>` écrase, `>>` ajoute. Confondre les deux = perdre des données.

#### Rediriger les erreurs

```bash
# Les erreurs vont dans un fichier, la sortie normale s'affiche à l'écran
ls /dossier_inexistant 2> erreurs.txt

# Masquer les erreurs en les envoyant dans le "trou noir"
find / -name "mon_fichier" 2>/dev/null
```

`/dev/null` est une "poubelle" : tout ce qu'on y envoie disparaît.

#### Rediriger tout (sortie + erreurs)

```bash
# Tout va dans le même fichier
./mon_script.sh > log.txt 2>&1 # > log.txt 2>&1 = "flux 1 va dans log.txt, et flux 2 suit flux 1" → tout finit dans log.txt.

# Tout dans le vide (script silencieux)
./mon_script.sh > /dev/null 2>&1
```

> **Explication de `2>&1` :** "envoie le flux 2 (erreurs) au même endroit que le flux 1 (sortie normale)".

#### Les pipes `|`

Le pipe envoie la **sortie d'une commande comme entrée d'une autre**. C'est l'outil le plus puissant de Bash.

```bash
# Compter le nombre de fichiers
ls | wc -l

# Chercher un mot dans un résultat
ps aux | grep firefox

# Trier et garder les lignes uniques
cat prenoms.txt | sort | uniq
```

Chaque commande reçoit la sortie de la précédente. C'est une chaîne de traitement.

> **Note :** ces exemples sont volontairement simples pour comprendre le principe d'un pipe. Tu verras plus tard qu'en Bash, certaines alternatives sont plus robustes selon le contexte.

#### La commande `tee`

`tee` permet d'**afficher ET sauvegarder** en même temps :

```bash
# Affiche à l'écran ET écrit dans log.txt
ls -la | tee log.txt

# Ajouter au fichier (au lieu d'écraser)
date | tee -a journal.log
```

### Très utile en pratique

#### Rediriger l'entrée avec `<`

```bash
# Compter les lignes d'un fichier
wc -l < mon_fichier.txt

# Trier le contenu d'un fichier
sort < liste_noms.txt
```

#### Enchaîner plusieurs pipes

```bash
# Les 5 plus gros fichiers
ls -lS | head -5

# Compter les fichiers .txt dans /etc
ls /etc | grep "\.txt" | wc -l
```

### Récapitulatif

| Syntaxe                     | Effet                           |
| --------------------------- | ------------------------------- |
| `commande > fichier`        | Sortie dans fichier (écrase)    |
| `commande >> fichier`       | Sortie dans fichier (ajoute)    |
| `commande 2> fichier`       | Erreurs dans fichier            |
| `commande > fichier 2>&1`   | Tout dans fichier               |
| `commande < fichier`        | Entrée depuis un fichier        |
| `cmd1 \| cmd2`              | Sortie de cmd1 → entrée de cmd2 |
| `commande \| tee fichier`   | Affiche ET sauvegarde           |
| `commande > /dev/null 2>&1` | Silence total                   |

### ❌ Erreur classique

```bash
# Confondre > et >> : tu écrases un fichier important !
echo "nouveau" > config.txt     # ❌ Tout l'ancien contenu est perdu
echo "nouveau" >> config.txt    # ✅ Ajoute à la fin

# Oublier 2> : les erreurs s'affichent en vrac et polluent la sortie
find / -name "*.log"            # ❌ Des dizaines de "Permission denied"
find / -name "*.log" 2>/dev/null  # ✅ Erreurs masquées
```

### Exercices

**Guidé :** Écris le résultat de `date` dans un fichier `log.txt` avec `>`, puis ajoute une deuxième date avec `>>`. Affiche le contenu avec `cat log.txt`.

**Autonome :** Crée un script qui compte le nombre de lignes de `/etc/passwd` en utilisant un pipe (`wc -l`), et qui utilise `tee` pour afficher le résultat ET l'écrire dans un fichier.

### 🧩 Mini-projet (chapitres 3-4)

Crée un script `rapport.sh` qui :
1. Prend un dossier en argument (vérifie qu'il est fourni)
2. Compte le nombre de fichiers dans ce dossier (`ls "$1" | wc -l`)
3. Écrit un mini-rapport dans `rapport.txt` avec la date, le dossier, et le nombre de fichiers
4. Affiche le rapport à l'écran avec `cat`

### ✅ Tu sais maintenant...

- Rediriger la sortie vers un fichier (`>`, `>>`)
- Rediriger les erreurs (`2>`, `2>&1`)
- Masquer les erreurs avec `/dev/null`
- Enchaîner des commandes avec le pipe `|`
- Afficher et sauvegarder en même temps avec `tee`

---

## Chapitre 5 — Opérateurs, calculs et logique

### Le minimum à savoir

#### Le calcul en Bash

Bash peut faire des calculs avec des nombres entiers. La syntaxe est `$(( expression ))` :

```bash
#!/bin/bash

a=10
b=3

echo "Addition      : $((a + b))"      # 13
echo "Soustraction  : $((a - b))"      # 7
echo "Multiplication: $((a * b))"      # 30
echo "Division      : $((a / b))"      # 3 (entière, pas de virgule !)
echo "Modulo        : $((a % b))"      # 1 (reste de la division)
```

> **Attention :** la division est **entière**. `10 / 3` donne `3`, pas `3.33`.

#### Stocker un résultat

```bash
prix=50
reduction=15
prix_final=$((prix - reduction))
echo "Le prix final est $prix_final euros"
```

#### Les opérateurs arithmétiques

| Opérateur | Signification    | Exemple       | Résultat |
| --------- | ---------------- | ------------- | -------- |
| `+`       | Addition         | `$((5 + 3))`  | `8`      |
| `-`       | Soustraction     | `$((5 - 3))`  | `2`      |
| `*`       | Multiplication   | `$((5 * 3))`  | `15`     |
| `/`       | Division entière | `$((5 / 3))`  | `1`      |
| `%`       | Modulo (reste)   | `$((5 % 3))`  | `2`      |
| `**`      | Puissance        | `$((2 ** 3))` | `8`      |

#### Comparer des nombres

Pour tester si un nombre est plus grand, plus petit, égal à un autre :

| Opérateur | Signification     | Moyen mnémotechnique     |
| --------- | ----------------- | ------------------------ |
| `-eq`     | Égal              | **eq**ual                |
| `-ne`     | Différent         | **n**ot **e**qual        |
| `-lt`     | Inférieur         | **l**ess **t**han        |
| `-le`     | Inférieur ou égal | **l**ess or **e**qual    |
| `-gt`     | Supérieur         | **g**reater **t**han     |
| `-ge`     | Supérieur ou égal | **g**reater or **e**qual |

```bash
age=25
[[ $age -ge 18 ]]    # Est-ce que 25 ≥ 18 ? → Vrai
[[ $age -eq 30 ]]    # Est-ce que 25 = 30 ? → Faux
```

> **Ne pas confondre :** `=` sert à **affecter** une valeur à une variable (`age=25`). `-eq` sert à **comparer** deux nombres dans un test.

#### Comparer des chaînes de texte

| Opérateur   | Signification                |
| ----------- | ---------------------------- |
| `=` ou `==` | Les chaînes sont identiques  |
| `!=`        | Les chaînes sont différentes |
| `-z`        | La chaîne est vide           |
| `-n`        | La chaîne n'est pas vide     |

```bash
nom="Alice"
[[ "$nom" == "Alice" ]]    # Vrai
[[ "$nom" != "Bob" ]]      # Vrai
[[ -z "$nom" ]]            # Faux (pas vide)
```

#### Les opérateurs logiques

| Opérateur | Signification                                |
| --------- | -------------------------------------------- |
| `&&`      | ET — les deux conditions doivent être vraies |
| `\|\|`    | OU — au moins une doit être vraie            |
| `!`       | NON — inverse la condition                   |

```bash
age=25
[[ $age -ge 18 && $age -le 65 ]]    # Vrai : entre 18 et 65

[[ $age -lt 10 || $age -gt 60 ]]     # Faux : ni < 10, ni > 60

[[ ! $age -lt 18 ]]                   # Vrai : 25 n'est PAS < 18
```

#### Raccourcis avec `&&` et `||` entre commandes

```bash
# Si la commande réussit, ALORS fait ceci
mkdir mon_dossier && echo "Dossier créé !"

# Si la commande échoue, ALORS fait cela
cd /inexistant || echo "Le dossier n'existe pas"
```

### Très utile en pratique

#### Les tests sur les fichiers

| Opérateur    | Signification             |
| ------------ | ------------------------- |
| `-e fichier` | Le fichier existe         |
| `-f fichier` | C'est un fichier normal   |
| `-d fichier` | C'est un dossier          |
| `-s fichier` | Le fichier n'est pas vide |
| `-r fichier` | Le fichier est lisible    |
| `-w fichier` | Le fichier est modifiable |
| `-x fichier` | Le fichier est exécutable |

```bash
[[ -f "/etc/passwd" ]]    # Vrai (le fichier existe)
[[ -d "/home" ]]          # Vrai (c'est un dossier)
```

#### Incrémenter un compteur

```bash
compteur=0
((compteur++))       # → 1
((compteur++))       # → 2
((compteur += 5))    # → 7
```

### Bonus

#### Le calcul décimal avec `bc`

Pour les nombres à virgule, utilise `bc` :

```bash
echo "scale=2; 10 / 3" | bc
# → 3.33

resultat=$(echo "scale=2; 10 / 3" | bc)
echo "Le résultat est $resultat"
```

#### Comparer avec `(( ))` (syntaxe mathématique)

Dans les doubles parenthèses, tu peux utiliser les symboles habituels :

```bash
a=10
(( a > 5 ))     # Vrai
(( a == 10 ))   # Vrai
```

> **Note :** dans `(( ))`, pas besoin de `$` devant les variables.

### 🔧 Quand ça plante : lire un code de retour

Quand quelque chose ne marche pas, vérifie `$?` :

```bash
ma_commande
echo "Code de retour : $?"
# 0 = tout va bien, autre chose = problème
```

### ❌ Erreur classique

```bash
# Confondre = (affectation) et -eq (comparaison)
if [[ $age = 18 ]]; then     # ⚠️ Compare comme du TEXTE, pas un nombre
if [[ $age -eq 18 ]]; then   # ✅ Compare comme un NOMBRE

# Oublier $(( )) pour le calcul
resultat=5+3                  # ❌ resultat vaut le TEXTE "5+3"
resultat=$((5 + 3))           # ✅ resultat vaut le NOMBRE 8
```

### Exercices

**Guidé :** Crée un script `calculatrice.sh` qui prend deux nombres en arguments et affiche leur somme, différence et produit.

**Autonome :** Crée un script `est_pair.sh` qui prend un nombre en argument et dit s'il est pair ou impair (indice : un nombre est pair si `nombre % 2` vaut 0).

### ✅ Tu sais maintenant...

- Faire des calculs avec `$(( ))`
- Comparer des nombres (`-eq`, `-lt`, `-gt`...)
- Comparer des chaînes (`==`, `!=`, `-z`, `-n`)
- Combiner des conditions avec `&&`, `||`, `!`
- Tester des propriétés de fichiers (`-f`, `-d`, `-e`)

---

## Chapitre 6 — Conditions, comparaisons et tests

### Le minimum à savoir

#### La structure `if`

```bash
if [[ condition ]]; then
    # code si la condition est vraie
fi
```

> **Note :** `fi` c'est `if` à l'envers. C'est la fermeture du bloc.

Exemple simple :

```bash
#!/bin/bash

nombre=15
if [[ $nombre -gt 10 ]]; then
    echo "Le nombre est supérieur à 10"
fi
```

**Règles de syntaxe :**

- Espace après `[[` et avant `]]`
- Espace autour de l'opérateur
- `then` sur la même ligne (avec `;`) ou sur la ligne suivante

#### `if...else`

```bash
#!/bin/bash

nombre=5
if [[ $nombre -gt 10 ]]; then
    echo "Supérieur à 10"
else
    echo "Inférieur ou égal à 10"
fi
```

#### `if...elif...else`

```bash
#!/bin/bash

age=$1

if [[ $age -lt 13 ]]; then
    echo "Tu es un enfant."
elif [[ $age -lt 18 ]]; then
    echo "Tu es un adolescent."
elif [[ $age -lt 65 ]]; then
    echo "Tu es un adulte."
else
    echo "Tu es un senior."
fi
```

> **À retenir :** autant de `elif` que tu veux, mais un seul `else` (à la fin), et un seul `fi`.

#### Les 6 tests les plus utiles

Pour débuter, ces 6 tests couvrent 90% des besoins :

| Test | Signification | Exemple |
|------|--------------|---------|
| `-f` | Le fichier existe | `[[ -f "config.txt" ]]` |
| `-d` | Le dossier existe | `[[ -d "/home" ]]` |
| `-e` | Le chemin existe (fichier ou dossier) | `[[ -e "$1" ]]` |
| `-z` | La chaîne est vide | `[[ -z "$nom" ]]` |
| `-n` | La chaîne n'est pas vide | `[[ -n "$nom" ]]` |
| `-gt` | Le nombre est supérieur | `[[ $a -gt $b ]]` |

#### Exemple concret : vérifier un fichier

```bash
#!/bin/bash

fichier=$1

if [[ -z "$fichier" ]]; then
    echo "Erreur : donne un chemin en argument."
    exit 1
fi

if [[ -f "$fichier" ]]; then
    echo "$fichier est un fichier."
elif [[ -d "$fichier" ]]; then
    echo "$fichier est un dossier."
else
    echo "$fichier n'existe pas."
fi
```

#### Combiner des conditions

```bash
#!/bin/bash

age=$1
nom=$2

# ET : les deux doivent être vraies
if [[ $age -ge 18 && "$nom" == "Alice" ]]; then
    echo "Alice est majeure."
fi

# OU : au moins une doit être vraie
if [[ $age -lt 10 || $age -gt 80 ]]; then
    echo "Âge extrême."
fi
```

### Très utile en pratique

#### Les conditions imbriquées

Tu peux mettre un `if` dans un autre `if` :

```bash
#!/bin/bash

temperature=$1

if [[ $temperature -gt 0 ]]; then
    if [[ $temperature -lt 15 ]]; then
        echo "Il fait frais."
    elif [[ $temperature -lt 25 ]]; then
        echo "Il fait bon."
    else
        echo "Il fait chaud."
    fi
else
    echo "Il gèle !"
fi
```

> **Conseil :** si tes conditions imbriquées dépassent 2-3 niveaux, c'est signe qu'il faut simplifier.

#### `[ ]` vs `[[ ]]` — ce qu'il faut savoir

Dans ce cours, on utilise `[[ ]]` (la syntaxe moderne). Mais tu verras souvent `[ ]` dans des scripts existants sur internet. C'est l'ancienne syntaxe. Elle fonctionne, mais elle est plus fragile (elle plante si une variable est vide et non protégée par des guillemets).

```bash
# Avec [ ] — risqué si $nom est vide
[ $nom = "Alice" ]     # ❌ Erreur si $nom est vide

# Avec [[ ]] — pas de problème
[[ $nom == "Alice" ]]  # ✅ Fonctionne même si $nom est vide
```

**Règle simple :** utilise `[[ ]]` dans tes scripts. Si tu vois `[ ]` ailleurs, sache que c'est l'équivalent en plus ancien.

### ❌ Erreur classique

```bash
# Oublier then
if [[ $a -gt 5 ]]      # ❌ Erreur : "then" manquant
    echo "Grand"
fi

# Oublier les espaces
if [[$a -gt 5]]; then   # ❌ Erreur : pas d'espace
if [[ $a -gt 5 ]]; then # ✅ Correct

# Utiliser > pour comparer des nombres
if [[ $a > $b ]]; then      # ⚠️ Compare comme du TEXTE, pas des nombres
if [[ $a -gt $b ]]; then    # ✅ Compare comme des NOMBRES

# Oublier fi
if [[ $a -gt 5 ]]; then
    echo "Grand"
                             # ❌ Erreur : fi manquant
```

### Exercices

**Guidé :** Crée un script `meteo.sh` qui prend une température en argument et affiche "Il gèle" (< 0), "Froid" (0-15), "Bon" (15-25), ou "Chaud" (> 25).

**Autonome :** Crée un script `verifier.sh` qui prend un chemin en argument et dit si c'est un fichier, un dossier, ou si ça n'existe pas. Pense à vérifier que l'argument est fourni.

### 🧩 Mini-projet (chapitres 5-6)

Crée un script `acces.sh` qui :
1. Prend un chemin de fichier en argument
2. Vérifie qu'il existe (`-e`)
3. Si c'est un fichier (`-f`), affiche s'il est lisible (`-r`), modifiable (`-w`) et exécutable (`-x`)
4. Si c'est un dossier (`-d`), compte le nombre d'éléments qu'il contient (`ls "$1" | wc -l`)

### ✅ Tu sais maintenant...

- Écrire des conditions avec `if / elif / else / fi`
- Utiliser `[[ ]]` pour les tests
- Tester des fichiers (`-f`, `-d`, `-e`)
- Combiner des conditions avec `&&` et `||`
- La différence entre `[[ ]]` (moderne) et `[ ]` (ancien)

---

## Chapitre 7 — Boucles

### Le minimum à savoir

#### À quoi servent les boucles ?

Les boucles répètent des actions. Tu dois renommer 200 fichiers ? Vérifier 50 serveurs ? Tu n'écris pas 200 commandes : tu écris une boucle.

Il y a deux façons de penser :

- **`for`** = répéter sur une **liste** d'éléments
- **`while`** = répéter **tant qu'une condition** est vraie

#### La boucle `for`

**Parcourir une liste de mots :**

```bash
#!/bin/bash

for fruit in pomme banane cerise; do
    echo "J'aime la $fruit"
done
```

```
J'aime la pomme
J'aime la banane
J'aime la cerise
```

**Parcourir une plage de nombres :**

```bash
for i in {1..5}; do
    echo "Tour numéro $i"
done
```

**Parcourir des fichiers (le cas le plus courant) :**

```bash
#!/bin/bash

for fichier in *.txt; do
    echo "Traitement de $fichier"
done
```

> **À retenir :** `for fichier in *.txt` parcourt tous les fichiers `.txt` du dossier actuel. C'est la façon propre et sûre de parcourir des fichiers.

**Parcourir avec un pas :**

```bash
# Compter de 2 en 2
for i in {0..10..2}; do
    echo $i
done
# → 0, 2, 4, 6, 8, 10
```

#### La boucle `while`

```bash
#!/bin/bash

compteur=1
while [[ $compteur -le 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done
```

```
Compteur : 1
Compteur : 2
Compteur : 3
Compteur : 4
Compteur : 5
```

> **Attention :** si tu oublies `((compteur++))`, la boucle tourne **à l'infini** ! Appuie sur `Ctrl+C` pour l'arrêter.

**Lire un fichier ligne par ligne :**

```bash
#!/bin/bash

while read -r ligne; do
    echo "Lu : $ligne"
done < mon_fichier.txt
```

> **Note :** `-r` empêche `read` d'interpréter les caractères spéciaux comme `\`. C'est une bonne pratique.

#### `break` et `continue`

**`break`** — sortir de la boucle :

```bash
for i in {1..10}; do
    if [[ $i -eq 6 ]]; then
        echo "Stop à $i"
        break
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 3, 4, 5 puis "Stop à 6"
```

**`continue`** — sauter au tour suivant :

```bash
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue
    fi
    echo "Numéro $i"
done
# Affiche 1, 2, 4, 5 (le 3 est sauté)
```

### Très utile en pratique

#### Le `for` style C (pour les plages dynamiques)

La syntaxe `{1..5}` ne fonctionne pas avec des variables. Pour ça :

```bash
#!/bin/bash

limite=$1
for (( i=1; i<=limite; i++ )); do
    echo "Tour $i"
done
```

#### Les boucles imbriquées

```bash
#!/bin/bash

for i in {1..3}; do
    for j in {1..3}; do
        echo "i=$i, j=$j"
    done
done
```

#### Attention aux boucles infinies

```bash
# ❌ BOUCLE INFINIE — le compteur ne change jamais
compteur=1
while [[ $compteur -le 5 ]]; do
    echo $compteur
    # Oubli de ((compteur++)) !
done
```

Si ça t'arrive : **Ctrl+C** pour arrêter.

**Boucle infinie volontaire** (parfois utile) :

```bash
while true; do
    echo "En attente..."
    sleep 5
done
```

### Bonus

#### La boucle `until`

`until` est l'inverse de `while` : elle boucle tant que la condition est **fausse** :

```bash
compteur=1
until [[ $compteur -gt 5 ]]; do
    echo "Compteur : $compteur"
    ((compteur++))
done
```

En pratique, `while` est beaucoup plus courant. `until` est juste une autre façon d'écrire certaines boucles.

### 🔧 Quand ça plante : déboguer une boucle

Ajoute des `echo` temporaires pour voir ce qui se passe :

```bash
for fichier in *.txt; do
    echo "[DEBUG] fichier = '$fichier'"    # ← ajoute ça
    # ... le reste du code
done
```

Si tu ne vois aucun `[DEBUG]`, c'est que la boucle ne s'exécute pas (peut-être qu'il n'y a aucun `.txt` dans le dossier).

### ❌ Erreur classique

```bash
# Oublier do
for i in {1..5};        # ❌ "do" manquant
    echo $i
done

# Oublier done
for i in {1..5}; do
    echo $i
                        # ❌ "done" manquant

# Boucle infinie par oubli d'incrément
while [[ $n -le 10 ]]; do
    echo $n
    # ← Il faut ((n++)) ici !
done
```

### Exercices

**Guidé :** Crée un script qui affiche les nombres de 1 à 10, un par ligne. Utilise une boucle `for` avec `{1..10}`.

**Autonome :** Crée un script qui lit un fichier texte ligne par ligne et affiche chaque ligne précédée de son numéro (indice : utilise un compteur avec `((numero++))`).

**Défi :** Crée un script qui affiche la table de multiplication d'un nombre donné en argument (de 1 à 10).

### ✅ Tu sais maintenant...

- Parcourir une liste ou des fichiers avec `for`
- Répéter tant qu'une condition est vraie avec `while`
- Lire un fichier ligne par ligne
- Contrôler une boucle avec `break` et `continue`
- Éviter et arrêter les boucles infinies

---

## Chapitre 8 — Fonctions et case

### Le minimum à savoir

#### Qu'est-ce qu'une fonction ?

Une fonction, c'est un **bloc de code réutilisable** auquel tu donnes un nom. Au lieu de copier-coller les mêmes lignes, tu les mets dans une fonction et tu l'appelles par son nom.

#### Définir et appeler une fonction

```bash
#!/bin/bash

# 1. Définir la fonction
saluer() {
    echo "Salut, bienvenue !"
}

# 2. L'appeler (juste son nom, sans parenthèses)
saluer
saluer
```

```
Salut, bienvenue !
Salut, bienvenue !
```

> **Règle :** la définition doit apparaître **AVANT** l'appel dans le script.

#### Passer des arguments à une fonction

À l'intérieur de la fonction, `$1`, `$2`... sont les arguments **de la fonction** (pas du script) :

```bash
#!/bin/bash

saluer() {
    echo "Bonjour, $1 ! Tu as $2 ans."
}

saluer "Alice" 25
saluer "Bob" 30
```

```
Bonjour, Alice ! Tu as 25 ans.
Bonjour, Bob ! Tu as 30 ans.
```

#### Récupérer le résultat d'une fonction

En Bash, une fonction renvoie un résultat en l'affichant avec `echo`. On le récupère avec `$(...)` :

```bash
#!/bin/bash

addition() {
    echo $(( $1 + $2 ))
}

resultat=$(addition 15 27)
echo "La somme est : $resultat"
```

> **À retenir :** `return` ne sert PAS à renvoyer une chaîne ou un nombre. Il sert uniquement à donner un code de succès (0) ou d'erreur (1). Pour renvoyer un résultat, utilise `echo` + `$(...)`.

#### Le `case` : choix multiples propres

Le `case` teste **une variable** contre plusieurs valeurs possibles. C'est plus lisible que des enchaînements de `elif` :

```bash
#!/bin/bash

case $1 in
    oui|o|yes|y)
        echo "Tu as dit oui." ;;
    non|n|no)
        echo "Tu as dit non." ;;
    *)
        echo "Réponse non reconnue." ;;
esac
```

> **Notes :**
> - `esac` c'est `case` à l'envers (fermeture du bloc)
> - Chaque bloc se termine par `;;`
> - `*` est le cas par défaut (si rien d'autre ne correspond)
> - `|` sépare plusieurs patterns pour le même bloc

### Très utile en pratique

#### Fonctions + case = script avec des options

```bash
#!/bin/bash

afficher_aide() {
    echo "Utilisation : $0 [option]"
    echo "  -l    Lister les fichiers"
    echo "  -d    Afficher la date"
    echo "  -h    Afficher cette aide"
}

case $1 in
    -l) ls -la ;;
    -d) date ;;
    -h) afficher_aide ;;
    "")
        echo "Erreur : aucune option fournie."
        afficher_aide
        exit 1 ;;
    *)
        echo "Option '$1' inconnue."
        afficher_aide
        exit 1 ;;
esac
```

```bash
./outil.sh -l      # Liste les fichiers
./outil.sh -d      # Affiche la date
./outil.sh -h      # Affiche l'aide
./outil.sh -z      # "Option '-z' inconnue."
```

#### Variables locales

Par défaut, les variables dans une fonction sont **globales**. Pour les limiter à la fonction, utilise `local` :

```bash
#!/bin/bash

nom="Global"

modifier() {
    local nom="Local"
    echo "Dans la fonction : $nom"
}

echo "Avant : $nom"    # → Global
modifier               # → Local
echo "Après : $nom"    # → Global (pas affecté)
```

> **Bonne pratique :** utilise toujours `local` pour les variables internes d'une fonction.

#### Valeurs par défaut pour les arguments

`${1:-"valeur"}` signifie : utilise `$1` s'il existe, sinon prends `"valeur"`.

```bash
saluer() {
    local nom=${1:-"Inconnu"}
    echo "Bonjour, $nom !"
}

saluer "Alice"    # → Bonjour, Alice !
saluer            # → Bonjour, Inconnu !
```

#### Le code de retour d'une fonction (`return`)

```bash
fichier_existe() {
    if [[ -f "$1" ]]; then
        return 0    # Succès
    else
        return 1    # Échec
    fi
}

if fichier_existe "/etc/passwd"; then
    echo "Le fichier existe."
else
    echo "Le fichier n'existe pas."
fi
```

### Bonus

#### Menu interactif avec `select`

`select` crée automatiquement un menu numéroté :

```bash
#!/bin/bash

echo "Que veux-tu faire ?"
select choix in "Lister les fichiers" "Afficher la date" "Quitter"; do
    case $choix in
        "Lister les fichiers") ls ;;
        "Afficher la date") date ;;
        "Quitter") echo "Au revoir." ; break ;;
        *) echo "Choix invalide." ;;
    esac
done
```

#### Parser des arguments nommés avec `shift`

Pour les scripts avec des flags comme `-n 42 -s "texte"` :

```bash
#!/bin/bash

while [[ $# -gt 0 ]]; do
    case $1 in
        -n) nombre="$2" ; shift 2 ;;
        -s) texte="$2" ; shift 2 ;;
        -h) echo "Aide : $0 -n <nombre> -s <texte>" ; exit 0 ;;
        *) echo "Option inconnue : $1" ; exit 1 ;;
    esac
done

echo "Nombre : $nombre"
echo "Texte : $texte"
```

> **Note :** `shift` décale les arguments : l'ancien `$2` devient `$1`. `shift 2` décale de 2 positions. C'est comme ça qu'on "consomme" les flags un par un.

### ❌ Erreur classique

```bash
# Croire que return renvoie une chaîne
ma_fonction() {
    return "Hello"     # ❌ return ne prend qu'un nombre (0-255)
}

# Il faut utiliser echo :
ma_fonction() {
    echo "Hello"       # ✅ On capture avec $(ma_fonction)
}

# Appeler une fonction avec des parenthèses
saluer()               # ❌ Les parenthèses sont pour la DÉFINITION
saluer                 # ✅ Pour appeler, juste le nom
```

### Exercices

**Guidé :** Crée une fonction `maximum` qui prend deux nombres et affiche le plus grand. Teste-la avec `echo "Le max est $(maximum 10 25)"`.

**Autonome :** Crée un script `outil.sh` avec les options `-l` (lister les fichiers), `-d` (afficher la date), `-u` (afficher l'utilisateur) en utilisant `case` et des fonctions.
1
### 🧩 Mini-projet (chapitres 7-8)

Crée un script `gestion.sh` qui :
1. Propose un menu avec `case` : 1) Lister les fichiers .txt, 2) Compter les lignes d'un fichier, 3) Quitter
2. Chaque option appelle une fonction dédiée
3. La boucle `while true` permet de revenir au menu après chaque action
4. L'option "Quitter" utilise `break` pour sortir

### ✅ Tu sais maintenant...

- Définir, appeler et passer des arguments à une fonction
- Récupérer un résultat avec `echo` + `$(...)` (et non avec `return`)
- Utiliser `case` pour des choix multiples propres
- Protéger les variables internes avec `local`

---

## Chapitre 9 — Chaînes de caractères

### Le minimum à savoir

#### Longueur d'une chaîne

```bash
mot="Bonjour"
echo ${#mot}       # → 7
```

#### Concaténation (coller des chaînes)

```bash
debut="Bon"
fin="jour"
mot=$debut$fin
echo "$mot"        # → Bonjour
```

#### Extraire une sous-chaîne

```bash
phrase="Bash est génial"

echo "${phrase:0:4}"     # → Bash     (4 caractères depuis la position 0)
echo "${phrase:5:3}"     # → est      (3 caractères depuis la position 5)
echo "${phrase:9}"       # → génial   (tout depuis la position 9)
```

> **Rappel :** les positions commencent à 0.

#### Remplacer dans une chaîne

```bash
phrase="J'adore les pommes"

# Remplacer la première occurrence
echo "${phrase/pommes/bananes}"
# → J'adore les bananes

# Remplacer TOUTES les occurrences (double slash)
tel="01-23-45-67-89"
echo "${tel//-/.}"
# → 01.23.45.67.89
```

#### Supprimer dans une chaîne

Supprimer, c'est remplacer par rien :

```bash
tel="01-23-45-67-89"

# Supprimer tous les tirets
echo "${tel//-/}"
# → 0123456789
```

#### Majuscules et minuscules

```bash
nom="alice dupont"
NOM="ALICE DUPONT"

echo "${nom^^}"          # → ALICE DUPONT  (tout en majuscules)
echo "${NOM,,}"          # → alice dupont  (tout en minuscules)
echo "${nom^}"           # → Alice dupont  (première lettre en majuscule)
```

### Très utile en pratique

#### Tester si une chaîne est vide

```bash
nom=""
[[ -z "$nom" ]] && echo "Nom est vide"       # → Nom est vide

autre="Alice"
[[ -n "$autre" ]] && echo "Autre n'est pas vide"  # → Autre n'est pas vide
```

#### Récapitulatif

| Syntaxe                  | Effet                            |
| ------------------------ | -------------------------------- |
| `${#var}`                | Longueur                         |
| `${var:pos:len}`         | Extraire une sous-chaîne         |
| `${var/ancien/nouveau}`  | Remplacer la 1ère occurrence     |
| `${var//ancien/nouveau}` | Remplacer toutes les occurrences |
| `${var//ancien/}`        | Supprimer toutes les occurrences |
| `${var^^}`               | Tout en majuscules               |
| `${var,,}`               | Tout en minuscules               |
| `${var^}`                | 1ère lettre en majuscule         |

### Bonus

#### Extraire l'extension d'un fichier

```bash
fichier="rapport.tar.gz"
echo "${fichier##*.}"    # → gz (tout après le dernier .)
echo "${fichier%.*}"     # → rapport.tar (tout avant le dernier .)
```

#### Pattern matching avancé

```bash
# Supprimer un préfixe
chemin="/home/user/documents/fichier.txt"
echo "${chemin##*/}"     # → fichier.txt (garde juste le nom)

# Supprimer un suffixe
echo "${chemin%/*}"      # → /home/user/documents (garde juste le dossier)
```

### ❌ Erreur classique

```bash
# Oublier les accolades
echo "$phrase:0:4"       # ❌ Affiche le contenu de $phrase suivi de ":0:4"
echo "${phrase:0:4}"     # ✅ Extrait correctement

# Confondre / et //
echo "${tel/-/}"         # Supprime seulement le PREMIER tiret
echo "${tel//-/}"        # Supprime TOUS les tirets
```

### Exercices

**Guidé :** Crée un script qui prend un numéro de téléphone avec des tirets (`01-23-45-67-89`) et l'affiche reformaté avec des points (`01.23.45.67.89`).

**Autonome :** Crée un script qui prend une phrase en argument et affiche sa longueur, la phrase en majuscules, et la phrase en minuscules.

### ✅ Tu sais maintenant...

- Mesurer la longueur d'une chaîne
- Extraire, remplacer et supprimer des parties de chaîne
- Convertir entre majuscules et minuscules
- Les syntaxes `${var/...}` et `${var^^}`/`${var,,}`

---

## Chapitre 10 — Tableaux

> **Note :** les tableaux sont utiles, mais pas indispensables pour commencer à automatiser. Tu peux écrire beaucoup de scripts sans en avoir besoin. Ce chapitre t'équipe pour le jour où tu en auras besoin. **Si ce chapitre te semble flou au premier passage, passe au suivant et reviens-y quand tu en auras besoin dans un vrai script.**

### Le minimum à savoir

#### Créer un tableau

Un tableau stocke **plusieurs valeurs** dans une seule variable. Chaque valeur a un index qui commence à 0.

```bash
fruits=("pomme" "banane" "cerise")
```

```
Index :     0         1         2
         ┌─────┐  ┌──────┐  ┌──────┐
         │pomme│  │banane│  │cerise│
         └─────┘  └──────┘  └──────┘
```

#### Accéder aux éléments

```bash
fruits=("pomme" "banane" "cerise")

echo "${fruits[0]}"      # → pomme
echo "${fruits[1]}"      # → banane
echo "${fruits[@]}"      # → pomme banane cerise (tout)
echo "${#fruits[@]}"     # → 3 (le nombre d'éléments)
```

#### Ajouter un élément

```bash
fruits+=("kiwi")
echo "${fruits[@]}"      # → pomme banane cerise kiwi
```

#### Modifier un élément

```bash
fruits[1]="fraise"
echo "${fruits[@]}"      # → pomme fraise cerise kiwi
```

#### Supprimer un élément

```bash
unset fruits[1]
echo "${fruits[@]}"      # → pomme cerise kiwi
```

#### Parcourir un tableau

```bash
#!/bin/bash

fruits=("pomme" "banane" "cerise" "kiwi")

for fruit in "${fruits[@]}"; do
    echo "Fruit : $fruit"
done
```

### Très utile en pratique

#### Parcourir avec les index

```bash
for i in "${!fruits[@]}"; do
    echo "Index $i : ${fruits[$i]}"
done
```

#### Tableaux multi-types

Un tableau Bash peut contenir des valeurs de types différents :

```bash
infos=("Alice" 25 "Paris" "admin")

echo "Nom  : ${infos[0]}"
echo "Âge  : ${infos[1]}"
echo "Ville: ${infos[2]}"
echo "Rôle : ${infos[3]}"
```

#### Récapitulatif

| Syntaxe             | Effet                 |
| ------------------- | --------------------- |
| `tab=("a" "b" "c")` | Créer un tableau      |
| `${tab[0]}`         | Accéder à l'élément 0 |
| `${tab[@]}`         | Tous les éléments     |
| `${#tab[@]}`        | Nombre d'éléments     |
| `${!tab[@]}`        | Tous les index        |
| `tab+=("d")`        | Ajouter un élément    |
| `tab[1]="x"`        | Modifier un élément   |
| `unset tab[1]`      | Supprimer un élément  |

### Bonus

#### Les tableaux associatifs (dictionnaires)

Les tableaux associatifs utilisent des **clés nommées** au lieu d'index numériques. C'est comme un dictionnaire : chaque mot (clé) a une définition (valeur).

```bash
# OBLIGATOIRE : declare -A
declare -A capitales

capitales[France]="Paris"
capitales[Allemagne]="Berlin"
capitales[Espagne]="Madrid"

echo "${capitales[France]}"       # → Paris
echo "${!capitales[@]}"           # → France Allemagne Espagne (les clés)

# Parcourir
for pays in "${!capitales[@]}"; do
    echo "La capitale de $pays est ${capitales[$pays]}"
done
```

> **Prérequis :** Bash 4.0+ (`bash --version` pour vérifier). Le `declare -A` est obligatoire, sinon Bash crée un tableau indexé normal.

### ❌ Erreur classique

```bash
# Oublier les accolades et l'[@]
echo $fruits         # ❌ N'affiche que le premier élément
echo "${fruits[@]}"  # ✅ Affiche tout

# Oublier les guillemets dans une boucle
for f in ${fruits[@]}; do     # ❌ Problème si un élément contient des espaces
for f in "${fruits[@]}"; do   # ✅ Correct
```

### Exercices

**Guidé :** Crée un tableau avec 5 prénoms, puis affiche-les numérotés avec une boucle `for` et un compteur.

**Autonome :** Crée un script qui prend des noms en arguments (`$@`), les stocke dans un tableau, et les affiche triés (indice : tu peux utiliser un pipe avec `sort`).

### 🧩 Mini-projet (chapitres 9-10)

Crée un script `contacts.sh` qui :
1. Contient un tableau de noms : `noms=("Alice" "Bob" "Charlie")`
2. Contient un tableau d'emails correspondants : `emails=("alice@mail.com" "bob@mail.com" "charlie@mail.com")`
3. Affiche chaque contact sous la forme "Nom : Alice — Email : alice@mail.com"
4. Demande à l'utilisateur un numéro et affiche le contact correspondant

### ✅ Tu sais maintenant...

- Créer, modifier et parcourir un tableau indexé
- Accéder aux éléments par leur index
- Ajouter et supprimer des éléments
- (Bonus) Utiliser des tableaux associatifs

---

## Chapitre 11 — Déboguer et écrire des scripts propres

### Le minimum à savoir

#### Les `echo` de débogage

La méthode la plus simple : ajouter des `echo` pour voir les valeurs en cours de route :

```bash
#!/bin/bash

fichier=$1
echo "[DEBUG] fichier = '$fichier'"

if [[ -f "$fichier" ]]; then
    echo "[DEBUG] Le fichier existe"
    nb_lignes=$(wc -l < "$fichier")
    echo "[DEBUG] nb_lignes = '$nb_lignes'"
fi
```

> **Astuce :** utilise le préfixe `[DEBUG]` pour retrouver facilement tes messages et les supprimer une fois le bug corrigé.

> Utiliser `echo` pour voir ce que contient une variable ou pour suivre l'exécution d'un script, c'est une méthode **normale**, simple, et utilisée par tout le monde — même les développeurs expérimentés. Ce n'est pas du bricolage, c'est du débogage.

#### Lire un message d'erreur

Les messages d'erreur de Bash suivent ce format :

```
./mon_script.sh: line 12: commande: command not found
```

- `./mon_script.sh` → quel fichier
- `line 12` → quelle ligne
- `command not found` → quel problème

#### Le mode trace avec `bash -x`

`-x` affiche chaque commande **avant** de l'exécuter, avec les variables remplacées par leurs valeurs :

```bash
bash -x mon_script.sh
```

Tu peux aussi l'activer/désactiver dans le script :

```bash
#!/bin/bash
set -x          # Active la trace
echo "Ceci sera tracé"
nombre=$((5 + 3))
set +x          # Désactive la trace
echo "Ceci ne sera plus tracé"
```

Sortie :

```
+ echo 'Ceci sera tracé'
Ceci sera tracé
+ nombre=8
+ set +x
Ceci ne sera plus tracé
```

#### Les 5 erreurs de débutant les plus fréquentes

| Erreur                   | Message                   | Solution                                       |
| ------------------------ | ------------------------- | ---------------------------------------------- |
| Espaces autour de `=`    | `command not found`       | `var="valeur"` (pas d'espace)                  |
| `then` ou `fi` oublié    | `syntax error`            | Vérifie chaque `if` a son `then` et son `fi`   |
| `do` ou `done` oublié    | `syntax error`            | Vérifie chaque boucle a son `do` et son `done` |
| Guillemets oubliés       | `unary operator expected` | Mets `"$var"` au lieu de `$var`                |
| `-eq` confondu avec `==` | Résultat inattendu        | `-eq` pour nombres, `==` pour texte            |

### Très utile en pratique

#### Vérifier les arguments en début de script

```bash
#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Erreur : argument manquant" >&2
    echo "Utilisation : $0 <fichier>" >&2
    exit 1
fi
```

> **Note :** `>&2` envoie le message vers stderr (la sortie d'erreur). C'est la bonne pratique pour les messages d'erreur.

#### Noms de variables descriptifs

```bash
# ❌ Incompréhensible
a=5
b="txt"

# ✅ Clair
nombre_fichiers=5
extension="txt"
```

#### Structurer avec des fonctions

```bash
# ❌ Script monolithique de 200 lignes

# ✅ Script structuré
verifier_arguments() { ... }
traiter_fichier() { ... }
generer_rapport() { ... }

verifier_arguments "$@"
traiter_fichier "$1"
generer_rapport
```

#### Commenter ton code

```bash
#!/bin/bash
# Ce script sauvegarde les fichiers de configuration
# Usage : ./backup.sh <dossier_destination>
```

#### Toujours mettre les variables entre guillemets

```bash
cat $fichier       # ❌ Dangereux si $fichier contient des espaces
cat "$fichier"     # ✅ Sûr
```

### Bonus

#### `set -e` : arrêt sur erreur

Par défaut, Bash continue même quand une commande échoue. `set -e` change ça :

```bash
#!/bin/bash
set -e

echo "Étape 1"
cd /dossier_inexistant     # ← Erreur ! Le script s'arrête ici
echo "Étape 2"             # ← Jamais exécuté
```

C'est utile pour les scripts importants, mais attention : ça peut aussi arrêter le script sur des erreurs "attendues". Utilise-le quand tu maîtrises bien ton script.

#### `set -u` : erreur si variable non définie

```bash
#!/bin/bash
set -u

echo "Mon nom est $nom"    # ← Erreur ! $nom n'est pas défini
```

#### La combinaison `set -euo pipefail`

Beaucoup de développeurs expérimentés utilisent :

```bash
#!/bin/bash
set -euo pipefail
```

- `-e` : arrêt sur erreur
- `-u` : erreur si variable non définie
- `-o pipefail` : un pipe échoue si n'importe quelle commande du pipe échoue

C'est un filet de sécurité puissant, mais à utiliser quand tu es à l'aise avec les bases. Ne te force pas à le mettre dans tes premiers scripts.

### ❌ Erreur classique

```bash
# Laisser des echo [DEBUG] dans le script final
echo "[DEBUG] valeur = $x"    # ← Pense à les supprimer !

# Ne pas tester le script avec des cas limites
./script.sh ""                # Que se passe-t-il avec un argument vide ?
./script.sh "fichier avec espaces.txt"   # Et avec des espaces ?
```

### Exercices

**Guidé :** Prends un de tes scripts précédents et lance-le avec `bash -x`. Observe les lignes précédées de `+`.

**Autonome :** Crée un script volontairement bugué (variable mal nommée, `fi` manquant, variable vide...) et corrige les erreurs en lisant les messages d'erreur.

### ✅ Tu sais maintenant...

- Déboguer avec `echo [DEBUG]` et `bash -x`
- Lire et comprendre les messages d'erreur
- Les 5 erreurs les plus fréquentes
- Les bonnes pratiques : guillemets, noms clairs, commentaires, fonctions
- (Bonus) `set -e`, `set -u`, `set -euo pipefail`

---

## Chapitre 12 — Cas pratiques et automatisation

> Jusqu'ici, tu as appris les briques du scripting Bash une par une. Maintenant, on les **combine** dans de vrais petits scripts, proches de situations réelles. C'est ici que tout prend son sens.

### Penser comme un automaticien

Avant d'écrire un script d'automatisation, pose-toi trois questions :

1. **Qu'est-ce que je fais à la main régulièrement ?**
2. **Est-ce que c'est toujours les mêmes étapes ?**
3. **Est-ce que ça pourrait tourner tout seul ?**

Si oui aux trois → c'est un bon candidat pour un script.

### Cas pratique 1 — Journaliser et accueillir

Un script simple qui journalise les connexions :

```bash
#!/bin/bash

LOG="$HOME/connexions.log"

utilisateur=$(whoami)
date_heure=$(date '+%Y-%m-%d %H:%M:%S')

echo "Bienvenue, $utilisateur !"
echo "[$date_heure] Connexion de $utilisateur" >> "$LOG"
echo "Connexion enregistrée dans $LOG"
```

> **Ce script illustre :** variables, substitution de commande, redirection `>>`.

### Cas pratique 2 — Tester des fichiers/dossiers

Un script qui vérifie l'état d'une liste de chemins :

```bash
#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Utilisation : $0 <chemin1> [chemin2] ..." >&2
    exit 1
fi

for chemin in "$@"; do
    if [[ -f "$chemin" ]]; then
        taille=$(wc -c < "$chemin")
        echo "✓ $chemin — fichier ($taille octets)"
    elif [[ -d "$chemin" ]]; then
        nb=$(ls "$chemin" | wc -l)
        echo "✓ $chemin — dossier ($nb éléments)"
    else
        echo "✗ $chemin — n'existe pas"
    fi
done
```

> **Ce script illustre :** arguments, boucle `for`, conditions, tests de fichiers, pipes.

### Cas pratique 3 — Sauvegarder des dossiers

```bash
#!/bin/bash

# --- Configuration ---
dossiers=("/etc" "/home")
destination="/tmp/backups"
date_du_jour=$(date +%Y-%m-%d)

# --- Préparation ---
mkdir -p "$destination"

echo "=== Sauvegarde du $date_du_jour ==="

for dossier in "${dossiers[@]}"; do
    nom_archive=$(echo "$dossier" | tr '/' '_')
    fichier="${destination}/${nom_archive}-${date_du_jour}.tar.gz"

    echo -n "Sauvegarde de $dossier ... "

    if tar -czf "$fichier" "$dossier" 2>/dev/null; then
        taille=$(du -h "$fichier" | cut -f1)
        echo "OK ($taille)"
    else
        echo "ERREUR" >&2
    fi
done

echo "=== Terminé ==="
```

> **Ce script illustre :** tableaux, boucle `for`, conditions, redirections, substitution de commande.

### Cas pratique 4 — Renommer des fichiers en masse

Renommer tous les `.jpeg` en `.jpg` :

```bash
#!/bin/bash

dossier=${1:-.}
compteur=0

for fichier in "$dossier"/*.jpeg; do
    [[ -f "$fichier" ]] || continue

    nouveau="${fichier%.jpeg}.jpg"
    mv "$fichier" "$nouveau"
    echo "Renommé : $fichier → $nouveau"
    ((compteur++))
done

echo "Total : $compteur fichier(s) renommé(s)."
```

> **Explication :** `${fichier%.jpeg}` supprime `.jpeg` à la fin de la chaîne (vu au chapitre 9).

### Planifier avec `cron`

`cron` exécute des scripts **automatiquement** à des heures précises.

#### Éditer la crontab

```bash
crontab -e     # Ouvrir l'éditeur
crontab -l     # Lister les tâches
```

#### La syntaxe cron

```
┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, 0 et 7 = dimanche)
│ │ │ │ │
* * * * * commande
```

#### Exemples

```bash
# Tous les jours à minuit
0 0 * * * /home/user/scripts/backup.sh

# Toutes les 6 heures
0 */6 * * * /home/user/scripts/check_disk.sh

# Tous les lundis à 8h
0 8 * * 1 /home/user/scripts/rapport.sh
```

> **Astuce :** redirige la sortie vers un log :
> ```bash
> 0 0 * * * /home/user/scripts/backup.sh >> /home/user/logs/backup.log 2>&1
> ```

### Script modèle

Voici un squelette "propre" que tu peux réutiliser comme base :

```bash
#!/bin/bash
# =============================================================================
# Nom        : mon_script.sh
# Description : [Ce que fait le script]
# Utilisation : ./mon_script.sh [options] <arguments>
# =============================================================================

# --- Fonctions ---
afficher_aide() {
    echo "Utilisation : $0 [options] <argument>"
    echo "  -h    Afficher cette aide"
}

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# --- Vérification des arguments ---
if [[ $# -lt 1 ]]; then
    afficher_aide
    exit 1
fi

case $1 in
    -h|--help) afficher_aide ; exit 0 ;;
esac

# --- Programme principal ---
log "Début du script"

# ... ton code ici ...

log "Fin du script"
```

### Exercices

**Guidé :** Crée un script de sauvegarde qui compresse un dossier donné en argument, le nomme avec la date, et le place dans `/tmp/backups/`.

**Autonome :** Crée un script "boîte à outils" avec un menu (`case` + boucle) : 1) Lister les fichiers, 2) Espace disque (`df -h`), 3) Info système (`uname -a`), 4) Quitter.

**Défi :** Planifie un de tes scripts pour qu'il s'exécute tous les jours à 8h avec `crontab -e`.

### ✅ Tu sais maintenant...

- Écrire des scripts d'automatisation complets
- Combiner toutes les notions apprises dans des cas concrets
- Planifier des scripts avec cron
- Structurer un script proprement avec un modèle réutilisable

---

## Conclusion

Tu as toutes les bases pour écrire des scripts Bash utiles et bien structurés :

- **Chapitres 1-3 :** Les fondamentaux — script, variables, arguments
- **Chapitre 4 :** Les flux — redirections et pipes
- **Chapitres 5-6 :** La logique — calculs, conditions, tests
- **Chapitre 7 :** La répétition — boucles
- **Chapitre 8 :** La structure — fonctions et case
- **Chapitres 9-10 :** Les données — chaînes et tableaux
- **Chapitre 11 :** La qualité — débogage et bonnes pratiques
- **Chapitre 12 :** La mise en pratique — automatisation et cron

**Pour continuer à progresser :**

- Écris des scripts pour tes propres besoins quotidiens
- Quand tu es bloqué, `man commande` est ton meilleur ami
- Lis les scripts des autres pour découvrir de nouvelles techniques
- La meilleure façon d'apprendre, c'est de pratiquer sur des problèmes réels

Bon scripting !
