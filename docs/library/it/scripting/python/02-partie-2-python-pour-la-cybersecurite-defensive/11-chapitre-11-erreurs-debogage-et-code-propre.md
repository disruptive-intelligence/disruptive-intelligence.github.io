---
title: Chapitre 11 — Erreurs, débogage et code propre
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Lire un message d'erreur Python (le traceback)

Quand Python plante, il affiche un **traceback** :

```
Traceback (most recent call last):
  File "parser.py", line 8, in <module>
    ip = ligne.split()[-1]
IndexError: list index out of range
```


Comment le lire :

1. **Dernière ligne** = type d'erreur + message (`IndexError: list index out of range`)
2. **Au-dessus** = la ligne fautive (`ip = ligne.split()[-1]`)
3. **Encore au-dessus** = fichier et numéro de ligne (`parser.py, line 8`)

> **Réflexe :** lis le traceback **de bas en haut**. La dernière ligne est la plus importante.

### Les 5 erreurs de débutant les plus fréquentes

|Erreur            |Cause                                   |Exemple cyber                          |
|------------------|----------------------------------------|---------------------------------------|
|`SyntaxError`     |Syntaxe (`:` oublié…)                   |`if "Failed" in ligne` sans `:`        |
|`IndentationError`|Indentation incorrecte                  |mauvais nombre d'espaces               |
|`NameError`       |Variable/fonction non définie           |faute de frappe dans `ip_soruce`       |
|`TypeError`       |Mauvais type                            |`"443" + 1` (port texte + nombre)      |
|`IndexError`/`KeyError`|Élément/clé inexistant             |`ligne.split()[-1]` sur ligne vide     |

```python
# TypeError — port lu comme texte
port = "443"
suivant = port + 1     # ❌ "443" + 1 impossible
suivant = int(port) + 1  # ✅

# IndexError — ligne vide dans un log
ligne = ""
ip = ligne.split()[-1]   # ❌ liste vide, pas d'index -1
```


### Les `print()` de débogage

La méthode la plus simple et universelle pour comprendre ce qui se passe :

```python
ligne = "Failed password for root from 203.0.113.5"
print(f"[DEBUG] ligne = {ligne!r}")     # ← ajoute ça
ip = ligne.split()[-1]
print(f"[DEBUG] ip extraite = {ip!r}")  # ← et ça
```


> **Astuce :** le préfixe `[DEBUG]` permet de retrouver et supprimer facilement ces messages. Utiliser `print()` pour suivre l'exécution est une méthode **normale**, utilisée même par les analystes expérimentés. Le `!r` affiche la valeur avec ses guillemets, pratique pour voir les espaces et `\n` cachés.

### Gérer les erreurs avec `try/except`

Au lieu de laisser le script planter sur un fichier absent ou une ligne mal formée, **capture** l'erreur :

```python
try:
    with open("auth.log", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print("[-] Fichier introuvable, analyse annulée")
```


> **Comparaison avec Bash :** équivalent de `commande || echo "Erreur"`, mais bien plus puissant : tu différencies les types d'erreurs.

### `try/except` avec plusieurs types

```python
import sys

try:
    fichier = sys.argv[1]
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
except IndexError:
    print("[-] Donne un fichier en argument.")
except FileNotFoundError:
    print(f"[-] Le fichier '{sys.argv[1]}' n'existe pas.")
except PermissionError:
    print(f"[-] Pas le droit de lire '{sys.argv[1]}'.")
```


### `finally`

Le bloc `finally` s'exécute **toujours**, erreur ou non :

```python
try:
    f = open("auth.log", "r", encoding="utf-8")
    données = f.read()
except FileNotFoundError:
    print("[-] Introuvable")
finally:
    print("[*] Analyse terminée")
```


## Très utile en pratique

### Rendre un parser robuste face aux lignes mal formées

Un vrai fichier de log contient des lignes vides, tronquées, ou inattendues. Un bon parser **ne plante pas** dessus, il les ignore proprement.

```python
lignes = [
    "Failed password for root from 203.0.113.5",
    "",                       # ligne vide
    "log corrompu sans ip",   # ligne sans IP exploitable
    "Failed password for admin from 198.51.100.9",
]

echecs = {}
for ligne in lignes:
    ligne = ligne.strip()
    if not ligne or "Failed password" not in ligne:
        continue              # on saute ce qui ne nous intéresse pas
    try:
        ip = ligne.split()[-1]
        echecs[ip] = echecs.get(ip, 0) + 1
    except IndexError:
        print(f"[DEBUG] ligne ignorée : {ligne!r}")

print(echecs)   # {'203.0.113.5': 1, '198.51.100.9': 1}
```


