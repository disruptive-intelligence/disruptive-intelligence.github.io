---
title: Chapitre 1 — Découverte de Python et premier script
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
chapter: 1
chapters: 20
---

## Le minimum à savoir

### Pourquoi Python en cybersécurité ?

Python est l'un des langages les plus utilisés au monde, et **l'un des langages les plus utilisés en cybersécurité défensive**. Il est populaire pour une raison simple : **il se lit presque comme de l'anglais**. Là où d'autres langages utilisent des symboles cryptiques, Python utilise des mots clairs.

En SOC, en analyse de menaces ou en forensic, on passe son temps à manipuler du texte : des logs, des adresses IP, des domaines, des hash. Python excelle exactement là-dessus. Un analyste qui sait scripter en Python peut automatiser en quelques lignes ce qui prendrait des heures à la main : extraire toutes les IP d'un fichier de logs, calculer le hash d'un fichier suspect, interroger une base de menaces…

Dans ce cours, on se concentre sur le **scripting** : écrire des petits programmes pour automatiser des tâches concrètes d'analyse défensive.

### Installer Python

**Linux :** Python est déjà installé. Vérifie avec :

```bash
python3 --version
```

Tu devrais voir quelque chose comme `Python 3.12.x` ou `Python 3.13.x`. Si tu vois une version 3.8 ou plus récente, c'est bon.

**Mac :** Python 3 n'est pas toujours installé par défaut. La méthode la plus simple :

```bash
# Vérifie d'abord
python3 --version

# Si ça ne fonctionne pas, va sur https://www.python.org/downloads/
# et télécharge l'installeur Mac
```

**Windows :**

