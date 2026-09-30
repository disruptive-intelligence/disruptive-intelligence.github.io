---
title: Chapitre 1 — Découverte de Bash et premier script
source: IT/05_Scripting_Langage-Prog/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Le terminal et le shell

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

### Quelques commandes pour se familiariser

Tape ces commandes dans ton terminal pour te familiariser :

```bash
echo "Bonjour !"       # Afficher du texte
pwd                     # Où suis-je ? (quel dossier)
ls                      # Qu'est-ce qu'il y a ici ? (liste des fichiers)
date                    # Quelle date et heure ?
whoami                  # Qui suis-je ? (nom d'utilisateur)
```


> **À retenir :** le symbole `#` marque un **commentaire**. Bash ignore tout ce qui suit un `#`. Les commentaires servent à expliquer ton code.

### Ton premier script en 5 étapes

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

### Le shebang : `#!/bin/bash`

La première ligne `#!/bin/bash` s'appelle le **shebang**. Elle dit au système : "ce fichier doit être lu par Bash".

Sans shebang, le système ne sait pas quel langage utiliser. Avec le shebang, tu peux lancer ton script avec `./script.sh` directement.

> **À retenir :** mets TOUJOURS `#!/bin/bash` en première ligne de tes scripts.

### Pourquoi `./` devant le script ?

Quand tu tapes `ls` ou `date`, le système sait où trouver ces commandes grâce à une variable appelée `PATH`. Ton dossier personnel n'est pas dans le `PATH`, donc il faut préciser "cherche dans le dossier actuel" avec `./`.

### La commande `exit`

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

## ❌ Erreur classique

```bash
# Oublier le shebang → le script peut ne pas fonctionner avec ./script.sh
# Oublier chmod +x → "Permission denied" quand tu lances le script
# Oublier le ./ → "command not found"
```


## Exercices

**Guidé :** Crée un script `salut.sh` qui affiche deux lignes : "Bonjour !" puis "Bienvenue dans le monde du scripting."

**Autonome :** Crée un script `info.sh` qui affiche ton nom d'utilisateur (`whoami`), la date (`date`), et le dossier actuel (`pwd`) sur des lignes séparées.

## ✅ Tu sais maintenant...

- Ce qu'est un terminal, un shell et un script
- Créer un fichier script avec le shebang `#!/bin/bash`
- Rendre un script exécutable avec `chmod +x`
- Lancer un script avec `./mon_script.sh`
- Ce que signifie un code de sortie

---