La combinaison `continue` (ignorer les lignes non pertinentes) + `try/except` (se protéger des surprises) est la clé d'un parser fiable.

### Noms de variables descriptifs

```python
# ❌ Incompréhensible
a = 5
b = []

# ✅ Clair
nb_echecs = 5
ips_suspectes = []
```


### Structurer avec des fonctions et `main()`

```python
import sys

def verifier_arguments():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>")
        sys.exit(1)
    return sys.argv[1]

def compter_echecs(chemin):
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" in ligne:
                ip = ligne.split()[-1]
                echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    chemin = verifier_arguments()
    echecs = compter_echecs(chemin)
    for ip, nb in echecs.items():
        print(f"{ip} : {nb}")

if __name__ == "__main__":
    main()
```


**Ce que fait `if __name__ == "__main__":`** : le code dedans ne s'exécute **que** si tu lances le script directement (`python3 script.py`). Si tu **importes** le fichier ailleurs pour réutiliser ses fonctions, ce bloc ne s'exécute pas. C'est une bonne habitude dès que tes scripts grandissent.

## Application cyber — un script défensif robuste

Réunissons tout : un outil qui ne plante jamais, quels que soient les arguments ou l'état du fichier.

```python
import sys
from pathlib import Path

def analyser(chemin):
    """Compte les échecs SSH par IP dans un fichier de log."""
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" not in ligne:
                continue
            try:
                ip = ligne.strip().split()[-1]
            except IndexError:
                continue          # ligne inattendue → on ignore
            echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
        sys.exit(1)

    chemin = Path(sys.argv[1])
    try:
        echecs = analyser(chemin)
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {chemin}")
        sys.exit(1)
    except PermissionError:
        print(f"[-] Lecture refusée : {chemin}")
        sys.exit(1)

    if not echecs:
        print("[+] Aucun échec détecté.")
        return
    for ip, nb in echecs.items():
        marque = "[!]" if nb >= 5 else "   "
        print(f"{marque} {ip} : {nb} échec(s)")

if __name__ == "__main__":
    main()
```


Ce script gère l'argument manquant, le fichier absent, l'accès refusé, les lignes mal formées et le cas « aucun résultat ». C'est la différence entre un script de TP et un outil sur lequel un analyste peut compter.

## Bonus

### Le module `logging`

Au lieu de `print("[DEBUG]...")`, les outils sérieux utilisent `logging`, qu'on peut activer/désactiver et rediriger vers un fichier :

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Analyse démarrée")
logger.warning("IP suspecte détectée")
logger.error("Fichier illisible")
```


## ❌ Erreur classique

```python
# Capturer toutes les erreurs sans les nommer (masque les vrais bugs)
try:
    analyser()
except:                         # ❌ trop large
    print("Erreur")

try:
    analyser()
except FileNotFoundError as e:  # ✅ erreur précise
    print(f"Fichier : {e}")

# Laisser des print de debug dans la version finale
print("[DEBUG] x =", x)        # ← pense à les retirer

# Ne pas tester les cas limites — teste toujours :
```


```bash
python3 parser.py                          # pas d'argument ?
python3 parser.py absent.log               # fichier inexistant ?
python3 parser.py vide.log                 # fichier vide ?
python3 parser.py "log avec espaces.txt"   # espaces dans le nom ?
```


## Exercices

**Guidé :** Reprends ton parser de logs et entoure l'ouverture du fichier d'un `try/except FileNotFoundError`. Teste-le avec un fichier inexistant pour vérifier qu'il affiche un message propre au lieu de planter.

**Autonome :** Écris une fonction `lire_port(texte)` qui tente `int(texte)` dans un `try/except ValueError` et retourne le port si valide, ou `None` sinon. Teste-la avec `"443"` et `"abc"`.

## ✅ Tu sais maintenant…

- Lire un traceback (de bas en haut) et reconnaître les 5 erreurs fréquentes
- Déboguer avec `print("[DEBUG]...")`
- Gérer les erreurs avec `try/except` (par type) et `finally`
- Rendre un parser robuste face aux fichiers absents et lignes mal formées
- Structurer proprement avec des fonctions et `if __name__ == "__main__":`

-----
