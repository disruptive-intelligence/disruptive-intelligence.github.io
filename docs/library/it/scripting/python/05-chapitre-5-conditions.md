---
title: Chapitre 5 — Conditions
source: IT/07 Scripting & programmation/Python.md
note: Python
up:
- - Python
  - index.md
---

## Le minimum à savoir

### La structure `if`

```python
score = 8

if score >= 7:
    print("[!] Alerte critique")
```


Deux choses cruciales :

1. **Les deux-points `:`** à la fin de la ligne `if`
2. **L'indentation** (les espaces en début de ligne) du bloc qui suit

### L'indentation : LE concept fondamental de Python

En Bash, les blocs sont délimités par des mots-clés (`then`/`fi`). **En Python, c'est l'indentation qui délimite les blocs.** Pas de `fi`, pas d'accolades : c'est l'alignement du texte qui dit « ce code fait partie de ce bloc ».

```python
if score >= 7:
    print("[!] Alerte critique")     # ← indenté = dans le if
    print("[!] Notification envoyée") # ← indenté = aussi dans le if
print("Fin de l'analyse")             # ← pas indenté = toujours exécuté
```


> **C'est le concept le plus important de Python pour un débutant.** Si tu comprends l'indentation, tu comprends Python.

**Les règles :**

- **4 espaces** par niveau d'indentation (standard Python)
- Tout le code d'un même bloc a **exactement** le même niveau
- Ne mélange **jamais** tabulations et espaces (configure ton éditeur pour convertir les tabs en 4 espaces)

```python
# ❌ Erreur — pas d'indentation
if score >= 7:
print("Alerte")        # IndentationError !
```


> **Conseil :** utilise un éditeur (VS Code) qui indente automatiquement après le `:`.

### `if...else`

```python
ip_externe = True

if ip_externe:
    print("[!] Connexion depuis Internet")
else:
    print("[+] Connexion interne")
```


> **Note :** `else` est au même niveau que `if`, avec ses propres deux-points `:`.

### `if...elif...else`

```python
code = 404

if code < 300:
    print("[+] Succès")
elif code < 400:
    print("[*] Redirection")
elif code < 500:
    print("[-] Erreur client")
else:
    print("[!] Erreur serveur")
```


`elif` = « else if ». Autant de `elif` que tu veux, mais un seul `else` (à la fin).

### Les tests les plus courants

```python
# Tester un nombre
if nb_echecs > 10:
    print("[!] Trop d'échecs")

# Tester l'égalité d'une chaîne
if statut == "malveillant":
    print("[!] À bloquer")

# Tester une chaîne vide
ligne = ""
if ligne == "":
    print("Ligne vide, ignorée")

# Plus pythonique :
if not ligne:
    print("Ligne vide, ignorée")

# Tester un mot-clé dans une ligne de log
if "Failed password" in ligne_log:
    print("[!] Tentative de connexion échouée")
```


### Combiner des conditions

```python
nb_echecs = 47
ip_externe = True

# ET
if nb_echecs > 10 and ip_externe:
    print("[!] Attaque par force brute probable")

# OU
if code == 502 or code == 503:
    print("[!] Service indisponible")

# NON
if not ip_externe:
    print("[+] Source interne")
```


## Très utile en pratique

### Les valeurs « falsy » et « truthy »

Certaines valeurs sont considérées comme « fausses » dans un test, sans comparaison explicite :

|Valeur            |Considérée comme|
|------------------|----------------|
|`False`           |Faux            |
|`0`               |Faux            |
|`""` (chaîne vide)|Faux            |
|`[]` (liste vide) |Faux            |
|`None`            |Faux            |
|Tout le reste     |Vrai            |

Ça rend les tests très lisibles :

```python
iocs_trouves = []

if iocs_trouves:        # équivalent de : if len(iocs_trouves) > 0
    print(f"[!] {len(iocs_trouves)} IOC trouvés")
else:
    print("[+] Aucun IOC, log propre")
```


### Conditions imbriquées

Un `if` dans un `if` — chaque niveau ajoute 4 espaces :

```python
if ip_externe:
    if nb_echecs > 50:
        print("[!] Force brute massive depuis l'extérieur")
    elif nb_echecs > 10:
        print("[*] Activité suspecte")
    else:
        print("[+] Activité normale")
else:
    print("[+] Trafic interne")
```


