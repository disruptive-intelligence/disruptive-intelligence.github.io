---
title: Chapitre 3 — Arguments, terminal et scripts paramétrés
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - index.md
---

## Le minimum à savoir

### C'est quoi un argument ?

Au chapitre 2, tu demandais des infos pendant l'exécution (avec `input()`). Mais il y a une autre façon de fournir des infos : **les arguments**, donnés au moment du lancement.

```bash
python3 analyse_ip.py 203.0.113.5
#                      ↑ c'est un argument
```


Les arguments rendent le script utilisable **sans interaction** : tu lances la commande et c'est fait. C'est **essentiel pour l'automatisation** — un script paramétré peut être appelé en boucle, depuis un autre script, ou planifié avec `cron`.

### `sys.argv` — la liste des arguments

Pour accéder aux arguments, on utilise le module `sys` et sa variable `argv` :

```python
import sys

print(sys.argv)
```


```bash
python3 test.py 203.0.113.5 evil.com 80
```


```
['test.py', '203.0.113.5', 'evil.com', '80']
```


`sys.argv` est une **liste** (vue en détail au chapitre 7). Pour l'instant, retiens :

- `sys.argv[0]` → le nom du script
- `sys.argv[1]` → le premier argument
- `sys.argv[2]` → le deuxième argument
- `len(sys.argv)` → le nombre total d'éléments (script + arguments)

```python
import sys

print(f"Script   : {sys.argv[0]}")
print(f"Cible     : {sys.argv[1]}")
print(f"Arguments : {len(sys.argv) - 1}")
```


```bash
python3 scan.py 203.0.113.5
```


```
Script   : scan.py
Cible     : 203.0.113.5
Arguments : 1
```


> **Comparaison avec Bash :** `sys.argv[1]` ≈ `$1`, `sys.argv[2]` ≈ `$2`, `len(sys.argv) - 1` ≈ `$#`. La différence : en Python les arguments sont dans une liste indexée à partir de 0, et le nom du script est `sys.argv[0]` (comme `$0`).

### Le `import` — un mot nouveau

`import sys` est ta première rencontre avec `import`. C'est un concept fondamental : **importer un module**.

Un module est un fichier contenant des fonctions et variables prêtes à l'emploi. `sys` est fourni avec Python et donne accès à des infos sur le système (arguments, version…).

La ligne `import sys` dit à Python : « charge le module `sys` ». Ensuite tu accèdes à ses fonctionnalités avec `sys.quelque_chose`.

On utilisera beaucoup de modules en cyber : `re` (regex), `hashlib` (hash), `ipaddress` (réseaux), `json`, `csv`… Le principe sera toujours le même.

> **Bonne pratique :** les `import` se mettent **tout en haut** du script.

### Vérifier qu'un argument est fourni

Un script qui attend un argument doit **toujours vérifier** qu'il a été donné, sinon Python plante avec `IndexError` :

```python
import sys

if len(sys.argv) < 2:
    print(f"[-] Erreur : donne une IP en argument.")
    print(f"Utilisation : python3 {sys.argv[0]} <ip>")
    sys.exit(1)

ip = sys.argv[1]
print(f"[+] Analyse de {ip}")
```


> **Note :** `sys.exit(1)` arrête le script avec un code d'erreur (comme `exit 1` en Bash). `sys.exit(0)` = succès. On met `sys.exit(1)` quand quelque chose ne va pas.

> **Pas de panique :** on utilise ici un `if` qu'on verra en détail au chapitre 5. La logique est intuitive : « si le nombre d'arguments est inférieur à 2, affiche un message et quitte ».

### La différence `input()` vs arguments

|`input()`                              |Arguments (`sys.argv`)                            |
|---------------------------------------|--------------------------------------------------|
|L'utilisateur tape pendant l'exécution |L'info est fournie au lancement                   |
|Pratique pour un script interactif     |Pratique pour l'automatisation                    |
|Difficile à enchaîner                  |Facile à intégrer dans un cron, un pipeline, un SOAR|

En pratique, beaucoup d'outils défensifs utilisent les arguments pour les paramètres (IP, fichier de log…) et `input()` pour une confirmation (« bloquer cette IP ? o/n »).

### Les arguments sont toujours du texte

Comme `input()`, les arguments de `sys.argv` sont **toujours des chaînes** (`str`). Si tu attends un nombre, convertis :

```python
import sys

if len(sys.argv) < 3:
    print(f"Utilisation : python3 {sys.argv[0]} <ip> <port>")
    sys.exit(1)

ip = sys.argv[1]            # reste du texte (une IP est du texte)
port = int(sys.argv[2])     # converti en entier pour comparaison
print(f"[+] {ip} sur le port {port}")
if port < 1024:
    print("[!] Port système")
```


## Très utile en pratique

### Accéder à tous les arguments d'un coup

`sys.argv[1:]` donne **tous les arguments sauf le nom du script** — très pratique pour traiter une liste d'IOC passés en ligne de commande :

