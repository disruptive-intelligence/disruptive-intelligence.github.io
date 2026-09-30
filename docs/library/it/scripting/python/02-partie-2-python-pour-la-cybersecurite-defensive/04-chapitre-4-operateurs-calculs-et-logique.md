---
title: Chapitre 4 — Opérateurs, calculs et logique
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Le calcul en Python

Python est un excellent calculateur, et il gère nativement les nombres à virgule :

```python
echecs = 47
fenetre = 5      # minutes

print(f"Total          : {echecs}")
print(f"Par minute     : {echecs / fenetre}")    # 9.4 (décimale !)
print(f"Par minute (entier) : {echecs // fenetre}")  # 9 (partie entière)
print(f"Reste          : {echecs % fenetre}")    # 2
print(f"Puissance      : {2 ** 10}")             # 1024
```


> **Différence majeure avec Bash :** en Python, `/` donne un résultat **décimal** (`9.4`). Pour la division entière (comme en Bash), utilise `//`. Et pas besoin de `$(( ))` — tu écris les calculs directement.

### Les opérateurs arithmétiques

| Opérateur | Signification       | Exemple  | Résultat    |
| --------- | ------------------- | -------- | ----------- |
| `+`       | Addition            | `5 + 3`  | `8`         |
| `-`       | Soustraction        | `5 - 3`  | `2`         |
| `*`       | Multiplication      | `5 * 3`  | `15`        |
| `/`       | Division (décimale) | `5 / 3`  | `1.6666...` |
| `//`      | Division entière    | `5 // 3` | `1`         |
| `%`       | Modulo (reste)      | `5 % 3`  | `2`         |
| `**`      | Puissance           | `2 ** 3` | `8`         |

### Les raccourcis d'affectation

Au lieu de `x = x + 1`, écris `x += 1`. Indispensable pour les compteurs (compter des échecs de connexion, par exemple) :

```python
echecs = 0
echecs += 1       # 1
echecs += 1       # 2
echecs += 5       # 7
```


### Les opérateurs de comparaison

Pour tester si une valeur est plus grande, plus petite, égale à une autre :

| Opérateur | Signification     | Exemple      | Résultat |
| --------- | ----------------- | ------------ | -------- |
| `==`      | Égal              | `200 == 200` | `True`   |
| `!=`      | Différent         | `404 != 200` | `True`   |
| `<`       | Inférieur         | `80 < 443`   | `True`   |
| `>`       | Supérieur         | `443 > 80`   | `True`   |
| `<=`      | Inférieur ou égal | `5 <= 5`     | `True`   |
| `>=`      | Supérieur ou égal | `8 >= 7`     | `True`   |

> **Différence avec Bash :** on utilise les symboles mathématiques (`==`, `<`, `>`) au lieu de `-eq`, `-lt`, `-gt`. Bien plus intuitif.

```python
code_http = 404
print(code_http == 200)    # False
print(code_http >= 400)    # True — c'est une erreur côté client/serveur
```


Le résultat d'une comparaison est toujours un **booléen** (`True` / `False`).

> **Ne pas confondre :** `=` **affecte** une valeur (`score = 8`), `==` **compare** (`score == 8`). C'est l'erreur la plus fréquente.

### Les opérateurs logiques

Python utilise des **mots** : `and`, `or`, `not`.

| Opérateur | Signification                     | Équivalent Bash |
| --------- | --------------------------------- | --------------- |
| `and`     | ET — les deux doivent être vraies | `&&`            |
| `or`      | OU — au moins une doit être vraie | `\|\|`          |
| `not`     | NON — inverse la condition        | `!`             |

```python
nb_echecs = 47
ip_externe = True

# Alerte si beaucoup d'échecs ET depuis l'extérieur
print(nb_echecs > 10 and ip_externe)    # True

code = 503
print(code == 502 or code == 503)        # True — erreur serveur

print(not ip_externe)                     # False
```


> **Astuce Python :** pour tester un intervalle, écriture mathématique naturelle (impossible en Bash) :

```python
port = 8080
print(1024 <= port <= 49151)    # True — port "enregistré"
```


### L'opérateur `in`

`in` teste si quelque chose est **contenu** dans autre chose. Extrêmement utile en cyber pour chercher un mot-clé dans une ligne de log :