> **Conseil :** si tu dépasses 2-3 niveaux imbriqués, simplifie (souvent en combinant avec `and`/`or`).

### L'opérateur ternaire (condition en une ligne)

```python
score = 9
verdict = "CRITIQUE" if score >= 8 else "normal"
print(verdict)    # → CRITIQUE
```


Pratique pour une affectation courte ; pour une logique complexe, garde un `if`/`else` classique.

## Application cyber — trier une ligne de log

Voici un mini-trieur qui classe une ligne de log selon son contenu. C'est le cœur de tout détecteur : *observer un signal, décider d'une catégorie*.

```python
ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5"

if "Failed password" in ligne and "root" in ligne:
    niveau = "CRITIQUE"
    raison = "Échec de connexion sur le compte root"
elif "Failed password" in ligne:
    niveau = "ALERTE"
    raison = "Échec de connexion"
elif "Accepted password" in ligne:
    niveau = "INFO"
    raison = "Connexion réussie"
else:
    niveau = "IGNORÉ"
    raison = "Aucun signal connu"

print(f"[{niveau}] {raison}")
```


Résultat :

```
[CRITIQUE] Échec de connexion sur le compte root
```


On combine ici `in` (chercher un mot-clé), `and` (deux conditions), et `if/elif/else` (décider la catégorie). C'est *littéralement* ce que fait un règle de détection.

## Bonus

### Le `match/case` (Python 3.10+)

> **Attention :** nécessite **Python 3.10 minimum** (`python3 --version`). Sinon, ignore cette section : les `if/elif` font la même chose.

```python
commande = input("Action (analyser/bloquer/quitter) : ")

match commande:
    case "analyser":
        print("[+] Analyse en cours")
    case "bloquer":
        print("[!] IP ajoutée à la liste de blocage")
    case "quitter":
        print("Au revoir")
    case _:
        print(f"[-] Action '{commande}' inconnue")
```


Le `_` est le cas par défaut. Les `if/elif` restent la méthode universelle.

## ❌ Erreur classique

```python
# Oublier les deux-points
if score >= 8         # ❌ SyntaxError — il manque le ":"
    print("Alerte")

# Indentation manquante
if score >= 8:
print("Alerte")       # ❌ IndentationError

# Utiliser = au lieu de ==
if statut = "malveillant":   # ❌ SyntaxError — affectation au lieu de test
if statut == "malveillant":  # ✅ Correct

# Oublier que "in" est sensible à la casse
ligne = "FAILED PASSWORD"
if "Failed password" in ligne:   # ❌ Ne matche pas (casse différente)
    print("Détecté")
if "failed password" in ligne.lower():  # ✅ On normalise d'abord (chapitre 6)
    print("Détecté")
```


## Exercices

**Guidé :** Crée un script `triage.py` qui prend un code HTTP en argument et affiche un verdict : `"[+] OK"` (200-299), `"[*] Redirection"` (300-399), `"[-] Erreur client"` (400-499), `"[!] Erreur serveur"` (500+).

**Autonome :** Crée un script `verif_ligne.py` qui prend une ligne de log en argument (entre guillemets) et affiche `"[!] SUSPECT"` si elle contient `"Failed password"` **ou** `"Invalid user"`, sinon `"[+] RAS"`.

## 🧩 Mini-projet (chapitres 3-5)

Crée un script `port_scanner_verdict.py` (sans rien scanner — on raisonne juste sur une valeur) qui :

1. Prend un numéro de port en argument et le convertit en entier.
2. Affiche `"port système"` (< 1024), `"port enregistré"` (1024-49151) ou `"port dynamique"` (> 49151).
3. Affiche en plus `"[!] Service sensible"` si le port est 22, 23, 3389 ou 445 (utilise `in` avec une liste, qu'on verra au chapitre 7 — ici tu peux enchaîner des `or`).

## ✅ Tu sais maintenant…

- Écrire des conditions avec `if`, `elif`, `else`
- L'indentation comme structure de bloc (4 espaces par niveau)
- Les deux-points `:` après chaque `if`, `elif`, `else`
- Combiner des conditions avec `and`, `or`, `not`
- Les valeurs « falsy » (chaîne vide, 0, liste vide, None)
- Classer une ligne de log selon son contenu (base d'une règle de détection)

-----
