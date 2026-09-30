---
title: Chapitre 6 — Chaînes de caractères
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Les chaînes sont des séquences

Une chaîne (`str`) n'est pas un bloc opaque : c'est une **séquence ordonnée de caractères**, chacun accessible par sa position (son **index**).

```
 Texte :   e    v    i    l
 Index :   0    1    2    3
 Négatif: -4   -3   -2   -1
```


```python
domaine = "evil.com"

print(domaine[0])      # e (premier)
print(domaine[-1])     # m (dernier)
print(domaine[-3])     # c
```


> **Rappel :** les index commencent à **0**.

### Longueur d'une chaîne

```python
hash_md5 = "d41d8cd98f00b204e9800998ecf8427e"
print(len(hash_md5))    # 32 — un MD5 fait toujours 32 caractères hexadécimaux
```


Mesurer la longueur d'un hash est une première vérification utile : 32 → MD5, 40 → SHA-1, 64 → SHA-256.

### Le slicing : extraire une partie

Syntaxe `[début:fin]` (de `début` **inclus** à `fin` **exclu**) :

```python
url = "https://evil.com/malware.exe"

print(url[0:5])     # "https"
print(url[8:16])    # "evil.com"
print(url[:5])      # "https"   (du début à 4)
print(url[8:])      # "evil.com/malware.exe"  (de 8 à la fin)
```


Slicing avec un **pas** :

```python
texte = "abcdef"
print(texte[::-1])     # "fedcba" — inverser la chaîne
```


### Les méthodes essentielles

Les chaînes ont des **méthodes** : des fonctions appelées avec un point.

```python
ligne = "  Failed Password For ROOT  "

print(ligne.upper())        # "  FAILED PASSWORD FOR ROOT  "
print(ligne.lower())        # "  failed password for root  "
print(ligne.strip())        # "Failed Password For ROOT" (espaces enlevés)
print(ligne.strip().lower()) # "failed password for root"
print(ligne.replace("ROOT", "[REDACTED]").strip())  # "Failed Password For [REDACTED]"
```


> **Différence avec Bash :** au lieu de `${var^^}` ou `${var/ancien/nouveau}`, on utilise des **méthodes** : `var.upper()`, `var.replace()`. Plus lisible.

> **Réflexe cyber :** avant de comparer du texte (un domaine, un mot-clé), on **normalise** souvent avec `.lower()` et `.strip()`, car `Evil.COM`, `evil.com` et `  evil.com ` désignent la même chose.

### Découper et joindre

```python
# split : découper en liste
ioc_brut = "203.0.113.5,evil.com,bad.net"
iocs = ioc_brut.split(",")
print(iocs)      # ['203.0.113.5', 'evil.com', 'bad.net']

# join : recoller une liste en chaîne
print(" | ".join(iocs))   # "203.0.113.5 | evil.com | bad.net"
```


`split()` sans argument découpe sur les espaces — parfait pour séparer les champs d'une ligne de log :

```python
ligne = "203.0.113.5 - - [10/Jan/2025] GET /admin"
champs = ligne.split()
print(champs[0])    # "203.0.113.5" — l'IP est le premier champ
```


### Chercher dans une chaîne

```python
ligne = "Failed password for root from 203.0.113.5"

print("root" in ligne)              # True
print(ligne.find("from"))           # 26 (position) ; -1 si absent
print(ligne.count("o"))             # nombre de 'o'

fichier = "facture.pdf.exe"
print(fichier.endswith(".exe"))     # True — extension exécutable, suspect !
print(fichier.startswith("facture")) # True
```


### Les chaînes sont immuables

On ne peut **pas** modifier une chaîne directement :

```python
mot = "evil"
mot[0] = "E"       # ❌ TypeError
```


Pour « modifier », on crée une **nouvelle** chaîne (`replace`, `upper`, etc. renvoient toujours une nouvelle chaîne).

## Très utile en pratique

### Les f-strings avancées (alignement, décimales)

Utile pour produire des rapports lisibles :

```python
ip = "203.0.113.5"
nb = 47
print(f"{ip:<18} {nb:>5} échecs")    # IP alignée à gauche, nombre à droite
# → 203.0.113.5            47 échecs

numero = 42
print(f"Alerte #{numero:04d}")        # "Alerte #0042"
```


### Tableau récapitulatif des méthodes

