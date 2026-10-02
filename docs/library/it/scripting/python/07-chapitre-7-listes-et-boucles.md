---
title: Chapitre 7 — Listes et boucles
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'une liste ?

Une liste est une **collection ordonnée de valeurs**, modifiable. C'est la structure la plus utilisée en Python — idéale pour stocker une série d'IOC, des lignes de log, des IP à bloquer.

```python
ips_suspectes = ["203.0.113.5", "198.51.100.9", "203.0.113.7"]
ports_sensibles = [22, 23, 445, 3389]
vide = []
```


### Accéder aux éléments

```python
ips = ["203.0.113.5", "198.51.100.9"]

print(ips[0])       # "203.0.113.5" (premier)
print(ips[-1])      # "198.51.100.9" (dernier)
print(len(ips))     # 2
```


### Modifier, ajouter, supprimer

```python
ips = ["203.0.113.5", "198.51.100.9"]

ips.append("203.0.113.7")    # ajouter à la fin
print(ips)   # ['203.0.113.5', '198.51.100.9', '203.0.113.7']

ips.remove("198.51.100.9")   # supprimer par valeur
print(ips)   # ['203.0.113.5', '203.0.113.7']

derniere = ips.pop()         # supprimer le dernier et le récupérer
print(derniere)              # "203.0.113.7"
```


### Tester l'appartenance

```python
liste_noire = ["203.0.113.5", "198.51.100.9"]

print("203.0.113.5" in liste_noire)    # True — IP connue malveillante
print("8.8.8.8" in liste_noire)        # False
```


C'est l'opérateur `in` du chapitre 4, qui marche aussi sur les listes. C'est exactement comme ça qu'on vérifie une IP contre une liste de blocage.

### Trier et dédoublonner

```python
ports = [443, 22, 80, 22, 8080]

ports.sort()              # trie la liste elle-même
print(ports)              # [22, 22, 80, 443, 8080]

uniques = sorted(set(ports))   # set() supprime les doublons, sorted() trie
print(uniques)            # [22, 80, 443, 8080]
```


> **Astuce cyber :** `set(liste)` enlève les doublons. Très pratique pour obtenir la liste des IP **uniques** vues dans un log.

### Le slicing sur les listes

Comme pour les chaînes :

```python
iocs = ["a", "b", "c", "d", "e"]
print(iocs[:3])     # ['a', 'b', 'c'] (les 3 premiers)
print(iocs[-2:])    # ['d', 'e'] (les 2 derniers)
```


-----

## Les boucles

### La boucle `for` : parcourir une liste

```python
ips = ["203.0.113.5", "198.51.100.9", "203.0.113.7"]

for ip in ips:
    print(f"[+] Analyse de {ip}")
```


```
[+] Analyse de 203.0.113.5
[+] Analyse de 198.51.100.9
[+] Analyse de 203.0.113.7
```


La variable `ip` prend successivement chaque valeur. L'indentation (4 espaces) délimite le bloc répété.

> **Comparaison avec Bash :** `for ip in "${ips[@]}"; do ... done` → en Python : `for ip in ips:` + bloc indenté. Plus court, pas de `do`/`done`.

### `range()` : générer une séquence de nombres

```python
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

for port in range(20, 23):
    print(port)        # 20, 21, 22
```


> **Attention :** `range(20, 23)` va de 20 à **22** (borne supérieure exclue).

### La boucle `while`

Répète tant qu'une condition est vraie :

```python
tentatives = 0

while tentatives < 3:
    print(f"Tentative {tentatives + 1}")
    tentatives += 1
```


> **Attention :** si tu oublies `tentatives += 1`, la boucle tourne **à l'infini**. `Ctrl+C` pour l'arrêter.

### `break` et `continue`

```python
# break — sortir de la boucle dès qu'on trouve
liste_noire = ["203.0.113.5", "198.51.100.9"]
for ip in liste_noire:
    if ip == "198.51.100.9":
        print("[!] IP recherchée trouvée, on arrête")
        break

# continue — sauter au tour suivant
for ligne in ["INFO ok", "", "ERROR fail", ""]:
    if not ligne:          # ligne vide
        continue           # on l'ignore
    print(f"Traitée : {ligne}")
```


### `enumerate()` : avoir l'index ET la valeur

Très pratique pour numéroter les lignes d'un log :

```python
lignes = ["connexion ok", "echec auth", "connexion ok"]

for numero, ligne in enumerate(lignes, start=1):
    print(f"Ligne {numero} : {ligne}")
```


```
Ligne 1 : connexion ok
Ligne 2 : echec auth
Ligne 3 : connexion ok
```


## Très utile en pratique

### Construire une liste dans une boucle (filtrer)

Le pattern le plus fréquent en analyse de logs : parcourir, tester, garder ce qui nous intéresse.

```python
lignes = [
    "Accepted password for alice",
    "Failed password for root",
    "Failed password for admin",
    "Accepted password for bob",
]

echecs = []                      # liste vide au départ
for ligne in lignes:
    if "Failed password" in ligne:
        echecs.append(ligne)     # on garde les échecs

print(f"[!] {len(echecs)} échec(s) détecté(s)")
for e in echecs:
    print(f"    {e}")
```