```python
import sys

iocs = sys.argv[1:]
print(f"[+] {len(iocs)} IOC à traiter : {iocs}")
```


```bash
python3 traite.py 203.0.113.5 evil.com bad-domain.net
# → [+] 3 IOC à traiter : ['203.0.113.5', 'evil.com', 'bad-domain.net']
```


> **Explication :** `sys.argv[1:]` utilise le **slicing** (détaillé aux chapitres 6 et 7). `[1:]` signifie « tout à partir de la position 1 » — donc tout sauf le nom du script.

### Script complet : un outil paramétré

Un petit outil qui qualifie une cible selon un type passé en argument :

```python
import sys

if len(sys.argv) < 2:
    print(f"Utilisation : python3 {sys.argv[0]} <indicateur> [type]")
    print("Types : ip (défaut), domaine, hash")
    sys.exit(1)

indicateur = sys.argv[1]

# Si un deuxième argument est fourni, on l'utilise ; sinon "ip" par défaut
if len(sys.argv) >= 3:
    type_ioc = sys.argv[2]
else:
    type_ioc = "ip"

if type_ioc == "ip":
    print(f"[+] IOC de type IP    : {indicateur}")
elif type_ioc == "domaine":
    print(f"[+] IOC de type domaine : {indicateur}")
elif type_ioc == "hash":
    print(f"[+] IOC de type hash    : {indicateur}")
else:
    print(f"[-] Type '{type_ioc}' non reconnu.")
```


```bash
python3 ioc.py 203.0.113.5            # → [+] IOC de type IP    : 203.0.113.5
python3 ioc.py evil.com domaine       # → [+] IOC de type domaine : evil.com
python3 ioc.py d41d8cd9... hash       # → [+] IOC de type hash    : d41d8cd9...
```


## Application cyber

Voici le squelette d'un outil défensif typique : il prend **un fichier de log en argument** et vérifie qu'il a bien été fourni. C'est la base de tous les parsers de logs qu'on écrira plus loin.

```python
import sys

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
    sys.exit(1)

fichier_log = sys.argv[1]
print(f"[+] Analyse du fichier de log : {fichier_log}")
# Au chapitre 10, on apprendra à ouvrir et lire ce fichier ligne par ligne.
```


Ce schéma — *vérifier l'argument, le stocker, puis traiter* — revient dans la quasi-totalité des outils en ligne de commande, qu'ils analysent un log, calculent un hash ou interrogent une API.

## Bonus

### `argparse` — pour les outils sérieux

Pour les scripts avec beaucoup d'options (`-v`, `--output rapport.json`), Python fournit `argparse`, l'équivalent professionnel. Un aperçu :

```python
import argparse

parser = argparse.ArgumentParser(description="Analyseur d'IOC")
parser.add_argument("ioc", help="L'indicateur à analyser")
parser.add_argument("-t", "--type", default="ip", help="Type d'IOC")
args = parser.parse_args()

print(f"[+] {args.ioc} (type : {args.type})")
```


```bash
python3 outil.py 203.0.113.5 --type ip
python3 outil.py --help        # affiche l'aide automatiquement
```


C'est puissant, mais `sys.argv` suffit largement pour débuter.

## ❌ Erreur classique

```python
# Oublier de vérifier le nombre d'arguments
import sys
ip = sys.argv[1]    # ❌ IndexError si lancé sans argument

# Il faut TOUJOURS vérifier :
if len(sys.argv) < 2:
    print("[-] Argument manquant")
    sys.exit(1)

# Oublier que les arguments sont du texte
import sys
port = sys.argv[1]
double = port * 2     # ❌ "22" * 2 = "2222" (texte répété, pas un calcul)
port = int(sys.argv[1])
double = port * 2     # ✅ 44

# Confondre sys.argv[0] et sys.argv[1]
# sys.argv[0] = nom du script, sys.argv[1] = PREMIER argument
```


## Exercices

**Guidé :** Crée un script `qualifie_ip.py` qui prend une IP en argument, vérifie qu'elle est fournie, et affiche `"[+] IP à analyser : {ip}"`. Sans argument, affiche un message d'utilisation et quitte avec `sys.exit(1)`.

**Autonome :** Crée un script `ports.py` qui prend deux numéros de port en arguments, les convertit en entiers, et affiche lequel est le plus petit, lequel est le plus grand, et si l'un des deux est inférieur à 1024 (port « système »). Vérifie que les deux arguments sont fournis.

## ✅ Tu sais maintenant…

- Passer des arguments à un script (`sys.argv`) — la base des outils en ligne de commande
- Accéder aux arguments par leur position (`sys.argv[1]`, `sys.argv[2]`…)
- Récupérer tous les arguments avec `sys.argv[1:]` (ex. une liste d'IOC)
- Vérifier le nombre d'arguments avec `len(sys.argv)`
- La différence entre `input()` (interactif) et `sys.argv` (automatisation)
- Importer un module avec `import` et quitter avec `sys.exit()`

-----