1. Va sur [python.org/downloads](https://python.org/downloads)
2. Télécharge la dernière version
3. **IMPORTANT : coche la case "Add Python to PATH"** pendant l'installation. Si tu oublies cette case, rien ne fonctionnera dans le terminal.
4. Ouvre un terminal (PowerShell) et tape `python --version`

> **Piège Windows :** sur Windows, la commande est souvent `python` (sans le `3`), alors que sur Linux et Mac c'est `python3`. Dans ce cours, on utilisera `python3`, mais adapte si tu es sur Windows.

### Environnement de travail conseillé

Avant de te lancer, prépare un environnement simple et sûr :

- **Un terminal** (celui de ton système suffit).
- **Un éditeur de code** : VS Code est recommandé (coloration, indentation automatique), mais nano ou n'importe quel éditeur fonctionne.
- **Un dossier dédié** `scripts_cyber` pour tous tes scripts.
- **Des fichiers de test que tu crées toi-même** (faux logs, faux CSV d'IOC). À partir du chapitre 10, garde sous la main quelques fichiers de test comme `auth.log`, `access.log`, `iocs.csv`, `rapport.txt` : c'est ce qui te fera progresser le plus vite.
- **Règle d'or :** ne lance jamais tes scripts sur des logs ou des systèmes que tu n'es pas autorisé à analyser.

> **Environnement virtuel (à garder pour le chapitre 16) :** dès que tu installeras une bibliothèque externe comme `requests`, il est propre de créer un environnement isolé. Tu n'en as pas besoin tout de suite, mais voici la commande pour plus tard :
```bash  
python3 -m venv venv  
source venv/bin/activate # sur Windows : venv\Scripts\activate  
pip install requests  
```
### Le mode interactif : ton terrain d'entraînement

Tape `python3` dans ton terminal :

```bash
python3
```

Tu vois apparaître les `>>>`, le **prompt interactif**. Tu peux taper des instructions et voir le résultat immédiatement :

```python
>>> print("Analyse démarrée")
Analyse démarrée
>>> 22 + 80
102
>>> "192.168.1.1" in "Connexion depuis 192.168.1.1"
True
```

C'est un bac à sable : tu tapes, Python répond. Parfait pour tester une idée rapidement, par exemple vérifier si une IP apparaît dans une ligne de log.

Pour quitter :

```python
>>> exit()
```

> **À retenir :** le mode interactif est idéal pour **tester** de petites choses. Pour écrire un vrai script réutilisable, tu utilises un fichier.

### Ton premier script en 3 étapes

**Étape 1 — Crée un dossier de travail :**

```bash
mkdir -p ~/scripts_cyber
cd ~/scripts_cyber
```

**Étape 2 — Crée le fichier et écris le script :**

Ouvre un éditeur de texte (nano, VS Code…) et crée un fichier `alerte.py` :

```python
# Mon tout premier script de sécurité
print("[+] Outil d'analyse démarré")
print("[+] Aucune menace détectée pour l'instant")
```

Sauvegarde le fichier.

**Étape 3 — Lance-le :**

```bash
python3 alerte.py
```

Résultat :

```
[+] Outil d'analyse démarré
[+] Aucune menace détectée pour l'instant
```

Félicitations, tu viens d'écrire et d'exécuter ton premier script Python ! Le préfixe `[+]` est une convention courante dans les outils de sécurité pour marquer une information ; on verra aussi `[-]` (problème) et `[!]` (alerte).

> **Remarque :** contrairement à Bash, pas besoin de `chmod +x` ni de shebang. Tu lances simplement `python3 nom_du_script.py`.

### Les commentaires

Le symbole `#` marque un commentaire. Python ignore tout ce qui suit un `#` sur la même ligne :

```python
# Ceci est un commentaire — Python l'ignore complètement
print("Ceci s'affiche")  # Un commentaire en fin de ligne
```

Les commentaires servent à expliquer ton code, pour toi et pour les autres analystes qui le reliront.

### Python est sensible à la casse

`print` et `Print` sont deux choses différentes pour Python :

```python
print("Bonjour")    # ✅ Fonctionne
Print("Bonjour")    # ❌ NameError: name 'Print' is not defined
```

Les commandes Python sont en **minuscules** : `print`, `input`, `if`, `for`.

## Très utile en pratique

### Le shebang (optionnel)

Si tu veux lancer ton outil directement avec `./scan.py`, ajoute un shebang en première ligne :

```python
#!/usr/bin/env python3
print("Outil prêt")
```

Puis :

```bash
chmod +x scan.py
./scan.py
```

Ce n'est pas obligatoire, mais c'est pratique pour transformer un script en commande réutilisable.

### Mode interactif vs fichier script

|Mode interactif (`python3`)        |Fichier script (`python3 script.py`)|
|-----------------------------------|------------------------------------|
|Pour tester une idée rapidement    |Pour un outil réutilisable          |
|Le code disparaît à la fermeture   |Le code est sauvegardé              |
|Résultat affiché automatiquement   |Il faut utiliser `print()`          |
|Pas pratique pour plus de 5 lignes |Adapté à n'importe quelle taille    |

## Application cyber

Un analyste teste souvent une idée dans le mode interactif avant d'écrire un script. Exemple : tu reçois une ligne de log et tu veux vérifier rapidement si elle contient un mot-clé suspect.

```python
>>> ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5"
>>> "Failed password" in ligne
True
>>> "root" in ligne
True
```

En deux secondes, tu as confirmé que cette ligne est une **tentative de connexion SSH échouée sur le compte root**, un signal classique de tentative d'intrusion. On apprendra à automatiser ça sur un fichier entier dans les chapitres suivants.

## ❌ Erreur classique

```python
# Oublier les parenthèses de print (syntaxe Python 2, plus valide)
print "Démarrage"        # ❌ SyntaxError
print("Démarrage")       # ✅ Correct

# Oublier les guillemets autour du texte
print(Demarrage)          # ❌ NameError: name 'Demarrage' is not defined
print("Demarrage")        # ✅ Correct

# Majuscule sur print
Print("Démarrage")        # ❌ NameError
print("Démarrage")        # ✅ Correct
```

## Exercices

**Guidé :** Crée un script `banniere.py` qui affiche trois lignes : `"=== Outil SOC ==="`, `"[+] Initialisation..."`, puis `"[+] Prêt à analyser."`.

**Autonome :** Crée un script `etat.py` qui affiche le résultat de `443 + 80` (total de deux ports), de `1024 * 64`, et le texte `"[+] Calculs réseau terminés"` — chacun sur une ligne séparée avec `print()`.

## ✅ Tu sais maintenant…

- Ce qu'est Python et pourquoi c'est central en cyber défensive
- Installer et vérifier ta version de Python
- Utiliser le mode interactif pour tester rapidement une idée (ex. chercher un mot-clé dans une ligne de log)
- Créer un fichier `.py` et le lancer avec `python3`
- Écrire des commentaires avec `#`

-----
