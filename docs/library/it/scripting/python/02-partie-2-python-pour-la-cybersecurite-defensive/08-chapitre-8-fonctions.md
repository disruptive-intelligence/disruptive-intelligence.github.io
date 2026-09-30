---
title: Chapitre 8 — Fonctions
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'une fonction ?

Une fonction est un **bloc de code réutilisable** auquel tu donnes un nom. En cyber, on encapsule souvent une vérification (« cette extension est-elle dangereuse ? », « cette IP est-elle privée ? ») dans une fonction qu'on réutilise partout.

### Définir et appeler une fonction

```python
def afficher_banniere():
    print("=" * 30)
    print("   Outil SOC v1.0")
    print("=" * 30)

afficher_banniere()
```


> **Note :** on utilise `def` (« define ») + nom + parenthèses + `:`. Le bloc est indenté. Pas d'accolades — c'est l'indentation qui délimite.

> **Règle :** la définition (`def ...`) doit apparaître **avant** l'appel. Python lit le fichier de haut en bas.

### Passer des arguments

```python
def analyser_ip(ip):
    print(f"[+] Analyse de {ip} en cours...")

analyser_ip("203.0.113.5")
analyser_ip("198.51.100.9")
```


> **Différence avec Bash :** en Bash, les arguments d'une fonction étaient `$1`, `$2`. En Python, chaque argument a un **nom clair** (`ip`). Bien plus lisible.

### Retourner un résultat avec `return`

`return` renvoie une valeur au code appelant. C'est ce qui rend une fonction réutilisable dans une condition.

```python
def is_suspicious_extension(nom_fichier):
    extensions_dangereuses = [".exe", ".scr", ".bat", ".js", ".vbs"]
    for ext in extensions_dangereuses:
        if nom_fichier.lower().endswith(ext):
            return True
    return False

print(is_suspicious_extension("facture.pdf.exe"))   # True
print(is_suspicious_extension("rapport.pdf"))        # False

# On l'utilise dans une condition :
if is_suspicious_extension("invoice.scr"):
    print("[!] Fichier potentiellement dangereux")
```


> **Différence majeure avec Bash :** en Bash, `return` ne sert qu'aux codes d'erreur (0-255). En Python, `return` renvoie **n'importe quelle valeur** (un booléen, du texte, une liste…).

Après un `return`, Python sort de la fonction immédiatement.

### Valeurs par défaut

```python
def normaliser_domaine(domaine, en_minuscules=True):
    domaine = domaine.strip()
    if en_minuscules:
        domaine = domaine.lower()
    return domaine

print(normaliser_domaine("  EVIL.com "))        # "evil.com"
print(normaliser_domaine("EVIL.com", False))    # "EVIL.com" (juste strip)
```


Les paramètres avec valeur par défaut viennent **après** les paramètres obligatoires.

### Portée des variables (locale par défaut)

Une variable créée **dans** une fonction n'existe que **dans** cette fonction :

```python
def verifier():
    verdict = "malveillant"     # variable locale
    print(verdict)

verifier()
print(verdict)     # ❌ NameError — "verdict" n'existe pas ici
```


> **Différence avec Bash :** en Bash, les variables d'une fonction sont globales par défaut. En Python, c'est l'inverse : **locales par défaut**. C'est plus sûr.

## Très utile en pratique

### Retourner plusieurs valeurs

```python
def analyser_ligne(ligne):
    champs = ligne.split()
    ip = champs[-1]
    est_echec = "Failed password" in ligne
    return ip, est_echec

ip, echec = analyser_ligne("Failed password for root from 203.0.113.5")
print(ip)      # "203.0.113.5"
print(echec)   # True
```


Python renvoie un **tuple** qu'on « décompacte » dans plusieurs variables.

### Une fonction utile : `is_private_ip()`

Une IP privée (réseau interne) commence par `10.`, `192.168.` ou `172.16.`–`172.31.`. Voici une version simple (on fera mieux avec `ipaddress` au chapitre 19) :

```python
def is_private_ip(ip):
    if ip.startswith("10.") or ip.startswith("192.168."):
        return True
    if ip.startswith("172."):
        # 172.16.x.x à 172.31.x.x
        deuxieme = int(ip.split(".")[1])
        if 16 <= deuxieme <= 31:
            return True
    return False

print(is_private_ip("10.0.0.4"))       # True (interne)
print(is_private_ip("203.0.113.5"))    # False (publique → vient d'Internet)
```


Savoir si une IP est privée ou publique est fondamental : une attaque venant d'une IP **publique** est généralement plus préoccupante.