```python
ligne = "Failed password for root from 203.0.113.5"
print("Failed password" in ligne)    # True
print("root" in ligne)               # True
print("sudo" in ligne)               # False
```


C'est un outil très puissant que Bash n'a pas sous cette forme.

## Très utile en pratique

### Priorité des opérateurs

Comme en maths, `*` passe avant `+`. En cas de doute, mets des parenthèses :

```python
score = 2 + 3 * 4     # 14 (le * d'abord)
score = (2 + 3) * 4   # 20
```


### Le modulo `%` en pratique

Le modulo donne le **reste**. Utile pour traiter une ligne sur N dans un gros log, ou détecter un nombre pair :

```python
numero_ligne = 1000
if numero_ligne % 100 == 0:
    print(f"[+] {numero_ligne} lignes traitées")
```


### Arrondir un nombre

```python
taux = 47 / 5
print(round(taux, 1))      # 9.4
print(round(taux))          # 9
```


## Application cyber — calculer un score de risque

Combinons calculs et logique pour produire un **score de risque** simple à partir de plusieurs signaux. C'est exactement le genre de logique qu'un SIEM applique pour prioriser les alertes.

```python
# Signaux observés sur une IP source
nb_echecs = 47          # tentatives de connexion échouées
ip_externe = True       # l'IP vient d'Internet (pas du réseau interne)
cible_sensible = True   # la cible est un serveur critique (ex. contrôleur de domaine)

# On construit un score sur 10
score = 0
score += nb_echecs * 0.1        # plus d'échecs = plus de risque
if ip_externe:
    score += 2
if cible_sensible:
    score += 3

# On plafonne à 10
score = min(score, 10)

print(f"[!] Score de risque : {round(score, 1)}/10")

# Décision logique
if score >= 8:
    print("[!] CRITIQUE — investigation immédiate")
elif score >= 5:
    print("[*] Moyen — à surveiller")
else:
    print("[+] Faible")
```


Résultat :

```
[!] Score de risque : 9.7/10
[!] CRITIQUE — investigation immédiate
```


On a utilisé : des calculs (`*`, `+=`), une fonction (`min`), des comparaisons (`>=`) et des conditions. Tu remarques qu'on a tout combiné — c'est le cœur de l'automatisation défensive.

## Bonus

### Les grands nombres et la lisibilité

Python gère des entiers de taille illimitée. Pour la lisibilité, on peut utiliser des underscores comme séparateurs :

```python
limite_octets = 1_000_000_000    # 1 Go, plus lisible
print(limite_octets)              # → 1000000000
```


## ❌ Erreur classique

```python
# Confondre = et ==
if score = 8:        # ❌ SyntaxError — c'est une affectation
if score == 8:       # ✅ Correct — c'est un test

# Diviser par zéro
taux = echecs / 0    # ❌ ZeroDivisionError

# Mélanger texte et nombre venant d'un argument
port = "443"
double = port * 2     # ❌ "443443" (texte répété)
double = int(port) * 2  # ✅ 886

# Comparer une IP (texte) avec < comme un nombre — n'a pas le sens attendu
print("203.0.113.5" < "203.0.113.50")   # comparaison alphabétique, pas numérique !
# (Pour comparer vraiment des IP, on utilisera le module ipaddress au chapitre 19.)
```


## Exercices

**Guidé :** Crée un script `risque.py` qui prend un nombre d'échecs de connexion en argument, le convertit en entier, calcule un score `echecs * 0.2`, et affiche `"CRITIQUE"` si le score dépasse 8, sinon `"OK"`.

**Autonome :** Crée un script `verdict_http.py` qui prend un code HTTP en argument (entier) et affiche : `"Succès"` (200-299), `"Redirection"` (300-399), `"Erreur client"` (400-499), `"Erreur serveur"` (500-599). Utilise les comparaisons et `and`.

## ✅ Tu sais maintenant…

- Faire des calculs avec les opérateurs arithmétiques
- La différence entre `/` (décimale) et `//` (entière)
- Comparer des valeurs avec `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combiner des conditions avec `and`, `or`, `not`
- Utiliser `in` pour chercher un mot-clé dans une ligne de log
- Construire un score de risque simple en combinant calculs et logique
- La différence entre `=` (affectation) et `==` (comparaison)

-----