| Méthode           | Effet                        | Exemple cyber                       |
| ----------------- | ---------------------------- | ----------------------------------- |
| `len(s)`          | Longueur                     | `len(hash)` → 32 / 40 / 64          |
| `s.upper()`       | Majuscules                   | normaliser un hash                  |
| `s.lower()`       | Minuscules                   | normaliser un domaine               |
| `s.strip()`       | Enlever espaces début/fin    | nettoyer une ligne lue              |
| `s.replace(a, b)` | Remplacer                    | anonymiser une IP dans un rapport   |
| `s.split(sep)`    | Découper en liste            | séparer les champs d'un log         |
| `sep.join(liste)` | Recoller une liste           | produire une ligne CSV              |
| `s.find(x)`       | Position de x (-1 si absent) | localiser un mot-clé                |
| `s.count(x)`      | Nombre d'occurrences         | compter les `Failed` dans une ligne |
| `s.startswith(x)` | Commence par x ?             | `url.startswith("http")`            |
| `s.endswith(x)`   | Finit par x ?                | `fichier.endswith(".exe")`          |
| `s.isdigit()`     | Que des chiffres ?           | valider un port saisi               |

## Application cyber — normaliser et inspecter un IOC

Un même indicateur peut arriver sous plusieurs formes. Normalisons un domaine et extrayons des infos d'une URL.

```python
# Normaliser un domaine (sources hétérogènes)
domaine_brut = "  EVIL.com  "
domaine = domaine_brut.strip().lower()
print(domaine)                  # "evil.com"

# Inspecter une URL simplement (sans regex, pour l'instant)
url = "https://evil.com/login.php?id=1"

print(url.startswith("https"))  # True — connexion chiffrée
print(".exe" in url)            # False
print("evil.com" in url)        # True — domaine connu malveillant

# Extraire grossièrement le domaine d'une URL
sans_schema = url.replace("https://", "").replace("http://", "")
domaine_url = sans_schema.split("/")[0]
print(domaine_url)              # "evil.com"
```


Ici, on a transformé `"  EVIL.com  "` en `"evil.com"` (comparable de façon fiable) et extrait le domaine d'une URL avec `replace` + `split`. Au chapitre 13, les regex rendront ce genre d'extraction beaucoup plus robuste — mais ces méthodes de base suffisent déjà pour beaucoup de cas.

## Bonus

### Les caractères d'échappement

```python
print("Ligne1\nLigne2")          # \n = retour à la ligne
print("Champ1\tChamp2")          # \t = tabulation
print("Chemin : C:\\Windows")    # \\ = un seul backslash
```


### Les raw strings (chemins Windows)

```python
chemin = r"C:\Users\Public\malware.exe"   # le r empêche l'interprétation des \
print(chemin)   # C:\Users\Public\malware.exe
```


Indispensable quand tu manipules des chemins Windows dans un contexte forensic.

## ❌ Erreur classique

```python
# Essayer de modifier une chaîne
empreinte = "abc"
empreinte[0] = "A"     # ❌ TypeError — les chaînes sont immuables

# Comparer sans normaliser
if "evil.com" == "Evil.com":   # ❌ False (casse différente)
    pass
if "evil.com" == "Evil.com".lower():  # ✅ True

# Oublier que find() renvoie -1 (pas une erreur) si absent
pos = "log normal".find("Failed")
print(pos)             # -1 — pas trouvé, mais pas d'erreur

# Confondre fonction et méthode
len("abc")             # ✅ fonction
"abc".upper()          # ✅ méthode
"abc".len()            # ❌ len n'est pas une méthode
```


## Exercices

**Guidé :** Crée un script `reformat_ip.py` qui prend une IP avec des tirets (`203-0-113-5`) en argument et l'affiche reformatée avec des points (`203.0.113.5`). Utilise `.replace()`.

**Autonome :** Crée un script `inspect_url.py` qui prend une URL en argument et affiche : son schéma (`http`/`https` via `startswith`), si elle se termine par une extension exécutable (`.exe`, `.scr`), le domaine (via `replace` + `split`), et la longueur totale de l'URL.

## ✅ Tu sais maintenant…

- Accéder aux caractères par index (`mot[0]`, `mot[-1]`) et au slicing (`url[8:16]`, `[::-1]`)
- Les méthodes clés : `upper`, `lower`, `strip`, `replace`, `split`, `join`, `find`, `count`, `startswith`, `endswith`
- Normaliser un IOC (`.strip().lower()`) avant de le comparer
- Découper une ligne de log en champs avec `split()`
- Que les chaînes sont immuables (on crée une nouvelle chaîne)

-----