### Documenter avec une docstring

```python
def calculer_score(nb_echecs, ip_externe):
    """Calcule un score de risque sur 10.

    Arguments :
        nb_echecs : nombre de connexions échouées (int)
        ip_externe : True si l'IP vient d'Internet (bool)
    Retourne : le score arrondi (float)
    """
    score = nb_echecs * 0.1
    if ip_externe:
        score += 2
    return min(round(score, 1), 10)
```


La docstring (entre `"""..."""`) documente la fonction. Accessible avec `help(calculer_score)`.

### Des fonctions qui s'appellent entre elles

```python
def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.")

def qualifier_ip(ip):
    if is_private_ip(ip):
        return f"{ip} → interne"
    return f"{ip} → EXTERNE (à surveiller)"

print(qualifier_ip("10.0.0.4"))        # 10.0.0.4 → interne
print(qualifier_ip("203.0.113.5"))     # 203.0.113.5 → EXTERNE (à surveiller)
```


## Application cyber — une petite boîte à fonctions défensives

Regroupons des vérifications réutilisables. C'est ainsi qu'on construit, brique par brique, une bibliothèque d'analyse.

```python
def normalize_domain(domaine):
    """Met un domaine en forme comparable."""
    return domaine.strip().lower().rstrip(".")

def is_suspicious_extension(nom):
    """True si le fichier a une extension exécutable courante."""
    dangereuses = (".exe", ".scr", ".bat", ".cmd", ".js", ".vbs")
    return nom.lower().endswith(dangereuses)

def is_private_ip(ip):
    """True si l'IP appartient à une plage privée (simplifié)."""
    return ip.startswith("10.") or ip.startswith("192.168.")

# Utilisation combinée
print(normalize_domain("  Evil.COM. "))          # "evil.com"
print(is_suspicious_extension("photo.jpg.exe"))  # True
print(is_private_ip("203.0.113.5"))              # False
```


Astuce : `nom.endswith(dangereuses)` accepte directement un **tuple** d'extensions — pas besoin de boucle. Ces trois fonctions sont la base d'outils plus gros qu'on assemblera aux chapitres 14-15.

## Bonus

### Les arguments nommés

```python
def creer_alerte(ip, niveau, raison):
    return f"[{niveau}] {ip} — {raison}"

# L'ordre n'importe plus si on nomme les arguments :
print(creer_alerte(raison="force brute", ip="203.0.113.5", niveau="CRITIQUE"))
```


### Le nombre variable d'arguments (`*args`)

```python
def compter_iocs(*iocs):
    return len(iocs)

print(compter_iocs("203.0.113.5", "evil.com"))    # 2
print(compter_iocs("a", "b", "c", "d"))           # 4
```


`*iocs` collecte tous les arguments dans un tuple (équivalent du `$@` de Bash).

## ❌ Erreur classique

```python
# Oublier les parenthèses à l'appel
afficher_banniere        # ❌ ne fait rien (référence, pas appel)
afficher_banniere()      # ✅ appelle la fonction

# Oublier return
def is_dangereux(nom):
    nom.endswith(".exe")    # ❌ calcule mais ne retourne rien
resultat = is_dangereux("x.exe")
print(resultat)              # None

def is_dangereux(nom):
    return nom.endswith(".exe")   # ✅

# Mettre du code après return (jamais exécuté)
def f():
    return True
    print("jamais affiché")    # ⚠️ code mort

# Croire qu'une variable locale modifie la globale
total = 0
def ajouter(n):
    total = total + n    # ❌ UnboundLocalError
```


## Exercices

**Guidé :** Crée une fonction `is_blacklisted(ip, liste_noire)` qui retourne `True` si l'IP est dans la liste noire. Teste-la avec une petite liste et deux IP.

**Autonome :** Crée une fonction `hash_type(h)` qui retourne `"MD5"`, `"SHA-1"`, `"SHA-256"` ou `"inconnu"` selon la **longueur** du hash (32, 40, 64). Teste-la sur trois hash de longueurs différentes.

## ✅ Tu sais maintenant…

- Définir une fonction avec `def` et l'appeler
- Passer des arguments (avec noms clairs) et des valeurs par défaut
- Retourner un résultat avec `return` (y compris plusieurs valeurs), utilisable dans une condition
- Écrire des fonctions défensives réutilisables (`is_suspicious_extension`, `normalize_domain`, `is_private_ip`)
- La portée locale des variables
- Documenter avec une docstring

-----