### La boucle infinie volontaire (menu d'outil)

```python
while True:
    action = input("Action (analyser/quitter) : ")
    if action == "quitter":
        print("Au revoir")
        break
    print(f"[+] Action : {action}")
```


### Compter avec un dictionnaire (aperçu)

On verra les dictionnaires au chapitre 9, mais voici un avant-goût : compter combien de fois chaque IP apparaît.

```python
ips = ["203.0.113.5", "198.51.100.9", "203.0.113.5", "203.0.113.5"]

compteur = {}
for ip in ips:
    compteur[ip] = compteur.get(ip, 0) + 1

print(compteur)   # {'203.0.113.5': 3, '198.51.100.9': 1}
```


## Application cyber — compter les échecs par IP

Combinons tout : parcourir des lignes de log, extraire l'IP, et compter les échecs par IP. C'est un mini-détecteur de force brute.

```python
lignes = [
    "Failed password for root from 203.0.113.5",
    "Failed password for admin from 203.0.113.5",
    "Accepted password for alice from 10.0.0.4",
    "Failed password for root from 203.0.113.5",
    "Failed password for root from 198.51.100.9",
]

echecs_par_ip = {}

for ligne in lignes:
    if "Failed password" in ligne:
        # L'IP est le dernier champ de la ligne
        ip = ligne.split()[-1]
        echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

print("[*] Échecs de connexion par IP :")
for ip, nb in echecs_par_ip.items():
    marqueur = "[!]" if nb >= 3 else "   "
    print(f"  {marqueur} {ip} : {nb} échec(s)")
```


Résultat :

```
[*] Échecs de connexion par IP :
   [!] 203.0.113.5 : 3 échec(s)
       198.51.100.9 : 1 échec(s)
```


On a utilisé : une boucle `for`, le test `in`, `split()` pour isoler l'IP, et un compteur. L'IP `203.0.113.5` avec 3 échecs est marquée `[!]` — c'est une candidate au blocage. Ce petit script est déjà un vrai outil défensif.

## Bonus

### Les compréhensions de liste

Syntaxe compacte pour filtrer/transformer une liste :

```python
lignes = ["Failed root", "Accepted alice", "Failed admin"]

# Au lieu d'une boucle + append :
echecs = [l for l in lignes if "Failed" in l]
print(echecs)    # ['Failed root', 'Failed admin']
```


Puissant et élégant, mais la boucle classique reste parfaitement correcte pour débuter.

### Les tuples — les listes immuables

Un **tuple** est comme une liste mais **non modifiable** (parenthèses au lieu de crochets). Utile pour un couple de valeurs fixes, comme une paire (IP, port) :

```python
cible = ("203.0.113.5", 22)
print(cible[0])    # "203.0.113.5"
cible[0] = "x"     # ❌ TypeError — un tuple ne se modifie pas
```


## ❌ Erreur classique

```python
# Oublier l'indentation dans la boucle
for ip in ips:
print(ip)              # ❌ IndentationError

# Modifier une liste qu'on parcourt (dangereux)
ips = ["a", "b", "c"]
for ip in ips:
    if ip == "b":
        ips.remove(ip)    # ❌ comportement imprévisible
# Solution : construire une nouvelle liste filtrée

# Boucle infinie par oubli d'incrément
n = 0
while n < 5:
    print(n)
    # ❌ oubli de n += 1 → boucle infinie

# Dépasser les bornes de la liste
ips = ["a", "b"]
print(ips[5])          # ❌ IndexError: list index out of range
```


## Exercices

**Guidé :** Crée un script `bloquer.py` qui contient une liste d'IP en liste noire, prend une IP en argument, et affiche `"[!] IP bloquée"` si elle est dans la liste, sinon `"[+] IP autorisée"`.

**Autonome :** Crée un script `iocs_uniques.py` qui prend plusieurs IOC en arguments (`sys.argv[1:]`), supprime les doublons (avec `set`), les trie, et les affiche numérotés avec `enumerate`.

**Défi :** Crée un script `top_ip.py` qui contient une liste de lignes de log (en dur), compte les échecs par IP (comme dans l'« Application cyber »), et affiche uniquement les IP ayant **3 échecs ou plus**.

## 🧩 Mini-projet (chapitres 5-7)

Crée un script `mini_soc.py` qui :

1. Contient une liste de lignes de log (en dur dans le script).
2. Parcourt les lignes et compte : le nombre total de lignes, le nombre d'échecs (`Failed password`), le nombre de connexions réussies (`Accepted password`).
3. Construit la liste des IP **uniques** ayant échoué.
4. Affiche un petit rapport résumé avec ces chiffres.

## ✅ Tu sais maintenant…

- Créer, modifier et parcourir une liste (`append`, `remove`, `pop`)
- Tester l'appartenance avec `in` (ex. IP contre une liste noire)
- Trier (`sort`, `sorted`) et dédoublonner (`set`)
- Parcourir avec `for ... in ...:` et générer des nombres avec `range()`
- Répéter avec `while`, contrôler avec `break` et `continue`
- Numéroter avec `enumerate()`
- Filtrer des lignes de log et compter par IP — un vrai mini-détecteur

-----
